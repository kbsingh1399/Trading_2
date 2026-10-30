# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 16:55:00 IST` (`2026-10-30 11:25:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2240.90` | **Live Ask Quote**: `2243.70` | **Mid Price**: `2242.30`
- **Spread Points**: `280.00` | **Spread BPS**: `12.49 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2220.81` | VWAP Z-Score: `+1.21` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.45` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.97` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2269.20` | Lower -3.00σ Band: `2172.42`
  * Upper +2.51σ Band: `2261.30` | Lower -2.51σ Band: `2180.32`
  * Upper +2.01σ Band: `2253.23` | Lower -2.01σ Band: `2188.39`
  * Upper +2.00σ Band: `2253.07` | Lower -2.00σ Band: `2188.55`
  * Upper +1.28σ Band: `2241.46` | Lower -1.28σ Band: `2200.16`
  * Upper +1.00σ Band: `2236.94` | Lower -1.00σ Band: `2204.68`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2233.01` | EMA-20=`2231.36` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2240.65` (Slope: `+0.0000`) | EMA-100=`2262.52`
  * Institutional Anchors: EMA-144=`2276.35` | EMA-200=`2289.64` (Slope: `-0.3447`) | EMA-233=`2294.73`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2250.66` (Distance: `-0.38%`)
  * Point of Control (POC) = `2241.75` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `2196.43` (Distance: `+2.08%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2356.25` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.10`
  * New York Session (13:00-21:00 UTC): High=`2247.90` | Low=`2216.10`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2233.33` - `2251.27`
  * Optimal Trade Entry (OTE 0.705): `2246.78`
  * Structural Invalidation Anchor (0.786): `2260.24`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2248.40` | `2251.73` | `2245.09` | `2245.99` | `16,580` | 37,285,508.15 USD | 3,417,494.60 USD | `+9.17%` | -907,887,116.55 USD | `+0.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2246.00` | `2247.55` | `2245.00` | `2245.54` | `6,528` | 14,660,785.32 USD | -1,299,861.36 USD | `-8.87%` | -909,186,977.92 USD | `-0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2245.53` | `2246.63` | `2243.18` | `2243.61` | `4,377` | 9,823,611.10 USD | -6,244,242.40 USD | `-63.56%` | -915,431,220.32 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2228.48` | `2248.56` | `2228.26` | `2244.65` | `86,803` | 194,501,635.59 USD | 31,319,310.03 USD | `+16.10%` | -902,115,502.51 USD | `+1.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2244.65` | `2248.55` | `2240.23` | `2248.40` | `38,721` | 86,877,812.25 USD | -9,189,108.64 USD | `-10.58%` | -911,304,611.15 USD | `-0.57` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2248.40` | `2251.73` | `2243.18` | `2243.61` | `27,441` | 61,672,626.04 USD | -4,067,162.56 USD | `-6.59%` | -915,371,773.71 USD | `-0.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2231.18` | `2220.24` | `2228.42` | `122,419` | 272,434,813.90 USD | 5,581,746.93 USD | `+2.05%` | -920,109,678.48 USD | `+0.46` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2228.43` | `2248.56` | `2220.36` | `2248.40` | `178,179` | 398,534,292.30 USD | 25,797,692.56 USD | `+6.47%` | -894,311,985.92 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2248.40` | `2251.73` | `2243.18` | `2243.61` | `27,484` | 61,769,904.57 USD | -4,126,609.16 USD | `-6.68%` | -898,438,595.08 USD | `+0.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2251.73` | `2220.24` | `2243.61` | `492,304` | 1,098,665,066.83 USD | -10,513,080.03 USD | `-0.96%` | -898,379,148.47 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2251.73` | `2220.24` | `2243.61` | `492,304` | 1,098,665,066.83 USD | -10,513,080.03 USD | `-0.96%` | -898,379,148.47 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`2242.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2243.00` | `81.5623` | 182,944.24 USD | 8,156,085.49 USD | `11 orders` | `-0.09%` | `-` |
| `BID` | `2243.10` | `203.7522` | 457,036.56 USD | 7,973,141.25 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `2243.20` | `226.9558` | 509,107.25 USD | 7,516,104.69 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `2243.30` | `111.3935` | 249,889.04 USD | 7,006,997.44 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2243.40` | `311.5891` | 699,018.99 USD | 6,757,108.41 USD | `11 orders` | `-0.07%` | `-` |
| `BID` | `2243.50` | `137.2964` | 308,024.47 USD | 6,058,089.42 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `2243.60` | `313.8486` | 704,150.72 USD | 5,750,064.94 USD | `11 orders` | `-0.06%` | `-` |
| `BID` | `2243.70` | `371.8318` | 834,279.01 USD | 5,045,914.23 USD | `16 orders` | `-0.06%` | `-` |
| `BID` | `2243.80` | `255.8709` | 574,123.13 USD | 4,211,635.22 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2243.90` | `154.8042` | 347,365.14 USD | 3,637,512.09 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `2244.00` | `227.0340` | 509,464.30 USD | 3,290,146.95 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `2244.10` | `249.3321` | 559,526.17 USD | 2,780,682.65 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2244.20` | `368.0108` | 825,889.84 USD | 2,221,156.48 USD | `11 orders` | `-0.04%` | `-` |
| `BID` | `2244.30` | `170.4126` | 382,457.00 USD | 1,395,266.65 USD | `11 orders` | `-0.03%` | `-` |
| `BID` | `2244.40` | `160.8294` | 360,965.51 USD | 1,012,809.65 USD | `11 orders` | `-0.03%` | `-` |
| `BID` | `2244.50` | `108.6874` | 243,948.87 USD | 651,844.14 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2244.60` | `165.2536` | 370,928.23 USD | 407,895.27 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2244.70` | `4.2900` | 9,629.76 USD | 36,967.04 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `2244.90` | `12.0641` | 27,082.70 USD | 27,337.28 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2245.00` | `0.1134` | 254.58 USD | 254.58 USD | `3 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2245.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,245.05` | `0.00%` | `-` |
| `ASK` | `2245.10` | `325.9858` | 731,870.72 USD | 731,870.72 USD | `49 orders` | `+0.00%` | `-` |
| `ASK` | `2245.20` | `110.1557` | 247,321.58 USD | 979,192.30 USD | `12 orders` | `+0.01%` | `-` |
| `ASK` | `2245.30` | `202.6415` | 454,990.96 USD | 1,434,183.26 USD | `12 orders` | `+0.01%` | `-` |
| `ASK` | `2245.40` | `120.7135` | 271,050.09 USD | 1,705,233.35 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `2245.50` | `309.3157` | 694,568.40 USD | 2,399,801.75 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `2245.60` | `76.6104` | 172,036.31 USD | 2,571,838.07 USD | `10 orders` | `+0.02%` | `-` |
| `ASK` | `2245.70` | `369.1516` | 829,003.75 USD | 3,400,841.82 USD | `12 orders` | `+0.03%` | `-` |
| `ASK` | `2245.80` | `450.3491` | 1,011,394.01 USD | 4,412,235.83 USD | `13 orders` | `+0.03%` | `-` |
| `ASK` | `2245.90` | `161.1345` | 361,891.97 USD | 4,774,127.80 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `2246.00` | `357.8157` | 803,654.06 USD | 5,577,781.86 USD | `17 orders` | `+0.04%` | `-` |
| `ASK` | `2246.10` | `141.6301` | 318,115.37 USD | 5,895,897.23 USD | `15 orders` | `+0.05%` | `-` |
| `ASK` | `2246.20` | `318.4873` | 715,386.17 USD | 6,611,283.40 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `2246.30` | `219.5877` | 493,259.85 USD | 7,104,543.25 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2246.40` | `126.5279` | 284,232.27 USD | 7,388,775.53 USD | `13 orders` | `+0.06%` | `-` |
| `ASK` | `2246.50` | `194.0010` | 435,823.25 USD | 7,824,598.77 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2246.60` | `151.3092` | 339,931.25 USD | 8,164,530.02 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `2246.70` | `206.0865` | 463,014.54 USD | 8,627,544.56 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2246.80` | `112.6796` | 253,168.53 USD | 8,880,713.09 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `2246.90` | `288.8151` | 648,938.65 USD | 9,529,651.74 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2247.00` | `205.8636` | 462,575.51 USD | 9,992,227.24 USD | `13 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1843.87` | `7,964.66` | 14,685,805.43 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.13` | `6,500.22` | 12,435,749.27 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1929.89` | `8,092.45` | 15,617,516.47 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.82` | `30,641.99` | 65,016,792.34 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.10` | `26,025.05` | 55,409,882.62 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2205.50` | `2,029.41` | 4,475,859.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.00` | `505.25` | 1,115,093.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.90` | `4,210.48` | 9,321,581.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.60` | `1,417.50` | 3,143,440.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.00` | `505.02` | 1,122,666.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.40` | `342.68` | 761,925.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.60` | `357.40` | 794,719.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.00` | `1,022.78` | 2,276,703.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.00` | `430.01` | 957,637.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.70` | `2,171.06` | 4,838,642.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2230.30` | `505.00` | 1,126,310.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.20` | `679.45` | 1,515,983.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.00` | `347.51` | 775,642.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.40` | `1,794.36` | 4,005,729.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.40` | `1,108.98` | 2,476,789.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.70` | `344.01` | 768,414.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.00` | `472.33` | 1,055,178.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2234.00` | `465.08` | 1,038,983.58 USD | `TRIGGER_STOP` | `0x0903f51b01` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.20` | `1,344.10` | 3,004,337.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.70` | `467.41` | 1,044,982.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.40` | `895.59` | 2,002,891.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.50` | `347.23` | 777,263.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.80` | `670.93` | 1,502,074.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.30` | `446.97` | 1,001,348.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.80` | `336.81` | 756,753.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.90` | `445.71` | 1,001,455.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.50` | `668.12` | 1,502,267.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.00` | `465.72` | 1,047,866.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.50` | `337.68` | 759,956.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.70` | `889.87` | 2,002,837.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.50` | `472.19` | 1,063,144.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.70` | `1,108.98` | 2,497,083.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.70` | `1,333.64` | 3,004,297.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.60` | `1,776.72` | 4,005,794.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.60` | `689.06` | 1,553,557.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.80` | `344.01` | 775,673.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.90` | `504.86` | 1,138,413.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2258.50` | `430.01` | 971,182.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2259.60` | `1,035.23` | 2,339,212.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.00` | `504.75` | 1,141,232.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.90` | `2,171.06` | 4,910,721.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.30` | `350.98` | 794,719.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.70` | `336.44` | 761,925.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.20` | `1,497.31` | 3,396,206.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2276.00` | `4,210.48` | 9,583,052.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2276.30` | `504.89` | 1,149,276.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 16:52:59 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.80` | `2,111.45` | 4,815,789.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2474.03` | `22,046.99` | 54,544,867.42 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2561.00` | `400.00` | 1,024,400.00 USD | `TRIGGER_STOP` | `0x6a417e59a8` | `2026-10-30 16:52:59 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2581.00` | `400.00` | 1,032,400.00 USD | `TRIGGER_STOP` | `0xbef32b1382` | `2026-10-30 16:52:59 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2584.93` | `6,224.05` | 16,088,712.55 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 230,508,523.84 USD | `102,676.40` | `2322.74` | `2243.20` | `3706.83` | 7,982,389.31 USD | `+3.46%` | `5X Cross` |
| `6` | `0xb83d...6e36` | `SHORT` | 100,035,048.97 USD | `44,580.89` | `2375.30` | `2243.20` | `4644.50` | 5,858,218.07 USD | `+5.86%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,775,950.37 USD | `30,641.99` | `2610.31` | `2243.20` | `2121.85` | -11,209,224.67 USD | `-16.30%` | `10X Cross` |
| `10` | `0xde8d...9524` | `LONG` | 68,011,250.02 USD | `30,282.40` | `2134.45` | `2243.20` | `1786.11` | 3,374,919.44 USD | `+4.96%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 58,431,704.98 USD | `26,025.05` | `2518.71` | `2243.20` | `2129.13` | -7,118,017.11 USD | `-12.18%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,493,285.16 USD | `22,046.99` | `2271.09` | `2243.20` | `2475.38` | 577,612.14 USD | `+1.17%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,900,000.00 USD | `20,000.00` | `2228.11` | `2243.20` | `3187.81` | -337,672.32 USD | `-0.75%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 44,254,046.99 USD | `19,712.62` | `2402.53` | `2243.20` | `4220.92` | 3,106,207.80 USD | `+7.02%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,773,366.47 USD | `15,927.59` | `2410.19` | `2243.20` | `1782.13` | -2,615,253.18 USD | `-7.31%` | `6X Cross` |
| `34` | `0xefe4...194b` | `SHORT` | 33,919,010.62 USD | `15,108.89` | `2250.33` | `2243.20` | `2882.68` | 81,006.13 USD | `+0.24%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 33,209,018.23 USD | `14,795.73` | `2557.74` | `2243.20` | `3776.38` | 4,634,695.88 USD | `+13.96%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,973,168.17 USD | `14,687.58` | `2522.09` | `2243.20` | `3654.08` | 4,070,349.37 USD | `+12.34%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,310,775.00 USD | `13,950.00` | `2443.60` | `2243.20` | `5292.75` | 2,777,507.46 USD | `+8.87%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,927,116.00 USD | `12,888.00` | `2369.69` | `2243.20` | `1506.85` | -1,613,538.54 USD | `-5.58%` | `10X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 26,934,480.00 USD | `12,000.00` | `2419.91` | `2243.20` | `1519.99` | -2,104,552.39 USD | `-7.81%` | `20X Cross` |
| `45` | `0x2371...0883` | `LONG` | 26,926,800.00 USD | `12,000.00` | `2421.77` | `2243.20` | `1279.08` | -2,134,494.85 USD | `-7.93%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 24,706,000.00 USD | `11,000.00` | `2482.20` | `2243.20` | `1644.06` | -2,598,253.24 USD | `-10.52%` | `20X Cross` |
| `53` | `0xa9de...e049` | `LONG` | 24,695,000.00 USD | `11,000.00` | `2481.81` | `2243.20` | `1643.73` | -2,604,979.46 USD | `-10.55%` | `20X Cross` |
| `54` | `0x09dc...c094` | `LONG` | 24,694,670.00 USD | `11,000.00` | `2465.31` | `2243.20` | `1637.05` | -2,423,753.04 USD | `-9.81%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 24,690,600.00 USD | `11,000.00` | `2441.15` | `2243.20` | `1602.02` | -2,162,072.73 USD | `-8.76%` | `20X Cross` |
| `62` | `0xecb6...2b00` | `SHORT` | 23,438,505.78 USD | `10,440.50` | `2238.79` | `2243.20` | `5514.74` | -64,370.51 USD | `-0.27%` | `15X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,487,484.15 USD | `10,016.88` | `2162.83` | `2243.20` | `1554.91` | 822,682.10 USD | `+3.66%` | `10X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,449,700.00 USD | `10,000.00` | `2719.35` | `2243.20` | `1720.58` | -4,743,848.52 USD | `-21.13%` | `20X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,445,400.00 USD | `10,000.00` | `1765.80` | `2243.20` | `1723.11` | 4,787,342.55 USD | `+21.33%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,064,283.77 USD | `9,823.81` | `2427.28` | `2243.20` | `1759.42` | -1,780,866.83 USD | `-8.07%` | `25X Cross` |
| `83` | `0xf517...c032` | `SHORT` | 20,932,986.07 USD | `9,326.35` | `2202.91` | `2243.20` | `3158.90` | -387,847.85 USD | `-1.85%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,608,745.15 USD | `9,181.89` | `2549.39` | `2243.20` | `3894.91` | 2,799,532.24 USD | `+13.58%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,325,598.70 USD | `9,054.12` | `2493.89` | `2243.20` | `2761.20` | 2,254,408.56 USD | `+11.09%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,221,693.49 USD | `9,003.83` | `2003.01` | `2243.20` | `1414.92` | 2,186,914.62 USD | `+10.81%` | `5X Cross` |
| `105` | `0x0622...8088` | `SHORT` | 18,699,585.98 USD | `8,329.81` | `2233.13` | `2243.20` | `3375.94` | -97,998.85 USD | `-0.52%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,163,508.74 USD | `8,092.45` | `1658.44` | `2243.20` | `1930.17` | 4,742,644.21 USD | `+26.11%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,887,820.69 USD | `7,964.66` | `1626.99` | `2243.20` | `1843.90` | 4,929,377.62 USD | `+27.56%` | `16X Cross` |
| `122` | `0xec0b...b078` | `LONG` | 15,729,004.63 USD | `7,007.80` | `2065.97` | `2243.20` | `1059.94` | 1,251,075.04 USD | `+7.95%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,388,945.05 USD | `6,855.99` | `2383.33` | `2243.20` | `1116.59` | -951,143.72 USD | `-6.18%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,273,872.49 USD | `6,803.63` | `1862.69` | `2243.20` | `4193.80` | -2,600,767.10 USD | `-17.03%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,735,745.17 USD | `6,564.10` | `2447.40` | `2243.20` | `1669.67` | -1,329,277.57 USD | `-9.02%` | `3X Isolated` |
| `138` | `0x1ee7...edf5` | `LONG` | 14,598,350.00 USD | `6,500.00` | `2301.55` | `2243.20` | `2068.89` | -361,743.66 USD | `-2.48%` | `25X Cross` |
| `139` | `0xf78c...c581` | `LONG` | 14,594,362.31 USD | `6,500.22` | `2521.53` | `2243.20` | `1913.16` | -1,796,178.63 USD | `-12.31%` | `20X Cross` |
| `143` | `0x4e23...20c3` | `LONG` | 14,287,572.36 USD | `6,365.31` | `2228.10` | `2243.20` | `270.43` | 104,994.92 USD | `+0.73%` | `20X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,165,453.55 USD | `6,310.90` | `2390.33` | `2243.20` | `1866.60` | -919,711.07 USD | `-6.49%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,969,874.39 USD | `6,224.05` | `2258.00` | `2243.20` | `2584.96` | 84,041.72 USD | `+0.60%` | `20X Cross` |
| `154` | `0xec4a...cf62` | `LONG` | 13,620,788.20 USD | `6,068.52` | `2223.80` | `2243.20` | `1959.91` | 125,572.88 USD | `+0.92%` | `25X Cross` |
| `155` | `0xd9e7...4aff` | `LONG` | 13,470,000.00 USD | `6,000.00` | `2480.18` | `2243.20` | `1407.44` | -1,411,124.33 USD | `-10.48%` | `20X Cross` |
| `156` | `0x524e...0de0` | `LONG` | 13,465,800.00 USD | `6,000.00` | `2246.48` | `2243.20` | `2002.86` | -13,085.04 USD | `-0.10%` | `10X Cross` |
| `157` | `0xc179...e0c8` | `LONG` | 13,143,636.01 USD | `5,854.73` | `2294.94` | `2243.20` | `1209.07` | -292,636.17 USD | `-2.23%` | `10X Cross` |
| `161` | `0x0c4a...1b19` | `LONG` | 12,706,749.08 USD | `5,660.10` | `2373.06` | `2243.20` | `2081.49` | -725,009.04 USD | `-5.71%` | `25X Isolated` |
| `185` | `0x45ab...6cbc` | `LONG` | 11,051,496.91 USD | `4,920.96` | `2727.66` | `2243.20` | `1375.10` | -2,371,246.89 USD | `-21.46%` | `7X Cross` |
| `187` | `0x64b7...9da9` | `LONG` | 10,901,175.58 USD | `4,856.84` | `2604.61` | `2243.20` | `590.79` | -1,749,038.83 USD | `-16.04%` | `25X Cross` |
| `194` | `0xfb18...eb17` | `SHORT` | 10,702,136.47 USD | `4,768.16` | `2315.53` | `2243.20` | `2616.00` | 338,693.23 USD | `+3.16%` | `25X Cross` |
| `197` | `0x5559...d43b` | `SHORT` | 10,677,052.30 USD | `4,755.93` | `2262.69` | `2243.20` | `2740.33` | 84,153.58 USD | `+0.79%` | `25X Cross` |
| `202` | `0x7fda...17d1` | `LONG` | 10,390,963.08 USD | `4,628.55` | `2211.05` | `2243.20` | `0.000000` | 156,970.75 USD | `+1.51%` | `25X Cross` |
| `209` | `0xe091...6705` | `SHORT` | 10,107,000.45 USD | `4,500.00` | `2467.33` | `2243.20` | `2463.07` | 996,008.06 USD | `+9.85%` | `20X Cross` |
| `210` | `0x418a...8888` | `SHORT` | 10,102,320.00 USD | `4,500.00` | `2494.55` | `2243.20` | `2991.75` | 1,123,164.41 USD | `+11.12%` | `25X Cross` |
| `220` | `0xb829...3a81` | `LONG` | 9,866,443.35 USD | `4,394.91` | `2398.60` | `2243.20` | `1461.08` | -675,198.60 USD | `-6.84%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,448,479.07 USD | `4,209.61` | `1896.10` | `2243.20` | `3033.56` | -1,466,596.51 USD | `-15.52%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,392,982.09 USD | `4,184.01` | `2602.13` | `2243.20` | `3425.02` | 1,494,364.57 USD | `+15.91%` | `20X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 8,995,119.07 USD | `4,007.56` | `1796.39` | `2243.20` | `2585.51` | -1,795,968.98 USD | `-19.97%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,988,319.31 USD | `4,002.10` | `2382.44` | `2243.20` | `5104.41` | 546,464.84 USD | `+6.08%` | `20X Cross` |
| `254` | `0x3dc9...54b0` | `SHORT` | 8,982,504.25 USD | `3,999.69` | `2480.32` | `2243.20` | `6490.65` | 938,032.30 USD | `+10.44%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 8,979,880.00 USD | `4,000.00` | `1791.18` | `2243.20` | `3505.68` | -1,815,133.33 USD | `-20.21%` | `25X Cross` |
| `271` | `0x4b67...f4e7` | `LONG` | 8,581,228.82 USD | `3,820.84` | `2591.51` | `2243.20` | `1344.11` | -1,320,544.72 USD | `-15.39%` | `20X Cross` |
| `276` | `0x12d2...f97f` | `LONG` | 8,433,172.76 USD | `3,757.26` | `2446.50` | `2243.20` | `1771.85` | -758,993.63 USD | `-9.00%` | `20X Cross` |
| `297` | `0x8ae4...3d60` | `LONG` | 7,988,048.44 USD | `3,558.20` | `2482.21` | `2243.20` | `519.59` | -844,149.60 USD | `-10.57%` | `10X Cross` |
| `300` | `0x469e...58a5` | `SHORT` | 7,931,979.70 USD | `3,533.33` | `2203.63` | `2243.20` | `3073.88` | -145,816.61 USD | `-1.84%` | `25X Cross` |
| `306` | `0x218a...7da2` | `SHORT` | 7,782,543.18 USD | `3,465.07` | `2208.16` | `2243.20` | `3101.73` | -131,113.92 USD | `-1.68%` | `10X Cross` |
| `340` | `0x9c2a...f6a8` | `SHORT` | 6,740,993.13 USD | `3,002.39` | `2515.77` | `2243.20` | `2594.55` | 812,344.76 USD | `+12.05%` | `20X Cross` |
| `341` | `0xb823...9763` | `SHORT` | 6,734,910.00 USD | `3,000.00` | `2229.66` | `2243.20` | `3233.41` | -45,913.32 USD | `-0.68%` | `25X Cross` |
| `342` | `0x4a20...3c26` | `LONG` | 6,733,500.00 USD | `3,000.00` | `2428.72` | `2243.20` | `621.94` | -552,660.28 USD | `-8.21%` | `20X Cross` |
| `343` | `0x007d...67a0` | `LONG` | 6,733,500.00 USD | `3,000.00` | `2400.00` | `2243.20` | `1473.46` | -466,500.00 USD | `-6.93%` | `25X Cross` |
| `389` | `0x8328...f54a` | `SHORT` | 5,786,709.17 USD | `2,576.45` | `2292.01` | `2243.20` | `3279.25` | 118,562.12 USD | `+2.05%` | `25X Cross` |
| `395` | `0xed48...7c9b` | `SHORT` | 5,726,012.41 USD | `2,551.13` | `2460.02` | `2243.20` | `3238.22` | 549,834.00 USD | `+9.60%` | `20X Cross` |
| `398` | `0x1c98...7fc7` | `LONG` | 5,612,435.10 USD | `2,500.00` | `2452.60` | `2243.20` | `1916.65` | -519,086.46 USD | `-9.25%` | `10X Cross` |
| `399` | `0x970c...2a93` | `SHORT` | 5,612,250.00 USD | `2,500.00` | `2229.57` | `2243.20` | `5069.17` | -38,305.51 USD | `-0.68%` | `20X Cross` |
| `415` | `0xa445...329d` | `LONG` | 5,400,571.80 USD | `2,406.14` | `2354.86` | `2243.20` | `1761.09` | -265,543.48 USD | `-4.92%` | `25X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,353,594.87 USD | `2,385.21` | `2041.57` | `2243.20` | `2622.36` | -484,028.21 USD | `-9.04%` | `20X Cross` |
| `417` | `0x6749...ce07` | `SHORT` | 5,353,133.52 USD | `2,384.89` | `2220.92` | `2243.20` | `3615.61` | -56,470.49 USD | `-1.05%` | `20X Cross` |
| `418` | `0x645b...87b8` | `SHORT` | 5,343,045.22 USD | `2,379.98` | `2421.64` | `2243.20` | `11308.41` | 420,401.73 USD | `+7.87%` | `10X Cross` |
| `431` | `0x77ee...2902` | `SHORT` | 5,142,533.02 USD | `2,290.69` | `2476.53` | `2243.20` | `6113.18` | 530,439.21 USD | `+10.31%` | `25X Cross` |
| `450` | `0xd507...c948` | `SHORT` | 4,875,053.78 USD | `2,172.00` | `2387.49` | `2243.20` | `2600.25` | 310,587.25 USD | `+6.37%` | `5X Isolated` |
| `457` | `0x023a...2355` | `LONG` | 4,809,563.98 USD | `2,142.82` | `2328.93` | `2243.20` | `0.000000` | -180,939.87 USD | `-3.76%` | `25X Cross` |
| `461` | `0x382b...3e39` | `SHORT` | 4,780,735.71 USD | `2,129.54` | `2296.66` | `2243.20` | `4624.56` | 110,101.50 USD | `+2.30%` | `25X Cross` |
| `484` | `0xd911...961e` | `SHORT` | 4,581,896.26 USD | `2,041.39` | `2231.45` | `2243.20` | `3284.38` | -26,637.21 USD | `-0.58%` | `25X Cross` |
| `496` | `0x3453...b323` | `SHORT` | 4,492,076.47 USD | `2,000.12` | `2322.47` | `2243.20` | `2396.93` | 153,159.37 USD | `+3.41%` | `25X Cross` |
| `498` | `0xe02e...d78b` | `LONG` | 4,489,000.00 USD | `2,000.00` | `2228.11` | `2243.20` | `2171.60` | 32,776.53 USD | `+0.73%` | `25X Cross` |
| `503` | `0xf3dc...1672` | `SHORT` | 4,443,534.68 USD | `1,980.36` | `2240.44` | `2243.20` | `2789.56` | -6,647.13 USD | `-0.15%` | `20X Cross` |
| `507` | `0x7a6d...f79c` | `SHORT` | 4,425,881.90 USD | `1,971.44` | `2418.41` | `2243.20` | `2545.73` | 341,879.27 USD | `+7.72%` | `25X Cross` |
| `511` | `0xac48...3201` | `SHORT` | 4,411,777.46 USD | `1,964.37` | `2272.04` | `2243.20` | `3093.55` | 51,364.84 USD | `+1.16%` | `20X Cross` |
| `517` | `0x8376...9a1e` | `SHORT` | 4,290,782.97 USD | `1,910.50` | `2477.72` | `2243.20` | `3185.18` | 442,905.20 USD | `+10.32%` | `20X Cross` |
| `522` | `0x739c...cfb2` | `SHORT` | 4,265,899.00 USD | `1,900.00` | `2418.12` | `2243.20` | `2456.09` | 328,547.38 USD | `+7.70%` | `25X Cross` |
| `527` | `0x020c...5872` | `LONG` | 4,209,300.00 USD | `1,875.00` | `2230.70` | `2243.20` | `2173.00` | 26,726.73 USD | `+0.63%` | `25X Cross` |
| `548` | `0x7265...91a5` | `LONG` | 4,045,196.80 USD | `1,801.87` | `2533.96` | `2243.20` | `1987.12` | -520,669.65 USD | `-12.87%` | `20X Cross` |
| `549` | `0xbb34...1696` | `LONG` | 4,042,620.00 USD | `1,800.00` | `2313.95` | `2243.20` | `1956.17` | -122,498.23 USD | `-3.03%` | `25X Cross` |
| `550` | `0xc619...10f5` | `LONG` | 4,040,820.00 USD | `1,800.00` | `2313.55` | `2243.20` | `1790.41` | -123,575.83 USD | `-3.06%` | `25X Cross` |
| `563` | `0x91a9...3f70` | `SHORT` | 3,968,275.40 USD | `1,767.48` | `2156.23` | `2243.20` | `3652.19` | -157,171.32 USD | `-3.96%` | `4X Cross` |
| `571` | `0xbcd4...0dd2` | `SHORT` | 3,923,471.66 USD | `1,747.52` | `2233.24` | `2243.20` | `2753.44` | -20,815.44 USD | `-0.53%` | `25X Cross` |
| `575` | `0xb8eb...1dd5` | `SHORT` | 3,906,383.10 USD | `1,740.35` | `2233.05` | `2243.20` | `3276.83` | -20,096.03 USD | `-0.51%` | `25X Cross` |
| `597` | `0xfeec...4e9c` | `SHORT` | 3,797,434.03 USD | `1,691.81` | `2566.49` | `2243.20` | `2509.20` | 544,590.48 USD | `+14.34%` | `10X Cross` |
| `616` | `0xeee0...0b53` | `LONG` | 3,676,816.57 USD | `1,637.12` | `2468.64` | `2243.20` | `172.42` | -364,659.49 USD | `-9.92%` | `7X Cross` |
| `621` | `0x27b8...12fc` | `LONG` | 3,655,080.78 USD | `1,628.12` | `2468.73` | `2243.20` | `635.31` | -364,313.85 USD | `-9.97%` | `10X Cross` |
| `622` | `0x982b...4606` | `LONG` | 3,653,668.97 USD | `1,626.82` | `2575.24` | `2243.20` | `1547.40` | -535,784.10 USD | `-14.66%` | `5X Isolated` |
| `628` | `0x73d7...8be1` | `LONG` | 3,594,553.37 USD | `1,601.47` | `2410.40` | `2243.20` | `1766.91` | -265,625.55 USD | `-7.39%` | `25X Cross` |
| `630` | `0xad54...6203` | `LONG` | 3,586,279.07 USD | `1,597.45` | `2591.98` | `2243.20` | `2043.80` | -554,298.98 USD | `-15.46%` | `10X Isolated` |
| `637` | `0x880a...311c` | `LONG` | 3,543,459.97 USD | `1,578.40` | `2209.72` | `2243.20` | `0.000000` | 55,636.12 USD | `+1.57%` | `9X Cross` |
| `645` | `0x936c...bb0f` | `LONG` | 3,498,649.61 USD | `1,558.77` | `2232.92` | `2243.20` | `0.000000` | 18,038.64 USD | `+0.52%` | `20X Cross` |
| `655` | `0xe170...9300` | `SHORT` | 3,442,329.66 USD | `1,533.40` | `2076.39` | `2243.20` | `3093.59` | -258,380.16 USD | `-7.51%` | `25X Cross` |
| `659` | `0x4b86...df9d` | `SHORT` | 3,421,380.00 USD | `1,524.00` | `2287.40` | `2243.20` | `2759.61` | 64,617.60 USD | `+1.89%` | `9X Isolated` |
| `665` | `0x2e2b...2fab` | `LONG` | 3,384,302.55 USD | `1,507.38` | `2245.53` | `2243.20` | `1223.36` | -570.55 USD | `-0.02%` | `25X Cross` |
| `668` | `0xde6b...3361` | `LONG` | 3,367,455.00 USD | `1,500.00` | `2216.98` | `2243.20` | `2168.53` | 41,974.26 USD | `+1.25%` | `25X Cross` |
| `670` | `0x251f...6e5d` | `LONG` | 3,366,750.00 USD | `1,500.00` | `2346.68` | `2243.20` | `1880.61` | -153,280.49 USD | `-4.55%` | `20X Cross` |
| `689` | `0xb885...3c54` | `LONG` | 3,254,587.94 USD | `1,450.00` | `2274.34` | `2243.20` | `39.32` | -43,220.20 USD | `-1.33%` | `20X Cross` |
| `693` | `0xef70...a84c` | `SHORT` | 3,238,237.56 USD | `1,442.74` | `2424.73` | `2243.20` | `3255.61` | 260,033.26 USD | `+8.03%` | `25X Cross` |
| `701` | `0xbadb...9ee6` | `LONG` | 3,206,219.20 USD | `1,428.16` | `1936.00` | `2243.20` | `1059.00` | 441,297.55 USD | `+13.76%` | `20X Cross` |
| `759` | `0x53f8...ceff` | `LONG` | 3,027,944.69 USD | `1,348.65` | `2276.73` | `2243.20` | `0.000000` | -42,579.78 USD | `-1.41%` | `20X Cross` |
| `769` | `0xa0fb...96be` | `LONG` | 2,994,456.60 USD | `1,333.85` | `2276.68` | `2243.20` | `1529.56` | -42,306.85 USD | `-1.41%` | `3X Cross` |
| `803` | `0x1f16...6d07` | `LONG` | 2,841,537.00 USD | `1,266.00` | `2261.43` | `2243.20` | `1377.71` | -21,434.23 USD | `-0.75%` | `7X Cross` |
| `815` | `0xc435...c905` | `SHORT` | 2,803,008.00 USD | `1,248.00` | `2704.38` | `2243.20` | `3764.67` | 572,062.35 USD | `+20.41%` | `20X Cross` |
| `822` | `0x6859...7e1e` | `SHORT` | 2,776,791.70 USD | `1,237.15` | `2200.39` | `2243.20` | `4800.84` | -54,564.55 USD | `-1.97%` | `25X Cross` |
| `829` | `0x7277...0b98` | `SHORT` | 2,737,064.28 USD | `1,219.45` | `2206.05` | `2243.20` | `3380.96` | -46,876.48 USD | `-1.71%` | `20X Cross` |
| `830` | `0x7178...0854` | `LONG` | 2,735,705.85 USD | `1,218.63` | `2461.81` | `2243.20` | `1185.23` | -264,340.55 USD | `-9.66%` | `10X Cross` |
| `841` | `0xaaa1...ab8c` | `SHORT` | 2,695,080.00 USD | `1,200.00` | `2276.29` | `2243.20` | `2365.23` | 36,477.58 USD | `+1.35%` | `25X Isolated` |
| `855` | `0x07fd...689d` | `LONG` | 2,640,850.75 USD | `1,176.69` | `2416.34` | `2243.20` | `0.000000` | -202,449.19 USD | `-7.67%` | `25X Cross` |
| `879` | `0x0dd5...f6ee` | `LONG` | 2,535,572.37 USD | `1,129.43` | `2286.86` | `2243.20` | `1439.61` | -47,278.18 USD | `-1.86%` | `5X Cross` |
| `910` | `0x2f80...f203` | `SHORT` | 2,444,640.10 USD | `1,088.94` | `1984.00` | `2243.20` | `2959.66` | -284,172.91 USD | `-11.62%` | `20X Cross` |
| `919` | `0x8eb7...b90f` | `LONG` | 2,420,494.47 USD | `1,077.74` | `2396.38` | `2243.20` | `1880.93` | -162,183.57 USD | `-6.70%` | `5X Isolated` |
| `920` | `0x2b61...2f6c` | `SHORT` | 2,416,928.42 USD | `1,076.60` | `2681.75` | `2243.20` | `6268.46` | 470,244.32 USD | `+19.46%` | `10X Cross` |
| `938` | `0x30af...393e` | `SHORT` | 2,336,686.39 USD | `1,041.16` | `2252.26` | `2243.20` | `2296.91` | 8,295.94 USD | `+0.36%` | `25X Cross` |
| `963` | `0x1b2a...f7a6` | `LONG` | 2,302,873.99 USD | `1,025.37` | `2737.51` | `2243.20` | `882.07` | -504,085.95 USD | `-21.89%` | `10X Cross` |
| `977` | `0xfc27...9d9d` | `LONG` | 2,265,970.66 USD | `1,009.57` | `2237.33` | `2243.20` | `0.000000` | 7,233.15 USD | `+0.32%` | `25X Cross` |
| `979` | `0x001a...fef6` | `SHORT` | 2,261,041.69 USD | `1,007.33` | `2022.19` | `2243.20` | `3085.65` | -224,033.74 USD | `-9.91%` | `10X Cross` |
| `980` | `0x02aa...1806` | `SHORT` | 2,260,436.17 USD | `1,007.10` | `2654.68` | `2243.20` | `3612.70` | 413,095.93 USD | `+18.28%` | `20X Cross` |
| `984` | `0xdb3a...cf3b` | `LONG` | 2,251,515.65 USD | `1,003.22` | `2705.01` | `2243.20` | `0.000000` | -462,191.24 USD | `-20.53%` | `4X Cross` |
| `986` | `0x8c02...b73f` | `SHORT` | 2,245,210.00 USD | `1,000.00` | `2250.37` | `2243.20` | `8098.39` | 5,161.47 USD | `+0.23%` | `20X Cross` |
| `987` | `0x6463...42f5` | `SHORT` | 2,244,970.00 USD | `1,000.00` | `2223.43` | `2243.20` | `3705.58` | -21,535.05 USD | `-0.96%` | `5X Cross` |
| `988` | `0x5272...fcd9` | `SHORT` | 2,244,600.00 USD | `1,000.00` | `2241.82` | `2243.20` | `2830.76` | -2,775.51 USD | `-0.12%` | `5X Cross` |
| `989` | `0xd7b8...9f55` | `LONG` | 2,242,755.00 USD | `999.00` | `2195.00` | `2243.20` | `0.000000` | 49,950.00 USD | `+2.23%` | `15X Cross` |
| `1010` | `0xb002...ed8a` | `SHORT` | 2,162,316.59 USD | `962.78` | `2299.66` | `2243.20` | `4197.86` | 51,761.32 USD | `+2.39%` | `25X Cross` |
| `1025` | `0xb1ec...e86a` | `SHORT` | 2,096,214.27 USD | `933.64` | `2272.72` | `2243.20` | `13135.28` | 25,692.68 USD | `+1.23%` | `25X Cross` |
| `1054` | `0xede2...f971` | `LONG` | 2,052,594.54 USD | `914.31` | `2208.16` | `2243.20` | `1462.97` | 33,637.55 USD | `+1.64%` | `5X Cross` |
| `1056` | `0x9606...4e5d` | `SHORT` | 2,049,586.29 USD | `913.00` | `2478.70` | `2243.20` | `3535.55` | 213,467.31 USD | `+10.42%` | `20X Cross` |
| `1076` | `0x5f10...d49d` | `LONG` | 2,020,050.00 USD | `900.00` | `2249.83` | `2243.20` | `1813.91` | -4,803.47 USD | `-0.24%` | `25X Cross` |
| `1086` | `0x51f6...2b39` | `LONG` | 1,997,936.06 USD | `890.15` | `2226.49` | `2243.20` | `813.64` | 16,029.17 USD | `+0.80%` | `25X Cross` |
| `1090` | `0xb812...b5e0` | `LONG` | 1,989,319.55 USD | `886.12` | `2263.21` | `2243.20` | `1112.20` | -16,166.82 USD | `-0.81%` | `25X Cross` |
| `1164` | `0x2828...93a0` | `LONG` | 1,884,906.49 USD | `839.60` | `2242.41` | `2243.20` | `2192.53` | 2,174.30 USD | `+0.12%` | `25X Cross` |
| `1166` | `0x6f11...0389` | `SHORT` | 1,882,967.70 USD | `839.00` | `2333.39` | `2243.20` | `2962.32` | 74,747.37 USD | `+3.97%` | `25X Cross` |
| `1167` | `0xcd27...52a8` | `LONG` | 1,878,946.59 USD | `837.21` | `2553.56` | `2243.20` | `1403.21` | -258,918.19 USD | `-13.78%` | `2X Cross` |
| `1227` | `0x7737...bf66` | `SHORT` | 1,795,452.84 USD | `799.79` | `2494.83` | `2243.20` | `24970.77` | 199,893.19 USD | `+11.13%` | `15X Cross` |
| `1228` | `0x04a9...95aa` | `LONG` | 1,795,440.00 USD | `800.00` | `2595.13` | `2243.20` | `1877.40` | -280,666.74 USD | `-15.63%` | `5X Cross` |
| `1264` | `0x458d...ab3b` | `LONG` | 1,740,081.76 USD | `774.75` | `2740.41` | `2243.20` | `1886.96` | -383,047.42 USD | `-22.01%` | `3X Isolated` |
| `1318` | `0xaa53...9cb7` | `LONG` | 1,639,313.76 USD | `730.34` | `2389.70` | `2243.20` | `1960.06` | -105,975.88 USD | `-6.46%` | `20X Cross` |
| `1319` | `0x3fc5...c0c1` | `SHORT` | 1,638,833.11 USD | `729.92` | `2702.11` | `2243.20` | `4627.01` | 333,509.09 USD | `+20.35%` | `25X Cross` |
| `1336` | `0xa189...94d7` | `SHORT` | 1,615,992.87 USD | `719.98` | `2691.84` | `2243.20` | `2914.86` | 322,079.80 USD | `+19.93%` | `25X Cross` |
| `1349` | `0x2f93...4404` | `LONG` | 1,587,948.08 USD | `707.47` | `1700.45` | `2243.20` | `1368.60` | 384,921.71 USD | `+24.24%` | `4X Isolated` |
| `1361` | `0x5605...fe0f` | `SHORT` | 1,576,291.32 USD | `702.14` | `2566.90` | `2243.20` | `3065.21` | 226,041.33 USD | `+14.34%` | `20X Cross` |
| `1364` | `0x26e6...6b28` | `LONG` | 1,572,130.00 USD | `700.00` | `1835.24` | `2243.20` | `2043.03` | 287,458.47 USD | `+18.28%` | `20X Cross` |
| `1367` | `0x0deb...0bc5` | `LONG` | 1,571,220.00 USD | `700.00` | `2071.05` | `2243.20` | `1597.19` | 121,484.21 USD | `+7.73%` | `20X Cross` |
| `1403` | `0x7b22...8a34` | `LONG` | 1,536,744.48 USD | `684.73` | `2228.49` | `2243.20` | `2181.59` | 10,820.91 USD | `+0.70%` | `25X Cross` |
| `1413` | `0x248e...6be2` | `SHORT` | 1,528,663.61 USD | `680.93` | `2282.89` | `2243.20` | `3432.78` | 25,822.06 USD | `+1.69%` | `20X Cross` |
| `1415` | `0xdbd1...29dd` | `SHORT` | 1,527,863.99 USD | `680.70` | `3030.57` | `2243.20` | `3771.76` | 535,057.14 USD | `+35.02%` | `6X Cross` |
| `1422` | `0x71e5...be04` | `LONG` | 1,521,090.90 USD | `677.67` | `2727.27` | `2243.20` | `1470.74` | -327,094.71 USD | `-21.50%` | `20X Cross` |
| `1427` | `0xa70a...4be9` | `SHORT` | 1,519,325.98 USD | `676.90` | `2238.95` | `2243.20` | `4276.47` | -3,777.13 USD | `-0.25%` | `20X Cross` |
| `1435` | `0x0b23...f37b` | `LONG` | 1,515,354.75 USD | `675.00` | `2238.15` | `2243.20` | `594.43` | 4,598.11 USD | `+0.30%` | `5X Cross` |
| `1446` | `0x0a97...347d` | `SHORT` | 1,500,445.74 USD | `668.47` | `2238.50` | `2243.20` | `3410.96` | -4,074.18 USD | `-0.27%` | `20X Cross` |
| `1452` | `0x6e6f...82a6` | `SHORT` | 1,491,098.78 USD | `664.39` | `2237.33` | `2243.20` | `3644.91` | -4,627.24 USD | `-0.31%` | `20X Cross` |
| `1462` | `0x0cac...6170` | `SHORT` | 1,475,758.75 USD | `657.50` | `2146.55` | `2243.20` | `2839.20` | -64,396.55 USD | `-4.36%` | `20X Cross` |
| `1494` | `0xf00e...fe3d` | `SHORT` | 1,443,008.45 USD | `642.88` | `2333.21` | `2243.20` | `2459.02` | 56,969.52 USD | `+3.95%` | `20X Cross` |
| `1495` | `0xb15b...dbae` | `SHORT` | 1,442,669.72 USD | `642.64` | `2290.80` | `2243.20` | `2322.95` | 29,497.76 USD | `+2.04%` | `25X Cross` |
| `1502` | `0xffb2...5ed6` | `SHORT` | 1,438,457.39 USD | `640.77` | `2672.96` | `2243.20` | `2492.84` | 274,290.96 USD | `+19.07%` | `20X Cross` |
| `1511` | `0x8505...1821` | `SHORT` | 1,422,797.10 USD | `633.96` | `2239.93` | `2243.20` | `3910.19` | -2,765.50 USD | `-0.19%` | `20X Cross` |
| `1536` | `0xfce0...f4c0` | `SHORT` | 1,400,112.96 USD | `623.60` | `3129.61` | `2243.20` | `2807.80` | 551,513.63 USD | `+39.39%` | `20X Cross` |
| `1583` | `0x7050...5fff` | `SHORT` | 1,349,577.80 USD | `601.11` | `2245.52` | `2243.20` | `3296.36` | 222.31 USD | `+0.02%` | `25X Cross` |
| `1584` | `0xad02...eb65` | `LONG` | 1,347,971.91 USD | `600.62` | `2460.69` | `2243.20` | `1078.66` | -129,968.64 USD | `-9.64%` | `5X Cross` |
| `1585` | `0x638f...f5f0` | `LONG` | 1,346,700.00 USD | `600.00` | `4011.50` | `2243.20` | `427.92` | -1,060,203.53 USD | `-78.73%` | `25X Cross` |
| `1659` | `0xfb99...37f3` | `LONG` | 1,269,699.58 USD | `565.34` | `2362.35` | `2243.20` | `1253.64` | -65,836.78 USD | `-5.19%` | `3X Cross` |
| `1675` | `0x844b...7f42` | `SHORT` | 1,259,388.90 USD | `561.00` | `2026.17` | `2243.20` | `2995.40` | -122,705.49 USD | `-9.74%` | `25X Cross` |
| `1690` | `0xabe6...1d99` | `SHORT` | 1,247,950.98 USD | `556.00` | `2484.68` | `2243.20` | `3119.61` | 133,544.91 USD | `+10.70%` | `20X Cross` |
| `1701` | `0xbef3...0d3e` | `LONG` | 1,239,311.32 USD | `552.33` | `2237.93` | `2243.20` | `2078.71` | 3,238.35 USD | `+0.26%` | `20X Cross` |
| `1704` | `0x6a41...a3b9` | `LONG` | 1,236,085.96 USD | `550.69` | `2237.64` | `2243.20` | `2084.06` | 3,827.95 USD | `+0.31%` | `20X Cross` |
| `1705` | `0x9599...c60a` | `SHORT` | 1,235,159.57 USD | `550.30` | `2241.99` | `2243.20` | `9405.07` | -1,379.05 USD | `-0.11%` | `20X Cross` |
| `1707` | `0x825c...465e` | `LONG` | 1,234,475.00 USD | `550.00` | `2208.12` | `2243.20` | `1189.25` | 20,005.50 USD | `+1.62%` | `4X Cross` |
| `1712` | `0xad21...fb6a` | `LONG` | 1,228,315.87 USD | `547.26` | `2565.80` | `2243.20` | `1732.60` | -175,837.13 USD | `-14.32%` | `6X Cross` |
| `1750` | `0x2e30...4cb5` | `SHORT` | 1,187,282.14 USD | `528.97` | `2315.37` | `2243.20` | `11676.11` | 37,491.53 USD | `+3.16%` | `2X Cross` |
| `1787` | `0x6dae...90de` | `SHORT` | 1,161,251.13 USD | `517.05` | `2292.28` | `2243.20` | `3817.00` | 23,982.29 USD | `+2.07%` | `25X Cross` |
| `1808` | `0xfc66...ca06` | `SHORT` | 1,146,932.33 USD | `510.89` | `2275.19` | `2243.20` | `55012.79` | 15,449.26 USD | `+1.35%` | `20X Cross` |
| `1817` | `0x0089...2410` | `SHORT` | 1,138,737.20 USD | `507.35` | `2308.88` | `2243.20` | `3403.17` | 32,663.06 USD | `+2.87%` | `20X Cross` |
| `1839` | `0x4044...794c` | `LONG` | 1,122,950.00 USD | `500.00` | `2260.80` | `2243.20` | `0.000000` | -7,450.00 USD | `-0.66%` | `25X Cross` |
| `1841` | `0x6936...9417` | `SHORT` | 1,122,605.00 USD | `500.00` | `2315.11` | `2243.20` | `2358.71` | 34,950.21 USD | `+3.11%` | `25X Isolated` |
| `1842` | `0x89b2...9ca6` | `LONG` | 1,122,480.00 USD | `500.00` | `2363.45` | `2243.20` | `1622.44` | -59,247.42 USD | `-5.28%` | `25X Cross` |
| `1844` | `0xb322...d51f` | `SHORT` | 1,122,250.00 USD | `500.00` | `2268.03` | `2243.20` | `3739.78` | 11,766.32 USD | `+1.05%` | `20X Cross` |
| `1845` | `0xe282...df29` | `LONG` | 1,122,150.00 USD | `500.00` | `2309.84` | `2243.20` | `2045.11` | -32,774.21 USD | `-2.92%` | `10X Isolated` |
| `1846` | `0xa559...ff95` | `LONG` | 1,121,900.00 USD | `500.00` | `2260.68` | `2243.20` | `1061.91` | -8,444.36 USD | `-0.75%` | `20X Cross` |
| `1850` | `0x7298...7d6c` | `SHORT` | 1,118,793.51 USD | `498.15` | `3426.75` | `2243.20` | `5421.42` | 588,242.31 USD | `+52.58%` | `20X Cross` |
| `1862` | `0x9c68...7783` | `SHORT` | 1,107,919.99 USD | `493.31` | `2273.58` | `2243.20` | `3890.10` | 13,659.26 USD | `+1.23%` | `25X Cross` |
| `1871` | `0x404c...5f03` | `SHORT` | 1,099,548.41 USD | `489.79` | `2671.94` | `2243.20` | `4937.66` | 209,131.15 USD | `+19.02%` | `20X Cross` |
| `1877` | `0x321f...1c84` | `SHORT` | 1,095,545.77 USD | `488.02` | `2370.09` | `2243.20` | `3047.05` | 61,098.83 USD | `+5.58%` | `10X Cross` |
| `1880` | `0x94b6...e5b3` | `SHORT` | 1,090,940.57 USD | `486.05` | `2260.75` | `2243.20` | `2370.95` | 7,902.02 USD | `+0.72%` | `25X Cross` |
| `1928` | `0x0903...6f81` | `LONG` | 1,044,052.93 USD | `465.08` | `2236.70` | `2243.20` | `1923.96` | 3,812.27 USD | `+0.37%` | `25X Cross` |
| `1935` | `0x82c6...fe42` | `LONG` | 1,038,409.62 USD | `462.50` | `2501.38` | `2243.20` | `2053.45` | -118,480.94 USD | `-11.41%` | `5X Isolated` |
| `1942` | `0xe330...77a1` | `SHORT` | 1,035,350.12 USD | `461.20` | `2206.97` | `2243.20` | `6446.97` | -17,492.76 USD | `-1.69%` | `20X Cross` |
| `1987` | `0x617e...0f97` | `SHORT` | 1,013,943.00 USD | `451.75` | `2205.60` | `2243.20` | `3332.35` | -17,572.74 USD | `-1.73%` | `10X Cross` |
| `1992` | `0xae55...2236` | `LONG` | 1,010,025.00 USD | `450.00` | `2510.21` | `2243.20` | `0.000000` | -119,572.50 USD | `-11.84%` | `25X Cross` |
| `2000` | `0xf71a...7215` | `LONG` | 1,005,070.63 USD | `447.91` | `2223.27` | `2243.20` | `1092.03` | 9,236.35 USD | `+0.92%` | `25X Cross` |
| `2010` | `0xac26...a9c7` | `SHORT` | 1,001,142.84 USD | `446.04` | `2192.58` | `2243.20` | `8635.39` | -23,156.64 USD | `-2.31%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2553.00` | 4,921.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.92K USD at 2553.0000 USD [API] | `2026-10-07 13:39:04` |
| `ANNOUNCEMENT` | `INFO` | `2553.20` | 15,355.71 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 15.36K USD at 2553.2000 USD [API] | `2026-10-07 13:39:04` |
| `ANNOUNCEMENT` | `INFO` | `2338.40` | 43,486.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 43.49K USD at 2338.4000 USD [API] | `2026-10-29 17:41:19` |
| `ANNOUNCEMENT` | `INFO` | `2380.80` | 43.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2380.8000 USD [API] | `2026-10-22 16:45:54` |
| `ANNOUNCEMENT` | `INFO` | `2330.90` | 40,043.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.04K USD at 2330.9000 USD [API] | `2026-10-29 18:31:28` |
| `ANNOUNCEMENT` | `INFO` | `2327.50` | 60,399.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 60.40K USD at 2327.5000 USD [API] | `2026-10-29 18:35:32` |
| `ANNOUNCEMENT` | `INFO` | `2430.50` | 11,757.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.76K USD at 2430.5000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.50` | 278.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.28K USD at 2430.5000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.50` | 23.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2430.5000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.60` | 11,151.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.15K USD at 2430.6000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.60` | 38,494.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 38.49K USD at 2430.6000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.70` | 607.67 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.61K USD at 2430.7000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.80` | 29.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2430.8000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2430.90` | 25,158.11 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 25.16K USD at 2430.9000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2431.00` | 20.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2431.0000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2431.00` | 9,706.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 9.71K USD at 2431.0000 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `2323.80` | 24,580.23 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 24.58K USD at 2323.8000 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `2310.30` | 21,500.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 21.50K USD at 2310.3000 USD [API] | `2026-10-25 23:30:50` |
| `ANNOUNCEMENT` | `INFO` | `2328.00` | 11,998.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 12.00K USD at 2328.0000 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `2335.30` | 96,002.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 96.00K USD at 2335.3000 USD [API] | `2026-10-29 19:59:25` |
| `ANNOUNCEMENT` | `INFO` | `2308.50` | 1,079.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.08K USD at 2308.5000 USD [API] | `2026-10-29 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `2310.50` | 48.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.05K USD at 2310.5000 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `2310.50` | 1,351.87 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.35K USD at 2310.5000 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `2310.50` | 1,093.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.09K USD at 2310.5000 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `2388.20` | 89,007.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 89.01K USD at 2388.2000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2295.00` | 118,879.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 118.88K USD at 2295.0000 USD [API] | `2026-10-29 20:36:25` |
| `ANNOUNCEMENT` | `INFO` | `2295.00` | 44,561.56 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 44.56K USD at 2295.0000 USD [API] | `2026-10-29 20:36:25` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 17,890.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 17.89K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 34,671.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 34.67K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 4,473.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.47K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2301.40` | 18,156.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.16K USD at 2301.4000 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `2313.50` | 16,143.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 16.14K USD at 2313.5000 USD [API] | `2026-10-29 20:04:17` |
| `ANNOUNCEMENT` | `INFO` | `2316.30` | 9,807.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 9.81K USD at 2316.3000 USD [API] | `2026-10-29 20:03:59` |
| `ANNOUNCEMENT` | `INFO` | `2316.30` | 2,479.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.48K USD at 2316.3000 USD [API] | `2026-10-29 20:03:59` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2275.30` (Vol: 35,200,000.00 USD, Dist: `+1.52%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.98%`)
  * 48H Horizon: Short MP=`2270.12` (Vol: 35,900,000.00 USD, Dist: `+1.29%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.00%`)
  * 3D Horizon: Short MP=`2270.12` (Vol: 35,900,000.00 USD, Dist: `+1.29%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.00%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.17%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.94%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 80,660.00 USD | 784,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 6,190.00 USD | 784,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 70,920.00 USD | 784,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 108,780.00 USD | 784,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 19,900.00 USD | 784,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 65,690.00 USD | 784,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 1,830,000.00 USD | 784,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 38,160.00 USD | 782,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 8,790.00 USD | 782,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 13,630.00 USD | 782,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 106,590.00 USD | 782,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 150,140.00 USD | 782,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 12,360.00 USD | 782,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 2,850,000.00 USD | 782,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 554,380.00 USD | 779,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 1,830,000.00 USD | 778,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 57,360.00 USD | 776,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 1,080,000.00 USD | 776,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 15,580.00 USD | 775,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 339,590.00 USD | 775,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 51,390.00 USD | 775,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 105,210.00 USD | 775,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 15,070.00 USD | 775,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 32,820.00 USD | 775,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 11,490.00 USD | 775,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 51,810.00 USD | 775,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,810.00 USD | 775,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 405,280.00 USD | 775,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 66,120.00 USD | 774,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 7,820.00 USD | 774,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 38,260.00 USD | 774,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 7,720.00 USD | 774,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 4,390.00 USD | 774,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 20,660.00 USD | 774,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 84,530.00 USD | 774,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 47,650.00 USD | 774,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 98,180.00 USD | 774,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 845,300.00 USD | 774,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 88,670.00 USD | 773,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 92,370.00 USD | 773,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 95,080.00 USD | 773,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 85,930.00 USD | 773,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 404,280.00 USD | 773,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,200,000.00 USD | 772,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 115,430.00 USD | 771,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 131,400.00 USD | 771,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 166,190.00 USD | 771,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 168,790.00 USD | 771,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 84,000.00 USD | 770,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 62,450.00 USD | 770,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 27,560.00 USD | 770,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 483,050.00 USD | 770,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 144,850.00 USD | 770,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 215,460.00 USD | 770,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 72,670.00 USD | 769,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 21,150.00 USD | 769,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 345,840.00 USD | 769,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 54,250.00 USD | 769,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 275,540.00 USD | 769,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 396,790.00 USD | 769,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 9,530,000.00 USD | 768,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 127,940.00 USD | 759,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 671,120.00 USD | 759,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 868,060.00 USD | 758,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 38,740.00 USD | 757,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 137,420.00 USD | 757,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 7,860,000.00 USD | 757,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 176,230.00 USD | 749,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 1,740,000.00 USD | 749,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 214,200.00 USD | 747,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 537,840.00 USD | 747,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 51,500.00 USD | 746,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 1,560,000.00 USD | 746,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 1,270,000.00 USD | 745,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 7,200,000.00 USD | 743,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 2,020,000.00 USD | 736,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 78,020.00 USD | 734,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 432,140.00 USD | 734,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 138,120.00 USD | 734,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 56,730.00 USD | 734,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 1,260,000.00 USD | 733,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 289,300.00 USD | 732,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,490,000.00 USD | 732,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 474,130.00 USD | 716,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 339,640.00 USD | 716,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 114,060.00 USD | 716,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 186,060.00 USD | 716,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 492,940.00 USD | 715,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 5,500,000.00 USD | 715,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 188,030.00 USD | 709,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 106,050.00 USD | 709,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,260,000.00 USD | 709,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 8,980,000.00 USD | 708,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 485,050.00 USD | 699,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 913,010.00 USD | 698,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 22,730,000.00 USD | 697,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 229,690.00 USD | 675,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 561,450.00 USD | 674,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 782,000.00 USD | 674,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 1,730,000.00 USD | 673,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 661,960.00 USD | 671,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 8,450,000.00 USD | 671,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,730,000.00 USD | 662,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 318,770.00 USD | 657,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 19,400,000.00 USD | 656,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 498,390.00 USD | 637,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 18,790,000.00 USD | 636,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 2,460,000.00 USD | 618,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 902,770.00 USD | 615,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 4,110,000.00 USD | 614,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 16,090,000.00 USD | 610,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 576,720.00 USD | 594,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 949,290.00 USD | 593,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 667,450.00 USD | 592,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 2,010,000.00 USD | 592,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,080,000.00 USD | 590,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 1,080,000.00 USD | 572,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,720,000.00 USD | 571,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,670,000.00 USD | 569,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 37,490,000.00 USD | 550,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 859,690.00 USD | 513,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 11,660,000.00 USD | 512,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 1,030,000.00 USD | 500,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 573,580.00 USD | 499,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 756,150.00 USD | 499,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,020,000.00 USD | 498,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 511,390.00 USD | 497,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 36,690,000.00 USD | 496,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,580,000.00 USD | 460,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 837,560.00 USD | 458,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 480,300.00 USD | 457,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 7,660,000.00 USD | 457,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 24,770,000.00 USD | 449,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 86,890,000.00 USD | 424,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 482,950.00 USD | 337,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 3,030,000.00 USD | 337,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 507,190.00 USD | 334,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,320,000.00 USD | 333,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,060,000.00 USD | 332,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 16,200,000.00 USD | 331,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,050,000.00 USD | 315,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 15,820,000.00 USD | 314,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 7,240,000.00 USD | 298,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 5,540,000.00 USD | 291,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 538,030.00 USD | 285,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,420,000.00 USD | 285,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 18,440,000.00 USD | 283,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 17,280,000.00 USD | 265,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 876,330.00 USD | 247,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 5,430,000.00 USD | 247,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 13,680,000.00 USD | 241,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 2,720,000.00 USD | 227,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1972.30` | 868,540,000.00 USD | 868,540,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 3,020,000.00 USD | 225,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.10` | 868,410,000.00 USD | 868,410,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1977.90` | 868,360,000.00 USD | 868,360,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.50` | 866,120,000.00 USD | 866,120,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,560,000.00 USD | 222,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.30` | 865,920,000.00 USD | 865,920,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.10` | 862,190,000.00 USD | 862,190,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.90` | 860,370,000.00 USD | 860,370,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.70` | 857,660,000.00 USD | 857,660,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 645,300.00 USD | 216,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1997.50` | 856,850,000.00 USD | 856,850,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1997.60` | 754,480,000.00 USD | 754,480,000.00 USD | 206,020.00 USD | 86,340.00 USD | 328,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.10` | 753,860,000.00 USD | 753,860,000.00 USD | 27,360.00 USD | 25,630.00 USD | 586,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2002.60` | 753,220,000.00 USD | 753,220,000.00 USD | 942,390.00 USD | 700,600.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2003.10` | 855,510,000.00 USD | 855,510,000.00 USD | 0.00 USD | 266,430.00 USD | 617,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 13,400,000.00 USD | 216,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.10` | 750,400,000.00 USD | 750,400,000.00 USD | 773,690.00 USD | 255,310.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.90` | 854,630,000.00 USD | 854,630,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.60` | 749,360,000.00 USD | 749,360,000.00 USD | 0.00 USD | 383,650.00 USD | 281,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.70` | 854,150,000.00 USD | 854,150,000.00 USD | 807,770.00 USD | 0.00 USD | 380,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.10` | 748,700,000.00 USD | 748,700,000.00 USD | 460,200.00 USD | 638,030.00 USD | 374,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.50` | 852,960,000.00 USD | 852,960,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.60` | 747,220,000.00 USD | 747,220,000.00 USD | 348,530.00 USD | 266,130.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,050,000.00 USD | 202,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.10` | 746,580,000.00 USD | 746,580,000.00 USD | 413,060.00 USD | 159,880.00 USD | 202,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2017.10` | 852,010,000.00 USD | 852,010,000.00 USD | 62,110.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2017.60` | 745,810,000.00 USD | 745,810,000.00 USD | 1,140,000.00 USD | 1,500,000.00 USD | 559,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2019.90` | 851,930,000.00 USD | 851,930,000.00 USD | 1,020,000.00 USD | 466,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.10` | 742,610,000.00 USD | 742,610,000.00 USD | 1,340,000.00 USD | 2,190,000.00 USD | 696,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.60` | 738,380,000.00 USD | 738,380,000.00 USD | 1,840,000.00 USD | 628,480.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.70` | 850,440,000.00 USD | 850,440,000.00 USD | 1,890,000.00 USD | 957,590.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,010,000.00 USD | 200,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.10` | 734,030,000.00 USD | 734,030,000.00 USD | 595,510.00 USD | 1,010,000.00 USD | 240,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2025.50` | 846,040,000.00 USD | 846,040,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.60` | 732,180,000.00 USD | 732,180,000.00 USD | 2,550,000.00 USD | 1,160,000.00 USD | 167,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.30` | 845,870,000.00 USD | 845,870,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.10` | 728,310,000.00 USD | 728,310,000.00 USD | 307,680.00 USD | 366,120.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.10` | 844,730,000.00 USD | 844,730,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.60` | 726,530,000.00 USD | 726,530,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.90` | 840,160,000.00 USD | 840,160,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 598,780.00 USD | 199,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.10` | 722,970,000.00 USD | 722,970,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2036.70` | 838,810,000.00 USD | 838,810,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.60` | 721,630,000.00 USD | 721,630,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2039.50` | 838,480,000.00 USD | 838,480,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.10` | 720,400,000.00 USD | 720,400,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.60` | 719,650,000.00 USD | 719,650,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,820,000.00 USD | 198,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.10` | 718,840,000.00 USD | 718,840,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2045.10` | 837,020,000.00 USD | 837,020,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.60` | 718,820,000.00 USD | 718,820,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.10` | 717,990,000.00 USD | 717,990,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.70` | 836,720,000.00 USD | 836,720,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.50` | 836,500,000.00 USD | 836,500,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,880,000.00 USD | 192,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.10` | 716,880,000.00 USD | 716,880,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2059.10` | 834,220,000.00 USD | 834,220,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.10` | 716,520,000.00 USD | 716,520,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.90` | 833,870,000.00 USD | 833,870,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.60` | 715,770,000.00 USD | 715,770,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.70` | 828,620,000.00 USD | 828,620,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 14,120,000.00 USD | 188,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.10` | 715,690,000.00 USD | 715,690,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.50` | 826,150,000.00 USD | 826,150,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.60` | 714,080,000.00 USD | 714,080,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.10` | 713,390,000.00 USD | 713,390,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.30` | 824,510,000.00 USD | 824,510,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.60` | 713,010,000.00 USD | 713,010,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 816,950,000.00 USD | 816,950,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,520,000.00 USD | 174,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.10` | 711,990,000.00 USD | 711,990,000.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2075.90` | 809,870,000.00 USD | 809,870,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.60` | 711,960,000.00 USD | 711,960,000.00 USD | 354,080.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.70` | 797,360,000.00 USD | 797,360,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.10` | 711,580,000.00 USD | 711,580,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.50` | 787,410,000.00 USD | 787,410,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.60` | 711,270,000.00 USD | 711,270,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.30` | 780,510,000.00 USD | 780,510,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,940,000.00 USD | 170,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.10` | 710,240,000.00 USD | 710,240,000.00 USD | 528,660.00 USD | 200,510.00 USD | 820,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.10` | 773,120,000.00 USD | 773,120,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.60` | 708,690,000.00 USD | 708,690,000.00 USD | 324,560.00 USD | 170,940.00 USD | 302,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.90` | 764,430,000.00 USD | 764,430,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.10` | 707,890,000.00 USD | 707,890,000.00 USD | 461,140.00 USD | 216,470.00 USD | 251,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.60` | 706,960,000.00 USD | 706,960,000.00 USD | 587,740.00 USD | 226,930.00 USD | 199,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.70` | 756,190,000.00 USD | 756,190,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,740,000.00 USD | 156,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.10` | 705,950,000.00 USD | 705,950,000.00 USD | 1,370,000.00 USD | 838,640.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2095.50` | 744,560,000.00 USD | 744,560,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.60` | 702,660,000.00 USD | 702,660,000.00 USD | 87,950.00 USD | 672,980.00 USD | 555,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2098.30` | 739,050,000.00 USD | 739,050,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.10` | 701,340,000.00 USD | 701,340,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.10` | 731,430,000.00 USD | 731,430,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.60` | 700,050,000.00 USD | 700,050,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.90` | 726,160,000.00 USD | 726,160,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,400,000.00 USD | 154,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.10` | 699,140,000.00 USD | 699,140,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2106.70` | 721,960,000.00 USD | 721,960,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.60` | 693,710,000.00 USD | 693,710,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.50` | 718,250,000.00 USD | 718,250,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.10` | 692,490,000.00 USD | 692,490,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.30` | 706,930,000.00 USD | 706,930,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.60` | 692,390,000.00 USD | 692,390,000.00 USD | 902,600.00 USD | 360,140.00 USD | 221,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,120,000.00 USD | 152,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.10` | 690,900,000.00 USD | 690,900,000.00 USD | 202,800.00 USD | 411,610.00 USD | 962,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2115.10` | 697,820,000.00 USD | 697,820,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.60` | 689,330,000.00 USD | 689,330,000.00 USD | 4,750,000.00 USD | 4,080,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.90` | 691,750,000.00 USD | 691,750,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.10` | 680,200,000.00 USD | 680,200,000.00 USD | 3,950,000.00 USD | 22,470.00 USD | 645,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.70` | 680,200,000.00 USD | 680,200,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.60` | 675,580,000.00 USD | 675,580,000.00 USD | 4,520,000.00 USD | 3,800,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.50` | 665,540,000.00 USD | 665,540,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,840,000.00 USD | 151,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.10` | 665,410,000.00 USD | 665,410,000.00 USD | 6,940,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2126.30` | 649,260,000.00 USD | 649,260,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.60` | 654,530,000.00 USD | 654,530,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.10` | 637,330,000.00 USD | 637,330,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.10` | 645,140,000.00 USD | 645,140,000.00 USD | 1,250,000.00 USD | 172,040.00 USD | 794,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.90` | 630,190,000.00 USD | 630,190,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.60` | 642,920,000.00 USD | 642,920,000.00 USD | 81,820.00 USD | 284,820.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.70` | 625,040,000.00 USD | 625,040,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 1,620,000.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.10` | 641,000,000.00 USD | 641,000,000.00 USD | 2,560,000.00 USD | 2,610,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 621,730,000.00 USD | 621,730,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.60` | 634,290,000.00 USD | 634,290,000.00 USD | 889,780.00 USD | 2,180,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.10` | 629,270,000.00 USD | 629,270,000.00 USD | 1,990,000.00 USD | 749,480.00 USD | 758,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 615,630,000.00 USD | 615,630,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.60` | 625,770,000.00 USD | 625,770,000.00 USD | 873,550.00 USD | 3,390,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.10` | 608,090,000.00 USD | 608,090,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 333,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,990,000.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.10` | 620,410,000.00 USD | 620,410,000.00 USD | 2,780,000.00 USD | 2,360,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.90` | 604,750,000.00 USD | 604,750,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.60` | 614,050,000.00 USD | 614,050,000.00 USD | 1,610,000.00 USD | 1,170,000.00 USD | 105,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.70` | 600,600,000.00 USD | 600,600,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.10` | 611,160,000.00 USD | 611,160,000.00 USD | 7,520,000.00 USD | 3,310,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.50` | 599,640,000.00 USD | 599,640,000.00 USD | 11,350,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.60` | 597,670,000.00 USD | 597,670,000.00 USD | 5,270,000.00 USD | 3,330,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 587,820,000.00 USD | 587,820,000.00 USD | 2,590,000.00 USD | 4,660,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,440,000.00 USD | 23,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.10` | 587,080,000.00 USD | 587,080,000.00 USD | 4,130,000.00 USD | 7,120,000.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.10` | 578,990,000.00 USD | 578,990,000.00 USD | 6,320,000.00 USD | 3,720,000.00 USD | 6,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.60` | 573,210,000.00 USD | 573,210,000.00 USD | 6,160,000.00 USD | 2,080,000.00 USD | 4,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.90` | 562,340,000.00 USD | 562,340,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.10` | 560,120,000.00 USD | 560,120,000.00 USD | 5,100,000.00 USD | 6,230,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.60` | 545,870,000.00 USD | 545,870,000.00 USD | 17,620,000.00 USD | 10,310,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.70` | 556,790,000.00 USD | 556,790,000.00 USD | 17,980,000.00 USD | 1,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 9,880,000.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.10` | 515,980,000.00 USD | 515,980,000.00 USD | 11,270,000.00 USD | 9,810,000.00 USD | 5,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2165.50` | 536,840,000.00 USD | 536,840,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.60` | 489,890,000.00 USD | 489,890,000.00 USD | 17,280,000.00 USD | 7,820,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.30` | 507,790,000.00 USD | 507,790,000.00 USD | 12,290,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.10` | 459,590,000.00 USD | 459,590,000.00 USD | 13,580,000.00 USD | 9,360,000.00 USD | 4,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.10` | 475,580,000.00 USD | 475,580,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.60` | 431,890,000.00 USD | 431,890,000.00 USD | 16,900,000.00 USD | 5,140,000.00 USD | 4,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.90` | 461,780,000.00 USD | 461,780,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 6,190,000.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.10` | 405,220,000.00 USD | 405,220,000.00 USD | 5,740,000.00 USD | 0.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.70` | 425,680,000.00 USD | 425,680,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.60` | 397,100,000.00 USD | 397,100,000.00 USD | 920,620.00 USD | 869,570.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2179.50` | 421,400,000.00 USD | 421,400,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.10` | 391,950,000.00 USD | 391,950,000.00 USD | 6,340,000.00 USD | 5,030,000.00 USD | 6,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2182.30` | 414,710,000.00 USD | 414,710,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.60` | 373,920,000.00 USD | 373,920,000.00 USD | 2,210,000.00 USD | 2,710,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 2,700,000.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.10` | 364,950,000.00 USD | 364,950,000.00 USD | 3,730,000.00 USD | 2,560,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2185.10` | 408,020,000.00 USD | 408,020,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.60` | 353,050,000.00 USD | 353,050,000.00 USD | 5,040,000.00 USD | 4,480,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.90` | 343,160,000.00 USD | 343,160,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.10` | 336,640,000.00 USD | 336,640,000.00 USD | 8,990,000.00 USD | 4,160,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.70` | 339,060,000.00 USD | 339,060,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.60` | 316,570,000.00 USD | 316,570,000.00 USD | 5,000,000.00 USD | 5,340,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.50` | 292,240,000.00 USD | 292,240,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,300,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.10` | 304,930,000.00 USD | 304,930,000.00 USD | 6,730,000.00 USD | 3,350,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.30` | 276,780,000.00 USD | 276,780,000.00 USD | 694,220.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.60` | 288,900,000.00 USD | 288,900,000.00 USD | 10,200,000.00 USD | 3,830,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.10` | 275,730,000.00 USD | 275,730,000.00 USD | 5,090,000.00 USD | 5,270,000.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.10` | 269,920,000.00 USD | 269,920,000.00 USD | 10,980,000.00 USD | 10,470,000.00 USD | 10,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.90` | 257,940,000.00 USD | 257,940,000.00 USD | 13,210,000.00 USD | 6,520,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.60` | 237,570,000.00 USD | 237,570,000.00 USD | 19,040,000.00 USD | 14,300,000.00 USD | 17,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.70` | 216,500,000.00 USD | 216,500,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 432,930.00 USD | 460,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.10` | 186,450,000.00 USD | 186,450,000.00 USD | 11,730,000.00 USD | 7,020,000.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.50` | 202,160,000.00 USD | 202,160,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.60` | 162,820,000.00 USD | 162,820,000.00 USD | 13,820,000.00 USD | 6,420,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.10` | 136,990,000.00 USD | 136,990,000.00 USD | 4,040,000.00 USD | 7,220,000.00 USD | 6,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.30` | 171,940,000.00 USD | 171,940,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.60` | 119,330,000.00 USD | 119,330,000.00 USD | 12,700,000.00 USD | 6,410,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.10` | 155,640,000.00 USD | 155,640,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 27,590.00 USD | 27,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.10` | 98,220,000.00 USD | 98,220,000.00 USD | 2,300,000.00 USD | 2,930,000.00 USD | 280,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2215.90` | 143,100,000.00 USD | 143,100,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.60` | 92,720,000.00 USD | 92,720,000.00 USD | 2,810,000.00 USD | 4,440,000.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.70` | 142,530,000.00 USD | 142,530,000.00 USD | 23,020,000.00 USD | 487,520.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.10` | 81,530,000.00 USD | 81,530,000.00 USD | 17,480,000.00 USD | 7,250,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.50` | 118,810,000.00 USD | 118,810,000.00 USD | 10,170,000.00 USD | 19,850,000.00 USD | 18,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.60` | 52,730,000.00 USD | 52,730,000.00 USD | 8,350,000.00 USD | 14,430,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.30` | 69,920,000.00 USD | 69,920,000.00 USD | 8,200,000.00 USD | 12,510,000.00 USD | 6,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.10` | 28,310,000.00 USD | 28,310,000.00 USD | 5,440,000.00 USD | 2,560,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2227.10` | 42,690,000.00 USD | 42,690,000.00 USD | 557,870.00 USD | 0.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.60` | 17,050,000.00 USD | 17,050,000.00 USD | 2,850,000.00 USD | 0.00 USD | 111,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 35,270,000.00 USD | 35,270,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.10` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.60` | 13,970,000.00 USD | 13,970,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2235.50` | 33,370,000.00 USD | 33,370,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.60` | 8,020,000.00 USD | 8,020,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2238.30` | 8,470,000.00 USD | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.10` | 21,970.00 USD | 21,970.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2242.60` | 22,480.00 USD | 22,480.00 USD | 0.00 USD | 0.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2243.90` | 268,650.00 USD | 268,650.00 USD | 0.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2245.10` | 84,720.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.70` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 1,300,000.00 USD | 709,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.60` | 627,550.00 USD | 627,550.00 USD | 0.00 USD | 243,170.00 USD | 299,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.50` | 6,670,000.00 USD | 6,670,000.00 USD | 861,640.00 USD | 2,660,000.00 USD | 867,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.10` | 3,010,000.00 USD | 3,010,000.00 USD | 255,300.00 USD | 446,930.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.30` | 31,940,000.00 USD | 31,940,000.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.60` | 11,200,000.00 USD | 11,200,000.00 USD | 1,470,000.00 USD | 3,300,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.10` | 36,260,000.00 USD | 36,260,000.00 USD | 12,360,000.00 USD | 6,830,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2255.10` | 49,360,000.00 USD | 49,360,000.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 774,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.60` | 70,410,000.00 USD | 70,410,000.00 USD | 19,980,000.00 USD | 8,290,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.90` | 89,060,000.00 USD | 89,060,000.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.10` | 92,470,000.00 USD | 92,470,000.00 USD | 9,050,000.00 USD | 10,340,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.70` | 93,380,000.00 USD | 93,380,000.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.60` | 120,860,000.00 USD | 120,860,000.00 USD | 15,390,000.00 USD | 6,760,000.00 USD | 6,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2263.50` | 102,390,000.00 USD | 102,390,000.00 USD | 7,340,000.00 USD | 1,460,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 34,370.00 USD | 54,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.10` | 166,830,000.00 USD | 166,830,000.00 USD | 19,500,000.00 USD | 16,750,000.00 USD | 9,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.30` | 134,680,000.00 USD | 134,680,000.00 USD | 10,170,000.00 USD | 15,790,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.60` | 222,770,000.00 USD | 222,770,000.00 USD | 20,700,000.00 USD | 22,510,000.00 USD | 12,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.10` | 190,860,000.00 USD | 190,860,000.00 USD | 19,210,000.00 USD | 12,640,000.00 USD | 24,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.10` | 282,240,000.00 USD | 282,240,000.00 USD | 23,390,000.00 USD | 12,160,000.00 USD | 23,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.90` | 219,760,000.00 USD | 219,760,000.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 7,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.60` | 313,170,000.00 USD | 313,170,000.00 USD | 19,020,000.00 USD | 5,610,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.70` | 248,060,000.00 USD | 248,060,000.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 791,770.00 USD | 846,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.10` | 360,690,000.00 USD | 360,690,000.00 USD | 27,310,000.00 USD | 15,610,000.00 USD | 4,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.50` | 274,450,000.00 USD | 274,450,000.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.60` | 398,310,000.00 USD | 398,310,000.00 USD | 10,430,000.00 USD | 15,200,000.00 USD | 11,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.10` | 446,800,000.00 USD | 446,800,000.00 USD | 26,670,000.00 USD | 9,750,000.00 USD | 12,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.30` | 318,770,000.00 USD | 318,770,000.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.60` | 501,330,000.00 USD | 501,330,000.00 USD | 22,560,000.00 USD | 24,830,000.00 USD | 7,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.10` | 410,580,000.00 USD | 410,580,000.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 235,710.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.10` | 529,190,000.00 USD | 529,190,000.00 USD | 11,520,000.00 USD | 9,410,000.00 USD | 6,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2285.90` | 414,600,000.00 USD | 414,600,000.00 USD | 1,320,000.00 USD | 2,590,000.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.60` | 568,320,000.00 USD | 568,320,000.00 USD | 19,470,000.00 USD | 11,060,000.00 USD | 8,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.70` | 456,130,000.00 USD | 456,130,000.00 USD | 13,470,000.00 USD | 13,140,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.10` | 614,240,000.00 USD | 614,240,000.00 USD | 19,770,000.00 USD | 21,020,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2291.50` | 481,440,000.00 USD | 481,440,000.00 USD | 8,400,000.00 USD | 6,770,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.60` | 648,230,000.00 USD | 648,230,000.00 USD | 17,860,000.00 USD | 4,710,000.00 USD | 11,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2294.30` | 502,780,000.00 USD | 502,780,000.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,490,000.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.10` | 684,840,000.00 USD | 684,840,000.00 USD | 12,280,000.00 USD | 13,600,000.00 USD | 10,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2297.10` | 552,530,000.00 USD | 552,530,000.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.60` | 731,170,000.00 USD | 731,170,000.00 USD | 29,190,000.00 USD | 11,160,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.90` | 595,450,000.00 USD | 595,450,000.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.10` | 770,690,000.00 USD | 770,690,000.00 USD | 11,250,000.00 USD | 14,710,000.00 USD | 13,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 798,290,000.00 USD | 798,290,000.00 USD | 16,060,000.00 USD | 2,700,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.70` | 650,110,000.00 USD | 650,110,000.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 310,530.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.10` | 837,020,000.00 USD | 837,020,000.00 USD | 14,970,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.50` | 676,130,000.00 USD | 676,130,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.60` | 848,320,000.00 USD | 848,320,000.00 USD | 4,390,000.00 USD | 3,680,000.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.30` | 678,430,000.00 USD | 678,430,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.10` | 866,820,000.00 USD | 866,820,000.00 USD | 4,990,000.00 USD | 2,820,000.00 USD | 10,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.10` | 708,930,000.00 USD | 708,930,000.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.60` | 883,400,000.00 USD | 883,400,000.00 USD | 6,950,000.00 USD | 8,040,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.90` | 719,750,000.00 USD | 719,750,000.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,030,000.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.10` | 905,950,000.00 USD | 905,950,000.00 USD | 5,980,000.00 USD | 13,500,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 725,500,000.00 USD | 725,500,000.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.60` | 933,100,000.00 USD | 933,100,000.00 USD | 8,220,000.00 USD | 10,500,000.00 USD | 8,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.50` | 755,660,000.00 USD | 755,660,000.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.10` | 958,960,000.00 USD | 958,960,000.00 USD | 10,150,000.00 USD | 12,260,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 761,580,000.00 USD | 761,580,000.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 172,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.60` | 976,910,000.00 USD | 976,910,000.00 USD | 3,370,000.00 USD | 9,320,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 3,580,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.10` | 990,830,000.00 USD | 990,830,000.00 USD | 3,060,000.00 USD | 9,360,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2325.10` | 784,620,000.00 USD | 784,620,000.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.60` | 997,390,000.00 USD | 997,390,000.00 USD | 553,100.00 USD | 1,410,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.90` | 796,510,000.00 USD | 796,510,000.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 11,750,000.00 USD | 3,450,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.70` | 812,890,000.00 USD | 812,890,000.00 USD | 15,960,000.00 USD | 363,770.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 5,020,000.00 USD | 3,500,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.50` | 858,190,000.00 USD | 858,190,000.00 USD | 22,570,000.00 USD | 14,770,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 79,270.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 11,180,000.00 USD | 7,590,000.00 USD | 5,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2336.30` | 902,400,000.00 USD | 902,400,000.00 USD | 26,590,000.00 USD | 10,690,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 14,050,000.00 USD | 1,830,000.00 USD | 6,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.10` | 928,810,000.00 USD | 928,810,000.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 11,670,000.00 USD | 6,260,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.90` | 969,240,000.00 USD | 969,240,000.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 8,670,000.00 USD | 4,470,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.70` | 997,150,000.00 USD | 997,150,000.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 550,680.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 5,430,000.00 USD | 8,130,000.00 USD | 8,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,960,000.00 USD | 3,520,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 23,260,000.00 USD | 6,880,000.00 USD | 10,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 5,150,000.00 USD | 3,400,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2353.10` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,280,000.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 2,320,000.00 USD | 3,770,000.00 USD | 951,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2355.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 3,780,000.00 USD | 4,290,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 9,090,000.00 USD | 4,260,000.00 USD | 5,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.50` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.60` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 8,700,000.00 USD | 6,710,000.00 USD | 7,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,970,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 4,830,000.00 USD | 3,010,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2367.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 2,910,000.00 USD | 1,110,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.10` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 10,250,000.00 USD | 7,700,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.60` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 11,280,000.00 USD | 1,790,000.00 USD | 4,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.70` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,760,000.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.10` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 5,700,000.00 USD | 557,400.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2375.50` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 3,340,000.00 USD | 3,070,000.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.30` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 6,310,000.00 USD | 389,290.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.10` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.90` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 1,890,000.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 7,540,000.00 USD | 11,520,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.70` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 9,850,000.00 USD | 5,970,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.50` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.30` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.60` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,870,000.00 USD | 23,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.10` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 2,380,000.00 USD | 2,830,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2395.10` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.10` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.70` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.50` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 225,400.00 USD | 24,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.10` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 5,960,000.00 USD | 3,440,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 6,810,000.00 USD | 3,500,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.10` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.10` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 4,520,000.00 USD | 3,540,000.00 USD | 3,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.60` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 4,850,000.00 USD | 2,970,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 116,740.00 USD | 24,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 2,080,000.00 USD | 1,910,000.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 2,060,000.00 USD | 1,260,000.00 USD | 707,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.10` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 5,060,000.00 USD | 2,860,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.60` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 693,410.00 USD | 2,620,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2423.10` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 435,780.00 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2425.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 12,980,000.00 USD | 15,010,000.00 USD | 17,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 603,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.10` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 691,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.30` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 8,200,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 532,800.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 2,480,000.00 USD | 559,660.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.10` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,240,000.00 USD | 502,040.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,040,000.00 USD | 743,640.00 USD | 827,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 1,630,000.00 USD | 26,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 218,020.00 USD | 703,990.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2445.50` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,210,000.00 USD | 751,450.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 10,750,000.00 USD | 3,620,000.00 USD | 13,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 627,630.00 USD | 311,480.00 USD | 35,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.10` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 3,200,000.00 USD | 1,840,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 194,210.00 USD | 27,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 2,270,000.00 USD | 1,990,000.00 USD | 994,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2456.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 5,900,000.00 USD | 7,380,000.00 USD | 7,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,770,000.00 USD | 1,980,000.00 USD | 845,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.50` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,530,000.00 USD | 1,370,000.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 413,060.00 USD | 629,460.00 USD | 851,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 16,250,000.00 USD | 43,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,090,000.00 USD | 1,050,000.00 USD | 525,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2465.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 4,960,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,140,000.00 USD | 1,580,000.00 USD | 377,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.90` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 3,830,000.00 USD | 2,330,000.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,440,000.00 USD | 2,220,000.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.70` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 4,870,000.00 USD | 3,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 653,960.00 USD | 275,370.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 54,870,000.00 USD | 98,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 595,510.00 USD | 914,780.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 2,200,000.00 USD | 405,410.00 USD | 156,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 567,450.00 USD | 943,540.00 USD | 731,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.70` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 41,090.00 USD | 98,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.50` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.30` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 1,740,000.00 USD | 99,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,900,000.00 USD | 104,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2515.00` | 60,730.00 USD | 104,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2525.00` | 79,800.00 USD | 104,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,060,000.00 USD | 106,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,080,000.00 USD | 111,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2555.00` | 262,820.00 USD | 111,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2565.00` | 38,980.00 USD | 111,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2575.00` | 45,990.00 USD | 111,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,690,000.00 USD | 138,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,000,000.00 USD | 146,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 5,810,000.00 USD | 151,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 12,770,000.00 USD | 164,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 6,640,000.00 USD | 171,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,480,000.00 USD | 172,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 860,740.00 USD | 173,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 398,020.00 USD | 174,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 462,390.00 USD | 174,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 1,590,000.00 USD | 176,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 17,400.00 USD | 176,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 275,120.00 USD | 176,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 1,270,000.00 USD | 177,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 533,790.00 USD | 178,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 409,700.00 USD | 178,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 435,040.00 USD | 179,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 13,800,000.00 USD | 192,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 35,320,000.00 USD | 228,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 376,890.00 USD | 228,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 405,060.00 USD | 229,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 5,570,000.00 USD | 234,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 22,260.00 USD | 234,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 5,280,000.00 USD | 239,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,890,000.00 USD | 241,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 106,590.00 USD | 241,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,290,000.00 USD | 248,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 121,050.00 USD | 248,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 1,090,000.00 USD | 249,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 50,400.00 USD | 249,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 43,550,000.00 USD | 292,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 2,080,000.00 USD | 295,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 533,420.00 USD | 295,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 1,200,000.00 USD | 296,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,750,000.00 USD | 299,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 24,140.00 USD | 299,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 182,240.00 USD | 299,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 412,780.00 USD | 300,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 280,690.00 USD | 300,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 3,890,000.00 USD | 304,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 18,050.00 USD | 304,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 2,370,000.00 USD | 306,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 14,980,000.00 USD | 321,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 559,150.00 USD | 322,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 163,470.00 USD | 322,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 2,090,000.00 USD | 324,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 12,810,000.00 USD | 337,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 947,940.00 USD | 338,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,180,000.00 USD | 340,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 1,510,000.00 USD | 341,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 11,210,000.00 USD | 353,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 7,870,000.00 USD | 361,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 6,890,000.00 USD | 367,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 12,140,000.00 USD | 380,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 1,750,000.00 USD | 381,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 116,140.00 USD | 381,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 600,340.00 USD | 382,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 35,850.00 USD | 382,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 3,250,000.00 USD | 385,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 29,530,000.00 USD | 415,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 9,000,000.00 USD | 424,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 70,710,000.00 USD | 495,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 230,850.00 USD | 495,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 106,300.00 USD | 495,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 335,380.00 USD | 495,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 35,870.00 USD | 495,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 18,000,000.00 USD | 513,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 182,250.00 USD | 513,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 1,530,000.00 USD | 515,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 4,780,000.00 USD | 520,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,450,000.00 USD | 528,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 118,750.00 USD | 528,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 2,080,000.00 USD | 530,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 2,850,000.00 USD | 533,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 6,270,000.00 USD | 540,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 260,460.00 USD | 540,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 29,130,000.00 USD | 569,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 372,490.00 USD | 569,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 2,510,000.00 USD | 572,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 4,340,000.00 USD | 576,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 3,250.00 USD | 576,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 102,400.00 USD | 576,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 1,130,000.00 USD | 577,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 402,390.00 USD | 578,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 1,850,000.00 USD | 580,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 15,090,000.00 USD | 595,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 739,940.00 USD | 595,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 2,740,000.00 USD | 598,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 473,740.00 USD | 599,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 65,160.00 USD | 599,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 57,870.00 USD | 599,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 14,200,000.00 USD | 613,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,300,000.00 USD | 614,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 1,390,000.00 USD | 616,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 691,460.00 USD | 616,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 167,320.00 USD | 617,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 244,270.00 USD | 617,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 30,420.00 USD | 617,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 178,820.00 USD | 617,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 55,400.00 USD | 617,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 80,150.00 USD | 617,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 2,840,000.00 USD | 620,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 118,080.00 USD | 620,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 1,010.00 USD | 620,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,790,000.00 USD | 624,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 9,700,000.00 USD | 634,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 73,410.00 USD | 634,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 6,560,000.00 USD | 640,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 54,100,000.00 USD | 694,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 12,160.00 USD | 694,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 347,420.00 USD | 695,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 222,990.00 USD | 695,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 383,100,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 102,260.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 2,100.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 234,460.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 3,780,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 7,650,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 80,890.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 2,640,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 57,020,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 3,170,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 1,250,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 8,090.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 27,530.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 115,860.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 281,470.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 3,430,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 67,010.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 817,060.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 39,470,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 266,110.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 971,390.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 2,580,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 197,460.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 5,050.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 24,650.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 1,760.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 5,480.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 241,590.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 600,020.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 607,880.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 52,680.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 1,810,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 702,730.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 1,120,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 48,020.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,620,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 70,150.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 271,220.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 451,090.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 9,770.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 535,670.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 3,810.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 64,130.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 196,720.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 774,090.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 40,030.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 123,950.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 92,210.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 854,050.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 32,940,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 82,260.00 USD | 1,250,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 83,090,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 16,670.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 1,530,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 420.39 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 58,530.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 766,900.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 5,810.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 5,560.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 153,740.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 248,420.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 116,150.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 152,480.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 598,750.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,010,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 448,590.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 178,700.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 81,540.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 42,140.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 116,160.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 22,970.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 390,430.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 75,710.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 37,040.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 18,450.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 138,480.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 784,540,000.00 USD | 0.00 USD | 80,660.00 USD | `-79.77%` | `177.28` |
| `Live` | `Long` | `465.00` | 784,460,000.00 USD | 0.00 USD | 6,190.00 USD | `-79.32%` | `13.30` |
| `Live` | `Long` | `475.00` | 784,460,000.00 USD | 0.00 USD | 70,920.00 USD | `-78.88%` | `149.30` |
| `Live` | `Long` | `485.00` | 784,390,000.00 USD | 0.00 USD | 108,780.00 USD | `-78.43%` | `224.30` |
| `Live` | `Long` | `495.00` | 784,280,000.00 USD | 0.00 USD | 19,900.00 USD | `-77.99%` | `40.21` |
| `Live` | `Long` | `505.00` | 784,260,000.00 USD | 0.00 USD | 65,690.00 USD | `-77.55%` | `130.08` |
| `Live` | `Long` | `515.00` | 784,190,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-77.10%` | `3,561.68` |
| `Live` | `Long` | `525.00` | 782,360,000.00 USD | 0.00 USD | 38,160.00 USD | `-76.66%` | `72.69` |
| `Live` | `Long` | `535.00` | 782,320,000.00 USD | 0.00 USD | 8,790.00 USD | `-76.21%` | `16.42` |
| `Live` | `Long` | `545.00` | 782,310,000.00 USD | 0.00 USD | 13,630.00 USD | `-75.77%` | `25.01` |
| `Live` | `Long` | `555.00` | 782,300,000.00 USD | 0.00 USD | 106,590.00 USD | `-75.32%` | `192.05` |
| `Live` | `Long` | `565.00` | 782,190,000.00 USD | 0.00 USD | 150,140.00 USD | `-74.88%` | `265.74` |
| `Live` | `Long` | `575.00` | 782,040,000.00 USD | 0.00 USD | 12,360.00 USD | `-74.43%` | `21.49` |
| `Live` | `Long` | `585.00` | 782,030,000.00 USD | 0.00 USD | 2,850,000.00 USD | `-73.99%` | `4,867.66` |
| `Live` | `Long` | `595.00` | 779,180,000.00 USD | 0.00 USD | 554,380.00 USD | `-73.54%` | `931.73` |
| `Live` | `Long` | `605.00` | 778,630,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-73.10%` | `3,017.99` |
| `Live` | `Long` | `615.00` | 776,800,000.00 USD | 0.00 USD | 57,360.00 USD | `-72.65%` | `93.26` |
| `Live` | `Long` | `625.00` | 776,740,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-72.21%` | `1,732.80` |
| `Live` | `Long` | `635.00` | 775,660,000.00 USD | 0.00 USD | 15,580.00 USD | `-71.77%` | `24.54` |
| `Live` | `Long` | `645.00` | 775,640,000.00 USD | 0.00 USD | 339,590.00 USD | `-71.32%` | `526.49` |
| `Live` | `Long` | `655.00` | 775,310,000.00 USD | 0.00 USD | 51,390.00 USD | `-70.88%` | `78.45` |
| `Live` | `Long` | `665.00` | 775,250,000.00 USD | 0.00 USD | 105,210.00 USD | `-70.43%` | `158.21` |
| `Live` | `Long` | `675.00` | 775,150,000.00 USD | 0.00 USD | 15,070.00 USD | `-69.99%` | `22.33` |
| `Live` | `Long` | `685.00` | 775,130,000.00 USD | 0.00 USD | 32,820.00 USD | `-69.54%` | `47.91` |
| `Live` | `Long` | `695.00` | 775,100,000.00 USD | 0.00 USD | 11,490.00 USD | `-69.10%` | `16.53` |
| `Live` | `Long` | `705.00` | 775,090,000.00 USD | 0.00 USD | 51,810.00 USD | `-68.65%` | `73.49` |
| `Live` | `Long` | `715.00` | 775,040,000.00 USD | 0.00 USD | 1,810.00 USD | `-68.21%` | `2.53` |
| `Live` | `Long` | `725.00` | 775,040,000.00 USD | 0.00 USD | 405,280.00 USD | `-67.76%` | `559.01` |
| `Live` | `Long` | `735.00` | 774,630,000.00 USD | 0.00 USD | 66,120.00 USD | `-67.32%` | `89.96` |
| `Live` | `Long` | `745.00` | 774,560,000.00 USD | 0.00 USD | 7,820.00 USD | `-66.87%` | `10.50` |
| `Live` | `Long` | `755.00` | 774,560,000.00 USD | 0.00 USD | 38,260.00 USD | `-66.43%` | `50.68` |
| `Live` | `Long` | `765.00` | 774,520,000.00 USD | 0.00 USD | 7,720.00 USD | `-65.98%` | `10.09` |
| `Live` | `Long` | `775.00` | 774,510,000.00 USD | 0.00 USD | 4,390.00 USD | `-65.54%` | `5.66` |
| `Live` | `Long` | `785.00` | 774,510,000.00 USD | 0.00 USD | 20,660.00 USD | `-65.10%` | `26.32` |
| `Live` | `Long` | `795.00` | 774,490,000.00 USD | 0.00 USD | 84,530.00 USD | `-64.65%` | `106.32` |
| `Live` | `Long` | `805.00` | 774,400,000.00 USD | 0.00 USD | 47,650.00 USD | `-64.21%` | `59.19` |
| `Live` | `Long` | `815.00` | 774,350,000.00 USD | 0.00 USD | 98,180.00 USD | `-63.76%` | `120.46` |
| `Live` | `Long` | `825.00` | 774,260,000.00 USD | 0.00 USD | 845,300.00 USD | `-63.32%` | `1,024.60` |
| `Live` | `Long` | `835.00` | 773,410,000.00 USD | 0.00 USD | 88,670.00 USD | `-62.87%` | `106.19` |
| `Live` | `Long` | `845.00` | 773,320,000.00 USD | 0.00 USD | 92,370.00 USD | `-62.43%` | `109.31` |
| `Live` | `Long` | `855.00` | 773,230,000.00 USD | 0.00 USD | 95,080.00 USD | `-61.98%` | `111.21` |
| `Live` | `Long` | `865.00` | 773,130,000.00 USD | 0.00 USD | 85,930.00 USD | `-61.54%` | `99.34` |
| `Live` | `Long` | `875.00` | 773,050,000.00 USD | 0.00 USD | 404,280.00 USD | `-61.09%` | `462.03` |
| `Live` | `Long` | `885.00` | 772,640,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-60.65%` | `1,360.87` |
| `Live` | `Long` | `895.00` | 771,440,000.00 USD | 0.00 USD | 115,430.00 USD | `-60.20%` | `128.98` |
| `Live` | `Long` | `905.00` | 771,320,000.00 USD | 0.00 USD | 131,400.00 USD | `-59.76%` | `145.19` |
| `Live` | `Long` | `915.00` | 771,190,000.00 USD | 0.00 USD | 166,190.00 USD | `-59.32%` | `181.63` |
| `Live` | `Long` | `925.00` | 771,030,000.00 USD | 0.00 USD | 168,790.00 USD | `-58.87%` | `182.48` |
| `Live` | `Long` | `935.00` | 770,860,000.00 USD | 0.00 USD | 84,000.00 USD | `-58.43%` | `89.84` |
| `Live` | `Long` | `945.00` | 770,770,000.00 USD | 0.00 USD | 62,450.00 USD | `-57.98%` | `66.08` |
| `Live` | `Long` | `955.00` | 770,710,000.00 USD | 0.00 USD | 27,560.00 USD | `-57.54%` | `28.86` |
| `Live` | `Long` | `965.00` | 770,680,000.00 USD | 0.00 USD | 483,050.00 USD | `-57.09%` | `500.57` |
| `Live` | `Long` | `975.00` | 770,200,000.00 USD | 0.00 USD | 144,850.00 USD | `-56.65%` | `148.57` |
| `Live` | `Long` | `985.00` | 770,060,000.00 USD | 0.00 USD | 215,460.00 USD | `-56.20%` | `218.74` |
| `Live` | `Long` | `995.00` | 769,840,000.00 USD | 0.00 USD | 72,670.00 USD | `-55.76%` | `73.03` |
| `Live` | `Long` | `1005.00` | 769,770,000.00 USD | 0.00 USD | 21,150.00 USD | `-55.31%` | `21.04` |
| `Live` | `Long` | `1015.00` | 769,750,000.00 USD | 0.00 USD | 345,840.00 USD | `-54.87%` | `340.73` |
| `Live` | `Long` | `1025.00` | 769,400,000.00 USD | 0.00 USD | 54,250.00 USD | `-54.42%` | `52.93` |
| `Live` | `Long` | `1035.00` | 769,350,000.00 USD | 0.00 USD | 275,540.00 USD | `-53.98%` | `266.23` |
| `Live` | `Long` | `1045.00` | 769,070,000.00 USD | 0.00 USD | 396,790.00 USD | `-53.53%` | `379.70` |
| `Live` | `Long` | `1055.00` | 768,670,000.00 USD | 0.00 USD | 9,530,000.00 USD | `-53.09%` | `9,034.88` |
| `Live` | `Long` | `1065.00` | 759,140,000.00 USD | 0.00 USD | 127,940.00 USD | `-52.65%` | `120.13` |
| `Live` | `Long` | `1075.00` | 759,010,000.00 USD | 0.00 USD | 671,120.00 USD | `-52.20%` | `624.30` |
| `Live` | `Long` | `1085.00` | 758,340,000.00 USD | 0.00 USD | 868,060.00 USD | `-51.76%` | `800.05` |
| `Live` | `Long` | `1095.00` | 757,470,000.00 USD | 0.00 USD | 38,740.00 USD | `-51.31%` | `35.38` |
| `Live` | `Long` | `1105.00` | 757,440,000.00 USD | 0.00 USD | 137,420.00 USD | `-50.87%` | `124.36` |
| `Live` | `Long` | `1115.00` | 757,300,000.00 USD | 0.00 USD | 7,860,000.00 USD | `-50.42%` | `7,051.32` |
| `Live` | `Long` | `1125.00` | 749,440,000.00 USD | 0.00 USD | 176,230.00 USD | `-49.98%` | `156.64` |
| `Live` | `Long` | `1135.00` | 749,260,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-49.53%` | `1,536.04` |
| `Live` | `Long` | `1145.00` | 747,520,000.00 USD | 0.00 USD | 214,200.00 USD | `-49.09%` | `187.07` |
| `Live` | `Long` | `1155.00` | 747,300,000.00 USD | 0.00 USD | 537,840.00 USD | `-48.64%` | `465.66` |
| `Live` | `Long` | `1165.00` | 746,760,000.00 USD | 0.00 USD | 51,500.00 USD | `-48.20%` | `44.20` |
| `Live` | `Long` | `1175.00` | 746,710,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-47.75%` | `1,328.41` |
| `Live` | `Long` | `1185.00` | 745,150,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-47.31%` | `1,067.75` |
| `Live` | `Long` | `1195.00` | 743,890,000.00 USD | 0.00 USD | 7,200,000.00 USD | `-46.87%` | `6,024.50` |
| `Live` | `Long` | `1205.00` | 736,690,000.00 USD | 0.00 USD | 2,020,000.00 USD | `-46.42%` | `1,673.31` |
| `Live` | `Long` | `1215.00` | 734,670,000.00 USD | 0.00 USD | 78,020.00 USD | `-45.98%` | `64.21` |
| `Live` | `Long` | `1225.00` | 734,590,000.00 USD | 0.00 USD | 432,140.00 USD | `-45.53%` | `352.77` |
| `Live` | `Long` | `1235.00` | 734,160,000.00 USD | 0.00 USD | 138,120.00 USD | `-45.09%` | `111.84` |
| `Live` | `Long` | `1245.00` | 734,020,000.00 USD | 0.00 USD | 56,730.00 USD | `-44.64%` | `45.57` |
| `Live` | `Long` | `1255.00` | 733,970,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-44.20%` | `1,002.44` |
| `Live` | `Long` | `1265.00` | 732,710,000.00 USD | 0.00 USD | 289,300.00 USD | `-43.75%` | `228.69` |
| `Live` | `Long` | `1275.00` | 732,420,000.00 USD | 0.00 USD | 15,490,000.00 USD | `-43.31%` | `12,145.72` |
| `Live` | `Long` | `1285.00` | 716,930,000.00 USD | 0.00 USD | 474,130.00 USD | `-42.86%` | `368.98` |
| `Live` | `Long` | `1295.00` | 716,460,000.00 USD | 0.00 USD | 339,640.00 USD | `-42.42%` | `262.27` |
| `Live` | `Long` | `1305.00` | 716,120,000.00 USD | 0.00 USD | 114,060.00 USD | `-41.97%` | `87.41` |
| `Live` | `Long` | `1315.00` | 716,010,000.00 USD | 0.00 USD | 186,060.00 USD | `-41.53%` | `141.49` |
| `Live` | `Long` | `1325.00` | 715,820,000.00 USD | 0.00 USD | 492,940.00 USD | `-41.08%` | `372.03` |
| `Live` | `Long` | `1335.00` | 715,330,000.00 USD | 0.00 USD | 5,500,000.00 USD | `-40.64%` | `4,118.27` |
| `Live` | `Long` | `1345.00` | 709,830,000.00 USD | 0.00 USD | 188,030.00 USD | `-40.20%` | `139.80` |
| `Live` | `Long` | `1355.00` | 709,640,000.00 USD | 0.00 USD | 106,050.00 USD | `-39.75%` | `78.27` |
| `Live` | `Long` | `1365.00` | 709,530,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-39.31%` | `921.62` |
| `Live` | `Long` | `1375.00` | 708,280,000.00 USD | 0.00 USD | 8,980,000.00 USD | `-38.86%` | `6,531.06` |
| `Live` | `Long` | `1385.00` | 699,300,000.00 USD | 0.00 USD | 485,050.00 USD | `-38.42%` | `350.21` |
| `Live` | `Long` | `1395.00` | 698,810,000.00 USD | 0.00 USD | 913,010.00 USD | `-37.97%` | `654.49` |
| `Live` | `Long` | `1405.00` | 697,900,000.00 USD | 0.00 USD | 22,730,000.00 USD | `-37.53%` | `16,181.47` |
| `Live` | `Long` | `1415.00` | 675,160,000.00 USD | 0.00 USD | 229,690.00 USD | `-37.08%` | `162.32` |
| `Live` | `Long` | `1425.00` | 674,930,000.00 USD | 0.00 USD | 561,450.00 USD | `-36.64%` | `394.00` |
| `Live` | `Long` | `1435.00` | 674,370,000.00 USD | 0.00 USD | 782,000.00 USD | `-36.19%` | `544.95` |
| `Live` | `Long` | `1445.00` | 673,590,000.00 USD | 0.00 USD | 1,730,000.00 USD | `-35.75%` | `1,195.74` |
| `Live` | `Long` | `1455.00` | 671,860,000.00 USD | 0.00 USD | 661,960.00 USD | `-35.30%` | `454.95` |
| `Live` | `Long` | `1465.00` | 671,200,000.00 USD | 0.00 USD | 8,450,000.00 USD | `-34.86%` | `5,767.16` |
| `Live` | `Long` | `1475.00` | 662,750,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-34.42%` | `3,887.69` |
| `Live` | `Long` | `1485.00` | 657,020,000.00 USD | 0.00 USD | 318,770.00 USD | `-33.97%` | `214.66` |
| `Live` | `Long` | `1495.00` | 656,700,000.00 USD | 0.00 USD | 19,400,000.00 USD | `-33.53%` | `12,976.71` |
| `Live` | `Long` | `1505.00` | 637,300,000.00 USD | 0.00 USD | 498,390.00 USD | `-33.08%` | `331.16` |
| `Live` | `Long` | `1515.00` | 636,800,000.00 USD | 0.00 USD | 18,790,000.00 USD | `-32.64%` | `12,405.12` |
| `Live` | `Long` | `1525.00` | 618,010,000.00 USD | 0.00 USD | 2,460,000.00 USD | `-32.19%` | `1,615.56` |
| `Live` | `Long` | `1535.00` | 615,540,000.00 USD | 0.00 USD | 902,770.00 USD | `-31.75%` | `588.12` |
| `Live` | `Long` | `1545.00` | 614,640,000.00 USD | 0.00 USD | 4,110,000.00 USD | `-31.30%` | `2,657.58` |
| `Live` | `Long` | `1555.00` | 610,530,000.00 USD | 0.00 USD | 16,090,000.00 USD | `-30.86%` | `10,347.34` |
| `Live` | `Long` | `1565.00` | 594,440,000.00 USD | 0.00 USD | 576,720.00 USD | `-30.41%` | `368.51` |
| `Live` | `Long` | `1575.00` | 593,870,000.00 USD | 0.00 USD | 949,290.00 USD | `-29.97%` | `602.72` |
| `Live` | `Long` | `1585.00` | 592,920,000.00 USD | 0.00 USD | 667,450.00 USD | `-29.52%` | `421.11` |
| `Live` | `Long` | `1595.00` | 592,250,000.00 USD | 0.00 USD | 2,010,000.00 USD | `-29.08%` | `1,263.08` |
| `Live` | `Long` | `1605.00` | 590,240,000.00 USD | 0.00 USD | 18,080,000.00 USD | `-28.63%` | `11,265.82` |
| `Live` | `Long` | `1615.00` | 572,150,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-28.19%` | `669.83` |
| `Live` | `Long` | `1625.00` | 571,070,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-27.75%` | `1,058.91` |
| `Live` | `Long` | `1635.00` | 569,350,000.00 USD | 0.00 USD | 18,670,000.00 USD | `-27.30%` | `11,419.54` |
| `Live` | `Long` | `1645.00` | 550,680,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-26.86%` | `22,788.26` |
| `Live` | `Long` | `1655.00` | 513,190,000.00 USD | 0.00 USD | 859,690.00 USD | `-26.41%` | `519.45` |
| `Live` | `Long` | `1665.00` | 512,330,000.00 USD | 0.00 USD | 11,660,000.00 USD | `-25.97%` | `7,003.36` |
| `Live` | `Long` | `1675.00` | 500,670,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-25.52%` | `612.33` |
| `Live` | `Long` | `1685.00` | 499,650,000.00 USD | 0.00 USD | 573,580.00 USD | `-25.08%` | `340.40` |
| `Live` | `Long` | `1695.00` | 499,070,000.00 USD | 0.00 USD | 756,150.00 USD | `-24.63%` | `446.11` |
| `Live` | `Long` | `1705.00` | 498,320,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-24.19%` | `597.96` |
| `Live` | `Long` | `1715.00` | 497,300,000.00 USD | 0.00 USD | 511,390.00 USD | `-23.74%` | `298.19` |
| `Live` | `Long` | `1725.00` | 496,790,000.00 USD | 0.00 USD | 36,690,000.00 USD | `-23.30%` | `21,269.24` |
| `Live` | `Long` | `1735.00` | 460,100,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-22.85%` | `911.34` |
| `Live` | `Long` | `1745.00` | 458,520,000.00 USD | 0.00 USD | 837,560.00 USD | `-22.41%` | `479.97` |
| `Live` | `Long` | `1755.00` | 457,680,000.00 USD | 0.00 USD | 480,300.00 USD | `-21.97%` | `273.67` |
| `Live` | `Long` | `1765.00` | 457,200,000.00 USD | 0.00 USD | 7,660,000.00 USD | `-21.52%` | `4,339.39` |
| `Live` | `Long` | `1775.00` | 449,540,000.00 USD | 0.00 USD | 24,770,000.00 USD | `-21.08%` | `13,955.49` |
| `Live` | `Long` | `1785.00` | 424,770,000.00 USD | 0.00 USD | 86,890,000.00 USD | `-20.63%` | `48,679.38` |
| `Live` | `Long` | `1795.00` | 337,880,000.00 USD | 0.00 USD | 482,950.00 USD | `-20.19%` | `269.05` |
| `Live` | `Long` | `1805.00` | 337,390,000.00 USD | 0.00 USD | 3,030,000.00 USD | `-19.74%` | `1,676.85` |
| `Live` | `Long` | `1815.00` | 334,370,000.00 USD | 0.00 USD | 507,190.00 USD | `-19.30%` | `279.44` |
| `Live` | `Long` | `1825.00` | 333,860,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-18.85%` | `724.95` |
| `Live` | `Long` | `1835.00` | 332,540,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-18.41%` | `579.27` |
| `Live` | `Long` | `1845.00` | 331,470,000.00 USD | 0.00 USD | 16,200,000.00 USD | `-17.96%` | `8,780.67` |
| `Live` | `Long` | `1855.00` | 315,270,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-17.52%` | `567.03` |
| `Live` | `Long` | `1865.00` | 314,220,000.00 USD | 0.00 USD | 15,820,000.00 USD | `-17.07%` | `8,484.98` |
| `Live` | `Long` | `1875.00` | 298,400,000.00 USD | 0.00 USD | 7,240,000.00 USD | `-16.63%` | `3,862.29` |
| `Live` | `Long` | `1885.00` | 291,150,000.00 USD | 0.00 USD | 5,540,000.00 USD | `-16.18%` | `2,938.71` |
| `Live` | `Long` | `1895.00` | 285,620,000.00 USD | 0.00 USD | 538,030.00 USD | `-15.74%` | `283.92` |
| `Live` | `Long` | `1905.00` | 285,080,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-15.30%` | `743.27` |
| `Live` | `Long` | `1915.00` | 283,660,000.00 USD | 0.00 USD | 18,440,000.00 USD | `-14.85%` | `9,629.63` |
| `Live` | `Long` | `1925.00` | 265,220,000.00 USD | 0.00 USD | 17,280,000.00 USD | `-14.41%` | `8,976.41` |
| `Live` | `Long` | `1935.00` | 247,940,000.00 USD | 0.00 USD | 876,330.00 USD | `-13.96%` | `452.88` |
| `Live` | `Long` | `1945.00` | 247,060,000.00 USD | 0.00 USD | 5,430,000.00 USD | `-13.52%` | `2,792.78` |
| `Live` | `Long` | `1955.00` | 241,630,000.00 USD | 0.00 USD | 13,680,000.00 USD | `-13.07%` | `6,998.40` |
| `Live` | `Long` | `1965.00` | 227,950,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-12.63%` | `1,385.08` |
| `Live` | `Long` | `1975.00` | 225,230,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-12.18%` | `1,528.88` |
| `Live` | `Long` | `1985.00` | 222,210,000.00 USD | 0.00 USD | 5,560,000.00 USD | `-11.74%` | `2,799.84` |
| `Live` | `Long` | `1995.00` | 216,650,000.00 USD | 0.00 USD | 645,300.00 USD | `-11.29%` | `323.46` |
| `Live` | `Long` | `2005.00` | 216,010,000.00 USD | 0.00 USD | 13,400,000.00 USD | `-10.85%` | `6,680.97` |
| `Live` | `Long` | `2015.00` | 202,610,000.00 USD | 0.00 USD | 2,050,000.00 USD | `-10.40%` | `1,016.65` |
| `Live` | `Long` | `2025.00` | 200,560,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-9.96%` | `499.16` |
| `Live` | `Long` | `2035.00` | 199,550,000.00 USD | 0.00 USD | 598,780.00 USD | `-9.52%` | `294.24` |
| `Live` | `Long` | `2045.00` | 198,950,000.00 USD | 0.00 USD | 6,820,000.00 USD | `-9.07%` | `3,337.16` |
| `Live` | `Long` | `2055.00` | 192,130,000.00 USD | 0.00 USD | 3,880,000.00 USD | `-8.63%` | `1,890.30` |
| `Live` | `Long` | `2065.00` | 188,240,000.00 USD | 0.00 USD | 14,120,000.00 USD | `-8.18%` | `6,836.44` |
| `Live` | `Long` | `2075.00` | 174,130,000.00 USD | 0.00 USD | 3,520,000.00 USD | `-7.74%` | `1,695.99` |
| `Live` | `Long` | `2085.00` | 170,610,000.00 USD | 0.00 USD | 13,940,000.00 USD | `-7.29%` | `6,685.99` |
| `Live` | `Long` | `2095.00` | 156,670,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-6.85%` | `830.54` |
| `Live` | `Long` | `2105.00` | 154,930,000.00 USD | 0.00 USD | 2,400,000.00 USD | `-6.40%` | `1,140.76` |
| `Live` | `Long` | `2115.00` | 152,530,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-5.96%` | `527.87` |
| `Live` | `Long` | `2125.00` | 151,410,000.00 USD | 0.00 USD | 123,840,000.00 USD | `-5.51%` | `58,278.99` |
| `Live` | `Long` | `2135.00` | 27,570,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-5.07%` | `757.55` |
| `Live` | `Long` | `2145.00` | 25,950,000.00 USD | 0.00 USD | 1,990,000.00 USD | `-4.62%` | `926.54` |
| `Live` | `Long` | `2155.00` | 23,960,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-4.18%` | `1,132.31` |
| `Live` | `Long` | `2165.00` | 21,520,000.00 USD | 0.00 USD | 9,880,000.00 USD | `-3.73%` | `4,561.89` |
| `Live` | `Long` | `2175.00` | 11,650,000.00 USD | 0.00 USD | 6,190,000.00 USD | `-3.29%` | `2,844.22` |
| `Live` | `Long` | `2185.00` | 5,460,000.00 USD | 0.00 USD | 2,700,000.00 USD | `-2.85%` | `1,236.31` |
| `Live` | `Long` | `2195.00` | 2,760,000.00 USD | 0.00 USD | 2,300,000.00 USD | `-2.40%` | `1,046.52` |
| `Live` | `Long` | `2205.00` | 460,520.00 USD | 0.00 USD | 432,930.00 USD | `-1.96%` | `196.34` |
| `Live` | `Long` | `2215.00` | 27,590.00 USD | 0.00 USD | 27,590.00 USD | `-1.51%` | `12.46` |
| `Live` | `Short` | `2255.00` | 20,070.00 USD | 20,070.00 USD | 0.00 USD | `+0.27%` | `8.90` |
| `Live` | `Short` | `2265.00` | 54,440.00 USD | 34,370.00 USD | 0.00 USD | `+0.71%` | `15.17` |
| `Live` | `Short` | `2275.00` | 846,210.00 USD | 791,770.00 USD | 0.00 USD | `+1.16%` | `348.03` |
| `Live` | `Short` | `2285.00` | 1,080,000.00 USD | 235,710.00 USD | 0.00 USD | `+1.60%` | `103.15` |
| `Live` | `Short` | `2295.00` | 4,580,000.00 USD | 3,490,000.00 USD | 0.00 USD | `+2.05%` | `1,522.56` |
| `Live` | `Short` | `2305.00` | 4,890,000.00 USD | 310,530.00 USD | 0.00 USD | `+2.49%` | `134.72` |
| `Live` | `Short` | `2315.00` | 5,910,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+2.93%` | `442.89` |
| `Live` | `Short` | `2325.00` | 9,490,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+3.38%` | `1,539.99` |
| `Live` | `Short` | `2335.00` | 9,570,000.00 USD | 79,270.00 USD | 0.00 USD | `+3.82%` | `33.95` |
| `Live` | `Short` | `2345.00` | 10,120,000.00 USD | 550,680.00 USD | 0.00 USD | `+4.27%` | `234.83` |
| `Live` | `Short` | `2355.00` | 11,400,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+4.71%` | `541.83` |
| `Live` | `Short` | `2365.00` | 15,370,000.00 USD | 3,970,000.00 USD | 0.00 USD | `+5.16%` | `1,680.06` |
| `Live` | `Short` | `2375.00` | 17,130,000.00 USD | 1,760,000.00 USD | 0.00 USD | `+5.60%` | `741.88` |
| `Live` | `Short` | `2385.00` | 19,020,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+6.05%` | `792.28` |
| `Live` | `Short` | `2395.00` | 23,900,000.00 USD | 4,870,000.00 USD | 0.00 USD | `+6.49%` | `2,035.38` |
| `Live` | `Short` | `2405.00` | 24,120,000.00 USD | 225,400.00 USD | 0.00 USD | `+6.94%` | `93.72` |
| `Live` | `Short` | `2415.00` | 24,240,000.00 USD | 116,740.00 USD | 0.00 USD | `+7.38%` | `48.34` |
| `Live` | `Short` | `2425.00` | 24,680,000.00 USD | 435,780.00 USD | 0.00 USD | `+7.83%` | `179.70` |
| `Live` | `Short` | `2435.00` | 25,210,000.00 USD | 532,800.00 USD | 0.00 USD | `+8.27%` | `218.81` |
| `Live` | `Short` | `2445.00` | 26,840,000.00 USD | 1,630,000.00 USD | 0.00 USD | `+8.71%` | `665.94` |
| `Live` | `Short` | `2455.00` | 27,030,000.00 USD | 194,210.00 USD | 0.00 USD | `+9.16%` | `79.11` |
| `Live` | `Short` | `2465.00` | 43,280,000.00 USD | 16,250,000.00 USD | 0.00 USD | `+9.60%` | `6,593.36` |
| `Live` | `Short` | `2475.00` | 98,150,000.00 USD | 54,870,000.00 USD | 0.00 USD | `+10.05%` | `22,170.01` |
| `Live` | `Short` | `2485.00` | 98,200,000.00 USD | 41,090.00 USD | 0.00 USD | `+10.49%` | `16.53` |
| `Live` | `Short` | `2495.00` | 99,940,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+10.94%` | `699.14` |
| `Live` | `Short` | `2505.00` | 104,840,000.00 USD | 4,900,000.00 USD | 0.00 USD | `+11.38%` | `1,957.96` |
| `Live` | `Short` | `2515.00` | 104,910,000.00 USD | 60,730.00 USD | 0.00 USD | `+11.83%` | `24.15` |
| `Live` | `Short` | `2525.00` | 104,990,000.00 USD | 79,800.00 USD | 0.00 USD | `+12.27%` | `31.60` |
| `Live` | `Short` | `2535.00` | 106,050,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+12.72%` | `418.95` |
| `Live` | `Short` | `2545.00` | 111,130,000.00 USD | 5,080,000.00 USD | 0.00 USD | `+13.16%` | `1,996.90` |
| `Live` | `Short` | `2555.00` | 111,390,000.00 USD | 262,820.00 USD | 0.00 USD | `+13.61%` | `102.87` |
| `Live` | `Short` | `2565.00` | 111,430,000.00 USD | 38,980.00 USD | 0.00 USD | `+14.05%` | `15.20` |
| `Live` | `Short` | `2575.00` | 111,480,000.00 USD | 45,990.00 USD | 0.00 USD | `+14.50%` | `17.86` |
| `Live` | `Short` | `2585.00` | 138,170,000.00 USD | 26,690,000.00 USD | 0.00 USD | `+14.94%` | `10,325.23` |
| `Live` | `Short` | `2595.00` | 146,160,000.00 USD | 8,000,000.00 USD | 0.00 USD | `+15.38%` | `3,081.17` |
| `Live` | `Short` | `2605.00` | 151,980,000.00 USD | 5,810,000.00 USD | 0.00 USD | `+15.83%` | `2,231.80` |
| `Live` | `Short` | `2615.00` | 164,750,000.00 USD | 12,770,000.00 USD | 0.00 USD | `+16.27%` | `4,884.95` |
| `Live` | `Short` | `2625.00` | 171,390,000.00 USD | 6,640,000.00 USD | 0.00 USD | `+16.72%` | `2,529.33` |
| `Live` | `Short` | `2635.00` | 172,870,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+17.16%` | `561.57` |
| `Live` | `Short` | `2645.00` | 173,730,000.00 USD | 860,740.00 USD | 0.00 USD | `+17.61%` | `325.42` |
| `Live` | `Short` | `2655.00` | 174,130,000.00 USD | 398,020.00 USD | 0.00 USD | `+18.05%` | `149.91` |
| `Live` | `Short` | `2665.00` | 174,590,000.00 USD | 462,390.00 USD | 0.00 USD | `+18.50%` | `173.51` |
| `Live` | `Short` | `2675.00` | 176,180,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+18.94%` | `594.35` |
| `Live` | `Short` | `2685.00` | 176,200,000.00 USD | 17,400.00 USD | 0.00 USD | `+19.39%` | `6.48` |
| `Live` | `Short` | `2695.00` | 176,470,000.00 USD | 275,120.00 USD | 0.00 USD | `+19.83%` | `102.09` |
| `Live` | `Short` | `2705.00` | 177,740,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+20.28%` | `468.81` |
| `Live` | `Short` | `2715.00` | 178,280,000.00 USD | 533,790.00 USD | 0.00 USD | `+20.72%` | `196.61` |
| `Live` | `Short` | `2725.00` | 178,690,000.00 USD | 409,700.00 USD | 0.00 USD | `+21.16%` | `150.35` |
| `Live` | `Short` | `2735.00` | 179,120,000.00 USD | 435,040.00 USD | 0.00 USD | `+21.61%` | `159.06` |
| `Live` | `Short` | `2745.00` | 192,920,000.00 USD | 13,800,000.00 USD | 0.00 USD | `+22.05%` | `5,028.25` |
| `Live` | `Short` | `2755.00` | 228,240,000.00 USD | 35,320,000.00 USD | 0.00 USD | `+22.50%` | `12,818.65` |
| `Live` | `Short` | `2765.00` | 228,620,000.00 USD | 376,890.00 USD | 0.00 USD | `+22.94%` | `136.31` |
| `Live` | `Short` | `2775.00` | 229,020,000.00 USD | 405,060.00 USD | 0.00 USD | `+23.39%` | `145.97` |
| `Live` | `Short` | `2785.00` | 234,590,000.00 USD | 5,570,000.00 USD | 0.00 USD | `+23.83%` | `1,999.72` |
| `Live` | `Short` | `2795.00` | 234,610,000.00 USD | 22,260.00 USD | 0.00 USD | `+24.28%` | `7.96` |
| `Live` | `Short` | `2805.00` | 239,890,000.00 USD | 5,280,000.00 USD | 0.00 USD | `+24.72%` | `1,881.35` |
| `Live` | `Short` | `2815.00` | 241,780,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+25.17%` | `671.39` |
| `Live` | `Short` | `2825.00` | 241,890,000.00 USD | 106,590.00 USD | 0.00 USD | `+25.61%` | `37.73` |
| `Live` | `Short` | `2835.00` | 248,170,000.00 USD | 6,290,000.00 USD | 0.00 USD | `+26.06%` | `2,217.87` |
| `Live` | `Short` | `2845.00` | 248,290,000.00 USD | 121,050.00 USD | 0.00 USD | `+26.50%` | `42.55` |
| `Live` | `Short` | `2855.00` | 249,390,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+26.95%` | `382.61` |
| `Live` | `Short` | `2865.00` | 249,440,000.00 USD | 50,400.00 USD | 0.00 USD | `+27.39%` | `17.59` |
| `Live` | `Short` | `2875.00` | 292,990,000.00 USD | 43,550,000.00 USD | 0.00 USD | `+27.83%` | `15,148.69` |
| `Live` | `Short` | `2885.00` | 295,070,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+28.28%` | `720.01` |
| `Live` | `Short` | `2895.00` | 295,600,000.00 USD | 533,420.00 USD | 0.00 USD | `+28.72%` | `184.26` |
| `Live` | `Short` | `2905.00` | 296,800,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+29.17%` | `412.89` |
| `Live` | `Short` | `2915.00` | 299,550,000.00 USD | 2,750,000.00 USD | 0.00 USD | `+29.61%` | `943.09` |
| `Live` | `Short` | `2925.00` | 299,570,000.00 USD | 24,140.00 USD | 0.00 USD | `+30.06%` | `8.25` |
| `Live` | `Short` | `2935.00` | 299,760,000.00 USD | 182,240.00 USD | 0.00 USD | `+30.50%` | `62.09` |
| `Live` | `Short` | `2945.00` | 300,170,000.00 USD | 412,780.00 USD | 0.00 USD | `+30.95%` | `140.16` |
| `Live` | `Short` | `2955.00` | 300,450,000.00 USD | 280,690.00 USD | 0.00 USD | `+31.39%` | `94.99` |
| `Live` | `Short` | `2965.00` | 304,340,000.00 USD | 3,890,000.00 USD | 0.00 USD | `+31.84%` | `1,312.86` |
| `Live` | `Short` | `2975.00` | 304,360,000.00 USD | 18,050.00 USD | 0.00 USD | `+32.28%` | `6.07` |
| `Live` | `Short` | `2985.00` | 306,730,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+32.73%` | `792.44` |
| `Live` | `Short` | `2995.00` | 321,710,000.00 USD | 14,980,000.00 USD | 0.00 USD | `+33.17%` | `5,002.66` |
| `Live` | `Short` | `3005.00` | 322,270,000.00 USD | 559,150.00 USD | 0.00 USD | `+33.61%` | `186.07` |
| `Live` | `Short` | `3015.00` | 322,430,000.00 USD | 163,470.00 USD | 0.00 USD | `+34.06%` | `54.22` |
| `Live` | `Short` | `3025.00` | 324,530,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+34.50%` | `692.34` |
| `Live` | `Short` | `3035.00` | 337,340,000.00 USD | 12,810,000.00 USD | 0.00 USD | `+34.95%` | `4,222.29` |
| `Live` | `Short` | `3045.00` | 338,290,000.00 USD | 947,940.00 USD | 0.00 USD | `+35.39%` | `311.31` |
| `Live` | `Short` | `3055.00` | 340,470,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+35.84%` | `713.85` |
| `Live` | `Short` | `3065.00` | 341,980,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+36.28%` | `493.82` |
| `Live` | `Short` | `3075.00` | 353,200,000.00 USD | 11,210,000.00 USD | 0.00 USD | `+36.73%` | `3,646.97` |
| `Live` | `Short` | `3085.00` | 361,070,000.00 USD | 7,870,000.00 USD | 0.00 USD | `+37.17%` | `2,550.82` |
| `Live` | `Short` | `3095.00` | 367,960,000.00 USD | 6,890,000.00 USD | 0.00 USD | `+37.62%` | `2,227.56` |
| `Live` | `Short` | `3105.00` | 380,100,000.00 USD | 12,140,000.00 USD | 0.00 USD | `+38.06%` | `3,908.62` |
| `Live` | `Short` | `3115.00` | 381,850,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+38.51%` | `561.85` |
| `Live` | `Short` | `3125.00` | 381,960,000.00 USD | 116,140.00 USD | 0.00 USD | `+38.95%` | `37.16` |
| `Live` | `Short` | `3135.00` | 382,560,000.00 USD | 600,340.00 USD | 0.00 USD | `+39.40%` | `191.49` |
| `Live` | `Short` | `3145.00` | 382,600,000.00 USD | 35,850.00 USD | 0.00 USD | `+39.84%` | `11.40` |
| `Live` | `Short` | `3155.00` | 385,850,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+40.28%` | `1,030.96` |
| `Live` | `Short` | `3165.00` | 415,380,000.00 USD | 29,530,000.00 USD | 0.00 USD | `+40.73%` | `9,329.08` |
| `Live` | `Short` | `3175.00` | 424,380,000.00 USD | 9,000,000.00 USD | 0.00 USD | `+41.17%` | `2,835.46` |
| `Live` | `Short` | `3185.00` | 495,090,000.00 USD | 70,710,000.00 USD | 0.00 USD | `+41.62%` | `22,199.66` |
| `Live` | `Short` | `3195.00` | 495,320,000.00 USD | 230,850.00 USD | 0.00 USD | `+42.06%` | `72.25` |
| `Live` | `Short` | `3205.00` | 495,420,000.00 USD | 106,300.00 USD | 0.00 USD | `+42.51%` | `33.17` |
| `Live` | `Short` | `3215.00` | 495,760,000.00 USD | 335,380.00 USD | 0.00 USD | `+42.95%` | `104.32` |
| `Live` | `Short` | `3225.00` | 495,800,000.00 USD | 35,870.00 USD | 0.00 USD | `+43.40%` | `11.12` |
| `Live` | `Short` | `3235.00` | 513,800,000.00 USD | 18,000,000.00 USD | 0.00 USD | `+43.84%` | `5,564.83` |
| `Live` | `Short` | `3245.00` | 513,980,000.00 USD | 182,250.00 USD | 0.00 USD | `+44.29%` | `56.16` |
| `Live` | `Short` | `3255.00` | 515,510,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+44.73%` | `469.41` |
| `Live` | `Short` | `3265.00` | 520,280,000.00 USD | 4,780,000.00 USD | 0.00 USD | `+45.18%` | `1,463.10` |
| `Live` | `Short` | `3275.00` | 528,740,000.00 USD | 8,450,000.00 USD | 0.00 USD | `+45.62%` | `2,580.89` |
| `Live` | `Short` | `3285.00` | 528,860,000.00 USD | 118,750.00 USD | 0.00 USD | `+46.06%` | `36.15` |
| `Live` | `Short` | `3295.00` | 530,940,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+46.51%` | `632.07` |
| `Live` | `Short` | `3305.00` | 533,790,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+46.95%` | `861.87` |
| `Live` | `Short` | `3315.00` | 540,060,000.00 USD | 6,270,000.00 USD | 0.00 USD | `+47.40%` | `1,890.92` |
| `Live` | `Short` | `3325.00` | 540,320,000.00 USD | 260,460.00 USD | 0.00 USD | `+47.84%` | `78.33` |
| `Live` | `Short` | `3335.00` | 569,450,000.00 USD | 29,130,000.00 USD | 0.00 USD | `+48.29%` | `8,735.57` |
| `Live` | `Short` | `3345.00` | 569,820,000.00 USD | 372,490.00 USD | 0.00 USD | `+48.73%` | `111.36` |
| `Live` | `Short` | `3355.00` | 572,330,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+49.18%` | `748.01` |
| `Live` | `Short` | `3365.00` | 576,670,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+49.62%` | `1,290.43` |
| `Live` | `Short` | `3375.00` | 576,680,000.00 USD | 3,250.00 USD | 0.00 USD | `+50.07%` | `0.96` |
| `Live` | `Short` | `3385.00` | 576,780,000.00 USD | 102,400.00 USD | 0.00 USD | `+50.51%` | `30.25` |
| `Live` | `Short` | `3395.00` | 577,910,000.00 USD | 1,130,000.00 USD | 0.00 USD | `+50.96%` | `332.09` |
| `Live` | `Short` | `3405.00` | 578,310,000.00 USD | 402,390.00 USD | 0.00 USD | `+51.40%` | `118.18` |
| `Live` | `Short` | `3415.00` | 580,150,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+51.85%` | `540.56` |
| `Live` | `Short` | `3425.00` | 595,240,000.00 USD | 15,090,000.00 USD | 0.00 USD | `+52.29%` | `4,405.35` |
| `Live` | `Short` | `3435.00` | 595,980,000.00 USD | 739,940.00 USD | 0.00 USD | `+52.73%` | `215.41` |
| `Live` | `Short` | `3445.00` | 598,720,000.00 USD | 2,740,000.00 USD | 0.00 USD | `+53.18%` | `794.99` |
| `Live` | `Short` | `3455.00` | 599,200,000.00 USD | 473,740.00 USD | 0.00 USD | `+53.62%` | `137.12` |
| `Live` | `Short` | `3465.00` | 599,260,000.00 USD | 65,160.00 USD | 0.00 USD | `+54.07%` | `18.80` |
| `Live` | `Short` | `3475.00` | 599,320,000.00 USD | 57,870.00 USD | 0.00 USD | `+54.51%` | `16.65` |
| `Live` | `Short` | `3485.00` | 613,520,000.00 USD | 14,200,000.00 USD | 0.00 USD | `+54.96%` | `4,074.89` |
| `Live` | `Short` | `3495.00` | 614,820,000.00 USD | 1,300,000.00 USD | 0.00 USD | `+55.40%` | `372.11` |
| `Live` | `Short` | `3505.00` | 616,210,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+55.85%` | `396.32` |
| `Live` | `Short` | `3515.00` | 616,900,000.00 USD | 691,460.00 USD | 0.00 USD | `+56.29%` | `196.72` |
| `Live` | `Short` | `3525.00` | 617,070,000.00 USD | 167,320.00 USD | 0.00 USD | `+56.74%` | `47.47` |
| `Live` | `Short` | `3535.00` | 617,310,000.00 USD | 244,270.00 USD | 0.00 USD | `+57.18%` | `69.10` |
| `Live` | `Short` | `3545.00` | 617,340,000.00 USD | 30,420.00 USD | 0.00 USD | `+57.63%` | `8.58` |
| `Live` | `Short` | `3555.00` | 617,520,000.00 USD | 178,820.00 USD | 0.00 USD | `+58.07%` | `50.30` |
| `Live` | `Short` | `3565.00` | 617,580,000.00 USD | 55,400.00 USD | 0.00 USD | `+58.51%` | `15.54` |
| `Live` | `Short` | `3575.00` | 617,660,000.00 USD | 80,150.00 USD | 0.00 USD | `+58.96%` | `22.42` |
| `Live` | `Short` | `3585.00` | 620,500,000.00 USD | 2,840,000.00 USD | 0.00 USD | `+59.40%` | `793.14` |
| `Live` | `Short` | `3595.00` | 620,620,000.00 USD | 118,080.00 USD | 0.00 USD | `+59.85%` | `32.85` |
| `Live` | `Short` | `3605.00` | 620,620,000.00 USD | 1,010.00 USD | 0.00 USD | `+60.29%` | `0.28` |
| `Live` | `Short` | `3615.00` | 624,410,000.00 USD | 3,790,000.00 USD | 0.00 USD | `+60.74%` | `1,047.40` |
| `Live` | `Short` | `3625.00` | 634,100,000.00 USD | 9,700,000.00 USD | 0.00 USD | `+61.18%` | `2,674.72` |
| `Live` | `Short` | `3635.00` | 634,180,000.00 USD | 73,410.00 USD | 0.00 USD | `+61.63%` | `20.20` |
| `Live` | `Short` | `3645.00` | 640,740,000.00 USD | 6,560,000.00 USD | 0.00 USD | `+62.07%` | `1,800.61` |
| `Live` | `Short` | `3655.00` | 694,840,000.00 USD | 54,100,000.00 USD | 0.00 USD | `+62.52%` | `14,800.93` |
| `Live` | `Short` | `3665.00` | 694,850,000.00 USD | 12,160.00 USD | 0.00 USD | `+62.96%` | `3.32` |
| `Live` | `Short` | `3675.00` | 695,200,000.00 USD | 347,420.00 USD | 0.00 USD | `+63.41%` | `94.54` |
| `Live` | `Short` | `3685.00` | 695,420,000.00 USD | 222,990.00 USD | 0.00 USD | `+63.85%` | `60.51` |
| `Live` | `Short` | `3695.00` | 1,080,000,000.00 USD | 383,100,000.00 USD | 0.00 USD | `+64.30%` | `103,681.40` |
| `Live` | `Short` | `3705.00` | 1,080,000,000.00 USD | 102,260.00 USD | 0.00 USD | `+64.74%` | `27.60` |
| `Live` | `Short` | `3715.00` | 1,080,000,000.00 USD | 2,100.00 USD | 0.00 USD | `+65.18%` | `0.57` |
| `Live` | `Short` | `3725.00` | 1,080,000,000.00 USD | 234,460.00 USD | 0.00 USD | `+65.63%` | `62.94` |
| `Live` | `Short` | `3735.00` | 1,080,000,000.00 USD | 3,780,000.00 USD | 0.00 USD | `+66.07%` | `1,011.11` |
| `Live` | `Short` | `3745.00` | 1,090,000,000.00 USD | 7,650,000.00 USD | 0.00 USD | `+66.52%` | `2,042.32` |
| `Live` | `Short` | `3755.00` | 1,090,000,000.00 USD | 80,890.00 USD | 0.00 USD | `+66.96%` | `21.54` |
| `Live` | `Short` | `3765.00` | 1,090,000,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+67.41%` | `701.06` |
| `Live` | `Short` | `3775.00` | 1,150,000,000.00 USD | 57,020,000.00 USD | 0.00 USD | `+67.85%` | `15,105.86` |
| `Live` | `Short` | `3785.00` | 1,150,000,000.00 USD | 3,170,000.00 USD | 0.00 USD | `+68.30%` | `837.62` |
| `Live` | `Short` | `3795.00` | 1,150,000,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+68.74%` | `328.72` |
| `Live` | `Short` | `3805.00` | 1,150,000,000.00 USD | 8,090.00 USD | 0.00 USD | `+69.19%` | `2.13` |
| `Live` | `Short` | `3815.00` | 1,150,000,000.00 USD | 27,530.00 USD | 0.00 USD | `+69.63%` | `7.22` |
| `Live` | `Short` | `3825.00` | 1,150,000,000.00 USD | 115,860.00 USD | 0.00 USD | `+70.08%` | `30.29` |
| `Live` | `Short` | `3835.00` | 1,150,000,000.00 USD | 281,470.00 USD | 0.00 USD | `+70.52%` | `73.40` |
| `Live` | `Short` | `3845.00` | 1,160,000,000.00 USD | 3,430,000.00 USD | 0.00 USD | `+70.96%` | `892.78` |
| `Live` | `Short` | `3855.00` | 1,160,000,000.00 USD | 67,010.00 USD | 0.00 USD | `+71.41%` | `17.38` |
| `Live` | `Short` | `3865.00` | 1,160,000,000.00 USD | 817,060.00 USD | 0.00 USD | `+71.85%` | `211.40` |
| `Live` | `Short` | `3885.00` | 1,200,000,000.00 USD | 39,470,000.00 USD | 0.00 USD | `+72.74%` | `10,160.83` |
| `Live` | `Short` | `3895.00` | 1,200,000,000.00 USD | 266,110.00 USD | 0.00 USD | `+73.19%` | `68.32` |
| `Live` | `Short` | `3905.00` | 1,200,000,000.00 USD | 971,390.00 USD | 0.00 USD | `+73.63%` | `248.76` |
| `Live` | `Short` | `3915.00` | 1,200,000,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+74.08%` | `658.45` |
| `Live` | `Short` | `3925.00` | 1,200,000,000.00 USD | 197,460.00 USD | 0.00 USD | `+74.52%` | `50.31` |
| `Live` | `Short` | `3935.00` | 1,200,000,000.00 USD | 5,050.00 USD | 0.00 USD | `+74.97%` | `1.28` |
| `Live` | `Short` | `3945.00` | 1,200,000,000.00 USD | 24,650.00 USD | 0.00 USD | `+75.41%` | `6.25` |
| `Live` | `Short` | `3955.00` | 1,200,000,000.00 USD | 1,760.00 USD | 0.00 USD | `+75.86%` | `0.44` |
| `Live` | `Short` | `3965.00` | 1,200,000,000.00 USD | 5,480.00 USD | 0.00 USD | `+76.30%` | `1.38` |
| `Live` | `Short` | `3975.00` | 1,200,000,000.00 USD | 241,590.00 USD | 0.00 USD | `+76.75%` | `60.78` |
| `Live` | `Short` | `3985.00` | 1,200,000,000.00 USD | 600,020.00 USD | 0.00 USD | `+77.19%` | `150.57` |
| `Live` | `Short` | `3995.00` | 1,200,000,000.00 USD | 607,880.00 USD | 0.00 USD | `+77.63%` | `152.16` |
| `Live` | `Short` | `4005.00` | 1,200,000,000.00 USD | 52,680.00 USD | 0.00 USD | `+78.08%` | `13.15` |
| `Live` | `Short` | `4015.00` | 1,210,000,000.00 USD | 1,810,000.00 USD | 0.00 USD | `+78.52%` | `450.27` |
| `Live` | `Short` | `4025.00` | 1,210,000,000.00 USD | 702,730.00 USD | 0.00 USD | `+78.97%` | `174.59` |
| `Live` | `Short` | `4035.00` | 1,210,000,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+79.41%` | `276.69` |
| `Live` | `Short` | `4045.00` | 1,210,000,000.00 USD | 48,020.00 USD | 0.00 USD | `+79.86%` | `11.87` |
| `Live` | `Short` | `4055.00` | 1,210,000,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+80.30%` | `399.95` |
| `Live` | `Short` | `4065.00` | 1,210,000,000.00 USD | 70,150.00 USD | 0.00 USD | `+80.75%` | `17.26` |
| `Live` | `Short` | `4075.00` | 1,210,000,000.00 USD | 271,220.00 USD | 0.00 USD | `+81.19%` | `66.56` |
| `Live` | `Short` | `4085.00` | 1,210,000,000.00 USD | 451,090.00 USD | 0.00 USD | `+81.64%` | `110.43` |
| `Live` | `Short` | `4095.00` | 1,210,000,000.00 USD | 9,770.00 USD | 0.00 USD | `+82.08%` | `2.39` |
| `Live` | `Short` | `4105.00` | 1,210,000,000.00 USD | 535,670.00 USD | 0.00 USD | `+82.53%` | `130.49` |
| `Live` | `Short` | `4115.00` | 1,210,000,000.00 USD | 3,810.00 USD | 0.00 USD | `+82.97%` | `0.93` |
| `Live` | `Short` | `4125.00` | 1,210,000,000.00 USD | 64,130.00 USD | 0.00 USD | `+83.41%` | `15.55` |
| `Live` | `Short` | `4135.00` | 1,210,000,000.00 USD | 196,720.00 USD | 0.00 USD | `+83.86%` | `47.57` |
| `Live` | `Short` | `4145.00` | 1,210,000,000.00 USD | 774,090.00 USD | 0.00 USD | `+84.30%` | `186.75` |
| `Live` | `Short` | `4155.00` | 1,210,000,000.00 USD | 40,030.00 USD | 0.00 USD | `+84.75%` | `9.63` |
| `Live` | `Short` | `4165.00` | 1,210,000,000.00 USD | 123,950.00 USD | 0.00 USD | `+85.19%` | `29.76` |
| `Live` | `Short` | `4175.00` | 1,210,000,000.00 USD | 92,210.00 USD | 0.00 USD | `+85.64%` | `22.09` |
| `Live` | `Short` | `4185.00` | 1,210,000,000.00 USD | 854,050.00 USD | 0.00 USD | `+86.08%` | `204.07` |
| `Live` | `Short` | `4195.00` | 1,250,000,000.00 USD | 32,940,000.00 USD | 0.00 USD | `+86.53%` | `7,851.08` |
| `Live` | `Short` | `4205.00` | 1,250,000,000.00 USD | 82,260.00 USD | 0.00 USD | `+86.97%` | `19.56` |
| `Live` | `Short` | `4215.00` | 1,330,000,000.00 USD | 83,090,000.00 USD | 0.00 USD | `+87.42%` | `19,712.87` |
| `Live` | `Short` | `4235.00` | 1,330,000,000.00 USD | 16,670.00 USD | 0.00 USD | `+88.31%` | `3.94` |
| `Live` | `Short` | `4245.00` | 1,330,000,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+88.75%` | `361.45` |
| `Live` | `Short` | `4255.00` | 1,330,000,000.00 USD | 420.39 USD | 0.00 USD | `+89.20%` | `0.10` |
| `Live` | `Short` | `4265.00` | 1,330,000,000.00 USD | 58,530.00 USD | 0.00 USD | `+89.64%` | `13.72` |
| `Live` | `Short` | `4285.00` | 1,330,000,000.00 USD | 766,900.00 USD | 0.00 USD | `+90.53%` | `178.97` |
| `Live` | `Short` | `4295.00` | 1,330,000,000.00 USD | 5,810.00 USD | 0.00 USD | `+90.97%` | `1.35` |
| `Live` | `Short` | `4305.00` | 1,330,000,000.00 USD | 5,560.00 USD | 0.00 USD | `+91.42%` | `1.29` |
| `Live` | `Short` | `4315.00` | 1,330,000,000.00 USD | 153,740.00 USD | 0.00 USD | `+91.86%` | `35.63` |
| `Live` | `Short` | `4325.00` | 1,330,000,000.00 USD | 248,420.00 USD | 0.00 USD | `+92.31%` | `57.44` |
| `Live` | `Short` | `4335.00` | 1,330,000,000.00 USD | 116,150.00 USD | 0.00 USD | `+92.75%` | `26.79` |
| `Live` | `Short` | `4345.00` | 1,330,000,000.00 USD | 152,480.00 USD | 0.00 USD | `+93.20%` | `35.09` |
| `Live` | `Short` | `4355.00` | 1,330,000,000.00 USD | 598,750.00 USD | 0.00 USD | `+93.64%` | `137.49` |
| `Live` | `Short` | `4365.00` | 1,330,000,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+94.09%` | `231.76` |
| `Live` | `Short` | `4375.00` | 1,330,000,000.00 USD | 448,590.00 USD | 0.00 USD | `+94.53%` | `102.54` |
| `Live` | `Short` | `4385.00` | 1,330,000,000.00 USD | 178,700.00 USD | 0.00 USD | `+94.98%` | `40.75` |
| `Live` | `Short` | `4395.00` | 1,330,000,000.00 USD | 81,540.00 USD | 0.00 USD | `+95.42%` | `18.55` |
| `Live` | `Short` | `4405.00` | 1,330,000,000.00 USD | 42,140.00 USD | 0.00 USD | `+95.86%` | `9.57` |
| `Live` | `Short` | `4415.00` | 1,330,000,000.00 USD | 116,160.00 USD | 0.00 USD | `+96.31%` | `26.31` |
| `Live` | `Short` | `4425.00` | 1,330,000,000.00 USD | 22,970.00 USD | 0.00 USD | `+96.75%` | `5.19` |
| `Live` | `Short` | `4455.00` | 1,340,000,000.00 USD | 390,430.00 USD | 0.00 USD | `+98.09%` | `87.64` |
| `Live` | `Short` | `4465.00` | 1,340,000,000.00 USD | 75,710.00 USD | 0.00 USD | `+98.53%` | `16.96` |
| `Live` | `Short` | `4475.00` | 1,340,000,000.00 USD | 37,040.00 USD | 0.00 USD | `+98.98%` | `8.28` |
| `Live` | `Short` | `4485.00` | 1,340,000,000.00 USD | 18,450.00 USD | 0.00 USD | `+99.42%` | `4.11` |
| `Live` | `Short` | `4495.00` | 1,340,000,000.00 USD | 138,480.00 USD | 0.00 USD | `+99.87%` | `30.81` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 34,130,000.00 USD | 0.00 USD | 278.83 USD | `-78.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 34,130,000.00 USD | 0.00 USD | 16,100.00 USD | `-77.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.00` | 34,110,000.00 USD | 0.00 USD | 300.66 USD | `-77.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 34,110,000.00 USD | 0.00 USD | 563.16 USD | `-75.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.00` | 34,110,000.00 USD | 0.00 USD | 170.14 USD | `-74.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.00` | 34,110,000.00 USD | 0.00 USD | 259.78 USD | `-72.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 34,110,000.00 USD | 0.00 USD | 583.40 USD | `-71.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 34,110,000.00 USD | 0.00 USD | 613.93 USD | `-70.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 34,110,000.00 USD | 0.00 USD | 578.54 USD | `-69.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 34,110,000.00 USD | 0.00 USD | 242.21 USD | `-69.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 34,110,000.00 USD | 0.00 USD | 885.90 USD | `-68.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.00` | 34,110,000.00 USD | 0.00 USD | 4,130.00 USD | `-68.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.00` | 34,110,000.00 USD | 0.00 USD | 15,090.00 USD | `-67.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 34,090,000.00 USD | 0.00 USD | 177.27 USD | `-66.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 34,090,000.00 USD | 0.00 USD | 2,400.00 USD | `-64.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 34,090,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 34,090,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 33,950,000.00 USD | 0.00 USD | 918.49 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 33,950,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 33,940,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 33,940,000.00 USD | 0.00 USD | 516.34 USD | `-56.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 33,940,000.00 USD | 0.00 USD | 100.50 USD | `-55.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 33,940,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 33,720,000.00 USD | 0.00 USD | 445.08 USD | `-54.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 33,720,000.00 USD | 0.00 USD | 112.03 USD | `-54.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 33,720,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 33,710,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 33,710,000.00 USD | 0.00 USD | 995.34 USD | `-52.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 33,710,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 33,710,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 33,700,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 33,700,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 33,700,000.00 USD | 0.00 USD | 476.46 USD | `-47.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 33,700,000.00 USD | 0.00 USD | 228.47 USD | `-47.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 33,700,000.00 USD | 0.00 USD | 221.55 USD | `-46.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 33,700,000.00 USD | 0.00 USD | 3,880.00 USD | `-46.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 33,690,000.00 USD | 0.00 USD | 995.93 USD | `-45.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 33,690,000.00 USD | 0.00 USD | 951.93 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 33,690,000.00 USD | 0.00 USD | 2,290.00 USD | `-44.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 33,690,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 33,680,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 33,670,000.00 USD | 0.00 USD | 23,030.00 USD | `-41.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 33,650,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1335.00` | 33,650,000.00 USD | 0.00 USD | 281.69 USD | `-40.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 33,650,000.00 USD | 0.00 USD | 144,020.00 USD | `-40.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 33,500,000.00 USD | 0.00 USD | 128.86 USD | `-39.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 33,500,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 33,500,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 33,500,000.00 USD | 0.00 USD | 100,800.00 USD | `-38.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 33,400,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 32,860,000.00 USD | 0.00 USD | 18,840.00 USD | `-37.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 32,840,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 32,840,000.00 USD | 0.00 USD | 852.10 USD | `-36.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 32,830,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 32,830,000.00 USD | 0.00 USD | 5,090.00 USD | `-35.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 32,830,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 32,810,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 32,810,000.00 USD | 0.00 USD | 19,930.00 USD | `-33.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 32,790,000.00 USD | 0.00 USD | 11,460.00 USD | `-33.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 32,770,000.00 USD | 0.00 USD | 68,840.00 USD | `-33.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 32,710,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 32,690,000.00 USD | 0.00 USD | 31,900.00 USD | `-32.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 32,660,000.00 USD | 0.00 USD | 983.78 USD | `-31.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 32,660,000.00 USD | 0.00 USD | 2,090.00 USD | `-31.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 32,660,000.00 USD | 0.00 USD | 32,880.00 USD | `-30.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 32,630,000.00 USD | 0.00 USD | 10,660.00 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 32,620,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 32,420,000.00 USD | 0.00 USD | 4,990.00 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 32,410,000.00 USD | 0.00 USD | 9,090.00 USD | `-29.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 32,400,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 31,970,000.00 USD | 0.00 USD | 25,700.00 USD | `-28.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 31,950,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 31,930,000.00 USD | 0.00 USD | 10,560.00 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 31,920,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 31,600,000.00 USD | 0.00 USD | 114,830.00 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 31,480,000.00 USD | 0.00 USD | 999.83 USD | `-25.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 31,480,000.00 USD | 0.00 USD | 289.27 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 31,480,000.00 USD | 0.00 USD | 35,320.00 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 31,440,000.00 USD | 0.00 USD | 42,420.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 31,400,000.00 USD | 0.00 USD | 84,860.00 USD | `-24.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 31,320,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 31,300,000.00 USD | 0.00 USD | 47,500.00 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 31,250,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 31,220,000.00 USD | 0.00 USD | 3,180.00 USD | `-22.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 31,220,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 30,750,000.00 USD | 0.00 USD | 77,450.00 USD | `-21.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 30,680,000.00 USD | 0.00 USD | 3,090.00 USD | `-21.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 30,670,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 30,670,000.00 USD | 0.00 USD | 191,070.00 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 30,470,000.00 USD | 0.00 USD | 744,540.00 USD | `-19.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 29,730,000.00 USD | 0.00 USD | 259,710.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 29,470,000.00 USD | 0.00 USD | 45,060.00 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 29,430,000.00 USD | 0.00 USD | 5,380.00 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 29,420,000.00 USD | 0.00 USD | 30,780.00 USD | `-17.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 29,390,000.00 USD | 0.00 USD | 485,090.00 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 28,900,000.00 USD | 0.00 USD | 41,250.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 28,860,000.00 USD | 0.00 USD | 9,620.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1885.00` | 28,850,000.00 USD | 0.00 USD | 19,770.00 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 28,830,000.00 USD | 0.00 USD | 61,630.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 28,770,000.00 USD | 0.00 USD | 152,510.00 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 28,620,000.00 USD | 0.00 USD | 105,830.00 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 28,510,000.00 USD | 0.00 USD | 56,430.00 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1935.00` | 28,460,000.00 USD | 0.00 USD | 117,650.00 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 28,340,000.00 USD | 0.00 USD | 61,020.00 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 28,280,000.00 USD | 0.00 USD | 81,030.00 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 28,200,000.00 USD | 0.00 USD | 138,620.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 28,060,000.00 USD | 0.00 USD | 69,900.00 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 27,990,000.00 USD | 0.00 USD | 105,150.00 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 27,880,000.00 USD | 0.00 USD | 122,280.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 27,760,000.00 USD | 0.00 USD | 2,080,000.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 25,680,000.00 USD | 0.00 USD | 48,350.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 25,630,000.00 USD | 0.00 USD | 15,730.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 25,620,000.00 USD | 0.00 USD | 175,420.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 25,440,000.00 USD | 0.00 USD | 50,140.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 25,390,000.00 USD | 0.00 USD | 269,160.00 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 25,120,000.00 USD | 0.00 USD | 825,500.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 24,300,000.00 USD | 0.00 USD | 148,720.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 24,150,000.00 USD | 0.00 USD | 153,080.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 24,000,000.00 USD | 0.00 USD | 33,690.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 23,960,000.00 USD | 0.00 USD | 470,900.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 23,490,000.00 USD | 0.00 USD | 191,710.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 23,300,000.00 USD | 0.00 USD | 462,910.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 22,840,000.00 USD | 0.00 USD | 311,950.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 22,530,000.00 USD | 0.00 USD | 492,720.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 22,030,000.00 USD | 0.00 USD | 638,630.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 21,390,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 19,690,000.00 USD | 0.00 USD | 9,700,000.00 USD | `-3.29%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 9,980,000.00 USD | 0.00 USD | 271,670.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 9,710,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 6,720,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 5,120,000.00 USD | 0.00 USD | 3,070,000.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 2,050,000.00 USD | 0.00 USD | 584,790.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,460,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 15,080.00 USD | 0.00 USD | 15,080.00 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 573,280.00 USD | 573,280.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 2,540,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 3,000,000.00 USD | 455,570.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 5,020,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 5,830,000.00 USD | 812,750.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 15,740,000.00 USD | 9,900,000.00 USD | 0.00 USD | `+2.49%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 16,860,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 17,090,000.00 USD | 229,720.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 17,250,000.00 USD | 164,580.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 18,840,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 20,130,000.00 USD | 1,290,000.00 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 22,350,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 22,510,000.00 USD | 166,390.00 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 24,850,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 25,950,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 28,490,000.00 USD | 2,540,000.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 28,820,000.00 USD | 321,000.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 31,090,000.00 USD | 2,280,000.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 31,280,000.00 USD | 192,130.00 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 33,770,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 33,920,000.00 USD | 148,840.00 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 36,040,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 36,220,000.00 USD | 181,240.00 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 38,330,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 38,450,000.00 USD | 122,320.00 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 41,000,000.00 USD | 2,550,000.00 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2515.00` | 48,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | `+11.83%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 51,210,000.00 USD | 2,610,000.00 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 51,280,000.00 USD | 61,230.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 53,450,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 53,650,000.00 USD | 200,490.00 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 56,010,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 56,100,000.00 USD | 93,110.00 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 58,620,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 58,630,000.00 USD | 10,500.00 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 61,900,000.00 USD | 3,270,000.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 61,980,000.00 USD | 79,040.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 64,160,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 64,300,000.00 USD | 147,930.00 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 66,430,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+17.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 66,740,000.00 USD | 306,950.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 68,880,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+18.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 69,150,000.00 USD | 265,610.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 71,320,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 71,420,000.00 USD | 94,620.00 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 74,270,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 74,340,000.00 USD | 76,590.00 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 74,630,000.00 USD | 286,910.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 74,670,000.00 USD | 43,050.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 74,850,000.00 USD | 180,060.00 USD | 0.00 USD | `+22.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 75,750,000.00 USD | 892,350.00 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 75,850,000.00 USD | 103,020.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 76,430,000.00 USD | 577,610.00 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 76,460,000.00 USD | 35,580.00 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 76,480,000.00 USD | 17,550.00 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 77,380,000.00 USD | 905,020.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 77,440,000.00 USD | 52,490.00 USD | 0.00 USD | `+25.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 77,480,000.00 USD | 43,930.00 USD | 0.00 USD | `+25.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 77,770,000.00 USD | 286,140.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 78,770,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 80,040,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 80,050,000.00 USD | 11,150.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 80,060,000.00 USD | 2,460.00 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 80,360,000.00 USD | 305,820.00 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 80,380,000.00 USD | 16,190.00 USD | 0.00 USD | `+28.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 81,860,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 81,870,000.00 USD | 10,340.00 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 81,880,000.00 USD | 3,050.00 USD | 0.00 USD | `+30.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 81,930,000.00 USD | 52,370.00 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 81,960,000.00 USD | 34,650.00 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 82,010,000.00 USD | 44,750.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 82,120,000.00 USD | 113,340.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 82,270,000.00 USD | 145,510.00 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 83,200,000.00 USD | 931,470.00 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 88,120,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+33.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 90,200,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+33.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 90,210,000.00 USD | 9,740.00 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 90,240,000.00 USD | 35,380.00 USD | 0.00 USD | `+34.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 90,320,000.00 USD | 74,910.00 USD | 0.00 USD | `+34.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 90,340,000.00 USD | 22,460.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 91,110,000.00 USD | 771,070.00 USD | 0.00 USD | `+35.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 91,110,000.00 USD | 612.69 USD | 0.00 USD | `+36.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 91,160,000.00 USD | 49,330.00 USD | 0.00 USD | `+36.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 91,180,000.00 USD | 19,570.00 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 91,180,000.00 USD | 928.50 USD | 0.00 USD | `+37.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 103,060,000.00 USD | 11,880,000.00 USD | 0.00 USD | `+38.06%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 103,170,000.00 USD | 110,480.00 USD | 0.00 USD | `+38.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 103,550,000.00 USD | 381,020.00 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3135.00` | 103,550,000.00 USD | 674.02 USD | 0.00 USD | `+39.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 103,560,000.00 USD | 2,660.00 USD | 0.00 USD | `+39.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 103,620,000.00 USD | 58,930.00 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 103,630,000.00 USD | 9,860.00 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 103,630,000.00 USD | 149.22 USD | 0.00 USD | `+41.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 103,630,000.00 USD | 1,920.00 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 103,670,000.00 USD | 41,120.00 USD | 0.00 USD | `+42.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 104,330,000.00 USD | 663,130.00 USD | 0.00 USD | `+42.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 104,330,000.00 USD | 1,760.00 USD | 0.00 USD | `+42.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 104,490,000.00 USD | 156,230.00 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 104,490,000.00 USD | 167.25 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 104,550,000.00 USD | 57,500.00 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 104,780,000.00 USD | 236,580.00 USD | 0.00 USD | `+44.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 104,800,000.00 USD | 15,710.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 104,800,000.00 USD | 1,630.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 104,940,000.00 USD | 141,980.00 USD | 0.00 USD | `+46.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 104,960,000.00 USD | 15,350.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 106,370,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 106,760,000.00 USD | 389,970.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 106,790,000.00 USD | 24,200.00 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 106,790,000.00 USD | 4,350.00 USD | 0.00 USD | `+48.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 106,790,000.00 USD | 2,170.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 106,800,000.00 USD | 2,520.00 USD | 0.00 USD | `+49.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 106,800,000.00 USD | 295.78 USD | 0.00 USD | `+49.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 106,820,000.00 USD | 21,260.00 USD | 0.00 USD | `+50.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 106,870,000.00 USD | 58,010.00 USD | 0.00 USD | `+50.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 107,200,000.00 USD | 321,800.00 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 108,680,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 108,690,000.00 USD | 5,700.00 USD | 0.00 USD | `+51.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 108,700,000.00 USD | 16,310.00 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 108,720,000.00 USD | 15,030.00 USD | 0.00 USD | `+53.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 108,740,000.00 USD | 18,600.00 USD | 0.00 USD | `+53.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 108,740,000.00 USD | 495.50 USD | 0.00 USD | `+54.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 108,740,000.00 USD | 3,190.00 USD | 0.00 USD | `+54.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 108,780,000.00 USD | 43,610.00 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 108,780,000.00 USD | 158.32 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 109,230,000.00 USD | 446,770.00 USD | 0.00 USD | `+55.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 109,270,000.00 USD | 43,460.00 USD | 0.00 USD | `+56.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 109,280,000.00 USD | 3,690.00 USD | 0.00 USD | `+56.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 109,290,000.00 USD | 9,810.00 USD | 0.00 USD | `+57.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 109,380,000.00 USD | 90,810.00 USD | 0.00 USD | `+58.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 109,380,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 109,380,000.00 USD | 2,870.00 USD | 0.00 USD | `+58.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 109,380,000.00 USD | 354.92 USD | 0.00 USD | `+59.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 109,400,000.00 USD | 13,160.00 USD | 0.00 USD | `+59.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 109,500,000.00 USD | 105,150.00 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 109,500,000.00 USD | 199.55 USD | 0.00 USD | `+60.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 109,510,000.00 USD | 10,210.00 USD | 0.00 USD | `+61.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 109,520,000.00 USD | 7,790.00 USD | 0.00 USD | `+61.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 109,520,000.00 USD | 3,860.00 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 109,530,000.00 USD | 8,100.00 USD | 0.00 USD | `+62.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 109,540,000.00 USD | 8,130.00 USD | 0.00 USD | `+62.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 109,590,000.00 USD | 55,120.00 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 109,600,000.00 USD | 1,410.00 USD | 0.00 USD | `+63.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 109,600,000.00 USD | 819.92 USD | 0.00 USD | `+64.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 109,600,000.00 USD | 323.58 USD | 0.00 USD | `+65.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 109,600,000.00 USD | 1,400.00 USD | 0.00 USD | `+65.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 109,610,000.00 USD | 6,490.00 USD | 0.00 USD | `+66.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 109,610,000.00 USD | 165.90 USD | 0.00 USD | `+66.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 109,610,000.00 USD | 751.00 USD | 0.00 USD | `+66.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 109,610,000.00 USD | 286.90 USD | 0.00 USD | `+68.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 109,610,000.00 USD | 1,560.00 USD | 0.00 USD | `+68.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 110,340,000.00 USD | 732,630.00 USD | 0.00 USD | `+69.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 110,360,000.00 USD | 20,930.00 USD | 0.00 USD | `+69.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 110,370,000.00 USD | 8,380.00 USD | 0.00 USD | `+70.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 110,370,000.00 USD | 711.78 USD | 0.00 USD | `+70.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 110,370,000.00 USD | 355.28 USD | 0.00 USD | `+70.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 110,380,000.00 USD | 5,170.00 USD | 0.00 USD | `+71.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 110,400,000.00 USD | 19,430.00 USD | 0.00 USD | `+72.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 110,410,000.00 USD | 12,120.00 USD | 0.00 USD | `+73.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 111,120,000.00 USD | 717,170.00 USD | 0.00 USD | `+74.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 111,170,000.00 USD | 42,570.00 USD | 0.00 USD | `+74.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 111,230,000.00 USD | 59,170.00 USD | 0.00 USD | `+75.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 111,230,000.00 USD | 1,380.00 USD | 0.00 USD | `+75.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 111,230,000.00 USD | 6,960.00 USD | 0.00 USD | `+76.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 111,250,000.00 USD | 14,610.00 USD | 0.00 USD | `+77.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 111,250,000.00 USD | 4,280.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 113,890,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+78.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 113,890,000.00 USD | 898.59 USD | 0.00 USD | `+79.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 113,890,000.00 USD | 811.00 USD | 0.00 USD | `+80.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 113,900,000.00 USD | 4,310.00 USD | 0.00 USD | `+81.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 113,900,000.00 USD | 3,050.00 USD | 0.00 USD | `+81.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 113,940,000.00 USD | 36,740.00 USD | 0.00 USD | `+82.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 113,940,000.00 USD | 5,990.00 USD | 0.00 USD | `+82.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 113,940,000.00 USD | 372.90 USD | 0.00 USD | `+83.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 113,940,000.00 USD | 395.43 USD | 0.00 USD | `+84.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 113,940,000.00 USD | 376.65 USD | 0.00 USD | `+86.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 113,990,000.00 USD | 42,260.00 USD | 0.00 USD | `+86.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 113,990,000.00 USD | 460.70 USD | 0.00 USD | `+87.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 113,990,000.00 USD | 1,270.00 USD | 0.00 USD | `+87.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 113,990,000.00 USD | 4,300.00 USD | 0.00 USD | `+89.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 113,990,000.00 USD | 437.16 USD | 0.00 USD | `+89.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 114,060,000.00 USD | 64,550.00 USD | 0.00 USD | `+90.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 114,060,000.00 USD | 1,610.00 USD | 0.00 USD | `+90.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 114,150,000.00 USD | 94,600.00 USD | 0.00 USD | `+91.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 114,150,000.00 USD | 1,070.00 USD | 0.00 USD | `+91.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 114,170,000.00 USD | 11,270.00 USD | 0.00 USD | `+93.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 114,170,000.00 USD | 2,400.00 USD | 0.00 USD | `+93.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 114,210,000.00 USD | 43,750.00 USD | 0.00 USD | `+94.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 114,280,000.00 USD | 64,570.00 USD | 0.00 USD | `+94.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 114,280,000.00 USD | 1,050.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 114,330,000.00 USD | 57,640.00 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 114,350,000.00 USD | 11,480.00 USD | 0.00 USD | `+96.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 114,350,000.00 USD | 2,510.00 USD | 0.00 USD | `+96.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 114,530,000.00 USD | 177,400.00 USD | 0.00 USD | `+97.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 114,530,000.00 USD | 2,040.00 USD | 0.00 USD | `+98.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 114,530,000.00 USD | 1,030.00 USD | 0.00 USD | `+98.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1972.30` | 868,540,000.00 USD | 0.00 USD | 868,540,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.10` | 868,410,000.00 USD | 0.00 USD | 868,410,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.90` | 868,360,000.00 USD | 0.00 USD | 868,360,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.50` | 866,120,000.00 USD | 0.00 USD | 866,120,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.30` | 865,920,000.00 USD | 0.00 USD | 865,920,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1989.10` | 862,190,000.00 USD | 0.00 USD | 862,190,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1991.90` | 860,370,000.00 USD | 0.00 USD | 860,370,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1994.70` | 857,660,000.00 USD | 0.00 USD | 857,660,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1997.50` | 856,850,000.00 USD | 0.00 USD | 856,850,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1997.60` | 754,480,000.00 USD | 0.00 USD | 754,480,000.00 USD | 206,020.00 USD | 86,340.00 USD | 328,290.00 USD |
| `1D` | `2000.10` | 753,860,000.00 USD | 0.00 USD | 753,860,000.00 USD | 27,360.00 USD | 25,630.00 USD | 586,930.00 USD |
| `1D` | `2002.60` | 753,220,000.00 USD | 0.00 USD | 753,220,000.00 USD | 942,390.00 USD | 700,600.00 USD | 1,180,000.00 USD |
| `7D` | `2003.10` | 855,510,000.00 USD | 0.00 USD | 855,510,000.00 USD | 0.00 USD | 266,430.00 USD | 617,240.00 USD |
| `1D` | `2005.10` | 750,400,000.00 USD | 0.00 USD | 750,400,000.00 USD | 773,690.00 USD | 255,310.00 USD | 9,210.00 USD |
| `7D` | `2005.90` | 854,630,000.00 USD | 0.00 USD | 854,630,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD |
| `1D` | `2007.60` | 749,360,000.00 USD | 0.00 USD | 749,360,000.00 USD | 0.00 USD | 383,650.00 USD | 281,160.00 USD |
| `7D` | `2008.70` | 854,150,000.00 USD | 0.00 USD | 854,150,000.00 USD | 807,770.00 USD | 0.00 USD | 380,820.00 USD |
| `1D` | `2010.10` | 748,700,000.00 USD | 0.00 USD | 748,700,000.00 USD | 460,200.00 USD | 638,030.00 USD | 374,070.00 USD |
| `7D` | `2011.50` | 852,960,000.00 USD | 0.00 USD | 852,960,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2012.60` | 747,220,000.00 USD | 0.00 USD | 747,220,000.00 USD | 348,530.00 USD | 266,130.00 USD | 25,520.00 USD |
| `1D` | `2015.10` | 746,580,000.00 USD | 0.00 USD | 746,580,000.00 USD | 413,060.00 USD | 159,880.00 USD | 202,180.00 USD |
| `7D` | `2017.10` | 852,010,000.00 USD | 0.00 USD | 852,010,000.00 USD | 62,110.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2017.60` | 745,810,000.00 USD | 0.00 USD | 745,810,000.00 USD | 1,140,000.00 USD | 1,500,000.00 USD | 559,250.00 USD |
| `7D` | `2019.90` | 851,930,000.00 USD | 0.00 USD | 851,930,000.00 USD | 1,020,000.00 USD | 466,180.00 USD | 0.00 USD |
| `1D` | `2020.10` | 742,610,000.00 USD | 0.00 USD | 742,610,000.00 USD | 1,340,000.00 USD | 2,190,000.00 USD | 696,790.00 USD |
| `1D` | `2022.60` | 738,380,000.00 USD | 0.00 USD | 738,380,000.00 USD | 1,840,000.00 USD | 628,480.00 USD | 1,890,000.00 USD |
| `7D` | `2022.70` | 850,440,000.00 USD | 0.00 USD | 850,440,000.00 USD | 1,890,000.00 USD | 957,590.00 USD | 1,550,000.00 USD |
| `1D` | `2025.10` | 734,030,000.00 USD | 0.00 USD | 734,030,000.00 USD | 595,510.00 USD | 1,010,000.00 USD | 240,540.00 USD |
| `7D` | `2025.50` | 846,040,000.00 USD | 0.00 USD | 846,040,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.60` | 732,180,000.00 USD | 0.00 USD | 732,180,000.00 USD | 2,550,000.00 USD | 1,160,000.00 USD | 167,580.00 USD |
| `7D` | `2028.30` | 845,870,000.00 USD | 0.00 USD | 845,870,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.10` | 728,310,000.00 USD | 0.00 USD | 728,310,000.00 USD | 307,680.00 USD | 366,120.00 USD | 1,100,000.00 USD |
| `7D` | `2031.10` | 844,730,000.00 USD | 0.00 USD | 844,730,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.60` | 726,530,000.00 USD | 0.00 USD | 726,530,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2033.90` | 840,160,000.00 USD | 0.00 USD | 840,160,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD |
| `1D` | `2035.10` | 722,970,000.00 USD | 0.00 USD | 722,970,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2036.70` | 838,810,000.00 USD | 0.00 USD | 838,810,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.60` | 721,630,000.00 USD | 0.00 USD | 721,630,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD |
| `7D` | `2039.50` | 838,480,000.00 USD | 0.00 USD | 838,480,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.10` | 720,400,000.00 USD | 0.00 USD | 720,400,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD |
| `1D` | `2042.60` | 719,650,000.00 USD | 0.00 USD | 719,650,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD |
| `1D` | `2045.10` | 718,840,000.00 USD | 0.00 USD | 718,840,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `7D` | `2045.10` | 837,020,000.00 USD | 0.00 USD | 837,020,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2047.60` | 718,820,000.00 USD | 0.00 USD | 718,820,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.10` | 717,990,000.00 USD | 0.00 USD | 717,990,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2050.70` | 836,720,000.00 USD | 0.00 USD | 836,720,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2053.50` | 836,500,000.00 USD | 0.00 USD | 836,500,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2055.10` | 716,880,000.00 USD | 0.00 USD | 716,880,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2059.10` | 834,220,000.00 USD | 0.00 USD | 834,220,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2060.10` | 716,520,000.00 USD | 0.00 USD | 716,520,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.90` | 833,870,000.00 USD | 0.00 USD | 833,870,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.60` | 715,770,000.00 USD | 0.00 USD | 715,770,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2064.70` | 828,620,000.00 USD | 0.00 USD | 828,620,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2065.10` | 715,690,000.00 USD | 0.00 USD | 715,690,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `7D` | `2067.50` | 826,150,000.00 USD | 0.00 USD | 826,150,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2067.60` | 714,080,000.00 USD | 0.00 USD | 714,080,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `1D` | `2070.10` | 713,390,000.00 USD | 0.00 USD | 713,390,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2070.30` | 824,510,000.00 USD | 0.00 USD | 824,510,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2072.60` | 713,010,000.00 USD | 0.00 USD | 713,010,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD |
| `7D` | `2073.10` | 816,950,000.00 USD | 0.00 USD | 816,950,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD |
| `1D` | `2075.10` | 711,990,000.00 USD | 0.00 USD | 711,990,000.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2075.90` | 809,870,000.00 USD | 0.00 USD | 809,870,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD |
| `1D` | `2077.60` | 711,960,000.00 USD | 0.00 USD | 711,960,000.00 USD | 354,080.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.70` | 797,360,000.00 USD | 0.00 USD | 797,360,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD |
| `1D` | `2080.10` | 711,580,000.00 USD | 0.00 USD | 711,580,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2081.50` | 787,410,000.00 USD | 0.00 USD | 787,410,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD |
| `1D` | `2082.60` | 711,270,000.00 USD | 0.00 USD | 711,270,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD |
| `7D` | `2084.30` | 780,510,000.00 USD | 0.00 USD | 780,510,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.10` | 710,240,000.00 USD | 0.00 USD | 710,240,000.00 USD | 528,660.00 USD | 200,510.00 USD | 820,410.00 USD |
| `7D` | `2087.10` | 773,120,000.00 USD | 0.00 USD | 773,120,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD |
| `1D` | `2087.60` | 708,690,000.00 USD | 0.00 USD | 708,690,000.00 USD | 324,560.00 USD | 170,940.00 USD | 302,640.00 USD |
| `7D` | `2089.90` | 764,430,000.00 USD | 0.00 USD | 764,430,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD |
| `1D` | `2090.10` | 707,890,000.00 USD | 0.00 USD | 707,890,000.00 USD | 461,140.00 USD | 216,470.00 USD | 251,600.00 USD |
| `1D` | `2092.60` | 706,960,000.00 USD | 0.00 USD | 706,960,000.00 USD | 587,740.00 USD | 226,930.00 USD | 199,290.00 USD |
| `7D` | `2092.70` | 756,190,000.00 USD | 0.00 USD | 756,190,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD |
| `1D` | `2095.10` | 705,950,000.00 USD | 0.00 USD | 705,950,000.00 USD | 1,370,000.00 USD | 838,640.00 USD | 1,080,000.00 USD |
| `7D` | `2095.50` | 744,560,000.00 USD | 0.00 USD | 744,560,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD |
| `1D` | `2097.60` | 702,660,000.00 USD | 0.00 USD | 702,660,000.00 USD | 87,950.00 USD | 672,980.00 USD | 555,060.00 USD |
| `7D` | `2098.30` | 739,050,000.00 USD | 0.00 USD | 739,050,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD |
| `1D` | `2100.10` | 701,340,000.00 USD | 0.00 USD | 701,340,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD |
| `7D` | `2101.10` | 731,430,000.00 USD | 0.00 USD | 731,430,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD |
| `1D` | `2102.60` | 700,050,000.00 USD | 0.00 USD | 700,050,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD |
| `7D` | `2103.90` | 726,160,000.00 USD | 0.00 USD | 726,160,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2105.10` | 699,140,000.00 USD | 0.00 USD | 699,140,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD |
| `7D` | `2106.70` | 721,960,000.00 USD | 0.00 USD | 721,960,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD |
| `1D` | `2107.60` | 693,710,000.00 USD | 0.00 USD | 693,710,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD |
| `7D` | `2109.50` | 718,250,000.00 USD | 0.00 USD | 718,250,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD |
| `1D` | `2110.10` | 692,490,000.00 USD | 0.00 USD | 692,490,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2112.30` | 706,930,000.00 USD | 0.00 USD | 706,930,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD |
| `1D` | `2112.60` | 692,390,000.00 USD | 0.00 USD | 692,390,000.00 USD | 902,600.00 USD | 360,140.00 USD | 221,490.00 USD |
| `1D` | `2115.10` | 690,900,000.00 USD | 0.00 USD | 690,900,000.00 USD | 202,800.00 USD | 411,610.00 USD | 962,630.00 USD |
| `7D` | `2115.10` | 697,820,000.00 USD | 0.00 USD | 697,820,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD |
| `1D` | `2117.60` | 689,330,000.00 USD | 0.00 USD | 689,330,000.00 USD | 4,750,000.00 USD | 4,080,000.00 USD | 302,800.00 USD |
| `7D` | `2117.90` | 691,750,000.00 USD | 0.00 USD | 691,750,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD |
| `1D` | `2120.10` | 680,200,000.00 USD | 0.00 USD | 680,200,000.00 USD | 3,950,000.00 USD | 22,470.00 USD | 645,650.00 USD |
| `7D` | `2120.70` | 680,200,000.00 USD | 0.00 USD | 680,200,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.60` | 675,580,000.00 USD | 0.00 USD | 675,580,000.00 USD | 4,520,000.00 USD | 3,800,000.00 USD | 1,860,000.00 USD |
| `7D` | `2123.50` | 665,540,000.00 USD | 0.00 USD | 665,540,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD |
| `1D` | `2125.10` | 665,410,000.00 USD | 0.00 USD | 665,410,000.00 USD | 6,940,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD |
| `7D` | `2126.30` | 649,260,000.00 USD | 0.00 USD | 649,260,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD |
| `1D` | `2127.60` | 654,530,000.00 USD | 0.00 USD | 654,530,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD |
| `7D` | `2129.10` | 637,330,000.00 USD | 0.00 USD | 637,330,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD |
| `1D` | `2130.10` | 645,140,000.00 USD | 0.00 USD | 645,140,000.00 USD | 1,250,000.00 USD | 172,040.00 USD | 794,920.00 USD |
| `7D` | `2131.90` | 630,190,000.00 USD | 0.00 USD | 630,190,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD |
| `1D` | `2132.60` | 642,920,000.00 USD | 0.00 USD | 642,920,000.00 USD | 81,820.00 USD | 284,820.00 USD | 1,550,000.00 USD |
| `7D` | `2134.70` | 625,040,000.00 USD | 0.00 USD | 625,040,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD |
| `1D` | `2135.10` | 641,000,000.00 USD | 0.00 USD | 641,000,000.00 USD | 2,560,000.00 USD | 2,610,000.00 USD | 1,540,000.00 USD |
| `7D` | `2137.50` | 621,730,000.00 USD | 0.00 USD | 621,730,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,590,000.00 USD |
| `1D` | `2137.60` | 634,290,000.00 USD | 0.00 USD | 634,290,000.00 USD | 889,780.00 USD | 2,180,000.00 USD | 1,940,000.00 USD |
| `1D` | `2140.10` | 629,270,000.00 USD | 0.00 USD | 629,270,000.00 USD | 1,990,000.00 USD | 749,480.00 USD | 758,120.00 USD |
| `7D` | `2140.30` | 615,630,000.00 USD | 0.00 USD | 615,630,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 1,690,000.00 USD |
| `1D` | `2142.60` | 625,770,000.00 USD | 0.00 USD | 625,770,000.00 USD | 873,550.00 USD | 3,390,000.00 USD | 1,100,000.00 USD |
| `7D` | `2143.10` | 608,090,000.00 USD | 0.00 USD | 608,090,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 333,410.00 USD |
| `1D` | `2145.10` | 620,410,000.00 USD | 0.00 USD | 620,410,000.00 USD | 2,780,000.00 USD | 2,360,000.00 USD | 1,220,000.00 USD |
| `7D` | `2145.90` | 604,750,000.00 USD | 0.00 USD | 604,750,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.60` | 614,050,000.00 USD | 0.00 USD | 614,050,000.00 USD | 1,610,000.00 USD | 1,170,000.00 USD | 105,220.00 USD |
| `7D` | `2148.70` | 600,600,000.00 USD | 0.00 USD | 600,600,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD |
| `1D` | `2150.10` | 611,160,000.00 USD | 0.00 USD | 611,160,000.00 USD | 7,520,000.00 USD | 3,310,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.50` | 599,640,000.00 USD | 0.00 USD | 599,640,000.00 USD | 11,350,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2152.60` | 597,670,000.00 USD | 0.00 USD | 597,670,000.00 USD | 5,270,000.00 USD | 3,330,000.00 USD | 1,980,000.00 USD |
| `7D` | `2154.30` | 587,820,000.00 USD | 0.00 USD | 587,820,000.00 USD | 2,590,000.00 USD | 4,660,000.00 USD | 1,580,000.00 USD |
| `1D` | `2155.10` | 587,080,000.00 USD | 0.00 USD | 587,080,000.00 USD | 4,130,000.00 USD | 7,120,000.00 USD | 2,620,000.00 USD |
| `7D` | `2157.10` | 578,990,000.00 USD | 0.00 USD | 578,990,000.00 USD | 6,320,000.00 USD | 3,720,000.00 USD | 6,600,000.00 USD |
| `1D` | `2157.60` | 573,210,000.00 USD | 0.00 USD | 573,210,000.00 USD | 6,160,000.00 USD | 2,080,000.00 USD | 4,850,000.00 USD |
| `7D` | `2159.90` | 562,340,000.00 USD | 0.00 USD | 562,340,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD |
| `1D` | `2160.10` | 560,120,000.00 USD | 0.00 USD | 560,120,000.00 USD | 5,100,000.00 USD | 6,230,000.00 USD | 2,930,000.00 USD |
| `1D` | `2162.60` | 545,870,000.00 USD | 0.00 USD | 545,870,000.00 USD | 17,620,000.00 USD | 10,310,000.00 USD | 1,950,000.00 USD |
| `7D` | `2162.70` | 556,790,000.00 USD | 0.00 USD | 556,790,000.00 USD | 17,980,000.00 USD | 1,960,000.00 USD | 0.00 USD |
| `1D` | `2165.10` | 515,980,000.00 USD | 0.00 USD | 515,980,000.00 USD | 11,270,000.00 USD | 9,810,000.00 USD | 5,000,000.00 USD |
| `7D` | `2165.50` | 536,840,000.00 USD | 0.00 USD | 536,840,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,900,000.00 USD |
| `1D` | `2167.60` | 489,890,000.00 USD | 0.00 USD | 489,890,000.00 USD | 17,280,000.00 USD | 7,820,000.00 USD | 5,200,000.00 USD |
| `7D` | `2168.30` | 507,790,000.00 USD | 0.00 USD | 507,790,000.00 USD | 12,290,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD |
| `1D` | `2170.10` | 459,590,000.00 USD | 0.00 USD | 459,590,000.00 USD | 13,580,000.00 USD | 9,360,000.00 USD | 4,760,000.00 USD |
| `7D` | `2171.10` | 475,580,000.00 USD | 0.00 USD | 475,580,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD |
| `1D` | `2172.60` | 431,890,000.00 USD | 0.00 USD | 431,890,000.00 USD | 16,900,000.00 USD | 5,140,000.00 USD | 4,630,000.00 USD |
| `7D` | `2173.90` | 461,780,000.00 USD | 0.00 USD | 461,780,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD |
| `1D` | `2175.10` | 405,220,000.00 USD | 0.00 USD | 405,220,000.00 USD | 5,740,000.00 USD | 0.00 USD | 2,380,000.00 USD |
| `7D` | `2176.70` | 425,680,000.00 USD | 0.00 USD | 425,680,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.60` | 397,100,000.00 USD | 0.00 USD | 397,100,000.00 USD | 920,620.00 USD | 869,570.00 USD | 3,360,000.00 USD |
| `7D` | `2179.50` | 421,400,000.00 USD | 0.00 USD | 421,400,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD |
| `1D` | `2180.10` | 391,950,000.00 USD | 0.00 USD | 391,950,000.00 USD | 6,340,000.00 USD | 5,030,000.00 USD | 6,660,000.00 USD |
| `7D` | `2182.30` | 414,710,000.00 USD | 0.00 USD | 414,710,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,770,000.00 USD |
| `1D` | `2182.60` | 373,920,000.00 USD | 0.00 USD | 373,920,000.00 USD | 2,210,000.00 USD | 2,710,000.00 USD | 4,040,000.00 USD |
| `1D` | `2185.10` | 364,950,000.00 USD | 0.00 USD | 364,950,000.00 USD | 3,730,000.00 USD | 2,560,000.00 USD | 5,600,000.00 USD |
| `7D` | `2185.10` | 408,020,000.00 USD | 0.00 USD | 408,020,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 3,070,000.00 USD |
| `1D` | `2187.60` | 353,050,000.00 USD | 0.00 USD | 353,050,000.00 USD | 5,040,000.00 USD | 4,480,000.00 USD | 6,890,000.00 USD |
| `7D` | `2187.90` | 343,160,000.00 USD | 0.00 USD | 343,160,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,730,000.00 USD |
| `1D` | `2190.10` | 336,640,000.00 USD | 0.00 USD | 336,640,000.00 USD | 8,990,000.00 USD | 4,160,000.00 USD | 6,930,000.00 USD |
| `7D` | `2190.70` | 339,060,000.00 USD | 0.00 USD | 339,060,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD |
| `1D` | `2192.60` | 316,570,000.00 USD | 0.00 USD | 316,570,000.00 USD | 5,000,000.00 USD | 5,340,000.00 USD | 1,290,000.00 USD |
| `7D` | `2193.50` | 292,240,000.00 USD | 0.00 USD | 292,240,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2195.10` | 304,930,000.00 USD | 0.00 USD | 304,930,000.00 USD | 6,730,000.00 USD | 3,350,000.00 USD | 5,950,000.00 USD |
| `7D` | `2196.30` | 276,780,000.00 USD | 0.00 USD | 276,780,000.00 USD | 694,220.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2197.60` | 288,900,000.00 USD | 0.00 USD | 288,900,000.00 USD | 10,200,000.00 USD | 3,830,000.00 USD | 4,940,000.00 USD |
| `7D` | `2199.10` | 275,730,000.00 USD | 0.00 USD | 275,730,000.00 USD | 5,090,000.00 USD | 5,270,000.00 USD | 7,440,000.00 USD |
| `1D` | `2200.10` | 269,920,000.00 USD | 0.00 USD | 269,920,000.00 USD | 10,980,000.00 USD | 10,470,000.00 USD | 10,900,000.00 USD |
| `7D` | `2201.90` | 257,940,000.00 USD | 0.00 USD | 257,940,000.00 USD | 13,210,000.00 USD | 6,520,000.00 USD | 21,720,000.00 USD |
| `1D` | `2202.60` | 237,570,000.00 USD | 0.00 USD | 237,570,000.00 USD | 19,040,000.00 USD | 14,300,000.00 USD | 17,770,000.00 USD |
| `7D` | `2204.70` | 216,500,000.00 USD | 0.00 USD | 216,500,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,660,000.00 USD |
| `1D` | `2205.10` | 186,450,000.00 USD | 0.00 USD | 186,450,000.00 USD | 11,730,000.00 USD | 7,020,000.00 USD | 4,880,000.00 USD |
| `7D` | `2207.50` | 202,160,000.00 USD | 0.00 USD | 202,160,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 7,200,000.00 USD |
| `1D` | `2207.60` | 162,820,000.00 USD | 0.00 USD | 162,820,000.00 USD | 13,820,000.00 USD | 6,420,000.00 USD | 5,600,000.00 USD |
| `1D` | `2210.10` | 136,990,000.00 USD | 0.00 USD | 136,990,000.00 USD | 4,040,000.00 USD | 7,220,000.00 USD | 6,410,000.00 USD |
| `7D` | `2210.30` | 171,940,000.00 USD | 0.00 USD | 171,940,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,560,000.00 USD |
| `1D` | `2212.60` | 119,330,000.00 USD | 0.00 USD | 119,330,000.00 USD | 12,700,000.00 USD | 6,410,000.00 USD | 1,990,000.00 USD |
| `7D` | `2213.10` | 155,640,000.00 USD | 0.00 USD | 155,640,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD |
| `1D` | `2215.10` | 98,220,000.00 USD | 0.00 USD | 98,220,000.00 USD | 2,300,000.00 USD | 2,930,000.00 USD | 280,820.00 USD |
| `7D` | `2215.90` | 143,100,000.00 USD | 0.00 USD | 143,100,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2217.60` | 92,720,000.00 USD | 0.00 USD | 92,720,000.00 USD | 2,810,000.00 USD | 4,440,000.00 USD | 3,930,000.00 USD |
| `7D` | `2218.70` | 142,530,000.00 USD | 0.00 USD | 142,530,000.00 USD | 23,020,000.00 USD | 487,520.00 USD | 218,310.00 USD |
| `1D` | `2220.10` | 81,530,000.00 USD | 0.00 USD | 81,530,000.00 USD | 17,480,000.00 USD | 7,250,000.00 USD | 4,070,000.00 USD |
| `7D` | `2221.50` | 118,810,000.00 USD | 0.00 USD | 118,810,000.00 USD | 10,170,000.00 USD | 19,850,000.00 USD | 18,870,000.00 USD |
| `1D` | `2222.60` | 52,730,000.00 USD | 0.00 USD | 52,730,000.00 USD | 8,350,000.00 USD | 14,430,000.00 USD | 1,640,000.00 USD |
| `7D` | `2224.30` | 69,920,000.00 USD | 0.00 USD | 69,920,000.00 USD | 8,200,000.00 USD | 12,510,000.00 USD | 6,530,000.00 USD |
| `1D` | `2225.10` | 28,310,000.00 USD | 0.00 USD | 28,310,000.00 USD | 5,440,000.00 USD | 2,560,000.00 USD | 3,260,000.00 USD |
| `7D` | `2227.10` | 42,690,000.00 USD | 0.00 USD | 42,690,000.00 USD | 557,870.00 USD | 0.00 USD | 6,860,000.00 USD |
| `1D` | `2227.60` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 2,850,000.00 USD | 0.00 USD | 111,560.00 USD |
| `7D` | `2229.90` | 35,270,000.00 USD | 0.00 USD | 35,270,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2230.10` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 113,200.00 USD |
| `1D` | `2232.60` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2235.50` | 33,370,000.00 USD | 0.00 USD | 33,370,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 0.00 USD |
| `1D` | `2237.60` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.30` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.10` | 21,970.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD |
| `1D` | `2241.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2242.60` | 22,480.00 USD | 22,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,480.00 USD |
| `7D` | `2243.90` | 268,650.00 USD | 268,650.00 USD | 0.00 USD | 0.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2245.10` | 84,720.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62,250.00 USD |
| `7D` | `2246.70` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 1,300,000.00 USD | 709,510.00 USD |
| `1D` | `2247.60` | 627,550.00 USD | 627,550.00 USD | 0.00 USD | 0.00 USD | 243,170.00 USD | 299,650.00 USD |
| `7D` | `2249.50` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 861,640.00 USD | 2,660,000.00 USD | 867,440.00 USD |
| `1D` | `2250.10` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 255,300.00 USD | 446,930.00 USD | 1,680,000.00 USD |
| `7D` | `2252.30` | 31,940,000.00 USD | 31,940,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 3,550,000.00 USD |
| `1D` | `2252.60` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 1,470,000.00 USD | 3,300,000.00 USD | 3,430,000.00 USD |
| `1D` | `2255.10` | 36,260,000.00 USD | 36,260,000.00 USD | 0.00 USD | 12,360,000.00 USD | 6,830,000.00 USD | 5,870,000.00 USD |
| `7D` | `2255.10` | 49,360,000.00 USD | 49,360,000.00 USD | 0.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 774,210.00 USD |
| `1D` | `2257.60` | 70,410,000.00 USD | 70,410,000.00 USD | 0.00 USD | 19,980,000.00 USD | 8,290,000.00 USD | 5,870,000.00 USD |
| `7D` | `2257.90` | 89,060,000.00 USD | 89,060,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD |
| `1D` | `2260.10` | 92,470,000.00 USD | 92,470,000.00 USD | 0.00 USD | 9,050,000.00 USD | 10,340,000.00 USD | 2,680,000.00 USD |
| `7D` | `2260.70` | 93,380,000.00 USD | 93,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD |
| `1D` | `2262.60` | 120,860,000.00 USD | 120,860,000.00 USD | 0.00 USD | 15,390,000.00 USD | 6,760,000.00 USD | 6,230,000.00 USD |
| `7D` | `2263.50` | 102,390,000.00 USD | 102,390,000.00 USD | 0.00 USD | 7,340,000.00 USD | 1,460,000.00 USD | 218,310.00 USD |
| `1D` | `2265.10` | 166,830,000.00 USD | 166,830,000.00 USD | 0.00 USD | 19,500,000.00 USD | 16,750,000.00 USD | 9,710,000.00 USD |
| `7D` | `2266.30` | 134,680,000.00 USD | 134,680,000.00 USD | 0.00 USD | 10,170,000.00 USD | 15,790,000.00 USD | 6,330,000.00 USD |
| `1D` | `2267.60` | 222,770,000.00 USD | 222,770,000.00 USD | 0.00 USD | 20,700,000.00 USD | 22,510,000.00 USD | 12,730,000.00 USD |
| `7D` | `2269.10` | 190,860,000.00 USD | 190,860,000.00 USD | 0.00 USD | 19,210,000.00 USD | 12,640,000.00 USD | 24,330,000.00 USD |
| `1D` | `2270.10` | 282,240,000.00 USD | 282,240,000.00 USD | 0.00 USD | 23,390,000.00 USD | 12,160,000.00 USD | 23,930,000.00 USD |
| `7D` | `2271.90` | 219,760,000.00 USD | 219,760,000.00 USD | 0.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 7,010,000.00 USD |
| `1D` | `2272.60` | 313,170,000.00 USD | 313,170,000.00 USD | 0.00 USD | 19,020,000.00 USD | 5,610,000.00 USD | 6,290,000.00 USD |
| `7D` | `2274.70` | 248,060,000.00 USD | 248,060,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 1,770,000.00 USD |
| `1D` | `2275.10` | 360,690,000.00 USD | 360,690,000.00 USD | 0.00 USD | 27,310,000.00 USD | 15,610,000.00 USD | 4,600,000.00 USD |
| `7D` | `2277.50` | 274,450,000.00 USD | 274,450,000.00 USD | 0.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,610,000.00 USD |
| `1D` | `2277.60` | 398,310,000.00 USD | 398,310,000.00 USD | 0.00 USD | 10,430,000.00 USD | 15,200,000.00 USD | 11,990,000.00 USD |
| `1D` | `2280.10` | 446,800,000.00 USD | 446,800,000.00 USD | 0.00 USD | 26,670,000.00 USD | 9,750,000.00 USD | 12,070,000.00 USD |
| `7D` | `2280.30` | 318,770,000.00 USD | 318,770,000.00 USD | 0.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD |
| `1D` | `2282.60` | 501,330,000.00 USD | 501,330,000.00 USD | 0.00 USD | 22,560,000.00 USD | 24,830,000.00 USD | 7,150,000.00 USD |
| `7D` | `2283.10` | 410,580,000.00 USD | 410,580,000.00 USD | 0.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD |
| `1D` | `2285.10` | 529,190,000.00 USD | 529,190,000.00 USD | 0.00 USD | 11,520,000.00 USD | 9,410,000.00 USD | 6,920,000.00 USD |
| `7D` | `2285.90` | 414,600,000.00 USD | 414,600,000.00 USD | 0.00 USD | 1,320,000.00 USD | 2,590,000.00 USD | 109,160.00 USD |
| `1D` | `2287.60` | 568,320,000.00 USD | 568,320,000.00 USD | 0.00 USD | 19,470,000.00 USD | 11,060,000.00 USD | 8,600,000.00 USD |
| `7D` | `2288.70` | 456,130,000.00 USD | 456,130,000.00 USD | 0.00 USD | 13,470,000.00 USD | 13,140,000.00 USD | 14,930,000.00 USD |
| `1D` | `2290.10` | 614,240,000.00 USD | 614,240,000.00 USD | 0.00 USD | 19,770,000.00 USD | 21,020,000.00 USD | 5,130,000.00 USD |
| `7D` | `2291.50` | 481,440,000.00 USD | 481,440,000.00 USD | 0.00 USD | 8,400,000.00 USD | 6,770,000.00 USD | 10,140,000.00 USD |
| `1D` | `2292.60` | 648,230,000.00 USD | 648,230,000.00 USD | 0.00 USD | 17,860,000.00 USD | 4,710,000.00 USD | 11,420,000.00 USD |
| `7D` | `2294.30` | 502,780,000.00 USD | 502,780,000.00 USD | 0.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD |
| `1D` | `2295.10` | 684,840,000.00 USD | 684,840,000.00 USD | 0.00 USD | 12,280,000.00 USD | 13,600,000.00 USD | 10,720,000.00 USD |
| `7D` | `2297.10` | 552,530,000.00 USD | 552,530,000.00 USD | 0.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD |
| `1D` | `2297.60` | 731,170,000.00 USD | 731,170,000.00 USD | 0.00 USD | 29,190,000.00 USD | 11,160,000.00 USD | 5,980,000.00 USD |
| `7D` | `2299.90` | 595,450,000.00 USD | 595,450,000.00 USD | 0.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD |
| `1D` | `2300.10` | 770,690,000.00 USD | 770,690,000.00 USD | 0.00 USD | 11,250,000.00 USD | 14,710,000.00 USD | 13,570,000.00 USD |
| `1D` | `2302.60` | 798,290,000.00 USD | 798,290,000.00 USD | 0.00 USD | 16,060,000.00 USD | 2,700,000.00 USD | 8,840,000.00 USD |
| `7D` | `2302.70` | 650,110,000.00 USD | 650,110,000.00 USD | 0.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD |
| `1D` | `2305.10` | 837,020,000.00 USD | 837,020,000.00 USD | 0.00 USD | 14,970,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD |
| `7D` | `2305.50` | 676,130,000.00 USD | 676,130,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD |
| `1D` | `2307.60` | 848,320,000.00 USD | 848,320,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,680,000.00 USD | 3,230,000.00 USD |
| `7D` | `2308.30` | 678,430,000.00 USD | 678,430,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD |
| `1D` | `2310.10` | 866,820,000.00 USD | 866,820,000.00 USD | 0.00 USD | 4,990,000.00 USD | 2,820,000.00 USD | 10,690,000.00 USD |
| `7D` | `2311.10` | 708,930,000.00 USD | 708,930,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD |
| `1D` | `2312.60` | 883,400,000.00 USD | 883,400,000.00 USD | 0.00 USD | 6,950,000.00 USD | 8,040,000.00 USD | 1,590,000.00 USD |
| `7D` | `2313.90` | 719,750,000.00 USD | 719,750,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD |
| `1D` | `2315.10` | 905,950,000.00 USD | 905,950,000.00 USD | 0.00 USD | 5,980,000.00 USD | 13,500,000.00 USD | 3,070,000.00 USD |
| `7D` | `2316.70` | 725,500,000.00 USD | 725,500,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,090,000.00 USD |
| `1D` | `2317.60` | 933,100,000.00 USD | 933,100,000.00 USD | 0.00 USD | 8,220,000.00 USD | 10,500,000.00 USD | 8,440,000.00 USD |
| `7D` | `2319.50` | 755,660,000.00 USD | 755,660,000.00 USD | 0.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 8,780,000.00 USD |
| `1D` | `2320.10` | 958,960,000.00 USD | 958,960,000.00 USD | 0.00 USD | 10,150,000.00 USD | 12,260,000.00 USD | 3,450,000.00 USD |
| `7D` | `2322.30` | 761,580,000.00 USD | 761,580,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 172,940.00 USD |
| `1D` | `2322.60` | 976,910,000.00 USD | 976,910,000.00 USD | 0.00 USD | 3,370,000.00 USD | 9,320,000.00 USD | 5,260,000.00 USD |
| `1D` | `2325.10` | 990,830,000.00 USD | 990,830,000.00 USD | 0.00 USD | 3,060,000.00 USD | 9,360,000.00 USD | 1,500,000.00 USD |
| `7D` | `2325.10` | 784,620,000.00 USD | 784,620,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2327.60` | 997,390,000.00 USD | 997,390,000.00 USD | 0.00 USD | 553,100.00 USD | 1,410,000.00 USD | 4,590,000.00 USD |
| `7D` | `2327.90` | 796,510,000.00 USD | 796,510,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD |
| `1D` | `2330.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 11,750,000.00 USD | 3,450,000.00 USD | 1,250,000.00 USD |
| `7D` | `2330.70` | 812,890,000.00 USD | 812,890,000.00 USD | 0.00 USD | 15,960,000.00 USD | 363,770.00 USD | 54,580.00 USD |
| `1D` | `2332.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 5,020,000.00 USD | 3,500,000.00 USD | 6,280,000.00 USD |
| `7D` | `2333.50` | 858,190,000.00 USD | 858,190,000.00 USD | 0.00 USD | 22,570,000.00 USD | 14,770,000.00 USD | 7,960,000.00 USD |
| `1D` | `2335.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,590,000.00 USD | 5,870,000.00 USD |
| `7D` | `2336.30` | 902,400,000.00 USD | 902,400,000.00 USD | 0.00 USD | 26,590,000.00 USD | 10,690,000.00 USD | 6,930,000.00 USD |
| `1D` | `2337.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 14,050,000.00 USD | 1,830,000.00 USD | 6,590,000.00 USD |
| `7D` | `2339.10` | 928,810,000.00 USD | 928,810,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD |
| `1D` | `2340.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 11,670,000.00 USD | 6,260,000.00 USD | 12,150,000.00 USD |
| `7D` | `2341.90` | 969,240,000.00 USD | 969,240,000.00 USD | 0.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 8,670,000.00 USD | 4,470,000.00 USD | 2,450,000.00 USD |
| `7D` | `2344.70` | 997,150,000.00 USD | 997,150,000.00 USD | 0.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD |
| `1D` | `2345.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 5,430,000.00 USD | 8,130,000.00 USD | 8,300,000.00 USD |
| `7D` | `2347.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD |
| `1D` | `2347.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,960,000.00 USD | 3,520,000.00 USD | 2,590,000.00 USD |
| `1D` | `2350.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 23,260,000.00 USD | 6,880,000.00 USD | 10,080,000.00 USD |
| `7D` | `2350.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD |
| `1D` | `2352.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,400,000.00 USD | 2,670,000.00 USD |
| `7D` | `2353.10` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD |
| `1D` | `2355.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 2,320,000.00 USD | 3,770,000.00 USD | 951,670.00 USD |
| `7D` | `2355.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD |
| `1D` | `2357.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 3,780,000.00 USD | 4,290,000.00 USD | 3,440,000.00 USD |
| `7D` | `2358.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2360.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 9,090,000.00 USD | 4,260,000.00 USD | 5,450,000.00 USD |
| `7D` | `2361.50` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2362.60` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 8,700,000.00 USD | 6,710,000.00 USD | 7,910,000.00 USD |
| `7D` | `2364.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2365.10` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,010,000.00 USD | 3,660,000.00 USD |
| `7D` | `2367.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD |
| `1D` | `2367.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 1,110,000.00 USD | 1,910,000.00 USD |
| `7D` | `2369.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD |
| `1D` | `2370.10` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 10,250,000.00 USD | 7,700,000.00 USD | 5,150,000.00 USD |
| `1D` | `2372.60` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 11,280,000.00 USD | 1,790,000.00 USD | 4,460,000.00 USD |
| `7D` | `2372.70` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD |
| `1D` | `2375.10` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 5,700,000.00 USD | 557,400.00 USD | 1,840,000.00 USD |
| `7D` | `2375.50` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD |
| `1D` | `2377.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 3,340,000.00 USD | 3,070,000.00 USD | 4,510,000.00 USD |
| `7D` | `2378.30` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD |
| `1D` | `2380.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 389,290.00 USD | 4,780,000.00 USD |
| `7D` | `2381.10` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD |
| `1D` | `2382.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,550,000.00 USD |
| `7D` | `2383.90` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD |
| `1D` | `2385.10` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 7,540,000.00 USD | 11,520,000.00 USD | 4,750,000.00 USD |
| `7D` | `2386.70` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD |
| `1D` | `2387.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 9,850,000.00 USD | 5,970,000.00 USD | 3,120,000.00 USD |
| `7D` | `2389.50` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD |
| `1D` | `2390.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD |
| `7D` | `2392.30` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD |
| `1D` | `2392.60` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD |
| `1D` | `2395.10` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,830,000.00 USD | 2,170,000.00 USD |
| `7D` | `2395.10` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD |
| `1D` | `2397.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,400,000.00 USD |
| `7D` | `2397.90` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD |
| `1D` | `2400.10` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2400.70` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 0.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD |
| `1D` | `2402.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD |
| `7D` | `2403.50` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD |
| `1D` | `2405.10` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 5,960,000.00 USD | 3,440,000.00 USD | 4,950,000.00 USD |
| `7D` | `2406.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD |
| `1D` | `2407.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 6,810,000.00 USD | 3,500,000.00 USD | 1,910,000.00 USD |
| `7D` | `2409.10` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD |
| `1D` | `2410.10` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,540,000.00 USD | 3,330,000.00 USD |
| `7D` | `2411.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD |
| `1D` | `2412.60` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 4,850,000.00 USD | 2,970,000.00 USD | 1,430,000.00 USD |
| `7D` | `2414.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD |
| `1D` | `2415.10` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,910,000.00 USD | 2,560,000.00 USD |
| `7D` | `2417.50` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD |
| `1D` | `2417.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,260,000.00 USD | 707,890.00 USD |
| `1D` | `2420.10` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 5,060,000.00 USD | 2,860,000.00 USD | 2,950,000.00 USD |
| `7D` | `2420.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD |
| `1D` | `2422.60` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 693,410.00 USD | 2,620,000.00 USD | 3,180,000.00 USD |
| `7D` | `2423.10` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD |
| `1D` | `2425.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 510,650.00 USD | 623,850.00 USD | 888,640.00 USD |
| `7D` | `2425.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 12,980,000.00 USD | 15,010,000.00 USD | 17,380,000.00 USD |
| `1D` | `2427.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 603,040.00 USD |
| `7D` | `2428.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD |
| `1D` | `2430.10` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD |
| `7D` | `2431.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,250,000.00 USD |
| `1D` | `2432.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 691,800.00 USD |
| `7D` | `2434.30` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 8,200,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD |
| `1D` | `2435.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 559,660.00 USD | 1,370,000.00 USD |
| `7D` | `2437.10` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD |
| `1D` | `2437.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD |
| `7D` | `2439.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD |
| `1D` | `2440.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,240,000.00 USD | 502,040.00 USD | 304,820.00 USD |
| `1D` | `2442.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 743,640.00 USD | 827,820.00 USD |
| `7D` | `2442.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD |
| `1D` | `2445.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 218,020.00 USD | 703,990.00 USD | 1,240,000.00 USD |
| `7D` | `2445.50` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD |
| `1D` | `2447.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 751,450.00 USD | 1,860,000.00 USD |
| `7D` | `2448.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 10,750,000.00 USD | 3,620,000.00 USD | 13,290,000.00 USD |
| `1D` | `2450.10` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 627,630.00 USD | 311,480.00 USD | 35,990.00 USD |
| `7D` | `2451.10` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD |
| `1D` | `2452.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,840,000.00 USD | 2,450,000.00 USD |
| `7D` | `2453.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,970,000.00 USD |
| `1D` | `2455.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,990,000.00 USD | 994,080.00 USD |
| `7D` | `2456.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 5,900,000.00 USD | 7,380,000.00 USD | 7,530,000.00 USD |
| `1D` | `2457.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,980,000.00 USD | 845,630.00 USD |
| `7D` | `2459.50` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD |
| `1D` | `2460.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,530,000.00 USD | 1,370,000.00 USD | 388,420.00 USD |
| `7D` | `2462.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD |
| `1D` | `2462.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 413,060.00 USD | 629,460.00 USD | 851,570.00 USD |
| `1D` | `2465.10` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,050,000.00 USD | 525,020.00 USD |
| `7D` | `2465.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 4,960,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD |
| `1D` | `2467.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 1,580,000.00 USD | 377,900.00 USD |
| `7D` | `2467.90` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 3,830,000.00 USD | 2,330,000.00 USD | 23,760.00 USD |
| `1D` | `2470.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,440,000.00 USD | 2,220,000.00 USD | 1,670,000.00 USD |
| `7D` | `2470.70` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 4,870,000.00 USD | 3,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `2472.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 653,960.00 USD | 275,370.00 USD | 1,160,000.00 USD |
| `7D` | `2473.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `1D` | `2475.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 595,510.00 USD | 914,780.00 USD | 231,680.00 USD |
| `7D` | `2476.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD |
| `1D` | `2477.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 2,200,000.00 USD | 405,410.00 USD | 156,140.00 USD |
| `7D` | `2479.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD |
| `1D` | `2480.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 567,450.00 USD | 943,540.00 USD | 731,890.00 USD |
| `7D` | `2481.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.70` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.50` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.30` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD |
| `7D` | `2491.80` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.67B` | Total OI Tokens: `12,785,087.1 ETH`
  * 1h OI Change: `+0.82%` | 4h OI Change: `-1.13%` | 24h OI Change: `-5.27%`
  * Exchange Breakdown: Binance=`8.49B` | Bybit=`2.11B` | OKX=`1.76B` | Hyperliquid=`2.32B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `202.89K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0005%` | **USDT OKX** | `0.0016%` |
| **USDT Bybit** | `0.0025%` | **USDT KuCoin** | `-0.0021%` |
| **USDT MEXC** | `-0.0003%` | **USDT BingX** | `0.0051%` |
| **USDT Gate** | `0.0068%` | **USDT Bitget** | `0.0052%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0025%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
| `15M` | `Binance` | `39.66%` | `60.34%` | `0.66` | 117,690,000.00 USD |
| `15M` | `OKX` | `45.16%` | `54.84%` | `0.82` | 48,650,000.00 USD |
| `15M` | `Bybit` | `47.94%` | `52.06%` | `0.92` | 43,720,000.00 USD |
| `15M` | `KuCoin` | `27.83%` | `72.17%` | `0.39` | 3,230,000.00 USD |
| `15M` | `Gate` | `44.54%` | `55.46%` | `0.80` | 37,920,000.00 USD |
| `15M` | `Bitget` | `44.67%` | `55.33%` | `0.81` | 16,680,000.00 USD |
| `15M` | `BingX` | `39.66%` | `60.34%` | `0.66` | 6,250,000.00 USD |
| `15M` | `MEXC` | `44.9%` | `55.1%` | `0.81` | 19,050,000.00 USD |
| `15M` | `Bitunix` | `43.94%` | `56.06%` | `0.78` | 15,450,000.00 USD |
| `15M` | `Hyperliquid` | `67.77%` | `32.23%` | `2.10` | 11,020,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.77%` | `49.23%` | `1.03` | 5,200,000.00 USD |
| `15M` | `Crypto.com` | `60.6%` | `39.4%` | `1.54` | 1,910,000.00 USD |
| `15M` | `WhiteBIT` | `0.08%` | `99.92%` | `0.00` | 4,220,000.00 USD |
| `15M` | `HTX` | `42.72%` | `57.28%` | `0.75` | 1,780,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `49.39%` | `50.61%` | `0.98` | 21,020,000.00 USD |
| `15M` | `Bitfinex` | `48.18%` | `51.82%` | `0.93` | 611,040.00 USD |
| `15M` | `Kraken` | `39.13%` | `60.87%` | `0.64` | 3,810,000.00 USD |
| `15M` | `Aster` | `33.84%` | `66.16%` | `0.51` | 7,620,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.41%` | `46.59%` | `1.15` | 4,080,000.00 USD |
| `15M` | `Whale Positions` | `39.66%` | `60.34%` | `0.66` | 117,690,000.00 USD |
| `15M` | `Global Accounts` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
| `1H` | `ETH` | `52.85%` | `47.15%` | `1.12` | 2,350,000,000.00 USD |
| `1H` | `Binance` | `50.09%` | `49.91%` | `1.00` | 769,630,000.00 USD |
| `1H` | `OKX` | `57.28%` | `42.72%` | `1.34` | 315,020,000.00 USD |
| `1H` | `Bybit` | `54.95%` | `45.05%` | `1.22` | 252,410,000.00 USD |
| `1H` | `KuCoin` | `43.95%` | `56.05%` | `0.78` | 5,190,000.00 USD |
| `1H` | `Gate` | `49.05%` | `50.95%` | `0.96` | 281,920,000.00 USD |
| `1H` | `Bitget` | `52.27%` | `47.73%` | `1.10` | 98,380,000.00 USD |
| `1H` | `BingX` | `58.49%` | `41.51%` | `1.41` | 46,420,000.00 USD |
| `1H` | `MEXC` | `55.85%` | `44.15%` | `1.27` | 134,600,000.00 USD |
| `1H` | `Bitunix` | `56.51%` | `43.49%` | `1.30` | 97,340,000.00 USD |
| `1H` | `Hyperliquid` | `71.61%` | `28.39%` | `2.52` | 96,450,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.59%` | `41.41%` | `1.41` | 17,410,000.00 USD |
| `1H` | `Crypto.com` | `52.25%` | `47.75%` | `1.09` | 9,610,000.00 USD |
| `1H` | `WhiteBIT` | `38.84%` | `61.16%` | `0.64` | 9,890,000.00 USD |
| `1H` | `HTX` | `56.78%` | `43.22%` | `1.31` | 7,290,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `45.28%` | `54.72%` | `0.83` | 108,430,000.00 USD |
| `1H` | `Bitfinex` | `59.31%` | `40.69%` | `1.46` | 3,860,000.00 USD |
| `1H` | `Kraken` | `49.17%` | `50.83%` | `0.97` | 24,530,000.00 USD |
| `1H` | `Aster` | `44.1%` | `55.9%` | `0.79` | 40,330,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.47%` | `54.53%` | `0.83` | 25,800,000.00 USD |
| `1H` | `Whale Positions` | `50.09%` | `49.91%` | `1.00` | 769,630,000.00 USD |
| `1H` | `Global Accounts` | `52.85%` | `47.15%` | `1.12` | 2,350,000,000.00 USD |
| `4H` | `ETH` | `46.66%` | `53.34%` | `0.87` | 10,830,000,000.00 USD |
| `4H` | `Binance` | `44.74%` | `55.26%` | `0.81` | 3,180,000,000.00 USD |
| `4H` | `OKX` | `49.3%` | `50.7%` | `0.97` | 1,520,000,000.00 USD |
| `4H` | `Bybit` | `45.9%` | `54.1%` | `0.85` | 963,310,000.00 USD |
| `4H` | `KuCoin` | `51.45%` | `48.55%` | `1.06` | 29,190,000.00 USD |
| `4H` | `Gate` | `50.72%` | `49.28%` | `1.03` | 1,090,000,000.00 USD |
| `4H` | `Bitget` | `43.9%` | `56.1%` | `0.78` | 486,630,000.00 USD |
| `4H` | `BingX` | `49.35%` | `50.65%` | `0.97` | 204,830,000.00 USD |
| `4H` | `MEXC` | `47.17%` | `52.83%` | `0.89` | 521,780,000.00 USD |
| `4H` | `Bitunix` | `48.26%` | `51.74%` | `0.93` | 441,020,000.00 USD |
| `4H` | `Hyperliquid` | `43.49%` | `56.51%` | `0.77` | 618,480,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.45%` | `49.55%` | `1.02` | 692,800,000.00 USD |
| `4H` | `Crypto.com` | `46.68%` | `53.32%` | `0.88` | 37,040,000.00 USD |
| `4H` | `WhiteBIT` | `16.56%` | `83.44%` | `0.20` | 192,110,000.00 USD |
| `4H` | `HTX` | `45.06%` | `54.94%` | `0.82` | 37,440,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `52.2%` | `47.8%` | `1.09` | 517,040,000.00 USD |
| `4H` | `Bitfinex` | `50.36%` | `49.64%` | `1.01` | 8,090,000.00 USD |
| `4H` | `Kraken` | `47.75%` | `52.25%` | `0.91` | 68,380,000.00 USD |
| `4H` | `Aster` | `45.13%` | `54.87%` | `0.82` | 117,290,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.84%` | `49.16%` | `1.03` | 104,150,000.00 USD |
| `4H` | `Whale Positions` | `44.74%` | `55.26%` | `0.81` | 3,180,000,000.00 USD |
| `4H` | `Global Accounts` | `46.66%` | `53.34%` | `0.87` | 10,830,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2223.05` | `2221.75` | `2226.25` | `2220.25` | 71,858,619.15 USD | 38,686,757.89 USD | 33,171,861.26 USD | 5,514,896.63 USD | `+7.67%` | `0B / 0S` |
| `0:00 UTC` | `2229.25` | `2226.54` | `2229.25` | `2231.25` | `2220.25` | 81,297,282.61 USD | 40,950,851.56 USD | 40,346,431.05 USD | 604,420.51 USD | `+0.74%` | `0B / 2S` |
| `5:00 UTC` | `2227.25` | `2227.77` | `2227.25` | `2229.75` | `2226.25` | 53,422,952.94 USD | 29,109,463.85 USD | 24,313,489.09 USD | 4,795,974.76 USD | `+8.98%` | `1B / 0S` |
| `0:00 UTC` | `2223.75` | `2224.01` | `2223.75` | `2228.25` | `2221.75` | 56,423,190.50 USD | 27,667,054.76 USD | 28,756,135.74 USD | -1,089,080.98 USD | `-1.93%` | `0B / 3S` |
| `5:00 UTC` | `2222.25` | `2225.79` | `2222.25` | `2230.75` | `2220.25` | 60,731,653.97 USD | 32,744,113.06 USD | 27,987,540.91 USD | 4,756,572.15 USD | `+7.83%` | `4B / 1S` |
| `0:00 UTC` | `2245.25` | `2240.77` | `2245.25` | `2248.75` | `2228.25` | 194,501,635.59 USD | 112,910,472.81 USD | 81,591,162.78 USD | 31,319,310.03 USD | `+16.10%` | `7B / 0S` |
| `5:00 UTC` | `2241.25` | `2243.75` | `2241.25` | `2248.75` | `2240.25` | 86,877,812.25 USD | 38,844,351.80 USD | 48,033,460.45 USD | -9,189,108.64 USD | `-10.58%` | `1B / 1S` |
| `0:00 UTC` | `2245.75` | `2246.97` | `2245.75` | `2251.75` | `2242.75` | 72,367,813.73 USD | 32,722,639.42 USD | 39,645,174.31 USD | -6,922,534.89 USD | `-9.57%` | `2B / 1S` |
| `5:00 UTC` | `2242.75` | `2242.41` | `2242.75` | `2244.25` | `2240.75` | 15,895,607.30 USD | 5,986,338.35 USD | 9,909,268.95 USD | -3,922,930.60 USD | `-24.68%` | `0B / 2S` |

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
| `5m` | 112,350.00 USD | -17,890,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,220,000.00 USD | -36,640,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,990,000.00 USD | -33,620,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 15,490,000.00 USD | 63,240,000.00 USD | **`ACCUMULATION`** |
| `2h` | 5,050,000.00 USD | 79,150,000.00 USD | **`ACCUMULATION`** |
| `4h` | -17,530,000.00 USD | -33,830,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,570,000.00 USD | -52,110,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 5,590,000.00 USD | 120,980,000.00 USD | **`ACCUMULATION`** |
| `12h` | -58,000,000.00 USD | -616,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -143,360,000.00 USD | -1,870,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -219,440,000.00 USD | -3,020,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,180,000,000.00 USD | -9,720,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+112.35K` | 15m=`-2.22M` | 1h=`+15.49M` | 24h=`-143.36M`
* Futures Capital Netflows: 5m=`-17.89M` | 15m=`-36.64M` | 1h=`+63.24M` | 24h=`-1.87B`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2196.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2178.50` (Risk Distance: `17.93` pts)
  * +2.5R Take Profit: `2241.27`
  * Mathematical Lot Sizing: **`0.55 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2250.66` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2268.59` (Risk Distance: `17.93` pts)
  * +2.5R Take Profit: `2205.82`
  * Mathematical Lot Sizing: **`0.55 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2260.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
