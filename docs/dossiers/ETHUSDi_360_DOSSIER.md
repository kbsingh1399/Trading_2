# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:47:31 IST` (`2026-10-30 06:17:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2238.90` | **Live Ask Quote**: `2242.20` | **Mid Price**: `2240.55`
- **Spread Points**: `330.00` | **Spread BPS**: `14.73 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2215.91` | VWAP Z-Score: `+0.98` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `14.62` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.97` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2267.40` | Lower -3.00σ Band: `2164.41`
  * Upper +2.51σ Band: `2258.99` | Lower -2.51σ Band: `2172.82`
  * Upper +2.01σ Band: `2250.41` | Lower -2.01σ Band: `2181.41`
  * Upper +2.00σ Band: `2250.23` | Lower -2.00σ Band: `2181.58`
  * Upper +1.28σ Band: `2237.88` | Lower -1.28σ Band: `2193.94`
  * Upper +1.00σ Band: `2233.07` | Lower -1.00σ Band: `2198.74`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2234.59` | EMA-20=`2232.33` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2252.85` (Slope: `+0.0000`) | EMA-100=`2278.61`
  * Institutional Anchors: EMA-144=`2290.95` | EMA-200=`2300.88` (Slope: `-0.3813`) | EMA-233=`2306.05`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2275.75` (Distance: `-1.50%`)
  * Point of Control (POC) = `2240.94` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `2209.38` (Distance: `+1.45%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2351.85` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2246.50` | Low=`2228.90`
  * New York Session (13:00-21:00 UTC): High=`2253.99` | Low=`2227.11`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2231.59` - `2249.51`
  * Optimal Trade Entry (OTE 0.705): `2245.03`
  * Structural Invalidation Anchor (0.786): `2258.47`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2238.29` | `2241.00` | `2235.52` | `2238.29` | `24,577` | 55,012,920.10 USD | 8,079,452.36 USD | `+14.69%` | -989,579,703.23 USD | `+1.95` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2238.29` | `2243.71` | `2238.01` | `2243.62` | `12,939` | 28,996,619.26 USD | 11,680,183.40 USD | `+40.28%` | -977,899,519.83 USD | `+2.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2243.62` | `2245.55` | `2242.57` | `2244.99` | `5,382` | 12,077,957.70 USD | 2,513,694.29 USD | `+20.81%` | -975,385,825.55 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2247.98` | `2251.99` | `2245.66` | `2249.06` | `29,442` | 66,196,194.89 USD | 1,091,278.95 USD | `+1.65%` | -997,016,665.47 USD | `+0.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `2249.05` | `2250.00` | `2237.35` | `2238.29` | `53,305` | 119,524,398.16 USD | -642,490.12 USD | `-0.54%` | -997,659,155.59 USD | `+0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2238.29` | `2245.55` | `2235.52` | `2244.87` | `42,882` | 96,053,449.89 USD | 22,249,012.58 USD | `+23.16%` | -975,410,143.01 USD | `+1.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `2236.81` | `2246.94` | `2225.47` | `2242.81` | `206,764` | 463,074,415.24 USD | -1,345,167.52 USD | `-0.29%` | -986,494,525.14 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2242.81` | `2252.87` | `2237.35` | `2238.29` | `157,304` | 353,288,585.81 USD | 4,209,421.63 USD | `+1.19%` | -982,285,103.51 USD | `+0.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `2238.29` | `2245.55` | `2235.52` | `2244.87` | `42,882` | 96,053,449.89 USD | 22,249,012.58 USD | `+23.16%` | -960,036,090.92 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2252.87` | `2225.47` | `2244.87` | `406,951` | 912,416,450.94 USD | 25,113,266.69 USD | `+2.75%` | -938,037,909.27 USD | `+0.83` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 54,877,924.52 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -147,278,192.42 USD | `-1.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2252.87` | `2225.47` | `2244.87` | `406,951` | 912,416,450.94 USD | 25,113,266.69 USD | `+2.75%` | -938,037,909.27 USD | `+0.83` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`2240.55`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2242.60` | `190.9260` | 428,170.65 USD | 7,051,576.68 USD | `7 orders` | `-0.09%` | `-` |
