# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.29` | **Live Ask Quote**: `96.53` | **Mid Price**: `96.41`
- **Spread Points**: `24.00` | **Spread BPS**: `24.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `99.63` | VWAP Z-Score: `-2.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.9338` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `28.87` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `104.61` | Lower -3.00σ Band: `94.64`
  * Upper +2.51σ Band: `103.79` | Lower -2.51σ Band: `95.46`
  * Upper +2.01σ Band: `102.96` | Lower -2.01σ Band: `96.29`
  * Upper +2.00σ Band: `102.95` | Lower -2.00σ Band: `96.31`
  * Upper +1.28σ Band: `101.75` | Lower -1.28σ Band: `97.50`
  * Upper +1.00σ Band: `101.29` | Lower -1.00σ Band: `97.97`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`97.00` | EMA-20=`97.94` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`99.19` (Slope: `+0.0000`) | EMA-100=`99.89`
  * Institutional Anchors: EMA-144=`100.14` | EMA-200=`100.25` (Slope: `-0.4201`) | EMA-233=`100.35`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`94.56` | Weekly High=`103.63` | Weekly Low=`94.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `97.46` (Distance: `-1.02%`)
  * Point of Control (POC) = `96.75` (Distance: `-0.30%`)
  * Value Area Low (VAL) = `96.47` (Distance: `-0.01%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.60` | Weekly POC=`100.94` | Weekly VAL=`99.61`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`95.04`
  * London Session (08:00-16:00 UTC): High=`96.80` | Low=`96.02`
  * New York Session (13:00-21:00 UTC): High=`96.99` | Low=`95.83`
  * Initial Balance (First Hour): IB High=`96.70` | IB Low=`96.12`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.02` - `96.80`
  * Optimal Trade Entry (OTE 0.705): `96.60`
  * Structural Invalidation Anchor (0.786): `97.18`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `96.40` | `96.67` | `96.24` | `96.60` | `144,097` | 13,895,955.40 USD | 917,831.66 USD | `+6.61%` | -185,409,020.01 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `96.59` | `96.73` | `96.52` | `96.62` | `141,565` | 13,678,988.55 USD | 2,810,427.50 USD | `+20.55%` | -182,598,592.51 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `96.63` | `96.64` | `96.56` | `96.58` | `20,136` | 1,945,034.26 USD | -153,067.52 USD | `-7.87%` | -182,751,660.03 USD | `+0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `97.35` | `97.40` | `96.78` | `97.02` | `270,663` | 26,257,148.78 USD | 19,383.03 USD | `+0.07%` | -186,722,487.29 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `97.01` | `97.08` | `96.24` | `96.62` | `438,539` | 42,350,844.60 USD | 3,657,690.21 USD | `+8.64%` | -183,064,797.08 USD | `+0.82` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `96.63` | `96.64` | `96.56` | `96.59` | `21,059` | 2,034,213.65 USD | -68,104.38 USD | `-3.35%` | -183,132,901.46 USD | `+0.51` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `96.11` | `98.04` | `95.34` | `97.50` | `3,580,269` | 347,367,878.36 USD | -51,442,556.41 USD | `-14.81%` | -171,425,272.13 USD | `-2.76` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.50` | `97.82` | `96.45` | `97.02` | `2,626,091` | 255,409,491.97 USD | -13,397,349.17 USD | `-5.25%` | -184,822,621.30 USD | `-0.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `97.01` | `97.08` | `96.24` | `96.57` | `458,685` | 44,296,920.85 USD | 3,503,580.70 USD | `+7.91%` | -181,319,040.60 USD | `+0.67` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `96.57` | `12,600,455` | 1,225,537,596.40 USD | -113,859,064.43 USD | `-9.29%` | -181,319,040.60 USD | `-2.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -29,365,912.19 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -33,659,266.07 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `96.57` | `12,600,455` | 1,225,537,596.40 USD | -113,859,064.43 USD | `-9.29%` | -181,319,040.60 USD | `-2.07` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`96.41`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `96.58` | `240.2200` | 23,201.65 USD | 600,580.31 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `96.58` | `140.4700` | 13,567.15 USD | 614,147.47 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `96.58` | `275.4600` | 26,604.75 USD | 640,752.22 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `96.58` | `65.6000` | 6,335.71 USD | 647,087.93 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.58` | `1971.6400` | 190,420.99 USD | 837,508.93 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `96.59` | `161.9800` | 15,646.46 USD | 131,520.23 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `249.9700` | 24,145.60 USD | 155,665.83 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `249.9700` | 24,145.35 USD | 179,811.18 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `341.0100` | 32,938.84 USD | 212,750.02 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `210.3900` | 20,321.78 USD | 233,071.80 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `438.1400` | 42,319.94 USD | 275,391.74 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `165.5300` | 15,988.38 USD | 291,380.12 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `2570.3300` | 248,263.03 USD | 539,643.15 USD | `30 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `325.0900` | 31,399.47 USD | 571,042.62 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `96.59` | `65.6000` | 6,336.04 USD | 577,378.66 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `96.60` | `3.1100` | 300.43 USD | 300.43 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `96.60` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 96.60` | `0.00%` | `-` |
| `BID` | `96.60` | `868.2500` | 83,872.95 USD | 83,872.95 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `96.60` | `82.8200` | 8,000.33 USD | 91,873.28 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `96.60` | `82.8200` | 8,000.25 USD | 99,873.53 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `96.60` | `82.8200` | 8,000.16 USD | 107,873.69 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `96.60` | `82.8200` | 8,000.08 USD | 115,873.77 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `96.61` | `102.0000` | 9,854.53 USD | 20,145.40 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.61` | `103.4100` | 9,990.44 USD | 10,290.87 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.62` | `1.5000` | 144.94 USD | 57,908.94 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.62` | `10.0000` | 966.23 USD | 57,764.00 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.62` | `102.0000` | 9,855.34 USD | 56,797.77 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.62` | `102.8700` | 9,939.30 USD | 46,942.43 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.62` | `174.4800` | 16,857.73 USD | 37,003.13 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.63` | `276.6000` | 26,727.86 USD | 94,492.95 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `96.63` | `102.0000` | 9,856.16 USD | 67,765.10 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `96.64` | `171.0500` | 16,531.13 USD | 169,653.41 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `96.64` | `65.5100` | 6,331.15 USD | 153,122.29 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `96.64` | `63.7800` | 6,163.89 USD | 146,791.14 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.64` | `115.0000` | 11,113.72 USD | 140,627.25 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.64` | `121.2000` | 11,712.77 USD | 129,513.53 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `96.64` | `24.1800` | 2,336.73 USD | 117,800.77 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.64` | `102.0000` | 9,856.97 USD | 115,464.03 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.64` | `115.0100` | 11,114.11 USD | 105,607.06 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `96.65` | `63.7800` | 6,164.15 USD | 181,981.64 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `96.65` | `63.7800` | 6,164.08 USD | 175,817.50 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15` | `0x5b5d...c060` | `SHORT` | 67,403,919.95 USD | `696,120.13` | `94.33` | `96.72` | `354.21` | -1,735,653.73 USD | `-2.58%` | `7X Cross` |
| `20` | `0x9c6a...a4ed` | `LONG` | 53,263,890.85 USD | `550,087.69` | `80.86` | `96.72` | `68.18` | 8,784,904.46 USD | `+16.49%` | `20X Cross` |
| `54` | `0xb83d...6e36` | `SHORT` | 25,099,982.64 USD | `259,300.02` | `91.42` | `96.72` | `690.54` | -1,394,849.62 USD | `-5.56%` | `5X Cross` |
| `82` | `0x3dc9...54b0` | `SHORT` | 21,269,618.37 USD | `220,000.19` | `105.90` | `96.72` | `175.47` | 2,029,488.91 USD | `+9.54%` | `20X Cross` |
| `109` | `0x9c89...600e` | `LONG` | 18,269,506.87 USD | `189,472.50` | `115.21` | `96.72` | `35.01` | -3,559,508.39 USD | `-19.48%` | `20X Cross` |
| `121` | `0x4a20...3c26` | `LONG` | 17,420,940.00 USD | `180,000.00` | `106.43` | `96.72` | `68.18` | -1,737,338.71 USD | `-9.97%` | `20X Cross` |
| `133` | `0xecb6...2b00` | `SHORT` | 15,364,817.01 USD | `158,679.91` | `101.98` | `96.72` | `280.50` | 817,329.13 USD | `+5.32%` | `20X Cross` |
| `180` | `0x7a5a...0394` | `SHORT` | 11,639,752.78 USD | `120,506.81` | `99.79` | `96.72` | `121.35` | 385,721.88 USD | `+3.31%` | `10X Cross` |
| `227` | `0xc63a...a3cd` | `LONG` | 9,661,800.00 USD | `100,000.00` | `112.22` | `96.72` | `0.000000` | -1,560,308.97 USD | `-16.15%` | `20X Cross` |
| `268` | `0xb581...6f4f` | `LONG` | 8,700,210.00 USD | `90,000.00` | `114.59` | `96.72` | `0.000000` | -1,613,082.29 USD | `-18.54%` | `3X Cross` |
| `290` | `0x645b...87b8` | `SHORT` | 8,081,579.76 USD | `83,462.39` | `103.90` | `96.72` | `357.78` | 590,406.64 USD | `+7.31%` | `20X Cross` |
| `299` | `0xdb3a...cf3b` | `LONG` | 7,913,348.24 USD | `81,851.78` | `106.04` | `96.72` | `44.61` | -766,398.62 USD | `-9.68%` | `4X Cross` |
| `314` | `0xe927...98ef` | `LONG` | 7,541,040.00 USD | `78,000.00` | `96.34` | `96.72` | `38.45` | 26,898.52 USD | `+0.36%` | `3X Cross` |
| `323` | `0xca49...53c8` | `SHORT` | 7,146,116.84 USD | `73,943.45` | `110.70` | `96.72` | `294.25` | 1,039,505.42 USD | `+14.55%` | `20X Cross` |
| `330` | `0x8ae4...3d60` | `LONG` | 6,978,295.05 USD | `72,180.05` | `111.72` | `96.72` | `9.24` | -1,085,865.18 USD | `-15.56%` | `10X Cross` |
| `335` | `0xa0b7...6165` | `SHORT` | 6,879,089.10 USD | `71,044.42` | `107.87` | `96.72` | `190.91` | 784,378.10 USD | `+11.40%` | `2X Cross` |
| `354` | `0xf517...c032` | `SHORT` | 6,558,860.57 USD | `67,778.53` | `84.64` | `96.72` | `213.00` | -821,829.41 USD | `-12.53%` | `20X Cross` |
| `383` | `0x7fda...17d1` | `SHORT` | 6,141,690.15 USD | `63,428.21` | `100.90` | `96.72` | `703.55` | 258,246.32 USD | `+4.20%` | `20X Cross` |
| `465` | `0x7e23...5a5a` | `LONG` | 4,701,000.84 USD | `48,564.56` | `105.17` | `96.72` | `57.00` | -406,568.32 USD | `-8.65%` | `5X Isolated` |
| `581` | `0x2e2b...2fab` | `LONG` | 3,871,960.00 USD | `40,000.00` | `119.55` | `96.72` | `58.63` | -910,075.64 USD | `-23.50%` | `10X Cross` |
| `592` | `0xf899...88db` | `SHORT` | 3,818,424.50 USD | `39,434.72` | `88.19` | `96.72` | `117.75` | -340,798.89 USD | `-8.93%` | `20X Cross` |
| `633` | `0x9946...0852` | `SHORT` | 3,600,171.78 USD | `37,198.39` | `112.11` | `96.72` | `138.21` | 570,310.42 USD | `+15.84%` | `20X Cross` |
| `643` | `0x27b8...12fc` | `LONG` | 3,488,732.29 USD | `36,085.73` | `110.86` | `96.72` | `20.88` | -511,612.96 USD | `-14.66%` | `10X Cross` |
| `650` | `0x9c16...4a6f` | `SHORT` | 3,457,553.94 USD | `35,779.15` | `90.45` | `96.72` | `119.55` | -221,448.91 USD | `-6.40%` | `20X Cross` |
| `654` | `0x3440...32c5` | `SHORT` | 3,431,722.17 USD | `35,529.12` | `95.02` | `96.72` | `174.16` | -55,700.74 USD | `-1.62%` | `20X Cross` |
| `717` | `0xfc27...9d9d` | `SHORT` | 3,149,640.55 USD | `32,528.20` | `101.14` | `96.72` | `632.96` | 140,384.04 USD | `+4.46%` | `20X Cross` |
| `732` | `0x023a...2355` | `SHORT` | 3,116,825.78 USD | `32,188.97` | `101.45` | `96.72` | `310.92` | 148,644.87 USD | `+4.77%` | `20X Cross` |
| `740` | `0x96a7...79df` | `LONG` | 3,097,760.00 USD | `32,000.00` | `74.39` | `96.72` | `0.000000` | 717,354.15 USD | `+23.16%` | `20X Cross` |
| `774` | `0xbe19...8bd1` | `SHORT` | 2,947,205.91 USD | `30,451.69` | `97.62` | `96.72` | `768.49` | 25,340.72 USD | `+0.86%` | `3X Cross` |
| `780` | `0x482b...cae4` | `SHORT` | 2,927,659.92 USD | `30,310.49` | `88.03` | `96.72` | `149.19` | -259,411.63 USD | `-8.86%` | `20X Cross` |
| `800` | `0x610b...b613` | `LONG` | 2,865,028.66 USD | `29,634.14` | `101.23` | `96.72` | `70.39` | -134,970.69 USD | `-4.71%` | `3X Isolated` |
| `812` | `0x45d2...4029` | `SHORT` | 2,822,535.12 USD | `29,220.00` | `93.28` | `96.72` | `1579.22` | -96,759.14 USD | `-3.43%` | `20X Cross` |
| `818` | `0xa61c...66b9` | `LONG` | 2,790,609.69 USD | `28,888.00` | `104.39` | `96.72` | `0.000000` | -224,954.43 USD | `-8.06%` | `5X Cross` |
| `856` | `0x458d...ab3b` | `LONG` | 2,651,007.83 USD | `27,385.03` | `117.17` | `96.72` | `81.07` | -557,654.69 USD | `-21.04%` | `3X Isolated` |
| `932` | `0x051c...693c` | `LONG` | 2,433,648.66 USD | `25,139.70` | `89.76` | `96.72` | `34.54` | 177,087.33 USD | `+7.28%` | `20X Cross` |
| `980` | `0x638f...f5f0` | `LONG` | 2,318,040.00 USD | `24,000.00` | `136.71` | `96.72` | `48.38` | -962,928.54 USD | `-41.54%` | `20X Cross` |
| `1026` | `0x7178...0854` | `LONG` | 2,183,033.04 USD | `22,545.24` | `110.94` | `96.72` | `36.54` | -318,111.43 USD | `-14.57%` | `10X Cross` |
| `1046` | `0x739c...cfb2` | `LONG` | 2,126,960.00 USD | `22,000.00` | `91.95` | `96.72` | `77.47` | 104,052.69 USD | `+4.89%` | `20X Cross` |
| `1058` | `0x69cc...14fd` | `SHORT` | 2,096,566.98 USD | `21,701.57` | `99.01` | `96.72` | `476.67` | 52,085.77 USD | `+2.48%` | `20X Cross` |
| `1129` | `0x7749...ea04` | `LONG` | 1,976,893.90 USD | `20,429.00` | `97.90` | `96.72` | `72.01` | -23,105.20 USD | `-1.17%` | `20X Cross` |
| `1133` | `0x7737...bf66` | `SHORT` | 1,973,768.15 USD | `20,384.06` | `102.94` | `96.72` | `926.71` | 124,573.75 USD | `+6.31%` | `10X Cross` |
| `1157` | `0xea00...a918` | `LONG` | 1,935,273.08 USD | `20,022.69` | `66.09` | `96.72` | `0.000000` | 611,964.48 USD | `+31.62%` | `20X Cross` |
| `1158` | `0xbfc7...80b4` | `SHORT` | 1,933,820.00 USD | `20,000.00` | `85.98` | `96.72` | `286.44` | -214,285.50 USD | `-11.08%` | `20X Cross` |
| `1159` | `0x3fc5...c0c1` | `SHORT` | 1,933,000.00 USD | `20,000.00` | `98.28` | `96.72` | `208.88` | 32,559.84 USD | `+1.68%` | `20X Cross` |
| `1160` | `0x251f...6e5d` | `LONG` | 1,931,680.00 USD | `20,000.00` | `101.15` | `96.72` | `67.89` | -91,417.77 USD | `-4.73%` | `20X Cross` |
| `1164` | `0xfc66...ca06` | `LONG` | 1,925,502.06 USD | `19,914.18` | `97.30` | `96.72` | `0.000000` | -12,141.91 USD | `-0.63%` | `20X Cross` |
| `1178` | `0x936c...bb0f` | `SHORT` | 1,904,029.67 USD | `19,664.04` | `105.57` | `96.72` | `292.92` | 171,932.51 USD | `+9.03%` | `20X Cross` |
| `1191` | `0x7160...d47c` | `LONG` | 1,881,201.45 USD | `19,434.10` | `105.03` | `96.72` | `82.70` | -160,019.84 USD | `-8.51%` | `20X Cross` |
| `1215` | `0xe097...d0fe` | `LONG` | 1,838,199.73 USD | `18,995.75` | `109.71` | `96.72` | `0.000000` | -245,797.16 USD | `-13.37%` | `20X Cross` |
| `1289` | `0xdf95...7d72` | `SHORT` | 1,726,329.38 USD | `17,828.64` | `104.53` | `96.72` | `2356.11` | 137,351.60 USD | `+7.96%` | `20X Cross` |
| `1296` | `0xe98b...8cd5` | `SHORT` | 1,706,389.19 USD | `17,622.89` | `187.95` | `96.72` | `262.77` | 1,605,831.53 USD | `+94.11%` | `20X Cross` |
| `1347` | `0xee2b...d67e` | `LONG` | 1,638,661.12 USD | `16,963.19` | `119.86` | `96.72` | `31.61` | -394,610.52 USD | `-24.08%` | `4X Cross` |
| `1350` | `0x123d...3bff` | `LONG` | 1,635,878.77 USD | `16,920.55` | `89.54` | `96.72` | `0.000000` | 120,885.02 USD | `+7.39%` | `10X Cross` |
| `1451` | `0x73d7...8be1` | `LONG` | 1,513,385.54 USD | `15,668.95` | `106.60` | `96.72` | `71.84` | -156,955.43 USD | `-10.37%` | `20X Cross` |
| `1459` | `0xc74a...ab93` | `LONG` | 1,504,414.74 USD | `15,536.82` | `64.06` | `96.72` | `54.88` | 509,185.91 USD | `+33.85%` | `5X Isolated` |
| `1462` | `0x8d0c...e17b` | `LONG` | 1,499,601.50 USD | `15,511.14` | `97.56` | `96.72` | `90.00` | -13,600.09 USD | `-0.91%` | `10X Cross` |
| `1494` | `0x34e6...8d74` | `LONG` | 1,457,628.95 USD | `15,091.67` | `101.19` | `96.72` | `39.53` | -69,441.94 USD | `-4.76%` | `20X Cross` |
| `1502` | `0x5f10...d49d` | `LONG` | 1,450,290.00 USD | `15,000.00` | `96.35` | `96.72` | `69.44` | 4,988.84 USD | `+0.34%` | `20X Cross` |
| `1503` | `0xc7d1...51af` | `SHORT` | 1,450,200.00 USD | `15,000.00` | `105.79` | `96.72` | `138.76` | 136,675.00 USD | `+9.42%` | `20X Cross` |
| `1505` | `0xb322...d51f` | `LONG` | 1,448,997.61 USD | `14,999.82` | `102.98` | `96.72` | `44.70` | -95,729.69 USD | `-6.61%` | `20X Cross` |
| `1557` | `0xffb2...5ed6` | `LONG` | 1,402,411.10 USD | `14,504.05` | `117.89` | `96.72` | `86.45` | -307,493.61 USD | `-21.93%` | `20X Cross` |
| `1583` | `0x0d6a...ca57` | `LONG` | 1,373,498.92 USD | `14,206.65` | `110.41` | `96.72` | `91.60` | -195,091.44 USD | `-14.20%` | `5X Isolated` |
| `1612` | `0x7277...0b98` | `SHORT` | 1,337,911.86 USD | `13,837.70` | `101.18` | `96.72` | `205.11` | 62,207.91 USD | `+4.65%` | `20X Cross` |
| `1863` | `0x2482...0e55` | `LONG` | 1,098,544.58 USD | `11,363.98` | `122.03` | `96.72` | `91.54` | -288,157.34 USD | `-26.23%` | `20X Isolated` |
| `1890` | `0x45db...86eb` | `LONG` | 1,074,135.90 USD | `11,100.00` | `110.69` | `96.72` | `68.72` | -154,546.00 USD | `-14.39%` | `5X Cross` |
| `1926` | `0x1d04...7c43` | `LONG` | 1,046,881.10 USD | `10,811.76` | `111.55` | `96.72` | `15.53` | -159,180.39 USD | `-15.21%` | `6X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `121.80` | 4,331.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.33K USD at 121.8000 USD [API] | `2026-10-05 08:07:00` |
| `ANNOUNCEMENT` | `INFO` | `102.17` | 44,049.57 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 44.05K USD at 102.1700 USD [API] | `2026-10-28 19:01:55` |
| `ANNOUNCEMENT` | `INFO` | `102.06` | 34,916.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 34.92K USD at 102.0600 USD [API] | `2026-10-28 19:06:18` |
| `ANNOUNCEMENT` | `INFO` | `102.06` | 67,302.45 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 67.30K USD at 102.0600 USD [API] | `2026-10-28 19:06:18` |
| `ANNOUNCEMENT` | `INFO` | `102.53` | 26,714.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 26.71K USD at 102.5300 USD [API] | `2026-10-28 19:45:32` |
| `ANNOUNCEMENT` | `INFO` | `102.60` | 31,605.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 31.61K USD at 102.6000 USD [API] | `2026-10-28 19:53:21` |
| `ANNOUNCEMENT` | `INFO` | `103.10` | 24,999.69 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 25.00K USD at 103.1000 USD [API] | `2026-10-28 20:10:26` |
| `ANNOUNCEMENT` | `INFO` | `103.47` | 212.11 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.21K USD at 103.4700 USD [API] | `2026-10-28 20:01:15` |
| `ANNOUNCEMENT` | `INFO` | `103.47` | 25.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.03K USD at 103.4700 USD [API] | `2026-10-28 20:01:15` |
| `ANNOUNCEMENT` | `INFO` | `103.47` | 220.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.22K USD at 103.4700 USD [API] | `2026-10-28 20:01:15` |
| `ANNOUNCEMENT` | `INFO` | `103.47` | 177.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.18K USD at 103.4700 USD [API] | `2026-10-28 20:01:15` |
| `ANNOUNCEMENT` | `INFO` | `103.83` | 122.52 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.12K USD at 103.8300 USD [API] | `2026-10-28 20:02:00` |
| `ANNOUNCEMENT` | `INFO` | `103.83` | 204.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 103.8300 USD [API] | `2026-10-28 20:02:00` |
| `ANNOUNCEMENT` | `INFO` | `103.83` | 12.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 103.8300 USD [API] | `2026-10-28 20:02:00` |
| `ANNOUNCEMENT` | `INFO` | `103.83` | 684.24 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.68K USD at 103.8300 USD [API] | `2026-10-28 20:02:00` |
| `ANNOUNCEMENT` | `INFO` | `103.83` | 12.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 103.8300 USD [API] | `2026-10-28 20:02:00` |
| `ANNOUNCEMENT` | `INFO` | `103.83` | 773.53 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.77K USD at 103.8300 USD [API] | `2026-10-28 20:02:00` |
| `ANNOUNCEMENT` | `INFO` | `67.00` | 8,673.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 8.67K USD at 67.0000 USD [API] | `2026-06-25 13:41:53` |
| `ANNOUNCEMENT` | `INFO` | `102.24` | 20,000.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 102.2400 USD [API] | `2026-10-28 20:52:09` |
| `ANNOUNCEMENT` | `INFO` | `102.31` | 21,333.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 21.33K USD at 102.3100 USD [API] | `2026-10-28 20:54:20` |
| `ANNOUNCEMENT` | `INFO` | `102.78` | 59,799.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 59.80K USD at 102.7800 USD [API] | `2026-10-28 21:59:24` |
| `ANNOUNCEMENT` | `INFO` | `102.40` | 31,110.14 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 31.11K USD at 102.4000 USD [API] | `2026-10-28 22:03:08` |
| `ANNOUNCEMENT` | `INFO` | `102.40` | 31,110.14 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 31.11K USD at 102.4000 USD [API] | `2026-10-28 22:03:08` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.19` (Vol: 5,600,000.00 USD, Dist: `+4.23%`) | Long MP=`94.69` (Vol: 2,200,000.00 USD, Dist: `--2.46%`)
  * 48H Horizon: Short MP=`104.09` (Vol: 5,300,000.00 USD, Dist: `+7.22%`) | Long MP=`94.72` (Vol: 2,100,000.00 USD, Dist: `--2.43%`)
  * 3D Horizon: Short MP=`104.09` (Vol: 5,800,000.00 USD, Dist: `+7.22%`) | Long MP=`94.72` (Vol: 2,100,000.00 USD, Dist: `--2.43%`)
  * 7D Horizon: Short MP=`104.13` (Vol: 7,700,000.00 USD, Dist: `+7.26%`) | Long MP=`94.75` (Vol: 2,100,000.00 USD, Dist: `--2.40%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.35` | 43,020.00 USD | 141,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,520.00 USD | 141,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.65` | 489.48 USD | 141,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.75` | 12,740.00 USD | 141,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.15` | 1,700.00 USD | 141,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 730,740.00 USD | 141,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.45` | 4,090.00 USD | 140,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.75` | 158.53 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 344.42 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 7,580.00 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 186.97 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.25` | 4,730.00 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,410.00 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 1,860.00 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 102.58 USD | 140,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 107.17 USD | 140,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 10,570.00 USD | 140,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 9,140.00 USD | 140,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 131.20 USD | 140,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 1,120.00 USD | 140,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 9,200.00 USD | 140,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 836.16 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 10,030.00 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 2,140.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.95` | 230.88 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 721.50 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.45` | 1,220.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.55` | 1,500.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 252.91 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 222,930.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 2,460.00 USD | 140,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 140,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 37,080.00 USD | 140,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 140,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 526.85 USD | 140,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.85` | 408.43 USD | 140,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 4,050.00 USD | 140,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 2,010.00 USD | 140,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.15` | 1,310.00 USD | 140,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 140,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 5,970.00 USD | 140,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 102.60 USD | 140,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 30,230.00 USD | 140,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 131.41 USD | 140,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.25` | 166.22 USD | 140,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 140,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.65` | 244.98 USD | 140,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.75` | 4,610.00 USD | 140,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 412.18 USD | 140,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 140,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 28,150.00 USD | 140,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 42,520.00 USD | 140,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 140,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 140,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 935.01 USD | 140,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 10,220.00 USD | 140,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 877.19 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 7,830.00 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 16,670.00 USD | 140,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 16,330.00 USD | 139,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.85` | 15,620.00 USD | 139,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 728.98 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 7,170.00 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 47,340.00 USD | 139,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.25` | 443.47 USD | 139,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.45` | 732.32 USD | 139,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 889.01 USD | 139,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 139,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.75` | 7,660.00 USD | 139,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 1,740.00 USD | 139,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 529,550.00 USD | 139,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 2,790.00 USD | 139,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 101.28 USD | 139,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 1,570.00 USD | 139,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 475.87 USD | 139,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 1,800.00 USD | 139,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 24,680.00 USD | 139,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 139,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 219.45 USD | 139,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 384.04 USD | 139,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 16,580.00 USD | 139,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 13,140.00 USD | 139,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 66,900.00 USD | 139,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 562.61 USD | 139,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,760.00 USD | 139,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 337.77 USD | 139,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 139,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 441.84 USD | 132,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 17,620.00 USD | 132,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 14,660.00 USD | 132,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.55` | 893,720.00 USD | 132,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 47,920.00 USD | 131,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 7,470.00 USD | 131,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 5,870.00 USD | 131,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 131,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 817,260.00 USD | 131,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,410.00 USD | 130,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 130,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 247.39 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 500.90 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 320.59 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 2,220.00 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 2,810.00 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 320.60 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 42,120.00 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 19,600.00 USD | 130,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 401.84 USD | 130,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 262.85 USD | 130,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,580.00 USD | 130,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 47,580.00 USD | 130,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 3,110.00 USD | 130,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,980.00 USD | 130,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 542.59 USD | 130,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 1,090.00 USD | 130,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 451.38 USD | 130,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 130,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 49,340.00 USD | 127,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 127,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,400.00 USD | 127,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 195,360.00 USD | 127,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,470.00 USD | 127,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 1,770.00 USD | 127,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 24,590.00 USD | 127,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 116,160.00 USD | 127,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 596,880.00 USD | 127,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 1,560.00 USD | 126,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 3,450.00 USD | 126,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 126,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.95` | 399.50 USD | 126,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 1,510.00 USD | 126,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 8,700.00 USD | 126,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 126,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 2,400.00 USD | 126,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 4,150.00 USD | 126,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 2,880.00 USD | 126,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 438.17 USD | 126,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 14,280.00 USD | 126,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 25,320.00 USD | 126,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 126,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 12,820.00 USD | 126,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 4,260.00 USD | 126,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 126,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 588.26 USD | 126,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 109,250.00 USD | 126,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 48,400.00 USD | 126,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 470.12 USD | 126,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 19,850.00 USD | 126,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 146.19 USD | 126,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 198.62 USD | 126,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 6,960.00 USD | 126,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,460.00 USD | 126,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 4,680.00 USD | 126,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,890.00 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 4,710.00 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 37,820.00 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 4,390.00 USD | 126,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 8,760.00 USD | 126,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 275.38 USD | 126,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 126,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,220.00 USD | 126,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 359,690.00 USD | 126,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,110.00 USD | 125,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 2,640.00 USD | 125,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 125,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 3,670,000.00 USD | 125,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 410.78 USD | 122,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 2,220.00 USD | 122,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 477.20 USD | 122,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 686,220.00 USD | 122,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 3,630.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 6,540.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 5,770.00 USD | 121,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 3,990.00 USD | 121,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 121,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 319.09 USD | 121,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,790.00 USD | 121,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 573.58 USD | 121,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 121,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 281.83 USD | 121,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 997.76 USD | 121,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 2,770.00 USD | 121,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 42,080.00 USD | 121,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 3,890.00 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 633.08 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 9,560.00 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 140.55 USD | 121,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,590.00 USD | 121,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 460.62 USD | 121,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 4,130.00 USD | 121,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 6,930.00 USD | 121,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 269.90 USD | 121,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 106.04 USD | 121,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 3,480.00 USD | 121,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 1,150,000.00 USD | 121,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 4,630.00 USD | 120,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 5,470.00 USD | 120,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,200.00 USD | 120,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 5,690.00 USD | 120,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 2,930.00 USD | 120,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,870.00 USD | 120,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 12,220.00 USD | 120,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 453.38 USD | 120,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 23,430.00 USD | 120,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,530.00 USD | 120,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,120.00 USD | 120,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 120,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 1,320.00 USD | 120,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 16,000.00 USD | 120,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 11,210.00 USD | 120,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 17,370.00 USD | 120,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 4,200.00 USD | 120,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 5,960.00 USD | 120,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 22,060.00 USD | 120,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,450.00 USD | 120,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 2,030.00 USD | 120,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 7,960.00 USD | 120,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 2,410.00 USD | 120,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,320.00 USD | 120,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,910.00 USD | 120,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 337.33 USD | 120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 15,400.00 USD | 120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 1,030,000.00 USD | 119,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 2,110.00 USD | 118,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 3,120.00 USD | 118,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 3,300.00 USD | 118,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 13,360.00 USD | 118,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 360.48 USD | 118,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 7,110.00 USD | 118,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 22,680.00 USD | 118,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 115,520.00 USD | 118,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 118,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 46,500.00 USD | 118,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 469,890.00 USD | 118,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 101,520.00 USD | 118,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 32,890.00 USD | 118,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 3,330.00 USD | 118,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,190.00 USD | 118,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 2,030.00 USD | 118,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 118,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 4,270.00 USD | 118,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 1,810.00 USD | 118,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 33,070.00 USD | 118,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 3,890.00 USD | 118,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,760.00 USD | 118,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 6,280.00 USD | 118,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 5,620.00 USD | 118,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,130.00 USD | 118,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,550.00 USD | 118,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 43,250.00 USD | 118,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 230.70 USD | 117,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 117,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 117,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 59,050.00 USD | 117,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 350.78 USD | 117,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 27,260.00 USD | 117,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 12,410.00 USD | 117,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 4,590.00 USD | 117,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 753.04 USD | 117,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 83,090.00 USD | 117,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,070.00 USD | 117,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 19,320.00 USD | 117,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 862,140.00 USD | 117,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 141,900.00 USD | 116,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 4,910.00 USD | 116,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 102.58 USD | 116,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 116,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,810.00 USD | 116,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 6,990.00 USD | 116,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 42,870.00 USD | 116,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 56,460.00 USD | 116,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 91,560.00 USD | 116,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 4,090.00 USD | 116,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 9,120.00 USD | 116,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 36,190.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 17,970.00 USD | 116,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 8,650.00 USD | 116,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 5,350.00 USD | 116,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 20,790.00 USD | 116,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 13,500.00 USD | 116,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 116,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 65,680.00 USD | 116,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 14,320.00 USD | 116,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 4,600.00 USD | 116,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 21,580.00 USD | 116,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 9,850.00 USD | 116,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 9,580.00 USD | 116,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 23,990.00 USD | 116,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 924.25 USD | 116,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 242.13 USD | 116,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 90,210.00 USD | 116,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 22,150.00 USD | 116,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 3,890.00 USD | 116,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 5,000.00 USD | 116,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 2,450,000.00 USD | 116,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 16,350.00 USD | 113,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 16,970.00 USD | 113,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 2,970.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 8,660.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 505.84 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 488.70 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 9,090.00 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 4,760.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 29,010.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 99,680.00 USD | 113,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,610.00 USD | 113,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 4,680.00 USD | 113,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 24,150.00 USD | 113,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 3,040.00 USD | 113,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 57,020.00 USD | 113,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 12,840.00 USD | 113,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 36,310.00 USD | 113,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 2,340.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 2,090.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 557.35 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 20,910.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 9,700.00 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,840.00 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 205,990.00 USD | 113,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 113,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 68,210.00 USD | 113,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 121,310.00 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 6,750.00 USD | 112,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 21,390.00 USD | 112,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 121.87 USD | 112,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 20,810.00 USD | 112,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 16,580.00 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 19,560.00 USD | 112,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 22,840.00 USD | 112,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 10,680.00 USD | 112,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 37,180.00 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 3,740.00 USD | 112,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 75,950.00 USD | 112,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 21,530.00 USD | 112,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 15,640.00 USD | 112,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,230.00 USD | 112,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 9,710.00 USD | 112,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 65,250.00 USD | 112,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 15,420.00 USD | 112,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 86,040.00 USD | 112,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 14,620.00 USD | 112,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.35` | 429.51 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 43,420.00 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 6,000.00 USD | 112,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 9,510.00 USD | 112,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 7,100.00 USD | 112,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 40,390.00 USD | 112,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 4,970.00 USD | 112,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.05` | 28,890.00 USD | 112,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 4,550.00 USD | 112,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 112,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 180,440.00 USD | 112,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 69,830.00 USD | 112,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 10,000.00 USD | 111,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 146.33 USD | 111,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 20,320.00 USD | 111,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 111,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 11,940.00 USD | 111,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 11,360.00 USD | 111,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 1,010.00 USD | 111,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 15,990.00 USD | 111,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 296.49 USD | 111,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 90,080.00 USD | 111,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,050.00 USD | 111,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 110,590.00 USD | 111,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 20,870.00 USD | 111,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 1,320,000.00 USD | 111,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 22,740.00 USD | 110,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 10,790.00 USD | 110,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 412,550.00 USD | 110,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 71,250.00 USD | 109,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 2,290.00 USD | 109,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 42,250.00 USD | 109,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 54,070.00 USD | 109,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 5,930.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 2,050.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 109,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 33,390.00 USD | 109,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 2,510.00 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 19,700.00 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 5,490.00 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 42,850.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 3,340,000.00 USD | 109,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 156,810.00 USD | 106,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 3,850.00 USD | 106,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 2,790.00 USD | 106,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.95` | 12,230,000.00 USD | 106,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 10,180.00 USD | 93,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 93,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,650.00 USD | 56,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 47,450.00 USD | 56,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 21,080.00 USD | 56,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 21,980.00 USD | 56,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 769,100.00 USD | 56,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 46,920.00 USD | 55,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 15,560.00 USD | 55,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 1,110,000.00 USD | 55,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 3,570.00 USD | 54,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 90,030.00 USD | 54,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 10,100.00 USD | 54,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 5,460.00 USD | 54,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 14,370.00 USD | 54,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 23,380.00 USD | 54,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 1,510.00 USD | 54,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 32,740.00 USD | 54,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 22,690.00 USD | 54,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 9,260.00 USD | 54,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 1,170.00 USD | 54,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 13,500.00 USD | 54,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 73,520.00 USD | 54,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,150,000.00 USD | 53,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 116,910.00 USD | 51,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 112,920.00 USD | 51,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 74,220.00 USD | 51,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 16,510.00 USD | 51,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 27,840.00 USD | 51,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 1,340,000.00 USD | 51,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 32,070.00 USD | 50,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 67,250.00 USD | 50,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 5,780.00 USD | 50,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 244.73 USD | 50,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 37,650.00 USD | 50,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 42,910.00 USD | 49,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 460.71 USD | 49,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 58,200.00 USD | 49,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 1,470,000.00 USD | 49,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 46,050.00 USD | 48,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 39,540.00 USD | 48,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 130,700.00 USD | 48,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 41,150.00 USD | 48,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 6,370.00 USD | 48,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 7,100.00 USD | 48,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 12,330.00 USD | 48,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 50,640.00 USD | 48,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 14,660.00 USD | 48,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 59,510.00 USD | 48,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 16,220.00 USD | 48,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 7,310.00 USD | 48,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 62,460.00 USD | 47,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 26,580.00 USD | 47,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 13,520.00 USD | 47,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 3,950.00 USD | 47,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 14,850.00 USD | 47,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 139,500.00 USD | 47,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 60,970.00 USD | 47,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 11,970.00 USD | 47,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,150.00 USD | 47,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 26,150.00 USD | 47,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 23,290.00 USD | 47,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 537,000.00 USD | 47,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 37,770.00 USD | 47,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 8,830.00 USD | 46,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 39,260.00 USD | 46,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 2,090.00 USD | 46,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 47,630.00 USD | 46,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 100,050.00 USD | 46,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 22,780.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 52,070.00 USD | 46,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 3,570.00 USD | 46,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 14,920.00 USD | 46,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 20,860.00 USD | 46,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 3,370.00 USD | 46,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 52,020.00 USD | 46,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 136,280.00 USD | 46,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 48,540.00 USD | 46,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 15,670.00 USD | 46,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 21,910.00 USD | 46,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 1,300.00 USD | 46,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,970.00 USD | 46,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 1,380.00 USD | 46,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 36,310.00 USD | 46,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 3,080.00 USD | 46,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 40,540.00 USD | 46,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 30,210.00 USD | 46,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 12,890.00 USD | 46,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 62,790.00 USD | 46,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 32,060.00 USD | 46,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 31,680.00 USD | 46,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 91,690.00 USD | 46,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 34,220.00 USD | 46,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 1,710,000.00 USD | 46,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 1,340.00 USD | 44,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 7,950.00 USD | 44,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.65` | 201,890.00 USD | 44,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 357,790.00 USD | 44,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 30,720.00 USD | 43,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 4,630.00 USD | 43,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 20,450.00 USD | 43,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 58,230.00 USD | 43,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 40,230.00 USD | 43,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 65,750.00 USD | 43,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 325,630.00 USD | 43,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 233,130.00 USD | 43,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 708.64 USD | 42,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 61,740.00 USD | 42,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 18,810.00 USD | 42,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 7,420.00 USD | 42,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 1,050.00 USD | 42,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 606,790.00 USD | 42,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 126,590.00 USD | 42,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 11,270.00 USD | 42,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 12,050.00 USD | 42,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 43,310.00 USD | 42,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 43,730.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 693.03 USD | 42,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 51,620.00 USD | 42,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 5,290.00 USD | 41,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 166.50 USD | 41,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 36,590.00 USD | 41,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 51,420.00 USD | 41,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 210,440.00 USD | 41,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 8,760.00 USD | 41,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 18,370.00 USD | 41,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 379,900.00 USD | 41,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 6,120.00 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 67,080.00 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 41,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,320,000.00 USD | 41,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 43,510.00 USD | 38,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 20,470.00 USD | 38,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 82,790.00 USD | 38,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 52,940.00 USD | 38,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 24,420.00 USD | 38,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 15,000.00 USD | 38,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 75,320.00 USD | 38,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 39,230.00 USD | 38,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 16,500.00 USD | 38,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 194,170.00 USD | 38,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 820,980.00 USD | 38,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 178,730.00 USD | 37,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 17,800.00 USD | 37,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 942,960.00 USD | 37,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 19,560.00 USD | 36,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 113,280.00 USD | 36,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 32,290.00 USD | 36,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 33,790.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 16,780.00 USD | 36,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 1,720,000.00 USD | 36,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 9,950.00 USD | 34,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 18,550.00 USD | 34,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 52,990.00 USD | 34,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 33,610.00 USD | 34,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 14,940.00 USD | 34,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 68,300.00 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 67,930.00 USD | 34,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 218,530.00 USD | 34,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 33,800.00 USD | 33,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 169,380.00 USD | 33,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 73,730.00 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 46,100.00 USD | 33,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 37,480.00 USD | 33,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 84,930.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 29,050.00 USD | 33,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 70,830.00 USD | 33,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 101,570.00 USD | 33,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 6,320.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 6,850.00 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 23,090.00 USD | 33,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 88,300.00 USD | 33,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 568,790.00 USD | 33,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 76,700.00 USD | 32,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 29,720.00 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 23,930.00 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 24,200.00 USD | 32,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 6,530.00 USD | 32,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 45,860.00 USD | 32,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 21,790.00 USD | 32,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 81,030.00 USD | 32,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 113,140.00 USD | 32,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.25` | 22,610.00 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.30` | 98,710,000.00 USD | 98,710,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.35` | 19,600.00 USD | 32,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 34,920.00 USD | 32,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.50` | 98,560,000.00 USD | 98,560,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.55` | 22,090.00 USD | 32,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.60` | 71,350,000.00 USD | 71,350,000.00 USD | 0.00 USD | 306,270.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.65` | 114,160.00 USD | 32,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 1,280,000.00 USD | 31,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.80` | 71,040,000.00 USD | 71,040,000.00 USD | 0.00 USD | 69,010.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 64,270.00 USD | 30,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.90` | 98,550,000.00 USD | 98,550,000.00 USD | 207,900.00 USD | 138,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 84,500.00 USD | 30,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.00` | 70,960,000.00 USD | 70,960,000.00 USD | 150,240.00 USD | 112,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 278,840.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.10` | 98,210,000.00 USD | 98,210,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 322,190.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.20` | 70,700,000.00 USD | 70,700,000.00 USD | 8,680.00 USD | 79,810.00 USD | 162,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 16,540.00 USD | 29,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.30` | 98,200,000.00 USD | 98,200,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 35,940.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.40` | 70,450,000.00 USD | 70,450,000.00 USD | 8,750.00 USD | 95,800.00 USD | 40,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 561,270.00 USD | 29,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.50` | 97,710,000.00 USD | 97,710,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 172,150.00 USD | 29,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.60` | 70,300,000.00 USD | 70,300,000.00 USD | 10,160.00 USD | 50,950.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 547,570.00 USD | 29,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.70` | 97,660,000.00 USD | 97,660,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 24,600.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.80` | 70,240,000.00 USD | 70,240,000.00 USD | 22,290.00 USD | 112,630.00 USD | 716,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 27,330.00 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.90` | 96,950,000.00 USD | 96,950,000.00 USD | 0.00 USD | 295,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 7,180.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.00` | 69,390,000.00 USD | 69,390,000.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 43,330.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 6,610.00 USD | 28,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 213,270.00 USD | 28,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 99,390.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 97,600.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 216,000.00 USD | 28,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.60` | 68,900,000.00 USD | 68,900,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.65` | 142,310.00 USD | 27,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.70` | 96,660,000.00 USD | 96,660,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 159,100.00 USD | 27,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 68,890,000.00 USD | 68,890,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 869,300.00 USD | 27,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.90` | 96,430,000.00 USD | 96,430,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 197,960.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 68,000,000.00 USD | 68,000,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 229,790.00 USD | 26,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.10` | 96,410,000.00 USD | 96,410,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 106,420.00 USD | 26,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 67,770,000.00 USD | 67,770,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 172,000.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.30` | 95,190,000.00 USD | 95,190,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 73,440.00 USD | 25,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 67,500,000.00 USD | 67,500,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 381,100.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.50` | 95,160,000.00 USD | 95,160,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 35,920.00 USD | 25,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 67,130,000.00 USD | 67,130,000.00 USD | 557,950.00 USD | 163,120.00 USD | 317,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 15,660.00 USD | 25,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.70` | 94,370,000.00 USD | 94,370,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 82,300.00 USD | 25,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 66,090,000.00 USD | 66,090,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 137,070.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.90` | 92,950,000.00 USD | 92,950,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 1,530,000.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 64,980,000.00 USD | 64,980,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 80,380.00 USD | 23,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.10` | 91,150,000.00 USD | 91,150,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 30,220.00 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 63,630,000.00 USD | 63,630,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 40,030.00 USD | 23,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.30` | 88,780,000.00 USD | 88,780,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 60,740.00 USD | 23,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 62,310,000.00 USD | 62,310,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 186,630.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.50` | 86,700,000.00 USD | 86,700,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 16,730.00 USD | 23,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 60,950,000.00 USD | 60,950,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 86,440.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.70` | 84,020,000.00 USD | 84,020,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 318,210.00 USD | 23,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 59,810,000.00 USD | 59,810,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 79,380.00 USD | 22,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.90` | 81,570,000.00 USD | 81,570,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 55,040.00 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 59,600,000.00 USD | 59,600,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 795,510.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.10` | 79,190,000.00 USD | 79,190,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 268,870.00 USD | 21,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 59,410,000.00 USD | 59,410,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 14,410.00 USD | 21,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.30` | 77,280,000.00 USD | 77,280,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 52,380.00 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 59,390,000.00 USD | 59,390,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 34,730.00 USD | 21,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.50` | 74,780,000.00 USD | 74,780,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 3,660,000.00 USD | 21,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 59,210,000.00 USD | 59,210,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 100,830.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.70` | 71,870,000.00 USD | 71,870,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 369,520.00 USD | 17,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 59,090,000.00 USD | 59,090,000.00 USD | 250,490.00 USD | 103,030.00 USD | 525,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 33,220.00 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.90` | 70,230,000.00 USD | 70,230,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 135,060.00 USD | 17,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 58,210,000.00 USD | 58,210,000.00 USD | 38,300.00 USD | 274,720.00 USD | 87,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 26,270.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.10` | 67,820,000.00 USD | 67,820,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 282,170.00 USD | 17,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 57,810,000.00 USD | 57,810,000.00 USD | 63,310.00 USD | 149,590.00 USD | 43,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 63,300.00 USD | 16,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.30` | 66,120,000.00 USD | 66,120,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 63,890.00 USD | 16,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 57,550,000.00 USD | 57,550,000.00 USD | 111,190.00 USD | 824,620.00 USD | 877,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 266,080.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.50` | 63,770,000.00 USD | 63,770,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 231,210.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 55,740,000.00 USD | 55,740,000.00 USD | 355,570.00 USD | 341,420.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 457,210.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.70` | 62,000,000.00 USD | 62,000,000.00 USD | 671,470.00 USD | 168,780.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 451,380.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 55,030,000.00 USD | 55,030,000.00 USD | 26,180.00 USD | 406,530.00 USD | 166,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 573,950.00 USD | 15,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.90` | 61,090,000.00 USD | 61,090,000.00 USD | 0.00 USD | 74,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 95,470.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.00` | 54,430,000.00 USD | 54,430,000.00 USD | 21,710.00 USD | 199,520.00 USD | 406,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 70,070.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.10` | 61,010,000.00 USD | 61,010,000.00 USD | 31,020.00 USD | 630,650.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 102,340.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.20` | 53,800,000.00 USD | 53,800,000.00 USD | 32,310.00 USD | 398,190.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 103,200.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.30` | 59,350,000.00 USD | 59,350,000.00 USD | 145,070.00 USD | 66,280.00 USD | 468,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 198,270.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.40` | 53,270,000.00 USD | 53,270,000.00 USD | 57,590.00 USD | 433,830.00 USD | 141,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 554,280.00 USD | 14,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.50` | 58,670,000.00 USD | 58,670,000.00 USD | 93,960.00 USD | 1,260,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 439,100.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.60` | 52,640,000.00 USD | 52,640,000.00 USD | 64,480.00 USD | 472,950.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 369,230.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.70` | 55,870,000.00 USD | 55,870,000.00 USD | 270,240.00 USD | 954,120.00 USD | 120,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 138,540.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.80` | 50,320,000.00 USD | 50,320,000.00 USD | 63,080.00 USD | 1,320,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 558,560.00 USD | 12,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.90` | 54,530,000.00 USD | 54,530,000.00 USD | 168,420.00 USD | 56,340.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 377,350.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.00` | 47,160,000.00 USD | 47,160,000.00 USD | 60,590.00 USD | 86,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 240,430.00 USD | 11,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.10` | 54,280,000.00 USD | 54,280,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 198,390.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.20` | 47,010,000.00 USD | 47,010,000.00 USD | 0.00 USD | 691,260.00 USD | 702,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 33,840.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.30` | 52,700,000.00 USD | 52,700,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 205,690.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.40` | 45,620,000.00 USD | 45,620,000.00 USD | 33,670.00 USD | 1,130,000.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 991,720.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.50` | 51,980,000.00 USD | 51,980,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 305,740.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 44,440,000.00 USD | 44,440,000.00 USD | 784,790.00 USD | 597,770.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 8,570,000.00 USD | 9,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.70` | 50,900,000.00 USD | 50,900,000.00 USD | 1,600,000.00 USD | 238,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 133,210.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.80` | 40,970,000.00 USD | 40,970,000.00 USD | 762,670.00 USD | 2,150,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 366,250.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.90` | 49,060,000.00 USD | 49,060,000.00 USD | 1,100,000.00 USD | 2,260,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 432,730.00 USD | 836,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.00` | 36,880,000.00 USD | 36,880,000.00 USD | 562,710.00 USD | 1,120,000.00 USD | 816,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 56,670.00 USD | 403,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.10` | 45,700,000.00 USD | 45,700,000.00 USD | 198,380.00 USD | 1,270,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 139,650.00 USD | 346,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.20` | 34,390,000.00 USD | 34,390,000.00 USD | 99,290.00 USD | 4,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 158,140.00 USD | 207,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.30` | 41,460,000.00 USD | 41,460,000.00 USD | 678,330.00 USD | 445,310.00 USD | 838,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 33,720.00 USD | 48,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.40` | 28,620,000.00 USD | 28,620,000.00 USD | 378,280.00 USD | 1,650,000.00 USD | 294,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 7,630.00 USD | 15,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.50` | 39,490,000.00 USD | 39,490,000.00 USD | 1,200,000.00 USD | 3,810,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 3,280.00 USD | 7,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 26,300,000.00 USD | 26,300,000.00 USD | 2,740,000.00 USD | 1,490,000.00 USD | 3,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 31,610,000.00 USD | 31,610,000.00 USD | 4,060,000.00 USD | 1,480,000.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.80` | 18,180,000.00 USD | 18,180,000.00 USD | 1,750,000.00 USD | 1,250,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 4,030.00 USD | 4,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.90` | 26,060,000.00 USD | 26,060,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.00` | 13,250,000.00 USD | 13,250,000.00 USD | 1,610,000.00 USD | 1,880,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 23,930,000.00 USD | 23,930,000.00 USD | 3,460,000.00 USD | 2,050,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.20` | 8,220,000.00 USD | 8,220,000.00 USD | 1,350,000.00 USD | 847,400.00 USD | 498,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 13,900,000.00 USD | 13,900,000.00 USD | 1,030,000.00 USD | 2,320,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.35` | 290.98 USD | 290.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.40` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 2,050,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.60` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.60` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.80` | 6,960,000.00 USD | 6,960,000.00 USD | 53,180.00 USD | 3,360,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.00` | 8,280,000.00 USD | 8,280,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.15` | 1,260.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.20` | 8,560,000.00 USD | 8,560,000.00 USD | 286,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.30` | 5,720,000.00 USD | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.35` | 19,660.00 USD | 20,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.40` | 9,250,000.00 USD | 9,250,000.00 USD | 690,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.50` | 12,360,000.00 USD | 12,360,000.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.55` | 1,010.00 USD | 21,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.60` | 14,720,000.00 USD | 14,720,000.00 USD | 5,180,000.00 USD | 0.00 USD | 277,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.70` | 19,680,000.00 USD | 19,680,000.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.80` | 20,390,000.00 USD | 20,390,000.00 USD | 5,150,000.00 USD | 39,060.00 USD | 488,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 45,230,000.00 USD | 45,230,000.00 USD | 11,920,000.00 USD | 5,860,000.00 USD | 7,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.00` | 35,060,000.00 USD | 35,060,000.00 USD | 6,070,000.00 USD | 2,650,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.10` | 80,140,000.00 USD | 80,140,000.00 USD | 9,820,000.00 USD | 9,540,000.00 USD | 15,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.20` | 46,000,000.00 USD | 46,000,000.00 USD | 4,100,000.00 USD | 3,690,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.30` | 96,710,000.00 USD | 96,710,000.00 USD | 43,030.00 USD | 6,830,000.00 USD | 9,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.40` | 59,510,000.00 USD | 59,510,000.00 USD | 2,290,000.00 USD | 2,630,000.00 USD | 8,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.50` | 102,860,000.00 USD | 102,860,000.00 USD | 1,040,000.00 USD | 5,110,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 604.11 USD | 22,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.60` | 67,470,000.00 USD | 67,470,000.00 USD | 52,360.00 USD | 2,590,000.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.70` | 102,890,000.00 USD | 102,890,000.00 USD | 0.00 USD | 28,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.80` | 74,180,000.00 USD | 74,180,000.00 USD | 43,420.00 USD | 2,900,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.85` | 2,190.00 USD | 24,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.90` | 105,430,000.00 USD | 105,430,000.00 USD | 57,310.00 USD | 1,040,000.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `99.00` | 75,550,000.00 USD | 75,550,000.00 USD | 64,620.00 USD | 1,100,000.00 USD | 202,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 2,350.00 USD | 27,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.10` | 106,570,000.00 USD | 106,570,000.00 USD | 179,190.00 USD | 124,230.00 USD | 838,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 185,850.00 USD | 212,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 80,410,000.00 USD | 80,410,000.00 USD | 115,180.00 USD | 867,660.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 57,360.00 USD | 270,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.30` | 111,700,000.00 USD | 111,700,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 65,580.00 USD | 335,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 85,250,000.00 USD | 85,250,000.00 USD | 2,860,000.00 USD | 509,170.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 42,320.00 USD | 378,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.50` | 115,440,000.00 USD | 115,440,000.00 USD | 2,240,000.00 USD | 1,480,000.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 508.70 USD | 378,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 99,250,000.00 USD | 99,250,000.00 USD | 1,520,000.00 USD | 5,710,000.00 USD | 6,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 17,170.00 USD | 395,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.70` | 117,450,000.00 USD | 117,450,000.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 165,500.00 USD | 561,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 112,150,000.00 USD | 112,150,000.00 USD | 2,250,000.00 USD | 3,870,000.00 USD | 6,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 34,420.00 USD | 595,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.90` | 124,600,000.00 USD | 124,600,000.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 422,380.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.00` | 117,630,000.00 USD | 117,630,000.00 USD | 2,080,000.00 USD | 1,770,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 7,120.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.10` | 127,990,000.00 USD | 127,990,000.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 18,360.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 118,490,000.00 USD | 118,490,000.00 USD | 16,830.00 USD | 838,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.30` | 130,840,000.00 USD | 130,840,000.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 799.79 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.40` | 122,250,000.00 USD | 122,250,000.00 USD | 355,570.00 USD | 767,780.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 137,780,000.00 USD | 137,780,000.00 USD | 2,500,000.00 USD | 128,740.00 USD | 4,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.60` | 131,650,000.00 USD | 131,650,000.00 USD | 1,990,000.00 USD | 1,190,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 1,680.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.70` | 139,160,000.00 USD | 139,160,000.00 USD | 133,340.00 USD | 1,240,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 31,580.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.80` | 136,350,000.00 USD | 136,350,000.00 USD | 1,520,000.00 USD | 1,690,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 1,060,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.90` | 152,250,000.00 USD | 152,250,000.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 6,290.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.00` | 147,750,000.00 USD | 147,750,000.00 USD | 7,810,000.00 USD | 2,650,000.00 USD | 935,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 20,440.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.10` | 162,020,000.00 USD | 162,020,000.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 18,750.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.20` | 164,060,000.00 USD | 164,060,000.00 USD | 5,230,000.00 USD | 6,870,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 1,210.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.30` | 182,590,000.00 USD | 182,590,000.00 USD | 7,310,000.00 USD | 4,280,000.00 USD | 8,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.35` | 51,620.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.40` | 173,970,000.00 USD | 173,970,000.00 USD | 3,450,000.00 USD | 2,420,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.50` | 197,860,000.00 USD | 197,860,000.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 814.43 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 194,780,000.00 USD | 194,780,000.00 USD | 4,700,000.00 USD | 3,450,000.00 USD | 12,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 1,820.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.70` | 207,210,000.00 USD | 207,210,000.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.80` | 201,070,000.00 USD | 201,070,000.00 USD | 483,810.00 USD | 381,190.00 USD | 5,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 215,210,000.00 USD | 215,210,000.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 205,460,000.00 USD | 205,460,000.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,690.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.10` | 219,850,000.00 USD | 219,850,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 212,300,000.00 USD | 212,300,000.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 225,900,000.00 USD | 225,900,000.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.35` | 6,240.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.40` | 216,880,000.00 USD | 216,880,000.00 USD | 1,430,000.00 USD | 579,100.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.45` | 421.07 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.50` | 229,560,000.00 USD | 229,560,000.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.60` | 219,520,000.00 USD | 219,520,000.00 USD | 978,360.00 USD | 625,050.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 872.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.70` | 230,330,000.00 USD | 230,330,000.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.80` | 223,980,000.00 USD | 223,980,000.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 251,620,000.00 USD | 251,620,000.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 3,080.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 229,240,000.00 USD | 229,240,000.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 2,980.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.10` | 257,830,000.00 USD | 257,830,000.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 232,840,000.00 USD | 232,840,000.00 USD | 585,300.00 USD | 1,180,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 9,960.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.30` | 275,400,000.00 USD | 275,400,000.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 530.19 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 237,950,000.00 USD | 237,950,000.00 USD | 2,140,000.00 USD | 1,620,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 297,800,000.00 USD | 297,800,000.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 2,680.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 248,510,000.00 USD | 248,510,000.00 USD | 3,310,000.00 USD | 1,240,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 1,040.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.70` | 310,030,000.00 USD | 310,030,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 4,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 255,310,000.00 USD | 255,310,000.00 USD | 2,280,000.00 USD | 2,510,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 14,170.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.90` | 328,060,000.00 USD | 328,060,000.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.95` | 8,540.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.00` | 264,860,000.00 USD | 264,860,000.00 USD | 3,550,000.00 USD | 2,790,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 877.14 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.10` | 356,790,000.00 USD | 356,790,000.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,060.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 270,590,000.00 USD | 270,590,000.00 USD | 2,070,000.00 USD | 1,830,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 37,460.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.30` | 378,170,000.00 USD | 378,170,000.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 3,740.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.40` | 276,580,000.00 USD | 276,580,000.00 USD | 2,370,000.00 USD | 1,790,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 7,090.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.50` | 390,170,000.00 USD | 390,170,000.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 11,290.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 281,500,000.00 USD | 281,500,000.00 USD | 1,430,000.00 USD | 963,940.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 632,260.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.70` | 410,170,000.00 USD | 410,170,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 285,300,000.00 USD | 285,300,000.00 USD | 948,860.00 USD | 905,680.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 430,770,000.00 USD | 430,770,000.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 50,510.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 286,490,000.00 USD | 286,490,000.00 USD | 487,580.00 USD | 351,350.00 USD | 350,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 1,200.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.10` | 443,980,000.00 USD | 443,980,000.00 USD | 5,580,000.00 USD | 4,800,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.20` | 287,750,000.00 USD | 287,750,000.00 USD | 237,100.00 USD | 4,110.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,300.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.30` | 448,980,000.00 USD | 448,980,000.00 USD | 2,740,000.00 USD | 1,820,000.00 USD | 428,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 4,800.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 287,920,000.00 USD | 287,920,000.00 USD | 84,970.00 USD | 88,270.00 USD | 769.33 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 636,160.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.50` | 468,490,000.00 USD | 468,490,000.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 6,290.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 288,500,000.00 USD | 288,500,000.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 1,060.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.70` | 482,660,000.00 USD | 482,660,000.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 289,240,000.00 USD | 289,240,000.00 USD | 132,310.00 USD | 591,910.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.90` | 492,550,000.00 USD | 492,550,000.00 USD | 3,680,000.00 USD | 1,870,000.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 266.99 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 290,370,000.00 USD | 290,370,000.00 USD | 377,210.00 USD | 525,540.00 USD | 226,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 1,420.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.10` | 504,690,000.00 USD | 504,690,000.00 USD | 6,090,000.00 USD | 3,080,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.15` | 4,350.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.20` | 291,700,000.00 USD | 291,700,000.00 USD | 614,770.00 USD | 344,210.00 USD | 367,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.25` | 819.19 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.30` | 514,650,000.00 USD | 514,650,000.00 USD | 4,750,000.00 USD | 2,990,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 53,990.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.40` | 292,380,000.00 USD | 292,380,000.00 USD | 233,950.00 USD | 319,460.00 USD | 125,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 6,370.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.50` | 519,890,000.00 USD | 519,890,000.00 USD | 1,700,000.00 USD | 1,650,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.60` | 294,140,000.00 USD | 294,140,000.00 USD | 399,220.00 USD | 321,480.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.70` | 529,510,000.00 USD | 529,510,000.00 USD | 2,280,000.00 USD | 2,870,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 295,290,000.00 USD | 295,290,000.00 USD | 319,360.00 USD | 179,630.00 USD | 649,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 478,970.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.90` | 535,340,000.00 USD | 535,340,000.00 USD | 1,220,000.00 USD | 1,150,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 291.97 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 295,650,000.00 USD | 295,650,000.00 USD | 98,730.00 USD | 169,460.00 USD | 95,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 15,740.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.10` | 539,450,000.00 USD | 539,450,000.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.20` | 296,140,000.00 USD | 296,140,000.00 USD | 0.00 USD | 49,040.00 USD | 436,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 36,010.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.30` | 539,900,000.00 USD | 539,900,000.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 197,950.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 296,750,000.00 USD | 296,750,000.00 USD | 22,290.00 USD | 63,590.00 USD | 523,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 53,960.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.50` | 540,880,000.00 USD | 540,880,000.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.60` | 297,230,000.00 USD | 297,230,000.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,820.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.70` | 541,850,000.00 USD | 541,850,000.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.75` | 5,840.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.85` | 106.77 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.90` | 542,020,000.00 USD | 542,020,000.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.10` | 542,630,000.00 USD | 542,630,000.00 USD | 249,450.00 USD | 347,250.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.30` | 544,780,000.00 USD | 544,780,000.00 USD | 964,640.00 USD | 578,980.00 USD | 612,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.35` | 13,880.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.45` | 119,130.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.50` | 545,820,000.00 USD | 545,820,000.00 USD | 867,380.00 USD | 157,660.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 548,060,000.00 USD | 548,060,000.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.75` | 188.14 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.90` | 550,100,000.00 USD | 550,100,000.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,740.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.10` | 551,190,000.00 USD | 551,190,000.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.15` | 22,380.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 1,070.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.30` | 552,350,000.00 USD | 552,350,000.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.35` | 247.13 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 105,660.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.50` | 552,590,000.00 USD | 552,590,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.55` | 461.21 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 42,990.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.70` | 553,770,000.00 USD | 553,770,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.75` | 256.81 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 572.32 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.90` | 555,570,000.00 USD | 555,570,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.95` | 537.66 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.10` | 557,940,000.00 USD | 557,940,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 218.29 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.30` | 560,020,000.00 USD | 560,020,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.35` | 534,860.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 16,940.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.50` | 560,500,000.00 USD | 560,500,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 112.86 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.70` | 562,710,000.00 USD | 562,710,000.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.75` | 575.90 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 103.09 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.90` | 565,150,000.00 USD | 565,150,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.95` | 12,860.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.05` | 8,630.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.10` | 567,540,000.00 USD | 567,540,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.25` | 196.91 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.30` | 569,440,000.00 USD | 569,440,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.50` | 571,950,000.00 USD | 571,950,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.55` | 2,780.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.70` | 573,090,000.00 USD | 573,090,000.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.75` | 339.72 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.90` | 574,860,000.00 USD | 574,860,000.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.95` | 895.60 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.05` | 626.36 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.10` | 576,490,000.00 USD | 576,490,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.30` | 578,900,000.00 USD | 578,900,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,910.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.50` | 580,210,000.00 USD | 580,210,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 584.65 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.70` | 580,740,000.00 USD | 580,740,000.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 1,460.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.90` | 582,230,000.00 USD | 582,230,000.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.05` | 263,100.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.10` | 583,620,000.00 USD | 583,620,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 114.38 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.30` | 583,890,000.00 USD | 583,890,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.45` | 104,430.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.50` | 583,950,000.00 USD | 583,950,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.55` | 515,190.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 3,220.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.70` | 584,350,000.00 USD | 584,350,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.75` | 22,100.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.90` | 584,400,000.00 USD | 584,400,000.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.95` | 22,160.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 21,420.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.10` | 584,460,000.00 USD | 584,460,000.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.15` | 2,820.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.30` | 584,690,000.00 USD | 584,690,000.00 USD | 93,960.00 USD | 135,190.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `114.40` | 585,020,000.00 USD | 585,020,000.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,050.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.95` | 496.58 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 7,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 2,360.00 USD | 7,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 18,240.00 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 5,850.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 879,040.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 61,070.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.45` | 716.17 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,780.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.75` | 31,740.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 23,970.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 230.01 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.45` | 128.02 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 4,650,000.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 353.85 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 966.63 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 85,100.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 4,280,000.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 6,180.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 2,980.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.35` | 145.62 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 93,000.00 USD | 17,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 12,790.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 1,570.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 12,720.00 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 414.68 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 6,220.00 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.65` | 16,300.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 15,610.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,200.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 17,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 17,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.85` | 14,930,000.00 USD | 32,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 2,790.00 USD | 32,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 32,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 124,510.00 USD | 32,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.55` | 3,430.00 USD | 32,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.75` | 55,610.00 USD | 32,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 32,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 17,600.00 USD | 32,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 859,810.00 USD | 33,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 33,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 5,920.00 USD | 33,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 33,830.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.25` | 2,420.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,910.00 USD | 33,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 46,480.00 USD | 33,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 33,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 12,690.00 USD | 33,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 33,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 33,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 33,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 506.66 USD | 33,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 32,990.00 USD | 33,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.75` | 6,420.00 USD | 33,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 4,260.00 USD | 33,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.95` | 9,460.00 USD | 33,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 4,280.00 USD | 33,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 33,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.55` | 128.83 USD | 33,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 33,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 256,560.00 USD | 33,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 33,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,200.00 USD | 34,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.15` | 3,350.00 USD | 34,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 34,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.45` | 271.03 USD | 34,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 34,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 714,710.00 USD | 34,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 44,790.00 USD | 34,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,480.00 USD | 34,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 56,180.00 USD | 34,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 67,370.00 USD | 34,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 34,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 6,660.00 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.55` | 195.83 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 503,820.00 USD | 35,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 14,890.00 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.35` | 855.09 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 5,540.00 USD | 35,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 35,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.35` | 4,630.00 USD | 35,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.45` | 8,530.00 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 695.89 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.75` | 2,580.00 USD | 35,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 51,560.00 USD | 35,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.95` | 3,630.00 USD | 35,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 16,530.00 USD | 35,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.55` | 186.97 USD | 35,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 35,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 35,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.85` | 12,740.00 USD | 35,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 35,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 8,290.00 USD | 35,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.15` | 30,190.00 USD | 35,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 59,870.00 USD | 35,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.05` | 181,050.00 USD | 36,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.25` | 4,050.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.85` | 204,950.00 USD | 36,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 36,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 25,200.00 USD | 36,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.25` | 83,240.00 USD | 36,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.95` | 538,000.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 41,450.00 USD | 36,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 36,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.35` | 5,170,000.00 USD | 42,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,080,000.00 USD | 44,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.85` | 14,930.00 USD | 44,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.95` | 4,420.00 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.05` | 620.16 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 253.62 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 769.47 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 85,850.00 USD | 44,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 44,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 8,030.00 USD | 44,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 1,130.00 USD | 44,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,070,000.00 USD | 45,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 125.53 USD | 45,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.25` | 1,330.00 USD | 45,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 45,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 248,810.00 USD | 45,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 45,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 2,140.00 USD | 45,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 862,970.00 USD | 46,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 80,180.00 USD | 46,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.35` | 1,640.00 USD | 46,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 776.35 USD | 46,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 2,450.00 USD | 46,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,330.00 USD | 46,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.25` | 840,780.00 USD | 47,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 47,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 47,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.25` | 13,110.00 USD | 47,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 47,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.85` | 52,050.00 USD | 47,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.05` | 435,640.00 USD | 48,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 48,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 3,720.00 USD | 48,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 48,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 2,220.00 USD | 48,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 89,860.00 USD | 48,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 3,940.00 USD | 48,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 48,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 48,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.85` | 77,890.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,070.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 2,290.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 312.59 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.75` | 211.28 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 300.14 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 5,730.00 USD | 48,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 2,110.00 USD | 48,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 49,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 1,530.00 USD | 49,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 91,450.00 USD | 49,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.95` | 1,390,000.00 USD | 50,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 160,350.00 USD | 50,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 50,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 50,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 29,270.00 USD | 50,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 1,120,000.00 USD | 51,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.25` | 345.57 USD | 51,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.35` | 17,270.00 USD | 51,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.45` | 4,560,000.00 USD | 56,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.55` | 109,920.00 USD | 56,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.85` | 39,610.00 USD | 56,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 2,540.00 USD | 56,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 56,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 56,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 2,320.00 USD | 56,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 22,220.00 USD | 56,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 200.97 USD | 56,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 286,550.00 USD | 57,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 57,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 426,020.00 USD | 57,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 3,750.00 USD | 57,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.95` | 40,230.00 USD | 57,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 17,750.00 USD | 57,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 119,730.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 57,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 43,540.00 USD | 57,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 57,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 57,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.35` | 362.72 USD | 57,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 57,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.65` | 43,580.00 USD | 57,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 232,580.00 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.45` | 324.89 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.65` | 113.62 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.75` | 99,200.00 USD | 58,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.95` | 7,800.00 USD | 58,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.25` | 295.31 USD | 58,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 3,320.00 USD | 58,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 1,770.00 USD | 58,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.85` | 156,850.00 USD | 58,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.95` | 113,950.00 USD | 58,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 58,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.25` | 190.27 USD | 58,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.45` | 1,470.00 USD | 58,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 58,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 58,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.95` | 28,000.00 USD | 58,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.25` | 120.27 USD | 58,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.75` | 79,380.00 USD | 58,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.85` | 2,870.00 USD | 58,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 44,690.00 USD | 58,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 495.89 USD | 58,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.55` | 85,000.00 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 300.52 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 722,570.00 USD | 59,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 1,340.00 USD | 59,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.55` | 436.70 USD | 59,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.85` | 641.79 USD | 59,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 59,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.25` | 18,880.00 USD | 59,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 59,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 1,600.00 USD | 59,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 468,510.00 USD | 59,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.15` | 1,340.00 USD | 59,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.35` | 668.10 USD | 59,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 59,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 16,950.00 USD | 59,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.05` | 144,260.00 USD | 60,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.45` | 822.25 USD | 60,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.55` | 16,450.00 USD | 60,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.75` | 207,840.00 USD | 60,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.05` | 72,620.00 USD | 60,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 60,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.45` | 18,710.00 USD | 60,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 60,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.55` | 3,440.00 USD | 60,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 67,790.00 USD | 60,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.95` | 27,870.00 USD | 60,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 2,770.00 USD | 60,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 5,130.00 USD | 60,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.95` | 122.60 USD | 60,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 60,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 60,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.75` | 151.88 USD | 60,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.85` | 1,160.00 USD | 60,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.65` | 366.44 USD | 60,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.05` | 34,990.00 USD | 60,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.35` | 119,250.00 USD | 61,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 61,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.65` | 182,260.00 USD | 61,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.85` | 859,250.00 USD | 62,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.35` | 210.27 USD | 62,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 62,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.65` | 481.69 USD | 62,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.05` | 1,010,000.00 USD | 63,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.25` | 6,180,000.00 USD | 69,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 69,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 69,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.95` | 104,370.00 USD | 69,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 104,430.00 USD | 69,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 69,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 70,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.45` | 697.80 USD | 70,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.55` | 38,410,000.00 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.85` | 1,290.00 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.95` | 654.31 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.05` | 388.61 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.25` | 13,140.00 USD | 108,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.35` | 141,620.00 USD | 108,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 108,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 108,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.55` | 95,510.00 USD | 108,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.85` | 48,790.00 USD | 108,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.05` | 354,860.00 USD | 109,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 109,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.25` | 1,610.00 USD | 109,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.95` | 160,380.00 USD | 109,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.25` | 268,880.00 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.35` | 11,060.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.55` | 1,350.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.75` | 154.59 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.45` | 5,000.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.75` | 146.41 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.05` | 1,900.00 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.45` | 18,140.00 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.75` | 36,350.00 USD | 109,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.45` | 2,060.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.85` | 618.03 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.15` | 52,620.00 USD | 109,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.35` | 7,600.00 USD | 109,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.65` | 9,500.00 USD | 109,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,950.00 USD | 109,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.45` | 968,240.00 USD | 110,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.75` | 214,100.00 USD | 110,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 111,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 111,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 111,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 246.78 USD | 111,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 111,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.05` | 2,090.00 USD | 111,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.35` | 987.66 USD | 111,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.95` | 286.03 USD | 111,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.15` | 232.07 USD | 111,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 111,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.25` | 5,340.00 USD | 111,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.35` | 2,700.00 USD | 111,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.45` | 12,740.00 USD | 111,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 111,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.85` | 283,200.00 USD | 111,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 111,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 838.38 USD | 111,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 111,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.05` | 117.83 USD | 111,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 1,480.00 USD | 111,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.55` | 381,100.00 USD | 112,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.65` | 62,550.00 USD | 112,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 125,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.25` | 175.95 USD | 125,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.55` | 2,910.00 USD | 125,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.65` | 505.96 USD | 125,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.85` | 1,370.00 USD | 125,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 125,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.95` | 246.98 USD | 125,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 5,770.00 USD | 125,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.35` | 378.97 USD | 125,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 125,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.65` | 542.22 USD | 125,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.35` | 141,290,000.00 USD | 0.00 USD | 43,020.00 USD | `-80.05%` | `2,223.50` |
| `Live` | `Long` | `19.45` | 141,250,000.00 USD | 0.00 USD | 2,520.00 USD | `-79.95%` | `129.70` |
| `Live` | `Long` | `19.65` | 141,240,000.00 USD | 0.00 USD | 489.48 USD | `-79.74%` | `24.91` |
| `Live` | `Long` | `19.75` | 141,240,000.00 USD | 0.00 USD | 12,740.00 USD | `-79.64%` | `645.00` |
| `Live` | `Long` | `20.15` | 141,230,000.00 USD | 0.00 USD | 1,700.00 USD | `-79.23%` | `84.16` |
| `Live` | `Long` | `20.25` | 141,230,000.00 USD | 0.00 USD | 730,740.00 USD | `-79.12%` | `36,085.73` |
| `Live` | `Long` | `20.45` | 140,500,000.00 USD | 0.00 USD | 4,090.00 USD | `-78.92%` | `200.00` |
| `Live` | `Long` | `20.55` | 140,490,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.81%` | `233.31` |
| `Live` | `Long` | `20.75` | 140,490,000.00 USD | 0.00 USD | 158.53 USD | `-78.61%` | `7.64` |
| `Live` | `Long` | `20.95` | 140,490,000.00 USD | 0.00 USD | 344.42 USD | `-78.40%` | `16.44` |
| `Live` | `Long` | `21.05` | 140,490,000.00 USD | 0.00 USD | 7,580.00 USD | `-78.30%` | `360.00` |
| `Live` | `Long` | `21.15` | 140,480,000.00 USD | 0.00 USD | 186.97 USD | `-78.20%` | `8.84` |
| `Live` | `Long` | `21.25` | 140,480,000.00 USD | 0.00 USD | 4,730.00 USD | `-78.09%` | `222.77` |
| `Live` | `Long` | `21.35` | 140,480,000.00 USD | 0.00 USD | 1,410.00 USD | `-77.99%` | `65.89` |
| `Live` | `Long` | `21.45` | 140,480,000.00 USD | 0.00 USD | 1,860.00 USD | `-77.89%` | `86.80` |
| `Live` | `Long` | `21.55` | 140,470,000.00 USD | 0.00 USD | 102.58 USD | `-77.78%` | `4.76` |
| `Live` | `Long` | `21.65` | 140,470,000.00 USD | 0.00 USD | 107.17 USD | `-77.68%` | `4.95` |
| `Live` | `Long` | `21.75` | 140,470,000.00 USD | 0.00 USD | 10,570.00 USD | `-77.58%` | `485.78` |
| `Live` | `Long` | `21.85` | 140,460,000.00 USD | 0.00 USD | 9,140.00 USD | `-77.47%` | `418.27` |
| `Live` | `Long` | `22.05` | 140,450,000.00 USD | 0.00 USD | 131.20 USD | `-77.27%` | `5.95` |
| `Live` | `Long` | `22.35` | 140,450,000.00 USD | 0.00 USD | 1,120.00 USD | `-76.96%` | `50.00` |
| `Live` | `Long` | `22.95` | 140,450,000.00 USD | 0.00 USD | 9,200.00 USD | `-76.34%` | `400.93` |
| `Live` | `Long` | `23.35` | 140,440,000.00 USD | 0.00 USD | 836.16 USD | `-75.93%` | `35.81` |
| `Live` | `Long` | `23.45` | 140,440,000.00 USD | 0.00 USD | 10,030.00 USD | `-75.82%` | `427.86` |
| `Live` | `Long` | `23.75` | 140,430,000.00 USD | 0.00 USD | 2,140.00 USD | `-75.51%` | `90.00` |
| `Live` | `Long` | `23.95` | 140,430,000.00 USD | 0.00 USD | 230.88 USD | `-75.31%` | `9.64` |
| `Live` | `Long` | `24.05` | 140,430,000.00 USD | 0.00 USD | 721.50 USD | `-75.21%` | `30.00` |
| `Live` | `Long` | `24.45` | 140,430,000.00 USD | 0.00 USD | 1,220.00 USD | `-74.79%` | `50.00` |
| `Live` | `Long` | `24.55` | 140,430,000.00 USD | 0.00 USD | 1,500.00 USD | `-74.69%` | `61.19` |
| `Live` | `Long` | `24.65` | 140,430,000.00 USD | 0.00 USD | 252.91 USD | `-74.59%` | `10.26` |
| `Live` | `Long` | `24.95` | 140,430,000.00 USD | 0.00 USD | 222,930.00 USD | `-74.28%` | `8,935.11` |
| `Live` | `Long` | `25.05` | 140,200,000.00 USD | 0.00 USD | 2,460.00 USD | `-74.17%` | `98.08` |
| `Live` | `Long` | `25.15` | 140,200,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.07%` | `80.00` |
| `Live` | `Long` | `25.25` | 140,200,000.00 USD | 0.00 USD | 37,080.00 USD | `-73.97%` | `1,468.70` |
| `Live` | `Long` | `25.45` | 140,160,000.00 USD | 0.00 USD | 106.64 USD | `-73.76%` | `4.19` |
| `Live` | `Long` | `25.65` | 140,160,000.00 USD | 0.00 USD | 526.85 USD | `-73.56%` | `20.54` |
| `Live` | `Long` | `25.85` | 140,160,000.00 USD | 0.00 USD | 408.43 USD | `-73.35%` | `15.80` |
| `Live` | `Long` | `25.95` | 140,160,000.00 USD | 0.00 USD | 4,050.00 USD | `-73.25%` | `156.06` |
| `Live` | `Long` | `26.05` | 140,160,000.00 USD | 0.00 USD | 2,010.00 USD | `-73.14%` | `77.00` |
| `Live` | `Long` | `26.15` | 140,150,000.00 USD | 0.00 USD | 1,310.00 USD | `-73.04%` | `50.00` |
| `Live` | `Long` | `26.25` | 140,150,000.00 USD | 0.00 USD | 136.24 USD | `-72.94%` | `5.19` |
| `Live` | `Long` | `26.35` | 140,150,000.00 USD | 0.00 USD | 5,970.00 USD | `-72.83%` | `226.66` |
| `Live` | `Long` | `26.65` | 140,150,000.00 USD | 0.00 USD | 102.60 USD | `-72.53%` | `3.85` |
| `Live` | `Long` | `26.95` | 140,150,000.00 USD | 0.00 USD | 30,230.00 USD | `-72.22%` | `1,121.64` |
| `Live` | `Long` | `27.15` | 140,120,000.00 USD | 0.00 USD | 131.41 USD | `-72.01%` | `4.84` |
| `Live` | `Long` | `27.25` | 140,120,000.00 USD | 0.00 USD | 166.22 USD | `-71.91%` | `6.10` |
| `Live` | `Long` | `27.35` | 140,120,000.00 USD | 0.00 USD | 332.30 USD | `-71.80%` | `12.15` |
| `Live` | `Long` | `27.65` | 140,120,000.00 USD | 0.00 USD | 244.98 USD | `-71.49%` | `8.86` |
| `Live` | `Long` | `27.75` | 140,120,000.00 USD | 0.00 USD | 4,610.00 USD | `-71.39%` | `166.22` |
| `Live` | `Long` | `27.85` | 140,110,000.00 USD | 0.00 USD | 412.18 USD | `-71.29%` | `14.80` |
| `Live` | `Long` | `28.05` | 140,110,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.08%` | `97.63` |
| `Live` | `Long` | `28.15` | 140,110,000.00 USD | 0.00 USD | 28,150.00 USD | `-70.98%` | `1,000.00` |
| `Live` | `Long` | `28.25` | 140,080,000.00 USD | 0.00 USD | 42,520.00 USD | `-70.88%` | `1,505.14` |
| `Live` | `Long` | `28.35` | 140,040,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.77%` | `218.55` |
| `Live` | `Long` | `28.45` | 140,030,000.00 USD | 0.00 USD | 113.80 USD | `-70.67%` | `4.00` |
| `Live` | `Long` | `28.55` | 140,030,000.00 USD | 0.00 USD | 935.01 USD | `-70.57%` | `32.75` |
| `Live` | `Long` | `28.85` | 140,030,000.00 USD | 0.00 USD | 10,220.00 USD | `-70.26%` | `354.37` |
| `Live` | `Long` | `28.95` | 140,020,000.00 USD | 0.00 USD | 877.19 USD | `-70.15%` | `30.30` |
| `Live` | `Long` | `29.05` | 140,020,000.00 USD | 0.00 USD | 7,830.00 USD | `-70.05%` | `269.62` |
| `Live` | `Long` | `29.15` | 140,010,000.00 USD | 0.00 USD | 16,670.00 USD | `-69.95%` | `571.84` |
| `Live` | `Long` | `29.65` | 139,990,000.00 USD | 0.00 USD | 16,330.00 USD | `-69.43%` | `550.72` |
| `Live` | `Long` | `29.85` | 139,980,000.00 USD | 0.00 USD | 15,620.00 USD | `-69.23%` | `523.23` |
| `Live` | `Long` | `29.95` | 139,960,000.00 USD | 0.00 USD | 728.98 USD | `-69.12%` | `24.34` |
| `Live` | `Long` | `30.05` | 139,960,000.00 USD | 0.00 USD | 7,170.00 USD | `-69.02%` | `238.70` |
| `Live` | `Long` | `30.15` | 139,950,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.92%` | `1,570.00` |
| `Live` | `Long` | `30.25` | 139,910,000.00 USD | 0.00 USD | 443.47 USD | `-68.81%` | `14.66` |
| `Live` | `Long` | `30.45` | 139,910,000.00 USD | 0.00 USD | 732.32 USD | `-68.61%` | `24.05` |
| `Live` | `Long` | `30.55` | 139,910,000.00 USD | 0.00 USD | 889.01 USD | `-68.50%` | `29.10` |
| `Live` | `Long` | `30.65` | 139,910,000.00 USD | 0.00 USD | 233.86 USD | `-68.40%` | `7.63` |
| `Live` | `Long` | `30.75` | 139,900,000.00 USD | 0.00 USD | 7,660.00 USD | `-68.30%` | `248.95` |
| `Live` | `Long` | `30.85` | 139,900,000.00 USD | 0.00 USD | 1,740.00 USD | `-68.20%` | `56.43` |
| `Live` | `Long` | `31.15` | 139,900,000.00 USD | 0.00 USD | 529,550.00 USD | `-67.89%` | `16,999.92` |
| `Live` | `Long` | `31.45` | 139,370,000.00 USD | 0.00 USD | 2,790.00 USD | `-67.58%` | `88.85` |
| `Live` | `Long` | `32.05` | 139,360,000.00 USD | 0.00 USD | 101.28 USD | `-66.96%` | `3.16` |
| `Live` | `Long` | `32.25` | 139,360,000.00 USD | 0.00 USD | 1,570.00 USD | `-66.75%` | `48.64` |
| `Live` | `Long` | `32.35` | 139,360,000.00 USD | 0.00 USD | 475.87 USD | `-66.65%` | `14.71` |
| `Live` | `Long` | `32.45` | 139,360,000.00 USD | 0.00 USD | 1,800.00 USD | `-66.55%` | `55.47` |
| `Live` | `Long` | `32.65` | 139,360,000.00 USD | 0.00 USD | 24,680.00 USD | `-66.34%` | `755.97` |
| `Live` | `Long` | `32.85` | 139,330,000.00 USD | 0.00 USD | 5,240.00 USD | `-66.13%` | `159.61` |
| `Live` | `Long` | `32.95` | 139,330,000.00 USD | 0.00 USD | 219.45 USD | `-66.03%` | `6.66` |
| `Live` | `Long` | `33.05` | 139,330,000.00 USD | 0.00 USD | 384.04 USD | `-65.93%` | `11.62` |
| `Live` | `Long` | `33.15` | 139,330,000.00 USD | 0.00 USD | 16,580.00 USD | `-65.82%` | `500.00` |
| `Live` | `Long` | `33.35` | 139,310,000.00 USD | 0.00 USD | 13,140.00 USD | `-65.62%` | `394.01` |
| `Live` | `Long` | `33.45` | 139,300,000.00 USD | 0.00 USD | 66,900.00 USD | `-65.51%` | `2,000.00` |
| `Live` | `Long` | `33.75` | 139,230,000.00 USD | 0.00 USD | 562.61 USD | `-65.21%` | `16.67` |
| `Live` | `Long` | `34.65` | 139,230,000.00 USD | 0.00 USD | 3,760.00 USD | `-64.28%` | `108.49` |
| `Live` | `Long` | `34.75` | 139,230,000.00 USD | 0.00 USD | 337.77 USD | `-64.17%` | `9.72` |
| `Live` | `Long` | `34.95` | 139,230,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-63.97%` | `189,472.50` |
| `Live` | `Long` | `35.15` | 132,610,000.00 USD | 0.00 USD | 441.84 USD | `-63.76%` | `12.57` |
| `Live` | `Long` | `35.25` | 132,610,000.00 USD | 0.00 USD | 17,620.00 USD | `-63.66%` | `500.00` |
| `Live` | `Long` | `35.45` | 132,590,000.00 USD | 0.00 USD | 14,660.00 USD | `-63.45%` | `413.53` |
| `Live` | `Long` | `35.55` | 132,570,000.00 USD | 0.00 USD | 893,720.00 USD | `-63.35%` | `25,139.70` |
| `Live` | `Long` | `35.65` | 131,680,000.00 USD | 0.00 USD | 47,920.00 USD | `-63.25%` | `1,344.19` |
| `Live` | `Long` | `35.75` | 131,630,000.00 USD | 0.00 USD | 7,470.00 USD | `-63.14%` | `209.02` |
| `Live` | `Long` | `35.95` | 131,620,000.00 USD | 0.00 USD | 5,870.00 USD | `-62.94%` | `163.21` |
| `Live` | `Long` | `36.15` | 131,620,000.00 USD | 0.00 USD | 531.41 USD | `-62.73%` | `14.70` |
| `Live` | `Long` | `36.25` | 131,620,000.00 USD | 0.00 USD | 817,260.00 USD | `-62.63%` | `22,545.24` |
| `Live` | `Long` | `36.35` | 130,800,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.53%` | `121.32` |
| `Live` | `Long` | `36.45` | 130,800,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.42%` | `66.24` |
| `Live` | `Long` | `36.65` | 130,790,000.00 USD | 0.00 USD | 247.39 USD | `-62.22%` | `6.75` |
| `Live` | `Long` | `36.75` | 130,790,000.00 USD | 0.00 USD | 500.90 USD | `-62.11%` | `13.63` |
| `Live` | `Long` | `36.85` | 130,790,000.00 USD | 0.00 USD | 320.59 USD | `-62.01%` | `8.70` |
| `Live` | `Long` | `36.95` | 130,790,000.00 USD | 0.00 USD | 2,220.00 USD | `-61.91%` | `60.18` |
| `Live` | `Long` | `37.05` | 130,790,000.00 USD | 0.00 USD | 2,810.00 USD | `-61.80%` | `75.83` |
| `Live` | `Long` | `37.15` | 130,790,000.00 USD | 0.00 USD | 320.60 USD | `-61.70%` | `8.63` |
| `Live` | `Long` | `37.25` | 130,790,000.00 USD | 0.00 USD | 42,120.00 USD | `-61.60%` | `1,130.72` |
| `Live` | `Long` | `37.35` | 130,740,000.00 USD | 0.00 USD | 19,600.00 USD | `-61.49%` | `524.75` |
| `Live` | `Long` | `37.45` | 130,720,000.00 USD | 0.00 USD | 401.84 USD | `-61.39%` | `10.73` |
| `Live` | `Long` | `37.55` | 130,720,000.00 USD | 0.00 USD | 262.85 USD | `-61.29%` | `7.00` |
| `Live` | `Long` | `37.65` | 130,720,000.00 USD | 0.00 USD | 2,580.00 USD | `-61.18%` | `68.46` |
| `Live` | `Long` | `37.75` | 130,720,000.00 USD | 0.00 USD | 47,580.00 USD | `-61.08%` | `1,260.30` |
| `Live` | `Long` | `37.85` | 130,670,000.00 USD | 0.00 USD | 3,110.00 USD | `-60.98%` | `82.13` |
| `Live` | `Long` | `37.95` | 130,670,000.00 USD | 0.00 USD | 4,980.00 USD | `-60.88%` | `131.15` |
| `Live` | `Long` | `38.05` | 130,670,000.00 USD | 0.00 USD | 542.59 USD | `-60.77%` | `14.26` |
| `Live` | `Long` | `38.25` | 130,670,000.00 USD | 0.00 USD | 1,090.00 USD | `-60.57%` | `28.60` |
| `Live` | `Long` | `38.35` | 130,660,000.00 USD | 0.00 USD | 451.38 USD | `-60.46%` | `11.77` |
| `Live` | `Long` | `38.45` | 130,660,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.36%` | `78,000.00` |
| `Live` | `Long` | `38.55` | 127,660,000.00 USD | 0.00 USD | 49,340.00 USD | `-60.26%` | `1,280.00` |
| `Live` | `Long` | `38.75` | 127,620,000.00 USD | 0.00 USD | 736.64 USD | `-60.05%` | `19.01` |
| `Live` | `Long` | `38.85` | 127,610,000.00 USD | 0.00 USD | 4,400.00 USD | `-59.95%` | `113.24` |
| `Live` | `Long` | `38.95` | 127,610,000.00 USD | 0.00 USD | 195,360.00 USD | `-59.84%` | `5,015.60` |
| `Live` | `Long` | `39.05` | 127,420,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.74%` | `1,292.50` |
| `Live` | `Long` | `39.15` | 127,360,000.00 USD | 0.00 USD | 1,770.00 USD | `-59.64%` | `45.13` |
| `Live` | `Long` | `39.35` | 127,360,000.00 USD | 0.00 USD | 24,590.00 USD | `-59.43%` | `624.90` |
| `Live` | `Long` | `39.45` | 127,340,000.00 USD | 0.00 USD | 116,160.00 USD | `-59.33%` | `2,944.47` |
| `Live` | `Long` | `39.55` | 127,220,000.00 USD | 0.00 USD | 596,880.00 USD | `-59.23%` | `15,091.67` |
| `Live` | `Long` | `39.65` | 126,630,000.00 USD | 0.00 USD | 1,560.00 USD | `-59.12%` | `39.31` |
| `Live` | `Long` | `39.75` | 126,620,000.00 USD | 0.00 USD | 3,450.00 USD | `-59.02%` | `86.82` |
| `Live` | `Long` | `39.85` | 126,620,000.00 USD | 0.00 USD | 1,270.00 USD | `-58.92%` | `31.86` |
| `Live` | `Long` | `39.95` | 126,620,000.00 USD | 0.00 USD | 399.50 USD | `-58.81%` | `10.00` |
| `Live` | `Long` | `40.05` | 126,620,000.00 USD | 0.00 USD | 1,510.00 USD | `-58.71%` | `37.77` |
| `Live` | `Long` | `40.15` | 126,620,000.00 USD | 0.00 USD | 8,700.00 USD | `-58.61%` | `216.59` |
| `Live` | `Long` | `40.25` | 126,610,000.00 USD | 0.00 USD | 632.73 USD | `-58.50%` | `15.72` |
| `Live` | `Long` | `40.35` | 126,610,000.00 USD | 0.00 USD | 2,400.00 USD | `-58.40%` | `59.42` |
| `Live` | `Long` | `40.55` | 126,610,000.00 USD | 0.00 USD | 4,150.00 USD | `-58.20%` | `102.43` |
| `Live` | `Long` | `40.85` | 126,600,000.00 USD | 0.00 USD | 2,880.00 USD | `-57.89%` | `70.42` |
| `Live` | `Long` | `40.95` | 126,600,000.00 USD | 0.00 USD | 438.17 USD | `-57.78%` | `10.70` |
| `Live` | `Long` | `41.05` | 126,600,000.00 USD | 0.00 USD | 14,280.00 USD | `-57.68%` | `347.76` |
| `Live` | `Long` | `41.15` | 126,580,000.00 USD | 0.00 USD | 25,320.00 USD | `-57.58%` | `615.36` |
| `Live` | `Long` | `41.25` | 126,560,000.00 USD | 0.00 USD | 368.36 USD | `-57.47%` | `8.93` |
| `Live` | `Long` | `41.35` | 126,560,000.00 USD | 0.00 USD | 12,820.00 USD | `-57.37%` | `310.12` |
| `Live` | `Long` | `41.55` | 126,550,000.00 USD | 0.00 USD | 4,260.00 USD | `-57.16%` | `102.60` |
| `Live` | `Long` | `41.65` | 126,540,000.00 USD | 0.00 USD | 770.11 USD | `-57.06%` | `18.49` |
| `Live` | `Long` | `41.75` | 126,540,000.00 USD | 0.00 USD | 588.26 USD | `-56.96%` | `14.09` |
| `Live` | `Long` | `41.85` | 126,540,000.00 USD | 0.00 USD | 109,250.00 USD | `-56.85%` | `2,610.45` |
| `Live` | `Long` | `41.95` | 126,430,000.00 USD | 0.00 USD | 48,400.00 USD | `-56.75%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 126,380,000.00 USD | 0.00 USD | 470.12 USD | `-56.65%` | `11.18` |
| `Live` | `Long` | `42.15` | 126,380,000.00 USD | 0.00 USD | 19,850.00 USD | `-56.55%` | `471.03` |
| `Live` | `Long` | `42.25` | 126,360,000.00 USD | 0.00 USD | 146.19 USD | `-56.44%` | `3.46` |
| `Live` | `Long` | `42.35` | 126,360,000.00 USD | 0.00 USD | 198.62 USD | `-56.34%` | `4.69` |
| `Live` | `Long` | `42.55` | 126,360,000.00 USD | 0.00 USD | 6,960.00 USD | `-56.13%` | `163.50` |
| `Live` | `Long` | `42.85` | 126,350,000.00 USD | 0.00 USD | 44,460.00 USD | `-55.82%` | `1,037.64` |
| `Live` | `Long` | `42.95` | 126,310,000.00 USD | 0.00 USD | 4,680.00 USD | `-55.72%` | `109.07` |
| `Live` | `Long` | `43.25` | 126,300,000.00 USD | 0.00 USD | 1,890.00 USD | `-55.41%` | `43.67` |
| `Live` | `Long` | `43.35` | 126,300,000.00 USD | 0.00 USD | 4,710.00 USD | `-55.31%` | `108.68` |
| `Live` | `Long` | `43.45` | 126,300,000.00 USD | 0.00 USD | 37,820.00 USD | `-55.21%` | `870.52` |
| `Live` | `Long` | `43.65` | 126,260,000.00 USD | 0.00 USD | 4,390.00 USD | `-55.00%` | `100.50` |
| `Live` | `Long` | `43.75` | 126,260,000.00 USD | 0.00 USD | 8,760.00 USD | `-54.90%` | `200.13` |
| `Live` | `Long` | `43.85` | 126,250,000.00 USD | 0.00 USD | 275.38 USD | `-54.79%` | `6.28` |
| `Live` | `Long` | `43.95` | 126,250,000.00 USD | 0.00 USD | 242.16 USD | `-54.69%` | `5.51` |
| `Live` | `Long` | `44.05` | 126,250,000.00 USD | 0.00 USD | 11,220.00 USD | `-54.59%` | `254.69` |
| `Live` | `Long` | `44.15` | 126,240,000.00 USD | 0.00 USD | 359,690.00 USD | `-54.48%` | `8,146.95` |
| `Live` | `Long` | `44.25` | 125,880,000.00 USD | 0.00 USD | 6,110.00 USD | `-54.38%` | `138.09` |
| `Live` | `Long` | `44.35` | 125,870,000.00 USD | 0.00 USD | 2,640.00 USD | `-54.28%` | `59.63` |
| `Live` | `Long` | `44.45` | 125,870,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.17%` | `229.02` |
| `Live` | `Long` | `44.55` | 125,860,000.00 USD | 0.00 USD | 3,670,000.00 USD | `-54.07%` | `82,466.96` |
| `Live` | `Long` | `44.65` | 122,180,000.00 USD | 0.00 USD | 410.78 USD | `-53.97%` | `9.20` |
| `Live` | `Long` | `44.75` | 122,180,000.00 USD | 0.00 USD | 2,220.00 USD | `-53.87%` | `49.62` |
| `Live` | `Long` | `44.85` | 122,180,000.00 USD | 0.00 USD | 477.20 USD | `-53.76%` | `10.64` |
| `Live` | `Long` | `44.95` | 122,180,000.00 USD | 0.00 USD | 686,220.00 USD | `-53.66%` | `15,266.38` |
| `Live` | `Long` | `45.05` | 121,490,000.00 USD | 0.00 USD | 3,630.00 USD | `-53.56%` | `80.49` |
| `Live` | `Long` | `45.15` | 121,490,000.00 USD | 0.00 USD | 6,540.00 USD | `-53.45%` | `144.86` |
| `Live` | `Long` | `45.25` | 121,480,000.00 USD | 0.00 USD | 5,770.00 USD | `-53.35%` | `127.50` |
| `Live` | `Long` | `45.35` | 121,480,000.00 USD | 0.00 USD | 3,990.00 USD | `-53.25%` | `88.07` |
| `Live` | `Long` | `45.45` | 121,470,000.00 USD | 0.00 USD | 9,480.00 USD | `-53.14%` | `208.64` |
| `Live` | `Long` | `45.55` | 121,460,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.04%` | `174.26` |
| `Live` | `Long` | `45.65` | 121,460,000.00 USD | 0.00 USD | 319.09 USD | `-52.94%` | `6.99` |
| `Live` | `Long` | `45.75` | 121,460,000.00 USD | 0.00 USD | 9,790.00 USD | `-52.83%` | `213.92` |
| `Live` | `Long` | `45.85` | 121,450,000.00 USD | 0.00 USD | 573.58 USD | `-52.73%` | `12.51` |
| `Live` | `Long` | `45.95` | 121,450,000.00 USD | 0.00 USD | 26,070.00 USD | `-52.63%` | `567.34` |
| `Live` | `Long` | `46.05` | 121,420,000.00 USD | 0.00 USD | 281.83 USD | `-52.52%` | `6.12` |
| `Live` | `Long` | `46.15` | 121,420,000.00 USD | 0.00 USD | 997.76 USD | `-52.42%` | `21.62` |
| `Live` | `Long` | `46.25` | 121,420,000.00 USD | 0.00 USD | 2,770.00 USD | `-52.32%` | `60.00` |
| `Live` | `Long` | `46.35` | 121,420,000.00 USD | 0.00 USD | 42,080.00 USD | `-52.22%` | `907.95` |
| `Live` | `Long` | `46.45` | 121,370,000.00 USD | 0.00 USD | 3,890.00 USD | `-52.11%` | `83.77` |
| `Live` | `Long` | `46.55` | 121,370,000.00 USD | 0.00 USD | 633.08 USD | `-52.01%` | `13.60` |
| `Live` | `Long` | `46.65` | 121,370,000.00 USD | 0.00 USD | 542.07 USD | `-51.91%` | `11.62` |
| `Live` | `Long` | `46.75` | 121,370,000.00 USD | 0.00 USD | 9,560.00 USD | `-51.80%` | `204.51` |
| `Live` | `Long` | `46.85` | 121,360,000.00 USD | 0.00 USD | 140.55 USD | `-51.70%` | `3.00` |
| `Live` | `Long` | `46.95` | 121,360,000.00 USD | 0.00 USD | 2,590.00 USD | `-51.60%` | `55.07` |
| `Live` | `Long` | `47.05` | 121,360,000.00 USD | 0.00 USD | 460.62 USD | `-51.49%` | `9.79` |
| `Live` | `Long` | `47.15` | 121,360,000.00 USD | 0.00 USD | 4,130.00 USD | `-51.39%` | `87.50` |
| `Live` | `Long` | `47.25` | 121,350,000.00 USD | 0.00 USD | 6,930.00 USD | `-51.29%` | `146.59` |
| `Live` | `Long` | `47.35` | 121,340,000.00 USD | 0.00 USD | 269.90 USD | `-51.18%` | `5.70` |
| `Live` | `Long` | `47.55` | 121,340,000.00 USD | 0.00 USD | 106.04 USD | `-50.98%` | `2.23` |
| `Live` | `Long` | `47.65` | 121,340,000.00 USD | 0.00 USD | 3,480.00 USD | `-50.88%` | `73.02` |
| `Live` | `Long` | `47.75` | 121,340,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-50.77%` | `24,003.37` |
| `Live` | `Long` | `48.05` | 120,190,000.00 USD | 0.00 USD | 4,630.00 USD | `-50.46%` | `96.46` |
| `Live` | `Long` | `48.15` | 120,190,000.00 USD | 0.00 USD | 5,470.00 USD | `-50.36%` | `113.54` |
| `Live` | `Long` | `48.25` | 120,180,000.00 USD | 0.00 USD | 2,200.00 USD | `-50.26%` | `45.57` |
| `Live` | `Long` | `48.35` | 120,180,000.00 USD | 0.00 USD | 5,690.00 USD | `-50.15%` | `117.78` |
| `Live` | `Long` | `48.45` | 120,180,000.00 USD | 0.00 USD | 2,930.00 USD | `-50.05%` | `60.44` |
| `Live` | `Long` | `48.55` | 120,170,000.00 USD | 0.00 USD | 2,870.00 USD | `-49.95%` | `59.06` |
| `Live` | `Long` | `48.65` | 120,170,000.00 USD | 0.00 USD | 12,220.00 USD | `-49.84%` | `251.14` |
| `Live` | `Long` | `48.75` | 120,160,000.00 USD | 0.00 USD | 453.38 USD | `-49.74%` | `9.30` |
| `Live` | `Long` | `48.85` | 120,160,000.00 USD | 0.00 USD | 23,430.00 USD | `-49.64%` | `479.62` |
| `Live` | `Long` | `48.95` | 120,130,000.00 USD | 0.00 USD | 1,530.00 USD | `-49.54%` | `31.26` |
| `Live` | `Long` | `49.05` | 120,130,000.00 USD | 0.00 USD | 1,120.00 USD | `-49.43%` | `22.86` |
| `Live` | `Long` | `49.25` | 120,130,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.23%` | `430.30` |
| `Live` | `Long` | `49.35` | 120,110,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.12%` | `26.77` |
| `Live` | `Long` | `49.45` | 120,110,000.00 USD | 0.00 USD | 16,000.00 USD | `-49.02%` | `323.47` |
| `Live` | `Long` | `49.55` | 120,090,000.00 USD | 0.00 USD | 11,210.00 USD | `-48.92%` | `226.32` |
| `Live` | `Long` | `49.65` | 120,080,000.00 USD | 0.00 USD | 17,370.00 USD | `-48.81%` | `349.79` |
| `Live` | `Long` | `49.75` | 120,070,000.00 USD | 0.00 USD | 4,200.00 USD | `-48.71%` | `84.49` |
| `Live` | `Long` | `49.85` | 120,060,000.00 USD | 0.00 USD | 5,960.00 USD | `-48.61%` | `119.64` |
| `Live` | `Long` | `49.95` | 120,050,000.00 USD | 0.00 USD | 22,060.00 USD | `-48.50%` | `441.68` |
| `Live` | `Long` | `50.05` | 120,030,000.00 USD | 0.00 USD | 9,450.00 USD | `-48.40%` | `188.80` |
| `Live` | `Long` | `50.15` | 120,020,000.00 USD | 0.00 USD | 2,030.00 USD | `-48.30%` | `40.52` |
| `Live` | `Long` | `50.25` | 120,020,000.00 USD | 0.00 USD | 7,960.00 USD | `-48.19%` | `158.41` |
| `Live` | `Long` | `50.35` | 120,010,000.00 USD | 0.00 USD | 2,410.00 USD | `-48.09%` | `47.91` |
| `Live` | `Long` | `50.45` | 120,010,000.00 USD | 0.00 USD | 4,320.00 USD | `-47.99%` | `85.67` |
| `Live` | `Long` | `50.55` | 120,010,000.00 USD | 0.00 USD | 2,910.00 USD | `-47.89%` | `57.47` |
| `Live` | `Long` | `50.65` | 120,000,000.00 USD | 0.00 USD | 337.33 USD | `-47.78%` | `6.66` |
| `Live` | `Long` | `50.75` | 120,000,000.00 USD | 0.00 USD | 15,400.00 USD | `-47.68%` | `303.40` |
| `Live` | `Long` | `50.85` | 119,990,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-47.58%` | `20,346.21` |
| `Live` | `Long` | `50.95` | 118,950,000.00 USD | 0.00 USD | 2,110.00 USD | `-47.47%` | `41.38` |
| `Live` | `Long` | `51.05` | 118,950,000.00 USD | 0.00 USD | 3,120.00 USD | `-47.37%` | `61.02` |
| `Live` | `Long` | `51.15` | 118,950,000.00 USD | 0.00 USD | 3,300.00 USD | `-47.27%` | `64.54` |
| `Live` | `Long` | `51.25` | 118,940,000.00 USD | 0.00 USD | 13,360.00 USD | `-47.16%` | `260.75` |
| `Live` | `Long` | `51.35` | 118,930,000.00 USD | 0.00 USD | 360.48 USD | `-47.06%` | `7.02` |
| `Live` | `Long` | `51.45` | 118,930,000.00 USD | 0.00 USD | 7,110.00 USD | `-46.96%` | `138.18` |
| `Live` | `Long` | `51.55` | 118,920,000.00 USD | 0.00 USD | 22,680.00 USD | `-46.85%` | `439.92` |
| `Live` | `Long` | `51.65` | 118,900,000.00 USD | 0.00 USD | 115,520.00 USD | `-46.75%` | `2,236.54` |
| `Live` | `Long` | `51.75` | 118,790,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.65%` | `478.71` |
| `Live` | `Long` | `51.85` | 118,760,000.00 USD | 0.00 USD | 46,500.00 USD | `-46.55%` | `896.84` |
| `Live` | `Long` | `51.95` | 118,710,000.00 USD | 0.00 USD | 469,890.00 USD | `-46.44%` | `9,045.12` |
| `Live` | `Long` | `52.05` | 118,240,000.00 USD | 0.00 USD | 101,520.00 USD | `-46.34%` | `1,950.52` |
| `Live` | `Long` | `52.15` | 118,140,000.00 USD | 0.00 USD | 32,890.00 USD | `-46.24%` | `630.75` |
| `Live` | `Long` | `52.25` | 118,110,000.00 USD | 0.00 USD | 3,330.00 USD | `-46.13%` | `63.73` |
| `Live` | `Long` | `52.35` | 118,110,000.00 USD | 0.00 USD | 1,190.00 USD | `-46.03%` | `22.74` |
| `Live` | `Long` | `52.45` | 118,110,000.00 USD | 0.00 USD | 2,030.00 USD | `-45.93%` | `38.67` |
| `Live` | `Long` | `52.55` | 118,100,000.00 USD | 0.00 USD | 11,110.00 USD | `-45.82%` | `211.45` |
| `Live` | `Long` | `52.65` | 118,090,000.00 USD | 0.00 USD | 4,270.00 USD | `-45.72%` | `81.04` |
| `Live` | `Long` | `52.75` | 118,090,000.00 USD | 0.00 USD | 1,810.00 USD | `-45.62%` | `34.28` |
| `Live` | `Long` | `52.85` | 118,090,000.00 USD | 0.00 USD | 33,070.00 USD | `-45.51%` | `625.77` |
| `Live` | `Long` | `52.95` | 118,050,000.00 USD | 0.00 USD | 3,890.00 USD | `-45.41%` | `73.46` |
| `Live` | `Long` | `53.05` | 118,050,000.00 USD | 0.00 USD | 5,760.00 USD | `-45.31%` | `108.66` |
| `Live` | `Long` | `53.15` | 118,040,000.00 USD | 0.00 USD | 6,280.00 USD | `-45.21%` | `118.12` |
| `Live` | `Long` | `53.25` | 118,040,000.00 USD | 0.00 USD | 5,620.00 USD | `-45.10%` | `105.59` |
| `Live` | `Long` | `53.35` | 118,030,000.00 USD | 0.00 USD | 2,130.00 USD | `-45.00%` | `39.99` |
| `Live` | `Long` | `53.45` | 118,030,000.00 USD | 0.00 USD | 34,550.00 USD | `-44.90%` | `646.33` |
| `Live` | `Long` | `53.55` | 118,000,000.00 USD | 0.00 USD | 43,250.00 USD | `-44.79%` | `807.62` |
| `Live` | `Long` | `53.65` | 117,950,000.00 USD | 0.00 USD | 230.70 USD | `-44.69%` | `4.30` |
| `Live` | `Long` | `53.75` | 117,950,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.59%` | `67.00` |
| `Live` | `Long` | `53.85` | 117,950,000.00 USD | 0.00 USD | 19,810.00 USD | `-44.48%` | `367.96` |
| `Live` | `Long` | `53.95` | 117,930,000.00 USD | 0.00 USD | 59,050.00 USD | `-44.38%` | `1,094.61` |
| `Live` | `Long` | `54.05` | 117,870,000.00 USD | 0.00 USD | 350.78 USD | `-44.28%` | `6.49` |
| `Live` | `Long` | `54.15` | 117,870,000.00 USD | 0.00 USD | 27,260.00 USD | `-44.17%` | `503.42` |
| `Live` | `Long` | `54.25` | 117,840,000.00 USD | 0.00 USD | 12,410.00 USD | `-44.07%` | `228.74` |
| `Live` | `Long` | `54.35` | 117,830,000.00 USD | 0.00 USD | 4,590.00 USD | `-43.97%` | `84.41` |
| `Live` | `Long` | `54.45` | 117,820,000.00 USD | 0.00 USD | 753.04 USD | `-43.86%` | `13.83` |
| `Live` | `Long` | `54.55` | 117,820,000.00 USD | 0.00 USD | 83,090.00 USD | `-43.76%` | `1,523.24` |
| `Live` | `Long` | `54.65` | 117,740,000.00 USD | 0.00 USD | 2,070.00 USD | `-43.66%` | `37.91` |
| `Live` | `Long` | `54.75` | 117,740,000.00 USD | 0.00 USD | 19,320.00 USD | `-43.56%` | `352.85` |
| `Live` | `Long` | `54.85` | 117,720,000.00 USD | 0.00 USD | 862,140.00 USD | `-43.45%` | `15,718.09` |
| `Live` | `Long` | `54.95` | 116,860,000.00 USD | 0.00 USD | 141,900.00 USD | `-43.35%` | `2,582.39` |
| `Live` | `Long` | `55.05` | 116,720,000.00 USD | 0.00 USD | 4,910.00 USD | `-43.25%` | `89.15` |
| `Live` | `Long` | `55.15` | 116,710,000.00 USD | 0.00 USD | 102.58 USD | `-43.14%` | `1.86` |
| `Live` | `Long` | `55.25` | 116,710,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.04%` | `36.31` |
| `Live` | `Long` | `55.35` | 116,710,000.00 USD | 0.00 USD | 9,810.00 USD | `-42.94%` | `177.30` |
| `Live` | `Long` | `55.45` | 116,700,000.00 USD | 0.00 USD | 6,990.00 USD | `-42.83%` | `126.10` |
| `Live` | `Long` | `55.55` | 116,690,000.00 USD | 0.00 USD | 42,870.00 USD | `-42.73%` | `771.70` |
| `Live` | `Long` | `55.65` | 116,650,000.00 USD | 0.00 USD | 56,460.00 USD | `-42.63%` | `1,014.60` |
| `Live` | `Long` | `55.75` | 116,590,000.00 USD | 0.00 USD | 91,560.00 USD | `-42.52%` | `1,642.37` |
| `Live` | `Long` | `55.85` | 116,500,000.00 USD | 0.00 USD | 4,090.00 USD | `-42.42%` | `73.18` |
| `Live` | `Long` | `56.05` | 116,500,000.00 USD | 0.00 USD | 9,120.00 USD | `-42.22%` | `162.73` |
| `Live` | `Long` | `56.15` | 116,490,000.00 USD | 0.00 USD | 36,190.00 USD | `-42.11%` | `644.50` |
| `Live` | `Long` | `56.25` | 116,450,000.00 USD | 0.00 USD | 17,970.00 USD | `-42.01%` | `319.43` |
| `Live` | `Long` | `56.35` | 116,430,000.00 USD | 0.00 USD | 8,650.00 USD | `-41.91%` | `153.57` |
| `Live` | `Long` | `56.45` | 116,420,000.00 USD | 0.00 USD | 5,350.00 USD | `-41.80%` | `94.82` |
| `Live` | `Long` | `56.55` | 116,420,000.00 USD | 0.00 USD | 20,790.00 USD | `-41.70%` | `367.59` |
| `Live` | `Long` | `56.65` | 116,400,000.00 USD | 0.00 USD | 13,500.00 USD | `-41.60%` | `238.26` |
| `Live` | `Long` | `56.75` | 116,390,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.49%` | `165.87` |
| `Live` | `Long` | `56.85` | 116,380,000.00 USD | 0.00 USD | 65,680.00 USD | `-41.39%` | `1,155.40` |
| `Live` | `Long` | `56.95` | 116,310,000.00 USD | 0.00 USD | 14,320.00 USD | `-41.29%` | `251.38` |
| `Live` | `Long` | `57.05` | 116,300,000.00 USD | 0.00 USD | 4,600.00 USD | `-41.18%` | `80.70` |
| `Live` | `Long` | `57.15` | 116,290,000.00 USD | 0.00 USD | 21,580.00 USD | `-41.08%` | `377.65` |
| `Live` | `Long` | `57.25` | 116,270,000.00 USD | 0.00 USD | 9,850.00 USD | `-40.98%` | `172.11` |
| `Live` | `Long` | `57.35` | 116,260,000.00 USD | 0.00 USD | 9,580.00 USD | `-40.88%` | `167.07` |
| `Live` | `Long` | `57.45` | 116,250,000.00 USD | 0.00 USD | 23,990.00 USD | `-40.77%` | `417.56` |
| `Live` | `Long` | `57.55` | 116,230,000.00 USD | 0.00 USD | 924.25 USD | `-40.67%` | `16.06` |
| `Live` | `Long` | `57.65` | 116,230,000.00 USD | 0.00 USD | 242.13 USD | `-40.57%` | `4.20` |
| `Live` | `Long` | `57.75` | 116,220,000.00 USD | 0.00 USD | 90,210.00 USD | `-40.46%` | `1,562.00` |
| `Live` | `Long` | `57.85` | 116,130,000.00 USD | 0.00 USD | 22,150.00 USD | `-40.36%` | `382.92` |
| `Live` | `Long` | `57.95` | 116,110,000.00 USD | 0.00 USD | 3,890.00 USD | `-40.26%` | `67.12` |
| `Live` | `Long` | `58.05` | 116,110,000.00 USD | 0.00 USD | 5,000.00 USD | `-40.15%` | `86.17` |
| `Live` | `Long` | `58.15` | 116,100,000.00 USD | 0.00 USD | 2,450,000.00 USD | `-40.05%` | `42,138.54` |
| `Live` | `Long` | `58.25` | 113,650,000.00 USD | 0.00 USD | 16,350.00 USD | `-39.95%` | `280.67` |
| `Live` | `Long` | `58.35` | 113,640,000.00 USD | 0.00 USD | 16,970.00 USD | `-39.84%` | `290.82` |
| `Live` | `Long` | `58.55` | 113,620,000.00 USD | 0.00 USD | 2,970.00 USD | `-39.64%` | `50.81` |
| `Live` | `Long` | `58.65` | 113,620,000.00 USD | 0.00 USD | 8,660.00 USD | `-39.53%` | `147.70` |
| `Live` | `Long` | `58.75` | 113,610,000.00 USD | 0.00 USD | 505.84 USD | `-39.43%` | `8.61` |
| `Live` | `Long` | `58.85` | 113,610,000.00 USD | 0.00 USD | 6,130.00 USD | `-39.33%` | `104.08` |
| `Live` | `Long` | `58.95` | 113,600,000.00 USD | 0.00 USD | 488.70 USD | `-39.23%` | `8.29` |
| `Live` | `Long` | `59.05` | 113,600,000.00 USD | 0.00 USD | 9,090.00 USD | `-39.12%` | `153.97` |
| `Live` | `Long` | `59.15` | 113,590,000.00 USD | 0.00 USD | 4,760.00 USD | `-39.02%` | `80.44` |
| `Live` | `Long` | `59.35` | 113,590,000.00 USD | 0.00 USD | 29,010.00 USD | `-38.81%` | `488.75` |
| `Live` | `Long` | `59.45` | 113,560,000.00 USD | 0.00 USD | 99,680.00 USD | `-38.71%` | `1,676.69` |
| `Live` | `Long` | `59.55` | 113,460,000.00 USD | 0.00 USD | 8,610.00 USD | `-38.61%` | `144.57` |
| `Live` | `Long` | `59.65` | 113,450,000.00 USD | 0.00 USD | 4,680.00 USD | `-38.50%` | `78.52` |
| `Live` | `Long` | `59.75` | 113,450,000.00 USD | 0.00 USD | 24,150.00 USD | `-38.40%` | `404.24` |
| `Live` | `Long` | `59.85` | 113,420,000.00 USD | 0.00 USD | 3,040.00 USD | `-38.30%` | `50.72` |
| `Live` | `Long` | `59.95` | 113,420,000.00 USD | 0.00 USD | 57,020.00 USD | `-38.19%` | `951.17` |
| `Live` | `Long` | `60.05` | 113,360,000.00 USD | 0.00 USD | 12,840.00 USD | `-38.09%` | `213.86` |
| `Live` | `Long` | `60.15` | 113,350,000.00 USD | 0.00 USD | 36,310.00 USD | `-37.99%` | `603.62` |
| `Live` | `Long` | `60.25` | 113,310,000.00 USD | 0.00 USD | 2,340.00 USD | `-37.89%` | `38.84` |
| `Live` | `Long` | `60.35` | 113,310,000.00 USD | 0.00 USD | 2,090.00 USD | `-37.78%` | `34.55` |
| `Live` | `Long` | `60.45` | 113,310,000.00 USD | 0.00 USD | 557.35 USD | `-37.68%` | `9.22` |
| `Live` | `Long` | `60.55` | 113,310,000.00 USD | 0.00 USD | 20,910.00 USD | `-37.58%` | `345.30` |
| `Live` | `Long` | `60.65` | 113,290,000.00 USD | 0.00 USD | 711.42 USD | `-37.47%` | `11.73` |
| `Live` | `Long` | `60.75` | 113,290,000.00 USD | 0.00 USD | 9,700.00 USD | `-37.37%` | `159.72` |
| `Live` | `Long` | `60.85` | 113,280,000.00 USD | 0.00 USD | 28,840.00 USD | `-37.27%` | `473.99` |
| `Live` | `Long` | `60.95` | 113,250,000.00 USD | 0.00 USD | 205,990.00 USD | `-37.16%` | `3,379.72` |
| `Live` | `Long` | `61.05` | 113,040,000.00 USD | 0.00 USD | 4,230.00 USD | `-37.06%` | `69.34` |
| `Live` | `Long` | `61.15` | 113,040,000.00 USD | 0.00 USD | 68,210.00 USD | `-36.96%` | `1,115.46` |
| `Live` | `Long` | `61.25` | 112,970,000.00 USD | 0.00 USD | 121,310.00 USD | `-36.85%` | `1,980.56` |
| `Live` | `Long` | `61.35` | 112,850,000.00 USD | 0.00 USD | 6,750.00 USD | `-36.75%` | `110.06` |
| `Live` | `Long` | `61.45` | 112,840,000.00 USD | 0.00 USD | 21,390.00 USD | `-36.65%` | `348.15` |
| `Live` | `Long` | `61.55` | 112,820,000.00 USD | 0.00 USD | 121.87 USD | `-36.55%` | `1.98` |
| `Live` | `Long` | `61.65` | 112,820,000.00 USD | 0.00 USD | 20,810.00 USD | `-36.44%` | `337.61` |
| `Live` | `Long` | `61.75` | 112,800,000.00 USD | 0.00 USD | 16,580.00 USD | `-36.34%` | `268.54` |
| `Live` | `Long` | `61.85` | 112,780,000.00 USD | 0.00 USD | 19,560.00 USD | `-36.24%` | `316.17` |
| `Live` | `Long` | `61.95` | 112,760,000.00 USD | 0.00 USD | 22,840.00 USD | `-36.13%` | `368.75` |
| `Live` | `Long` | `62.05` | 112,740,000.00 USD | 0.00 USD | 10,680.00 USD | `-36.03%` | `172.05` |
| `Live` | `Long` | `62.15` | 112,730,000.00 USD | 0.00 USD | 37,180.00 USD | `-35.93%` | `598.28` |
| `Live` | `Long` | `62.25` | 112,690,000.00 USD | 0.00 USD | 3,740.00 USD | `-35.82%` | `60.06` |
| `Live` | `Long` | `62.35` | 112,690,000.00 USD | 0.00 USD | 75,950.00 USD | `-35.72%` | `1,218.09` |
| `Live` | `Long` | `62.45` | 112,610,000.00 USD | 0.00 USD | 21,530.00 USD | `-35.62%` | `344.79` |
| `Live` | `Long` | `62.55` | 112,590,000.00 USD | 0.00 USD | 15,640.00 USD | `-35.51%` | `250.00` |
| `Live` | `Long` | `62.65` | 112,570,000.00 USD | 0.00 USD | 2,230.00 USD | `-35.41%` | `35.62` |
| `Live` | `Long` | `62.75` | 112,570,000.00 USD | 0.00 USD | 9,710.00 USD | `-35.31%` | `154.75` |
| `Live` | `Long` | `62.85` | 112,560,000.00 USD | 0.00 USD | 31,310.00 USD | `-35.20%` | `498.17` |
| `Live` | `Long` | `62.95` | 112,530,000.00 USD | 0.00 USD | 65,250.00 USD | `-35.10%` | `1,036.59` |
| `Live` | `Long` | `63.05` | 112,470,000.00 USD | 0.00 USD | 15,420.00 USD | `-35.00%` | `244.49` |
| `Live` | `Long` | `63.15` | 112,450,000.00 USD | 0.00 USD | 86,040.00 USD | `-34.90%` | `1,362.41` |
| `Live` | `Long` | `63.25` | 112,360,000.00 USD | 0.00 USD | 14,620.00 USD | `-34.79%` | `231.15` |
| `Live` | `Long` | `63.35` | 112,350,000.00 USD | 0.00 USD | 429.51 USD | `-34.69%` | `6.78` |
| `Live` | `Long` | `63.45` | 112,350,000.00 USD | 0.00 USD | 43,420.00 USD | `-34.59%` | `684.37` |
| `Live` | `Long` | `63.55` | 112,310,000.00 USD | 0.00 USD | 6,000.00 USD | `-34.48%` | `94.40` |
| `Live` | `Long` | `63.65` | 112,300,000.00 USD | 0.00 USD | 9,510.00 USD | `-34.38%` | `149.41` |
| `Live` | `Long` | `63.75` | 112,290,000.00 USD | 0.00 USD | 7,100.00 USD | `-34.28%` | `111.42` |
| `Live` | `Long` | `63.85` | 112,280,000.00 USD | 0.00 USD | 40,390.00 USD | `-34.17%` | `632.50` |
| `Live` | `Long` | `63.95` | 112,240,000.00 USD | 0.00 USD | 4,970.00 USD | `-34.07%` | `77.76` |
| `Live` | `Long` | `64.05` | 112,240,000.00 USD | 0.00 USD | 28,890.00 USD | `-33.97%` | `451.13` |
| `Live` | `Long` | `64.25` | 112,210,000.00 USD | 0.00 USD | 4,550.00 USD | `-33.76%` | `70.81` |
| `Live` | `Long` | `64.35` | 112,200,000.00 USD | 0.00 USD | 875.16 USD | `-33.66%` | `13.60` |
| `Live` | `Long` | `64.45` | 112,200,000.00 USD | 0.00 USD | 180,440.00 USD | `-33.56%` | `2,799.76` |
| `Live` | `Long` | `64.55` | 112,020,000.00 USD | 0.00 USD | 69,830.00 USD | `-33.45%` | `1,081.78` |
| `Live` | `Long` | `64.65` | 111,950,000.00 USD | 0.00 USD | 10,000.00 USD | `-33.35%` | `154.63` |
| `Live` | `Long` | `64.75` | 111,940,000.00 USD | 0.00 USD | 146.33 USD | `-33.25%` | `2.26` |
| `Live` | `Long` | `64.85` | 111,940,000.00 USD | 0.00 USD | 20,320.00 USD | `-33.14%` | `313.38` |
| `Live` | `Long` | `64.95` | 111,920,000.00 USD | 0.00 USD | 209.79 USD | `-33.04%` | `3.23` |
| `Live` | `Long` | `65.05` | 111,920,000.00 USD | 0.00 USD | 11,940.00 USD | `-32.94%` | `183.59` |
| `Live` | `Long` | `65.15` | 111,910,000.00 USD | 0.00 USD | 11,360.00 USD | `-32.83%` | `174.40` |
| `Live` | `Long` | `65.25` | 111,900,000.00 USD | 0.00 USD | 1,010.00 USD | `-32.73%` | `15.53` |
| `Live` | `Long` | `65.35` | 111,900,000.00 USD | 0.00 USD | 15,990.00 USD | `-32.63%` | `244.68` |
| `Live` | `Long` | `65.45` | 111,880,000.00 USD | 0.00 USD | 296.49 USD | `-32.52%` | `4.53` |
| `Live` | `Long` | `65.55` | 111,880,000.00 USD | 0.00 USD | 90,080.00 USD | `-32.42%` | `1,374.25` |
| `Live` | `Long` | `65.65` | 111,790,000.00 USD | 0.00 USD | 58,050.00 USD | `-32.32%` | `884.16` |
| `Live` | `Long` | `65.75` | 111,730,000.00 USD | 0.00 USD | 110,590.00 USD | `-32.22%` | `1,681.92` |
| `Live` | `Long` | `65.85` | 111,620,000.00 USD | 0.00 USD | 20,870.00 USD | `-32.11%` | `316.99` |
| `Live` | `Long` | `65.95` | 111,600,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-32.01%` | `20,087.71` |
| `Live` | `Long` | `66.05` | 110,280,000.00 USD | 0.00 USD | 22,740.00 USD | `-31.91%` | `344.26` |
| `Live` | `Long` | `66.15` | 110,250,000.00 USD | 0.00 USD | 10,790.00 USD | `-31.80%` | `163.15` |
| `Live` | `Long` | `66.25` | 110,240,000.00 USD | 0.00 USD | 412,550.00 USD | `-31.70%` | `6,227.19` |
| `Live` | `Long` | `66.35` | 109,830,000.00 USD | 0.00 USD | 71,250.00 USD | `-31.60%` | `1,073.87` |
| `Live` | `Long` | `66.45` | 109,760,000.00 USD | 0.00 USD | 2,290.00 USD | `-31.49%` | `34.45` |
| `Live` | `Long` | `66.55` | 109,760,000.00 USD | 0.00 USD | 42,250.00 USD | `-31.39%` | `634.82` |
| `Live` | `Long` | `66.65` | 109,720,000.00 USD | 0.00 USD | 54,070.00 USD | `-31.29%` | `811.19` |
| `Live` | `Long` | `66.75` | 109,660,000.00 USD | 0.00 USD | 5,930.00 USD | `-31.18%` | `88.77` |
| `Live` | `Long` | `66.85` | 109,660,000.00 USD | 0.00 USD | 2,050.00 USD | `-31.08%` | `30.61` |
| `Live` | `Long` | `66.95` | 109,650,000.00 USD | 0.00 USD | 937.30 USD | `-30.98%` | `14.00` |
| `Live` | `Long` | `67.05` | 109,650,000.00 USD | 0.00 USD | 33,390.00 USD | `-30.87%` | `497.96` |
| `Live` | `Long` | `67.15` | 109,620,000.00 USD | 0.00 USD | 2,510.00 USD | `-30.77%` | `37.39` |
| `Live` | `Long` | `67.25` | 109,620,000.00 USD | 0.00 USD | 19,700.00 USD | `-30.67%` | `292.97` |
| `Live` | `Long` | `67.35` | 109,600,000.00 USD | 0.00 USD | 5,490.00 USD | `-30.57%` | `81.53` |
| `Live` | `Long` | `67.45` | 109,590,000.00 USD | 0.00 USD | 42,850.00 USD | `-30.46%` | `635.34` |
| `Live` | `Long` | `67.55` | 109,550,000.00 USD | 0.00 USD | 3,340,000.00 USD | `-30.36%` | `49,421.58` |
| `Live` | `Long` | `67.65` | 106,210,000.00 USD | 0.00 USD | 156,810.00 USD | `-30.26%` | `2,317.95` |
| `Live` | `Long` | `67.75` | 106,050,000.00 USD | 0.00 USD | 3,850.00 USD | `-30.15%` | `56.88` |
| `Live` | `Long` | `67.85` | 106,050,000.00 USD | 0.00 USD | 2,790.00 USD | `-30.05%` | `41.13` |
| `Live` | `Long` | `67.95` | 106,050,000.00 USD | 0.00 USD | 12,230,000.00 USD | `-29.95%` | `180,019.28` |
| `Live` | `Long` | `68.05` | 93,810,000.00 USD | 0.00 USD | 10,180.00 USD | `-29.84%` | `149.62` |
| `Live` | `Long` | `68.15` | 93,800,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.74%` | `550,114.70` |
| `Live` | `Long` | `68.25` | 56,310,000.00 USD | 0.00 USD | 13,650.00 USD | `-29.64%` | `199.93` |
| `Live` | `Long` | `68.35` | 56,300,000.00 USD | 0.00 USD | 47,450.00 USD | `-29.53%` | `694.29` |
| `Live` | `Long` | `68.45` | 56,250,000.00 USD | 0.00 USD | 21,080.00 USD | `-29.43%` | `308.02` |
| `Live` | `Long` | `68.55` | 56,230,000.00 USD | 0.00 USD | 21,980.00 USD | `-29.33%` | `320.59` |
| `Live` | `Long` | `68.65` | 56,210,000.00 USD | 0.00 USD | 769,100.00 USD | `-29.23%` | `11,203.22` |
| `Live` | `Long` | `68.75` | 55,440,000.00 USD | 0.00 USD | 46,920.00 USD | `-29.12%` | `682.52` |
| `Live` | `Long` | `68.85` | 55,390,000.00 USD | 0.00 USD | 15,560.00 USD | `-29.02%` | `226.06` |
| `Live` | `Long` | `68.95` | 55,380,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-28.92%` | `16,032.66` |
| `Live` | `Long` | `69.05` | 54,270,000.00 USD | 0.00 USD | 3,570.00 USD | `-28.81%` | `51.69` |
| `Live` | `Long` | `69.15` | 54,270,000.00 USD | 0.00 USD | 90,030.00 USD | `-28.71%` | `1,301.89` |
| `Live` | `Long` | `69.25` | 54,180,000.00 USD | 0.00 USD | 10,100.00 USD | `-28.61%` | `145.85` |
| `Live` | `Long` | `69.35` | 54,170,000.00 USD | 0.00 USD | 5,460.00 USD | `-28.50%` | `78.68` |
| `Live` | `Long` | `69.45` | 54,160,000.00 USD | 0.00 USD | 14,370.00 USD | `-28.40%` | `206.85` |
| `Live` | `Long` | `69.55` | 54,150,000.00 USD | 0.00 USD | 23,380.00 USD | `-28.30%` | `336.17` |
| `Live` | `Long` | `69.65` | 54,130,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.19%` | `21.67` |
| `Live` | `Long` | `69.75` | 54,120,000.00 USD | 0.00 USD | 32,740.00 USD | `-28.09%` | `469.35` |
| `Live` | `Long` | `69.85` | 54,090,000.00 USD | 0.00 USD | 22,690.00 USD | `-27.99%` | `324.84` |
| `Live` | `Long` | `69.95` | 54,070,000.00 USD | 0.00 USD | 9,260.00 USD | `-27.89%` | `132.31` |
| `Live` | `Long` | `70.05` | 54,060,000.00 USD | 0.00 USD | 1,170.00 USD | `-27.78%` | `16.70` |
| `Live` | `Long` | `70.15` | 54,060,000.00 USD | 0.00 USD | 13,500.00 USD | `-27.68%` | `192.43` |
| `Live` | `Long` | `70.25` | 54,050,000.00 USD | 0.00 USD | 73,520.00 USD | `-27.58%` | `1,046.55` |
| `Live` | `Long` | `70.35` | 53,970,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-27.47%` | `30,497.85` |
| `Live` | `Long` | `70.45` | 51,830,000.00 USD | 0.00 USD | 116,910.00 USD | `-27.37%` | `1,659.42` |
| `Live` | `Long` | `70.55` | 51,710,000.00 USD | 0.00 USD | 112,920.00 USD | `-27.27%` | `1,600.61` |
| `Live` | `Long` | `70.65` | 51,600,000.00 USD | 0.00 USD | 74,220.00 USD | `-27.16%` | `1,050.54` |
| `Live` | `Long` | `70.75` | 51,520,000.00 USD | 0.00 USD | 16,510.00 USD | `-27.06%` | `233.35` |
| `Live` | `Long` | `70.85` | 51,510,000.00 USD | 0.00 USD | 27,840.00 USD | `-26.96%` | `392.98` |
| `Live` | `Long` | `70.95` | 51,480,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-26.85%` | `18,908.95` |
| `Live` | `Long` | `71.05` | 50,140,000.00 USD | 0.00 USD | 32,070.00 USD | `-26.75%` | `451.43` |
| `Live` | `Long` | `71.15` | 50,100,000.00 USD | 0.00 USD | 67,250.00 USD | `-26.65%` | `945.23` |
| `Live` | `Long` | `71.25` | 50,040,000.00 USD | 0.00 USD | 5,780.00 USD | `-26.54%` | `81.07` |
| `Live` | `Long` | `71.35` | 50,030,000.00 USD | 0.00 USD | 244.73 USD | `-26.44%` | `3.43` |
| `Live` | `Long` | `71.45` | 50,030,000.00 USD | 0.00 USD | 37,650.00 USD | `-26.34%` | `526.93` |
| `Live` | `Long` | `71.55` | 49,990,000.00 USD | 0.00 USD | 42,910.00 USD | `-26.24%` | `599.79` |
| `Live` | `Long` | `71.65` | 49,950,000.00 USD | 0.00 USD | 460.71 USD | `-26.13%` | `6.43` |
| `Live` | `Long` | `71.75` | 49,950,000.00 USD | 0.00 USD | 58,200.00 USD | `-26.03%` | `811.14` |
| `Live` | `Long` | `71.85` | 49,890,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-25.93%` | `20,487.94` |
| `Live` | `Long` | `71.95` | 48,420,000.00 USD | 0.00 USD | 46,050.00 USD | `-25.82%` | `640.08` |
| `Live` | `Long` | `72.05` | 48,370,000.00 USD | 0.00 USD | 39,540.00 USD | `-25.72%` | `548.83` |
| `Live` | `Long` | `72.15` | 48,330,000.00 USD | 0.00 USD | 130,700.00 USD | `-25.62%` | `1,811.56` |
| `Live` | `Long` | `72.25` | 48,200,000.00 USD | 0.00 USD | 41,150.00 USD | `-25.51%` | `569.59` |
| `Live` | `Long` | `72.35` | 48,160,000.00 USD | 0.00 USD | 6,370.00 USD | `-25.41%` | `87.99` |
| `Live` | `Long` | `72.45` | 48,160,000.00 USD | 0.00 USD | 7,100.00 USD | `-25.31%` | `98.04` |
| `Live` | `Long` | `72.55` | 48,150,000.00 USD | 0.00 USD | 12,330.00 USD | `-25.20%` | `169.91` |
| `Live` | `Long` | `72.65` | 48,140,000.00 USD | 0.00 USD | 50,640.00 USD | `-25.10%` | `697.02` |
| `Live` | `Long` | `72.75` | 48,090,000.00 USD | 0.00 USD | 14,660.00 USD | `-25.00%` | `201.53` |
| `Live` | `Long` | `72.85` | 48,070,000.00 USD | 0.00 USD | 59,510.00 USD | `-24.90%` | `816.88` |
| `Live` | `Long` | `72.95` | 48,010,000.00 USD | 0.00 USD | 16,220.00 USD | `-24.79%` | `222.33` |
| `Live` | `Long` | `73.05` | 48,000,000.00 USD | 0.00 USD | 7,310.00 USD | `-24.69%` | `100.09` |
| `Live` | `Long` | `73.15` | 47,990,000.00 USD | 0.00 USD | 62,460.00 USD | `-24.59%` | `853.85` |
| `Live` | `Long` | `73.25` | 47,930,000.00 USD | 0.00 USD | 26,580.00 USD | `-24.48%` | `362.84` |
| `Live` | `Long` | `73.35` | 47,900,000.00 USD | 0.00 USD | 13,520.00 USD | `-24.38%` | `184.38` |
| `Live` | `Long` | `73.45` | 47,890,000.00 USD | 0.00 USD | 3,950.00 USD | `-24.28%` | `53.83` |
| `Live` | `Long` | `73.55` | 47,880,000.00 USD | 0.00 USD | 14,850.00 USD | `-24.17%` | `201.89` |
| `Live` | `Long` | `73.65` | 47,870,000.00 USD | 0.00 USD | 139,500.00 USD | `-24.07%` | `1,894.07` |
| `Live` | `Long` | `73.75` | 47,730,000.00 USD | 0.00 USD | 60,970.00 USD | `-23.97%` | `826.67` |
| `Live` | `Long` | `73.85` | 47,670,000.00 USD | 0.00 USD | 11,970.00 USD | `-23.86%` | `162.13` |
| `Live` | `Long` | `73.95` | 47,650,000.00 USD | 0.00 USD | 40,150.00 USD | `-23.76%` | `542.87` |
| `Live` | `Long` | `74.05` | 47,610,000.00 USD | 0.00 USD | 26,150.00 USD | `-23.66%` | `353.08` |
| `Live` | `Long` | `74.15` | 47,590,000.00 USD | 0.00 USD | 23,290.00 USD | `-23.56%` | `314.11` |
| `Live` | `Long` | `74.25` | 47,560,000.00 USD | 0.00 USD | 537,000.00 USD | `-23.45%` | `7,232.37` |
| `Live` | `Long` | `74.35` | 47,030,000.00 USD | 0.00 USD | 37,770.00 USD | `-23.35%` | `507.99` |
| `Live` | `Long` | `74.45` | 46,990,000.00 USD | 0.00 USD | 8,830.00 USD | `-23.25%` | `118.56` |
| `Live` | `Long` | `74.55` | 46,980,000.00 USD | 0.00 USD | 39,260.00 USD | `-23.14%` | `526.58` |
| `Live` | `Long` | `74.65` | 46,940,000.00 USD | 0.00 USD | 2,090.00 USD | `-23.04%` | `27.99` |
| `Live` | `Long` | `74.75` | 46,940,000.00 USD | 0.00 USD | 47,630.00 USD | `-22.94%` | `637.15` |
| `Live` | `Long` | `74.85` | 46,890,000.00 USD | 0.00 USD | 100,050.00 USD | `-22.83%` | `1,336.64` |
| `Live` | `Long` | `74.95` | 46,790,000.00 USD | 0.00 USD | 22,780.00 USD | `-22.73%` | `303.94` |
| `Live` | `Long` | `75.05` | 46,770,000.00 USD | 0.00 USD | 52,070.00 USD | `-22.63%` | `693.74` |
| `Live` | `Long` | `75.15` | 46,720,000.00 USD | 0.00 USD | 3,570.00 USD | `-22.52%` | `47.44` |
| `Live` | `Long` | `75.25` | 46,710,000.00 USD | 0.00 USD | 14,920.00 USD | `-22.42%` | `198.25` |
| `Live` | `Long` | `75.35` | 46,700,000.00 USD | 0.00 USD | 20,860.00 USD | `-22.32%` | `276.82` |
| `Live` | `Long` | `75.45` | 46,680,000.00 USD | 0.00 USD | 3,370.00 USD | `-22.21%` | `44.65` |
| `Live` | `Long` | `75.55` | 46,670,000.00 USD | 0.00 USD | 52,020.00 USD | `-22.11%` | `688.59` |
| `Live` | `Long` | `75.65` | 46,620,000.00 USD | 0.00 USD | 136,280.00 USD | `-22.01%` | `1,801.45` |
| `Live` | `Long` | `75.75` | 46,490,000.00 USD | 0.00 USD | 48,540.00 USD | `-21.91%` | `640.77` |
| `Live` | `Long` | `75.85` | 46,440,000.00 USD | 0.00 USD | 15,670.00 USD | `-21.80%` | `206.53` |
| `Live` | `Long` | `75.95` | 46,420,000.00 USD | 0.00 USD | 21,910.00 USD | `-21.70%` | `288.51` |
| `Live` | `Long` | `76.05` | 46,400,000.00 USD | 0.00 USD | 1,300.00 USD | `-21.60%` | `17.03` |
| `Live` | `Long` | `76.15` | 46,400,000.00 USD | 0.00 USD | 4,970.00 USD | `-21.49%` | `65.29` |
| `Live` | `Long` | `76.25` | 46,390,000.00 USD | 0.00 USD | 1,380.00 USD | `-21.39%` | `18.08` |
| `Live` | `Long` | `76.35` | 46,390,000.00 USD | 0.00 USD | 36,310.00 USD | `-21.29%` | `475.56` |
| `Live` | `Long` | `76.45` | 46,360,000.00 USD | 0.00 USD | 3,080.00 USD | `-21.18%` | `40.29` |
| `Live` | `Long` | `76.55` | 46,350,000.00 USD | 0.00 USD | 40,540.00 USD | `-21.08%` | `529.64` |
| `Live` | `Long` | `76.65` | 46,310,000.00 USD | 0.00 USD | 30,210.00 USD | `-20.98%` | `394.08` |
| `Live` | `Long` | `76.75` | 46,280,000.00 USD | 0.00 USD | 12,890.00 USD | `-20.87%` | `168.01` |
| `Live` | `Long` | `76.85` | 46,270,000.00 USD | 0.00 USD | 62,790.00 USD | `-20.77%` | `817.02` |
| `Live` | `Long` | `76.95` | 46,210,000.00 USD | 0.00 USD | 32,060.00 USD | `-20.67%` | `416.67` |
| `Live` | `Long` | `77.05` | 46,170,000.00 USD | 0.00 USD | 31,680.00 USD | `-20.57%` | `411.10` |
| `Live` | `Long` | `77.15` | 46,140,000.00 USD | 0.00 USD | 91,690.00 USD | `-20.46%` | `1,188.43` |
| `Live` | `Long` | `77.25` | 46,050,000.00 USD | 0.00 USD | 34,220.00 USD | `-20.36%` | `442.96` |
| `Live` | `Long` | `77.35` | 46,020,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-20.26%` | `22,098.14` |
| `Live` | `Long` | `77.45` | 44,310,000.00 USD | 0.00 USD | 1,340.00 USD | `-20.15%` | `17.25` |
| `Live` | `Long` | `77.55` | 44,310,000.00 USD | 0.00 USD | 7,950.00 USD | `-20.05%` | `102.50` |
| `Live` | `Long` | `77.65` | 44,300,000.00 USD | 0.00 USD | 201,890.00 USD | `-19.95%` | `2,600.00` |
| `Live` | `Long` | `77.75` | 44,100,000.00 USD | 0.00 USD | 357,790.00 USD | `-19.84%` | `4,601.80` |
| `Live` | `Long` | `77.85` | 43,740,000.00 USD | 0.00 USD | 30,720.00 USD | `-19.74%` | `394.55` |
| `Live` | `Long` | `77.95` | 43,710,000.00 USD | 0.00 USD | 4,630.00 USD | `-19.64%` | `59.45` |
| `Live` | `Long` | `78.05` | 43,700,000.00 USD | 0.00 USD | 20,450.00 USD | `-19.53%` | `262.01` |
| `Live` | `Long` | `78.15` | 43,680,000.00 USD | 0.00 USD | 58,230.00 USD | `-19.43%` | `745.16` |
| `Live` | `Long` | `78.25` | 43,620,000.00 USD | 0.00 USD | 40,230.00 USD | `-19.33%` | `514.13` |
| `Live` | `Long` | `78.35` | 43,580,000.00 USD | 0.00 USD | 65,750.00 USD | `-19.23%` | `839.17` |
| `Live` | `Long` | `78.45` | 43,520,000.00 USD | 0.00 USD | 325,630.00 USD | `-19.12%` | `4,150.74` |
| `Live` | `Long` | `78.55` | 43,190,000.00 USD | 0.00 USD | 233,130.00 USD | `-19.02%` | `2,967.87` |
| `Live` | `Long` | `78.65` | 42,960,000.00 USD | 0.00 USD | 708.64 USD | `-18.92%` | `9.01` |
| `Live` | `Long` | `78.75` | 42,960,000.00 USD | 0.00 USD | 61,740.00 USD | `-18.81%` | `784.03` |
| `Live` | `Long` | `78.85` | 42,900,000.00 USD | 0.00 USD | 18,810.00 USD | `-18.71%` | `238.56` |
| `Live` | `Long` | `78.95` | 42,880,000.00 USD | 0.00 USD | 7,420.00 USD | `-18.61%` | `93.93` |
| `Live` | `Long` | `79.05` | 42,870,000.00 USD | 0.00 USD | 1,050.00 USD | `-18.50%` | `13.28` |
| `Live` | `Long` | `79.15` | 42,870,000.00 USD | 0.00 USD | 606,790.00 USD | `-18.40%` | `7,666.35` |
| `Live` | `Long` | `79.25` | 42,260,000.00 USD | 0.00 USD | 126,590.00 USD | `-18.30%` | `1,597.41` |
| `Live` | `Long` | `79.35` | 42,140,000.00 USD | 0.00 USD | 11,270.00 USD | `-18.19%` | `142.03` |
| `Live` | `Long` | `79.45` | 42,130,000.00 USD | 0.00 USD | 12,050.00 USD | `-18.09%` | `151.72` |
| `Live` | `Long` | `79.55` | 42,110,000.00 USD | 0.00 USD | 43,310.00 USD | `-17.99%` | `544.48` |
| `Live` | `Long` | `79.65` | 42,070,000.00 USD | 0.00 USD | 43,730.00 USD | `-17.88%` | `549.02` |
| `Live` | `Long` | `79.75` | 42,030,000.00 USD | 0.00 USD | 693.03 USD | `-17.78%` | `8.69` |
| `Live` | `Long` | `79.85` | 42,030,000.00 USD | 0.00 USD | 51,620.00 USD | `-17.68%` | `646.42` |
| `Live` | `Long` | `79.95` | 41,970,000.00 USD | 0.00 USD | 5,290.00 USD | `-17.58%` | `66.11` |
| `Live` | `Long` | `80.05` | 41,970,000.00 USD | 0.00 USD | 166.50 USD | `-17.47%` | `2.08` |
| `Live` | `Long` | `80.15` | 41,970,000.00 USD | 0.00 USD | 36,590.00 USD | `-17.37%` | `456.48` |
| `Live` | `Long` | `80.25` | 41,930,000.00 USD | 0.00 USD | 51,420.00 USD | `-17.27%` | `640.79` |
| `Live` | `Long` | `80.35` | 41,880,000.00 USD | 0.00 USD | 210,440.00 USD | `-17.16%` | `2,619.07` |
| `Live` | `Long` | `80.45` | 41,670,000.00 USD | 0.00 USD | 8,760.00 USD | `-17.06%` | `108.85` |
| `Live` | `Long` | `80.55` | 41,660,000.00 USD | 0.00 USD | 18,370.00 USD | `-16.96%` | `228.10` |
| `Live` | `Long` | `80.65` | 41,640,000.00 USD | 0.00 USD | 379,900.00 USD | `-16.85%` | `4,710.44` |
| `Live` | `Long` | `80.75` | 41,260,000.00 USD | 0.00 USD | 6,120.00 USD | `-16.75%` | `75.79` |
| `Live` | `Long` | `80.85` | 41,260,000.00 USD | 0.00 USD | 67,080.00 USD | `-16.65%` | `829.68` |
| `Live` | `Long` | `80.95` | 41,190,000.00 USD | 0.00 USD | 10,620.00 USD | `-16.54%` | `131.18` |
| `Live` | `Long` | `81.05` | 41,180,000.00 USD | 0.00 USD | 2,320,000.00 USD | `-16.44%` | `28,570.70` |
| `Live` | `Long` | `81.15` | 38,860,000.00 USD | 0.00 USD | 43,510.00 USD | `-16.34%` | `536.17` |
| `Live` | `Long` | `81.25` | 38,820,000.00 USD | 0.00 USD | 20,470.00 USD | `-16.24%` | `251.90` |
| `Live` | `Long` | `81.35` | 38,800,000.00 USD | 0.00 USD | 82,790.00 USD | `-16.13%` | `1,017.76` |
| `Live` | `Long` | `81.45` | 38,720,000.00 USD | 0.00 USD | 52,940.00 USD | `-16.03%` | `650.01` |
| `Live` | `Long` | `81.55` | 38,660,000.00 USD | 0.00 USD | 24,420.00 USD | `-15.93%` | `299.49` |
| `Live` | `Long` | `81.65` | 38,640,000.00 USD | 0.00 USD | 15,000.00 USD | `-15.82%` | `183.66` |
| `Live` | `Long` | `81.75` | 38,620,000.00 USD | 0.00 USD | 75,320.00 USD | `-15.72%` | `921.36` |
| `Live` | `Long` | `81.85` | 38,550,000.00 USD | 0.00 USD | 39,230.00 USD | `-15.62%` | `479.33` |
| `Live` | `Long` | `81.95` | 38,510,000.00 USD | 0.00 USD | 16,500.00 USD | `-15.51%` | `201.33` |
| `Live` | `Long` | `82.05` | 38,490,000.00 USD | 0.00 USD | 194,170.00 USD | `-15.41%` | `2,366.46` |
| `Live` | `Long` | `82.15` | 38,300,000.00 USD | 0.00 USD | 820,980.00 USD | `-15.31%` | `9,993.70` |
| `Live` | `Long` | `82.25` | 37,480,000.00 USD | 0.00 USD | 178,730.00 USD | `-15.20%` | `2,172.99` |
| `Live` | `Long` | `82.35` | 37,300,000.00 USD | 0.00 USD | 17,800.00 USD | `-15.10%` | `216.10` |
| `Live` | `Long` | `82.45` | 37,280,000.00 USD | 0.00 USD | 942,960.00 USD | `-15.00%` | `11,436.75` |
| `Live` | `Long` | `82.55` | 36,340,000.00 USD | 0.00 USD | 19,560.00 USD | `-14.90%` | `236.89` |
| `Live` | `Long` | `82.65` | 36,320,000.00 USD | 0.00 USD | 113,280.00 USD | `-14.79%` | `1,370.58` |
| `Live` | `Long` | `82.75` | 36,210,000.00 USD | 0.00 USD | 32,290.00 USD | `-14.69%` | `390.25` |
| `Live` | `Long` | `82.85` | 36,170,000.00 USD | 0.00 USD | 33,790.00 USD | `-14.59%` | `407.81` |
| `Live` | `Long` | `82.95` | 36,140,000.00 USD | 0.00 USD | 16,780.00 USD | `-14.48%` | `202.25` |
| `Live` | `Long` | `83.05` | 36,120,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-14.38%` | `20,662.27` |
| `Live` | `Long` | `83.15` | 34,410,000.00 USD | 0.00 USD | 9,950.00 USD | `-14.28%` | `119.64` |
| `Live` | `Long` | `83.25` | 34,400,000.00 USD | 0.00 USD | 18,550.00 USD | `-14.17%` | `222.81` |
| `Live` | `Long` | `83.35` | 34,380,000.00 USD | 0.00 USD | 52,990.00 USD | `-14.07%` | `635.70` |
| `Live` | `Long` | `83.45` | 34,330,000.00 USD | 0.00 USD | 33,610.00 USD | `-13.97%` | `402.73` |
| `Live` | `Long` | `83.55` | 34,290,000.00 USD | 0.00 USD | 14,940.00 USD | `-13.86%` | `178.87` |
| `Live` | `Long` | `83.65` | 34,280,000.00 USD | 0.00 USD | 68,300.00 USD | `-13.76%` | `816.53` |
| `Live` | `Long` | `83.75` | 34,210,000.00 USD | 0.00 USD | 67,930.00 USD | `-13.66%` | `811.08` |
| `Live` | `Long` | `83.85` | 34,140,000.00 USD | 0.00 USD | 218,530.00 USD | `-13.55%` | `2,606.22` |
| `Live` | `Long` | `83.95` | 33,920,000.00 USD | 0.00 USD | 33,800.00 USD | `-13.45%` | `402.64` |
| `Live` | `Long` | `84.05` | 33,890,000.00 USD | 0.00 USD | 169,380.00 USD | `-13.35%` | `2,015.26` |
| `Live` | `Long` | `84.15` | 33,720,000.00 USD | 0.00 USD | 73,730.00 USD | `-13.25%` | `876.14` |
| `Live` | `Long` | `84.25` | 33,650,000.00 USD | 0.00 USD | 46,100.00 USD | `-13.14%` | `547.21` |
| `Live` | `Long` | `84.35` | 33,600,000.00 USD | 0.00 USD | 37,480.00 USD | `-13.04%` | `444.37` |
| `Live` | `Long` | `84.45` | 33,560,000.00 USD | 0.00 USD | 84,930.00 USD | `-12.94%` | `1,005.69` |
| `Live` | `Long` | `84.55` | 33,480,000.00 USD | 0.00 USD | 29,050.00 USD | `-12.83%` | `343.56` |
| `Live` | `Long` | `84.65` | 33,450,000.00 USD | 0.00 USD | 70,830.00 USD | `-12.73%` | `836.77` |
| `Live` | `Long` | `84.75` | 33,380,000.00 USD | 0.00 USD | 101,570.00 USD | `-12.63%` | `1,198.42` |
| `Live` | `Long` | `84.85` | 33,280,000.00 USD | 0.00 USD | 6,320.00 USD | `-12.52%` | `74.50` |
| `Live` | `Long` | `84.95` | 33,270,000.00 USD | 0.00 USD | 6,850.00 USD | `-12.42%` | `80.67` |
| `Live` | `Long` | `85.05` | 33,260,000.00 USD | 0.00 USD | 23,090.00 USD | `-12.32%` | `271.48` |
| `Live` | `Long` | `85.15` | 33,240,000.00 USD | 0.00 USD | 88,300.00 USD | `-12.21%` | `1,037.05` |
| `Live` | `Long` | `85.25` | 33,150,000.00 USD | 0.00 USD | 568,790.00 USD | `-12.11%` | `6,672.08` |
| `Live` | `Long` | `85.35` | 32,580,000.00 USD | 0.00 USD | 76,700.00 USD | `-12.01%` | `898.62` |
| `Live` | `Long` | `85.45` | 32,510,000.00 USD | 0.00 USD | 29,720.00 USD | `-11.91%` | `347.84` |
| `Live` | `Long` | `85.55` | 32,480,000.00 USD | 0.00 USD | 23,930.00 USD | `-11.80%` | `279.70` |
| `Live` | `Long` | `85.65` | 32,450,000.00 USD | 0.00 USD | 24,200.00 USD | `-11.70%` | `282.60` |
| `Live` | `Long` | `85.75` | 32,430,000.00 USD | 0.00 USD | 6,530.00 USD | `-11.60%` | `76.14` |
| `Live` | `Long` | `85.85` | 32,420,000.00 USD | 0.00 USD | 45,860.00 USD | `-11.49%` | `534.16` |
| `Live` | `Long` | `85.95` | 32,380,000.00 USD | 0.00 USD | 21,790.00 USD | `-11.39%` | `253.47` |
| `Live` | `Long` | `86.05` | 32,350,000.00 USD | 0.00 USD | 81,030.00 USD | `-11.29%` | `941.68` |
| `Live` | `Long` | `86.15` | 32,270,000.00 USD | 0.00 USD | 113,140.00 USD | `-11.18%` | `1,313.26` |
| `Live` | `Long` | `86.25` | 32,160,000.00 USD | 0.00 USD | 22,610.00 USD | `-11.08%` | `262.17` |
| `Live` | `Long` | `86.35` | 32,140,000.00 USD | 0.00 USD | 19,600.00 USD | `-10.98%` | `226.98` |
| `Live` | `Long` | `86.45` | 32,120,000.00 USD | 0.00 USD | 34,920.00 USD | `-10.87%` | `403.96` |
| `Live` | `Long` | `86.55` | 32,080,000.00 USD | 0.00 USD | 22,090.00 USD | `-10.77%` | `255.26` |
| `Live` | `Long` | `86.65` | 32,060,000.00 USD | 0.00 USD | 114,160.00 USD | `-10.67%` | `1,317.49` |
| `Live` | `Long` | `86.75` | 31,950,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-10.57%` | `14,768.99` |
| `Live` | `Long` | `86.85` | 30,660,000.00 USD | 0.00 USD | 64,270.00 USD | `-10.46%` | `740.03` |
| `Live` | `Long` | `86.95` | 30,600,000.00 USD | 0.00 USD | 84,500.00 USD | `-10.36%` | `971.83` |
| `Live` | `Long` | `87.05` | 30,520,000.00 USD | 0.00 USD | 278,840.00 USD | `-10.26%` | `3,203.27` |
| `Live` | `Long` | `87.15` | 30,240,000.00 USD | 0.00 USD | 322,190.00 USD | `-10.15%` | `3,697.01` |
| `Live` | `Long` | `87.25` | 29,910,000.00 USD | 0.00 USD | 16,540.00 USD | `-10.05%` | `189.55` |
| `Live` | `Long` | `87.35` | 29,900,000.00 USD | 0.00 USD | 35,940.00 USD | `-9.95%` | `411.45` |
| `Live` | `Long` | `87.45` | 29,860,000.00 USD | 0.00 USD | 561,270.00 USD | `-9.84%` | `6,418.17` |
| `Live` | `Long` | `87.55` | 29,300,000.00 USD | 0.00 USD | 172,150.00 USD | `-9.74%` | `1,966.30` |
| `Live` | `Long` | `87.65` | 29,130,000.00 USD | 0.00 USD | 547,570.00 USD | `-9.64%` | `6,247.27` |
| `Live` | `Long` | `87.75` | 28,580,000.00 USD | 0.00 USD | 24,600.00 USD | `-9.53%` | `280.36` |
| `Live` | `Long` | `87.85` | 28,560,000.00 USD | 0.00 USD | 27,330.00 USD | `-9.43%` | `311.09` |
| `Live` | `Long` | `87.95` | 28,530,000.00 USD | 0.00 USD | 7,180.00 USD | `-9.33%` | `81.67` |
| `Live` | `Long` | `88.05` | 28,520,000.00 USD | 0.00 USD | 43,330.00 USD | `-9.22%` | `492.09` |
| `Live` | `Long` | `88.15` | 28,480,000.00 USD | 0.00 USD | 6,610.00 USD | `-9.12%` | `75.01` |
| `Live` | `Long` | `88.25` | 28,470,000.00 USD | 0.00 USD | 213,270.00 USD | `-9.02%` | `2,416.70` |
| `Live` | `Long` | `88.35` | 28,260,000.00 USD | 0.00 USD | 99,390.00 USD | `-8.92%` | `1,125.00` |
| `Live` | `Long` | `88.45` | 28,160,000.00 USD | 0.00 USD | 97,600.00 USD | `-8.81%` | `1,103.45` |
| `Live` | `Long` | `88.55` | 28,060,000.00 USD | 0.00 USD | 216,000.00 USD | `-8.71%` | `2,439.26` |
| `Live` | `Long` | `88.65` | 27,850,000.00 USD | 0.00 USD | 142,310.00 USD | `-8.61%` | `1,605.31` |
| `Live` | `Long` | `88.75` | 27,700,000.00 USD | 0.00 USD | 159,100.00 USD | `-8.50%` | `1,792.69` |
| `Live` | `Long` | `88.85` | 27,540,000.00 USD | 0.00 USD | 869,300.00 USD | `-8.40%` | `9,783.96` |
| `Live` | `Long` | `88.95` | 26,680,000.00 USD | 0.00 USD | 197,960.00 USD | `-8.30%` | `2,225.51` |
| `Live` | `Long` | `89.05` | 26,480,000.00 USD | 0.00 USD | 229,790.00 USD | `-8.19%` | `2,580.50` |
| `Live` | `Long` | `89.15` | 26,250,000.00 USD | 0.00 USD | 106,420.00 USD | `-8.09%` | `1,193.75` |
| `Live` | `Long` | `89.25` | 26,140,000.00 USD | 0.00 USD | 172,000.00 USD | `-7.99%` | `1,927.18` |
| `Live` | `Long` | `89.35` | 25,970,000.00 USD | 0.00 USD | 73,440.00 USD | `-7.88%` | `821.99` |
| `Live` | `Long` | `89.45` | 25,900,000.00 USD | 0.00 USD | 381,100.00 USD | `-7.78%` | `4,260.50` |
| `Live` | `Long` | `89.55` | 25,510,000.00 USD | 0.00 USD | 35,920.00 USD | `-7.68%` | `401.11` |
| `Live` | `Long` | `89.65` | 25,480,000.00 USD | 0.00 USD | 15,660.00 USD | `-7.58%` | `174.68` |
| `Live` | `Long` | `89.75` | 25,460,000.00 USD | 0.00 USD | 82,300.00 USD | `-7.47%` | `917.02` |
| `Live` | `Long` | `89.85` | 25,380,000.00 USD | 0.00 USD | 137,070.00 USD | `-7.37%` | `1,525.59` |
| `Live` | `Long` | `89.95` | 25,240,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-7.27%` | `16,994.09` |
| `Live` | `Long` | `90.05` | 23,710,000.00 USD | 0.00 USD | 80,380.00 USD | `-7.16%` | `892.64` |
| `Live` | `Long` | `90.15` | 23,630,000.00 USD | 0.00 USD | 30,220.00 USD | `-7.06%` | `335.26` |
| `Live` | `Long` | `90.25` | 23,600,000.00 USD | 0.00 USD | 40,030.00 USD | `-6.96%` | `443.50` |
| `Live` | `Long` | `90.35` | 23,560,000.00 USD | 0.00 USD | 60,740.00 USD | `-6.85%` | `672.27` |
| `Live` | `Long` | `90.45` | 23,500,000.00 USD | 0.00 USD | 186,630.00 USD | `-6.75%` | `2,063.30` |
| `Live` | `Long` | `90.55` | 23,320,000.00 USD | 0.00 USD | 16,730.00 USD | `-6.65%` | `184.80` |
| `Live` | `Long` | `90.65` | 23,300,000.00 USD | 0.00 USD | 86,440.00 USD | `-6.54%` | `953.52` |
| `Live` | `Long` | `90.75` | 23,210,000.00 USD | 0.00 USD | 318,210.00 USD | `-6.44%` | `3,506.49` |
| `Live` | `Long` | `90.85` | 22,900,000.00 USD | 0.00 USD | 79,380.00 USD | `-6.34%` | `873.80` |
| `Live` | `Long` | `90.95` | 22,820,000.00 USD | 0.00 USD | 55,040.00 USD | `-6.24%` | `605.18` |
| `Live` | `Long` | `91.05` | 22,760,000.00 USD | 0.00 USD | 795,510.00 USD | `-6.13%` | `8,737.07` |
| `Live` | `Long` | `91.15` | 21,970,000.00 USD | 0.00 USD | 268,870.00 USD | `-6.03%` | `2,949.75` |
| `Live` | `Long` | `91.25` | 21,700,000.00 USD | 0.00 USD | 14,410.00 USD | `-5.93%` | `157.97` |
| `Live` | `Long` | `91.35` | 21,680,000.00 USD | 0.00 USD | 52,380.00 USD | `-5.82%` | `573.38` |
| `Live` | `Long` | `91.45` | 21,630,000.00 USD | 0.00 USD | 34,730.00 USD | `-5.72%` | `379.82` |
| `Live` | `Long` | `91.55` | 21,600,000.00 USD | 0.00 USD | 3,660,000.00 USD | `-5.62%` | `39,953.20` |
| `Live` | `Long` | `91.65` | 17,940,000.00 USD | 0.00 USD | 100,830.00 USD | `-5.51%` | `1,100.20` |
| `Live` | `Long` | `91.75` | 17,840,000.00 USD | 0.00 USD | 369,520.00 USD | `-5.41%` | `4,027.44` |
| `Live` | `Long` | `91.85` | 17,470,000.00 USD | 0.00 USD | 33,220.00 USD | `-5.31%` | `361.68` |
| `Live` | `Long` | `91.95` | 17,430,000.00 USD | 0.00 USD | 135,060.00 USD | `-5.20%` | `1,468.81` |
| `Live` | `Long` | `92.05` | 17,300,000.00 USD | 0.00 USD | 26,270.00 USD | `-5.10%` | `285.38` |
| `Live` | `Long` | `92.15` | 17,270,000.00 USD | 0.00 USD | 282,170.00 USD | `-5.00%` | `3,062.08` |
| `Live` | `Long` | `92.25` | 16,990,000.00 USD | 0.00 USD | 63,300.00 USD | `-4.89%` | `686.21` |
| `Live` | `Long` | `92.35` | 16,930,000.00 USD | 0.00 USD | 63,890.00 USD | `-4.79%` | `691.79` |
| `Live` | `Long` | `92.45` | 16,860,000.00 USD | 0.00 USD | 266,080.00 USD | `-4.69%` | `2,878.12` |
| `Live` | `Long` | `92.55` | 16,600,000.00 USD | 0.00 USD | 231,210.00 USD | `-4.59%` | `2,498.24` |
| `Live` | `Long` | `92.65` | 16,370,000.00 USD | 0.00 USD | 457,210.00 USD | `-4.48%` | `4,934.85` |
| `Live` | `Long` | `92.75` | 15,910,000.00 USD | 0.00 USD | 451,380.00 USD | `-4.38%` | `4,866.66` |
| `Live` | `Long` | `92.85` | 15,460,000.00 USD | 0.00 USD | 573,950.00 USD | `-4.28%` | `6,181.44` |
| `Live` | `Long` | `92.95` | 14,880,000.00 USD | 0.00 USD | 95,470.00 USD | `-4.17%` | `1,027.16` |
| `Live` | `Long` | `93.05` | 14,790,000.00 USD | 0.00 USD | 70,070.00 USD | `-4.07%` | `753.03` |
| `Live` | `Long` | `93.15` | 14,720,000.00 USD | 0.00 USD | 102,340.00 USD | `-3.97%` | `1,098.68` |
| `Live` | `Long` | `93.25` | 14,620,000.00 USD | 0.00 USD | 103,200.00 USD | `-3.86%` | `1,106.74` |
| `Live` | `Long` | `93.35` | 14,510,000.00 USD | 0.00 USD | 198,270.00 USD | `-3.76%` | `2,123.91` |
| `Live` | `Long` | `93.45` | 14,310,000.00 USD | 0.00 USD | 554,280.00 USD | `-3.66%` | `5,931.27` |
| `Live` | `Long` | `93.55` | 13,760,000.00 USD | 0.00 USD | 439,100.00 USD | `-3.55%` | `4,693.77` |
| `Live` | `Long` | `93.65` | 13,320,000.00 USD | 0.00 USD | 369,230.00 USD | `-3.45%` | `3,942.67` |
| `Live` | `Long` | `93.75` | 12,950,000.00 USD | 0.00 USD | 138,540.00 USD | `-3.35%` | `1,477.73` |
| `Live` | `Long` | `93.85` | 12,810,000.00 USD | 0.00 USD | 558,560.00 USD | `-3.25%` | `5,951.66` |
| `Live` | `Long` | `93.95` | 12,250,000.00 USD | 0.00 USD | 377,350.00 USD | `-3.14%` | `4,016.51` |
| `Live` | `Long` | `94.05` | 11,880,000.00 USD | 0.00 USD | 240,430.00 USD | `-3.04%` | `2,556.40` |
| `Live` | `Long` | `94.15` | 11,640,000.00 USD | 0.00 USD | 198,390.00 USD | `-2.94%` | `2,107.20` |
| `Live` | `Long` | `94.25` | 11,440,000.00 USD | 0.00 USD | 33,840.00 USD | `-2.83%` | `359.06` |
| `Live` | `Long` | `94.35` | 11,400,000.00 USD | 0.00 USD | 205,690.00 USD | `-2.73%` | `2,180.10` |
| `Live` | `Long` | `94.45` | 11,200,000.00 USD | 0.00 USD | 991,720.00 USD | `-2.63%` | `10,499.90` |
| `Live` | `Long` | `94.55` | 10,210,000.00 USD | 0.00 USD | 305,740.00 USD | `-2.52%` | `3,233.63` |
| `Live` | `Long` | `94.65` | 9,900,000.00 USD | 0.00 USD | 8,570,000.00 USD | `-2.42%` | `90,498.04` |
| `Live` | `Long` | `94.75` | 1,340,000.00 USD | 0.00 USD | 133,210.00 USD | `-2.32%` | `1,405.87` |
| `Live` | `Long` | `94.85` | 1,200,000.00 USD | 0.00 USD | 366,250.00 USD | `-2.21%` | `3,861.35` |
| `Live` | `Long` | `94.95` | 836,130.00 USD | 0.00 USD | 432,730.00 USD | `-2.11%` | `4,557.43` |
| `Live` | `Long` | `95.05` | 403,400.00 USD | 0.00 USD | 56,670.00 USD | `-2.01%` | `596.19` |
| `Live` | `Long` | `95.15` | 346,740.00 USD | 0.00 USD | 139,650.00 USD | `-1.91%` | `1,467.65` |
| `Live` | `Long` | `95.25` | 207,090.00 USD | 0.00 USD | 158,140.00 USD | `-1.80%` | `1,660.23` |
| `Live` | `Long` | `95.35` | 48,950.00 USD | 0.00 USD | 33,720.00 USD | `-1.70%` | `353.63` |
| `Live` | `Long` | `95.45` | 15,230.00 USD | 0.00 USD | 7,630.00 USD | `-1.60%` | `79.97` |
| `Live` | `Long` | `95.55` | 7,600.00 USD | 0.00 USD | 3,280.00 USD | `-1.49%` | `34.36` |
| `Live` | `Long` | `95.85` | 4,320.00 USD | 0.00 USD | 4,030.00 USD | `-1.18%` | `42.01` |
| `Live` | `Long` | `96.35` | 290.98 USD | 0.00 USD | 290.98 USD | `-0.67%` | `3.02` |
| `Live` | `Short` | `97.15` | 1,260.00 USD | 1,260.00 USD | 0.00 USD | `+0.16%` | `12.95` |
| `Live` | `Short` | `97.35` | 20,920.00 USD | 19,660.00 USD | 0.00 USD | `+0.36%` | `201.97` |
| `Live` | `Short` | `97.55` | 21,930.00 USD | 1,010.00 USD | 0.00 USD | `+0.57%` | `10.37` |
| `Live` | `Short` | `98.55` | 22,540.00 USD | 604.11 USD | 0.00 USD | `+1.60%` | `6.13` |
| `Live` | `Short` | `98.85` | 24,730.00 USD | 2,190.00 USD | 0.00 USD | `+1.91%` | `22.19` |
| `Live` | `Short` | `99.05` | 27,080.00 USD | 2,350.00 USD | 0.00 USD | `+2.12%` | `23.76` |
| `Live` | `Short` | `99.15` | 212,930.00 USD | 185,850.00 USD | 0.00 USD | `+2.22%` | `1,874.42` |
| `Live` | `Short` | `99.25` | 270,290.00 USD | 57,360.00 USD | 0.00 USD | `+2.32%` | `577.89` |
| `Live` | `Short` | `99.35` | 335,870.00 USD | 65,580.00 USD | 0.00 USD | `+2.42%` | `660.13` |
| `Live` | `Short` | `99.45` | 378,200.00 USD | 42,320.00 USD | 0.00 USD | `+2.53%` | `425.59` |
| `Live` | `Short` | `99.55` | 378,700.00 USD | 508.70 USD | 0.00 USD | `+2.63%` | `5.11` |
| `Live` | `Short` | `99.65` | 395,880.00 USD | 17,170.00 USD | 0.00 USD | `+2.73%` | `172.34` |
| `Live` | `Short` | `99.75` | 561,370.00 USD | 165,500.00 USD | 0.00 USD | `+2.84%` | `1,659.10` |
| `Live` | `Short` | `99.85` | 595,800.00 USD | 34,420.00 USD | 0.00 USD | `+2.94%` | `344.76` |
| `Live` | `Short` | `99.95` | 1,020,000.00 USD | 422,380.00 USD | 0.00 USD | `+3.04%` | `4,225.96` |
| `Live` | `Short` | `100.05` | 1,030,000.00 USD | 7,120.00 USD | 0.00 USD | `+3.15%` | `71.18` |
| `Live` | `Short` | `100.15` | 1,040,000.00 USD | 18,360.00 USD | 0.00 USD | `+3.25%` | `183.30` |
| `Live` | `Short` | `100.35` | 1,040,000.00 USD | 799.79 USD | 0.00 USD | `+3.46%` | `7.97` |
| `Live` | `Short` | `100.65` | 1,050,000.00 USD | 1,680.00 USD | 0.00 USD | `+3.77%` | `16.69` |
| `Live` | `Short` | `100.75` | 1,080,000.00 USD | 31,580.00 USD | 0.00 USD | `+3.87%` | `313.47` |
| `Live` | `Short` | `100.85` | 2,140,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+3.97%` | `10,525.44` |
| `Live` | `Short` | `100.95` | 2,150,000.00 USD | 6,290.00 USD | 0.00 USD | `+4.07%` | `62.29` |
| `Live` | `Short` | `101.05` | 2,170,000.00 USD | 20,440.00 USD | 0.00 USD | `+4.18%` | `202.28` |
| `Live` | `Short` | `101.15` | 2,180,000.00 USD | 18,750.00 USD | 0.00 USD | `+4.28%` | `185.38` |
| `Live` | `Short` | `101.25` | 2,190,000.00 USD | 1,210.00 USD | 0.00 USD | `+4.38%` | `11.99` |
| `Live` | `Short` | `101.35` | 2,240,000.00 USD | 51,620.00 USD | 0.00 USD | `+4.49%` | `509.37` |
| `Live` | `Short` | `101.55` | 2,240,000.00 USD | 814.43 USD | 0.00 USD | `+4.69%` | `8.02` |
| `Live` | `Short` | `101.65` | 2,240,000.00 USD | 1,820.00 USD | 0.00 USD | `+4.80%` | `17.95` |
| `Live` | `Short` | `102.05` | 2,240,000.00 USD | 4,690.00 USD | 0.00 USD | `+5.21%` | `45.92` |
| `Live` | `Short` | `102.35` | 2,250,000.00 USD | 6,240.00 USD | 0.00 USD | `+5.52%` | `60.95` |
| `Live` | `Short` | `102.45` | 2,250,000.00 USD | 421.07 USD | 0.00 USD | `+5.62%` | `4.11` |
| `Live` | `Short` | `102.65` | 2,250,000.00 USD | 872.53 USD | 0.00 USD | `+5.83%` | `8.50` |
| `Live` | `Short` | `102.95` | 2,260,000.00 USD | 3,080.00 USD | 0.00 USD | `+6.14%` | `29.92` |
| `Live` | `Short` | `103.05` | 2,260,000.00 USD | 2,980.00 USD | 0.00 USD | `+6.24%` | `28.89` |
| `Live` | `Short` | `103.15` | 2,270,000.00 USD | 11,000.00 USD | 0.00 USD | `+6.34%` | `106.62` |
| `Live` | `Short` | `103.25` | 2,280,000.00 USD | 9,960.00 USD | 0.00 USD | `+6.45%` | `96.47` |
| `Live` | `Short` | `103.35` | 2,280,000.00 USD | 530.19 USD | 0.00 USD | `+6.55%` | `5.13` |
| `Live` | `Short` | `103.55` | 2,280,000.00 USD | 2,680.00 USD | 0.00 USD | `+6.75%` | `25.89` |
| `Live` | `Short` | `103.65` | 2,280,000.00 USD | 1,040.00 USD | 0.00 USD | `+6.86%` | `10.00` |
| `Live` | `Short` | `103.75` | 2,290,000.00 USD | 4,000.00 USD | 0.00 USD | `+6.96%` | `38.53` |
| `Live` | `Short` | `103.85` | 2,300,000.00 USD | 14,170.00 USD | 0.00 USD | `+7.06%` | `136.46` |
| `Live` | `Short` | `103.95` | 2,310,000.00 USD | 8,540.00 USD | 0.00 USD | `+7.17%` | `82.12` |
| `Live` | `Short` | `104.05` | 2,310,000.00 USD | 877.14 USD | 0.00 USD | `+7.27%` | `8.43` |
| `Live` | `Short` | `104.15` | 2,310,000.00 USD | 1,060.00 USD | 0.00 USD | `+7.37%` | `10.20` |
| `Live` | `Short` | `104.25` | 2,350,000.00 USD | 37,460.00 USD | 0.00 USD | `+7.48%` | `359.31` |
| `Live` | `Short` | `104.35` | 2,350,000.00 USD | 3,740.00 USD | 0.00 USD | `+7.58%` | `35.81` |
| `Live` | `Short` | `104.45` | 2,360,000.00 USD | 7,090.00 USD | 0.00 USD | `+7.68%` | `67.90` |
| `Live` | `Short` | `104.55` | 2,370,000.00 USD | 11,290.00 USD | 0.00 USD | `+7.79%` | `107.95` |
| `Live` | `Short` | `104.65` | 3,000,000.00 USD | 632,260.00 USD | 0.00 USD | `+7.89%` | `6,041.63` |
| `Live` | `Short` | `104.75` | 3,000,000.00 USD | 199.02 USD | 0.00 USD | `+7.99%` | `1.90` |
| `Live` | `Short` | `104.95` | 3,050,000.00 USD | 50,510.00 USD | 0.00 USD | `+8.20%` | `481.32` |
| `Live` | `Short` | `105.05` | 3,060,000.00 USD | 1,200.00 USD | 0.00 USD | `+8.30%` | `11.44` |
| `Live` | `Short` | `105.25` | 3,060,000.00 USD | 2,300.00 USD | 0.00 USD | `+8.51%` | `21.87` |
| `Live` | `Short` | `105.35` | 3,060,000.00 USD | 4,800.00 USD | 0.00 USD | `+8.61%` | `45.56` |
| `Live` | `Short` | `105.45` | 3,700,000.00 USD | 636,160.00 USD | 0.00 USD | `+8.71%` | `6,032.82` |
| `Live` | `Short` | `105.55` | 3,710,000.00 USD | 6,290.00 USD | 0.00 USD | `+8.82%` | `59.61` |
| `Live` | `Short` | `105.65` | 3,710,000.00 USD | 1,060.00 USD | 0.00 USD | `+8.92%` | `10.00` |
| `Live` | `Short` | `105.95` | 3,710,000.00 USD | 266.99 USD | 0.00 USD | `+9.23%` | `2.52` |
| `Live` | `Short` | `106.05` | 3,710,000.00 USD | 1,420.00 USD | 0.00 USD | `+9.33%` | `13.39` |
| `Live` | `Short` | `106.15` | 3,710,000.00 USD | 4,350.00 USD | 0.00 USD | `+9.44%` | `40.95` |
| `Live` | `Short` | `106.25` | 3,710,000.00 USD | 819.19 USD | 0.00 USD | `+9.54%` | `7.71` |
| `Live` | `Short` | `106.35` | 3,770,000.00 USD | 53,990.00 USD | 0.00 USD | `+9.64%` | `507.65` |
| `Live` | `Short` | `106.45` | 3,770,000.00 USD | 6,370.00 USD | 0.00 USD | `+9.74%` | `59.84` |
| `Live` | `Short` | `106.85` | 4,250,000.00 USD | 478,970.00 USD | 0.00 USD | `+10.16%` | `4,482.65` |
| `Live` | `Short` | `106.95` | 4,250,000.00 USD | 291.97 USD | 0.00 USD | `+10.26%` | `2.73` |
| `Live` | `Short` | `107.05` | 4,270,000.00 USD | 15,740.00 USD | 0.00 USD | `+10.36%` | `147.04` |
| `Live` | `Short` | `107.25` | 4,300,000.00 USD | 36,010.00 USD | 0.00 USD | `+10.57%` | `335.77` |
| `Live` | `Short` | `107.35` | 4,500,000.00 USD | 197,950.00 USD | 0.00 USD | `+10.67%` | `1,843.95` |
| `Live` | `Short` | `107.45` | 4,560,000.00 USD | 53,960.00 USD | 0.00 USD | `+10.78%` | `502.17` |
| `Live` | `Short` | `107.65` | 4,560,000.00 USD | 1,820.00 USD | 0.00 USD | `+10.98%` | `16.87` |
| `Live` | `Short` | `107.75` | 4,560,000.00 USD | 5,840.00 USD | 0.00 USD | `+11.08%` | `54.18` |
| `Live` | `Short` | `107.85` | 4,560,000.00 USD | 106.77 USD | 0.00 USD | `+11.19%` | `0.99` |
| `Live` | `Short` | `108.05` | 4,570,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.39%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,570,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.50%` | `10.66` |
| `Live` | `Short` | `108.35` | 4,580,000.00 USD | 13,880.00 USD | 0.00 USD | `+11.70%` | `128.09` |
| `Live` | `Short` | `108.45` | 4,700,000.00 USD | 119,130.00 USD | 0.00 USD | `+11.81%` | `1,098.52` |
| `Live` | `Short` | `108.55` | 4,700,000.00 USD | 117.23 USD | 0.00 USD | `+11.91%` | `1.08` |
| `Live` | `Short` | `108.65` | 4,700,000.00 USD | 5,050.00 USD | 0.00 USD | `+12.01%` | `46.45` |
| `Live` | `Short` | `108.75` | 4,710,000.00 USD | 188.14 USD | 0.00 USD | `+12.12%` | `1.73` |
| `Live` | `Short` | `108.85` | 4,710,000.00 USD | 3,230.00 USD | 0.00 USD | `+12.22%` | `29.68` |
| `Live` | `Short` | `108.95` | 4,710,000.00 USD | 3,740.00 USD | 0.00 USD | `+12.32%` | `34.31` |
| `Live` | `Short` | `109.15` | 4,730,000.00 USD | 22,380.00 USD | 0.00 USD | `+12.53%` | `205.03` |
| `Live` | `Short` | `109.25` | 4,740,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.63%` | `9.76` |
| `Live` | `Short` | `109.35` | 4,740,000.00 USD | 247.13 USD | 0.00 USD | `+12.73%` | `2.26` |
| `Live` | `Short` | `109.45` | 4,840,000.00 USD | 105,660.00 USD | 0.00 USD | `+12.84%` | `965.36` |
| `Live` | `Short` | `109.55` | 4,840,000.00 USD | 461.21 USD | 0.00 USD | `+12.94%` | `4.21` |
| `Live` | `Short` | `109.65` | 4,880,000.00 USD | 42,990.00 USD | 0.00 USD | `+13.04%` | `392.09` |
| `Live` | `Short` | `109.75` | 4,890,000.00 USD | 256.81 USD | 0.00 USD | `+13.15%` | `2.34` |
| `Live` | `Short` | `109.85` | 4,890,000.00 USD | 572.32 USD | 0.00 USD | `+13.25%` | `5.21` |
| `Live` | `Short` | `109.95` | 4,890,000.00 USD | 537.66 USD | 0.00 USD | `+13.35%` | `4.89` |
| `Live` | `Short` | `110.15` | 4,890,000.00 USD | 194.97 USD | 0.00 USD | `+13.56%` | `1.77` |
| `Live` | `Short` | `110.25` | 4,890,000.00 USD | 218.29 USD | 0.00 USD | `+13.66%` | `1.98` |
| `Live` | `Short` | `110.35` | 5,420,000.00 USD | 534,860.00 USD | 0.00 USD | `+13.77%` | `4,846.90` |
| `Live` | `Short` | `110.45` | 5,440,000.00 USD | 16,940.00 USD | 0.00 USD | `+13.87%` | `153.41` |
| `Live` | `Short` | `110.55` | 5,440,000.00 USD | 203.41 USD | 0.00 USD | `+13.97%` | `1.84` |
| `Live` | `Short` | `110.65` | 5,440,000.00 USD | 112.86 USD | 0.00 USD | `+14.07%` | `1.02` |
| `Live` | `Short` | `110.75` | 5,440,000.00 USD | 575.90 USD | 0.00 USD | `+14.18%` | `5.20` |
| `Live` | `Short` | `110.85` | 5,440,000.00 USD | 103.09 USD | 0.00 USD | `+14.28%` | `0.93` |
| `Live` | `Short` | `110.95` | 5,450,000.00 USD | 12,860.00 USD | 0.00 USD | `+14.38%` | `115.95` |
| `Live` | `Short` | `111.05` | 5,460,000.00 USD | 8,630.00 USD | 0.00 USD | `+14.49%` | `77.74` |
| `Live` | `Short` | `111.15` | 5,460,000.00 USD | 1,710.00 USD | 0.00 USD | `+14.59%` | `15.37` |
| `Live` | `Short` | `111.25` | 5,460,000.00 USD | 196.91 USD | 0.00 USD | `+14.69%` | `1.77` |
| `Live` | `Short` | `111.35` | 5,460,000.00 USD | 390.84 USD | 0.00 USD | `+14.80%` | `3.51` |
| `Live` | `Short` | `111.45` | 5,460,000.00 USD | 841.45 USD | 0.00 USD | `+14.90%` | `7.55` |
| `Live` | `Short` | `111.55` | 5,470,000.00 USD | 2,780.00 USD | 0.00 USD | `+15.00%` | `24.90` |
| `Live` | `Short` | `111.75` | 5,470,000.00 USD | 339.72 USD | 0.00 USD | `+15.21%` | `3.04` |
| `Live` | `Short` | `111.85` | 5,480,000.00 USD | 15,880.00 USD | 0.00 USD | `+15.31%` | `141.95` |
| `Live` | `Short` | `111.95` | 5,480,000.00 USD | 895.60 USD | 0.00 USD | `+15.41%` | `8.00` |
| `Live` | `Short` | `112.05` | 5,480,000.00 USD | 626.36 USD | 0.00 USD | `+15.52%` | `5.59` |
| `Live` | `Short` | `112.45` | 5,490,000.00 USD | 5,910.00 USD | 0.00 USD | `+15.93%` | `52.53` |
| `Live` | `Short` | `112.55` | 5,490,000.00 USD | 844.13 USD | 0.00 USD | `+16.03%` | `7.50` |
| `Live` | `Short` | `112.65` | 5,490,000.00 USD | 584.65 USD | 0.00 USD | `+16.14%` | `5.19` |
| `Live` | `Short` | `112.75` | 5,610,000.00 USD | 118,640.00 USD | 0.00 USD | `+16.24%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 5,610,000.00 USD | 1,460.00 USD | 0.00 USD | `+16.34%` | `12.91` |
| `Live` | `Short` | `113.05` | 5,880,000.00 USD | 263,100.00 USD | 0.00 USD | `+16.55%` | `2,327.32` |
| `Live` | `Short` | `113.15` | 5,880,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.65%` | `84.51` |
| `Live` | `Short` | `113.25` | 5,880,000.00 USD | 114.38 USD | 0.00 USD | `+16.75%` | `1.01` |
| `Live` | `Short` | `113.45` | 5,990,000.00 USD | 104,430.00 USD | 0.00 USD | `+16.96%` | `920.47` |
| `Live` | `Short` | `113.55` | 6,500,000.00 USD | 515,190.00 USD | 0.00 USD | `+17.06%` | `4,537.14` |
| `Live` | `Short` | `113.65` | 6,510,000.00 USD | 3,220.00 USD | 0.00 USD | `+17.17%` | `28.37` |
| `Live` | `Short` | `113.75` | 6,530,000.00 USD | 22,100.00 USD | 0.00 USD | `+17.27%` | `194.26` |
| `Live` | `Short` | `113.95` | 6,550,000.00 USD | 22,160.00 USD | 0.00 USD | `+17.48%` | `194.45` |
| `Live` | `Short` | `114.05` | 6,570,000.00 USD | 21,420.00 USD | 0.00 USD | `+17.58%` | `187.79` |
| `Live` | `Short` | `114.15` | 6,580,000.00 USD | 2,820.00 USD | 0.00 USD | `+17.68%` | `24.71` |
| `Live` | `Short` | `114.25` | 6,580,000.00 USD | 2,150.00 USD | 0.00 USD | `+17.79%` | `18.80` |
| `Live` | `Short` | `114.45` | 6,580,000.00 USD | 3,050.00 USD | 0.00 USD | `+17.99%` | `26.65` |
| `Live` | `Short` | `114.95` | 6,580,000.00 USD | 496.58 USD | 0.00 USD | `+18.51%` | `4.32` |
| `Live` | `Short` | `115.05` | 7,150,000.00 USD | 569,550.00 USD | 0.00 USD | `+18.61%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 7,150,000.00 USD | 2,360.00 USD | 0.00 USD | `+18.71%` | `20.46` |
| `Live` | `Short` | `115.25` | 7,170,000.00 USD | 18,240.00 USD | 0.00 USD | `+18.82%` | `158.28` |
| `Live` | `Short` | `115.35` | 7,180,000.00 USD | 5,850.00 USD | 0.00 USD | `+18.92%` | `50.73` |
| `Live` | `Short` | `115.45` | 8,060,000.00 USD | 879,040.00 USD | 0.00 USD | `+19.02%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 8,120,000.00 USD | 61,070.00 USD | 0.00 USD | `+19.13%` | `528.48` |
| `Live` | `Short` | `115.75` | 8,120,000.00 USD | 160.89 USD | 0.00 USD | `+19.33%` | `1.39` |
| `Live` | `Short` | `115.85` | 8,120,000.00 USD | 289.62 USD | 0.00 USD | `+19.44%` | `2.50` |
| `Live` | `Short` | `116.05` | 8,120,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.64%` | `38.34` |
| `Live` | `Short` | `116.25` | 8,120,000.00 USD | 180.19 USD | 0.00 USD | `+19.85%` | `1.55` |
| `Live` | `Short` | `116.35` | 8,130,000.00 USD | 4,960.00 USD | 0.00 USD | `+19.95%` | `42.60` |
| `Live` | `Short` | `116.45` | 8,130,000.00 USD | 716.17 USD | 0.00 USD | `+20.05%` | `6.15` |
| `Live` | `Short` | `116.55` | 8,130,000.00 USD | 2,780.00 USD | 0.00 USD | `+20.16%` | `23.86` |
| `Live` | `Short` | `116.65` | 8,130,000.00 USD | 113.15 USD | 0.00 USD | `+20.26%` | `0.97` |
| `Live` | `Short` | `116.75` | 8,160,000.00 USD | 31,740.00 USD | 0.00 USD | `+20.36%` | `271.88` |
| `Live` | `Short` | `117.05` | 8,160,000.00 USD | 156.85 USD | 0.00 USD | `+20.67%` | `1.34` |
| `Live` | `Short` | `117.15` | 8,190,000.00 USD | 23,970.00 USD | 0.00 USD | `+20.78%` | `204.62` |
| `Live` | `Short` | `117.35` | 8,190,000.00 USD | 230.01 USD | 0.00 USD | `+20.98%` | `1.96` |
| `Live` | `Short` | `117.45` | 8,190,000.00 USD | 128.02 USD | 0.00 USD | `+21.08%` | `1.09` |
| `Live` | `Short` | `117.75` | 12,840,000.00 USD | 4,650,000.00 USD | 0.00 USD | `+21.39%` | `39,522.70` |
| `Live` | `Short` | `117.95` | 12,840,000.00 USD | 353.85 USD | 0.00 USD | `+21.60%` | `3.00` |
| `Live` | `Short` | `118.45` | 12,870,000.00 USD | 30,080.00 USD | 0.00 USD | `+22.12%` | `253.91` |
| `Live` | `Short` | `118.55` | 12,870,000.00 USD | 1,110.00 USD | 0.00 USD | `+22.22%` | `9.38` |
| `Live` | `Short` | `118.75` | 12,870,000.00 USD | 966.63 USD | 0.00 USD | `+22.43%` | `8.14` |
| `Live` | `Short` | `119.25` | 12,870,000.00 USD | 240.88 USD | 0.00 USD | `+22.94%` | `2.02` |
| `Live` | `Short` | `119.35` | 12,960,000.00 USD | 85,100.00 USD | 0.00 USD | `+23.04%` | `712.99` |
| `Live` | `Short` | `119.55` | 17,240,000.00 USD | 4,280,000.00 USD | 0.00 USD | `+23.25%` | `35,779.15` |
| `Live` | `Short` | `119.75` | 17,240,000.00 USD | 261.06 USD | 0.00 USD | `+23.46%` | `2.18` |
| `Live` | `Short` | `119.85` | 17,240,000.00 USD | 6,180.00 USD | 0.00 USD | `+23.56%` | `51.58` |
| `Live` | `Short` | `120.15` | 17,250,000.00 USD | 2,980.00 USD | 0.00 USD | `+23.87%` | `24.83` |
| `Live` | `Short` | `120.35` | 17,250,000.00 USD | 145.62 USD | 0.00 USD | `+24.07%` | `1.21` |
| `Live` | `Short` | `120.45` | 17,340,000.00 USD | 93,000.00 USD | 0.00 USD | `+24.18%` | `772.14` |
| `Live` | `Short` | `120.55` | 17,350,000.00 USD | 12,790.00 USD | 0.00 USD | `+24.28%` | `106.08` |
| `Live` | `Short` | `120.65` | 17,350,000.00 USD | 1,570.00 USD | 0.00 USD | `+24.38%` | `13.05` |
| `Live` | `Short` | `121.15` | 17,370,000.00 USD | 12,720.00 USD | 0.00 USD | `+24.90%` | `105.00` |
| `Live` | `Short` | `121.25` | 17,370,000.00 USD | 414.68 USD | 0.00 USD | `+25.00%` | `3.42` |
| `Live` | `Short` | `121.55` | 17,370,000.00 USD | 6,220.00 USD | 0.00 USD | `+25.31%` | `51.21` |
| `Live` | `Short` | `121.65` | 17,390,000.00 USD | 16,300.00 USD | 0.00 USD | `+25.41%` | `133.95` |
| `Live` | `Short` | `122.05` | 17,450,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.83%` | `460.06` |
| `Live` | `Short` | `122.15` | 17,460,000.00 USD | 15,610.00 USD | 0.00 USD | `+25.93%` | `127.77` |
| `Live` | `Short` | `122.25` | 17,460,000.00 USD | 2,200.00 USD | 0.00 USD | `+26.03%` | `17.99` |
| `Live` | `Short` | `122.45` | 17,480,000.00 USD | 17,500.00 USD | 0.00 USD | `+26.24%` | `142.95` |
| `Live` | `Short` | `122.65` | 17,480,000.00 USD | 116.52 USD | 0.00 USD | `+26.45%` | `0.95` |
| `Live` | `Short` | `122.85` | 32,410,000.00 USD | 14,930,000.00 USD | 0.00 USD | `+26.65%` | `121,552.79` |
| `Live` | `Short` | `122.95` | 32,420,000.00 USD | 2,790.00 USD | 0.00 USD | `+26.76%` | `22.66` |
| `Live` | `Short` | `123.35` | 32,420,000.00 USD | 2,330.00 USD | 0.00 USD | `+27.17%` | `18.92` |
| `Live` | `Short` | `123.45` | 32,540,000.00 USD | 124,510.00 USD | 0.00 USD | `+27.27%` | `1,008.56` |
| `Live` | `Short` | `123.55` | 32,550,000.00 USD | 3,430.00 USD | 0.00 USD | `+27.37%` | `27.73` |
| `Live` | `Short` | `123.75` | 32,600,000.00 USD | 55,610.00 USD | 0.00 USD | `+27.58%` | `449.38` |
| `Live` | `Short` | `124.05` | 32,600,000.00 USD | 586.76 USD | 0.00 USD | `+27.89%` | `4.73` |
| `Live` | `Short` | `124.25` | 32,620,000.00 USD | 17,600.00 USD | 0.00 USD | `+28.10%` | `141.62` |
| `Live` | `Short` | `124.45` | 33,480,000.00 USD | 859,810.00 USD | 0.00 USD | `+28.30%` | `6,908.91` |
| `Live` | `Short` | `124.65` | 33,480,000.00 USD | 675.60 USD | 0.00 USD | `+28.51%` | `5.42` |
| `Live` | `Short` | `124.75` | 33,490,000.00 USD | 5,920.00 USD | 0.00 USD | `+28.61%` | `47.43` |
| `Live` | `Short` | `124.95` | 33,520,000.00 USD | 33,830.00 USD | 0.00 USD | `+28.82%` | `270.71` |
| `Live` | `Short` | `125.25` | 33,520,000.00 USD | 2,420.00 USD | 0.00 USD | `+29.13%` | `19.35` |
| `Live` | `Short` | `125.35` | 33,530,000.00 USD | 5,910.00 USD | 0.00 USD | `+29.23%` | `47.15` |
| `Live` | `Short` | `125.45` | 33,580,000.00 USD | 46,480.00 USD | 0.00 USD | `+29.33%` | `370.50` |
| `Live` | `Short` | `125.75` | 33,580,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.64%` | `15.31` |
| `Live` | `Short` | `125.85` | 33,590,000.00 USD | 12,690.00 USD | 0.00 USD | `+29.74%` | `100.83` |
| `Live` | `Short` | `125.95` | 33,590,000.00 USD | 110.84 USD | 0.00 USD | `+29.85%` | `0.88` |
| `Live` | `Short` | `126.05` | 33,590,000.00 USD | 810.50 USD | 0.00 USD | `+29.95%` | `6.43` |
| `Live` | `Short` | `126.15` | 33,590,000.00 USD | 470.54 USD | 0.00 USD | `+30.05%` | `3.73` |
| `Live` | `Short` | `126.35` | 33,590,000.00 USD | 506.66 USD | 0.00 USD | `+30.26%` | `4.01` |
| `Live` | `Short` | `126.65` | 33,630,000.00 USD | 32,990.00 USD | 0.00 USD | `+30.57%` | `260.47` |
| `Live` | `Short` | `126.75` | 33,630,000.00 USD | 6,420.00 USD | 0.00 USD | `+30.67%` | `50.69` |
| `Live` | `Short` | `126.85` | 33,640,000.00 USD | 4,260.00 USD | 0.00 USD | `+30.78%` | `33.56` |
| `Live` | `Short` | `126.95` | 33,650,000.00 USD | 9,460.00 USD | 0.00 USD | `+30.88%` | `74.51` |
| `Live` | `Short` | `127.05` | 33,650,000.00 USD | 4,280.00 USD | 0.00 USD | `+30.98%` | `33.71` |
| `Live` | `Short` | `127.35` | 33,670,000.00 USD | 16,190.00 USD | 0.00 USD | `+31.29%` | `127.13` |
| `Live` | `Short` | `127.55` | 33,670,000.00 USD | 128.83 USD | 0.00 USD | `+31.50%` | `1.01` |
| `Live` | `Short` | `127.65` | 33,670,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.60%` | `37.89` |
| `Live` | `Short` | `127.85` | 33,930,000.00 USD | 256,560.00 USD | 0.00 USD | `+31.81%` | `2,006.76` |
| `Live` | `Short` | `127.95` | 33,940,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.91%` | `82.13` |
| `Live` | `Short` | `128.05` | 34,050,000.00 USD | 116,200.00 USD | 0.00 USD | `+32.01%` | `907.49` |
| `Live` | `Short` | `128.15` | 34,060,000.00 USD | 3,350.00 USD | 0.00 USD | `+32.12%` | `26.12` |
| `Live` | `Short` | `128.35` | 34,060,000.00 USD | 195.09 USD | 0.00 USD | `+32.32%` | `1.52` |
| `Live` | `Short` | `128.45` | 34,060,000.00 USD | 271.03 USD | 0.00 USD | `+32.43%` | `2.11` |
| `Live` | `Short` | `128.65` | 34,060,000.00 USD | 788.62 USD | 0.00 USD | `+32.63%` | `6.13` |
| `Live` | `Short` | `128.75` | 34,770,000.00 USD | 714,710.00 USD | 0.00 USD | `+32.73%` | `5,551.11` |
| `Live` | `Short` | `128.85` | 34,820,000.00 USD | 44,790.00 USD | 0.00 USD | `+32.84%` | `347.60` |
| `Live` | `Short` | `129.25` | 34,850,000.00 USD | 32,480.00 USD | 0.00 USD | `+33.25%` | `251.27` |
| `Live` | `Short` | `129.55` | 34,910,000.00 USD | 56,180.00 USD | 0.00 USD | `+33.56%` | `433.68` |
| `Live` | `Short` | `129.75` | 34,970,000.00 USD | 67,370.00 USD | 0.00 USD | `+33.77%` | `519.23` |
| `Live` | `Short` | `129.85` | 34,970,000.00 USD | 490.83 USD | 0.00 USD | `+33.87%` | `3.78` |
| `Live` | `Short` | `130.25` | 34,980,000.00 USD | 6,660.00 USD | 0.00 USD | `+34.28%` | `51.12` |
| `Live` | `Short` | `130.55` | 34,980,000.00 USD | 195.83 USD | 0.00 USD | `+34.59%` | `1.50` |
| `Live` | `Short` | `130.85` | 35,490,000.00 USD | 503,820.00 USD | 0.00 USD | `+34.90%` | `3,850.39` |
| `Live` | `Short` | `130.95` | 35,500,000.00 USD | 14,890.00 USD | 0.00 USD | `+35.00%` | `113.72` |
| `Live` | `Short` | `131.05` | 35,500,000.00 USD | 188.71 USD | 0.00 USD | `+35.11%` | `1.44` |
| `Live` | `Short` | `131.25` | 35,500,000.00 USD | 1,560.00 USD | 0.00 USD | `+35.31%` | `11.87` |
| `Live` | `Short` | `131.35` | 35,500,000.00 USD | 855.09 USD | 0.00 USD | `+35.42%` | `6.51` |
| `Live` | `Short` | `131.45` | 35,500,000.00 USD | 219.52 USD | 0.00 USD | `+35.52%` | `1.67` |
| `Live` | `Short` | `131.85` | 35,510,000.00 USD | 5,540.00 USD | 0.00 USD | `+35.93%` | `42.01` |
| `Live` | `Short` | `132.15` | 35,510,000.00 USD | 325.09 USD | 0.00 USD | `+36.24%` | `2.46` |
| `Live` | `Short` | `132.35` | 35,510,000.00 USD | 4,630.00 USD | 0.00 USD | `+36.45%` | `35.00` |
| `Live` | `Short` | `132.45` | 35,520,000.00 USD | 8,530.00 USD | 0.00 USD | `+36.55%` | `64.37` |
| `Live` | `Short` | `132.55` | 35,520,000.00 USD | 695.89 USD | 0.00 USD | `+36.65%` | `5.25` |
| `Live` | `Short` | `132.65` | 35,520,000.00 USD | 240.10 USD | 0.00 USD | `+36.76%` | `1.81` |
| `Live` | `Short` | `132.75` | 35,530,000.00 USD | 2,580.00 USD | 0.00 USD | `+36.86%` | `19.46` |
| `Live` | `Short` | `132.85` | 35,580,000.00 USD | 51,560.00 USD | 0.00 USD | `+36.96%` | `388.08` |
| `Live` | `Short` | `132.95` | 35,580,000.00 USD | 3,630.00 USD | 0.00 USD | `+37.06%` | `27.29` |
| `Live` | `Short` | `133.15` | 35,600,000.00 USD | 16,530.00 USD | 0.00 USD | `+37.27%` | `124.13` |
| `Live` | `Short` | `133.55` | 35,600,000.00 USD | 186.97 USD | 0.00 USD | `+37.68%` | `1.40` |
| `Live` | `Short` | `133.65` | 35,600,000.00 USD | 156.37 USD | 0.00 USD | `+37.79%` | `1.17` |
| `Live` | `Short` | `133.75` | 35,750,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.89%` | `1,130.50` |
| `Live` | `Short` | `133.85` | 35,760,000.00 USD | 12,740.00 USD | 0.00 USD | `+37.99%` | `95.21` |
| `Live` | `Short` | `133.95` | 35,760,000.00 USD | 503.65 USD | 0.00 USD | `+38.10%` | `3.76` |
| `Live` | `Short` | `134.05` | 35,770,000.00 USD | 8,290.00 USD | 0.00 USD | `+38.20%` | `61.86` |
| `Live` | `Short` | `134.15` | 35,800,000.00 USD | 30,190.00 USD | 0.00 USD | `+38.30%` | `225.08` |
| `Live` | `Short` | `134.25` | 35,860,000.00 USD | 59,870.00 USD | 0.00 USD | `+38.40%` | `445.96` |
| `Live` | `Short` | `135.05` | 36,040,000.00 USD | 181,050.00 USD | 0.00 USD | `+39.23%` | `1,340.64` |
| `Live` | `Short` | `135.25` | 36,050,000.00 USD | 4,050.00 USD | 0.00 USD | `+39.44%` | `29.93` |
| `Live` | `Short` | `135.85` | 36,050,000.00 USD | 3,250.00 USD | 0.00 USD | `+40.05%` | `23.94` |
| `Live` | `Short` | `135.95` | 36,050,000.00 USD | 504.37 USD | 0.00 USD | `+40.16%` | `3.71` |
| `Live` | `Short` | `136.55` | 36,050,000.00 USD | 136.55 USD | 0.00 USD | `+40.78%` | `1.00` |
| `Live` | `Short` | `136.65` | 36,050,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.88%` | `8.14` |
| `Live` | `Short` | `136.85` | 36,260,000.00 USD | 204,950.00 USD | 0.00 USD | `+41.09%` | `1,497.60` |
| `Live` | `Short` | `137.05` | 36,260,000.00 USD | 836.00 USD | 0.00 USD | `+41.29%` | `6.10` |
| `Live` | `Short` | `137.15` | 36,280,000.00 USD | 25,200.00 USD | 0.00 USD | `+41.39%` | `183.77` |
| `Live` | `Short` | `137.25` | 36,360,000.00 USD | 83,240.00 USD | 0.00 USD | `+41.50%` | `606.49` |
| `Live` | `Short` | `137.95` | 36,900,000.00 USD | 538,000.00 USD | 0.00 USD | `+42.22%` | `3,900.00` |
| `Live` | `Short` | `138.05` | 36,900,000.00 USD | 1,270.00 USD | 0.00 USD | `+42.32%` | `9.20` |
| `Live` | `Short` | `138.15` | 36,950,000.00 USD | 41,450.00 USD | 0.00 USD | `+42.43%` | `300.00` |
| `Live` | `Short` | `138.25` | 36,990,000.00 USD | 45,220.00 USD | 0.00 USD | `+42.53%` | `327.11` |
| `Live` | `Short` | `138.35` | 42,160,000.00 USD | 5,170,000.00 USD | 0.00 USD | `+42.63%` | `37,335.59` |
| `Live` | `Short` | `138.75` | 44,240,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+43.04%` | `15,001.76` |
| `Live` | `Short` | `138.85` | 44,250,000.00 USD | 14,930.00 USD | 0.00 USD | `+43.15%` | `107.50` |
| `Live` | `Short` | `138.95` | 44,260,000.00 USD | 4,420.00 USD | 0.00 USD | `+43.25%` | `31.84` |
| `Live` | `Short` | `139.05` | 44,260,000.00 USD | 620.16 USD | 0.00 USD | `+43.35%` | `4.46` |
| `Live` | `Short` | `139.15` | 44,260,000.00 USD | 552.43 USD | 0.00 USD | `+43.46%` | `3.97` |
| `Live` | `Short` | `139.35` | 44,260,000.00 USD | 253.62 USD | 0.00 USD | `+43.66%` | `1.82` |
| `Live` | `Short` | `139.55` | 44,260,000.00 USD | 494.01 USD | 0.00 USD | `+43.87%` | `3.54` |
| `Live` | `Short` | `139.65` | 44,260,000.00 USD | 769.47 USD | 0.00 USD | `+43.97%` | `5.51` |
| `Live` | `Short` | `140.05` | 44,260,000.00 USD | 116.24 USD | 0.00 USD | `+44.38%` | `0.83` |
| `Live` | `Short` | `140.35` | 44,350,000.00 USD | 85,850.00 USD | 0.00 USD | `+44.69%` | `611.68` |
| `Live` | `Short` | `140.45` | 44,350,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.80%` | `34.66` |
| `Live` | `Short` | `140.55` | 44,360,000.00 USD | 8,030.00 USD | 0.00 USD | `+44.90%` | `57.16` |
| `Live` | `Short` | `140.65` | 44,360,000.00 USD | 1,130.00 USD | 0.00 USD | `+45.00%` | `8.06` |
| `Live` | `Short` | `140.95` | 45,430,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+45.31%` | `7,623.31` |
| `Live` | `Short` | `141.05` | 45,430,000.00 USD | 125.53 USD | 0.00 USD | `+45.42%` | `0.89` |
| `Live` | `Short` | `141.25` | 45,440,000.00 USD | 1,330.00 USD | 0.00 USD | `+45.62%` | `9.41` |
| `Live` | `Short` | `141.35` | 45,440,000.00 USD | 210.61 USD | 0.00 USD | `+45.72%` | `1.49` |
| `Live` | `Short` | `141.45` | 45,680,000.00 USD | 248,810.00 USD | 0.00 USD | `+45.83%` | `1,759.00` |
| `Live` | `Short` | `141.55` | 45,680,000.00 USD | 236.39 USD | 0.00 USD | `+45.93%` | `1.67` |
| `Live` | `Short` | `141.65` | 45,690,000.00 USD | 2,140.00 USD | 0.00 USD | `+46.03%` | `15.11` |
| `Live` | `Short` | `141.75` | 46,550,000.00 USD | 862,970.00 USD | 0.00 USD | `+46.14%` | `6,087.97` |
| `Live` | `Short` | `142.15` | 46,630,000.00 USD | 80,180.00 USD | 0.00 USD | `+46.55%` | `564.06` |
| `Live` | `Short` | `142.35` | 46,630,000.00 USD | 1,640.00 USD | 0.00 USD | `+46.76%` | `11.52` |
| `Live` | `Short` | `142.45` | 46,630,000.00 USD | 776.35 USD | 0.00 USD | `+46.86%` | `5.45` |
| `Live` | `Short` | `142.75` | 46,640,000.00 USD | 2,450.00 USD | 0.00 USD | `+47.17%` | `17.17` |
| `Live` | `Short` | `143.15` | 46,640,000.00 USD | 1,330.00 USD | 0.00 USD | `+47.58%` | `9.31` |
| `Live` | `Short` | `143.25` | 47,480,000.00 USD | 840,780.00 USD | 0.00 USD | `+47.68%` | `5,869.33` |
| `Live` | `Short` | `143.35` | 47,500,000.00 USD | 22,260.00 USD | 0.00 USD | `+47.79%` | `155.27` |
| `Live` | `Short` | `144.05` | 47,500,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.51%` | `26.00` |
| `Live` | `Short` | `144.25` | 47,520,000.00 USD | 13,110.00 USD | 0.00 USD | `+48.71%` | `90.91` |
| `Live` | `Short` | `144.65` | 47,520,000.00 USD | 1,240.00 USD | 0.00 USD | `+49.13%` | `8.60` |
| `Live` | `Short` | `144.85` | 47,570,000.00 USD | 52,050.00 USD | 0.00 USD | `+49.33%` | `359.32` |
| `Live` | `Short` | `145.05` | 48,010,000.00 USD | 435,640.00 USD | 0.00 USD | `+49.54%` | `3,003.36` |
| `Live` | `Short` | `145.15` | 48,010,000.00 USD | 1,760.00 USD | 0.00 USD | `+49.64%` | `12.12` |
| `Live` | `Short` | `145.35` | 48,010,000.00 USD | 3,720.00 USD | 0.00 USD | `+49.85%` | `25.60` |
| `Live` | `Short` | `145.85` | 48,020,000.00 USD | 5,850.00 USD | 0.00 USD | `+50.36%` | `40.09` |
| `Live` | `Short` | `145.95` | 48,020,000.00 USD | 2,220.00 USD | 0.00 USD | `+50.47%` | `15.19` |
| `Live` | `Short` | `146.15` | 48,110,000.00 USD | 89,860.00 USD | 0.00 USD | `+50.67%` | `614.83` |
| `Live` | `Short` | `146.25` | 48,110,000.00 USD | 3,940.00 USD | 0.00 USD | `+50.78%` | `26.95` |
| `Live` | `Short` | `146.35` | 48,120,000.00 USD | 7,330.00 USD | 0.00 USD | `+50.88%` | `50.10` |
| `Live` | `Short` | `146.65` | 48,710,000.00 USD | 587,730.00 USD | 0.00 USD | `+51.19%` | `4,007.68` |
| `Live` | `Short` | `146.85` | 48,790,000.00 USD | 77,890.00 USD | 0.00 USD | `+51.39%` | `530.42` |
| `Live` | `Short` | `146.95` | 48,790,000.00 USD | 3,070.00 USD | 0.00 USD | `+51.50%` | `20.88` |
| `Live` | `Short` | `147.05` | 48,790,000.00 USD | 2,290.00 USD | 0.00 USD | `+51.60%` | `15.54` |
| `Live` | `Short` | `147.15` | 48,790,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.70%` | `11.75` |
| `Live` | `Short` | `147.35` | 48,790,000.00 USD | 169.45 USD | 0.00 USD | `+51.91%` | `1.15` |
| `Live` | `Short` | `147.45` | 48,790,000.00 USD | 312.59 USD | 0.00 USD | `+52.01%` | `2.12` |
| `Live` | `Short` | `147.55` | 48,790,000.00 USD | 1,000.00 USD | 0.00 USD | `+52.12%` | `6.78` |
| `Live` | `Short` | `147.65` | 48,790,000.00 USD | 237.72 USD | 0.00 USD | `+52.22%` | `1.61` |
| `Live` | `Short` | `147.75` | 48,790,000.00 USD | 211.28 USD | 0.00 USD | `+52.32%` | `1.43` |
| `Live` | `Short` | `147.85` | 48,790,000.00 USD | 300.14 USD | 0.00 USD | `+52.43%` | `2.03` |
| `Live` | `Short` | `148.15` | 48,800,000.00 USD | 5,730.00 USD | 0.00 USD | `+52.74%` | `38.69` |
| `Live` | `Short` | `148.45` | 48,800,000.00 USD | 2,110.00 USD | 0.00 USD | `+53.04%` | `14.20` |
| `Live` | `Short` | `148.55` | 49,150,000.00 USD | 344,780.00 USD | 0.00 USD | `+53.15%` | `2,321.00` |
| `Live` | `Short` | `148.65` | 49,150,000.00 USD | 1,530.00 USD | 0.00 USD | `+53.25%` | `10.26` |
| `Live` | `Short` | `148.75` | 49,240,000.00 USD | 91,450.00 USD | 0.00 USD | `+53.35%` | `614.80` |
| `Live` | `Short` | `148.95` | 50,630,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+53.56%` | `9,328.87` |
| `Live` | `Short` | `149.05` | 50,790,000.00 USD | 160,350.00 USD | 0.00 USD | `+53.66%` | `1,075.79` |
| `Live` | `Short` | `149.55` | 50,790,000.00 USD | 116.65 USD | 0.00 USD | `+54.18%` | `0.78` |
| `Live` | `Short` | `149.65` | 50,810,000.00 USD | 16,030.00 USD | 0.00 USD | `+54.28%` | `107.15` |
| `Live` | `Short` | `149.95` | 50,840,000.00 USD | 29,270.00 USD | 0.00 USD | `+54.59%` | `195.19` |
| `Live` | `Short` | `150.05` | 51,960,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+54.69%` | `7,472.25` |
| `Live` | `Short` | `150.25` | 51,960,000.00 USD | 345.57 USD | 0.00 USD | `+54.90%` | `2.30` |
| `Live` | `Short` | `150.35` | 51,970,000.00 USD | 17,270.00 USD | 0.00 USD | `+55.00%` | `114.86` |
| `Live` | `Short` | `150.45` | 56,530,000.00 USD | 4,560,000.00 USD | 0.00 USD | `+55.11%` | `30,310.49` |
| `Live` | `Short` | `150.55` | 56,640,000.00 USD | 109,920.00 USD | 0.00 USD | `+55.21%` | `730.14` |
| `Live` | `Short` | `150.85` | 56,680,000.00 USD | 39,610.00 USD | 0.00 USD | `+55.52%` | `262.55` |
| `Live` | `Short` | `151.15` | 56,690,000.00 USD | 2,540.00 USD | 0.00 USD | `+55.83%` | `16.81` |
| `Live` | `Short` | `151.45` | 56,700,000.00 USD | 8,830.00 USD | 0.00 USD | `+56.14%` | `58.32` |
| `Live` | `Short` | `151.95` | 56,700,000.00 USD | 1,920.00 USD | 0.00 USD | `+56.65%` | `12.64` |
| `Live` | `Short` | `152.05` | 56,700,000.00 USD | 2,320.00 USD | 0.00 USD | `+56.76%` | `15.28` |
| `Live` | `Short` | `152.15` | 56,720,000.00 USD | 22,220.00 USD | 0.00 USD | `+56.86%` | `146.04` |
| `Live` | `Short` | `152.25` | 56,720,000.00 USD | 200.97 USD | 0.00 USD | `+56.96%` | `1.32` |
| `Live` | `Short` | `152.35` | 57,010,000.00 USD | 286,550.00 USD | 0.00 USD | `+57.07%` | `1,880.87` |
| `Live` | `Short` | `152.45` | 57,010,000.00 USD | 3,150.00 USD | 0.00 USD | `+57.17%` | `20.65` |
| `Live` | `Short` | `152.55` | 57,440,000.00 USD | 426,020.00 USD | 0.00 USD | `+57.27%` | `2,792.65` |
| `Live` | `Short` | `152.75` | 57,440,000.00 USD | 3,750.00 USD | 0.00 USD | `+57.48%` | `24.56` |
| `Live` | `Short` | `152.95` | 57,480,000.00 USD | 40,230.00 USD | 0.00 USD | `+57.68%` | `263.05` |
| `Live` | `Short` | `153.05` | 57,500,000.00 USD | 17,750.00 USD | 0.00 USD | `+57.79%` | `115.95` |
| `Live` | `Short` | `153.15` | 57,620,000.00 USD | 119,730.00 USD | 0.00 USD | `+57.89%` | `781.77` |
| `Live` | `Short` | `153.35` | 57,620,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.10%` | `15.00` |
| `Live` | `Short` | `153.65` | 57,630,000.00 USD | 8,340.00 USD | 0.00 USD | `+58.41%` | `54.29` |
| `Live` | `Short` | `153.85` | 57,670,000.00 USD | 43,540.00 USD | 0.00 USD | `+58.61%` | `283.01` |
| `Live` | `Short` | `154.15` | 57,670,000.00 USD | 292.89 USD | 0.00 USD | `+58.92%` | `1.90` |
| `Live` | `Short` | `154.25` | 57,680,000.00 USD | 2,340.00 USD | 0.00 USD | `+59.02%` | `15.20` |
| `Live` | `Short` | `154.35` | 57,680,000.00 USD | 362.72 USD | 0.00 USD | `+59.13%` | `2.35` |
| `Live` | `Short` | `154.45` | 57,680,000.00 USD | 4,240.00 USD | 0.00 USD | `+59.23%` | `27.45` |
| `Live` | `Short` | `154.65` | 57,720,000.00 USD | 43,580.00 USD | 0.00 USD | `+59.44%` | `281.77` |
| `Live` | `Short` | `155.05` | 57,960,000.00 USD | 232,580.00 USD | 0.00 USD | `+59.85%` | `1,500.00` |
| `Live` | `Short` | `155.45` | 57,960,000.00 USD | 324.89 USD | 0.00 USD | `+60.26%` | `2.09` |
| `Live` | `Short` | `155.55` | 57,960,000.00 USD | 267.55 USD | 0.00 USD | `+60.36%` | `1.72` |
| `Live` | `Short` | `155.65` | 57,960,000.00 USD | 113.62 USD | 0.00 USD | `+60.47%` | `0.73` |
| `Live` | `Short` | `155.75` | 58,060,000.00 USD | 99,200.00 USD | 0.00 USD | `+60.57%` | `636.89` |
| `Live` | `Short` | `155.95` | 58,060,000.00 USD | 7,800.00 USD | 0.00 USD | `+60.78%` | `50.00` |
| `Live` | `Short` | `156.25` | 58,070,000.00 USD | 295.31 USD | 0.00 USD | `+61.09%` | `1.89` |
| `Live` | `Short` | `156.35` | 58,070,000.00 USD | 3,320.00 USD | 0.00 USD | `+61.19%` | `21.26` |
| `Live` | `Short` | `156.45` | 58,070,000.00 USD | 1,770.00 USD | 0.00 USD | `+61.29%` | `11.29` |
| `Live` | `Short` | `156.85` | 58,230,000.00 USD | 156,850.00 USD | 0.00 USD | `+61.70%` | `1,000.00` |
| `Live` | `Short` | `156.95` | 58,340,000.00 USD | 113,950.00 USD | 0.00 USD | `+61.81%` | `726.01` |
| `Live` | `Short` | `157.15` | 58,390,000.00 USD | 49,270.00 USD | 0.00 USD | `+62.01%` | `313.50` |
| `Live` | `Short` | `157.25` | 58,390,000.00 USD | 190.27 USD | 0.00 USD | `+62.12%` | `1.21` |
| `Live` | `Short` | `157.45` | 58,390,000.00 USD | 1,470.00 USD | 0.00 USD | `+62.32%` | `9.31` |
| `Live` | `Short` | `157.65` | 58,390,000.00 USD | 654.25 USD | 0.00 USD | `+62.53%` | `4.15` |
| `Live` | `Short` | `157.75` | 58,490,000.00 USD | 92,600.00 USD | 0.00 USD | `+62.63%` | `587.00` |
| `Live` | `Short` | `157.95` | 58,510,000.00 USD | 28,000.00 USD | 0.00 USD | `+62.84%` | `177.28` |
| `Live` | `Short` | `158.25` | 58,510,000.00 USD | 120.27 USD | 0.00 USD | `+63.15%` | `0.76` |
| `Live` | `Short` | `158.75` | 58,590,000.00 USD | 79,380.00 USD | 0.00 USD | `+63.66%` | `500.00` |
| `Live` | `Short` | `158.85` | 58,600,000.00 USD | 2,870.00 USD | 0.00 USD | `+63.77%` | `18.06` |
| `Live` | `Short` | `159.05` | 58,640,000.00 USD | 44,690.00 USD | 0.00 USD | `+63.97%` | `281.00` |
| `Live` | `Short` | `159.45` | 58,640,000.00 USD | 495.89 USD | 0.00 USD | `+64.38%` | `3.11` |
| `Live` | `Short` | `159.55` | 58,730,000.00 USD | 85,000.00 USD | 0.00 USD | `+64.49%` | `532.74` |
| `Live` | `Short` | `159.65` | 58,730,000.00 USD | 1,760.00 USD | 0.00 USD | `+64.59%` | `11.01` |
| `Live` | `Short` | `159.85` | 58,730,000.00 USD | 300.52 USD | 0.00 USD | `+64.80%` | `1.88` |
| `Live` | `Short` | `160.15` | 59,450,000.00 USD | 722,570.00 USD | 0.00 USD | `+65.11%` | `4,511.82` |
| `Live` | `Short` | `160.35` | 59,450,000.00 USD | 1,340.00 USD | 0.00 USD | `+65.31%` | `8.33` |
| `Live` | `Short` | `160.55` | 59,450,000.00 USD | 436.70 USD | 0.00 USD | `+65.52%` | `2.72` |
| `Live` | `Short` | `160.85` | 59,450,000.00 USD | 641.79 USD | 0.00 USD | `+65.83%` | `3.99` |
| `Live` | `Short` | `161.05` | 59,450,000.00 USD | 2,240.00 USD | 0.00 USD | `+66.03%` | `13.93` |
| `Live` | `Short` | `161.25` | 59,470,000.00 USD | 18,880.00 USD | 0.00 USD | `+66.24%` | `117.09` |
| `Live` | `Short` | `161.35` | 59,480,000.00 USD | 1,530.00 USD | 0.00 USD | `+66.34%` | `9.51` |
| `Live` | `Short` | `161.55` | 59,480,000.00 USD | 1,600.00 USD | 0.00 USD | `+66.55%` | `9.88` |
| `Live` | `Short` | `161.95` | 59,950,000.00 USD | 468,510.00 USD | 0.00 USD | `+66.96%` | `2,892.95` |
| `Live` | `Short` | `162.15` | 59,950,000.00 USD | 1,340.00 USD | 0.00 USD | `+67.17%` | `8.29` |
| `Live` | `Short` | `163.35` | 59,950,000.00 USD | 668.10 USD | 0.00 USD | `+68.41%` | `4.09` |
| `Live` | `Short` | `163.85` | 59,950,000.00 USD | 786.48 USD | 0.00 USD | `+68.92%` | `4.80` |
| `Live` | `Short` | `163.95` | 59,970,000.00 USD | 16,950.00 USD | 0.00 USD | `+69.02%` | `103.36` |
| `Live` | `Short` | `164.05` | 60,110,000.00 USD | 144,260.00 USD | 0.00 USD | `+69.13%` | `879.39` |
| `Live` | `Short` | `164.45` | 60,110,000.00 USD | 822.25 USD | 0.00 USD | `+69.54%` | `5.00` |
| `Live` | `Short` | `164.55` | 60,130,000.00 USD | 16,450.00 USD | 0.00 USD | `+69.64%` | `100.00` |
| `Live` | `Short` | `164.75` | 60,330,000.00 USD | 207,840.00 USD | 0.00 USD | `+69.85%` | `1,261.56` |
| `Live` | `Short` | `165.05` | 60,410,000.00 USD | 72,620.00 USD | 0.00 USD | `+70.16%` | `440.00` |
| `Live` | `Short` | `165.15` | 60,410,000.00 USD | 198.18 USD | 0.00 USD | `+70.26%` | `1.20` |
| `Live` | `Short` | `165.45` | 60,430,000.00 USD | 18,710.00 USD | 0.00 USD | `+70.57%` | `113.07` |
| `Live` | `Short` | `166.25` | 60,440,000.00 USD | 14,070.00 USD | 0.00 USD | `+71.40%` | `84.61` |
| `Live` | `Short` | `166.55` | 60,440,000.00 USD | 3,440.00 USD | 0.00 USD | `+71.70%` | `20.63` |
| `Live` | `Short` | `166.65` | 60,510,000.00 USD | 67,790.00 USD | 0.00 USD | `+71.81%` | `406.80` |
| `Live` | `Short` | `166.95` | 60,540,000.00 USD | 27,870.00 USD | 0.00 USD | `+72.12%` | `166.92` |
| `Live` | `Short` | `167.65` | 60,540,000.00 USD | 2,770.00 USD | 0.00 USD | `+72.84%` | `16.53` |
| `Live` | `Short` | `167.75` | 60,550,000.00 USD | 5,130.00 USD | 0.00 USD | `+72.94%` | `30.60` |
| `Live` | `Short` | `167.95` | 60,550,000.00 USD | 122.60 USD | 0.00 USD | `+73.15%` | `0.73` |
| `Live` | `Short` | `168.35` | 60,570,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.56%` | `117.24` |
| `Live` | `Short` | `168.65` | 60,890,000.00 USD | 325,850.00 USD | 0.00 USD | `+73.87%` | `1,932.10` |
| `Live` | `Short` | `168.75` | 60,890,000.00 USD | 151.88 USD | 0.00 USD | `+73.97%` | `0.90` |
| `Live` | `Short` | `168.85` | 60,890,000.00 USD | 1,160.00 USD | 0.00 USD | `+74.08%` | `6.88` |
| `Live` | `Short` | `169.65` | 60,890,000.00 USD | 366.44 USD | 0.00 USD | `+74.90%` | `2.16` |
| `Live` | `Short` | `170.05` | 60,930,000.00 USD | 34,990.00 USD | 0.00 USD | `+75.31%` | `205.77` |
| `Live` | `Short` | `170.35` | 61,050,000.00 USD | 119,250.00 USD | 0.00 USD | `+75.62%` | `700.00` |
| `Live` | `Short` | `171.45` | 61,050,000.00 USD | 111.44 USD | 0.00 USD | `+76.76%` | `0.65` |
| `Live` | `Short` | `171.65` | 61,230,000.00 USD | 182,260.00 USD | 0.00 USD | `+76.96%` | `1,061.79` |
| `Live` | `Short` | `171.85` | 62,090,000.00 USD | 859,250.00 USD | 0.00 USD | `+77.17%` | `5,000.00` |
| `Live` | `Short` | `172.35` | 62,090,000.00 USD | 210.27 USD | 0.00 USD | `+77.68%` | `1.22` |
| `Live` | `Short` | `172.45` | 62,140,000.00 USD | 51,730.00 USD | 0.00 USD | `+77.79%` | `300.00` |
| `Live` | `Short` | `172.65` | 62,140,000.00 USD | 481.69 USD | 0.00 USD | `+77.99%` | `2.79` |
| `Live` | `Short` | `173.05` | 63,150,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+78.41%` | `5,820.70` |
| `Live` | `Short` | `173.25` | 69,330,000.00 USD | 6,180,000.00 USD | 0.00 USD | `+78.61%` | `35,645.69` |
| `Live` | `Short` | `173.45` | 69,340,000.00 USD | 16,540.00 USD | 0.00 USD | `+78.82%` | `95.36` |
| `Live` | `Short` | `173.85` | 69,340,000.00 USD | 695.40 USD | 0.00 USD | `+79.23%` | `4.00` |
| `Live` | `Short` | `173.95` | 69,450,000.00 USD | 104,370.00 USD | 0.00 USD | `+79.33%` | `600.00` |
| `Live` | `Short` | `174.05` | 69,550,000.00 USD | 104,430.00 USD | 0.00 USD | `+79.44%` | `600.00` |
| `Live` | `Short` | `174.25` | 69,800,000.00 USD | 245,010.00 USD | 0.00 USD | `+79.64%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 70,000,000.00 USD | 205,490.00 USD | 0.00 USD | `+79.75%` | `1,178.60` |
| `Live` | `Short` | `174.45` | 70,000,000.00 USD | 697.80 USD | 0.00 USD | `+79.85%` | `4.00` |
| `Live` | `Short` | `174.55` | 108,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | `+79.95%` | `220,025.19` |
| `Live` | `Short` | `174.75` | 108,410,000.00 USD | 146.79 USD | 0.00 USD | `+80.16%` | `0.84` |
| `Live` | `Short` | `174.85` | 108,410,000.00 USD | 1,290.00 USD | 0.00 USD | `+80.26%` | `7.37` |
| `Live` | `Short` | `174.95` | 108,410,000.00 USD | 654.31 USD | 0.00 USD | `+80.36%` | `3.74` |
| `Live` | `Short` | `175.05` | 108,410,000.00 USD | 388.61 USD | 0.00 USD | `+80.47%` | `2.22` |
| `Live` | `Short` | `175.25` | 108,420,000.00 USD | 13,140.00 USD | 0.00 USD | `+80.67%` | `75.00` |
| `Live` | `Short` | `175.35` | 108,570,000.00 USD | 141,620.00 USD | 0.00 USD | `+80.78%` | `807.63` |
| `Live` | `Short` | `175.75` | 108,570,000.00 USD | 263.62 USD | 0.00 USD | `+81.19%` | `1.50` |
| `Live` | `Short` | `176.25` | 108,570,000.00 USD | 625.69 USD | 0.00 USD | `+81.70%` | `3.55` |
| `Live` | `Short` | `176.55` | 108,660,000.00 USD | 95,510.00 USD | 0.00 USD | `+82.01%` | `540.96` |
| `Live` | `Short` | `176.85` | 108,710,000.00 USD | 48,790.00 USD | 0.00 USD | `+82.32%` | `275.89` |
| `Live` | `Short` | `177.05` | 109,070,000.00 USD | 354,860.00 USD | 0.00 USD | `+82.53%` | `2,004.31` |
| `Live` | `Short` | `177.95` | 109,140,000.00 USD | 78,300.00 USD | 0.00 USD | `+83.46%` | `440.00` |
| `Live` | `Short` | `178.25` | 109,150,000.00 USD | 1,610.00 USD | 0.00 USD | `+83.77%` | `9.06` |
| `Live` | `Short` | `178.95` | 109,310,000.00 USD | 160,380.00 USD | 0.00 USD | `+84.49%` | `896.22` |
| `Live` | `Short` | `179.25` | 109,570,000.00 USD | 268,880.00 USD | 0.00 USD | `+84.80%` | `1,500.00` |
| `Live` | `Short` | `179.35` | 109,590,000.00 USD | 11,060.00 USD | 0.00 USD | `+84.90%` | `61.64` |
| `Live` | `Short` | `179.55` | 109,590,000.00 USD | 1,350.00 USD | 0.00 USD | `+85.11%` | `7.52` |
| `Live` | `Short` | `179.75` | 109,590,000.00 USD | 154.59 USD | 0.00 USD | `+85.31%` | `0.86` |
| `Live` | `Short` | `180.45` | 109,590,000.00 USD | 5,000.00 USD | 0.00 USD | `+86.03%` | `27.73` |
| `Live` | `Short` | `180.55` | 109,600,000.00 USD | 3,970.00 USD | 0.00 USD | `+86.14%` | `22.01` |
| `Live` | `Short` | `180.75` | 109,600,000.00 USD | 146.41 USD | 0.00 USD | `+86.34%` | `0.81` |
| `Live` | `Short` | `181.05` | 109,600,000.00 USD | 1,900.00 USD | 0.00 USD | `+86.65%` | `10.50` |
| `Live` | `Short` | `181.45` | 109,620,000.00 USD | 18,140.00 USD | 0.00 USD | `+87.07%` | `100.00` |
| `Live` | `Short` | `181.55` | 109,620,000.00 USD | 254.17 USD | 0.00 USD | `+87.17%` | `1.40` |
| `Live` | `Short` | `181.75` | 109,650,000.00 USD | 36,350.00 USD | 0.00 USD | `+87.37%` | `200.00` |
| `Live` | `Short` | `182.15` | 109,660,000.00 USD | 3,990.00 USD | 0.00 USD | `+87.79%` | `21.93` |
| `Live` | `Short` | `182.45` | 109,660,000.00 USD | 2,060.00 USD | 0.00 USD | `+88.10%` | `11.28` |
| `Live` | `Short` | `182.85` | 109,660,000.00 USD | 618.03 USD | 0.00 USD | `+88.51%` | `3.38` |
| `Live` | `Short` | `183.15` | 109,710,000.00 USD | 52,620.00 USD | 0.00 USD | `+88.82%` | `287.30` |
| `Live` | `Short` | `183.35` | 109,720,000.00 USD | 7,600.00 USD | 0.00 USD | `+89.02%` | `41.43` |
| `Live` | `Short` | `183.65` | 109,730,000.00 USD | 9,500.00 USD | 0.00 USD | `+89.33%` | `51.72` |
| `Live` | `Short` | `184.25` | 109,730,000.00 USD | 1,950.00 USD | 0.00 USD | `+89.95%` | `10.59` |
| `Live` | `Short` | `184.45` | 110,700,000.00 USD | 968,240.00 USD | 0.00 USD | `+90.16%` | `5,249.32` |
| `Live` | `Short` | `184.75` | 110,910,000.00 USD | 214,100.00 USD | 0.00 USD | `+90.47%` | `1,158.88` |
| `Live` | `Short` | `184.95` | 111,080,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.67%` | `893.35` |
| `Live` | `Short` | `185.25` | 111,080,000.00 USD | 737.29 USD | 0.00 USD | `+90.98%` | `3.98` |
| `Live` | `Short` | `185.45` | 111,080,000.00 USD | 2,770.00 USD | 0.00 USD | `+91.19%` | `14.94` |
| `Live` | `Short` | `185.55` | 111,080,000.00 USD | 246.78 USD | 0.00 USD | `+91.29%` | `1.33` |
| `Live` | `Short` | `185.65` | 111,080,000.00 USD | 137.38 USD | 0.00 USD | `+91.40%` | `0.74` |
| `Live` | `Short` | `186.05` | 111,090,000.00 USD | 2,090.00 USD | 0.00 USD | `+91.81%` | `11.24` |
| `Live` | `Short` | `186.35` | 111,090,000.00 USD | 987.66 USD | 0.00 USD | `+92.12%` | `5.30` |
| `Live` | `Short` | `186.95` | 111,090,000.00 USD | 286.03 USD | 0.00 USD | `+92.74%` | `1.53` |
| `Live` | `Short` | `187.15` | 111,090,000.00 USD | 232.07 USD | 0.00 USD | `+92.94%` | `1.24` |
| `Live` | `Short` | `187.85` | 111,090,000.00 USD | 1,560.00 USD | 0.00 USD | `+93.66%` | `8.32` |
| `Live` | `Short` | `188.25` | 111,090,000.00 USD | 5,340.00 USD | 0.00 USD | `+94.08%` | `28.34` |
| `Live` | `Short` | `188.35` | 111,100,000.00 USD | 2,700.00 USD | 0.00 USD | `+94.18%` | `14.32` |
| `Live` | `Short` | `188.45` | 111,110,000.00 USD | 12,740.00 USD | 0.00 USD | `+94.28%` | `67.60` |
| `Live` | `Short` | `188.55` | 111,110,000.00 USD | 231.92 USD | 0.00 USD | `+94.39%` | `1.23` |
| `Live` | `Short` | `188.85` | 111,390,000.00 USD | 283,200.00 USD | 0.00 USD | `+94.69%` | `1,499.60` |
| `Live` | `Short` | `188.95` | 111,390,000.00 USD | 1,450.00 USD | 0.00 USD | `+94.80%` | `7.69` |
| `Live` | `Short` | `189.25` | 111,390,000.00 USD | 838.38 USD | 0.00 USD | `+95.11%` | `4.43` |
| `Live` | `Short` | `189.95` | 111,680,000.00 USD | 284,930.00 USD | 0.00 USD | `+95.83%` | `1,500.00` |
| `Live` | `Short` | `190.05` | 111,680,000.00 USD | 117.83 USD | 0.00 USD | `+95.93%` | `0.62` |
| `Live` | `Short` | `190.15` | 111,680,000.00 USD | 1,480.00 USD | 0.00 USD | `+96.03%` | `7.78` |
| `Live` | `Short` | `190.55` | 112,060,000.00 USD | 381,100.00 USD | 0.00 USD | `+96.45%` | `2,000.00` |
| `Live` | `Short` | `190.65` | 112,120,000.00 USD | 62,550.00 USD | 0.00 USD | `+96.55%` | `328.11` |
| `Live` | `Short` | `190.95` | 125,690,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+96.86%` | `71,045.74` |
| `Live` | `Short` | `191.25` | 125,690,000.00 USD | 175.95 USD | 0.00 USD | `+97.17%` | `0.92` |
| `Live` | `Short` | `191.55` | 125,690,000.00 USD | 2,910.00 USD | 0.00 USD | `+97.48%` | `15.17` |
| `Live` | `Short` | `191.65` | 125,690,000.00 USD | 505.96 USD | 0.00 USD | `+97.58%` | `2.64` |
| `Live` | `Short` | `191.85` | 125,700,000.00 USD | 1,370.00 USD | 0.00 USD | `+97.79%` | `7.13` |
| `Live` | `Short` | `191.95` | 125,700,000.00 USD | 322.48 USD | 0.00 USD | `+97.89%` | `1.68` |
| `Live` | `Short` | `192.95` | 125,700,000.00 USD | 246.98 USD | 0.00 USD | `+98.92%` | `1.28` |
| `Live` | `Short` | `193.15` | 125,700,000.00 USD | 5,770.00 USD | 0.00 USD | `+99.13%` | `29.85` |
| `Live` | `Short` | `193.35` | 125,700,000.00 USD | 378.97 USD | 0.00 USD | `+99.33%` | `1.96` |
| `Live` | `Short` | `193.55` | 125,820,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.54%` | `592.00` |
| `Live` | `Short` | `193.65` | 125,820,000.00 USD | 542.22 USD | 0.00 USD | `+99.64%` | `2.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 12,780,000.00 USD | 0.00 USD | 13,980.00 USD | `-76.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 12,760,000.00 USD | 0.00 USD | 3,760.00 USD | `-74.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.15` | 12,760,000.00 USD | 0.00 USD | 103.82 USD | `-73.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 12,760,000.00 USD | 0.00 USD | 519.56 USD | `-69.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 12,760,000.00 USD | 0.00 USD | 499.56 USD | `-68.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 12,760,000.00 USD | 0.00 USD | 818.32 USD | `-65.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 12,760,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 12,750,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 12,750,000.00 USD | 0.00 USD | 201.74 USD | `-60.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 12,750,000.00 USD | 0.00 USD | 150.30 USD | `-60.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.65` | 12,750,000.00 USD | 0.00 USD | 206.00 USD | `-60.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 12,750,000.00 USD | 0.00 USD | 208.14 USD | `-59.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 12,750,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 12,750,000.00 USD | 0.00 USD | 157.01 USD | `-59.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 12,750,000.00 USD | 0.00 USD | 583.13 USD | `-58.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 12,750,000.00 USD | 0.00 USD | 121.81 USD | `-56.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 12,750,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 12,580,000.00 USD | 0.00 USD | 105.00 USD | `-54.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 12,580,000.00 USD | 0.00 USD | 59,750.00 USD | `-53.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 12,520,000.00 USD | 0.00 USD | 251.05 USD | `-51.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 12,520,000.00 USD | 0.00 USD | 143.25 USD | `-50.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 12,520,000.00 USD | 0.00 USD | 191.40 USD | `-50.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 12,520,000.00 USD | 0.00 USD | 103.35 USD | `-49.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 12,520,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 12,510,000.00 USD | 0.00 USD | 107.03 USD | `-48.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 12,510,000.00 USD | 0.00 USD | 102.62 USD | `-47.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 12,510,000.00 USD | 0.00 USD | 134.28 USD | `-47.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 12,510,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 12,510,000.00 USD | 0.00 USD | 102.74 USD | `-46.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 12,510,000.00 USD | 0.00 USD | 126.12 USD | `-45.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 12,510,000.00 USD | 0.00 USD | 200.15 USD | `-45.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 12,510,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 12,480,000.00 USD | 0.00 USD | 1,980.00 USD | `-44.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 12,480,000.00 USD | 0.00 USD | 641.57 USD | `-44.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 12,480,000.00 USD | 0.00 USD | 139.87 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 12,480,000.00 USD | 0.00 USD | 209.19 USD | `-43.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 12,480,000.00 USD | 0.00 USD | 894.56 USD | `-42.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 12,480,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 12,470,000.00 USD | 0.00 USD | 6,680.00 USD | `-41.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 12,470,000.00 USD | 0.00 USD | 158.48 USD | `-40.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 12,470,000.00 USD | 0.00 USD | 428.72 USD | `-39.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 12,470,000.00 USD | 0.00 USD | 236.20 USD | `-39.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 12,470,000.00 USD | 0.00 USD | 200.01 USD | `-38.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 12,470,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 12,460,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 12,460,000.00 USD | 0.00 USD | 32,240.00 USD | `-38.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 12,420,000.00 USD | 0.00 USD | 488.63 USD | `-37.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 12,420,000.00 USD | 0.00 USD | 258.90 USD | `-37.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 12,420,000.00 USD | 0.00 USD | 206.13 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 12,420,000.00 USD | 0.00 USD | 724.78 USD | `-37.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 12,420,000.00 USD | 0.00 USD | 18,360.00 USD | `-37.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 12,400,000.00 USD | 0.00 USD | 142.33 USD | `-36.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 12,400,000.00 USD | 0.00 USD | 100.78 USD | `-36.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 12,400,000.00 USD | 0.00 USD | 243.74 USD | `-36.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 12,400,000.00 USD | 0.00 USD | 4,640.00 USD | `-36.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 12,400,000.00 USD | 0.00 USD | 136.98 USD | `-35.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 12,400,000.00 USD | 0.00 USD | 12,950.00 USD | `-35.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 12,380,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 12,380,000.00 USD | 0.00 USD | 222.55 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 12,380,000.00 USD | 0.00 USD | 163.19 USD | `-33.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 12,380,000.00 USD | 0.00 USD | 129.70 USD | `-33.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 12,380,000.00 USD | 0.00 USD | 2,440.00 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 12,380,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 12,380,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 12,370,000.00 USD | 0.00 USD | 9,140.00 USD | `-31.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 12,370,000.00 USD | 0.00 USD | 541.72 USD | `-31.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 12,360,000.00 USD | 0.00 USD | 8,930.00 USD | `-30.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 12,360,000.00 USD | 0.00 USD | 268.60 USD | `-30.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.85` | 12,360,000.00 USD | 0.00 USD | 303.29 USD | `-30.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 12,360,000.00 USD | 0.00 USD | 195.30 USD | `-29.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 12,350,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 12,350,000.00 USD | 0.00 USD | 359.04 USD | `-29.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 12,350,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 12,350,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 12,340,000.00 USD | 0.00 USD | 172.18 USD | `-28.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 12,340,000.00 USD | 0.00 USD | 668.96 USD | `-28.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 12,340,000.00 USD | 0.00 USD | 107.96 USD | `-28.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 12,340,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 12,290,000.00 USD | 0.00 USD | 365.32 USD | `-27.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 12,290,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 12,290,000.00 USD | 0.00 USD | 34,540.00 USD | `-27.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 12,260,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 12,250,000.00 USD | 0.00 USD | 562.80 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 12,250,000.00 USD | 0.00 USD | 681.51 USD | `-27.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 12,250,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 12,250,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 12,240,000.00 USD | 0.00 USD | 265.02 USD | `-26.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 12,240,000.00 USD | 0.00 USD | 32,400.00 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 12,210,000.00 USD | 0.00 USD | 289.37 USD | `-26.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 12,210,000.00 USD | 0.00 USD | 1,170.00 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 12,210,000.00 USD | 0.00 USD | 913.54 USD | `-26.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 12,210,000.00 USD | 0.00 USD | 2,770.00 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 12,200,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 12,190,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 12,120,000.00 USD | 0.00 USD | 139.56 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 12,120,000.00 USD | 0.00 USD | 510.95 USD | `-23.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 12,120,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 12,120,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 12,110,000.00 USD | 0.00 USD | 331.00 USD | `-23.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 12,110,000.00 USD | 0.00 USD | 28,050.00 USD | `-22.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 12,080,000.00 USD | 0.00 USD | 23,250.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 12,050,000.00 USD | 0.00 USD | 2,220.00 USD | `-21.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 12,050,000.00 USD | 0.00 USD | 277.98 USD | `-21.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 12,050,000.00 USD | 0.00 USD | 10,650.00 USD | `-21.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 12,040,000.00 USD | 0.00 USD | 254.34 USD | `-21.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 12,040,000.00 USD | 0.00 USD | 486.47 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 12,040,000.00 USD | 0.00 USD | 358.84 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 12,040,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 12,040,000.00 USD | 0.00 USD | 536.55 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 12,040,000.00 USD | 0.00 USD | 251.74 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.95` | 12,030,000.00 USD | 0.00 USD | 320.11 USD | `-20.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 12,030,000.00 USD | 0.00 USD | 3,210.00 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 12,030,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 12,030,000.00 USD | 0.00 USD | 155.12 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 12,030,000.00 USD | 0.00 USD | 56,050.00 USD | `-19.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 11,970,000.00 USD | 0.00 USD | 494.69 USD | `-19.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 11,970,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 11,950,000.00 USD | 0.00 USD | 379.58 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 11,950,000.00 USD | 0.00 USD | 4,660.00 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 11,950,000.00 USD | 0.00 USD | 381.50 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 11,940,000.00 USD | 0.00 USD | 1,750.00 USD | `-18.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 11,940,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 11,940,000.00 USD | 0.00 USD | 238.95 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 11,940,000.00 USD | 0.00 USD | 808.29 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 11,940,000.00 USD | 0.00 USD | 55,180.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 11,880,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 11,880,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 11,870,000.00 USD | 0.00 USD | 295.21 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 11,870,000.00 USD | 0.00 USD | 160.03 USD | `-15.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 11,870,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 11,870,000.00 USD | 0.00 USD | 71,590.00 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 11,800,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 11,800,000.00 USD | 0.00 USD | 684.31 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 11,800,000.00 USD | 0.00 USD | 264.34 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 11,800,000.00 USD | 0.00 USD | 2,920.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 11,790,000.00 USD | 0.00 USD | 12,040.00 USD | `-14.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 11,780,000.00 USD | 0.00 USD | 1,320.00 USD | `-14.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 11,780,000.00 USD | 0.00 USD | 7,000.00 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 11,770,000.00 USD | 0.00 USD | 1,560.00 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 11,770,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 11,750,000.00 USD | 0.00 USD | 405.57 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 11,750,000.00 USD | 0.00 USD | 421.09 USD | `-13.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 11,750,000.00 USD | 0.00 USD | 1,370.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 11,750,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 11,750,000.00 USD | 0.00 USD | 426.47 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 11,750,000.00 USD | 0.00 USD | 29,730.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 11,720,000.00 USD | 0.00 USD | 3,490.00 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 11,720,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 11,710,000.00 USD | 0.00 USD | 371.58 USD | `-12.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 11,710,000.00 USD | 0.00 USD | 169.95 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 11,710,000.00 USD | 0.00 USD | 519.75 USD | `-12.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 11,710,000.00 USD | 0.00 USD | 306.80 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 11,710,000.00 USD | 0.00 USD | 1,350.00 USD | `-12.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 11,710,000.00 USD | 0.00 USD | 250,560.00 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 11,460,000.00 USD | 0.00 USD | 437.67 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 11,460,000.00 USD | 0.00 USD | 1,500.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 11,460,000.00 USD | 0.00 USD | 915.81 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 11,460,000.00 USD | 0.00 USD | 120.48 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 11,460,000.00 USD | 0.00 USD | 105.23 USD | `-11.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 11,460,000.00 USD | 0.00 USD | 310.05 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 11,460,000.00 USD | 0.00 USD | 142.34 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 11,460,000.00 USD | 0.00 USD | 1,370.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 11,450,000.00 USD | 0.00 USD | 604.23 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 11,450,000.00 USD | 0.00 USD | 8,070.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 11,450,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 11,440,000.00 USD | 0.00 USD | 538.20 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 11,440,000.00 USD | 0.00 USD | 4,080.00 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 11,440,000.00 USD | 0.00 USD | 2,540.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 11,440,000.00 USD | 0.00 USD | 417.17 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 11,440,000.00 USD | 0.00 USD | 305.87 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 11,440,000.00 USD | 0.00 USD | 2,020.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 11,430,000.00 USD | 0.00 USD | 1,160.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 11,430,000.00 USD | 0.00 USD | 132.16 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 11,430,000.00 USD | 0.00 USD | 297,900.00 USD | `-10.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 11,130,000.00 USD | 0.00 USD | 435.75 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 11,130,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 11,130,000.00 USD | 0.00 USD | 436.75 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 11,130,000.00 USD | 0.00 USD | 730.21 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 11,130,000.00 USD | 0.00 USD | 316.93 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 11,120,000.00 USD | 0.00 USD | 2,880.00 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 11,120,000.00 USD | 0.00 USD | 177.66 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 11,120,000.00 USD | 0.00 USD | 88,070.00 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 11,030,000.00 USD | 0.00 USD | 1,050.00 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 11,030,000.00 USD | 0.00 USD | 8,860.00 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 11,020,000.00 USD | 0.00 USD | 29,150.00 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 10,990,000.00 USD | 0.00 USD | 1,010.00 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 10,990,000.00 USD | 0.00 USD | 7,610.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 10,990,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 10,960,000.00 USD | 0.00 USD | 53,250.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 10,910,000.00 USD | 0.00 USD | 95,650.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 10,810,000.00 USD | 0.00 USD | 141.43 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 10,810,000.00 USD | 0.00 USD | 8,910.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 10,800,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 10,790,000.00 USD | 0.00 USD | 960.33 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 10,790,000.00 USD | 0.00 USD | 4,220.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 10,790,000.00 USD | 0.00 USD | 13,620.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 10,780,000.00 USD | 0.00 USD | 348.35 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 10,780,000.00 USD | 0.00 USD | 173.02 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 10,770,000.00 USD | 0.00 USD | 105.01 USD | `-7.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 10,770,000.00 USD | 0.00 USD | 20,850.00 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 10,750,000.00 USD | 0.00 USD | 86,920.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 10,670,000.00 USD | 0.00 USD | 680,960.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 9,990,000.00 USD | 0.00 USD | 180.30 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 9,990,000.00 USD | 0.00 USD | 13,600.00 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 9,970,000.00 USD | 0.00 USD | 4,900.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 9,970,000.00 USD | 0.00 USD | 2,670.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 9,960,000.00 USD | 0.00 USD | 663.56 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 9,960,000.00 USD | 0.00 USD | 17,680.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 9,950,000.00 USD | 0.00 USD | 13,930.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 9,930,000.00 USD | 0.00 USD | 9,110.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 9,920,000.00 USD | 0.00 USD | 69,530.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 9,850,000.00 USD | 0.00 USD | 975.30 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 9,850,000.00 USD | 0.00 USD | 5,560.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 9,850,000.00 USD | 0.00 USD | 5,840.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 9,840,000.00 USD | 0.00 USD | 920.90 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 9,840,000.00 USD | 0.00 USD | 421,630.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 9,420,000.00 USD | 0.00 USD | 27,950.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 9,390,000.00 USD | 0.00 USD | 2,450.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 9,390,000.00 USD | 0.00 USD | 41,740.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 9,350,000.00 USD | 0.00 USD | 26,880.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 9,320,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 7,730,000.00 USD | 0.00 USD | 2,030.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 7,730,000.00 USD | 0.00 USD | 139.30 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 7,730,000.00 USD | 0.00 USD | 19,510.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 7,710,000.00 USD | 0.00 USD | 10,590.00 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 7,700,000.00 USD | 0.00 USD | 12,530.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 7,680,000.00 USD | 0.00 USD | 12,220.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 7,670,000.00 USD | 0.00 USD | 11,740.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 7,660,000.00 USD | 0.00 USD | 28,600.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 7,630,000.00 USD | 0.00 USD | 61,570.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 7,570,000.00 USD | 0.00 USD | 76,480.00 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 7,490,000.00 USD | 0.00 USD | 712.60 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 7,490,000.00 USD | 0.00 USD | 8,050.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 7,480,000.00 USD | 0.00 USD | 1,160.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 7,480,000.00 USD | 0.00 USD | 94,000.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 7,390,000.00 USD | 0.00 USD | 570,010.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 6,820,000.00 USD | 0.00 USD | 440,480.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 6,380,000.00 USD | 0.00 USD | 11,210.00 USD | `-3.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 6,370,000.00 USD | 0.00 USD | 36,730.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 6,330,000.00 USD | 0.00 USD | 41,100.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 6,290,000.00 USD | 0.00 USD | 558,180.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 5,730,000.00 USD | 0.00 USD | 11,070.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 5,720,000.00 USD | 0.00 USD | 31,500.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 5,690,000.00 USD | 0.00 USD | 4,120.00 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 5,690,000.00 USD | 0.00 USD | 49,310.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 5,640,000.00 USD | 0.00 USD | 94,860.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 5,540,000.00 USD | 0.00 USD | 930,150.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 4,610,000.00 USD | 0.00 USD | 57,510.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 4,550,000.00 USD | 0.00 USD | 2,020,000.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 2,530,000.00 USD | 0.00 USD | 14,150.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 2,520,000.00 USD | 0.00 USD | 320,040.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 2,200,000.00 USD | 0.00 USD | 44,760.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 2,150,000.00 USD | 0.00 USD | 48,920.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 2,100,000.00 USD | 0.00 USD | 3,810.00 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 2,100,000.00 USD | 0.00 USD | 8,800.00 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 2,090,000.00 USD | 0.00 USD | 51,850.00 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 2,040,000.00 USD | 0.00 USD | 6,350.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 2,030,000.00 USD | 0.00 USD | 50,810.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 1,980,000.00 USD | 0.00 USD | 11,390.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 1,970,000.00 USD | 0.00 USD | 1,850.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 1,970,000.00 USD | 0.00 USD | 214,260.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 1,750,000.00 USD | 0.00 USD | 106,340.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 1,650,000.00 USD | 0.00 USD | 8,770.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 1,640,000.00 USD | 0.00 USD | 3,180.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 1,630,000.00 USD | 0.00 USD | 290,800.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 1,340,000.00 USD | 0.00 USD | 82,100.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 1,260,000.00 USD | 0.00 USD | 53,870.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 1,210,000.00 USD | 0.00 USD | 1,980.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 1,210,000.00 USD | 0.00 USD | 195,810.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.05` | 71,680.00 USD | 71,680.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.15` | 79,850.00 USD | 8,170.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 95,720.00 USD | 15,870.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 97,880.00 USD | 2,160.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 99,740.00 USD | 1,860.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 100,750.00 USD | 1,010.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 112,970.00 USD | 12,220.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 115,980.00 USD | 3,010.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 116,360.00 USD | 384.55 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 144,910.00 USD | 28,550.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 160,210.00 USD | 15,290.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 375,490.00 USD | 215,290.00 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 387,280.00 USD | 11,790.00 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 391,830.00 USD | 4,550.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 497,470.00 USD | 105,640.00 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 553,660.00 USD | 56,200.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 658,840.00 USD | 105,180.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 686,700.00 USD | 27,860.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 697,470.00 USD | 10,770.00 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 701,590.00 USD | 4,110.00 USD | 0.00 USD | `+2.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 912,750.00 USD | 211,170.00 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 919,090.00 USD | 6,330.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 919,610.00 USD | 520.07 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 927,500.00 USD | 7,890.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 929,280.00 USD | 1,790.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 934,600.00 USD | 5,310.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 936,920.00 USD | 2,330.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 943,200.00 USD | 6,280.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 946,560.00 USD | 3,350.00 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 950,970.00 USD | 4,420.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,010,000.00 USD | 54,510.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 1,020,000.00 USD | 13,440.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 1,030,000.00 USD | 8,530.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 1,030,000.00 USD | 4,750.00 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 1,820,000.00 USD | 784,920.00 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 1,820,000.00 USD | 313.72 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 1,820,000.00 USD | 165.07 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 1,820,000.00 USD | 1,020.00 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 1,820,000.00 USD | 5,260.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 1,830,000.00 USD | 5,040.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 2,380,000.00 USD | 547,260.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 2,450,000.00 USD | 72,390.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 2,450,000.00 USD | 3,080.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 2,450,000.00 USD | 3,120.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 2,460,000.00 USD | 7,180.00 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 2,460,000.00 USD | 2,560.00 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 2,470,000.00 USD | 9,160.00 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 2,520,000.00 USD | 50,380.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 2,530,000.00 USD | 4,970.00 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 2,540,000.00 USD | 6,970.00 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 2,760,000.00 USD | 225,550.00 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 2,780,000.00 USD | 17,560.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 2,790,000.00 USD | 13,380.00 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 3,450,000.00 USD | 657,460.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 3,470,000.00 USD | 20,640.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 3,510,000.00 USD | 34,910.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 3,520,000.00 USD | 10,590.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 3,520,000.00 USD | 1,810.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 3,520,000.00 USD | 1,070.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 3,530,000.00 USD | 7,920.00 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 3,570,000.00 USD | 45,780.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 3,740,000.00 USD | 166,600.00 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 3,850,000.00 USD | 109,440.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 3,860,000.00 USD | 8,580.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 3,860,000.00 USD | 3,760.00 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 3,870,000.00 USD | 7,280.00 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 3,870,000.00 USD | 2,660.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 3,870,000.00 USD | 611.09 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 4,130,000.00 USD | 254,760.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 4,190,000.00 USD | 59,050.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 4,220,000.00 USD | 35,010.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 4,220,000.00 USD | 1,980.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 4,220,000.00 USD | 733.92 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 4,220,000.00 USD | 146.09 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 4,230,000.00 USD | 5,400.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 4,250,000.00 USD | 17,430.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 4,270,000.00 USD | 21,730.00 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 4,270,000.00 USD | 1,100.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 4,270,000.00 USD | 5,900.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 4,300,000.00 USD | 25,930.00 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 4,360,000.00 USD | 62,730.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 4,390,000.00 USD | 27,500.00 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 4,390,000.00 USD | 1,210.00 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 4,390,000.00 USD | 1,110.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 4,390,000.00 USD | 1,680.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 4,400,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 4,400,000.00 USD | 235.60 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 4,410,000.00 USD | 10,860.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 4,420,000.00 USD | 11,960.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 4,420,000.00 USD | 101.71 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 4,440,000.00 USD | 20,560.00 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 4,450,000.00 USD | 9,170.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 4,450,000.00 USD | 935.00 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 4,530,000.00 USD | 82,010.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 4,560,000.00 USD | 26,280.00 USD | 0.00 USD | `+9.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 4,570,000.00 USD | 6,950.00 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 4,570,000.00 USD | 355.14 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 4,680,000.00 USD | 110,390.00 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 4,680,000.00 USD | 1,000.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 4,710,000.00 USD | 29,910.00 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 4,730,000.00 USD | 17,970.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 4,730,000.00 USD | 1,200.00 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 4,750,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 4,750,000.00 USD | 698.85 USD | 0.00 USD | `+10.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 4,760,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 4,810,000.00 USD | 52,130.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 4,880,000.00 USD | 71,910.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 4,880,000.00 USD | 164.86 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 4,890,000.00 USD | 4,420.00 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 4,890,000.00 USD | 930.53 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 4,950,000.00 USD | 63,540.00 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 5,020,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.25` | 5,020,000.00 USD | 1,240.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 5,040,000.00 USD | 15,750.00 USD | 0.00 USD | `+11.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 5,040,000.00 USD | 4,500.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 5,060,000.00 USD | 16,860.00 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 5,060,000.00 USD | 2,310.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 5,060,000.00 USD | 2,120.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 5,070,000.00 USD | 3,260.00 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 5,110,000.00 USD | 42,240.00 USD | 0.00 USD | `+12.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 5,130,000.00 USD | 21,010.00 USD | 0.00 USD | `+12.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 5,140,000.00 USD | 8,620.00 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 9,210,000.00 USD | 4,070,000.00 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 9,250,000.00 USD | 44,780.00 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 9,270,000.00 USD | 19,080.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 9,270,000.00 USD | 1,170.00 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 9,280,000.00 USD | 7,430.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 9,280,000.00 USD | 4,370.00 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 9,280,000.00 USD | 1,210.00 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 9,290,000.00 USD | 583.83 USD | 0.00 USD | `+13.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 9,850,000.00 USD | 564,110.00 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 9,850,000.00 USD | 340.36 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 9,850,000.00 USD | 102.53 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 9,850,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 9,850,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 9,860,000.00 USD | 10,820.00 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 9,870,000.00 USD | 3,030.00 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 9,880,000.00 USD | 17,520.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 10,110,000.00 USD | 227,610.00 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 10,110,000.00 USD | 799.56 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 10,110,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 10,120,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 10,120,000.00 USD | 842.56 USD | 0.00 USD | `+14.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 10,130,000.00 USD | 6,380.00 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 10,130,000.00 USD | 106.07 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 10,130,000.00 USD | 2,420.00 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 10,130,000.00 USD | 2,100.00 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.95` | 10,130,000.00 USD | 559.75 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 10,150,000.00 USD | 17,640.00 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 10,200,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 10,200,000.00 USD | 4,960.00 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 10,210,000.00 USD | 4,920.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 10,210,000.00 USD | 2,290.00 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 10,250,000.00 USD | 36,280.00 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 10,250,000.00 USD | 1,690.00 USD | 0.00 USD | `+16.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 10,250,000.00 USD | 586.82 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 10,330,000.00 USD | 81,750.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.15` | 10,330,000.00 USD | 427.71 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 10,330,000.00 USD | 349.94 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 10,460,000.00 USD | 128,070.00 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 10,460,000.00 USD | 655.74 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 10,490,000.00 USD | 25,440.00 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 10,490,000.00 USD | 230.71 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 10,490,000.00 USD | 257.07 USD | 0.00 USD | `+17.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 10,490,000.00 USD | 5,140.00 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 10,490,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 10,510,000.00 USD | 11,410.00 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 10,510,000.00 USD | 584.96 USD | 0.00 USD | `+17.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 10,520,000.00 USD | 9,320.00 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 10,520,000.00 USD | 343.35 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 10,520,000.00 USD | 5,150.00 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 10,530,000.00 USD | 11,800.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 10,530,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 10,540,000.00 USD | 2,630.00 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 10,620,000.00 USD | 81,650.00 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 10,620,000.00 USD | 448.71 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 10,640,000.00 USD | 23,260.00 USD | 0.00 USD | `+19.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 10,640,000.00 USD | 2,210.00 USD | 0.00 USD | `+19.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 10,650,000.00 USD | 579.25 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 10,670,000.00 USD | 20,280.00 USD | 0.00 USD | `+19.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 10,670,000.00 USD | 1,730.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 10,670,000.00 USD | 3,840.00 USD | 0.00 USD | `+19.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 10,680,000.00 USD | 4,160.00 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,690,000.00 USD | 10,810.00 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,690,000.00 USD | 1,100.00 USD | 0.00 USD | `+20.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,690,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,690,000.00 USD | 234.87 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,690,000.00 USD | 1,170.00 USD | 0.00 USD | `+20.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,700,000.00 USD | 4,990.00 USD | 0.00 USD | `+20.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,700,000.00 USD | 686.50 USD | 0.00 USD | `+20.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,700,000.00 USD | 349.40 USD | 0.00 USD | `+20.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,700,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,810,000.00 USD | 108,640.00 USD | 0.00 USD | `+21.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,910,000.00 USD | 105,720.00 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,920,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,980,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 11,050,000.00 USD | 71,690.00 USD | 0.00 USD | `+21.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 11,060,000.00 USD | 13,120.00 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 11,060,000.00 USD | 2,830.00 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 11,080,000.00 USD | 12,610.00 USD | 0.00 USD | `+22.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 11,080,000.00 USD | 707.15 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 11,150,000.00 USD | 70,980.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 11,150,000.00 USD | 593.25 USD | 0.00 USD | `+22.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 11,150,000.00 USD | 403.75 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 11,170,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 11,210,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 11,290,000.00 USD | 84,580.00 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 11,300,000.00 USD | 8,120.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 11,300,000.00 USD | 2,050.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 11,310,000.00 USD | 4,150.00 USD | 0.00 USD | `+23.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 11,310,000.00 USD | 3,580.00 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 11,310,000.00 USD | 615.00 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 11,440,000.00 USD | 125,500.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 11,470,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 11,470,000.00 USD | 458.21 USD | 0.00 USD | `+23.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 11,610,000.00 USD | 137,400.00 USD | 0.00 USD | `+23.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 11,610,000.00 USD | 414.52 USD | 0.00 USD | `+23.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 11,620,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 11,620,000.00 USD | 7,850.00 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 11,620,000.00 USD | 184.29 USD | 0.00 USD | `+24.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 11,620,000.00 USD | 964.40 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 11,620,000.00 USD | 191.83 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 11,630,000.00 USD | 2,150.00 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 11,630,000.00 USD | 650.17 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 11,650,000.00 USD | 20,950.00 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 11,650,000.00 USD | 122.36 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 11,660,000.00 USD | 8,780.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 11,670,000.00 USD | 11,570.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 11,680,000.00 USD | 7,860.00 USD | 0.00 USD | `+25.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 11,680,000.00 USD | 4,360.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 11,680,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 11,690,000.00 USD | 7,600.00 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 11,700,000.00 USD | 12,910.00 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,910,000.00 USD | 203,590.00 USD | 0.00 USD | `+25.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,910,000.00 USD | 2,690.00 USD | 0.00 USD | `+25.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 12,150,000.00 USD | 235,280.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 12,200,000.00 USD | 52,330.00 USD | 0.00 USD | `+26.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 12,200,000.00 USD | 5,060.00 USD | 0.00 USD | `+26.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 12,210,000.00 USD | 7,020.00 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 12,220,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 12,220,000.00 USD | 235.68 USD | 0.00 USD | `+26.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 12,220,000.00 USD | 3,780.00 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 12,240,000.00 USD | 11,830.00 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 13,240,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+26.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 13,240,000.00 USD | 252.46 USD | 0.00 USD | `+26.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 13,250,000.00 USD | 7,710.00 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 13,250,000.00 USD | 6,790.00 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 13,260,000.00 USD | 2,670.00 USD | 0.00 USD | `+27.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 13,260,000.00 USD | 632.58 USD | 0.00 USD | `+27.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 13,270,000.00 USD | 11,600.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 13,280,000.00 USD | 11,530.00 USD | 0.00 USD | `+27.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 13,300,000.00 USD | 18,820.00 USD | 0.00 USD | `+27.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 13,370,000.00 USD | 74,530.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 13,380,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 13,380,000.00 USD | 151.59 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 13,380,000.00 USD | 4,110.00 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 13,380,000.00 USD | 1,370.00 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 13,390,000.00 USD | 7,330.00 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 13,400,000.00 USD | 7,280.00 USD | 0.00 USD | `+28.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 13,400,000.00 USD | 596.78 USD | 0.00 USD | `+28.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 13,410,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,940,000.00 USD | 536,280.00 USD | 0.00 USD | `+28.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,940,000.00 USD | 178.96 USD | 0.00 USD | `+29.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,940,000.00 USD | 311.87 USD | 0.00 USD | `+29.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,950,000.00 USD | 1,310.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,950,000.00 USD | 3,320.00 USD | 0.00 USD | `+29.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,960,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,970,000.00 USD | 471.94 USD | 0.00 USD | `+29.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,970,000.00 USD | 209.08 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 14,120,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 14,130,000.00 USD | 12,800.00 USD | 0.00 USD | `+30.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 14,130,000.00 USD | 187.15 USD | 0.00 USD | `+30.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 14,130,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 14,140,000.00 USD | 6,100.00 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 14,400,000.00 USD | 263,730.00 USD | 0.00 USD | `+30.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 14,400,000.00 USD | 534.87 USD | 0.00 USD | `+31.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 14,410,000.00 USD | 4,290.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 14,410,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 14,410,000.00 USD | 362.81 USD | 0.00 USD | `+31.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 14,470,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 14,470,000.00 USD | 482.37 USD | 0.00 USD | `+31.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 14,520,000.00 USD | 48,740.00 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 14,530,000.00 USD | 3,010.00 USD | 0.00 USD | `+32.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 14,530,000.00 USD | 191.09 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.85` | 14,530,000.00 USD | 132.72 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 14,540,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 14,590,000.00 USD | 50,720.00 USD | 0.00 USD | `+33.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 14,610,000.00 USD | 15,330.00 USD | 0.00 USD | `+33.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 14,610,000.00 USD | 401.29 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 14,610,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 14,610,000.00 USD | 152.99 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 14,610,000.00 USD | 1,040.00 USD | 0.00 USD | `+33.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 14,610,000.00 USD | 116.87 USD | 0.00 USD | `+33.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 14,630,000.00 USD | 26,240.00 USD | 0.00 USD | `+34.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 14,640,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 14,640,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 14,640,000.00 USD | 192.06 USD | 0.00 USD | `+34.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 14,640,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 14,650,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 14,660,000.00 USD | 10,140.00 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 14,660,000.00 USD | 6,000.00 USD | 0.00 USD | `+35.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 14,670,000.00 USD | 5,950.00 USD | 0.00 USD | `+35.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 14,670,000.00 USD | 6,160.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 14,840,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 14,840,000.00 USD | 144.93 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 14,860,000.00 USD | 24,010.00 USD | 0.00 USD | `+36.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 14,860,000.00 USD | 397.95 USD | 0.00 USD | `+36.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 14,870,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 14,870,000.00 USD | 3,910.00 USD | 0.00 USD | `+37.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 14,880,000.00 USD | 6,700.00 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 14,880,000.00 USD | 509.96 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 14,880,000.00 USD | 191.88 USD | 0.00 USD | `+37.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 14,880,000.00 USD | 237.36 USD | 0.00 USD | `+37.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 14,880,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 14,880,000.00 USD | 192.46 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 14,880,000.00 USD | 112.35 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 14,890,000.00 USD | 4,150.00 USD | 0.00 USD | `+38.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,940,000.00 USD | 54,080.00 USD | 0.00 USD | `+38.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,940,000.00 USD | 331.60 USD | 0.00 USD | `+38.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 15,140,000.00 USD | 195,540.00 USD | 0.00 USD | `+38.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 15,140,000.00 USD | 647.28 USD | 0.00 USD | `+39.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 15,210,000.00 USD | 74,910.00 USD | 0.00 USD | `+39.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 15,220,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 15,220,000.00 USD | 1,890.00 USD | 0.00 USD | `+40.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 15,220,000.00 USD | 192.25 USD | 0.00 USD | `+40.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 15,220,000.00 USD | 465.29 USD | 0.00 USD | `+40.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 15,220,000.00 USD | 389.17 USD | 0.00 USD | `+40.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 15,220,000.00 USD | 826.57 USD | 0.00 USD | `+41.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 15,220,000.00 USD | 1,330.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 15,230,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 15,230,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 15,260,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 15,260,000.00 USD | 133.62 USD | 0.00 USD | `+42.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 15,280,000.00 USD | 18,910.00 USD | 0.00 USD | `+42.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 15,280,000.00 USD | 692.25 USD | 0.00 USD | `+42.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 15,280,000.00 USD | 406.24 USD | 0.00 USD | `+42.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 22,020,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+43.15%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 22,020,000.00 USD | 826.75 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 24,220,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+43.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 24,230,000.00 USD | 7,530.00 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 24,330,000.00 USD | 97,310.00 USD | 0.00 USD | `+44.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 24,430,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 24,430,000.00 USD | 990.88 USD | 0.00 USD | `+45.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 24,430,000.00 USD | 3,510.00 USD | 0.00 USD | `+45.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 24,440,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 24,440,000.00 USD | 796.07 USD | 0.00 USD | `+46.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 24,440,000.00 USD | 826.73 USD | 0.00 USD | `+46.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 24,440,000.00 USD | 278.56 USD | 0.00 USD | `+47.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 24,790,000.00 USD | 346,420.00 USD | 0.00 USD | `+47.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 25,000,000.00 USD | 215,510.00 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 25,000,000.00 USD | 528.96 USD | 0.00 USD | `+47.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 25,010,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 25,010,000.00 USD | 415.44 USD | 0.00 USD | `+48.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 25,290,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 25,300,000.00 USD | 7,260.00 USD | 0.00 USD | `+49.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 25,300,000.00 USD | 791.78 USD | 0.00 USD | `+49.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 25,320,000.00 USD | 21,070.00 USD | 0.00 USD | `+49.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 25,320,000.00 USD | 209.16 USD | 0.00 USD | `+49.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 25,320,000.00 USD | 698.64 USD | 0.00 USD | `+50.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 25,510,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 25,510,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 25,520,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 25,520,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 25,550,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 25,560,000.00 USD | 844.89 USD | 0.00 USD | `+52.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 25,560,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 25,560,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 26,900,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 26,900,000.00 USD | 1,370.00 USD | 0.00 USD | `+53.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 26,900,000.00 USD | 773.95 USD | 0.00 USD | `+53.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 26,900,000.00 USD | 549.99 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 27,410,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 27,770,000.00 USD | 352,280.00 USD | 0.00 USD | `+54.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 27,770,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 27,770,000.00 USD | 178.92 USD | 0.00 USD | `+55.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 27,770,000.00 USD | 1,360.00 USD | 0.00 USD | `+55.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 27,780,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 27,790,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 27,790,000.00 USD | 411.94 USD | 0.00 USD | `+56.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.95` | 27,800,000.00 USD | 10,230.00 USD | 0.00 USD | `+56.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.15` | 27,810,000.00 USD | 12,000.00 USD | 0.00 USD | `+56.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 27,820,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 27,820,000.00 USD | 1,020.00 USD | 0.00 USD | `+58.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 27,830,000.00 USD | 12,000.00 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 27,830,000.00 USD | 113.04 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 27,830,000.00 USD | 1,830.00 USD | 0.00 USD | `+59.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 27,850,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 27,850,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 27,860,000.00 USD | 6,640.00 USD | 0.00 USD | `+62.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 27,880,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 27,880,000.00 USD | 692.30 USD | 0.00 USD | `+64.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 27,880,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 27,970,000.00 USD | 90,570.00 USD | 0.00 USD | `+65.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 27,970,000.00 USD | 281.84 USD | 0.00 USD | `+66.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 27,980,000.00 USD | 4,080.00 USD | 0.00 USD | `+68.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 28,060,000.00 USD | 82,530.00 USD | 0.00 USD | `+70.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 28,060,000.00 USD | 823.94 USD | 0.00 USD | `+70.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 28,060,000.00 USD | 211.39 USD | 0.00 USD | `+71.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 28,060,000.00 USD | 307.19 USD | 0.00 USD | `+72.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 28,060,000.00 USD | 593.03 USD | 0.00 USD | `+72.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 28,060,000.00 USD | 1,440.00 USD | 0.00 USD | `+72.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 28,070,000.00 USD | 5,720.00 USD | 0.00 USD | `+73.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 28,070,000.00 USD | 495.09 USD | 0.00 USD | `+74.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 28,070,000.00 USD | 912.63 USD | 0.00 USD | `+75.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 28,110,000.00 USD | 42,840.00 USD | 0.00 USD | `+75.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 28,110,000.00 USD | 686.20 USD | 0.00 USD | `+76.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 28,150,000.00 USD | 35,280.00 USD | 0.00 USD | `+77.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 28,150,000.00 USD | 703.60 USD | 0.00 USD | `+77.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 28,150,000.00 USD | 3,160.00 USD | 0.00 USD | `+78.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 28,210,000.00 USD | 52,520.00 USD | 0.00 USD | `+80.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 28,230,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 28,230,000.00 USD | 1,450.00 USD | 0.00 USD | `+82.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 28,230,000.00 USD | 1,840.00 USD | 0.00 USD | `+82.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 28,230,000.00 USD | 2,990.00 USD | 0.00 USD | `+84.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 28,230,000.00 USD | 261.56 USD | 0.00 USD | `+84.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 28,300,000.00 USD | 70,250.00 USD | 0.00 USD | `+85.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 28,310,000.00 USD | 2,440.00 USD | 0.00 USD | `+86.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 28,310,000.00 USD | 349.34 USD | 0.00 USD | `+87.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 28,330,000.00 USD | 19,620.00 USD | 0.00 USD | `+88.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 28,880,000.00 USD | 550,350.00 USD | 0.00 USD | `+89.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 28,910,000.00 USD | 29,610.00 USD | 0.00 USD | `+90.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 29,100,000.00 USD | 198,160.00 USD | 0.00 USD | `+92.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 29,250,000.00 USD | 141,190.00 USD | 0.00 USD | `+93.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 29,280,000.00 USD | 35,880.00 USD | 0.00 USD | `+95.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 29,280,000.00 USD | 744.27 USD | 0.00 USD | `+96.24%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `86.30` | 98,710,000.00 USD | 0.00 USD | 98,710,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD |
| `7D` | `86.50` | 98,560,000.00 USD | 0.00 USD | 98,560,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `1D` | `86.60` | 71,350,000.00 USD | 0.00 USD | 71,350,000.00 USD | 0.00 USD | 306,270.00 USD | 3,100.00 USD |
| `1D` | `86.80` | 71,040,000.00 USD | 0.00 USD | 71,040,000.00 USD | 0.00 USD | 69,010.00 USD | 4,330.00 USD |
| `7D` | `86.90` | 98,550,000.00 USD | 0.00 USD | 98,550,000.00 USD | 207,900.00 USD | 138,700.00 USD | 0.00 USD |
| `1D` | `87.00` | 70,960,000.00 USD | 0.00 USD | 70,960,000.00 USD | 150,240.00 USD | 112,850.00 USD | 0.00 USD |
| `7D` | `87.10` | 98,210,000.00 USD | 0.00 USD | 98,210,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD |
| `1D` | `87.20` | 70,700,000.00 USD | 0.00 USD | 70,700,000.00 USD | 8,680.00 USD | 79,810.00 USD | 162,690.00 USD |
| `7D` | `87.30` | 98,200,000.00 USD | 0.00 USD | 98,200,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD |
| `1D` | `87.40` | 70,450,000.00 USD | 0.00 USD | 70,450,000.00 USD | 8,750.00 USD | 95,800.00 USD | 40,280.00 USD |
| `7D` | `87.50` | 97,710,000.00 USD | 0.00 USD | 97,710,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD |
| `1D` | `87.60` | 70,300,000.00 USD | 0.00 USD | 70,300,000.00 USD | 10,160.00 USD | 50,950.00 USD | 5,580.00 USD |
| `7D` | `87.70` | 97,660,000.00 USD | 0.00 USD | 97,660,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD |
| `1D` | `87.80` | 70,240,000.00 USD | 0.00 USD | 70,240,000.00 USD | 22,290.00 USD | 112,630.00 USD | 716,950.00 USD |
| `7D` | `87.90` | 96,950,000.00 USD | 0.00 USD | 96,950,000.00 USD | 0.00 USD | 295,390.00 USD | 0.00 USD |
| `1D` | `88.00` | 69,390,000.00 USD | 0.00 USD | 69,390,000.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD |
| `1D` | `88.60` | 68,900,000.00 USD | 0.00 USD | 68,900,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD |
| `7D` | `88.70` | 96,660,000.00 USD | 0.00 USD | 96,660,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.80` | 68,890,000.00 USD | 0.00 USD | 68,890,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD |
| `7D` | `88.90` | 96,430,000.00 USD | 0.00 USD | 96,430,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD |
| `1D` | `89.00` | 68,000,000.00 USD | 0.00 USD | 68,000,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD |
| `7D` | `89.10` | 96,410,000.00 USD | 0.00 USD | 96,410,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD |
| `1D` | `89.20` | 67,770,000.00 USD | 0.00 USD | 67,770,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD |
| `7D` | `89.30` | 95,190,000.00 USD | 0.00 USD | 95,190,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD |
| `1D` | `89.40` | 67,500,000.00 USD | 0.00 USD | 67,500,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD |
| `7D` | `89.50` | 95,160,000.00 USD | 0.00 USD | 95,160,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD |
| `1D` | `89.60` | 67,130,000.00 USD | 0.00 USD | 67,130,000.00 USD | 557,950.00 USD | 163,120.00 USD | 317,090.00 USD |
| `7D` | `89.70` | 94,370,000.00 USD | 0.00 USD | 94,370,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD |
| `1D` | `89.80` | 66,090,000.00 USD | 0.00 USD | 66,090,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD |
| `7D` | `89.90` | 92,950,000.00 USD | 0.00 USD | 92,950,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `1D` | `90.00` | 64,980,000.00 USD | 0.00 USD | 64,980,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD |
| `7D` | `90.10` | 91,150,000.00 USD | 0.00 USD | 91,150,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `1D` | `90.20` | 63,630,000.00 USD | 0.00 USD | 63,630,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `90.30` | 88,780,000.00 USD | 0.00 USD | 88,780,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `90.40` | 62,310,000.00 USD | 0.00 USD | 62,310,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `90.50` | 86,700,000.00 USD | 0.00 USD | 86,700,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD |
| `1D` | `90.60` | 60,950,000.00 USD | 0.00 USD | 60,950,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD |
| `7D` | `90.70` | 84,020,000.00 USD | 0.00 USD | 84,020,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `90.80` | 59,810,000.00 USD | 0.00 USD | 59,810,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `90.90` | 81,570,000.00 USD | 0.00 USD | 81,570,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `91.00` | 59,600,000.00 USD | 0.00 USD | 59,600,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `91.10` | 79,190,000.00 USD | 0.00 USD | 79,190,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `91.20` | 59,410,000.00 USD | 0.00 USD | 59,410,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD |
| `7D` | `91.30` | 77,280,000.00 USD | 0.00 USD | 77,280,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `91.40` | 59,390,000.00 USD | 0.00 USD | 59,390,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD |
| `7D` | `91.50` | 74,780,000.00 USD | 0.00 USD | 74,780,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD |
| `1D` | `91.60` | 59,210,000.00 USD | 0.00 USD | 59,210,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD |
| `7D` | `91.70` | 71,870,000.00 USD | 0.00 USD | 71,870,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `91.80` | 59,090,000.00 USD | 0.00 USD | 59,090,000.00 USD | 250,490.00 USD | 103,030.00 USD | 525,270.00 USD |
| `7D` | `91.90` | 70,230,000.00 USD | 0.00 USD | 70,230,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `1D` | `92.00` | 58,210,000.00 USD | 0.00 USD | 58,210,000.00 USD | 38,300.00 USD | 274,720.00 USD | 87,940.00 USD |
| `7D` | `92.10` | 67,820,000.00 USD | 0.00 USD | 67,820,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD |
| `1D` | `92.20` | 57,810,000.00 USD | 0.00 USD | 57,810,000.00 USD | 63,310.00 USD | 149,590.00 USD | 43,140.00 USD |
| `7D` | `92.30` | 66,120,000.00 USD | 0.00 USD | 66,120,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD |
| `1D` | `92.40` | 57,550,000.00 USD | 0.00 USD | 57,550,000.00 USD | 111,190.00 USD | 824,620.00 USD | 877,000.00 USD |
| `7D` | `92.50` | 63,770,000.00 USD | 0.00 USD | 63,770,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD |
| `1D` | `92.60` | 55,740,000.00 USD | 0.00 USD | 55,740,000.00 USD | 355,570.00 USD | 341,420.00 USD | 10,820.00 USD |
| `7D` | `92.70` | 62,000,000.00 USD | 0.00 USD | 62,000,000.00 USD | 671,470.00 USD | 168,780.00 USD | 70,750.00 USD |
| `1D` | `92.80` | 55,030,000.00 USD | 0.00 USD | 55,030,000.00 USD | 26,180.00 USD | 406,530.00 USD | 166,400.00 USD |
| `7D` | `92.90` | 61,090,000.00 USD | 0.00 USD | 61,090,000.00 USD | 0.00 USD | 74,260.00 USD | 0.00 USD |
| `1D` | `93.00` | 54,430,000.00 USD | 0.00 USD | 54,430,000.00 USD | 21,710.00 USD | 199,520.00 USD | 406,710.00 USD |
| `7D` | `93.10` | 61,010,000.00 USD | 0.00 USD | 61,010,000.00 USD | 31,020.00 USD | 630,650.00 USD | 1,000,000.00 USD |
| `1D` | `93.20` | 53,800,000.00 USD | 0.00 USD | 53,800,000.00 USD | 32,310.00 USD | 398,190.00 USD | 100,690.00 USD |
| `7D` | `93.30` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 145,070.00 USD | 66,280.00 USD | 468,690.00 USD |
| `1D` | `93.40` | 53,270,000.00 USD | 0.00 USD | 53,270,000.00 USD | 57,590.00 USD | 433,830.00 USD | 141,640.00 USD |
| `7D` | `93.50` | 58,670,000.00 USD | 0.00 USD | 58,670,000.00 USD | 93,960.00 USD | 1,260,000.00 USD | 1,450,000.00 USD |
| `1D` | `93.60` | 52,640,000.00 USD | 0.00 USD | 52,640,000.00 USD | 64,480.00 USD | 472,950.00 USD | 1,790,000.00 USD |
| `7D` | `93.70` | 55,870,000.00 USD | 0.00 USD | 55,870,000.00 USD | 270,240.00 USD | 954,120.00 USD | 120,980.00 USD |
| `1D` | `93.80` | 50,320,000.00 USD | 0.00 USD | 50,320,000.00 USD | 63,080.00 USD | 1,320,000.00 USD | 1,770,000.00 USD |
| `7D` | `93.90` | 54,530,000.00 USD | 0.00 USD | 54,530,000.00 USD | 168,420.00 USD | 56,340.00 USD | 23,050.00 USD |
| `1D` | `94.00` | 47,160,000.00 USD | 0.00 USD | 47,160,000.00 USD | 60,590.00 USD | 86,320.00 USD | 0.00 USD |
| `7D` | `94.10` | 54,280,000.00 USD | 0.00 USD | 54,280,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD |
| `1D` | `94.20` | 47,010,000.00 USD | 0.00 USD | 47,010,000.00 USD | 0.00 USD | 691,260.00 USD | 702,910.00 USD |
| `7D` | `94.30` | 52,700,000.00 USD | 0.00 USD | 52,700,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD |
| `1D` | `94.40` | 45,620,000.00 USD | 0.00 USD | 45,620,000.00 USD | 33,670.00 USD | 1,130,000.00 USD | 15,520.00 USD |
| `7D` | `94.50` | 51,980,000.00 USD | 0.00 USD | 51,980,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD |
| `1D` | `94.60` | 44,440,000.00 USD | 0.00 USD | 44,440,000.00 USD | 784,790.00 USD | 597,770.00 USD | 2,080,000.00 USD |
| `7D` | `94.70` | 50,900,000.00 USD | 0.00 USD | 50,900,000.00 USD | 1,600,000.00 USD | 238,650.00 USD | 0.00 USD |
| `1D` | `94.80` | 40,970,000.00 USD | 0.00 USD | 40,970,000.00 USD | 762,670.00 USD | 2,150,000.00 USD | 1,180,000.00 USD |
| `7D` | `94.90` | 49,060,000.00 USD | 0.00 USD | 49,060,000.00 USD | 1,100,000.00 USD | 2,260,000.00 USD | 0.00 USD |
| `1D` | `95.00` | 36,880,000.00 USD | 0.00 USD | 36,880,000.00 USD | 562,710.00 USD | 1,120,000.00 USD | 816,740.00 USD |
| `7D` | `95.10` | 45,700,000.00 USD | 0.00 USD | 45,700,000.00 USD | 198,380.00 USD | 1,270,000.00 USD | 2,770,000.00 USD |
| `1D` | `95.20` | 34,390,000.00 USD | 0.00 USD | 34,390,000.00 USD | 99,290.00 USD | 4,070,000.00 USD | 1,600,000.00 USD |
| `7D` | `95.30` | 41,460,000.00 USD | 0.00 USD | 41,460,000.00 USD | 678,330.00 USD | 445,310.00 USD | 838,770.00 USD |
| `1D` | `95.40` | 28,620,000.00 USD | 0.00 USD | 28,620,000.00 USD | 378,280.00 USD | 1,650,000.00 USD | 294,280.00 USD |
| `7D` | `95.50` | 39,490,000.00 USD | 0.00 USD | 39,490,000.00 USD | 1,200,000.00 USD | 3,810,000.00 USD | 2,880,000.00 USD |
| `1D` | `95.60` | 26,300,000.00 USD | 0.00 USD | 26,300,000.00 USD | 2,740,000.00 USD | 1,490,000.00 USD | 3,890,000.00 USD |
| `7D` | `95.70` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 4,060,000.00 USD | 1,480,000.00 USD | 10,200.00 USD |
| `1D` | `95.80` | 18,180,000.00 USD | 0.00 USD | 18,180,000.00 USD | 1,750,000.00 USD | 1,250,000.00 USD | 1,930,000.00 USD |
| `7D` | `95.90` | 26,060,000.00 USD | 0.00 USD | 26,060,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.00` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 1,610,000.00 USD | 1,880,000.00 USD | 1,540,000.00 USD |
| `7D` | `96.10` | 23,930,000.00 USD | 0.00 USD | 23,930,000.00 USD | 3,460,000.00 USD | 2,050,000.00 USD | 4,520,000.00 USD |
| `1D` | `96.20` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 1,350,000.00 USD | 847,400.00 USD | 498,740.00 USD |
| `7D` | `96.30` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 1,030,000.00 USD | 2,320,000.00 USD | 5,630,000.00 USD |
| `1D` | `96.40` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 0.00 USD | 2,050,000.00 USD | 3,480,000.00 USD |
| `7D` | `96.50` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD |
| `1D` | `96.60` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD |
| `1D` | `96.60` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD |
| `7D` | `96.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.80` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 53,180.00 USD | 3,360,000.00 USD | 0.00 USD |
| `1D` | `97.00` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.20` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 286,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.30` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.40` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 690,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.50` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.60` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 5,180,000.00 USD | 0.00 USD | 277,170.00 USD |
| `7D` | `97.70` | 19,680,000.00 USD | 19,680,000.00 USD | 0.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.80` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 5,150,000.00 USD | 39,060.00 USD | 488,470.00 USD |
| `7D` | `97.90` | 45,230,000.00 USD | 45,230,000.00 USD | 0.00 USD | 11,920,000.00 USD | 5,860,000.00 USD | 7,770,000.00 USD |
| `1D` | `98.00` | 35,060,000.00 USD | 35,060,000.00 USD | 0.00 USD | 6,070,000.00 USD | 2,650,000.00 USD | 5,940,000.00 USD |
| `7D` | `98.10` | 80,140,000.00 USD | 80,140,000.00 USD | 0.00 USD | 9,820,000.00 USD | 9,540,000.00 USD | 15,550,000.00 USD |
| `1D` | `98.20` | 46,000,000.00 USD | 46,000,000.00 USD | 0.00 USD | 4,100,000.00 USD | 3,690,000.00 USD | 3,140,000.00 USD |
| `7D` | `98.30` | 96,710,000.00 USD | 96,710,000.00 USD | 0.00 USD | 43,030.00 USD | 6,830,000.00 USD | 9,700,000.00 USD |
| `1D` | `98.40` | 59,510,000.00 USD | 59,510,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,630,000.00 USD | 8,600,000.00 USD |
| `7D` | `98.50` | 102,860,000.00 USD | 102,860,000.00 USD | 0.00 USD | 1,040,000.00 USD | 5,110,000.00 USD | 0.00 USD |
| `1D` | `98.60` | 67,470,000.00 USD | 67,470,000.00 USD | 0.00 USD | 52,360.00 USD | 2,590,000.00 USD | 5,320,000.00 USD |
| `7D` | `98.70` | 102,890,000.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 28,080.00 USD | 0.00 USD |
| `1D` | `98.80` | 74,180,000.00 USD | 74,180,000.00 USD | 0.00 USD | 43,420.00 USD | 2,900,000.00 USD | 3,760,000.00 USD |
| `7D` | `98.90` | 105,430,000.00 USD | 105,430,000.00 USD | 0.00 USD | 57,310.00 USD | 1,040,000.00 USD | 1,440,000.00 USD |
| `1D` | `99.00` | 75,550,000.00 USD | 75,550,000.00 USD | 0.00 USD | 64,620.00 USD | 1,100,000.00 USD | 202,560.00 USD |
| `7D` | `99.10` | 106,570,000.00 USD | 106,570,000.00 USD | 0.00 USD | 179,190.00 USD | 124,230.00 USD | 838,770.00 USD |
| `1D` | `99.20` | 80,410,000.00 USD | 80,410,000.00 USD | 0.00 USD | 115,180.00 USD | 867,660.00 USD | 3,870,000.00 USD |
| `7D` | `99.30` | 111,700,000.00 USD | 111,700,000.00 USD | 0.00 USD | 0.00 USD | 2,230,000.00 USD | 2,890,000.00 USD |
| `1D` | `99.40` | 85,250,000.00 USD | 85,250,000.00 USD | 0.00 USD | 2,860,000.00 USD | 509,170.00 USD | 1,480,000.00 USD |
| `7D` | `99.50` | 115,440,000.00 USD | 115,440,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,480,000.00 USD | 16,920.00 USD |
| `1D` | `99.60` | 99,250,000.00 USD | 99,250,000.00 USD | 0.00 USD | 1,520,000.00 USD | 5,710,000.00 USD | 6,770,000.00 USD |
| `7D` | `99.70` | 117,450,000.00 USD | 117,450,000.00 USD | 0.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD |
| `1D` | `99.80` | 112,150,000.00 USD | 112,150,000.00 USD | 0.00 USD | 2,250,000.00 USD | 3,870,000.00 USD | 6,780,000.00 USD |
| `7D` | `99.90` | 124,600,000.00 USD | 124,600,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD |
| `1D` | `100.00` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,770,000.00 USD | 1,630,000.00 USD |
| `7D` | `100.10` | 127,990,000.00 USD | 127,990,000.00 USD | 0.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD |
| `1D` | `100.20` | 118,490,000.00 USD | 118,490,000.00 USD | 0.00 USD | 16,830.00 USD | 838,950.00 USD | 0.00 USD |
| `7D` | `100.30` | 130,840,000.00 USD | 130,840,000.00 USD | 0.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD |
| `1D` | `100.40` | 122,250,000.00 USD | 122,250,000.00 USD | 0.00 USD | 355,570.00 USD | 767,780.00 USD | 2,640,000.00 USD |
| `7D` | `100.50` | 137,780,000.00 USD | 137,780,000.00 USD | 0.00 USD | 2,500,000.00 USD | 128,740.00 USD | 4,310,000.00 USD |
| `1D` | `100.60` | 131,650,000.00 USD | 131,650,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,190,000.00 USD | 6,220,000.00 USD |
| `7D` | `100.70` | 139,160,000.00 USD | 139,160,000.00 USD | 0.00 USD | 133,340.00 USD | 1,240,000.00 USD | 0.00 USD |
| `1D` | `100.80` | 136,350,000.00 USD | 136,350,000.00 USD | 0.00 USD | 1,520,000.00 USD | 1,690,000.00 USD | 1,490,000.00 USD |
| `7D` | `100.90` | 152,250,000.00 USD | 152,250,000.00 USD | 0.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD |
| `1D` | `101.00` | 147,750,000.00 USD | 147,750,000.00 USD | 0.00 USD | 7,810,000.00 USD | 2,650,000.00 USD | 935,430.00 USD |
| `7D` | `101.10` | 162,020,000.00 USD | 162,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD |
| `1D` | `101.20` | 164,060,000.00 USD | 164,060,000.00 USD | 0.00 USD | 5,230,000.00 USD | 6,870,000.00 USD | 4,220,000.00 USD |
| `7D` | `101.30` | 182,590,000.00 USD | 182,590,000.00 USD | 0.00 USD | 7,310,000.00 USD | 4,280,000.00 USD | 8,980,000.00 USD |
| `1D` | `101.40` | 173,970,000.00 USD | 173,970,000.00 USD | 0.00 USD | 3,450,000.00 USD | 2,420,000.00 USD | 4,030,000.00 USD |
| `7D` | `101.50` | 197,860,000.00 USD | 197,860,000.00 USD | 0.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD |
| `1D` | `101.60` | 194,780,000.00 USD | 194,780,000.00 USD | 0.00 USD | 4,700,000.00 USD | 3,450,000.00 USD | 12,660,000.00 USD |
| `7D` | `101.70` | 207,210,000.00 USD | 207,210,000.00 USD | 0.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD |
| `1D` | `101.80` | 201,070,000.00 USD | 201,070,000.00 USD | 0.00 USD | 483,810.00 USD | 381,190.00 USD | 5,430,000.00 USD |
| `7D` | `101.90` | 215,210,000.00 USD | 215,210,000.00 USD | 0.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD |
| `1D` | `102.00` | 205,460,000.00 USD | 205,460,000.00 USD | 0.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD |
| `7D` | `102.10` | 219,850,000.00 USD | 219,850,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD |
| `1D` | `102.20` | 212,300,000.00 USD | 212,300,000.00 USD | 0.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD |
| `7D` | `102.30` | 225,900,000.00 USD | 225,900,000.00 USD | 0.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD |
| `1D` | `102.40` | 216,880,000.00 USD | 216,880,000.00 USD | 0.00 USD | 1,430,000.00 USD | 579,100.00 USD | 2,570,000.00 USD |
| `7D` | `102.50` | 229,560,000.00 USD | 229,560,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.60` | 219,520,000.00 USD | 219,520,000.00 USD | 0.00 USD | 978,360.00 USD | 625,050.00 USD | 1,040,000.00 USD |
| `7D` | `102.70` | 230,330,000.00 USD | 230,330,000.00 USD | 0.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD |
| `1D` | `102.80` | 223,980,000.00 USD | 223,980,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 1,100,000.00 USD |
| `7D` | `102.90` | 251,620,000.00 USD | 251,620,000.00 USD | 0.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD |
| `1D` | `103.00` | 229,240,000.00 USD | 229,240,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD |
| `7D` | `103.10` | 257,830,000.00 USD | 257,830,000.00 USD | 0.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD |
| `1D` | `103.20` | 232,840,000.00 USD | 232,840,000.00 USD | 0.00 USD | 585,300.00 USD | 1,180,000.00 USD | 1,830,000.00 USD |
| `7D` | `103.30` | 275,400,000.00 USD | 275,400,000.00 USD | 0.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD |
| `1D` | `103.40` | 237,950,000.00 USD | 237,950,000.00 USD | 0.00 USD | 2,140,000.00 USD | 1,620,000.00 USD | 1,350,000.00 USD |
| `7D` | `103.50` | 297,800,000.00 USD | 297,800,000.00 USD | 0.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD |
| `1D` | `103.60` | 248,510,000.00 USD | 248,510,000.00 USD | 0.00 USD | 3,310,000.00 USD | 1,240,000.00 USD | 6,000,000.00 USD |
| `7D` | `103.70` | 310,030,000.00 USD | 310,030,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.80` | 255,310,000.00 USD | 255,310,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,510,000.00 USD | 2,010,000.00 USD |
| `7D` | `103.90` | 328,060,000.00 USD | 328,060,000.00 USD | 0.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.00` | 264,860,000.00 USD | 264,860,000.00 USD | 0.00 USD | 3,550,000.00 USD | 2,790,000.00 USD | 3,220,000.00 USD |
| `7D` | `104.10` | 356,790,000.00 USD | 356,790,000.00 USD | 0.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD |
| `1D` | `104.20` | 270,590,000.00 USD | 270,590,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,830,000.00 USD | 1,830,000.00 USD |
| `7D` | `104.30` | 378,170,000.00 USD | 378,170,000.00 USD | 0.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD |
| `1D` | `104.40` | 276,580,000.00 USD | 276,580,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,790,000.00 USD | 1,830,000.00 USD |
| `7D` | `104.50` | 390,170,000.00 USD | 390,170,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD |
| `1D` | `104.60` | 281,500,000.00 USD | 281,500,000.00 USD | 0.00 USD | 1,430,000.00 USD | 963,940.00 USD | 2,530,000.00 USD |
| `7D` | `104.70` | 410,170,000.00 USD | 410,170,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD |
| `1D` | `104.80` | 285,300,000.00 USD | 285,300,000.00 USD | 0.00 USD | 948,860.00 USD | 905,680.00 USD | 1,950,000.00 USD |
| `7D` | `104.90` | 430,770,000.00 USD | 430,770,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.00` | 286,490,000.00 USD | 286,490,000.00 USD | 0.00 USD | 487,580.00 USD | 351,350.00 USD | 350,200.00 USD |
| `7D` | `105.10` | 443,980,000.00 USD | 443,980,000.00 USD | 0.00 USD | 5,580,000.00 USD | 4,800,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.20` | 287,750,000.00 USD | 287,750,000.00 USD | 0.00 USD | 237,100.00 USD | 4,110.00 USD | 1,020,000.00 USD |
| `7D` | `105.30` | 448,980,000.00 USD | 448,980,000.00 USD | 0.00 USD | 2,740,000.00 USD | 1,820,000.00 USD | 428,740.00 USD |
| `1D` | `105.40` | 287,920,000.00 USD | 287,920,000.00 USD | 0.00 USD | 84,970.00 USD | 88,270.00 USD | 769.33 USD |
| `7D` | `105.50` | 468,490,000.00 USD | 468,490,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD |
| `1D` | `105.60` | 288,500,000.00 USD | 288,500,000.00 USD | 0.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD |
| `7D` | `105.70` | 482,660,000.00 USD | 482,660,000.00 USD | 0.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD |
| `1D` | `105.80` | 289,240,000.00 USD | 289,240,000.00 USD | 0.00 USD | 132,310.00 USD | 591,910.00 USD | 22,350.00 USD |
| `7D` | `105.90` | 492,550,000.00 USD | 492,550,000.00 USD | 0.00 USD | 3,680,000.00 USD | 1,870,000.00 USD | 4,340,000.00 USD |
| `1D` | `106.00` | 290,370,000.00 USD | 290,370,000.00 USD | 0.00 USD | 377,210.00 USD | 525,540.00 USD | 226,180.00 USD |
| `7D` | `106.10` | 504,690,000.00 USD | 504,690,000.00 USD | 0.00 USD | 6,090,000.00 USD | 3,080,000.00 USD | 2,960,000.00 USD |
| `1D` | `106.20` | 291,700,000.00 USD | 291,700,000.00 USD | 0.00 USD | 614,770.00 USD | 344,210.00 USD | 367,070.00 USD |
| `7D` | `106.30` | 514,650,000.00 USD | 514,650,000.00 USD | 0.00 USD | 4,750,000.00 USD | 2,990,000.00 USD | 2,230,000.00 USD |
| `1D` | `106.40` | 292,380,000.00 USD | 292,380,000.00 USD | 0.00 USD | 233,950.00 USD | 319,460.00 USD | 125,880.00 USD |
| `7D` | `106.50` | 519,890,000.00 USD | 519,890,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,650,000.00 USD | 1,890,000.00 USD |
| `1D` | `106.60` | 294,140,000.00 USD | 294,140,000.00 USD | 0.00 USD | 399,220.00 USD | 321,480.00 USD | 1,040,000.00 USD |
| `7D` | `106.70` | 529,510,000.00 USD | 529,510,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,870,000.00 USD | 4,470,000.00 USD |
| `1D` | `106.80` | 295,290,000.00 USD | 295,290,000.00 USD | 0.00 USD | 319,360.00 USD | 179,630.00 USD | 649,600.00 USD |
| `7D` | `106.90` | 535,340,000.00 USD | 535,340,000.00 USD | 0.00 USD | 1,220,000.00 USD | 1,150,000.00 USD | 3,470,000.00 USD |
| `1D` | `107.00` | 295,650,000.00 USD | 295,650,000.00 USD | 0.00 USD | 98,730.00 USD | 169,460.00 USD | 95,590.00 USD |
| `7D` | `107.10` | 539,450,000.00 USD | 539,450,000.00 USD | 0.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD |
| `1D` | `107.20` | 296,140,000.00 USD | 296,140,000.00 USD | 0.00 USD | 0.00 USD | 49,040.00 USD | 436,040.00 USD |
| `7D` | `107.30` | 539,900,000.00 USD | 539,900,000.00 USD | 0.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD |
| `1D` | `107.40` | 296,750,000.00 USD | 296,750,000.00 USD | 0.00 USD | 22,290.00 USD | 63,590.00 USD | 523,690.00 USD |
| `7D` | `107.50` | 540,880,000.00 USD | 540,880,000.00 USD | 0.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD |
| `1D` | `107.60` | 297,230,000.00 USD | 297,230,000.00 USD | 0.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD |
| `7D` | `107.70` | 541,850,000.00 USD | 541,850,000.00 USD | 0.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD |
| `7D` | `107.90` | 542,020,000.00 USD | 542,020,000.00 USD | 0.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.10` | 542,630,000.00 USD | 542,630,000.00 USD | 0.00 USD | 249,450.00 USD | 347,250.00 USD | 5,590.00 USD |
| `7D` | `108.30` | 544,780,000.00 USD | 544,780,000.00 USD | 0.00 USD | 964,640.00 USD | 578,980.00 USD | 612,150.00 USD |
| `7D` | `108.50` | 545,820,000.00 USD | 545,820,000.00 USD | 0.00 USD | 867,380.00 USD | 157,660.00 USD | 9,530.00 USD |
| `7D` | `108.70` | 548,060,000.00 USD | 548,060,000.00 USD | 0.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD |
| `7D` | `108.90` | 550,100,000.00 USD | 550,100,000.00 USD | 0.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD |
| `7D` | `109.10` | 551,190,000.00 USD | 551,190,000.00 USD | 0.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD |
| `7D` | `109.30` | 552,350,000.00 USD | 552,350,000.00 USD | 0.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD |
| `7D` | `109.50` | 552,590,000.00 USD | 552,590,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `7D` | `109.70` | 553,770,000.00 USD | 553,770,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `7D` | `109.90` | 555,570,000.00 USD | 555,570,000.00 USD | 0.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `7D` | `110.10` | 557,940,000.00 USD | 557,940,000.00 USD | 0.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `7D` | `110.30` | 560,020,000.00 USD | 560,020,000.00 USD | 0.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `7D` | `110.50` | 560,500,000.00 USD | 560,500,000.00 USD | 0.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD |
| `7D` | `110.70` | 562,710,000.00 USD | 562,710,000.00 USD | 0.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD |
| `7D` | `110.90` | 565,150,000.00 USD | 565,150,000.00 USD | 0.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `7D` | `111.10` | 567,540,000.00 USD | 567,540,000.00 USD | 0.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `7D` | `111.30` | 569,440,000.00 USD | 569,440,000.00 USD | 0.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `7D` | `111.50` | 571,950,000.00 USD | 571,950,000.00 USD | 0.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `7D` | `111.70` | 573,090,000.00 USD | 573,090,000.00 USD | 0.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD |
| `7D` | `111.90` | 574,860,000.00 USD | 574,860,000.00 USD | 0.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD |
| `7D` | `112.10` | 576,490,000.00 USD | 576,490,000.00 USD | 0.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `7D` | `112.30` | 578,900,000.00 USD | 578,900,000.00 USD | 0.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `7D` | `112.50` | 580,210,000.00 USD | 580,210,000.00 USD | 0.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `7D` | `112.70` | 580,740,000.00 USD | 580,740,000.00 USD | 0.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD |
| `7D` | `112.90` | 582,230,000.00 USD | 582,230,000.00 USD | 0.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD |
| `7D` | `113.10` | 583,620,000.00 USD | 583,620,000.00 USD | 0.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `7D` | `113.30` | 583,890,000.00 USD | 583,890,000.00 USD | 0.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `7D` | `113.50` | 583,950,000.00 USD | 583,950,000.00 USD | 0.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `7D` | `113.70` | 584,350,000.00 USD | 584,350,000.00 USD | 0.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.90` | 584,400,000.00 USD | 584,400,000.00 USD | 0.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `114.10` | 584,460,000.00 USD | 584,460,000.00 USD | 0.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `114.30` | 584,690,000.00 USD | 584,690,000.00 USD | 0.00 USD | 93,960.00 USD | 135,190.00 USD | 1,290.00 USD |
| `7D` | `114.40` | 585,020,000.00 USD | 585,020,000.00 USD | 0.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.97B` | Total OI Tokens: `61,665,879.4 SOL`
  * 1h OI Change: `+0.07%` | 4h OI Change: `-4.04%` | 24h OI Change: `-6.21%`
  * Exchange Breakdown: Binance=`989.76M` | Bybit=`618.31M` | OKX=`362.35M` | Hyperliquid=`547.22M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `51.60K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0065%` | **USDT OKX** | `0.0061%` |
| **USDT Bybit** | `-0.0029%` | **USDT KuCoin** | `0.0028%` |
| **USDT MEXC** | `0.0061%` | **USDT BingX** | `0.0060%` |
| **USDT Gate** | `0.0007%` | **USDT Bitget** | `0.0051%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `52.30%` | `47.70%` | `1.10` | 126,920,000.00 USD |
| `15M` | `Binance` | `54.46%` | `45.54%` | `1.20` | 51,330,000.00 USD |
| `15M` | `OKX` | `44.51%` | `55.49%` | `0.80` | 19,170,000.00 USD |
| `15M` | `Bybit` | `50.55%` | `49.45%` | `1.02` | 8,610,000.00 USD |
| `15M` | `KuCoin` | `46.54%` | `53.46%` | `0.87` | 685,320.00 USD |
| `15M` | `Gate` | `56%` | `44%` | `1.27` | 6,190,000.00 USD |
| `15M` | `Bitget` | `36.74%` | `63.26%` | `0.58` | 4,300,000.00 USD |
| `15M` | `BingX` | `67.19%` | `32.81%` | `2.05` | 7,580,000.00 USD |
| `15M` | `MEXC` | `57.46%` | `42.54%` | `1.35` | 5,660,000.00 USD |
| `15M` | `Bitunix` | `49.73%` | `50.27%` | `0.99` | 5,330,000.00 USD |
| `15M` | `Hyperliquid` | `52.53%` | `47.47%` | `1.11` | 4,020,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.35%` | `44.65%` | `1.24` | 4,980,000.00 USD |
| `15M` | `Crypto.com` | `49.35%` | `50.65%` | `0.97` | 216,970.00 USD |
| `15M` | `WhiteBIT` | `9.47%` | `90.53%` | `0.10` | 1,030,000.00 USD |
| `15M` | `HTX` | `47.91%` | `52.09%` | `0.92` | 130,140.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `53.01%` | `46.99%` | `1.13` | 5,280,000.00 USD |
| `15M` | `Aster` | `50.06%` | `49.94%` | `1.00` | 1,280,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54%` | `46%` | `1.17` | 1,120,000.00 USD |
| `15M` | `Whale Positions` | `54.46%` | `45.54%` | `1.20` | 51,330,000.00 USD |
| `15M` | `Global Accounts` | `52.30%` | `47.70%` | `1.10` | 126,920,000.00 USD |
| `1H` | `SOL` | `51.30%` | `48.70%` | `1.05` | 459,410,000.00 USD |
| `1H` | `Binance` | `54.03%` | `45.97%` | `1.18` | 192,780,000.00 USD |
| `1H` | `OKX` | `44.89%` | `55.11%` | `0.81` | 68,050,000.00 USD |
| `1H` | `Bybit` | `47.33%` | `52.67%` | `0.90` | 36,300,000.00 USD |
| `1H` | `KuCoin` | `47.46%` | `52.54%` | `0.90` | 3,200,000.00 USD |
| `1H` | `Gate` | `49.24%` | `50.76%` | `0.97` | 23,780,000.00 USD |
| `1H` | `Bitget` | `41.81%` | `58.19%` | `0.72` | 17,100,000.00 USD |
| `1H` | `BingX` | `55.36%` | `44.64%` | `1.24` | 18,690,000.00 USD |
| `1H` | `MEXC` | `49.43%` | `50.57%` | `0.98` | 19,990,000.00 USD |
| `1H` | `Bitunix` | `48.86%` | `51.14%` | `0.96` | 16,400,000.00 USD |
| `1H` | `Hyperliquid` | `65.65%` | `34.35%` | `1.91` | 25,910,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.19%` | `43.81%` | `1.28` | 11,070,000.00 USD |
| `1H` | `Crypto.com` | `49.44%` | `50.56%` | `0.98` | 835,320.00 USD |
| `1H` | `WhiteBIT` | `13.07%` | `86.93%` | `0.15` | 4,910,000.00 USD |
| `1H` | `HTX` | `49.38%` | `50.62%` | `0.98` | 347,690.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.26%` | `54.74%` | `0.83` | 8,180,000.00 USD |
| `1H` | `Aster` | `62.38%` | `37.62%` | `1.66` | 7,840,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.24%` | `47.76%` | `1.09` | 4,020,000.00 USD |
| `1H` | `Whale Positions` | `54.03%` | `45.97%` | `1.18` | 192,780,000.00 USD |
| `1H` | `Global Accounts` | `51.30%` | `48.70%` | `1.05` | 459,410,000.00 USD |
| `4H` | `SOL` | `45.55%` | `54.45%` | `0.84` | 4,010,000,000.00 USD |
| `4H` | `Binance` | `45.04%` | `54.96%` | `0.82` | 1,610,000,000.00 USD |
| `4H` | `OKX` | `46.2%` | `53.8%` | `0.86` | 636,810,000.00 USD |
| `4H` | `Bybit` | `42.03%` | `57.97%` | `0.73` | 429,570,000.00 USD |
| `4H` | `KuCoin` | `47.62%` | `52.38%` | `0.91` | 30,350,000.00 USD |
| `4H` | `Gate` | `48.02%` | `51.98%` | `0.92` | 168,620,000.00 USD |
| `4H` | `Bitget` | `42.8%` | `57.2%` | `0.75` | 145,670,000.00 USD |
| `4H` | `BingX` | `47.71%` | `52.29%` | `0.91` | 132,420,000.00 USD |
| `4H` | `MEXC` | `50.72%` | `49.28%` | `1.03` | 232,990,000.00 USD |
| `4H` | `Bitunix` | `47.07%` | `52.93%` | `0.89` | 182,260,000.00 USD |
| `4H` | `Hyperliquid` | `41.69%` | `58.31%` | `0.71` | 203,390,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.86%` | `47.14%` | `1.12` | 52,650,000.00 USD |
| `4H` | `Crypto.com` | `46.09%` | `53.91%` | `0.85` | 11,290,000.00 USD |
| `4H` | `WhiteBIT` | `41.04%` | `58.96%` | `0.70` | 17,920,000.00 USD |
| `4H` | `HTX` | `44.79%` | `55.21%` | `0.81` | 4,970,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.3%` | `51.7%` | `0.93` | 42,240,000.00 USD |
| `4H` | `Aster` | `53.9%` | `46.1%` | `1.17` | 50,970,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.05%` | `53.95%` | `0.85` | 56,240,000.00 USD |
| `4H` | `Whale Positions` | `45.04%` | `54.96%` | `0.82` | 1,610,000,000.00 USD |
| `4H` | `Global Accounts` | `45.55%` | `54.45%` | `0.84` | 4,010,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `96.70` | `96.08` | `96.70` | `97.16` | `94.82` | 215,726,671.39 USD | 100,520,655.67 USD | 115,206,015.72 USD | -14,685,360.05 USD | `-6.81%` | `2B / 14S` |
| `0:00 UTC` | `95.81` | `96.26` | `95.81` | `97.12` | `95.34` | 129,728,839.74 USD | 65,325,713.62 USD | 64,403,126.12 USD | 922,587.50 USD | `+0.71%` | `8B / 11S` |
| `5:00 UTC` | `97.38` | `97.38` | `97.38` | `97.88` | `96.80` | 101,047,979.53 USD | 36,621,270.69 USD | 64,426,708.83 USD | -27,805,438.14 USD | `-27.52%` | `3B / 13S` |
| `0:00 UTC` | `97.82` | `97.78` | `97.82` | `98.05` | `97.22` | 66,557,018.60 USD | 21,423,499.46 USD | 45,133,519.15 USD | -23,710,019.69 USD | `-35.62%` | `8B / 8S` |
| `5:00 UTC` | `97.38` | `97.35` | `97.38` | `97.77` | `97.00` | 50,034,040.48 USD | 24,592,177.20 USD | 25,441,863.28 USD | -849,686.07 USD | `-1.70%` | `18B / 3S` |
| `0:00 UTC` | `97.18` | `97.24` | `97.18` | `97.81` | `96.45` | 125,028,825.31 USD | 50,577,751.56 USD | 74,451,073.75 USD | -23,873,322.19 USD | `-19.09%` | `23B / 8S` |
| `5:00 UTC` | `97.41` | `97.23` | `97.41` | `97.50` | `96.77` | 61,370,185.01 USD | 39,379,012.75 USD | 21,991,172.26 USD | 17,387,840.49 USD | `+28.33%` | `8B / 1S` |
| `0:00 UTC` | `97.75` | `97.54` | `97.75` | `97.82` | `97.10` | 42,753,332.88 USD | 17,911,041.19 USD | 24,842,291.69 USD | -6,931,250.50 USD | `-16.21%` | `13B / 2S` |
| `5:00 UTC` | `96.94` | `97.02` | `96.94` | `97.41` | `96.78` | 26,257,148.78 USD | 13,138,265.90 USD | 13,118,882.88 USD | 19,383.03 USD | `+0.07%` | `4B / 10S` |
| `0:00 UTC` | `96.43` | `96.57` | `96.43` | `97.09` | `96.25` | 36,256,451.41 USD | 19,295,719.54 USD | 16,960,731.87 USD | 2,334,987.67 USD | `+6.44%` | `11B / 7S` |

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
| `5m` | -926,080.00 USD | 2,420,000.00 USD | **`ACCUMULATION`** |
| `15m` | -2,510,000.00 USD | 2,640,000.00 USD | **`ACCUMULATION`** |
| `30m` | -4,250,000.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -14,340,000.00 USD | 5,210,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -25,660,000.00 USD | -116,840,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -58,850,000.00 USD | -278,790,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -61,170,000.00 USD | -301,440,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -58,410,000.00 USD | -306,840,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -46,750,000.00 USD | -336,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -39,580,000.00 USD | -377,160,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 30,730,000.00 USD | -576,530,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 1,750,000.00 USD | -2,130,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-926.08K` | 15m=`-2.51M` | 1h=`-14.34M` | 24h=`-39.58M`
* Futures Capital Netflows: 5m=`+2.42M` | 15m=`+2.64M` | 1h=`+5.21M` | 24h=`-377.16M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `96.47` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `94.99` (Risk Distance: `1.48` pts)
  * +2.5R Take Profit: `100.17`
  * Mathematical Lot Sizing: **`6.75 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `97.46` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `98.94` (Risk Distance: `1.48` pts)
  * +2.5R Take Profit: `93.76`
  * Mathematical Lot Sizing: **`6.75 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.18`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
