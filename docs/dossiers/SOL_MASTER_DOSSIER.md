# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:17:48 IST` (`2026-10-29 19:47:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `99.85` | **Live Ask Quote**: `100.09` | **Mid Price**: `99.97`
- **Spread Points**: `24.00` | **Spread BPS**: `24.01 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `100.42` | VWAP Z-Score: `-0.54` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4813` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.10` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `102.98` | Lower -3.00σ Band: `97.86`
  * Upper +2.51σ Band: `102.56` | Lower -2.51σ Band: `98.28`
  * Upper +2.01σ Band: `102.14` | Lower -2.01σ Band: `98.71`
  * Upper +2.00σ Band: `102.13` | Lower -2.00σ Band: `98.72`
  * Upper +1.28σ Band: `101.51` | Lower -1.28σ Band: `99.33`
  * Upper +1.00σ Band: `101.28` | Lower -1.00σ Band: `99.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`100.51` | EMA-20=`100.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.75` (Slope: `+0.0000`) | EMA-100=`100.78`
  * Institutional Anchors: EMA-144=`100.80` | EMA-200=`100.75` (Slope: `+0.0041`) | EMA-233=`100.71`
- **Range Boundaries**: 24H High=`103.63` | 24H Low=`98.95` | Weekly High=`103.63` | Weekly Low=`98.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.25` (Distance: `-1.23%`)
  * Point of Control (POC) = `99.92` (Distance: `+0.08%`)
  * Value Area Low (VAL) = `99.18` (Distance: `+0.83%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.11` | POC=`100.90` | VAL=`100.63`
  * Prior Day Extremes: PDH=`103.63` | PDL=`100.15` | PDC=`102.27`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.48` | Weekly POC=`100.91` | Weekly VAL=`99.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.77` | Low=`98.95`
  * London Session (08:00-16:00 UTC): High=`100.61` | Low=`99.44`
  * New York Session (13:00-21:00 UTC): High=`102.93` | Low=`99.78`
  * Initial Balance (First Hour): IB High=`100.61` | IB Low=`99.91`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `99.57` - `100.37`
  * Optimal Trade Entry (OTE 0.705): `100.17`
  * Structural Invalidation Anchor (0.786): `100.77`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.18` | `100.37` | `100.18` | `100.24` | `42,426` | 4,254,239.57 USD | 615,741.61 USD | `+14.47%` | -71,289,687.20 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `100.24` | `100.24` | `100.10` | `100.11` | `52,275` | 5,235,928.43 USD | 2,039,225.45 USD | `+38.95%` | -69,250,461.75 USD | `+1.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `100.11` | `100.20` | `100.08` | `100.10` | `47,169` | 4,723,411.86 USD | 323,406.75 USD | `+6.85%` | -68,927,055.00 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `100.57` | `100.61` | `100.24` | `100.27` | `94,842` | 9,521,682.83 USD | -44,411.28 USD | `-0.47%` | -70,635,604.28 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `100.27` | `100.42` | `100.15` | `100.19` | `109,464` | 10,974,925.19 USD | -1,269,824.53 USD | `-11.57%` | -71,905,428.81 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `100.18` | `100.37` | `100.08` | `100.10` | `141,870` | 14,213,579.86 USD | 2,978,373.81 USD | `+20.95%` | -68,927,055.00 USD | `+1.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `101.87` | `101.93` | `100.71` | `101.06` | `773,410` | 78,387,335.50 USD | -11,810,112.06 USD | `-15.07%` | -67,707,300.30 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.06` | `101.18` | `100.29` | `100.57` | `555,290` | 55,901,104.31 USD | -7,049,401.02 USD | `-12.61%` | -74,756,701.33 USD | `-0.46` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `100.57` | `100.61` | `100.08` | `100.12` | `346,886` | 34,781,171.81 USD | 1,726,586.65 USD | `+4.96%` | -73,030,114.68 USD | `+0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.08` | `100.12` | `2,775,561` | 281,657,684.29 USD | -29,157,752.38 USD | `-10.35%` | -73,026,395.60 USD | `-1.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.37` | `102.50` | `99.16` | `99.64` | `3,450,297` | 345,810,531.49 USD | -35,022,306.76 USD | `-10.13%` | -43,673,756.58 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -38,017,362.01 USD | `+1.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.08` | `100.12` | `2,775,561` | 281,657,684.29 USD | -29,157,752.38 USD | `-10.35%` | -73,026,395.60 USD | `-1.15` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`99.97`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `99.99` | `1562.9500` | 156,285.62 USD | 4,301,913.22 USD | `1 orders` | `-0.14%` | `-` |
| `BID` | `99.99` | `1501.8500` | 150,174.49 USD | 4,452,087.71 USD | `1 orders` | `-0.14%` | `-` |
| `BID` | `99.99` | `1807.1900` | 180,704.54 USD | 4,632,792.25 USD | `5 orders` | `-0.14%` | `-` |
| `BID` | `99.99` | `0.1100` | 11.00 USD | 4,632,803.25 USD | `1 orders` | `-0.14%` | `-` |
| `BID` | `100.00` | `1766.1600` | 176,616.00 USD | 4,084,729.95 USD | `41 orders` | `-0.13%` | `-` |
| `BID` | `100.00` | `231.2100` | 23,120.54 USD | 4,107,850.49 USD | `3 orders` | `-0.14%` | `-` |
| `BID` | `100.00` | `377.7900` | 37,777.11 USD | 4,145,627.60 USD | `1 orders` | `-0.14%` | `-` |
| `BID` | `100.01` | `2677.0300` | 267,729.77 USD | 3,908,113.95 USD | `12 orders` | `-0.12%` | `-` |
| `BID` | `100.02` | `5303.5300` | 530,459.07 USD | 3,640,384.18 USD | `21 orders` | `-0.11%` | `-` |
| `BID` | `100.03` | `2628.9500` | 262,973.87 USD | 3,109,925.11 USD | `12 orders` | `-0.10%` | `-` |
| `BID` | `100.04` | `1553.3100` | 155,393.13 USD | 2,846,951.24 USD | `16 orders` | `-0.09%` | `-` |
| `BID` | `100.05` | `4023.5900` | 402,560.18 USD | 2,691,558.11 USD | `21 orders` | `-0.08%` | `-` |
| `BID` | `100.06` | `4809.7300` | 481,261.58 USD | 2,288,997.93 USD | `32 orders` | `-0.07%` | `-` |
| `BID` | `100.07` | `5023.6400` | 502,715.65 USD | 1,807,736.34 USD | `27 orders` | `-0.06%` | `-` |
| `BID` | `100.08` | `2647.4500` | 264,956.80 USD | 1,305,020.69 USD | `24 orders` | `-0.05%` | `-` |
| `BID` | `100.09` | `3567.9200` | 357,113.11 USD | 1,040,063.89 USD | `26 orders` | `-0.04%` | `-` |
| `BID` | `100.10` | `1699.7400` | 170,143.97 USD | 682,950.78 USD | `31 orders` | `-0.03%` | `-` |
| `BID` | `100.11` | `3632.8100` | 363,680.61 USD | 512,806.81 USD | `26 orders` | `-0.02%` | `-` |
| `BID` | `100.12` | `1143.0900` | 114,446.17 USD | 149,126.20 USD | `18 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `100.13` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 100.13` | `0.00%` | `-` |
| `BID` | `100.13` | `346.3500` | 34,680.03 USD | 34,680.03 USD | `11 orders` | `-0.00%` | `-` |
| `ASK` | `100.14` | `1071.6600` | 107,316.03 USD | 107,316.03 USD | `16 orders` | `+0.00%` | `-` |
| `ASK` | `100.15` | `1463.2300` | 146,542.48 USD | 253,858.52 USD | `29 orders` | `+0.01%` | `-` |
| `ASK` | `100.16` | `1305.3200` | 130,740.85 USD | 384,599.37 USD | `22 orders` | `+0.02%` | `-` |
| `ASK` | `100.17` | `1942.3500` | 194,565.20 USD | 579,164.57 USD | `35 orders` | `+0.03%` | `-` |
| `ASK` | `100.18` | `2710.7500` | 271,562.93 USD | 850,727.50 USD | `19 orders` | `+0.04%` | `-` |
| `ASK` | `100.19` | `1735.5200` | 173,881.75 USD | 1,024,609.25 USD | `22 orders` | `+0.05%` | `-` |
| `ASK` | `100.20` | `3617.8500` | 362,508.57 USD | 1,387,117.82 USD | `23 orders` | `+0.06%` | `-` |
| `ASK` | `100.21` | `2318.0500` | 232,291.79 USD | 1,619,409.61 USD | `16 orders` | `+0.07%` | `-` |
| `ASK` | `100.22` | `5092.8400` | 510,404.42 USD | 2,129,814.04 USD | `18 orders` | `+0.08%` | `-` |
| `ASK` | `100.23` | `2793.2600` | 279,968.45 USD | 2,409,782.49 USD | `20 orders` | `+0.09%` | `-` |
| `ASK` | `100.24` | `2401.2000` | 240,696.29 USD | 2,650,478.77 USD | `14 orders` | `+0.10%` | `-` |
| `ASK` | `100.25` | `5977.7100` | 599,265.43 USD | 3,249,744.20 USD | `15 orders` | `+0.11%` | `-` |
| `ASK` | `100.26` | `1647.3400` | 165,162.31 USD | 3,414,906.51 USD | `11 orders` | `+0.12%` | `-` |
| `ASK` | `100.27` | `4218.3200` | 422,970.95 USD | 3,837,877.46 USD | `13 orders` | `+0.13%` | `-` |
| `ASK` | `100.28` | `845.4800` | 84,784.73 USD | 3,922,662.19 USD | `11 orders` | `+0.14%` | `-` |
| `ASK` | `100.29` | `3345.2500` | 335,495.12 USD | 4,258,157.31 USD | `11 orders` | `+0.15%` | `-` |
| `ASK` | `100.30` | `2321.0600` | 232,802.32 USD | 4,490,959.63 USD | `9 orders` | `+0.16%` | `-` |
| `ASK` | `100.31` | `3111.9800` | 312,162.71 USD | 4,803,122.35 USD | `6 orders` | `+0.17%` | `-` |
| `ASK` | `100.32` | `3996.9800` | 400,977.03 USD | 5,204,099.38 USD | `11 orders` | `+0.18%` | `-` |
| `ASK` | `100.33` | `2039.1200` | 204,584.91 USD | 5,408,684.29 USD | `7 orders` | `+0.19%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 72,178,618.33 USD | `721,165.26` | `94.33` | `100.11` | `317.65` | -4,147,727.91 USD | `-5.75%` | `7X Cross` |
| `21` | `0x9c6a...a4ed` | `LONG` | 55,074,779.52 USD | `550,087.69` | `80.86` | `100.11` | `68.18` | 10,595,793.13 USD | `+19.24%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 25,967,885.73 USD | `259,300.02` | `91.42` | `100.11` | `609.93` | -2,262,752.71 USD | `-8.71%` | `5X Cross` |
| `78` | `0x3dc9...54b0` | `SHORT` | 22,032,161.03 USD | `220,000.19` | `105.90` | `100.11` | `165.81` | 1,266,946.25 USD | `+5.75%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 18,966,197.25 USD | `189,472.50` | `115.21` | `100.11` | `34.72` | -2,862,818.01 USD | `-15.09%` | `20X Cross` |
| `113` | `0x4a20...3c26` | `LONG` | 18,027,000.00 USD | `180,000.00` | `106.43` | `100.11` | `65.50` | -1,131,278.71 USD | `-6.28%` | `20X Cross` |
| `137` | `0xecb6...2b00` | `SHORT` | 15,023,433.05 USD | `150,104.94` | `102.72` | `100.11` | `282.72` | 395,182.48 USD | `+2.63%` | `20X Cross` |
| `220` | `0x7a5a...0394` | `SHORT` | 10,227,394.11 USD | `102,120.76` | `100.91` | `100.11` | `126.24` | 77,208.49 USD | `+0.75%` | `10X Cross` |
| `230` | `0xc63a...a3cd` | `LONG` | 10,015,000.00 USD | `100,000.00` | `112.22` | `100.11` | `0.000000` | -1,207,108.97 USD | `-12.05%` | `20X Cross` |
| `245` | `0x13da...08be` | `LONG` | 9,585,485.69 USD | `95,711.29` | `100.55` | `100.11` | `98.09` | -38,254.98 USD | `-0.40%` | `20X Isolated` |
| `268` | `0xb581...6f4f` | `LONG` | 9,009,900.00 USD | `90,000.00` | `114.59` | `100.11` | `0.000000` | -1,303,392.29 USD | `-14.47%` | `3X Cross` |
| `290` | `0x645b...87b8` | `SHORT` | 8,367,727.42 USD | `83,605.29` | `103.91` | `100.11` | `334.81` | 319,401.75 USD | `+3.82%` | `20X Cross` |
| `298` | `0xdb3a...cf3b` | `LONG` | 8,197,136.55 USD | `81,851.78` | `106.04` | `100.11` | `46.85` | -482,610.31 USD | `-5.89%` | `4X Cross` |
| `317` | `0xe927...98ef` | `LONG` | 7,811,395.80 USD | `78,000.00` | `96.34` | `100.11` | `38.44` | 297,254.32 USD | `+3.81%` | `3X Cross` |
| `325` | `0xca49...53c8` | `SHORT` | 7,405,436.52 USD | `73,943.45` | `110.70` | `100.11` | `274.00` | 780,185.74 USD | `+10.54%` | `20X Cross` |
| `329` | `0x8ae4...3d60` | `LONG` | 7,224,573.38 USD | `72,180.05` | `111.72` | `100.11` | `2.16` | -839,586.85 USD | `-11.62%` | `10X Cross` |
| `336` | `0xa0b7...6165` | `SHORT` | 7,112,967.33 USD | `71,044.42` | `107.87` | `100.11` | `190.90` | 550,499.87 USD | `+7.74%` | `2X Cross` |
| `350` | `0xf517...c032` | `SHORT` | 6,786,664.21 USD | `67,778.53` | `84.64` | `100.11` | `229.64` | -1,049,633.04 USD | `-15.47%` | `20X Cross` |
| `480` | `0x7e23...5a5a` | `LONG` | 4,860,637.41 USD | `48,564.56` | `105.17` | `100.11` | `78.11` | -246,931.75 USD | `-5.08%` | `5X Isolated` |
| `580` | `0x2e2b...2fab` | `LONG` | 4,005,844.00 USD | `40,000.00` | `119.55` | `100.11` | `53.88` | -776,191.64 USD | `-19.38%` | `10X Cross` |
| `582` | `0x7fda...17d1` | `SHORT` | 3,980,793.49 USD | `39,773.65` | `103.76` | `100.11` | `1004.46` | 146,072.12 USD | `+3.67%` | `20X Cross` |
| `602` | `0xf899...88db` | `SHORT` | 3,862,871.49 USD | `38,586.27` | `87.86` | `100.11` | `117.06` | -472,496.30 USD | `-12.23%` | `20X Cross` |
| `618` | `0x9946...0852` | `SHORT` | 3,784,147.72 USD | `37,784.80` | `112.11` | `100.11` | `129.49` | 452,079.60 USD | `+11.95%` | `20X Cross` |
| `641` | `0x27b8...12fc` | `LONG` | 3,612,040.84 USD | `36,085.73` | `110.86` | `100.11` | `14.34` | -388,304.41 USD | `-10.75%` | `10X Cross` |
| `646` | `0x9c16...4a6f` | `SHORT` | 3,583,281.87 USD | `35,779.15` | `90.45` | `100.11` | `128.60` | -347,176.84 USD | `-9.69%` | `20X Cross` |
| `651` | `0x3440...32c5` | `SHORT` | 3,558,241.37 USD | `35,529.12` | `95.02` | `100.11` | `167.53` | -182,219.94 USD | `-5.12%` | `20X Cross` |
| `731` | `0x96a7...79df` | `LONG` | 3,204,675.20 USD | `32,000.00` | `74.39` | `100.11` | `0.000000` | 824,269.35 USD | `+25.72%` | `20X Cross` |
| `733` | `0x023a...2355` | `SHORT` | 3,199,863.91 USD | `31,971.08` | `101.46` | `100.11` | `360.10` | 43,817.86 USD | `+1.37%` | `20X Cross` |
| `776` | `0xbe19...8bd1` | `SHORT` | 3,049,736.75 USD | `30,451.69` | `97.62` | `100.11` | `739.99` | -77,190.12 USD | `-2.53%` | `3X Cross` |
| `780` | `0x482b...cae4` | `SHORT` | 3,035,595.57 USD | `30,310.49` | `88.03` | `100.11` | `155.13` | -367,347.29 USD | `-12.10%` | `20X Cross` |
| `788` | `0x610b...b613` | `LONG` | 2,967,743.55 USD | `29,634.14` | `101.23` | `100.11` | `70.39` | -32,255.80 USD | `-1.09%` | `3X Isolated` |
| `792` | `0xfc66...ca06` | `SHORT` | 2,958,474.01 USD | `29,559.26` | `102.17` | `100.11` | `1289.89` | 61,512.29 USD | `+2.08%` | `20X Cross` |
| `803` | `0x45d2...4029` | `SHORT` | 2,926,383.00 USD | `29,220.00` | `93.28` | `100.11` | `1363.67` | -200,607.02 USD | `-6.86%` | `20X Cross` |
| `811` | `0xa61c...66b9` | `LONG` | 2,893,020.54 USD | `28,888.00` | `104.39` | `100.11` | `0.000000` | -122,543.58 USD | `-4.24%` | `5X Cross` |
| `846` | `0x458d...ab3b` | `LONG` | 2,742,503.95 USD | `27,385.03` | `117.17` | `100.11` | `81.07` | -466,158.56 USD | `-17.00%` | `3X Isolated` |
| `885` | `0xfc27...9d9d` | `SHORT` | 2,581,579.40 USD | `25,793.56` | `102.76` | `100.11` | `657.96` | 68,908.39 USD | `+2.67%` | `20X Cross` |
| `911` | `0x051c...693c` | `LONG` | 2,517,642.91 USD | `25,139.70` | `89.76` | `100.11` | `22.83` | 261,081.58 USD | `+10.37%` | `20X Cross` |
| `948` | `0x638f...f5f0` | `LONG` | 2,403,600.00 USD | `24,000.00` | `136.71` | `100.11` | `42.27` | -877,368.54 USD | `-36.50%` | `20X Cross` |
| `1004` | `0x7178...0854` | `LONG` | 2,257,003.98 USD | `22,545.24` | `110.94` | `100.11` | `30.89` | -244,140.50 USD | `-10.82%` | `10X Cross` |
| `1028` | `0x739c...cfb2` | `LONG` | 2,203,214.20 USD | `22,000.00` | `91.95` | `100.11` | `72.58` | 180,306.89 USD | `+8.18%` | `20X Cross` |
| `1038` | `0x69cc...14fd` | `SHORT` | 2,173,412.24 USD | `21,701.57` | `99.01` | `100.11` | `459.32` | -24,759.49 USD | `-1.14%` | `20X Cross` |
| `1064` | `0xb90d...870c` | `SHORT` | 2,115,095.65 USD | `21,120.10` | `102.00` | `100.11` | `111.38` | 39,229.13 USD | `+1.85%` | `20X Cross` |
| `1101` | `0x7737...bf66` | `SHORT` | 2,040,852.09 USD | `20,384.06` | `102.94` | `100.11` | `973.60` | 57,489.80 USD | `+2.82%` | `10X Cross` |
| `1128` | `0xea00...a918` | `LONG` | 2,005,194.31 USD | `20,022.69` | `66.09` | `100.11` | `0.000000` | 681,885.72 USD | `+34.01%` | `20X Cross` |
| `1130` | `0x251f...6e5d` | `LONG` | 2,003,000.00 USD | `20,000.00` | `101.15` | `100.11` | `46.58` | -20,097.77 USD | `-1.00%` | `20X Cross` |
| `1131` | `0x3fc5...c0c1` | `SHORT` | 2,002,600.00 USD | `20,000.00` | `98.28` | `100.11` | `203.84` | -37,040.16 USD | `-1.85%` | `20X Cross` |
| `1132` | `0xdf60...d3c7` | `LONG` | 2,002,600.00 USD | `20,000.00` | `120.12` | `100.11` | `94.00` | -399,808.53 USD | `-19.96%` | `7X Isolated` |
| `1133` | `0xbfc7...80b4` | `SHORT` | 2,002,200.00 USD | `20,000.00` | `85.98` | `100.11` | `327.26` | -282,665.50 USD | `-14.12%` | `20X Cross` |
| `1134` | `0x5986...89d9` | `LONG` | 2,001,922.00 USD | `20,000.00` | `101.84` | `100.11` | `46.42` | -34,875.53 USD | `-1.74%` | `20X Cross` |
| `1154` | `0xb322...d51f` | `LONG` | 1,980,052.73 USD | `19,774.82` | `102.98` | `100.11` | `55.87` | -56,418.67 USD | `-2.85%` | `20X Cross` |
| `1162` | `0x34e6...8d74` | `LONG` | 1,971,760.21 USD | `19,688.07` | `101.19` | `100.11` | `53.20` | -20,403.59 USD | `-1.03%` | `20X Cross` |
| `1178` | `0x7160...d47c` | `LONG` | 1,946,325.11 USD | `19,434.10` | `105.03` | `100.11` | `80.24` | -94,896.18 USD | `-4.88%` | `20X Cross` |
| `1180` | `0x936c...bb0f` | `SHORT` | 1,945,457.54 USD | `19,437.82` | `105.65` | `100.11` | `636.53` | 108,056.84 USD | `+5.55%` | `20X Cross` |
| `1206` | `0xe097...d0fe` | `LONG` | 1,902,424.36 USD | `18,995.75` | `109.71` | `100.11` | `0.000000` | -181,572.53 USD | `-9.54%` | `20X Cross` |
| `1291` | `0xe98b...8cd5` | `SHORT` | 1,764,403.75 USD | `17,622.89` | `187.95` | `100.11` | `260.46` | 1,547,816.98 USD | `+87.72%` | `20X Cross` |
| `1310` | `0xdf95...7d72` | `SHORT` | 1,745,840.13 USD | `17,443.40` | `104.70` | `100.11` | `2218.52` | 80,423.53 USD | `+4.61%` | `20X Cross` |
| `1334` | `0xee2b...d67e` | `LONG` | 1,698,797.32 USD | `16,963.19` | `119.86` | `100.11` | `20.52` | -334,474.32 USD | `-19.69%` | `4X Cross` |
| `1338` | `0x123d...3bff` | `LONG` | 1,694,314.78 USD | `16,918.43` | `89.53` | `100.11` | `0.000000` | 179,528.30 USD | `+10.60%` | `10X Cross` |
| `1372` | `0x7277...0b98` | `SHORT` | 1,662,801.47 USD | `16,603.11` | `101.18` | `100.11` | `179.12` | 17,126.74 USD | `+1.03%` | `20X Cross` |
| `1450` | `0x73d7...8be1` | `LONG` | 1,569,245.34 USD | `15,668.95` | `106.60` | `100.11` | `70.58` | -101,095.62 USD | `-6.44%` | `20X Cross` |
| `1459` | `0xc74a...ab93` | `LONG` | 1,555,391.05 USD | `15,536.82` | `64.06` | `100.11` | `54.88` | 560,162.22 USD | `+36.01%` | `5X Isolated` |
| `1505` | `0xc7d1...51af` | `SHORT` | 1,502,191.50 USD | `15,000.00` | `105.79` | `100.11` | `138.76` | 84,683.50 USD | `+5.64%` | `20X Cross` |
| `1541` | `0xffb2...5ed6` | `LONG` | 1,451,855.41 USD | `14,504.05` | `117.89` | `100.11` | `89.48` | -258,049.31 USD | `-17.77%` | `20X Cross` |
| `1567` | `0x0d6a...ca57` | `LONG` | 1,422,511.86 USD | `14,206.65` | `110.41` | `100.11` | `91.59` | -146,078.49 USD | `-10.27%` | `5X Isolated` |
| `1849` | `0x2482...0e55` | `LONG` | 1,138,058.28 USD | `11,363.98` | `122.03` | `100.11` | `94.24` | -248,643.65 USD | `-21.85%` | `20X Isolated` |
| `1866` | `0xe105...6a47` | `LONG` | 1,122,185.76 USD | `11,205.05` | `107.11` | `100.11` | `92.14` | -77,971.30 USD | `-6.95%` | `20X Cross` |
| `1877` | `0x45db...86eb` | `LONG` | 1,111,665.00 USD | `11,100.00` | `110.69` | `100.11` | `67.97` | -117,016.90 USD | `-10.53%` | `5X Cross` |
| `1908` | `0x1d04...7c43` | `LONG` | 1,082,473.41 USD | `10,811.76` | `111.55` | `100.11` | `19.45` | -123,588.08 USD | `-11.42%` | `6X Cross` |
| `1967` | `0xa6a1...29eb` | `LONG` | 1,036,120.85 USD | `10,348.79` | `100.79` | `100.11` | `0.000000` | -6,909.99 USD | `-0.67%` | `20X Cross` |
| `2035` | `0x0daf...47e0` | `SHORT` | 1,001,464.00 USD | `10,000.00` | `99.07` | `100.11` | `250.80` | -10,751.78 USD | `-1.07%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `130.74` | 1,361.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.36K USD at 130.7400 USD [API] | `2026-01-21 15:16:43` |
| `ANNOUNCEMENT` | `INFO` | `122.75` | 4,485.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.49K USD at 122.7500 USD [API] | `2025-12-23 13:36:37` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 3,751.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.75K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 820.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.82K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `126.81` | 3,182.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.18K USD at 126.8100 USD [API] | `2025-12-17 15:52:14` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,808.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.81K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,998.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,510.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.51K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `129.25` | 4,809.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.81K USD at 129.2500 USD [API] | `2025-12-14 23:27:00` |
| `ANNOUNCEMENT` | `INFO` | `134.26` | 5,544.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.54K USD at 134.2600 USD [API] | `2025-12-11 18:35:47` |
| `ANNOUNCEMENT` | `INFO` | `128.92` | 6,032.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.03K USD at 128.9200 USD [API] | `2025-12-07 14:24:53` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 6,367.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.37K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 19.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 12.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 202.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 1,588.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.59K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,040.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.04K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,710.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.71K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 1,543.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.54K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 2,490.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.49K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `101.15` | 86,233.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 86.23K USD at 101.1500 USD [API] | `2026-10-27 23:35:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.65` (Vol: 2,900,000.00 USD, Dist: `+3.51%`) | Long MP=`98.78` (Vol: 4,200,000.00 USD, Dist: `--1.35%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+3.95%`) | Long MP=`99.30` (Vol: 5,000,000.00 USD, Dist: `--0.83%`)
  * 3D Horizon: Short MP=`104.03` (Vol: 4,200,000.00 USD, Dist: `+3.90%`) | Long MP=`99.07` (Vol: 5,800,000.00 USD, Dist: `--1.06%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+3.91%`) | Long MP=`98.63` (Vol: 8,800,000.00 USD, Dist: `--1.50%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `20.50` | 23,250.00 USD | 141,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.50` | 544,040.00 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.50` | 62,010.00 USD | 140,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.50` | 62,020.00 USD | 140,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.50` | 645,300.00 USD | 140,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 58,760.00 USD | 140,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 18,480.00 USD | 140,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 17,520.00 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 190,510.00 USD | 140,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 45,390.00 USD | 139,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 308,240.00 USD | 139,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 876,640.00 USD | 139,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 18,410.00 USD | 138,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 7,870.00 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 6,590,000.00 USD | 138,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 175,700.00 USD | 131,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 66,810.00 USD | 131,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 234,310.00 USD | 131,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,020,000.00 USD | 131,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 57,940.00 USD | 128,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 76,680.00 USD | 128,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 29,060.00 USD | 128,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 1,040,000.00 USD | 128,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 155,310.00 USD | 127,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 216,380.00 USD | 127,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 60,640.00 USD | 126,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 4,760,000.00 USD | 126,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 144,140.00 USD | 122,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 1,040,000.00 USD | 121,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 76,710.00 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 95,290.00 USD | 120,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 745,920.00 USD | 120,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 191,460.00 USD | 119,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 3,380,000.00 USD | 119,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 1,160,000.00 USD | 116,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 190,340.00 USD | 115,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,260,000.00 USD | 115,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 453,280.00 USD | 113,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 238,880.00 USD | 113,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 140,510.00 USD | 113,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 188,530.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 215,540.00 USD | 112,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 209,880.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 277,870.00 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 144,330.00 USD | 112,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 11,970,000.00 USD | 111,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 93,730.00 USD | 99,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 1,050,000.00 USD | 99,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 37,980,000.00 USD | 98,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 166,780.00 USD | 60,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 2,440,000.00 USD | 60,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,410,000.00 USD | 58,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 2,200,000.00 USD | 56,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 593,320.00 USD | 54,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 614,790.00 USD | 54,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 754,900.00 USD | 53,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 203,660.00 USD | 52,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 1,430,000.00 USD | 52,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,940,000.00 USD | 51,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 333,690.00 USD | 46,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 2,060,000.00 USD | 45,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 2,610,000.00 USD | 43,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,470,000.00 USD | 41,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 739,670.00 USD | 39,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 710,900.00 USD | 38,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 879,320.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 839,590.00 USD | 37,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,450,000.00 USD | 36,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 3,950,000.00 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,940,000.00 USD | 31,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.90` | 374,300,000.00 USD | 374,300,000.00 USD | 525,310.00 USD | 459,170.00 USD | 925,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.10` | 372,390,000.00 USD | 372,390,000.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.20` | 182,550,000.00 USD | 182,550,000.00 USD | 445,880.00 USD | 674,190.00 USD | 467,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.30` | 370,320,000.00 USD | 370,320,000.00 USD | 826,230.00 USD | 342,020.00 USD | 654,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.40` | 180,960,000.00 USD | 180,960,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.50` | 368,490,000.00 USD | 368,490,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.50` | 374,770.00 USD | 29,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 179,610,000.00 USD | 179,610,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.70` | 365,810,000.00 USD | 365,810,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.80` | 178,470,000.00 USD | 178,470,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.90` | 363,370,000.00 USD | 363,370,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.00` | 178,260,000.00 USD | 178,260,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.10` | 360,980,000.00 USD | 360,980,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.20` | 178,070,000.00 USD | 178,070,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.30` | 359,080,000.00 USD | 359,080,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.40` | 178,040,000.00 USD | 178,040,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.50` | 356,570,000.00 USD | 356,570,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.50` | 3,160,000.00 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 177,870,000.00 USD | 177,870,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.70` | 353,660,000.00 USD | 353,660,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.80` | 177,750,000.00 USD | 177,750,000.00 USD | 229,430.00 USD | 103,030.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.90` | 352,030,000.00 USD | 352,030,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.00` | 177,400,000.00 USD | 177,400,000.00 USD | 137,240.00 USD | 74,290.00 USD | 90,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.10` | 349,610,000.00 USD | 349,610,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.20` | 177,100,000.00 USD | 177,100,000.00 USD | 157,710.00 USD | 41,040.00 USD | 107,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.30` | 348,300,000.00 USD | 348,300,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.40` | 176,790,000.00 USD | 176,790,000.00 USD | 151,210.00 USD | 110,310.00 USD | 782,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.50` | 346,290,000.00 USD | 346,290,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.50` | 2,250,000.00 USD | 25,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 175,750,000.00 USD | 175,750,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.70` | 344,890,000.00 USD | 344,890,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.80` | 175,500,000.00 USD | 175,500,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.90` | 344,620,000.00 USD | 344,620,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.00` | 175,340,000.00 USD | 175,340,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.10` | 344,560,000.00 USD | 344,560,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.20` | 175,180,000.00 USD | 175,180,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.30` | 344,170,000.00 USD | 344,170,000.00 USD | 55,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.40` | 174,970,000.00 USD | 174,970,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.50` | 344,060,000.00 USD | 344,060,000.00 USD | 101,820.00 USD | 260,630.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.50` | 3,120,000.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.70` | 343,700,000.00 USD | 343,700,000.00 USD | 270,240.00 USD | 262,300.00 USD | 115,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.90` | 343,050,000.00 USD | 343,050,000.00 USD | 236,340.00 USD | 90,940.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.10` | 342,570,000.00 USD | 342,570,000.00 USD | 233,120.00 USD | 296,810.00 USD | 321,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.30` | 341,720,000.00 USD | 341,720,000.00 USD | 10,610.00 USD | 0.00 USD | 44,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.50` | 341,670,000.00 USD | 341,670,000.00 USD | 183,750.00 USD | 0.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,970,000.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.90` | 341,340,000.00 USD | 341,340,000.00 USD | 297,690.00 USD | 444,840.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.10` | 340,580,000.00 USD | 340,580,000.00 USD | 141,070.00 USD | 115,890.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.20` | 174,910,000.00 USD | 174,910,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.30` | 340,320,000.00 USD | 340,320,000.00 USD | 251,720.00 USD | 196,820.00 USD | 474,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.40` | 174,900,000.00 USD | 174,900,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.50` | 339,390,000.00 USD | 339,390,000.00 USD | 1,000,000.00 USD | 732,540.00 USD | 341,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.50` | 1,810,000.00 USD | 17,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 174,380,000.00 USD | 174,380,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 337,320,000.00 USD | 337,320,000.00 USD | 1,980,000.00 USD | 1,130,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.80` | 171,810,000.00 USD | 171,810,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.90` | 332,760,000.00 USD | 332,760,000.00 USD | 1,610,000.00 USD | 1,260,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.00` | 167,990,000.00 USD | 167,990,000.00 USD | 1,200,000.00 USD | 1,170,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 327,220,000.00 USD | 327,220,000.00 USD | 2,910,000.00 USD | 2,330,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.20` | 164,400,000.00 USD | 164,400,000.00 USD | 1,230,000.00 USD | 1,230,000.00 USD | 747,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 319,340,000.00 USD | 319,340,000.00 USD | 3,210,000.00 USD | 1,280,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.40` | 161,190,000.00 USD | 161,190,000.00 USD | 1,540,000.00 USD | 1,270,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 312,460,000.00 USD | 312,460,000.00 USD | 2,870,000.00 USD | 1,580,000.00 USD | 2,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.50` | 1,350,000.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.60` | 156,800,000.00 USD | 156,800,000.00 USD | 1,040,000.00 USD | 839,050.00 USD | 934,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.70` | 305,150,000.00 USD | 305,150,000.00 USD | 2,220,000.00 USD | 2,450,000.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.80` | 153,980,000.00 USD | 153,980,000.00 USD | 327,640.00 USD | 738,000.00 USD | 729,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.90` | 298,110,000.00 USD | 298,110,000.00 USD | 5,140,000.00 USD | 3,170,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.00` | 152,190,000.00 USD | 152,190,000.00 USD | 310,450.00 USD | 114,330.00 USD | 170,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.10` | 286,450,000.00 USD | 286,450,000.00 USD | 4,430,000.00 USD | 2,080,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.20` | 151,590,000.00 USD | 151,590,000.00 USD | 336,680.00 USD | 6,890.00 USD | 336,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.30` | 278,290,000.00 USD | 278,290,000.00 USD | 5,780,000.00 USD | 4,270,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.40` | 150,910,000.00 USD | 150,910,000.00 USD | 821,270.00 USD | 642,050.00 USD | 150,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.50` | 264,490,000.00 USD | 264,490,000.00 USD | 4,390,000.00 USD | 4,370,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.50` | 2,510,000.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.60` | 149,300,000.00 USD | 149,300,000.00 USD | 1,940,000.00 USD | 1,700,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.70` | 251,340,000.00 USD | 251,340,000.00 USD | 5,660,000.00 USD | 3,410,000.00 USD | 5,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.80` | 143,730,000.00 USD | 143,730,000.00 USD | 3,790,000.00 USD | 3,090,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.90` | 236,870,000.00 USD | 236,870,000.00 USD | 8,020,000.00 USD | 6,060,000.00 USD | 7,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.00` | 135,030,000.00 USD | 135,030,000.00 USD | 3,010,000.00 USD | 2,750,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.10` | 215,590,000.00 USD | 215,590,000.00 USD | 8,580,000.00 USD | 7,190,000.00 USD | 7,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.20` | 126,440,000.00 USD | 126,440,000.00 USD | 3,090,000.00 USD | 2,770,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.30` | 192,700,000.00 USD | 192,700,000.00 USD | 8,150,000.00 USD | 4,260,000.00 USD | 7,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.40` | 118,880,000.00 USD | 118,880,000.00 USD | 5,090,000.00 USD | 3,720,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.50` | 172,430,000.00 USD | 172,430,000.00 USD | 10,550,000.00 USD | 7,040,000.00 USD | 9,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.50` | 11,170,000.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.60` | 105,630,000.00 USD | 105,630,000.00 USD | 6,300,000.00 USD | 4,610,000.00 USD | 6,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.70` | 145,230,000.00 USD | 145,230,000.00 USD | 11,830,000.00 USD | 9,800,000.00 USD | 13,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.80` | 87,980,000.00 USD | 87,980,000.00 USD | 7,340,000.00 USD | 6,980,000.00 USD | 5,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.90` | 110,120,000.00 USD | 110,120,000.00 USD | 15,300,000.00 USD | 9,640,000.00 USD | 17,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.00` | 68,610,000.00 USD | 68,610,000.00 USD | 5,060,000.00 USD | 4,770,000.00 USD | 5,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.10` | 67,670,000.00 USD | 67,670,000.00 USD | 18,940,000.00 USD | 12,780,000.00 USD | 10,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.20` | 53,320,000.00 USD | 53,320,000.00 USD | 5,170,000.00 USD | 4,750,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.30` | 25,570,000.00 USD | 25,570,000.00 USD | 4,260,000.00 USD | 1,630,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.40` | 39,430,000.00 USD | 39,430,000.00 USD | 6,080,000.00 USD | 5,170,000.00 USD | 6,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.50` | 12,730,000.00 USD | 12,730,000.00 USD | 1,370,000.00 USD | 1,380,000.00 USD | 4,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.50` | 260,560.00 USD | 366,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `99.60` | 21,510,000.00 USD | 21,510,000.00 USD | 3,520,000.00 USD | 3,320,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.70` | 5,920,000.00 USD | 5,920,000.00 USD | 661,070.00 USD | 1,650,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.80` | 11,700,000.00 USD | 11,700,000.00 USD | 1,490,000.00 USD | 2,600,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.90` | 1,380,000.00 USD | 1,380,000.00 USD | 843,730.00 USD | 0.00 USD | 531,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.00` | 4,460,000.00 USD | 4,460,000.00 USD | 2,110,000.00 USD | 1,230,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.10` | 1,610,000.00 USD | 1,610,000.00 USD | 533,430.00 USD | 36,980.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.10` | 3,220,000.00 USD | 3,220,000.00 USD | 533,430.00 USD | 36,980.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.20` | 1,520,000.00 USD | 1,520,000.00 USD | 407,760.00 USD | 147,570.00 USD | 968,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.30` | 3,320,000.00 USD | 3,320,000.00 USD | 39,280.00 USD | 68,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.40` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 4,840,000.00 USD | 4,840,000.00 USD | 39,680.00 USD | 0.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `100.50` | 105,480.00 USD | 105,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 167,670.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 6,110,000.00 USD | 6,110,000.00 USD | 46,010.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.80` | 5,570,000.00 USD | 5,570,000.00 USD | 274,280.00 USD | 802,330.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.90` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 1,610,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.00` | 11,400,000.00 USD | 11,400,000.00 USD | 4,870,000.00 USD | 953,600.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.10` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.20` | 23,090,000.00 USD | 23,090,000.00 USD | 2,930,000.00 USD | 6,400,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.30` | 30,160,000.00 USD | 30,160,000.00 USD | 5,710,000.00 USD | 2,910,000.00 USD | 6,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.40` | 30,130,000.00 USD | 30,130,000.00 USD | 3,360,000.00 USD | 1,720,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.50` | 42,880,000.00 USD | 42,880,000.00 USD | 2,560,000.00 USD | 0.00 USD | 10,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.50` | 2,210.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 50,410,000.00 USD | 50,410,000.00 USD | 4,610,000.00 USD | 2,550,000.00 USD | 13,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.70` | 52,220,000.00 USD | 52,220,000.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.80` | 56,980,000.00 USD | 56,980,000.00 USD | 212,730.00 USD | 142,780.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 58,680,000.00 USD | 58,680,000.00 USD | 2,670,000.00 USD | 0.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 59,550,000.00 USD | 59,550,000.00 USD | 1,110,000.00 USD | 439,590.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.10` | 61,400,000.00 USD | 61,400,000.00 USD | 0.00 USD | 0.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 63,740,000.00 USD | 63,740,000.00 USD | 1,540,000.00 USD | 1,230,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 66,570,000.00 USD | 66,570,000.00 USD | 2,130,000.00 USD | 803,220.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.40` | 68,220,000.00 USD | 68,220,000.00 USD | 1,360,000.00 USD | 569,360.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.50` | 69,670,000.00 USD | 69,670,000.00 USD | 680,620.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.50` | 39,060.00 USD | 41,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 68,710,000.00 USD | 68,710,000.00 USD | 289,550.00 USD | 190,630.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.70` | 70,400,000.00 USD | 70,400,000.00 USD | 722,800.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.80` | 72,560,000.00 USD | 72,560,000.00 USD | 1,410,000.00 USD | 1,870,000.00 USD | 563,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 89,910,000.00 USD | 89,910,000.00 USD | 16,450,000.00 USD | 0.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.00` | 76,930,000.00 USD | 76,930,000.00 USD | 2,600,000.00 USD | 1,430,000.00 USD | 340,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.10` | 95,280,000.00 USD | 95,280,000.00 USD | 4,750,000.00 USD | 4,380.00 USD | 616,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.20` | 82,260,000.00 USD | 82,260,000.00 USD | 1,840,000.00 USD | 1,670,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.30` | 112,880,000.00 USD | 112,880,000.00 USD | 17,450,000.00 USD | 9,520.00 USD | 140,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.40` | 89,490,000.00 USD | 89,490,000.00 USD | 3,920,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 134,390,000.00 USD | 134,390,000.00 USD | 13,580,000.00 USD | 1,770,000.00 USD | 6,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.50` | 39,100.00 USD | 80,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 103,880,000.00 USD | 103,880,000.00 USD | 4,250,000.00 USD | 2,110,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.70` | 146,610,000.00 USD | 146,610,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.80` | 113,350,000.00 USD | 113,350,000.00 USD | 3,350,000.00 USD | 2,690,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.90` | 163,870,000.00 USD | 163,870,000.00 USD | 8,600,000.00 USD | 2,630,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.00` | 123,260,000.00 USD | 123,260,000.00 USD | 2,990,000.00 USD | 3,120,000.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.10` | 191,630,000.00 USD | 191,630,000.00 USD | 10,840,000.00 USD | 8,150,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.20` | 130,540,000.00 USD | 130,540,000.00 USD | 2,980,000.00 USD | 2,100,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.30` | 212,590,000.00 USD | 212,590,000.00 USD | 7,050,000.00 USD | 6,370,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.40` | 139,320,000.00 USD | 139,320,000.00 USD | 3,430,000.00 USD | 1,940,000.00 USD | 3,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.50` | 224,590,000.00 USD | 224,590,000.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.50` | 756,860.00 USD | 837,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 147,760,000.00 USD | 147,760,000.00 USD | 2,310,000.00 USD | 2,110,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.70` | 244,590,000.00 USD | 244,590,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.80` | 154,070,000.00 USD | 154,070,000.00 USD | 1,630,000.00 USD | 1,620,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 265,200,000.00 USD | 265,200,000.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.00` | 156,630,000.00 USD | 156,630,000.00 USD | 708,730.00 USD | 754,560.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 278,870,000.00 USD | 278,870,000.00 USD | 5,580,000.00 USD | 5,260,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.20` | 157,970,000.00 USD | 157,970,000.00 USD | 514,940.00 USD | 4,110.00 USD | 814,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.30` | 284,580,000.00 USD | 284,580,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | 428,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.40` | 159,000,000.00 USD | 159,000,000.00 USD | 299,190.00 USD | 2,770.00 USD | 727,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.50` | 304,420,000.00 USD | 304,420,000.00 USD | 5,600,000.00 USD | 6,270,000.00 USD | 7,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.50` | 58,280.00 USD | 895,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 160,550,000.00 USD | 160,550,000.00 USD | 273,980.00 USD | 638,670.00 USD | 642,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.70` | 319,270,000.00 USD | 319,270,000.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 161,610,000.00 USD | 161,610,000.00 USD | 225,560.00 USD | 542,960.00 USD | 287,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.90` | 329,240,000.00 USD | 329,240,000.00 USD | 3,740,000.00 USD | 1,890,000.00 USD | 4,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.00` | 162,670,000.00 USD | 162,670,000.00 USD | 377,210.00 USD | 456,530.00 USD | 222,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.10` | 342,500,000.00 USD | 342,500,000.00 USD | 6,610,000.00 USD | 3,690,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.20` | 164,070,000.00 USD | 164,070,000.00 USD | 606,390.00 USD | 420,460.00 USD | 375,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 353,780,000.00 USD | 353,780,000.00 USD | 5,120,000.00 USD | 3,230,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.40` | 165,220,000.00 USD | 165,220,000.00 USD | 632,850.00 USD | 313,010.00 USD | 207,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.50` | 359,410,000.00 USD | 359,410,000.00 USD | 1,730,000.00 USD | 2,010,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.50` | 11,260.00 USD | 906,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 167,980,000.00 USD | 167,980,000.00 USD | 957,870.00 USD | 536,470.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.70` | 369,140,000.00 USD | 369,140,000.00 USD | 2,290,000.00 USD | 3,150,000.00 USD | 4,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 169,970,000.00 USD | 169,970,000.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.90` | 374,920,000.00 USD | 374,920,000.00 USD | 1,190,000.00 USD | 1,120,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.00` | 170,960,000.00 USD | 170,960,000.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.10` | 378,320,000.00 USD | 378,320,000.00 USD | 1,630,000.00 USD | 508,540.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.20` | 171,340,000.00 USD | 171,340,000.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.30` | 378,480,000.00 USD | 378,480,000.00 USD | 0.00 USD | 156,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.40` | 171,820,000.00 USD | 171,820,000.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.50` | 379,460,000.00 USD | 379,460,000.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.50` | 351,530.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 172,310,000.00 USD | 172,310,000.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.70` | 380,430,000.00 USD | 380,430,000.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.80` | 172,620,000.00 USD | 172,620,000.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.90` | 380,600,000.00 USD | 380,600,000.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.10` | 381,850,000.00 USD | 381,850,000.00 USD | 509,480.00 USD | 727,340.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.30` | 384,250,000.00 USD | 384,250,000.00 USD | 1,090,000.00 USD | 697,770.00 USD | 612,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.50` | 385,790,000.00 USD | 385,790,000.00 USD | 835,610.00 USD | 340,050.00 USD | 367,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.50` | 100,500.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 388,160,000.00 USD | 388,160,000.00 USD | 575,510.00 USD | 726,100.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.90` | 389,450,000.00 USD | 389,450,000.00 USD | 414,890.00 USD | 701,350.00 USD | 181,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.00` | 172,620,000.00 USD | 172,620,000.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.10` | 390,540,000.00 USD | 390,540,000.00 USD | 434,330.00 USD | 185,250.00 USD | 461,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.20` | 172,640,000.00 USD | 172,640,000.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.30` | 391,390,000.00 USD | 391,390,000.00 USD | 486,260.00 USD | 85,680.00 USD | 286,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.40` | 172,760,000.00 USD | 172,760,000.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.50` | 391,630,000.00 USD | 391,630,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.50` | 427,240.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.60` | 173,420,000.00 USD | 173,420,000.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.70` | 392,820,000.00 USD | 392,820,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.80` | 174,450,000.00 USD | 174,450,000.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.90` | 394,310,000.00 USD | 394,310,000.00 USD | 238,580.00 USD | 447,100.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.00` | 175,520,000.00 USD | 175,520,000.00 USD | 213,690.00 USD | 401,420.00 USD | 453,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.10` | 396,380,000.00 USD | 396,380,000.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.20` | 176,440,000.00 USD | 176,440,000.00 USD | 275,070.00 USD | 392,200.00 USD | 251,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.30` | 398,200,000.00 USD | 398,200,000.00 USD | 826,230.00 USD | 342,020.00 USD | 654,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.40` | 177,790,000.00 USD | 177,790,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.50` | 398,690,000.00 USD | 398,690,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.50` | 194,170.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.60` | 178,250,000.00 USD | 178,250,000.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.70` | 400,890,000.00 USD | 400,890,000.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.80` | 178,930,000.00 USD | 178,930,000.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.90` | 403,330,000.00 USD | 403,330,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.00` | 179,140,000.00 USD | 179,140,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.10` | 405,720,000.00 USD | 405,720,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.20` | 179,330,000.00 USD | 179,330,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.30` | 407,620,000.00 USD | 407,620,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.40` | 179,360,000.00 USD | 179,360,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.50` | 410,130,000.00 USD | 410,130,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.50` | 88,260.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.60` | 179,480,000.00 USD | 179,480,000.00 USD | 1,690.00 USD | 77,530.00 USD | 42,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.70` | 411,270,000.00 USD | 411,270,000.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.80` | 179,530,000.00 USD | 179,530,000.00 USD | 0.00 USD | 46,120.00 USD | 641.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.90` | 179,540,000.00 USD | 179,540,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.90` | 413,040,000.00 USD | 413,040,000.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.10` | 414,670,000.00 USD | 414,670,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.30` | 417,090,000.00 USD | 417,090,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.50` | 418,400,000.00 USD | 418,400,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.50` | 2,490,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.70` | 418,920,000.00 USD | 418,920,000.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.90` | 420,410,000.00 USD | 420,410,000.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.10` | 421,800,000.00 USD | 421,800,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.30` | 422,080,000.00 USD | 422,080,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.50` | 422,140,000.00 USD | 422,140,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.50` | 155,490.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.70` | 422,530,000.00 USD | 422,530,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.50` | 51,280.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.50` | 2,010,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.50` | 135,940.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.50` | 4,860,000.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 40,610.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.50` | 152,830.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 186,470.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 72,730.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 137,850.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 15,050.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 214,090.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 517,660.00 USD | 13,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 12,720,000.00 USD | 25,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 769,380.00 USD | 26,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 5,640,000.00 USD | 32,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 148,750.00 USD | 32,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 5,500,000.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 14,090.00 USD | 37,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 119,170.00 USD | 38,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 175,260.00 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 30,810.00 USD | 38,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 1,530,000.00 USD | 39,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 51,040.00 USD | 39,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 225,800.00 USD | 40,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,320,000.00 USD | 42,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 67,400.00 USD | 42,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,080,000.00 USD | 43,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 462,490.00 USD | 43,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 96,220.00 USD | 44,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 62,920.00 USD | 44,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 87,980.00 USD | 44,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 1,030,000.00 USD | 45,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 689,270.00 USD | 45,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 12,450.00 USD | 45,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,390,000.00 USD | 48,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 18,880.00 USD | 48,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 38,370.00 USD | 48,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 53,640.00 USD | 48,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 976,210.00 USD | 49,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.50` | 416,970.00 USD | 49,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 8,740.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 129,920.00 USD | 49,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 4,840,000.00 USD | 54,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 1,650,000.00 USD | 56,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 337,110.00 USD | 56,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.50` | 82,340.00 USD | 56,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 2,150,000.00 USD | 59,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 215,730.00 USD | 59,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 145,240.00 USD | 59,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 1,610.00 USD | 59,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 209,200.00 USD | 59,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 36,490,000.00 USD | 96,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 337,280.00 USD | 96,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,000,000.00 USD | 97,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 6,330,000.00 USD | 103,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 138,280.00 USD | 103,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 102,300.00 USD | 104,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 3,430.00 USD | 104,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 108,350.00 USD | 104,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 17,240.00 USD | 104,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 562,640.00 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,370.00 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 27,570.00 USD | 104,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 78,780.00 USD | 104,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 4,180.00 USD | 104,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 5,740.00 USD | 104,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 3,010,000.00 USD | 107,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 289,190.00 USD | 108,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 28,040.00 USD | 108,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 93,060.00 USD | 108,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 533,820.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 9,460.00 USD | 108,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 793,890.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 223,740.00 USD | 109,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 176,580.00 USD | 109,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 568,880.00 USD | 110,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 13,540,000.00 USD | 124,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 123,640.00 USD | 124,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 222,880.00 USD | 124,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 160,020.00 USD | 124,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 20,120.00 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 14,910.00 USD | 124,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 62,700.00 USD | 124,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 533,520.00 USD | 125,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 111,020.00 USD | 125,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 52,390.00 USD | 125,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 5,230.00 USD | 125,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 55,500.00 USD | 125,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `20.50` | 141,440,000.00 USD | 0.00 USD | 23,250.00 USD | `-79.63%` | `1,133.91` |
| `Live` | `Long` | `21.50` | 141,420,000.00 USD | 0.00 USD | 544,040.00 USD | `-78.63%` | `25,304.35` |
| `Live` | `Long` | `22.50` | 140,870,000.00 USD | 0.00 USD | 62,010.00 USD | `-77.64%` | `2,756.07` |
| `Live` | `Long` | `23.50` | 140,810,000.00 USD | 0.00 USD | 62,020.00 USD | `-76.65%` | `2,639.24` |
| `Live` | `Long` | `24.50` | 140,750,000.00 USD | 0.00 USD | 645,300.00 USD | `-75.65%` | `26,338.79` |
| `Live` | `Long` | `25.50` | 140,100,000.00 USD | 0.00 USD | 58,760.00 USD | `-74.66%` | `2,304.13` |
| `Live` | `Long` | `26.50` | 140,040,000.00 USD | 0.00 USD | 18,480.00 USD | `-73.67%` | `697.20` |
| `Live` | `Long` | `27.50` | 140,020,000.00 USD | 0.00 USD | 17,520.00 USD | `-72.67%` | `636.97` |
| `Live` | `Long` | `28.50` | 140,010,000.00 USD | 0.00 USD | 190,510.00 USD | `-71.68%` | `6,684.52` |
| `Live` | `Long` | `29.50` | 139,820,000.00 USD | 0.00 USD | 45,390.00 USD | `-70.68%` | `1,538.48` |
| `Live` | `Long` | `30.50` | 139,770,000.00 USD | 0.00 USD | 308,240.00 USD | `-69.69%` | `10,106.09` |
| `Live` | `Long` | `31.50` | 139,460,000.00 USD | 0.00 USD | 876,640.00 USD | `-68.70%` | `27,829.85` |
| `Live` | `Long` | `32.50` | 138,590,000.00 USD | 0.00 USD | 18,410.00 USD | `-67.70%` | `566.60` |
| `Live` | `Long` | `33.50` | 138,570,000.00 USD | 0.00 USD | 7,870.00 USD | `-66.71%` | `235.05` |
| `Live` | `Long` | `34.50` | 138,560,000.00 USD | 0.00 USD | 6,590,000.00 USD | `-65.72%` | `190,908.48` |
| `Live` | `Long` | `35.50` | 131,970,000.00 USD | 0.00 USD | 175,700.00 USD | `-64.72%` | `4,949.32` |
| `Live` | `Long` | `36.50` | 131,800,000.00 USD | 0.00 USD | 66,810.00 USD | `-63.73%` | `1,830.53` |
| `Live` | `Long` | `37.50` | 131,730,000.00 USD | 0.00 USD | 234,310.00 USD | `-62.73%` | `6,248.15` |
| `Live` | `Long` | `38.50` | 131,500,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-61.74%` | `78,450.68` |
| `Live` | `Long` | `39.50` | 128,480,000.00 USD | 0.00 USD | 57,940.00 USD | `-60.75%` | `1,466.71` |
| `Live` | `Long` | `40.50` | 128,420,000.00 USD | 0.00 USD | 76,680.00 USD | `-59.75%` | `1,893.34` |
| `Live` | `Long` | `41.50` | 128,340,000.00 USD | 0.00 USD | 29,060.00 USD | `-58.76%` | `700.31` |
| `Live` | `Long` | `42.50` | 128,310,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-57.76%` | `24,384.40` |
| `Live` | `Long` | `43.50` | 127,280,000.00 USD | 0.00 USD | 155,310.00 USD | `-56.77%` | `3,570.36` |
| `Live` | `Long` | `44.50` | 127,120,000.00 USD | 0.00 USD | 216,380.00 USD | `-55.78%` | `4,862.47` |
| `Live` | `Long` | `45.50` | 126,910,000.00 USD | 0.00 USD | 60,640.00 USD | `-54.78%` | `1,332.78` |
| `Live` | `Long` | `46.50` | 126,840,000.00 USD | 0.00 USD | 4,760,000.00 USD | `-53.79%` | `102,329.93` |
| `Live` | `Long` | `47.50` | 122,090,000.00 USD | 0.00 USD | 144,140.00 USD | `-52.80%` | `3,034.45` |
| `Live` | `Long` | `48.50` | 121,940,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-51.80%` | `21,399.98` |
| `Live` | `Long` | `49.50` | 120,900,000.00 USD | 0.00 USD | 76,710.00 USD | `-50.81%` | `1,549.72` |
| `Live` | `Long` | `50.50` | 120,830,000.00 USD | 0.00 USD | 95,290.00 USD | `-49.81%` | `1,887.00` |
| `Live` | `Long` | `51.50` | 120,730,000.00 USD | 0.00 USD | 745,920.00 USD | `-48.82%` | `14,483.94` |
| `Live` | `Long` | `52.50` | 119,990,000.00 USD | 0.00 USD | 191,460.00 USD | `-47.83%` | `3,646.77` |
| `Live` | `Long` | `53.50` | 119,790,000.00 USD | 0.00 USD | 3,380,000.00 USD | `-46.83%` | `63,257.90` |
| `Live` | `Long` | `54.50` | 116,410,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-45.84%` | `21,299.56` |
| `Live` | `Long` | `55.50` | 115,250,000.00 USD | 0.00 USD | 190,340.00 USD | `-44.85%` | `3,429.52` |
| `Live` | `Long` | `56.50` | 115,060,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-43.85%` | `22,338.98` |
| `Live` | `Long` | `57.50` | 113,800,000.00 USD | 0.00 USD | 453,280.00 USD | `-42.86%` | `7,883.05` |
| `Live` | `Long` | `58.50` | 113,340,000.00 USD | 0.00 USD | 238,880.00 USD | `-41.86%` | `4,083.44` |
| `Live` | `Long` | `59.50` | 113,100,000.00 USD | 0.00 USD | 140,510.00 USD | `-40.87%` | `2,361.54` |
| `Live` | `Long` | `60.50` | 112,960,000.00 USD | 0.00 USD | 188,530.00 USD | `-39.88%` | `3,116.27` |
| `Live` | `Long` | `61.50` | 112,780,000.00 USD | 0.00 USD | 215,540.00 USD | `-38.88%` | `3,504.68` |
| `Live` | `Long` | `62.50` | 112,560,000.00 USD | 0.00 USD | 209,880.00 USD | `-37.89%` | `3,358.11` |
| `Live` | `Long` | `63.50` | 112,350,000.00 USD | 0.00 USD | 277,870.00 USD | `-36.90%` | `4,375.97` |
| `Live` | `Long` | `64.50` | 112,070,000.00 USD | 0.00 USD | 144,330.00 USD | `-35.90%` | `2,237.65` |
| `Live` | `Long` | `65.50` | 111,930,000.00 USD | 0.00 USD | 11,970,000.00 USD | `-34.91%` | `182,672.60` |
| `Live` | `Long` | `66.50` | 99,960,000.00 USD | 0.00 USD | 93,730.00 USD | `-33.91%` | `1,409.40` |
| `Live` | `Long` | `67.50` | 99,870,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-32.92%` | `15,615.65` |
| `Live` | `Long` | `68.50` | 98,820,000.00 USD | 0.00 USD | 37,980,000.00 USD | `-31.93%` | `554,400.53` |
| `Live` | `Long` | `69.50` | 60,840,000.00 USD | 0.00 USD | 166,780.00 USD | `-30.93%` | `2,399.68` |
| `Live` | `Long` | `70.50` | 60,670,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-29.94%` | `34,551.91` |
| `Live` | `Long` | `71.50` | 58,240,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-28.95%` | `19,744.20` |
| `Live` | `Long` | `72.50` | 56,820,000.00 USD | 0.00 USD | 2,200,000.00 USD | `-27.95%` | `30,378.07` |
| `Live` | `Long` | `73.50` | 54,620,000.00 USD | 0.00 USD | 593,320.00 USD | `-26.96%` | `8,072.32` |
| `Live` | `Long` | `74.50` | 54,030,000.00 USD | 0.00 USD | 614,790.00 USD | `-25.96%` | `8,252.21` |
| `Live` | `Long` | `75.50` | 53,410,000.00 USD | 0.00 USD | 754,900.00 USD | `-24.97%` | `9,998.66` |
| `Live` | `Long` | `76.50` | 52,660,000.00 USD | 0.00 USD | 203,660.00 USD | `-23.98%` | `2,662.17` |
| `Live` | `Long` | `77.50` | 52,460,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-22.98%` | `18,436.01` |
| `Live` | `Long` | `78.50` | 51,030,000.00 USD | 0.00 USD | 4,940,000.00 USD | `-21.99%` | `62,983.95` |
| `Live` | `Long` | `79.50` | 46,080,000.00 USD | 0.00 USD | 333,690.00 USD | `-21.00%` | `4,197.36` |
| `Live` | `Long` | `80.50` | 45,750,000.00 USD | 0.00 USD | 2,060,000.00 USD | `-20.00%` | `25,634.79` |
| `Live` | `Long` | `81.50` | 43,690,000.00 USD | 0.00 USD | 2,610,000.00 USD | `-19.01%` | `32,076.77` |
| `Live` | `Long` | `82.50` | 41,070,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-18.01%` | `17,816.94` |
| `Live` | `Long` | `83.50` | 39,600,000.00 USD | 0.00 USD | 739,670.00 USD | `-17.02%` | `8,858.32` |
| `Live` | `Long` | `84.50` | 38,860,000.00 USD | 0.00 USD | 710,900.00 USD | `-16.03%` | `8,413.02` |
| `Live` | `Long` | `85.50` | 38,150,000.00 USD | 0.00 USD | 879,320.00 USD | `-15.03%` | `10,284.44` |
| `Live` | `Long` | `86.50` | 37,270,000.00 USD | 0.00 USD | 839,590.00 USD | `-14.04%` | `9,706.20` |
| `Live` | `Long` | `87.50` | 36,430,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-13.05%` | `16,621.55` |
| `Live` | `Long` | `88.50` | 34,980,000.00 USD | 0.00 USD | 3,950,000.00 USD | `-12.05%` | `44,647.32` |
| `Live` | `Long` | `89.50` | 31,030,000.00 USD | 0.00 USD | 1,940,000.00 USD | `-11.06%` | `21,726.56` |
| `Live` | `Long` | `90.50` | 29,080,000.00 USD | 0.00 USD | 374,770.00 USD | `-10.06%` | `4,141.11` |
| `Live` | `Long` | `91.50` | 28,710,000.00 USD | 0.00 USD | 3,160,000.00 USD | `-9.07%` | `34,499.74` |
| `Live` | `Long` | `92.50` | 25,550,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-8.08%` | `24,325.41` |
| `Live` | `Long` | `93.50` | 23,300,000.00 USD | 0.00 USD | 3,120,000.00 USD | `-7.08%` | `33,408.47` |
| `Live` | `Long` | `94.50` | 20,180,000.00 USD | 0.00 USD | 2,970,000.00 USD | `-6.09%` | `31,393.63` |
| `Live` | `Long` | `95.50` | 17,210,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-5.10%` | `18,936.34` |
| `Live` | `Long` | `96.50` | 15,400,000.00 USD | 0.00 USD | 1,350,000.00 USD | `-4.10%` | `13,989.82` |
| `Live` | `Long` | `97.50` | 14,050,000.00 USD | 0.00 USD | 2,510,000.00 USD | `-3.11%` | `25,762.76` |
| `Live` | `Long` | `98.50` | 11,540,000.00 USD | 0.00 USD | 11,170,000.00 USD | `-2.11%` | `113,431.74` |
| `Live` | `Long` | `99.50` | 366,040.00 USD | 0.00 USD | 260,560.00 USD | `-1.12%` | `2,618.70` |
| `Live` | `Long` | `100.50` | 105,480.00 USD | 0.00 USD | 105,480.00 USD | `-0.13%` | `1,049.56` |
| `Live` | `Short` | `101.50` | 2,210.00 USD | 2,210.00 USD | 0.00 USD | `+0.87%` | `21.78` |
| `Live` | `Short` | `102.50` | 41,270.00 USD | 39,060.00 USD | 0.00 USD | `+1.86%` | `381.03` |
| `Live` | `Short` | `103.50` | 80,360.00 USD | 39,100.00 USD | 0.00 USD | `+2.85%` | `377.74` |
| `Live` | `Short` | `104.50` | 837,220.00 USD | 756,860.00 USD | 0.00 USD | `+3.85%` | `7,242.66` |
| `Live` | `Short` | `105.50` | 895,500.00 USD | 58,280.00 USD | 0.00 USD | `+4.84%` | `552.45` |
| `Live` | `Short` | `106.50` | 906,760.00 USD | 11,260.00 USD | 0.00 USD | `+5.84%` | `105.72` |
| `Live` | `Short` | `107.50` | 1,260,000.00 USD | 351,530.00 USD | 0.00 USD | `+6.83%` | `3,270.03` |
| `Live` | `Short` | `108.50` | 1,360,000.00 USD | 100,500.00 USD | 0.00 USD | `+7.82%` | `926.28` |
| `Live` | `Short` | `109.50` | 1,790,000.00 USD | 427,240.00 USD | 0.00 USD | `+8.82%` | `3,901.70` |
| `Live` | `Short` | `110.50` | 1,980,000.00 USD | 194,170.00 USD | 0.00 USD | `+9.81%` | `1,757.21` |
| `Live` | `Short` | `111.50` | 2,070,000.00 USD | 88,260.00 USD | 0.00 USD | `+10.80%` | `791.60` |
| `Live` | `Short` | `112.50` | 4,560,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+11.80%` | `22,115.34` |
| `Live` | `Short` | `113.50` | 4,710,000.00 USD | 155,490.00 USD | 0.00 USD | `+12.79%` | `1,369.94` |
| `Live` | `Short` | `114.50` | 4,760,000.00 USD | 51,280.00 USD | 0.00 USD | `+13.79%` | `447.86` |
| `Live` | `Short` | `115.50` | 6,780,000.00 USD | 2,010,000.00 USD | 0.00 USD | `+14.78%` | `17,433.68` |
| `Live` | `Short` | `116.50` | 6,910,000.00 USD | 135,940.00 USD | 0.00 USD | `+15.77%` | `1,166.84` |
| `Live` | `Short` | `117.50` | 11,780,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+16.77%` | `41,396.32` |
| `Live` | `Short` | `118.50` | 11,820,000.00 USD | 40,610.00 USD | 0.00 USD | `+17.76%` | `342.71` |
| `Live` | `Short` | `119.50` | 11,970,000.00 USD | 152,830.00 USD | 0.00 USD | `+18.76%` | `1,278.92` |
| `Live` | `Short` | `120.50` | 12,160,000.00 USD | 186,470.00 USD | 0.00 USD | `+19.75%` | `1,547.49` |
| `Live` | `Short` | `121.50` | 12,230,000.00 USD | 72,730.00 USD | 0.00 USD | `+20.74%` | `598.64` |
| `Live` | `Short` | `122.50` | 12,370,000.00 USD | 137,850.00 USD | 0.00 USD | `+21.74%` | `1,125.33` |
| `Live` | `Short` | `123.50` | 12,380,000.00 USD | 15,050.00 USD | 0.00 USD | `+22.73%` | `121.85` |
| `Live` | `Short` | `124.50` | 12,600,000.00 USD | 214,090.00 USD | 0.00 USD | `+23.72%` | `1,719.56` |
| `Live` | `Short` | `125.50` | 13,110,000.00 USD | 517,660.00 USD | 0.00 USD | `+24.72%` | `4,124.79` |
| `Live` | `Short` | `126.50` | 25,830,000.00 USD | 12,720,000.00 USD | 0.00 USD | `+25.71%` | `100,528.45` |
| `Live` | `Short` | `127.50` | 26,600,000.00 USD | 769,380.00 USD | 0.00 USD | `+26.71%` | `6,034.37` |
| `Live` | `Short` | `128.50` | 32,240,000.00 USD | 5,640,000.00 USD | 0.00 USD | `+27.70%` | `43,910.64` |
| `Live` | `Short` | `129.50` | 32,390,000.00 USD | 148,750.00 USD | 0.00 USD | `+28.69%` | `1,148.67` |
| `Live` | `Short` | `130.50` | 37,890,000.00 USD | 5,500,000.00 USD | 0.00 USD | `+29.69%` | `42,147.45` |
| `Live` | `Short` | `131.50` | 37,910,000.00 USD | 14,090.00 USD | 0.00 USD | `+30.68%` | `107.14` |
| `Live` | `Short` | `132.50` | 38,030,000.00 USD | 119,170.00 USD | 0.00 USD | `+31.67%` | `899.37` |
| `Live` | `Short` | `133.50` | 38,200,000.00 USD | 175,260.00 USD | 0.00 USD | `+32.67%` | `1,312.84` |
| `Live` | `Short` | `134.50` | 38,230,000.00 USD | 30,810.00 USD | 0.00 USD | `+33.66%` | `229.10` |
| `Live` | `Short` | `135.50` | 39,760,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+34.66%` | `11,272.94` |
| `Live` | `Short` | `136.50` | 39,810,000.00 USD | 51,040.00 USD | 0.00 USD | `+35.65%` | `373.94` |
| `Live` | `Short` | `137.50` | 40,040,000.00 USD | 225,800.00 USD | 0.00 USD | `+36.64%` | `1,642.19` |
| `Live` | `Short` | `138.50` | 42,350,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+37.64%` | `16,740.33` |
| `Live` | `Short` | `139.50` | 42,420,000.00 USD | 67,400.00 USD | 0.00 USD | `+38.63%` | `483.13` |
| `Live` | `Short` | `140.50` | 43,500,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+39.62%` | `7,710.96` |
| `Live` | `Short` | `141.50` | 43,970,000.00 USD | 462,490.00 USD | 0.00 USD | `+40.62%` | `3,268.45` |
| `Live` | `Short` | `142.50` | 44,060,000.00 USD | 96,220.00 USD | 0.00 USD | `+41.61%` | `675.20` |
| `Live` | `Short` | `143.50` | 44,130,000.00 USD | 62,920.00 USD | 0.00 USD | `+42.61%` | `438.47` |
| `Live` | `Short` | `144.50` | 44,210,000.00 USD | 87,980.00 USD | 0.00 USD | `+43.60%` | `608.89` |
| `Live` | `Short` | `145.50` | 45,250,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+44.59%` | `7,111.90` |
| `Live` | `Short` | `146.50` | 45,940,000.00 USD | 689,270.00 USD | 0.00 USD | `+45.59%` | `4,704.94` |
| `Live` | `Short` | `147.50` | 45,950,000.00 USD | 12,450.00 USD | 0.00 USD | `+46.58%` | `84.38` |
| `Live` | `Short` | `148.50` | 48,340,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+47.57%` | `16,073.53` |
| `Live` | `Short` | `149.50` | 48,360,000.00 USD | 18,880.00 USD | 0.00 USD | `+48.57%` | `126.26` |
| `Live` | `Short` | `150.50` | 48,400,000.00 USD | 38,370.00 USD | 0.00 USD | `+49.56%` | `254.96` |
| `Live` | `Short` | `151.50` | 48,450,000.00 USD | 53,640.00 USD | 0.00 USD | `+50.56%` | `354.05` |
| `Live` | `Short` | `152.50` | 49,420,000.00 USD | 976,210.00 USD | 0.00 USD | `+51.55%` | `6,401.39` |
| `Live` | `Short` | `153.50` | 49,840,000.00 USD | 416,970.00 USD | 0.00 USD | `+52.54%` | `2,716.39` |
| `Live` | `Short` | `154.50` | 49,850,000.00 USD | 8,740.00 USD | 0.00 USD | `+53.54%` | `56.59` |
| `Live` | `Short` | `155.50` | 49,980,000.00 USD | 129,920.00 USD | 0.00 USD | `+54.53%` | `835.52` |
| `Live` | `Short` | `156.50` | 54,820,000.00 USD | 4,840,000.00 USD | 0.00 USD | `+55.52%` | `30,912.73` |
| `Live` | `Short` | `157.50` | 56,470,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+56.52%` | `10,461.37` |
| `Live` | `Short` | `158.50` | 56,800,000.00 USD | 337,110.00 USD | 0.00 USD | `+57.51%` | `2,126.88` |
| `Live` | `Short` | `159.50` | 56,890,000.00 USD | 82,340.00 USD | 0.00 USD | `+58.51%` | `516.24` |
| `Live` | `Short` | `160.50` | 59,040,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+59.50%` | `13,413.09` |
| `Live` | `Short` | `161.50` | 59,250,000.00 USD | 215,730.00 USD | 0.00 USD | `+60.49%` | `1,335.78` |
| `Live` | `Short` | `162.50` | 59,400,000.00 USD | 145,240.00 USD | 0.00 USD | `+61.49%` | `893.79` |
| `Live` | `Short` | `163.50` | 59,400,000.00 USD | 1,610.00 USD | 0.00 USD | `+62.48%` | `9.85` |
| `Live` | `Short` | `164.50` | 59,610,000.00 USD | 209,200.00 USD | 0.00 USD | `+63.47%` | `1,271.73` |
| `Live` | `Short` | `165.50` | 96,100,000.00 USD | 36,490,000.00 USD | 0.00 USD | `+64.47%` | `220,467.98` |
| `Live` | `Short` | `166.50` | 96,430,000.00 USD | 337,280.00 USD | 0.00 USD | `+65.46%` | `2,025.72` |
| `Live` | `Short` | `167.50` | 97,440,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+66.46%` | `5,997.79` |
| `Live` | `Short` | `168.50` | 103,770,000.00 USD | 6,330,000.00 USD | 0.00 USD | `+67.45%` | `37,594.08` |
| `Live` | `Short` | `169.50` | 103,910,000.00 USD | 138,280.00 USD | 0.00 USD | `+68.44%` | `815.84` |
| `Live` | `Short` | `170.50` | 104,010,000.00 USD | 102,300.00 USD | 0.00 USD | `+69.44%` | `600.00` |
| `Live` | `Short` | `171.50` | 104,020,000.00 USD | 3,430.00 USD | 0.00 USD | `+70.43%` | `19.98` |
| `Live` | `Short` | `172.50` | 104,130,000.00 USD | 108,350.00 USD | 0.00 USD | `+71.42%` | `628.11` |
| `Live` | `Short` | `173.50` | 104,140,000.00 USD | 17,240.00 USD | 0.00 USD | `+72.42%` | `99.36` |
| `Live` | `Short` | `174.50` | 104,710,000.00 USD | 562,640.00 USD | 0.00 USD | `+73.41%` | `3,224.32` |
| `Live` | `Short` | `175.50` | 104,710,000.00 USD | 5,370.00 USD | 0.00 USD | `+74.41%` | `30.60` |
| `Live` | `Short` | `176.50` | 104,740,000.00 USD | 27,570.00 USD | 0.00 USD | `+75.40%` | `156.23` |
| `Live` | `Short` | `177.50` | 104,820,000.00 USD | 78,780.00 USD | 0.00 USD | `+76.39%` | `443.83` |
| `Live` | `Short` | `178.50` | 104,820,000.00 USD | 4,180.00 USD | 0.00 USD | `+77.39%` | `23.41` |
| `Live` | `Short` | `179.50` | 104,830,000.00 USD | 5,740.00 USD | 0.00 USD | `+78.38%` | `31.98` |
| `Live` | `Short` | `180.50` | 107,840,000.00 USD | 3,010,000.00 USD | 0.00 USD | `+79.37%` | `16,680.65` |
| `Live` | `Short` | `181.50` | 108,130,000.00 USD | 289,190.00 USD | 0.00 USD | `+80.37%` | `1,593.33` |
| `Live` | `Short` | `182.50` | 108,160,000.00 USD | 28,040.00 USD | 0.00 USD | `+81.36%` | `153.65` |
| `Live` | `Short` | `183.50` | 108,250,000.00 USD | 93,060.00 USD | 0.00 USD | `+82.36%` | `507.13` |
| `Live` | `Short` | `184.50` | 108,780,000.00 USD | 533,820.00 USD | 0.00 USD | `+83.35%` | `2,893.35` |
| `Live` | `Short` | `185.50` | 108,790,000.00 USD | 9,460.00 USD | 0.00 USD | `+84.34%` | `50.99` |
| `Live` | `Short` | `186.50` | 109,590,000.00 USD | 793,890.00 USD | 0.00 USD | `+85.34%` | `4,256.77` |
| `Live` | `Short` | `187.50` | 109,810,000.00 USD | 223,740.00 USD | 0.00 USD | `+86.33%` | `1,193.30` |
| `Live` | `Short` | `188.50` | 109,990,000.00 USD | 176,580.00 USD | 0.00 USD | `+87.32%` | `936.76` |
| `Live` | `Short` | `189.50` | 110,560,000.00 USD | 568,880.00 USD | 0.00 USD | `+88.32%` | `3,002.01` |
| `Live` | `Short` | `190.50` | 124,090,000.00 USD | 13,540,000.00 USD | 0.00 USD | `+89.31%` | `71,053.17` |
| `Live` | `Short` | `191.50` | 124,210,000.00 USD | 123,640.00 USD | 0.00 USD | `+90.31%` | `645.65` |
| `Live` | `Short` | `192.50` | 124,440,000.00 USD | 222,880.00 USD | 0.00 USD | `+91.30%` | `1,157.80` |
| `Live` | `Short` | `193.50` | 124,600,000.00 USD | 160,020.00 USD | 0.00 USD | `+92.29%` | `826.98` |
| `Live` | `Short` | `194.50` | 124,620,000.00 USD | 20,120.00 USD | 0.00 USD | `+93.29%` | `103.43` |
| `Live` | `Short` | `195.50` | 124,630,000.00 USD | 14,910.00 USD | 0.00 USD | `+94.28%` | `76.28` |
| `Live` | `Short` | `196.50` | 124,700,000.00 USD | 62,700.00 USD | 0.00 USD | `+95.28%` | `319.06` |
| `Live` | `Short` | `197.50` | 125,230,000.00 USD | 533,520.00 USD | 0.00 USD | `+96.27%` | `2,701.39` |
| `Live` | `Short` | `198.50` | 125,340,000.00 USD | 111,020.00 USD | 0.00 USD | `+97.26%` | `559.31` |
| `Live` | `Short` | `199.50` | 125,390,000.00 USD | 52,390.00 USD | 0.00 USD | `+98.26%` | `262.61` |
| `Live` | `Short` | `200.50` | 125,400,000.00 USD | 5,230.00 USD | 0.00 USD | `+99.25%` | `26.07` |
| `Live` | `Short` | `201.50` | 125,450,000.00 USD | 55,500.00 USD | 0.00 USD | `+100.24%` | `275.42` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.50` | 10,870,000.00 USD | 0.00 USD | 15,240.00 USD | `-76.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.50` | 10,850,000.00 USD | 0.00 USD | 3,830.00 USD | `-74.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.50` | 10,850,000.00 USD | 0.00 USD | 105.20 USD | `-73.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.50` | 10,850,000.00 USD | 0.00 USD | 502.03 USD | `-69.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.50` | 10,850,000.00 USD | 0.00 USD | 829.46 USD | `-66.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.50` | 10,840,000.00 USD | 0.00 USD | 1,320.00 USD | `-65.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.50` | 10,840,000.00 USD | 0.00 USD | 199.88 USD | `-62.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.50` | 10,840,000.00 USD | 0.00 USD | 205.21 USD | `-61.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.50` | 10,840,000.00 USD | 0.00 USD | 3,620.00 USD | `-60.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.50` | 10,840,000.00 USD | 0.00 USD | 423.63 USD | `-59.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.50` | 10,840,000.00 USD | 0.00 USD | 170,330.00 USD | `-57.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.50` | 10,670,000.00 USD | 0.00 USD | 104.40 USD | `-56.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.50` | 10,670,000.00 USD | 0.00 USD | 64,090.00 USD | `-54.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.50` | 10,600,000.00 USD | 0.00 USD | 249.71 USD | `-53.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.50` | 10,600,000.00 USD | 0.00 USD | 332.50 USD | `-52.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.50` | 10,600,000.00 USD | 0.00 USD | 102.82 USD | `-51.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.50` | 10,600,000.00 USD | 0.00 USD | 5,510.00 USD | `-49.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.50` | 10,600,000.00 USD | 0.00 USD | 4,070.00 USD | `-48.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.50` | 10,590,000.00 USD | 0.00 USD | 427.88 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.50` | 10,590,000.00 USD | 0.00 USD | 26,860.00 USD | `-46.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.50` | 10,570,000.00 USD | 0.00 USD | 785.89 USD | `-45.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.50` | 10,570,000.00 USD | 0.00 USD | 210.90 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.50` | 10,570,000.00 USD | 0.00 USD | 5,860.00 USD | `-43.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.50` | 10,560,000.00 USD | 0.00 USD | 6,550.00 USD | `-42.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.50` | 10,550,000.00 USD | 0.00 USD | 159.71 USD | `-41.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.50` | 10,550,000.00 USD | 0.00 USD | 10,860.00 USD | `-40.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.50` | 10,540,000.00 USD | 0.00 USD | 40,470.00 USD | `-39.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.50` | 10,500,000.00 USD | 0.00 USD | 18,990.00 USD | `-38.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.50` | 10,480,000.00 USD | 0.00 USD | 4,810.00 USD | `-37.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.50` | 10,480,000.00 USD | 0.00 USD | 13,260.00 USD | `-36.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.50` | 10,470,000.00 USD | 0.00 USD | 129.00 USD | `-35.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.50` | 10,460,000.00 USD | 0.00 USD | 4,650.00 USD | `-34.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.50` | 10,460,000.00 USD | 0.00 USD | 7,690.00 USD | `-33.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.50` | 10,450,000.00 USD | 0.00 USD | 607.50 USD | `-32.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.50` | 10,450,000.00 USD | 0.00 USD | 7,360.00 USD | `-31.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.50` | 10,440,000.00 USD | 0.00 USD | 54,850.00 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.50` | 10,390,000.00 USD | 0.00 USD | 50,700.00 USD | `-29.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.50` | 10,340,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.50` | 10,340,000.00 USD | 0.00 USD | 153,140.00 USD | `-27.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.50` | 10,180,000.00 USD | 0.00 USD | 139.65 USD | `-26.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.50` | 10,180,000.00 USD | 0.00 USD | 52,170.00 USD | `-25.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.50` | 10,130,000.00 USD | 0.00 USD | 26,730.00 USD | `-24.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.50` | 10,110,000.00 USD | 0.00 USD | 16,050.00 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.50` | 10,090,000.00 USD | 0.00 USD | 14,790.00 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.50` | 10,070,000.00 USD | 0.00 USD | 81,220.00 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.50` | 9,990,000.00 USD | 0.00 USD | 13,780.00 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.50` | 9,980,000.00 USD | 0.00 USD | 118,650.00 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.50` | 9,860,000.00 USD | 0.00 USD | 78,820.00 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.50` | 9,780,000.00 USD | 0.00 USD | 27,520.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.50` | 9,750,000.00 USD | 0.00 USD | 74,090.00 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.50` | 9,680,000.00 USD | 0.00 USD | 24,890.00 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.50` | 9,660,000.00 USD | 0.00 USD | 173,420.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.50` | 9,480,000.00 USD | 0.00 USD | 16,550.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.50` | 9,470,000.00 USD | 0.00 USD | 231,120.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.50` | 9,230,000.00 USD | 0.00 USD | 282,560.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.50` | 8,950,000.00 USD | 0.00 USD | 69,740.00 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.50` | 8,880,000.00 USD | 0.00 USD | 176,870.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.50` | 8,710,000.00 USD | 0.00 USD | 431,250.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.50` | 8,270,000.00 USD | 0.00 USD | 67,860.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.50` | 8,210,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.50` | 7,140,000.00 USD | 0.00 USD | 588,910.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.50` | 6,550,000.00 USD | 0.00 USD | 970,270.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.50` | 5,580,000.00 USD | 0.00 USD | 766,810.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.50` | 4,820,000.00 USD | 0.00 USD | 492,480.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.50` | 4,320,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.50` | 1,270,000.00 USD | 0.00 USD | 781,380.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `100.50` | 492,500.00 USD | 0.00 USD | 492,500.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.50` | 129,930.00 USD | 129,930.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.50` | 894,140.00 USD | 764,210.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.50` | 1,190,000.00 USD | 297,830.00 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.50` | 1,490,000.00 USD | 300,780.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.50` | 1,860,000.00 USD | 369,240.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.50` | 2,220,000.00 USD | 360,910.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.50` | 2,410,000.00 USD | 188,070.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.50` | 2,770,000.00 USD | 357,200.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.50` | 7,090,000.00 USD | 4,320,000.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.50` | 8,420,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.50` | 8,460,000.00 USD | 42,320.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.50` | 8,680,000.00 USD | 222,460.00 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.50` | 9,050,000.00 USD | 362,790.00 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.50` | 9,080,000.00 USD | 32,290.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.50` | 9,220,000.00 USD | 145,270.00 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.50` | 9,270,000.00 USD | 47,920.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.50` | 9,530,000.00 USD | 255,160.00 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.50` | 9,700,000.00 USD | 177,700.00 USD | 0.00 USD | `+17.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.50` | 9,940,000.00 USD | 239,490.00 USD | 0.00 USD | `+18.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.50` | 10,100,000.00 USD | 152,250.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.50` | 10,170,000.00 USD | 75,800.00 USD | 0.00 USD | `+20.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.50` | 10,700,000.00 USD | 528,840.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.50` | 11,760,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.50` | 11,930,000.00 USD | 166,110.00 USD | 0.00 USD | `+23.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.50` | 12,490,000.00 USD | 558,940.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.50` | 12,600,000.00 USD | 114,230.00 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.50` | 12,880,000.00 USD | 275,030.00 USD | 0.00 USD | `+26.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.50` | 12,940,000.00 USD | 58,000.00 USD | 0.00 USD | `+27.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.50` | 15,600,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+28.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.50` | 15,660,000.00 USD | 68,340.00 USD | 0.00 USD | `+29.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.50` | 15,840,000.00 USD | 179,050.00 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.50` | 15,870,000.00 USD | 26,010.00 USD | 0.00 USD | `+31.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.50` | 15,880,000.00 USD | 13,090.00 USD | 0.00 USD | `+32.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.50` | 16,130,000.00 USD | 250,640.00 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.50` | 16,210,000.00 USD | 74,880.00 USD | 0.00 USD | `+34.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.50` | 16,210,000.00 USD | 3,770.00 USD | 0.00 USD | `+35.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.50` | 16,250,000.00 USD | 34,120.00 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.50` | 23,000,000.00 USD | 6,760,000.00 USD | 0.00 USD | `+37.64%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `139.50` | 25,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.50` | 25,550,000.00 USD | 331,100.00 USD | 0.00 USD | `+39.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.50` | 25,560,000.00 USD | 10,520.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.50` | 25,910,000.00 USD | 346,440.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.50` | 25,910,000.00 USD | 529.51 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.50` | 26,180,000.00 USD | 269,670.00 USD | 0.00 USD | `+43.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.50` | 26,190,000.00 USD | 13,070.00 USD | 0.00 USD | `+44.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.50` | 26,390,000.00 USD | 198,500.00 USD | 0.00 USD | `+45.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.50` | 26,440,000.00 USD | 46,350.00 USD | 0.00 USD | `+46.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.50` | 27,770,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+47.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.50` | 28,280,000.00 USD | 512,760.00 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.50` | 28,550,000.00 USD | 268,780.00 USD | 0.00 USD | `+49.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.50` | 28,570,000.00 USD | 16,890.00 USD | 0.00 USD | `+50.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.50` | 28,580,000.00 USD | 12,020.00 USD | 0.00 USD | `+51.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.50` | 28,590,000.00 USD | 10,650.00 USD | 0.00 USD | `+52.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.50` | 28,600,000.00 USD | 12,110.00 USD | 0.00 USD | `+53.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.50` | 28,620,000.00 USD | 13,650.00 USD | 0.00 USD | `+54.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.50` | 28,620,000.00 USD | 2,230.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.50` | 28,640,000.00 USD | 22,350.00 USD | 0.00 USD | `+57.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.50` | 28,640,000.00 USD | 815.04 USD | 0.00 USD | `+58.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.50` | 28,880,000.00 USD | 242,540.00 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.50` | 28,880,000.00 USD | 282.62 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.50` | 28,890,000.00 USD | 5,030.00 USD | 0.00 USD | `+62.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.50` | 28,970,000.00 USD | 83,570.00 USD | 0.00 USD | `+64.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.50` | 28,970,000.00 USD | 517.81 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.50` | 28,980,000.00 USD | 2,030.00 USD | 0.00 USD | `+66.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.50` | 28,980,000.00 USD | 5,560.00 USD | 0.00 USD | `+67.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.50` | 28,980,000.00 USD | 1,410.00 USD | 0.00 USD | `+68.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.50` | 29,030,000.00 USD | 42,950.00 USD | 0.00 USD | `+69.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.50` | 29,030,000.00 USD | 686.00 USD | 0.00 USD | `+70.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.50` | 29,060,000.00 USD | 36,070.00 USD | 0.00 USD | `+71.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.50` | 29,070,000.00 USD | 6,550.00 USD | 0.00 USD | `+72.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.50` | 29,140,000.00 USD | 74,640.00 USD | 0.00 USD | `+74.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.50` | 29,150,000.00 USD | 1,450.00 USD | 0.00 USD | `+75.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.50` | 29,150,000.00 USD | 2,140.00 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.50` | 29,150,000.00 USD | 2,990.00 USD | 0.00 USD | `+77.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.50` | 29,150,000.00 USD | 262.07 USD | 0.00 USD | `+78.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.50` | 29,250,000.00 USD | 102,680.00 USD | 0.00 USD | `+79.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.50` | 29,260,000.00 USD | 2,730.00 USD | 0.00 USD | `+80.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.50` | 29,280,000.00 USD | 19,620.00 USD | 0.00 USD | `+81.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.50` | 29,830,000.00 USD | 550,500.00 USD | 0.00 USD | `+82.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.50` | 29,860,000.00 USD | 29,490.00 USD | 0.00 USD | `+84.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.50` | 30,050,000.00 USD | 191,020.00 USD | 0.00 USD | `+86.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.50` | 30,190,000.00 USD | 141,530.00 USD | 0.00 USD | `+87.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.50` | 30,230,000.00 USD | 38,960.00 USD | 0.00 USD | `+89.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.50` | 30,230,000.00 USD | 4,280.00 USD | 0.00 USD | `+93.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.50` | 30,230,000.00 USD | 1,760.00 USD | 0.00 USD | `+94.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `196.50` | 30,490,000.00 USD | 253,980.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.50` | 30,580,000.00 USD | 94,590.00 USD | 0.00 USD | `+96.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.50` | 30,960,000.00 USD | 374,220.00 USD | 0.00 USD | `+97.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.50` | 30,980,000.00 USD | 28,310.00 USD | 0.00 USD | `+98.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `200.50` | 31,290,000.00 USD | 302,360.00 USD | 0.00 USD | `+99.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `201.50` | 31,290,000.00 USD | 398.97 USD | 0.00 USD | `+100.24%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `89.90` | 374,300,000.00 USD | 0.00 USD | 374,300,000.00 USD | 525,310.00 USD | 459,170.00 USD | 925,200.00 USD |
| `1D` | `90.10` | 188,880,000.00 USD | 0.00 USD | 188,880,000.00 USD | 555,690.00 USD | 609,110.00 USD | 703,010.00 USD |
| `7D` | `90.10` | 372,390,000.00 USD | 0.00 USD | 372,390,000.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD |
| `1D` | `90.30` | 187,020,000.00 USD | 0.00 USD | 187,020,000.00 USD | 373,160.00 USD | 370,710.00 USD | 437,780.00 USD |
| `7D` | `90.30` | 370,320,000.00 USD | 0.00 USD | 370,320,000.00 USD | 826,230.00 USD | 342,020.00 USD | 654,780.00 USD |
| `1D` | `90.50` | 185,830,000.00 USD | 0.00 USD | 185,830,000.00 USD | 523,240.00 USD | 419,800.00 USD | 531,060.00 USD |
| `7D` | `90.50` | 368,490,000.00 USD | 0.00 USD | 368,490,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD |
| `1D` | `90.70` | 184,360,000.00 USD | 0.00 USD | 184,360,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `90.70` | 365,810,000.00 USD | 0.00 USD | 365,810,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `90.90` | 183,860,000.00 USD | 0.00 USD | 183,860,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `90.90` | 363,370,000.00 USD | 0.00 USD | 363,370,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `91.10` | 183,750,000.00 USD | 0.00 USD | 183,750,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `91.10` | 360,980,000.00 USD | 0.00 USD | 360,980,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `91.30` | 183,570,000.00 USD | 0.00 USD | 183,570,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD |
| `7D` | `91.30` | 359,080,000.00 USD | 0.00 USD | 359,080,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `91.50` | 183,420,000.00 USD | 0.00 USD | 183,420,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD |
| `7D` | `91.50` | 356,570,000.00 USD | 0.00 USD | 356,570,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD |
| `1D` | `91.70` | 183,310,000.00 USD | 0.00 USD | 183,310,000.00 USD | 107,440.00 USD | 112,260.00 USD | 1,080.00 USD |
| `7D` | `91.70` | 353,660,000.00 USD | 0.00 USD | 353,660,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `91.90` | 183,090,000.00 USD | 0.00 USD | 183,090,000.00 USD | 187,160.00 USD | 63,660.00 USD | 67,580.00 USD |
| `7D` | `91.90` | 352,030,000.00 USD | 0.00 USD | 352,030,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `1D` | `92.10` | 182,770,000.00 USD | 0.00 USD | 182,770,000.00 USD | 161,220.00 USD | 78,270.00 USD | 64,070.00 USD |
| `7D` | `92.10` | 349,610,000.00 USD | 0.00 USD | 349,610,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `1D` | `92.30` | 182,470,000.00 USD | 0.00 USD | 182,470,000.00 USD | 215,030.00 USD | 59,330.00 USD | 738,010.00 USD |
| `7D` | `92.30` | 348,300,000.00 USD | 0.00 USD | 348,300,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,200,000.00 USD |
| `1D` | `92.50` | 181,450,000.00 USD | 0.00 USD | 181,450,000.00 USD | 37,670.00 USD | 53,380.00 USD | 168,480.00 USD |
| `7D` | `92.50` | 346,290,000.00 USD | 0.00 USD | 346,290,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `1D` | `92.70` | 181,200,000.00 USD | 0.00 USD | 181,200,000.00 USD | 0.00 USD | 86,970.00 USD | 168,150.00 USD |
| `7D` | `92.70` | 344,890,000.00 USD | 0.00 USD | 344,890,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `1D` | `92.90` | 180,940,000.00 USD | 0.00 USD | 180,940,000.00 USD | 100,830.00 USD | 0.00 USD | 60,580.00 USD |
| `7D` | `92.90` | 344,620,000.00 USD | 0.00 USD | 344,620,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `1D` | `93.10` | 180,780,000.00 USD | 0.00 USD | 180,780,000.00 USD | 0.00 USD | 2,580.00 USD | 115,350.00 USD |
| `7D` | `93.10` | 344,560,000.00 USD | 0.00 USD | 344,560,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |
| `1D` | `93.30` | 180,660,000.00 USD | 0.00 USD | 180,660,000.00 USD | 0.00 USD | 103,020.00 USD | 99,970.00 USD |
| `7D` | `93.30` | 344,170,000.00 USD | 0.00 USD | 344,170,000.00 USD | 55,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `93.50` | 344,060,000.00 USD | 0.00 USD | 344,060,000.00 USD | 101,820.00 USD | 260,630.00 USD | 2,240.00 USD |
| `7D` | `93.70` | 343,700,000.00 USD | 0.00 USD | 343,700,000.00 USD | 270,240.00 USD | 262,300.00 USD | 115,880.00 USD |
| `7D` | `93.90` | 343,050,000.00 USD | 0.00 USD | 343,050,000.00 USD | 236,340.00 USD | 90,940.00 USD | 145,470.00 USD |
| `7D` | `94.10` | 342,570,000.00 USD | 0.00 USD | 342,570,000.00 USD | 233,120.00 USD | 296,810.00 USD | 321,280.00 USD |
| `7D` | `94.30` | 341,720,000.00 USD | 0.00 USD | 341,720,000.00 USD | 10,610.00 USD | 0.00 USD | 44,740.00 USD |
| `7D` | `94.50` | 341,670,000.00 USD | 0.00 USD | 341,670,000.00 USD | 183,750.00 USD | 0.00 USD | 140,220.00 USD |
| `7D` | `94.90` | 341,340,000.00 USD | 0.00 USD | 341,340,000.00 USD | 297,690.00 USD | 444,840.00 USD | 18,350.00 USD |
| `1D` | `95.10` | 180,460,000.00 USD | 0.00 USD | 180,460,000.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `95.10` | 340,580,000.00 USD | 0.00 USD | 340,580,000.00 USD | 141,070.00 USD | 115,890.00 USD | 9,610.00 USD |
| `1D` | `95.30` | 180,440,000.00 USD | 0.00 USD | 180,440,000.00 USD | 18,710.00 USD | 89,760.00 USD | 6,930.00 USD |
| `7D` | `95.30` | 340,320,000.00 USD | 0.00 USD | 340,320,000.00 USD | 251,720.00 USD | 196,820.00 USD | 474,750.00 USD |
| `1D` | `95.50` | 180,330,000.00 USD | 0.00 USD | 180,330,000.00 USD | 679,320.00 USD | 458,400.00 USD | 465,470.00 USD |
| `7D` | `95.50` | 339,390,000.00 USD | 0.00 USD | 339,390,000.00 USD | 1,000,000.00 USD | 732,540.00 USD | 341,230.00 USD |
| `1D` | `95.70` | 178,730,000.00 USD | 0.00 USD | 178,730,000.00 USD | 1,490,000.00 USD | 1,130,000.00 USD | 649,920.00 USD |
| `7D` | `95.70` | 337,320,000.00 USD | 0.00 USD | 337,320,000.00 USD | 1,980,000.00 USD | 1,130,000.00 USD | 1,450,000.00 USD |
| `1D` | `95.90` | 175,460,000.00 USD | 0.00 USD | 175,460,000.00 USD | 1,150,000.00 USD | 885,010.00 USD | 1,240,000.00 USD |
| `7D` | `95.90` | 332,760,000.00 USD | 0.00 USD | 332,760,000.00 USD | 1,610,000.00 USD | 1,260,000.00 USD | 2,660,000.00 USD |
| `1D` | `96.10` | 172,180,000.00 USD | 0.00 USD | 172,180,000.00 USD | 1,980,000.00 USD | 1,490,000.00 USD | 1,370,000.00 USD |
| `7D` | `96.10` | 327,220,000.00 USD | 0.00 USD | 327,220,000.00 USD | 2,910,000.00 USD | 2,330,000.00 USD | 2,640,000.00 USD |
| `1D` | `96.30` | 167,340,000.00 USD | 0.00 USD | 167,340,000.00 USD | 1,320,000.00 USD | 1,300,000.00 USD | 1,310,000.00 USD |
| `7D` | `96.30` | 319,340,000.00 USD | 0.00 USD | 319,340,000.00 USD | 3,210,000.00 USD | 1,280,000.00 USD | 2,390,000.00 USD |
| `1D` | `96.50` | 163,410,000.00 USD | 0.00 USD | 163,410,000.00 USD | 1,410,000.00 USD | 1,030,000.00 USD | 1,490,000.00 USD |
| `7D` | `96.50` | 312,460,000.00 USD | 0.00 USD | 312,460,000.00 USD | 2,870,000.00 USD | 1,580,000.00 USD | 2,860,000.00 USD |
| `1D` | `96.70` | 159,480,000.00 USD | 0.00 USD | 159,480,000.00 USD | 681,660.00 USD | 858,670.00 USD | 909,580.00 USD |
| `7D` | `96.70` | 305,150,000.00 USD | 0.00 USD | 305,150,000.00 USD | 2,220,000.00 USD | 2,450,000.00 USD | 2,360,000.00 USD |
| `1D` | `96.90` | 157,030,000.00 USD | 0.00 USD | 157,030,000.00 USD | 383,880.00 USD | 290,640.00 USD | 167,820.00 USD |
| `7D` | `96.90` | 298,110,000.00 USD | 0.00 USD | 298,110,000.00 USD | 5,140,000.00 USD | 3,170,000.00 USD | 3,350,000.00 USD |
| `1D` | `97.10` | 156,190,000.00 USD | 0.00 USD | 156,190,000.00 USD | 271,410.00 USD | 113,790.00 USD | 379,350.00 USD |
| `7D` | `97.10` | 286,450,000.00 USD | 0.00 USD | 286,450,000.00 USD | 4,430,000.00 USD | 2,080,000.00 USD | 1,660,000.00 USD |
| `1D` | `97.30` | 155,420,000.00 USD | 0.00 USD | 155,420,000.00 USD | 197,550.00 USD | 378,560.00 USD | 121,680.00 USD |
| `7D` | `97.30` | 278,290,000.00 USD | 0.00 USD | 278,290,000.00 USD | 5,780,000.00 USD | 4,270,000.00 USD | 3,750,000.00 USD |
| `1D` | `97.50` | 154,720,000.00 USD | 0.00 USD | 154,720,000.00 USD | 1,460,000.00 USD | 1,060,000.00 USD | 960,650.00 USD |
| `7D` | `97.50` | 264,490,000.00 USD | 0.00 USD | 264,490,000.00 USD | 4,390,000.00 USD | 4,370,000.00 USD | 4,390,000.00 USD |
| `1D` | `97.70` | 151,240,000.00 USD | 0.00 USD | 151,240,000.00 USD | 3,200,000.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `7D` | `97.70` | 251,340,000.00 USD | 0.00 USD | 251,340,000.00 USD | 5,660,000.00 USD | 3,410,000.00 USD | 5,400,000.00 USD |
| `1D` | `97.90` | 143,940,000.00 USD | 0.00 USD | 143,940,000.00 USD | 3,030,000.00 USD | 2,240,000.00 USD | 2,740,000.00 USD |
| `7D` | `97.90` | 236,870,000.00 USD | 0.00 USD | 236,870,000.00 USD | 8,020,000.00 USD | 6,060,000.00 USD | 7,190,000.00 USD |
| `1D` | `98.10` | 135,940,000.00 USD | 0.00 USD | 135,940,000.00 USD | 4,340,000.00 USD | 3,430,000.00 USD | 3,040,000.00 USD |
| `7D` | `98.10` | 215,590,000.00 USD | 0.00 USD | 215,590,000.00 USD | 8,580,000.00 USD | 7,190,000.00 USD | 7,130,000.00 USD |
| `1D` | `98.30` | 125,140,000.00 USD | 0.00 USD | 125,140,000.00 USD | 3,510,000.00 USD | 3,270,000.00 USD | 2,940,000.00 USD |
| `7D` | `98.30` | 192,700,000.00 USD | 0.00 USD | 192,700,000.00 USD | 8,150,000.00 USD | 4,260,000.00 USD | 7,860,000.00 USD |
| `1D` | `98.50` | 115,410,000.00 USD | 0.00 USD | 115,410,000.00 USD | 6,220,000.00 USD | 4,060,000.00 USD | 6,610,000.00 USD |
| `7D` | `98.50` | 172,430,000.00 USD | 0.00 USD | 172,430,000.00 USD | 10,550,000.00 USD | 7,040,000.00 USD | 9,610,000.00 USD |
| `1D` | `98.70` | 98,520,000.00 USD | 0.00 USD | 98,520,000.00 USD | 7,440,000.00 USD | 6,270,000.00 USD | 4,920,000.00 USD |
| `7D` | `98.70` | 145,230,000.00 USD | 0.00 USD | 145,230,000.00 USD | 11,830,000.00 USD | 9,800,000.00 USD | 13,480,000.00 USD |
| `1D` | `98.90` | 79,890,000.00 USD | 0.00 USD | 79,890,000.00 USD | 5,040,000.00 USD | 4,270,000.00 USD | 5,750,000.00 USD |
| `7D` | `98.90` | 110,120,000.00 USD | 0.00 USD | 110,120,000.00 USD | 15,300,000.00 USD | 9,640,000.00 USD | 17,510,000.00 USD |
| `1D` | `99.10` | 64,830,000.00 USD | 0.00 USD | 64,830,000.00 USD | 8,200,000.00 USD | 6,070,000.00 USD | 6,420,000.00 USD |
| `7D` | `99.10` | 67,670,000.00 USD | 0.00 USD | 67,670,000.00 USD | 18,940,000.00 USD | 12,780,000.00 USD | 10,390,000.00 USD |
| `1D` | `99.30` | 44,140,000.00 USD | 0.00 USD | 44,140,000.00 USD | 5,000,000.00 USD | 5,030,000.00 USD | 5,480,000.00 USD |
| `7D` | `99.30` | 25,570,000.00 USD | 0.00 USD | 25,570,000.00 USD | 4,260,000.00 USD | 1,630,000.00 USD | 6,950,000.00 USD |
| `1D` | `99.50` | 28,640,000.00 USD | 0.00 USD | 28,640,000.00 USD | 5,380,000.00 USD | 4,270,000.00 USD | 5,820,000.00 USD |
| `7D` | `99.50` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 1,370,000.00 USD | 1,380,000.00 USD | 4,060,000.00 USD |
| `1D` | `99.70` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 2,480,000.00 USD | 3,410,000.00 USD | 3,230,000.00 USD |
| `7D` | `99.70` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 661,070.00 USD | 1,650,000.00 USD | 2,240,000.00 USD |
| `1D` | `99.90` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 1,650,000.00 USD | 1,300,000.00 USD | 1,100,000.00 USD |
| `7D` | `99.90` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 843,730.00 USD | 0.00 USD | 531,900.00 USD |
| `1D` | `100.10` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 838,400.00 USD | 749,480.00 USD | 469,100.00 USD |
| `1D` | `100.10` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 838,400.00 USD | 749,480.00 USD | 469,100.00 USD |
| `7D` | `100.10` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 533,430.00 USD | 36,980.00 USD | 1,040,000.00 USD |
| `7D` | `100.10` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 533,430.00 USD | 36,980.00 USD | 1,040,000.00 USD |
| `1D` | `100.30` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,240.00 USD |
| `7D` | `100.30` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 39,280.00 USD | 68,710.00 USD | 0.00 USD |
| `1D` | `100.50` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,320,000.00 USD |
| `7D` | `100.50` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 39,680.00 USD | 0.00 USD | 1,480,000.00 USD |
| `1D` | `100.70` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 274,280.00 USD | 970,010.00 USD | 476,700.00 USD |
| `7D` | `100.70` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 46,010.00 USD | 1,230,000.00 USD | 0.00 USD |
| `1D` | `100.90` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 953,600.00 USD | 5,230.00 USD |
| `7D` | `100.90` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 1,610,000.00 USD | 3,730,000.00 USD |
| `1D` | `101.10` | 21,210,000.00 USD | 21,210,000.00 USD | 0.00 USD | 7,000,000.00 USD | 3,400,000.00 USD | 1,690,000.00 USD |
| `7D` | `101.10` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD |
| `1D` | `101.30` | 32,050,000.00 USD | 32,050,000.00 USD | 0.00 USD | 4,350,000.00 USD | 3,830,000.00 USD | 2,670,000.00 USD |
| `7D` | `101.30` | 30,160,000.00 USD | 30,160,000.00 USD | 0.00 USD | 5,710,000.00 USD | 2,910,000.00 USD | 6,370,000.00 USD |
| `1D` | `101.50` | 48,060,000.00 USD | 48,060,000.00 USD | 0.00 USD | 2,130,000.00 USD | 3,760,000.00 USD | 10,110,000.00 USD |
| `7D` | `101.50` | 42,880,000.00 USD | 42,880,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 10,160,000.00 USD |
| `1D` | `101.70` | 61,380,000.00 USD | 61,380,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 8,900,000.00 USD |
| `7D` | `101.70` | 52,220,000.00 USD | 52,220,000.00 USD | 0.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD |
| `1D` | `101.90` | 65,910,000.00 USD | 65,910,000.00 USD | 0.00 USD | 1,320,000.00 USD | 142,780.00 USD | 3,070,000.00 USD |
| `7D` | `101.90` | 58,680,000.00 USD | 58,680,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 3,790,000.00 USD |
| `1D` | `102.10` | 69,640,000.00 USD | 69,640,000.00 USD | 0.00 USD | 1,510,000.00 USD | 599,390.00 USD | 1,620,000.00 USD |
| `7D` | `102.10` | 61,400,000.00 USD | 61,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,720,000.00 USD |
| `1D` | `102.30` | 75,410,000.00 USD | 75,410,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,490,000.00 USD | 2,600,000.00 USD |
| `7D` | `102.30` | 66,570,000.00 USD | 66,570,000.00 USD | 0.00 USD | 2,130,000.00 USD | 803,220.00 USD | 2,240,000.00 USD |
| `1D` | `102.50` | 77,980,000.00 USD | 77,980,000.00 USD | 0.00 USD | 1,090,000.00 USD | 495,060.00 USD | 984,060.00 USD |
| `7D` | `102.50` | 69,670,000.00 USD | 69,670,000.00 USD | 0.00 USD | 680,620.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.70` | 79,440,000.00 USD | 79,440,000.00 USD | 0.00 USD | 931,170.00 USD | 524,710.00 USD | 3,170.00 USD |
| `7D` | `102.70` | 70,400,000.00 USD | 70,400,000.00 USD | 0.00 USD | 722,800.00 USD | 0.00 USD | 7,680.00 USD |
| `1D` | `102.90` | 83,380,000.00 USD | 83,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,770,000.00 USD | 792,760.00 USD |
| `7D` | `102.90` | 89,910,000.00 USD | 89,910,000.00 USD | 0.00 USD | 16,450,000.00 USD | 0.00 USD | 3,060,000.00 USD |
| `1D` | `103.10` | 89,550,000.00 USD | 89,550,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,800,000.00 USD | 1,590,000.00 USD |
| `7D` | `103.10` | 95,280,000.00 USD | 95,280,000.00 USD | 0.00 USD | 4,750,000.00 USD | 4,380.00 USD | 616,540.00 USD |
| `1D` | `103.30` | 93,950,000.00 USD | 93,950,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,200,000.00 USD | 815,560.00 USD |
| `7D` | `103.30` | 112,880,000.00 USD | 112,880,000.00 USD | 0.00 USD | 17,450,000.00 USD | 9,520.00 USD | 140,130.00 USD |
| `1D` | `103.50` | 106,460,000.00 USD | 106,460,000.00 USD | 0.00 USD | 4,290,000.00 USD | 2,690,000.00 USD | 5,530,000.00 USD |
| `7D` | `103.50` | 134,390,000.00 USD | 134,390,000.00 USD | 0.00 USD | 13,580,000.00 USD | 1,770,000.00 USD | 6,150,000.00 USD |
| `1D` | `103.70` | 118,380,000.00 USD | 118,380,000.00 USD | 0.00 USD | 4,210,000.00 USD | 2,380,000.00 USD | 5,340,000.00 USD |
| `7D` | `103.70` | 146,610,000.00 USD | 146,610,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.90` | 127,700,000.00 USD | 127,700,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,080,000.00 USD | 3,530,000.00 USD |
| `7D` | `103.90` | 163,870,000.00 USD | 163,870,000.00 USD | 0.00 USD | 8,600,000.00 USD | 2,630,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.10` | 136,870,000.00 USD | 136,870,000.00 USD | 0.00 USD | 3,750,000.00 USD | 2,340,000.00 USD | 3,090,000.00 USD |
| `7D` | `104.10` | 191,630,000.00 USD | 191,630,000.00 USD | 0.00 USD | 10,840,000.00 USD | 8,150,000.00 USD | 8,780,000.00 USD |
| `1D` | `104.30` | 144,910,000.00 USD | 144,910,000.00 USD | 0.00 USD | 2,940,000.00 USD | 1,930,000.00 USD | 3,170,000.00 USD |
| `7D` | `104.30` | 212,590,000.00 USD | 212,590,000.00 USD | 0.00 USD | 7,050,000.00 USD | 6,370,000.00 USD | 7,540,000.00 USD |
| `1D` | `104.50` | 152,670,000.00 USD | 152,670,000.00 USD | 0.00 USD | 2,600,000.00 USD | 2,230,000.00 USD | 2,930,000.00 USD |
| `7D` | `104.50` | 224,590,000.00 USD | 224,590,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD |
| `1D` | `104.70` | 162,280,000.00 USD | 162,280,000.00 USD | 0.00 USD | 2,570,000.00 USD | 1,950,000.00 USD | 5,080,000.00 USD |
| `7D` | `104.70` | 244,590,000.00 USD | 244,590,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD |
| `1D` | `104.90` | 165,250,000.00 USD | 165,250,000.00 USD | 0.00 USD | 1,020,000.00 USD | 592,030.00 USD | 1,360,000.00 USD |
| `7D` | `104.90` | 265,200,000.00 USD | 265,200,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.10` | 167,690,000.00 USD | 167,690,000.00 USD | 0.00 USD | 421,810.00 USD | 622,250.00 USD | 1,400,000.00 USD |
| `7D` | `105.10` | 278,870,000.00 USD | 278,870,000.00 USD | 0.00 USD | 5,580,000.00 USD | 5,260,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.30` | 168,620,000.00 USD | 168,620,000.00 USD | 0.00 USD | 506,770.00 USD | 2,430.00 USD | 425,580.00 USD |
| `7D` | `105.30` | 284,580,000.00 USD | 284,580,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | 428,740.00 USD |
| `1D` | `105.50` | 169,680,000.00 USD | 169,680,000.00 USD | 0.00 USD | 157,550.00 USD | 209,490.00 USD | 684,590.00 USD |
| `7D` | `105.50` | 304,420,000.00 USD | 304,420,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,270,000.00 USD | 7,970,000.00 USD |
| `1D` | `105.70` | 171,010,000.00 USD | 171,010,000.00 USD | 0.00 USD | 294,800.00 USD | 506,510.00 USD | 529,580.00 USD |
| `7D` | `105.70` | 319,270,000.00 USD | 319,270,000.00 USD | 0.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | 5,260,000.00 USD |
| `1D` | `105.90` | 172,020,000.00 USD | 172,020,000.00 USD | 0.00 USD | 215,940.00 USD | 666,590.00 USD | 135,010.00 USD |
| `7D` | `105.90` | 329,240,000.00 USD | 329,240,000.00 USD | 0.00 USD | 3,740,000.00 USD | 1,890,000.00 USD | 4,350,000.00 USD |
| `1D` | `106.10` | 173,480,000.00 USD | 173,480,000.00 USD | 0.00 USD | 716,050.00 USD | 470,500.00 USD | 267,330.00 USD |
| `7D` | `106.10` | 342,500,000.00 USD | 342,500,000.00 USD | 0.00 USD | 6,610,000.00 USD | 3,690,000.00 USD | 2,960,000.00 USD |
| `1D` | `106.30` | 174,590,000.00 USD | 174,590,000.00 USD | 0.00 USD | 371,950.00 USD | 438,180.00 USD | 299,430.00 USD |
| `7D` | `106.30` | 353,780,000.00 USD | 353,780,000.00 USD | 0.00 USD | 5,120,000.00 USD | 3,230,000.00 USD | 2,940,000.00 USD |
| `1D` | `106.50` | 176,140,000.00 USD | 176,140,000.00 USD | 0.00 USD | 882,260.00 USD | 333,990.00 USD | 333,130.00 USD |
| `7D` | `106.50` | 359,410,000.00 USD | 359,410,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,010,000.00 USD | 1,890,000.00 USD |
| `1D` | `106.70` | 179,100,000.00 USD | 179,100,000.00 USD | 0.00 USD | 852,650.00 USD | 288,850.00 USD | 1,820,000.00 USD |
| `7D` | `106.70` | 369,140,000.00 USD | 369,140,000.00 USD | 0.00 USD | 2,290,000.00 USD | 3,150,000.00 USD | 4,290,000.00 USD |
| `1D` | `106.90` | 180,160,000.00 USD | 180,160,000.00 USD | 0.00 USD | 317,210.00 USD | 150,690.00 USD | 594,370.00 USD |
| `7D` | `106.90` | 374,920,000.00 USD | 374,920,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,120,000.00 USD | 3,470,000.00 USD |
| `1D` | `107.10` | 181,010,000.00 USD | 181,010,000.00 USD | 0.00 USD | 88,570.00 USD | 254,230.00 USD | 510,390.00 USD |
| `7D` | `107.10` | 378,320,000.00 USD | 378,320,000.00 USD | 0.00 USD | 1,630,000.00 USD | 508,540.00 USD | 1,260,000.00 USD |
| `1D` | `107.30` | 181,480,000.00 USD | 181,480,000.00 USD | 0.00 USD | 252,090.00 USD | 0.00 USD | 212,790.00 USD |
| `7D` | `107.30` | 378,480,000.00 USD | 378,480,000.00 USD | 0.00 USD | 0.00 USD | 156,300.00 USD | 0.00 USD |
| `1D` | `107.50` | 181,770,000.00 USD | 181,770,000.00 USD | 0.00 USD | 0.00 USD | 6,440.00 USD | 288,380.00 USD |
| `7D` | `107.50` | 379,460,000.00 USD | 379,460,000.00 USD | 0.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD |
| `1D` | `107.70` | 182,300,000.00 USD | 182,300,000.00 USD | 0.00 USD | 94,360.00 USD | 181,310.00 USD | 249,940.00 USD |
| `7D` | `107.70` | 380,430,000.00 USD | 380,430,000.00 USD | 0.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD |
| `1D` | `107.90` | 182,420,000.00 USD | 182,420,000.00 USD | 0.00 USD | 0.00 USD | 128,660.00 USD | 0.00 USD |
| `7D` | `107.90` | 380,600,000.00 USD | 380,600,000.00 USD | 0.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.10` | 381,850,000.00 USD | 381,850,000.00 USD | 0.00 USD | 509,480.00 USD | 727,340.00 USD | 7,940.00 USD |
| `7D` | `108.30` | 384,250,000.00 USD | 384,250,000.00 USD | 0.00 USD | 1,090,000.00 USD | 697,770.00 USD | 612,150.00 USD |
| `7D` | `108.50` | 385,790,000.00 USD | 385,790,000.00 USD | 0.00 USD | 835,610.00 USD | 340,050.00 USD | 367,300.00 USD |
| `7D` | `108.70` | 388,160,000.00 USD | 388,160,000.00 USD | 0.00 USD | 575,510.00 USD | 726,100.00 USD | 1,070,000.00 USD |
| `7D` | `108.90` | 389,450,000.00 USD | 389,450,000.00 USD | 0.00 USD | 414,890.00 USD | 701,350.00 USD | 181,660.00 USD |
| `1D` | `109.10` | 182,430,000.00 USD | 182,430,000.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `109.10` | 390,540,000.00 USD | 390,540,000.00 USD | 0.00 USD | 434,330.00 USD | 185,250.00 USD | 461,880.00 USD |
| `1D` | `109.30` | 182,570,000.00 USD | 182,570,000.00 USD | 0.00 USD | 126,020.00 USD | 9,360.00 USD | 2,950.00 USD |
| `7D` | `109.30` | 391,390,000.00 USD | 391,390,000.00 USD | 0.00 USD | 486,260.00 USD | 85,680.00 USD | 286,560.00 USD |
| `1D` | `109.50` | 182,830,000.00 USD | 182,830,000.00 USD | 0.00 USD | 133,350.00 USD | 84,430.00 USD | 44,310.00 USD |
| `7D` | `109.50` | 391,630,000.00 USD | 391,630,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `1D` | `109.70` | 183,740,000.00 USD | 183,740,000.00 USD | 0.00 USD | 456,990.00 USD | 277,760.00 USD | 171,080.00 USD |
| `7D` | `109.70` | 392,820,000.00 USD | 392,820,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `1D` | `109.90` | 184,680,000.00 USD | 184,680,000.00 USD | 0.00 USD | 268,320.00 USD | 266,300.00 USD | 405,440.00 USD |
| `7D` | `109.90` | 394,310,000.00 USD | 394,310,000.00 USD | 0.00 USD | 238,580.00 USD | 447,100.00 USD | 807,700.00 USD |
| `1D` | `110.10` | 186,100,000.00 USD | 186,100,000.00 USD | 0.00 USD | 478,410.00 USD | 482,760.00 USD | 463,520.00 USD |
| `7D` | `110.10` | 396,380,000.00 USD | 396,380,000.00 USD | 0.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD |
| `1D` | `110.30` | 187,290,000.00 USD | 187,290,000.00 USD | 0.00 USD | 373,160.00 USD | 370,710.00 USD | 437,780.00 USD |
| `7D` | `110.30` | 398,200,000.00 USD | 398,200,000.00 USD | 0.00 USD | 826,230.00 USD | 342,020.00 USD | 654,780.00 USD |
| `1D` | `110.50` | 188,010,000.00 USD | 188,010,000.00 USD | 0.00 USD | 300,210.00 USD | 170,900.00 USD | 254,570.00 USD |
| `7D` | `110.50` | 398,690,000.00 USD | 398,690,000.00 USD | 0.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD |
| `1D` | `110.70` | 188,760,000.00 USD | 188,760,000.00 USD | 0.00 USD | 223,030.00 USD | 248,900.00 USD | 276,490.00 USD |
| `7D` | `110.70` | 400,890,000.00 USD | 400,890,000.00 USD | 0.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD |
| `1D` | `110.90` | 189,260,000.00 USD | 189,260,000.00 USD | 0.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `110.90` | 403,330,000.00 USD | 403,330,000.00 USD | 0.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `111.10` | 189,370,000.00 USD | 189,370,000.00 USD | 0.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `111.10` | 405,720,000.00 USD | 405,720,000.00 USD | 0.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `111.30` | 189,550,000.00 USD | 189,550,000.00 USD | 0.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `111.30` | 407,620,000.00 USD | 407,620,000.00 USD | 0.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `111.40` | 189,580,000.00 USD | 189,580,000.00 USD | 0.00 USD | 27,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `111.50` | 410,130,000.00 USD | 410,130,000.00 USD | 0.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `7D` | `111.70` | 411,270,000.00 USD | 411,270,000.00 USD | 0.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD |
| `7D` | `111.90` | 413,040,000.00 USD | 413,040,000.00 USD | 0.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD |
| `7D` | `112.10` | 414,670,000.00 USD | 414,670,000.00 USD | 0.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `7D` | `112.30` | 417,090,000.00 USD | 417,090,000.00 USD | 0.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `7D` | `112.50` | 418,400,000.00 USD | 418,400,000.00 USD | 0.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `7D` | `112.70` | 418,920,000.00 USD | 418,920,000.00 USD | 0.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD |
| `7D` | `112.90` | 420,410,000.00 USD | 420,410,000.00 USD | 0.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD |
| `7D` | `113.10` | 421,800,000.00 USD | 421,800,000.00 USD | 0.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `7D` | `113.30` | 422,080,000.00 USD | 422,080,000.00 USD | 0.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `7D` | `113.50` | 422,140,000.00 USD | 422,140,000.00 USD | 0.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `7D` | `113.70` | 422,530,000.00 USD | 422,530,000.00 USD | 0.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.24B` | Total OI Tokens: `62,314,694.1 SOL`
  * 1h OI Change: `+0.25%` | 4h OI Change: `-2.07%` | 24h OI Change: `-3.11%`
  * Exchange Breakdown: Binance=`1.09B` | Bybit=`615.77M` | OKX=`352.75M` | Hyperliquid=`565.30M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `183.37K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0080%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0042%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `50.12%` | `49.88%` | `1.00` | 14,160,000.00 USD |
| `15M` | `Binance` | `54.08%` | `45.92%` | `1.18` | 4,800,000.00 USD |
| `15M` | `OKX` | `46.96%` | `53.04%` | `0.89` | 1,100,000.00 USD |
| `15M` | `Bybit` | `46.14%` | `53.86%` | `0.86` | 1,810,000.00 USD |
| `15M` | `KuCoin` | `62.57%` | `37.43%` | `1.67` | 16,350.00 USD |
| `15M` | `Gate` | `52.38%` | `47.62%` | `1.10` | 1,070,000.00 USD |
| `15M` | `Bitget` | `68.39%` | `31.61%` | `2.16` | 628,060.00 USD |
| `15M` | `BingX` | `50.03%` | `49.97%` | `1.00` | 190,270.00 USD |
| `15M` | `MEXC` | `60.14%` | `39.86%` | `1.51` | 1,470,000.00 USD |
| `15M` | `Bitunix` | `31.98%` | `68.02%` | `0.47` | 1,060,000.00 USD |
| `15M` | `Hyperliquid` | `64.1%` | `35.9%` | `1.79` | 79,200.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.26%` | `50.74%` | `0.97` | 74,740.00 USD |
| `15M` | `Crypto.com` | `65.57%` | `34.43%` | `1.90` | 22,790.00 USD |
| `15M` | `WhiteBIT` | `29.39%` | `70.61%` | `0.42` | 1,600,000.00 USD |
| `15M` | `HTX` | `37.15%` | `62.85%` | `0.59` | 8,840.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `62.49%` | `37.51%` | `1.67` | 58,070.00 USD |
| `15M` | `Aster` | `67.13%` | `32.87%` | `2.04` | 130,850.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `28.87%` | `71.13%` | `0.41` | 34,240.00 USD |
| `15M` | `Whale Positions` | `54.08%` | `45.92%` | `1.18` | 4,800,000.00 USD |
| `15M` | `Global Accounts` | `50.12%` | `49.88%` | `1.00` | 14,160,000.00 USD |
| `1H` | `SOL` | `56.31%` | `43.69%` | `1.29` | 91,240,000.00 USD |
| `1H` | `Binance` | `51.27%` | `48.73%` | `1.05` | 28,610,000.00 USD |
| `1H` | `OKX` | `58.81%` | `41.19%` | `1.43` | 8,690,000.00 USD |
| `1H` | `Bybit` | `47.55%` | `52.45%` | `0.91` | 11,290,000.00 USD |
| `1H` | `KuCoin` | `69.37%` | `30.63%` | `2.26` | 131,430.00 USD |
| `1H` | `Gate` | `55.51%` | `44.49%` | `1.25` | 6,270,000.00 USD |
| `1H` | `Bitget` | `54.85%` | `45.15%` | `1.21` | 3,830,000.00 USD |
| `1H` | `BingX` | `26%` | `74%` | `0.35` | 4,350,000.00 USD |
| `1H` | `MEXC` | `61.71%` | `38.29%` | `1.61` | 10,310,000.00 USD |
| `1H` | `Bitunix` | `56.57%` | `43.43%` | `1.30` | 7,320,000.00 USD |
| `1H` | `Hyperliquid` | `55.9%` | `44.1%` | `1.27` | 1,370,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `67.04%` | `32.96%` | `2.03` | 406,960.00 USD |
| `1H` | `Crypto.com` | `64.86%` | `35.14%` | `1.85` | 142,610.00 USD |
| `1H` | `WhiteBIT` | `99.52%` | `0.48%` | `207.33` | 6,980,000.00 USD |
| `1H` | `HTX` | `63.96%` | `36.04%` | `1.77` | 171,660.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `58.54%` | `41.46%` | `1.41` | 315,860.00 USD |
| `1H` | `Aster` | `55.29%` | `44.71%` | `1.24` | 906,570.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `35.8%` | `64.2%` | `0.56` | 133,020.00 USD |
| `1H` | `Whale Positions` | `51.27%` | `48.73%` | `1.05` | 28,610,000.00 USD |
| `1H` | `Global Accounts` | `56.31%` | `43.69%` | `1.29` | 91,240,000.00 USD |
| `4H` | `SOL` | `45.58%` | `54.42%` | `0.84` | 539,540,000.00 USD |
| `4H` | `Binance` | `46%` | `54%` | `0.85` | 176,440,000.00 USD |
| `4H` | `OKX` | `45.35%` | `54.65%` | `0.83` | 56,090,000.00 USD |
| `4H` | `Bybit` | `42.44%` | `57.56%` | `0.74` | 76,060,000.00 USD |
| `4H` | `KuCoin` | `46.31%` | `53.69%` | `0.86` | 4,490,000.00 USD |
| `4H` | `Gate` | `47.22%` | `52.78%` | `0.89` | 24,750,000.00 USD |
| `4H` | `Bitget` | `43.82%` | `56.18%` | `0.78` | 39,750,000.00 USD |
| `4H` | `BingX` | `29.99%` | `70.01%` | `0.43` | 14,980,000.00 USD |
| `4H` | `MEXC` | `49.92%` | `50.08%` | `1.00` | 67,100,000.00 USD |
| `4H` | `Bitunix` | `48.45%` | `51.55%` | `0.94` | 31,730,000.00 USD |
| `4H` | `Hyperliquid` | `45.33%` | `54.67%` | `0.83` | 10,350,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.92%` | `42.08%` | `1.38` | 2,280,000.00 USD |
| `4H` | `Crypto.com` | `51.42%` | `48.58%` | `1.06` | 732,090.00 USD |
| `4H` | `WhiteBIT` | `47.47%` | `52.53%` | `0.90` | 24,750,000.00 USD |
| `4H` | `HTX` | `63.11%` | `36.89%` | `1.71` | 444,590.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.51%` | `50.49%` | `0.98` | 2,720,000.00 USD |
| `4H` | `Aster` | `39.66%` | `60.34%` | `0.66` | 6,320,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.29%` | `55.71%` | `0.80` | 563,680.00 USD |
| `4H` | `Whale Positions` | `46%` | `54%` | `0.85` | 176,440,000.00 USD |
| `4H` | `Global Accounts` | `45.58%` | `54.42%` | `0.84` | 539,540,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `101.65` | `101.65` | `101.65` | `101.78` | `101.53` | 12,871,901.66 USD | 6,991,731.87 USD | 5,880,169.78 USD | 1,111,562.09 USD | `+8.64%` | `1B / 2S` |
| `0:00 UTC` | `101.00` | `101.32` | `101.00` | `101.77` | `100.97` | 23,345,961.64 USD | 9,081,895.18 USD | 14,264,066.46 USD | -5,182,171.27 USD | `-22.20%` | `6B / 20S` |
| `5:00 UTC` | `100.91` | `100.89` | `100.91` | `101.13` | `100.72` | 21,682,501.47 USD | 10,212,926.11 USD | 11,469,575.36 USD | -1,256,649.25 USD | `-5.80%` | `6B / 4S` |
| `0:00 UTC` | `101.07` | `101.03` | `101.07` | `101.19` | `100.90` | 11,845,890.84 USD | 5,647,320.15 USD | 6,198,570.68 USD | -551,250.53 USD | `-4.65%` | `2B / 1S` |
| `5:00 UTC` | `100.81` | `100.98` | `100.81` | `101.18` | `100.75` | 7,681,327.85 USD | 3,539,960.94 USD | 4,141,366.91 USD | -601,405.98 USD | `-7.83%` | `5B / 12S` |
| `0:00 UTC` | `100.38` | `100.47` | `100.38` | `100.81` | `100.30` | 26,755,803.01 USD | 9,721,488.50 USD | 17,034,314.50 USD | -7,312,826.00 USD | `-27.33%` | `0B / 21S` |
| `5:00 UTC` | `100.66` | `100.58` | `100.66` | `100.78` | `100.34` | 9,618,082.62 USD | 5,517,082.05 USD | 4,101,000.56 USD | 1,416,081.49 USD | `+14.72%` | `9B / 2S` |
| `0:00 UTC` | `100.38` | `100.40` | `100.38` | `100.62` | `100.25` | 9,521,682.83 USD | 4,738,635.78 USD | 4,783,047.06 USD | -44,411.28 USD | `-0.47%` | `0B / 7S` |
| `5:00 UTC` | `100.31` | `100.27` | `100.31` | `100.43` | `100.16` | 10,974,925.19 USD | 4,852,550.33 USD | 6,122,374.86 USD | -1,269,824.53 USD | `-11.57%` | `4B / 3S` |
| `0:00 UTC` | `100.13` | `100.21` | `100.13` | `100.38` | `100.10` | 10,332,121.05 USD | 6,736,138.61 USD | 3,595,982.44 USD | 3,140,156.17 USD | `+30.39%` | `6B / 2S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 293,930.00 USD | 1,880,000.00 USD | **`ACCUMULATION`** |
| `15m` | 419,570.00 USD | 1,990,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,340,000.00 USD | -1,150,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,230,000.00 USD | 1,440,000.00 USD | **`ACCUMULATION`** |
| `2h` | -924,680.00 USD | -17,080,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -265,930.00 USD | -61,800,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 11,770,000.00 USD | -29,160,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 14,590,000.00 USD | -58,630,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 24,930,000.00 USD | -52,210,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 22,300,000.00 USD | -108,450,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 86,510,000.00 USD | -303,480,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 63,940,000.00 USD | -1,880,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+293.93K` | 15m=`+419.57K` | 1h=`+2.23M` | 24h=`+22.30M`
* Futures Capital Netflows: 5m=`+1.88M` | 15m=`+1.99M` | 1h=`+1.44M` | 24h=`-108.45M`
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
  * Execution Entry: `99.18` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `98.24` (Risk Distance: `0.9376` pts)
  * +2.5R Take Profit: `101.52`
  * Mathematical Lot Sizing: **`10.66 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.19` (Risk Distance: `0.9376` pts)
  * +2.5R Take Profit: `98.91`
  * Mathematical Lot Sizing: **`10.66 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`100.77`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
