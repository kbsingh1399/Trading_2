# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 17:10:07 IST` (`2026-10-30 11:40:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.61` | **Live Ask Quote**: `96.84` | **Mid Price**: `96.72`
- **Spread Points**: `23.00` | **Spread BPS**: `23.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `95.80` | VWAP Z-Score: `+0.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5957` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.03` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `100.49` | Lower -3.00σ Band: `91.10`
  * Upper +2.51σ Band: `99.72` | Lower -2.51σ Band: `91.87`
  * Upper +2.01σ Band: `98.94` | Lower -2.01σ Band: `92.65`
  * Upper +2.00σ Band: `98.93` | Lower -2.00σ Band: `92.67`
  * Upper +1.28σ Band: `97.80` | Lower -1.28σ Band: `93.80`
  * Upper +1.00σ Band: `97.36` | Lower -1.00σ Band: `94.23`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`96.74` | EMA-20=`96.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.00` (Slope: `+0.0000`) | EMA-100=`97.77`
  * Institutional Anchors: EMA-144=`98.32` | EMA-200=`98.88` (Slope: `-0.2777`) | EMA-233=`99.10`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `98.09` (Distance: `-1.43%`)
  * Point of Control (POC) = `96.89` (Distance: `-0.21%`)
  * Value Area Low (VAL) = `95.26` (Distance: `+1.49%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`102.18` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`95.96`
  * New York Session (13:00-21:00 UTC): High=`97.11` | Low=`95.96`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.34` - `97.11`
  * Optimal Trade Entry (OTE 0.705): `96.92`
  * Structural Invalidation Anchor (0.786): `97.50`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `97.30` | `97.38` | `97.01` | `97.07` | `51,723` | 5,027,184.94 USD | -711,193.91 USD | `-14.15%` | -214,839,007.40 USD | `-0.91` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `97.08` | `97.12` | `96.90` | `96.96` | `29,283` | 2,840,806.14 USD | -8,680.46 USD | `-0.31%` | -214,847,687.87 USD | `-0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `96.96` | `97.01` | `96.84` | `96.85` | `20,146` | 1,952,912.65 USD | 246,676.82 USD | `+12.63%` | -214,601,011.05 USD | `-0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `96.68` | `97.23` | `96.62` | `97.07` | `228,268` | 22,145,911.65 USD | 1,091,769.84 USD | `+4.93%` | -215,814,697.50 USD | `+0.97` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `97.07` | `97.35` | `96.74` | `97.31` | `151,568` | 14,711,636.00 USD | 1,686,884.02 USD | `+11.47%` | -214,127,813.49 USD | `+1.25` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `97.30` | `97.38` | `96.84` | `96.84` | `100,750` | 9,782,014.85 USD | -450,451.64 USD | `-4.60%` | -214,578,265.13 USD | `+0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `97.34` | `97.44` | `96.68` | `96.83` | `564,041` | 54,709,052.00 USD | -2,626,000.84 USD | `-4.80%` | -213,658,118.44 USD | `+0.40` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `96.84` | `97.35` | `96.27` | `97.31` | `737,625` | 71,383,557.65 USD | 4,115,844.55 USD | `+5.77%` | -209,542,273.89 USD | `+0.78` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `97.30` | `97.38` | `96.84` | `96.84` | `101,115` | 9,817,290.62 USD | -469,603.83 USD | `-4.78%` | -210,011,877.72 USD | `+0.54` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.27` | `96.84` | `1,966,724` | 190,730,606.75 USD | -217,474.31 USD | `-0.11%` | -209,992,725.53 USD | `+0.88` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -33,800,710.11 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -149,674,135.76 USD | `-1.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.27` | `96.84` | `1,966,724` | 190,730,606.75 USD | -217,474.31 USD | `-0.11%` | -209,992,725.53 USD | `+0.88` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`96.72`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `96.81` | `151.0500` | 14,623.91 USD | 178,837.39 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `96.81` | `361.7200` | 35,019.56 USD | 213,856.95 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `96.81` | `41.3100` | 3,999.35 USD | 217,856.29 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `96.81` | `41.3100` | 3,999.30 USD | 221,855.60 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `96.81` | `1937.8200` | 187,602.29 USD | 409,457.89 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `96.82` | `77.9100` | 7,543.40 USD | 120,753.66 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.82` | `397.2500` | 38,462.14 USD | 159,215.80 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `96.82` | `7.9100` | 765.85 USD | 159,981.65 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `96.82` | `0.5100` | 49.38 USD | 160,031.03 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.82` | `1.8900` | 182.98 USD | 160,214.01 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `96.82` | `41.3100` | 3,999.47 USD | 164,213.48 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `96.83` | `6.5600` | 635.24 USD | 39,228.51 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `205.7400` | 19,922.63 USD | 59,151.14 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `77.1100` | 7,466.72 USD | 66,617.86 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `226.7900` | 21,960.30 USD | 88,578.16 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `145.0200` | 14,042.29 USD | 102,620.45 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `62.9000` | 6,090.36 USD | 108,710.80 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `96.83` | `46.4700` | 4,499.46 USD | 113,210.26 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `96.84` | `54.4100` | 5,269.34 USD | 98,654.24 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `96.84` | `37.6000` | 3,641.30 USD | 93,384.90 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `96.84` | `80.3800` | 7,784.16 USD | 89,743.60 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `96.84` | `846.3300` | 81,959.44 USD | 81,959.44 USD | `6 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `96.84` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 96.84` | `0.00%` | `-` |
| `BID` | `96.84` | `214.2600` | 20,748.94 USD | 20,748.94 USD | `4 orders` | `-0.00%` | `-` |
| `BID` | `96.84` | `184.2700` | 17,844.34 USD | 38,593.28 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `96.85` | `51.2100` | 4,959.84 USD | 305,099.00 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.85` | `99.6100` | 9,647.33 USD | 300,139.15 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `96.85` | `67.7600` | 6,562.49 USD | 290,491.83 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.85` | `10.0000` | 968.48 USD | 283,929.34 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `96.85` | `1903.0700` | 184,306.62 USD | 282,960.86 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `96.86` | `271.7800` | 26,325.97 USD | 444,839.09 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `96.86` | `82.7100` | 8,011.54 USD | 418,513.12 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.86` | `772.5300` | 74,828.80 USD | 410,501.58 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `96.86` | `103.6200` | 10,036.74 USD | 335,672.78 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `96.86` | `96.4500` | 9,342.15 USD | 325,636.04 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `96.86` | `67.7600` | 6,563.17 USD | 316,293.89 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.86` | `38.8200` | 3,760.03 USD | 309,730.73 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.86` | `9.0000` | 871.70 USD | 305,970.70 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `96.87` | `472.0400` | 45,725.57 USD | 729,182.61 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `96.87` | `185.3300` | 17,952.36 USD | 683,457.04 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `96.87` | `2278.0500` | 220,665.59 USD | 665,504.68 USD | `3 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `11` | `0x5b5d...c060` | `SHORT` | 67,396,958.75 USD | `696,120.13` | `94.33` | `96.82` | `309.57` | -1,728,692.53 USD | `-2.56%` | `7X Cross` |
| `19` | `0x9c6a...a4ed` | `LONG` | 53,266,641.29 USD | `550,087.69` | `80.86` | `96.82` | `68.18` | 8,787,654.90 USD | `+16.50%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 25,105,735.70 USD | `259,338.02` | `91.42` | `96.82` | `507.39` | -1,396,921.66 USD | `-5.56%` | `5X Cross` |
| `78` | `0x3dc9...54b0` | `SHORT` | 21,302,134.40 USD | `220,000.19` | `105.90` | `96.82` | `173.81` | 1,996,972.88 USD | `+9.37%` | `20X Cross` |
| `113` | `0x9c89...600e` | `LONG` | 18,344,348.50 USD | `189,472.50` | `115.21` | `96.82` | `34.99` | -3,484,666.76 USD | `-19.00%` | `20X Cross` |
| `118` | `0x4a20...3c26` | `LONG` | 17,431,020.00 USD | `180,000.00` | `106.43` | `96.82` | `69.76` | -1,727,258.71 USD | `-9.91%` | `20X Cross` |
| `147` | `0xecb6...2b00` | `SHORT` | 13,995,929.55 USD | `144,533.79` | `100.85` | `96.82` | `332.38` | 580,482.36 USD | `+4.15%` | `20X Cross` |
| `229` | `0xc63a...a3cd` | `LONG` | 9,683,820.00 USD | `100,000.00` | `112.22` | `96.82` | `0.000000` | -1,538,288.97 USD | `-15.89%` | `20X Cross` |
| `230` | `0xb581...6f4f` | `LONG` | 9,680,700.00 USD | `100,000.00` | `112.81` | `96.82` | `0.000000` | -1,600,009.14 USD | `-16.53%` | `3X Cross` |
| `297` | `0x645b...87b8` | `SHORT` | 8,026,012.45 USD | `82,879.96` | `103.90` | `96.82` | `355.06` | 585,457.78 USD | `+7.29%` | `20X Cross` |
| `303` | `0xdb3a...cf3b` | `LONG` | 7,925,544.15 USD | `81,851.78` | `106.04` | `96.82` | `46.21` | -754,202.70 USD | `-9.52%` | `4X Cross` |
| `319` | `0xe927...98ef` | `LONG` | 7,552,568.40 USD | `78,000.00` | `96.34` | `96.82` | `38.45` | 38,426.92 USD | `+0.51%` | `3X Cross` |
| `327` | `0xca49...53c8` | `SHORT` | 7,160,550.60 USD | `73,943.45` | `110.70` | `96.82` | `301.15` | 1,025,071.66 USD | `+14.32%` | `20X Cross` |
| `332` | `0x8ae4...3d60` | `LONG` | 6,988,328.08 USD | `72,180.05` | `111.72` | `96.82` | `11.55` | -1,075,832.16 USD | `-15.39%` | `10X Cross` |
| `336` | `0xa0b7...6165` | `SHORT` | 6,879,444.32 USD | `71,044.42` | `107.87` | `96.82` | `190.91` | 784,022.88 USD | `+11.40%` | `2X Cross` |
| `354` | `0xf517...c032` | `SHORT` | 6,563,333.95 USD | `67,778.53` | `84.64` | `96.82` | `223.25` | -826,302.79 USD | `-12.59%` | `20X Cross` |
| `417` | `0x7fda...17d1` | `SHORT` | 5,379,916.32 USD | `55,557.56` | `100.53` | `96.82` | `677.66` | 205,493.51 USD | `+3.82%` | `20X Cross` |
| `474` | `0x7e23...5a5a` | `LONG` | 4,702,603.47 USD | `48,564.56` | `105.17` | `96.82` | `57.00` | -404,965.69 USD | `-8.61%` | `5X Isolated` |
| `569` | `0xf899...88db` | `SHORT` | 3,942,116.04 USD | `40,716.81` | `88.40` | `96.82` | `109.11` | -342,843.17 USD | `-8.70%` | `20X Cross` |
| `587` | `0x2e2b...2fab` | `LONG` | 3,873,080.00 USD | `40,000.00` | `119.55` | `96.82` | `58.03` | -908,955.64 USD | `-23.47%` | `10X Cross` |
| `621` | `0x9c16...4a6f` | `SHORT` | 3,660,109.20 USD | `37,796.13` | `90.79` | `96.82` | `118.42` | -228,758.47 USD | `-6.25%` | `20X Cross` |
| `646` | `0x9946...0852` | `SHORT` | 3,496,063.83 USD | `36,099.58` | `110.82` | `96.82` | `141.04` | 504,522.56 USD | `+14.43%` | `20X Cross` |
| `648` | `0x27b8...12fc` | `LONG` | 3,493,748.21 USD | `36,085.73` | `110.86` | `96.82` | `23.99` | -506,597.05 USD | `-14.50%` | `10X Cross` |
| `674` | `0xa61c...66b9` | `LONG` | 3,356,568.36 USD | `34,662.76` | `102.73` | `96.82` | `0.000000` | -204,503.10 USD | `-6.09%` | `5X Cross` |
| `687` | `0x3440...32c5` | `SHORT` | 3,267,940.59 USD | `33,744.03` | `95.02` | `96.82` | `169.32` | -61,540.64 USD | `-1.88%` | `20X Cross` |
| `708` | `0x7a5a...0394` | `SHORT` | 3,179,758.37 USD | `32,833.48` | `99.28` | `96.82` | `125.06` | 79,794.67 USD | `+2.51%` | `10X Cross` |
| `739` | `0x96a7...79df` | `LONG` | 3,098,492.80 USD | `32,000.00` | `74.39` | `96.82` | `0.000000` | 718,086.95 USD | `+23.18%` | `20X Cross` |
| `777` | `0xbe19...8bd1` | `SHORT` | 2,949,093.92 USD | `30,451.69` | `97.62` | `96.82` | `757.03` | 23,452.71 USD | `+0.80%` | `3X Cross` |
| `780` | `0x482b...cae4` | `SHORT` | 2,935,237.54 USD | `30,310.49` | `88.03` | `96.82` | `154.76` | -266,989.25 USD | `-9.10%` | `20X Cross` |
| `796` | `0x610b...b613` | `LONG` | 2,869,325.61 USD | `29,634.14` | `101.23` | `96.82` | `70.40` | -130,673.74 USD | `-4.55%` | `3X Isolated` |
| `807` | `0x45d2...4029` | `SHORT` | 2,829,635.58 USD | `29,220.00` | `93.28` | `96.82` | `1541.88` | -103,859.60 USD | `-3.67%` | `20X Cross` |
| `850` | `0x458d...ab3b` | `LONG` | 2,651,634.95 USD | `27,385.03` | `117.17` | `96.82` | `81.08` | -557,027.57 USD | `-21.01%` | `3X Isolated` |
| `887` | `0x023a...2355` | `SHORT` | 2,511,890.22 USD | `25,939.90` | `101.15` | `96.82` | `296.06` | 111,847.43 USD | `+4.45%` | `20X Cross` |
| `903` | `0xfc27...9d9d` | `SHORT` | 2,461,172.87 USD | `25,415.10` | `100.27` | `96.82` | `841.44` | 87,140.06 USD | `+3.54%` | `20X Cross` |
| `915` | `0x051c...693c` | `LONG` | 2,434,224.36 USD | `25,139.70` | `89.76` | `96.82` | `45.87` | 177,663.03 USD | `+7.30%` | `20X Cross` |
| `957` | `0x638f...f5f0` | `LONG` | 2,324,116.80 USD | `24,000.00` | `136.71` | `96.82` | `51.27` | -956,851.74 USD | `-41.17%` | `20X Cross` |
| `998` | `0x7277...0b98` | `SHORT` | 2,205,095.69 USD | `22,770.74` | `99.32` | `96.82` | `157.72` | 56,508.07 USD | `+2.56%` | `20X Cross` |
| `1003` | `0x7178...0854` | `LONG` | 2,182,782.79 USD | `22,545.24` | `110.94` | `96.82` | `39.38` | -318,361.68 USD | `-14.59%` | `10X Cross` |
| `1035` | `0x739c...cfb2` | `LONG` | 2,081,737.50 USD | `21,500.00` | `91.95` | `96.82` | `77.29` | 104,805.35 USD | `+5.03%` | `20X Cross` |
| `1104` | `0x7737...bf66` | `SHORT` | 1,973,584.69 USD | `20,384.06` | `102.94` | `96.82` | `978.99` | 124,757.20 USD | `+6.32%` | `10X Cross` |
| `1134` | `0xea00...a918` | `LONG` | 1,938,753.02 USD | `20,022.69` | `66.09` | `96.82` | `0.000000` | 615,444.42 USD | `+31.74%` | `20X Cross` |
| `1136` | `0x251f...6e5d` | `LONG` | 1,936,700.00 USD | `20,000.00` | `101.15` | `96.82` | `69.31` | -86,397.77 USD | `-4.46%` | `20X Cross` |
| `1138` | `0x3fc5...c0c1` | `SHORT` | 1,936,340.00 USD | `20,000.00` | `98.28` | `96.82` | `183.76` | 29,219.84 USD | `+1.51%` | `20X Cross` |
| `1140` | `0xbfc7...80b4` | `SHORT` | 1,936,140.00 USD | `20,000.00` | `85.98` | `96.82` | `173.74` | -216,605.50 USD | `-11.19%` | `20X Cross` |
| `1168` | `0x7160...d47c` | `LONG` | 1,881,901.07 USD | `19,434.10` | `105.03` | `96.82` | `76.00` | -159,320.22 USD | `-8.47%` | `20X Cross` |
| `1201` | `0xe097...d0fe` | `LONG` | 1,839,514.24 USD | `18,995.75` | `109.71` | `96.82` | `0.000000` | -244,482.65 USD | `-13.29%` | `20X Cross` |
| `1202` | `0x936c...bb0f` | `SHORT` | 1,838,791.10 USD | `18,988.91` | `105.57` | `96.82` | `525.45` | 165,896.59 USD | `+9.02%` | `20X Cross` |
| `1270` | `0xdf95...7d72` | `SHORT` | 1,723,984.04 USD | `17,802.58` | `104.53` | `96.82` | `2277.08` | 136,972.81 USD | `+7.95%` | `20X Cross` |
| `1274` | `0xe98b...8cd5` | `SHORT` | 1,706,477.31 USD | `17,622.89` | `187.95` | `96.82` | `261.99` | 1,605,743.42 USD | `+94.10%` | `20X Cross` |
| `1315` | `0xee2b...d67e` | `LONG` | 1,642,630.50 USD | `16,963.19` | `119.86` | `96.82` | `34.96` | -390,641.14 USD | `-23.78%` | `4X Cross` |
| `1330` | `0x123d...3bff` | `LONG` | 1,630,077.92 USD | `16,835.30` | `89.54` | `96.82` | `0.000000` | 122,636.67 USD | `+7.52%` | `10X Cross` |
| `1428` | `0x73d7...8be1` | `LONG` | 1,517,352.91 USD | `15,668.95` | `106.60` | `96.82` | `47.81` | -152,988.05 USD | `-10.08%` | `20X Cross` |
| `1446` | `0xc74a...ab93` | `LONG` | 1,504,242.29 USD | `15,536.82` | `64.06` | `96.82` | `54.89` | 509,013.45 USD | `+33.84%` | `5X Isolated` |
| `1484` | `0x5f10...d49d` | `LONG` | 1,452,585.00 USD | `15,000.00` | `96.35` | `96.82` | `70.94` | 7,283.84 USD | `+0.50%` | `20X Cross` |
| `1485` | `0xb322...d51f` | `LONG` | 1,452,507.57 USD | `14,999.82` | `102.98` | `96.82` | `44.83` | -92,219.74 USD | `-6.35%` | `20X Cross` |
| `1535` | `0xffb2...5ed6` | `LONG` | 1,404,093.57 USD | `14,504.05` | `117.89` | `96.82` | `85.42` | -305,811.14 USD | `-21.78%` | `20X Cross` |
| `1567` | `0x0d6a...ca57` | `LONG` | 1,375,658.33 USD | `14,206.65` | `110.41` | `96.82` | `91.60` | -192,932.02 USD | `-14.02%` | `5X Isolated` |
| `1580` | `0xe863...8bb8` | `SHORT` | 1,360,180.68 USD | `14,047.39` | `97.02` | `96.82` | `212.55` | 2,653.27 USD | `+0.20%` | `20X Cross` |
| `1749` | `0x69cc...14fd` | `SHORT` | 1,193,119.43 USD | `12,320.65` | `99.01` | `96.82` | `746.17` | 26,736.95 USD | `+2.24%` | `20X Cross` |
| `1773` | `0x2814...9b08` | `LONG` | 1,168,034.29 USD | `12,061.71` | `96.37` | `96.82` | `93.93` | 5,695.54 USD | `+0.49%` | `20X Isolated` |
| `1857` | `0x7808...6e70` | `SHORT` | 1,112,271.32 USD | `11,488.27` | `97.15` | `96.82` | `152.00` | 3,790.90 USD | `+0.34%` | `10X Cross` |
| `1870` | `0x2482...0e55` | `LONG` | 1,100,112.81 USD | `11,363.98` | `122.03` | `96.82` | `88.83` | -286,589.11 USD | `-26.05%` | `20X Isolated` |
| `1893` | `0x45db...86eb` | `LONG` | 1,074,904.02 USD | `11,100.00` | `110.69` | `96.82` | `69.28` | -153,777.88 USD | `-14.31%` | `5X Cross` |
| `1922` | `0x1d04...7c43` | `LONG` | 1,046,772.98 USD | `10,811.76` | `111.55` | `96.82` | `16.54` | -159,288.51 USD | `-15.22%` | `6X Cross` |
| `1946` | `0x34e6...8d74` | `LONG` | 1,033,374.96 USD | `10,671.15` | `101.19` | `96.82` | `15.56` | -46,399.68 USD | `-4.49%` | `20X Cross` |
| `2005` | `0x2577...4897` | `LONG` | 1,002,854.25 USD | `10,356.32` | `96.58` | `96.82` | `0.000000` | 2,621.85 USD | `+0.26%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `101.56` | 22,019.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.02K USD at 101.5600 USD [API] | `2026-10-29 17:38:34` |
| `ANNOUNCEMENT` | `INFO` | `101.01` | 23,419.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 23.42K USD at 101.0100 USD [API] | `2026-10-29 17:57:56` |
| `ANNOUNCEMENT` | `INFO` | `100.53` | 22,222.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.22K USD at 100.5300 USD [API] | `2026-10-29 18:45:28` |
| `ANNOUNCEMENT` | `INFO` | `100.44` | 43.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.04K USD at 100.4400 USD [API] | `2026-10-29 18:31:45` |
| `ANNOUNCEMENT` | `INFO` | `101.79` | 242.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.24K USD at 101.7900 USD [API] | `2026-10-29 14:36:25` |
| `ANNOUNCEMENT` | `INFO` | `100.28` | 12.03 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 100.2800 USD [API] | `2026-10-29 19:14:24` |
| `ANNOUNCEMENT` | `INFO` | `100.23` | 223.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.22K USD at 100.2300 USD [API] | `2026-10-29 19:17:00` |
| `ANNOUNCEMENT` | `INFO` | `100.26` | 31,045.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 31.05K USD at 100.2600 USD [API] | `2026-10-29 19:19:43` |
| `ANNOUNCEMENT` | `INFO` | `100.03` | 29,424.82 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 29.42K USD at 100.0300 USD [API] | `2026-10-29 19:54:45` |
| `ANNOUNCEMENT` | `INFO` | `100.05` | 19.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.02K USD at 100.0500 USD [API] | `2026-10-29 19:53:00` |
| `ANNOUNCEMENT` | `INFO` | `100.05` | 12.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 100.0500 USD [API] | `2026-10-29 19:46:18` |
| `ANNOUNCEMENT` | `INFO` | `99.80` | 10,861.34 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 10.86K USD at 99.8010 USD [API] | `2026-10-29 19:59:10` |
| `ANNOUNCEMENT` | `INFO` | `99.80` | 109.78 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.11K USD at 99.8010 USD [API] | `2026-10-29 19:59:10` |
| `ANNOUNCEMENT` | `INFO` | `99.80` | 367.27 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.37K USD at 99.8010 USD [API] | `2026-10-29 19:59:10` |
| `ANNOUNCEMENT` | `INFO` | `99.48` | 40,603.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 40.60K USD at 99.4800 USD [API] | `2026-10-29 20:02:41` |
| `ANNOUNCEMENT` | `INFO` | `99.48` | 27,296.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 27.30K USD at 99.4810 USD [API] | `2026-10-29 20:02:41` |
| `ANNOUNCEMENT` | `INFO` | `98.86` | 2,361.74 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.36K USD at 98.8590 USD [API] | `2026-10-29 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `98.85` | 4,662.85 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.66K USD at 98.8520 USD [API] | `2026-10-29 20:05:30` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 11.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 11.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 1,282.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.28K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 64.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.06K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 18.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.02K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 397.03 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.40K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 11.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 8,009.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 8.01K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 48.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.05K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 491.09 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.49K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 43.56 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.04K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 115.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.12K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 179.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.18K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.01` | 11.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.0100 USD [API] | `2026-10-29 20:05:04` |
| `ANNOUNCEMENT` | `INFO` | `99.09` | 4,229.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.23K USD at 99.0890 USD [API] | `2026-10-29 20:04:57` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 5,158.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.16K USD at 102.3600 USD [API] | `2026-10-29 15:09:44` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 20.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 102.3600 USD [API] | `2026-10-29 15:09:44` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 1,279.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.28K USD at 102.3600 USD [API] | `2026-10-29 15:09:44` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 2,190.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.19K USD at 102.3600 USD [API] | `2026-10-29 15:09:44` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 885.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.89K USD at 102.3600 USD [API] | `2026-10-29 15:09:44` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 1,339.89 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.34K USD at 102.3600 USD [API] | `2026-10-29 15:09:44` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 233.38 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.23K USD at 102.3600 USD [API] | `2026-10-29 15:09:41` |
| `ANNOUNCEMENT` | `INFO` | `102.36` | 158.66 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.16K USD at 102.3600 USD [API] | `2026-10-29 15:09:41` |
| `ANNOUNCEMENT` | `INFO` | `98.64` | 41,786.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 41.79K USD at 98.6450 USD [API] | `2026-10-29 20:06:19` |
| `ANNOUNCEMENT` | `INFO` | `98.35` | 2,239.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.24K USD at 98.3530 USD [API] | `2026-10-29 20:06:49` |
| `ANNOUNCEMENT` | `INFO` | `98.66` | 1,050.72 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.05K USD at 98.6590 USD [API] | `2026-10-29 20:06:22` |
| `ANNOUNCEMENT` | `INFO` | `98.66` | 362.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.36K USD at 98.6590 USD [API] | `2026-10-29 20:06:22` |
| `ANNOUNCEMENT` | `INFO` | `98.66` | 323.60 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.32K USD at 98.6590 USD [API] | `2026-10-29 20:06:22` |
| `ANNOUNCEMENT` | `INFO` | `98.66` | 166.73 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.17K USD at 98.6590 USD [API] | `2026-10-29 20:06:22` |
| `ANNOUNCEMENT` | `INFO` | `98.36` | 16,621.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 16.62K USD at 98.3640 USD [API] | `2026-10-29 20:06:49` |
| `ANNOUNCEMENT` | `INFO` | `103.85` | 420.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.42K USD at 103.8500 USD [API] | `2026-10-28 20:01:53` |
| `ANNOUNCEMENT` | `INFO` | `103.85` | 24.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 103.8500 USD [API] | `2026-10-28 20:01:53` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 3,544.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.54K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 16.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 100.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 499.48 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.50K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 1,304.49 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.30K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 21.11 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 402.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.40K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 226.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.23K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 29.14 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.03K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 11.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 804.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.80K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 11.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 51.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.05K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 75.38 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.08K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.50` | 3,999.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.00K USD at 100.5000 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.51` | 22,221.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 22.22K USD at 100.5100 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `100.51` | 2,923.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.92K USD at 100.5100 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `98.61` | 13,937.11 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 13.94K USD at 98.6070 USD [API] | `2026-09-10 12:47:06` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+4.42%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--4.91%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.32%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--4.93%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.32%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--4.93%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+7.32%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--4.98%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.45` | 2,520.00 USD | 122,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.65` | 650.22 USD | 122,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.75` | 15,800.00 USD | 122,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 719.56 USD | 122,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 1,010.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.75` | 1,310.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 906.41 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.25` | 243.53 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,740.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 299.66 USD | 122,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 1,280.00 USD | 122,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 122,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 4,920.00 USD | 122,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 111.13 USD | 122,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 14,160.00 USD | 122,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.85` | 1,140.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,150.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 243.31 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 106.48 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 1,100.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 9,510.00 USD | 122,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 863,150.00 USD | 122,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.95` | 1,120.00 USD | 121,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.35` | 134.41 USD | 121,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.45` | 386.31 USD | 121,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 147,190.00 USD | 121,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 664.24 USD | 121,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,250.00 USD | 121,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 121,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 15,610.00 USD | 121,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 121,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 22,870.00 USD | 121,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 2,930.00 USD | 121,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 5,210.00 USD | 121,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 296.36 USD | 121,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 9,760.00 USD | 121,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.55` | 478.70 USD | 121,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 102.60 USD | 121,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 10,110.00 USD | 121,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 260.76 USD | 121,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 5,380.00 USD | 121,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 121,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 32,050.00 USD | 121,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 698.75 USD | 121,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,910.00 USD | 121,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 4,610.00 USD | 121,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,320.00 USD | 121,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 15,020.00 USD | 121,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.65` | 1,940.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 5,770.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 9,830.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 10,680.00 USD | 121,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 433.20 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.85` | 67,250.00 USD | 121,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 239.60 USD | 121,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 5,410.00 USD | 121,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 49,040.00 USD | 121,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.45` | 4,240.00 USD | 121,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 889.01 USD | 121,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 121,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 157.64 USD | 121,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 92,850.00 USD | 121,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 621.00 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 160.11 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 161.77 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 37,860.00 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 1,600.00 USD | 120,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 853.90 USD | 120,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 48,870.00 USD | 120,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 20,580.00 USD | 120,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 120,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 137.24 USD | 120,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 8,530.00 USD | 120,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 3,750.00 USD | 120,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 535.71 USD | 120,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 500.85 USD | 120,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 574,700.00 USD | 120,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 226.11 USD | 120,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.25` | 979.55 USD | 120,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 687.00 USD | 120,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 575.95 USD | 120,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 6,330.00 USD | 120,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 38,240.00 USD | 120,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 120,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 3,760.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 580.33 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 9,280.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 2,570.00 USD | 113,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.55` | 39,390.00 USD | 113,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 7,370.00 USD | 113,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 2,940.00 USD | 113,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 48,880.00 USD | 113,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 6,340.00 USD | 113,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 951.47 USD | 113,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 397,000.00 USD | 113,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 5,300.00 USD | 113,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 4,650.00 USD | 113,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 500.90 USD | 113,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 248.74 USD | 113,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 113,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 39,090.00 USD | 113,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 373.62 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 19,820.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 987.18 USD | 112,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 262.85 USD | 112,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,770.00 USD | 112,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,160.00 USD | 112,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 542.59 USD | 112,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.15` | 191,700.00 USD | 112,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 3,210.00 USD | 112,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 477.84 USD | 112,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 112,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 15,940.00 USD | 109,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 984.42 USD | 109,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 109,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 109,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 5,550.00 USD | 109,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,470.00 USD | 109,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 882,650.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.25` | 3,580.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 3,640.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 258.40 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 1,560.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 12,080.00 USD | 108,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 108,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.95` | 599.25 USD | 108,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 12,450.00 USD | 108,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 2,510.00 USD | 108,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 108,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 12,720.00 USD | 108,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 2,770.00 USD | 108,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 142.10 USD | 108,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 6,650.00 USD | 108,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 3,070.00 USD | 108,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 108,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 251.82 USD | 108,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 19,430.00 USD | 108,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 576.71 USD | 108,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 59,950.00 USD | 108,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 2,160.00 USD | 108,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,020.00 USD | 108,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 48,400.00 USD | 108,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 213.61 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 8,930.00 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 146.19 USD | 108,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 8,370.00 USD | 108,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 302.67 USD | 108,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,250.00 USD | 108,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 9,810.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,440.00 USD | 108,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 4,980.00 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 570.93 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 1,080.00 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 512.45 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 68,830.00 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 106.56 USD | 108,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 108,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,220.00 USD | 108,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,550.00 USD | 108,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 2,910.00 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 1,130,000.00 USD | 108,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 18,310.00 USD | 107,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 25,520.00 USD | 107,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 107,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 711,130.00 USD | 107,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 6,510.00 USD | 106,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 9,620.00 USD | 106,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 106,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 31,200.00 USD | 106,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 106,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 106,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 319.09 USD | 106,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 106,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 106,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 106,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 3,770,000.00 USD | 106,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 730.66 USD | 102,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 102,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 102,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 10,430.00 USD | 102,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 140.55 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,090.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 2,820.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,430.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 5,430.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 165.73 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 1,940.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 745,160.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 103,540.00 USD | 101,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 58,180.00 USD | 101,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 13,300.00 USD | 101,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 5,970.00 USD | 101,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,430.00 USD | 101,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 5,280.00 USD | 101,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 2,930.00 USD | 101,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,250.00 USD | 101,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 9,370.00 USD | 101,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 30,920.00 USD | 101,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 15,720.00 USD | 101,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,840.00 USD | 101,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 8,510.00 USD | 101,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 276.22 USD | 101,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,700.00 USD | 101,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 888.30 USD | 101,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 17,180.00 USD | 101,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 2,870.00 USD | 101,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 8,890.00 USD | 101,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 100.50 USD | 101,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 41,900.00 USD | 101,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 24,170.00 USD | 101,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,450.00 USD | 101,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 1,730.00 USD | 101,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 7,860.00 USD | 101,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 18,190.00 USD | 101,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,800.00 USD | 101,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,400.00 USD | 101,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 5,570.00 USD | 101,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 41,900.00 USD | 101,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 27,930.00 USD | 101,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 5,110.00 USD | 101,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 1,230,000.00 USD | 101,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 2,620.00 USD | 100,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,940.00 USD | 100,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 4,280.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 3,920.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 135,710.00 USD | 100,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,620.00 USD | 99,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 99,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 46,110.00 USD | 99,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 470,630.00 USD | 99,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 10,410.00 USD | 99,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 117,540.00 USD | 99,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 6,220.00 USD | 99,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 2,820.00 USD | 99,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 28,310.00 USD | 99,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 99,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 2,630.00 USD | 99,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 3,990.00 USD | 99,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 99,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 2,210.00 USD | 99,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 7,080.00 USD | 99,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 3,110.00 USD | 99,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,230.00 USD | 99,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,130.00 USD | 99,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,000.00 USD | 99,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 44,280.00 USD | 99,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 1,390.00 USD | 99,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 99,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 99,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 60,060.00 USD | 99,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 3,490.00 USD | 98,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 98,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 5,360.00 USD | 98,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 15,930.00 USD | 98,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 753.04 USD | 98,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 60,580.00 USD | 98,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,730.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 16,300.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 867,810.00 USD | 98,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 97,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 1,650.00 USD | 97,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 341.93 USD | 97,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,170.00 USD | 97,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 97,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 157,120.00 USD | 97,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 5,090.00 USD | 97,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 97,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 91,560.00 USD | 97,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 3,550.00 USD | 97,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,050.00 USD | 97,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 5,640.00 USD | 97,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 37,740.00 USD | 97,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 14,990.00 USD | 97,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 12,550.00 USD | 97,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 362,970.00 USD | 97,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 4,730.00 USD | 97,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 17,590.00 USD | 97,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 97,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 4,260.00 USD | 97,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 74,000.00 USD | 97,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 2,770,000.00 USD | 96,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 94,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 2,410.00 USD | 94,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 7,120.00 USD | 94,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 32,060.00 USD | 94,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 12,790.00 USD | 94,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 3,130.00 USD | 94,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 2,370,000.00 USD | 94,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 324.52 USD | 91,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 15,270.00 USD | 91,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 124,360.00 USD | 91,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 6,670.00 USD | 91,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 4,670.00 USD | 91,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 463.51 USD | 91,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 44,840.00 USD | 91,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 703.80 USD | 91,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 1,430.00 USD | 91,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 91,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 51,240.00 USD | 91,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 9,090.00 USD | 91,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 5,000.00 USD | 91,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 34,530.00 USD | 91,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,880.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,390.00 USD | 91,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,610.00 USD | 91,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 5,630.00 USD | 91,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 45,900.00 USD | 91,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 28,800.00 USD | 91,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 127,760.00 USD | 91,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 19,630.00 USD | 91,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 35,140.00 USD | 91,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 11,410.00 USD | 91,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 24,600.00 USD | 91,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 183.16 USD | 91,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 9,630.00 USD | 91,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 91,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,590.00 USD | 91,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,700.00 USD | 91,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 54,770.00 USD | 91,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,850.00 USD | 91,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 4,870.00 USD | 91,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 4,630.00 USD | 91,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 10,170.00 USD | 91,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 4,110.00 USD | 90,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 23,350.00 USD | 90,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 50,540.00 USD | 90,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 7,260.00 USD | 90,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 50,720.00 USD | 90,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 27,860.00 USD | 90,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 36,150.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 1,800.00 USD | 90,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 16,330.00 USD | 90,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 30,200.00 USD | 90,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 134,180.00 USD | 90,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 3,950.00 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,140.00 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 49,160.00 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 2,990.00 USD | 90,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 30,290.00 USD | 90,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 99,650.00 USD | 90,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 16,330.00 USD | 90,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 291.24 USD | 90,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 90,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 416.27 USD | 90,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 49,820.00 USD | 90,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 132,740.00 USD | 90,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 2,280.00 USD | 90,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.15` | 1,600.00 USD | 90,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 5,090.00 USD | 90,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 90,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 8,210.00 USD | 90,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 721.67 USD | 90,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 1,740.00 USD | 90,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 236.99 USD | 90,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 90,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 90,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 317,970.00 USD | 90,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 25,400.00 USD | 89,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 13,060.00 USD | 89,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 37,840.00 USD | 89,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 3,130.00 USD | 89,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,640.00 USD | 89,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,050.00 USD | 89,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,050.00 USD | 89,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 7,510.00 USD | 89,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 15,550.00 USD | 89,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 4,940.00 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 27,320.00 USD | 89,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,750.00 USD | 89,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 66,530.00 USD | 89,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 53,740.00 USD | 89,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 13,170.00 USD | 89,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 5,930.00 USD | 89,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 6,380.00 USD | 89,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 89,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 46,770.00 USD | 89,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 7,370.00 USD | 89,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 39,700.00 USD | 89,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 1,500.00 USD | 89,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 22,250.00 USD | 89,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 72,610.00 USD | 89,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 129,430.00 USD | 89,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 12,060.00 USD | 89,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 5,610.00 USD | 89,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 10,180.00 USD | 89,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,500,000.00 USD | 89,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,650.00 USD | 51,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 22,350.00 USD | 51,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 234,800.00 USD | 51,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 1,370,000.00 USD | 51,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 6,150.00 USD | 49,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 148,710.00 USD | 49,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 5,950.00 USD | 49,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 25,810.00 USD | 49,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 1,640.00 USD | 49,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 21,360.00 USD | 49,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 772,430.00 USD | 49,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 14,370.00 USD | 48,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 9,430.00 USD | 48,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 12,540,000.00 USD | 48,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 212,520.00 USD | 36,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 8,470.00 USD | 36,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 36,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 496,560.00 USD | 36,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 10,540.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 72,890.00 USD | 35,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,170,000.00 USD | 35,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 132,570.00 USD | 33,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 4,770.00 USD | 33,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 46,000.00 USD | 33,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 1,070,000.00 USD | 33,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 18,960.00 USD | 32,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 4,890.00 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 37,930.00 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 69,160.00 USD | 32,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 1,610.00 USD | 32,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 18,890.00 USD | 32,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 16,710.00 USD | 32,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 42,800.00 USD | 32,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 2,170.00 USD | 31,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 27,710.00 USD | 31,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,130.00 USD | 31,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 14,750.00 USD | 31,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 8,210.00 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 159,200.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 258,520.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 29,100.00 USD | 31,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 1,590.00 USD | 31,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 29,400.00 USD | 31,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 33,720.00 USD | 31,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,920.00 USD | 31,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 187,310.00 USD | 31,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 5,600.00 USD | 31,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 34,330.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 16,780.00 USD | 31,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 28,470.00 USD | 31,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 8,830.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 5,350.00 USD | 31,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 18,650.00 USD | 31,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 37,850.00 USD | 31,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 70,280.00 USD | 31,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 26,370.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,040.00 USD | 30,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 33,110.00 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,920.00 USD | 30,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 31,090.00 USD | 30,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 25,000.00 USD | 30,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 22,750.00 USD | 30,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 6,540.00 USD | 30,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 1,030.00 USD | 30,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 218,530.00 USD | 30,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 37,250.00 USD | 30,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 19,330.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 45,730.00 USD | 30,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 56,410.00 USD | 30,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 258,860.00 USD | 30,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 33,560.00 USD | 30,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 28,520.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 1,610,000.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 53,510.00 USD | 28,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 2,880.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 27,920.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,370.00 USD | 28,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 6,190.00 USD | 28,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 37,840.00 USD | 28,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 234,960.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 50,530.00 USD | 28,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 55,910.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 5,060.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 138,630.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 29,350.00 USD | 27,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 1,740,000.00 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 112,880.00 USD | 26,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 25,020.00 USD | 25,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 12,510.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 48,500.00 USD | 25,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 14,630.00 USD | 25,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 9,870.00 USD | 25,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 99,970.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 29,790.00 USD | 25,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,520.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 64,100.00 USD | 25,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 39,070.00 USD | 25,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 232,820.00 USD | 25,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 30,620.00 USD | 25,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,740.00 USD | 25,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,860.00 USD | 25,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 52,670.00 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 68,300.00 USD | 25,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 17,120.00 USD | 25,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 24,370.00 USD | 25,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 156,040.00 USD | 25,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 47,570.00 USD | 24,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 65,100.00 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 9,530.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 5,290.00 USD | 24,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 58,360.00 USD | 24,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 16,340.00 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 30,450.00 USD | 24,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 61,370.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 12,060.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 40,260.00 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 57,660.00 USD | 24,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 104,890.00 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 19,710.00 USD | 24,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 40,160.00 USD | 24,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 82,330.00 USD | 24,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 40,450.00 USD | 24,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 447,810.00 USD | 24,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,990.00 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 23,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 87,540.00 USD | 21,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 62,020.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 46,040.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 65,900.00 USD | 21,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 144,710.00 USD | 21,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 15,000.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 35,560.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 28,980.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,210.00 USD | 21,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 816,770.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 45,020.00 USD | 20,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 157,760.00 USD | 20,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 210,920.00 USD | 19,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 24,020.00 USD | 19,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 318,730.00 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 7,300.00 USD | 19,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 21,450.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 757,820.00 USD | 19,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 105,340.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 99,370.00 USD | 18,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 154,480.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 265,320.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.40` | 169,610,000.00 USD | 169,610,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.45` | 226,260.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 11,130.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.60` | 169,570,000.00 USD | 169,570,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.65` | 444,340.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 84,820.00 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.80` | 169,560,000.00 USD | 169,560,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.85` | 11,040.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 98,980.00 USD | 17,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 118,290.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 74,940.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.20` | 169,550,000.00 USD | 169,550,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.25` | 46,440.00 USD | 16,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.40` | 169,530,000.00 USD | 169,530,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.45` | 85,960.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 7,850.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 101,540.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 291,660.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 106,940.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 617.59 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 27,400.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 5,060.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.20` | 169,500,000.00 USD | 169,500,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.25` | 610,150.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,460.00 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.40` | 169,280,000.00 USD | 169,280,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.45` | 77,940.00 USD | 15,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 1,250,000.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.60` | 169,080,000.00 USD | 169,080,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.65` | 44,390.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 97,950.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.80` | 168,890,000.00 USD | 168,890,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.85` | 82,540.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 332,500.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 138,200.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 51,580.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.20` | 168,630,000.00 USD | 168,630,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 52,570.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 3,370.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.40` | 168,420,000.00 USD | 168,420,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.45` | 187,940.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 27,880.00 USD | 13,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 190,730.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.70` | 180,650,000.00 USD | 180,650,000.00 USD | 5,980.00 USD | 367,860.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.75` | 34,760.00 USD | 13,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.80` | 168,100,000.00 USD | 168,100,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 75,910.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.90` | 180,200,000.00 USD | 180,200,000.00 USD | 330,140.00 USD | 382,120.00 USD | 267,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 152,510.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.00` | 167,950,000.00 USD | 167,950,000.00 USD | 271,000.00 USD | 183,160.00 USD | 310,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 30,400.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.10` | 179,220,000.00 USD | 179,220,000.00 USD | 121,630.00 USD | 119,130.00 USD | 301,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 4,670.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.20` | 167,190,000.00 USD | 167,190,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 92,480.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.30` | 178,680,000.00 USD | 178,680,000.00 USD | 254,340.00 USD | 268,220.00 USD | 308,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 72,050.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.40` | 167,160,000.00 USD | 167,160,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 149,740.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.50` | 177,850,000.00 USD | 177,850,000.00 USD | 158,670.00 USD | 252,960.00 USD | 86,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 136,390.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.60` | 166,400,000.00 USD | 166,400,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 105,660.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.70` | 177,350,000.00 USD | 177,350,000.00 USD | 8,600.00 USD | 250,230.00 USD | 263,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 28,570.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.80` | 165,710,000.00 USD | 165,710,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 132,500.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.90` | 176,830,000.00 USD | 176,830,000.00 USD | 134,550.00 USD | 427,430.00 USD | 933,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 7,240.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.00` | 165,280,000.00 USD | 165,280,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 157,170.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.10` | 175,330,000.00 USD | 175,330,000.00 USD | 59,290.00 USD | 35,690.00 USD | 232,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.15` | 21,240.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.20` | 165,020,000.00 USD | 165,020,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.25` | 49,430.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.30` | 175,000,000.00 USD | 175,000,000.00 USD | 116,980.00 USD | 275,350.00 USD | 276,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.35` | 29,870.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.40` | 164,960,000.00 USD | 164,960,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.45` | 120,820.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.50` | 174,340,000.00 USD | 174,340,000.00 USD | 86,840.00 USD | 99,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.55` | 293,840.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 110,320.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.70` | 174,150,000.00 USD | 174,150,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 167,190.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.80` | 164,390,000.00 USD | 164,390,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,100,000.00 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.90` | 173,400,000.00 USD | 173,400,000.00 USD | 143,140.00 USD | 62,660.00 USD | 214,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 35,580.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.00` | 164,140,000.00 USD | 164,140,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 31,430.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.10` | 172,980,000.00 USD | 172,980,000.00 USD | 160,900.00 USD | 83,520.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 160,380.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.20` | 163,210,000.00 USD | 163,210,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.30` | 172,720,000.00 USD | 172,720,000.00 USD | 221,290.00 USD | 284,680.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 24,970.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.40` | 162,880,000.00 USD | 162,880,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 533,440.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.50` | 172,210,000.00 USD | 172,210,000.00 USD | 4,870.00 USD | 50,620.00 USD | 293,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 73,400.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.60` | 161,990,000.00 USD | 161,990,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 13,840.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.70` | 171,860,000.00 USD | 171,860,000.00 USD | 133,580.00 USD | 30,600.00 USD | 423,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 131,170.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.80` | 160,310,000.00 USD | 160,310,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 71,740.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.90` | 171,270,000.00 USD | 171,270,000.00 USD | 129,660.00 USD | 91,010.00 USD | 144,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 75,470.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.00` | 159,260,000.00 USD | 159,260,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 37,810.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.10` | 170,910,000.00 USD | 170,910,000.00 USD | 1,080,000.00 USD | 892,740.00 USD | 573,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 60,790.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.20` | 157,140,000.00 USD | 157,140,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 106,900.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.30` | 168,360,000.00 USD | 168,360,000.00 USD | 661,900.00 USD | 443,900.00 USD | 346,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 63,960.00 USD | 8,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.40` | 154,560,000.00 USD | 154,560,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 34,130.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.50` | 166,910,000.00 USD | 166,910,000.00 USD | 630,230.00 USD | 452,810.00 USD | 814,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 78,250.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.60` | 153,000,000.00 USD | 153,000,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 116,420.00 USD | 8,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 165,010,000.00 USD | 165,010,000.00 USD | 628,630.00 USD | 803,190.00 USD | 348,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 79,020.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.80` | 149,390,000.00 USD | 149,390,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 73,170.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.90` | 163,230,000.00 USD | 163,230,000.00 USD | 673,680.00 USD | 420,760.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 16,410.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.00` | 145,500,000.00 USD | 145,500,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 389,160.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.10` | 162,040,000.00 USD | 162,040,000.00 USD | 436,270.00 USD | 732,110.00 USD | 467,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 288,250.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.20` | 142,890,000.00 USD | 142,890,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 29,640.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.30` | 160,410,000.00 USD | 160,410,000.00 USD | 150,320.00 USD | 221,290.00 USD | 484,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 30,150.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.40` | 139,110,000.00 USD | 139,110,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 350,660.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.50` | 159,550,000.00 USD | 159,550,000.00 USD | 850,930.00 USD | 781,420.00 USD | 644,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,210,000.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.60` | 135,280,000.00 USD | 135,280,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,430,000.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 157,270,000.00 USD | 157,270,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 237,680.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.80` | 132,890,000.00 USD | 132,890,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 32,760.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.90` | 155,370,000.00 USD | 155,370,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 652,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 161,120.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.00` | 130,470,000.00 USD | 130,470,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 75,600.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.10` | 152,620,000.00 USD | 152,620,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 577,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 324,120.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.20` | 128,140,000.00 USD | 128,140,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 234,300.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.30` | 147,060,000.00 USD | 147,060,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 371,010.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.40` | 123,880,000.00 USD | 123,880,000.00 USD | 550,500.00 USD | 843,410.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 83,740.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.50` | 144,140,000.00 USD | 144,140,000.00 USD | 1,300,000.00 USD | 712,060.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 4,870.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.60` | 120,950,000.00 USD | 120,950,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 14,980.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 139,570,000.00 USD | 139,570,000.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 2,250.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.80` | 118,280,000.00 USD | 118,280,000.00 USD | 463,730.00 USD | 2,370,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 16,750.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.90` | 135,680,000.00 USD | 135,680,000.00 USD | 3,420,000.00 USD | 2,100,000.00 USD | 2,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 688,830.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.00` | 113,800,000.00 USD | 113,800,000.00 USD | 708,990.00 USD | 557,320.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 29,940.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.10` | 127,310,000.00 USD | 127,310,000.00 USD | 2,850,000.00 USD | 3,470,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 29,150.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.20` | 110,510,000.00 USD | 110,510,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 40,160.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.30` | 118,730,000.00 USD | 118,730,000.00 USD | 3,040,000.00 USD | 3,230,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 10,780.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.40` | 106,620,000.00 USD | 106,620,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 8,530.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.50` | 110,930,000.00 USD | 110,930,000.00 USD | 3,020,000.00 USD | 2,340,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 205.81 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 101,910,000.00 USD | 101,910,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 3,240.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.70` | 103,220,000.00 USD | 103,220,000.00 USD | 640,730.00 USD | 3,170,000.00 USD | 960,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 21,700.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.80` | 98,970,000.00 USD | 98,970,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 16,380.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.90` | 98,450,000.00 USD | 98,450,000.00 USD | 1,610,000.00 USD | 967,780.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,190,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.00` | 93,720,000.00 USD | 93,720,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 8,980.00 USD | 825,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.10` | 94,440,000.00 USD | 94,440,000.00 USD | 768,990.00 USD | 1,310,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 29,670.00 USD | 816,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.20` | 87,070,000.00 USD | 87,070,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 14,820.00 USD | 786,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.30` | 89,700,000.00 USD | 89,700,000.00 USD | 2,300,000.00 USD | 1,250,000.00 USD | 531,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 13,000.00 USD | 771,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.40` | 83,330,000.00 USD | 83,330,000.00 USD | 0.00 USD | 515,800.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 185,300.00 USD | 758,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.50` | 85,610,000.00 USD | 85,610,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 141,190.00 USD | 573,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 82,810,000.00 USD | 82,810,000.00 USD | 560,570.00 USD | 0.00 USD | 432,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 37,940.00 USD | 432,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.70` | 82,160,000.00 USD | 82,160,000.00 USD | 1,570,000.00 USD | 598,120.00 USD | 429,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 45,890.00 USD | 394,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.80` | 81,810,000.00 USD | 81,810,000.00 USD | 2,090,000.00 USD | 152,290.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 32,160.00 USD | 348,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.90` | 79,560,000.00 USD | 79,560,000.00 USD | 3,530,000.00 USD | 900,710.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 28,900.00 USD | 316,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.00` | 76,140,000.00 USD | 76,140,000.00 USD | 3,740,000.00 USD | 4,780,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 59,310.00 USD | 287,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.10` | 73,160,000.00 USD | 73,160,000.00 USD | 3,780,000.00 USD | 1,900,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 20,810.00 USD | 228,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.20` | 66,040,000.00 USD | 66,040,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 42,330.00 USD | 207,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.30` | 66,410,000.00 USD | 66,410,000.00 USD | 1,850,000.00 USD | 1,790,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 6,050.00 USD | 164,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.40` | 63,290,000.00 USD | 63,290,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 8,540.00 USD | 158,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.50` | 58,840,000.00 USD | 58,840,000.00 USD | 833,050.00 USD | 1,690,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 33,150.00 USD | 150,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.60` | 53,990,000.00 USD | 53,990,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 5,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 37,490.00 USD | 117,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.70` | 53,950,000.00 USD | 53,950,000.00 USD | 2,410,000.00 USD | 2,670,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.75` | 44,730.00 USD | 79,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.80` | 37,680,000.00 USD | 37,680,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 34,800.00 USD | 35,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.90` | 42,400,000.00 USD | 42,400,000.00 USD | 4,490,000.00 USD | 2,100,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.95` | 231.24 USD | 231.24 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.00` | 31,890,000.00 USD | 31,890,000.00 USD | 5,990,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 31,890,000.00 USD | 31,890,000.00 USD | 4,130,000.00 USD | 5,640,000.00 USD | 5,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 18,990,000.00 USD | 18,990,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 16,980,000.00 USD | 16,980,000.00 USD | 6,740,000.00 USD | 6,040,000.00 USD | 453,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 4,190,000.00 USD | 4,190,000.00 USD | 1,600,000.00 USD | 2,550,000.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 3,750,000.00 USD | 3,750,000.00 USD | 1,300,000.00 USD | 1,230,000.00 USD | 328,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 24,800.00 USD | 24,800.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.70` | 894,880.00 USD | 894,880.00 USD | 0.00 USD | 894,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.30` | 174,820.00 USD | 174,820.00 USD | 174,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.50` | 3,190,000.00 USD | 3,190,000.00 USD | 896,130.00 USD | 1,280,000.00 USD | 844,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 24,930.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.70` | 6,180,000.00 USD | 6,180,000.00 USD | 512,980.00 USD | 441,570.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.80` | 20,260,000.00 USD | 20,260,000.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 13,810,000.00 USD | 13,810,000.00 USD | 4,730,000.00 USD | 690,250.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.00` | 37,600,000.00 USD | 37,600,000.00 USD | 14,750,000.00 USD | 561,730.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.10` | 20,320,000.00 USD | 20,320,000.00 USD | 2,790,000.00 USD | 2,530,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.20` | 48,530,000.00 USD | 48,530,000.00 USD | 9,790,000.00 USD | 1,140,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.30` | 29,990,000.00 USD | 29,990,000.00 USD | 2,390,000.00 USD | 941,940.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.40` | 60,100,000.00 USD | 60,100,000.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.50` | 41,170,000.00 USD | 41,170,000.00 USD | 847,660.00 USD | 3,490,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 23,180.00 USD | 23,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.60` | 69,530,000.00 USD | 69,530,000.00 USD | 1,960,000.00 USD | 5,450,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 2,850.00 USD | 26,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.70` | 58,990,000.00 USD | 58,990,000.00 USD | 1,790,000.00 USD | 5,700,000.00 USD | 10,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.75` | 10,260.00 USD | 36,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.80` | 75,680,000.00 USD | 75,680,000.00 USD | 1,420,000.00 USD | 797,640.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.90` | 71,140,000.00 USD | 71,140,000.00 USD | 2,810,000.00 USD | 3,940,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 8,770.00 USD | 45,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.00` | 84,510,000.00 USD | 84,510,000.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 42,640.00 USD | 87,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.10` | 86,980,000.00 USD | 86,980,000.00 USD | 3,640,000.00 USD | 6,370,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,140,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.20` | 98,480,000.00 USD | 98,480,000.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 50,940.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.30` | 96,020,000.00 USD | 96,020,000.00 USD | 3,190,000.00 USD | 3,420,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 79,350.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.40` | 99,520,000.00 USD | 99,520,000.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 4,360.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.50` | 100,980,000.00 USD | 100,980,000.00 USD | 1,560,000.00 USD | 2,630,000.00 USD | 761,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 12,460.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.60` | 104,950,000.00 USD | 104,950,000.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 36,170.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.70` | 123,500,000.00 USD | 123,500,000.00 USD | 4,400,000.00 USD | 7,120,000.00 USD | 11,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 25,510.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.80` | 108,280,000.00 USD | 108,280,000.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 4,370.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.90` | 132,290,000.00 USD | 132,290,000.00 USD | 857,690.00 USD | 1,960,000.00 USD | 5,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 2,110.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.00` | 119,610,000.00 USD | 119,610,000.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 48,480.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.10` | 139,550,000.00 USD | 139,550,000.00 USD | 2,220,000.00 USD | 3,440,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 44,320.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.20` | 125,710,000.00 USD | 125,710,000.00 USD | 843,770.00 USD | 2,470,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 347,460.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.30` | 145,450,000.00 USD | 145,450,000.00 USD | 869,050.00 USD | 2,130,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 391,910.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.40` | 130,400,000.00 USD | 130,400,000.00 USD | 993,830.00 USD | 654,600.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.45` | 6,010.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.50` | 153,220,000.00 USD | 153,220,000.00 USD | 2,300,000.00 USD | 1,270,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 13,880.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.60` | 136,280,000.00 USD | 136,280,000.00 USD | 2,150,000.00 USD | 1,480,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.70` | 161,550,000.00 USD | 161,550,000.00 USD | 2,340,000.00 USD | 2,480,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,590.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.80` | 139,610,000.00 USD | 139,610,000.00 USD | 1,160,000.00 USD | 1,380,000.00 USD | 786,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 742.26 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.90` | 169,110,000.00 USD | 169,110,000.00 USD | 2,580,000.00 USD | 2,670,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 12,270.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.00` | 158,590,000.00 USD | 158,590,000.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 698.26 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.10` | 182,380,000.00 USD | 182,380,000.00 USD | 7,690,000.00 USD | 2,790,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 12,940.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.20` | 178,000,000.00 USD | 178,000,000.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.30` | 192,290,000.00 USD | 192,290,000.00 USD | 3,410,000.00 USD | 3,630,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.35` | 922.29 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.40` | 195,050,000.00 USD | 195,050,000.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.50` | 206,430,000.00 USD | 206,430,000.00 USD | 3,140,000.00 USD | 3,310,000.00 USD | 7,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.60` | 205,580,000.00 USD | 205,580,000.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 2,640.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 215,870,000.00 USD | 215,870,000.00 USD | 2,080,000.00 USD | 881,090.00 USD | 6,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 215,500,000.00 USD | 215,500,000.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.85` | 13,380.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.90` | 221,690,000.00 USD | 221,690,000.00 USD | 2,320,000.00 USD | 1,290,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,560.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.00` | 221,490,000.00 USD | 221,490,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,710.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.10` | 228,150,000.00 USD | 228,150,000.00 USD | 2,960,000.00 USD | 1,440,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 228,220,000.00 USD | 228,220,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.30` | 232,120,000.00 USD | 232,120,000.00 USD | 1,670,000.00 USD | 1,260,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 233,520,000.00 USD | 233,520,000.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.50` | 236,450,000.00 USD | 236,450,000.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.55` | 632.73 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.60` | 235,980,000.00 USD | 235,980,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,070.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 238,340,000.00 USD | 238,340,000.00 USD | 1,110,000.00 USD | 660,360.00 USD | 126,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,340.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.80` | 244,080,000.00 USD | 244,080,000.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.90` | 242,870,000.00 USD | 242,870,000.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,380.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.00` | 261,010,000.00 USD | 261,010,000.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 692.50 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.10` | 247,830,000.00 USD | 247,830,000.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 14,800.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.20` | 273,680,000.00 USD | 273,680,000.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 551.36 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.30` | 249,650,000.00 USD | 249,650,000.00 USD | 334,720.00 USD | 717,010.00 USD | 773,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 7,370.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.40` | 288,250,000.00 USD | 288,250,000.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.50` | 256,230,000.00 USD | 256,230,000.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 1,610.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.60` | 306,640,000.00 USD | 306,640,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 13,760.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 260,940,000.00 USD | 260,940,000.00 USD | 1,370,000.00 USD | 720,260.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,320.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.80` | 319,030,000.00 USD | 319,030,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 14,630.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.90` | 264,760,000.00 USD | 264,760,000.00 USD | 1,370,000.00 USD | 1,640,000.00 USD | 803,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.95` | 1,580.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.00` | 345,730,000.00 USD | 345,730,000.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 775.17 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.10` | 269,680,000.00 USD | 269,680,000.00 USD | 2,020,000.00 USD | 724,740.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,060.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.20` | 367,760,000.00 USD | 367,760,000.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 1,240.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.30` | 272,360,000.00 USD | 272,360,000.00 USD | 1,000,000.00 USD | 971,040.00 USD | 701,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 3,900.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.40` | 384,940,000.00 USD | 384,940,000.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 8,820.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.50` | 275,510,000.00 USD | 275,510,000.00 USD | 1,200,000.00 USD | 974,960.00 USD | 968,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 575.03 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.60` | 402,690,000.00 USD | 402,690,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 1,140.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 281,100,000.00 USD | 281,100,000.00 USD | 1,660,000.00 USD | 910,560.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 3,620.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.80` | 420,090,000.00 USD | 420,090,000.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.85` | 41,340.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.90` | 282,570,000.00 USD | 282,570,000.00 USD | 486,940.00 USD | 283,560.00 USD | 703,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 125,660.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.00` | 436,250,000.00 USD | 436,250,000.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 8,570.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.10` | 284,410,000.00 USD | 284,410,000.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.15` | 12,590.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.20` | 446,920,000.00 USD | 446,920,000.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,090.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.30` | 284,600,000.00 USD | 284,600,000.00 USD | 94,380.00 USD | 96,460.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 6,840.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.40` | 455,130,000.00 USD | 455,130,000.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 531,450.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.50` | 285,210,000.00 USD | 285,210,000.00 USD | 245,610.00 USD | 180,000.00 USD | 188,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.60` | 463,550,000.00 USD | 463,550,000.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 216.58 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 285,430,000.00 USD | 285,430,000.00 USD | 65,040.00 USD | 150,210.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 472,360,000.00 USD | 472,360,000.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 91,620.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.90` | 286,490,000.00 USD | 286,490,000.00 USD | 177,140.00 USD | 685,100.00 USD | 191,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.00` | 477,520,000.00 USD | 477,520,000.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.10` | 287,960,000.00 USD | 287,960,000.00 USD | 706,860.00 USD | 459,510.00 USD | 301,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.15` | 605.06 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.20` | 486,410,000.00 USD | 486,410,000.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.25` | 180.62 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.30` | 289,160,000.00 USD | 289,160,000.00 USD | 320,000.00 USD | 488,800.00 USD | 395,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 253,580.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.40` | 492,500,000.00 USD | 492,500,000.00 USD | 2,430,000.00 USD | 2,180,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 198,600.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.50` | 290,090,000.00 USD | 290,090,000.00 USD | 326,070.00 USD | 292,550.00 USD | 306,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.55` | 108.68 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.60` | 497,340,000.00 USD | 497,340,000.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 19,750.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.70` | 292,620,000.00 USD | 292,620,000.00 USD | 758,730.00 USD | 310,350.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.75` | 397,560.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.80` | 501,990,000.00 USD | 501,990,000.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 478,970.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.90` | 293,440,000.00 USD | 293,440,000.00 USD | 158,670.00 USD | 336,790.00 USD | 322,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 291.97 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.00` | 506,130,000.00 USD | 506,130,000.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 15,220.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.10` | 294,500,000.00 USD | 294,500,000.00 USD | 97,170.00 USD | 367,640.00 USD | 596,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.20` | 507,220,000.00 USD | 507,220,000.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 34,950.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.40` | 508,510,000.00 USD | 508,510,000.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.60` | 509,140,000.00 USD | 509,140,000.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 509,970,000.00 USD | 509,970,000.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 146,260.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.00` | 510,550,000.00 USD | 510,550,000.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.20` | 510,830,000.00 USD | 510,830,000.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 179,190.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.40` | 511,320,000.00 USD | 511,320,000.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 261.61 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 511,510,000.00 USD | 511,510,000.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.80` | 512,430,000.00 USD | 512,430,000.00 USD | 350,210.00 USD | 286,220.00 USD | 287,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.00` | 512,720,000.00 USD | 512,720,000.00 USD | 0.00 USD | 0.00 USD | 286,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.05` | 4,440,000.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.35` | 1,850.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 426.86 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.55` | 356.04 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 38,640.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 459.17 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.95` | 495.87 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.05` | 14,790.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 2,970.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 385.12 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,580.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 4,450.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 260,900.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 1,910.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 1,070.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 130,940.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,990.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 619.51 USD | 10,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 10,030.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 698.75 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 4,970.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 3,360.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.55` | 17,470.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 31,480.00 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 107,800.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 2,370.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,740.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,830.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 3,430.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.95` | 220.70 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 1,260.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 878,270.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 182,070.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.95` | 162.33 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.15` | 5,990.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 5,400.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.75` | 40,860.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 89,950.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 11,780.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 188.08 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 10,360.00 USD | 12,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 2,090.00 USD | 12,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.25` | 8,670.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.35` | 4,470,000.00 USD | 17,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 17,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 7,700.00 USD | 17,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.65` | 5,740.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.15` | 12,550.00 USD | 17,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 17,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 57,850.00 USD | 17,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 8,970.00 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 485.39 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.95` | 29,570.00 USD | 17,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 98,720.00 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.25` | 925.93 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 60,370.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 1,110.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 316.20 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 31,420.00 USD | 17,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 34,870.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,330.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.35` | 881,450.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 45,560.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.75` | 61,380.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.05` | 9,500.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 471,560.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,990.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 1,960.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.55` | 124,410.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.85` | 126.33 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.95` | 762.29 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 114.40 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 5,330.00 USD | 19,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 9,550.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.25` | 3,330.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 19,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 4,160,000.00 USD | 23,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 4,610.00 USD | 23,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 1,560.00 USD | 23,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 23,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 23,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 23,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 1,030.00 USD | 23,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 6,050.00 USD | 23,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 5,150.00 USD | 23,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.55` | 403.69 USD | 23,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 35,270.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.15` | 389.08 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 28,940.00 USD | 23,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.45` | 138.92 USD | 23,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 20,800.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 23,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.15` | 221.70 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 257,680.00 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.45` | 6,420.00 USD | 23,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 23,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 23,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 32,440.00 USD | 23,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 124,100.00 USD | 24,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,310.00 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 35,060.00 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.45` | 700,490.00 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 910.74 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 2,210.00 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 13,360.00 USD | 24,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.55` | 1,860.00 USD | 24,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 3,180.00 USD | 24,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 24,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 24,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 24,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.35` | 14,160.00 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 6,700.00 USD | 24,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 106.88 USD | 24,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 30,070.00 USD | 24,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.45` | 1,720.00 USD | 24,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.75` | 136.73 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 103.78 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 24,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.25` | 1,330.00 USD | 24,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 24,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 25,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 25,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 25,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.15` | 2,180.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 25,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.05` | 6,390.00 USD | 25,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.35` | 8,560.00 USD | 25,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.65` | 48,790.00 USD | 25,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.75` | 4,060.00 USD | 25,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 21,460.00 USD | 25,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 25,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.15` | 40,190.00 USD | 25,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 25,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 25,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.85` | 14,710.00 USD | 25,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 35,260.00 USD | 25,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 25,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 809.19 USD | 25,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.25` | 68,620.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.65` | 2,050.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.75` | 12,520.00 USD | 25,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 25,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 44,270.00 USD | 25,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 25,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 7,310.00 USD | 25,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.55` | 538.96 USD | 25,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.65` | 1,530.00 USD | 25,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 25,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.95` | 8,750.00 USD | 25,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 25,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 253.80 USD | 25,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 25,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 9,060.00 USD | 25,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.85` | 5,050,000.00 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.15` | 625.07 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 127.72 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 702.75 USD | 30,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 7,340.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 70,450.00 USD | 30,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 23,350.00 USD | 30,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 1,950,000.00 USD | 32,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 2,250.00 USD | 32,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.05` | 2,580.00 USD | 32,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 112.30 USD | 32,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.25` | 3,470.00 USD | 32,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.35` | 593,190.00 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.65` | 2,960.00 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.85` | 18,720.00 USD | 33,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,460.00 USD | 33,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 126,920.00 USD | 33,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.45` | 790.41 USD | 33,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 103.36 USD | 33,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 33,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 33,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 33,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 118,420.00 USD | 33,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.65` | 607.36 USD | 33,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 6,300.00 USD | 33,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 685.96 USD | 33,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 33,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 8,730.00 USD | 33,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.45` | 439,350.00 USD | 34,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 75,880.00 USD | 34,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 34,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,070.00 USD | 34,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 17,760.00 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.75` | 75,610.00 USD | 35,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 78,720.00 USD | 35,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.05` | 518,180.00 USD | 35,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 102.22 USD | 35,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 9,130.00 USD | 35,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 95,070.00 USD | 36,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.45` | 1,390,000.00 USD | 37,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 37,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 37,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 263,290.00 USD | 37,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 126,150.00 USD | 37,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.95` | 347.18 USD | 37,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.05` | 24,850.00 USD | 37,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 3,180.00 USD | 37,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.25` | 2,780.00 USD | 37,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 37,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.85` | 1,740,000.00 USD | 39,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 39,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 1,150,000.00 USD | 40,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 200.97 USD | 40,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 286,550.00 USD | 41,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 41,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 41,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 761,410.00 USD | 41,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 44,870.00 USD | 41,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 109,650.00 USD | 42,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.55` | 17,980.00 USD | 42,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 2,110.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 5,430.00 USD | 42,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 42,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 42,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 42,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.65` | 363.43 USD | 42,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 1,160.00 USD | 42,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.95` | 4,700,000.00 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.75` | 2,350.00 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.95` | 118.52 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 7,810.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 4,900.00 USD | 46,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.55` | 327.19 USD | 46,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.85` | 3,570,000.00 USD | 50,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 50,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.45` | 297.58 USD | 50,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 80,280.00 USD | 50,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 95,670.00 USD | 50,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.85` | 236,780.00 USD | 50,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.95` | 27,690.00 USD | 50,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 45,350.00 USD | 50,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 101,550.00 USD | 51,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 51,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 85,160.00 USD | 51,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.95` | 431,860.00 USD | 51,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.05` | 497.76 USD | 51,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 52,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 52,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.65` | 141,270.00 USD | 52,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 52,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 52,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 52,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.85` | 323,700.00 USD | 52,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 52,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.15` | 1,050.00 USD | 52,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.45` | 1,350.00 USD | 52,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.75` | 12,390.00 USD | 52,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 52,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 206,830.00 USD | 53,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.45` | 6,580.00 USD | 53,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.65` | 3,400.00 USD | 53,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 53,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.85` | 620.28 USD | 53,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 996.90 USD | 53,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 53,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.45` | 149.81 USD | 53,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.85` | 685.75 USD | 53,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.55` | 11,330.00 USD | 53,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 3,360.00 USD | 53,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 2,730.00 USD | 53,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 122.68 USD | 53,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 53,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 53,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.05` | 5,700,000.00 USD | 59,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.25` | 25,150.00 USD | 59,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.35` | 112,210.00 USD | 59,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.55` | 444.22 USD | 59,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.15` | 3,400,000.00 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.15` | 232.76 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 202,840.00 USD | 62,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 62,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.05` | 1,190.00 USD | 62,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.35` | 38,140,000.00 USD | 101,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 101,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.75` | 28,130.00 USD | 101,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 900.54 USD | 101,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 36,210.00 USD | 101,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 101,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,790.00 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.25` | 19,820.00 USD | 101,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 119.31 USD | 101,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.55` | 1,640.00 USD | 101,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 101,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.95` | 44,010.00 USD | 101,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.05` | 105,630.00 USD | 101,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 101,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.35` | 1,020,000.00 USD | 102,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 637.76 USD | 102,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.75` | 29,380.00 USD | 102,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 350,160.00 USD | 103,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.55` | 2,830.00 USD | 103,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.75` | 715.00 USD | 103,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.95` | 4,470.00 USD | 103,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.25` | 17,390.00 USD | 103,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.65` | 11,320.00 USD | 103,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.95` | 352,500.00 USD | 103,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.05` | 1,340,000.00 USD | 104,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 104,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.35` | 18,140.00 USD | 104,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.45` | 33,720.00 USD | 104,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 104,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.85` | 3,640,000.00 USD | 108,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 108,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.45` | 1,370.00 USD | 108,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.05` | 73,220.00 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.65` | 286.49 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.65` | 7,650.00 USD | 108,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 108,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 108,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.35` | 10,940.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.15` | 802.31 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.05` | 53,740.00 USD | 108,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.45` | 1,230.00 USD | 108,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.65` | 2,560.00 USD | 108,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 108,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.05` | 2,470.00 USD | 108,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 108,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,110.00 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 439.79 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.55` | 284.33 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 109,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 109,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 118.08 USD | 109,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 122,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.15` | 62,720.00 USD | 122,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.55` | 383,100.00 USD | 123,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.75` | 3,590.00 USD | 123,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.85` | 47,960.00 USD | 123,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 5,760.00 USD | 123,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.55` | 281.12 USD | 123,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 193.15 USD | 123,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 123,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.05` | 9,370.00 USD | 123,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.25` | 1,390.00 USD | 123,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 122,370,000.00 USD | 0.00 USD | 2,520.00 USD | `-80.00%` | `129.70` |
| `Live` | `Long` | `19.65` | 122,370,000.00 USD | 0.00 USD | 650.22 USD | `-79.79%` | `33.09` |
| `Live` | `Long` | `19.75` | 122,370,000.00 USD | 0.00 USD | 15,800.00 USD | `-79.69%` | `800.00` |
| `Live` | `Long` | `19.85` | 122,360,000.00 USD | 0.00 USD | 719.56 USD | `-79.59%` | `36.25` |
| `Live` | `Long` | `20.25` | 122,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-79.18%` | `50.00` |
| `Live` | `Long` | `20.55` | 122,350,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.87%` | `233.31` |
| `Live` | `Long` | `20.75` | 122,350,000.00 USD | 0.00 USD | 1,310.00 USD | `-78.66%` | `63.07` |
| `Live` | `Long` | `21.05` | 122,350,000.00 USD | 0.00 USD | 906.41 USD | `-78.35%` | `43.06` |
| `Live` | `Long` | `21.25` | 122,350,000.00 USD | 0.00 USD | 243.53 USD | `-78.15%` | `11.46` |
| `Live` | `Long` | `21.35` | 122,350,000.00 USD | 0.00 USD | 1,740.00 USD | `-78.04%` | `81.52` |
| `Live` | `Long` | `21.45` | 122,340,000.00 USD | 0.00 USD | 299.66 USD | `-77.94%` | `13.97` |
| `Live` | `Long` | `21.65` | 122,340,000.00 USD | 0.00 USD | 1,280.00 USD | `-77.74%` | `59.27` |
| `Live` | `Long` | `21.75` | 122,340,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.63%` | `212.70` |
| `Live` | `Long` | `22.25` | 122,340,000.00 USD | 0.00 USD | 4,920.00 USD | `-77.12%` | `220.95` |
| `Live` | `Long` | `22.45` | 122,330,000.00 USD | 0.00 USD | 111.13 USD | `-76.91%` | `4.95` |
| `Live` | `Long` | `22.65` | 122,330,000.00 USD | 0.00 USD | 14,160.00 USD | `-76.71%` | `625.38` |
| `Live` | `Long` | `22.85` | 122,320,000.00 USD | 0.00 USD | 1,140.00 USD | `-76.50%` | `50.00` |
| `Live` | `Long` | `22.95` | 122,320,000.00 USD | 0.00 USD | 1,150.00 USD | `-76.40%` | `50.00` |
| `Live` | `Long` | `23.15` | 122,320,000.00 USD | 0.00 USD | 243.31 USD | `-76.19%` | `10.51` |
| `Live` | `Long` | `23.25` | 122,320,000.00 USD | 0.00 USD | 106.48 USD | `-76.09%` | `4.58` |
| `Live` | `Long` | `23.35` | 122,320,000.00 USD | 0.00 USD | 1,100.00 USD | `-75.99%` | `47.02` |
| `Live` | `Long` | `23.45` | 122,320,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.88%` | `58.86` |
| `Live` | `Long` | `23.65` | 122,310,000.00 USD | 0.00 USD | 9,510.00 USD | `-75.68%` | `402.03` |
| `Live` | `Long` | `23.75` | 122,300,000.00 USD | 0.00 USD | 863,150.00 USD | `-75.58%` | `36,343.14` |
| `Live` | `Long` | `23.95` | 121,440,000.00 USD | 0.00 USD | 1,120.00 USD | `-75.37%` | `46.58` |
| `Live` | `Long` | `24.35` | 121,440,000.00 USD | 0.00 USD | 134.41 USD | `-74.96%` | `5.52` |
| `Live` | `Long` | `24.45` | 121,440,000.00 USD | 0.00 USD | 386.31 USD | `-74.86%` | `15.80` |
| `Live` | `Long` | `24.75` | 121,440,000.00 USD | 0.00 USD | 147,190.00 USD | `-74.55%` | `5,947.11` |
| `Live` | `Long` | `24.85` | 121,290,000.00 USD | 0.00 USD | 664.24 USD | `-74.44%` | `26.73` |
| `Live` | `Long` | `25.05` | 121,290,000.00 USD | 0.00 USD | 1,250.00 USD | `-74.24%` | `50.00` |
| `Live` | `Long` | `25.15` | 121,290,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.14%` | `80.00` |
| `Live` | `Long` | `25.35` | 121,290,000.00 USD | 0.00 USD | 15,610.00 USD | `-73.93%` | `615.67` |
| `Live` | `Long` | `25.45` | 121,270,000.00 USD | 0.00 USD | 106.64 USD | `-73.83%` | `4.19` |
| `Live` | `Long` | `25.65` | 121,270,000.00 USD | 0.00 USD | 22,870.00 USD | `-73.62%` | `891.66` |
| `Live` | `Long` | `25.95` | 121,250,000.00 USD | 0.00 USD | 2,930.00 USD | `-73.31%` | `113.00` |
| `Live` | `Long` | `26.05` | 121,250,000.00 USD | 0.00 USD | 5,210.00 USD | `-73.21%` | `200.00` |
| `Live` | `Long` | `26.25` | 121,240,000.00 USD | 0.00 USD | 296.36 USD | `-73.01%` | `11.29` |
| `Live` | `Long` | `26.45` | 121,240,000.00 USD | 0.00 USD | 9,760.00 USD | `-72.80%` | `369.00` |
| `Live` | `Long` | `26.55` | 121,230,000.00 USD | 0.00 USD | 478.70 USD | `-72.70%` | `18.03` |
| `Live` | `Long` | `26.65` | 121,230,000.00 USD | 0.00 USD | 102.60 USD | `-72.59%` | `3.85` |
| `Live` | `Long` | `26.95` | 121,230,000.00 USD | 0.00 USD | 10,110.00 USD | `-72.29%` | `375.19` |
| `Live` | `Long` | `27.05` | 121,220,000.00 USD | 0.00 USD | 260.76 USD | `-72.18%` | `9.64` |
| `Live` | `Long` | `27.15` | 121,220,000.00 USD | 0.00 USD | 5,380.00 USD | `-72.08%` | `198.28` |
| `Live` | `Long` | `27.35` | 121,220,000.00 USD | 0.00 USD | 332.30 USD | `-71.87%` | `12.15` |
| `Live` | `Long` | `27.85` | 121,210,000.00 USD | 0.00 USD | 32,050.00 USD | `-71.36%` | `1,150.66` |
| `Live` | `Long` | `27.95` | 121,180,000.00 USD | 0.00 USD | 698.75 USD | `-71.26%` | `25.00` |
| `Live` | `Long` | `28.05` | 121,180,000.00 USD | 0.00 USD | 2,910.00 USD | `-71.15%` | `103.75` |
| `Live` | `Long` | `28.15` | 121,180,000.00 USD | 0.00 USD | 4,610.00 USD | `-71.05%` | `163.78` |
| `Live` | `Long` | `28.35` | 121,170,000.00 USD | 0.00 USD | 6,320.00 USD | `-70.85%` | `223.00` |
| `Live` | `Long` | `28.45` | 121,170,000.00 USD | 0.00 USD | 15,020.00 USD | `-70.74%` | `527.99` |
| `Live` | `Long` | `28.65` | 121,150,000.00 USD | 0.00 USD | 1,940.00 USD | `-70.54%` | `67.74` |
| `Live` | `Long` | `28.85` | 121,150,000.00 USD | 0.00 USD | 5,770.00 USD | `-70.33%` | `200.00` |
| `Live` | `Long` | `29.15` | 121,150,000.00 USD | 0.00 USD | 9,830.00 USD | `-70.02%` | `337.19` |
| `Live` | `Long` | `29.25` | 121,140,000.00 USD | 0.00 USD | 10,680.00 USD | `-69.92%` | `365.00` |
| `Live` | `Long` | `29.55` | 121,130,000.00 USD | 0.00 USD | 433.20 USD | `-69.61%` | `14.66` |
| `Live` | `Long` | `29.85` | 121,120,000.00 USD | 0.00 USD | 67,250.00 USD | `-69.30%` | `2,252.87` |
| `Live` | `Long` | `29.95` | 121,060,000.00 USD | 0.00 USD | 239.60 USD | `-69.20%` | `8.00` |
| `Live` | `Long` | `30.05` | 121,060,000.00 USD | 0.00 USD | 5,410.00 USD | `-69.10%` | `180.04` |
| `Live` | `Long` | `30.15` | 121,050,000.00 USD | 0.00 USD | 49,040.00 USD | `-68.99%` | `1,626.43` |
| `Live` | `Long` | `30.45` | 121,000,000.00 USD | 0.00 USD | 4,240.00 USD | `-68.69%` | `139.36` |
| `Live` | `Long` | `30.55` | 121,000,000.00 USD | 0.00 USD | 889.01 USD | `-68.58%` | `29.10` |
| `Live` | `Long` | `30.65` | 121,000,000.00 USD | 0.00 USD | 233.86 USD | `-68.48%` | `7.63` |
| `Live` | `Long` | `30.85` | 121,000,000.00 USD | 0.00 USD | 157.64 USD | `-68.27%` | `5.11` |
| `Live` | `Long` | `30.95` | 121,000,000.00 USD | 0.00 USD | 92,850.00 USD | `-68.17%` | `3,000.00` |
| `Live` | `Long` | `31.05` | 120,900,000.00 USD | 0.00 USD | 621.00 USD | `-68.07%` | `20.00` |
| `Live` | `Long` | `31.15` | 120,900,000.00 USD | 0.00 USD | 160.11 USD | `-67.97%` | `5.14` |
| `Live` | `Long` | `31.35` | 120,900,000.00 USD | 0.00 USD | 161.77 USD | `-67.76%` | `5.16` |
| `Live` | `Long` | `31.45` | 120,900,000.00 USD | 0.00 USD | 278.33 USD | `-67.66%` | `8.85` |
| `Live` | `Long` | `31.55` | 120,900,000.00 USD | 0.00 USD | 37,860.00 USD | `-67.55%` | `1,200.00` |
| `Live` | `Long` | `31.95` | 120,870,000.00 USD | 0.00 USD | 1,600.00 USD | `-67.14%` | `50.00` |
| `Live` | `Long` | `32.15` | 120,860,000.00 USD | 0.00 USD | 853.90 USD | `-66.94%` | `26.56` |
| `Live` | `Long` | `32.25` | 120,860,000.00 USD | 0.00 USD | 48,870.00 USD | `-66.83%` | `1,515.38` |
| `Live` | `Long` | `32.35` | 120,810,000.00 USD | 0.00 USD | 20,580.00 USD | `-66.73%` | `636.10` |
| `Live` | `Long` | `32.85` | 120,790,000.00 USD | 0.00 USD | 5,240.00 USD | `-66.22%` | `159.61` |
| `Live` | `Long` | `33.15` | 120,790,000.00 USD | 0.00 USD | 137.24 USD | `-65.91%` | `4.14` |
| `Live` | `Long` | `33.25` | 120,790,000.00 USD | 0.00 USD | 8,530.00 USD | `-65.81%` | `256.66` |
| `Live` | `Long` | `33.45` | 120,780,000.00 USD | 0.00 USD | 3,750.00 USD | `-65.60%` | `112.22` |
| `Live` | `Long` | `33.65` | 120,780,000.00 USD | 0.00 USD | 535.71 USD | `-65.40%` | `15.92` |
| `Live` | `Long` | `33.75` | 120,780,000.00 USD | 0.00 USD | 500.85 USD | `-65.29%` | `14.84` |
| `Live` | `Long` | `33.85` | 120,770,000.00 USD | 0.00 USD | 574,700.00 USD | `-65.19%` | `16,977.90` |
| `Live` | `Long` | `33.95` | 120,200,000.00 USD | 0.00 USD | 226.11 USD | `-65.09%` | `6.66` |
| `Live` | `Long` | `34.25` | 120,200,000.00 USD | 0.00 USD | 979.55 USD | `-64.78%` | `28.60` |
| `Live` | `Long` | `34.35` | 120,200,000.00 USD | 0.00 USD | 687.00 USD | `-64.68%` | `20.00` |
| `Live` | `Long` | `34.55` | 120,200,000.00 USD | 0.00 USD | 575.95 USD | `-64.47%` | `16.67` |
| `Live` | `Long` | `34.65` | 120,200,000.00 USD | 0.00 USD | 6,330.00 USD | `-64.37%` | `182.57` |
| `Live` | `Long` | `34.85` | 120,190,000.00 USD | 0.00 USD | 38,240.00 USD | `-64.16%` | `1,097.38` |
| `Live` | `Long` | `34.95` | 120,150,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-64.06%` | `189,499.36` |
| `Live` | `Long` | `35.05` | 113,530,000.00 USD | 0.00 USD | 3,760.00 USD | `-63.96%` | `107.30` |
| `Live` | `Long` | `35.15` | 113,530,000.00 USD | 0.00 USD | 580.33 USD | `-63.85%` | `16.51` |
| `Live` | `Long` | `35.35` | 113,530,000.00 USD | 0.00 USD | 9,280.00 USD | `-63.65%` | `262.64` |
| `Live` | `Long` | `35.45` | 113,520,000.00 USD | 0.00 USD | 2,570.00 USD | `-63.54%` | `72.60` |
| `Live` | `Long` | `35.55` | 113,510,000.00 USD | 0.00 USD | 39,390.00 USD | `-63.44%` | `1,108.13` |
| `Live` | `Long` | `35.75` | 113,470,000.00 USD | 0.00 USD | 7,370.00 USD | `-63.24%` | `206.10` |
| `Live` | `Long` | `35.85` | 113,470,000.00 USD | 0.00 USD | 2,940.00 USD | `-63.13%` | `82.13` |
| `Live` | `Long` | `35.95` | 113,460,000.00 USD | 0.00 USD | 48,880.00 USD | `-63.03%` | `1,359.71` |
| `Live` | `Long` | `36.05` | 113,420,000.00 USD | 0.00 USD | 6,340.00 USD | `-62.93%` | `175.99` |
| `Live` | `Long` | `36.15` | 113,410,000.00 USD | 0.00 USD | 951.47 USD | `-62.82%` | `26.32` |
| `Live` | `Long` | `36.25` | 113,410,000.00 USD | 0.00 USD | 397,000.00 USD | `-62.72%` | `10,951.59` |
| `Live` | `Long` | `36.35` | 113,010,000.00 USD | 0.00 USD | 5,300.00 USD | `-62.62%` | `145.85` |
| `Live` | `Long` | `36.45` | 113,010,000.00 USD | 0.00 USD | 4,650.00 USD | `-62.52%` | `127.68` |
| `Live` | `Long` | `36.75` | 113,000,000.00 USD | 0.00 USD | 500.90 USD | `-62.21%` | `13.63` |
| `Live` | `Long` | `36.85` | 113,000,000.00 USD | 0.00 USD | 248.74 USD | `-62.10%` | `6.75` |
| `Live` | `Long` | `36.95` | 113,000,000.00 USD | 0.00 USD | 1,660.00 USD | `-62.00%` | `45.00` |
| `Live` | `Long` | `37.15` | 113,000,000.00 USD | 0.00 USD | 39,090.00 USD | `-61.80%` | `1,052.17` |
| `Live` | `Long` | `37.25` | 112,960,000.00 USD | 0.00 USD | 373.62 USD | `-61.69%` | `10.03` |
| `Live` | `Long` | `37.35` | 112,960,000.00 USD | 0.00 USD | 19,820.00 USD | `-61.59%` | `530.70` |
| `Live` | `Long` | `37.45` | 112,940,000.00 USD | 0.00 USD | 987.18 USD | `-61.49%` | `26.36` |
| `Live` | `Long` | `37.55` | 112,940,000.00 USD | 0.00 USD | 262.85 USD | `-61.38%` | `7.00` |
| `Live` | `Long` | `37.65` | 112,940,000.00 USD | 0.00 USD | 2,770.00 USD | `-61.28%` | `73.54` |
| `Live` | `Long` | `37.95` | 112,940,000.00 USD | 0.00 USD | 4,160.00 USD | `-60.97%` | `109.49` |
| `Live` | `Long` | `38.05` | 112,930,000.00 USD | 0.00 USD | 542.59 USD | `-60.87%` | `14.26` |
| `Live` | `Long` | `38.15` | 112,930,000.00 USD | 0.00 USD | 191,700.00 USD | `-60.77%` | `5,025.00` |
| `Live` | `Long` | `38.25` | 112,740,000.00 USD | 0.00 USD | 3,210.00 USD | `-60.66%` | `84.00` |
| `Live` | `Long` | `38.35` | 112,740,000.00 USD | 0.00 USD | 477.84 USD | `-60.56%` | `12.46` |
| `Live` | `Long` | `38.45` | 112,740,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.46%` | `78,049.45` |
| `Live` | `Long` | `38.55` | 109,730,000.00 USD | 0.00 USD | 15,940.00 USD | `-60.36%` | `413.53` |
| `Live` | `Long` | `38.65` | 109,720,000.00 USD | 0.00 USD | 984.42 USD | `-60.25%` | `25.47` |
| `Live` | `Long` | `38.75` | 109,720,000.00 USD | 0.00 USD | 736.64 USD | `-60.15%` | `19.01` |
| `Live` | `Long` | `38.85` | 109,720,000.00 USD | 0.00 USD | 4,270.00 USD | `-60.05%` | `109.96` |
| `Live` | `Long` | `38.95` | 109,710,000.00 USD | 0.00 USD | 5,550.00 USD | `-59.94%` | `142.40` |
| `Live` | `Long` | `39.05` | 109,710,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.84%` | `1,292.50` |
| `Live` | `Long` | `39.15` | 109,660,000.00 USD | 0.00 USD | 882,650.00 USD | `-59.74%` | `22,545.24` |
| `Live` | `Long` | `39.25` | 108,770,000.00 USD | 0.00 USD | 3,580.00 USD | `-59.64%` | `91.16` |
| `Live` | `Long` | `39.35` | 108,770,000.00 USD | 0.00 USD | 3,640.00 USD | `-59.53%` | `92.49` |
| `Live` | `Long` | `39.45` | 108,770,000.00 USD | 0.00 USD | 258.40 USD | `-59.43%` | `6.55` |
| `Live` | `Long` | `39.65` | 108,770,000.00 USD | 0.00 USD | 1,560.00 USD | `-59.23%` | `39.31` |
| `Live` | `Long` | `39.75` | 108,760,000.00 USD | 0.00 USD | 12,080.00 USD | `-59.12%` | `304.00` |
| `Live` | `Long` | `39.85` | 108,750,000.00 USD | 0.00 USD | 1,270.00 USD | `-59.02%` | `31.86` |
| `Live` | `Long` | `39.95` | 108,750,000.00 USD | 0.00 USD | 599.25 USD | `-58.92%` | `15.00` |
| `Live` | `Long` | `40.05` | 108,750,000.00 USD | 0.00 USD | 12,450.00 USD | `-58.81%` | `310.89` |
| `Live` | `Long` | `40.15` | 108,740,000.00 USD | 0.00 USD | 2,510.00 USD | `-58.71%` | `62.48` |
| `Live` | `Long` | `40.25` | 108,740,000.00 USD | 0.00 USD | 632.73 USD | `-58.61%` | `15.72` |
| `Live` | `Long` | `40.55` | 108,730,000.00 USD | 0.00 USD | 12,720.00 USD | `-58.30%` | `313.61` |
| `Live` | `Long` | `40.85` | 108,720,000.00 USD | 0.00 USD | 2,770.00 USD | `-57.99%` | `67.92` |
| `Live` | `Long` | `40.95` | 108,720,000.00 USD | 0.00 USD | 142.10 USD | `-57.89%` | `3.47` |
| `Live` | `Long` | `41.05` | 108,720,000.00 USD | 0.00 USD | 6,650.00 USD | `-57.79%` | `162.05` |
| `Live` | `Long` | `41.15` | 108,710,000.00 USD | 0.00 USD | 3,070.00 USD | `-57.68%` | `74.72` |
| `Live` | `Long` | `41.25` | 108,710,000.00 USD | 0.00 USD | 368.36 USD | `-57.58%` | `8.93` |
| `Live` | `Long` | `41.35` | 108,710,000.00 USD | 0.00 USD | 251.82 USD | `-57.48%` | `6.09` |
| `Live` | `Long` | `41.45` | 108,710,000.00 USD | 0.00 USD | 19,430.00 USD | `-57.37%` | `468.86` |
| `Live` | `Long` | `41.55` | 108,690,000.00 USD | 0.00 USD | 576.71 USD | `-57.27%` | `13.88` |
| `Live` | `Long` | `41.65` | 108,690,000.00 USD | 0.00 USD | 59,950.00 USD | `-57.17%` | `1,439.37` |
| `Live` | `Long` | `41.75` | 108,630,000.00 USD | 0.00 USD | 2,160.00 USD | `-57.07%` | `51.71` |
| `Live` | `Long` | `41.85` | 108,630,000.00 USD | 0.00 USD | 1,020.00 USD | `-56.96%` | `24.39` |
| `Live` | `Long` | `41.95` | 108,630,000.00 USD | 0.00 USD | 48,400.00 USD | `-56.86%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 108,580,000.00 USD | 0.00 USD | 213.61 USD | `-56.76%` | `5.08` |
| `Live` | `Long` | `42.15` | 108,580,000.00 USD | 0.00 USD | 8,930.00 USD | `-56.65%` | `211.93` |
| `Live` | `Long` | `42.25` | 108,570,000.00 USD | 0.00 USD | 146.19 USD | `-56.55%` | `3.46` |
| `Live` | `Long` | `42.35` | 108,570,000.00 USD | 0.00 USD | 8,370.00 USD | `-56.45%` | `197.69` |
| `Live` | `Long` | `42.45` | 108,560,000.00 USD | 0.00 USD | 302.67 USD | `-56.35%` | `7.13` |
| `Live` | `Long` | `42.85` | 108,560,000.00 USD | 0.00 USD | 44,250.00 USD | `-55.93%` | `1,032.68` |
| `Live` | `Long` | `43.15` | 108,520,000.00 USD | 0.00 USD | 9,810.00 USD | `-55.63%` | `227.28` |
| `Live` | `Long` | `43.25` | 108,510,000.00 USD | 0.00 USD | 1,440.00 USD | `-55.52%` | `33.27` |
| `Live` | `Long` | `43.35` | 108,500,000.00 USD | 0.00 USD | 4,980.00 USD | `-55.42%` | `114.90` |
| `Live` | `Long` | `43.45` | 108,500,000.00 USD | 0.00 USD | 570.93 USD | `-55.32%` | `13.14` |
| `Live` | `Long` | `43.55` | 108,500,000.00 USD | 0.00 USD | 1,080.00 USD | `-55.21%` | `24.79` |
| `Live` | `Long` | `43.65` | 108,500,000.00 USD | 0.00 USD | 512.45 USD | `-55.11%` | `11.74` |
| `Live` | `Long` | `43.75` | 108,500,000.00 USD | 0.00 USD | 68,830.00 USD | `-55.01%` | `1,573.15` |
| `Live` | `Long` | `43.85` | 108,430,000.00 USD | 0.00 USD | 106.56 USD | `-54.91%` | `2.43` |
| `Live` | `Long` | `43.95` | 108,430,000.00 USD | 0.00 USD | 242.16 USD | `-54.80%` | `5.51` |
| `Live` | `Long` | `44.05` | 108,430,000.00 USD | 0.00 USD | 11,220.00 USD | `-54.70%` | `254.69` |
| `Live` | `Long` | `44.25` | 108,420,000.00 USD | 0.00 USD | 6,550.00 USD | `-54.49%` | `148.09` |
| `Live` | `Long` | `44.35` | 108,410,000.00 USD | 0.00 USD | 2,910.00 USD | `-54.39%` | `65.68` |
| `Live` | `Long` | `44.45` | 108,410,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-54.29%` | `25,368.72` |
| `Live` | `Long` | `44.55` | 107,280,000.00 USD | 0.00 USD | 18,310.00 USD | `-54.19%` | `410.93` |
| `Live` | `Long` | `44.65` | 107,260,000.00 USD | 0.00 USD | 25,520.00 USD | `-54.08%` | `571.46` |
| `Live` | `Long` | `44.75` | 107,240,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.98%` | `39.98` |
| `Live` | `Long` | `44.85` | 107,230,000.00 USD | 0.00 USD | 711,130.00 USD | `-53.88%` | `15,855.72` |
| `Live` | `Long` | `44.95` | 106,520,000.00 USD | 0.00 USD | 6,510.00 USD | `-53.77%` | `144.85` |
| `Live` | `Long` | `45.05` | 106,520,000.00 USD | 0.00 USD | 9,620.00 USD | `-53.67%` | `213.65` |
| `Live` | `Long` | `45.15` | 106,510,000.00 USD | 0.00 USD | 179.70 USD | `-53.57%` | `3.98` |
| `Live` | `Long` | `45.35` | 106,510,000.00 USD | 0.00 USD | 31,200.00 USD | `-53.36%` | `688.07` |
| `Live` | `Long` | `45.45` | 106,480,000.00 USD | 0.00 USD | 9,480.00 USD | `-53.26%` | `208.64` |
| `Live` | `Long` | `45.55` | 106,470,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.16%` | `174.26` |
| `Live` | `Long` | `45.65` | 106,460,000.00 USD | 0.00 USD | 319.09 USD | `-53.05%` | `6.99` |
| `Live` | `Long` | `45.75` | 106,460,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.95%` | `206.46` |
| `Live` | `Long` | `45.85` | 106,450,000.00 USD | 0.00 USD | 458.50 USD | `-52.85%` | `10.00` |
| `Live` | `Long` | `45.95` | 106,450,000.00 USD | 0.00 USD | 26,070.00 USD | `-52.75%` | `567.34` |
| `Live` | `Long` | `46.05` | 106,420,000.00 USD | 0.00 USD | 3,770,000.00 USD | `-52.64%` | `81,857.90` |
| `Live` | `Long` | `46.45` | 102,650,000.00 USD | 0.00 USD | 730.66 USD | `-52.23%` | `15.73` |
| `Live` | `Long` | `46.55` | 102,650,000.00 USD | 0.00 USD | 522.76 USD | `-52.13%` | `11.23` |
| `Live` | `Long` | `46.65` | 102,650,000.00 USD | 0.00 USD | 542.07 USD | `-52.03%` | `11.62` |
| `Live` | `Long` | `46.75` | 102,650,000.00 USD | 0.00 USD | 10,430.00 USD | `-51.92%` | `223.05` |
| `Live` | `Long` | `46.85` | 102,640,000.00 USD | 0.00 USD | 140.55 USD | `-51.82%` | `3.00` |
| `Live` | `Long` | `46.95` | 102,640,000.00 USD | 0.00 USD | 2,090.00 USD | `-51.72%` | `44.48` |
| `Live` | `Long` | `47.05` | 102,640,000.00 USD | 0.00 USD | 2,820.00 USD | `-51.62%` | `59.88` |
| `Live` | `Long` | `47.15` | 102,630,000.00 USD | 0.00 USD | 1,430.00 USD | `-51.51%` | `30.31` |
| `Live` | `Long` | `47.25` | 102,630,000.00 USD | 0.00 USD | 5,430.00 USD | `-51.41%` | `114.90` |
| `Live` | `Long` | `47.35` | 102,630,000.00 USD | 0.00 USD | 165.73 USD | `-51.31%` | `3.50` |
| `Live` | `Long` | `47.45` | 102,630,000.00 USD | 0.00 USD | 1,940.00 USD | `-51.20%` | `40.89` |
| `Live` | `Long` | `47.55` | 102,630,000.00 USD | 0.00 USD | 745,160.00 USD | `-51.10%` | `15,671.18` |
| `Live` | `Long` | `47.65` | 101,880,000.00 USD | 0.00 USD | 103,540.00 USD | `-51.00%` | `2,173.02` |
| `Live` | `Long` | `47.75` | 101,780,000.00 USD | 0.00 USD | 58,180.00 USD | `-50.90%` | `1,218.40` |
| `Live` | `Long` | `48.05` | 101,720,000.00 USD | 0.00 USD | 13,300.00 USD | `-50.59%` | `276.89` |
| `Live` | `Long` | `48.15` | 101,710,000.00 USD | 0.00 USD | 5,970.00 USD | `-50.48%` | `124.07` |
| `Live` | `Long` | `48.25` | 101,700,000.00 USD | 0.00 USD | 2,430.00 USD | `-50.38%` | `50.45` |
| `Live` | `Long` | `48.35` | 101,700,000.00 USD | 0.00 USD | 5,280.00 USD | `-50.28%` | `109.21` |
| `Live` | `Long` | `48.45` | 101,690,000.00 USD | 0.00 USD | 2,930.00 USD | `-50.18%` | `60.44` |
| `Live` | `Long` | `48.55` | 101,690,000.00 USD | 0.00 USD | 97,250.00 USD | `-50.07%` | `2,003.13` |
| `Live` | `Long` | `48.65` | 101,590,000.00 USD | 0.00 USD | 9,370.00 USD | `-49.97%` | `192.52` |
| `Live` | `Long` | `48.75` | 101,580,000.00 USD | 0.00 USD | 30,920.00 USD | `-49.87%` | `634.29` |
| `Live` | `Long` | `48.85` | 101,550,000.00 USD | 0.00 USD | 15,720.00 USD | `-49.76%` | `321.74` |
| `Live` | `Long` | `48.95` | 101,540,000.00 USD | 0.00 USD | 1,840.00 USD | `-49.66%` | `37.60` |
| `Live` | `Long` | `49.05` | 101,530,000.00 USD | 0.00 USD | 8,510.00 USD | `-49.56%` | `173.52` |
| `Live` | `Long` | `49.15` | 101,530,000.00 USD | 0.00 USD | 276.22 USD | `-49.46%` | `5.62` |
| `Live` | `Long` | `49.25` | 101,520,000.00 USD | 0.00 USD | 21,700.00 USD | `-49.35%` | `440.62` |
| `Live` | `Long` | `49.35` | 101,500,000.00 USD | 0.00 USD | 888.30 USD | `-49.25%` | `18.00` |
| `Live` | `Long` | `49.45` | 101,500,000.00 USD | 0.00 USD | 17,180.00 USD | `-49.15%` | `347.38` |
| `Live` | `Long` | `49.55` | 101,490,000.00 USD | 0.00 USD | 2,870.00 USD | `-49.04%` | `57.92` |
| `Live` | `Long` | `49.65` | 101,480,000.00 USD | 0.00 USD | 8,890.00 USD | `-48.94%` | `179.12` |
| `Live` | `Long` | `49.75` | 101,470,000.00 USD | 0.00 USD | 100.50 USD | `-48.84%` | `2.02` |
| `Live` | `Long` | `49.85` | 101,470,000.00 USD | 0.00 USD | 41,900.00 USD | `-48.74%` | `840.48` |
| `Live` | `Long` | `49.95` | 101,430,000.00 USD | 0.00 USD | 24,170.00 USD | `-48.63%` | `483.82` |
| `Live` | `Long` | `50.05` | 101,410,000.00 USD | 0.00 USD | 9,450.00 USD | `-48.53%` | `188.80` |
| `Live` | `Long` | `50.15` | 101,400,000.00 USD | 0.00 USD | 1,730.00 USD | `-48.43%` | `34.44` |
| `Live` | `Long` | `50.25` | 101,400,000.00 USD | 0.00 USD | 7,860.00 USD | `-48.32%` | `156.35` |
| `Live` | `Long` | `50.35` | 101,390,000.00 USD | 0.00 USD | 18,190.00 USD | `-48.22%` | `361.23` |
| `Live` | `Long` | `50.45` | 101,370,000.00 USD | 0.00 USD | 4,800.00 USD | `-48.12%` | `95.10` |
| `Live` | `Long` | `50.55` | 101,370,000.00 USD | 0.00 USD | 2,400.00 USD | `-48.02%` | `47.47` |
| `Live` | `Long` | `50.65` | 101,360,000.00 USD | 0.00 USD | 5,570.00 USD | `-47.91%` | `109.94` |
| `Live` | `Long` | `50.75` | 101,360,000.00 USD | 0.00 USD | 41,900.00 USD | `-47.81%` | `825.71` |
| `Live` | `Long` | `50.85` | 101,320,000.00 USD | 0.00 USD | 27,930.00 USD | `-47.71%` | `549.35` |
| `Live` | `Long` | `50.95` | 101,290,000.00 USD | 0.00 USD | 5,110.00 USD | `-47.60%` | `100.23` |
| `Live` | `Long` | `51.05` | 101,280,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-47.50%` | `24,062.21` |
| `Live` | `Long` | `51.15` | 100,050,000.00 USD | 0.00 USD | 2,620.00 USD | `-47.40%` | `51.22` |
| `Live` | `Long` | `51.25` | 100,050,000.00 USD | 0.00 USD | 10,940.00 USD | `-47.30%` | `213.44` |
| `Live` | `Long` | `51.35` | 100,040,000.00 USD | 0.00 USD | 4,280.00 USD | `-47.19%` | `83.40` |
| `Live` | `Long` | `51.45` | 100,040,000.00 USD | 0.00 USD | 3,920.00 USD | `-47.09%` | `76.22` |
| `Live` | `Long` | `51.55` | 100,030,000.00 USD | 0.00 USD | 135,710.00 USD | `-46.99%` | `2,632.56` |
| `Live` | `Long` | `51.65` | 99,900,000.00 USD | 0.00 USD | 9,620.00 USD | `-46.88%` | `186.35` |
| `Live` | `Long` | `51.75` | 99,890,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.78%` | `478.71` |
| `Live` | `Long` | `51.85` | 99,860,000.00 USD | 0.00 USD | 46,110.00 USD | `-46.68%` | `889.34` |
| `Live` | `Long` | `51.95` | 99,820,000.00 USD | 0.00 USD | 470,630.00 USD | `-46.58%` | `9,059.28` |
| `Live` | `Long` | `52.05` | 99,350,000.00 USD | 0.00 USD | 10,410.00 USD | `-46.47%` | `200.00` |
| `Live` | `Long` | `52.15` | 99,330,000.00 USD | 0.00 USD | 117,540.00 USD | `-46.37%` | `2,253.79` |
| `Live` | `Long` | `52.25` | 99,220,000.00 USD | 0.00 USD | 6,220.00 USD | `-46.27%` | `119.09` |
| `Live` | `Long` | `52.35` | 99,210,000.00 USD | 0.00 USD | 2,820.00 USD | `-46.16%` | `53.96` |
| `Live` | `Long` | `52.45` | 99,210,000.00 USD | 0.00 USD | 28,310.00 USD | `-46.06%` | `539.78` |
| `Live` | `Long` | `52.55` | 99,180,000.00 USD | 0.00 USD | 11,110.00 USD | `-45.96%` | `211.45` |
| `Live` | `Long` | `52.65` | 99,170,000.00 USD | 0.00 USD | 2,630.00 USD | `-45.86%` | `50.00` |
| `Live` | `Long` | `52.75` | 99,170,000.00 USD | 0.00 USD | 3,990.00 USD | `-45.75%` | `75.59` |
| `Live` | `Long` | `52.85` | 99,160,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.65%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,150,000.00 USD | 0.00 USD | 2,210.00 USD | `-45.55%` | `41.82` |
| `Live` | `Long` | `53.05` | 99,150,000.00 USD | 0.00 USD | 7,080.00 USD | `-45.44%` | `133.41` |
| `Live` | `Long` | `53.15` | 99,140,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.34%` | `58.53` |
| `Live` | `Long` | `53.25` | 99,140,000.00 USD | 0.00 USD | 24,230.00 USD | `-45.24%` | `455.06` |
| `Live` | `Long` | `53.35` | 99,120,000.00 USD | 0.00 USD | 2,130.00 USD | `-45.14%` | `39.99` |
| `Live` | `Long` | `53.45` | 99,110,000.00 USD | 0.00 USD | 34,000.00 USD | `-45.03%` | `636.19` |
| `Live` | `Long` | `53.55` | 99,080,000.00 USD | 0.00 USD | 44,280.00 USD | `-44.93%` | `826.84` |
| `Live` | `Long` | `53.65` | 99,040,000.00 USD | 0.00 USD | 1,390.00 USD | `-44.83%` | `25.92` |
| `Live` | `Long` | `53.75` | 99,030,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.72%` | `67.00` |
| `Live` | `Long` | `53.85` | 99,030,000.00 USD | 0.00 USD | 19,810.00 USD | `-44.62%` | `367.96` |
| `Live` | `Long` | `53.95` | 99,010,000.00 USD | 0.00 USD | 60,060.00 USD | `-44.52%` | `1,113.22` |
| `Live` | `Long` | `54.05` | 98,950,000.00 USD | 0.00 USD | 3,490.00 USD | `-44.42%` | `64.53` |
| `Live` | `Long` | `54.15` | 98,950,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.31%` | `270.39` |
| `Live` | `Long` | `54.25` | 98,930,000.00 USD | 0.00 USD | 5,360.00 USD | `-44.21%` | `98.83` |
| `Live` | `Long` | `54.35` | 98,930,000.00 USD | 0.00 USD | 15,930.00 USD | `-44.11%` | `293.15` |
| `Live` | `Long` | `54.45` | 98,910,000.00 USD | 0.00 USD | 753.04 USD | `-44.01%` | `13.83` |
| `Live` | `Long` | `54.55` | 98,910,000.00 USD | 0.00 USD | 60,580.00 USD | `-43.90%` | `1,110.45` |
| `Live` | `Long` | `54.65` | 98,850,000.00 USD | 0.00 USD | 2,730.00 USD | `-43.80%` | `49.91` |
| `Live` | `Long` | `54.75` | 98,850,000.00 USD | 0.00 USD | 16,300.00 USD | `-43.70%` | `297.67` |
| `Live` | `Long` | `54.85` | 98,830,000.00 USD | 0.00 USD | 867,810.00 USD | `-43.59%` | `15,821.57` |
| `Live` | `Long` | `54.95` | 97,960,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.49%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 97,820,000.00 USD | 0.00 USD | 1,650.00 USD | `-43.39%` | `30.04` |
| `Live` | `Long` | `55.15` | 97,820,000.00 USD | 0.00 USD | 341.93 USD | `-43.29%` | `6.20` |
| `Live` | `Long` | `55.25` | 97,820,000.00 USD | 0.00 USD | 2,170.00 USD | `-43.18%` | `39.19` |
| `Live` | `Long` | `55.35` | 97,820,000.00 USD | 0.00 USD | 9,920.00 USD | `-43.08%` | `179.16` |
| `Live` | `Long` | `55.45` | 97,810,000.00 USD | 0.00 USD | 157,120.00 USD | `-42.98%` | `2,833.48` |
| `Live` | `Long` | `55.55` | 97,650,000.00 USD | 0.00 USD | 5,090.00 USD | `-42.87%` | `91.69` |
| `Live` | `Long` | `55.65` | 97,640,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.77%` | `206.41` |
| `Live` | `Long` | `55.75` | 97,630,000.00 USD | 0.00 USD | 91,560.00 USD | `-42.67%` | `1,642.37` |
| `Live` | `Long` | `55.85` | 97,540,000.00 USD | 0.00 USD | 3,550.00 USD | `-42.57%` | `63.56` |
| `Live` | `Long` | `55.95` | 97,540,000.00 USD | 0.00 USD | 7,050.00 USD | `-42.46%` | `125.95` |
| `Live` | `Long` | `56.05` | 97,530,000.00 USD | 0.00 USD | 5,640.00 USD | `-42.36%` | `100.70` |
| `Live` | `Long` | `56.15` | 97,530,000.00 USD | 0.00 USD | 37,740.00 USD | `-42.26%` | `672.10` |
| `Live` | `Long` | `56.25` | 97,490,000.00 USD | 0.00 USD | 14,990.00 USD | `-42.15%` | `266.52` |
| `Live` | `Long` | `56.35` | 97,470,000.00 USD | 0.00 USD | 12,550.00 USD | `-42.05%` | `222.68` |
| `Live` | `Long` | `56.45` | 97,460,000.00 USD | 0.00 USD | 362,970.00 USD | `-41.95%` | `6,429.97` |
| `Live` | `Long` | `56.55` | 97,100,000.00 USD | 0.00 USD | 4,730.00 USD | `-41.85%` | `83.63` |
| `Live` | `Long` | `56.65` | 97,090,000.00 USD | 0.00 USD | 17,590.00 USD | `-41.74%` | `310.46` |
| `Live` | `Long` | `56.75` | 97,070,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.64%` | `165.87` |
| `Live` | `Long` | `56.85` | 97,070,000.00 USD | 0.00 USD | 4,260.00 USD | `-41.54%` | `74.99` |
| `Live` | `Long` | `56.95` | 97,060,000.00 USD | 0.00 USD | 74,000.00 USD | `-41.43%` | `1,299.41` |
| `Live` | `Long` | `57.05` | 96,990,000.00 USD | 0.00 USD | 2,770,000.00 USD | `-41.33%` | `48,627.98` |
| `Live` | `Long` | `57.15` | 94,210,000.00 USD | 0.00 USD | 5,380.00 USD | `-41.23%` | `94.22` |
| `Live` | `Long` | `57.25` | 94,210,000.00 USD | 0.00 USD | 2,410.00 USD | `-41.13%` | `42.11` |
| `Live` | `Long` | `57.35` | 94,210,000.00 USD | 0.00 USD | 7,120.00 USD | `-41.02%` | `124.09` |
| `Live` | `Long` | `57.45` | 94,200,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.92%` | `334.25` |
| `Live` | `Long` | `57.55` | 94,180,000.00 USD | 0.00 USD | 32,060.00 USD | `-40.82%` | `557.12` |
| `Live` | `Long` | `57.65` | 94,150,000.00 USD | 0.00 USD | 12,790.00 USD | `-40.71%` | `221.85` |
| `Live` | `Long` | `57.75` | 94,130,000.00 USD | 0.00 USD | 3,130.00 USD | `-40.61%` | `54.14` |
| `Live` | `Long` | `57.85` | 94,130,000.00 USD | 0.00 USD | 2,370,000.00 USD | `-40.51%` | `40,888.89` |
| `Live` | `Long` | `57.95` | 91,770,000.00 USD | 0.00 USD | 324.52 USD | `-40.41%` | `5.60` |
| `Live` | `Long` | `58.05` | 91,760,000.00 USD | 0.00 USD | 15,270.00 USD | `-40.30%` | `263.04` |
| `Live` | `Long` | `58.15` | 91,750,000.00 USD | 0.00 USD | 124,360.00 USD | `-40.20%` | `2,138.54` |
| `Live` | `Long` | `58.25` | 91,630,000.00 USD | 0.00 USD | 6,670.00 USD | `-40.10%` | `114.44` |
| `Live` | `Long` | `58.35` | 91,620,000.00 USD | 0.00 USD | 4,670.00 USD | `-39.99%` | `80.09` |
| `Live` | `Long` | `58.45` | 91,610,000.00 USD | 0.00 USD | 463.51 USD | `-39.89%` | `7.93` |
| `Live` | `Long` | `58.55` | 91,610,000.00 USD | 0.00 USD | 44,840.00 USD | `-39.79%` | `765.84` |
| `Live` | `Long` | `58.65` | 91,570,000.00 USD | 0.00 USD | 703.80 USD | `-39.69%` | `12.00` |
| `Live` | `Long` | `58.75` | 91,570,000.00 USD | 0.00 USD | 1,430.00 USD | `-39.58%` | `24.40` |
| `Live` | `Long` | `58.85` | 91,570,000.00 USD | 0.00 USD | 6,130.00 USD | `-39.48%` | `104.08` |
| `Live` | `Long` | `58.95` | 91,560,000.00 USD | 0.00 USD | 51,240.00 USD | `-39.38%` | `869.15` |
| `Live` | `Long` | `59.05` | 91,510,000.00 USD | 0.00 USD | 9,090.00 USD | `-39.27%` | `153.97` |
| `Live` | `Long` | `59.15` | 91,500,000.00 USD | 0.00 USD | 5,000.00 USD | `-39.17%` | `84.52` |
| `Live` | `Long` | `59.25` | 91,500,000.00 USD | 0.00 USD | 34,530.00 USD | `-39.07%` | `582.71` |
| `Live` | `Long` | `59.35` | 91,460,000.00 USD | 0.00 USD | 28,880.00 USD | `-38.97%` | `486.54` |
| `Live` | `Long` | `59.45` | 91,430,000.00 USD | 0.00 USD | 4,390.00 USD | `-38.86%` | `73.76` |
| `Live` | `Long` | `59.55` | 91,430,000.00 USD | 0.00 USD | 8,610.00 USD | `-38.76%` | `144.57` |
| `Live` | `Long` | `59.65` | 91,420,000.00 USD | 0.00 USD | 5,630.00 USD | `-38.66%` | `94.42` |
| `Live` | `Long` | `59.75` | 91,410,000.00 USD | 0.00 USD | 45,900.00 USD | `-38.55%` | `768.15` |
| `Live` | `Long` | `59.85` | 91,370,000.00 USD | 0.00 USD | 28,800.00 USD | `-38.45%` | `481.25` |
| `Live` | `Long` | `59.95` | 91,340,000.00 USD | 0.00 USD | 127,760.00 USD | `-38.35%` | `2,131.17` |
| `Live` | `Long` | `60.05` | 91,210,000.00 USD | 0.00 USD | 19,630.00 USD | `-38.25%` | `326.86` |
| `Live` | `Long` | `60.15` | 91,190,000.00 USD | 0.00 USD | 35,140.00 USD | `-38.14%` | `584.16` |
| `Live` | `Long` | `60.25` | 91,160,000.00 USD | 0.00 USD | 11,410.00 USD | `-38.04%` | `189.35` |
| `Live` | `Long` | `60.35` | 91,140,000.00 USD | 0.00 USD | 24,600.00 USD | `-37.94%` | `407.54` |
| `Live` | `Long` | `60.45` | 91,120,000.00 USD | 0.00 USD | 183.16 USD | `-37.83%` | `3.03` |
| `Live` | `Long` | `60.55` | 91,120,000.00 USD | 0.00 USD | 9,630.00 USD | `-37.73%` | `159.09` |
| `Live` | `Long` | `60.65` | 91,110,000.00 USD | 0.00 USD | 711.42 USD | `-37.63%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,110,000.00 USD | 0.00 USD | 5,590.00 USD | `-37.53%` | `92.02` |
| `Live` | `Long` | `60.85` | 91,100,000.00 USD | 0.00 USD | 28,700.00 USD | `-37.42%` | `471.62` |
| `Live` | `Long` | `60.95` | 91,080,000.00 USD | 0.00 USD | 54,770.00 USD | `-37.32%` | `898.59` |
| `Live` | `Long` | `61.05` | 91,020,000.00 USD | 0.00 USD | 4,850.00 USD | `-37.22%` | `79.50` |
| `Live` | `Long` | `61.15` | 91,020,000.00 USD | 0.00 USD | 4,870.00 USD | `-37.12%` | `79.64` |
| `Live` | `Long` | `61.25` | 91,010,000.00 USD | 0.00 USD | 4,630.00 USD | `-37.01%` | `75.67` |
| `Live` | `Long` | `61.35` | 91,010,000.00 USD | 0.00 USD | 10,170.00 USD | `-36.91%` | `165.83` |
| `Live` | `Long` | `61.45` | 91,000,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.81%` | `340.48` |
| `Live` | `Long` | `61.55` | 90,970,000.00 USD | 0.00 USD | 4,110.00 USD | `-36.70%` | `66.78` |
| `Live` | `Long` | `61.65` | 90,970,000.00 USD | 0.00 USD | 23,350.00 USD | `-36.60%` | `378.68` |
| `Live` | `Long` | `61.75` | 90,950,000.00 USD | 0.00 USD | 50,540.00 USD | `-36.50%` | `818.54` |
| `Live` | `Long` | `61.85` | 90,900,000.00 USD | 0.00 USD | 7,260.00 USD | `-36.40%` | `117.33` |
| `Live` | `Long` | `61.95` | 90,890,000.00 USD | 0.00 USD | 50,720.00 USD | `-36.29%` | `818.75` |
| `Live` | `Long` | `62.05` | 90,840,000.00 USD | 0.00 USD | 27,860.00 USD | `-36.19%` | `449.05` |
| `Live` | `Long` | `62.15` | 90,810,000.00 USD | 0.00 USD | 36,150.00 USD | `-36.09%` | `581.72` |
| `Live` | `Long` | `62.25` | 90,770,000.00 USD | 0.00 USD | 1,800.00 USD | `-35.98%` | `28.90` |
| `Live` | `Long` | `62.35` | 90,770,000.00 USD | 0.00 USD | 16,330.00 USD | `-35.88%` | `261.86` |
| `Live` | `Long` | `62.45` | 90,760,000.00 USD | 0.00 USD | 30,200.00 USD | `-35.78%` | `483.58` |
| `Live` | `Long` | `62.55` | 90,730,000.00 USD | 0.00 USD | 134,180.00 USD | `-35.68%` | `2,145.23` |
| `Live` | `Long` | `62.65` | 90,590,000.00 USD | 0.00 USD | 3,950.00 USD | `-35.57%` | `63.01` |
| `Live` | `Long` | `62.75` | 90,590,000.00 USD | 0.00 USD | 3,140.00 USD | `-35.47%` | `49.97` |
| `Live` | `Long` | `62.85` | 90,590,000.00 USD | 0.00 USD | 49,160.00 USD | `-35.37%` | `782.20` |
| `Live` | `Long` | `62.95` | 90,540,000.00 USD | 0.00 USD | 2,990.00 USD | `-35.26%` | `47.46` |
| `Live` | `Long` | `63.05` | 90,530,000.00 USD | 0.00 USD | 30,290.00 USD | `-35.16%` | `480.34` |
| `Live` | `Long` | `63.15` | 90,500,000.00 USD | 0.00 USD | 99,650.00 USD | `-35.06%` | `1,577.92` |
| `Live` | `Long` | `63.25` | 90,400,000.00 USD | 0.00 USD | 16,330.00 USD | `-34.96%` | `258.15` |
| `Live` | `Long` | `63.45` | 90,390,000.00 USD | 0.00 USD | 291.24 USD | `-34.75%` | `4.59` |
| `Live` | `Long` | `63.55` | 90,390,000.00 USD | 0.00 USD | 49,290.00 USD | `-34.65%` | `775.56` |
| `Live` | `Long` | `63.65` | 90,340,000.00 USD | 0.00 USD | 416.27 USD | `-34.54%` | `6.54` |
| `Live` | `Long` | `63.75` | 90,340,000.00 USD | 0.00 USD | 49,820.00 USD | `-34.44%` | `781.54` |
| `Live` | `Long` | `63.85` | 90,290,000.00 USD | 0.00 USD | 132,740.00 USD | `-34.34%` | `2,078.89` |
| `Live` | `Long` | `63.95` | 90,150,000.00 USD | 0.00 USD | 2,280.00 USD | `-34.24%` | `35.70` |
| `Live` | `Long` | `64.15` | 90,150,000.00 USD | 0.00 USD | 1,600.00 USD | `-34.03%` | `25.00` |
| `Live` | `Long` | `64.25` | 90,150,000.00 USD | 0.00 USD | 5,090.00 USD | `-33.93%` | `79.27` |
| `Live` | `Long` | `64.35` | 90,150,000.00 USD | 0.00 USD | 875.16 USD | `-33.82%` | `13.60` |
| `Live` | `Long` | `64.45` | 90,140,000.00 USD | 0.00 USD | 8,210.00 USD | `-33.72%` | `127.36` |
| `Live` | `Long` | `64.55` | 90,140,000.00 USD | 0.00 USD | 721.67 USD | `-33.62%` | `11.18` |
| `Live` | `Long` | `64.65` | 90,140,000.00 USD | 0.00 USD | 1,740.00 USD | `-33.52%` | `26.99` |
| `Live` | `Long` | `64.75` | 90,130,000.00 USD | 0.00 USD | 236.99 USD | `-33.41%` | `3.66` |
| `Live` | `Long` | `64.85` | 90,130,000.00 USD | 0.00 USD | 396.23 USD | `-33.31%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,130,000.00 USD | 0.00 USD | 209.79 USD | `-33.21%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,130,000.00 USD | 0.00 USD | 317,970.00 USD | `-33.10%` | `4,888.02` |
| `Live` | `Long` | `65.15` | 89,810,000.00 USD | 0.00 USD | 25,400.00 USD | `-33.00%` | `389.82` |
| `Live` | `Long` | `65.25` | 89,790,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.90%` | `200.16` |
| `Live` | `Long` | `65.35` | 89,780,000.00 USD | 0.00 USD | 37,840.00 USD | `-32.80%` | `579.07` |
| `Live` | `Long` | `65.45` | 89,740,000.00 USD | 0.00 USD | 3,130.00 USD | `-32.69%` | `47.89` |
| `Live` | `Long` | `65.55` | 89,740,000.00 USD | 0.00 USD | 10,640.00 USD | `-32.59%` | `162.26` |
| `Live` | `Long` | `65.65` | 89,720,000.00 USD | 0.00 USD | 58,050.00 USD | `-32.49%` | `884.16` |
| `Live` | `Long` | `65.75` | 89,670,000.00 USD | 0.00 USD | 5,050.00 USD | `-32.38%` | `76.84` |
| `Live` | `Long` | `65.85` | 89,660,000.00 USD | 0.00 USD | 7,510.00 USD | `-32.28%` | `114.00` |
| `Live` | `Long` | `65.95` | 89,650,000.00 USD | 0.00 USD | 15,550.00 USD | `-32.18%` | `235.72` |
| `Live` | `Long` | `66.05` | 89,640,000.00 USD | 0.00 USD | 4,940.00 USD | `-32.08%` | `74.78` |
| `Live` | `Long` | `66.25` | 89,630,000.00 USD | 0.00 USD | 27,320.00 USD | `-31.87%` | `412.39` |
| `Live` | `Long` | `66.35` | 89,610,000.00 USD | 0.00 USD | 1,750.00 USD | `-31.77%` | `26.35` |
| `Live` | `Long` | `66.45` | 89,600,000.00 USD | 0.00 USD | 66,530.00 USD | `-31.66%` | `1,001.25` |
| `Live` | `Long` | `66.55` | 89,540,000.00 USD | 0.00 USD | 53,740.00 USD | `-31.56%` | `807.44` |
| `Live` | `Long` | `66.65` | 89,480,000.00 USD | 0.00 USD | 13,170.00 USD | `-31.46%` | `197.56` |
| `Live` | `Long` | `66.75` | 89,470,000.00 USD | 0.00 USD | 5,930.00 USD | `-31.36%` | `88.77` |
| `Live` | `Long` | `66.85` | 89,470,000.00 USD | 0.00 USD | 6,380.00 USD | `-31.25%` | `95.40` |
| `Live` | `Long` | `66.95` | 89,460,000.00 USD | 0.00 USD | 937.30 USD | `-31.15%` | `14.00` |
| `Live` | `Long` | `67.05` | 89,460,000.00 USD | 0.00 USD | 46,770.00 USD | `-31.05%` | `697.58` |
| `Live` | `Long` | `67.15` | 89,410,000.00 USD | 0.00 USD | 7,370.00 USD | `-30.94%` | `109.76` |
| `Live` | `Long` | `67.25` | 89,400,000.00 USD | 0.00 USD | 39,700.00 USD | `-30.84%` | `590.33` |
| `Live` | `Long` | `67.35` | 89,360,000.00 USD | 0.00 USD | 1,500.00 USD | `-30.74%` | `22.34` |
| `Live` | `Long` | `67.45` | 89,360,000.00 USD | 0.00 USD | 22,250.00 USD | `-30.64%` | `329.80` |
| `Live` | `Long` | `67.55` | 89,340,000.00 USD | 0.00 USD | 72,610.00 USD | `-30.53%` | `1,074.93` |
| `Live` | `Long` | `67.65` | 89,270,000.00 USD | 0.00 USD | 129,430.00 USD | `-30.43%` | `1,913.17` |
| `Live` | `Long` | `67.75` | 89,140,000.00 USD | 0.00 USD | 12,060.00 USD | `-30.33%` | `177.96` |
| `Live` | `Long` | `67.85` | 89,130,000.00 USD | 0.00 USD | 5,610.00 USD | `-30.22%` | `82.70` |
| `Live` | `Long` | `68.05` | 89,120,000.00 USD | 0.00 USD | 10,180.00 USD | `-30.02%` | `149.62` |
| `Live` | `Long` | `68.15` | 89,110,000.00 USD | 0.00 USD | 37,500,000.00 USD | `-29.92%` | `550,292.43` |
| `Live` | `Long` | `68.25` | 51,610,000.00 USD | 0.00 USD | 13,650.00 USD | `-29.81%` | `199.93` |
| `Live` | `Long` | `68.35` | 51,590,000.00 USD | 0.00 USD | 22,350.00 USD | `-29.71%` | `326.98` |
| `Live` | `Long` | `68.45` | 51,570,000.00 USD | 0.00 USD | 234,800.00 USD | `-29.61%` | `3,430.25` |
| `Live` | `Long` | `68.55` | 51,340,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-29.51%` | `20,049.41` |
| `Live` | `Long` | `68.65` | 49,960,000.00 USD | 0.00 USD | 6,150.00 USD | `-29.40%` | `89.56` |
| `Live` | `Long` | `68.75` | 49,960,000.00 USD | 0.00 USD | 148,710.00 USD | `-29.30%` | `2,163.12` |
| `Live` | `Long` | `68.85` | 49,810,000.00 USD | 0.00 USD | 5,950.00 USD | `-29.20%` | `86.35` |
| `Live` | `Long` | `68.95` | 49,800,000.00 USD | 0.00 USD | 25,810.00 USD | `-29.09%` | `374.37` |
| `Live` | `Long` | `69.05` | 49,780,000.00 USD | 0.00 USD | 1,640.00 USD | `-28.99%` | `23.82` |
| `Live` | `Long` | `69.15` | 49,770,000.00 USD | 0.00 USD | 21,360.00 USD | `-28.89%` | `308.95` |
| `Live` | `Long` | `69.25` | 49,750,000.00 USD | 0.00 USD | 772,430.00 USD | `-28.79%` | `11,154.25` |
| `Live` | `Long` | `69.45` | 48,980,000.00 USD | 0.00 USD | 14,370.00 USD | `-28.58%` | `206.85` |
| `Live` | `Long` | `69.55` | 48,970,000.00 USD | 0.00 USD | 9,430.00 USD | `-28.48%` | `135.62` |
| `Live` | `Long` | `69.65` | 48,960,000.00 USD | 0.00 USD | 12,540,000.00 USD | `-28.37%` | `180,040.77` |
| `Live` | `Long` | `69.75` | 36,420,000.00 USD | 0.00 USD | 212,520.00 USD | `-28.27%` | `3,046.83` |
| `Live` | `Long` | `69.85` | 36,200,000.00 USD | 0.00 USD | 8,470.00 USD | `-28.17%` | `121.19` |
| `Live` | `Long` | `69.95` | 36,200,000.00 USD | 0.00 USD | 8,800.00 USD | `-28.07%` | `125.81` |
| `Live` | `Long` | `70.05` | 36,190,000.00 USD | 0.00 USD | 496,560.00 USD | `-27.96%` | `7,088.66` |
| `Live` | `Long` | `70.15` | 35,690,000.00 USD | 0.00 USD | 10,540.00 USD | `-27.86%` | `150.19` |
| `Live` | `Long` | `70.25` | 35,680,000.00 USD | 0.00 USD | 72,890.00 USD | `-27.76%` | `1,037.54` |
| `Live` | `Long` | `70.35` | 35,610,000.00 USD | 0.00 USD | 2,170,000.00 USD | `-27.65%` | `30,864.61` |
| `Live` | `Long` | `70.45` | 33,440,000.00 USD | 0.00 USD | 132,570.00 USD | `-27.55%` | `1,881.70` |
| `Live` | `Long` | `70.55` | 33,300,000.00 USD | 0.00 USD | 4,770.00 USD | `-27.45%` | `67.67` |
| `Live` | `Long` | `70.65` | 33,300,000.00 USD | 0.00 USD | 46,000.00 USD | `-27.35%` | `651.07` |
| `Live` | `Long` | `70.75` | 33,250,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-27.24%` | `15,176.35` |
| `Live` | `Long` | `70.85` | 32,180,000.00 USD | 0.00 USD | 18,960.00 USD | `-27.14%` | `267.67` |
| `Live` | `Long` | `70.95` | 32,160,000.00 USD | 0.00 USD | 4,890.00 USD | `-27.04%` | `68.89` |
| `Live` | `Long` | `71.05` | 32,160,000.00 USD | 0.00 USD | 37,930.00 USD | `-26.93%` | `533.81` |
| `Live` | `Long` | `71.15` | 32,120,000.00 USD | 0.00 USD | 69,160.00 USD | `-26.83%` | `972.07` |
| `Live` | `Long` | `71.25` | 32,050,000.00 USD | 0.00 USD | 1,610.00 USD | `-26.73%` | `22.59` |
| `Live` | `Long` | `71.35` | 32,050,000.00 USD | 0.00 USD | 18,890.00 USD | `-26.63%` | `264.74` |
| `Live` | `Long` | `71.45` | 32,030,000.00 USD | 0.00 USD | 16,710.00 USD | `-26.52%` | `233.93` |
| `Live` | `Long` | `71.55` | 32,010,000.00 USD | 0.00 USD | 42,800.00 USD | `-26.42%` | `598.14` |
| `Live` | `Long` | `71.65` | 31,970,000.00 USD | 0.00 USD | 2,170.00 USD | `-26.32%` | `30.24` |
| `Live` | `Long` | `71.75` | 31,970,000.00 USD | 0.00 USD | 27,710.00 USD | `-26.21%` | `386.16` |
| `Live` | `Long` | `71.85` | 31,940,000.00 USD | 0.00 USD | 2,130.00 USD | `-26.11%` | `29.71` |
| `Live` | `Long` | `71.95` | 31,940,000.00 USD | 0.00 USD | 14,750.00 USD | `-26.01%` | `205.02` |
| `Live` | `Long` | `72.05` | 31,920,000.00 USD | 0.00 USD | 8,210.00 USD | `-25.91%` | `113.98` |
| `Live` | `Long` | `72.15` | 31,910,000.00 USD | 0.00 USD | 159,200.00 USD | `-25.80%` | `2,206.58` |
| `Live` | `Long` | `72.25` | 31,750,000.00 USD | 0.00 USD | 258,520.00 USD | `-25.70%` | `3,578.20` |
| `Live` | `Long` | `72.35` | 31,500,000.00 USD | 0.00 USD | 29,100.00 USD | `-25.60%` | `402.20` |
| `Live` | `Long` | `72.45` | 31,470,000.00 USD | 0.00 USD | 1,590.00 USD | `-25.49%` | `22.01` |
| `Live` | `Long` | `72.55` | 31,460,000.00 USD | 0.00 USD | 29,400.00 USD | `-25.39%` | `405.19` |
| `Live` | `Long` | `72.65` | 31,440,000.00 USD | 0.00 USD | 33,720.00 USD | `-25.29%` | `464.15` |
| `Live` | `Long` | `72.75` | 31,400,000.00 USD | 0.00 USD | 3,920.00 USD | `-25.19%` | `53.92` |
| `Live` | `Long` | `72.85` | 31,400,000.00 USD | 0.00 USD | 187,310.00 USD | `-25.08%` | `2,571.23` |
| `Live` | `Long` | `72.95` | 31,210,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.98%` | `76.71` |
| `Live` | `Long` | `73.05` | 31,200,000.00 USD | 0.00 USD | 34,330.00 USD | `-24.88%` | `469.92` |
| `Live` | `Long` | `73.15` | 31,170,000.00 USD | 0.00 USD | 16,780.00 USD | `-24.77%` | `229.39` |
| `Live` | `Long` | `73.25` | 31,150,000.00 USD | 0.00 USD | 28,470.00 USD | `-24.67%` | `388.71` |
| `Live` | `Long` | `73.35` | 31,130,000.00 USD | 0.00 USD | 8,830.00 USD | `-24.57%` | `120.42` |
| `Live` | `Long` | `73.45` | 31,120,000.00 USD | 0.00 USD | 5,350.00 USD | `-24.47%` | `72.82` |
| `Live` | `Long` | `73.55` | 31,110,000.00 USD | 0.00 USD | 18,650.00 USD | `-24.36%` | `253.56` |
| `Live` | `Long` | `73.65` | 31,090,000.00 USD | 0.00 USD | 37,850.00 USD | `-24.26%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,050,000.00 USD | 0.00 USD | 70,280.00 USD | `-24.16%` | `952.95` |
| `Live` | `Long` | `73.85` | 30,980,000.00 USD | 0.00 USD | 26,370.00 USD | `-24.05%` | `357.05` |
| `Live` | `Long` | `73.95` | 30,960,000.00 USD | 0.00 USD | 40,040.00 USD | `-23.95%` | `541.40` |
| `Live` | `Long` | `74.05` | 30,920,000.00 USD | 0.00 USD | 33,110.00 USD | `-23.85%` | `447.16` |
| `Live` | `Long` | `74.15` | 30,880,000.00 USD | 0.00 USD | 21,920.00 USD | `-23.75%` | `295.57` |
| `Live` | `Long` | `74.25` | 30,860,000.00 USD | 0.00 USD | 31,090.00 USD | `-23.64%` | `418.75` |
| `Live` | `Long` | `74.35` | 30,830,000.00 USD | 0.00 USD | 25,000.00 USD | `-23.54%` | `336.22` |
| `Live` | `Long` | `74.45` | 30,810,000.00 USD | 0.00 USD | 22,750.00 USD | `-23.44%` | `305.54` |
| `Live` | `Long` | `74.55` | 30,780,000.00 USD | 0.00 USD | 6,540.00 USD | `-23.33%` | `87.73` |
| `Live` | `Long` | `74.65` | 30,780,000.00 USD | 0.00 USD | 1,030.00 USD | `-23.23%` | `13.82` |
| `Live` | `Long` | `74.75` | 30,780,000.00 USD | 0.00 USD | 218,530.00 USD | `-23.13%` | `2,923.47` |
| `Live` | `Long` | `74.85` | 30,560,000.00 USD | 0.00 USD | 37,250.00 USD | `-23.03%` | `497.65` |
| `Live` | `Long` | `74.95` | 30,520,000.00 USD | 0.00 USD | 19,330.00 USD | `-22.92%` | `257.88` |
| `Live` | `Long` | `75.05` | 30,500,000.00 USD | 0.00 USD | 45,730.00 USD | `-22.82%` | `609.34` |
| `Live` | `Long` | `75.25` | 30,460,000.00 USD | 0.00 USD | 56,410.00 USD | `-22.61%` | `749.58` |
| `Live` | `Long` | `75.35` | 30,400,000.00 USD | 0.00 USD | 258,860.00 USD | `-22.51%` | `3,435.37` |
| `Live` | `Long` | `75.45` | 30,140,000.00 USD | 0.00 USD | 33,560.00 USD | `-22.41%` | `444.85` |
| `Live` | `Long` | `75.55` | 30,110,000.00 USD | 0.00 USD | 28,520.00 USD | `-22.31%` | `377.53` |
| `Live` | `Long` | `75.65` | 30,080,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-22.20%` | `21,229.31` |
| `Live` | `Long` | `75.75` | 28,470,000.00 USD | 0.00 USD | 53,510.00 USD | `-22.10%` | `706.36` |
| `Live` | `Long` | `75.85` | 28,420,000.00 USD | 0.00 USD | 2,880.00 USD | `-22.00%` | `37.95` |
| `Live` | `Long` | `75.95` | 28,420,000.00 USD | 0.00 USD | 27,920.00 USD | `-21.90%` | `367.58` |
| `Live` | `Long` | `76.15` | 28,390,000.00 USD | 0.00 USD | 4,370.00 USD | `-21.69%` | `57.43` |
| `Live` | `Long` | `76.25` | 28,380,000.00 USD | 0.00 USD | 6,190.00 USD | `-21.59%` | `81.22` |
| `Live` | `Long` | `76.35` | 28,380,000.00 USD | 0.00 USD | 37,840.00 USD | `-21.48%` | `495.62` |
| `Live` | `Long` | `76.45` | 28,340,000.00 USD | 0.00 USD | 234,960.00 USD | `-21.38%` | `3,073.34` |
| `Live` | `Long` | `76.55` | 28,100,000.00 USD | 0.00 USD | 50,530.00 USD | `-21.28%` | `660.14` |
| `Live` | `Long` | `76.65` | 28,050,000.00 USD | 0.00 USD | 55,910.00 USD | `-21.18%` | `729.36` |
| `Live` | `Long` | `76.75` | 28,000,000.00 USD | 0.00 USD | 5,060.00 USD | `-21.07%` | `65.89` |
| `Live` | `Long` | `76.85` | 27,990,000.00 USD | 0.00 USD | 138,630.00 USD | `-20.97%` | `1,803.84` |
| `Live` | `Long` | `76.95` | 27,850,000.00 USD | 0.00 USD | 29,350.00 USD | `-20.87%` | `381.42` |
| `Live` | `Long` | `77.05` | 27,830,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-20.76%` | `22,588.19` |
| `Live` | `Long` | `77.15` | 26,080,000.00 USD | 0.00 USD | 112,880.00 USD | `-20.66%` | `1,463.08` |
| `Live` | `Long` | `77.25` | 25,970,000.00 USD | 0.00 USD | 25,020.00 USD | `-20.56%` | `323.94` |
| `Live` | `Long` | `77.35` | 25,950,000.00 USD | 0.00 USD | 12,510.00 USD | `-20.46%` | `161.78` |
| `Live` | `Long` | `77.45` | 25,930,000.00 USD | 0.00 USD | 48,500.00 USD | `-20.35%` | `626.25` |
| `Live` | `Long` | `77.55` | 25,890,000.00 USD | 0.00 USD | 14,630.00 USD | `-20.25%` | `188.71` |
| `Live` | `Long` | `77.75` | 25,870,000.00 USD | 0.00 USD | 9,870.00 USD | `-20.04%` | `126.99` |
| `Live` | `Long` | `77.85` | 25,860,000.00 USD | 0.00 USD | 99,970.00 USD | `-19.94%` | `1,284.12` |
| `Live` | `Long` | `77.95` | 25,760,000.00 USD | 0.00 USD | 29,790.00 USD | `-19.84%` | `382.11` |
| `Live` | `Long` | `78.05` | 25,730,000.00 USD | 0.00 USD | 21,520.00 USD | `-19.74%` | `275.71` |
| `Live` | `Long` | `78.15` | 25,710,000.00 USD | 0.00 USD | 64,100.00 USD | `-19.63%` | `820.22` |
| `Live` | `Long` | `78.25` | 25,650,000.00 USD | 0.00 USD | 39,070.00 USD | `-19.53%` | `499.28` |
| `Live` | `Long` | `78.35` | 25,610,000.00 USD | 0.00 USD | 232,820.00 USD | `-19.43%` | `2,971.50` |
| `Live` | `Long` | `78.45` | 25,370,000.00 USD | 0.00 USD | 30,620.00 USD | `-19.32%` | `390.36` |
| `Live` | `Long` | `78.55` | 25,340,000.00 USD | 0.00 USD | 5,740.00 USD | `-19.22%` | `73.09` |
| `Live` | `Long` | `78.65` | 25,340,000.00 USD | 0.00 USD | 32,860.00 USD | `-19.12%` | `417.75` |
| `Live` | `Long` | `78.75` | 25,300,000.00 USD | 0.00 USD | 52,670.00 USD | `-19.02%` | `668.88` |
| `Live` | `Long` | `78.85` | 25,250,000.00 USD | 0.00 USD | 68,300.00 USD | `-18.91%` | `866.23` |
| `Live` | `Long` | `78.95` | 25,180,000.00 USD | 0.00 USD | 17,120.00 USD | `-18.81%` | `216.80` |
| `Live` | `Long` | `79.05` | 25,170,000.00 USD | 0.00 USD | 24,370.00 USD | `-18.71%` | `308.30` |
| `Live` | `Long` | `79.15` | 25,140,000.00 USD | 0.00 USD | 156,040.00 USD | `-18.60%` | `1,971.45` |
| `Live` | `Long` | `79.25` | 24,990,000.00 USD | 0.00 USD | 47,570.00 USD | `-18.50%` | `600.23` |
| `Live` | `Long` | `79.35` | 24,940,000.00 USD | 0.00 USD | 65,100.00 USD | `-18.40%` | `820.45` |
| `Live` | `Long` | `79.45` | 24,870,000.00 USD | 0.00 USD | 9,530.00 USD | `-18.30%` | `120.01` |
| `Live` | `Long` | `79.55` | 24,860,000.00 USD | 0.00 USD | 5,290.00 USD | `-18.19%` | `66.51` |
| `Live` | `Long` | `79.65` | 24,860,000.00 USD | 0.00 USD | 58,360.00 USD | `-18.09%` | `732.68` |
| `Live` | `Long` | `79.75` | 24,800,000.00 USD | 0.00 USD | 16,340.00 USD | `-17.99%` | `204.93` |
| `Live` | `Long` | `79.85` | 24,780,000.00 USD | 0.00 USD | 30,450.00 USD | `-17.88%` | `381.36` |
| `Live` | `Long` | `79.95` | 24,750,000.00 USD | 0.00 USD | 61,370.00 USD | `-17.78%` | `767.64` |
| `Live` | `Long` | `80.05` | 24,690,000.00 USD | 0.00 USD | 12,060.00 USD | `-17.68%` | `150.63` |
| `Live` | `Long` | `80.15` | 24,680,000.00 USD | 0.00 USD | 40,260.00 USD | `-17.58%` | `502.25` |
| `Live` | `Long` | `80.25` | 24,640,000.00 USD | 0.00 USD | 57,660.00 USD | `-17.47%` | `718.54` |
| `Live` | `Long` | `80.35` | 24,580,000.00 USD | 0.00 USD | 104,890.00 USD | `-17.37%` | `1,305.38` |
| `Live` | `Long` | `80.45` | 24,480,000.00 USD | 0.00 USD | 19,710.00 USD | `-17.27%` | `245.01` |
| `Live` | `Long` | `80.55` | 24,460,000.00 USD | 0.00 USD | 40,160.00 USD | `-17.16%` | `498.53` |
| `Live` | `Long` | `80.65` | 24,420,000.00 USD | 0.00 USD | 82,330.00 USD | `-17.06%` | `1,020.84` |
| `Live` | `Long` | `80.75` | 24,340,000.00 USD | 0.00 USD | 40,450.00 USD | `-16.96%` | `500.90` |
| `Live` | `Long` | `80.85` | 24,290,000.00 USD | 0.00 USD | 447,810.00 USD | `-16.86%` | `5,538.82` |
| `Live` | `Long` | `80.95` | 23,850,000.00 USD | 0.00 USD | 10,990.00 USD | `-16.75%` | `135.71` |
| `Live` | `Long` | `81.05` | 23,840,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-16.65%` | `27,457.97` |
| `Live` | `Long` | `81.15` | 21,610,000.00 USD | 0.00 USD | 87,540.00 USD | `-16.55%` | `1,078.71` |
| `Live` | `Long` | `81.25` | 21,520,000.00 USD | 0.00 USD | 62,020.00 USD | `-16.44%` | `763.32` |
| `Live` | `Long` | `81.35` | 21,460,000.00 USD | 0.00 USD | 46,040.00 USD | `-16.34%` | `565.97` |
| `Live` | `Long` | `81.45` | 21,410,000.00 USD | 0.00 USD | 65,900.00 USD | `-16.24%` | `809.11` |
| `Live` | `Long` | `81.55` | 21,350,000.00 USD | 0.00 USD | 144,710.00 USD | `-16.14%` | `1,774.51` |
| `Live` | `Long` | `81.65` | 21,200,000.00 USD | 0.00 USD | 15,000.00 USD | `-16.03%` | `183.66` |
| `Live` | `Long` | `81.75` | 21,190,000.00 USD | 0.00 USD | 18,650.00 USD | `-15.93%` | `228.11` |
| `Live` | `Long` | `81.85` | 21,170,000.00 USD | 0.00 USD | 35,560.00 USD | `-15.83%` | `434.40` |
| `Live` | `Long` | `81.95` | 21,140,000.00 USD | 0.00 USD | 28,980.00 USD | `-15.72%` | `353.69` |
| `Live` | `Long` | `82.05` | 21,110,000.00 USD | 0.00 USD | 117,210.00 USD | `-15.62%` | `1,428.53` |
| `Live` | `Long` | `82.15` | 20,990,000.00 USD | 0.00 USD | 816,770.00 USD | `-15.52%` | `9,942.41` |
| `Live` | `Long` | `82.25` | 20,170,000.00 USD | 0.00 USD | 45,020.00 USD | `-15.42%` | `547.41` |
| `Live` | `Long` | `82.35` | 20,130,000.00 USD | 0.00 USD | 157,760.00 USD | `-15.31%` | `1,915.68` |
| `Live` | `Long` | `82.45` | 19,970,000.00 USD | 0.00 USD | 210,920.00 USD | `-15.21%` | `2,558.16` |
| `Live` | `Long` | `82.55` | 19,760,000.00 USD | 0.00 USD | 24,020.00 USD | `-15.11%` | `290.95` |
| `Live` | `Long` | `82.65` | 19,730,000.00 USD | 0.00 USD | 318,730.00 USD | `-15.00%` | `3,856.38` |
| `Live` | `Long` | `82.75` | 19,420,000.00 USD | 0.00 USD | 7,300.00 USD | `-14.90%` | `88.21` |
| `Live` | `Long` | `82.85` | 19,410,000.00 USD | 0.00 USD | 21,450.00 USD | `-14.80%` | `258.92` |
| `Live` | `Long` | `82.95` | 19,390,000.00 USD | 0.00 USD | 757,820.00 USD | `-14.70%` | `9,135.91` |
| `Live` | `Long` | `83.05` | 18,630,000.00 USD | 0.00 USD | 105,340.00 USD | `-14.59%` | `1,268.40` |
| `Live` | `Long` | `83.15` | 18,520,000.00 USD | 0.00 USD | 99,370.00 USD | `-14.49%` | `1,195.12` |
| `Live` | `Long` | `83.25` | 18,420,000.00 USD | 0.00 USD | 154,480.00 USD | `-14.39%` | `1,855.64` |
| `Live` | `Long` | `83.35` | 18,270,000.00 USD | 0.00 USD | 265,320.00 USD | `-14.29%` | `3,183.16` |
| `Live` | `Long` | `83.45` | 18,000,000.00 USD | 0.00 USD | 226,260.00 USD | `-14.18%` | `2,711.29` |
| `Live` | `Long` | `83.55` | 17,780,000.00 USD | 0.00 USD | 11,130.00 USD | `-14.08%` | `133.25` |
| `Live` | `Long` | `83.65` | 17,770,000.00 USD | 0.00 USD | 444,340.00 USD | `-13.98%` | `5,311.94` |
| `Live` | `Long` | `83.75` | 17,320,000.00 USD | 0.00 USD | 84,820.00 USD | `-13.87%` | `1,012.81` |
| `Live` | `Long` | `83.85` | 17,240,000.00 USD | 0.00 USD | 11,040.00 USD | `-13.77%` | `131.62` |
| `Live` | `Long` | `83.95` | 17,230,000.00 USD | 0.00 USD | 98,980.00 USD | `-13.67%` | `1,178.98` |
| `Live` | `Long` | `84.05` | 17,130,000.00 USD | 0.00 USD | 118,290.00 USD | `-13.57%` | `1,407.41` |
| `Live` | `Long` | `84.15` | 17,010,000.00 USD | 0.00 USD | 74,940.00 USD | `-13.46%` | `890.56` |
| `Live` | `Long` | `84.25` | 16,930,000.00 USD | 0.00 USD | 46,440.00 USD | `-13.36%` | `551.21` |
| `Live` | `Long` | `84.35` | 16,890,000.00 USD | 0.00 USD | 25,180.00 USD | `-13.26%` | `298.47` |
| `Live` | `Long` | `84.45` | 16,860,000.00 USD | 0.00 USD | 85,960.00 USD | `-13.15%` | `1,017.88` |
| `Live` | `Long` | `84.55` | 16,780,000.00 USD | 0.00 USD | 7,850.00 USD | `-13.05%` | `92.80` |
| `Live` | `Long` | `84.65` | 16,770,000.00 USD | 0.00 USD | 101,540.00 USD | `-12.95%` | `1,199.56` |
| `Live` | `Long` | `84.75` | 16,670,000.00 USD | 0.00 USD | 291,660.00 USD | `-12.85%` | `3,441.46` |
| `Live` | `Long` | `84.85` | 16,380,000.00 USD | 0.00 USD | 106,940.00 USD | `-12.74%` | `1,260.36` |
| `Live` | `Long` | `84.95` | 16,270,000.00 USD | 0.00 USD | 617.59 USD | `-12.64%` | `7.27` |
| `Live` | `Long` | `85.05` | 16,270,000.00 USD | 0.00 USD | 27,400.00 USD | `-12.54%` | `322.18` |
| `Live` | `Long` | `85.15` | 16,240,000.00 USD | 0.00 USD | 5,060.00 USD | `-12.43%` | `59.48` |
| `Live` | `Long` | `85.25` | 16,240,000.00 USD | 0.00 USD | 610,150.00 USD | `-12.33%` | `7,157.16` |
| `Live` | `Long` | `85.35` | 15,630,000.00 USD | 0.00 USD | 21,460.00 USD | `-12.23%` | `251.38` |
| `Live` | `Long` | `85.45` | 15,600,000.00 USD | 0.00 USD | 77,940.00 USD | `-12.13%` | `912.17` |
| `Live` | `Long` | `85.55` | 15,530,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-12.02%` | `14,610.81` |
| `Live` | `Long` | `85.65` | 14,280,000.00 USD | 0.00 USD | 44,390.00 USD | `-11.92%` | `518.32` |
| `Live` | `Long` | `85.75` | 14,230,000.00 USD | 0.00 USD | 97,950.00 USD | `-11.82%` | `1,142.26` |
| `Live` | `Long` | `85.85` | 14,130,000.00 USD | 0.00 USD | 82,540.00 USD | `-11.71%` | `961.42` |
| `Live` | `Long` | `85.95` | 14,050,000.00 USD | 0.00 USD | 332,500.00 USD | `-11.61%` | `3,868.56` |
| `Live` | `Long` | `86.05` | 13,720,000.00 USD | 0.00 USD | 138,200.00 USD | `-11.51%` | `1,606.03` |
| `Live` | `Long` | `86.15` | 13,580,000.00 USD | 0.00 USD | 51,580.00 USD | `-11.41%` | `598.73` |
| `Live` | `Long` | `86.25` | 13,530,000.00 USD | 0.00 USD | 52,570.00 USD | `-11.30%` | `609.53` |
| `Live` | `Long` | `86.35` | 13,480,000.00 USD | 0.00 USD | 3,370.00 USD | `-11.20%` | `39.07` |
| `Live` | `Long` | `86.45` | 13,470,000.00 USD | 0.00 USD | 187,940.00 USD | `-11.10%` | `2,174.00` |
| `Live` | `Long` | `86.55` | 13,290,000.00 USD | 0.00 USD | 27,880.00 USD | `-10.99%` | `322.09` |
| `Live` | `Long` | `86.65` | 13,260,000.00 USD | 0.00 USD | 190,730.00 USD | `-10.89%` | `2,201.12` |
| `Live` | `Long` | `86.75` | 13,070,000.00 USD | 0.00 USD | 34,760.00 USD | `-10.79%` | `400.74` |
| `Live` | `Long` | `86.85` | 13,030,000.00 USD | 0.00 USD | 75,910.00 USD | `-10.69%` | `874.00` |
| `Live` | `Long` | `86.95` | 12,960,000.00 USD | 0.00 USD | 152,510.00 USD | `-10.58%` | `1,754.01` |
| `Live` | `Long` | `87.05` | 12,800,000.00 USD | 0.00 USD | 30,400.00 USD | `-10.48%` | `349.18` |
| `Live` | `Long` | `87.15` | 12,770,000.00 USD | 0.00 USD | 4,670.00 USD | `-10.38%` | `53.54` |
| `Live` | `Long` | `87.25` | 12,770,000.00 USD | 0.00 USD | 92,480.00 USD | `-10.27%` | `1,059.91` |
| `Live` | `Long` | `87.35` | 12,680,000.00 USD | 0.00 USD | 72,050.00 USD | `-10.17%` | `824.89` |
| `Live` | `Long` | `87.45` | 12,600,000.00 USD | 0.00 USD | 149,740.00 USD | `-10.07%` | `1,712.27` |
| `Live` | `Long` | `87.55` | 12,450,000.00 USD | 0.00 USD | 136,390.00 USD | `-9.97%` | `1,557.85` |
| `Live` | `Long` | `87.65` | 12,320,000.00 USD | 0.00 USD | 105,660.00 USD | `-9.86%` | `1,205.42` |
| `Live` | `Long` | `87.75` | 12,210,000.00 USD | 0.00 USD | 28,570.00 USD | `-9.76%` | `325.62` |
| `Live` | `Long` | `87.85` | 12,180,000.00 USD | 0.00 USD | 132,500.00 USD | `-9.66%` | `1,508.25` |
| `Live` | `Long` | `87.95` | 12,050,000.00 USD | 0.00 USD | 7,240.00 USD | `-9.55%` | `82.36` |
| `Live` | `Long` | `88.05` | 12,040,000.00 USD | 0.00 USD | 157,170.00 USD | `-9.45%` | `1,785.00` |
| `Live` | `Long` | `88.15` | 11,890,000.00 USD | 0.00 USD | 21,240.00 USD | `-9.35%` | `240.98` |
| `Live` | `Long` | `88.25` | 11,870,000.00 USD | 0.00 USD | 49,430.00 USD | `-9.25%` | `560.10` |
| `Live` | `Long` | `88.35` | 11,820,000.00 USD | 0.00 USD | 29,870.00 USD | `-9.14%` | `338.06` |
| `Live` | `Long` | `88.45` | 11,790,000.00 USD | 0.00 USD | 120,820.00 USD | `-9.04%` | `1,365.96` |
| `Live` | `Long` | `88.55` | 11,670,000.00 USD | 0.00 USD | 293,840.00 USD | `-8.94%` | `3,318.30` |
| `Live` | `Long` | `88.65` | 11,370,000.00 USD | 0.00 USD | 110,320.00 USD | `-8.83%` | `1,244.46` |
| `Live` | `Long` | `88.75` | 11,260,000.00 USD | 0.00 USD | 167,190.00 USD | `-8.73%` | `1,883.78` |
| `Live` | `Long` | `88.85` | 11,090,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-8.63%` | `12,325.18` |
| `Live` | `Long` | `88.95` | 10,000,000.00 USD | 0.00 USD | 35,580.00 USD | `-8.53%` | `399.98` |
| `Live` | `Long` | `89.05` | 9,960,000.00 USD | 0.00 USD | 31,430.00 USD | `-8.42%` | `352.98` |
| `Live` | `Long` | `89.15` | 9,930,000.00 USD | 0.00 USD | 160,380.00 USD | `-8.32%` | `1,798.99` |
| `Live` | `Long` | `89.25` | 9,770,000.00 USD | 0.00 USD | 31,740.00 USD | `-8.22%` | `355.61` |
| `Live` | `Long` | `89.35` | 9,740,000.00 USD | 0.00 USD | 24,970.00 USD | `-8.11%` | `279.47` |
| `Live` | `Long` | `89.45` | 9,720,000.00 USD | 0.00 USD | 533,440.00 USD | `-8.01%` | `5,963.50` |
| `Live` | `Long` | `89.55` | 9,180,000.00 USD | 0.00 USD | 73,400.00 USD | `-7.91%` | `819.61` |
| `Live` | `Long` | `89.65` | 9,110,000.00 USD | 0.00 USD | 13,840.00 USD | `-7.81%` | `154.37` |
| `Live` | `Long` | `89.75` | 9,090,000.00 USD | 0.00 USD | 131,170.00 USD | `-7.70%` | `1,461.47` |
| `Live` | `Long` | `89.85` | 8,960,000.00 USD | 0.00 USD | 71,740.00 USD | `-7.60%` | `798.46` |
| `Live` | `Long` | `89.95` | 8,890,000.00 USD | 0.00 USD | 75,470.00 USD | `-7.50%` | `838.98` |
| `Live` | `Long` | `90.05` | 8,820,000.00 USD | 0.00 USD | 37,810.00 USD | `-7.40%` | `419.93` |
| `Live` | `Long` | `90.15` | 8,780,000.00 USD | 0.00 USD | 60,790.00 USD | `-7.29%` | `674.32` |
| `Live` | `Long` | `90.25` | 8,720,000.00 USD | 0.00 USD | 106,900.00 USD | `-7.19%` | `1,184.54` |
| `Live` | `Long` | `90.35` | 8,610,000.00 USD | 0.00 USD | 63,960.00 USD | `-7.09%` | `707.87` |
| `Live` | `Long` | `90.45` | 8,550,000.00 USD | 0.00 USD | 34,130.00 USD | `-6.98%` | `377.34` |
| `Live` | `Long` | `90.55` | 8,510,000.00 USD | 0.00 USD | 78,250.00 USD | `-6.88%` | `864.15` |
| `Live` | `Long` | `90.65` | 8,430,000.00 USD | 0.00 USD | 116,420.00 USD | `-6.78%` | `1,284.25` |
| `Live` | `Long` | `90.75` | 8,320,000.00 USD | 0.00 USD | 79,020.00 USD | `-6.68%` | `870.71` |
| `Live` | `Long` | `90.85` | 8,240,000.00 USD | 0.00 USD | 73,170.00 USD | `-6.57%` | `805.35` |
| `Live` | `Long` | `90.95` | 8,170,000.00 USD | 0.00 USD | 16,410.00 USD | `-6.47%` | `180.44` |
| `Live` | `Long` | `91.05` | 8,150,000.00 USD | 0.00 USD | 389,160.00 USD | `-6.37%` | `4,274.12` |
| `Live` | `Long` | `91.15` | 7,760,000.00 USD | 0.00 USD | 288,250.00 USD | `-6.26%` | `3,162.34` |
| `Live` | `Long` | `91.25` | 7,470,000.00 USD | 0.00 USD | 29,640.00 USD | `-6.16%` | `324.80` |
| `Live` | `Long` | `91.35` | 7,440,000.00 USD | 0.00 USD | 30,150.00 USD | `-6.06%` | `330.08` |
| `Live` | `Long` | `91.45` | 7,410,000.00 USD | 0.00 USD | 350,660.00 USD | `-5.96%` | `3,834.40` |
| `Live` | `Long` | `91.55` | 7,060,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-5.85%` | `13,204.29` |
| `Live` | `Long` | `91.65` | 5,850,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-5.75%` | `15,594.68` |
| `Live` | `Long` | `91.75` | 4,420,000.00 USD | 0.00 USD | 237,680.00 USD | `-5.65%` | `2,590.54` |
| `Live` | `Long` | `91.85` | 4,190,000.00 USD | 0.00 USD | 32,760.00 USD | `-5.54%` | `356.67` |
| `Live` | `Long` | `91.95` | 4,150,000.00 USD | 0.00 USD | 161,120.00 USD | `-5.44%` | `1,752.27` |
| `Live` | `Long` | `92.05` | 3,990,000.00 USD | 0.00 USD | 75,600.00 USD | `-5.34%` | `821.30` |
| `Live` | `Long` | `92.15` | 3,920,000.00 USD | 0.00 USD | 324,120.00 USD | `-5.24%` | `3,517.35` |
| `Live` | `Long` | `92.25` | 3,590,000.00 USD | 0.00 USD | 234,300.00 USD | `-5.13%` | `2,539.82` |
| `Live` | `Long` | `92.35` | 3,360,000.00 USD | 0.00 USD | 371,010.00 USD | `-5.03%` | `4,017.44` |
| `Live` | `Long` | `92.45` | 2,990,000.00 USD | 0.00 USD | 83,740.00 USD | `-4.93%` | `905.79` |
| `Live` | `Long` | `92.55` | 2,900,000.00 USD | 0.00 USD | 4,870.00 USD | `-4.82%` | `52.65` |
| `Live` | `Long` | `92.65` | 2,900,000.00 USD | 0.00 USD | 14,980.00 USD | `-4.72%` | `161.63` |
| `Live` | `Long` | `92.75` | 2,880,000.00 USD | 0.00 USD | 2,250.00 USD | `-4.62%` | `24.21` |
| `Live` | `Long` | `92.85` | 2,880,000.00 USD | 0.00 USD | 16,750.00 USD | `-4.52%` | `180.44` |
| `Live` | `Long` | `92.95` | 2,860,000.00 USD | 0.00 USD | 688,830.00 USD | `-4.41%` | `7,410.75` |
| `Live` | `Long` | `93.05` | 2,180,000.00 USD | 0.00 USD | 29,940.00 USD | `-4.31%` | `321.71` |
| `Live` | `Long` | `93.15` | 2,150,000.00 USD | 0.00 USD | 29,150.00 USD | `-4.21%` | `312.91` |
| `Live` | `Long` | `93.25` | 2,120,000.00 USD | 0.00 USD | 40,160.00 USD | `-4.10%` | `430.62` |
| `Live` | `Long` | `93.35` | 2,080,000.00 USD | 0.00 USD | 10,780.00 USD | `-4.00%` | `115.49` |
| `Live` | `Long` | `93.45` | 2,070,000.00 USD | 0.00 USD | 8,530.00 USD | `-3.90%` | `91.26` |
| `Live` | `Long` | `93.55` | 2,060,000.00 USD | 0.00 USD | 205.81 USD | `-3.80%` | `2.20` |
| `Live` | `Long` | `93.65` | 2,060,000.00 USD | 0.00 USD | 3,240.00 USD | `-3.69%` | `34.59` |
| `Live` | `Long` | `93.75` | 2,050,000.00 USD | 0.00 USD | 21,700.00 USD | `-3.59%` | `231.49` |
| `Live` | `Long` | `93.85` | 2,030,000.00 USD | 0.00 USD | 16,380.00 USD | `-3.49%` | `174.51` |
| `Live` | `Long` | `93.95` | 2,020,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-3.38%` | `12,663.99` |
| `Live` | `Long` | `94.05` | 825,280.00 USD | 0.00 USD | 8,980.00 USD | `-3.28%` | `95.46` |
| `Live` | `Long` | `94.15` | 816,300.00 USD | 0.00 USD | 29,670.00 USD | `-3.18%` | `315.12` |
| `Live` | `Long` | `94.25` | 786,640.00 USD | 0.00 USD | 14,820.00 USD | `-3.08%` | `157.22` |
| `Live` | `Long` | `94.35` | 771,820.00 USD | 0.00 USD | 13,000.00 USD | `-2.97%` | `137.79` |
| `Live` | `Long` | `94.45` | 758,820.00 USD | 0.00 USD | 185,300.00 USD | `-2.87%` | `1,961.92` |
| `Live` | `Long` | `94.55` | 573,510.00 USD | 0.00 USD | 141,190.00 USD | `-2.77%` | `1,493.29` |
| `Live` | `Long` | `94.65` | 432,320.00 USD | 0.00 USD | 37,940.00 USD | `-2.66%` | `400.82` |
| `Live` | `Long` | `94.75` | 394,390.00 USD | 0.00 USD | 45,890.00 USD | `-2.56%` | `484.29` |
| `Live` | `Long` | `94.85` | 348,500.00 USD | 0.00 USD | 32,160.00 USD | `-2.46%` | `339.09` |
| `Live` | `Long` | `94.95` | 316,340.00 USD | 0.00 USD | 28,900.00 USD | `-2.36%` | `304.37` |
| `Live` | `Long` | `95.05` | 287,440.00 USD | 0.00 USD | 59,310.00 USD | `-2.25%` | `623.97` |
| `Live` | `Long` | `95.15` | 228,130.00 USD | 0.00 USD | 20,810.00 USD | `-2.15%` | `218.71` |
| `Live` | `Long` | `95.25` | 207,320.00 USD | 0.00 USD | 42,330.00 USD | `-2.05%` | `444.46` |
| `Live` | `Long` | `95.35` | 164,980.00 USD | 0.00 USD | 6,050.00 USD | `-1.94%` | `63.42` |
| `Live` | `Long` | `95.45` | 158,940.00 USD | 0.00 USD | 8,540.00 USD | `-1.84%` | `89.47` |
| `Live` | `Long` | `95.55` | 150,400.00 USD | 0.00 USD | 33,150.00 USD | `-1.74%` | `346.89` |
| `Live` | `Long` | `95.65` | 117,250.00 USD | 0.00 USD | 37,490.00 USD | `-1.64%` | `391.99` |
| `Live` | `Long` | `95.75` | 79,760.00 USD | 0.00 USD | 44,730.00 USD | `-1.53%` | `467.15` |
| `Live` | `Long` | `95.85` | 35,030.00 USD | 0.00 USD | 34,800.00 USD | `-1.43%` | `363.02` |
| `Live` | `Long` | `95.95` | 231.24 USD | 0.00 USD | 231.24 USD | `-1.33%` | `2.41` |
| `Live` | `Short` | `98.55` | 23,180.00 USD | 23,180.00 USD | 0.00 USD | `+1.35%` | `235.20` |
| `Live` | `Short` | `98.65` | 26,030.00 USD | 2,850.00 USD | 0.00 USD | `+1.45%` | `28.90` |
| `Live` | `Short` | `98.75` | 36,290.00 USD | 10,260.00 USD | 0.00 USD | `+1.55%` | `103.94` |
| `Live` | `Short` | `98.95` | 45,070.00 USD | 8,770.00 USD | 0.00 USD | `+1.76%` | `88.65` |
| `Live` | `Short` | `99.05` | 87,700.00 USD | 42,640.00 USD | 0.00 USD | `+1.86%` | `430.46` |
| `Live` | `Short` | `99.15` | 1,230,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+1.96%` | `11,483.10` |
| `Live` | `Short` | `99.25` | 1,280,000.00 USD | 50,940.00 USD | 0.00 USD | `+2.07%` | `513.21` |
| `Live` | `Short` | `99.35` | 1,360,000.00 USD | 79,350.00 USD | 0.00 USD | `+2.17%` | `798.68` |
| `Live` | `Short` | `99.45` | 1,360,000.00 USD | 4,360.00 USD | 0.00 USD | `+2.27%` | `43.84` |
| `Live` | `Short` | `99.55` | 1,370,000.00 USD | 12,460.00 USD | 0.00 USD | `+2.37%` | `125.21` |
| `Live` | `Short` | `99.65` | 1,410,000.00 USD | 36,170.00 USD | 0.00 USD | `+2.48%` | `362.97` |
| `Live` | `Short` | `99.75` | 1,440,000.00 USD | 25,510.00 USD | 0.00 USD | `+2.58%` | `255.74` |
| `Live` | `Short` | `99.85` | 1,440,000.00 USD | 4,370.00 USD | 0.00 USD | `+2.68%` | `43.73` |
| `Live` | `Short` | `99.95` | 1,440,000.00 USD | 2,110.00 USD | 0.00 USD | `+2.79%` | `21.11` |
| `Live` | `Short` | `100.05` | 1,490,000.00 USD | 48,480.00 USD | 0.00 USD | `+2.89%` | `484.56` |
| `Live` | `Short` | `100.15` | 1,530,000.00 USD | 44,320.00 USD | 0.00 USD | `+2.99%` | `442.58` |
| `Live` | `Short` | `100.25` | 1,880,000.00 USD | 347,460.00 USD | 0.00 USD | `+3.09%` | `3,465.93` |
| `Live` | `Short` | `100.35` | 2,270,000.00 USD | 391,910.00 USD | 0.00 USD | `+3.20%` | `3,905.45` |
| `Live` | `Short` | `100.45` | 2,280,000.00 USD | 6,010.00 USD | 0.00 USD | `+3.30%` | `59.81` |
| `Live` | `Short` | `100.55` | 2,290,000.00 USD | 13,880.00 USD | 0.00 USD | `+3.40%` | `138.00` |
| `Live` | `Short` | `100.75` | 2,310,000.00 USD | 19,590.00 USD | 0.00 USD | `+3.61%` | `194.44` |
| `Live` | `Short` | `100.85` | 2,310,000.00 USD | 742.26 USD | 0.00 USD | `+3.71%` | `7.36` |
| `Live` | `Short` | `100.95` | 2,330,000.00 USD | 12,270.00 USD | 0.00 USD | `+3.81%` | `121.52` |
| `Live` | `Short` | `101.05` | 2,330,000.00 USD | 698.26 USD | 0.00 USD | `+3.92%` | `6.91` |
| `Live` | `Short` | `101.15` | 2,340,000.00 USD | 12,940.00 USD | 0.00 USD | `+4.02%` | `127.95` |
| `Live` | `Short` | `101.25` | 2,340,000.00 USD | 769.50 USD | 0.00 USD | `+4.12%` | `7.60` |
| `Live` | `Short` | `101.35` | 2,340,000.00 USD | 922.29 USD | 0.00 USD | `+4.23%` | `9.10` |
| `Live` | `Short` | `101.45` | 2,340,000.00 USD | 118.70 USD | 0.00 USD | `+4.33%` | `1.17` |
| `Live` | `Short` | `101.55` | 2,340,000.00 USD | 2,790.00 USD | 0.00 USD | `+4.43%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,350,000.00 USD | 2,640.00 USD | 0.00 USD | `+4.53%` | `26.02` |
| `Live` | `Short` | `101.85` | 2,360,000.00 USD | 13,380.00 USD | 0.00 USD | `+4.74%` | `131.39` |
| `Live` | `Short` | `101.95` | 2,360,000.00 USD | 1,560.00 USD | 0.00 USD | `+4.84%` | `15.31` |
| `Live` | `Short` | `102.05` | 2,370,000.00 USD | 4,710.00 USD | 0.00 USD | `+4.95%` | `46.14` |
| `Live` | `Short` | `102.25` | 2,370,000.00 USD | 1,170.00 USD | 0.00 USD | `+5.15%` | `11.44` |
| `Live` | `Short` | `102.55` | 2,370,000.00 USD | 632.73 USD | 0.00 USD | `+5.46%` | `6.17` |
| `Live` | `Short` | `102.65` | 2,370,000.00 USD | 1,070.00 USD | 0.00 USD | `+5.56%` | `10.45` |
| `Live` | `Short` | `102.75` | 2,370,000.00 USD | 3,340.00 USD | 0.00 USD | `+5.67%` | `32.53` |
| `Live` | `Short` | `102.95` | 2,380,000.00 USD | 4,380.00 USD | 0.00 USD | `+5.87%` | `42.55` |
| `Live` | `Short` | `103.05` | 2,380,000.00 USD | 692.50 USD | 0.00 USD | `+5.97%` | `6.72` |
| `Live` | `Short` | `103.15` | 2,390,000.00 USD | 14,800.00 USD | 0.00 USD | `+6.08%` | `143.46` |
| `Live` | `Short` | `103.25` | 2,390,000.00 USD | 551.36 USD | 0.00 USD | `+6.18%` | `5.34` |
| `Live` | `Short` | `103.35` | 2,400,000.00 USD | 7,370.00 USD | 0.00 USD | `+6.28%` | `71.33` |
| `Live` | `Short` | `103.45` | 2,400,000.00 USD | 3,300.00 USD | 0.00 USD | `+6.39%` | `31.94` |
| `Live` | `Short` | `103.55` | 2,410,000.00 USD | 1,610.00 USD | 0.00 USD | `+6.49%` | `15.59` |
| `Live` | `Short` | `103.65` | 2,420,000.00 USD | 13,760.00 USD | 0.00 USD | `+6.59%` | `132.78` |
| `Live` | `Short` | `103.75` | 2,680,000.00 USD | 261,320.00 USD | 0.00 USD | `+6.69%` | `2,518.70` |
| `Live` | `Short` | `103.85` | 2,700,000.00 USD | 14,630.00 USD | 0.00 USD | `+6.80%` | `140.89` |
| `Live` | `Short` | `103.95` | 2,700,000.00 USD | 1,580.00 USD | 0.00 USD | `+6.90%` | `15.17` |
| `Live` | `Short` | `104.05` | 2,700,000.00 USD | 775.17 USD | 0.00 USD | `+7.00%` | `7.45` |
| `Live` | `Short` | `104.15` | 2,700,000.00 USD | 1,060.00 USD | 0.00 USD | `+7.11%` | `10.20` |
| `Live` | `Short` | `104.25` | 2,700,000.00 USD | 1,240.00 USD | 0.00 USD | `+7.21%` | `11.93` |
| `Live` | `Short` | `104.35` | 2,700,000.00 USD | 3,900.00 USD | 0.00 USD | `+7.31%` | `37.41` |
| `Live` | `Short` | `104.45` | 2,710,000.00 USD | 8,820.00 USD | 0.00 USD | `+7.41%` | `84.42` |
| `Live` | `Short` | `104.55` | 2,710,000.00 USD | 575.03 USD | 0.00 USD | `+7.52%` | `5.50` |
| `Live` | `Short` | `104.65` | 2,710,000.00 USD | 1,140.00 USD | 0.00 USD | `+7.62%` | `10.94` |
| `Live` | `Short` | `104.75` | 2,720,000.00 USD | 3,620.00 USD | 0.00 USD | `+7.72%` | `34.59` |
| `Live` | `Short` | `104.85` | 2,760,000.00 USD | 41,340.00 USD | 0.00 USD | `+7.82%` | `394.26` |
| `Live` | `Short` | `104.95` | 2,890,000.00 USD | 125,660.00 USD | 0.00 USD | `+7.93%` | `1,197.29` |
| `Live` | `Short` | `105.05` | 2,890,000.00 USD | 8,570.00 USD | 0.00 USD | `+8.03%` | `81.59` |
| `Live` | `Short` | `105.15` | 2,910,000.00 USD | 12,590.00 USD | 0.00 USD | `+8.13%` | `119.78` |
| `Live` | `Short` | `105.25` | 2,910,000.00 USD | 2,090.00 USD | 0.00 USD | `+8.24%` | `19.84` |
| `Live` | `Short` | `105.35` | 2,920,000.00 USD | 6,840.00 USD | 0.00 USD | `+8.34%` | `64.89` |
| `Live` | `Short` | `105.45` | 3,450,000.00 USD | 531,450.00 USD | 0.00 USD | `+8.44%` | `5,039.81` |
| `Live` | `Short` | `105.55` | 3,450,000.00 USD | 4,180.00 USD | 0.00 USD | `+8.54%` | `39.61` |
| `Live` | `Short` | `105.65` | 3,450,000.00 USD | 216.58 USD | 0.00 USD | `+8.65%` | `2.05` |
| `Live` | `Short` | `105.85` | 3,540,000.00 USD | 91,620.00 USD | 0.00 USD | `+8.85%` | `865.57` |
| `Live` | `Short` | `105.95` | 3,540,000.00 USD | 592.26 USD | 0.00 USD | `+8.96%` | `5.59` |
| `Live` | `Short` | `106.05` | 3,580,000.00 USD | 33,380.00 USD | 0.00 USD | `+9.06%` | `314.77` |
| `Live` | `Short` | `106.15` | 3,580,000.00 USD | 605.06 USD | 0.00 USD | `+9.16%` | `5.70` |
| `Live` | `Short` | `106.25` | 3,580,000.00 USD | 180.62 USD | 0.00 USD | `+9.26%` | `1.70` |
| `Live` | `Short` | `106.35` | 3,830,000.00 USD | 253,580.00 USD | 0.00 USD | `+9.37%` | `2,384.36` |
| `Live` | `Short` | `106.45` | 4,030,000.00 USD | 198,600.00 USD | 0.00 USD | `+9.47%` | `1,865.68` |
| `Live` | `Short` | `106.55` | 4,030,000.00 USD | 108.68 USD | 0.00 USD | `+9.57%` | `1.02` |
| `Live` | `Short` | `106.65` | 4,050,000.00 USD | 19,750.00 USD | 0.00 USD | `+9.68%` | `185.14` |
| `Live` | `Short` | `106.75` | 4,450,000.00 USD | 397,560.00 USD | 0.00 USD | `+9.78%` | `3,724.17` |
| `Live` | `Short` | `106.85` | 4,930,000.00 USD | 478,970.00 USD | 0.00 USD | `+9.88%` | `4,482.65` |
| `Live` | `Short` | `106.95` | 4,930,000.00 USD | 291.97 USD | 0.00 USD | `+9.98%` | `2.73` |
| `Live` | `Short` | `107.05` | 4,940,000.00 USD | 15,220.00 USD | 0.00 USD | `+10.09%` | `142.16` |
| `Live` | `Short` | `107.15` | 4,940,000.00 USD | 3,060.00 USD | 0.00 USD | `+10.19%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,980,000.00 USD | 34,950.00 USD | 0.00 USD | `+10.29%` | `325.92` |
| `Live` | `Short` | `107.35` | 4,980,000.00 USD | 766.48 USD | 0.00 USD | `+10.40%` | `7.14` |
| `Live` | `Short` | `107.45` | 5,010,000.00 USD | 32,580.00 USD | 0.00 USD | `+10.50%` | `303.18` |
| `Live` | `Short` | `107.55` | 5,010,000.00 USD | 221.55 USD | 0.00 USD | `+10.60%` | `2.06` |
| `Live` | `Short` | `107.85` | 5,160,000.00 USD | 146,260.00 USD | 0.00 USD | `+10.91%` | `1,356.11` |
| `Live` | `Short` | `108.05` | 5,160,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.12%` | `10.04` |
| `Live` | `Short` | `108.15` | 5,160,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.22%` | `10.66` |
| `Live` | `Short` | `108.25` | 5,340,000.00 USD | 179,190.00 USD | 0.00 USD | `+11.32%` | `1,655.31` |
| `Live` | `Short` | `108.35` | 5,340,000.00 USD | 3,470.00 USD | 0.00 USD | `+11.42%` | `32.00` |
| `Live` | `Short` | `108.55` | 5,340,000.00 USD | 261.61 USD | 0.00 USD | `+11.63%` | `2.41` |
| `Live` | `Short` | `108.65` | 5,350,000.00 USD | 5,050.00 USD | 0.00 USD | `+11.73%` | `46.45` |
| `Live` | `Short` | `108.85` | 5,350,000.00 USD | 3,230.00 USD | 0.00 USD | `+11.94%` | `29.68` |
| `Live` | `Short` | `108.95` | 5,360,000.00 USD | 3,170.00 USD | 0.00 USD | `+12.04%` | `29.10` |
| `Live` | `Short` | `109.05` | 9,800,000.00 USD | 4,440,000.00 USD | 0.00 USD | `+12.14%` | `40,718.31` |
| `Live` | `Short` | `109.35` | 9,800,000.00 USD | 1,850.00 USD | 0.00 USD | `+12.45%` | `16.92` |
| `Live` | `Short` | `109.45` | 9,800,000.00 USD | 426.86 USD | 0.00 USD | `+12.56%` | `3.90` |
| `Live` | `Short` | `109.55` | 9,800,000.00 USD | 356.04 USD | 0.00 USD | `+12.66%` | `3.25` |
| `Live` | `Short` | `109.65` | 9,840,000.00 USD | 38,640.00 USD | 0.00 USD | `+12.76%` | `352.40` |
| `Live` | `Short` | `109.85` | 9,840,000.00 USD | 459.17 USD | 0.00 USD | `+12.97%` | `4.18` |
| `Live` | `Short` | `109.95` | 9,840,000.00 USD | 495.87 USD | 0.00 USD | `+13.07%` | `4.51` |
| `Live` | `Short` | `110.05` | 9,850,000.00 USD | 14,790.00 USD | 0.00 USD | `+13.17%` | `134.36` |
| `Live` | `Short` | `110.15` | 9,850,000.00 USD | 194.97 USD | 0.00 USD | `+13.28%` | `1.77` |
| `Live` | `Short` | `110.25` | 9,860,000.00 USD | 2,970.00 USD | 0.00 USD | `+13.38%` | `26.95` |
| `Live` | `Short` | `110.35` | 9,860,000.00 USD | 385.12 USD | 0.00 USD | `+13.48%` | `3.49` |
| `Live` | `Short` | `110.45` | 10,000,000.00 USD | 143,580.00 USD | 0.00 USD | `+13.58%` | `1,299.91` |
| `Live` | `Short` | `110.55` | 10,000,000.00 USD | 203.41 USD | 0.00 USD | `+13.69%` | `1.84` |
| `Live` | `Short` | `110.95` | 10,010,000.00 USD | 4,450.00 USD | 0.00 USD | `+14.10%` | `40.12` |
| `Live` | `Short` | `111.15` | 10,010,000.00 USD | 1,710.00 USD | 0.00 USD | `+14.30%` | `15.37` |
| `Live` | `Short` | `111.35` | 10,010,000.00 USD | 390.84 USD | 0.00 USD | `+14.51%` | `3.51` |
| `Live` | `Short` | `111.45` | 10,010,000.00 USD | 841.45 USD | 0.00 USD | `+14.61%` | `7.55` |
| `Live` | `Short` | `111.75` | 10,010,000.00 USD | 169.86 USD | 0.00 USD | `+14.92%` | `1.52` |
| `Live` | `Short` | `111.85` | 10,020,000.00 USD | 15,880.00 USD | 0.00 USD | `+15.02%` | `141.95` |
| `Live` | `Short` | `111.95` | 10,020,000.00 USD | 223.90 USD | 0.00 USD | `+15.13%` | `2.00` |
| `Live` | `Short` | `112.15` | 10,290,000.00 USD | 260,900.00 USD | 0.00 USD | `+15.33%` | `2,326.32` |
| `Live` | `Short` | `112.35` | 10,290,000.00 USD | 1,910.00 USD | 0.00 USD | `+15.54%` | `17.00` |
| `Live` | `Short` | `112.45` | 10,290,000.00 USD | 5,670.00 USD | 0.00 USD | `+15.64%` | `50.42` |
| `Live` | `Short` | `112.55` | 10,290,000.00 USD | 1,070.00 USD | 0.00 USD | `+15.74%` | `9.55` |
| `Live` | `Short` | `112.65` | 10,290,000.00 USD | 707.44 USD | 0.00 USD | `+15.85%` | `6.28` |
| `Live` | `Short` | `112.75` | 10,430,000.00 USD | 130,940.00 USD | 0.00 USD | `+15.95%` | `1,161.31` |
| `Live` | `Short` | `112.85` | 10,530,000.00 USD | 108,990.00 USD | 0.00 USD | `+16.05%` | `965.83` |
| `Live` | `Short` | `113.05` | 10,540,000.00 USD | 619.51 USD | 0.00 USD | `+16.26%` | `5.48` |
| `Live` | `Short` | `113.15` | 10,550,000.00 USD | 10,030.00 USD | 0.00 USD | `+16.36%` | `88.67` |
| `Live` | `Short` | `113.25` | 10,550,000.00 USD | 698.75 USD | 0.00 USD | `+16.46%` | `6.17` |
| `Live` | `Short` | `113.35` | 10,550,000.00 USD | 4,970.00 USD | 0.00 USD | `+16.57%` | `43.83` |
| `Live` | `Short` | `113.45` | 10,550,000.00 USD | 3,360.00 USD | 0.00 USD | `+16.67%` | `29.62` |
| `Live` | `Short` | `113.55` | 10,570,000.00 USD | 17,470.00 USD | 0.00 USD | `+16.77%` | `153.86` |
| `Live` | `Short` | `113.65` | 10,600,000.00 USD | 31,480.00 USD | 0.00 USD | `+16.87%` | `276.99` |
| `Live` | `Short` | `113.75` | 10,710,000.00 USD | 107,800.00 USD | 0.00 USD | `+16.98%` | `947.67` |
| `Live` | `Short` | `113.85` | 10,710,000.00 USD | 2,370.00 USD | 0.00 USD | `+17.08%` | `20.80` |
| `Live` | `Short` | `113.95` | 10,740,000.00 USD | 21,840.00 USD | 0.00 USD | `+17.18%` | `191.69` |
| `Live` | `Short` | `114.05` | 10,770,000.00 USD | 31,740.00 USD | 0.00 USD | `+17.29%` | `278.26` |
| `Live` | `Short` | `114.25` | 10,770,000.00 USD | 2,150.00 USD | 0.00 USD | `+17.49%` | `18.80` |
| `Live` | `Short` | `114.45` | 10,770,000.00 USD | 3,830.00 USD | 0.00 USD | `+17.70%` | `33.46` |
| `Live` | `Short` | `114.65` | 10,780,000.00 USD | 3,430.00 USD | 0.00 USD | `+17.90%` | `29.93` |
| `Live` | `Short` | `114.95` | 10,780,000.00 USD | 220.70 USD | 0.00 USD | `+18.21%` | `1.92` |
| `Live` | `Short` | `115.05` | 11,350,000.00 USD | 569,550.00 USD | 0.00 USD | `+18.31%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 11,350,000.00 USD | 1,100.00 USD | 0.00 USD | `+18.42%` | `9.52` |
| `Live` | `Short` | `115.25` | 11,350,000.00 USD | 1,260.00 USD | 0.00 USD | `+18.52%` | `10.94` |
| `Live` | `Short` | `115.35` | 12,230,000.00 USD | 878,270.00 USD | 0.00 USD | `+18.62%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 12,410,000.00 USD | 182,070.00 USD | 0.00 USD | `+18.83%` | `1,575.66` |
| `Live` | `Short` | `115.75` | 12,410,000.00 USD | 160.89 USD | 0.00 USD | `+19.03%` | `1.39` |
| `Live` | `Short` | `115.85` | 12,410,000.00 USD | 289.62 USD | 0.00 USD | `+19.14%` | `2.50` |
| `Live` | `Short` | `115.95` | 12,410,000.00 USD | 162.33 USD | 0.00 USD | `+19.24%` | `1.40` |
| `Live` | `Short` | `116.05` | 12,410,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.34%` | `38.34` |
| `Live` | `Short` | `116.15` | 12,420,000.00 USD | 5,990.00 USD | 0.00 USD | `+19.45%` | `51.58` |
| `Live` | `Short` | `116.25` | 12,420,000.00 USD | 180.19 USD | 0.00 USD | `+19.55%` | `1.55` |
| `Live` | `Short` | `116.35` | 12,430,000.00 USD | 5,400.00 USD | 0.00 USD | `+19.65%` | `46.41` |
| `Live` | `Short` | `116.55` | 12,430,000.00 USD | 2,040.00 USD | 0.00 USD | `+19.86%` | `17.52` |
| `Live` | `Short` | `116.65` | 12,430,000.00 USD | 113.15 USD | 0.00 USD | `+19.96%` | `0.97` |
| `Live` | `Short` | `116.75` | 12,470,000.00 USD | 40,860.00 USD | 0.00 USD | `+20.06%` | `350.00` |
| `Live` | `Short` | `117.05` | 12,470,000.00 USD | 156.85 USD | 0.00 USD | `+20.37%` | `1.34` |
| `Live` | `Short` | `117.15` | 12,560,000.00 USD | 89,950.00 USD | 0.00 USD | `+20.47%` | `767.80` |
| `Live` | `Short` | `117.35` | 12,570,000.00 USD | 11,780.00 USD | 0.00 USD | `+20.68%` | `100.38` |
| `Live` | `Short` | `117.55` | 12,570,000.00 USD | 188.08 USD | 0.00 USD | `+20.89%` | `1.60` |
| `Live` | `Short` | `117.75` | 12,580,000.00 USD | 10,360.00 USD | 0.00 USD | `+21.09%` | `87.98` |
| `Live` | `Short` | `117.95` | 12,580,000.00 USD | 2,090.00 USD | 0.00 USD | `+21.30%` | `17.72` |
| `Live` | `Short` | `118.25` | 12,590,000.00 USD | 8,670.00 USD | 0.00 USD | `+21.61%` | `73.31` |
| `Live` | `Short` | `118.35` | 17,060,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+21.71%` | `37,796.13` |
| `Live` | `Short` | `118.45` | 17,090,000.00 USD | 30,080.00 USD | 0.00 USD | `+21.81%` | `253.91` |
| `Live` | `Short` | `118.55` | 17,100,000.00 USD | 7,700.00 USD | 0.00 USD | `+21.91%` | `64.98` |
| `Live` | `Short` | `118.65` | 17,110,000.00 USD | 5,740.00 USD | 0.00 USD | `+22.02%` | `48.34` |
| `Live` | `Short` | `118.75` | 17,110,000.00 USD | 309.94 USD | 0.00 USD | `+22.12%` | `2.61` |
| `Live` | `Short` | `119.15` | 17,120,000.00 USD | 12,550.00 USD | 0.00 USD | `+22.53%` | `105.36` |
| `Live` | `Short` | `119.25` | 17,120,000.00 USD | 240.88 USD | 0.00 USD | `+22.63%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,180,000.00 USD | 57,850.00 USD | 0.00 USD | `+22.74%` | `484.72` |
| `Live` | `Short` | `119.55` | 17,190,000.00 USD | 8,970.00 USD | 0.00 USD | `+22.94%` | `75.00` |
| `Live` | `Short` | `119.75` | 17,190,000.00 USD | 261.06 USD | 0.00 USD | `+23.15%` | `2.18` |
| `Live` | `Short` | `119.85` | 17,190,000.00 USD | 485.39 USD | 0.00 USD | `+23.25%` | `4.05` |
| `Live` | `Short` | `119.95` | 17,220,000.00 USD | 29,570.00 USD | 0.00 USD | `+23.35%` | `246.48` |
| `Live` | `Short` | `120.15` | 17,320,000.00 USD | 98,720.00 USD | 0.00 USD | `+23.56%` | `821.66` |
| `Live` | `Short` | `120.25` | 17,320,000.00 USD | 925.93 USD | 0.00 USD | `+23.66%` | `7.70` |
| `Live` | `Short` | `120.45` | 17,380,000.00 USD | 60,370.00 USD | 0.00 USD | `+23.87%` | `501.21` |
| `Live` | `Short` | `120.55` | 17,380,000.00 USD | 1,190.00 USD | 0.00 USD | `+23.97%` | `9.86` |
| `Live` | `Short` | `120.65` | 17,380,000.00 USD | 1,110.00 USD | 0.00 USD | `+24.07%` | `9.19` |
| `Live` | `Short` | `120.95` | 17,390,000.00 USD | 13,290.00 USD | 0.00 USD | `+24.38%` | `109.91` |
| `Live` | `Short` | `121.15` | 17,390,000.00 USD | 316.20 USD | 0.00 USD | `+24.59%` | `2.61` |
| `Live` | `Short` | `121.25` | 17,430,000.00 USD | 31,420.00 USD | 0.00 USD | `+24.69%` | `259.16` |
| `Live` | `Short` | `121.55` | 17,460,000.00 USD | 34,870.00 USD | 0.00 USD | `+25.00%` | `286.91` |
| `Live` | `Short` | `121.75` | 17,460,000.00 USD | 105.92 USD | 0.00 USD | `+25.20%` | `0.87` |
| `Live` | `Short` | `122.05` | 17,520,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.51%` | `460.06` |
| `Live` | `Short` | `122.15` | 17,520,000.00 USD | 169.79 USD | 0.00 USD | `+25.62%` | `1.39` |
| `Live` | `Short` | `122.25` | 17,520,000.00 USD | 2,330.00 USD | 0.00 USD | `+25.72%` | `19.10` |
| `Live` | `Short` | `122.35` | 18,400,000.00 USD | 881,450.00 USD | 0.00 USD | `+25.82%` | `7,204.35` |
| `Live` | `Short` | `122.45` | 18,420,000.00 USD | 17,500.00 USD | 0.00 USD | `+25.92%` | `142.95` |
| `Live` | `Short` | `122.65` | 18,460,000.00 USD | 45,560.00 USD | 0.00 USD | `+26.13%` | `371.45` |
| `Live` | `Short` | `122.75` | 18,530,000.00 USD | 61,380.00 USD | 0.00 USD | `+26.23%` | `500.00` |
| `Live` | `Short` | `123.05` | 18,530,000.00 USD | 9,500.00 USD | 0.00 USD | `+26.54%` | `77.19` |
| `Live` | `Short` | `123.25` | 19,010,000.00 USD | 471,560.00 USD | 0.00 USD | `+26.75%` | `3,826.05` |
| `Live` | `Short` | `123.35` | 19,010,000.00 USD | 2,990.00 USD | 0.00 USD | `+26.85%` | `24.24` |
| `Live` | `Short` | `123.45` | 19,010,000.00 USD | 1,960.00 USD | 0.00 USD | `+26.95%` | `15.87` |
| `Live` | `Short` | `123.55` | 19,140,000.00 USD | 124,410.00 USD | 0.00 USD | `+27.06%` | `1,006.96` |
| `Live` | `Short` | `123.85` | 19,140,000.00 USD | 126.33 USD | 0.00 USD | `+27.36%` | `1.02` |
| `Live` | `Short` | `123.95` | 19,140,000.00 USD | 762.29 USD | 0.00 USD | `+27.47%` | `6.15` |
| `Live` | `Short` | `124.05` | 19,140,000.00 USD | 586.76 USD | 0.00 USD | `+27.57%` | `4.73` |
| `Live` | `Short` | `124.15` | 19,140,000.00 USD | 121.67 USD | 0.00 USD | `+27.67%` | `0.98` |
| `Live` | `Short` | `124.25` | 19,160,000.00 USD | 23,360.00 USD | 0.00 USD | `+27.78%` | `188.01` |
| `Live` | `Short` | `124.35` | 19,160,000.00 USD | 114.40 USD | 0.00 USD | `+27.88%` | `0.92` |
| `Live` | `Short` | `124.55` | 19,160,000.00 USD | 3,080.00 USD | 0.00 USD | `+28.08%` | `24.76` |
| `Live` | `Short` | `124.65` | 19,160,000.00 USD | 675.60 USD | 0.00 USD | `+28.19%` | `5.42` |
| `Live` | `Short` | `124.75` | 19,170,000.00 USD | 5,330.00 USD | 0.00 USD | `+28.29%` | `42.73` |
| `Live` | `Short` | `124.95` | 19,180,000.00 USD | 9,550.00 USD | 0.00 USD | `+28.50%` | `76.46` |
| `Live` | `Short` | `125.05` | 19,180,000.00 USD | 208.83 USD | 0.00 USD | `+28.60%` | `1.67` |
| `Live` | `Short` | `125.25` | 19,180,000.00 USD | 3,330.00 USD | 0.00 USD | `+28.80%` | `26.58` |
| `Live` | `Short` | `125.35` | 19,190,000.00 USD | 5,320.00 USD | 0.00 USD | `+28.91%` | `42.44` |
| `Live` | `Short` | `125.45` | 23,350,000.00 USD | 4,160,000.00 USD | 0.00 USD | `+29.01%` | `33,165.14` |
| `Live` | `Short` | `125.55` | 23,350,000.00 USD | 4,610.00 USD | 0.00 USD | `+29.11%` | `36.71` |
| `Live` | `Short` | `125.65` | 23,360,000.00 USD | 1,560.00 USD | 0.00 USD | `+29.22%` | `12.41` |
| `Live` | `Short` | `125.75` | 23,360,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.32%` | `15.31` |
| `Live` | `Short` | `125.95` | 23,360,000.00 USD | 110.84 USD | 0.00 USD | `+29.52%` | `0.88` |
| `Live` | `Short` | `126.05` | 23,360,000.00 USD | 810.50 USD | 0.00 USD | `+29.63%` | `6.43` |
| `Live` | `Short` | `126.15` | 23,360,000.00 USD | 1,030.00 USD | 0.00 USD | `+29.73%` | `8.16` |
| `Live` | `Short` | `126.35` | 23,360,000.00 USD | 6,050.00 USD | 0.00 USD | `+29.93%` | `47.86` |
| `Live` | `Short` | `126.45` | 23,370,000.00 USD | 5,150.00 USD | 0.00 USD | `+30.04%` | `40.70` |
| `Live` | `Short` | `126.55` | 23,370,000.00 USD | 403.69 USD | 0.00 USD | `+30.14%` | `3.19` |
| `Live` | `Short` | `126.65` | 23,410,000.00 USD | 35,270.00 USD | 0.00 USD | `+30.24%` | `278.46` |
| `Live` | `Short` | `126.85` | 23,410,000.00 USD | 3,870.00 USD | 0.00 USD | `+30.45%` | `30.49` |
| `Live` | `Short` | `127.05` | 23,410,000.00 USD | 2,030.00 USD | 0.00 USD | `+30.65%` | `16.01` |
| `Live` | `Short` | `127.15` | 23,410,000.00 USD | 389.08 USD | 0.00 USD | `+30.76%` | `3.06` |
| `Live` | `Short` | `127.35` | 23,440,000.00 USD | 28,940.00 USD | 0.00 USD | `+30.96%` | `227.26` |
| `Live` | `Short` | `127.45` | 23,440,000.00 USD | 138.92 USD | 0.00 USD | `+31.07%` | `1.09` |
| `Live` | `Short` | `127.65` | 23,450,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.27%` | `37.89` |
| `Live` | `Short` | `127.75` | 23,470,000.00 USD | 20,800.00 USD | 0.00 USD | `+31.37%` | `162.83` |
| `Live` | `Short` | `127.85` | 23,470,000.00 USD | 388.66 USD | 0.00 USD | `+31.48%` | `3.04` |
| `Live` | `Short` | `127.95` | 23,480,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.58%` | `82.13` |
| `Live` | `Short` | `128.05` | 23,590,000.00 USD | 116,190.00 USD | 0.00 USD | `+31.68%` | `907.38` |
| `Live` | `Short` | `128.15` | 23,590,000.00 USD | 221.70 USD | 0.00 USD | `+31.79%` | `1.73` |
| `Live` | `Short` | `128.35` | 23,850,000.00 USD | 257,680.00 USD | 0.00 USD | `+31.99%` | `2,007.62` |
| `Live` | `Short` | `128.45` | 23,860,000.00 USD | 6,420.00 USD | 0.00 USD | `+32.09%` | `50.00` |
| `Live` | `Short` | `128.65` | 23,860,000.00 USD | 788.62 USD | 0.00 USD | `+32.30%` | `6.13` |
| `Live` | `Short` | `128.75` | 23,880,000.00 USD | 18,730.00 USD | 0.00 USD | `+32.40%` | `145.45` |
| `Live` | `Short` | `128.85` | 23,910,000.00 USD | 32,440.00 USD | 0.00 USD | `+32.51%` | `251.77` |
| `Live` | `Short` | `129.15` | 24,030,000.00 USD | 124,100.00 USD | 0.00 USD | `+32.81%` | `960.86` |
| `Live` | `Short` | `129.25` | 24,070,000.00 USD | 32,310.00 USD | 0.00 USD | `+32.92%` | `250.00` |
| `Live` | `Short` | `129.35` | 24,100,000.00 USD | 35,060.00 USD | 0.00 USD | `+33.02%` | `271.06` |
| `Live` | `Short` | `129.45` | 24,800,000.00 USD | 700,490.00 USD | 0.00 USD | `+33.12%` | `5,411.30` |
| `Live` | `Short` | `129.55` | 24,800,000.00 USD | 910.74 USD | 0.00 USD | `+33.23%` | `7.03` |
| `Live` | `Short` | `129.75` | 24,810,000.00 USD | 2,210.00 USD | 0.00 USD | `+33.43%` | `17.05` |
| `Live` | `Short` | `129.85` | 24,810,000.00 USD | 490.83 USD | 0.00 USD | `+33.53%` | `3.78` |
| `Live` | `Short` | `130.35` | 24,820,000.00 USD | 13,360.00 USD | 0.00 USD | `+34.05%` | `102.50` |
| `Live` | `Short` | `130.55` | 24,820,000.00 USD | 1,860.00 USD | 0.00 USD | `+34.25%` | `14.21` |
| `Live` | `Short` | `130.85` | 24,820,000.00 USD | 3,180.00 USD | 0.00 USD | `+34.56%` | `24.34` |
| `Live` | `Short` | `130.95` | 24,830,000.00 USD | 2,070.00 USD | 0.00 USD | `+34.67%` | `15.84` |
| `Live` | `Short` | `131.05` | 24,830,000.00 USD | 188.71 USD | 0.00 USD | `+34.77%` | `1.44` |
| `Live` | `Short` | `131.25` | 24,830,000.00 USD | 1,560.00 USD | 0.00 USD | `+34.97%` | `11.87` |
| `Live` | `Short` | `131.35` | 24,840,000.00 USD | 14,160.00 USD | 0.00 USD | `+35.08%` | `107.79` |
| `Live` | `Short` | `131.45` | 24,840,000.00 USD | 219.52 USD | 0.00 USD | `+35.18%` | `1.67` |
| `Live` | `Short` | `131.85` | 24,850,000.00 USD | 6,700.00 USD | 0.00 USD | `+35.59%` | `50.83` |
| `Live` | `Short` | `131.95` | 24,850,000.00 USD | 106.88 USD | 0.00 USD | `+35.69%` | `0.81` |
| `Live` | `Short` | `132.15` | 24,880,000.00 USD | 30,070.00 USD | 0.00 USD | `+35.90%` | `227.54` |
| `Live` | `Short` | `132.45` | 24,880,000.00 USD | 1,720.00 USD | 0.00 USD | `+36.21%` | `12.98` |
| `Live` | `Short` | `132.55` | 24,890,000.00 USD | 8,730.00 USD | 0.00 USD | `+36.31%` | `65.85` |
| `Live` | `Short` | `132.65` | 24,890,000.00 USD | 240.10 USD | 0.00 USD | `+36.41%` | `1.81` |
| `Live` | `Short` | `132.75` | 24,890,000.00 USD | 136.73 USD | 0.00 USD | `+36.52%` | `1.03` |
| `Live` | `Short` | `132.85` | 24,940,000.00 USD | 49,280.00 USD | 0.00 USD | `+36.62%` | `370.98` |
| `Live` | `Short` | `133.05` | 24,940,000.00 USD | 103.78 USD | 0.00 USD | `+36.83%` | `0.78` |
| `Live` | `Short` | `133.15` | 24,950,000.00 USD | 8,440.00 USD | 0.00 USD | `+36.93%` | `63.42` |
| `Live` | `Short` | `133.25` | 24,950,000.00 USD | 1,330.00 USD | 0.00 USD | `+37.03%` | `9.95` |
| `Live` | `Short` | `133.65` | 24,950,000.00 USD | 156.37 USD | 0.00 USD | `+37.44%` | `1.17` |
| `Live` | `Short` | `133.75` | 25,100,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.54%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 25,100,000.00 USD | 503.65 USD | 0.00 USD | `+37.75%` | `3.76` |
| `Live` | `Short` | `134.05` | 25,110,000.00 USD | 12,620.00 USD | 0.00 USD | `+37.85%` | `94.18` |
| `Live` | `Short` | `134.15` | 25,120,000.00 USD | 2,180.00 USD | 0.00 USD | `+37.96%` | `16.25` |
| `Live` | `Short` | `134.25` | 25,130,000.00 USD | 11,590.00 USD | 0.00 USD | `+38.06%` | `86.32` |
| `Live` | `Short` | `135.05` | 25,130,000.00 USD | 6,390.00 USD | 0.00 USD | `+38.88%` | `47.30` |
| `Live` | `Short` | `135.35` | 25,140,000.00 USD | 8,560.00 USD | 0.00 USD | `+39.19%` | `63.21` |
| `Live` | `Short` | `135.65` | 25,190,000.00 USD | 48,790.00 USD | 0.00 USD | `+39.50%` | `359.64` |
| `Live` | `Short` | `135.75` | 25,200,000.00 USD | 4,060.00 USD | 0.00 USD | `+39.60%` | `29.93` |
| `Live` | `Short` | `135.85` | 25,220,000.00 USD | 21,460.00 USD | 0.00 USD | `+39.70%` | `157.95` |
| `Live` | `Short` | `135.95` | 25,220,000.00 USD | 504.37 USD | 0.00 USD | `+39.81%` | `3.71` |
| `Live` | `Short` | `136.15` | 25,260,000.00 USD | 40,190.00 USD | 0.00 USD | `+40.01%` | `295.19` |
| `Live` | `Short` | `136.55` | 25,260,000.00 USD | 136.55 USD | 0.00 USD | `+40.42%` | `1.00` |
| `Live` | `Short` | `136.65` | 25,260,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.53%` | `8.14` |
| `Live` | `Short` | `136.85` | 25,270,000.00 USD | 14,710.00 USD | 0.00 USD | `+40.73%` | `107.50` |
| `Live` | `Short` | `136.95` | 25,310,000.00 USD | 35,260.00 USD | 0.00 USD | `+40.84%` | `257.50` |
| `Live` | `Short` | `137.05` | 25,310,000.00 USD | 836.00 USD | 0.00 USD | `+40.94%` | `6.10` |
| `Live` | `Short` | `137.15` | 25,310,000.00 USD | 809.19 USD | 0.00 USD | `+41.04%` | `5.90` |
| `Live` | `Short` | `137.25` | 25,380,000.00 USD | 68,620.00 USD | 0.00 USD | `+41.14%` | `500.00` |
| `Live` | `Short` | `137.65` | 25,380,000.00 USD | 2,050.00 USD | 0.00 USD | `+41.56%` | `14.87` |
| `Live` | `Short` | `137.75` | 25,390,000.00 USD | 12,520.00 USD | 0.00 USD | `+41.66%` | `90.91` |
| `Live` | `Short` | `138.05` | 25,390,000.00 USD | 1,270.00 USD | 0.00 USD | `+41.97%` | `9.20` |
| `Live` | `Short` | `138.15` | 25,440,000.00 USD | 44,270.00 USD | 0.00 USD | `+42.07%` | `320.42` |
| `Live` | `Short` | `138.25` | 25,480,000.00 USD | 45,220.00 USD | 0.00 USD | `+42.17%` | `327.11` |
| `Live` | `Short` | `138.45` | 25,490,000.00 USD | 7,310.00 USD | 0.00 USD | `+42.38%` | `52.83` |
| `Live` | `Short` | `138.55` | 25,490,000.00 USD | 538.96 USD | 0.00 USD | `+42.48%` | `3.89` |
| `Live` | `Short` | `138.65` | 25,490,000.00 USD | 1,530.00 USD | 0.00 USD | `+42.58%` | `11.00` |
| `Live` | `Short` | `138.75` | 25,500,000.00 USD | 2,360.00 USD | 0.00 USD | `+42.69%` | `17.04` |
| `Live` | `Short` | `138.95` | 25,500,000.00 USD | 8,750.00 USD | 0.00 USD | `+42.89%` | `63.00` |
| `Live` | `Short` | `139.15` | 25,510,000.00 USD | 552.43 USD | 0.00 USD | `+43.10%` | `3.97` |
| `Live` | `Short` | `139.45` | 25,510,000.00 USD | 253.80 USD | 0.00 USD | `+43.41%` | `1.82` |
| `Live` | `Short` | `139.55` | 25,510,000.00 USD | 494.01 USD | 0.00 USD | `+43.51%` | `3.54` |
| `Live` | `Short` | `139.75` | 25,520,000.00 USD | 9,060.00 USD | 0.00 USD | `+43.72%` | `64.82` |
| `Live` | `Short` | `139.85` | 30,570,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+43.82%` | `36,111.60` |
| `Live` | `Short` | `139.95` | 30,570,000.00 USD | 394.66 USD | 0.00 USD | `+43.92%` | `2.82` |
| `Live` | `Short` | `140.05` | 30,570,000.00 USD | 116.24 USD | 0.00 USD | `+44.02%` | `0.83` |
| `Live` | `Short` | `140.15` | 30,570,000.00 USD | 625.07 USD | 0.00 USD | `+44.13%` | `4.46` |
| `Live` | `Short` | `140.35` | 30,570,000.00 USD | 127.72 USD | 0.00 USD | `+44.33%` | `0.91` |
| `Live` | `Short` | `140.45` | 30,570,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.43%` | `34.66` |
| `Live` | `Short` | `140.55` | 30,570,000.00 USD | 702.75 USD | 0.00 USD | `+44.54%` | `5.00` |
| `Live` | `Short` | `140.65` | 30,580,000.00 USD | 7,340.00 USD | 0.00 USD | `+44.64%` | `52.16` |
| `Live` | `Short` | `140.95` | 30,580,000.00 USD | 1,940.00 USD | 0.00 USD | `+44.95%` | `13.73` |
| `Live` | `Short` | `141.05` | 30,650,000.00 USD | 70,450.00 USD | 0.00 USD | `+45.05%` | `499.50` |
| `Live` | `Short` | `141.35` | 30,680,000.00 USD | 23,350.00 USD | 0.00 USD | `+45.36%` | `165.17` |
| `Live` | `Short` | `141.45` | 30,920,000.00 USD | 247,540.00 USD | 0.00 USD | `+45.46%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 30,920,000.00 USD | 236.39 USD | 0.00 USD | `+45.57%` | `1.67` |
| `Live` | `Short` | `141.65` | 32,870,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+45.67%` | `13,744.62` |
| `Live` | `Short` | `141.75` | 32,870,000.00 USD | 2,250.00 USD | 0.00 USD | `+45.77%` | `15.84` |
| `Live` | `Short` | `142.05` | 32,870,000.00 USD | 2,580.00 USD | 0.00 USD | `+46.08%` | `18.15` |
| `Live` | `Short` | `142.15` | 32,870,000.00 USD | 112.30 USD | 0.00 USD | `+46.18%` | `0.79` |
| `Live` | `Short` | `142.25` | 32,880,000.00 USD | 3,470.00 USD | 0.00 USD | `+46.29%` | `24.41` |
| `Live` | `Short` | `142.35` | 33,470,000.00 USD | 593,190.00 USD | 0.00 USD | `+46.39%` | `4,167.10` |
| `Live` | `Short` | `142.45` | 33,470,000.00 USD | 151.00 USD | 0.00 USD | `+46.49%` | `1.06` |
| `Live` | `Short` | `142.65` | 33,470,000.00 USD | 2,960.00 USD | 0.00 USD | `+46.70%` | `20.75` |
| `Live` | `Short` | `142.75` | 33,470,000.00 USD | 368.30 USD | 0.00 USD | `+46.80%` | `2.58` |
| `Live` | `Short` | `142.85` | 33,490,000.00 USD | 18,720.00 USD | 0.00 USD | `+46.90%` | `131.07` |
| `Live` | `Short` | `143.15` | 33,500,000.00 USD | 1,460.00 USD | 0.00 USD | `+47.21%` | `10.22` |
| `Live` | `Short` | `143.35` | 33,620,000.00 USD | 126,920.00 USD | 0.00 USD | `+47.42%` | `885.41` |
| `Live` | `Short` | `143.45` | 33,620,000.00 USD | 790.41 USD | 0.00 USD | `+47.52%` | `5.51` |
| `Live` | `Short` | `143.55` | 33,620,000.00 USD | 103.36 USD | 0.00 USD | `+47.62%` | `0.72` |
| `Live` | `Short` | `144.05` | 33,630,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.14%` | `26.00` |
| `Live` | `Short` | `144.65` | 33,630,000.00 USD | 1,240.00 USD | 0.00 USD | `+48.75%` | `8.60` |
| `Live` | `Short` | `145.15` | 33,630,000.00 USD | 1,760.00 USD | 0.00 USD | `+49.27%` | `12.12` |
| `Live` | `Short` | `145.45` | 33,750,000.00 USD | 118,420.00 USD | 0.00 USD | `+49.58%` | `814.19` |
| `Live` | `Short` | `145.65` | 33,750,000.00 USD | 607.36 USD | 0.00 USD | `+49.78%` | `4.17` |
| `Live` | `Short` | `145.85` | 33,760,000.00 USD | 6,300.00 USD | 0.00 USD | `+49.99%` | `43.20` |
| `Live` | `Short` | `145.95` | 33,760,000.00 USD | 685.96 USD | 0.00 USD | `+50.09%` | `4.70` |
| `Live` | `Short` | `146.15` | 33,840,000.00 USD | 88,760.00 USD | 0.00 USD | `+50.30%` | `607.33` |
| `Live` | `Short` | `146.25` | 33,850,000.00 USD | 2,770.00 USD | 0.00 USD | `+50.40%` | `18.95` |
| `Live` | `Short` | `146.35` | 33,860,000.00 USD | 8,730.00 USD | 0.00 USD | `+50.50%` | `59.67` |
| `Live` | `Short` | `146.45` | 34,300,000.00 USD | 439,350.00 USD | 0.00 USD | `+50.61%` | `3,000.00` |
| `Live` | `Short` | `146.55` | 34,370,000.00 USD | 75,880.00 USD | 0.00 USD | `+50.71%` | `517.77` |
| `Live` | `Short` | `146.65` | 34,960,000.00 USD | 587,730.00 USD | 0.00 USD | `+50.81%` | `4,007.68` |
| `Live` | `Short` | `146.95` | 34,960,000.00 USD | 3,070.00 USD | 0.00 USD | `+51.12%` | `20.88` |
| `Live` | `Short` | `147.05` | 34,980,000.00 USD | 17,760.00 USD | 0.00 USD | `+51.22%` | `120.76` |
| `Live` | `Short` | `147.15` | 34,980,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.33%` | `11.75` |
| `Live` | `Short` | `147.35` | 34,980,000.00 USD | 169.45 USD | 0.00 USD | `+51.53%` | `1.15` |
| `Live` | `Short` | `147.45` | 34,980,000.00 USD | 204.96 USD | 0.00 USD | `+51.63%` | `1.39` |
| `Live` | `Short` | `147.55` | 34,980,000.00 USD | 1,000.00 USD | 0.00 USD | `+51.74%` | `6.78` |
| `Live` | `Short` | `147.65` | 34,980,000.00 USD | 237.72 USD | 0.00 USD | `+51.84%` | `1.61` |
| `Live` | `Short` | `147.75` | 35,060,000.00 USD | 75,610.00 USD | 0.00 USD | `+51.94%` | `511.72` |
| `Live` | `Short` | `147.85` | 35,140,000.00 USD | 78,720.00 USD | 0.00 USD | `+52.04%` | `532.45` |
| `Live` | `Short` | `148.05` | 35,660,000.00 USD | 518,180.00 USD | 0.00 USD | `+52.25%` | `3,500.00` |
| `Live` | `Short` | `148.15` | 35,660,000.00 USD | 102.22 USD | 0.00 USD | `+52.35%` | `0.69` |
| `Live` | `Short` | `148.45` | 35,660,000.00 USD | 9,130.00 USD | 0.00 USD | `+52.66%` | `61.53` |
| `Live` | `Short` | `148.55` | 36,010,000.00 USD | 344,780.00 USD | 0.00 USD | `+52.76%` | `2,321.00` |
| `Live` | `Short` | `148.75` | 36,100,000.00 USD | 95,070.00 USD | 0.00 USD | `+52.97%` | `639.13` |
| `Live` | `Short` | `149.45` | 37,490,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+53.69%` | `9,286.68` |
| `Live` | `Short` | `149.55` | 37,490,000.00 USD | 116.65 USD | 0.00 USD | `+53.79%` | `0.78` |
| `Live` | `Short` | `149.65` | 37,510,000.00 USD | 16,030.00 USD | 0.00 USD | `+53.90%` | `107.15` |
| `Live` | `Short` | `149.95` | 37,770,000.00 USD | 263,290.00 USD | 0.00 USD | `+54.20%` | `1,755.87` |
| `Live` | `Short` | `150.05` | 37,900,000.00 USD | 126,150.00 USD | 0.00 USD | `+54.31%` | `840.75` |
| `Live` | `Short` | `150.95` | 37,900,000.00 USD | 347.18 USD | 0.00 USD | `+55.23%` | `2.30` |
| `Live` | `Short` | `151.05` | 37,920,000.00 USD | 24,850.00 USD | 0.00 USD | `+55.34%` | `164.53` |
| `Live` | `Short` | `151.15` | 37,930,000.00 USD | 3,180.00 USD | 0.00 USD | `+55.44%` | `21.05` |
| `Live` | `Short` | `151.25` | 37,930,000.00 USD | 2,780.00 USD | 0.00 USD | `+55.54%` | `18.37` |
| `Live` | `Short` | `151.45` | 37,940,000.00 USD | 8,830.00 USD | 0.00 USD | `+55.75%` | `58.32` |
| `Live` | `Short` | `151.85` | 39,680,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+56.16%` | `11,488.27` |
| `Live` | `Short` | `151.95` | 39,680,000.00 USD | 1,920.00 USD | 0.00 USD | `+56.26%` | `12.64` |
| `Live` | `Short` | `152.05` | 40,840,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+56.36%` | `7,566.18` |
| `Live` | `Short` | `152.25` | 40,840,000.00 USD | 200.97 USD | 0.00 USD | `+56.57%` | `1.32` |
| `Live` | `Short` | `152.35` | 41,120,000.00 USD | 286,550.00 USD | 0.00 USD | `+56.67%` | `1,880.87` |
| `Live` | `Short` | `152.45` | 41,120,000.00 USD | 3,150.00 USD | 0.00 USD | `+56.78%` | `20.65` |
| `Live` | `Short` | `152.75` | 41,130,000.00 USD | 1,570.00 USD | 0.00 USD | `+57.08%` | `10.30` |
| `Live` | `Short` | `153.05` | 41,890,000.00 USD | 761,410.00 USD | 0.00 USD | `+57.39%` | `4,974.90` |
| `Live` | `Short` | `153.25` | 41,930,000.00 USD | 44,870.00 USD | 0.00 USD | `+57.60%` | `292.82` |
| `Live` | `Short` | `153.35` | 42,040,000.00 USD | 109,650.00 USD | 0.00 USD | `+57.70%` | `715.00` |
| `Live` | `Short` | `153.55` | 42,060,000.00 USD | 17,980.00 USD | 0.00 USD | `+57.91%` | `117.09` |
| `Live` | `Short` | `153.65` | 42,070,000.00 USD | 8,340.00 USD | 0.00 USD | `+58.01%` | `54.29` |
| `Live` | `Short` | `153.85` | 42,070,000.00 USD | 2,110.00 USD | 0.00 USD | `+58.22%` | `13.71` |
| `Live` | `Short` | `154.05` | 42,080,000.00 USD | 5,430.00 USD | 0.00 USD | `+58.42%` | `35.27` |
| `Live` | `Short` | `154.15` | 42,080,000.00 USD | 292.89 USD | 0.00 USD | `+58.52%` | `1.90` |
| `Live` | `Short` | `154.25` | 42,080,000.00 USD | 2,340.00 USD | 0.00 USD | `+58.63%` | `15.20` |
| `Live` | `Short` | `154.45` | 42,080,000.00 USD | 4,240.00 USD | 0.00 USD | `+58.83%` | `27.45` |
| `Live` | `Short` | `154.65` | 42,080,000.00 USD | 363.43 USD | 0.00 USD | `+59.04%` | `2.35` |
| `Live` | `Short` | `154.75` | 42,080,000.00 USD | 1,160.00 USD | 0.00 USD | `+59.14%` | `7.50` |
| `Live` | `Short` | `154.95` | 46,780,000.00 USD | 4,700,000.00 USD | 0.00 USD | `+59.35%` | `30,310.49` |
| `Live` | `Short` | `155.55` | 46,780,000.00 USD | 267.55 USD | 0.00 USD | `+59.96%` | `1.72` |
| `Live` | `Short` | `155.75` | 46,780,000.00 USD | 2,350.00 USD | 0.00 USD | `+60.17%` | `15.09` |
| `Live` | `Short` | `155.95` | 46,780,000.00 USD | 118.52 USD | 0.00 USD | `+60.37%` | `0.76` |
| `Live` | `Short` | `156.15` | 46,790,000.00 USD | 7,810.00 USD | 0.00 USD | `+60.58%` | `50.00` |
| `Live` | `Short` | `156.35` | 46,790,000.00 USD | 197.00 USD | 0.00 USD | `+60.79%` | `1.26` |
| `Live` | `Short` | `156.45` | 46,800,000.00 USD | 4,900.00 USD | 0.00 USD | `+60.89%` | `31.29` |
| `Live` | `Short` | `156.55` | 46,800,000.00 USD | 327.19 USD | 0.00 USD | `+60.99%` | `2.09` |
| `Live` | `Short` | `156.85` | 50,370,000.00 USD | 3,570,000.00 USD | 0.00 USD | `+61.30%` | `22,770.74` |
| `Live` | `Short` | `157.15` | 50,420,000.00 USD | 49,270.00 USD | 0.00 USD | `+61.61%` | `313.50` |
| `Live` | `Short` | `157.45` | 50,420,000.00 USD | 297.58 USD | 0.00 USD | `+61.92%` | `1.89` |
| `Live` | `Short` | `157.65` | 50,500,000.00 USD | 80,280.00 USD | 0.00 USD | `+62.12%` | `509.22` |
| `Live` | `Short` | `157.75` | 50,590,000.00 USD | 95,670.00 USD | 0.00 USD | `+62.23%` | `606.46` |
| `Live` | `Short` | `157.85` | 50,830,000.00 USD | 236,780.00 USD | 0.00 USD | `+62.33%` | `1,500.00` |
| `Live` | `Short` | `157.95` | 50,860,000.00 USD | 27,690.00 USD | 0.00 USD | `+62.43%` | `175.30` |
| `Live` | `Short` | `159.05` | 50,900,000.00 USD | 45,350.00 USD | 0.00 USD | `+63.56%` | `285.11` |
| `Live` | `Short` | `159.45` | 51,010,000.00 USD | 101,550.00 USD | 0.00 USD | `+63.97%` | `636.89` |
| `Live` | `Short` | `159.65` | 51,010,000.00 USD | 1,760.00 USD | 0.00 USD | `+64.18%` | `11.01` |
| `Live` | `Short` | `159.85` | 51,090,000.00 USD | 85,160.00 USD | 0.00 USD | `+64.39%` | `532.74` |
| `Live` | `Short` | `159.95` | 51,520,000.00 USD | 431,860.00 USD | 0.00 USD | `+64.49%` | `2,700.00` |
| `Live` | `Short` | `160.05` | 51,530,000.00 USD | 497.76 USD | 0.00 USD | `+64.59%` | `3.11` |
| `Live` | `Short` | `160.15` | 52,210,000.00 USD | 683,000.00 USD | 0.00 USD | `+64.69%` | `4,264.75` |
| `Live` | `Short` | `160.35` | 52,210,000.00 USD | 655.83 USD | 0.00 USD | `+64.90%` | `4.09` |
| `Live` | `Short` | `160.65` | 52,350,000.00 USD | 141,270.00 USD | 0.00 USD | `+65.21%` | `879.39` |
| `Live` | `Short` | `161.05` | 52,350,000.00 USD | 2,240.00 USD | 0.00 USD | `+65.62%` | `13.93` |
| `Live` | `Short` | `161.35` | 52,350,000.00 USD | 1,530.00 USD | 0.00 USD | `+65.93%` | `9.51` |
| `Live` | `Short` | `161.55` | 52,350,000.00 USD | 410.34 USD | 0.00 USD | `+66.13%` | `2.54` |
| `Live` | `Short` | `161.85` | 52,680,000.00 USD | 323,700.00 USD | 0.00 USD | `+66.44%` | `2,000.00` |
| `Live` | `Short` | `161.95` | 52,820,000.00 USD | 144,610.00 USD | 0.00 USD | `+66.54%` | `892.95` |
| `Live` | `Short` | `162.15` | 52,820,000.00 USD | 1,050.00 USD | 0.00 USD | `+66.75%` | `6.49` |
| `Live` | `Short` | `162.45` | 52,820,000.00 USD | 1,350.00 USD | 0.00 USD | `+67.06%` | `8.29` |
| `Live` | `Short` | `163.75` | 52,840,000.00 USD | 12,390.00 USD | 0.00 USD | `+68.40%` | `75.65` |
| `Live` | `Short` | `163.85` | 52,840,000.00 USD | 786.48 USD | 0.00 USD | `+68.50%` | `4.80` |
| `Live` | `Short` | `163.95` | 53,040,000.00 USD | 206,830.00 USD | 0.00 USD | `+68.60%` | `1,261.56` |
| `Live` | `Short` | `164.45` | 53,050,000.00 USD | 6,580.00 USD | 0.00 USD | `+69.12%` | `40.03` |
| `Live` | `Short` | `164.65` | 53,050,000.00 USD | 3,400.00 USD | 0.00 USD | `+69.32%` | `20.63` |
| `Live` | `Short` | `165.15` | 53,060,000.00 USD | 198.18 USD | 0.00 USD | `+69.84%` | `1.20` |
| `Live` | `Short` | `165.85` | 53,060,000.00 USD | 620.28 USD | 0.00 USD | `+70.56%` | `3.74` |
| `Live` | `Short` | `166.15` | 53,060,000.00 USD | 996.90 USD | 0.00 USD | `+70.86%` | `6.00` |
| `Live` | `Short` | `166.25` | 53,070,000.00 USD | 14,070.00 USD | 0.00 USD | `+70.97%` | `84.61` |
| `Live` | `Short` | `166.45` | 53,070,000.00 USD | 149.81 USD | 0.00 USD | `+71.17%` | `0.90` |
| `Live` | `Short` | `166.85` | 53,070,000.00 USD | 685.75 USD | 0.00 USD | `+71.58%` | `4.11` |
| `Live` | `Short` | `167.55` | 53,080,000.00 USD | 11,330.00 USD | 0.00 USD | `+72.30%` | `67.60` |
| `Live` | `Short` | `167.65` | 53,090,000.00 USD | 3,360.00 USD | 0.00 USD | `+72.41%` | `20.02` |
| `Live` | `Short` | `167.75` | 53,090,000.00 USD | 2,730.00 USD | 0.00 USD | `+72.51%` | `16.27` |
| `Live` | `Short` | `168.05` | 53,090,000.00 USD | 122.68 USD | 0.00 USD | `+72.82%` | `0.73` |
| `Live` | `Short` | `168.35` | 53,110,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.13%` | `117.24` |
| `Live` | `Short` | `168.65` | 53,430,000.00 USD | 325,850.00 USD | 0.00 USD | `+73.44%` | `1,932.10` |
| `Live` | `Short` | `169.05` | 59,140,000.00 USD | 5,700,000.00 USD | 0.00 USD | `+73.85%` | `33,744.03` |
| `Live` | `Short` | `169.25` | 59,160,000.00 USD | 25,150.00 USD | 0.00 USD | `+74.05%` | `148.59` |
| `Live` | `Short` | `169.35` | 59,280,000.00 USD | 112,210.00 USD | 0.00 USD | `+74.15%` | `662.62` |
| `Live` | `Short` | `169.55` | 59,280,000.00 USD | 444.22 USD | 0.00 USD | `+74.36%` | `2.62` |
| `Live` | `Short` | `170.15` | 62,680,000.00 USD | 3,400,000.00 USD | 0.00 USD | `+74.98%` | `20,000.00` |
| `Live` | `Short` | `171.15` | 62,680,000.00 USD | 232.76 USD | 0.00 USD | `+76.01%` | `1.36` |
| `Live` | `Short` | `171.45` | 62,880,000.00 USD | 202,840.00 USD | 0.00 USD | `+76.31%` | `1,183.10` |
| `Live` | `Short` | `172.45` | 62,930,000.00 USD | 51,730.00 USD | 0.00 USD | `+77.34%` | `300.00` |
| `Live` | `Short` | `173.05` | 62,940,000.00 USD | 1,190.00 USD | 0.00 USD | `+77.96%` | `6.88` |
| `Live` | `Short` | `173.35` | 101,070,000.00 USD | 38,140,000.00 USD | 0.00 USD | `+78.27%` | `220,000.19` |
| `Live` | `Short` | `173.45` | 101,090,000.00 USD | 16,540.00 USD | 0.00 USD | `+78.37%` | `95.36` |
| `Live` | `Short` | `173.75` | 101,120,000.00 USD | 28,130.00 USD | 0.00 USD | `+78.68%` | `161.92` |
| `Live` | `Short` | `173.85` | 101,120,000.00 USD | 900.54 USD | 0.00 USD | `+78.78%` | `5.18` |
| `Live` | `Short` | `174.05` | 101,150,000.00 USD | 36,210.00 USD | 0.00 USD | `+78.99%` | `208.07` |
| `Live` | `Short` | `174.15` | 101,260,000.00 USD | 104,490.00 USD | 0.00 USD | `+79.09%` | `600.00` |
| `Live` | `Short` | `174.25` | 101,510,000.00 USD | 245,790.00 USD | 0.00 USD | `+79.19%` | `1,410.57` |
| `Live` | `Short` | `174.75` | 101,510,000.00 USD | 146.79 USD | 0.00 USD | `+79.71%` | `0.84` |
| `Live` | `Short` | `175.25` | 101,520,000.00 USD | 19,820.00 USD | 0.00 USD | `+80.22%` | `113.07` |
| `Live` | `Short` | `175.45` | 101,530,000.00 USD | 119.31 USD | 0.00 USD | `+80.43%` | `0.68` |
| `Live` | `Short` | `175.55` | 101,530,000.00 USD | 1,640.00 USD | 0.00 USD | `+80.53%` | `9.36` |
| `Live` | `Short` | `175.75` | 101,530,000.00 USD | 263.62 USD | 0.00 USD | `+80.74%` | `1.50` |
| `Live` | `Short` | `175.95` | 101,570,000.00 USD | 44,010.00 USD | 0.00 USD | `+80.94%` | `250.10` |
| `Live` | `Short` | `176.05` | 101,680,000.00 USD | 105,630.00 USD | 0.00 USD | `+81.05%` | `600.00` |
| `Live` | `Short` | `176.25` | 101,680,000.00 USD | 625.69 USD | 0.00 USD | `+81.25%` | `3.55` |
| `Live` | `Short` | `176.35` | 102,700,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+81.35%` | `5,800.00` |
| `Live` | `Short` | `177.65` | 102,700,000.00 USD | 637.76 USD | 0.00 USD | `+82.69%` | `3.59` |
| `Live` | `Short` | `177.75` | 102,730,000.00 USD | 29,380.00 USD | 0.00 USD | `+82.79%` | `165.30` |
| `Live` | `Short` | `177.95` | 103,080,000.00 USD | 350,160.00 USD | 0.00 USD | `+83.00%` | `1,967.73` |
| `Live` | `Short` | `178.55` | 103,080,000.00 USD | 2,830.00 USD | 0.00 USD | `+83.62%` | `15.84` |
| `Live` | `Short` | `178.75` | 103,080,000.00 USD | 715.00 USD | 0.00 USD | `+83.82%` | `4.00` |
| `Live` | `Short` | `178.95` | 103,090,000.00 USD | 4,470.00 USD | 0.00 USD | `+84.03%` | `25.00` |
| `Live` | `Short` | `179.25` | 103,110,000.00 USD | 17,390.00 USD | 0.00 USD | `+84.34%` | `97.00` |
| `Live` | `Short` | `179.65` | 103,120,000.00 USD | 11,320.00 USD | 0.00 USD | `+84.75%` | `62.99` |
| `Live` | `Short` | `179.95` | 103,470,000.00 USD | 352,500.00 USD | 0.00 USD | `+85.06%` | `1,958.88` |
| `Live` | `Short` | `180.05` | 104,810,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+85.16%` | `7,439.01` |
| `Live` | `Short` | `180.55` | 104,810,000.00 USD | 3,970.00 USD | 0.00 USD | `+85.67%` | `22.01` |
| `Live` | `Short` | `181.35` | 104,830,000.00 USD | 18,140.00 USD | 0.00 USD | `+86.50%` | `100.00` |
| `Live` | `Short` | `181.45` | 104,860,000.00 USD | 33,720.00 USD | 0.00 USD | `+86.60%` | `185.84` |
| `Live` | `Short` | `181.55` | 104,860,000.00 USD | 254.17 USD | 0.00 USD | `+86.70%` | `1.40` |
| `Live` | `Short` | `181.85` | 108,500,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+87.01%` | `20,011.24` |
| `Live` | `Short` | `182.15` | 108,510,000.00 USD | 3,990.00 USD | 0.00 USD | `+87.32%` | `21.93` |
| `Live` | `Short` | `182.45` | 108,510,000.00 USD | 1,370.00 USD | 0.00 USD | `+87.63%` | `7.52` |
| `Live` | `Short` | `183.05` | 108,580,000.00 USD | 73,220.00 USD | 0.00 USD | `+88.24%` | `400.00` |
| `Live` | `Short` | `183.65` | 108,580,000.00 USD | 286.49 USD | 0.00 USD | `+88.86%` | `1.56` |
| `Live` | `Short` | `184.25` | 108,580,000.00 USD | 1,680.00 USD | 0.00 USD | `+89.48%` | `9.12` |
| `Live` | `Short` | `184.65` | 108,590,000.00 USD | 7,650.00 USD | 0.00 USD | `+89.89%` | `41.43` |
| `Live` | `Short` | `184.95` | 108,760,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.20%` | `893.35` |
| `Live` | `Short` | `185.25` | 108,760,000.00 USD | 737.29 USD | 0.00 USD | `+90.51%` | `3.98` |
| `Live` | `Short` | `185.35` | 108,770,000.00 USD | 10,940.00 USD | 0.00 USD | `+90.61%` | `59.00` |
| `Live` | `Short` | `185.45` | 108,770,000.00 USD | 2,770.00 USD | 0.00 USD | `+90.71%` | `14.94` |
| `Live` | `Short` | `185.65` | 108,770,000.00 USD | 137.38 USD | 0.00 USD | `+90.92%` | `0.74` |
| `Live` | `Short` | `186.15` | 108,770,000.00 USD | 802.31 USD | 0.00 USD | `+91.43%` | `4.31` |
| `Live` | `Short` | `186.85` | 108,780,000.00 USD | 2,190.00 USD | 0.00 USD | `+92.15%` | `11.72` |
| `Live` | `Short` | `187.05` | 108,830,000.00 USD | 53,740.00 USD | 0.00 USD | `+92.36%` | `287.30` |
| `Live` | `Short` | `187.45` | 108,830,000.00 USD | 1,230.00 USD | 0.00 USD | `+92.77%` | `6.54` |
| `Live` | `Short` | `187.65` | 108,830,000.00 USD | 2,560.00 USD | 0.00 USD | `+92.97%` | `13.65` |
| `Live` | `Short` | `187.85` | 108,830,000.00 USD | 1,560.00 USD | 0.00 USD | `+93.18%` | `8.32` |
| `Live` | `Short` | `188.05` | 108,840,000.00 USD | 2,470.00 USD | 0.00 USD | `+93.39%` | `13.11` |
| `Live` | `Short` | `188.55` | 108,840,000.00 USD | 231.92 USD | 0.00 USD | `+93.90%` | `1.23` |
| `Live` | `Short` | `188.65` | 108,870,000.00 USD | 29,110.00 USD | 0.00 USD | `+94.00%` | `154.32` |
| `Live` | `Short` | `188.75` | 108,870,000.00 USD | 439.79 USD | 0.00 USD | `+94.11%` | `2.33` |
| `Live` | `Short` | `188.95` | 108,870,000.00 USD | 1,450.00 USD | 0.00 USD | `+94.31%` | `7.69` |
| `Live` | `Short` | `189.25` | 108,870,000.00 USD | 456.09 USD | 0.00 USD | `+94.62%` | `2.41` |
| `Live` | `Short` | `189.55` | 108,870,000.00 USD | 284.33 USD | 0.00 USD | `+94.93%` | `1.50` |
| `Live` | `Short` | `189.85` | 108,870,000.00 USD | 189.85 USD | 0.00 USD | `+95.24%` | `1.00` |
| `Live` | `Short` | `189.95` | 109,150,000.00 USD | 284,930.00 USD | 0.00 USD | `+95.34%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 109,150,000.00 USD | 148.32 USD | 0.00 USD | `+95.55%` | `0.78` |
| `Live` | `Short` | `190.45` | 109,150,000.00 USD | 118.08 USD | 0.00 USD | `+95.85%` | `0.62` |
| `Live` | `Short` | `190.95` | 122,720,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+96.37%` | `71,045.04` |
| `Live` | `Short` | `191.15` | 122,780,000.00 USD | 62,720.00 USD | 0.00 USD | `+96.57%` | `328.11` |
| `Live` | `Short` | `191.55` | 123,170,000.00 USD | 383,100.00 USD | 0.00 USD | `+96.98%` | `2,000.00` |
| `Live` | `Short` | `191.75` | 123,170,000.00 USD | 3,590.00 USD | 0.00 USD | `+97.19%` | `18.73` |
| `Live` | `Short` | `191.85` | 123,220,000.00 USD | 47,960.00 USD | 0.00 USD | `+97.29%` | `250.00` |
| `Live` | `Short` | `191.95` | 123,220,000.00 USD | 5,760.00 USD | 0.00 USD | `+97.40%` | `30.02` |
| `Live` | `Short` | `192.55` | 123,220,000.00 USD | 281.12 USD | 0.00 USD | `+98.01%` | `1.46` |
| `Live` | `Short` | `193.15` | 123,220,000.00 USD | 193.15 USD | 0.00 USD | `+98.63%` | `1.00` |
| `Live` | `Short` | `193.55` | 123,340,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.04%` | `592.00` |
| `Live` | `Short` | `194.05` | 123,350,000.00 USD | 9,370.00 USD | 0.00 USD | `+99.56%` | `48.28` |
| `Live` | `Short` | `194.25` | 123,350,000.00 USD | 1,390.00 USD | 0.00 USD | `+99.76%` | `7.13` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,240,000.00 USD | 0.00 USD | 14,170.00 USD | `-76.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,230,000.00 USD | 0.00 USD | 499.56 USD | `-68.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 10,230,000.00 USD | 0.00 USD | 1,230.00 USD | `-67.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,230,000.00 USD | 0.00 USD | 818.32 USD | `-66.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,230,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 10,220,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 10,220,000.00 USD | 0.00 USD | 434.85 USD | `-62.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 10,220,000.00 USD | 0.00 USD | 267.87 USD | `-60.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,220,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,220,000.00 USD | 0.00 USD | 157.01 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,220,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 10,220,000.00 USD | 0.00 USD | 120.66 USD | `-57.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 10,220,000.00 USD | 0.00 USD | 121.81 USD | `-56.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,220,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 10,050,000.00 USD | 0.00 USD | 105.00 USD | `-55.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 10,050,000.00 USD | 0.00 USD | 59,730.00 USD | `-53.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 9,990,000.00 USD | 0.00 USD | 251.05 USD | `-51.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 9,990,000.00 USD | 0.00 USD | 143.25 USD | `-50.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 9,990,000.00 USD | 0.00 USD | 191.40 USD | `-50.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 9,990,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 9,940,000.00 USD | 0.00 USD | 664.65 USD | `-50.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 9,930,000.00 USD | 0.00 USD | 103.35 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 9,930,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 9,930,000.00 USD | 0.00 USD | 107.03 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 9,930,000.00 USD | 0.00 USD | 102.62 USD | `-48.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 9,930,000.00 USD | 0.00 USD | 134.28 USD | `-47.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 9,930,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 9,930,000.00 USD | 0.00 USD | 102.74 USD | `-46.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 9,930,000.00 USD | 0.00 USD | 126.12 USD | `-45.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 9,930,000.00 USD | 0.00 USD | 200.15 USD | `-45.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 9,920,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 9,900,000.00 USD | 0.00 USD | 1,660.00 USD | `-45.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 9,900,000.00 USD | 0.00 USD | 641.57 USD | `-44.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 9,900,000.00 USD | 0.00 USD | 139.87 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 9,900,000.00 USD | 0.00 USD | 209.19 USD | `-43.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 9,900,000.00 USD | 0.00 USD | 4,350.00 USD | `-42.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 9,890,000.00 USD | 0.00 USD | 894.56 USD | `-42.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 9,890,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 9,890,000.00 USD | 0.00 USD | 6,790.00 USD | `-41.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 9,880,000.00 USD | 0.00 USD | 265.53 USD | `-41.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 9,880,000.00 USD | 0.00 USD | 268.31 USD | `-40.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 9,880,000.00 USD | 0.00 USD | 158.48 USD | `-40.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 9,880,000.00 USD | 0.00 USD | 3,820.00 USD | `-40.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 9,880,000.00 USD | 0.00 USD | 428.72 USD | `-40.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 9,880,000.00 USD | 0.00 USD | 295.25 USD | `-39.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 9,880,000.00 USD | 0.00 USD | 200.01 USD | `-38.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 9,880,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 9,870,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 9,860,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 9,830,000.00 USD | 0.00 USD | 2,820.00 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 9,830,000.00 USD | 0.00 USD | 488.63 USD | `-38.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 9,830,000.00 USD | 0.00 USD | 258.90 USD | `-37.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 9,830,000.00 USD | 0.00 USD | 206.13 USD | `-37.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 9,830,000.00 USD | 0.00 USD | 724.78 USD | `-37.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 9,830,000.00 USD | 0.00 USD | 14,350.00 USD | `-37.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 9,810,000.00 USD | 0.00 USD | 142.33 USD | `-36.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 9,810,000.00 USD | 0.00 USD | 100.78 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 9,810,000.00 USD | 0.00 USD | 243.74 USD | `-36.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 9,810,000.00 USD | 0.00 USD | 6,720.00 USD | `-36.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 9,800,000.00 USD | 0.00 USD | 136.98 USD | `-35.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 9,800,000.00 USD | 0.00 USD | 9,990.00 USD | `-35.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 9,790,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 9,790,000.00 USD | 0.00 USD | 222.55 USD | `-34.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 9,790,000.00 USD | 0.00 USD | 163.19 USD | `-33.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 9,790,000.00 USD | 0.00 USD | 129.70 USD | `-33.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 9,790,000.00 USD | 0.00 USD | 2,450.00 USD | `-33.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 9,790,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 9,790,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 9,780,000.00 USD | 0.00 USD | 7,100.00 USD | `-32.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 9,780,000.00 USD | 0.00 USD | 541.72 USD | `-31.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 9,780,000.00 USD | 0.00 USD | 335.25 USD | `-31.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 9,780,000.00 USD | 0.00 USD | 268.60 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 9,780,000.00 USD | 0.00 USD | 13,310.00 USD | `-30.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 9,760,000.00 USD | 0.00 USD | 7,600.00 USD | `-29.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 9,750,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 9,750,000.00 USD | 0.00 USD | 552.63 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 9,750,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 9,750,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 9,740,000.00 USD | 0.00 USD | 172.18 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 9,740,000.00 USD | 0.00 USD | 668.96 USD | `-28.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 9,730,000.00 USD | 0.00 USD | 107.96 USD | `-28.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 9,730,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 9,690,000.00 USD | 0.00 USD | 365.32 USD | `-28.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 9,690,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 9,690,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 9,650,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 9,640,000.00 USD | 0.00 USD | 562.80 USD | `-27.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 9,640,000.00 USD | 0.00 USD | 681.51 USD | `-27.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 9,640,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 9,630,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 9,630,000.00 USD | 0.00 USD | 265.02 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 9,630,000.00 USD | 0.00 USD | 32,450.00 USD | `-26.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 9,600,000.00 USD | 0.00 USD | 289.37 USD | `-26.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 9,600,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 9,600,000.00 USD | 0.00 USD | 235.34 USD | `-26.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 9,600,000.00 USD | 0.00 USD | 2,300.00 USD | `-25.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 9,590,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 9,580,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 9,560,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 9,490,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 9,490,000.00 USD | 0.00 USD | 733.50 USD | `-24.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 9,490,000.00 USD | 0.00 USD | 139.56 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 9,490,000.00 USD | 0.00 USD | 510.95 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 9,490,000.00 USD | 0.00 USD | 621.47 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 9,480,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 9,480,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 9,470,000.00 USD | 0.00 USD | 331.00 USD | `-23.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 9,470,000.00 USD | 0.00 USD | 28,050.00 USD | `-23.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 9,440,000.00 USD | 0.00 USD | 27,010.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 9,420,000.00 USD | 0.00 USD | 153.71 USD | `-22.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 9,420,000.00 USD | 0.00 USD | 163.73 USD | `-22.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,420,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,410,000.00 USD | 0.00 USD | 277.98 USD | `-21.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,410,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,410,000.00 USD | 0.00 USD | 254.34 USD | `-21.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,400,000.00 USD | 0.00 USD | 486.47 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 9,400,000.00 USD | 0.00 USD | 358.84 USD | `-21.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,400,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,400,000.00 USD | 0.00 USD | 536.55 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,400,000.00 USD | 0.00 USD | 251.74 USD | `-21.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,400,000.00 USD | 0.00 USD | 5,000.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,390,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 9,390,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.55` | 9,390,000.00 USD | 0.00 USD | 242.73 USD | `-20.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,390,000.00 USD | 0.00 USD | 155.12 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,390,000.00 USD | 0.00 USD | 60,010.00 USD | `-19.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,330,000.00 USD | 0.00 USD | 532.98 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,330,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 9,310,000.00 USD | 0.00 USD | 116.40 USD | `-19.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,310,000.00 USD | 0.00 USD | 5,300.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,300,000.00 USD | 0.00 USD | 201.04 USD | `-18.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,300,000.00 USD | 0.00 USD | 2,140.00 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,300,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,290,000.00 USD | 0.00 USD | 238.95 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 9,290,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 9,290,000.00 USD | 0.00 USD | 289.06 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,290,000.00 USD | 0.00 USD | 808.29 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,290,000.00 USD | 0.00 USD | 40,560.00 USD | `-17.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 9,250,000.00 USD | 0.00 USD | 8,360.00 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 9,240,000.00 USD | 0.00 USD | 359.97 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 9,240,000.00 USD | 0.00 USD | 8,770.00 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 9,230,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 9,230,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 9,230,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 9,210,000.00 USD | 0.00 USD | 341.19 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,210,000.00 USD | 0.00 USD | 26,190.00 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 9,180,000.00 USD | 0.00 USD | 266.50 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,180,000.00 USD | 0.00 USD | 6,260.00 USD | `-16.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 9,180,000.00 USD | 0.00 USD | 572.48 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,170,000.00 USD | 0.00 USD | 806.70 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 9,170,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 9,170,000.00 USD | 0.00 USD | 818.50 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,170,000.00 USD | 0.00 USD | 70,900.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 9,100,000.00 USD | 0.00 USD | 6,750.00 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 9,090,000.00 USD | 0.00 USD | 684.31 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 9,090,000.00 USD | 0.00 USD | 486.92 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 9,090,000.00 USD | 0.00 USD | 386.22 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 9,090,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.55` | 9,090,000.00 USD | 0.00 USD | 1,310.00 USD | `-15.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 9,090,000.00 USD | 0.00 USD | 267,390.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 8,820,000.00 USD | 0.00 USD | 1,910.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 8,820,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 8,820,000.00 USD | 0.00 USD | 945.63 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 8,820,000.00 USD | 0.00 USD | 6,040.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 8,810,000.00 USD | 0.00 USD | 239.47 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 8,810,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 8,790,000.00 USD | 0.00 USD | 168.57 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 8,790,000.00 USD | 0.00 USD | 421.09 USD | `-14.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 8,790,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 8,790,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 8,790,000.00 USD | 0.00 USD | 4,550.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 8,780,000.00 USD | 0.00 USD | 10,570.00 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 8,770,000.00 USD | 0.00 USD | 25,220.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 8,750,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 8,740,000.00 USD | 0.00 USD | 965.26 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 8,740,000.00 USD | 0.00 USD | 169.95 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 8,740,000.00 USD | 0.00 USD | 858.35 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 8,740,000.00 USD | 0.00 USD | 306.80 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 8,740,000.00 USD | 0.00 USD | 137.62 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 8,740,000.00 USD | 0.00 USD | 235,040.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 8,510,000.00 USD | 0.00 USD | 437.67 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 8,510,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 8,510,000.00 USD | 0.00 USD | 39,110.00 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 8,470,000.00 USD | 0.00 USD | 120.48 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 8,470,000.00 USD | 0.00 USD | 105.23 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 8,470,000.00 USD | 0.00 USD | 787.12 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 8,470,000.00 USD | 0.00 USD | 142.34 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 8,470,000.00 USD | 0.00 USD | 360.57 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 8,470,000.00 USD | 0.00 USD | 2,050.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 8,460,000.00 USD | 0.00 USD | 10,910.00 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 8,450,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 8,450,000.00 USD | 0.00 USD | 163.88 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 8,450,000.00 USD | 0.00 USD | 5,710.00 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 8,440,000.00 USD | 0.00 USD | 2,790.00 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 8,440,000.00 USD | 0.00 USD | 417.17 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 8,440,000.00 USD | 0.00 USD | 222,240.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 8,220,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 8,220,000.00 USD | 0.00 USD | 788.60 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 8,210,000.00 USD | 0.00 USD | 132.16 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 8,210,000.00 USD | 0.00 USD | 283,280.00 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,930,000.00 USD | 0.00 USD | 23,550.00 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,910,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,900,000.00 USD | 0.00 USD | 102.20 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,900,000.00 USD | 0.00 USD | 10,980.00 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,890,000.00 USD | 0.00 USD | 1,160.00 USD | `-9.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,890,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,890,000.00 USD | 0.00 USD | 131.78 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,880,000.00 USD | 0.00 USD | 1,410.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,880,000.00 USD | 0.00 USD | 132,850.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 7,750,000.00 USD | 0.00 USD | 833.02 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 7,750,000.00 USD | 0.00 USD | 1,870.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 7,750,000.00 USD | 0.00 USD | 38,020.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 7,710,000.00 USD | 0.00 USD | 867.69 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 7,710,000.00 USD | 0.00 USD | 32,280.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 7,680,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 7,650,000.00 USD | 0.00 USD | 53,390.00 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 7,600,000.00 USD | 0.00 USD | 91,430.00 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 7,500,000.00 USD | 0.00 USD | 141.43 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 7,500,000.00 USD | 0.00 USD | 12,930.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 7,490,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 7,490,000.00 USD | 0.00 USD | 1,340.00 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 7,480,000.00 USD | 0.00 USD | 4,220.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 7,480,000.00 USD | 0.00 USD | 5,620.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 7,470,000.00 USD | 0.00 USD | 348.35 USD | `-7.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 7,470,000.00 USD | 0.00 USD | 192.75 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 7,470,000.00 USD | 0.00 USD | 105.01 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 7,470,000.00 USD | 0.00 USD | 18,010.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 7,460,000.00 USD | 0.00 USD | 87,020.00 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 7,370,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 5,020,000.00 USD | 0.00 USD | 301.10 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 5,020,000.00 USD | 0.00 USD | 12,170.00 USD | `-7.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 5,010,000.00 USD | 0.00 USD | 1,400.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 5,000,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 5,000,000.00 USD | 0.00 USD | 12,520.00 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 4,990,000.00 USD | 0.00 USD | 76,690.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 4,910,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 4,910,000.00 USD | 0.00 USD | 615.96 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 4,900,000.00 USD | 0.00 USD | 8,130.00 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 4,900,000.00 USD | 0.00 USD | 627,180.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 4,270,000.00 USD | 0.00 USD | 1,120.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 4,270,000.00 USD | 0.00 USD | 1,660.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 4,270,000.00 USD | 0.00 USD | 16,980.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 4,250,000.00 USD | 0.00 USD | 920.90 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 4,250,000.00 USD | 0.00 USD | 18,290.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 4,230,000.00 USD | 0.00 USD | 37,810.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 4,190,000.00 USD | 0.00 USD | 22,140.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 4,170,000.00 USD | 0.00 USD | 41,980.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 4,130,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 2,930,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 1,750,000.00 USD | 0.00 USD | 64,260.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 1,680,000.00 USD | 0.00 USD | 22,180.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 1,660,000.00 USD | 0.00 USD | 21,200.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 1,640,000.00 USD | 0.00 USD | 5,630.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 1,630,000.00 USD | 0.00 USD | 17,280.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,620,000.00 USD | 0.00 USD | 59,380.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,560,000.00 USD | 0.00 USD | 2,260.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,560,000.00 USD | 0.00 USD | 137.42 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,560,000.00 USD | 0.00 USD | 14,800.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,540,000.00 USD | 0.00 USD | 43,190.00 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,500,000.00 USD | 0.00 USD | 134,170.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,360,000.00 USD | 0.00 USD | 9,220.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,350,000.00 USD | 0.00 USD | 1,760.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,350,000.00 USD | 0.00 USD | 6,240.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,350,000.00 USD | 0.00 USD | 1,600.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,340,000.00 USD | 0.00 USD | 1,550.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,340,000.00 USD | 0.00 USD | 4,050.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,340,000.00 USD | 0.00 USD | 1,730.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,340,000.00 USD | 0.00 USD | 472.57 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,340,000.00 USD | 0.00 USD | 111,180.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 1,230,000.00 USD | 0.00 USD | 528.18 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 1,220,000.00 USD | 0.00 USD | 3,930.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 1,220,000.00 USD | 0.00 USD | 4,780.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 1,220,000.00 USD | 0.00 USD | 69,890.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 1,150,000.00 USD | 0.00 USD | 45,050.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 1,100,000.00 USD | 0.00 USD | 33,070.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 1,070,000.00 USD | 0.00 USD | 79,700.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 988,340.00 USD | 0.00 USD | 15,150.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 973,190.00 USD | 0.00 USD | 11,540.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 961,650.00 USD | 0.00 USD | 166,820.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 794,830.00 USD | 0.00 USD | 64,210.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 730,620.00 USD | 0.00 USD | 1,480.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 729,130.00 USD | 0.00 USD | 13,990.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 715,150.00 USD | 0.00 USD | 89,160.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 625,980.00 USD | 0.00 USD | 169,260.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 456,720.00 USD | 0.00 USD | 4,730.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 451,990.00 USD | 0.00 USD | 135,460.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 316,530.00 USD | 0.00 USD | 28,080.00 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 288,450.00 USD | 0.00 USD | 44,570.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 243,880.00 USD | 0.00 USD | 84,660.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 159,220.00 USD | 0.00 USD | 25,790.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 133,440.00 USD | 0.00 USD | 9,970.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 123,470.00 USD | 0.00 USD | 5,590.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 117,880.00 USD | 0.00 USD | 10,370.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 107,510.00 USD | 0.00 USD | 16,780.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 90,720.00 USD | 0.00 USD | 25,560.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 65,170.00 USD | 0.00 USD | 6,580.00 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 58,580.00 USD | 0.00 USD | 19,320.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 39,260.00 USD | 0.00 USD | 731.97 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 38,530.00 USD | 0.00 USD | 194.10 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 38,340.00 USD | 0.00 USD | 38,340.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 27,460.00 USD | 27,460.00 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 27,610.00 USD | 149.92 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 33,980.00 USD | 6,380.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 87,060.00 USD | 53,080.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 122,720.00 USD | 35,660.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 159,580.00 USD | 36,860.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 208,600.00 USD | 49,020.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 209,670.00 USD | 1,070.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 233,430.00 USD | 23,760.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 236,150.00 USD | 2,720.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 240,640.00 USD | 4,490.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 251,340.00 USD | 10,700.00 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 277,040.00 USD | 25,700.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 290,660.00 USD | 13,610.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 318,590.00 USD | 27,930.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 375,280.00 USD | 56,690.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 401,720.00 USD | 26,440.00 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 425,770.00 USD | 24,050.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 443,610.00 USD | 17,840.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 446,770.00 USD | 3,160.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 453,700.00 USD | 6,940.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 493,090.00 USD | 39,390.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 494,860.00 USD | 1,770.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 529,320.00 USD | 34,470.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 546,370.00 USD | 17,050.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 566,310.00 USD | 19,940.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 570,040.00 USD | 3,730.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 613,080.00 USD | 43,040.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,200,000.00 USD | 590,700.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 1,210,000.00 USD | 11,150.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 1,220,000.00 USD | 3,730.00 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 1,220,000.00 USD | 1,250.00 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 1,230,000.00 USD | 6,890.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 1,230,000.00 USD | 2,700.00 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 1,230,000.00 USD | 2,370.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 1,230,000.00 USD | 911.79 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 1,230,000.00 USD | 2,010.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 1,240,000.00 USD | 2,490.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 1,460,000.00 USD | 223,790.00 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 2,680,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 2,690,000.00 USD | 8,940.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 2,690,000.00 USD | 3,850.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 2,710,000.00 USD | 18,710.00 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 2,720,000.00 USD | 5,070.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 2,720,000.00 USD | 2,400.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 2,720,000.00 USD | 1,160.00 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 2,720,000.00 USD | 2,110.00 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 2,720,000.00 USD | 928.76 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 2,830,000.00 USD | 102,510.00 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 2,830,000.00 USD | 231.88 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 2,830,000.00 USD | 3,310.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 2,830,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 2,840,000.00 USD | 7,440.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 3,010,000.00 USD | 168,300.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 3,280,000.00 USD | 268,070.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 3,280,000.00 USD | 1,280.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 3,280,000.00 USD | 1,780.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 3,290,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 3,330,000.00 USD | 42,010.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 3,330,000.00 USD | 3,180.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 3,400,000.00 USD | 64,180.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 3,400,000.00 USD | 4,260.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 3,400,000.00 USD | 3,860.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 3,420,000.00 USD | 20,580.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 3,440,000.00 USD | 17,250.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 3,440,000.00 USD | 980.44 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 3,670,000.00 USD | 226,540.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 3,730,000.00 USD | 62,400.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 3,740,000.00 USD | 13,740.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 3,750,000.00 USD | 1,850.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 3,750,000.00 USD | 519.17 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 3,750,000.00 USD | 323.49 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 3,840,000.00 USD | 95,950.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 3,870,000.00 USD | 28,050.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 3,870,000.00 USD | 680.23 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 3,870,000.00 USD | 2,150.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 3,880,000.00 USD | 5,900.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 3,910,000.00 USD | 25,930.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 4,030,000.00 USD | 122,820.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 4,060,000.00 USD | 28,780.00 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 4,080,000.00 USD | 18,380.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 4,080,000.00 USD | 1,090.00 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 4,080,000.00 USD | 266.79 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 4,080,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 4,080,000.00 USD | 235.60 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 4,080,000.00 USD | 549.90 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 4,090,000.00 USD | 10,600.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 4,100,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 4,120,000.00 USD | 19,780.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 4,120,000.00 USD | 7,080.00 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 4,120,000.00 USD | 758.62 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 4,130,000.00 USD | 7,980.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 4,160,000.00 USD | 26,170.00 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 4,160,000.00 USD | 6,950.00 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 4,170,000.00 USD | 355.14 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 4,280,000.00 USD | 110,390.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 4,280,000.00 USD | 1,730.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 4,280,000.00 USD | 2,990.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 4,420,000.00 USD | 142,930.00 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 4,420,000.00 USD | 109.29 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 4,440,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 4,440,000.00 USD | 698.85 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 4,450,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 4,510,000.00 USD | 53,110.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 4,570,000.00 USD | 65,380.00 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 4,570,000.00 USD | 536.60 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 4,580,000.00 USD | 11,350.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 4,590,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 4,680,000.00 USD | 87,120.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 4,750,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 4,750,000.00 USD | 6,900.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 4,760,000.00 USD | 2,580.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 4,760,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 4,760,000.00 USD | 666.02 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 4,760,000.00 USD | 1,010.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 4,770,000.00 USD | 1,430.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 4,810,000.00 USD | 40,920.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 4,880,000.00 USD | 73,460.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 4,890,000.00 USD | 7,660.00 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 8,830,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 8,870,000.00 USD | 31,070.00 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 8,870,000.00 USD | 5,880.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 8,870,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 8,880,000.00 USD | 5,040.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 8,880,000.00 USD | 1,370.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 8,880,000.00 USD | 1,420.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 8,880,000.00 USD | 357.34 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 9,410,000.00 USD | 525,550.00 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 9,410,000.00 USD | 4,150.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 9,410,000.00 USD | 102.53 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 9,410,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 9,410,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 9,420,000.00 USD | 10,280.00 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 9,430,000.00 USD | 3,030.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 9,440,000.00 USD | 17,520.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 9,520,000.00 USD | 74,620.00 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 9,580,000.00 USD | 64,770.00 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 9,580,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 9,590,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 9,590,000.00 USD | 585.11 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 9,590,000.00 USD | 852.24 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 9,620,000.00 USD | 22,910.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 9,620,000.00 USD | 2,420.00 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 9,620,000.00 USD | 2,100.00 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 9,630,000.00 USD | 14,960.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 9,680,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 9,690,000.00 USD | 5,260.00 USD | 0.00 USD | `+15.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 9,690,000.00 USD | 4,920.00 USD | 0.00 USD | `+15.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 9,700,000.00 USD | 953.58 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 9,730,000.00 USD | 36,280.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 9,740,000.00 USD | 6,710.00 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 9,740,000.00 USD | 586.82 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 9,820,000.00 USD | 81,560.00 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 9,820,000.00 USD | 710.08 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 9,860,000.00 USD | 35,250.00 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 9,860,000.00 USD | 655.74 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 9,860,000.00 USD | 4,470.00 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 9,860,000.00 USD | 230.71 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 9,860,000.00 USD | 257.07 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 9,870,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 9,870,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 9,870,000.00 USD | 122.14 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 9,870,000.00 USD | 907.14 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 9,870,000.00 USD | 740.99 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 9,870,000.00 USD | 343.35 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 9,870,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 9,870,000.00 USD | 105.48 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 9,870,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 9,880,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 9,960,000.00 USD | 83,040.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 9,960,000.00 USD | 309.14 USD | 0.00 USD | `+18.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 9,960,000.00 USD | 346.35 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 9,960,000.00 USD | 2,440.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 9,970,000.00 USD | 7,440.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 9,970,000.00 USD | 579.25 USD | 0.00 USD | `+19.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 9,980,000.00 USD | 6,400.00 USD | 0.00 USD | `+19.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 9,980,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 9,980,000.00 USD | 1,920.00 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 9,980,000.00 USD | 2,870.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,000,000.00 USD | 14,010.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,000,000.00 USD | 6,000.00 USD | 0.00 USD | `+19.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,010,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,010,000.00 USD | 234.87 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,020,000.00 USD | 12,860.00 USD | 0.00 USD | `+20.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,020,000.00 USD | 4,200.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,020,000.00 USD | 584.58 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,030,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,030,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,150,000.00 USD | 118,690.00 USD | 0.00 USD | `+20.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,250,000.00 USD | 106,330.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,260,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,320,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 10,380,000.00 USD | 69,220.00 USD | 0.00 USD | `+21.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 10,390,000.00 USD | 3,980.00 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 10,390,000.00 USD | 4,460.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 10,390,000.00 USD | 127.82 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 10,390,000.00 USD | 707.15 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 10,400,000.00 USD | 1,260.00 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 10,400,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 10,400,000.00 USD | 403.75 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 10,410,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 10,460,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 10,510,000.00 USD | 52,430.00 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 10,520,000.00 USD | 15,130.00 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 10,530,000.00 USD | 1,850.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 10,530,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 10,530,000.00 USD | 310.57 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 10,530,000.00 USD | 615.00 USD | 0.00 USD | `+23.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 10,660,000.00 USD | 126,700.00 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 10,700,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 10,700,000.00 USD | 458.21 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 10,870,000.00 USD | 177,600.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 10,870,000.00 USD | 414.52 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 10,880,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 10,880,000.00 USD | 7,850.00 USD | 0.00 USD | `+23.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 10,900,000.00 USD | 13,560.00 USD | 0.00 USD | `+23.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 10,900,000.00 USD | 904.13 USD | 0.00 USD | `+23.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 10,900,000.00 USD | 191.83 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 10,900,000.00 USD | 663.47 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 10,920,000.00 USD | 20,960.00 USD | 0.00 USD | `+24.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 10,920,000.00 USD | 122.36 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 10,930,000.00 USD | 11,200.00 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 10,940,000.00 USD | 11,570.00 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 10,950,000.00 USD | 7,860.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 10,960,000.00 USD | 4,430.00 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 10,960,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 10,960,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 11,040,000.00 USD | 80,260.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,230,000.00 USD | 192,930.00 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,230,000.00 USD | 1,000.00 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 11,470,000.00 USD | 234,430.00 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 11,520,000.00 USD | 52,330.00 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 11,520,000.00 USD | 3,060.00 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 11,530,000.00 USD | 7,020.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 11,540,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 11,540,000.00 USD | 104.34 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 11,550,000.00 USD | 3,850.00 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 11,560,000.00 USD | 16,430.00 USD | 0.00 USD | `+26.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 12,570,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 12,570,000.00 USD | 252.46 USD | 0.00 USD | `+26.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 12,580,000.00 USD | 7,710.00 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 12,590,000.00 USD | 6,790.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 12,590,000.00 USD | 2,670.00 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 12,590,000.00 USD | 632.58 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 12,600,000.00 USD | 11,550.00 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 12,610,000.00 USD | 5,530.00 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 12,630,000.00 USD | 18,470.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 12,640,000.00 USD | 16,360.00 USD | 0.00 USD | `+27.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 12,640,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 12,640,000.00 USD | 151.59 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 12,650,000.00 USD | 4,240.00 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 12,650,000.00 USD | 1,370.00 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 12,660,000.00 USD | 7,330.00 USD | 0.00 USD | `+28.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 12,660,000.00 USD | 6,610.00 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 12,660,000.00 USD | 596.78 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 12,670,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,230,000.00 USD | 554,250.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,230,000.00 USD | 603.22 USD | 0.00 USD | `+28.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,230,000.00 USD | 311.87 USD | 0.00 USD | `+28.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,240,000.00 USD | 6,780.00 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,240,000.00 USD | 993.56 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,250,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,250,000.00 USD | 471.94 USD | 0.00 USD | `+29.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,250,000.00 USD | 209.08 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 13,410,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 13,410,000.00 USD | 189.23 USD | 0.00 USD | `+29.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 13,410,000.00 USD | 187.15 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 13,410,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 13,420,000.00 USD | 7,460.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 13,610,000.00 USD | 190,580.00 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 13,610,000.00 USD | 534.87 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 13,610,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 13,620,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 13,620,000.00 USD | 362.81 USD | 0.00 USD | `+31.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 13,680,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 13,680,000.00 USD | 482.37 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 13,680,000.00 USD | 3,700.00 USD | 0.00 USD | `+31.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 13,690,000.00 USD | 3,010.00 USD | 0.00 USD | `+31.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 13,690,000.00 USD | 191.09 USD | 0.00 USD | `+31.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 13,730,000.00 USD | 41,130.00 USD | 0.00 USD | `+32.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 13,740,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 13,790,000.00 USD | 50,720.00 USD | 0.00 USD | `+32.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 13,790,000.00 USD | 229.89 USD | 0.00 USD | `+32.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 13,810,000.00 USD | 15,330.00 USD | 0.00 USD | `+32.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 13,810,000.00 USD | 401.29 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 13,810,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 13,810,000.00 USD | 152.99 USD | 0.00 USD | `+33.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 13,810,000.00 USD | 153.10 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 13,810,000.00 USD | 116.87 USD | 0.00 USD | `+33.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 13,860,000.00 USD | 51,520.00 USD | 0.00 USD | `+33.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 13,860,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 13,870,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 13,870,000.00 USD | 192.06 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 13,870,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 13,870,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 13,880,000.00 USD | 10,140.00 USD | 0.00 USD | `+34.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 13,890,000.00 USD | 6,000.00 USD | 0.00 USD | `+34.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 13,890,000.00 USD | 5,950.00 USD | 0.00 USD | `+34.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 13,900,000.00 USD | 8,820.00 USD | 0.00 USD | `+34.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 13,900,000.00 USD | 135.39 USD | 0.00 USD | `+35.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 14,060,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 14,060,000.00 USD | 144.93 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 14,080,000.00 USD | 12,390.00 USD | 0.00 USD | `+35.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 14,080,000.00 USD | 397.95 USD | 0.00 USD | `+36.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 14,090,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 14,090,000.00 USD | 3,910.00 USD | 0.00 USD | `+36.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 14,090,000.00 USD | 267.43 USD | 0.00 USD | `+36.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 14,090,000.00 USD | 509.96 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 14,090,000.00 USD | 191.88 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 14,090,000.00 USD | 237.36 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 14,090,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 14,090,000.00 USD | 112.35 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 14,100,000.00 USD | 4,620.00 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,150,000.00 USD | 54,080.00 USD | 0.00 USD | `+37.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,150,000.00 USD | 331.60 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 14,420,000.00 USD | 270,270.00 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 14,420,000.00 USD | 668.86 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 14,540,000.00 USD | 116,220.00 USD | 0.00 USD | `+38.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 14,550,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 14,550,000.00 USD | 1,890.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 14,550,000.00 USD | 192.25 USD | 0.00 USD | `+40.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 14,550,000.00 USD | 465.29 USD | 0.00 USD | `+40.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 14,550,000.00 USD | 389.17 USD | 0.00 USD | `+40.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 14,550,000.00 USD | 826.57 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 14,550,000.00 USD | 231.61 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 14,550,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 14,560,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 14,580,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 14,580,000.00 USD | 133.62 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 14,600,000.00 USD | 14,550.00 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 14,600,000.00 USD | 692.25 USD | 0.00 USD | `+42.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 14,600,000.00 USD | 447.84 USD | 0.00 USD | `+42.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 21,340,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+42.79%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 21,340,000.00 USD | 826.75 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 23,530,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+43.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 23,540,000.00 USD | 5,920.00 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 23,650,000.00 USD | 110,660.00 USD | 0.00 USD | `+44.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 23,660,000.00 USD | 12,120.00 USD | 0.00 USD | `+44.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 23,760,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 23,760,000.00 USD | 990.88 USD | 0.00 USD | `+44.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 23,770,000.00 USD | 12,080.00 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 23,780,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 23,780,000.00 USD | 796.07 USD | 0.00 USD | `+45.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 23,780,000.00 USD | 826.73 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 23,780,000.00 USD | 278.56 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 24,110,000.00 USD | 329,100.00 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 24,180,000.00 USD | 72,610.00 USD | 0.00 USD | `+47.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 24,200,000.00 USD | 16,980.00 USD | 0.00 USD | `+47.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 24,200,000.00 USD | 528.96 USD | 0.00 USD | `+47.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 24,210,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 24,210,000.00 USD | 415.44 USD | 0.00 USD | `+48.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 24,490,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 24,500,000.00 USD | 7,260.00 USD | 0.00 USD | `+48.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 24,500,000.00 USD | 791.78 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 24,540,000.00 USD | 36,040.00 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 24,540,000.00 USD | 209.16 USD | 0.00 USD | `+49.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 24,540,000.00 USD | 698.64 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 24,730,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 24,730,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 24,730,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 24,730,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 24,770,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 24,770,000.00 USD | 844.89 USD | 0.00 USD | `+51.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 24,780,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 24,780,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 26,120,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 26,120,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 26,130,000.00 USD | 4,760.00 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 26,130,000.00 USD | 549.99 USD | 0.00 USD | `+53.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 26,640,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 26,890,000.00 USD | 249,190.00 USD | 0.00 USD | `+54.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 26,890,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 26,890,000.00 USD | 178.92 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 26,890,000.00 USD | 1,360.00 USD | 0.00 USD | `+54.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 26,900,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 26,900,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 26,900,000.00 USD | 411.94 USD | 0.00 USD | `+55.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.85` | 26,900,000.00 USD | 137.57 USD | 0.00 USD | `+57.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 26,920,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 26,920,000.00 USD | 1,020.00 USD | 0.00 USD | `+58.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 26,930,000.00 USD | 12,000.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 26,930,000.00 USD | 113.04 USD | 0.00 USD | `+59.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 26,930,000.00 USD | 1,830.00 USD | 0.00 USD | `+59.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 26,950,000.00 USD | 22,680.00 USD | 0.00 USD | `+59.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 26,970,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 26,970,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.95` | 26,980,000.00 USD | 3,340.00 USD | 0.00 USD | `+61.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 26,980,000.00 USD | 6,640.00 USD | 0.00 USD | `+62.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 27,000,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 27,000,000.00 USD | 692.30 USD | 0.00 USD | `+63.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 27,000,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 27,090,000.00 USD | 89,040.00 USD | 0.00 USD | `+64.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 27,100,000.00 USD | 4,080.00 USD | 0.00 USD | `+67.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 27,190,000.00 USD | 89,230.00 USD | 0.00 USD | `+69.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 27,190,000.00 USD | 823.94 USD | 0.00 USD | `+70.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 27,190,000.00 USD | 211.39 USD | 0.00 USD | `+71.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 27,190,000.00 USD | 307.19 USD | 0.00 USD | `+71.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 27,190,000.00 USD | 593.03 USD | 0.00 USD | `+71.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 27,190,000.00 USD | 1,440.00 USD | 0.00 USD | `+72.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 27,200,000.00 USD | 5,720.00 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 27,200,000.00 USD | 495.09 USD | 0.00 USD | `+74.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 27,200,000.00 USD | 912.63 USD | 0.00 USD | `+74.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 27,240,000.00 USD | 43,480.00 USD | 0.00 USD | `+74.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 27,240,000.00 USD | 686.20 USD | 0.00 USD | `+76.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 27,280,000.00 USD | 35,280.00 USD | 0.00 USD | `+76.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 27,280,000.00 USD | 703.60 USD | 0.00 USD | `+77.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 27,280,000.00 USD | 3,160.00 USD | 0.00 USD | `+77.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 27,280,000.00 USD | 1,430.00 USD | 0.00 USD | `+79.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 27,330,000.00 USD | 52,520.00 USD | 0.00 USD | `+80.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 27,360,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 27,360,000.00 USD | 1,450.00 USD | 0.00 USD | `+81.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 27,360,000.00 USD | 885.25 USD | 0.00 USD | `+82.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 27,360,000.00 USD | 2,990.00 USD | 0.00 USD | `+83.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 27,360,000.00 USD | 261.56 USD | 0.00 USD | `+84.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 27,440,000.00 USD | 80,290.00 USD | 0.00 USD | `+85.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 27,440,000.00 USD | 2,440.00 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 27,450,000.00 USD | 349.34 USD | 0.00 USD | `+87.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 27,460,000.00 USD | 19,620.00 USD | 0.00 USD | `+87.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 28,020,000.00 USD | 550,350.00 USD | 0.00 USD | `+88.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 28,040,000.00 USD | 29,610.00 USD | 0.00 USD | `+90.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 28,210,000.00 USD | 165,580.00 USD | 0.00 USD | `+92.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 28,350,000.00 USD | 141,190.00 USD | 0.00 USD | `+93.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `189.05` | 28,370,000.00 USD | 15,340.00 USD | 0.00 USD | `+94.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 28,400,000.00 USD | 35,880.00 USD | 0.00 USD | `+95.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 28,400,000.00 USD | 744.27 USD | 0.00 USD | `+95.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 28,410,000.00 USD | 7,750.00 USD | 0.00 USD | `+96.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 28,420,000.00 USD | 4,270.00 USD | 0.00 USD | `+99.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `83.40` | 169,610,000.00 USD | 0.00 USD | 169,610,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD |
| `7D` | `83.60` | 169,570,000.00 USD | 0.00 USD | 169,570,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD |
| `7D` | `83.80` | 169,560,000.00 USD | 0.00 USD | 169,560,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `84.20` | 169,550,000.00 USD | 0.00 USD | 169,550,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.40` | 169,530,000.00 USD | 0.00 USD | 169,530,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.20` | 169,500,000.00 USD | 0.00 USD | 169,500,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD |
| `7D` | `85.40` | 169,280,000.00 USD | 0.00 USD | 169,280,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD |
| `7D` | `85.60` | 169,080,000.00 USD | 0.00 USD | 169,080,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.80` | 168,890,000.00 USD | 0.00 USD | 168,890,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.20` | 168,630,000.00 USD | 0.00 USD | 168,630,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD |
| `7D` | `86.40` | 168,420,000.00 USD | 0.00 USD | 168,420,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD |
| `1D` | `86.70` | 180,650,000.00 USD | 0.00 USD | 180,650,000.00 USD | 5,980.00 USD | 367,860.00 USD | 76,300.00 USD |
| `7D` | `86.80` | 168,100,000.00 USD | 0.00 USD | 168,100,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD |
| `1D` | `86.90` | 180,200,000.00 USD | 0.00 USD | 180,200,000.00 USD | 330,140.00 USD | 382,120.00 USD | 267,630.00 USD |
| `7D` | `87.00` | 167,950,000.00 USD | 0.00 USD | 167,950,000.00 USD | 271,000.00 USD | 183,160.00 USD | 310,380.00 USD |
| `1D` | `87.10` | 179,220,000.00 USD | 0.00 USD | 179,220,000.00 USD | 121,630.00 USD | 119,130.00 USD | 301,060.00 USD |
| `7D` | `87.20` | 167,190,000.00 USD | 0.00 USD | 167,190,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD |
| `1D` | `87.30` | 178,680,000.00 USD | 0.00 USD | 178,680,000.00 USD | 254,340.00 USD | 268,220.00 USD | 308,570.00 USD |
| `7D` | `87.40` | 167,160,000.00 USD | 0.00 USD | 167,160,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD |
| `1D` | `87.50` | 177,850,000.00 USD | 0.00 USD | 177,850,000.00 USD | 158,670.00 USD | 252,960.00 USD | 86,480.00 USD |
| `7D` | `87.60` | 166,400,000.00 USD | 0.00 USD | 166,400,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD |
| `1D` | `87.70` | 177,350,000.00 USD | 0.00 USD | 177,350,000.00 USD | 8,600.00 USD | 250,230.00 USD | 263,600.00 USD |
| `7D` | `87.80` | 165,710,000.00 USD | 0.00 USD | 165,710,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD |
| `1D` | `87.90` | 176,830,000.00 USD | 0.00 USD | 176,830,000.00 USD | 134,550.00 USD | 427,430.00 USD | 933,540.00 USD |
| `7D` | `88.00` | 165,280,000.00 USD | 0.00 USD | 165,280,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD |
| `1D` | `88.10` | 175,330,000.00 USD | 0.00 USD | 175,330,000.00 USD | 59,290.00 USD | 35,690.00 USD | 232,180.00 USD |
| `7D` | `88.20` | 165,020,000.00 USD | 0.00 USD | 165,020,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD |
| `1D` | `88.30` | 175,000,000.00 USD | 0.00 USD | 175,000,000.00 USD | 116,980.00 USD | 275,350.00 USD | 276,140.00 USD |
| `7D` | `88.40` | 164,960,000.00 USD | 0.00 USD | 164,960,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `88.50` | 174,340,000.00 USD | 0.00 USD | 174,340,000.00 USD | 86,840.00 USD | 99,900.00 USD | 0.00 USD |
| `1D` | `88.70` | 174,150,000.00 USD | 0.00 USD | 174,150,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,360.00 USD |
| `7D` | `88.80` | 164,390,000.00 USD | 0.00 USD | 164,390,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.90` | 173,400,000.00 USD | 0.00 USD | 173,400,000.00 USD | 143,140.00 USD | 62,660.00 USD | 214,680.00 USD |
| `7D` | `89.00` | 164,140,000.00 USD | 0.00 USD | 164,140,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `1D` | `89.10` | 172,980,000.00 USD | 0.00 USD | 172,980,000.00 USD | 160,900.00 USD | 83,520.00 USD | 22,410.00 USD |
| `7D` | `89.20` | 163,210,000.00 USD | 0.00 USD | 163,210,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD |
| `1D` | `89.30` | 172,720,000.00 USD | 0.00 USD | 172,720,000.00 USD | 221,290.00 USD | 284,680.00 USD | 2,740.00 USD |
| `7D` | `89.40` | 162,880,000.00 USD | 0.00 USD | 162,880,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD |
| `1D` | `89.50` | 172,210,000.00 USD | 0.00 USD | 172,210,000.00 USD | 4,870.00 USD | 50,620.00 USD | 293,050.00 USD |
| `7D` | `89.60` | 161,990,000.00 USD | 0.00 USD | 161,990,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.70` | 171,860,000.00 USD | 0.00 USD | 171,860,000.00 USD | 133,580.00 USD | 30,600.00 USD | 423,020.00 USD |
| `7D` | `89.80` | 160,310,000.00 USD | 0.00 USD | 160,310,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD |
| `1D` | `89.90` | 171,270,000.00 USD | 0.00 USD | 171,270,000.00 USD | 129,660.00 USD | 91,010.00 USD | 144,940.00 USD |
| `7D` | `90.00` | 159,260,000.00 USD | 0.00 USD | 159,260,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD |
| `1D` | `90.10` | 170,910,000.00 USD | 0.00 USD | 170,910,000.00 USD | 1,080,000.00 USD | 892,740.00 USD | 573,360.00 USD |
| `7D` | `90.20` | 157,140,000.00 USD | 0.00 USD | 157,140,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD |
| `1D` | `90.30` | 168,360,000.00 USD | 0.00 USD | 168,360,000.00 USD | 661,900.00 USD | 443,900.00 USD | 346,050.00 USD |
| `7D` | `90.40` | 154,560,000.00 USD | 0.00 USD | 154,560,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD |
| `1D` | `90.50` | 166,910,000.00 USD | 0.00 USD | 166,910,000.00 USD | 630,230.00 USD | 452,810.00 USD | 814,130.00 USD |
| `7D` | `90.60` | 153,000,000.00 USD | 0.00 USD | 153,000,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD |
| `1D` | `90.70` | 165,010,000.00 USD | 0.00 USD | 165,010,000.00 USD | 628,630.00 USD | 803,190.00 USD | 348,330.00 USD |
| `7D` | `90.80` | 149,390,000.00 USD | 0.00 USD | 149,390,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD |
| `1D` | `90.90` | 163,230,000.00 USD | 0.00 USD | 163,230,000.00 USD | 673,680.00 USD | 420,760.00 USD | 91,240.00 USD |
| `7D` | `91.00` | 145,500,000.00 USD | 0.00 USD | 145,500,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD |
| `1D` | `91.10` | 162,040,000.00 USD | 0.00 USD | 162,040,000.00 USD | 436,270.00 USD | 732,110.00 USD | 467,290.00 USD |
| `7D` | `91.20` | 142,890,000.00 USD | 0.00 USD | 142,890,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD |
| `1D` | `91.30` | 160,410,000.00 USD | 0.00 USD | 160,410,000.00 USD | 150,320.00 USD | 221,290.00 USD | 484,170.00 USD |
| `7D` | `91.40` | 139,110,000.00 USD | 0.00 USD | 139,110,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD |
| `1D` | `91.50` | 159,550,000.00 USD | 0.00 USD | 159,550,000.00 USD | 850,930.00 USD | 781,420.00 USD | 644,560.00 USD |
| `7D` | `91.60` | 135,280,000.00 USD | 0.00 USD | 135,280,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD |
| `1D` | `91.70` | 157,270,000.00 USD | 0.00 USD | 157,270,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,170,000.00 USD |
| `7D` | `91.80` | 132,890,000.00 USD | 0.00 USD | 132,890,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD |
| `1D` | `91.90` | 155,370,000.00 USD | 0.00 USD | 155,370,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 652,430.00 USD |
| `7D` | `92.00` | 130,470,000.00 USD | 0.00 USD | 130,470,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD |
| `1D` | `92.10` | 152,620,000.00 USD | 0.00 USD | 152,620,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 577,390.00 USD |
| `7D` | `92.20` | 128,140,000.00 USD | 0.00 USD | 128,140,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD |
| `1D` | `92.30` | 147,060,000.00 USD | 0.00 USD | 147,060,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD |
| `7D` | `92.40` | 123,880,000.00 USD | 0.00 USD | 123,880,000.00 USD | 550,500.00 USD | 843,410.00 USD | 1,540,000.00 USD |
| `1D` | `92.50` | 144,140,000.00 USD | 0.00 USD | 144,140,000.00 USD | 1,300,000.00 USD | 712,060.00 USD | 2,560,000.00 USD |
| `7D` | `92.60` | 120,950,000.00 USD | 0.00 USD | 120,950,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,690,000.00 USD |
| `1D` | `92.70` | 139,570,000.00 USD | 0.00 USD | 139,570,000.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | 1,680,000.00 USD |
| `7D` | `92.80` | 118,280,000.00 USD | 0.00 USD | 118,280,000.00 USD | 463,730.00 USD | 2,370,000.00 USD | 1,640,000.00 USD |
| `1D` | `92.90` | 135,680,000.00 USD | 0.00 USD | 135,680,000.00 USD | 3,420,000.00 USD | 2,100,000.00 USD | 2,850,000.00 USD |
| `7D` | `93.00` | 113,800,000.00 USD | 0.00 USD | 113,800,000.00 USD | 708,990.00 USD | 557,320.00 USD | 2,030,000.00 USD |
| `1D` | `93.10` | 127,310,000.00 USD | 0.00 USD | 127,310,000.00 USD | 2,850,000.00 USD | 3,470,000.00 USD | 2,250,000.00 USD |
| `7D` | `93.20` | 110,510,000.00 USD | 0.00 USD | 110,510,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD |
| `1D` | `93.30` | 118,730,000.00 USD | 0.00 USD | 118,730,000.00 USD | 3,040,000.00 USD | 3,230,000.00 USD | 1,530,000.00 USD |
| `7D` | `93.40` | 106,620,000.00 USD | 0.00 USD | 106,620,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `1D` | `93.50` | 110,930,000.00 USD | 0.00 USD | 110,930,000.00 USD | 3,020,000.00 USD | 2,340,000.00 USD | 2,350,000.00 USD |
| `7D` | `93.60` | 101,910,000.00 USD | 0.00 USD | 101,910,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD |
| `1D` | `93.70` | 103,220,000.00 USD | 0.00 USD | 103,220,000.00 USD | 640,730.00 USD | 3,170,000.00 USD | 960,280.00 USD |
| `7D` | `93.80` | 98,970,000.00 USD | 0.00 USD | 98,970,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD |
| `1D` | `93.90` | 98,450,000.00 USD | 0.00 USD | 98,450,000.00 USD | 1,610,000.00 USD | 967,780.00 USD | 1,430,000.00 USD |
| `7D` | `94.00` | 93,720,000.00 USD | 0.00 USD | 93,720,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD |
| `1D` | `94.10` | 94,440,000.00 USD | 0.00 USD | 94,440,000.00 USD | 768,990.00 USD | 1,310,000.00 USD | 2,670,000.00 USD |
| `7D` | `94.20` | 87,070,000.00 USD | 0.00 USD | 87,070,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD |
| `1D` | `94.30` | 89,700,000.00 USD | 0.00 USD | 89,700,000.00 USD | 2,300,000.00 USD | 1,250,000.00 USD | 531,650.00 USD |
| `7D` | `94.40` | 83,330,000.00 USD | 0.00 USD | 83,330,000.00 USD | 0.00 USD | 515,800.00 USD | 9,790.00 USD |
| `1D` | `94.50` | 85,610,000.00 USD | 0.00 USD | 85,610,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,040,000.00 USD |
| `7D` | `94.60` | 82,810,000.00 USD | 0.00 USD | 82,810,000.00 USD | 560,570.00 USD | 0.00 USD | 432,770.00 USD |
| `1D` | `94.70` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 1,570,000.00 USD | 598,120.00 USD | 429,400.00 USD |
| `7D` | `94.80` | 81,810,000.00 USD | 0.00 USD | 81,810,000.00 USD | 2,090,000.00 USD | 152,290.00 USD | 3,430,000.00 USD |
| `1D` | `94.90` | 79,560,000.00 USD | 0.00 USD | 79,560,000.00 USD | 3,530,000.00 USD | 900,710.00 USD | 1,980,000.00 USD |
| `7D` | `95.00` | 76,140,000.00 USD | 0.00 USD | 76,140,000.00 USD | 3,740,000.00 USD | 4,780,000.00 USD | 1,570,000.00 USD |
| `1D` | `95.10` | 73,160,000.00 USD | 0.00 USD | 73,160,000.00 USD | 3,780,000.00 USD | 1,900,000.00 USD | 1,060,000.00 USD |
| `7D` | `95.20` | 66,040,000.00 USD | 0.00 USD | 66,040,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD |
| `1D` | `95.30` | 66,410,000.00 USD | 0.00 USD | 66,410,000.00 USD | 1,850,000.00 USD | 1,790,000.00 USD | 3,920,000.00 USD |
| `7D` | `95.40` | 63,290,000.00 USD | 0.00 USD | 63,290,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.50` | 58,840,000.00 USD | 0.00 USD | 58,840,000.00 USD | 833,050.00 USD | 1,690,000.00 USD | 2,370,000.00 USD |
| `7D` | `95.60` | 53,990,000.00 USD | 0.00 USD | 53,990,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 5,460,000.00 USD |
| `1D` | `95.70` | 53,950,000.00 USD | 0.00 USD | 53,950,000.00 USD | 2,410,000.00 USD | 2,670,000.00 USD | 6,470,000.00 USD |
| `7D` | `95.80` | 37,680,000.00 USD | 0.00 USD | 37,680,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 2,300,000.00 USD |
| `1D` | `95.90` | 42,400,000.00 USD | 0.00 USD | 42,400,000.00 USD | 4,490,000.00 USD | 2,100,000.00 USD | 3,920,000.00 USD |
| `7D` | `96.00` | 31,890,000.00 USD | 0.00 USD | 31,890,000.00 USD | 5,990,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD |
| `1D` | `96.10` | 31,890,000.00 USD | 0.00 USD | 31,890,000.00 USD | 4,130,000.00 USD | 5,640,000.00 USD | 5,140,000.00 USD |
| `7D` | `96.20` | 18,990,000.00 USD | 0.00 USD | 18,990,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD |
| `1D` | `96.30` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 6,740,000.00 USD | 6,040,000.00 USD | 453,420.00 USD |
| `7D` | `96.40` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 1,600,000.00 USD | 2,550,000.00 USD | 20,910.00 USD |
| `1D` | `96.50` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 1,300,000.00 USD | 1,230,000.00 USD | 328,870.00 USD |
| `7D` | `96.60` | 24,800.00 USD | 0.00 USD | 24,800.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.70` | 894,880.00 USD | 0.00 USD | 894,880.00 USD | 0.00 USD | 894,880.00 USD | 0.00 USD |
| `7D` | `97.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD |
| `1D` | `97.30` | 174,820.00 USD | 174,820.00 USD | 0.00 USD | 174,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `1D` | `97.50` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 896,130.00 USD | 1,280,000.00 USD | 844,990.00 USD |
| `7D` | `97.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 24,930.00 USD | 4,780,000.00 USD |
| `1D` | `97.70` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 512,980.00 USD | 441,570.00 USD | 2,030,000.00 USD |
| `7D` | `97.80` | 20,260,000.00 USD | 20,260,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 1,020,000.00 USD |
| `1D` | `97.90` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 4,730,000.00 USD | 690,250.00 USD | 2,210,000.00 USD |
| `7D` | `98.00` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 14,750,000.00 USD | 561,730.00 USD | 2,030,000.00 USD |
| `1D` | `98.10` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 2,790,000.00 USD | 2,530,000.00 USD | 1,190,000.00 USD |
| `7D` | `98.20` | 48,530,000.00 USD | 48,530,000.00 USD | 0.00 USD | 9,790,000.00 USD | 1,140,000.00 USD | 0.00 USD |
| `1D` | `98.30` | 29,990,000.00 USD | 29,990,000.00 USD | 0.00 USD | 2,390,000.00 USD | 941,940.00 USD | 6,330,000.00 USD |
| `7D` | `98.40` | 60,100,000.00 USD | 60,100,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,460,000.00 USD |
| `1D` | `98.50` | 41,170,000.00 USD | 41,170,000.00 USD | 0.00 USD | 847,660.00 USD | 3,490,000.00 USD | 6,850,000.00 USD |
| `7D` | `98.60` | 69,530,000.00 USD | 69,530,000.00 USD | 0.00 USD | 1,960,000.00 USD | 5,450,000.00 USD | 2,020,000.00 USD |
| `1D` | `98.70` | 58,990,000.00 USD | 58,990,000.00 USD | 0.00 USD | 1,790,000.00 USD | 5,700,000.00 USD | 10,330,000.00 USD |
| `7D` | `98.80` | 75,680,000.00 USD | 75,680,000.00 USD | 0.00 USD | 1,420,000.00 USD | 797,640.00 USD | 3,930,000.00 USD |
| `1D` | `98.90` | 71,140,000.00 USD | 71,140,000.00 USD | 0.00 USD | 2,810,000.00 USD | 3,940,000.00 USD | 5,390,000.00 USD |
| `7D` | `99.00` | 84,510,000.00 USD | 84,510,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD |
| `1D` | `99.10` | 86,980,000.00 USD | 86,980,000.00 USD | 0.00 USD | 3,640,000.00 USD | 6,370,000.00 USD | 5,830,000.00 USD |
| `7D` | `99.20` | 98,480,000.00 USD | 98,480,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD |
| `1D` | `99.30` | 96,020,000.00 USD | 96,020,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,420,000.00 USD | 2,430,000.00 USD |
| `7D` | `99.40` | 99,520,000.00 USD | 99,520,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD |
| `1D` | `99.50` | 100,980,000.00 USD | 100,980,000.00 USD | 0.00 USD | 1,560,000.00 USD | 2,630,000.00 USD | 761,870.00 USD |
| `7D` | `99.60` | 104,950,000.00 USD | 104,950,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD |
| `1D` | `99.70` | 123,500,000.00 USD | 123,500,000.00 USD | 0.00 USD | 4,400,000.00 USD | 7,120,000.00 USD | 11,010,000.00 USD |
| `7D` | `99.80` | 108,280,000.00 USD | 108,280,000.00 USD | 0.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD |
| `1D` | `99.90` | 132,290,000.00 USD | 132,290,000.00 USD | 0.00 USD | 857,690.00 USD | 1,960,000.00 USD | 5,970,000.00 USD |
| `7D` | `100.00` | 119,610,000.00 USD | 119,610,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD |
| `1D` | `100.10` | 139,550,000.00 USD | 139,550,000.00 USD | 0.00 USD | 2,220,000.00 USD | 3,440,000.00 USD | 1,600,000.00 USD |
| `7D` | `100.20` | 125,710,000.00 USD | 125,710,000.00 USD | 0.00 USD | 843,770.00 USD | 2,470,000.00 USD | 2,780,000.00 USD |
| `1D` | `100.30` | 145,450,000.00 USD | 145,450,000.00 USD | 0.00 USD | 869,050.00 USD | 2,130,000.00 USD | 2,900,000.00 USD |
| `7D` | `100.40` | 130,400,000.00 USD | 130,400,000.00 USD | 0.00 USD | 993,830.00 USD | 654,600.00 USD | 3,050,000.00 USD |
| `1D` | `100.50` | 153,220,000.00 USD | 153,220,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,270,000.00 USD | 4,200,000.00 USD |
| `7D` | `100.60` | 136,280,000.00 USD | 136,280,000.00 USD | 0.00 USD | 2,150,000.00 USD | 1,480,000.00 USD | 2,250,000.00 USD |
| `1D` | `100.70` | 161,550,000.00 USD | 161,550,000.00 USD | 0.00 USD | 2,340,000.00 USD | 2,480,000.00 USD | 3,510,000.00 USD |
| `7D` | `100.80` | 139,610,000.00 USD | 139,610,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,380,000.00 USD | 786,390.00 USD |
| `1D` | `100.90` | 169,110,000.00 USD | 169,110,000.00 USD | 0.00 USD | 2,580,000.00 USD | 2,670,000.00 USD | 2,320,000.00 USD |
| `7D` | `101.00` | 158,590,000.00 USD | 158,590,000.00 USD | 0.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD |
| `1D` | `101.10` | 182,380,000.00 USD | 182,380,000.00 USD | 0.00 USD | 7,690,000.00 USD | 2,790,000.00 USD | 2,800,000.00 USD |
| `7D` | `101.20` | 178,000,000.00 USD | 178,000,000.00 USD | 0.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD |
| `1D` | `101.30` | 192,290,000.00 USD | 192,290,000.00 USD | 0.00 USD | 3,410,000.00 USD | 3,630,000.00 USD | 2,870,000.00 USD |
| `7D` | `101.40` | 195,050,000.00 USD | 195,050,000.00 USD | 0.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD |
| `1D` | `101.50` | 206,430,000.00 USD | 206,430,000.00 USD | 0.00 USD | 3,140,000.00 USD | 3,310,000.00 USD | 7,700,000.00 USD |
| `7D` | `101.60` | 205,580,000.00 USD | 205,580,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD |
| `1D` | `101.70` | 215,870,000.00 USD | 215,870,000.00 USD | 0.00 USD | 2,080,000.00 USD | 881,090.00 USD | 6,480,000.00 USD |
| `7D` | `101.80` | 215,500,000.00 USD | 215,500,000.00 USD | 0.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD |
| `1D` | `101.90` | 221,690,000.00 USD | 221,690,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,290,000.00 USD | 2,210,000.00 USD |
| `7D` | `102.00` | 221,490,000.00 USD | 221,490,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD |
| `1D` | `102.10` | 228,150,000.00 USD | 228,150,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,440,000.00 USD | 2,060,000.00 USD |
| `7D` | `102.20` | 228,220,000.00 USD | 228,220,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD |
| `1D` | `102.30` | 232,120,000.00 USD | 232,120,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,260,000.00 USD | 1,050,000.00 USD |
| `7D` | `102.40` | 233,520,000.00 USD | 233,520,000.00 USD | 0.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD |
| `1D` | `102.50` | 236,450,000.00 USD | 236,450,000.00 USD | 0.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,030,000.00 USD |
| `7D` | `102.60` | 235,980,000.00 USD | 235,980,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD |
| `1D` | `102.70` | 238,340,000.00 USD | 238,340,000.00 USD | 0.00 USD | 1,110,000.00 USD | 660,360.00 USD | 126,010.00 USD |
| `7D` | `102.80` | 244,080,000.00 USD | 244,080,000.00 USD | 0.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD |
| `1D` | `102.90` | 242,870,000.00 USD | 242,870,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD |
| `7D` | `103.00` | 261,010,000.00 USD | 261,010,000.00 USD | 0.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD |
| `1D` | `103.10` | 247,830,000.00 USD | 247,830,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,220,000.00 USD |
| `7D` | `103.20` | 273,680,000.00 USD | 273,680,000.00 USD | 0.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD |
| `1D` | `103.30` | 249,650,000.00 USD | 249,650,000.00 USD | 0.00 USD | 334,720.00 USD | 717,010.00 USD | 773,020.00 USD |
| `7D` | `103.40` | 288,250,000.00 USD | 288,250,000.00 USD | 0.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.50` | 256,230,000.00 USD | 256,230,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD |
| `7D` | `103.60` | 306,640,000.00 USD | 306,640,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.70` | 260,940,000.00 USD | 260,940,000.00 USD | 0.00 USD | 1,370,000.00 USD | 720,260.00 USD | 2,620,000.00 USD |
| `7D` | `103.80` | 319,030,000.00 USD | 319,030,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `103.90` | 264,760,000.00 USD | 264,760,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,640,000.00 USD | 803,690.00 USD |
| `7D` | `104.00` | 345,730,000.00 USD | 345,730,000.00 USD | 0.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD |
| `1D` | `104.10` | 269,680,000.00 USD | 269,680,000.00 USD | 0.00 USD | 2,020,000.00 USD | 724,740.00 USD | 2,180,000.00 USD |
| `7D` | `104.20` | 367,760,000.00 USD | 367,760,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.30` | 272,360,000.00 USD | 272,360,000.00 USD | 0.00 USD | 1,000,000.00 USD | 971,040.00 USD | 701,650.00 USD |
| `7D` | `104.40` | 384,940,000.00 USD | 384,940,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD |
| `1D` | `104.50` | 275,510,000.00 USD | 275,510,000.00 USD | 0.00 USD | 1,200,000.00 USD | 974,960.00 USD | 968,800.00 USD |
| `7D` | `104.60` | 402,690,000.00 USD | 402,690,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD |
| `1D` | `104.70` | 281,100,000.00 USD | 281,100,000.00 USD | 0.00 USD | 1,660,000.00 USD | 910,560.00 USD | 3,020,000.00 USD |
| `7D` | `104.80` | 420,090,000.00 USD | 420,090,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD |
| `1D` | `104.90` | 282,570,000.00 USD | 282,570,000.00 USD | 0.00 USD | 486,940.00 USD | 283,560.00 USD | 703,860.00 USD |
| `7D` | `105.00` | 436,250,000.00 USD | 436,250,000.00 USD | 0.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.10` | 284,410,000.00 USD | 284,410,000.00 USD | 0.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD |
| `7D` | `105.20` | 446,920,000.00 USD | 446,920,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.30` | 284,600,000.00 USD | 284,600,000.00 USD | 0.00 USD | 94,380.00 USD | 96,460.00 USD | 3,230.00 USD |
| `7D` | `105.40` | 455,130,000.00 USD | 455,130,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD |
| `1D` | `105.50` | 285,210,000.00 USD | 285,210,000.00 USD | 0.00 USD | 245,610.00 USD | 180,000.00 USD | 188,040.00 USD |
| `7D` | `105.60` | 463,550,000.00 USD | 463,550,000.00 USD | 0.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD |
| `1D` | `105.70` | 285,430,000.00 USD | 285,430,000.00 USD | 0.00 USD | 65,040.00 USD | 150,210.00 USD | 4,800.00 USD |
| `7D` | `105.80` | 472,360,000.00 USD | 472,360,000.00 USD | 0.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD |
| `1D` | `105.90` | 286,490,000.00 USD | 286,490,000.00 USD | 0.00 USD | 177,140.00 USD | 685,100.00 USD | 191,490.00 USD |
| `7D` | `106.00` | 477,520,000.00 USD | 477,520,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD |
| `1D` | `106.10` | 287,960,000.00 USD | 287,960,000.00 USD | 0.00 USD | 706,860.00 USD | 459,510.00 USD | 301,930.00 USD |
| `7D` | `106.20` | 486,410,000.00 USD | 486,410,000.00 USD | 0.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD |
| `1D` | `106.30` | 289,160,000.00 USD | 289,160,000.00 USD | 0.00 USD | 320,000.00 USD | 488,800.00 USD | 395,540.00 USD |
| `7D` | `106.40` | 492,500,000.00 USD | 492,500,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,180,000.00 USD | 1,480,000.00 USD |
| `1D` | `106.50` | 290,090,000.00 USD | 290,090,000.00 USD | 0.00 USD | 326,070.00 USD | 292,550.00 USD | 306,350.00 USD |
| `7D` | `106.60` | 497,340,000.00 USD | 497,340,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD |
| `1D` | `106.70` | 292,620,000.00 USD | 292,620,000.00 USD | 0.00 USD | 758,730.00 USD | 310,350.00 USD | 1,470,000.00 USD |
| `7D` | `106.80` | 501,990,000.00 USD | 501,990,000.00 USD | 0.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD |
| `1D` | `106.90` | 293,440,000.00 USD | 293,440,000.00 USD | 0.00 USD | 158,670.00 USD | 336,790.00 USD | 322,640.00 USD |
| `7D` | `107.00` | 506,130,000.00 USD | 506,130,000.00 USD | 0.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD |
| `1D` | `107.10` | 294,500,000.00 USD | 294,500,000.00 USD | 0.00 USD | 97,170.00 USD | 367,640.00 USD | 596,390.00 USD |
| `7D` | `107.20` | 507,220,000.00 USD | 507,220,000.00 USD | 0.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD |
| `7D` | `107.40` | 508,510,000.00 USD | 508,510,000.00 USD | 0.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD |
| `7D` | `107.60` | 509,140,000.00 USD | 509,140,000.00 USD | 0.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD |
| `7D` | `107.80` | 509,970,000.00 USD | 509,970,000.00 USD | 0.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD |
| `7D` | `108.00` | 510,550,000.00 USD | 510,550,000.00 USD | 0.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD |
| `7D` | `108.20` | 510,830,000.00 USD | 510,830,000.00 USD | 0.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD |
| `7D` | `108.40` | 511,320,000.00 USD | 511,320,000.00 USD | 0.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.60` | 511,510,000.00 USD | 511,510,000.00 USD | 0.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD |
| `7D` | `108.80` | 512,430,000.00 USD | 512,430,000.00 USD | 0.00 USD | 350,210.00 USD | 286,220.00 USD | 287,660.00 USD |
| `7D` | `109.00` | 512,720,000.00 USD | 512,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 286,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.59B` | Total OI Tokens: `57,759,368.2 SOL`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-1.66%` | 24h OI Change: `-13.50%`
  * Exchange Breakdown: Binance=`966.72M` | Bybit=`610.70M` | OKX=`376.63M` | Hyperliquid=`516.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `99.10K` | Last 24h: `177.62K` | Last 3d: `997.77K` | Last 7d: `2.11M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0015%` |
| **USDT Bybit** | `0.0047%` | **USDT KuCoin** | `-0.0005%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0046%` | **USDT Bitget** | `-0.0071%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0026%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
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
| `1H` | `SOL` | `54.23%` | `45.77%` | `1.18` | 1,840,000,000.00 USD |
| `1H` | `Binance` | `53.06%` | `46.94%` | `1.13` | 578,840,000.00 USD |
| `1H` | `OKX` | `51.54%` | `48.46%` | `1.06` | 398,660,000.00 USD |
| `1H` | `Bybit` | `55.88%` | `44.12%` | `1.27` | 119,050,000.00 USD |
| `1H` | `KuCoin` | `68.51%` | `31.49%` | `2.18` | 12,010,000.00 USD |
| `1H` | `Gate` | `50.71%` | `49.29%` | `1.03` | 288,920,000.00 USD |
| `1H` | `Bitget` | `53.84%` | `46.16%` | `1.17` | 72,030,000.00 USD |
| `1H` | `BingX` | `59.2%` | `40.8%` | `1.45` | 33,480,000.00 USD |
| `1H` | `MEXC` | `54.52%` | `45.48%` | `1.20` | 83,080,000.00 USD |
| `1H` | `Bitunix` | `51.08%` | `48.92%` | `1.04` | 69,540,000.00 USD |
| `1H` | `Hyperliquid` | `81.65%` | `18.35%` | `4.45` | 81,210,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.24%` | `45.76%` | `1.19` | 4,240,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `76.82%` | `23.18%` | `3.31` | 13,250,000.00 USD |
| `1H` | `HTX` | `57.9%` | `42.1%` | `1.38` | 18,530,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `54.85%` | `45.15%` | `1.21` | 10,450,000.00 USD |
| `1H` | `Bitfinex` | `67.63%` | `32.37%` | `2.09` | 480,390.00 USD |
| `1H` | `Kraken` | `48.52%` | `51.48%` | `0.94` | 8,660,000.00 USD |
| `1H` | `Aster` | `52.36%` | `47.64%` | `1.10` | 28,570,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.08%` | `47.92%` | `1.09` | 22,680,000.00 USD |
| `1H` | `Whale Positions` | `53.06%` | `46.94%` | `1.13` | 578,840,000.00 USD |
| `1H` | `Global Accounts` | `54.23%` | `45.77%` | `1.18` | 1,840,000,000.00 USD |
| `4H` | `SOL` | `46.48%` | `53.52%` | `0.87` | 10,770,000,000.00 USD |
| `4H` | `Binance` | `44.28%` | `55.72%` | `0.79` | 3,140,000,000.00 USD |
| `4H` | `OKX` | `49.27%` | `50.73%` | `0.97` | 1,510,000,000.00 USD |
| `4H` | `Bybit` | `45.96%` | `54.04%` | `0.85` | 961,110,000.00 USD |
| `4H` | `KuCoin` | `51.59%` | `48.41%` | `1.07` | 29,620,000.00 USD |
| `4H` | `Gate` | `50.56%` | `49.44%` | `1.02` | 1,080,000,000.00 USD |
| `4H` | `Bitget` | `44.16%` | `55.84%` | `0.79` | 487,570,000.00 USD |
| `4H` | `BingX` | `49.63%` | `50.37%` | `0.99` | 203,010,000.00 USD |
| `4H` | `MEXC` | `46.77%` | `53.23%` | `0.88` | 515,790,000.00 USD |
| `4H` | `Bitunix` | `48.49%` | `51.51%` | `0.94` | 436,620,000.00 USD |
| `4H` | `Hyperliquid` | `43.64%` | `56.36%` | `0.77` | 619,770,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.38%` | `49.62%` | `1.02` | 693,970,000.00 USD |
| `4H` | `Crypto.com` | `47.15%` | `52.85%` | `0.89` | 37,350,000.00 USD |
| `4H` | `WhiteBIT` | `16.18%` | `83.82%` | `0.19` | 193,410,000.00 USD |
| `4H` | `HTX` | `44.94%` | `55.06%` | `0.82` | 36,960,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.43%` | `48.57%` | `1.06` | 515,160,000.00 USD |
| `4H` | `Bitfinex` | `50.22%` | `49.78%` | `1.01` | 8,360,000.00 USD |
| `4H` | `Kraken` | `47.61%` | `52.39%` | `0.91` | 71,120,000.00 USD |
| `4H` | `Aster` | `45.14%` | `54.86%` | `0.82` | 116,140,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.46%` | `48.54%` | `1.06` | 99,410,000.00 USD |
| `4H` | `Whale Positions` | `44.28%` | `55.72%` | `0.79` | 3,140,000,000.00 USD |
| `4H` | `Global Accounts` | `46.48%` | `53.52%` | `0.87` | 10,770,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `97.13` | `97.19` | `97.13` | `97.44` | `97.03` | 17,561,649.50 USD | 7,274,477.25 USD | 10,287,172.25 USD | -3,012,695.00 USD | `-17.15%` | `4B / 13S` |
| `5:00 UTC` | `96.81` | `96.94` | `96.81` | `97.16` | `96.81` | 12,337,515.78 USD | 5,226,804.15 USD | 7,110,711.63 USD | -1,883,907.48 USD | `-15.27%` | `2B / 2S` |
| `0:00 UTC` | `96.81` | `96.92` | `96.81` | `97.16` | `96.69` | 14,931,632.13 USD | 8,028,191.38 USD | 6,903,440.75 USD | 1,124,750.63 USD | `+7.53%` | `9B / 6S` |
| `5:00 UTC` | `96.80` | `96.85` | `96.80` | `97.02` | `96.73` | 9,878,254.59 USD | 5,512,052.81 USD | 4,366,201.79 USD | 1,145,851.02 USD | `+11.60%` | `5B / 5S` |
| `0:00 UTC` | `96.43` | `96.47` | `96.43` | `96.84` | `96.31` | 18,229,950.06 USD | 9,017,649.47 USD | 9,212,300.59 USD | -194,651.12 USD | `-1.07%` | `1B / 6S` |
| `5:00 UTC` | `96.75` | `96.54` | `96.75` | `96.78` | `96.28` | 16,296,059.94 USD | 8,913,950.87 USD | 7,382,109.07 USD | 1,531,841.80 USD | `+9.40%` | `13B / 2S` |
| `0:00 UTC` | `97.12` | `97.02` | `97.12` | `97.23` | `96.62` | 22,145,911.65 USD | 11,618,840.75 USD | 10,527,070.90 USD | 1,091,769.84 USD | `+4.93%` | `11B / 4S` |
| `5:00 UTC` | `96.98` | `97.07` | `96.98` | `97.35` | `96.75` | 14,711,636.00 USD | 8,199,260.01 USD | 6,512,375.99 USD | 1,686,884.02 USD | `+11.47%` | `16B / 7S` |
| `0:00 UTC` | `97.00` | `97.07` | `97.00` | `97.38` | `96.84` | 11,259,592.25 USD | 5,463,221.88 USD | 5,796,370.37 USD | -333,148.49 USD | `-2.96%` | `4B / 11S` |
| `5:00 UTC` | `96.87` | `96.86` | `96.87` | `96.94` | `96.78` | 3,775,752.43 USD | 1,506,050.78 USD | 2,269,701.65 USD | -763,650.87 USD | `-20.23%` | `1B / 5S` |

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
| `5m` | -214,680.00 USD | -592,750.00 USD | **`DISTRIBUTION`** |
| `15m` | -743,180.00 USD | 452,240.00 USD | **`DISTRIBUTION`** |
| `30m` | -981,850.00 USD | 5,510,000.00 USD | **`ACCUMULATION`** |
| `1h` | -2,290,000.00 USD | 12,930,000.00 USD | **`ACCUMULATION`** |
| `2h` | -5,090,000.00 USD | -2,320,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,690,000.00 USD | -36,920,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,740,000.00 USD | -42,250,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,230,000.00 USD | 17,590,000.00 USD | **`ACCUMULATION`** |
| `12h` | -8,510,000.00 USD | -97,900,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -54,990,000.00 USD | -433,880,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 28,850,000.00 USD | -698,430,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,540,000.00 USD | -2,180,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-214.68K` | 15m=`-743.18K` | 1h=`-2.29M` | 24h=`-54.99M`
* Futures Capital Netflows: 5m=`-592.75K` | 15m=`+452.24K` | 1h=`+12.93M` | 24h=`-433.88M`
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
  * Execution Entry: `95.26` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `94.20` (Risk Distance: `1.06` pts)
  * +2.5R Take Profit: `97.91`
  * Mathematical Lot Sizing: **`9.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `98.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.15` (Risk Distance: `1.06` pts)
  * +2.5R Take Profit: `95.44`
  * Mathematical Lot Sizing: **`9.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.50`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