| `BID` | `2242.70` | `261.9111` | 587,388.02 USD | 6,623,406.03 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2242.80` | `45.8818` | 102,903.70 USD | 6,036,018.01 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2242.90` | `124.9020` | 280,142.70 USD | 5,933,114.31 USD | `4 orders` | `-0.07%` | `-` |
| `BID` | `2243.00` | `93.3029` | 209,278.40 USD | 5,652,971.61 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2243.10` | `133.2961` | 298,996.48 USD | 5,443,693.21 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2243.20` | `228.5799` | 512,750.43 USD | 5,144,696.72 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2243.30` | `302.9840` | 679,684.01 USD | 4,631,946.29 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2243.40` | `310.4385` | 696,437.73 USD | 3,952,262.28 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2243.50` | `136.9903` | 307,337.74 USD | 3,255,824.55 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2243.60` | `43.0019` | 96,479.06 USD | 2,948,486.82 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `2243.70` | `379.3288` | 851,100.03 USD | 2,852,007.75 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `2243.80` | `230.6049` | 517,431.27 USD | 2,000,907.72 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `2243.90` | `61.5455` | 138,101.95 USD | 1,483,476.45 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2244.00` | `146.9493` | 329,754.23 USD | 1,345,374.50 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `2244.10` | `198.7349` | 445,980.99 USD | 1,015,620.27 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2244.20` | `59.7879` | 134,176.01 USD | 569,639.28 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2244.30` | `18.0117` | 40,423.66 USD | 435,463.28 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2244.40` | `15.8208` | 35,508.20 USD | 395,039.62 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2244.50` | `160.1833` | 359,531.42 USD | 359,531.42 USD | `21 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2244.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,244.55` | `0.00%` | `-` |
| `ASK` | `2244.60` | `95.9030` | 215,263.87 USD | 215,263.87 USD | `14 orders` | `+0.00%` | `-` |
| `ASK` | `2244.70` | `57.8340` | 129,819.98 USD | 345,083.85 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2244.80` | `37.2448` | 83,607.13 USD | 428,690.98 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2244.90` | `76.9743` | 172,799.61 USD | 601,490.59 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `2245.00` | `88.9065` | 199,595.09 USD | 801,085.68 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2245.10` | `175.0543` | 393,014.41 USD | 1,194,100.09 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2245.20` | `32.1251` | 72,127.27 USD | 1,266,227.36 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2245.30` | `171.6928` | 385,501.84 USD | 1,651,729.21 USD | `10 orders` | `+0.03%` | `-` |
| `ASK` | `2245.40` | `62.4238` | 140,166.40 USD | 1,791,895.61 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `2245.50` | `546.5336` | 1,227,241.20 USD | 3,019,136.81 USD | `31 orders` | `+0.04%` | `-` |
| `ASK` | `2245.60` | `58.8473` | 132,147.50 USD | 3,151,284.30 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `2245.70` | `49.7213` | 111,659.12 USD | 3,262,943.43 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `2245.80` | `376.5472` | 845,649.70 USD | 4,108,593.13 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `2245.90` | `232.9923` | 523,277.41 USD | 4,631,870.53 USD | `12 orders` | `+0.06%` | `-` |
| `ASK` | `2246.00` | `379.9748` | 853,423.40 USD | 5,485,293.94 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2246.10` | `285.6002` | 641,486.61 USD | 6,126,780.54 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `2246.20` | `96.6404` | 217,073.67 USD | 6,343,854.21 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `2246.30` | `139.3159` | 312,945.31 USD | 6,656,799.52 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `2246.40` | `148.0623` | 332,607.15 USD | 6,989,406.67 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `2246.50` | `8.5374` | 19,179.27 USD | 7,008,585.94 USD | `8 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1796.46` | `9,823.81` | 17,648,096.61 USD | `AT_RISK_LIQ` | `0x939f95036d` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.11` | `7,964.66` | 14,687,675.90 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1926.56` | `8,092.45` | 15,590,585.94 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.05` | `30,641.99` | 65,023,988.50 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.33` | `26,025.05` | 55,415,994.51 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,133.33` | 6,814,999.93 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.00` | `1,524.00` | 3,352,800.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x4b8600a785` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2202.30` | `2,056.54` | 4,529,118.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2205.60` | `505.78` | 1,115,543.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.00` | `4,705.83` | 10,395,186.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.40` | `1,412.11` | 3,125,569.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.80` | `401.99` | 891,943.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc86781f990` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.80` | `358.18` | 794,719.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `458.19` | 1,017,637.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `500.00` | 1,110,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.30` | `505.56` | 1,123,517.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.80` | `1,010.81` | 2,247,841.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2225.00` | `2,425.00` | 5,395,614.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.60` | `505.68` | 1,126,455.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.80` | `346.19` | 771,584.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2229.10` | `1,797.65` | 4,007,145.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2229.70` | `655.98` | 1,462,637.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.10` | `500.00` | 1,115,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.80` | `1,346.61` | 3,005,374.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.30` | `472.65` | 1,055,101.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.50` | `1,237.26` | 2,762,185.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.10` | `896.82` | 2,003,580.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.20` | `491.65` | 1,098,444.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.10` | `671.99` | 1,502,639.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2237.30` | `348.64` | 780,022.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.30` | `447.55` | 1,001,748.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.20` | `339.74` | 762,442.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.60` | `446.32` | 1,001,803.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.10` | `669.01` | 1,502,659.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.00` | `1,238.38` | 2,783,871.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.30` | `891.14` | 2,003,558.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.40` | `472.77` | 1,062,976.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.30` | `683.74` | 1,537,930.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.70` | `1,335.88` | 3,005,340.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.40` | `338.80` | 762,442.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.30` | `679.58` | 1,530,616.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.30` | `505.63` | 1,138,837.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.00` | `1,778.60` | 4,007,195.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2255.50` | `2,427.22` | 5,474,592.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.00` | `506.24` | 1,142,576.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.40` | `971.01` | 2,191,948.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.60` | `351.09` | 794,719.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.60` | `336.60` | 761,925.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2266.00` | `1,413.77` | 3,203,602.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.00` | `505.39` | 1,149,764.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.70` | `4,696.65` | 10,688,176.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 11:43:56 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2277.30` | `2,065.35` | 4,703,425.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2448.72` | `22,046.99` | 53,986,945.47 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 11:43:56 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `2,823.41` | 7,097,769.90 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.08` | `10,000.00` | 26,240,750.24 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 11:43:56 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.93` | `9,700.00` | 25,781,903.05 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 239,003,537.58 USD | `106,417.71` | `2322.74` | `2244.40` | `3772.97` | 8,177,474.57 USD | `+3.42%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 145,253,268.78 USD | `64,680.62` | `2375.30` | `2244.40` | `4304.32` | 8,383,028.71 USD | `+5.77%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,782,078.77 USD | `30,641.99` | `2610.31` | `2244.40` | `2122.00` | -11,203,096.27 USD | `-16.29%` | `10X Cross` |
| `12` | `0xde8d...9524` | `LONG` | 68,026,391.22 USD | `30,282.40` | `2134.45` | `2244.40` | `1786.26` | 3,390,060.65 USD | `+4.98%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 58,462,674.79 USD | `26,025.05` | `2518.71` | `2244.40` | `2129.28` | -7,087,047.30 USD | `-12.12%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,482,261.66 USD | `22,046.99` | `2271.09` | `2244.40` | `2450.49` | 588,635.64 USD | `+1.19%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,859,478.58 USD | `19,971.28` | `2402.53` | `2244.40` | `4172.70` | 3,122,200.66 USD | `+6.96%` | `25X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 37,491,977.67 USD | `16,687.58` | `2522.09` | `2244.40` | `3479.16` | 4,595,737.32 USD | `+12.26%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 35,779,737.50 USD | `15,927.59` | `2410.19` | `2244.40` | `1743.96` | -2,608,882.15 USD | `-7.29%` | `6X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 35,000,030.87 USD | `15,592.30` | `2557.74` | `2244.40` | `3966.07` | 4,881,098.37 USD | `+13.95%` | `20X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,313,565.00 USD | `13,950.00` | `2443.60` | `2244.40` | `5240.35` | 2,774,717.46 USD | `+8.86%` | `20X Cross` |
| `43` | `0xa61c...66b9` | `LONG` | 28,938,715.20 USD | `12,888.00` | `2369.69` | `2244.40` | `1439.51` | -1,601,939.34 USD | `-5.54%` | `10X Cross` |
| `46` | `0xbd1c...ff0e` | `LONG` | 26,952,000.00 USD | `12,000.00` | `2419.91` | `2244.40` | `1520.14` | -2,087,032.39 USD | `-7.74%` | `20X Cross` |
| `47` | `0x2371...0883` | `LONG` | 26,948,400.00 USD | `12,000.00` | `2421.77` | `2244.40` | `1279.24` | -2,112,894.85 USD | `-7.84%` | `20X Cross` |
| `53` | `0x0c5d...36b3` | `LONG` | 24,710,400.00 USD | `11,000.00` | `2482.20` | `2244.40` | `1644.21` | -2,593,853.24 USD | `-10.50%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,704,900.00 USD | `11,000.00` | `2481.81` | `2244.40` | `1643.88` | -2,595,079.46 USD | `-10.50%` | `20X Cross` |
| `56` | `0x6c93...59a4` | `LONG` | 24,697,200.00 USD | `11,000.00` | `2441.15` | `2244.40` | `1602.17` | -2,155,472.73 USD | `-8.73%` | `20X Cross` |
| `57` | `0x09dc...c094` | `LONG` | 24,691,700.00 USD | `11,000.00` | `2465.31` | `2244.40` | `1637.21` | -2,426,723.04 USD | `-9.83%` | `20X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,497,901.70 USD | `10,016.88` | `2162.83` | `2244.40` | `1525.13` | 833,099.65 USD | `+3.70%` | `10X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,467,000.00 USD | `10,000.00` | `2719.35` | `2244.40` | `1720.73` | -4,726,548.52 USD | `-21.04%` | `20X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,460,000.00 USD | `10,000.00` | `1765.80` | `2244.40` | `1724.07` | 4,801,942.55 USD | `+21.38%` | `25X Cross` |
| `74` | `0x15a4...dfdb` | `LONG` | 22,459,000.00 USD | `10,000.00` | `1761.94` | `2244.40` | `241.34` | 4,839,518.97 USD | `+21.55%` | `20X Cross` |
| `75` | `0xb37f...66ca` | `SHORT` | 22,447,000.00 USD | `10,000.00` | `2290.69` | `2244.40` | `2624.03` | 459,991.85 USD | `+2.05%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,068,213.30 USD | `9,823.81` | `2427.28` | `2244.40` | `1802.24` | -1,776,937.30 USD | `-8.05%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,783,290.00 USD | `9,700.00` | `2311.92` | `2244.40` | `2657.88` | 642,392.40 USD | `+2.95%` | `25X Cross` |
| `82` | `0xecb6...2b00` | `SHORT` | 21,327,077.35 USD | `9,499.39` | `2243.20` | `2244.40` | `5273.07` | -17,954.24 USD | `-0.08%` | `15X Cross` |
| `85` | `0xf517...c032` | `SHORT` | 20,941,379.78 USD | `9,326.35` | `2202.91` | `2244.40` | `3180.33` | -396,241.57 USD | `-1.89%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,624,621.09 USD | `9,184.87` | `2549.39` | `2244.40` | `3852.91` | 2,791,256.30 USD | `+13.53%` | `25X Cross` |
| `89` | `0xba5d...a352` | `SHORT` | 20,341,896.12 USD | `9,054.12` | `2493.89` | `2244.40` | `2903.21` | 2,238,111.14 USD | `+11.00%` | `20X Cross` |
| `90` | `0xea00...a918` | `LONG` | 20,226,195.40 USD | `9,003.83` | `2003.01` | `2244.40` | `1352.35` | 2,191,416.54 USD | `+10.83%` | `5X Cross` |
| `94` | `0xefe4...194b` | `SHORT` | 19,817,182.93 USD | `8,820.57` | `2267.42` | `2244.40` | `3529.61` | 182,831.46 USD | `+0.92%` | `20X Cross` |
| `115` | `0x9eec...daab` | `LONG` | 18,165,127.23 USD | `8,092.45` | `1658.44` | `2244.40` | `1926.77` | 4,744,262.70 USD | `+26.12%` | `15X Cross` |
| `116` | `0x5f91...65aa` | `LONG` | 17,891,803.01 USD | `7,964.66` | `1626.99` | `2244.40` | `1844.06` | 4,933,359.95 USD | `+27.57%` | `16X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,733,910.09 USD | `7,007.80` | `2065.97` | `2244.40` | `1059.37` | 1,255,980.50 USD | `+7.98%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,393,058.64 USD | `6,855.99` | `2383.33` | `2244.40` | `1115.81` | -947,030.12 USD | `-6.15%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,280,948.26 USD | `6,803.63` | `1862.69` | `2244.40` | `4203.70` | -2,607,842.87 USD | `-17.07%` | `7X Cross` |
| `138` | `0x4ff9...38d3` | `LONG` | 14,747,560.55 USD | `6,564.10` | `2447.40` | `2244.40` | `1669.83` | -1,317,462.20 USD | `-8.93%` | `3X Isolated` |
| `140` | `0xf78c...c581` | `LONG` | 14,602,097.58 USD | `6,500.22` | `2521.53` | `2244.40` | `1913.31` | -1,788,443.37 USD | `-12.25%` | `20X Cross` |
| `141` | `0x1ee7...edf5` | `LONG` | 14,601,600.00 USD | `6,500.00` | `2301.55` | `2244.40` | `2069.05` | -358,493.66 USD | `-2.46%` | `25X Cross` |
| `143` | `0x799f...5f4c` | `LONG` | 14,169,240.09 USD | `6,310.90` | `2390.33` | `2244.40` | `1821.60` | -915,924.53 USD | `-6.46%` | `20X Cross` |
| `149` | `0x08bf...7872` | `SHORT` | 13,972,986.41 USD | `6,224.05` | `2258.00` | `2244.40` | `2585.10` | 80,929.69 USD | `+0.58%` | `20X Cross` |
| `152` | `0xc179...e0c8` | `LONG` | 13,822,107.67 USD | `6,156.57` | `2294.94` | `2244.40` | `1198.30` | -306,860.87 USD | `-2.22%` | `10X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,475,400.00 USD | `6,000.00` | `2480.18` | `2244.40` | `1407.60` | -1,405,724.33 USD | `-10.43%` | `20X Cross` |
| `164` | `0x0c4a...1b19` | `LONG` | 12,702,390.81 USD | `5,660.10` | `2373.06` | `2244.40` | `2081.65` | -729,367.32 USD | `-5.74%` | `25X Isolated` |
| `167` | `0x418a...8888` | `SHORT` | 12,356,850.00 USD | `5,500.00` | `2494.55` | `2244.40` | `2828.74` | 1,363,186.50 USD | `+11.03%` | `25X Cross` |
| `170` | `0x7fda...17d1` | `LONG` | 11,932,283.33 USD | `5,315.76` | `2211.05` | `2244.40` | `0.000000` | 178,841.09 USD | `+1.50%` | `25X Cross` |
| `177` | `0x218a...7da2` | `SHORT` | 11,732,651.12 USD | `5,222.87` | `2208.16` | `2244.40` | `2792.76` | -199,716.06 USD | `-1.70%` | `10X Cross` |
| `186` | `0x524e...0de0` | `LONG` | 11,225,500.00 USD | `5,000.00` | `2246.29` | `2244.40` | `1944.80` | -5,955.08 USD | `-0.05%` | `10X Cross` |
| `190` | `0x45ab...6cbc` | `LONG` | 11,054,449.49 USD | `4,920.96` | `2727.66` | `2244.40` | `1375.97` | -2,368,294.31 USD | `-21.42%` | `7X Cross` |
| `196` | `0x64b7...9da9` | `LONG` | 10,905,546.74 USD | `4,856.84` | `2604.61` | `2244.40` | `592.79` | -1,744,667.67 USD | `-16.00%` | `25X Cross` |
| `202` | `0xfb18...eb17` | `SHORT` | 10,706,955.15 USD | `4,768.18` | `2315.53` | `2244.40` | `2595.31` | 333,926.65 USD | `+3.12%` | `25X Cross` |
| `203` | `0x5559...d43b` | `SHORT` | 10,681,332.63 USD | `4,755.93` | `2262.69` | `2244.40` | `2784.94` | 79,873.25 USD | `+0.75%` | `25X Cross` |
| `213` | `0xe091...6705` | `SHORT` | 10,108,800.45 USD | `4,500.00` | `2467.33` | `2244.40` | `2463.22` | 994,208.06 USD | `+9.84%` | `20X Cross` |
| `222` | `0xb829...3a81` | `LONG` | 9,865,256.72 USD | `4,394.91` | `2398.60` | `2244.40` | `1484.40` | -676,385.23 USD | `-6.86%` | `20X Cross` |
| `239` | `0x28bb...fca6` | `SHORT` | 9,452,267.72 USD | `4,209.61` | `1896.10` | `2244.40` | `3035.98` | -1,470,385.16 USD | `-15.56%` | `20X Cross` |
| `241` | `0x6ea4...0ea7` | `SHORT` | 9,400,220.43 USD | `4,184.01` | `2602.13` | `2244.40` | `3425.17` | 1,487,126.23 USD | `+15.82%` | `20X Cross` |
| `254` | `0x5e9e...35ee` | `SHORT` | 9,000,970.10 USD | `4,007.56` | `1796.39` | `2244.40` | `2585.66` | -1,801,820.01 USD | `-20.02%` | `20X Cross` |
| `256` | `0x3dc9...54b0` | `SHORT` | 8,984,904.07 USD | `3,999.69` | `2480.32` | `2244.40` | `6400.78` | 935,632.49 USD | `+10.41%` | `20X Cross` |
| `257` | `0xfb94...0ddf` | `SHORT` | 8,981,115.53 USD | `4,002.10` | `2382.44` | `2244.40` | `5104.56` | 553,668.62 USD | `+6.16%` | `20X Cross` |
| `258` | `0x8cc9...2b6a` | `SHORT` | 8,980,400.00 USD | `4,000.00` | `1791.18` | `2244.40` | `3530.62` | -1,815,653.33 USD | `-20.22%` | `25X Cross` |
| `274` | `0x4b67...f4e7` | `LONG` | 8,583,139.24 USD | `3,820.84` | `2591.51` | `2244.40` | `1336.33` | -1,318,634.30 USD | `-15.36%` | `20X Cross` |
| `278` | `0x12d2...f97f` | `LONG` | 8,436,554.30 USD | `3,757.26` | `2446.50` | `2244.40` | `1762.21` | -755,612.09 USD | `-8.96%` | `20X Cross` |
| `297` | `0x8ae4...3d60` | `LONG` | 7,985,308.62 USD | `3,558.20` | `2482.21` | `2244.40` | `474.80` | -846,889.41 USD | `-10.61%` | `10X Cross` |
| `317` | `0x469e...58a5` | `SHORT` | 7,337,586.52 USD | `3,266.67` | `2199.65` | `2244.40` | `3167.07` | -152,049.94 USD | `-2.07%` | `25X Cross` |
| `336` | `0xb823...9763` | `SHORT` | 6,740,100.00 USD | `3,000.00` | `2229.66` | `2244.40` | `3233.56` | -51,103.32 USD | `-0.76%` | `25X Cross` |
| `337` | `0x007d...67a0` | `LONG` | 6,736,500.00 USD | `3,000.00` | `2400.00` | `2244.40` | `1472.70` | -463,500.00 USD | `-6.88%` | `25X Cross` |
| `338` | `0x4a20...3c26` | `LONG` | 6,734,100.00 USD | `3,000.00` | `2428.72` | `2244.40` | `509.18` | -552,060.28 USD | `-8.20%` | `20X Cross` |
| `367` | `0x9c2a...f6a8` | `SHORT` | 6,342,507.77 USD | `2,823.41` | `2533.78` | `2244.40` | `2628.63` | 811,403.04 USD | `+12.79%` | `20X Cross` |
| `390` | `0x8328...f54a` | `SHORT` | 5,787,739.75 USD | `2,576.45` | `2292.01` | `2244.40` | `3279.40` | 117,531.54 USD | `+2.03%` | `25X Cross` |
| `393` | `0xed48...7c9b` | `SHORT` | 5,727,287.97 USD | `2,551.13` | `2460.02` | `2244.40` | `3248.45` | 548,558.44 USD | `+9.58%` | `20X Cross` |
| `399` | `0x1c98...7fc7` | `LONG` | 5,616,760.11 USD | `2,500.00` | `2452.60` | `2244.40` | `1916.80` | -514,761.45 USD | `-9.16%` | `10X Cross` |
| `400` | `0x970c...2a93` | `SHORT` | 5,615,500.00 USD | `2,500.00` | `2229.57` | `2244.40` | `5045.94` | -41,555.51 USD | `-0.74%` | `20X Cross` |
| `413` | `0xa445...329d` | `LONG` | 5,401,053.03 USD | `2,406.14` | `2354.86` | `2244.40` | `1695.36` | -265,062.25 USD | `-4.91%` | `25X Cross` |
| `415` | `0x6749...ce07` | `SHORT` | 5,354,087.48 USD | `2,384.89` | `2220.92` | `2244.40` | `3631.57` | -57,424.45 USD | `-1.07%` | `20X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,354,071.91 USD | `2,385.21` | `2041.57` | `2244.40` | `2621.43` | -484,505.25 USD | `-9.05%` | `20X Cross` |
| `417` | `0x645b...87b8` | `SHORT` | 5,345,901.19 USD | `2,379.98` | `2421.64` | `2244.40` | `11220.88` | 417,545.76 USD | `+7.81%` | `10X Cross` |
| `428` | `0x77ee...2902` | `SHORT` | 5,146,495.92 USD | `2,290.69` | `2476.53` | `2244.40` | `5929.48` | 526,476.32 USD | `+10.23%` | `25X Cross` |
| `434` | `0xbcd4...0dd2` | `SHORT` | 5,078,387.93 USD | `2,263.50` | `2233.24` | `2244.40` | `2647.91` | -23,430.36 USD | `-0.46%` | `25X Cross` |
| `452` | `0xd507...c948` | `SHORT` | 4,876,574.18 USD | `2,172.00` | `2387.49` | `2244.40` | `2600.40` | 309,066.85 USD | `+6.34%` | `5X Isolated` |
| `460` | `0x382b...3e39` | `SHORT` | 4,783,376.34 USD | `2,129.54` | `2296.66` | `2244.40` | `4638.99` | 107,460.87 USD | `+2.25%` | `25X Cross` |
| `462` | `0x023a...2355` | `LONG` | 4,768,829.74 USD | `2,123.54` | `2330.15` | `2244.40` | `0.000000` | -179,344.08 USD | `-3.76%` | `25X Cross` |
| `497` | `0x3453...b323` | `SHORT` | 4,493,076.53 USD | `2,000.12` | `2322.47` | `2244.40` | `2372.91` | 152,159.31 USD | `+3.39%` | `25X Cross` |
| `498` | `0xe02e...d78b` | `LONG` | 4,490,000.00 USD | `2,000.00` | `2228.11` | `2244.40` | `2171.75` | 33,776.53 USD | `+0.75%` | `25X Cross` |
| `499` | `0x7a6d...f79c` | `SHORT` | 4,487,600.00 USD | `2,000.00` | `2418.41` | `2244.40` | `2543.83` | 349,232.11 USD | `+7.78%` | `25X Cross` |
| `507` | `0xf3dc...1672` | `SHORT` | 4,448,683.62 USD | `1,980.36` | `2240.44` | `2244.40` | `2764.82` | -11,796.07 USD | `-0.27%` | `20X Cross` |
| `511` | `0xac48...3201` | `SHORT` | 4,412,759.64 USD | `1,964.37` | `2272.04` | `2244.40` | `3106.02` | 50,382.65 USD | `+1.14%` | `20X Cross` |
| `519` | `0x8376...9a1e` | `SHORT` | 4,291,738.21 USD | `1,910.50` | `2477.72` | `2244.40` | `3177.50` | 441,949.96 USD | `+10.30%` | `20X Cross` |
| `522` | `0x739c...cfb2` | `SHORT` | 4,268,160.00 USD | `1,900.00` | `2418.12` | `2244.40` | `2509.52` | 326,286.38 USD | `+7.64%` | `25X Cross` |
| `554` | `0x7265...91a5` | `LONG` | 4,046,818.49 USD | `1,801.87` | `2533.96` | `2244.40` | `1987.28` | -519,047.97 USD | `-12.83%` | `20X Cross` |
| `555` | `0xbb34...1696` | `LONG` | 4,043,520.00 USD | `1,800.00` | `2313.95` | `2244.40` | `1936.35` | -121,598.23 USD | `-3.01%` | `25X Cross` |
| `556` | `0xc619...10f5` | `LONG` | 4,039,470.00 USD | `1,800.00` | `2313.55` | `2244.40` | `1770.16` | -124,925.83 USD | `-3.09%` | `25X Cross` |
| `566` | `0x91a9...3f70` | `SHORT` | 3,969,760.08 USD | `1,767.48` | `2156.23` | `2244.40` | `3647.58` | -158,656.00 USD | `-4.00%` | `4X Cross` |
| `600` | `0xfeec...4e9c` | `SHORT` | 3,798,449.12 USD | `1,691.81` | `2566.49` | `2244.40` | `2508.90` | 543,575.40 USD | `+14.31%` | `10X Cross` |
| `614` | `0xeee0...0b53` | `LONG` | 3,677,635.13 USD | `1,637.12` | `2468.64` | `2244.40` | `172.62` | -363,840.93 USD | `-9.89%` | `7X Cross` |
| `618` | `0x982b...4606` | `LONG` | 3,654,482.38 USD | `1,626.82` | `2575.24` | `2244.40` | `1547.56` | -534,970.69 USD | `-14.64%` | `5X Isolated` |
| `619` | `0x27b8...12fc` | `LONG` | 3,654,478.38 USD | `1,628.12` | `2468.73` | `2244.40` | `575.40` | -364,916.26 USD | `-9.99%` | `10X Cross` |
| `628` | `0x73d7...8be1` | `LONG` | 3,596,891.51 USD | `1,601.47` | `2410.40` | `2244.40` | `1756.14` | -263,287.41 USD | `-7.32%` | `25X Cross` |
| `631` | `0xad54...6203` | `LONG` | 3,583,882.89 USD | `1,597.45` | `2591.98` | `2244.40` | `2051.91` | -556,695.16 USD | `-15.53%` | `10X Isolated` |
| `636` | `0x880a...311c` | `LONG` | 3,546,190.61 USD | `1,578.40` | `2209.72` | `2244.40` | `0.000000` | 58,366.75 USD | `+1.65%` | `9X Cross` |
| `654` | `0xe170...9300` | `SHORT` | 3,443,863.06 USD | `1,533.40` | `2076.39` | `2244.40` | `3143.38` | -259,913.56 USD | `-7.55%` | `25X Cross` |
| `659` | `0x4b86...df9d` | `SHORT` | 3,419,094.00 USD | `1,524.00` | `2287.40` | `2244.40` | `2759.76` | 66,903.60 USD | `+1.96%` | `9X Isolated` |
| `665` | `0x2e2b...2fab` | `LONG` | 3,385,568.74 USD | `1,507.38` | `2245.53` | `2244.40` | `1186.46` | 695.64 USD | `+0.02%` | `25X Cross` |
| `668` | `0xf929...d1f9` | `SHORT` | 3,368,850.00 USD | `1,500.00` | `2423.37` | `2244.40` | `2677.79` | 266,205.26 USD | `+7.90%` | `25X Cross` |
| `669` | `0x251f...6e5d` | `LONG` | 3,368,100.00 USD | `1,500.00` | `2346.68` | `2244.40` | `1819.34` | -151,930.49 USD | `-4.51%` | `20X Cross` |
| `670` | `0xde6b...3361` | `LONG` | 3,366,300.00 USD | `1,500.00` | `2216.98` | `2244.40` | `2168.68` | 40,819.26 USD | `+1.21%` | `25X Cross` |
| `691` | `0xb885...3c54` | `LONG` | 3,256,704.94 USD | `1,450.00` | `2274.34` | `2244.40` | `17.11` | -41,103.20 USD | `-1.26%` | `20X Cross` |
| `692` | `0x3440...32c5` | `SHORT` | 3,253,237.77 USD | `1,448.97` | `2198.21` | `2244.40` | `3769.81` | -68,086.81 USD | `-2.09%` | `25X Cross` |
| `697` | `0xef70...a84c` | `SHORT` | 3,239,536.03 USD | `1,442.74` | `2424.73` | `2244.40` | `3303.81` | 258,734.79 USD | `+7.99%` | `25X Cross` |
| `703` | `0x4b5f...0dd8` | `LONG` | 3,216,174.97 USD | `1,431.96` | `2339.45` | `2244.40` | `2147.84` | -133,817.97 USD | `-4.16%` | `10X Cross` |
| `706` | `0xbadb...9ee6` | `LONG` | 3,207,504.54 USD | `1,428.16` | `1936.00` | `2244.40` | `1053.94` | 442,582.90 USD | `+13.80%` | `20X Cross` |
| `761` | `0x53f8...ceff` | `LONG` | 3,029,617.02 USD | `1,348.65` | `2276.73` | `2244.40` | `0.000000` | -40,907.45 USD | `-1.35%` | `20X Cross` |
| `778` | `0x0dd5...f6ee` | `LONG` | 2,953,358.50 USD | `1,315.00` | `2306.05` | `2244.40` | `1560.18` | -79,105.88 USD | `-2.68%` | `5X Cross` |
| `802` | `0x0622...8088` | `LONG` | 2,843,131.90 USD | `1,265.47` | `2217.42` | `2244.40` | `0.000000` | 37,049.77 USD | `+1.30%` | `5X Cross` |
| `803` | `0x1f16...6d07` | `LONG` | 2,842,170.00 USD | `1,266.00` | `2261.43` | `2244.40` | `1388.79` | -20,801.23 USD | `-0.73%` | `7X Cross` |
| `812` | `0xc435...c905` | `SHORT` | 2,803,507.20 USD | `1,248.00` | `2704.38` | `2244.40` | `4205.83` | 571,563.15 USD | `+20.39%` | `20X Cross` |
| `820` | `0x6859...7e1e` | `SHORT` | 2,777,657.71 USD | `1,237.15` | `2200.39` | `2244.40` | `4646.23` | -55,430.55 USD | `-2.00%` | `25X Cross` |
| `830` | `0x7277...0b98` | `SHORT` | 2,737,674.01 USD | `1,219.45` | `2206.05` | `2244.40` | `3344.90` | -47,486.20 USD | `-1.73%` | `20X Cross` |
| `831` | `0x7178...0854` | `LONG` | 2,737,290.08 USD | `1,218.63` | `2461.81` | `2244.40` | `1146.15` | -262,756.33 USD | `-9.60%` | `10X Cross` |
| `843` | `0xaaa1...ab8c` | `SHORT` | 2,695,680.00 USD | `1,200.00` | `2276.29` | `2244.40` | `2365.38` | 35,877.58 USD | `+1.33%` | `25X Isolated` |
| `856` | `0x07fd...689d` | `LONG` | 2,642,145.12 USD | `1,176.69` | `2416.34` | `2244.40` | `0.000000` | -201,154.82 USD | `-7.61%` | `25X Cross` |
| `861` | `0x4487...c92d` | `LONG` | 2,633,344.36 USD | `1,173.24` | `2231.32` | `2244.40` | `1571.73` | 15,454.87 USD | `+0.59%` | `10X Cross` |
| `916` | `0x2f80...f203` | `SHORT` | 2,442,059.31 USD | `1,088.94` | `1984.00` | `2244.40` | `2964.86` | -281,592.12 USD | `-11.53%` | `20X Cross` |
| `922` | `0x6f11...0389` | `SHORT` | 2,423,110.30 USD | `1,079.00` | `2333.39` | `2244.40` | `3198.86` | 94,618.61 USD | `+3.90%` | `25X Cross` |
| `923` | `0x8eb7...b90f` | `LONG` | 2,421,033.34 USD | `1,077.74` | `2396.38` | `2244.40` | `1881.09` | -161,644.70 USD | `-6.68%` | `5X Isolated` |
| `925` | `0x2b61...2f6c` | `SHORT` | 2,416,422.42 USD | `1,076.60` | `2681.75` | `2244.40` | `6341.12` | 470,750.32 USD | `+19.48%` | `10X Cross` |
| `935` | `0x6e6f...82a6` | `LONG` | 2,366,513.94 USD | `1,053.80` | `2266.07` | `2244.40` | `1299.19` | -21,476.37 USD | `-0.91%` | `20X Cross` |
| `945` | `0x0a97...347d` | `LONG` | 2,355,529.58 USD | `1,049.14` | `2267.88` | `2244.40` | `1442.66` | -23,796.69 USD | `-1.01%` | `20X Cross` |
| `951` | `0x30af...393e` | `SHORT` | 2,338,144.02 USD | `1,041.16` | `2252.26` | `2244.40` | `2297.06` | 6,838.31 USD | `+0.29%` | `25X Cross` |
| `965` | `0x1b2a...f7a6` | `LONG` | 2,303,386.68 USD | `1,025.37` | `2737.51` | `2244.40` | `882.22` | -503,573.26 USD | `-21.86%` | `10X Cross` |
| `974` | `0x001a...fef6` | `SHORT` | 2,261,444.62 USD | `1,007.33` | `2022.19` | `2244.40` | `3071.04` | -224,436.67 USD | `-9.92%` | `10X Cross` |
| `975` | `0x02aa...1806` | `SHORT` | 2,261,342.56 USD | `1,007.10` | `2654.68` | `2244.40` | `3612.85` | 412,189.54 USD | `+18.23%` | `20X Cross` |
| `980` | `0xdb3a...cf3b` | `LONG` | 2,252,619.19 USD | `1,003.22` | `2705.01` | `2244.40` | `0.000000` | -461,087.71 USD | `-20.47%` | `4X Cross` |
| `984` | `0x8c02...b73f` | `SHORT` | 2,246,400.00 USD | `1,000.00` | `2250.37` | `2244.40` | `8098.54` | 3,971.47 USD | `+0.18%` | `20X Cross` |
| `986` | `0x5272...fcd9` | `SHORT` | 2,245,000.00 USD | `1,000.00` | `2241.82` | `2244.40` | `2830.91` | -3,175.51 USD | `-0.14%` | `5X Cross` |
| `987` | `0xd7b8...9f55` | `LONG` | 2,243,654.10 USD | `999.00` | `2195.00` | `2244.40` | `0.000000` | 50,849.10 USD | `+2.27%` | `15X Cross` |
| `992` | `0xa70a...4be9` | `LONG` | 2,227,648.61 USD | `991.83` | `2259.08` | `2244.40` | `775.91` | -12,973.62 USD | `-0.58%` | `20X Cross` |
| `999` | `0xa0fb...96be` | `LONG` | 2,207,356.24 USD | `982.49` | `2287.96` | `2244.40` | `1257.43` | -40,545.22 USD | `-1.84%` | `3X Cross` |
| `1011` | `0xb002...ed8a` | `SHORT` | 2,160,294.74 USD | `962.78` | `2299.66` | `2244.40` | `4199.14` | 53,783.17 USD | `+2.49%` | `25X Cross` |
| `1015` | `0xbef3...0d3e` | `LONG` | 2,139,307.37 USD | `952.33` | `2233.44` | `2244.40` | `2156.95` | 12,339.39 USD | `+0.58%` | `20X Cross` |
| `1018` | `0x6a41...a3b9` | `LONG` | 2,134,306.23 USD | `950.69` | `2233.05` | `2244.40` | `2160.21` | 11,359.22 USD | `+0.53%` | `20X Cross` |
| `1023` | `0xb812...b5e0` | `LONG` | 2,113,297.69 USD | `940.62` | `2263.21` | `2244.40` | `1184.66` | -15,533.86 USD | `-0.74%` | `25X Cross` |
| `1030` | `0xb1ec...e86a` | `SHORT` | 2,097,325.30 USD | `933.64` | `2272.72` | `2244.40` | `12764.67` | 24,581.65 USD | `+1.17%` | `25X Cross` |
| `1053` | `0xef96...9383` | `LONG` | 2,061,240.26 USD | `917.57` | `2235.00` | `2244.40` | `0.000000` | 10,456.60 USD | `+0.51%` | `25X Cross` |
| `1054` | `0xede2...f971` | `LONG` | 2,053,545.43 USD | `914.31` | `2208.16` | `2244.40` | `1463.13` | 34,588.44 USD | `+1.68%` | `5X Cross` |
| `1060` | `0x9606...4e5d` | `SHORT` | 2,050,773.19 USD | `913.00` | `2478.70` | `2244.40` | `4253.47` | 212,280.42 USD | `+10.35%` | `20X Cross` |
| `1079` | `0x5f10...d49d` | `LONG` | 2,020,500.00 USD | `900.00` | `2249.83` | `2244.40` | `1792.08` | -4,353.47 USD | `-0.22%` | `25X Cross` |
| `1170` | `0x2828...93a0` | `LONG` | 1,883,898.97 USD | `839.60` | `2242.41` | `2244.40` | `2192.68` | 1,166.78 USD | `+0.06%` | `25X Cross` |
| `1173` | `0xcd27...52a8` | `LONG` | 1,880,118.68 USD | `837.21` | `2553.56` | `2244.40` | `1403.37` | -257,746.10 USD | `-13.71%` | `2X Cross` |
| `1234` | `0x04a9...95aa` | `LONG` | 1,796,560.00 USD | `800.00` | `2595.13` | `2244.40` | `1867.30` | -279,546.74 USD | `-15.56%` | `5X Cross` |
| `1235` | `0x7737...bf66` | `SHORT` | 1,796,492.57 USD | `799.79` | `2494.83` | `2244.40` | `24243.83` | 198,853.46 USD | `+11.07%` | `15X Cross` |
| `1269` | `0x458d...ab3b` | `LONG` | 1,740,391.66 USD | `774.75` | `2740.41` | `2244.40` | `1887.12` | -382,737.52 USD | `-21.99%` | `3X Isolated` |
| `1287` | `0x51f6...2b39` | `LONG` | 1,691,511.19 USD | `753.56` | `2224.94` | `2244.40` | `503.75` | 14,888.32 USD | `+0.88%` | `25X Cross` |
| `1324` | `0x3fc5...c0c1` | `SHORT` | 1,639,701.72 USD | `729.92` | `2702.11` | `2244.40` | `4453.70` | 332,640.48 USD | `+20.29%` | `25X Cross` |
| `1325` | `0xaa53...9cb7` | `LONG` | 1,639,605.89 USD | `730.34` | `2389.70` | `2244.40` | `1974.26` | -105,683.75 USD | `-6.45%` | `20X Cross` |
| `1334` | `0xa189...94d7` | `SHORT` | 1,616,136.86 USD | `719.98` | `2691.84` | `2244.40` | `2914.99` | 321,935.80 USD | `+19.92%` | `25X Cross` |
| `1352` | `0x2f93...4404` | `LONG` | 1,587,919.78 USD | `707.47` | `1700.45` | `2244.40` | `1368.75` | 384,893.41 USD | `+24.24%` | `4X Isolated` |
| `1362` | `0x5605...fe0f` | `SHORT` | 1,575,750.67 USD | `702.14` | `2566.90` | `2244.40` | `3061.96` | 226,581.98 USD | `+14.38%` | `20X Cross` |
| `1366` | `0x7743...e4fe` | `SHORT` | 1,573,028.89 USD | `700.56` | `2298.56` | `2244.40` | `6178.18` | 37,246.20 USD | `+2.37%` | `25X Cross` |
| `1381` | `0x0deb...0bc5` | `LONG` | 1,571,500.00 USD | `700.00` | `2071.05` | `2244.40` | `1597.34` | 121,764.21 USD | `+7.75%` | `20X Cross` |
| `1394` | `0x2e30...4cb5` | `SHORT` | 1,551,702.76 USD | `691.06` | `2334.27` | `2244.40` | `9386.29` | 61,415.11 USD | `+3.96%` | `2X Cross` |
| `1416` | `0x248e...6be2` | `SHORT` | 1,529,841.61 USD | `680.93` | `2282.89` | `2244.40` | `3463.18` | 24,644.05 USD | `+1.61%` | `20X Cross` |
| `1422` | `0xdbd1...29dd` | `SHORT` | 1,527,836.76 USD | `680.70` | `3030.57` | `2244.40` | `3771.04` | 535,084.36 USD | `+35.02%` | `6X Cross` |
| `1426` | `0x71e5...be04` | `LONG` | 1,521,361.97 USD | `677.67` | `2727.27` | `2244.40` | `1470.90` | -326,823.64 USD | `-21.48%` | `20X Cross` |
| `1435` | `0x0b23...f37b` | `LONG` | 1,515,037.50 USD | `675.00` | `2238.15` | `2244.40` | `590.62` | 4,280.86 USD | `+0.28%` | `5X Cross` |
| `1459` | `0x0cac...6170` | `SHORT` | 1,476,350.50 USD | `657.50` | `2146.55` | `2244.40` | `2839.35` | -64,988.30 USD | `-4.40%` | `20X Cross` |
| `1494` | `0xb15b...dbae` | `SHORT` | 1,443,505.16 USD | `642.64` | `2290.80` | `2244.40` | `2277.84` | 28,662.32 USD | `+1.99%` | `25X Cross` |
| `1495` | `0xf00e...fe3d` | `SHORT` | 1,443,394.18 USD | `642.88` | `2333.21` | `2244.40` | `2475.01` | 56,583.79 USD | `+3.92%` | `20X Cross` |
| `1500` | `0xffb2...5ed6` | `SHORT` | 1,438,137.01 USD | `640.77` | `2672.96` | `2244.40` | `2516.27` | 274,611.34 USD | `+19.09%` | `20X Cross` |
| `1508` | `0x8505...1821` | `SHORT` | 1,423,494.46 USD | `633.96` | `2239.93` | `2244.40` | `3896.47` | -3,462.86 USD | `-0.24%` | `20X Cross` |
| `1524` | `0xfc27...9d9d` | `LONG` | 1,408,145.20 USD | `627.32` | `2242.98` | `2244.40` | `0.000000` | 1,073.24 USD | `+0.08%` | `25X Cross` |
| `1529` | `0xfce0...f4c0` | `SHORT` | 1,400,855.04 USD | `623.60` | `3129.61` | `2244.40` | `2802.49` | 550,771.55 USD | `+39.32%` | `20X Cross` |
| `1580` | `0xad02...eb65` | `LONG` | 1,348,632.60 USD | `600.62` | `2460.69` | `2244.40` | `1078.82` | -129,307.96 USD | `-9.59%` | `5X Cross` |
| `1581` | `0x24fb...ed0f` | `LONG` | 1,347,815.62 USD | `600.10` | `2199.85` | `2244.40` | `0.000000` | 27,692.18 USD | `+2.05%` | `15X Cross` |
| `1582` | `0x638f...f5f0` | `LONG` | 1,347,240.00 USD | `600.00` | `4011.50` | `2244.40` | `308.95` | -1,059,663.53 USD | `-78.65%` | `25X Cross` |
| `1585` | `0x26e6...6b28` | `LONG` | 1,346,460.00 USD | `600.00` | `1769.78` | `2244.40` | `2004.62` | 284,588.47 USD | `+21.14%` | `20X Cross` |
| `1650` | `0xfc66...ca06` | `SHORT` | 1,274,851.50 USD | `567.43` | `2275.19` | `2244.40` | `7316.74` | 16,171.71 USD | `+1.27%` | `20X Cross` |
| `1653` | `0x9362...7d7c` | `SHORT` | 1,272,418.46 USD | `566.99` | `2226.19` | `2244.40` | `2518.80` | -10,182.64 USD | `-0.80%` | `20X Cross` |
| `1657` | `0xfb99...37f3` | `LONG` | 1,269,982.25 USD | `565.34` | `2362.35` | `2244.40` | `1240.41` | -65,554.11 USD | `-5.16%` | `3X Cross` |
| `1666` | `0x844b...7f42` | `SHORT` | 1,260,118.20 USD | `561.00` | `2026.17` | `2244.40` | `2996.89` | -123,434.79 USD | `-9.80%` | `25X Cross` |
| `1680` | `0xabe6...1d99` | `SHORT` | 1,248,340.18 USD | `556.00` | `2484.68` | `2244.40` | `3094.76` | 133,155.71 USD | `+10.67%` | `20X Cross` |
| `1682` | `0x2a76...9a53` | `LONG` | 1,246,507.54 USD | `554.99` | `2231.40` | `2244.40` | `0.000000` | 8,100.48 USD | `+0.65%` | `25X Cross` |
| `1695` | `0x936c...bb0f` | `LONG` | 1,235,168.94 USD | `550.09` | `2218.31` | `2244.40` | `0.000000` | 14,901.67 USD | `+1.21%` | `20X Cross` |
| `1696` | `0x825c...465e` | `LONG` | 1,234,970.00 USD | `550.00` | `2208.12` | `2244.40` | `1189.41` | 20,500.50 USD | `+1.66%` | `4X Cross` |
| `1703` | `0xad21...fb6a` | `LONG` | 1,228,589.50 USD | `547.26` | `2565.80` | `2244.40` | `1724.25` | -175,563.50 USD | `-14.29%` | `6X Cross` |
| `1795` | `0x0c7a...2f50` | `SHORT` | 1,143,255.70 USD | `509.25` | `2122.56` | `2244.40` | `4102.46` | -62,350.27 USD | `-5.45%` | `20X Cross` |
| `1803` | `0x0089...2410` | `SHORT` | 1,138,990.87 USD | `507.35` | `2308.88` | `2244.40` | `3416.52` | 32,409.39 USD | `+2.85%` | `20X Cross` |
| `1822` | `0xa559...ff95` | `LONG` | 1,123,200.00 USD | `500.00` | `2260.68` | `2244.40` | `1042.59` | -7,144.36 USD | `-0.64%` | `20X Cross` |
| `1823` | `0x6936...9417` | `SHORT` | 1,123,200.00 USD | `500.00` | `2315.11` | `2244.40` | `2358.86` | 34,355.21 USD | `+3.06%` | `25X Isolated` |
| `1824` | `0x4044...794c` | `LONG` | 1,123,200.00 USD | `500.00` | `2260.80` | `2244.40` | `0.000000` | -7,200.00 USD | `-0.64%` | `25X Cross` |
| `1825` | `0x89b2...9ca6` | `LONG` | 1,123,000.00 USD | `500.00` | `2363.45` | `2244.40` | `1622.60` | -58,727.42 USD | `-5.23%` | `25X Cross` |
| `1827` | `0xe282...df29` | `LONG` | 1,122,700.00 USD | `500.00` | `2309.84` | `2244.40` | `2045.26` | -32,224.21 USD | `-2.87%` | `10X Isolated` |
| `1828` | `0xb322...d51f` | `SHORT` | 1,122,700.00 USD | `500.00` | `2268.03` | `2244.40` | `3781.35` | 11,316.32 USD | `+1.01%` | `20X Cross` |
| `1833` | `0x7298...7d6c` | `SHORT` | 1,119,042.59 USD | `498.15` | `3426.75` | `2244.40` | `5421.56` | 587,993.23 USD | `+52.54%` | `20X Cross` |
| `1845` | `0x9c68...7783` | `SHORT` | 1,108,166.64 USD | `493.31` | `2273.58` | `2244.40` | `3959.94` | 13,412.61 USD | `+1.21%` | `25X Cross` |
| `1853` | `0x404c...5f03` | `SHORT` | 1,100,057.78 USD | `489.79` | `2671.94` | `2244.40` | `4926.39` | 208,621.77 USD | `+18.96%` | `20X Cross` |
| `1855` | `0x321f...1c84` | `SHORT` | 1,096,180.19 USD | `488.02` | `2370.09` | `2244.40` | `3055.28` | 60,464.41 USD | `+5.52%` | `10X Cross` |
| `1900` | `0xe86b...3664` | `LONG` | 1,049,940.40 USD | `467.39` | `2231.29` | `2244.40` | `0.000000` | 7,059.47 USD | `+0.67%` | `25X Cross` |
| `1915` | `0x94b6...e5b3` | `SHORT` | 1,041,593.14 USD | `463.86` | `2261.12` | `2244.40` | `2403.56` | 7,249.53 USD | `+0.70%` | `25X Cross` |
| `1921` | `0x82c6...fe42` | `LONG` | 1,038,960.00 USD | `462.50` | `2501.38` | `2244.40` | `2053.60` | -117,930.57 USD | `-11.35%` | `5X Isolated` |
| `1926` | `0xe330...77a1` | `SHORT` | 1,036,180.29 USD | `461.20` | `2206.97` | `2244.40` | `6421.47` | -18,322.92 USD | `-1.77%` | `20X Cross` |
| `1934` | `0x2de3...486d` | `LONG` | 1,033,598.00 USD | `460.40` | `2286.27` | `2244.40` | `1193.24` | -19,002.91 USD | `-1.84%` | `25X Cross` |
| `1943` | `0x617e...0f97` | `SHORT` | 1,027,883.13 USD | `457.85` | `2205.60` | `2244.40` | `3342.21` | -18,039.29 USD | `-1.75%` | `10X Cross` |
| `1986` | `0xae55...2236` | `LONG` | 1,010,115.00 USD | `450.00` | `2510.21` | `2244.40` | `0.000000` | -119,482.50 USD | `-11.83%` | `25X Cross` |
| `1988` | `0xc10f...23b3` | `LONG` | 1,009,867.50 USD | `450.00` | `2366.44` | `2244.40` | `2016.67` | -55,030.77 USD | `-5.45%` | `25X Cross` |
| `1999` | `0xac26...a9c7` | `SHORT` | 1,001,441.25 USD | `446.14` | `2192.58` | `2244.40` | `8651.03` | -23,250.71 USD | `-2.32%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2739.00` | 83,040.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 83.04K USD at 2739.0000 USD [API] | `2026-09-29 12:15:35` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 41,987.26 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 41.99K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 40,056.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 115,537.73 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 115.54K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2308.40` | 136,902.43 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 136.90K USD at 2308.4000 USD [API] | `2026-10-29 03:43:57` |
| `ANNOUNCEMENT` | `INFO` | `2362.70` | 42.29 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.04K USD at 2362.7000 USD [API] | `2026-10-27 21:33:33` |
| `ANNOUNCEMENT` | `INFO` | `2362.70` | 36.62 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.04K USD at 2362.7000 USD [API] | `2026-10-27 21:33:33` |
| `ANNOUNCEMENT` | `INFO` | `1592.40` | 11,956.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.96K USD at 1592.4000 USD [API] | `2026-06-24 16:51:42` |
| `ANNOUNCEMENT` | `INFO` | `2375.40` | 17,545.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 17.55K USD at 2375.4000 USD [API] | `2026-10-28 08:26:36` |
| `ANNOUNCEMENT` | `INFO` | `2309.50` | 46,190.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 46.19K USD at 2309.5000 USD [API] | `2026-10-29 04:24:02` |
| `ANNOUNCEMENT` | `INFO` | `2325.50` | 145,724.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 145.72K USD at 2325.5000 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `2325.50` | 59,066.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 59.07K USD at 2325.5000 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `2325.50` | 94,775.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 94.78K USD at 2325.5000 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `2292.40` | 14,347.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 14.35K USD at 2292.4000 USD [API] | `2026-10-29 02:36:05` |
| `ANNOUNCEMENT` | `INFO` | `2292.40` | 4,279.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.28K USD at 2292.4000 USD [API] | `2026-10-29 02:36:05` |
| `ANNOUNCEMENT` | `INFO` | `2292.40` | 1,975.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.98K USD at 2292.4000 USD [API] | `2026-10-29 02:36:05` |
| `ANNOUNCEMENT` | `INFO` | `2293.50` | 22.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2293.5000 USD [API] | `2026-10-29 02:36:02` |
| `ANNOUNCEMENT` | `INFO` | `2295.60` | 18,364.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.36K USD at 2295.6000 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `2295.60` | 5,870.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 5.87K USD at 2295.6000 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 18,298.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.30K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 3,147.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.15K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 189.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.19K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 1,020.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.02K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 755.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.76K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2324.10` | 1,329.62 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.33K USD at 2324.1000 USD [API] | `2026-10-29 01:48:08` |
| `ANNOUNCEMENT` | `INFO` | `2325.70` | 22,155.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 22.16K USD at 2325.7000 USD [API] | `2026-10-29 01:48:04` |
| `ANNOUNCEMENT` | `INFO` | `2328.20` | 15.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2328.2000 USD [API] | `2026-10-29 01:45:39` |
| `ANNOUNCEMENT` | `INFO` | `2326.40` | 45,946.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 45.95K USD at 2326.4000 USD [API] | `2026-10-29 05:07:16` |
| `ANNOUNCEMENT` | `INFO` | `2326.20` | 73,539.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 73.54K USD at 2326.2000 USD [API] | `2026-10-29 05:07:10` |
| `ANNOUNCEMENT` | `INFO` | `2974.40` | 2,185.89 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.19K USD at 2974.4000 USD [API] | `2025-11-25 22:58:18` |
| `ANNOUNCEMENT` | `INFO` | `2974.40` | 184.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.18K USD at 2974.4000 USD [API] | `2025-11-25 22:58:18` |
| `ANNOUNCEMENT` | `INFO` | `2920.50` | 4,440.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.44K USD at 2920.5000 USD [API] | `2025-11-25 01:57:27` |
| `ANNOUNCEMENT` | `INFO` | `2328.30` | 46,566.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 46.57K USD at 2328.3000 USD [API] | `2026-10-29 05:11:13` |
| `ANNOUNCEMENT` | `INFO` | `2330.20` | 40,000.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.00K USD at 2330.2000 USD [API] | `2026-10-29 05:15:56` |
| `ANNOUNCEMENT` | `INFO` | `4627.50` | 49,004.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 49.00K USD at 4627.5000 USD [API] | `2025-09-13 16:16:18` |
| `ANNOUNCEMENT` | `INFO` | `4336.50` | 111,284.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 111.28K USD at 4336.5000 USD [API] | `2025-09-02 01:49:43` |
| `ANNOUNCEMENT` | `INFO` | `4336.50` | 9,999.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 10.00K USD at 4336.5000 USD [API] | `2025-09-02 01:49:43` |
| `ANNOUNCEMENT` | `INFO` | `4336.50` | 24,999.92 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 25.00K USD at 4336.5000 USD [API] | `2025-09-02 01:49:43` |
| `ANNOUNCEMENT` | `INFO` | `4336.50` | 3,332.17 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.33K USD at 4336.5000 USD [API] | `2025-09-02 01:49:43` |
| `ANNOUNCEMENT` | `INFO` | `4336.50` | 37,403.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 37.40K USD at 4336.5000 USD [API] | `2025-09-02 01:49:39` |
| `ANNOUNCEMENT` | `INFO` | `4428.00` | 1,398.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.40K USD at 4428.0000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 1,758.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.76K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 1,758.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.76K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 1,758.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.76K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 114.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.11K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 1,758.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.76K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 2,870.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.87K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 1,758.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.76K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 44,279.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 44.28K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 17,656.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 17.66K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 44,279.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 44.28K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4427.90` | 33,887.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 33.89K USD at 4427.9000 USD [API] | `2025-08-31 00:46:03` |
| `ANNOUNCEMENT` | `INFO` | `4428.00` | 1,353.64 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.35K USD at 4428.0000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4428.00` | 221.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 4428.0000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.80` | 221.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 4427.8000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.70` | 10,670.31 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 10.67K USD at 4427.7000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.70` | 6,082.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 6.08K USD at 4427.7000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.70` | 221.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 4427.7000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.70` | 442.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.44K USD at 4427.7000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.60` | 221.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 4427.6000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.50` | 718.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.72K USD at 4427.5000 USD [API] | `2025-08-31 00:46:00` |
| `ANNOUNCEMENT` | `INFO` | `4427.50` | 18,162.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.16K USD at 4427.5000 USD [API] | `2025-08-31 00:46:00` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2296.42` (Vol: 23,400,000.00 USD, Dist: `+2.12%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--3.31%`)
  * 48H Horizon: Short MP=`2402.29` (Vol: 24,100,000.00 USD, Dist: `+6.83%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.32%`)
  * 3D Horizon: Short MP=`2402.29` (Vol: 29,900,000.00 USD, Dist: `+6.83%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.32%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+6.81%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--3.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 110,170.00 USD | 759,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 1,690,000.00 USD | 759,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 1,430,000.00 USD | 757,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 175,090.00 USD | 756,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 15,890.00 USD | 756,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 50,760.00 USD | 756,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 4,970.00 USD | 756,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 23,410.00 USD | 756,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 8,530.00 USD | 756,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 170,330.00 USD | 756,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 39,640.00 USD | 755,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 924,020.00 USD | 755,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 2,870,000.00 USD | 754,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 53,900.00 USD | 752,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 459,960.00 USD | 752,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 21,160.00 USD | 751,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 129,260.00 USD | 751,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 22,970.00 USD | 751,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 590.55 USD | 751,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 193,580.00 USD | 751,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 67,600.00 USD | 751,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 73,910.00 USD | 751,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 27,470.00 USD | 751,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 163,870.00 USD | 751,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 35,390.00 USD | 750,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 27,860.00 USD | 750,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,580.00 USD | 750,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 433,130.00 USD | 750,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 61,900.00 USD | 750,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 76,030.00 USD | 750,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 38,370.00 USD | 750,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 50,490.00 USD | 750,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 65,760.00 USD | 750,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 94,180.00 USD | 750,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 59,650.00 USD | 749,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 147,660.00 USD | 749,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 137,500.00 USD | 749,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 344,930.00 USD | 749,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 54,230.00 USD | 749,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 893,380.00 USD | 749,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 53,780.00 USD | 748,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 635,970.00 USD | 748,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 492,740.00 USD | 747,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 972,570.00 USD | 747,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 223,800.00 USD | 746,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 131,270.00 USD | 745,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 180,390.00 USD | 745,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 207,340.00 USD | 745,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 49,510.00 USD | 745,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 57,540.00 USD | 745,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 211,110.00 USD | 745,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 321,380.00 USD | 745,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 242,680.00 USD | 744,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 202,990.00 USD | 744,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 17,760.00 USD | 744,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 452,000.00 USD | 744,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 200,320.00 USD | 743,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 360,290.00 USD | 743,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 23,860.00 USD | 743,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 1,000,000.00 USD | 743,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 8,920,000.00 USD | 742,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 331,680.00 USD | 733,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 656,510.00 USD | 733,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 370,330.00 USD | 732,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 71,160.00 USD | 732,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 151,030.00 USD | 731,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 7,660,000.00 USD | 731,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 1,270,000.00 USD | 724,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 1,490,000.00 USD | 722,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 767,090.00 USD | 721,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 542,570.00 USD | 720,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 22,160.00 USD | 720,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 287,780.00 USD | 720,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 3,950,000.00 USD | 719,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 343,160.00 USD | 715,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 737,430.00 USD | 715,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 128,250.00 USD | 714,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 8,140,000.00 USD | 714,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 797,860.00 USD | 706,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 137,210.00 USD | 705,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 405,660.00 USD | 705,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 159,410.00 USD | 705,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,430,000.00 USD | 704,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 273,630.00 USD | 689,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 453,230.00 USD | 689,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 424,160.00 USD | 688,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 189,440.00 USD | 688,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 494,710.00 USD | 688,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 6,890,000.00 USD | 687,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 12,240,000.00 USD | 680,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 53,710.00 USD | 668,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,230,000.00 USD | 668,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 7,670,000.00 USD | 667,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 2,390,000.00 USD | 659,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 405,620.00 USD | 657,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,120,000.00 USD | 656,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 167,710.00 USD | 646,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 708,070.00 USD | 646,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 19,400,000.00 USD | 645,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 325,300.00 USD | 626,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 999,940.00 USD | 626,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 1,880,000.00 USD | 625,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 12,290,000.00 USD | 623,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 1,880,000.00 USD | 610,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 319,620.00 USD | 609,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 374,890.00 USD | 608,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 543,600.00 USD | 608,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 33,880,000.00 USD | 607,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 879,130.00 USD | 573,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 3,480,000.00 USD | 573,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 323,910.00 USD | 569,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 2,760,000.00 USD | 569,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 949,950.00 USD | 566,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 2,470,000.00 USD | 565,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,810,000.00 USD | 563,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,110,000.00 USD | 561,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 850,040.00 USD | 543,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,910,000.00 USD | 542,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,900,000.00 USD | 540,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,650,000.00 USD | 521,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 1,370,000.00 USD | 484,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 11,830,000.00 USD | 483,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 754,140.00 USD | 471,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 4,680,000.00 USD | 470,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 354,260.00 USD | 466,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,220,000.00 USD | 465,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 757,730.00 USD | 464,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 37,730,000.00 USD | 463,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 606,210.00 USD | 426,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 28,750,000.00 USD | 425,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 10,030,000.00 USD | 396,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 675,970.00 USD | 386,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 3,900,000.00 USD | 386,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 56,040,000.00 USD | 382,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 18,460,000.00 USD | 326,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 4,320,000.00 USD | 307,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 12,040,000.00 USD | 303,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,530,000.00 USD | 291,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 941,830.00 USD | 289,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 16,830,000.00 USD | 288,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,260,000.00 USD | 272,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 2,730,000.00 USD | 270,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 5,700,000.00 USD | 268,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 4,940,000.00 USD | 262,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 1,100,000.00 USD | 257,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 403,940.00 USD | 256,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,040,000.00 USD | 255,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 16,740,000.00 USD | 237,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 827,870.00 USD | 221,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 5,110,000.00 USD | 220,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 1,720,000.00 USD | 215,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 3,200,000.00 USD | 213,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1972.90` | 981,920,000.00 USD | 981,920,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,510,000.00 USD | 210,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1976.10` | 981,790,000.00 USD | 981,790,000.00 USD | 2,240,000.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1982.50` | 979,500,000.00 USD | 979,500,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 4,860,000.00 USD | 208,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1985.70` | 979,290,000.00 USD | 979,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1988.90` | 977,000,000.00 USD | 977,000,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1992.10` | 973,750,000.00 USD | 973,750,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,500,000.00 USD | 203,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1995.30` | 971,040,000.00 USD | 971,040,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2004.90` | 968,890,000.00 USD | 968,890,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,170,000.00 USD | 202,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.10` | 693,530,000.00 USD | 693,530,000.00 USD | 14,690.00 USD | 18,870.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.50` | 693,480,000.00 USD | 693,480,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2009.90` | 693,260,000.00 USD | 693,260,000.00 USD | 0.00 USD | 308,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.30` | 968,620,000.00 USD | 968,620,000.00 USD | 170,840.00 USD | 92,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.30` | 692,950,000.00 USD | 692,950,000.00 USD | 323,820.00 USD | 266,130.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2014.70` | 692,340,000.00 USD | 692,340,000.00 USD | 355,800.00 USD | 31,280.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,740,000.00 USD | 200,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2017.10` | 691,940,000.00 USD | 691,940,000.00 USD | 483,920.00 USD | 897,320.00 USD | 518,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2019.50` | 690,040,000.00 USD | 690,040,000.00 USD | 326,370.00 USD | 1,460,000.00 USD | 377,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2021.90` | 687,880,000.00 USD | 687,880,000.00 USD | 973,110.00 USD | 199,120.00 USD | 800,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2024.30` | 685,910,000.00 USD | 685,910,000.00 USD | 122,610.00 USD | 0.00 USD | 927,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,930,000.00 USD | 197,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2026.70` | 684,860,000.00 USD | 684,860,000.00 USD | 280,250.00 USD | 1,130,000.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2027.30` | 968,360,000.00 USD | 968,360,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.10` | 683,410,000.00 USD | 683,410,000.00 USD | 1,140,000.00 USD | 1,180,000.00 USD | 609,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2030.50` | 968,180,000.00 USD | 968,180,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2031.50` | 680,480,000.00 USD | 680,480,000.00 USD | 677,540.00 USD | 293,350.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.70` | 963,780,000.00 USD | 963,780,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2033.90` | 678,450,000.00 USD | 678,450,000.00 USD | 1,810,000.00 USD | 1,330,000.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 519,090.00 USD | 195,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2036.30` | 675,150,000.00 USD | 675,150,000.00 USD | 119,600.00 USD | 177,360.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2036.90` | 962,220,000.00 USD | 962,220,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.70` | 674,840,000.00 USD | 674,840,000.00 USD | 939,380.00 USD | 300,240.00 USD | 377,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2040.10` | 961,890,000.00 USD | 961,890,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.10` | 673,220,000.00 USD | 673,220,000.00 USD | 626,840.00 USD | 178,560.00 USD | 176,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2043.30` | 960,440,000.00 USD | 960,440,000.00 USD | 0.00 USD | 0.00 USD | 101,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2043.50` | 672,240,000.00 USD | 672,240,000.00 USD | 0.00 USD | 0.00 USD | 28,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 1,880,000.00 USD | 195,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.90` | 672,210,000.00 USD | 672,210,000.00 USD | 0.00 USD | 0.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2046.50` | 960,330,000.00 USD | 960,330,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2048.30` | 672,190,000.00 USD | 672,190,000.00 USD | 518,440.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2049.70` | 960,140,000.00 USD | 960,140,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.70` | 671,310,000.00 USD | 671,310,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2052.90` | 959,910,000.00 USD | 959,910,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.10` | 670,260,000.00 USD | 670,260,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 6,680,000.00 USD | 193,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.50` | 670,230,000.00 USD | 670,230,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2057.90` | 669,900,000.00 USD | 669,900,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2059.30` | 957,630,000.00 USD | 957,630,000.00 USD | 153,480.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2062.50` | 956,470,000.00 USD | 956,470,000.00 USD | 1,680,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.70` | 669,140,000.00 USD | 669,140,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 14,080,000.00 USD | 186,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.10` | 669,060,000.00 USD | 669,060,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2065.70` | 951,950,000.00 USD | 951,950,000.00 USD | 1,380,000.00 USD | 313,000.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.50` | 667,450,000.00 USD | 667,450,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.90` | 949,180,000.00 USD | 949,180,000.00 USD | 1,580,000.00 USD | 2,680,000.00 USD | 811,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2069.90` | 666,760,000.00 USD | 666,760,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2072.10` | 944,110,000.00 USD | 944,110,000.00 USD | 4,410,000.00 USD | 2,530,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.30` | 666,380,000.00 USD | 666,380,000.00 USD | 67,060.00 USD | 534,600.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2074.70` | 665,770,000.00 USD | 665,770,000.00 USD | 46,190.00 USD | 244,720.00 USD | 423,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,650,000.00 USD | 172,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2075.30` | 935,070,000.00 USD | 935,070,000.00 USD | 4,120,000.00 USD | 3,610,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.10` | 665,060,000.00 USD | 665,060,000.00 USD | 998,330.00 USD | 327,010.00 USD | 448,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.50` | 923,320,000.00 USD | 923,320,000.00 USD | 4,400,000.00 USD | 3,500,000.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.50` | 663,290,000.00 USD | 663,290,000.00 USD | 953,710.00 USD | 846,970.00 USD | 268,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.70` | 913,330,000.00 USD | 913,330,000.00 USD | 4,470,000.00 USD | 2,960,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.90` | 661,220,000.00 USD | 661,220,000.00 USD | 1,060,000.00 USD | 825,250.00 USD | 208,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.30` | 659,120,000.00 USD | 659,120,000.00 USD | 875,040.00 USD | 789,300.00 USD | 291,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.90` | 903,900,000.00 USD | 903,900,000.00 USD | 3,070,000.00 USD | 2,030,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 12,760,000.00 USD | 170,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.70` | 657,170,000.00 USD | 657,170,000.00 USD | 1,560,000.00 USD | 559,980.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.10` | 893,190,000.00 USD | 893,190,000.00 USD | 3,310,000.00 USD | 2,260,000.00 USD | 924,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.10` | 653,470,000.00 USD | 653,470,000.00 USD | 445,800.00 USD | 218,010.00 USD | 79,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 886,700,000.00 USD | 886,700,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.50` | 652,720,000.00 USD | 652,720,000.00 USD | 995,340.00 USD | 294,070.00 USD | 548,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2093.90` | 650,880,000.00 USD | 650,880,000.00 USD | 1,760,000.00 USD | 775,630.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.50` | 873,750,000.00 USD | 873,750,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,850,000.00 USD | 157,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.30` | 647,290,000.00 USD | 647,290,000.00 USD | 655,450.00 USD | 616,370.00 USD | 982,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.70` | 863,520,000.00 USD | 863,520,000.00 USD | 1,850,000.00 USD | 3,350,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.70` | 645,030,000.00 USD | 645,030,000.00 USD | 296,850.00 USD | 970,270.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.90` | 857,030,000.00 USD | 857,030,000.00 USD | 1,810,000.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.10` | 643,520,000.00 USD | 643,520,000.00 USD | 145,240.00 USD | 353,390.00 USD | 231,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.50` | 642,790,000.00 USD | 642,790,000.00 USD | 268,400.00 USD | 119,690.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.10` | 849,620,000.00 USD | 849,620,000.00 USD | 1,440,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,330,000.00 USD | 155,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.90` | 642,090,000.00 USD | 642,090,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.30` | 845,130,000.00 USD | 845,130,000.00 USD | 8,470,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.30` | 636,150,000.00 USD | 636,150,000.00 USD | 656,240.00 USD | 9,120.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.50` | 834,320,000.00 USD | 834,320,000.00 USD | 2,930,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.70` | 635,480,000.00 USD | 635,480,000.00 USD | 36,110.00 USD | 22,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.10` | 635,420,000.00 USD | 635,420,000.00 USD | 866,490.00 USD | 506,690.00 USD | 244,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.70` | 826,490,000.00 USD | 826,490,000.00 USD | 1,810,000.00 USD | 1,810,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,800,000.00 USD | 152,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.50` | 633,800,000.00 USD | 633,800,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2116.90` | 819,860,000.00 USD | 819,860,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.90` | 632,050,000.00 USD | 632,050,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.10` | 812,580,000.00 USD | 812,580,000.00 USD | 13,490,000.00 USD | 5,410,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.30` | 623,260,000.00 USD | 623,260,000.00 USD | 5,430,000.00 USD | 325,610.00 USD | 671,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.70` | 616,830,000.00 USD | 616,830,000.00 USD | 3,690,000.00 USD | 3,490,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.30` | 791,080,000.00 USD | 791,080,000.00 USD | 7,590,000.00 USD | 6,420,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,380,000.00 USD | 150,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.10` | 607,810,000.00 USD | 607,810,000.00 USD | 6,280,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2126.50` | 775,080,000.00 USD | 775,080,000.00 USD | 3,220,000.00 USD | 6,310,000.00 USD | 5,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.50` | 597,590,000.00 USD | 597,590,000.00 USD | 3,570,000.00 USD | 4,180,000.00 USD | 782,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.70` | 759,960,000.00 USD | 759,960,000.00 USD | 5,040,000.00 USD | 1,260,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2129.90` | 589,060,000.00 USD | 589,060,000.00 USD | 2,080,000.00 USD | 172,040.00 USD | 762,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.30` | 586,040,000.00 USD | 586,040,000.00 USD | 0.00 USD | 177,810.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2132.90` | 751,960,000.00 USD | 751,960,000.00 USD | 1,850,000.00 USD | 1,790,000.00 USD | 770,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2134.70` | 584,330,000.00 USD | 584,330,000.00 USD | 20,600.00 USD | 460,010.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,250,000.00 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2136.10` | 747,540,000.00 USD | 747,540,000.00 USD | 1,820,000.00 USD | 849,030.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.10` | 583,760,000.00 USD | 583,760,000.00 USD | 21,090.00 USD | 1,090,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.30` | 744,860,000.00 USD | 744,860,000.00 USD | 1,110,000.00 USD | 1,920,000.00 USD | 434,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2139.50` | 582,650,000.00 USD | 582,650,000.00 USD | 36,740.00 USD | 265,280.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2141.90` | 582,280,000.00 USD | 582,280,000.00 USD | 473,480.00 USD | 805,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.50` | 741,400,000.00 USD | 741,400,000.00 USD | 2,300,000.00 USD | 503,710.00 USD | 661,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2144.30` | 581,010,000.00 USD | 581,010,000.00 USD | 258,680.00 USD | 2,770,000.00 USD | 118,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 4,680,000.00 USD | 25,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2145.70` | 737,940,000.00 USD | 737,940,000.00 USD | 1,110,000.00 USD | 1,760,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2146.70` | 577,860,000.00 USD | 577,860,000.00 USD | 1,500,000.00 USD | 1,410,000.00 USD | 58,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.90` | 735,070,000.00 USD | 735,070,000.00 USD | 485,890.00 USD | 1,000,000.00 USD | 465,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2149.10` | 574,890,000.00 USD | 574,890,000.00 USD | 6,970,000.00 USD | 1,320,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.50` | 565,250,000.00 USD | 565,250,000.00 USD | 2,630,000.00 USD | 2,580,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2152.10` | 733,110,000.00 USD | 733,110,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2153.90` | 557,730,000.00 USD | 557,730,000.00 USD | 722,300.00 USD | 3,860,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 3,580,000.00 USD | 20,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.30` | 721,550,000.00 USD | 721,550,000.00 USD | 186,890.00 USD | 1,720,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2156.30` | 551,760,000.00 USD | 551,760,000.00 USD | 4,060,000.00 USD | 1,550,000.00 USD | 2,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.50` | 718,020,000.00 USD | 718,020,000.00 USD | 4,580,000.00 USD | 2,190,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.70` | 544,020,000.00 USD | 544,020,000.00 USD | 1,300,000.00 USD | 790,770.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2161.10` | 538,170,000.00 USD | 538,170,000.00 USD | 6,320,000.00 USD | 7,640,000.00 USD | 549,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.70` | 708,510,000.00 USD | 708,510,000.00 USD | 236,540.00 USD | 2,620,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.50` | 523,670,000.00 USD | 523,670,000.00 USD | 12,520,000.00 USD | 8,710,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2164.90` | 704,460,000.00 USD | 704,460,000.00 USD | 21,940,000.00 USD | 17,760,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,760,000.00 USD | 17,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.90` | 500,130,000.00 USD | 500,130,000.00 USD | 11,060,000.00 USD | 11,880,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.10` | 661,640,000.00 USD | 661,640,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2168.30` | 472,600,000.00 USD | 472,600,000.00 USD | 16,140,000.00 USD | 6,570,000.00 USD | 5,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.70` | 444,830,000.00 USD | 444,830,000.00 USD | 22,920,000.00 USD | 8,330,000.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.30` | 629,030,000.00 USD | 629,030,000.00 USD | 2,550,000.00 USD | 6,730,000.00 USD | 6,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.10` | 406,740,000.00 USD | 406,740,000.00 USD | 6,820,000.00 USD | 3,860,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2174.50` | 613,120,000.00 USD | 613,120,000.00 USD | 35,320,000.00 USD | 1,690,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 10,540,000.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.50` | 392,260,000.00 USD | 392,260,000.00 USD | 3,540,000.00 USD | 355,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.70` | 573,600,000.00 USD | 573,600,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.90` | 388,370,000.00 USD | 388,370,000.00 USD | 771,300.00 USD | 0.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.30` | 384,770,000.00 USD | 384,770,000.00 USD | 853,380.00 USD | 1,460,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.70` | 381,090,000.00 USD | 381,090,000.00 USD | 73,470.00 USD | 26,540.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2184.10` | 572,280,000.00 USD | 572,280,000.00 USD | 24,680,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 462,620.00 USD | 782,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.10` | 377,950,000.00 USD | 377,950,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.30` | 542,350,000.00 USD | 542,350,000.00 USD | 14,380,000.00 USD | 17,750,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.50` | 372,790,000.00 USD | 372,790,000.00 USD | 3,960,000.00 USD | 1,250,000.00 USD | 5,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2189.90` | 362,220,000.00 USD | 362,220,000.00 USD | 3,010,000.00 USD | 3,680,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.50` | 510,210,000.00 USD | 510,210,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.30` | 350,440,000.00 USD | 350,440,000.00 USD | 6,650,000.00 USD | 2,870,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.70` | 465,250,000.00 USD | 465,250,000.00 USD | 141,070.00 USD | 7,340,000.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2194.70` | 339,720,000.00 USD | 339,720,000.00 USD | 5,460,000.00 USD | 4,300,000.00 USD | 2,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 146,720.00 USD | 319,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2196.90` | 449,680,000.00 USD | 449,680,000.00 USD | 242,610.00 USD | 243,760.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.10` | 327,340,000.00 USD | 327,340,000.00 USD | 4,540,000.00 USD | 978,380.00 USD | 6,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2199.50` | 315,460,000.00 USD | 315,460,000.00 USD | 1,510,000.00 USD | 2,760,000.00 USD | 7,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.10` | 447,160,000.00 USD | 447,160,000.00 USD | 0.00 USD | 0.00 USD | 5,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.90` | 303,420,000.00 USD | 303,420,000.00 USD | 7,020,000.00 USD | 4,720,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.30` | 441,760,000.00 USD | 441,760,000.00 USD | 4,310,000.00 USD | 0.00 USD | 7,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.30` | 288,800,000.00 USD | 288,800,000.00 USD | 1,750,000.00 USD | 779,370.00 USD | 3,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 152,940.00 USD | 172,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.50` | 429,780,000.00 USD | 429,780,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2206.70` | 282,540,000.00 USD | 282,540,000.00 USD | 146,940.00 USD | 1,570,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.10` | 280,820,000.00 USD | 280,820,000.00 USD | 104,760.00 USD | 3,130,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.70` | 423,060,000.00 USD | 423,060,000.00 USD | 0.00 USD | 0.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.50` | 277,580,000.00 USD | 277,580,000.00 USD | 247,260.00 USD | 3,350,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.90` | 413,100,000.00 USD | 413,100,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.90` | 273,980,000.00 USD | 273,980,000.00 USD | 5,830,000.00 USD | 5,040,000.00 USD | 141,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 11,070.00 USD | 19,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2216.10` | 406,110,000.00 USD | 406,110,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.30` | 262,970,000.00 USD | 262,970,000.00 USD | 522,020.00 USD | 978,580.00 USD | 68,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.70` | 261,410,000.00 USD | 261,410,000.00 USD | 7,780,000.00 USD | 1,490,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.30` | 405,620,000.00 USD | 405,620,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.10` | 247,690,000.00 USD | 247,690,000.00 USD | 876,990.00 USD | 5,240,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.50` | 379,040,000.00 USD | 379,040,000.00 USD | 815,570.00 USD | 11,530,000.00 USD | 17,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.50` | 238,110,000.00 USD | 238,110,000.00 USD | 16,610,000.00 USD | 3,630,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 8,670.00 USD | 8,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2225.70` | 349,320,000.00 USD | 349,320,000.00 USD | 9,260,000.00 USD | 15,570,000.00 USD | 21,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.90` | 209,960,000.00 USD | 209,960,000.00 USD | 10,730,000.00 USD | 2,590,000.00 USD | 8,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.30` | 187,760,000.00 USD | 187,760,000.00 USD | 23,080,000.00 USD | 16,570,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.90` | 303,160,000.00 USD | 303,160,000.00 USD | 31,720,000.00 USD | 12,750,000.00 USD | 18,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.70` | 145,890,000.00 USD | 145,890,000.00 USD | 40,470,000.00 USD | 0.00 USD | 7,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2232.10` | 240,380,000.00 USD | 240,380,000.00 USD | 30,250,000.00 USD | 45,540,000.00 USD | 29,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.10` | 97,500,000.00 USD | 97,500,000.00 USD | 14,300,000.00 USD | 6,600,000.00 USD | 20,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2235.30` | 135,220,000.00 USD | 135,220,000.00 USD | 39,990,000.00 USD | 43,730,000.00 USD | 14,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2235.50` | 55,740,000.00 USD | 55,740,000.00 USD | 15,850,000.00 USD | 0.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.90` | 19,670,000.00 USD | 19,670,000.00 USD | 8,000,000.00 USD | 0.00 USD | 4,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2238.50` | 36,840,000.00 USD | 36,840,000.00 USD | 14,060,000.00 USD | 0.00 USD | 22,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.30` | 7,220,000.00 USD | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2241.70` | 32,370,000.00 USD | 32,370,000.00 USD | 32,370,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2242.70` | 192,730.00 USD | 192,730.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2244.90` | 34,180,000.00 USD | 34,180,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2245.10` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,650,000.00 USD | 45,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.50` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 16,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2248.10` | 41,880,000.00 USD | 41,880,000.00 USD | 2,650,000.00 USD | 3,700,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2249.90` | 8,060,000.00 USD | 8,060,000.00 USD | 5,930,000.00 USD | 166,850.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2251.30` | 71,980,000.00 USD | 71,980,000.00 USD | 21,220,000.00 USD | 8,880,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.30` | 13,980,000.00 USD | 13,980,000.00 USD | 4,530,000.00 USD | 122,810.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2254.50` | 80,780,000.00 USD | 80,780,000.00 USD | 1,790,000.00 USD | 6,600,000.00 USD | 406,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2254.70` | 33,640,000.00 USD | 33,640,000.00 USD | 9,970,000.00 USD | 6,950,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 196,090.00 USD | 196,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2257.10` | 60,610,000.00 USD | 60,610,000.00 USD | 16,500,000.00 USD | 7,220,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.70` | 118,110,000.00 USD | 118,110,000.00 USD | 24,930,000.00 USD | 12,290,000.00 USD | 108,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2259.50` | 82,830,000.00 USD | 82,830,000.00 USD | 10,420,000.00 USD | 10,920,000.00 USD | 891,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.90` | 129,080,000.00 USD | 129,080,000.00 USD | 6,720,000.00 USD | 0.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2261.90` | 102,820,000.00 USD | 102,820,000.00 USD | 8,860,000.00 USD | 4,740,000.00 USD | 6,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2264.10` | 130,540,000.00 USD | 130,540,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2264.30` | 131,160,000.00 USD | 131,160,000.00 USD | 9,090,000.00 USD | 11,030,000.00 USD | 8,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 432,670.00 USD | 628,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2266.70` | 149,730,000.00 USD | 149,730,000.00 USD | 5,960,000.00 USD | 6,730,000.00 USD | 5,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2267.30` | 142,520,000.00 USD | 142,520,000.00 USD | 0.00 USD | 5,650,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2269.10` | 178,060,000.00 USD | 178,060,000.00 USD | 14,740,000.00 USD | 5,520,000.00 USD | 8,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2270.50` | 168,330,000.00 USD | 168,330,000.00 USD | 15,780,000.00 USD | 1,330,000.00 USD | 8,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2271.50` | 192,170,000.00 USD | 192,170,000.00 USD | 3,470,000.00 USD | 1,340,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2273.70` | 174,340,000.00 USD | 174,340,000.00 USD | 373,530.00 USD | 5,640,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.90` | 198,090,000.00 USD | 198,090,000.00 USD | 256,830.00 USD | 4,450,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 1,550,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.30` | 236,790,000.00 USD | 236,790,000.00 USD | 16,020,000.00 USD | 15,520,000.00 USD | 7,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2276.90` | 184,820,000.00 USD | 184,820,000.00 USD | 0.00 USD | 0.00 USD | 10,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.70` | 252,400,000.00 USD | 252,400,000.00 USD | 5,600,000.00 USD | 6,290,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.10` | 231,180,000.00 USD | 231,180,000.00 USD | 854,200.00 USD | 45,440,000.00 USD | 67,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.10` | 311,600,000.00 USD | 311,600,000.00 USD | 27,140,000.00 USD | 24,180,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.30` | 326,370,000.00 USD | 326,370,000.00 USD | 5,600,000.00 USD | 75,810,000.00 USD | 13,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2283.50` | 367,080,000.00 USD | 367,080,000.00 USD | 28,940,000.00 USD | 14,190,000.00 USD | 12,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 95,270.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.90` | 388,210,000.00 USD | 388,210,000.00 USD | 4,500,000.00 USD | 11,700,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2286.50` | 331,810,000.00 USD | 331,810,000.00 USD | 2,380,000.00 USD | 2,590,000.00 USD | 483,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.30` | 410,970,000.00 USD | 410,970,000.00 USD | 11,850,000.00 USD | 5,000,000.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.70` | 361,980,000.00 USD | 361,980,000.00 USD | 7,010,000.00 USD | 8,650,000.00 USD | 14,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.70` | 447,860,000.00 USD | 447,860,000.00 USD | 17,540,000.00 USD | 12,460,000.00 USD | 6,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.90` | 375,230,000.00 USD | 375,230,000.00 USD | 7,890,000.00 USD | 0.00 USD | 5,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.10` | 471,420,000.00 USD | 471,420,000.00 USD | 11,970,000.00 USD | 3,760,000.00 USD | 7,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 2,680,000.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.50` | 494,160,000.00 USD | 494,160,000.00 USD | 5,060,000.00 USD | 11,890,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2296.10` | 424,680,000.00 USD | 424,680,000.00 USD | 23,390,000.00 USD | 9,570,000.00 USD | 16,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.90` | 535,280,000.00 USD | 535,280,000.00 USD | 23,620,000.00 USD | 12,300,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.30` | 460,270,000.00 USD | 460,270,000.00 USD | 14,380,000.00 USD | 20,670,000.00 USD | 541,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.30` | 571,270,000.00 USD | 571,270,000.00 USD | 9,580,000.00 USD | 12,870,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 520,450,000.00 USD | 520,450,000.00 USD | 26,960,000.00 USD | 11,130,000.00 USD | 22,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.70` | 597,390,000.00 USD | 597,390,000.00 USD | 17,120,000.00 USD | 1,760,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 236,300.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.10` | 635,900,000.00 USD | 635,900,000.00 USD | 14,750,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.70` | 546,600,000.00 USD | 546,600,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.50` | 647,960,000.00 USD | 647,960,000.00 USD | 4,370,000.00 USD | 4,480,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.90` | 549,790,000.00 USD | 549,790,000.00 USD | 1,920,000.00 USD | 930,630.00 USD | 338,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2309.90` | 665,550,000.00 USD | 665,550,000.00 USD | 4,220,000.00 USD | 2,720,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.10` | 579,100,000.00 USD | 579,100,000.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 15,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.30` | 673,750,000.00 USD | 673,750,000.00 USD | 3,160,000.00 USD | 4,900,000.00 USD | 135,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2314.70` | 690,900,000.00 USD | 690,900,000.00 USD | 3,210,000.00 USD | 12,880,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,000,000.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.30` | 587,850,000.00 USD | 587,850,000.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.10` | 718,680,000.00 USD | 718,680,000.00 USD | 10,260,000.00 USD | 9,530,000.00 USD | 7,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.50` | 602,770,000.00 USD | 602,770,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2319.50` | 738,580,000.00 USD | 738,580,000.00 USD | 9,790,000.00 USD | 9,150,000.00 USD | 952,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2321.70` | 621,400,000.00 USD | 621,400,000.00 USD | 0.00 USD | 15,930,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2321.90` | 755,030,000.00 USD | 755,030,000.00 USD | 1,730,000.00 USD | 9,350,000.00 USD | 5,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2324.30` | 767,800,000.00 USD | 767,800,000.00 USD | 1,490,000.00 USD | 11,270,000.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2324.90` | 638,350,000.00 USD | 638,350,000.00 USD | 5,790,000.00 USD | 2,770,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,810,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2326.70` | 775,670,000.00 USD | 775,670,000.00 USD | 985,290.00 USD | 1,020,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.10` | 655,700,000.00 USD | 655,700,000.00 USD | 9,330,000.00 USD | 0.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.10` | 787,340,000.00 USD | 787,340,000.00 USD | 8,760,000.00 USD | 1,990,000.00 USD | 918,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.30` | 679,090,000.00 USD | 679,090,000.00 USD | 23,030,000.00 USD | 363,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.50` | 807,730,000.00 USD | 807,730,000.00 USD | 15,540,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.90` | 830,070,000.00 USD | 830,070,000.00 USD | 9,780,000.00 USD | 4,510,000.00 USD | 8,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2334.50` | 731,270,000.00 USD | 731,270,000.00 USD | 20,300,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 944,360.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2336.30` | 848,120,000.00 USD | 848,120,000.00 USD | 12,350,000.00 USD | 1,550,000.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.70` | 770,290,000.00 USD | 770,290,000.00 USD | 28,410,000.00 USD | 0.00 USD | 10,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.70` | 863,190,000.00 USD | 863,190,000.00 USD | 7,190,000.00 USD | 2,930,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.90` | 805,370,000.00 USD | 805,370,000.00 USD | 4,720,000.00 USD | 16,440,000.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.10` | 882,760,000.00 USD | 882,760,000.00 USD | 5,340,000.00 USD | 4,080,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.50` | 899,640,000.00 USD | 899,640,000.00 USD | 4,110,000.00 USD | 7,620,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.10` | 821,970,000.00 USD | 821,970,000.00 USD | 1,350,000.00 USD | 9,270,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 817,860.00 USD | 9,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.90` | 912,050,000.00 USD | 912,050,000.00 USD | 3,680,000.00 USD | 3,280,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.30` | 860,690,000.00 USD | 860,690,000.00 USD | 0.00 USD | 17,240,000.00 USD | 21,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.30` | 924,460,000.00 USD | 924,460,000.00 USD | 5,020,000.00 USD | 4,640,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.50` | 905,390,000.00 USD | 905,390,000.00 USD | 3,120,000.00 USD | 22,500,000.00 USD | 19,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.70` | 969,610,000.00 USD | 969,610,000.00 USD | 28,110,000.00 USD | 6,920,000.00 USD | 10,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.10` | 976,820,000.00 USD | 976,820,000.00 USD | 3,010,000.00 USD | 2,550,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2353.70` | 942,460,000.00 USD | 942,460,000.00 USD | 2,960,000.00 USD | 33,380,000.00 USD | 723,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,240,000.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.50` | 989,910,000.00 USD | 989,910,000.00 USD | 3,770,000.00 USD | 7,700,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2356.90` | 981,700,000.00 USD | 981,700,000.00 USD | 21,390,000.00 USD | 10,720,000.00 USD | 7,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.90` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 3,270,000.00 USD | 4,470,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.10` | 990,050,000.00 USD | 990,050,000.00 USD | 4,260,000.00 USD | 3,940,000.00 USD | 151,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.30` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 10,920,000.00 USD | 3,880,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.70` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 6,590,000.00 USD | 6,710,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 5,040,000.00 USD | 373,740.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 4,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 4,830,000.00 USD | 3,140,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2366.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 2,980,000.00 USD | 1,110,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.70` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 24,570,000.00 USD | 475,460.00 USD | 13,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2369.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 10,660,000.00 USD | 5,540,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 9,810,000.00 USD | 5,630,000.00 USD | 8,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 17,480,000.00 USD | 121,480.00 USD | 45,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.70` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 12,780,000.00 USD | 557,400.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 5,860,000.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2376.10` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 9,370,000.00 USD | 925,700.00 USD | 22,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.10` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 2,610,000.00 USD | 2,530,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 14,060,000.00 USD | 7,600,000.00 USD | 12,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2379.50` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,200,000.00 USD | 1,330,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 11,190,000.00 USD | 8,290,000.00 USD | 11,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.50` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 8,620,000.00 USD | 12,380,000.00 USD | 27,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 14,340,000.00 USD | 8,580,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 740,950.00 USD | 21,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.70` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 15,780,000.00 USD | 39,650,000.00 USD | 57,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2386.70` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 6,620,000.00 USD | 10,580,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 5,490,000.00 USD | 31,800,000.00 USD | 34,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 10,580,000.00 USD | 6,800,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 270,800.00 USD | 3,710,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 18,500,000.00 USD | 53,390,000.00 USD | 43,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 4,630,000.00 USD | 2,780,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 14,510.00 USD | 21,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2395.30` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 52,350,000.00 USD | 28,350,000.00 USD | 30,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2396.30` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 163,360.00 USD | 1,160,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.50` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 43,330,000.00 USD | 39,800,000.00 USD | 27,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.70` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 2,700,000.00 USD | 3,760,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 3,630,000.00 USD | 3,010,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.70` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 54,210,000.00 USD | 27,480,000.00 USD | 32,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.50` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 5,270,000.00 USD | 2,820,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.90` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 43,350,000.00 USD | 29,960,000.00 USD | 22,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 1,450,000.00 USD | 23,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.90` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 7,470,000.00 USD | 5,220,000.00 USD | 5,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 33,260,000.00 USD | 31,290,000.00 USD | 22,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.30` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 6,920,000.00 USD | 5,490,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.70` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 4,650,000.00 USD | 4,780,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.30` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 19,200,000.00 USD | 28,860,000.00 USD | 27,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.10` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 7,470,000.00 USD | 3,470,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 22,650,000.00 USD | 25,120,000.00 USD | 22,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 242,220.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.50` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 2,990,000.00 USD | 2,330,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.70` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 31,590,000.00 USD | 11,300,000.00 USD | 23,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.90` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 2,620,000.00 USD | 2,090,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.30` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 6,150,000.00 USD | 2,900,000.00 USD | 3,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.90` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 30,470,000.00 USD | 23,750,000.00 USD | 12,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.70` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 1,380,000.00 USD | 2,790,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.10` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 20,130,000.00 USD | 28,380,000.00 USD | 23,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 304,360.00 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.50` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 2,250,000.00 USD | 1,070,000.00 USD | 603,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2429.90` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 1,200,000.00 USD | 2,000,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.50` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 8,480,000.00 USD | 15,370,000.00 USD | 9,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.30` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,630,000.00 USD | 2,230,000.00 USD | 762,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2433.70` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 19,810,000.00 USD | 7,430,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.70` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 2,370,000.00 USD | 545,610.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 270,450.00 USD | 23,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2436.90` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 14,880,000.00 USD | 16,620,000.00 USD | 7,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,320,000.00 USD | 1,050,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2439.50` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,600,000.00 USD | 479,780.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2440.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 14,940,000.00 USD | 10,690,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.90` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 1,130,000.00 USD | 723,100.00 USD | 553,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 6,880,000.00 USD | 7,430,000.00 USD | 10,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.30` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 467,480.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 53,980,000.00 USD | 77,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2446.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 12,840,000.00 USD | 10,790,000.00 USD | 14,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2446.70` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 472,100.00 USD | 504,420.00 USD | 687,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 321,220.00 USD | 0.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 11,870,000.00 USD | 9,640,000.00 USD | 11,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.50` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 1,380,000.00 USD | 1,650,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.90` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 8,060,000.00 USD | 6,090,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 3,640,000.00 USD | 1,890,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 218,520.00 USD | 78,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2456.10` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 6,330,000.00 USD | 6,830,000.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2456.30` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 622,030.00 USD | 1,560,000.00 USD | 479,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.70` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 1,680,000.00 USD | 1,490,000.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.30` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 8,020,000.00 USD | 10,190,000.00 USD | 11,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 540,100.00 USD | 242,570.00 USD | 379,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.50` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 9,000,000.00 USD | 9,210,000.00 USD | 5,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.50` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 330,880.00 USD | 940,830.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,430,000.00 USD | 89,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2465.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 5,970,000.00 USD | 2,890,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2465.90` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 483,920.00 USD | 872,060.00 USD | 553,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.30` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 326,370.00 USD | 1,680,000.00 USD | 164,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2468.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 2,780,000.00 USD | 3,570,000.00 USD | 432,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 973,110.00 USD | 199,120.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 3,720,000.00 USD | 2,760,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.10` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 0.00 USD | 933,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 234,680.00 USD | 89,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2475.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 5,400,000.00 USD | 1,040,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2475.50` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 122,610.00 USD | 1,100,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.90` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 1,080,000.00 USD | 475,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2478.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 2,370,000.00 USD | 5,290,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.30` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 346,950.00 USD | 659,030.00 USD | 586,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 0.00 USD | 327,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.70` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,150,000.00 USD | 1,360,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 1,790,000.00 USD | 91,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2488.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,120,000.00 USD | 963,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 2,330,000.00 USD | 330,130.00 USD | 137,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 1,980,000.00 USD | 2,940,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 125,630.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.70` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 591,360.00 USD | 3,190,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.90` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 358,770.00 USD | 828,970.00 USD | 969,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2504.10` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 222,640.00 USD | 0.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,860,000.00 USD | 96,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2507.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 2,320,000.00 USD | 1,790,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 6,380,000.00 USD | 102,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.90` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,690,000.00 USD | 104,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.50` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 237,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2529.70` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 1,510,000.00 USD | 2,730,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2532.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 4,410,000.00 USD | 1,470,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 905,830.00 USD | 105,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.10` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 3,210,000.00 USD | 2,330,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 3,530,000.00 USD | 3,690,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.50` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 4,230,000.00 USD | 3,240,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,100,000.00 USD | 110,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2545.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 2,270,000.00 USD | 1,360,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2548.90` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2552.10` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 195,620.00 USD | 110,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2555.30` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 4,340,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.70` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 2,780,000.00 USD | 2,400,000.00 USD | 813,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.90` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 1,800,000.00 USD | 2,090,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 253,810.00 USD | 111,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.90` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 552,750.00 USD | 1,170,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 42,620.00 USD | 111,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,630,000.00 USD | 137,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 12,410,000.00 USD | 150,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 6,240,000.00 USD | 156,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 190,600.00 USD | 156,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 40,290,000.00 USD | 196,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 918,490.00 USD | 197,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 6,390,000.00 USD | 204,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,850,000.00 USD | 231,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 583,800.00 USD | 231,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 4,380,000.00 USD | 235,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 105,760.00 USD | 236,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 96,250.00 USD | 236,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 542,680.00 USD | 236,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 566,380.00 USD | 237,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 346,320.00 USD | 237,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 678,250.00 USD | 238,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 733,960.00 USD | 239,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 5,330,000.00 USD | 244,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 5,550,000.00 USD | 249,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 16,720,000.00 USD | 266,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 19,140.00 USD | 266,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 27,910,000.00 USD | 294,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 5,790,000.00 USD | 300,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,170,000.00 USD | 301,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 966,200.00 USD | 302,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,450,000.00 USD | 308,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 465,490.00 USD | 309,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 148,620.00 USD | 309,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 49,820.00 USD | 309,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 403,710.00 USD | 310,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 941,680.00 USD | 310,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 373,570.00 USD | 311,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 27,380,000.00 USD | 338,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 3,260,000.00 USD | 341,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 923,780.00 USD | 342,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 45,430.00 USD | 342,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 595,340.00 USD | 343,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 195,540.00 USD | 343,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 3,840,000.00 USD | 347,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 64,010.00 USD | 347,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 263,200.00 USD | 347,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 3,750,000.00 USD | 351,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 558,790.00 USD | 352,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 156,160.00 USD | 352,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 2,040,000.00 USD | 354,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 12,820,000.00 USD | 367,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 1,800,000.00 USD | 369,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 792,010.00 USD | 369,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 5,250,000.00 USD | 375,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 46,710.00 USD | 375,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 341,970.00 USD | 375,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 3,430,000.00 USD | 378,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 6,240,000.00 USD | 385,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 467,930.00 USD | 385,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 112,120.00 USD | 385,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 203,940.00 USD | 385,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 5,000,000.00 USD | 390,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 116,780.00 USD | 391,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 15,960.00 USD | 391,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 36,340,000.00 USD | 427,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 780,770.00 USD | 428,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,640,000.00 USD | 431,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 181,980.00 USD | 431,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 222,240.00 USD | 432,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 260,650.00 USD | 432,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,900,000.00 USD | 442,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 18,190,000.00 USD | 460,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 1,510,000.00 USD | 462,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 325,000.00 USD | 462,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,460,000.00 USD | 470,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 72,520.00 USD | 470,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 93,310.00 USD | 471,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 5,950,000.00 USD | 476,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 1,360,000.00 USD | 478,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 267,850.00 USD | 478,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 4,120,000.00 USD | 482,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 1,570,000.00 USD | 484,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 405,140.00 USD | 484,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 158,830.00 USD | 484,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 250,720.00 USD | 485,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 2,310,000.00 USD | 487,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 66,390.00 USD | 487,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 1,350,000.00 USD | 488,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 1,890,000.00 USD | 490,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,980,000.00 USD | 505,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 93,400.00 USD | 505,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 30,870.00 USD | 505,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 2,760,000.00 USD | 508,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 596,640.00 USD | 509,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 58,050,000.00 USD | 567,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 839,680.00 USD | 568,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 2,070,000.00 USD | 570,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 90,350.00 USD | 570,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 383,510.00 USD | 570,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 185,310.00 USD | 570,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 14,400,000.00 USD | 585,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 31,280,000.00 USD | 616,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 96,350.00 USD | 616,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 62,950.00 USD | 616,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 104,570.00 USD | 616,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 749,360.00 USD | 617,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 80,590.00 USD | 617,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 1,410.00 USD | 617,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,720,000.00 USD | 621,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 473,380.00 USD | 621,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 10,040,000.00 USD | 631,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 1,640,000.00 USD | 633,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 6,500,000.00 USD | 639,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 373,640.00 USD | 640,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 5,910.00 USD | 640,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 202,890.00 USD | 640,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 271,950.00 USD | 640,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 5,830.00 USD | 640,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 1,840,000.00 USD | 642,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 525,580.00 USD | 643,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 363,320.00 USD | 643,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 882,670.00 USD | 644,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 5,520,000.00 USD | 649,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 403,440,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 277,040.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 4,020.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 1,900,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 117,810.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 114,840.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 587,440.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 379,460.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 36,330,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 67,620.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 1,370,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 214,310.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,620,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 2,500,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 970,350.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 19,860.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 303,170.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 45,410.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 62,140,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 755,660.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 1,960,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 230,210.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 1,200,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 81,660.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 138,770.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 81,640.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 304,520.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 1,820.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 113,860.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,620,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 792,670.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 63,580.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 57,350.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 2,200,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 151,570.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 139,550.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 811,010.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 2,050.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 21,380.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 2,820,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 951,460.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 83,590,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 228,140.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,050,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 28,680,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 5,270,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 37,310.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 194,370.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 6,400.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 484,630.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 3,950,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 93,710.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 48,360.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 277,850,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 24,070.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 52,650.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 1,250,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 28,870.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 550,170.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 26,100.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 547,750.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 13,200.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 117.96 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 298,180.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 23,210.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 47,770.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 14,660.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 388,920.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 9,060.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 400,860.00 USD | 1,580,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 50,360.00 USD | 1,590,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 339,770.00 USD | 1,590,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 759,590,000.00 USD | 0.00 USD | 110,170.00 USD | `-79.73%` | `242.13` |
| `Live` | `Long` | `465.00` | 759,480,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-79.28%` | `3,633.80` |
| `Live` | `Long` | `475.00` | 757,790,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-78.84%` | `3,014.06` |
| `Live` | `Long` | `485.00` | 756,350,000.00 USD | 0.00 USD | 175,090.00 USD | `-78.39%` | `361.01` |
| `Live` | `Long` | `495.00` | 756,180,000.00 USD | 0.00 USD | 15,890.00 USD | `-77.95%` | `32.11` |
| `Live` | `Long` | `505.00` | 756,160,000.00 USD | 0.00 USD | 50,760.00 USD | `-77.50%` | `100.51` |
| `Live` | `Long` | `515.00` | 756,110,000.00 USD | 0.00 USD | 4,970.00 USD | `-77.05%` | `9.65` |
| `Live` | `Long` | `525.00` | 756,110,000.00 USD | 0.00 USD | 23,410.00 USD | `-76.61%` | `44.60` |
| `Live` | `Long` | `535.00` | 756,080,000.00 USD | 0.00 USD | 8,530.00 USD | `-76.16%` | `15.94` |
| `Live` | `Long` | `545.00` | 756,080,000.00 USD | 0.00 USD | 170,330.00 USD | `-75.72%` | `312.54` |
| `Live` | `Long` | `555.00` | 755,910,000.00 USD | 0.00 USD | 39,640.00 USD | `-75.27%` | `71.43` |
| `Live` | `Long` | `565.00` | 755,870,000.00 USD | 0.00 USD | 924,020.00 USD | `-74.83%` | `1,635.44` |
| `Live` | `Long` | `575.00` | 754,940,000.00 USD | 0.00 USD | 2,870,000.00 USD | `-74.38%` | `4,998.97` |
| `Live` | `Long` | `585.00` | 752,070,000.00 USD | 0.00 USD | 53,900.00 USD | `-73.94%` | `92.14` |
| `Live` | `Long` | `595.00` | 752,010,000.00 USD | 0.00 USD | 459,960.00 USD | `-73.49%` | `773.04` |
| `Live` | `Long` | `605.00` | 751,550,000.00 USD | 0.00 USD | 21,160.00 USD | `-73.04%` | `34.98` |
| `Live` | `Long` | `615.00` | 751,530,000.00 USD | 0.00 USD | 129,260.00 USD | `-72.60%` | `210.18` |
| `Live` | `Long` | `625.00` | 751,400,000.00 USD | 0.00 USD | 22,970.00 USD | `-72.15%` | `36.75` |
| `Live` | `Long` | `635.00` | 751,380,000.00 USD | 0.00 USD | 590.55 USD | `-71.71%` | `0.93` |
| `Live` | `Long` | `645.00` | 751,380,000.00 USD | 0.00 USD | 193,580.00 USD | `-71.26%` | `300.12` |
| `Live` | `Long` | `655.00` | 751,190,000.00 USD | 0.00 USD | 67,600.00 USD | `-70.82%` | `103.20` |
| `Live` | `Long` | `665.00` | 751,120,000.00 USD | 0.00 USD | 73,910.00 USD | `-70.37%` | `111.14` |
| `Live` | `Long` | `675.00` | 751,050,000.00 USD | 0.00 USD | 27,470.00 USD | `-69.93%` | `40.70` |
| `Live` | `Long` | `685.00` | 751,020,000.00 USD | 0.00 USD | 163,870.00 USD | `-69.48%` | `239.22` |
| `Live` | `Long` | `695.00` | 750,850,000.00 USD | 0.00 USD | 35,390.00 USD | `-69.03%` | `50.92` |
| `Live` | `Long` | `705.00` | 750,820,000.00 USD | 0.00 USD | 27,860.00 USD | `-68.59%` | `39.52` |
| `Live` | `Long` | `715.00` | 750,790,000.00 USD | 0.00 USD | 1,580.00 USD | `-68.14%` | `2.20` |
| `Live` | `Long` | `725.00` | 750,790,000.00 USD | 0.00 USD | 433,130.00 USD | `-67.70%` | `597.42` |
| `Live` | `Long` | `735.00` | 750,360,000.00 USD | 0.00 USD | 61,900.00 USD | `-67.25%` | `84.21` |
| `Live` | `Long` | `745.00` | 750,290,000.00 USD | 0.00 USD | 76,030.00 USD | `-66.81%` | `102.05` |
| `Live` | `Long` | `755.00` | 750,220,000.00 USD | 0.00 USD | 38,370.00 USD | `-66.36%` | `50.82` |
| `Live` | `Long` | `765.00` | 750,180,000.00 USD | 0.00 USD | 50,490.00 USD | `-65.92%` | `66.00` |
| `Live` | `Long` | `775.00` | 750,130,000.00 USD | 0.00 USD | 65,760.00 USD | `-65.47%` | `84.85` |
| `Live` | `Long` | `785.00` | 750,060,000.00 USD | 0.00 USD | 94,180.00 USD | `-65.02%` | `119.97` |
| `Live` | `Long` | `795.00` | 749,970,000.00 USD | 0.00 USD | 59,650.00 USD | `-64.58%` | `75.04` |
| `Live` | `Long` | `805.00` | 749,910,000.00 USD | 0.00 USD | 147,660.00 USD | `-64.13%` | `183.43` |
| `Live` | `Long` | `815.00` | 749,760,000.00 USD | 0.00 USD | 137,500.00 USD | `-63.69%` | `168.71` |
| `Live` | `Long` | `825.00` | 749,620,000.00 USD | 0.00 USD | 344,930.00 USD | `-63.24%` | `418.10` |
| `Live` | `Long` | `835.00` | 749,280,000.00 USD | 0.00 USD | 54,230.00 USD | `-62.80%` | `64.94` |
| `Live` | `Long` | `845.00` | 749,230,000.00 USD | 0.00 USD | 893,380.00 USD | `-62.35%` | `1,057.25` |
| `Live` | `Long` | `855.00` | 748,330,000.00 USD | 0.00 USD | 53,780.00 USD | `-61.91%` | `62.90` |
| `Live` | `Long` | `865.00` | 748,280,000.00 USD | 0.00 USD | 635,970.00 USD | `-61.46%` | `735.22` |
| `Live` | `Long` | `875.00` | 747,640,000.00 USD | 0.00 USD | 492,740.00 USD | `-61.01%` | `563.13` |
| `Live` | `Long` | `885.00` | 747,150,000.00 USD | 0.00 USD | 972,570.00 USD | `-60.57%` | `1,098.95` |
| `Live` | `Long` | `895.00` | 746,180,000.00 USD | 0.00 USD | 223,800.00 USD | `-60.12%` | `250.05` |
| `Live` | `Long` | `905.00` | 745,950,000.00 USD | 0.00 USD | 131,270.00 USD | `-59.68%` | `145.05` |
| `Live` | `Long` | `915.00` | 745,820,000.00 USD | 0.00 USD | 180,390.00 USD | `-59.23%` | `197.15` |
| `Live` | `Long` | `925.00` | 745,640,000.00 USD | 0.00 USD | 207,340.00 USD | `-58.79%` | `224.15` |
| `Live` | `Long` | `935.00` | 745,430,000.00 USD | 0.00 USD | 49,510.00 USD | `-58.34%` | `52.95` |
| `Live` | `Long` | `945.00` | 745,380,000.00 USD | 0.00 USD | 57,540.00 USD | `-57.90%` | `60.89` |
| `Live` | `Long` | `955.00` | 745,330,000.00 USD | 0.00 USD | 211,110.00 USD | `-57.45%` | `221.06` |
| `Live` | `Long` | `965.00` | 745,120,000.00 USD | 0.00 USD | 321,380.00 USD | `-57.00%` | `333.03` |
| `Live` | `Long` | `975.00` | 744,790,000.00 USD | 0.00 USD | 242,680.00 USD | `-56.56%` | `248.90` |
| `Live` | `Long` | `985.00` | 744,550,000.00 USD | 0.00 USD | 202,990.00 USD | `-56.11%` | `206.09` |
| `Live` | `Long` | `995.00` | 744,350,000.00 USD | 0.00 USD | 17,760.00 USD | `-55.67%` | `17.85` |
| `Live` | `Long` | `1005.00` | 744,330,000.00 USD | 0.00 USD | 452,000.00 USD | `-55.22%` | `449.75` |
| `Live` | `Long` | `1015.00` | 743,880,000.00 USD | 0.00 USD | 200,320.00 USD | `-54.78%` | `197.36` |
| `Live` | `Long` | `1025.00` | 743,680,000.00 USD | 0.00 USD | 360,290.00 USD | `-54.33%` | `351.51` |
| `Live` | `Long` | `1035.00` | 743,320,000.00 USD | 0.00 USD | 23,860.00 USD | `-53.89%` | `23.05` |
| `Live` | `Long` | `1045.00` | 743,290,000.00 USD | 0.00 USD | 1,000,000.00 USD | `-53.44%` | `960.01` |
| `Live` | `Long` | `1055.00` | 742,290,000.00 USD | 0.00 USD | 8,920,000.00 USD | `-52.99%` | `8,453.79` |
| `Live` | `Long` | `1065.00` | 733,370,000.00 USD | 0.00 USD | 331,680.00 USD | `-52.55%` | `311.44` |
| `Live` | `Long` | `1075.00` | 733,040,000.00 USD | 0.00 USD | 656,510.00 USD | `-52.10%` | `610.71` |
| `Live` | `Long` | `1085.00` | 732,380,000.00 USD | 0.00 USD | 370,330.00 USD | `-51.66%` | `341.32` |
| `Live` | `Long` | `1095.00` | 732,010,000.00 USD | 0.00 USD | 71,160.00 USD | `-51.21%` | `64.98` |
| `Live` | `Long` | `1105.00` | 731,940,000.00 USD | 0.00 USD | 151,030.00 USD | `-50.77%` | `136.68` |
| `Live` | `Long` | `1115.00` | 731,790,000.00 USD | 0.00 USD | 7,660,000.00 USD | `-50.32%` | `6,868.93` |
| `Live` | `Long` | `1125.00` | 724,130,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-49.88%` | `1,130.28` |
| `Live` | `Long` | `1135.00` | 722,860,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-49.43%` | `1,309.73` |
| `Live` | `Long` | `1145.00` | 721,370,000.00 USD | 0.00 USD | 767,090.00 USD | `-48.98%` | `669.95` |
| `Live` | `Long` | `1155.00` | 720,610,000.00 USD | 0.00 USD | 542,570.00 USD | `-48.54%` | `469.76` |
| `Live` | `Long` | `1165.00` | 720,070,000.00 USD | 0.00 USD | 22,160.00 USD | `-48.09%` | `19.02` |
| `Live` | `Long` | `1175.00` | 720,040,000.00 USD | 0.00 USD | 287,780.00 USD | `-47.65%` | `244.92` |
| `Live` | `Long` | `1185.00` | 719,760,000.00 USD | 0.00 USD | 3,950,000.00 USD | `-47.20%` | `3,332.08` |
| `Live` | `Long` | `1195.00` | 715,810,000.00 USD | 0.00 USD | 343,160.00 USD | `-46.76%` | `287.17` |
| `Live` | `Long` | `1205.00` | 715,460,000.00 USD | 0.00 USD | 737,430.00 USD | `-46.31%` | `611.98` |
| `Live` | `Long` | `1215.00` | 714,730,000.00 USD | 0.00 USD | 128,250.00 USD | `-45.87%` | `105.56` |
| `Live` | `Long` | `1225.00` | 714,600,000.00 USD | 0.00 USD | 8,140,000.00 USD | `-45.42%` | `6,645.00` |
| `Live` | `Long` | `1235.00` | 706,460,000.00 USD | 0.00 USD | 797,860.00 USD | `-44.97%` | `646.04` |
| `Live` | `Long` | `1245.00` | 705,660,000.00 USD | 0.00 USD | 137,210.00 USD | `-44.53%` | `110.21` |
| `Live` | `Long` | `1255.00` | 705,520,000.00 USD | 0.00 USD | 405,660.00 USD | `-44.08%` | `323.23` |
| `Live` | `Long` | `1265.00` | 705,120,000.00 USD | 0.00 USD | 159,410.00 USD | `-43.64%` | `126.01` |
| `Live` | `Long` | `1275.00` | 704,960,000.00 USD | 0.00 USD | 15,430,000.00 USD | `-43.19%` | `12,098.05` |
| `Live` | `Long` | `1285.00` | 689,530,000.00 USD | 0.00 USD | 273,630.00 USD | `-42.75%` | `212.94` |
| `Live` | `Long` | `1295.00` | 689,260,000.00 USD | 0.00 USD | 453,230.00 USD | `-42.30%` | `349.99` |
| `Live` | `Long` | `1305.00` | 688,810,000.00 USD | 0.00 USD | 424,160.00 USD | `-41.86%` | `325.03` |
| `Live` | `Long` | `1315.00` | 688,380,000.00 USD | 0.00 USD | 189,440.00 USD | `-41.41%` | `144.06` |
| `Live` | `Long` | `1325.00` | 688,190,000.00 USD | 0.00 USD | 494,710.00 USD | `-40.96%` | `373.36` |
| `Live` | `Long` | `1335.00` | 687,700,000.00 USD | 0.00 USD | 6,890,000.00 USD | `-40.52%` | `5,161.20` |
| `Live` | `Long` | `1345.00` | 680,810,000.00 USD | 0.00 USD | 12,240,000.00 USD | `-40.07%` | `9,098.67` |
| `Live` | `Long` | `1355.00` | 668,570,000.00 USD | 0.00 USD | 53,710.00 USD | `-39.63%` | `39.64` |
| `Live` | `Long` | `1365.00` | 668,520,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-39.18%` | `900.67` |
| `Live` | `Long` | `1375.00` | 667,290,000.00 USD | 0.00 USD | 7,670,000.00 USD | `-38.74%` | `5,577.73` |
| `Live` | `Long` | `1385.00` | 659,620,000.00 USD | 0.00 USD | 2,390,000.00 USD | `-38.29%` | `1,722.76` |
| `Live` | `Long` | `1395.00` | 657,230,000.00 USD | 0.00 USD | 405,620.00 USD | `-37.85%` | `290.77` |
| `Live` | `Long` | `1405.00` | 656,830,000.00 USD | 0.00 USD | 10,120,000.00 USD | `-37.40%` | `7,201.45` |
| `Live` | `Long` | `1415.00` | 646,710,000.00 USD | 0.00 USD | 167,710.00 USD | `-36.95%` | `118.52` |
| `Live` | `Long` | `1425.00` | 646,540,000.00 USD | 0.00 USD | 708,070.00 USD | `-36.51%` | `496.89` |
| `Live` | `Long` | `1435.00` | 645,830,000.00 USD | 0.00 USD | 19,400,000.00 USD | `-36.06%` | `13,519.19` |
| `Live` | `Long` | `1445.00` | 626,430,000.00 USD | 0.00 USD | 325,300.00 USD | `-35.62%` | `225.12` |
| `Live` | `Long` | `1455.00` | 626,110,000.00 USD | 0.00 USD | 999,940.00 USD | `-35.17%` | `687.24` |
| `Live` | `Long` | `1465.00` | 625,110,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-34.73%` | `1,286.17` |
| `Live` | `Long` | `1475.00` | 623,220,000.00 USD | 0.00 USD | 12,290,000.00 USD | `-34.28%` | `8,330.13` |
| `Live` | `Long` | `1485.00` | 610,930,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-33.84%` | `1,263.09` |
| `Live` | `Long` | `1495.00` | 609,060,000.00 USD | 0.00 USD | 319,620.00 USD | `-33.39%` | `213.79` |
| `Live` | `Long` | `1505.00` | 608,740,000.00 USD | 0.00 USD | 374,890.00 USD | `-32.94%` | `249.10` |
| `Live` | `Long` | `1515.00` | 608,360,000.00 USD | 0.00 USD | 543,600.00 USD | `-32.50%` | `358.81` |
| `Live` | `Long` | `1525.00` | 607,820,000.00 USD | 0.00 USD | 33,880,000.00 USD | `-32.05%` | `22,216.26` |
| `Live` | `Long` | `1535.00` | 573,940,000.00 USD | 0.00 USD | 879,130.00 USD | `-31.61%` | `572.72` |
| `Live` | `Long` | `1545.00` | 573,060,000.00 USD | 0.00 USD | 3,480,000.00 USD | `-31.16%` | `2,254.48` |
| `Live` | `Long` | `1555.00` | 569,580,000.00 USD | 0.00 USD | 323,910.00 USD | `-30.72%` | `208.30` |
| `Live` | `Long` | `1565.00` | 569,260,000.00 USD | 0.00 USD | 2,760,000.00 USD | `-30.27%` | `1,764.14` |
| `Live` | `Long` | `1575.00` | 566,490,000.00 USD | 0.00 USD | 949,950.00 USD | `-29.83%` | `603.14` |
| `Live` | `Long` | `1585.00` | 565,540,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-29.38%` | `1,560.56` |
| `Live` | `Long` | `1595.00` | 563,070,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-28.93%` | `1,134.07` |
| `Live` | `Long` | `1605.00` | 561,260,000.00 USD | 0.00 USD | 18,110,000.00 USD | `-28.49%` | `11,284.43` |
| `Live` | `Long` | `1615.00` | 543,150,000.00 USD | 0.00 USD | 850,040.00 USD | `-28.04%` | `526.34` |
| `Live` | `Long` | `1625.00` | 542,300,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-27.60%` | `1,174.63` |
| `Live` | `Long` | `1635.00` | 540,390,000.00 USD | 0.00 USD | 18,900,000.00 USD | `-27.15%` | `11,556.77` |
| `Live` | `Long` | `1645.00` | 521,500,000.00 USD | 0.00 USD | 36,650,000.00 USD | `-26.71%` | `22,276.64` |
| `Live` | `Long` | `1655.00` | 484,850,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-26.26%` | `828.93` |
| `Live` | `Long` | `1665.00` | 483,480,000.00 USD | 0.00 USD | 11,830,000.00 USD | `-25.82%` | `7,104.30` |
| `Live` | `Long` | `1675.00` | 471,650,000.00 USD | 0.00 USD | 754,140.00 USD | `-25.37%` | `450.23` |
| `Live` | `Long` | `1685.00` | 470,900,000.00 USD | 0.00 USD | 4,680,000.00 USD | `-24.92%` | `2,779.00` |
| `Live` | `Long` | `1695.00` | 466,210,000.00 USD | 0.00 USD | 354,260.00 USD | `-24.48%` | `209.00` |
| `Live` | `Long` | `1705.00` | 465,860,000.00 USD | 0.00 USD | 1,220,000.00 USD | `-24.03%` | `715.25` |
| `Live` | `Long` | `1715.00` | 464,640,000.00 USD | 0.00 USD | 757,730.00 USD | `-23.59%` | `441.83` |
| `Live` | `Long` | `1725.00` | 463,880,000.00 USD | 0.00 USD | 37,730,000.00 USD | `-23.14%` | `21,874.58` |
| `Live` | `Long` | `1735.00` | 426,150,000.00 USD | 0.00 USD | 606,210.00 USD | `-22.70%` | `349.40` |
| `Live` | `Long` | `1745.00` | 425,540,000.00 USD | 0.00 USD | 28,750,000.00 USD | `-22.25%` | `16,477.75` |
| `Live` | `Long` | `1755.00` | 396,790,000.00 USD | 0.00 USD | 10,030,000.00 USD | `-21.81%` | `5,714.67` |
| `Live` | `Long` | `1765.00` | 386,760,000.00 USD | 0.00 USD | 675,970.00 USD | `-21.36%` | `382.99` |
| `Live` | `Long` | `1775.00` | 386,080,000.00 USD | 0.00 USD | 3,900,000.00 USD | `-20.91%` | `2,199.72` |
| `Live` | `Long` | `1785.00` | 382,180,000.00 USD | 0.00 USD | 56,040,000.00 USD | `-20.47%` | `31,393.11` |
| `Live` | `Long` | `1795.00` | 326,140,000.00 USD | 0.00 USD | 18,460,000.00 USD | `-20.02%` | `10,284.29` |
| `Live` | `Long` | `1805.00` | 307,680,000.00 USD | 0.00 USD | 4,320,000.00 USD | `-19.58%` | `2,396.03` |
| `Live` | `Long` | `1815.00` | 303,360,000.00 USD | 0.00 USD | 12,040,000.00 USD | `-19.13%` | `6,633.27` |
| `Live` | `Long` | `1825.00` | 291,320,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-18.69%` | `837.74` |
| `Live` | `Long` | `1835.00` | 289,790,000.00 USD | 0.00 USD | 941,830.00 USD | `-18.24%` | `513.26` |
| `Live` | `Long` | `1845.00` | 288,850,000.00 USD | 0.00 USD | 16,830,000.00 USD | `-17.80%` | `9,121.32` |
| `Live` | `Long` | `1855.00` | 272,020,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-17.35%` | `679.15` |
| `Live` | `Long` | `1865.00` | 270,760,000.00 USD | 0.00 USD | 2,730,000.00 USD | `-16.90%` | `1,465.10` |
| `Live` | `Long` | `1875.00` | 268,030,000.00 USD | 0.00 USD | 5,700,000.00 USD | `-16.46%` | `3,039.02` |
| `Live` | `Long` | `1885.00` | 262,330,000.00 USD | 0.00 USD | 4,940,000.00 USD | `-16.01%` | `2,622.82` |
| `Live` | `Long` | `1895.00` | 257,380,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-15.57%` | `582.68` |
| `Live` | `Long` | `1905.00` | 256,280,000.00 USD | 0.00 USD | 403,940.00 USD | `-15.12%` | `212.04` |
| `Live` | `Long` | `1915.00` | 255,880,000.00 USD | 0.00 USD | 18,040,000.00 USD | `-14.68%` | `9,420.95` |
| `Live` | `Long` | `1925.00` | 237,830,000.00 USD | 0.00 USD | 16,740,000.00 USD | `-14.23%` | `8,698.60` |
| `Live` | `Long` | `1935.00` | 221,090,000.00 USD | 0.00 USD | 827,870.00 USD | `-13.79%` | `427.84` |
| `Live` | `Long` | `1945.00` | 220,260,000.00 USD | 0.00 USD | 5,110,000.00 USD | `-13.34%` | `2,629.76` |
| `Live` | `Long` | `1955.00` | 215,150,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-12.89%` | `878.23` |
| `Live` | `Long` | `1965.00` | 213,430,000.00 USD | 0.00 USD | 3,200,000.00 USD | `-12.45%` | `1,626.74` |
| `Live` | `Long` | `1975.00` | 210,230,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-12.00%` | `762.96` |
| `Live` | `Long` | `1985.00` | 208,730,000.00 USD | 0.00 USD | 4,860,000.00 USD | `-11.56%` | `2,448.96` |
| `Live` | `Long` | `1995.00` | 203,870,000.00 USD | 0.00 USD | 1,500,000.00 USD | `-11.11%` | `752.75` |
| `Live` | `Long` | `2005.00` | 202,360,000.00 USD | 0.00 USD | 2,170,000.00 USD | `-10.67%` | `1,082.60` |
| `Live` | `Long` | `2015.00` | 200,190,000.00 USD | 0.00 USD | 2,740,000.00 USD | `-10.22%` | `1,360.99` |
| `Live` | `Long` | `2025.00` | 197,450,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-9.78%` | `954.15` |
| `Live` | `Long` | `2035.00` | 195,520,000.00 USD | 0.00 USD | 519,090.00 USD | `-9.33%` | `255.08` |
| `Live` | `Long` | `2045.00` | 195,000,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-8.88%` | `921.49` |
| `Live` | `Long` | `2055.00` | 193,120,000.00 USD | 0.00 USD | 6,680,000.00 USD | `-8.44%` | `3,249.75` |
| `Live` | `Long` | `2065.00` | 186,440,000.00 USD | 0.00 USD | 14,080,000.00 USD | `-7.99%` | `6,816.31` |
| `Live` | `Long` | `2075.00` | 172,360,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-7.55%` | `796.40` |
| `Live` | `Long` | `2085.00` | 170,710,000.00 USD | 0.00 USD | 12,760,000.00 USD | `-7.10%` | `6,118.32` |
| `Live` | `Long` | `2095.00` | 157,950,000.00 USD | 0.00 USD | 2,850,000.00 USD | `-6.66%` | `1,361.33` |
| `Live` | `Long` | `2105.00` | 155,100,000.00 USD | 0.00 USD | 2,330,000.00 USD | `-6.21%` | `1,109.05` |
| `Live` | `Long` | `2115.00` | 152,770,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-5.77%` | `850.08` |
| `Live` | `Long` | `2125.00` | 150,970,000.00 USD | 0.00 USD | 123,380,000.00 USD | `-5.32%` | `58,059.01` |
| `Live` | `Long` | `2135.00` | 27,590,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-4.87%` | `1,052.30` |
| `Live` | `Long` | `2145.00` | 25,350,000.00 USD | 0.00 USD | 4,680,000.00 USD | `-4.43%` | `2,182.68` |
| `Live` | `Long` | `2155.00` | 20,660,000.00 USD | 0.00 USD | 3,580,000.00 USD | `-3.98%` | `1,659.17` |
| `Live` | `Long` | `2165.00` | 17,090,000.00 USD | 0.00 USD | 5,760,000.00 USD | `-3.54%` | `2,662.61` |
| `Live` | `Long` | `2175.00` | 11,320,000.00 USD | 0.00 USD | 10,540,000.00 USD | `-3.09%` | `4,846.80` |
| `Live` | `Long` | `2185.00` | 782,030.00 USD | 0.00 USD | 462,620.00 USD | `-2.65%` | `211.72` |
| `Live` | `Long` | `2195.00` | 319,410.00 USD | 0.00 USD | 146,720.00 USD | `-2.20%` | `66.84` |
| `Live` | `Long` | `2205.00` | 172,690.00 USD | 0.00 USD | 152,940.00 USD | `-1.76%` | `69.36` |
| `Live` | `Long` | `2215.00` | 19,750.00 USD | 0.00 USD | 11,070.00 USD | `-1.31%` | `5.00` |
| `Live` | `Long` | `2225.00` | 8,670.00 USD | 0.00 USD | 8,670.00 USD | `-0.86%` | `3.90` |
| `Live` | `Short` | `2255.00` | 196,090.00 USD | 196,090.00 USD | 0.00 USD | `+0.47%` | `86.96` |
| `Live` | `Short` | `2265.00` | 628,760.00 USD | 432,670.00 USD | 0.00 USD | `+0.92%` | `191.02` |
| `Live` | `Short` | `2275.00` | 2,180,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+1.36%` | `682.27` |
| `Live` | `Short` | `2285.00` | 2,280,000.00 USD | 95,270.00 USD | 0.00 USD | `+1.81%` | `41.69` |
| `Live` | `Short` | `2295.00` | 4,960,000.00 USD | 2,680,000.00 USD | 0.00 USD | `+2.25%` | `1,167.25` |
| `Live` | `Short` | `2305.00` | 5,190,000.00 USD | 236,300.00 USD | 0.00 USD | `+2.70%` | `102.52` |
| `Live` | `Short` | `2315.00` | 6,190,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+3.15%` | `432.01` |
| `Live` | `Short` | `2325.00` | 8,000,000.00 USD | 1,810,000.00 USD | 0.00 USD | `+3.59%` | `778.18` |
| `Live` | `Short` | `2335.00` | 8,950,000.00 USD | 944,360.00 USD | 0.00 USD | `+4.04%` | `404.44` |
| `Live` | `Short` | `2345.00` | 9,760,000.00 USD | 817,860.00 USD | 0.00 USD | `+4.48%` | `348.77` |
| `Live` | `Short` | `2355.00` | 11,010,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+4.93%` | `528.64` |
| `Live` | `Short` | `2365.00` | 15,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | `+5.37%` | `1,689.41` |
| `Live` | `Short` | `2375.00` | 20,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | `+5.82%` | `2,466.72` |
| `Live` | `Short` | `2385.00` | 21,600,000.00 USD | 740,950.00 USD | 0.00 USD | `+6.26%` | `310.67` |
| `Live` | `Short` | `2395.00` | 21,620,000.00 USD | 14,510.00 USD | 0.00 USD | `+6.71%` | `6.06` |
| `Live` | `Short` | `2405.00` | 23,070,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+7.16%` | `603.44` |
| `Live` | `Short` | `2415.00` | 23,310,000.00 USD | 242,220.00 USD | 0.00 USD | `+7.60%` | `100.30` |
| `Live` | `Short` | `2425.00` | 23,620,000.00 USD | 304,360.00 USD | 0.00 USD | `+8.05%` | `125.51` |
| `Live` | `Short` | `2435.00` | 23,890,000.00 USD | 270,450.00 USD | 0.00 USD | `+8.49%` | `111.07` |
| `Live` | `Short` | `2445.00` | 77,870,000.00 USD | 53,980,000.00 USD | 0.00 USD | `+8.94%` | `22,078.52` |
| `Live` | `Short` | `2455.00` | 78,090,000.00 USD | 218,520.00 USD | 0.00 USD | `+9.38%` | `89.01` |
| `Live` | `Short` | `2465.00` | 89,520,000.00 USD | 11,430,000.00 USD | 0.00 USD | `+9.83%` | `4,637.35` |
| `Live` | `Short` | `2475.00` | 89,750,000.00 USD | 234,680.00 USD | 0.00 USD | `+10.27%` | `94.82` |
| `Live` | `Short` | `2485.00` | 91,550,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+10.72%` | `722.29` |
| `Live` | `Short` | `2495.00` | 91,670,000.00 USD | 125,630.00 USD | 0.00 USD | `+11.17%` | `50.35` |
| `Live` | `Short` | `2505.00` | 96,530,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+11.61%` | `1,940.35` |
| `Live` | `Short` | `2515.00` | 102,920,000.00 USD | 6,380,000.00 USD | 0.00 USD | `+12.06%` | `2,537.62` |
| `Live` | `Short` | `2525.00` | 104,610,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+12.50%` | `669.60` |
| `Live` | `Short` | `2535.00` | 105,510,000.00 USD | 905,830.00 USD | 0.00 USD | `+12.95%` | `357.33` |
| `Live` | `Short` | `2545.00` | 110,610,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+13.39%` | `2,004.82` |
| `Live` | `Short` | `2555.00` | 110,810,000.00 USD | 195,620.00 USD | 0.00 USD | `+13.84%` | `76.56` |
| `Live` | `Short` | `2565.00` | 111,060,000.00 USD | 253,810.00 USD | 0.00 USD | `+14.28%` | `98.95` |
| `Live` | `Short` | `2575.00` | 111,110,000.00 USD | 42,620.00 USD | 0.00 USD | `+14.73%` | `16.55` |
| `Live` | `Short` | `2585.00` | 137,740,000.00 USD | 26,630,000.00 USD | 0.00 USD | `+15.18%` | `10,301.86` |
| `Live` | `Short` | `2595.00` | 150,150,000.00 USD | 12,410,000.00 USD | 0.00 USD | `+15.62%` | `4,781.84` |
| `Live` | `Short` | `2605.00` | 156,380,000.00 USD | 6,240,000.00 USD | 0.00 USD | `+16.07%` | `2,393.66` |
| `Live` | `Short` | `2615.00` | 156,570,000.00 USD | 190,600.00 USD | 0.00 USD | `+16.51%` | `72.89` |
| `Live` | `Short` | `2625.00` | 196,860,000.00 USD | 40,290,000.00 USD | 0.00 USD | `+16.96%` | `15,346.85` |
| `Live` | `Short` | `2635.00` | 197,780,000.00 USD | 918,490.00 USD | 0.00 USD | `+17.40%` | `348.57` |
| `Live` | `Short` | `2645.00` | 204,170,000.00 USD | 6,390,000.00 USD | 0.00 USD | `+17.85%` | `2,416.57` |
| `Live` | `Short` | `2655.00` | 231,020,000.00 USD | 26,850,000.00 USD | 0.00 USD | `+18.29%` | `10,113.21` |
| `Live` | `Short` | `2665.00` | 231,600,000.00 USD | 583,800.00 USD | 0.00 USD | `+18.74%` | `219.06` |
| `Live` | `Short` | `2675.00` | 235,980,000.00 USD | 4,380,000.00 USD | 0.00 USD | `+19.19%` | `1,638.58` |
| `Live` | `Short` | `2685.00` | 236,090,000.00 USD | 105,760.00 USD | 0.00 USD | `+19.63%` | `39.39` |
| `Live` | `Short` | `2695.00` | 236,190,000.00 USD | 96,250.00 USD | 0.00 USD | `+20.08%` | `35.72` |
| `Live` | `Short` | `2705.00` | 236,730,000.00 USD | 542,680.00 USD | 0.00 USD | `+20.52%` | `200.62` |
| `Live` | `Short` | `2715.00` | 237,300,000.00 USD | 566,380.00 USD | 0.00 USD | `+20.97%` | `208.61` |
| `Live` | `Short` | `2725.00` | 237,640,000.00 USD | 346,320.00 USD | 0.00 USD | `+21.41%` | `127.09` |
| `Live` | `Short` | `2735.00` | 238,320,000.00 USD | 678,250.00 USD | 0.00 USD | `+21.86%` | `247.99` |
| `Live` | `Short` | `2745.00` | 239,050,000.00 USD | 733,960.00 USD | 0.00 USD | `+22.30%` | `267.38` |
| `Live` | `Short` | `2755.00` | 244,380,000.00 USD | 5,330,000.00 USD | 0.00 USD | `+22.75%` | `1,933.87` |
| `Live` | `Short` | `2765.00` | 249,930,000.00 USD | 5,550,000.00 USD | 0.00 USD | `+23.20%` | `2,005.47` |
| `Live` | `Short` | `2775.00` | 266,640,000.00 USD | 16,720,000.00 USD | 0.00 USD | `+23.64%` | `6,023.51` |
| `Live` | `Short` | `2785.00` | 266,660,000.00 USD | 19,140.00 USD | 0.00 USD | `+24.09%` | `6.87` |
| `Live` | `Short` | `2795.00` | 294,570,000.00 USD | 27,910,000.00 USD | 0.00 USD | `+24.53%` | `9,985.98` |
| `Live` | `Short` | `2805.00` | 300,370,000.00 USD | 5,790,000.00 USD | 0.00 USD | `+24.98%` | `2,065.42` |
| `Live` | `Short` | `2815.00` | 301,530,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+25.42%` | `414.54` |
| `Live` | `Short` | `2825.00` | 302,500,000.00 USD | 966,200.00 USD | 0.00 USD | `+25.87%` | `342.02` |
| `Live` | `Short` | `2835.00` | 308,950,000.00 USD | 6,450,000.00 USD | 0.00 USD | `+26.31%` | `2,275.31` |
| `Live` | `Short` | `2845.00` | 309,410,000.00 USD | 465,490.00 USD | 0.00 USD | `+26.76%` | `163.62` |
| `Live` | `Short` | `2855.00` | 309,560,000.00 USD | 148,620.00 USD | 0.00 USD | `+27.21%` | `52.06` |
| `Live` | `Short` | `2865.00` | 309,610,000.00 USD | 49,820.00 USD | 0.00 USD | `+27.65%` | `17.39` |
| `Live` | `Short` | `2875.00` | 310,020,000.00 USD | 403,710.00 USD | 0.00 USD | `+28.10%` | `140.42` |
| `Live` | `Short` | `2885.00` | 310,960,000.00 USD | 941,680.00 USD | 0.00 USD | `+28.54%` | `326.41` |
| `Live` | `Short` | `2895.00` | 311,330,000.00 USD | 373,570.00 USD | 0.00 USD | `+28.99%` | `129.04` |
| `Live` | `Short` | `2905.00` | 338,710,000.00 USD | 27,380,000.00 USD | 0.00 USD | `+29.43%` | `9,425.03` |
| `Live` | `Short` | `2915.00` | 341,970,000.00 USD | 3,260,000.00 USD | 0.00 USD | `+29.88%` | `1,117.46` |
| `Live` | `Short` | `2925.00` | 342,890,000.00 USD | 923,780.00 USD | 0.00 USD | `+30.32%` | `315.82` |
| `Live` | `Short` | `2935.00` | 342,940,000.00 USD | 45,430.00 USD | 0.00 USD | `+30.77%` | `15.48` |
| `Live` | `Short` | `2945.00` | 343,530,000.00 USD | 595,340.00 USD | 0.00 USD | `+31.22%` | `202.15` |
| `Live` | `Short` | `2955.00` | 343,730,000.00 USD | 195,540.00 USD | 0.00 USD | `+31.66%` | `66.17` |
| `Live` | `Short` | `2965.00` | 347,570,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+32.11%` | `1,293.83` |
| `Live` | `Short` | `2975.00` | 347,630,000.00 USD | 64,010.00 USD | 0.00 USD | `+32.55%` | `21.52` |
| `Live` | `Short` | `2985.00` | 347,890,000.00 USD | 263,200.00 USD | 0.00 USD | `+33.00%` | `88.17` |
| `Live` | `Short` | `2995.00` | 351,650,000.00 USD | 3,750,000.00 USD | 0.00 USD | `+33.44%` | `1,253.53` |
| `Live` | `Short` | `3005.00` | 352,210,000.00 USD | 558,790.00 USD | 0.00 USD | `+33.89%` | `185.95` |
| `Live` | `Short` | `3015.00` | 352,360,000.00 USD | 156,160.00 USD | 0.00 USD | `+34.33%` | `51.79` |
| `Live` | `Short` | `3025.00` | 354,400,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+34.78%` | `672.90` |
| `Live` | `Short` | `3035.00` | 367,220,000.00 USD | 12,820,000.00 USD | 0.00 USD | `+35.23%` | `4,225.04` |
| `Live` | `Short` | `3045.00` | 369,020,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+35.67%` | `590.54` |
| `Live` | `Short` | `3055.00` | 369,810,000.00 USD | 792,010.00 USD | 0.00 USD | `+36.12%` | `259.25` |
| `Live` | `Short` | `3065.00` | 375,070,000.00 USD | 5,250,000.00 USD | 0.00 USD | `+36.56%` | `1,714.43` |
| `Live` | `Short` | `3075.00` | 375,110,000.00 USD | 46,710.00 USD | 0.00 USD | `+37.01%` | `15.19` |
| `Live` | `Short` | `3085.00` | 375,450,000.00 USD | 341,970.00 USD | 0.00 USD | `+37.45%` | `110.85` |
| `Live` | `Short` | `3095.00` | 378,880,000.00 USD | 3,430,000.00 USD | 0.00 USD | `+37.90%` | `1,107.52` |
| `Live` | `Short` | `3105.00` | 385,120,000.00 USD | 6,240,000.00 USD | 0.00 USD | `+38.34%` | `2,008.79` |
| `Live` | `Short` | `3115.00` | 385,590,000.00 USD | 467,930.00 USD | 0.00 USD | `+38.79%` | `150.22` |
| `Live` | `Short` | `3125.00` | 385,700,000.00 USD | 112,120.00 USD | 0.00 USD | `+39.24%` | `35.88` |
| `Live` | `Short` | `3135.00` | 385,900,000.00 USD | 203,940.00 USD | 0.00 USD | `+39.68%` | `65.05` |
| `Live` | `Short` | `3145.00` | 390,900,000.00 USD | 5,000,000.00 USD | 0.00 USD | `+40.13%` | `1,588.25` |
| `Live` | `Short` | `3155.00` | 391,020,000.00 USD | 116,780.00 USD | 0.00 USD | `+40.57%` | `37.02` |
| `Live` | `Short` | `3165.00` | 391,030,000.00 USD | 15,960.00 USD | 0.00 USD | `+41.02%` | `5.04` |
| `Live` | `Short` | `3175.00` | 427,380,000.00 USD | 36,340,000.00 USD | 0.00 USD | `+41.46%` | `11,446.96` |
| `Live` | `Short` | `3185.00` | 428,160,000.00 USD | 780,770.00 USD | 0.00 USD | `+41.91%` | `245.14` |
| `Live` | `Short` | `3195.00` | 431,790,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+42.35%` | `1,138.94` |
| `Live` | `Short` | `3205.00` | 431,980,000.00 USD | 181,980.00 USD | 0.00 USD | `+42.80%` | `56.78` |
| `Live` | `Short` | `3215.00` | 432,200,000.00 USD | 222,240.00 USD | 0.00 USD | `+43.25%` | `69.13` |
| `Live` | `Short` | `3225.00` | 432,460,000.00 USD | 260,650.00 USD | 0.00 USD | `+43.69%` | `80.82` |
| `Live` | `Short` | `3235.00` | 442,360,000.00 USD | 9,900,000.00 USD | 0.00 USD | `+44.14%` | `3,059.59` |
| `Live` | `Short` | `3245.00` | 460,540,000.00 USD | 18,190,000.00 USD | 0.00 USD | `+44.58%` | `5,604.22` |
| `Live` | `Short` | `3255.00` | 462,050,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+45.03%` | `462.83` |
| `Live` | `Short` | `3265.00` | 462,370,000.00 USD | 325,000.00 USD | 0.00 USD | `+45.47%` | `99.54` |
| `Live` | `Short` | `3275.00` | 470,830,000.00 USD | 8,460,000.00 USD | 0.00 USD | `+45.92%` | `2,581.71` |
| `Live` | `Short` | `3285.00` | 470,900,000.00 USD | 72,520.00 USD | 0.00 USD | `+46.36%` | `22.08` |
| `Live` | `Short` | `3295.00` | 471,000,000.00 USD | 93,310.00 USD | 0.00 USD | `+46.81%` | `28.32` |
| `Live` | `Short` | `3305.00` | 476,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | `+47.26%` | `1,801.61` |
| `Live` | `Short` | `3315.00` | 478,310,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+47.70%` | `411.71` |
| `Live` | `Short` | `3325.00` | 478,580,000.00 USD | 267,850.00 USD | 0.00 USD | `+48.15%` | `80.56` |
| `Live` | `Short` | `3335.00` | 482,700,000.00 USD | 4,120,000.00 USD | 0.00 USD | `+48.59%` | `1,235.64` |
| `Live` | `Short` | `3345.00` | 484,270,000.00 USD | 1,570,000.00 USD | 0.00 USD | `+49.04%` | `469.12` |
| `Live` | `Short` | `3355.00` | 484,680,000.00 USD | 405,140.00 USD | 0.00 USD | `+49.48%` | `120.76` |
| `Live` | `Short` | `3365.00` | 484,840,000.00 USD | 158,830.00 USD | 0.00 USD | `+49.93%` | `47.20` |
| `Live` | `Short` | `3375.00` | 485,090,000.00 USD | 250,720.00 USD | 0.00 USD | `+50.37%` | `74.29` |
| `Live` | `Short` | `3385.00` | 487,390,000.00 USD | 2,310,000.00 USD | 0.00 USD | `+50.82%` | `680.96` |
| `Live` | `Short` | `3395.00` | 487,460,000.00 USD | 66,390.00 USD | 0.00 USD | `+51.27%` | `19.56` |
| `Live` | `Short` | `3405.00` | 488,800,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+51.71%` | `395.29` |
| `Live` | `Short` | `3415.00` | 490,690,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+52.16%` | `552.39` |
| `Live` | `Short` | `3425.00` | 505,670,000.00 USD | 14,980,000.00 USD | 0.00 USD | `+52.60%` | `4,374.54` |
| `Live` | `Short` | `3435.00` | 505,770,000.00 USD | 93,400.00 USD | 0.00 USD | `+53.05%` | `27.19` |
| `Live` | `Short` | `3445.00` | 505,800,000.00 USD | 30,870.00 USD | 0.00 USD | `+53.49%` | `8.96` |
| `Live` | `Short` | `3455.00` | 508,560,000.00 USD | 2,760,000.00 USD | 0.00 USD | `+53.94%` | `799.40` |
| `Live` | `Short` | `3465.00` | 509,160,000.00 USD | 596,640.00 USD | 0.00 USD | `+54.38%` | `172.19` |
| `Live` | `Short` | `3475.00` | 567,210,000.00 USD | 58,050,000.00 USD | 0.00 USD | `+54.83%` | `16,705.92` |
| `Live` | `Short` | `3485.00` | 568,050,000.00 USD | 839,680.00 USD | 0.00 USD | `+55.28%` | `240.94` |
| `Live` | `Short` | `3495.00` | 570,120,000.00 USD | 2,070,000.00 USD | 0.00 USD | `+55.72%` | `592.51` |
| `Live` | `Short` | `3505.00` | 570,210,000.00 USD | 90,350.00 USD | 0.00 USD | `+56.17%` | `25.78` |
| `Live` | `Short` | `3515.00` | 570,590,000.00 USD | 383,510.00 USD | 0.00 USD | `+56.61%` | `109.11` |
| `Live` | `Short` | `3525.00` | 570,780,000.00 USD | 185,310.00 USD | 0.00 USD | `+57.06%` | `52.57` |
| `Live` | `Short` | `3535.00` | 585,180,000.00 USD | 14,400,000.00 USD | 0.00 USD | `+57.50%` | `4,074.27` |
| `Live` | `Short` | `3545.00` | 616,460,000.00 USD | 31,280,000.00 USD | 0.00 USD | `+57.95%` | `8,823.72` |
| `Live` | `Short` | `3555.00` | 616,560,000.00 USD | 96,350.00 USD | 0.00 USD | `+58.39%` | `27.10` |
| `Live` | `Short` | `3565.00` | 616,620,000.00 USD | 62,950.00 USD | 0.00 USD | `+58.84%` | `17.66` |
| `Live` | `Short` | `3575.00` | 616,730,000.00 USD | 104,570.00 USD | 0.00 USD | `+59.29%` | `29.25` |
| `Live` | `Short` | `3585.00` | 617,480,000.00 USD | 749,360.00 USD | 0.00 USD | `+59.73%` | `209.03` |
| `Live` | `Short` | `3595.00` | 617,560,000.00 USD | 80,590.00 USD | 0.00 USD | `+60.18%` | `22.42` |
| `Live` | `Short` | `3605.00` | 617,560,000.00 USD | 1,410.00 USD | 0.00 USD | `+60.62%` | `0.39` |
| `Live` | `Short` | `3615.00` | 621,280,000.00 USD | 3,720,000.00 USD | 0.00 USD | `+61.07%` | `1,029.29` |
| `Live` | `Short` | `3625.00` | 621,750,000.00 USD | 473,380.00 USD | 0.00 USD | `+61.51%` | `130.59` |
| `Live` | `Short` | `3635.00` | 631,790,000.00 USD | 10,040,000.00 USD | 0.00 USD | `+61.96%` | `2,761.28` |
| `Live` | `Short` | `3645.00` | 633,420,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+62.40%` | `448.64` |
| `Live` | `Short` | `3655.00` | 639,920,000.00 USD | 6,500,000.00 USD | 0.00 USD | `+62.85%` | `1,777.53` |
| `Live` | `Short` | `3665.00` | 640,290,000.00 USD | 373,640.00 USD | 0.00 USD | `+63.30%` | `101.95` |
| `Live` | `Short` | `3675.00` | 640,300,000.00 USD | 5,910.00 USD | 0.00 USD | `+63.74%` | `1.61` |
| `Live` | `Short` | `3685.00` | 640,500,000.00 USD | 202,890.00 USD | 0.00 USD | `+64.19%` | `55.06` |
| `Live` | `Short` | `3695.00` | 640,780,000.00 USD | 271,950.00 USD | 0.00 USD | `+64.63%` | `73.60` |
| `Live` | `Short` | `3705.00` | 640,780,000.00 USD | 5,830.00 USD | 0.00 USD | `+65.08%` | `1.57` |
| `Live` | `Short` | `3715.00` | 642,620,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+65.52%` | `494.64` |
| `Live` | `Short` | `3725.00` | 643,140,000.00 USD | 525,580.00 USD | 0.00 USD | `+65.97%` | `141.09` |
| `Live` | `Short` | `3735.00` | 643,510,000.00 USD | 363,320.00 USD | 0.00 USD | `+66.41%` | `97.27` |
| `Live` | `Short` | `3745.00` | 644,390,000.00 USD | 882,670.00 USD | 0.00 USD | `+66.86%` | `235.69` |
| `Live` | `Short` | `3755.00` | 649,910,000.00 USD | 5,520,000.00 USD | 0.00 USD | `+67.31%` | `1,469.92` |
| `Live` | `Short` | `3765.00` | 1,050,000,000.00 USD | 403,440,000.00 USD | 0.00 USD | `+67.75%` | `107,155.97` |
| `Live` | `Short` | `3775.00` | 1,050,000,000.00 USD | 277,040.00 USD | 0.00 USD | `+68.20%` | `73.39` |
| `Live` | `Short` | `3785.00` | 1,050,000,000.00 USD | 4,020.00 USD | 0.00 USD | `+68.64%` | `1.06` |
| `Live` | `Short` | `3795.00` | 1,060,000,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+69.09%` | `501.78` |
| `Live` | `Short` | `3805.00` | 1,060,000,000.00 USD | 117,810.00 USD | 0.00 USD | `+69.53%` | `30.96` |
| `Live` | `Short` | `3815.00` | 1,060,000,000.00 USD | 114,840.00 USD | 0.00 USD | `+69.98%` | `30.10` |
| `Live` | `Short` | `3825.00` | 1,060,000,000.00 USD | 587,440.00 USD | 0.00 USD | `+70.42%` | `153.58` |
| `Live` | `Short` | `3835.00` | 1,060,000,000.00 USD | 379,460.00 USD | 0.00 USD | `+70.87%` | `98.95` |
| `Live` | `Short` | `3845.00` | 1,090,000,000.00 USD | 36,330,000.00 USD | 0.00 USD | `+71.32%` | `9,447.41` |
| `Live` | `Short` | `3855.00` | 1,090,000,000.00 USD | 67,620.00 USD | 0.00 USD | `+71.76%` | `17.54` |
| `Live` | `Short` | `3865.00` | 1,090,000,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+72.21%` | `354.09` |
| `Live` | `Short` | `3875.00` | 1,090,000,000.00 USD | 214,310.00 USD | 0.00 USD | `+72.65%` | `55.30` |
| `Live` | `Short` | `3885.00` | 1,100,000,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+73.10%` | `417.68` |
| `Live` | `Short` | `3895.00` | 1,100,000,000.00 USD | 2,500,000.00 USD | 0.00 USD | `+73.54%` | `641.91` |
| `Live` | `Short` | `3905.00` | 1,100,000,000.00 USD | 970,350.00 USD | 0.00 USD | `+73.99%` | `248.49` |
| `Live` | `Short` | `3915.00` | 1,100,000,000.00 USD | 19,860.00 USD | 0.00 USD | `+74.43%` | `5.07` |
| `Live` | `Short` | `3925.00` | 1,100,000,000.00 USD | 303,170.00 USD | 0.00 USD | `+74.88%` | `77.24` |
| `Live` | `Short` | `3935.00` | 1,100,000,000.00 USD | 45,410.00 USD | 0.00 USD | `+75.33%` | `11.54` |
| `Live` | `Short` | `3945.00` | 1,160,000,000.00 USD | 62,140,000.00 USD | 0.00 USD | `+75.77%` | `15,752.53` |
| `Live` | `Short` | `3955.00` | 1,160,000,000.00 USD | 755,660.00 USD | 0.00 USD | `+76.22%` | `191.06` |
| `Live` | `Short` | `3965.00` | 1,170,000,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+76.66%` | `493.38` |
| `Live` | `Short` | `3975.00` | 1,170,000,000.00 USD | 230,210.00 USD | 0.00 USD | `+77.11%` | `57.91` |
| `Live` | `Short` | `3985.00` | 1,170,000,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+77.55%` | `300.50` |
| `Live` | `Short` | `3995.00` | 1,170,000,000.00 USD | 81,660.00 USD | 0.00 USD | `+78.00%` | `20.44` |
| `Live` | `Short` | `4005.00` | 1,170,000,000.00 USD | 138,770.00 USD | 0.00 USD | `+78.44%` | `34.65` |
| `Live` | `Short` | `4015.00` | 1,170,000,000.00 USD | 81,640.00 USD | 0.00 USD | `+78.89%` | `20.33` |
| `Live` | `Short` | `4025.00` | 1,170,000,000.00 USD | 304,520.00 USD | 0.00 USD | `+79.34%` | `75.66` |
| `Live` | `Short` | `4035.00` | 1,170,000,000.00 USD | 1,820.00 USD | 0.00 USD | `+79.78%` | `0.45` |
| `Live` | `Short` | `4045.00` | 1,170,000,000.00 USD | 113,860.00 USD | 0.00 USD | `+80.23%` | `28.15` |
| `Live` | `Short` | `4055.00` | 1,170,000,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+80.67%` | `399.36` |
| `Live` | `Short` | `4065.00` | 1,170,000,000.00 USD | 792,670.00 USD | 0.00 USD | `+81.12%` | `195.00` |
| `Live` | `Short` | `4075.00` | 1,170,000,000.00 USD | 63,580.00 USD | 0.00 USD | `+81.56%` | `15.60` |
| `Live` | `Short` | `4085.00` | 1,170,000,000.00 USD | 57,350.00 USD | 0.00 USD | `+82.01%` | `14.04` |
| `Live` | `Short` | `4095.00` | 1,170,000,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+82.45%` | `538.45` |
| `Live` | `Short` | `4105.00` | 1,170,000,000.00 USD | 151,570.00 USD | 0.00 USD | `+82.90%` | `36.92` |
| `Live` | `Short` | `4115.00` | 1,170,000,000.00 USD | 139,550.00 USD | 0.00 USD | `+83.35%` | `33.91` |
| `Live` | `Short` | `4125.00` | 1,170,000,000.00 USD | 811,010.00 USD | 0.00 USD | `+83.79%` | `196.61` |
| `Live` | `Short` | `4135.00` | 1,170,000,000.00 USD | 2,050.00 USD | 0.00 USD | `+84.24%` | `0.50` |
| `Live` | `Short` | `4145.00` | 1,170,000,000.00 USD | 21,380.00 USD | 0.00 USD | `+84.68%` | `5.16` |
| `Live` | `Short` | `4155.00` | 1,180,000,000.00 USD | 2,820,000.00 USD | 0.00 USD | `+85.13%` | `679.40` |
| `Live` | `Short` | `4165.00` | 1,180,000,000.00 USD | 951,460.00 USD | 0.00 USD | `+85.57%` | `228.44` |
| `Live` | `Short` | `4175.00` | 1,260,000,000.00 USD | 83,590,000.00 USD | 0.00 USD | `+86.02%` | `20,020.80` |
| `Live` | `Short` | `4185.00` | 1,260,000,000.00 USD | 228,140.00 USD | 0.00 USD | `+86.46%` | `54.51` |
| `Live` | `Short` | `4195.00` | 1,260,000,000.00 USD | 4,050,000.00 USD | 0.00 USD | `+86.91%` | `964.37` |
| `Live` | `Short` | `4205.00` | 1,290,000,000.00 USD | 28,680,000.00 USD | 0.00 USD | `+87.36%` | `6,821.44` |
| `Live` | `Short` | `4215.00` | 1,300,000,000.00 USD | 5,270,000.00 USD | 0.00 USD | `+87.80%` | `1,249.50` |
| `Live` | `Short` | `4225.00` | 1,300,000,000.00 USD | 37,310.00 USD | 0.00 USD | `+88.25%` | `8.83` |
| `Live` | `Short` | `4235.00` | 1,300,000,000.00 USD | 194,370.00 USD | 0.00 USD | `+88.69%` | `45.90` |
| `Live` | `Short` | `4245.00` | 1,300,000,000.00 USD | 6,400.00 USD | 0.00 USD | `+89.14%` | `1.51` |
| `Live` | `Short` | `4255.00` | 1,300,000,000.00 USD | 484,630.00 USD | 0.00 USD | `+89.58%` | `113.90` |
| `Live` | `Short` | `4265.00` | 1,300,000,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+90.03%` | `927.26` |
| `Live` | `Short` | `4275.00` | 1,300,000,000.00 USD | 93,710.00 USD | 0.00 USD | `+90.47%` | `21.92` |
| `Live` | `Short` | `4285.00` | 1,300,000,000.00 USD | 48,360.00 USD | 0.00 USD | `+90.92%` | `11.29` |
| `Live` | `Short` | `4295.00` | 1,580,000,000.00 USD | 277,850,000.00 USD | 0.00 USD | `+91.37%` | `64,692.43` |
| `Live` | `Short` | `4305.00` | 1,580,000,000.00 USD | 24,070.00 USD | 0.00 USD | `+91.81%` | `5.59` |
| `Live` | `Short` | `4315.00` | 1,580,000,000.00 USD | 52,650.00 USD | 0.00 USD | `+92.26%` | `12.20` |
| `Live` | `Short` | `4325.00` | 1,580,000,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+92.70%` | `288.91` |
| `Live` | `Short` | `4335.00` | 1,580,000,000.00 USD | 28,870.00 USD | 0.00 USD | `+93.15%` | `6.66` |
| `Live` | `Short` | `4345.00` | 1,580,000,000.00 USD | 550,170.00 USD | 0.00 USD | `+93.59%` | `126.62` |
| `Live` | `Short` | `4355.00` | 1,580,000,000.00 USD | 26,100.00 USD | 0.00 USD | `+94.04%` | `5.99` |
| `Live` | `Short` | `4365.00` | 1,580,000,000.00 USD | 547,750.00 USD | 0.00 USD | `+94.48%` | `125.49` |
| `Live` | `Short` | `4375.00` | 1,580,000,000.00 USD | 13,200.00 USD | 0.00 USD | `+94.93%` | `3.02` |
| `Live` | `Short` | `4385.00` | 1,580,000,000.00 USD | 117.96 USD | 0.00 USD | `+95.38%` | `0.03` |
| `Live` | `Short` | `4395.00` | 1,580,000,000.00 USD | 298,180.00 USD | 0.00 USD | `+95.82%` | `67.85` |
| `Live` | `Short` | `4405.00` | 1,580,000,000.00 USD | 23,210.00 USD | 0.00 USD | `+96.27%` | `5.27` |
| `Live` | `Short` | `4415.00` | 1,580,000,000.00 USD | 47,770.00 USD | 0.00 USD | `+96.71%` | `10.82` |
| `Live` | `Short` | `4425.00` | 1,580,000,000.00 USD | 14,660.00 USD | 0.00 USD | `+97.16%` | `3.31` |
| `Live` | `Short` | `4435.00` | 1,580,000,000.00 USD | 388,920.00 USD | 0.00 USD | `+97.60%` | `87.69` |
| `Live` | `Short` | `4445.00` | 1,580,000,000.00 USD | 9,060.00 USD | 0.00 USD | `+98.05%` | `2.04` |
| `Live` | `Short` | `4455.00` | 1,580,000,000.00 USD | 400,860.00 USD | 0.00 USD | `+98.49%` | `89.98` |
| `Live` | `Short` | `4465.00` | 1,590,000,000.00 USD | 50,360.00 USD | 0.00 USD | `+98.94%` | `11.28` |
| `Live` | `Short` | `4475.00` | 1,590,000,000.00 USD | 339,770.00 USD | 0.00 USD | `+99.39%` | `75.93` |
| `Live` | `Short` | `4485.00` | 1,590,000,000.00 USD | 67,280.00 USD | 0.00 USD | `+99.83%` | `15.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 70,110,000.00 USD | 0.00 USD | 278.83 USD | `-78.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 70,110,000.00 USD | 0.00 USD | 16,000.00 USD | `-77.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 70,090,000.00 USD | 0.00 USD | 563.16 USD | `-75.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 70,090,000.00 USD | 0.00 USD | 583.40 USD | `-71.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 70,090,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 70,070,000.00 USD | 0.00 USD | 578.54 USD | `-69.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 70,070,000.00 USD | 0.00 USD | 242.21 USD | `-69.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 70,070,000.00 USD | 0.00 USD | 885.90 USD | `-68.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 70,070,000.00 USD | 0.00 USD | 177.27 USD | `-66.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 70,070,000.00 USD | 0.00 USD | 2,090.00 USD | `-64.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 70,070,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 70,070,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 69,930,000.00 USD | 0.00 USD | 918.49 USD | `-61.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 69,930,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 69,930,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 69,920,000.00 USD | 0.00 USD | 516.34 USD | `-56.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 69,920,000.00 USD | 0.00 USD | 100.50 USD | `-55.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 69,920,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 69,700,000.00 USD | 0.00 USD | 445.08 USD | `-54.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 69,700,000.00 USD | 0.00 USD | 112.03 USD | `-54.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 69,700,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 69,700,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 69,700,000.00 USD | 0.00 USD | 995.34 USD | `-52.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 69,690,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 69,690,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 69,680,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 69,680,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 69,680,000.00 USD | 0.00 USD | 476.46 USD | `-47.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 69,680,000.00 USD | 0.00 USD | 972.41 USD | `-47.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 69,680,000.00 USD | 0.00 USD | 221.55 USD | `-46.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 69,680,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 69,670,000.00 USD | 0.00 USD | 995.93 USD | `-45.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 69,670,000.00 USD | 0.00 USD | 951.93 USD | `-44.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 69,670,000.00 USD | 0.00 USD | 2,290.00 USD | `-44.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 69,670,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 69,660,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 69,650,000.00 USD | 0.00 USD | 25,040.00 USD | `-41.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 69,630,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 69,630,000.00 USD | 0.00 USD | 141,950.00 USD | `-40.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 69,490,000.00 USD | 0.00 USD | 128.86 USD | `-39.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 69,490,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 69,480,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 69,480,000.00 USD | 0.00 USD | 100,800.00 USD | `-38.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 69,380,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 68,840,000.00 USD | 0.00 USD | 18,840.00 USD | `-37.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 68,820,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 68,820,000.00 USD | 0.00 USD | 852.10 USD | `-36.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 68,820,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 68,820,000.00 USD | 0.00 USD | 5,090.00 USD | `-35.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 68,810,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 68,790,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 68,790,000.00 USD | 0.00 USD | 19,050.00 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 68,770,000.00 USD | 0.00 USD | 11,460.00 USD | `-33.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 68,760,000.00 USD | 0.00 USD | 84,170.00 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 68,670,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 68,660,000.00 USD | 0.00 USD | 31,900.00 USD | `-32.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 68,630,000.00 USD | 0.00 USD | 2,090.00 USD | `-31.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 68,630,000.00 USD | 0.00 USD | 960.99 USD | `-31.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 68,630,000.00 USD | 0.00 USD | 25,420.00 USD | `-30.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 68,600,000.00 USD | 0.00 USD | 10,660.00 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 68,590,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 68,390,000.00 USD | 0.00 USD | 4,990.00 USD | `-29.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 68,390,000.00 USD | 0.00 USD | 7,240.00 USD | `-28.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 68,380,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 67,950,000.00 USD | 0.00 USD | 25,810.00 USD | `-28.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 67,920,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 67,910,000.00 USD | 0.00 USD | 10,560.00 USD | `-27.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 67,900,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 67,570,000.00 USD | 0.00 USD | 114,830.00 USD | `-26.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 67,460,000.00 USD | 0.00 USD | 865.13 USD | `-25.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 67,460,000.00 USD | 0.00 USD | 289.27 USD | `-25.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 67,460,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 67,420,000.00 USD | 0.00 USD | 42,690.00 USD | `-24.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 67,380,000.00 USD | 0.00 USD | 84,490.00 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 67,290,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 67,280,000.00 USD | 0.00 USD | 47,500.00 USD | `-23.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 67,230,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 67,200,000.00 USD | 0.00 USD | 3,180.00 USD | `-22.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 67,200,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 66,730,000.00 USD | 0.00 USD | 77,220.00 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 66,660,000.00 USD | 0.00 USD | 3,090.00 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 66,650,000.00 USD | 0.00 USD | 26,700.00 USD | `-20.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 66,630,000.00 USD | 0.00 USD | 191,050.00 USD | `-20.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 66,430,000.00 USD | 0.00 USD | 732,750.00 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 65,700,000.00 USD | 0.00 USD | 263,150.00 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 65,440,000.00 USD | 0.00 USD | 35,520.00 USD | `-18.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 65,400,000.00 USD | 0.00 USD | 2,950.00 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 65,400,000.00 USD | 0.00 USD | 39,740.00 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 65,360,000.00 USD | 0.00 USD | 789,490.00 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 64,570,000.00 USD | 0.00 USD | 37,480.00 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 64,530,000.00 USD | 0.00 USD | 18,240,000.00 USD | `-16.46%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 46,300,000.00 USD | 0.00 USD | 17,330.00 USD | `-16.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 46,280,000.00 USD | 0.00 USD | 60,360.00 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 46,220,000.00 USD | 0.00 USD | 139,910.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 46,080,000.00 USD | 0.00 USD | 104,130.00 USD | `-14.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 45,970,000.00 USD | 0.00 USD | 19,290,000.00 USD | `-14.23%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 26,680,000.00 USD | 0.00 USD | 105,080.00 USD | `-13.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 26,570,000.00 USD | 0.00 USD | 61,020.00 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 26,510,000.00 USD | 0.00 USD | 64,040.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 26,450,000.00 USD | 0.00 USD | 139,400.00 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 26,310,000.00 USD | 0.00 USD | 74,090.00 USD | `-12.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 26,240,000.00 USD | 0.00 USD | 102,900.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 26,130,000.00 USD | 0.00 USD | 122,920.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 26,010,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 23,900,000.00 USD | 0.00 USD | 48,020.00 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 23,850,000.00 USD | 0.00 USD | 14,360.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 23,840,000.00 USD | 0.00 USD | 311,320.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 23,530,000.00 USD | 0.00 USD | 698,630.00 USD | `-8.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 22,830,000.00 USD | 0.00 USD | 269,140.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 22,560,000.00 USD | 0.00 USD | 119,510.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 22,440,000.00 USD | 0.00 USD | 162,590.00 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 22,280,000.00 USD | 0.00 USD | 143,520.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 22,130,000.00 USD | 0.00 USD | 29,580.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 22,110,000.00 USD | 0.00 USD | 547,760.00 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 21,560,000.00 USD | 0.00 USD | 156,280.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 21,400,000.00 USD | 0.00 USD | 123,110.00 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 21,280,000.00 USD | 0.00 USD | 585,260.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 20,690,000.00 USD | 0.00 USD | 208,830.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 20,480,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 18,250,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 16,570,000.00 USD | 0.00 USD | 8,510,000.00 USD | `-3.09%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 8,060,000.00 USD | 0.00 USD | 130,460.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 7,930,000.00 USD | 0.00 USD | 2,640,000.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 5,290,000.00 USD | 0.00 USD | 597,250.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 4,690,000.00 USD | 0.00 USD | 2,840,000.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,850,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 115,400.00 USD | 0.00 USD | 115,400.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 153,020.00 USD | 153,020.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 1,060,000.00 USD | 911,340.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 2,130,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 2,370,000.00 USD | 244,300.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 3,500,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 4,190,000.00 USD | 691,240.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 14,350,000.00 USD | 10,160,000.00 USD | 0.00 USD | `+2.70%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 15,790,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 16,110,000.00 USD | 316,370.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 16,260,000.00 USD | 151,690.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 17,280,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 18,570,000.00 USD | 1,290,000.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 18,860,000.00 USD | 283,620.00 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 19,000,000.00 USD | 146,720.00 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 19,060,000.00 USD | 50,700.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 20,100,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 21,620,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 21,870,000.00 USD | 250,590.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 24,820,000.00 USD | 2,950,000.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 25,000,000.00 USD | 184,400.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 25,530,000.00 USD | 525,910.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 25,670,000.00 USD | 144,890.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 27,770,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 27,960,000.00 USD | 188,650.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 30,070,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 30,510,000.00 USD | 439,630.00 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 35,590,000.00 USD | 5,090,000.00 USD | 0.00 USD | `+11.61%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 42,740,000.00 USD | 7,150,000.00 USD | 0.00 USD | `+12.06%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 45,370,000.00 USD | 2,620,000.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 45,430,000.00 USD | 64,370.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 47,620,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 47,840,000.00 USD | 218,500.00 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 50,180,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 50,260,000.00 USD | 80,760.00 USD | 0.00 USD | `+14.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 52,770,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 52,780,000.00 USD | 10,500.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 55,680,000.00 USD | 2,900,000.00 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 55,770,000.00 USD | 91,920.00 USD | 0.00 USD | `+16.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 57,950,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 58,100,000.00 USD | 147,930.00 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 60,220,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+17.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 60,530,000.00 USD | 306,950.00 USD | 0.00 USD | `+18.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 62,670,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 62,880,000.00 USD | 208,460.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 65,060,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 65,150,000.00 USD | 94,620.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 70,160,000.00 USD | 5,010,000.00 USD | 0.00 USD | `+20.52%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2715.00` | 70,240,000.00 USD | 76,590.00 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 72,700,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+21.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 72,750,000.00 USD | 43,050.00 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 75,120,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+22.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 76,010,000.00 USD | 892,870.00 USD | 0.00 USD | `+22.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 78,330,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 78,900,000.00 USD | 577,610.00 USD | 0.00 USD | `+23.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 81,170,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+24.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 81,180,000.00 USD | 17,550.00 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 84,340,000.00 USD | 3,150,000.00 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 84,390,000.00 USD | 52,490.00 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 84,430,000.00 USD | 43,930.00 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 84,720,000.00 USD | 286,140.00 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 85,720,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 86,990,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 87,000,000.00 USD | 11,150.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 87,010,000.00 USD | 2,460.00 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 87,310,000.00 USD | 305,820.00 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 87,330,000.00 USD | 16,190.00 USD | 0.00 USD | `+28.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 88,810,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 88,820,000.00 USD | 10,340.00 USD | 0.00 USD | `+29.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 88,830,000.00 USD | 3,050.00 USD | 0.00 USD | `+30.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 88,880,000.00 USD | 52,370.00 USD | 0.00 USD | `+30.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 88,910,000.00 USD | 34,650.00 USD | 0.00 USD | `+31.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 88,960,000.00 USD | 43,460.00 USD | 0.00 USD | `+31.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 89,070,000.00 USD | 113,340.00 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 89,220,000.00 USD | 145,510.00 USD | 0.00 USD | `+32.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 90,150,000.00 USD | 931,470.00 USD | 0.00 USD | `+33.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 95,070,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+33.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 97,180,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 97,190,000.00 USD | 6,950.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 97,220,000.00 USD | 35,380.00 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 97,300,000.00 USD | 74,910.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 97,320,000.00 USD | 22,460.00 USD | 0.00 USD | `+35.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 98,090,000.00 USD | 771,070.00 USD | 0.00 USD | `+36.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 98,090,000.00 USD | 612.69 USD | 0.00 USD | `+36.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 98,140,000.00 USD | 49,500.00 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 98,160,000.00 USD | 19,570.00 USD | 0.00 USD | `+37.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 98,160,000.00 USD | 928.50 USD | 0.00 USD | `+37.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 110,120,000.00 USD | 11,960,000.00 USD | 0.00 USD | `+38.34%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 110,230,000.00 USD | 111,160.00 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 110,610,000.00 USD | 381,020.00 USD | 0.00 USD | `+39.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 110,610,000.00 USD | 2,660.00 USD | 0.00 USD | `+40.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 110,670,000.00 USD | 58,930.00 USD | 0.00 USD | `+40.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 110,680,000.00 USD | 9,860.00 USD | 0.00 USD | `+41.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 110,680,000.00 USD | 149.22 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 110,680,000.00 USD | 1,330.00 USD | 0.00 USD | `+41.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 110,720,000.00 USD | 41,120.00 USD | 0.00 USD | `+42.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 111,380,000.00 USD | 658,320.00 USD | 0.00 USD | `+42.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 111,380,000.00 USD | 1,760.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 111,540,000.00 USD | 156,230.00 USD | 0.00 USD | `+43.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 111,540,000.00 USD | 167.25 USD | 0.00 USD | `+44.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 111,600,000.00 USD | 57,500.00 USD | 0.00 USD | `+44.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 111,830,000.00 USD | 236,580.00 USD | 0.00 USD | `+45.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 111,850,000.00 USD | 15,710.00 USD | 0.00 USD | `+45.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 111,850,000.00 USD | 1,630.00 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 111,990,000.00 USD | 141,980.00 USD | 0.00 USD | `+46.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 112,010,000.00 USD | 15,350.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 113,420,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+47.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 113,810,000.00 USD | 389,970.00 USD | 0.00 USD | `+47.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 113,840,000.00 USD | 24,200.00 USD | 0.00 USD | `+48.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 113,840,000.00 USD | 4,350.00 USD | 0.00 USD | `+48.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 113,840,000.00 USD | 2,170.00 USD | 0.00 USD | `+49.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 113,840,000.00 USD | 2,520.00 USD | 0.00 USD | `+49.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 113,850,000.00 USD | 2,780.00 USD | 0.00 USD | `+49.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 113,870,000.00 USD | 21,260.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 113,930,000.00 USD | 58,140.00 USD | 0.00 USD | `+50.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 114,250,000.00 USD | 322,160.00 USD | 0.00 USD | `+51.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 115,750,000.00 USD | 1,500,000.00 USD | 0.00 USD | `+51.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 115,750,000.00 USD | 5,700.00 USD | 0.00 USD | `+52.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 115,770,000.00 USD | 16,310.00 USD | 0.00 USD | `+52.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 115,780,000.00 USD | 15,030.00 USD | 0.00 USD | `+53.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 115,800,000.00 USD | 18,600.00 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 115,800,000.00 USD | 495.50 USD | 0.00 USD | `+54.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 115,810,000.00 USD | 3,190.00 USD | 0.00 USD | `+54.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 115,850,000.00 USD | 43,610.00 USD | 0.00 USD | `+55.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 115,850,000.00 USD | 158.32 USD | 0.00 USD | `+55.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 116,300,000.00 USD | 446,770.00 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 116,340,000.00 USD | 43,460.00 USD | 0.00 USD | `+56.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 116,340,000.00 USD | 3,690.00 USD | 0.00 USD | `+57.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 116,350,000.00 USD | 9,810.00 USD | 0.00 USD | `+57.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 116,440,000.00 USD | 90,810.00 USD | 0.00 USD | `+58.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 116,450,000.00 USD | 2,590.00 USD | 0.00 USD | `+58.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 116,450,000.00 USD | 2,870.00 USD | 0.00 USD | `+59.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 116,450,000.00 USD | 354.92 USD | 0.00 USD | `+59.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 116,460,000.00 USD | 13,160.00 USD | 0.00 USD | `+60.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 116,560,000.00 USD | 101,080.00 USD | 0.00 USD | `+60.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 116,560,000.00 USD | 199.55 USD | 0.00 USD | `+61.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 116,570,000.00 USD | 10,210.00 USD | 0.00 USD | `+61.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 116,580,000.00 USD | 7,790.00 USD | 0.00 USD | `+61.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 116,590,000.00 USD | 3,860.00 USD | 0.00 USD | `+62.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 116,590,000.00 USD | 8,090.00 USD | 0.00 USD | `+62.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 116,600,000.00 USD | 8,130.00 USD | 0.00 USD | `+63.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 116,660,000.00 USD | 55,120.00 USD | 0.00 USD | `+63.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 116,660,000.00 USD | 1,410.00 USD | 0.00 USD | `+64.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 116,660,000.00 USD | 819.92 USD | 0.00 USD | `+65.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 116,660,000.00 USD | 323.58 USD | 0.00 USD | `+65.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 116,660,000.00 USD | 1,400.00 USD | 0.00 USD | `+65.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 116,670,000.00 USD | 6,490.00 USD | 0.00 USD | `+66.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 116,670,000.00 USD | 165.90 USD | 0.00 USD | `+66.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 116,670,000.00 USD | 751.00 USD | 0.00 USD | `+67.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 116,670,000.00 USD | 286.90 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 116,670,000.00 USD | 1,560.00 USD | 0.00 USD | `+69.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 117,400,000.00 USD | 732,630.00 USD | 0.00 USD | `+69.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 117,420,000.00 USD | 20,930.00 USD | 0.00 USD | `+69.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 117,430,000.00 USD | 8,380.00 USD | 0.00 USD | `+70.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 117,430,000.00 USD | 711.78 USD | 0.00 USD | `+70.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 117,430,000.00 USD | 355.28 USD | 0.00 USD | `+71.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 117,440,000.00 USD | 5,170.00 USD | 0.00 USD | `+71.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 117,460,000.00 USD | 19,430.00 USD | 0.00 USD | `+73.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 117,470,000.00 USD | 12,120.00 USD | 0.00 USD | `+73.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 118,190,000.00 USD | 717,170.00 USD | 0.00 USD | `+74.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 118,230,000.00 USD | 42,570.00 USD | 0.00 USD | `+75.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 118,290,000.00 USD | 59,170.00 USD | 0.00 USD | `+75.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 118,290,000.00 USD | 1,380.00 USD | 0.00 USD | `+76.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 118,300,000.00 USD | 6,960.00 USD | 0.00 USD | `+77.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 118,310,000.00 USD | 14,610.00 USD | 0.00 USD | `+77.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 118,320,000.00 USD | 4,280.00 USD | 0.00 USD | `+78.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 121,070,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+78.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 121,070,000.00 USD | 898.59 USD | 0.00 USD | `+79.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 121,070,000.00 USD | 811.00 USD | 0.00 USD | `+80.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 121,070,000.00 USD | 4,310.00 USD | 0.00 USD | `+81.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 121,080,000.00 USD | 3,050.00 USD | 0.00 USD | `+82.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 121,110,000.00 USD | 36,740.00 USD | 0.00 USD | `+82.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 121,120,000.00 USD | 5,990.00 USD | 0.00 USD | `+83.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 121,120,000.00 USD | 372.90 USD | 0.00 USD | `+83.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 121,120,000.00 USD | 395.43 USD | 0.00 USD | `+84.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 121,120,000.00 USD | 376.65 USD | 0.00 USD | `+86.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 121,160,000.00 USD | 42,260.00 USD | 0.00 USD | `+87.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 121,160,000.00 USD | 460.70 USD | 0.00 USD | `+87.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 121,160,000.00 USD | 1,270.00 USD | 0.00 USD | `+88.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 121,170,000.00 USD | 4,300.00 USD | 0.00 USD | `+89.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 121,170,000.00 USD | 437.16 USD | 0.00 USD | `+90.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 121,230,000.00 USD | 64,550.00 USD | 0.00 USD | `+90.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 121,230,000.00 USD | 1,610.00 USD | 0.00 USD | `+90.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 121,330,000.00 USD | 94,600.00 USD | 0.00 USD | `+91.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 121,330,000.00 USD | 1,070.00 USD | 0.00 USD | `+92.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 121,340,000.00 USD | 11,270.00 USD | 0.00 USD | `+93.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 121,340,000.00 USD | 2,400.00 USD | 0.00 USD | `+94.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 121,390,000.00 USD | 43,750.00 USD | 0.00 USD | `+94.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 121,450,000.00 USD | 64,570.00 USD | 0.00 USD | `+95.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 121,450,000.00 USD | 1,050.00 USD | 0.00 USD | `+95.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 121,750,000.00 USD | 300,210.00 USD | 0.00 USD | `+96.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 121,760,000.00 USD | 11,480.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 121,770,000.00 USD | 2,510.00 USD | 0.00 USD | `+97.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 121,940,000.00 USD | 177,400.00 USD | 0.00 USD | `+97.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 121,950,000.00 USD | 2,040.00 USD | 0.00 USD | `+98.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 121,950,000.00 USD | 1,030.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1972.90` | 981,920,000.00 USD | 0.00 USD | 981,920,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1976.10` | 981,790,000.00 USD | 0.00 USD | 981,790,000.00 USD | 2,240,000.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1982.50` | 979,500,000.00 USD | 0.00 USD | 979,500,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1985.70` | 979,290,000.00 USD | 0.00 USD | 979,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1988.90` | 977,000,000.00 USD | 0.00 USD | 977,000,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1992.10` | 973,750,000.00 USD | 0.00 USD | 973,750,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1995.30` | 971,040,000.00 USD | 0.00 USD | 971,040,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `2004.90` | 968,890,000.00 USD | 0.00 USD | 968,890,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD |
| `1D` | `2005.10` | 693,530,000.00 USD | 0.00 USD | 693,530,000.00 USD | 14,690.00 USD | 18,870.00 USD | 10,310.00 USD |
| `1D` | `2007.50` | 693,480,000.00 USD | 0.00 USD | 693,480,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD |
| `1D` | `2009.90` | 693,260,000.00 USD | 0.00 USD | 693,260,000.00 USD | 0.00 USD | 308,260.00 USD | 0.00 USD |
| `7D` | `2011.30` | 968,620,000.00 USD | 0.00 USD | 968,620,000.00 USD | 170,840.00 USD | 92,470.00 USD | 0.00 USD |
| `1D` | `2012.30` | 692,950,000.00 USD | 0.00 USD | 692,950,000.00 USD | 323,820.00 USD | 266,130.00 USD | 16,930.00 USD |
| `1D` | `2014.70` | 692,340,000.00 USD | 0.00 USD | 692,340,000.00 USD | 355,800.00 USD | 31,280.00 USD | 12,280.00 USD |
| `1D` | `2017.10` | 691,940,000.00 USD | 0.00 USD | 691,940,000.00 USD | 483,920.00 USD | 897,320.00 USD | 518,850.00 USD |
| `1D` | `2019.50` | 690,040,000.00 USD | 0.00 USD | 690,040,000.00 USD | 326,370.00 USD | 1,460,000.00 USD | 377,900.00 USD |
| `1D` | `2021.90` | 687,880,000.00 USD | 0.00 USD | 687,880,000.00 USD | 973,110.00 USD | 199,120.00 USD | 800,660.00 USD |
| `1D` | `2024.30` | 685,910,000.00 USD | 0.00 USD | 685,910,000.00 USD | 122,610.00 USD | 0.00 USD | 927,480.00 USD |
| `1D` | `2026.70` | 684,860,000.00 USD | 0.00 USD | 684,860,000.00 USD | 280,250.00 USD | 1,130,000.00 USD | 40,210.00 USD |
| `7D` | `2027.30` | 968,360,000.00 USD | 0.00 USD | 968,360,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2029.10` | 683,410,000.00 USD | 0.00 USD | 683,410,000.00 USD | 1,140,000.00 USD | 1,180,000.00 USD | 609,000.00 USD |
| `7D` | `2030.50` | 968,180,000.00 USD | 0.00 USD | 968,180,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,080,000.00 USD |
| `1D` | `2031.50` | 680,480,000.00 USD | 0.00 USD | 680,480,000.00 USD | 677,540.00 USD | 293,350.00 USD | 1,060,000.00 USD |
| `7D` | `2033.70` | 963,780,000.00 USD | 0.00 USD | 963,780,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `1D` | `2033.90` | 678,450,000.00 USD | 0.00 USD | 678,450,000.00 USD | 1,810,000.00 USD | 1,330,000.00 USD | 165,760.00 USD |
| `1D` | `2036.30` | 675,150,000.00 USD | 0.00 USD | 675,150,000.00 USD | 119,600.00 USD | 177,360.00 USD | 11,070.00 USD |
| `7D` | `2036.90` | 962,220,000.00 USD | 0.00 USD | 962,220,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2038.70` | 674,840,000.00 USD | 0.00 USD | 674,840,000.00 USD | 939,380.00 USD | 300,240.00 USD | 377,350.00 USD |
| `7D` | `2040.10` | 961,890,000.00 USD | 0.00 USD | 961,890,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2041.10` | 673,220,000.00 USD | 0.00 USD | 673,220,000.00 USD | 626,840.00 USD | 178,560.00 USD | 176,570.00 USD |
| `7D` | `2043.30` | 960,440,000.00 USD | 0.00 USD | 960,440,000.00 USD | 0.00 USD | 0.00 USD | 101,940.00 USD |
| `1D` | `2043.50` | 672,240,000.00 USD | 0.00 USD | 672,240,000.00 USD | 0.00 USD | 0.00 USD | 28,960.00 USD |
| `1D` | `2045.90` | 672,210,000.00 USD | 0.00 USD | 672,210,000.00 USD | 0.00 USD | 0.00 USD | 19,040.00 USD |
| `7D` | `2046.50` | 960,330,000.00 USD | 0.00 USD | 960,330,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD |
| `1D` | `2048.30` | 672,190,000.00 USD | 0.00 USD | 672,190,000.00 USD | 518,440.00 USD | 0.00 USD | 357,950.00 USD |
| `7D` | `2049.70` | 960,140,000.00 USD | 0.00 USD | 960,140,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2050.70` | 671,310,000.00 USD | 0.00 USD | 671,310,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2052.90` | 959,910,000.00 USD | 0.00 USD | 959,910,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.10` | 670,260,000.00 USD | 0.00 USD | 670,260,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `1D` | `2055.50` | 670,230,000.00 USD | 0.00 USD | 670,230,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `1D` | `2057.90` | 669,900,000.00 USD | 0.00 USD | 669,900,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2059.30` | 957,630,000.00 USD | 0.00 USD | 957,630,000.00 USD | 153,480.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2062.50` | 956,470,000.00 USD | 0.00 USD | 956,470,000.00 USD | 1,680,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2062.70` | 669,140,000.00 USD | 0.00 USD | 669,140,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `1D` | `2065.10` | 669,060,000.00 USD | 0.00 USD | 669,060,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `7D` | `2065.70` | 951,950,000.00 USD | 0.00 USD | 951,950,000.00 USD | 1,380,000.00 USD | 313,000.00 USD | 1,070,000.00 USD |
| `1D` | `2067.50` | 667,450,000.00 USD | 0.00 USD | 667,450,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2068.90` | 949,180,000.00 USD | 0.00 USD | 949,180,000.00 USD | 1,580,000.00 USD | 2,680,000.00 USD | 811,640.00 USD |
| `1D` | `2069.90` | 666,760,000.00 USD | 0.00 USD | 666,760,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2072.10` | 944,110,000.00 USD | 0.00 USD | 944,110,000.00 USD | 4,410,000.00 USD | 2,530,000.00 USD | 2,110,000.00 USD |
| `1D` | `2072.30` | 666,380,000.00 USD | 0.00 USD | 666,380,000.00 USD | 67,060.00 USD | 534,600.00 USD | 8,470.00 USD |
| `1D` | `2074.70` | 665,770,000.00 USD | 0.00 USD | 665,770,000.00 USD | 46,190.00 USD | 244,720.00 USD | 423,660.00 USD |
| `7D` | `2075.30` | 935,070,000.00 USD | 0.00 USD | 935,070,000.00 USD | 4,120,000.00 USD | 3,610,000.00 USD | 4,010,000.00 USD |
| `1D` | `2077.10` | 665,060,000.00 USD | 0.00 USD | 665,060,000.00 USD | 998,330.00 USD | 327,010.00 USD | 448,840.00 USD |
| `7D` | `2078.50` | 923,320,000.00 USD | 0.00 USD | 923,320,000.00 USD | 4,400,000.00 USD | 3,500,000.00 USD | 2,100,000.00 USD |
| `1D` | `2079.50` | 663,290,000.00 USD | 0.00 USD | 663,290,000.00 USD | 953,710.00 USD | 846,970.00 USD | 268,880.00 USD |
| `7D` | `2081.70` | 913,330,000.00 USD | 0.00 USD | 913,330,000.00 USD | 4,470,000.00 USD | 2,960,000.00 USD | 1,980,000.00 USD |
| `1D` | `2081.90` | 661,220,000.00 USD | 0.00 USD | 661,220,000.00 USD | 1,060,000.00 USD | 825,250.00 USD | 208,160.00 USD |
| `1D` | `2084.30` | 659,120,000.00 USD | 0.00 USD | 659,120,000.00 USD | 875,040.00 USD | 789,300.00 USD | 291,230.00 USD |
| `7D` | `2084.90` | 903,900,000.00 USD | 0.00 USD | 903,900,000.00 USD | 3,070,000.00 USD | 2,030,000.00 USD | 5,620,000.00 USD |
| `1D` | `2086.70` | 657,170,000.00 USD | 0.00 USD | 657,170,000.00 USD | 1,560,000.00 USD | 559,980.00 USD | 1,580,000.00 USD |
| `7D` | `2088.10` | 893,190,000.00 USD | 0.00 USD | 893,190,000.00 USD | 3,310,000.00 USD | 2,260,000.00 USD | 924,970.00 USD |
| `1D` | `2089.10` | 653,470,000.00 USD | 0.00 USD | 653,470,000.00 USD | 445,800.00 USD | 218,010.00 USD | 79,710.00 USD |
| `7D` | `2091.30` | 886,700,000.00 USD | 0.00 USD | 886,700,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2091.50` | 652,720,000.00 USD | 0.00 USD | 652,720,000.00 USD | 995,340.00 USD | 294,070.00 USD | 548,480.00 USD |
| `1D` | `2093.90` | 650,880,000.00 USD | 0.00 USD | 650,880,000.00 USD | 1,760,000.00 USD | 775,630.00 USD | 1,060,000.00 USD |
| `7D` | `2094.50` | 873,750,000.00 USD | 0.00 USD | 873,750,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2096.30` | 647,290,000.00 USD | 0.00 USD | 647,290,000.00 USD | 655,450.00 USD | 616,370.00 USD | 982,020.00 USD |
| `7D` | `2097.70` | 863,520,000.00 USD | 0.00 USD | 863,520,000.00 USD | 1,850,000.00 USD | 3,350,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.70` | 645,030,000.00 USD | 0.00 USD | 645,030,000.00 USD | 296,850.00 USD | 970,270.00 USD | 248,570.00 USD |
| `7D` | `2100.90` | 857,030,000.00 USD | 0.00 USD | 857,030,000.00 USD | 1,810,000.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2101.10` | 643,520,000.00 USD | 0.00 USD | 643,520,000.00 USD | 145,240.00 USD | 353,390.00 USD | 231,410.00 USD |
| `1D` | `2103.50` | 642,790,000.00 USD | 0.00 USD | 642,790,000.00 USD | 268,400.00 USD | 119,690.00 USD | 306,410.00 USD |
| `7D` | `2104.10` | 849,620,000.00 USD | 0.00 USD | 849,620,000.00 USD | 1,440,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2105.90` | 642,090,000.00 USD | 0.00 USD | 642,090,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | 1,180,000.00 USD |
| `7D` | `2107.30` | 845,130,000.00 USD | 0.00 USD | 845,130,000.00 USD | 8,470,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD |
| `1D` | `2108.30` | 636,150,000.00 USD | 0.00 USD | 636,150,000.00 USD | 656,240.00 USD | 9,120.00 USD | 6,190.00 USD |
| `7D` | `2110.50` | 834,320,000.00 USD | 0.00 USD | 834,320,000.00 USD | 2,930,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD |
| `1D` | `2110.70` | 635,480,000.00 USD | 0.00 USD | 635,480,000.00 USD | 36,110.00 USD | 22,440.00 USD | 0.00 USD |
| `1D` | `2113.10` | 635,420,000.00 USD | 0.00 USD | 635,420,000.00 USD | 866,490.00 USD | 506,690.00 USD | 244,160.00 USD |
| `7D` | `2113.70` | 826,490,000.00 USD | 0.00 USD | 826,490,000.00 USD | 1,810,000.00 USD | 1,810,000.00 USD | 3,000,000.00 USD |
| `1D` | `2115.50` | 633,800,000.00 USD | 0.00 USD | 633,800,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD |
| `7D` | `2116.90` | 819,860,000.00 USD | 0.00 USD | 819,860,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD |
| `1D` | `2117.90` | 632,050,000.00 USD | 0.00 USD | 632,050,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD |
| `7D` | `2120.10` | 812,580,000.00 USD | 0.00 USD | 812,580,000.00 USD | 13,490,000.00 USD | 5,410,000.00 USD | 2,600,000.00 USD |
| `1D` | `2120.30` | 623,260,000.00 USD | 0.00 USD | 623,260,000.00 USD | 5,430,000.00 USD | 325,610.00 USD | 671,270.00 USD |
| `1D` | `2122.70` | 616,830,000.00 USD | 0.00 USD | 616,830,000.00 USD | 3,690,000.00 USD | 3,490,000.00 USD | 1,830,000.00 USD |
| `7D` | `2123.30` | 791,080,000.00 USD | 0.00 USD | 791,080,000.00 USD | 7,590,000.00 USD | 6,420,000.00 USD | 1,990,000.00 USD |
| `1D` | `2125.10` | 607,810,000.00 USD | 0.00 USD | 607,810,000.00 USD | 6,280,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD |
| `7D` | `2126.50` | 775,080,000.00 USD | 0.00 USD | 775,080,000.00 USD | 3,220,000.00 USD | 6,310,000.00 USD | 5,590,000.00 USD |
| `1D` | `2127.50` | 597,590,000.00 USD | 0.00 USD | 597,590,000.00 USD | 3,570,000.00 USD | 4,180,000.00 USD | 782,350.00 USD |
| `7D` | `2129.70` | 759,960,000.00 USD | 0.00 USD | 759,960,000.00 USD | 5,040,000.00 USD | 1,260,000.00 USD | 1,700,000.00 USD |
| `1D` | `2129.90` | 589,060,000.00 USD | 0.00 USD | 589,060,000.00 USD | 2,080,000.00 USD | 172,040.00 USD | 762,060.00 USD |
| `1D` | `2132.30` | 586,040,000.00 USD | 0.00 USD | 586,040,000.00 USD | 0.00 USD | 177,810.00 USD | 1,540,000.00 USD |
| `7D` | `2132.90` | 751,960,000.00 USD | 0.00 USD | 751,960,000.00 USD | 1,850,000.00 USD | 1,790,000.00 USD | 770,730.00 USD |
| `1D` | `2134.70` | 584,330,000.00 USD | 0.00 USD | 584,330,000.00 USD | 20,600.00 USD | 460,010.00 USD | 86,940.00 USD |
| `7D` | `2136.10` | 747,540,000.00 USD | 0.00 USD | 747,540,000.00 USD | 1,820,000.00 USD | 849,030.00 USD | 18,020.00 USD |
| `1D` | `2137.10` | 583,760,000.00 USD | 0.00 USD | 583,760,000.00 USD | 21,090.00 USD | 1,090,000.00 USD | 0.00 USD |
| `7D` | `2139.30` | 744,860,000.00 USD | 0.00 USD | 744,860,000.00 USD | 1,110,000.00 USD | 1,920,000.00 USD | 434,700.00 USD |
| `1D` | `2139.50` | 582,650,000.00 USD | 0.00 USD | 582,650,000.00 USD | 36,740.00 USD | 265,280.00 USD | 64,360.00 USD |
| `1D` | `2141.90` | 582,280,000.00 USD | 0.00 USD | 582,280,000.00 USD | 473,480.00 USD | 805,020.00 USD | 0.00 USD |
| `7D` | `2142.50` | 741,400,000.00 USD | 0.00 USD | 741,400,000.00 USD | 2,300,000.00 USD | 503,710.00 USD | 661,260.00 USD |
| `1D` | `2144.30` | 581,010,000.00 USD | 0.00 USD | 581,010,000.00 USD | 258,680.00 USD | 2,770,000.00 USD | 118,750.00 USD |
| `7D` | `2145.70` | 737,940,000.00 USD | 0.00 USD | 737,940,000.00 USD | 1,110,000.00 USD | 1,760,000.00 USD | 0.00 USD |
| `1D` | `2146.70` | 577,860,000.00 USD | 0.00 USD | 577,860,000.00 USD | 1,500,000.00 USD | 1,410,000.00 USD | 58,110.00 USD |
| `7D` | `2148.90` | 735,070,000.00 USD | 0.00 USD | 735,070,000.00 USD | 485,890.00 USD | 1,000,000.00 USD | 465,750.00 USD |
| `1D` | `2149.10` | 574,890,000.00 USD | 0.00 USD | 574,890,000.00 USD | 6,970,000.00 USD | 1,320,000.00 USD | 1,350,000.00 USD |
| `1D` | `2151.50` | 565,250,000.00 USD | 0.00 USD | 565,250,000.00 USD | 2,630,000.00 USD | 2,580,000.00 USD | 2,300,000.00 USD |
| `7D` | `2152.10` | 733,110,000.00 USD | 0.00 USD | 733,110,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 0.00 USD |
| `1D` | `2153.90` | 557,730,000.00 USD | 0.00 USD | 557,730,000.00 USD | 722,300.00 USD | 3,860,000.00 USD | 1,390,000.00 USD |
| `7D` | `2155.30` | 721,550,000.00 USD | 0.00 USD | 721,550,000.00 USD | 186,890.00 USD | 1,720,000.00 USD | 1,620,000.00 USD |
| `1D` | `2156.30` | 551,760,000.00 USD | 0.00 USD | 551,760,000.00 USD | 4,060,000.00 USD | 1,550,000.00 USD | 2,120,000.00 USD |
| `7D` | `2158.50` | 718,020,000.00 USD | 0.00 USD | 718,020,000.00 USD | 4,580,000.00 USD | 2,190,000.00 USD | 2,740,000.00 USD |
| `1D` | `2158.70` | 544,020,000.00 USD | 0.00 USD | 544,020,000.00 USD | 1,300,000.00 USD | 790,770.00 USD | 3,760,000.00 USD |
| `1D` | `2161.10` | 538,170,000.00 USD | 0.00 USD | 538,170,000.00 USD | 6,320,000.00 USD | 7,640,000.00 USD | 549,880.00 USD |
| `7D` | `2161.70` | 708,510,000.00 USD | 0.00 USD | 708,510,000.00 USD | 236,540.00 USD | 2,620,000.00 USD | 1,190,000.00 USD |
| `1D` | `2163.50` | 523,670,000.00 USD | 0.00 USD | 523,670,000.00 USD | 12,520,000.00 USD | 8,710,000.00 USD | 2,300,000.00 USD |
| `7D` | `2164.90` | 704,460,000.00 USD | 0.00 USD | 704,460,000.00 USD | 21,940,000.00 USD | 17,760,000.00 USD | 3,110,000.00 USD |
| `1D` | `2165.90` | 500,130,000.00 USD | 0.00 USD | 500,130,000.00 USD | 11,060,000.00 USD | 11,880,000.00 USD | 4,590,000.00 USD |
| `7D` | `2168.10` | 661,640,000.00 USD | 0.00 USD | 661,640,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,690,000.00 USD |
| `1D` | `2168.30` | 472,600,000.00 USD | 0.00 USD | 472,600,000.00 USD | 16,140,000.00 USD | 6,570,000.00 USD | 5,060,000.00 USD |
| `1D` | `2170.70` | 444,830,000.00 USD | 0.00 USD | 444,830,000.00 USD | 22,920,000.00 USD | 8,330,000.00 USD | 6,840,000.00 USD |
| `7D` | `2171.30` | 629,030,000.00 USD | 0.00 USD | 629,030,000.00 USD | 2,550,000.00 USD | 6,730,000.00 USD | 6,630,000.00 USD |
| `1D` | `2173.10` | 406,740,000.00 USD | 0.00 USD | 406,740,000.00 USD | 6,820,000.00 USD | 3,860,000.00 USD | 3,800,000.00 USD |
| `7D` | `2174.50` | 613,120,000.00 USD | 0.00 USD | 613,120,000.00 USD | 35,320,000.00 USD | 1,690,000.00 USD | 2,510,000.00 USD |
| `1D` | `2175.50` | 392,260,000.00 USD | 0.00 USD | 392,260,000.00 USD | 3,540,000.00 USD | 355,620.00 USD | 0.00 USD |
| `7D` | `2177.70` | 573,600,000.00 USD | 0.00 USD | 573,600,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD |
| `1D` | `2177.90` | 388,370,000.00 USD | 0.00 USD | 388,370,000.00 USD | 771,300.00 USD | 0.00 USD | 2,830,000.00 USD |
| `1D` | `2180.30` | 384,770,000.00 USD | 0.00 USD | 384,770,000.00 USD | 853,380.00 USD | 1,460,000.00 USD | 1,370,000.00 USD |
| `1D` | `2182.70` | 381,090,000.00 USD | 0.00 USD | 381,090,000.00 USD | 73,470.00 USD | 26,540.00 USD | 3,040,000.00 USD |
| `7D` | `2184.10` | 572,280,000.00 USD | 0.00 USD | 572,280,000.00 USD | 24,680,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD |
| `1D` | `2185.10` | 377,950,000.00 USD | 0.00 USD | 377,950,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 3,190,000.00 USD |
| `7D` | `2187.30` | 542,350,000.00 USD | 0.00 USD | 542,350,000.00 USD | 14,380,000.00 USD | 17,750,000.00 USD | 0.00 USD |
| `1D` | `2187.50` | 372,790,000.00 USD | 0.00 USD | 372,790,000.00 USD | 3,960,000.00 USD | 1,250,000.00 USD | 5,360,000.00 USD |
| `1D` | `2189.90` | 362,220,000.00 USD | 0.00 USD | 362,220,000.00 USD | 3,010,000.00 USD | 3,680,000.00 USD | 5,100,000.00 USD |
| `7D` | `2190.50` | 510,210,000.00 USD | 0.00 USD | 510,210,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 4,580,000.00 USD |
| `1D` | `2192.30` | 350,440,000.00 USD | 0.00 USD | 350,440,000.00 USD | 6,650,000.00 USD | 2,870,000.00 USD | 1,200,000.00 USD |
| `7D` | `2193.70` | 465,250,000.00 USD | 0.00 USD | 465,250,000.00 USD | 141,070.00 USD | 7,340,000.00 USD | 8,080,000.00 USD |
| `1D` | `2194.70` | 339,720,000.00 USD | 0.00 USD | 339,720,000.00 USD | 5,460,000.00 USD | 4,300,000.00 USD | 2,630,000.00 USD |
| `7D` | `2196.90` | 449,680,000.00 USD | 0.00 USD | 449,680,000.00 USD | 242,610.00 USD | 243,760.00 USD | 2,040,000.00 USD |
| `1D` | `2197.10` | 327,340,000.00 USD | 0.00 USD | 327,340,000.00 USD | 4,540,000.00 USD | 978,380.00 USD | 6,350,000.00 USD |
| `1D` | `2199.50` | 315,460,000.00 USD | 0.00 USD | 315,460,000.00 USD | 1,510,000.00 USD | 2,760,000.00 USD | 7,780,000.00 USD |
| `7D` | `2200.10` | 447,160,000.00 USD | 0.00 USD | 447,160,000.00 USD | 0.00 USD | 0.00 USD | 5,400,000.00 USD |
| `1D` | `2201.90` | 303,420,000.00 USD | 0.00 USD | 303,420,000.00 USD | 7,020,000.00 USD | 4,720,000.00 USD | 2,880,000.00 USD |
| `7D` | `2203.30` | 441,760,000.00 USD | 0.00 USD | 441,760,000.00 USD | 4,310,000.00 USD | 0.00 USD | 7,670,000.00 USD |
| `1D` | `2204.30` | 288,800,000.00 USD | 0.00 USD | 288,800,000.00 USD | 1,750,000.00 USD | 779,370.00 USD | 3,740,000.00 USD |
| `7D` | `2206.50` | 429,780,000.00 USD | 0.00 USD | 429,780,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD |
| `1D` | `2206.70` | 282,540,000.00 USD | 0.00 USD | 282,540,000.00 USD | 146,940.00 USD | 1,570,000.00 USD | 0.00 USD |
| `1D` | `2209.10` | 280,820,000.00 USD | 0.00 USD | 280,820,000.00 USD | 104,760.00 USD | 3,130,000.00 USD | 0.00 USD |
| `7D` | `2209.70` | 423,060,000.00 USD | 0.00 USD | 423,060,000.00 USD | 0.00 USD | 0.00 USD | 9,960,000.00 USD |
| `1D` | `2211.50` | 277,580,000.00 USD | 0.00 USD | 277,580,000.00 USD | 247,260.00 USD | 3,350,000.00 USD | 0.00 USD |
| `7D` | `2212.90` | 413,100,000.00 USD | 0.00 USD | 413,100,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 3,300,000.00 USD |
| `1D` | `2213.90` | 273,980,000.00 USD | 0.00 USD | 273,980,000.00 USD | 5,830,000.00 USD | 5,040,000.00 USD | 141,190.00 USD |
| `7D` | `2216.10` | 406,110,000.00 USD | 0.00 USD | 406,110,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD |
| `1D` | `2216.30` | 262,970,000.00 USD | 0.00 USD | 262,970,000.00 USD | 522,020.00 USD | 978,580.00 USD | 68,610.00 USD |
| `1D` | `2218.70` | 261,410,000.00 USD | 0.00 USD | 261,410,000.00 USD | 7,780,000.00 USD | 1,490,000.00 USD | 4,440,000.00 USD |
| `7D` | `2219.30` | 405,620,000.00 USD | 0.00 USD | 405,620,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD |
| `1D` | `2221.10` | 247,690,000.00 USD | 0.00 USD | 247,690,000.00 USD | 876,990.00 USD | 5,240,000.00 USD | 3,470,000.00 USD |
| `7D` | `2222.50` | 379,040,000.00 USD | 0.00 USD | 379,040,000.00 USD | 815,570.00 USD | 11,530,000.00 USD | 17,370,000.00 USD |
| `1D` | `2223.50` | 238,110,000.00 USD | 0.00 USD | 238,110,000.00 USD | 16,610,000.00 USD | 3,630,000.00 USD | 7,890,000.00 USD |
| `7D` | `2225.70` | 349,320,000.00 USD | 0.00 USD | 349,320,000.00 USD | 9,260,000.00 USD | 15,570,000.00 USD | 21,330,000.00 USD |
| `1D` | `2225.90` | 209,960,000.00 USD | 0.00 USD | 209,960,000.00 USD | 10,730,000.00 USD | 2,590,000.00 USD | 8,880,000.00 USD |
| `1D` | `2228.30` | 187,760,000.00 USD | 0.00 USD | 187,760,000.00 USD | 23,080,000.00 USD | 16,570,000.00 USD | 2,230,000.00 USD |
| `7D` | `2228.90` | 303,160,000.00 USD | 0.00 USD | 303,160,000.00 USD | 31,720,000.00 USD | 12,750,000.00 USD | 18,310,000.00 USD |
| `1D` | `2230.70` | 145,890,000.00 USD | 0.00 USD | 145,890,000.00 USD | 40,470,000.00 USD | 0.00 USD | 7,920,000.00 USD |
| `7D` | `2232.10` | 240,380,000.00 USD | 0.00 USD | 240,380,000.00 USD | 30,250,000.00 USD | 45,540,000.00 USD | 29,360,000.00 USD |
| `1D` | `2233.10` | 97,500,000.00 USD | 0.00 USD | 97,500,000.00 USD | 14,300,000.00 USD | 6,600,000.00 USD | 20,860,000.00 USD |
| `7D` | `2235.30` | 135,220,000.00 USD | 0.00 USD | 135,220,000.00 USD | 39,990,000.00 USD | 43,730,000.00 USD | 14,660,000.00 USD |
| `1D` | `2235.50` | 55,740,000.00 USD | 0.00 USD | 55,740,000.00 USD | 15,850,000.00 USD | 0.00 USD | 20,220,000.00 USD |
| `1D` | `2237.90` | 19,670,000.00 USD | 0.00 USD | 19,670,000.00 USD | 8,000,000.00 USD | 0.00 USD | 4,460,000.00 USD |
| `7D` | `2238.50` | 36,840,000.00 USD | 0.00 USD | 36,840,000.00 USD | 14,060,000.00 USD | 0.00 USD | 22,780,000.00 USD |
| `1D` | `2240.30` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.70` | 32,370,000.00 USD | 32,370,000.00 USD | 0.00 USD | 32,370,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2242.70` | 192,730.00 USD | 192,730.00 USD | 0.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD |
| `7D` | `2244.90` | 34,180,000.00 USD | 34,180,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2245.10` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 1,650,000.00 USD | 45,350.00 USD |
| `1D` | `2247.50` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,950.00 USD |
| `7D` | `2248.10` | 41,880,000.00 USD | 41,880,000.00 USD | 0.00 USD | 2,650,000.00 USD | 3,700,000.00 USD | 1,350,000.00 USD |
| `1D` | `2249.90` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 5,930,000.00 USD | 166,850.00 USD | 55,780.00 USD |
| `7D` | `2251.30` | 71,980,000.00 USD | 71,980,000.00 USD | 0.00 USD | 21,220,000.00 USD | 8,880,000.00 USD | 0.00 USD |
| `1D` | `2252.30` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 4,530,000.00 USD | 122,810.00 USD | 1,270,000.00 USD |
| `7D` | `2254.50` | 80,780,000.00 USD | 80,780,000.00 USD | 0.00 USD | 1,790,000.00 USD | 6,600,000.00 USD | 406,400.00 USD |
| `1D` | `2254.70` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 9,970,000.00 USD | 6,950,000.00 USD | 2,740,000.00 USD |
| `1D` | `2257.10` | 60,610,000.00 USD | 60,610,000.00 USD | 0.00 USD | 16,500,000.00 USD | 7,220,000.00 USD | 3,250,000.00 USD |
| `7D` | `2257.70` | 118,110,000.00 USD | 118,110,000.00 USD | 0.00 USD | 24,930,000.00 USD | 12,290,000.00 USD | 108,210.00 USD |
| `1D` | `2259.50` | 82,830,000.00 USD | 82,830,000.00 USD | 0.00 USD | 10,420,000.00 USD | 10,920,000.00 USD | 891,660.00 USD |
| `7D` | `2260.90` | 129,080,000.00 USD | 129,080,000.00 USD | 0.00 USD | 6,720,000.00 USD | 0.00 USD | 4,250,000.00 USD |
| `1D` | `2261.90` | 102,820,000.00 USD | 102,820,000.00 USD | 0.00 USD | 8,860,000.00 USD | 4,740,000.00 USD | 6,400,000.00 USD |
| `7D` | `2264.10` | 130,540,000.00 USD | 130,540,000.00 USD | 0.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD |
| `1D` | `2264.30` | 131,160,000.00 USD | 131,160,000.00 USD | 0.00 USD | 9,090,000.00 USD | 11,030,000.00 USD | 8,220,000.00 USD |
| `1D` | `2266.70` | 149,730,000.00 USD | 149,730,000.00 USD | 0.00 USD | 5,960,000.00 USD | 6,730,000.00 USD | 5,880,000.00 USD |
| `7D` | `2267.30` | 142,520,000.00 USD | 142,520,000.00 USD | 0.00 USD | 0.00 USD | 5,650,000.00 USD | 6,330,000.00 USD |
| `1D` | `2269.10` | 178,060,000.00 USD | 178,060,000.00 USD | 0.00 USD | 14,740,000.00 USD | 5,520,000.00 USD | 8,070,000.00 USD |
| `7D` | `2270.50` | 168,330,000.00 USD | 168,330,000.00 USD | 0.00 USD | 15,780,000.00 USD | 1,330,000.00 USD | 8,700,000.00 USD |
| `1D` | `2271.50` | 192,170,000.00 USD | 192,170,000.00 USD | 0.00 USD | 3,470,000.00 USD | 1,340,000.00 USD | 9,300,000.00 USD |
| `7D` | `2273.70` | 174,340,000.00 USD | 174,340,000.00 USD | 0.00 USD | 373,530.00 USD | 5,640,000.00 USD | 0.00 USD |
| `1D` | `2273.90` | 198,090,000.00 USD | 198,090,000.00 USD | 0.00 USD | 256,830.00 USD | 4,450,000.00 USD | 1,220,000.00 USD |
| `1D` | `2276.30` | 236,790,000.00 USD | 236,790,000.00 USD | 0.00 USD | 16,020,000.00 USD | 15,520,000.00 USD | 7,160,000.00 USD |
| `7D` | `2276.90` | 184,820,000.00 USD | 184,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,480,000.00 USD |
| `1D` | `2278.70` | 252,400,000.00 USD | 252,400,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,290,000.00 USD | 3,720,000.00 USD |
| `7D` | `2280.10` | 231,180,000.00 USD | 231,180,000.00 USD | 0.00 USD | 854,200.00 USD | 45,440,000.00 USD | 67,210.00 USD |
| `1D` | `2281.10` | 311,600,000.00 USD | 311,600,000.00 USD | 0.00 USD | 27,140,000.00 USD | 24,180,000.00 USD | 7,870,000.00 USD |
| `7D` | `2283.30` | 326,370,000.00 USD | 326,370,000.00 USD | 0.00 USD | 5,600,000.00 USD | 75,810,000.00 USD | 13,780,000.00 USD |
| `1D` | `2283.50` | 367,080,000.00 USD | 367,080,000.00 USD | 0.00 USD | 28,940,000.00 USD | 14,190,000.00 USD | 12,350,000.00 USD |
| `1D` | `2285.90` | 388,210,000.00 USD | 388,210,000.00 USD | 0.00 USD | 4,500,000.00 USD | 11,700,000.00 USD | 4,930,000.00 USD |
| `7D` | `2286.50` | 331,810,000.00 USD | 331,810,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,590,000.00 USD | 483,080.00 USD |
| `1D` | `2288.30` | 410,970,000.00 USD | 410,970,000.00 USD | 0.00 USD | 11,850,000.00 USD | 5,000,000.00 USD | 5,910,000.00 USD |
| `7D` | `2289.70` | 361,980,000.00 USD | 361,980,000.00 USD | 0.00 USD | 7,010,000.00 USD | 8,650,000.00 USD | 14,500,000.00 USD |
| `1D` | `2290.70` | 447,860,000.00 USD | 447,860,000.00 USD | 0.00 USD | 17,540,000.00 USD | 12,460,000.00 USD | 6,880,000.00 USD |
| `7D` | `2292.90` | 375,230,000.00 USD | 375,230,000.00 USD | 0.00 USD | 7,890,000.00 USD | 0.00 USD | 5,370,000.00 USD |
| `1D` | `2293.10` | 471,420,000.00 USD | 471,420,000.00 USD | 0.00 USD | 11,970,000.00 USD | 3,760,000.00 USD | 7,840,000.00 USD |
| `1D` | `2295.50` | 494,160,000.00 USD | 494,160,000.00 USD | 0.00 USD | 5,060,000.00 USD | 11,890,000.00 USD | 5,790,000.00 USD |
| `7D` | `2296.10` | 424,680,000.00 USD | 424,680,000.00 USD | 0.00 USD | 23,390,000.00 USD | 9,570,000.00 USD | 16,490,000.00 USD |
| `1D` | `2297.90` | 535,280,000.00 USD | 535,280,000.00 USD | 0.00 USD | 23,620,000.00 USD | 12,300,000.00 USD | 5,200,000.00 USD |
| `7D` | `2299.30` | 460,270,000.00 USD | 460,270,000.00 USD | 0.00 USD | 14,380,000.00 USD | 20,670,000.00 USD | 541,260.00 USD |
| `1D` | `2300.30` | 571,270,000.00 USD | 571,270,000.00 USD | 0.00 USD | 9,580,000.00 USD | 12,870,000.00 USD | 13,550,000.00 USD |
| `7D` | `2302.50` | 520,450,000.00 USD | 520,450,000.00 USD | 0.00 USD | 26,960,000.00 USD | 11,130,000.00 USD | 22,080,000.00 USD |
| `1D` | `2302.70` | 597,390,000.00 USD | 597,390,000.00 USD | 0.00 USD | 17,120,000.00 USD | 1,760,000.00 USD | 7,240,000.00 USD |
| `1D` | `2305.10` | 635,900,000.00 USD | 635,900,000.00 USD | 0.00 USD | 14,750,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD |
| `7D` | `2305.70` | 546,600,000.00 USD | 546,600,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,990,000.00 USD |
| `1D` | `2307.50` | 647,960,000.00 USD | 647,960,000.00 USD | 0.00 USD | 4,370,000.00 USD | 4,480,000.00 USD | 3,210,000.00 USD |
| `7D` | `2308.90` | 549,790,000.00 USD | 549,790,000.00 USD | 0.00 USD | 1,920,000.00 USD | 930,630.00 USD | 338,800.00 USD |
| `1D` | `2309.90` | 665,550,000.00 USD | 665,550,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,720,000.00 USD | 10,660,000.00 USD |
| `7D` | `2312.10` | 579,100,000.00 USD | 579,100,000.00 USD | 0.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 15,880,000.00 USD |
| `1D` | `2312.30` | 673,750,000.00 USD | 673,750,000.00 USD | 0.00 USD | 3,160,000.00 USD | 4,900,000.00 USD | 135,490.00 USD |
| `1D` | `2314.70` | 690,900,000.00 USD | 690,900,000.00 USD | 0.00 USD | 3,210,000.00 USD | 12,880,000.00 USD | 1,060,000.00 USD |
| `7D` | `2315.30` | 587,850,000.00 USD | 587,850,000.00 USD | 0.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD |
| `1D` | `2317.10` | 718,680,000.00 USD | 718,680,000.00 USD | 0.00 USD | 10,260,000.00 USD | 9,530,000.00 USD | 7,990,000.00 USD |
| `7D` | `2318.50` | 602,770,000.00 USD | 602,770,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD |
| `1D` | `2319.50` | 738,580,000.00 USD | 738,580,000.00 USD | 0.00 USD | 9,790,000.00 USD | 9,150,000.00 USD | 952,870.00 USD |
| `7D` | `2321.70` | 621,400,000.00 USD | 621,400,000.00 USD | 0.00 USD | 0.00 USD | 15,930,000.00 USD | 2,690,000.00 USD |
| `1D` | `2321.90` | 755,030,000.00 USD | 755,030,000.00 USD | 0.00 USD | 1,730,000.00 USD | 9,350,000.00 USD | 5,380,000.00 USD |
| `1D` | `2324.30` | 767,800,000.00 USD | 767,800,000.00 USD | 0.00 USD | 1,490,000.00 USD | 11,270,000.00 USD | 9,730.00 USD |
| `7D` | `2324.90` | 638,350,000.00 USD | 638,350,000.00 USD | 0.00 USD | 5,790,000.00 USD | 2,770,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.70` | 775,670,000.00 USD | 775,670,000.00 USD | 0.00 USD | 985,290.00 USD | 1,020,000.00 USD | 5,870,000.00 USD |
| `7D` | `2328.10` | 655,700,000.00 USD | 655,700,000.00 USD | 0.00 USD | 9,330,000.00 USD | 0.00 USD | 8,020,000.00 USD |
| `1D` | `2329.10` | 787,340,000.00 USD | 787,340,000.00 USD | 0.00 USD | 8,760,000.00 USD | 1,990,000.00 USD | 918,990.00 USD |
| `7D` | `2331.30` | 679,090,000.00 USD | 679,090,000.00 USD | 0.00 USD | 23,030,000.00 USD | 363,770.00 USD | 0.00 USD |
| `1D` | `2331.50` | 807,730,000.00 USD | 807,730,000.00 USD | 0.00 USD | 15,540,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD |
| `1D` | `2333.90` | 830,070,000.00 USD | 830,070,000.00 USD | 0.00 USD | 9,780,000.00 USD | 4,510,000.00 USD | 8,050,000.00 USD |
| `7D` | `2334.50` | 731,270,000.00 USD | 731,270,000.00 USD | 0.00 USD | 20,300,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD |
| `1D` | `2336.30` | 848,120,000.00 USD | 848,120,000.00 USD | 0.00 USD | 12,350,000.00 USD | 1,550,000.00 USD | 4,150,000.00 USD |
| `7D` | `2337.70` | 770,290,000.00 USD | 770,290,000.00 USD | 0.00 USD | 28,410,000.00 USD | 0.00 USD | 10,620,000.00 USD |
| `1D` | `2338.70` | 863,190,000.00 USD | 863,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 2,930,000.00 USD | 4,950,000.00 USD |
| `7D` | `2340.90` | 805,370,000.00 USD | 805,370,000.00 USD | 0.00 USD | 4,720,000.00 USD | 16,440,000.00 USD | 13,920,000.00 USD |
| `1D` | `2341.10` | 882,760,000.00 USD | 882,760,000.00 USD | 0.00 USD | 5,340,000.00 USD | 4,080,000.00 USD | 10,140,000.00 USD |
| `1D` | `2343.50` | 899,640,000.00 USD | 899,640,000.00 USD | 0.00 USD | 4,110,000.00 USD | 7,620,000.00 USD | 5,150,000.00 USD |
| `7D` | `2344.10` | 821,970,000.00 USD | 821,970,000.00 USD | 0.00 USD | 1,350,000.00 USD | 9,270,000.00 USD | 5,980,000.00 USD |
| `1D` | `2345.90` | 912,050,000.00 USD | 912,050,000.00 USD | 0.00 USD | 3,680,000.00 USD | 3,280,000.00 USD | 5,440,000.00 USD |
| `7D` | `2347.30` | 860,690,000.00 USD | 860,690,000.00 USD | 0.00 USD | 0.00 USD | 17,240,000.00 USD | 21,480,000.00 USD |
| `1D` | `2348.30` | 924,460,000.00 USD | 924,460,000.00 USD | 0.00 USD | 5,020,000.00 USD | 4,640,000.00 USD | 2,760,000.00 USD |
| `7D` | `2350.50` | 905,390,000.00 USD | 905,390,000.00 USD | 0.00 USD | 3,120,000.00 USD | 22,500,000.00 USD | 19,070,000.00 USD |
| `1D` | `2350.70` | 969,610,000.00 USD | 969,610,000.00 USD | 0.00 USD | 28,110,000.00 USD | 6,920,000.00 USD | 10,130,000.00 USD |
| `1D` | `2353.10` | 976,820,000.00 USD | 976,820,000.00 USD | 0.00 USD | 3,010,000.00 USD | 2,550,000.00 USD | 1,650,000.00 USD |
| `7D` | `2353.70` | 942,460,000.00 USD | 942,460,000.00 USD | 0.00 USD | 2,960,000.00 USD | 33,380,000.00 USD | 723,430.00 USD |
| `1D` | `2355.50` | 989,910,000.00 USD | 989,910,000.00 USD | 0.00 USD | 3,770,000.00 USD | 7,700,000.00 USD | 1,620,000.00 USD |
| `7D` | `2356.90` | 981,700,000.00 USD | 981,700,000.00 USD | 0.00 USD | 21,390,000.00 USD | 10,720,000.00 USD | 7,140,000.00 USD |
| `1D` | `2357.90` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 3,270,000.00 USD | 4,470,000.00 USD | 3,480,000.00 USD |
| `7D` | `2360.10` | 990,050,000.00 USD | 990,050,000.00 USD | 0.00 USD | 4,260,000.00 USD | 3,940,000.00 USD | 151,860.00 USD |
| `1D` | `2360.30` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 10,920,000.00 USD | 3,880,000.00 USD | 5,490,000.00 USD |
| `1D` | `2362.70` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 6,590,000.00 USD | 6,710,000.00 USD | 7,930,000.00 USD |
| `7D` | `2363.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 5,040,000.00 USD | 373,740.00 USD | 6,930,000.00 USD |
| `1D` | `2365.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,140,000.00 USD | 3,680,000.00 USD |
| `7D` | `2366.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 4,210,000.00 USD |
| `1D` | `2367.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 2,980,000.00 USD | 1,110,000.00 USD | 1,920,000.00 USD |
| `7D` | `2369.70` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 24,570,000.00 USD | 475,460.00 USD | 13,880,000.00 USD |
| `1D` | `2369.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 10,660,000.00 USD | 5,540,000.00 USD | 3,730,000.00 USD |
| `1D` | `2372.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 9,810,000.00 USD | 5,630,000.00 USD | 8,730,000.00 USD |
| `7D` | `2372.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 17,480,000.00 USD | 121,480.00 USD | 45,550,000.00 USD |
| `1D` | `2374.70` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 12,780,000.00 USD | 557,400.00 USD | 1,840,000.00 USD |
| `7D` | `2376.10` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 9,370,000.00 USD | 925,700.00 USD | 22,120,000.00 USD |
| `1D` | `2377.10` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 2,610,000.00 USD | 2,530,000.00 USD | 4,820,000.00 USD |
| `7D` | `2379.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 14,060,000.00 USD | 7,600,000.00 USD | 12,980,000.00 USD |
| `1D` | `2379.50` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,330,000.00 USD | 2,050,000.00 USD |
| `1D` | `2381.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 11,190,000.00 USD | 8,290,000.00 USD | 11,930,000.00 USD |
| `7D` | `2382.50` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 8,620,000.00 USD | 12,380,000.00 USD | 27,930,000.00 USD |
| `1D` | `2384.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 14,340,000.00 USD | 8,580,000.00 USD | 5,130,000.00 USD |
| `7D` | `2385.70` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 15,780,000.00 USD | 39,650,000.00 USD | 57,320,000.00 USD |
| `1D` | `2386.70` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 6,620,000.00 USD | 10,580,000.00 USD | 4,810,000.00 USD |
| `7D` | `2388.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 5,490,000.00 USD | 31,800,000.00 USD | 34,870,000.00 USD |
| `1D` | `2389.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 10,580,000.00 USD | 6,800,000.00 USD | 1,770,000.00 USD |
| `1D` | `2391.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 270,800.00 USD | 3,710,000.00 USD | 3,350,000.00 USD |
| `7D` | `2392.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 18,500,000.00 USD | 53,390,000.00 USD | 43,670,000.00 USD |
| `1D` | `2393.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 4,630,000.00 USD | 2,780,000.00 USD | 1,140,000.00 USD |
| `7D` | `2395.30` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 52,350,000.00 USD | 28,350,000.00 USD | 30,450,000.00 USD |
| `1D` | `2396.30` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 163,360.00 USD | 1,160,000.00 USD | 2,890,000.00 USD |
| `7D` | `2398.50` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 0.00 USD | 43,330,000.00 USD | 39,800,000.00 USD | 27,700,000.00 USD |
| `1D` | `2398.70` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 2,700,000.00 USD | 3,760,000.00 USD | 2,010,000.00 USD |
| `1D` | `2401.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 3,630,000.00 USD | 3,010,000.00 USD | 2,310,000.00 USD |
| `7D` | `2401.70` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 54,210,000.00 USD | 27,480,000.00 USD | 32,780,000.00 USD |
| `1D` | `2403.50` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 5,270,000.00 USD | 2,820,000.00 USD | 1,500,000.00 USD |
| `7D` | `2404.90` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 0.00 USD | 43,350,000.00 USD | 29,960,000.00 USD | 22,830,000.00 USD |
| `1D` | `2405.90` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 7,470,000.00 USD | 5,220,000.00 USD | 5,840,000.00 USD |
| `7D` | `2408.10` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 33,260,000.00 USD | 31,290,000.00 USD | 22,590,000.00 USD |
| `1D` | `2408.30` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 6,920,000.00 USD | 5,490,000.00 USD | 1,870,000.00 USD |
| `1D` | `2410.70` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 4,650,000.00 USD | 4,780,000.00 USD | 5,290,000.00 USD |
| `7D` | `2411.30` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 28,860,000.00 USD | 27,690,000.00 USD |
| `1D` | `2413.10` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 7,470,000.00 USD | 3,470,000.00 USD | 1,760,000.00 USD |
| `7D` | `2414.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 22,650,000.00 USD | 25,120,000.00 USD | 22,420,000.00 USD |
| `1D` | `2415.50` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 2,990,000.00 USD | 2,330,000.00 USD | 3,510,000.00 USD |
| `7D` | `2417.70` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 31,590,000.00 USD | 11,300,000.00 USD | 23,700,000.00 USD |
| `1D` | `2417.90` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,090,000.00 USD | 1,530,000.00 USD |
| `1D` | `2420.30` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 6,150,000.00 USD | 2,900,000.00 USD | 3,810,000.00 USD |
| `7D` | `2420.90` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 30,470,000.00 USD | 23,750,000.00 USD | 12,980,000.00 USD |
| `1D` | `2422.70` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 2,790,000.00 USD | 3,170,000.00 USD |
| `7D` | `2424.10` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 20,130,000.00 USD | 28,380,000.00 USD | 23,670,000.00 USD |
| `1D` | `2425.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD |
| `7D` | `2427.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD |
| `1D` | `2427.50` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,070,000.00 USD | 603,040.00 USD |
| `1D` | `2429.90` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,000,000.00 USD | 1,020,000.00 USD |
| `7D` | `2430.50` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 8,480,000.00 USD | 15,370,000.00 USD | 9,620,000.00 USD |
| `1D` | `2432.30` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,230,000.00 USD | 762,920.00 USD |
| `7D` | `2433.70` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 19,810,000.00 USD | 7,430,000.00 USD | 12,150,000.00 USD |
| `1D` | `2434.70` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 545,610.00 USD | 1,620,000.00 USD |
| `7D` | `2436.90` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 14,880,000.00 USD | 16,620,000.00 USD | 7,210,000.00 USD |
| `1D` | `2437.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,320,000.00 USD | 1,050,000.00 USD | 30,250.00 USD |
| `1D` | `2439.50` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 479,780.00 USD | 304,820.00 USD |
| `7D` | `2440.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 14,940,000.00 USD | 10,690,000.00 USD | 3,760,000.00 USD |
| `1D` | `2441.90` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 1,130,000.00 USD | 723,100.00 USD | 553,720.00 USD |
| `7D` | `2443.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 6,880,000.00 USD | 7,430,000.00 USD | 10,770,000.00 USD |
| `1D` | `2444.30` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 0.00 USD | 467,480.00 USD | 1,400,000.00 USD |
| `7D` | `2446.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 12,840,000.00 USD | 10,790,000.00 USD | 14,550,000.00 USD |
| `1D` | `2446.70` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 472,100.00 USD | 504,420.00 USD | 687,270.00 USD |
| `1D` | `2449.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 321,220.00 USD | 0.00 USD | 26,770.00 USD |
| `7D` | `2449.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 11,870,000.00 USD | 9,640,000.00 USD | 11,360,000.00 USD |
| `1D` | `2451.50` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,650,000.00 USD | 1,010,000.00 USD |
| `7D` | `2452.90` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 8,060,000.00 USD | 6,090,000.00 USD | 7,870,000.00 USD |
| `1D` | `2453.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 1,890,000.00 USD | 2,140,000.00 USD |
| `7D` | `2456.10` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 6,330,000.00 USD | 6,830,000.00 USD | 6,720,000.00 USD |
| `1D` | `2456.30` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 622,030.00 USD | 1,560,000.00 USD | 479,530.00 USD |
| `1D` | `2458.70` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,490,000.00 USD | 16,930.00 USD |
| `7D` | `2459.30` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 8,020,000.00 USD | 10,190,000.00 USD | 11,340,000.00 USD |
| `1D` | `2461.10` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 540,100.00 USD | 242,570.00 USD | 379,080.00 USD |
| `7D` | `2462.50` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 9,210,000.00 USD | 5,460,000.00 USD |
| `1D` | `2463.50` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 330,880.00 USD | 940,830.00 USD | 1,010,000.00 USD |
| `7D` | `2465.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 5,970,000.00 USD | 2,890,000.00 USD | 2,780,000.00 USD |
| `1D` | `2465.90` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 483,920.00 USD | 872,060.00 USD | 553,080.00 USD |
| `1D` | `2468.30` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 326,370.00 USD | 1,680,000.00 USD | 164,010.00 USD |
| `7D` | `2468.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 3,570,000.00 USD | 432,050.00 USD |
| `1D` | `2470.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 973,110.00 USD | 199,120.00 USD | 1,190,000.00 USD |
| `7D` | `2472.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 2,760,000.00 USD | 1,210,000.00 USD |
| `1D` | `2473.10` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 933,760.00 USD |
| `7D` | `2475.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 1,040,000.00 USD | 2,020,000.00 USD |
| `1D` | `2475.50` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 122,610.00 USD | 1,100,000.00 USD | 0.00 USD |
| `1D` | `2477.90` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 1,080,000.00 USD | 475,250.00 USD | 0.00 USD |
| `7D` | `2478.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 5,290,000.00 USD | 540,990.00 USD |
| `1D` | `2480.30` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 346,950.00 USD | 659,030.00 USD | 586,640.00 USD |
| `1D` | `2480.70` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327,340.00 USD |
| `7D` | `2481.70` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,360,000.00 USD | 1,430,000.00 USD |
| `7D` | `2488.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,120,000.00 USD | 963,790.00 USD | 0.00 USD |
| `7D` | `2491.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 2,330,000.00 USD | 330,130.00 USD | 137,010.00 USD |
| `7D` | `2494.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 1,980,000.00 USD | 2,940,000.00 USD | 4,360,000.00 USD |
| `7D` | `2497.70` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 591,360.00 USD | 3,190,000.00 USD | 1,970,000.00 USD |
| `7D` | `2500.90` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 358,770.00 USD | 828,970.00 USD | 969,050.00 USD |
| `7D` | `2504.10` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 222,640.00 USD | 0.00 USD | 125,600.00 USD |
| `7D` | `2507.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,790,000.00 USD | 3,180,000.00 USD |
| `7D` | `2510.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `7D` | `2513.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.90` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2520.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `7D` | `2523.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD |
| `7D` | `2526.50` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 237,300.00 USD |
| `7D` | `2529.70` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 2,730,000.00 USD | 1,260,000.00 USD |
| `7D` | `2532.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 4,410,000.00 USD | 1,470,000.00 USD | 1,550,000.00 USD |
| `7D` | `2536.10` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 3,210,000.00 USD | 2,330,000.00 USD | 4,010,000.00 USD |
| `7D` | `2539.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 3,690,000.00 USD | 1,090,000.00 USD |
| `7D` | `2542.50` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 4,230,000.00 USD | 3,240,000.00 USD | 2,910,000.00 USD |
| `7D` | `2545.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,360,000.00 USD | 1,880,000.00 USD |
| `7D` | `2548.90` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,840,000.00 USD |
| `7D` | `2552.10` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD |
| `7D` | `2555.30` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `7D` | `2558.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,940,000.00 USD |
| `7D` | `2561.70` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,400,000.00 USD | 813,430.00 USD |
| `7D` | `2564.90` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,090,000.00 USD | 1,090,000.00 USD |
| `7D` | `2566.90` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 0.00 USD | 552,750.00 USD | 1,170,000.00 USD | 2,660,000.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.98B` | Total OI Tokens: `12,915,722.6 ETH`
  * 1h OI Change: `-0.57%` | 4h OI Change: `+0.40%` | 24h OI Change: `-2.84%`
  * Exchange Breakdown: Binance=`8.44B` | Bybit=`2.12B` | OKX=`1.78B` | Hyperliquid=`2.36B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-60.53K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0028%` | **USDT OKX** | `-0.0077%` |
| **USDT Bybit** | `-0.0139%` | **USDT KuCoin** | `-0.0097%` |
| **USDT MEXC** | `0.0026%` | **USDT BingX** | `0.0027%` |
| **USDT Gate** | `-0.0108%` | **USDT Bitget** | `0.0006%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0074%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `50.48%` | `49.52%` | `1.02` | 406,540,000.00 USD |
| `15M` | `Binance` | `46.57%` | `53.43%` | `0.87` | 135,930,000.00 USD |
| `15M` | `OKX` | `50.55%` | `49.45%` | `1.02` | 55,590,000.00 USD |
| `15M` | `Bybit` | `50.44%` | `49.56%` | `1.02` | 39,140,000.00 USD |
| `15M` | `KuCoin` | `71.04%` | `28.96%` | `2.45` | 954,200.00 USD |
| `15M` | `Gate` | `47.34%` | `52.66%` | `0.90` | 49,200,000.00 USD |
| `15M` | `Bitget` | `53.96%` | `46.04%` | `1.17` | 20,690,000.00 USD |
| `15M` | `BingX` | `40.58%` | `59.42%` | `0.68` | 4,780,000.00 USD |
| `15M` | `MEXC` | `53.16%` | `46.84%` | `1.13` | 21,670,000.00 USD |
| `15M` | `Bitunix` | `48.12%` | `51.88%` | `0.93` | 13,070,000.00 USD |
| `15M` | `Hyperliquid` | `60.74%` | `39.26%` | `1.55` | 26,790,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.6%` | `56.4%` | `0.77` | 2,570,000.00 USD |
| `15M` | `Crypto.com` | `58.59%` | `41.41%` | `1.41` | 1,590,000.00 USD |
| `15M` | `WhiteBIT` | `86.13%` | `13.87%` | `6.21` | 7,990,000.00 USD |
| `15M` | `HTX` | `58.63%` | `41.37%` | `1.42` | 2,030,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `52.73%` | `47.27%` | `1.12` | 14,670,000.00 USD |
| `15M` | `Bitfinex` | `12.74%` | `87.26%` | `0.15` | 915,950.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `48.68%` | `51.32%` | `0.95` | 2,760,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.87%` | `42.13%` | `1.37` | 6,220,000.00 USD |
| `15M` | `Whale Positions` | `46.57%` | `53.43%` | `0.87` | 135,930,000.00 USD |
| `15M` | `Global Accounts` | `50.48%` | `49.52%` | `1.02` | 406,540,000.00 USD |
| `1H` | `ETH` | `44.53%` | `55.47%` | `0.80` | 2,070,000,000.00 USD |
| `1H` | `Binance` | `40.94%` | `59.06%` | `0.69` | 746,780,000.00 USD |
| `1H` | `OKX` | `43.83%` | `56.17%` | `0.78` | 300,780,000.00 USD |
| `1H` | `Bybit` | `43.25%` | `56.75%` | `0.76` | 177,450,000.00 USD |
| `1H` | `KuCoin` | `40.12%` | `59.88%` | `0.67` | 5,490,000.00 USD |
| `1H` | `Gate` | `45.93%` | `54.07%` | `0.85` | 221,440,000.00 USD |
| `1H` | `Bitget` | `46.58%` | `53.42%` | `0.87` | 106,770,000.00 USD |
| `1H` | `BingX` | `39.21%` | `60.79%` | `0.65` | 29,330,000.00 USD |
| `1H` | `MEXC` | `38.65%` | `61.35%` | `0.63` | 94,780,000.00 USD |
| `1H` | `Bitunix` | `39.41%` | `60.59%` | `0.65` | 81,170,000.00 USD |
| `1H` | `Hyperliquid` | `60.59%` | `39.41%` | `1.54` | 132,510,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `43.44%` | `56.56%` | `0.77` | 11,710,000.00 USD |
| `1H` | `Crypto.com` | `50.65%` | `49.35%` | `1.03` | 5,830,000.00 USD |
| `1H` | `WhiteBIT` | `88.6%` | `11.4%` | `7.77` | 18,560,000.00 USD |
| `1H` | `HTX` | `42.26%` | `57.74%` | `0.73` | 9,420,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.7%` | `50.3%` | `0.99` | 83,010,000.00 USD |
| `1H` | `Bitfinex` | `36.58%` | `63.42%` | `0.58` | 1,690,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `53.88%` | `46.12%` | `1.17` | 16,960,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.22%` | `46.78%` | `1.14` | 24,920,000.00 USD |
| `1H` | `Whale Positions` | `40.94%` | `59.06%` | `0.69` | 746,780,000.00 USD |
| `1H` | `Global Accounts` | `44.53%` | `55.47%` | `0.80` | 2,070,000,000.00 USD |
| `4H` | `ETH` | `53.47%` | `46.53%` | `1.15` | 12,210,000,000.00 USD |
| `4H` | `Binance` | `52.39%` | `47.61%` | `1.10` | 3,950,000,000.00 USD |
| `4H` | `OKX` | `51.99%` | `48.01%` | `1.08` | 1,700,000,000.00 USD |
| `4H` | `Bybit` | `56.28%` | `43.72%` | `1.29` | 1,170,000,000.00 USD |
| `4H` | `KuCoin` | `69.5%` | `30.5%` | `2.28` | 44,000,000.00 USD |
| `4H` | `Gate` | `46.78%` | `53.22%` | `0.88` | 1,310,000,000.00 USD |
| `4H` | `Bitget` | `51.46%` | `48.54%` | `1.06` | 659,250,000.00 USD |
| `4H` | `BingX` | `49.1%` | `50.9%` | `0.96` | 178,000,000.00 USD |
| `4H` | `MEXC` | `46.71%` | `53.29%` | `0.88` | 508,040,000.00 USD |
| `4H` | `Bitunix` | `49.98%` | `50.02%` | `1.00` | 511,440,000.00 USD |
| `4H` | `Hyperliquid` | `56.29%` | `43.71%` | `1.29` | 861,710,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `64.13%` | `35.87%` | `1.79` | 105,280,000.00 USD |
| `4H` | `Crypto.com` | `50.8%` | `49.2%` | `1.03` | 36,170,000.00 USD |
| `4H` | `WhiteBIT` | `94.72%` | `5.28%` | `17.94` | 420,100,000.00 USD |
| `4H` | `HTX` | `51.97%` | `48.03%` | `1.08` | 43,020,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.86%` | `49.14%` | `1.04` | 445,660,000.00 USD |
| `4H` | `Bitfinex` | `60.69%` | `39.31%` | `1.54` | 10,300,000.00 USD |
| `4H` | `Kraken` | `26.88%` | `73.12%` | `0.37` | 2,900,000.00 USD |
| `4H` | `Aster` | `52.17%` | `47.83%` | `1.09` | 121,780,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.53%` | `50.47%` | `0.98` | 130,960,000.00 USD |
| `4H` | `Whale Positions` | `52.39%` | `47.61%` | `1.10` | 3,950,000,000.00 USD |
| `4H` | `Global Accounts` | `53.47%` | `46.53%` | `1.15` | 12,210,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2234.75` | `2234.69` | `2234.75` | `2238.25` | `2230.25` | 138,036,296.36 USD | 70,500,947.16 USD | 67,535,349.20 USD | 2,965,597.96 USD | `+2.15%` | `1B / 0S` |
| `0:00 UTC` | `2229.75` | `2230.64` | `2229.75` | `2236.75` | `2225.25` | 125,588,915.24 USD | 57,499,740.21 USD | 68,089,175.03 USD | -10,589,434.83 USD | `-8.43%` | `0B / 2S` |
| `5:00 UTC` | `2241.25` | `2240.18` | `2241.25` | `2243.25` | `2233.75` | 123,392,803.54 USD | 67,738,859.18 USD | 55,653,944.36 USD | 12,084,914.83 USD | `+9.79%` | `1B / 2S` |
| `0:00 UTC` | `2245.25` | `2244.67` | `2245.25` | `2246.25` | `2242.75` | 130,536,562.11 USD | 61,753,972.34 USD | 68,782,589.78 USD | -7,028,617.44 USD | `-5.38%` | `0B / 0S` |
| `5:00 UTC` | `2246.25` | `2244.65` | `2246.25` | `2246.75` | `2241.25` | 83,556,134.35 USD | 43,872,052.14 USD | 39,684,082.21 USD | 4,187,969.92 USD | `+5.01%` | `0B / 0S` |
| `0:00 UTC` | `2250.25` | `2247.75` | `2250.25` | `2252.75` | `2241.75` | 107,425,896.61 USD | 60,168,072.38 USD | 47,257,824.22 USD | 12,910,248.16 USD | `+12.02%` | `3B / 0S` |
| `5:00 UTC` | `2247.75` | `2247.16` | `2247.75` | `2249.25` | `2244.75` | 60,142,096.16 USD | 25,496,240.40 USD | 34,645,855.76 USD | -9,149,615.36 USD | `-15.21%` | `0B / 0S` |
| `0:00 UTC` | `2248.25` | `2248.34` | `2248.25` | `2251.75` | `2245.75` | 66,196,194.89 USD | 33,643,736.92 USD | 32,552,457.97 USD | 1,091,278.95 USD | `+1.65%` | `2B / 0S` |
| `5:00 UTC` | `2239.25` | `2242.30` | `2239.25` | `2250.25` | `2237.25` | 119,524,398.16 USD | 59,440,954.02 USD | 60,083,444.14 USD | -642,490.12 USD | `-0.54%` | `0B / 3S` |
| `0:00 UTC` | `2240.25` | `2239.34` | `2240.25` | `2243.75` | `2235.75` | 83,893,654.12 USD | 51,857,859.31 USD | 32,035,794.81 USD | 19,822,064.50 USD | `+23.63%` | `5B / 0S` |

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
| `5m` | 992,390.00 USD | 11,270,000.00 USD | **`ACCUMULATION`** |
| `15m` | 3,460,000.00 USD | 34,330,000.00 USD | **`ACCUMULATION`** |
| `30m` | -809,320.00 USD | -10,430,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,480,000.00 USD | -32,080,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -913,110.00 USD | 17,840,000.00 USD | **`ACCUMULATION`** |
| `4h` | 15,980,000.00 USD | 139,220,000.00 USD | **`ACCUMULATION`** |
| `6h` | -48,520,000.00 USD | -491,760,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -67,320,000.00 USD | -684,740,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -150,020,000.00 USD | -1,850,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -126,460,000.00 USD | -1,890,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -150,260,000.00 USD | -3,130,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,510,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+992.39K` | 15m=`+3.46M` | 1h=`+2.48M` | 24h=`-126.46M`
* Futures Capital Netflows: 5m=`+11.27M` | 15m=`+34.33M` | 1h=`-32.08M` | 24h=`-1.89B`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2209.38` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2186.89` (Risk Distance: `22.49` pts)
  * +2.5R Take Profit: `2265.60`
  * Mathematical Lot Sizing: **`0.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2275.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2298.24` (Risk Distance: `22.49` pts)
  * +2.5R Take Profit: `2219.53`
  * Mathematical Lot Sizing: **`0.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2258.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
