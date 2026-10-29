# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:31:59 IST` (`2026-10-29 23:01:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.62` | **Live Ask Quote**: `96.89` | **Mid Price**: `96.75`
- **Spread Points**: `27.00` | **Spread BPS**: `27.91 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `99.73` | VWAP Z-Score: `-1.72` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.9594` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.15` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `104.49` | Lower -3.00σ Band: `94.97`
  * Upper +2.51σ Band: `103.71` | Lower -2.51σ Band: `95.75`
  * Upper +2.01σ Band: `102.92` | Lower -2.01σ Band: `96.54`
  * Upper +2.00σ Band: `102.90` | Lower -2.00σ Band: `96.56`
  * Upper +1.28σ Band: `101.76` | Lower -1.28σ Band: `97.70`
  * Upper +1.00σ Band: `101.32` | Lower -1.00σ Band: `98.15`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`97.28` | EMA-20=`98.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`99.41` (Slope: `+0.0000`) | EMA-100=`100.03`
  * Institutional Anchors: EMA-144=`100.24` | EMA-200=`100.33` (Slope: `-0.3755`) | EMA-233=`100.41`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`94.56` | Weekly High=`103.63` | Weekly Low=`94.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `97.44` (Distance: `-0.66%`)
  * Point of Control (POC) = `96.90` (Distance: `-0.10%`)
  * Value Area Low (VAL) = `96.54` (Distance: `+0.27%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.60` | Weekly POC=`100.94` | Weekly VAL=`99.67`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`95.04`
  * London Session (08:00-16:00 UTC): High=`97.14` | Low=`96.37`
  * New York Session (13:00-21:00 UTC): High=`97.34` | Low=`96.17`
  * Initial Balance (First Hour): IB High=`97.05` | IB Low=`96.46`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.37` - `97.14`
  * Optimal Trade Entry (OTE 0.705): `96.95`
  * Structural Invalidation Anchor (0.786): `97.53`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `97.26` | `97.50` | `97.19` | `97.39` | `204,119` | 19,871,728.21 USD | 5,367,719.56 USD | `+27.01%` | -187,730,508.22 USD | `+1.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `97.40` | `97.49` | `97.10` | `97.13` | `199,854` | 19,452,284.48 USD | 6,031,596.90 USD | `+31.01%` | -181,698,911.31 USD | `+1.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `97.13` | `97.54` | `97.10` | `97.50` | `119,425` | 11,626,460.60 USD | 2,825,998.51 USD | `+24.31%` | -178,872,912.81 USD | `+0.72` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `97.50` | `97.80` | `96.45` | `97.08` | `1,285,686` | 125,008,227.84 USD | -23,852,724.73 USD | `-19.08%` | -197,842,024.92 USD | `-1.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `97.08` | `97.50` | `96.76` | `97.13` | `631,405` | 61,390,782.47 USD | 17,367,243.03 USD | `+28.29%` | -180,474,781.89 USD | `+2.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `97.13` | `97.56` | `97.10` | `97.55` | `122,222` | 11,899,277.94 USD | 3,097,688.20 USD | `+26.03%` | -177,377,093.68 USD | `+0.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `99.78` | `99.90` | `94.81` | `96.10` | `5,935,409` | 578,463,305.23 USD | -52,522,739.54 USD | `-9.08%` | -122,417,365.15 USD | `-3.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `96.11` | `98.04` | `95.34` | `97.50` | `3,580,269` | 347,367,878.36 USD | -51,442,556.41 USD | `-14.81%` | -173,859,921.56 USD | `-2.76` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.50` | `97.80` | `96.45` | `97.50` | `2,036,516` | 198,025,470.92 USD | -3,659,483.19 USD | `-1.85%` | -177,519,404.75 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `97.50` | `11,552,194` | 1,123,856,654.50 USD | -107,624,779.14 USD | `-9.58%` | -175,084,755.32 USD | `-2.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -29,365,912.19 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -33,659,266.07 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `97.50` | `11,552,194` | 1,123,856,654.50 USD | -107,624,779.14 USD | `-9.58%` | -175,084,755.32 USD | `-2.05` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`96.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:26:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15` | `0x5b5d...c060` | `SHORT` | 67,493,023.32 USD | `696,120.13` | `94.33` | `96.94` | `353.69` | -1,824,757.11 USD | `-2.70%` | `7X Cross` |
| `20` | `0x9c6a...a4ed` | `LONG` | 53,334,302.07 USD | `550,087.69` | `80.86` | `96.94` | `68.18` | 8,855,315.68 USD | `+16.60%` | `20X Cross` |
| `54` | `0xb83d...6e36` | `SHORT` | 25,153,398.44 USD | `259,300.02` | `91.42` | `96.94` | `686.86` | -1,448,265.42 USD | `-5.76%` | `5X Cross` |
| `80` | `0x3dc9...54b0` | `SHORT` | 21,331,438.42 USD | `220,000.19` | `105.90` | `96.94` | `174.50` | 1,967,668.85 USD | `+9.22%` | `20X Cross` |
| `109` | `0x9c89...600e` | `LONG` | 18,370,495.71 USD | `189,472.50` | `115.21` | `96.94` | `34.98` | -3,458,519.55 USD | `-18.83%` | `20X Cross` |
| `119` | `0x4a20...3c26` | `LONG` | 17,467,200.00 USD | `180,000.00` | `106.43` | `96.94` | `67.95` | -1,691,078.71 USD | `-9.68%` | `20X Cross` |
| `133` | `0xecb6...2b00` | `SHORT` | 15,240,482.71 USD | `157,210.76` | `102.03` | `96.94` | `282.96` | 800,487.62 USD | `+5.25%` | `20X Cross` |
| `174` | `0x7a5a...0394` | `SHORT` | 11,796,333.61 USD | `121,552.79` | `99.81` | `96.94` | `122.69` | 335,607.77 USD | `+2.85%` | `10X Cross` |
| `226` | `0xc63a...a3cd` | `LONG` | 9,684,400.00 USD | `100,000.00` | `112.22` | `96.94` | `0.000000` | -1,537,708.97 USD | `-15.88%` | `20X Cross` |
| `263` | `0xb581...6f4f` | `LONG` | 8,726,040.00 USD | `90,000.00` | `114.59` | `96.94` | `0.000000` | -1,587,252.29 USD | `-18.19%` | `3X Cross` |
| `285` | `0x645b...87b8` | `SHORT` | 8,092,179.48 USD | `83,462.39` | `103.90` | `96.94` | `356.44` | 579,806.92 USD | `+7.17%` | `20X Cross` |
| `295` | `0xdb3a...cf3b` | `LONG` | 7,940,031.92 USD | `81,851.78` | `106.04` | `96.94` | `44.53` | -739,714.94 USD | `-9.32%` | `4X Cross` |
| `312` | `0xe927...98ef` | `LONG` | 7,562,958.00 USD | `78,000.00` | `96.34` | `96.94` | `38.45` | 48,816.52 USD | `+0.65%` | `3X Cross` |
| `320` | `0xca49...53c8` | `SHORT` | 7,175,398.44 USD | `73,943.45` | `110.70` | `96.94` | `292.62` | 1,010,223.82 USD | `+14.08%` | `20X Cross` |
| `326` | `0x8ae4...3d60` | `LONG` | 6,998,649.83 USD | `72,180.05` | `111.72` | `96.94` | `8.78` | -1,065,510.41 USD | `-15.22%` | `10X Cross` |
| `332` | `0xa0b7...6165` | `SHORT` | 6,888,182.79 USD | `71,044.42` | `107.87` | `96.94` | `190.91` | 775,284.41 USD | `+11.26%` | `2X Cross` |
| `351` | `0xf517...c032` | `SHORT` | 6,577,228.55 USD | `67,778.53` | `84.64` | `96.94` | `220.01` | -840,197.39 USD | `-12.77%` | `20X Cross` |
| `380` | `0x7fda...17d1` | `SHORT` | 6,139,797.84 USD | `63,325.61` | `100.91` | `96.94` | `700.81` | 250,424.07 USD | `+4.08%` | `20X Cross` |
| `458` | `0x7e23...5a5a` | `LONG` | 4,709,936.72 USD | `48,564.56` | `105.17` | `96.94` | `67.56` | -397,632.44 USD | `-8.44%` | `5X Isolated` |
| `576` | `0x2e2b...2fab` | `LONG` | 3,879,320.00 USD | `40,000.00` | `119.55` | `96.94` | `58.11` | -902,715.64 USD | `-23.27%` | `10X Cross` |
| `587` | `0xf899...88db` | `SHORT` | 3,823,393.28 USD | `39,434.72` | `88.19` | `96.94` | `117.72` | -345,767.66 USD | `-9.04%` | `20X Cross` |
| `626` | `0x9946...0852` | `SHORT` | 3,609,731.77 USD | `37,198.39` | `112.11` | `96.94` | `138.34` | 560,750.43 USD | `+15.53%` | `20X Cross` |
| `639` | `0x27b8...12fc` | `LONG` | 3,498,908.47 USD | `36,085.73` | `110.86` | `96.94` | `20.39` | -501,436.79 USD | `-14.33%` | `10X Cross` |
| `645` | `0x9c16...4a6f` | `SHORT` | 3,469,504.18 USD | `35,779.15` | `90.45` | `96.94` | `119.58` | -233,399.15 USD | `-6.73%` | `20X Cross` |
| `650` | `0x3440...32c5` | `SHORT` | 3,447,745.80 USD | `35,529.12` | `95.02` | `96.94` | `173.27` | -71,724.37 USD | `-2.08%` | `20X Cross` |
| `725` | `0x023a...2355` | `SHORT` | 3,123,327.95 USD | `32,188.97` | `101.45` | `96.94` | `313.74` | 142,142.70 USD | `+4.55%` | `20X Cross` |
| `729` | `0x96a7...79df` | `LONG` | 3,102,752.00 USD | `32,000.00` | `74.39` | `96.94` | `0.000000` | 722,346.15 USD | `+23.28%` | `20X Cross` |
| `764` | `0xbe19...8bd1` | `SHORT` | 2,955,245.16 USD | `30,451.69` | `97.62` | `96.94` | `766.47` | 17,301.47 USD | `+0.59%` | `3X Cross` |
| `767` | `0x482b...cae4` | `SHORT` | 2,941,299.64 USD | `30,310.49` | `88.03` | `96.94` | `150.57` | -273,051.35 USD | `-9.28%` | `20X Cross` |
| `789` | `0x610b...b613` | `LONG` | 2,873,355.85 USD | `29,634.14` | `101.23` | `96.94` | `70.39` | -126,643.50 USD | `-4.41%` | `3X Isolated` |
| `799` | `0x45d2...4029` | `SHORT` | 2,829,577.14 USD | `29,220.00` | `93.28` | `96.94` | `1564.21` | -103,801.16 USD | `-3.67%` | `20X Cross` |
| `806` | `0xa61c...66b9` | `LONG` | 2,803,031.53 USD | `28,888.00` | `104.39` | `96.94` | `0.000000` | -212,532.59 USD | `-7.58%` | `5X Cross` |
| `842` | `0x458d...ab3b` | `LONG` | 2,655,279.89 USD | `27,385.03` | `117.17` | `96.94` | `81.07` | -553,382.62 USD | `-20.84%` | `3X Isolated` |
| `867` | `0xfc27...9d9d` | `SHORT` | 2,578,291.90 USD | `26,625.07` | `102.14` | `96.94` | `751.01` | 141,204.86 USD | `+5.48%` | `20X Cross` |
| `922` | `0x051c...693c` | `LONG` | 2,437,570.45 USD | `25,139.70` | `89.76` | `96.94` | `35.68` | 181,009.12 USD | `+7.43%` | `20X Cross` |
| `963` | `0x638f...f5f0` | `LONG` | 2,328,936.00 USD | `24,000.00` | `136.71` | `96.94` | `47.72` | -952,032.54 USD | `-40.88%` | `20X Cross` |
| `1014` | `0x7178...0854` | `LONG` | 2,185,873.74 USD | `22,545.24` | `110.94` | `96.94` | `36.38` | -315,270.73 USD | `-14.42%` | `10X Cross` |
| `1033` | `0x739c...cfb2` | `LONG` | 2,133,626.00 USD | `22,000.00` | `91.95` | `96.94` | `77.21` | 110,718.69 USD | `+5.19%` | `20X Cross` |
| `1044` | `0x69cc...14fd` | `SHORT` | 2,106,462.89 USD | `21,701.57` | `99.01` | `96.94` | `473.75` | 42,189.86 USD | `+2.00%` | `20X Cross` |
| `1119` | `0x7749...ea04` | `LONG` | 1,978,283.07 USD | `20,429.00` | `97.90` | `96.94` | `71.86` | -21,716.03 USD | `-1.10%` | `20X Cross` |
| `1121` | `0x7737...bf66` | `SHORT` | 1,976,356.92 USD | `20,384.06` | `102.94` | `96.94` | `925.75` | 121,984.97 USD | `+6.17%` | `10X Cross` |
| `1147` | `0xea00...a918` | `LONG` | 1,941,420.05 USD | `20,022.69` | `66.09` | `96.94` | `0.000000` | 618,111.45 USD | `+31.84%` | `20X Cross` |
| `1148` | `0x251f...6e5d` | `LONG` | 1,940,800.00 USD | `20,000.00` | `101.15` | `96.94` | `65.85` | -82,297.77 USD | `-4.24%` | `20X Cross` |
| `1149` | `0x3fc5...c0c1` | `SHORT` | 1,939,660.00 USD | `20,000.00` | `98.28` | `96.94` | `206.64` | 25,899.84 USD | `+1.34%` | `20X Cross` |
| `1150` | `0xbfc7...80b4` | `SHORT` | 1,939,220.00 USD | `20,000.00` | `85.98` | `96.94` | `284.49` | -219,685.50 USD | `-11.33%` | `20X Cross` |
| `1153` | `0xfc66...ca06` | `LONG` | 1,932,611.43 USD | `19,914.18` | `97.30` | `96.94` | `0.000000` | -5,032.55 USD | `-0.26%` | `20X Cross` |
| `1168` | `0x936c...bb0f` | `SHORT` | 1,908,690.04 USD | `19,664.04` | `105.57` | `96.94` | `288.22` | 167,272.13 USD | `+8.76%` | `20X Cross` |
| `1184` | `0x7160...d47c` | `LONG` | 1,885,885.06 USD | `19,434.10` | `105.03` | `96.94` | `83.00` | -155,336.23 USD | `-8.24%` | `20X Cross` |
| `1204` | `0xe097...d0fe` | `LONG` | 1,842,017.88 USD | `18,995.75` | `109.71` | `96.94` | `0.000000` | -241,979.01 USD | `-13.14%` | `20X Cross` |
| `1284` | `0xdf95...7d72` | `SHORT` | 1,728,593.62 USD | `17,828.64` | `104.53` | `96.94` | `2354.52` | 135,087.36 USD | `+7.81%` | `20X Cross` |
| `1294` | `0xe98b...8cd5` | `SHORT` | 1,708,644.92 USD | `17,622.89` | `187.95` | `96.94` | `262.78` | 1,603,575.80 USD | `+93.85%` | `20X Cross` |
| `1339` | `0xee2b...d67e` | `LONG` | 1,645,955.29 USD | `16,963.19` | `119.86` | `96.94` | `31.08` | -387,316.35 USD | `-23.53%` | `4X Cross` |
| `1346` | `0x123d...3bff` | `LONG` | 1,640,633.45 USD | `16,920.55` | `89.54` | `96.94` | `0.000000` | 125,639.70 USD | `+7.66%` | `10X Cross` |
| `1447` | `0x73d7...8be1` | `LONG` | 1,520,452.23 USD | `15,668.95` | `106.60` | `96.94` | `70.93` | -149,888.73 USD | `-9.86%` | `20X Cross` |
| `1454` | `0xc74a...ab93` | `LONG` | 1,506,372.38 USD | `15,536.82` | `64.06` | `96.94` | `54.88` | 511,143.55 USD | `+33.93%` | `5X Isolated` |
| `1456` | `0x8d0c...e17b` | `LONG` | 1,503,975.65 USD | `15,511.14` | `97.56` | `96.94` | `90.00` | -9,225.95 USD | `-0.61%` | `10X Cross` |
| `1487` | `0x34e6...8d74` | `LONG` | 1,463,122.31 USD | `15,091.67` | `101.19` | `96.94` | `39.53` | -63,948.58 USD | `-4.37%` | `20X Cross` |
| `1494` | `0x5f10...d49d` | `LONG` | 1,455,975.00 USD | `15,000.00` | `96.35` | `96.94` | `68.91` | 10,673.84 USD | `+0.73%` | `20X Cross` |
| `1495` | `0xb322...d51f` | `LONG` | 1,455,447.53 USD | `14,999.82` | `102.98` | `96.94` | `44.95` | -89,279.77 USD | `-6.13%` | `20X Cross` |
| `1497` | `0xc7d1...51af` | `SHORT` | 1,454,415.00 USD | `15,000.00` | `105.79` | `96.94` | `138.76` | 132,460.00 USD | `+9.11%` | `20X Cross` |
| `1553` | `0xffb2...5ed6` | `LONG` | 1,406,254.67 USD | `14,504.05` | `117.89` | `96.94` | `86.68` | -303,650.04 USD | `-21.59%` | `20X Cross` |
| `1578` | `0x0d6a...ca57` | `LONG` | 1,377,803.54 USD | `14,206.65` | `110.41` | `96.94` | `91.60` | -190,786.82 USD | `-13.85%` | `5X Isolated` |
| `1603` | `0x7277...0b98` | `SHORT` | 1,343,156.35 USD | `13,837.70` | `101.18` | `96.94` | `204.59` | 56,963.42 USD | `+4.24%` | `20X Cross` |
| `1859` | `0x2482...0e55` | `LONG` | 1,102,362.88 USD | `11,363.98` | `122.03` | `96.94` | `91.54` | -284,339.04 USD | `-25.79%` | `20X Isolated` |
| `1885` | `0x45db...86eb` | `LONG` | 1,075,656.60 USD | `11,100.00` | `110.69` | `96.94` | `68.69` | -153,025.30 USD | `-14.23%` | `5X Cross` |
| `1922` | `0x1d04...7c43` | `LONG` | 1,048,265.00 USD | `10,811.76` | `111.55` | `96.94` | `15.47` | -157,796.49 USD | `-15.05%` | `6X Cross` |
| `1961` | `0xc4a9...eafb` | `SHORT` | 1,016,617.59 USD | `10,485.35` | `97.38` | `96.94` | `102.89` | 4,468.92 USD | `+0.44%` | `12X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `100.92` | 30,116.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 30.12K USD at 100.9200 USD [API] | `2026-10-28 14:01:36` |
| `ANNOUNCEMENT` | `INFO` | `100.94` | 29,173.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 29.17K USD at 100.9400 USD [API] | `2026-10-28 14:09:43` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 16,520.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 16.52K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 2,565.25 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.57K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 567.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.57K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 12.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 59.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.06K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 39.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.04K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 1,354.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.35K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 308.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.31K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.63` | 93,348.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 93.35K USD at 100.6300 USD [API] | `2026-10-28 14:31:36` |
| `ANNOUNCEMENT` | `INFO` | `100.45` | 104.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.10K USD at 100.4500 USD [API] | `2026-10-28 14:26:24` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 3,965.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.97K USD at 100.4800 USD [API] | `2026-10-28 14:21:52` |
| `ANNOUNCEMENT` | `INFO` | `100.96` | 26,399.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 26.40K USD at 100.9600 USD [API] | `2026-10-28 16:11:22` |
| `ANNOUNCEMENT` | `INFO` | `100.96` | 63,701.72 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 63.70K USD at 100.9600 USD [API] | `2026-10-28 16:13:11` |
| `ANNOUNCEMENT` | `INFO` | `100.96` | 27,645.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 27.65K USD at 100.9600 USD [API] | `2026-10-28 16:13:11` |
| `ANNOUNCEMENT` | `INFO` | `82.36` | 3,380.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.38K USD at 82.3550 USD [API] | `2026-05-23 07:49:33` |
| `ANNOUNCEMENT` | `INFO` | `82.36` | 5,761.56 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.76K USD at 82.3550 USD [API] | `2026-05-23 07:49:33` |
| `ANNOUNCEMENT` | `INFO` | `100.98` | 92,811.73 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 92.81K USD at 100.9800 USD [API] | `2026-10-28 16:40:00` |
| `ANNOUNCEMENT` | `INFO` | `101.23` | 99,380.53 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 99.38K USD at 101.2300 USD [API] | `2026-10-28 17:02:40` |
| `ANNOUNCEMENT` | `INFO` | `101.50` | 40,575.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 40.58K USD at 101.5000 USD [API] | `2026-10-28 18:09:09` |
| `ANNOUNCEMENT` | `INFO` | `103.15` | 20,630.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 20.63K USD at 103.1500 USD [API] | `2026-10-28 08:35:30` |
| `ANNOUNCEMENT` | `INFO` | `102.35` | 410.42 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.41K USD at 102.3500 USD [API] | `2026-10-28 03:32:43` |
| `ANNOUNCEMENT` | `INFO` | `102.35` | 3,299.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.30K USD at 102.3500 USD [API] | `2026-10-28 03:32:43` |
| `ANNOUNCEMENT` | `INFO` | `102.35` | 221.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.22K USD at 102.3500 USD [API] | `2026-10-28 03:32:40` |
| `ANNOUNCEMENT` | `INFO` | `102.45` | 201.83 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 102.4500 USD [API] | `2026-10-26 15:07:26` |
| `ANNOUNCEMENT` | `INFO` | `103.18` | 750.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.75K USD at 103.1800 USD [API] | `2026-10-28 08:27:09` |
| `ANNOUNCEMENT` | `INFO` | `103.18` | 4,408.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.41K USD at 103.1800 USD [API] | `2026-10-28 08:27:09` |
| `ANNOUNCEMENT` | `INFO` | `112.98` | 14,122.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 14.12K USD at 112.9800 USD [API] | `2026-10-12 04:43:15` |
| `ANNOUNCEMENT` | `INFO` | `101.32` | 26,065.58 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 26.07K USD at 101.3200 USD [API] | `2026-10-28 18:32:41` |
| `ANNOUNCEMENT` | `INFO` | `121.80` | 4,331.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.33K USD at 121.8000 USD [API] | `2026-10-05 08:07:00` |
| `ANNOUNCEMENT` | `INFO` | `102.17` | 44,049.57 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 44.05K USD at 102.1700 USD [API] | `2026-10-28 19:01:55` |
| `ANNOUNCEMENT` | `INFO` | `102.06` | 34,916.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 34.92K USD at 102.0600 USD [API] | `2026-10-28 19:06:18` |
| `ANNOUNCEMENT` | `INFO` | `102.06` | 67,302.45 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 67.30K USD at 102.0600 USD [API] | `2026-10-28 19:06:18` |


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
| `Live` | `Long Liquidation` | `19.45` | 2,520.00 USD | 141,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.05` | 501.25 USD | 141,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 730,740.00 USD | 141,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.85` | 501.44 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 618.03 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 186.97 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.25` | 5,420.00 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,410.00 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 161.73 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,730.00 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 10,010.00 USD | 140,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.95` | 11,480.00 USD | 140,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 13,910.00 USD | 140,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.15` | 1,530.00 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 800.35 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 709.85 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.85` | 1,140.00 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,150.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 4,370.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 8,540.00 USD | 140,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 1,000.00 USD | 140,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 140,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 8,260.00 USD | 140,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 122.03 USD | 140,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 115.43 USD | 140,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 232.81 USD | 140,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.35` | 5,040.00 USD | 140,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.55` | 20,690.00 USD | 140,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 141,750.00 USD | 140,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 4,590.00 USD | 140,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,250.00 USD | 140,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 140,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 37,230.00 USD | 140,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 140,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 2,930.00 USD | 140,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 140,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 475.09 USD | 140,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 13,230.00 USD | 140,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.55` | 161.95 USD | 140,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 814.96 USD | 140,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.75` | 4,310.00 USD | 140,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 238.78 USD | 140,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 31,230.00 USD | 140,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 29,640.00 USD | 140,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.25` | 4,460.00 USD | 140,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 717.12 USD | 140,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.65` | 82,950.00 USD | 140,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.75` | 55,500.00 USD | 140,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 412.18 USD | 139,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 139,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 1,590.00 USD | 139,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 145.20 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 418.54 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.65` | 5,630.00 USD | 139,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 12,270.00 USD | 139,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 6,800.00 USD | 139,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 16,100.00 USD | 139,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 10,940.00 USD | 139,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.85` | 44,770.00 USD | 139,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 131.48 USD | 139,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 7,900.00 USD | 139,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 47,340.00 USD | 139,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.25` | 513,140.00 USD | 139,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 3,210.00 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 350.76 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 314.76 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 3,100.00 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 827.34 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.25` | 1,520.00 USD | 139,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 139,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 473.70 USD | 139,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 6,280.00 USD | 139,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 1,180.00 USD | 139,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 1,810.00 USD | 139,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 139,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 1,430.00 USD | 139,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 1,120.00 USD | 139,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 5,990.00 USD | 139,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 867,050.00 USD | 139,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 4,040.00 USD | 138,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 4,600.00 USD | 138,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 1,230.00 USD | 138,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 138,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 39,390.00 USD | 131,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 17,620.00 USD | 131,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 987.68 USD | 131,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 250.99 USD | 131,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 4,840.00 USD | 131,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 537.75 USD | 131,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 5,610.00 USD | 131,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 8,400.00 USD | 131,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 131,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 3,980.00 USD | 131,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 867,550.00 USD | 131,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 300,360.00 USD | 130,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 500.90 USD | 130,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 320.59 USD | 130,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,910.00 USD | 130,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 2,220.00 USD | 130,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 17,870.00 USD | 130,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 58,200.00 USD | 130,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 19,600.00 USD | 130,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 401.84 USD | 130,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 22,820.00 USD | 130,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,430.00 USD | 130,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,160.00 USD | 130,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 768.99 USD | 130,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.15` | 2,300.00 USD | 130,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 191,380.00 USD | 130,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 388.10 USD | 130,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,050,000.00 USD | 130,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 51,820.00 USD | 127,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 127,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 127,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 607.62 USD | 127,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,470.00 USD | 127,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 11,490.00 USD | 127,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 1,330.00 USD | 127,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 596,880.00 USD | 127,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 114,640.00 USD | 126,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 102,950.00 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 2,260.00 USD | 126,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 1,510.00 USD | 126,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 20,740.00 USD | 126,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 126,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,270.00 USD | 126,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 292.68 USD | 126,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 5,130.00 USD | 126,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 9,250.00 USD | 126,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 142.10 USD | 126,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 14,570.00 USD | 126,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 1,070.00 USD | 126,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 126,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 418.46 USD | 126,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 9,130.00 USD | 126,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 130.88 USD | 126,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 126,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 2,460.00 USD | 126,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 2,850.00 USD | 126,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 48,400.00 USD | 126,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 470.12 USD | 126,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 17,340.00 USD | 126,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 6,100.00 USD | 126,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 4,430.00 USD | 126,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 5,580.00 USD | 126,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,420.00 USD | 126,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 389.56 USD | 126,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 16,590.00 USD | 126,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 34,910.00 USD | 125,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 2,400.00 USD | 125,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 311.94 USD | 125,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 106.56 USD | 125,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 125,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,220.00 USD | 125,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 165.56 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,110.00 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 2,380.00 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 3,660,000.00 USD | 125,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 841.21 USD | 122,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 122,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 8,260.00 USD | 122,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 4,350.00 USD | 122,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 2,970.00 USD | 122,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 5,940.00 USD | 122,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 13,790.00 USD | 122,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 122,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 122,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 774.22 USD | 122,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 122,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 122,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 74,660.00 USD | 122,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 281.83 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 42,900.00 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 1,220.00 USD | 122,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 122,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 122,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 11,410.00 USD | 122,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 140.55 USD | 122,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 22,000.00 USD | 122,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 4,130.00 USD | 122,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 4,560.00 USD | 122,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,860.00 USD | 122,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 3,480.00 USD | 122,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 1,150,000.00 USD | 122,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 10,310.00 USD | 120,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 4,630.00 USD | 120,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 5,470.00 USD | 120,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,780.00 USD | 120,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 11,200.00 USD | 120,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 2,930.00 USD | 120,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,870.00 USD | 120,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 8,450.00 USD | 120,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 3,280.00 USD | 120,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 12,920.00 USD | 120,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,530.00 USD | 120,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,270.00 USD | 120,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 120,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 120,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 16,730.00 USD | 120,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 627.80 USD | 120,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 8,890.00 USD | 120,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 5,230.00 USD | 120,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 5,450.00 USD | 120,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 20,850.00 USD | 120,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 8,560.00 USD | 120,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 2,030.00 USD | 120,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 10,370.00 USD | 120,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 3,820.00 USD | 120,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 3,770.00 USD | 120,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 337.33 USD | 120,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,850.00 USD | 120,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 20,140.00 USD | 120,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 2,270.00 USD | 120,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 2,680.00 USD | 120,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 13,820.00 USD | 120,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,390.00 USD | 120,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 360.48 USD | 120,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 7,210.00 USD | 120,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 22,260.00 USD | 120,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 115,520.00 USD | 120,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 26,920.00 USD | 120,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 47,000.00 USD | 120,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 470,160.00 USD | 120,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 99,370.00 USD | 119,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 2,870.00 USD | 119,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 3,800.00 USD | 119,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 33,350.00 USD | 119,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 879.59 USD | 119,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 1,610.00 USD | 119,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 4,270.00 USD | 119,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 26,880.00 USD | 119,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 119,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 5,010.00 USD | 119,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,460.00 USD | 119,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 6,350.00 USD | 119,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,790.00 USD | 119,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,130.00 USD | 119,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,810.00 USD | 119,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 43,250.00 USD | 119,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 3,220.00 USD | 119,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 119,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 119,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 68,960.00 USD | 119,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 81,970.00 USD | 119,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 15,030.00 USD | 119,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 57,560.00 USD | 119,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 1,800.00 USD | 119,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 753.04 USD | 119,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 85,190.00 USD | 119,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,420.00 USD | 119,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 17,320.00 USD | 119,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 946,880.00 USD | 119,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,320.00 USD | 118,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 4,910.00 USD | 118,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 654.08 USD | 118,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 118,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,810.00 USD | 118,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 5,620.00 USD | 118,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 13,240.00 USD | 118,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 8,520.00 USD | 118,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 86,030.00 USD | 118,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 4,090.00 USD | 118,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,890.00 USD | 118,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 7,190.00 USD | 118,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 36,190.00 USD | 118,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 17,970.00 USD | 118,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 19,410.00 USD | 118,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 5,350.00 USD | 117,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 27,410.00 USD | 117,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 14,910.00 USD | 117,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 117,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 1,120,000.00 USD | 117,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 2,320,000.00 USD | 116,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 13,460.00 USD | 114,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 114,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 15,200.00 USD | 114,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 14,740.00 USD | 114,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 17,480.00 USD | 114,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 924.25 USD | 114,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 18,730.00 USD | 114,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 90,210.00 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 80,450.00 USD | 114,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 324.52 USD | 114,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 4,710.00 USD | 114,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 124,470.00 USD | 114,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 23,110.00 USD | 114,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 23,460.00 USD | 114,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 61,260.00 USD | 114,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 3,150.00 USD | 113,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 418.17 USD | 113,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 350.74 USD | 113,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,630.00 USD | 113,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 488.70 USD | 113,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 14,900.00 USD | 113,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 4,870.00 USD | 113,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 418.90 USD | 113,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,320.00 USD | 113,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,230.00 USD | 113,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,610.00 USD | 113,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 18,020.00 USD | 113,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 33,460.00 USD | 113,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 407.58 USD | 113,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 58,710.00 USD | 113,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 12,840.00 USD | 113,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 36,310.00 USD | 113,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 2,340.00 USD | 113,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 2,710.00 USD | 113,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 1,770.00 USD | 113,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 2,760.00 USD | 113,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 150,050.00 USD | 113,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 9,700.00 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,700.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 54,910.00 USD | 113,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 113,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 4,120.00 USD | 113,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 139,530.00 USD | 113,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 12,920.00 USD | 113,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 21,290.00 USD | 113,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 18,590.00 USD | 113,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 22,370.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 69,530.00 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 5,780.00 USD | 113,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 8,430.00 USD | 113,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 9,000.00 USD | 113,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 26,400.00 USD | 113,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 1,800.00 USD | 113,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 43,640.00 USD | 113,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 20,480.00 USD | 113,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 3,130.00 USD | 113,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 4,060.00 USD | 113,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,290.00 USD | 113,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 48,000.00 USD | 113,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 67,330.00 USD | 113,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 54,010.00 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 84,650.00 USD | 112,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 77,870.00 USD | 112,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.35` | 224.26 USD | 112,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 43,420.00 USD | 112,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 6,000.00 USD | 112,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 8,840.00 USD | 112,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 8,560.00 USD | 112,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 38,350.00 USD | 112,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 6,310.00 USD | 112,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 4,920.00 USD | 112,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 16,160.00 USD | 112,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 174,880.00 USD | 112,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 6,660.00 USD | 112,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 1,740.00 USD | 112,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 388,660.00 USD | 112,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 3,220.00 USD | 112,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 6,700.00 USD | 112,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 11,820.00 USD | 112,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 11,050.00 USD | 112,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 47,410.00 USD | 112,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 122,690.00 USD | 111,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 630.94 USD | 111,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 1,320,000.00 USD | 111,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,050.00 USD | 110,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,230.00 USD | 110,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 30,200.00 USD | 110,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 7,020.00 USD | 110,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 12,130.00 USD | 110,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 10,580.00 USD | 110,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 15,730.00 USD | 110,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,580.00 USD | 110,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 2,290.00 USD | 110,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 42,780.00 USD | 110,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 729.82 USD | 110,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 7,360.00 USD | 110,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 2,050.00 USD | 110,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 1,530.00 USD | 110,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 33,390.00 USD | 110,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 2,510.00 USD | 110,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 19,700.00 USD | 110,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 22,240.00 USD | 110,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 45,280.00 USD | 110,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 3,340,000.00 USD | 110,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 173,850.00 USD | 106,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 4,020.00 USD | 106,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 28,230.00 USD | 106,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.95` | 1,310.00 USD | 106,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 12,260,000.00 USD | 106,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 94,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 17,060.00 USD | 56,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 2,860.00 USD | 56,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 24,310.00 USD | 56,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 21,500.00 USD | 56,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 783,800.00 USD | 56,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 47,370.00 USD | 56,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 4,550.00 USD | 56,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 69,280.00 USD | 56,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 1,040,000.00 USD | 55,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 20,880.00 USD | 54,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 7,370.00 USD | 54,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 509.03 USD | 54,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 14,370.00 USD | 54,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 11,710.00 USD | 54,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 1,990.00 USD | 54,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 19,890.00 USD | 54,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 47,550.00 USD | 54,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 54,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 682.99 USD | 54,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 11,700.00 USD | 54,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 190,720.00 USD | 54,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,150,000.00 USD | 54,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 113,380.00 USD | 52,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 34,660.00 USD | 52,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 45,020.00 USD | 52,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 13,570.00 USD | 52,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 20,720.00 USD | 52,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 5,520.00 USD | 52,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 37,460.00 USD | 52,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 1,400,000.00 USD | 52,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 11,640.00 USD | 50,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 21,320.00 USD | 50,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 16,710.00 USD | 50,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 44,020.00 USD | 50,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 460.71 USD | 50,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 532,080.00 USD | 50,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,130.00 USD | 50,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 40,950.00 USD | 50,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 13,460.00 USD | 50,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 145,290.00 USD | 50,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 41,150.00 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 6,370.00 USD | 49,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 8,260.00 USD | 49,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 12,330.00 USD | 49,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 92,150.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 19,820.00 USD | 49,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 1,230.00 USD | 49,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 8,740.00 USD | 49,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 16,410.00 USD | 49,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 62,460.00 USD | 49,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 26,770.00 USD | 49,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 3,410.00 USD | 49,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 536.92 USD | 49,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 18,920.00 USD | 49,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 164,120.00 USD | 49,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 65,320.00 USD | 49,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 1,520,000.00 USD | 49,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,150.00 USD | 47,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 26,320.00 USD | 47,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 22,030.00 USD | 47,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 33,730.00 USD | 47,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 38,740.00 USD | 47,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 7,080.00 USD | 47,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 1,980.00 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 149,570.00 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 15,780.00 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 19,620.00 USD | 47,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 43,400.00 USD | 47,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 10,980.00 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 16,870.00 USD | 47,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 18,800.00 USD | 47,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 3,370.00 USD | 47,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 46,880.00 USD | 47,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 129,160.00 USD | 47,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 48,470.00 USD | 47,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 15,170.00 USD | 47,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 21,910.00 USD | 47,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 1,670,000.00 USD | 47,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,790.00 USD | 45,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 9,000.00 USD | 45,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 35,070.00 USD | 45,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 3,080.00 USD | 45,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 38,050.00 USD | 45,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 15,730.00 USD | 45,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 12,890.00 USD | 45,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 62,560.00 USD | 45,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 35,920.00 USD | 45,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 27,740.00 USD | 45,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 78,320.00 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 34,220.00 USD | 45,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 4,210.00 USD | 45,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 14,830.00 USD | 45,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 7,950.00 USD | 45,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.65` | 201,890.00 USD | 45,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 357,790.00 USD | 44,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 22,500.00 USD | 44,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 12,740.00 USD | 44,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 20,450.00 USD | 44,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 71,470.00 USD | 44,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 24,450.00 USD | 44,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 66,240.00 USD | 44,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 34,280.00 USD | 44,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 524,840.00 USD | 44,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 8,740.00 USD | 43,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 64,950.00 USD | 43,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 24,750.00 USD | 43,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 9,060.00 USD | 43,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 1,500.00 USD | 43,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 620,870.00 USD | 43,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 107,100.00 USD | 43,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 18,890.00 USD | 42,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 4,860.00 USD | 42,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 10,480.00 USD | 42,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 30,610.00 USD | 42,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 693.03 USD | 42,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 51,290.00 USD | 42,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 4,940.00 USD | 42,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 27,450.00 USD | 42,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 38,640.00 USD | 42,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 45,510.00 USD | 42,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 560,470.00 USD | 42,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 11,820.00 USD | 42,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 6,450.00 USD | 42,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 24,310.00 USD | 42,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 14,200.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 35,690.00 USD | 42,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 42,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,310,000.00 USD | 42,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 766,000.00 USD | 39,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 18,710.00 USD | 38,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 82,790.00 USD | 38,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 59,690.00 USD | 38,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 24,020.00 USD | 38,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 16,470.00 USD | 38,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 81,300.00 USD | 38,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 37,370.00 USD | 38,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 16,500.00 USD | 38,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 211,400.00 USD | 38,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 800,060.00 USD | 38,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 163,410.00 USD | 37,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 31,900.00 USD | 37,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 212,870.00 USD | 37,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 41,380.00 USD | 37,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 104,530.00 USD | 37,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 33,040.00 USD | 37,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 19,850.00 USD | 37,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 25,410.00 USD | 36,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 79,640.00 USD | 36,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 24,720.00 USD | 36,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 15,340.00 USD | 36,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 55,090.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 53,590.00 USD | 36,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 10,910.00 USD | 36,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 68,150.00 USD | 36,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 1,700,000.00 USD | 36,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 219,130.00 USD | 34,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 62,100.00 USD | 34,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 174,990.00 USD | 34,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 79,210.00 USD | 34,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 45,260.00 USD | 34,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 42,940.00 USD | 34,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 115,750.00 USD | 34,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 481,260.00 USD | 34,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 64,650.00 USD | 33,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 48,990.00 USD | 33,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 6,300.00 USD | 33,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 3,780.00 USD | 33,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 20,170.00 USD | 33,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 63,110.00 USD | 33,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 567,940.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 41,540.00 USD | 32,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 27,730.00 USD | 32,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 14,630.00 USD | 32,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 16,210.00 USD | 32,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 5,920.00 USD | 32,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 40,200.00 USD | 32,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 60,980.00 USD | 32,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 57,960.00 USD | 32,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.10` | 85,680,000.00 USD | 85,680,000.00 USD | 0.00 USD | 85,490.00 USD | 205,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.15` | 116,560.00 USD | 32,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.25` | 12,230.00 USD | 32,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.30` | 85,390,000.00 USD | 85,390,000.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `86.30` | 89,660,000.00 USD | 89,660,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.35` | 21,350.00 USD | 32,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 34,960.00 USD | 32,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.50` | 85,370,000.00 USD | 85,370,000.00 USD | 0.00 USD | 88,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `86.50` | 89,510,000.00 USD | 89,510,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.55` | 17,960.00 USD | 32,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 1,390,000.00 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.70` | 85,290,000.00 USD | 85,290,000.00 USD | 0.00 USD | 222,710.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.75` | 26,450.00 USD | 31,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.85` | 63,540.00 USD | 31,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.90` | 85,060,000.00 USD | 85,060,000.00 USD | 139,770.00 USD | 174,950.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `86.90` | 89,500,000.00 USD | 89,500,000.00 USD | 207,900.00 USD | 138,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 151,110.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.05` | 310,570.00 USD | 30,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.10` | 84,740,000.00 USD | 84,740,000.00 USD | 19,160.00 USD | 0.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.10` | 89,150,000.00 USD | 89,150,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 295,220.00 USD | 30,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.25` | 174,090.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.30` | 84,720,000.00 USD | 84,720,000.00 USD | 8,750.00 USD | 7,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.30` | 89,150,000.00 USD | 89,150,000.00 USD | 0.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 35,470.00 USD | 30,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.45` | 541,520.00 USD | 30,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.50` | 84,700,000.00 USD | 84,700,000.00 USD | 10,160.00 USD | 12,060.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.50` | 89,150,000.00 USD | 89,150,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 173,280.00 USD | 29,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.65` | 561,140.00 USD | 29,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.70` | 84,680,000.00 USD | 84,680,000.00 USD | 0.00 USD | 99,990.00 USD | 195,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.70` | 89,100,000.00 USD | 89,100,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 26,530.00 USD | 28,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.85` | 21,470.00 USD | 28,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.90` | 84,380,000.00 USD | 84,380,000.00 USD | 22,290.00 USD | 258,430.00 USD | 818,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.90` | 88,390,000.00 USD | 88,390,000.00 USD | 0.00 USD | 295,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 5,470.00 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.05` | 45,710.00 USD | 28,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 6,610.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 198,990.00 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 44,640.00 USD | 28,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 193,140.00 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.50` | 83,280,000.00 USD | 83,280,000.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.55` | 253,250.00 USD | 28,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 149,640.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.70` | 83,280,000.00 USD | 83,280,000.00 USD | 170,450.00 USD | 124,180.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.70` | 88,090,000.00 USD | 88,090,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 147,100.00 USD | 27,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.85` | 57,610.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.90` | 82,570,000.00 USD | 82,570,000.00 USD | 143,140.00 USD | 53,480.00 USD | 216,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.90` | 87,870,000.00 USD | 87,870,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 202,370.00 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.05` | 300,350.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.10` | 82,160,000.00 USD | 82,160,000.00 USD | 160,900.00 USD | 63,750.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.10` | 87,840,000.00 USD | 87,840,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 265,920.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.25` | 88,470.00 USD | 26,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.30` | 81,930,000.00 USD | 81,930,000.00 USD | 10,500.00 USD | 83,100.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.30` | 86,630,000.00 USD | 86,630,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 37,830.00 USD | 26,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.45` | 359,670.00 USD | 26,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.50` | 81,830,000.00 USD | 81,830,000.00 USD | 130,890.00 USD | 55,430.00 USD | 266,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.50` | 86,600,000.00 USD | 86,600,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 42,370.00 USD | 26,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.65` | 16,270.00 USD | 26,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.70` | 81,380,000.00 USD | 81,380,000.00 USD | 705,660.00 USD | 362,180.00 USD | 343,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.70` | 85,810,000.00 USD | 85,810,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 61,120.00 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.85` | 75,680.00 USD | 26,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.90` | 79,970,000.00 USD | 79,970,000.00 USD | 397,980.00 USD | 328,910.00 USD | 405,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.90` | 84,390,000.00 USD | 84,390,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 125,830.00 USD | 26,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.05` | 50,020.00 USD | 26,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.10` | 78,840,000.00 USD | 78,840,000.00 USD | 597,590.00 USD | 530,230.00 USD | 464,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.10` | 82,590,000.00 USD | 82,590,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 36,330.00 USD | 25,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.25` | 44,240.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.30` | 77,240,000.00 USD | 77,240,000.00 USD | 373,160.00 USD | 370,710.00 USD | 437,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.30` | 80,220,000.00 USD | 80,220,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 44,640.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.45` | 186,800.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.50` | 76,060,000.00 USD | 76,060,000.00 USD | 523,240.00 USD | 419,800.00 USD | 531,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.50` | 78,140,000.00 USD | 78,140,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 13,950.00 USD | 25,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.65` | 81,000.00 USD | 25,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 74,590,000.00 USD | 74,590,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.70` | 75,450,000.00 USD | 75,450,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 61,230.00 USD | 25,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.85` | 94,820.00 USD | 25,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.90` | 74,090,000.00 USD | 74,090,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.90` | 73,010,000.00 USD | 73,010,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 55,160.00 USD | 25,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.05` | 811,710.00 USD | 25,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.10` | 73,980,000.00 USD | 73,980,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.10` | 70,630,000.00 USD | 70,630,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 290,130.00 USD | 24,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.25` | 19,390.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.30` | 73,800,000.00 USD | 73,800,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.30` | 68,720,000.00 USD | 68,720,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 52,720.00 USD | 24,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.45` | 34,520.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.50` | 73,650,000.00 USD | 73,650,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.50` | 66,210,000.00 USD | 66,210,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 3,660,000.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.65` | 81,870.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 73,540,000.00 USD | 73,540,000.00 USD | 107,440.00 USD | 112,260.00 USD | 514,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.70` | 63,300,000.00 USD | 63,300,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 369,210.00 USD | 20,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.85` | 37,650.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.90` | 72,800,000.00 USD | 72,800,000.00 USD | 156,200.00 USD | 277,390.00 USD | 65,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.90` | 61,670,000.00 USD | 61,670,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 128,670.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.05` | 29,340.00 USD | 19,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.10` | 72,300,000.00 USD | 72,300,000.00 USD | 65,530.00 USD | 68,940.00 USD | 63,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.10` | 59,260,000.00 USD | 59,260,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 269,080.00 USD | 19,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.25` | 66,830.00 USD | 19,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.30` | 72,110,000.00 USD | 72,110,000.00 USD | 124,630.00 USD | 367,400.00 USD | 841,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.30` | 57,560,000.00 USD | 57,560,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 191,580.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.45` | 185,890.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.50` | 70,770,000.00 USD | 70,770,000.00 USD | 16,830.00 USD | 884,320.00 USD | 77,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.50` | 55,200,000.00 USD | 55,200,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 238,380.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.65` | 451,720.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 69,790,000.00 USD | 69,790,000.00 USD | 349,430.00 USD | 333,670.00 USD | 97,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.70` | 53,440,000.00 USD | 53,440,000.00 USD | 671,470.00 USD | 168,780.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 430,540.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.85` | 518,600.00 USD | 18,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.90` | 69,010,000.00 USD | 69,010,000.00 USD | 47,890.00 USD | 120,260.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.90` | 52,530,000.00 USD | 52,530,000.00 USD | 0.00 USD | 74,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 84,580.00 USD | 17,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.05` | 197,380.00 USD | 17,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.10` | 68,840,000.00 USD | 68,840,000.00 USD | 21,880.00 USD | 106,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.10` | 52,450,000.00 USD | 52,450,000.00 USD | 31,020.00 USD | 118,670.00 USD | 290,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 78,980.00 USD | 17,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.25` | 475,120.00 USD | 17,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.30` | 68,710,000.00 USD | 68,710,000.00 USD | 35,840.00 USD | 251,260.00 USD | 134,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.30` | 52,010,000.00 USD | 52,010,000.00 USD | 145,070.00 USD | 66,280.00 USD | 468,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 201,450.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.45` | 585,030.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.50` | 68,290,000.00 USD | 68,290,000.00 USD | 40,950.00 USD | 537,430.00 USD | 489,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.50` | 51,330,000.00 USD | 51,330,000.00 USD | 93,960.00 USD | 1,260,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 341,130.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.65` | 373,280.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.70` | 67,220,000.00 USD | 67,220,000.00 USD | 118,790.00 USD | 487,680.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.70` | 48,530,000.00 USD | 48,530,000.00 USD | 270,240.00 USD | 954,120.00 USD | 120,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 129,890.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.85` | 576,790.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.90` | 64,270,000.00 USD | 64,270,000.00 USD | 60,590.00 USD | 1,050,000.00 USD | 737,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.90` | 47,190,000.00 USD | 47,190,000.00 USD | 168,420.00 USD | 56,340.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 2,270,000.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.05` | 264,200.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.10` | 62,420,000.00 USD | 62,420,000.00 USD | 0.00 USD | 337,220.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.10` | 46,940,000.00 USD | 46,940,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 183,590.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.25` | 37,910.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.30` | 62,080,000.00 USD | 62,080,000.00 USD | 0.00 USD | 1,530,000.00 USD | 708,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.30` | 45,360,000.00 USD | 45,360,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 208,080.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.45` | 958,060.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.50` | 59,840,000.00 USD | 59,840,000.00 USD | 33,670.00 USD | 620,570.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.50` | 44,640,000.00 USD | 44,640,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 559,630.00 USD | 10,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.65` | 8,510,000.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.70` | 57,100,000.00 USD | 57,100,000.00 USD | 1,120,000.00 USD | 1,730,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.70` | 43,560,000.00 USD | 43,560,000.00 USD | 1,600,000.00 USD | 238,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `94.75` | 26,420.00 USD | 26,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.85` | 803,260.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.90` | 53,210,000.00 USD | 53,210,000.00 USD | 570,680.00 USD | 487,560.00 USD | 23,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.90` | 41,720,000.00 USD | 41,720,000.00 USD | 1,100,000.00 USD | 2,260,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 237,840.00 USD | 666,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.05` | 222,650.00 USD | 428,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.10` | 52,130,000.00 USD | 52,130,000.00 USD | 459,370.00 USD | 1,850,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.10` | 38,360,000.00 USD | 38,360,000.00 USD | 198,380.00 USD | 243,490.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 20,190.00 USD | 206,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.25` | 142,840.00 USD | 185,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.30` | 48,430,000.00 USD | 48,430,000.00 USD | 92,990.00 USD | 3,000,000.00 USD | 276,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.30` | 36,560,000.00 USD | 36,560,000.00 USD | 678,340.00 USD | 445,310.00 USD | 838,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 9,410.00 USD | 43,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.45` | 17,100.00 USD | 33,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.50` | 45,060,000.00 USD | 45,060,000.00 USD | 2,390,000.00 USD | 1,660,000.00 USD | 997,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.50` | 34,600,000.00 USD | 34,600,000.00 USD | 1,200,000.00 USD | 3,810,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 11,290.00 USD | 16,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.70` | 40,010,000.00 USD | 40,010,000.00 USD | 1,590,000.00 USD | 2,220,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 26,720,000.00 USD | 26,720,000.00 USD | 4,060,000.00 USD | 1,480,000.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 5,330.00 USD | 5,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.90` | 32,080,000.00 USD | 32,080,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.90` | 21,170,000.00 USD | 21,170,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 30,730,000.00 USD | 30,730,000.00 USD | 2,430,000.00 USD | 576,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 19,040,000.00 USD | 19,040,000.00 USD | 3,460,000.00 USD | 0.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 27,720,000.00 USD | 27,720,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 13,900,000.00 USD | 13,900,000.00 USD | 1,030,000.00 USD | 2,320,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.35` | 60,150.00 USD | 86,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.50` | 24,820,000.00 USD | 24,820,000.00 USD | 0.00 USD | 1,770,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.70` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 4,380,000.00 USD | 10,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 2,110,000.00 USD | 2,110,000.00 USD | 561,460.00 USD | 4,300.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.10` | 1,080,000.00 USD | 1,080,000.00 USD | 1,020,000.00 USD | 0.00 USD | 54,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.10` | 2,150,000.00 USD | 2,150,000.00 USD | 1,020,000.00 USD | 0.00 USD | 54,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.30` | 2,300,000.00 USD | 2,300,000.00 USD | 146,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.30` | 5,720,000.00 USD | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.50` | 5,610,000.00 USD | 5,610,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.50` | 12,360,000.00 USD | 12,360,000.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.65` | 5,390.00 USD | 91,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.70` | 11,220,000.00 USD | 11,220,000.00 USD | 5,590,000.00 USD | 0.00 USD | 24,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.70` | 19,680,000.00 USD | 19,680,000.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 17,690,000.00 USD | 17,690,000.00 USD | 4,140,000.00 USD | 332,830.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 45,230,000.00 USD | 45,230,000.00 USD | 11,920,000.00 USD | 5,860,000.00 USD | 7,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.10` | 30,600,000.00 USD | 30,600,000.00 USD | 6,760,000.00 USD | 2,150,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.10` | 75,240,000.00 USD | 75,240,000.00 USD | 9,820,000.00 USD | 7,490,000.00 USD | 12,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.30` | 43,430,000.00 USD | 43,430,000.00 USD | 2,970,000.00 USD | 3,940,000.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.30` | 91,820,000.00 USD | 91,820,000.00 USD | 43,030.00 USD | 6,830,000.00 USD | 9,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.50` | 51,890,000.00 USD | 51,890,000.00 USD | 698,860.00 USD | 2,340,000.00 USD | 5,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.50` | 97,970,000.00 USD | 97,970,000.00 USD | 1,040,000.00 USD | 5,110,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 3,190.00 USD | 95,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.65` | 624.45 USD | 95,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.70` | 62,810,000.00 USD | 62,810,000.00 USD | 95,780.00 USD | 3,780,000.00 USD | 7,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.70` | 98,000,000.00 USD | 98,000,000.00 USD | 0.00 USD | 28,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.85` | 217.47 USD | 96,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.90` | 63,370,000.00 USD | 63,370,000.00 USD | 43,770.00 USD | 518,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.90` | 98,090,000.00 USD | 98,090,000.00 USD | 57,310.00 USD | 17,430.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 2,350.00 USD | 98,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.10` | 67,800,000.00 USD | 67,800,000.00 USD | 71,670.00 USD | 502,530.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.10` | 99,230,000.00 USD | 99,230,000.00 USD | 179,200.00 USD | 124,230.00 USD | 838,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 185,850.00 USD | 284,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.25` | 76,600.00 USD | 360,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.30` | 73,270,000.00 USD | 73,270,000.00 USD | 2,900,000.00 USD | 1,070,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.30` | 104,360,000.00 USD | 104,360,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 61,920.00 USD | 422,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.45` | 35,680.00 USD | 458,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.50` | 76,300,000.00 USD | 76,300,000.00 USD | 132,490.00 USD | 2,340,000.00 USD | 560,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.50` | 108,100,000.00 USD | 108,100,000.00 USD | 2,240,000.00 USD | 1,480,000.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 14,140.00 USD | 472,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.65` | 5,650.00 USD | 478,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.70` | 97,280,000.00 USD | 97,280,000.00 USD | 3,660,000.00 USD | 6,920,000.00 USD | 10,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.70` | 110,110,000.00 USD | 110,110,000.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 11,680.00 USD | 489,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.85` | 90,500.00 USD | 580,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.90` | 102,870,000.00 USD | 102,870,000.00 USD | 468,220.00 USD | 914,600.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.90` | 117,260,000.00 USD | 117,260,000.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 45,240.00 USD | 625,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.05` | 8,030.00 USD | 633,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.10` | 106,050,000.00 USD | 106,050,000.00 USD | 1,610,000.00 USD | 1,560,000.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.10` | 120,650,000.00 USD | 120,650,000.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 10,180.00 USD | 643,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.30` | 109,920,000.00 USD | 109,920,000.00 USD | 16,830.00 USD | 1,210,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.30` | 123,500,000.00 USD | 123,500,000.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 799.79 USD | 644,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.50` | 115,450,000.00 USD | 115,450,000.00 USD | 1,610,000.00 USD | 305,750.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 130,440,000.00 USD | 130,440,000.00 USD | 2,500,000.00 USD | 128,740.00 USD | 4,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 21,810.00 USD | 666,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.70` | 121,650,000.00 USD | 121,650,000.00 USD | 1,700,000.00 USD | 1,960,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 131,820,000.00 USD | 131,820,000.00 USD | 133,340.00 USD | 1,240,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 31,580.00 USD | 698,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.85` | 4,040.00 USD | 702,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.90` | 126,500,000.00 USD | 126,500,000.00 USD | 1,540,000.00 USD | 1,910,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.90` | 143,690,000.00 USD | 143,690,000.00 USD | 3,480,000.00 USD | 3,220,000.00 USD | 5,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 12,260.00 USD | 714,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.05` | 230.39 USD | 714,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.10` | 143,090,000.00 USD | 143,090,000.00 USD | 9,810,000.00 USD | 4,430,000.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.10` | 153,460,000.00 USD | 153,460,000.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 3,380.00 USD | 717,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.25` | 275.40 USD | 718,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.30` | 155,350,000.00 USD | 155,350,000.00 USD | 3,680,000.00 USD | 4,410,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.30` | 174,030,000.00 USD | 174,030,000.00 USD | 7,310,000.00 USD | 4,280,000.00 USD | 8,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.35` | 3,970.00 USD | 722,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.50` | 173,360,000.00 USD | 173,360,000.00 USD | 2,790,000.00 USD | 4,250,000.00 USD | 10,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.50` | 189,300,000.00 USD | 189,300,000.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 814.43 USD | 722,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.65` | 1,820.00 USD | 724,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 185,970,000.00 USD | 185,970,000.00 USD | 3,930,000.00 USD | 625,490.00 USD | 8,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.70` | 198,640,000.00 USD | 198,640,000.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.90` | 190,750,000.00 USD | 190,750,000.00 USD | 1,970,000.00 USD | 532,070.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 206,650,000.00 USD | 206,650,000.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,690.00 USD | 729,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.10` | 196,170,000.00 USD | 196,170,000.00 USD | 2,650,000.00 USD | 880,210.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.10` | 211,290,000.00 USD | 211,290,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.30` | 201,950,000.00 USD | 201,950,000.00 USD | 1,680,000.00 USD | 1,500,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 217,340,000.00 USD | 217,340,000.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.35` | 6,240.00 USD | 735,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.45` | 116.79 USD | 735,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.50` | 206,280,000.00 USD | 206,280,000.00 USD | 1,510,000.00 USD | 800,630.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.50` | 221,000,000.00 USD | 221,000,000.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.55` | 648.12 USD | 736,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.65` | 223.78 USD | 736,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 208,210,000.00 USD | 208,210,000.00 USD | 1,270,000.00 USD | 658,410.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.70` | 221,770,000.00 USD | 221,770,000.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.90` | 213,110,000.00 USD | 213,110,000.00 USD | 1,520,000.00 USD | 1,880,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 243,060,000.00 USD | 243,060,000.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 3,080.00 USD | 739,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.05` | 2,460.00 USD | 742,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.10` | 219,130,000.00 USD | 219,130,000.00 USD | 2,660,000.00 USD | 1,770,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.10` | 249,260,000.00 USD | 249,260,000.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 753,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.30` | 222,490,000.00 USD | 222,490,000.00 USD | 1,020,000.00 USD | 1,010,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.30` | 266,830,000.00 USD | 266,830,000.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 1,050.00 USD | 754,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.45` | 129.31 USD | 754,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.50` | 232,440,000.00 USD | 232,440,000.00 USD | 3,150,000.00 USD | 2,070,000.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 289,240,000.00 USD | 289,240,000.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 11,180.00 USD | 765,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 240,500,000.00 USD | 240,500,000.00 USD | 2,940,000.00 USD | 1,990,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.70` | 301,460,000.00 USD | 301,460,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 4,000.00 USD | 769,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.85` | 22,700.00 USD | 792,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.90` | 247,550,000.00 USD | 247,550,000.00 USD | 2,590,000.00 USD | 2,430,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.90` | 319,500,000.00 USD | 319,500,000.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 1,670.00 USD | 793,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.10` | 256,580,000.00 USD | 256,580,000.00 USD | 3,500,000.00 USD | 2,320,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.10` | 348,220,000.00 USD | 348,220,000.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,060.00 USD | 795,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 91,820.00 USD | 886,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.30` | 261,710,000.00 USD | 261,710,000.00 USD | 1,770,000.00 USD | 1,720,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.30` | 369,600,000.00 USD | 369,600,000.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 625.06 USD | 887,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.45` | 2,850.00 USD | 890,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.50` | 266,710,000.00 USD | 266,710,000.00 USD | 1,960,000.00 USD | 1,390,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.50` | 381,610,000.00 USD | 381,610,000.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 12,340.00 USD | 902,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.65` | 630,930.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 272,860,000.00 USD | 272,860,000.00 USD | 1,760,000.00 USD | 1,050,000.00 USD | 3,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.70` | 401,610,000.00 USD | 401,610,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.90` | 274,340,000.00 USD | 274,340,000.00 USD | 383,880.00 USD | 458,320.00 USD | 640,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 422,210,000.00 USD | 422,210,000.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 1,060.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.10` | 276,370,000.00 USD | 276,370,000.00 USD | 421,810.00 USD | 350,810.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 435,420,000.00 USD | 435,420,000.00 USD | 5,580,000.00 USD | 4,800,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 3,350.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.30` | 276,460,000.00 USD | 276,460,000.00 USD | 2,590.00 USD | 87,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.30` | 440,410,000.00 USD | 440,410,000.00 USD | 2,740,000.00 USD | 1,820,000.00 USD | 428,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 431.94 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 636,160.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.50` | 276,930,000.00 USD | 276,930,000.00 USD | 169,670.00 USD | 196,610.00 USD | 107,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.50` | 459,930,000.00 USD | 459,930,000.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 277,300,000.00 USD | 277,300,000.00 USD | 106,090.00 USD | 231,960.00 USD | 29,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.70` | 474,090,000.00 USD | 474,090,000.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.90` | 278,290,000.00 USD | 278,290,000.00 USD | 215,940.00 USD | 631,980.00 USD | 138,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.90` | 483,990,000.00 USD | 483,990,000.00 USD | 3,680,000.00 USD | 1,870,000.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 266.99 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.05` | 1,420.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.10` | 279,800,000.00 USD | 279,800,000.00 USD | 716,050.00 USD | 528,260.00 USD | 268,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.10` | 496,130,000.00 USD | 496,130,000.00 USD | 6,090,000.00 USD | 3,080,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.15` | 5,380.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.25` | 435.62 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.30` | 280,660,000.00 USD | 280,660,000.00 USD | 188,620.00 USD | 376,430.00 USD | 293,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 506,120,000.00 USD | 506,120,000.00 USD | 4,780,000.00 USD | 2,990,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 651.93 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.45` | 696.18 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.50` | 281,590,000.00 USD | 281,590,000.00 USD | 509,190.00 USD | 259,330.00 USD | 167,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.50` | 511,360,000.00 USD | 511,360,000.00 USD | 1,700,000.00 USD | 1,650,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.70` | 283,460,000.00 USD | 283,460,000.00 USD | 550,310.00 USD | 103,750.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.70` | 520,490,000.00 USD | 520,490,000.00 USD | 2,280,000.00 USD | 2,670,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 478,970.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.90` | 283,800,000.00 USD | 283,800,000.00 USD | 10,160.00 USD | 95,900.00 USD | 239,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.90` | 526,320,000.00 USD | 526,320,000.00 USD | 1,220,000.00 USD | 1,150,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 291.97 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.05` | 12,400.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.10` | 284,640,000.00 USD | 284,640,000.00 USD | 88,570.00 USD | 218,500.00 USD | 528,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.10` | 530,430,000.00 USD | 530,430,000.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 613.97 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.25` | 35,170.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.30` | 284,830,000.00 USD | 284,830,000.00 USD | 22,290.00 USD | 60,380.00 USD | 110,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.30` | 530,880,000.00 USD | 530,880,000.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 198,170.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.45` | 53,960.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.50` | 285,740,000.00 USD | 285,740,000.00 USD | 0.00 USD | 198,050.00 USD | 708,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.50` | 531,860,000.00 USD | 531,860,000.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,820.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.70` | 532,830,000.00 USD | 532,830,000.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.75` | 5,840.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.85` | 106.77 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.90` | 533,000,000.00 USD | 533,000,000.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.10` | 533,610,000.00 USD | 533,610,000.00 USD | 249,450.00 USD | 347,250.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.30` | 535,760,000.00 USD | 535,760,000.00 USD | 964,640.00 USD | 578,980.00 USD | 612,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,690.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.45` | 119,130.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.50` | 536,810,000.00 USD | 536,810,000.00 USD | 883,300.00 USD | 157,660.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 539,050,000.00 USD | 539,050,000.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.75` | 6,560.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.90` | 541,100,000.00 USD | 541,100,000.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.95` | 955.49 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.05` | 11,060.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.10` | 542,180,000.00 USD | 542,180,000.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.15` | 22,380.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 1,070.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.30` | 543,350,000.00 USD | 543,350,000.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.35` | 247.13 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 105,660.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.50` | 543,590,000.00 USD | 543,590,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.55` | 461.21 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 42,990.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.70` | 544,770,000.00 USD | 544,770,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.85` | 572.32 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.90` | 546,570,000.00 USD | 546,570,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.95` | 537.66 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.10` | 548,940,000.00 USD | 548,940,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.15` | 6,080.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 37,080.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.30` | 551,020,000.00 USD | 551,020,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.35` | 152,660.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 16,940.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.50` | 551,500,000.00 USD | 551,500,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.55` | 391,490.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.70` | 553,700,000.00 USD | 553,700,000.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.75` | 575.90 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 12,850.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.90` | 556,150,000.00 USD | 556,150,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.95` | 12,860.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.10` | 558,530,000.00 USD | 558,530,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.25` | 234.74 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.30` | 560,440,000.00 USD | 560,440,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 3,620.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.50` | 562,940,000.00 USD | 562,940,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.65` | 197.62 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.70` | 564,090,000.00 USD | 564,090,000.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.75` | 339.72 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.90` | 565,860,000.00 USD | 565,860,000.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.95` | 1,010.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.10` | 567,490,000.00 USD | 567,490,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.25` | 627.48 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.30` | 569,900,000.00 USD | 569,900,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.50` | 571,210,000.00 USD | 571,210,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 584.65 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.70` | 571,730,000.00 USD | 571,730,000.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 1,460.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.90` | 573,220,000.00 USD | 573,220,000.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.95` | 11,290.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 263,100.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.10` | 574,620,000.00 USD | 574,620,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 114.38 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.30` | 574,890,000.00 USD | 574,890,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.45` | 104,150.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.50` | 574,950,000.00 USD | 574,950,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.55` | 5,180.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 3,220.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.70` | 575,340,000.00 USD | 575,340,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.75` | 1,180.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.90` | 575,400,000.00 USD | 575,400,000.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 21,420.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.10` | 575,450,000.00 USD | 575,450,000.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.15` | 1,960.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,620.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.30` | 575,680,000.00 USD | 575,680,000.00 USD | 93,960.00 USD | 135,190.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `114.40` | 576,010,000.00 USD | 576,010,000.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,050.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.95` | 496.58 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 570,810.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 518,330.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 18,240.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 884,130.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 46,710.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.15` | 14,220.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.45` | 716.17 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,780.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.75` | 31,740.00 USD | 6,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 6,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 23,970.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.25` | 4,700,000.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 230.01 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.45` | 128.02 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 11,130.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 12,060.00 USD | 11,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 27,460.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 57,850.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 4,280,000.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.95` | 100,320.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 4,920.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.35` | 145.62 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 2,640.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 874.71 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.75` | 10,870.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.85` | 282.79 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 15,290.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 12,720.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 1,530.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.65` | 16,300.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.85` | 54,760.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,200.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 2,790.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 15,260,000.00 USD | 31,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.55` | 3,430.00 USD | 31,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 31,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 17,600.00 USD | 31,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 859,810.00 USD | 32,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 32,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 5,920.00 USD | 32,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 33,830.00 USD | 32,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.25` | 2,420.00 USD | 32,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,910.00 USD | 32,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 3,760.00 USD | 32,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 32,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 6,200.00 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 305.77 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 32,990.00 USD | 32,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.75` | 8,670.00 USD | 32,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 2,100.00 USD | 32,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.95` | 56,490.00 USD | 32,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 32,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 32,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 32,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 255,500.00 USD | 32,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 4,200.00 USD | 32,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 32,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,200.00 USD | 32,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 32,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.45` | 271.03 USD | 32,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 944.29 USD | 32,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 714,710.00 USD | 33,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 45,050.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.95` | 30,700.00 USD | 33,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,480.00 USD | 33,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 8,620.00 USD | 33,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 56,180.00 USD | 33,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 36,480.00 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.95` | 131.25 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 145.88 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.55` | 195.83 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 866.21 USD | 33,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 503,820.00 USD | 34,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 14,890.00 USD | 34,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 34,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 34,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 34,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 5,540.00 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.25` | 6,610.00 USD | 34,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.35` | 12,870.00 USD | 34,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.45` | 8,530.00 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 695.89 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 62,170.00 USD | 34,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.95` | 9,110.00 USD | 34,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 34,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.55` | 186.97 USD | 34,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 48,220.00 USD | 34,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 34,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 34,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 2,430.00 USD | 34,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 41,810.00 USD | 34,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.75` | 2,620.00 USD | 34,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.05` | 181,050.00 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 809.19 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.55` | 5,120,000.00 USD | 39,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.85` | 537,620.00 USD | 40,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 40,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 86,640.00 USD | 40,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 136,610.00 USD | 40,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.35` | 18,980.00 USD | 40,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.55` | 207,490.00 USD | 40,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.65` | 14,900.00 USD | 40,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,080,000.00 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.95` | 1,670.00 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 1,170.00 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 2,990.00 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 769.47 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 1,040.00 USD | 43,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 67,040.00 USD | 43,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 43,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 8,030.00 USD | 43,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 209.57 USD | 43,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,070,000.00 USD | 44,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 125.53 USD | 44,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 44,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 250,580.00 USD | 44,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 44,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 2,650.00 USD | 44,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 103.48 USD | 44,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 131,260.00 USD | 44,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 44,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.55` | 12,960.00 USD | 44,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.65` | 112.69 USD | 44,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 44,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.95` | 87,010.00 USD | 44,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,330.00 USD | 44,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 44,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.45` | 1,150.00 USD | 44,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.95` | 19,290.00 USD | 44,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 44,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 44,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.05` | 487.37 USD | 44,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 44,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 3,720.00 USD | 44,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.55` | 1,390.00 USD | 44,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 44,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 820.24 USD | 44,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.05` | 438,150.00 USD | 45,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 45,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 45,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 45,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 2,110.00 USD | 45,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 45,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.85` | 859,100.00 USD | 46,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 81,010.00 USD | 46,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 46,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 300.14 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 5,730.00 USD | 46,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.25` | 5,450.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 2,060.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 47,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 91,450.00 USD | 47,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.95` | 1,380,000.00 USD | 48,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 48,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 48,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 1,120,000.00 USD | 49,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 49,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.25` | 345.57 USD | 49,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.35` | 17,270.00 USD | 49,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.45` | 43,030.00 USD | 49,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.05` | 2,770.00 USD | 49,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 2,540.00 USD | 49,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 9,040.00 USD | 49,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.75` | 4,630,000.00 USD | 54,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 54,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 2,320.00 USD | 54,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 22,670.00 USD | 54,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 286,550.00 USD | 54,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 54,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 423,220.00 USD | 55,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 55,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 1,060.00 USD | 55,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 16,690.00 USD | 55,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 34,880.00 USD | 55,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 55,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.45` | 119,650.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 55,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 43,540.00 USD | 55,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 292.69 USD | 55,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 55,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.35` | 362.72 USD | 55,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 55,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.65` | 43,580.00 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 232,580.00 USD | 55,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.15` | 1,240.00 USD | 55,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 55,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.85` | 123.12 USD | 55,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.95` | 7,800.00 USD | 55,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 99,780.00 USD | 55,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 3,930.00 USD | 55,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 1,770.00 USD | 55,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 163,360.00 USD | 55,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.25` | 18,600.00 USD | 56,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.35` | 157,350.00 USD | 56,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.45` | 1,470.00 USD | 56,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 56,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 56,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.15` | 709,580.00 USD | 56,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.45` | 120.42 USD | 56,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.65` | 84,520.00 USD | 57,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.95` | 27,860.00 USD | 57,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 44,690.00 USD | 57,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.25` | 39,350.00 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 495.89 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 1,330.00 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.95` | 300.71 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.05` | 654.60 USD | 57,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 1,340.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.45` | 640.20 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.55` | 1,060.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.95` | 260.74 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 57,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 57,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.75` | 323,500.00 USD | 58,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 58,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.25` | 120.06 USD | 58,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.55` | 142,940.00 USD | 58,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.55` | 3,160.00 USD | 58,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 58,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 16,950.00 USD | 58,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.45` | 822.25 USD | 58,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.65` | 16,470.00 USD | 58,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.75` | 207,840.00 USD | 58,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 58,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.35` | 72,750.00 USD | 58,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.45` | 827.25 USD | 58,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 58,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 67,790.00 USD | 58,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.75` | 3,440.00 USD | 58,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.85` | 27,020.00 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.85` | 95,710.00 USD | 59,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.95` | 122.60 USD | 59,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.25` | 1,170.00 USD | 59,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 59,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 59,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.75` | 20,240.00 USD | 59,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.85` | 152.87 USD | 59,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.35` | 181,940.00 USD | 59,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 59,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.05` | 209.90 USD | 59,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.35` | 37,920,000.00 USD | 97,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 97,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.55` | 124,210.00 USD | 97,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.65` | 3,570.00 USD | 97,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.75` | 1,000,000.00 USD | 98,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.85` | 20,150.00 USD | 98,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.35` | 35,670.00 USD | 98,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 98,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.55` | 6,170,000.00 USD | 104,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.75` | 4,340.00 USD | 104,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 104,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.95` | 104,370.00 USD | 104,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 104,430.00 USD | 105,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,660.00 USD | 105,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 105,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 105,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.05` | 388.61 USD | 105,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.25` | 140,200.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.35` | 119.24 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.15` | 1,940.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.55` | 24,890.00 USD | 105,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.75` | 11,950.00 USD | 105,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.95` | 48,820.00 USD | 105,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.05` | 1,020.00 USD | 105,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.25` | 129.39 USD | 105,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.35` | 44,360.00 USD | 105,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.45` | 70,980.00 USD | 105,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 105,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.25` | 12,130.00 USD | 105,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.05` | 115,690.00 USD | 106,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.15` | 268,730.00 USD | 106,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.35` | 473.48 USD | 106,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.45` | 1,350.00 USD | 106,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.75` | 154.59 USD | 106,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 106,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.65` | 361,300.00 USD | 106,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.75` | 146.41 USD | 106,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.45` | 18,140.00 USD | 106,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 106,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 106,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.55` | 2,060.00 USD | 106,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.85` | 618.03 USD | 106,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.25` | 2,860.00 USD | 106,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.45` | 7,600.00 USD | 106,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 106,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.55` | 1,010,000.00 USD | 107,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 107,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.05` | 980.76 USD | 107,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 107,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 107,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 384.30 USD | 107,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.15` | 671.87 USD | 107,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.25` | 2,100.00 USD | 107,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.35` | 9,690.00 USD | 107,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 107,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.25` | 5,340.00 USD | 107,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.35` | 2,660.00 USD | 107,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 107,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 283,050.00 USD | 108,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 108,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 108,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.65` | 379,420.00 USD | 108,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.75` | 37,950.00 USD | 108,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 225,680.00 USD | 108,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 109,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 1,330.00 USD | 109,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.55` | 259.15 USD | 109,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.65` | 166,600.00 USD | 109,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 122,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.25` | 175.95 USD | 122,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.45` | 1,370.00 USD | 122,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.55` | 2,910.00 USD | 122,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.75` | 253.11 USD | 122,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 122,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.55` | 799,080.00 USD | 123,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 3,980.00 USD | 123,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.35` | 378.97 USD | 123,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 115,120.00 USD | 123,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.95` | 140,910.00 USD | 123,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.15` | 88,880.00 USD | 124,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.55` | 8,670.00 USD | 124,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.75` | 20,290.00 USD | 124,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 141,230,000.00 USD | 0.00 USD | 2,520.00 USD | `-80.06%` | `129.70` |
| `Live` | `Long` | `20.05` | 141,220,000.00 USD | 0.00 USD | 501.25 USD | `-79.44%` | `25.00` |
| `Live` | `Long` | `20.25` | 141,220,000.00 USD | 0.00 USD | 730,740.00 USD | `-79.24%` | `36,085.73` |
| `Live` | `Long` | `20.55` | 140,490,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.93%` | `233.31` |
| `Live` | `Long` | `20.85` | 140,490,000.00 USD | 0.00 USD | 501.44 USD | `-78.62%` | `24.05` |
| `Live` | `Long` | `20.95` | 140,490,000.00 USD | 0.00 USD | 618.03 USD | `-78.52%` | `29.50` |
| `Live` | `Long` | `21.15` | 140,490,000.00 USD | 0.00 USD | 186.97 USD | `-78.31%` | `8.84` |
| `Live` | `Long` | `21.25` | 140,490,000.00 USD | 0.00 USD | 5,420.00 USD | `-78.21%` | `255.26` |
| `Live` | `Long` | `21.35` | 140,480,000.00 USD | 0.00 USD | 1,410.00 USD | `-78.11%` | `65.89` |
| `Live` | `Long` | `21.45` | 140,480,000.00 USD | 0.00 USD | 161.73 USD | `-78.01%` | `7.54` |
| `Live` | `Long` | `21.75` | 140,480,000.00 USD | 0.00 USD | 4,730.00 USD | `-77.70%` | `217.65` |
| `Live` | `Long` | `21.85` | 140,470,000.00 USD | 0.00 USD | 10,010.00 USD | `-77.60%` | `458.18` |
| `Live` | `Long` | `21.95` | 140,460,000.00 USD | 0.00 USD | 11,480.00 USD | `-77.49%` | `523.23` |
| `Live` | `Long` | `22.05` | 140,450,000.00 USD | 0.00 USD | 13,910.00 USD | `-77.39%` | `630.95` |
| `Live` | `Long` | `22.15` | 140,440,000.00 USD | 0.00 USD | 1,530.00 USD | `-77.29%` | `69.00` |
| `Live` | `Long` | `22.35` | 140,440,000.00 USD | 0.00 USD | 800.35 USD | `-77.08%` | `35.81` |
| `Live` | `Long` | `22.65` | 140,440,000.00 USD | 0.00 USD | 709.85 USD | `-76.78%` | `31.34` |
| `Live` | `Long` | `22.85` | 140,440,000.00 USD | 0.00 USD | 1,140.00 USD | `-76.57%` | `50.00` |
| `Live` | `Long` | `22.95` | 140,430,000.00 USD | 0.00 USD | 1,150.00 USD | `-76.47%` | `50.00` |
| `Live` | `Long` | `23.05` | 140,430,000.00 USD | 0.00 USD | 4,370.00 USD | `-76.37%` | `189.63` |
| `Live` | `Long` | `23.15` | 140,430,000.00 USD | 0.00 USD | 8,540.00 USD | `-76.26%` | `369.00` |
| `Live` | `Long` | `23.25` | 140,420,000.00 USD | 0.00 USD | 1,000.00 USD | `-76.16%` | `43.06` |
| `Live` | `Long` | `23.45` | 140,420,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.96%` | `58.86` |
| `Live` | `Long` | `23.55` | 140,420,000.00 USD | 0.00 USD | 8,260.00 USD | `-75.85%` | `350.93` |
| `Live` | `Long` | `23.65` | 140,410,000.00 USD | 0.00 USD | 122.03 USD | `-75.75%` | `5.16` |
| `Live` | `Long` | `23.85` | 140,410,000.00 USD | 0.00 USD | 115.43 USD | `-75.55%` | `4.84` |
| `Live` | `Long` | `24.15` | 140,410,000.00 USD | 0.00 USD | 232.81 USD | `-75.24%` | `9.64` |
| `Live` | `Long` | `24.35` | 140,410,000.00 USD | 0.00 USD | 5,040.00 USD | `-75.03%` | `207.04` |
| `Live` | `Long` | `24.55` | 140,400,000.00 USD | 0.00 USD | 20,690.00 USD | `-74.83%` | `842.80` |
| `Live` | `Long` | `24.65` | 140,380,000.00 USD | 0.00 USD | 141,750.00 USD | `-74.73%` | `5,750.44` |
| `Live` | `Long` | `24.85` | 140,240,000.00 USD | 0.00 USD | 4,590.00 USD | `-74.52%` | `184.67` |
| `Live` | `Long` | `25.05` | 140,240,000.00 USD | 0.00 USD | 1,250.00 USD | `-74.32%` | `50.00` |
| `Live` | `Long` | `25.15` | 140,240,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.21%` | `80.00` |
| `Live` | `Long` | `25.35` | 140,230,000.00 USD | 0.00 USD | 37,230.00 USD | `-74.01%` | `1,468.70` |
| `Live` | `Long` | `25.45` | 140,200,000.00 USD | 0.00 USD | 106.64 USD | `-73.91%` | `4.19` |
| `Live` | `Long` | `25.95` | 140,200,000.00 USD | 0.00 USD | 2,930.00 USD | `-73.39%` | `113.00` |
| `Live` | `Long` | `26.25` | 140,190,000.00 USD | 0.00 USD | 136.24 USD | `-73.09%` | `5.19` |
| `Live` | `Long` | `26.35` | 140,190,000.00 USD | 0.00 USD | 475.09 USD | `-72.98%` | `18.03` |
| `Live` | `Long` | `26.45` | 140,190,000.00 USD | 0.00 USD | 13,230.00 USD | `-72.88%` | `500.00` |
| `Live` | `Long` | `26.55` | 140,180,000.00 USD | 0.00 USD | 161.95 USD | `-72.78%` | `6.10` |
| `Live` | `Long` | `26.65` | 140,180,000.00 USD | 0.00 USD | 814.96 USD | `-72.68%` | `30.58` |
| `Live` | `Long` | `26.75` | 140,180,000.00 USD | 0.00 USD | 4,310.00 USD | `-72.57%` | `161.06` |
| `Live` | `Long` | `26.95` | 140,170,000.00 USD | 0.00 USD | 238.78 USD | `-72.37%` | `8.86` |
| `Live` | `Long` | `27.05` | 140,170,000.00 USD | 0.00 USD | 31,230.00 USD | `-72.27%` | `1,154.39` |
| `Live` | `Long` | `27.15` | 140,140,000.00 USD | 0.00 USD | 29,640.00 USD | `-72.16%` | `1,091.87` |
| `Live` | `Long` | `27.25` | 140,110,000.00 USD | 0.00 USD | 4,460.00 USD | `-72.06%` | `163.78` |
| `Live` | `Long` | `27.35` | 140,110,000.00 USD | 0.00 USD | 717.12 USD | `-71.96%` | `26.22` |
| `Live` | `Long` | `27.65` | 140,110,000.00 USD | 0.00 USD | 82,950.00 USD | `-71.65%` | `3,000.00` |
| `Live` | `Long` | `27.75` | 140,030,000.00 USD | 0.00 USD | 55,500.00 USD | `-71.55%` | `2,000.00` |
| `Live` | `Long` | `27.85` | 139,970,000.00 USD | 0.00 USD | 412.18 USD | `-71.45%` | `14.80` |
| `Live` | `Long` | `28.05` | 139,970,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.24%` | `97.63` |
| `Live` | `Long` | `28.15` | 139,970,000.00 USD | 0.00 USD | 1,590.00 USD | `-71.14%` | `56.43` |
| `Live` | `Long` | `28.25` | 139,960,000.00 USD | 0.00 USD | 145.20 USD | `-71.04%` | `5.14` |
| `Live` | `Long` | `28.35` | 139,960,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.93%` | `218.55` |
| `Live` | `Long` | `28.45` | 139,960,000.00 USD | 0.00 USD | 113.80 USD | `-70.83%` | `4.00` |
| `Live` | `Long` | `28.55` | 139,960,000.00 USD | 0.00 USD | 418.54 USD | `-70.73%` | `14.66` |
| `Live` | `Long` | `28.65` | 139,960,000.00 USD | 0.00 USD | 5,630.00 USD | `-70.63%` | `196.65` |
| `Live` | `Long` | `28.85` | 139,950,000.00 USD | 0.00 USD | 12,270.00 USD | `-70.42%` | `425.17` |
| `Live` | `Long` | `28.95` | 139,940,000.00 USD | 0.00 USD | 6,800.00 USD | `-70.32%` | `235.00` |
| `Live` | `Long` | `29.05` | 139,930,000.00 USD | 0.00 USD | 16,100.00 USD | `-70.21%` | `554.29` |
| `Live` | `Long` | `29.15` | 139,920,000.00 USD | 0.00 USD | 10,940.00 USD | `-70.11%` | `375.19` |
| `Live` | `Long` | `29.85` | 139,910,000.00 USD | 0.00 USD | 44,770.00 USD | `-69.39%` | `1,500.00` |
| `Live` | `Long` | `29.95` | 139,860,000.00 USD | 0.00 USD | 131.48 USD | `-69.29%` | `4.39` |
| `Live` | `Long` | `30.05` | 139,860,000.00 USD | 0.00 USD | 7,900.00 USD | `-69.19%` | `263.04` |
| `Live` | `Long` | `30.15` | 139,850,000.00 USD | 0.00 USD | 47,340.00 USD | `-69.09%` | `1,570.00` |
| `Live` | `Long` | `30.25` | 139,810,000.00 USD | 0.00 USD | 513,140.00 USD | `-68.98%` | `16,963.19` |
| `Live` | `Long` | `30.55` | 139,290,000.00 USD | 0.00 USD | 3,210.00 USD | `-68.68%` | `104.93` |
| `Live` | `Long` | `30.65` | 139,290,000.00 USD | 0.00 USD | 233.86 USD | `-68.57%` | `7.63` |
| `Live` | `Long` | `30.85` | 139,290,000.00 USD | 0.00 USD | 350.76 USD | `-68.37%` | `11.37` |
| `Live` | `Long` | `30.95` | 139,290,000.00 USD | 0.00 USD | 314.76 USD | `-68.27%` | `10.17` |
| `Live` | `Long` | `31.05` | 139,290,000.00 USD | 0.00 USD | 3,100.00 USD | `-68.16%` | `100.00` |
| `Live` | `Long` | `31.15` | 139,290,000.00 USD | 0.00 USD | 827.34 USD | `-68.06%` | `26.56` |
| `Live` | `Long` | `31.25` | 139,280,000.00 USD | 0.00 USD | 1,520.00 USD | `-67.96%` | `48.64` |
| `Live` | `Long` | `31.45` | 139,280,000.00 USD | 0.00 USD | 278.33 USD | `-67.75%` | `8.85` |
| `Live` | `Long` | `32.05` | 139,280,000.00 USD | 0.00 USD | 473.70 USD | `-67.14%` | `14.78` |
| `Live` | `Long` | `32.35` | 139,280,000.00 USD | 0.00 USD | 6,280.00 USD | `-66.83%` | `194.07` |
| `Live` | `Long` | `32.45` | 139,280,000.00 USD | 0.00 USD | 1,180.00 USD | `-66.73%` | `36.37` |
| `Live` | `Long` | `32.55` | 139,280,000.00 USD | 0.00 USD | 1,810.00 USD | `-66.63%` | `55.47` |
| `Live` | `Long` | `32.85` | 139,270,000.00 USD | 0.00 USD | 5,240.00 USD | `-66.32%` | `159.61` |
| `Live` | `Long` | `33.05` | 139,270,000.00 USD | 0.00 USD | 1,430.00 USD | `-66.11%` | `43.29` |
| `Live` | `Long` | `33.35` | 139,270,000.00 USD | 0.00 USD | 1,120.00 USD | `-65.81%` | `33.68` |
| `Live` | `Long` | `33.65` | 139,270,000.00 USD | 0.00 USD | 5,990.00 USD | `-65.50%` | `177.89` |
| `Live` | `Long` | `34.45` | 139,260,000.00 USD | 0.00 USD | 867,050.00 USD | `-64.68%` | `25,168.30` |
| `Live` | `Long` | `34.55` | 138,390,000.00 USD | 0.00 USD | 4,040.00 USD | `-64.58%` | `116.90` |
| `Live` | `Long` | `34.65` | 138,390,000.00 USD | 0.00 USD | 4,600.00 USD | `-64.47%` | `132.83` |
| `Live` | `Long` | `34.75` | 138,380,000.00 USD | 0.00 USD | 1,230.00 USD | `-64.37%` | `35.38` |
| `Live` | `Long` | `34.95` | 138,380,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-64.17%` | `189,475.65` |
| `Live` | `Long` | `35.15` | 131,760,000.00 USD | 0.00 USD | 39,390.00 USD | `-63.96%` | `1,120.70` |
| `Live` | `Long` | `35.25` | 131,720,000.00 USD | 0.00 USD | 17,620.00 USD | `-63.86%` | `500.00` |
| `Live` | `Long` | `35.35` | 131,700,000.00 USD | 0.00 USD | 987.68 USD | `-63.76%` | `27.94` |
| `Live` | `Long` | `35.45` | 131,700,000.00 USD | 0.00 USD | 250.99 USD | `-63.65%` | `7.08` |
| `Live` | `Long` | `35.75` | 131,700,000.00 USD | 0.00 USD | 4,840.00 USD | `-63.35%` | `135.34` |
| `Live` | `Long` | `35.85` | 131,700,000.00 USD | 0.00 USD | 537.75 USD | `-63.24%` | `15.00` |
| `Live` | `Long` | `35.95` | 131,700,000.00 USD | 0.00 USD | 5,610.00 USD | `-63.14%` | `156.13` |
| `Live` | `Long` | `36.05` | 131,690,000.00 USD | 0.00 USD | 8,400.00 USD | `-63.04%` | `232.92` |
| `Live` | `Long` | `36.15` | 131,680,000.00 USD | 0.00 USD | 531.41 USD | `-62.94%` | `14.70` |
| `Live` | `Long` | `36.25` | 131,680,000.00 USD | 0.00 USD | 3,980.00 USD | `-62.83%` | `109.90` |
| `Live` | `Long` | `36.35` | 131,680,000.00 USD | 0.00 USD | 867,550.00 USD | `-62.73%` | `23,866.56` |
| `Live` | `Long` | `36.45` | 130,810,000.00 USD | 0.00 USD | 300,360.00 USD | `-62.63%` | `8,240.28` |
| `Live` | `Long` | `36.75` | 130,510,000.00 USD | 0.00 USD | 500.90 USD | `-62.32%` | `13.63` |
| `Live` | `Long` | `36.85` | 130,510,000.00 USD | 0.00 USD | 320.59 USD | `-62.22%` | `8.70` |
| `Live` | `Long` | `36.95` | 130,510,000.00 USD | 0.00 USD | 1,910.00 USD | `-62.11%` | `51.75` |
| `Live` | `Long` | `37.05` | 130,510,000.00 USD | 0.00 USD | 2,220.00 USD | `-62.01%` | `60.00` |
| `Live` | `Long` | `37.15` | 130,510,000.00 USD | 0.00 USD | 17,870.00 USD | `-61.91%` | `481.01` |
| `Live` | `Long` | `37.25` | 130,490,000.00 USD | 0.00 USD | 58,200.00 USD | `-61.81%` | `1,562.47` |
| `Live` | `Long` | `37.35` | 130,430,000.00 USD | 0.00 USD | 19,600.00 USD | `-61.70%` | `524.75` |
| `Live` | `Long` | `37.45` | 130,410,000.00 USD | 0.00 USD | 401.84 USD | `-61.60%` | `10.73` |
| `Live` | `Long` | `37.55` | 130,410,000.00 USD | 0.00 USD | 22,820.00 USD | `-61.50%` | `607.75` |
| `Live` | `Long` | `37.65` | 130,390,000.00 USD | 0.00 USD | 2,430.00 USD | `-61.40%` | `64.52` |
| `Live` | `Long` | `37.95` | 130,380,000.00 USD | 0.00 USD | 4,160.00 USD | `-61.09%` | `109.49` |
| `Live` | `Long` | `38.05` | 130,380,000.00 USD | 0.00 USD | 768.99 USD | `-60.99%` | `20.21` |
| `Live` | `Long` | `38.15` | 130,380,000.00 USD | 0.00 USD | 2,300.00 USD | `-60.88%` | `60.30` |
| `Live` | `Long` | `38.25` | 130,380,000.00 USD | 0.00 USD | 191,380.00 USD | `-60.78%` | `5,003.28` |
| `Live` | `Long` | `38.35` | 130,190,000.00 USD | 0.00 USD | 388.10 USD | `-60.68%` | `10.12` |
| `Live` | `Long` | `38.45` | 130,190,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-60.58%` | `79,280.00` |
| `Live` | `Long` | `38.55` | 127,140,000.00 USD | 0.00 USD | 51,820.00 USD | `-60.47%` | `1,344.19` |
| `Live` | `Long` | `38.75` | 127,090,000.00 USD | 0.00 USD | 736.64 USD | `-60.27%` | `19.01` |
| `Live` | `Long` | `38.85` | 127,080,000.00 USD | 0.00 USD | 4,270.00 USD | `-60.17%` | `109.96` |
| `Live` | `Long` | `38.95` | 127,080,000.00 USD | 0.00 USD | 607.62 USD | `-60.06%` | `15.60` |
| `Live` | `Long` | `39.05` | 127,080,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.96%` | `1,292.50` |
| `Live` | `Long` | `39.35` | 127,030,000.00 USD | 0.00 USD | 11,490.00 USD | `-59.65%` | `292.08` |
| `Live` | `Long` | `39.45` | 127,020,000.00 USD | 0.00 USD | 1,330.00 USD | `-59.55%` | `33.74` |
| `Live` | `Long` | `39.55` | 127,020,000.00 USD | 0.00 USD | 596,880.00 USD | `-59.45%` | `15,091.67` |
| `Live` | `Long` | `39.65` | 126,420,000.00 USD | 0.00 USD | 114,640.00 USD | `-59.35%` | `2,891.25` |
| `Live` | `Long` | `39.75` | 126,300,000.00 USD | 0.00 USD | 102,950.00 USD | `-59.24%` | `2,590.06` |
| `Live` | `Long` | `39.85` | 126,200,000.00 USD | 0.00 USD | 2,260.00 USD | `-59.14%` | `56.71` |
| `Live` | `Long` | `40.05` | 126,200,000.00 USD | 0.00 USD | 1,510.00 USD | `-58.94%` | `37.77` |
| `Live` | `Long` | `40.15` | 126,200,000.00 USD | 0.00 USD | 20,740.00 USD | `-58.83%` | `516.59` |
| `Live` | `Long` | `40.25` | 126,180,000.00 USD | 0.00 USD | 632.73 USD | `-58.73%` | `15.72` |
| `Live` | `Long` | `40.55` | 126,180,000.00 USD | 0.00 USD | 3,270.00 USD | `-58.42%` | `80.66` |
| `Live` | `Long` | `40.65` | 126,170,000.00 USD | 0.00 USD | 292.68 USD | `-58.32%` | `7.20` |
| `Live` | `Long` | `40.75` | 126,170,000.00 USD | 0.00 USD | 5,130.00 USD | `-58.22%` | `125.92` |
| `Live` | `Long` | `40.85` | 126,170,000.00 USD | 0.00 USD | 9,250.00 USD | `-58.12%` | `226.50` |
| `Live` | `Long` | `40.95` | 126,160,000.00 USD | 0.00 USD | 142.10 USD | `-58.01%` | `3.47` |
| `Live` | `Long` | `41.05` | 126,160,000.00 USD | 0.00 USD | 14,570.00 USD | `-57.91%` | `354.99` |
| `Live` | `Long` | `41.15` | 126,140,000.00 USD | 0.00 USD | 1,070.00 USD | `-57.81%` | `26.08` |
| `Live` | `Long` | `41.25` | 126,140,000.00 USD | 0.00 USD | 368.36 USD | `-57.71%` | `8.93` |
| `Live` | `Long` | `41.35` | 126,140,000.00 USD | 0.00 USD | 418.46 USD | `-57.60%` | `10.12` |
| `Live` | `Long` | `41.45` | 126,140,000.00 USD | 0.00 USD | 9,130.00 USD | `-57.50%` | `220.26` |
| `Live` | `Long` | `41.55` | 126,130,000.00 USD | 0.00 USD | 130.88 USD | `-57.40%` | `3.15` |
| `Live` | `Long` | `41.65` | 126,130,000.00 USD | 0.00 USD | 770.11 USD | `-57.30%` | `18.49` |
| `Live` | `Long` | `41.75` | 126,130,000.00 USD | 0.00 USD | 2,460.00 USD | `-57.19%` | `59.03` |
| `Live` | `Long` | `41.85` | 126,130,000.00 USD | 0.00 USD | 2,850.00 USD | `-57.09%` | `68.06` |
| `Live` | `Long` | `41.95` | 126,130,000.00 USD | 0.00 USD | 48,400.00 USD | `-56.99%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 126,080,000.00 USD | 0.00 USD | 470.12 USD | `-56.89%` | `11.18` |
| `Live` | `Long` | `42.15` | 126,080,000.00 USD | 0.00 USD | 17,340.00 USD | `-56.78%` | `411.33` |
| `Live` | `Long` | `42.25` | 126,060,000.00 USD | 0.00 USD | 6,100.00 USD | `-56.68%` | `144.34` |
| `Live` | `Long` | `42.35` | 126,050,000.00 USD | 0.00 USD | 4,430.00 USD | `-56.58%` | `104.69` |
| `Live` | `Long` | `42.45` | 126,050,000.00 USD | 0.00 USD | 5,580.00 USD | `-56.48%` | `131.50` |
| `Live` | `Long` | `42.85` | 126,040,000.00 USD | 0.00 USD | 44,420.00 USD | `-56.07%` | `1,036.53` |
| `Live` | `Long` | `42.95` | 126,000,000.00 USD | 0.00 USD | 389.56 USD | `-55.96%` | `9.07` |
| `Live` | `Long` | `43.35` | 126,000,000.00 USD | 0.00 USD | 16,590.00 USD | `-55.55%` | `382.64` |
| `Live` | `Long` | `43.55` | 125,980,000.00 USD | 0.00 USD | 34,910.00 USD | `-55.35%` | `801.71` |
| `Live` | `Long` | `43.65` | 125,950,000.00 USD | 0.00 USD | 2,400.00 USD | `-55.25%` | `54.88` |
| `Live` | `Long` | `43.75` | 125,950,000.00 USD | 0.00 USD | 311.94 USD | `-55.14%` | `7.13` |
| `Live` | `Long` | `43.85` | 125,950,000.00 USD | 0.00 USD | 106.56 USD | `-55.04%` | `2.43` |
| `Live` | `Long` | `43.95` | 125,950,000.00 USD | 0.00 USD | 242.16 USD | `-54.94%` | `5.51` |
| `Live` | `Long` | `44.05` | 125,940,000.00 USD | 0.00 USD | 11,220.00 USD | `-54.84%` | `254.69` |
| `Live` | `Long` | `44.15` | 125,930,000.00 USD | 0.00 USD | 165.56 USD | `-54.73%` | `3.75` |
| `Live` | `Long` | `44.25` | 125,930,000.00 USD | 0.00 USD | 6,110.00 USD | `-54.63%` | `138.09` |
| `Live` | `Long` | `44.35` | 125,930,000.00 USD | 0.00 USD | 2,380.00 USD | `-54.53%` | `53.68` |
| `Live` | `Long` | `44.45` | 125,930,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.43%` | `229.02` |
| `Live` | `Long` | `44.55` | 125,910,000.00 USD | 0.00 USD | 3,660,000.00 USD | `-54.32%` | `82,257.93` |
| `Live` | `Long` | `44.65` | 122,250,000.00 USD | 0.00 USD | 841.21 USD | `-54.22%` | `18.84` |
| `Live` | `Long` | `44.75` | 122,250,000.00 USD | 0.00 USD | 1,790.00 USD | `-54.12%` | `39.98` |
| `Live` | `Long` | `44.85` | 122,250,000.00 USD | 0.00 USD | 8,260.00 USD | `-54.02%` | `184.26` |
| `Live` | `Long` | `44.95` | 122,240,000.00 USD | 0.00 USD | 4,350.00 USD | `-53.91%` | `96.78` |
| `Live` | `Long` | `45.05` | 122,240,000.00 USD | 0.00 USD | 2,970.00 USD | `-53.81%` | `65.96` |
| `Live` | `Long` | `45.15` | 122,230,000.00 USD | 0.00 USD | 5,940.00 USD | `-53.71%` | `131.48` |
| `Live` | `Long` | `45.35` | 122,230,000.00 USD | 0.00 USD | 13,790.00 USD | `-53.50%` | `304.09` |
| `Live` | `Long` | `45.45` | 122,210,000.00 USD | 0.00 USD | 9,480.00 USD | `-53.40%` | `208.64` |
| `Live` | `Long` | `45.55` | 122,200,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.30%` | `174.26` |
| `Live` | `Long` | `45.65` | 122,190,000.00 USD | 0.00 USD | 774.22 USD | `-53.19%` | `16.96` |
| `Live` | `Long` | `45.75` | 122,190,000.00 USD | 0.00 USD | 9,450.00 USD | `-53.09%` | `206.46` |
| `Live` | `Long` | `45.85` | 122,180,000.00 USD | 0.00 USD | 458.50 USD | `-52.99%` | `10.00` |
| `Live` | `Long` | `45.95` | 122,180,000.00 USD | 0.00 USD | 74,660.00 USD | `-52.89%` | `1,624.74` |
| `Live` | `Long` | `46.05` | 122,110,000.00 USD | 0.00 USD | 281.83 USD | `-52.78%` | `6.12` |
| `Live` | `Long` | `46.15` | 122,110,000.00 USD | 0.00 USD | 42,900.00 USD | `-52.68%` | `929.57` |
| `Live` | `Long` | `46.45` | 122,070,000.00 USD | 0.00 USD | 1,220.00 USD | `-52.37%` | `26.37` |
| `Live` | `Long` | `46.55` | 122,070,000.00 USD | 0.00 USD | 522.76 USD | `-52.27%` | `11.23` |
| `Live` | `Long` | `46.65` | 122,060,000.00 USD | 0.00 USD | 542.07 USD | `-52.17%` | `11.62` |
| `Live` | `Long` | `46.75` | 122,060,000.00 USD | 0.00 USD | 11,410.00 USD | `-52.07%` | `243.98` |
| `Live` | `Long` | `46.85` | 122,050,000.00 USD | 0.00 USD | 140.55 USD | `-51.96%` | `3.00` |
| `Live` | `Long` | `46.95` | 122,050,000.00 USD | 0.00 USD | 22,000.00 USD | `-51.86%` | `468.60` |
| `Live` | `Long` | `47.15` | 122,030,000.00 USD | 0.00 USD | 4,130.00 USD | `-51.66%` | `87.50` |
| `Live` | `Long` | `47.25` | 122,030,000.00 USD | 0.00 USD | 4,560.00 USD | `-51.55%` | `96.59` |
| `Live` | `Long` | `47.55` | 122,020,000.00 USD | 0.00 USD | 4,860.00 USD | `-51.25%` | `102.23` |
| `Live` | `Long` | `47.65` | 122,020,000.00 USD | 0.00 USD | 3,480.00 USD | `-51.14%` | `73.02` |
| `Live` | `Long` | `47.75` | 122,010,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-51.04%` | `24,003.37` |
| `Live` | `Long` | `47.95` | 120,870,000.00 USD | 0.00 USD | 10,310.00 USD | `-50.84%` | `215.05` |
| `Live` | `Long` | `48.05` | 120,860,000.00 USD | 0.00 USD | 4,630.00 USD | `-50.73%` | `96.46` |
| `Live` | `Long` | `48.15` | 120,850,000.00 USD | 0.00 USD | 5,470.00 USD | `-50.63%` | `113.54` |
| `Live` | `Long` | `48.25` | 120,850,000.00 USD | 0.00 USD | 2,780.00 USD | `-50.53%` | `57.66` |
| `Live` | `Long` | `48.35` | 120,840,000.00 USD | 0.00 USD | 11,200.00 USD | `-50.43%` | `231.69` |
| `Live` | `Long` | `48.45` | 120,830,000.00 USD | 0.00 USD | 2,930.00 USD | `-50.32%` | `60.44` |
| `Live` | `Long` | `48.55` | 120,830,000.00 USD | 0.00 USD | 2,870.00 USD | `-50.22%` | `59.06` |
| `Live` | `Long` | `48.65` | 120,830,000.00 USD | 0.00 USD | 8,450.00 USD | `-50.12%` | `173.68` |
| `Live` | `Long` | `48.75` | 120,820,000.00 USD | 0.00 USD | 3,280.00 USD | `-50.02%` | `67.31` |
| `Live` | `Long` | `48.85` | 120,820,000.00 USD | 0.00 USD | 12,920.00 USD | `-49.91%` | `264.57` |
| `Live` | `Long` | `48.95` | 120,800,000.00 USD | 0.00 USD | 1,530.00 USD | `-49.81%` | `31.26` |
| `Live` | `Long` | `49.05` | 120,800,000.00 USD | 0.00 USD | 1,270.00 USD | `-49.71%` | `25.86` |
| `Live` | `Long` | `49.25` | 120,800,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.50%` | `430.30` |
| `Live` | `Long` | `49.35` | 120,780,000.00 USD | 0.00 USD | 585.29 USD | `-49.40%` | `11.86` |
| `Live` | `Long` | `49.45` | 120,780,000.00 USD | 0.00 USD | 16,730.00 USD | `-49.30%` | `338.38` |
| `Live` | `Long` | `49.55` | 120,760,000.00 USD | 0.00 USD | 627.80 USD | `-49.20%` | `12.67` |
| `Live` | `Long` | `49.65` | 120,760,000.00 USD | 0.00 USD | 8,890.00 USD | `-49.09%` | `179.12` |
| `Live` | `Long` | `49.75` | 120,750,000.00 USD | 0.00 USD | 5,230.00 USD | `-48.99%` | `105.03` |
| `Live` | `Long` | `49.85` | 120,750,000.00 USD | 0.00 USD | 5,450.00 USD | `-48.89%` | `109.35` |
| `Live` | `Long` | `49.95` | 120,740,000.00 USD | 0.00 USD | 20,850.00 USD | `-48.79%` | `417.37` |
| `Live` | `Long` | `50.05` | 120,720,000.00 USD | 0.00 USD | 8,560.00 USD | `-48.68%` | `171.08` |
| `Live` | `Long` | `50.15` | 120,710,000.00 USD | 0.00 USD | 2,030.00 USD | `-48.58%` | `40.52` |
| `Live` | `Long` | `50.25` | 120,710,000.00 USD | 0.00 USD | 10,370.00 USD | `-48.48%` | `206.32` |
| `Live` | `Long` | `50.45` | 120,700,000.00 USD | 0.00 USD | 3,820.00 USD | `-48.27%` | `75.77` |
| `Live` | `Long` | `50.55` | 120,700,000.00 USD | 0.00 USD | 3,770.00 USD | `-48.17%` | `74.49` |
| `Live` | `Long` | `50.65` | 120,690,000.00 USD | 0.00 USD | 337.33 USD | `-48.07%` | `6.66` |
| `Live` | `Long` | `50.75` | 120,690,000.00 USD | 0.00 USD | 12,850.00 USD | `-47.97%` | `253.20` |
| `Live` | `Long` | `50.85` | 120,680,000.00 USD | 0.00 USD | 20,140.00 USD | `-47.86%` | `396.09` |
| `Live` | `Long` | `50.95` | 120,660,000.00 USD | 0.00 USD | 2,270.00 USD | `-47.76%` | `44.46` |
| `Live` | `Long` | `51.05` | 120,660,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.66%` | `52.57` |
| `Live` | `Long` | `51.15` | 120,650,000.00 USD | 0.00 USD | 13,820.00 USD | `-47.56%` | `270.10` |
| `Live` | `Long` | `51.25` | 120,640,000.00 USD | 0.00 USD | 10,390.00 USD | `-47.45%` | `202.74` |
| `Live` | `Long` | `51.35` | 120,630,000.00 USD | 0.00 USD | 360.48 USD | `-47.35%` | `7.02` |
| `Live` | `Long` | `51.45` | 120,630,000.00 USD | 0.00 USD | 7,210.00 USD | `-47.25%` | `140.17` |
| `Live` | `Long` | `51.55` | 120,620,000.00 USD | 0.00 USD | 22,260.00 USD | `-47.15%` | `431.84` |
| `Live` | `Long` | `51.65` | 120,600,000.00 USD | 0.00 USD | 115,520.00 USD | `-47.04%` | `2,236.54` |
| `Live` | `Long` | `51.75` | 120,480,000.00 USD | 0.00 USD | 26,920.00 USD | `-46.94%` | `520.14` |
| `Live` | `Long` | `51.85` | 120,460,000.00 USD | 0.00 USD | 47,000.00 USD | `-46.84%` | `906.45` |
| `Live` | `Long` | `51.95` | 120,410,000.00 USD | 0.00 USD | 470,160.00 USD | `-46.74%` | `9,050.26` |
| `Live` | `Long` | `52.05` | 119,940,000.00 USD | 0.00 USD | 99,370.00 USD | `-46.63%` | `1,909.09` |
| `Live` | `Long` | `52.15` | 119,840,000.00 USD | 0.00 USD | 2,870.00 USD | `-46.53%` | `54.96` |
| `Live` | `Long` | `52.25` | 119,840,000.00 USD | 0.00 USD | 3,800.00 USD | `-46.43%` | `72.81` |
| `Live` | `Long` | `52.35` | 119,830,000.00 USD | 0.00 USD | 33,350.00 USD | `-46.33%` | `637.05` |
| `Live` | `Long` | `52.45` | 119,800,000.00 USD | 0.00 USD | 879.59 USD | `-46.22%` | `16.77` |
| `Live` | `Long` | `52.55` | 119,800,000.00 USD | 0.00 USD | 1,610.00 USD | `-46.12%` | `30.70` |
| `Live` | `Long` | `52.65` | 119,800,000.00 USD | 0.00 USD | 4,270.00 USD | `-46.02%` | `81.04` |
| `Live` | `Long` | `52.75` | 119,790,000.00 USD | 0.00 USD | 26,880.00 USD | `-45.92%` | `509.62` |
| `Live` | `Long` | `52.85` | 119,770,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.81%` | `177.38` |
| `Live` | `Long` | `52.95` | 119,760,000.00 USD | 0.00 USD | 5,010.00 USD | `-45.71%` | `94.63` |
| `Live` | `Long` | `53.05` | 119,750,000.00 USD | 0.00 USD | 5,460.00 USD | `-45.61%` | `102.95` |
| `Live` | `Long` | `53.15` | 119,750,000.00 USD | 0.00 USD | 6,350.00 USD | `-45.51%` | `119.38` |
| `Live` | `Long` | `53.25` | 119,740,000.00 USD | 0.00 USD | 1,790.00 USD | `-45.40%` | `33.70` |
| `Live` | `Long` | `53.35` | 119,740,000.00 USD | 0.00 USD | 2,130.00 USD | `-45.30%` | `39.99` |
| `Live` | `Long` | `53.45` | 119,740,000.00 USD | 0.00 USD | 34,810.00 USD | `-45.20%` | `651.25` |
| `Live` | `Long` | `53.55` | 119,700,000.00 USD | 0.00 USD | 43,250.00 USD | `-45.09%` | `807.62` |
| `Live` | `Long` | `53.65` | 119,660,000.00 USD | 0.00 USD | 3,220.00 USD | `-44.99%` | `59.93` |
| `Live` | `Long` | `53.75` | 119,660,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.89%` | `67.00` |
| `Live` | `Long` | `53.85` | 119,650,000.00 USD | 0.00 USD | 19,810.00 USD | `-44.79%` | `367.96` |
| `Live` | `Long` | `53.95` | 119,630,000.00 USD | 0.00 USD | 68,960.00 USD | `-44.68%` | `1,278.26` |
| `Live` | `Long` | `54.05` | 119,560,000.00 USD | 0.00 USD | 81,970.00 USD | `-44.58%` | `1,516.49` |
| `Live` | `Long` | `54.15` | 119,480,000.00 USD | 0.00 USD | 15,030.00 USD | `-44.48%` | `277.53` |
| `Live` | `Long` | `54.25` | 119,470,000.00 USD | 0.00 USD | 57,560.00 USD | `-44.38%` | `1,061.09` |
| `Live` | `Long` | `54.35` | 119,410,000.00 USD | 0.00 USD | 1,800.00 USD | `-44.27%` | `33.16` |
| `Live` | `Long` | `54.45` | 119,410,000.00 USD | 0.00 USD | 753.04 USD | `-44.17%` | `13.83` |
| `Live` | `Long` | `54.55` | 119,410,000.00 USD | 0.00 USD | 85,190.00 USD | `-44.07%` | `1,561.73` |
| `Live` | `Long` | `54.65` | 119,320,000.00 USD | 0.00 USD | 2,420.00 USD | `-43.97%` | `44.29` |
| `Live` | `Long` | `54.75` | 119,320,000.00 USD | 0.00 USD | 17,320.00 USD | `-43.86%` | `316.32` |
| `Live` | `Long` | `54.85` | 119,300,000.00 USD | 0.00 USD | 946,880.00 USD | `-43.76%` | `17,263.07` |
| `Live` | `Long` | `54.95` | 118,350,000.00 USD | 0.00 USD | 142,320.00 USD | `-43.66%` | `2,590.04` |
| `Live` | `Long` | `55.05` | 118,210,000.00 USD | 0.00 USD | 4,910.00 USD | `-43.56%` | `89.15` |
| `Live` | `Long` | `55.15` | 118,210,000.00 USD | 0.00 USD | 654.08 USD | `-43.45%` | `11.86` |
| `Live` | `Long` | `55.25` | 118,210,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.35%` | `36.31` |
| `Live` | `Long` | `55.35` | 118,200,000.00 USD | 0.00 USD | 9,810.00 USD | `-43.25%` | `177.30` |
| `Live` | `Long` | `55.45` | 118,190,000.00 USD | 0.00 USD | 5,620.00 USD | `-43.15%` | `101.35` |
| `Live` | `Long` | `55.55` | 118,190,000.00 USD | 0.00 USD | 13,240.00 USD | `-43.04%` | `238.37` |
| `Live` | `Long` | `55.65` | 118,180,000.00 USD | 0.00 USD | 8,520.00 USD | `-42.94%` | `153.01` |
| `Live` | `Long` | `55.75` | 118,170,000.00 USD | 0.00 USD | 86,030.00 USD | `-42.84%` | `1,543.18` |
| `Live` | `Long` | `55.85` | 118,080,000.00 USD | 0.00 USD | 4,090.00 USD | `-42.74%` | `73.18` |
| `Live` | `Long` | `55.95` | 118,080,000.00 USD | 0.00 USD | 7,890.00 USD | `-42.63%` | `140.97` |
| `Live` | `Long` | `56.05` | 118,070,000.00 USD | 0.00 USD | 7,190.00 USD | `-42.53%` | `128.30` |
| `Live` | `Long` | `56.15` | 118,060,000.00 USD | 0.00 USD | 36,190.00 USD | `-42.43%` | `644.50` |
| `Live` | `Long` | `56.25` | 118,030,000.00 USD | 0.00 USD | 17,970.00 USD | `-42.33%` | `319.43` |
| `Live` | `Long` | `56.35` | 118,010,000.00 USD | 0.00 USD | 19,410.00 USD | `-42.22%` | `344.45` |
| `Live` | `Long` | `56.45` | 117,990,000.00 USD | 0.00 USD | 5,350.00 USD | `-42.12%` | `94.82` |
| `Live` | `Long` | `56.55` | 117,980,000.00 USD | 0.00 USD | 27,410.00 USD | `-42.02%` | `484.71` |
| `Live` | `Long` | `56.65` | 117,960,000.00 USD | 0.00 USD | 14,910.00 USD | `-41.92%` | `263.26` |
| `Live` | `Long` | `56.75` | 117,940,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.81%` | `165.87` |
| `Live` | `Long` | `56.85` | 117,930,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-41.71%` | `19,776.98` |
| `Live` | `Long` | `56.95` | 116,810,000.00 USD | 0.00 USD | 2,320,000.00 USD | `-41.61%` | `40,751.38` |
| `Live` | `Long` | `57.05` | 114,490,000.00 USD | 0.00 USD | 13,460.00 USD | `-41.51%` | `235.86` |
| `Live` | `Long` | `57.15` | 114,470,000.00 USD | 0.00 USD | 5,380.00 USD | `-41.40%` | `94.22` |
| `Live` | `Long` | `57.25` | 114,470,000.00 USD | 0.00 USD | 15,200.00 USD | `-41.30%` | `265.54` |
| `Live` | `Long` | `57.35` | 114,450,000.00 USD | 0.00 USD | 14,740.00 USD | `-41.20%` | `257.07` |
| `Live` | `Long` | `57.45` | 114,440,000.00 USD | 0.00 USD | 17,480.00 USD | `-41.10%` | `304.28` |
| `Live` | `Long` | `57.55` | 114,420,000.00 USD | 0.00 USD | 924.25 USD | `-40.99%` | `16.06` |
| `Live` | `Long` | `57.65` | 114,420,000.00 USD | 0.00 USD | 18,730.00 USD | `-40.89%` | `324.85` |
| `Live` | `Long` | `57.75` | 114,400,000.00 USD | 0.00 USD | 90,210.00 USD | `-40.79%` | `1,562.00` |
| `Live` | `Long` | `57.85` | 114,310,000.00 USD | 0.00 USD | 80,450.00 USD | `-40.69%` | `1,390.59` |
| `Live` | `Long` | `57.95` | 114,230,000.00 USD | 0.00 USD | 324.52 USD | `-40.58%` | `5.60` |
| `Live` | `Long` | `58.05` | 114,230,000.00 USD | 0.00 USD | 4,710.00 USD | `-40.48%` | `81.10` |
| `Live` | `Long` | `58.15` | 114,220,000.00 USD | 0.00 USD | 124,470.00 USD | `-40.38%` | `2,140.55` |
| `Live` | `Long` | `58.25` | 114,100,000.00 USD | 0.00 USD | 23,110.00 USD | `-40.28%` | `396.72` |
| `Live` | `Long` | `58.35` | 114,080,000.00 USD | 0.00 USD | 23,460.00 USD | `-40.17%` | `402.05` |
| `Live` | `Long` | `58.45` | 114,050,000.00 USD | 0.00 USD | 61,260.00 USD | `-40.07%` | `1,048.03` |
| `Live` | `Long` | `58.55` | 113,990,000.00 USD | 0.00 USD | 3,150.00 USD | `-39.97%` | `53.84` |
| `Live` | `Long` | `58.65` | 113,990,000.00 USD | 0.00 USD | 418.17 USD | `-39.87%` | `7.13` |
| `Live` | `Long` | `58.75` | 113,990,000.00 USD | 0.00 USD | 350.74 USD | `-39.76%` | `5.97` |
| `Live` | `Long` | `58.85` | 113,990,000.00 USD | 0.00 USD | 6,630.00 USD | `-39.66%` | `112.70` |
| `Live` | `Long` | `58.95` | 113,980,000.00 USD | 0.00 USD | 488.70 USD | `-39.56%` | `8.29` |
| `Live` | `Long` | `59.05` | 113,980,000.00 USD | 0.00 USD | 14,900.00 USD | `-39.46%` | `252.36` |
| `Live` | `Long` | `59.15` | 113,970,000.00 USD | 0.00 USD | 4,870.00 USD | `-39.35%` | `82.25` |
| `Live` | `Long` | `59.25` | 113,960,000.00 USD | 0.00 USD | 418.90 USD | `-39.25%` | `7.07` |
| `Live` | `Long` | `59.35` | 113,960,000.00 USD | 0.00 USD | 28,320.00 USD | `-39.15%` | `477.21` |
| `Live` | `Long` | `59.45` | 113,930,000.00 USD | 0.00 USD | 4,230.00 USD | `-39.05%` | `71.12` |
| `Live` | `Long` | `59.55` | 113,930,000.00 USD | 0.00 USD | 8,610.00 USD | `-38.94%` | `144.57` |
| `Live` | `Long` | `59.65` | 113,920,000.00 USD | 0.00 USD | 18,020.00 USD | `-38.84%` | `302.16` |
| `Live` | `Long` | `59.75` | 113,900,000.00 USD | 0.00 USD | 33,460.00 USD | `-38.74%` | `560.08` |
| `Live` | `Long` | `59.85` | 113,870,000.00 USD | 0.00 USD | 407.58 USD | `-38.64%` | `6.81` |
| `Live` | `Long` | `59.95` | 113,870,000.00 USD | 0.00 USD | 58,710.00 USD | `-38.53%` | `979.37` |
| `Live` | `Long` | `60.05` | 113,810,000.00 USD | 0.00 USD | 12,840.00 USD | `-38.43%` | `213.86` |
| `Live` | `Long` | `60.15` | 113,800,000.00 USD | 0.00 USD | 36,310.00 USD | `-38.33%` | `603.62` |
| `Live` | `Long` | `60.25` | 113,760,000.00 USD | 0.00 USD | 2,340.00 USD | `-38.23%` | `38.84` |
| `Live` | `Long` | `60.35` | 113,760,000.00 USD | 0.00 USD | 2,710.00 USD | `-38.12%` | `44.97` |
| `Live` | `Long` | `60.45` | 113,750,000.00 USD | 0.00 USD | 1,770.00 USD | `-38.02%` | `29.22` |
| `Live` | `Long` | `60.55` | 113,750,000.00 USD | 0.00 USD | 2,760.00 USD | `-37.92%` | `45.51` |
| `Live` | `Long` | `60.65` | 113,750,000.00 USD | 0.00 USD | 150,050.00 USD | `-37.82%` | `2,474.06` |
| `Live` | `Long` | `60.75` | 113,600,000.00 USD | 0.00 USD | 9,700.00 USD | `-37.71%` | `159.72` |
| `Live` | `Long` | `60.85` | 113,590,000.00 USD | 0.00 USD | 28,700.00 USD | `-37.61%` | `471.62` |
| `Live` | `Long` | `60.95` | 113,560,000.00 USD | 0.00 USD | 54,910.00 USD | `-37.51%` | `900.96` |
| `Live` | `Long` | `61.05` | 113,510,000.00 USD | 0.00 USD | 4,230.00 USD | `-37.41%` | `69.34` |
| `Live` | `Long` | `61.15` | 113,500,000.00 USD | 0.00 USD | 4,120.00 USD | `-37.30%` | `67.43` |
| `Live` | `Long` | `61.25` | 113,500,000.00 USD | 0.00 USD | 139,530.00 USD | `-37.20%` | `2,278.06` |
| `Live` | `Long` | `61.35` | 113,360,000.00 USD | 0.00 USD | 12,920.00 USD | `-37.10%` | `210.52` |
| `Live` | `Long` | `61.45` | 113,350,000.00 USD | 0.00 USD | 21,290.00 USD | `-37.00%` | `346.45` |
| `Live` | `Long` | `61.55` | 113,320,000.00 USD | 0.00 USD | 18,590.00 USD | `-36.89%` | `301.98` |
| `Live` | `Long` | `61.65` | 113,310,000.00 USD | 0.00 USD | 22,370.00 USD | `-36.79%` | `362.80` |
| `Live` | `Long` | `61.75` | 113,280,000.00 USD | 0.00 USD | 69,530.00 USD | `-36.69%` | `1,126.01` |
| `Live` | `Long` | `61.85` | 113,210,000.00 USD | 0.00 USD | 5,780.00 USD | `-36.58%` | `93.47` |
| `Live` | `Long` | `61.95` | 113,210,000.00 USD | 0.00 USD | 8,430.00 USD | `-36.48%` | `136.15` |
| `Live` | `Long` | `62.05` | 113,200,000.00 USD | 0.00 USD | 9,000.00 USD | `-36.38%` | `145.05` |
| `Live` | `Long` | `62.15` | 113,190,000.00 USD | 0.00 USD | 26,400.00 USD | `-36.28%` | `424.71` |
| `Live` | `Long` | `62.25` | 113,160,000.00 USD | 0.00 USD | 1,800.00 USD | `-36.17%` | `28.90` |
| `Live` | `Long` | `62.35` | 113,160,000.00 USD | 0.00 USD | 43,640.00 USD | `-36.07%` | `699.89` |
| `Live` | `Long` | `62.45` | 113,120,000.00 USD | 0.00 USD | 20,480.00 USD | `-35.97%` | `327.96` |
| `Live` | `Long` | `62.55` | 113,100,000.00 USD | 0.00 USD | 3,130.00 USD | `-35.87%` | `50.00` |
| `Live` | `Long` | `62.65` | 113,100,000.00 USD | 0.00 USD | 4,060.00 USD | `-35.76%` | `64.85` |
| `Live` | `Long` | `62.75` | 113,090,000.00 USD | 0.00 USD | 3,290.00 USD | `-35.66%` | `52.49` |
| `Live` | `Long` | `62.85` | 113,090,000.00 USD | 0.00 USD | 48,000.00 USD | `-35.56%` | `763.76` |
| `Live` | `Long` | `62.95` | 113,040,000.00 USD | 0.00 USD | 67,330.00 USD | `-35.46%` | `1,069.59` |
| `Live` | `Long` | `63.05` | 112,970,000.00 USD | 0.00 USD | 54,010.00 USD | `-35.35%` | `856.60` |
| `Live` | `Long` | `63.15` | 112,920,000.00 USD | 0.00 USD | 84,650.00 USD | `-35.25%` | `1,340.43` |
| `Live` | `Long` | `63.25` | 112,830,000.00 USD | 0.00 USD | 77,870.00 USD | `-35.15%` | `1,231.15` |
| `Live` | `Long` | `63.35` | 112,760,000.00 USD | 0.00 USD | 224.26 USD | `-35.05%` | `3.54` |
| `Live` | `Long` | `63.45` | 112,760,000.00 USD | 0.00 USD | 43,420.00 USD | `-34.94%` | `684.37` |
| `Live` | `Long` | `63.55` | 112,710,000.00 USD | 0.00 USD | 6,000.00 USD | `-34.84%` | `94.40` |
| `Live` | `Long` | `63.65` | 112,710,000.00 USD | 0.00 USD | 8,840.00 USD | `-34.74%` | `138.96` |
| `Live` | `Long` | `63.75` | 112,700,000.00 USD | 0.00 USD | 8,560.00 USD | `-34.64%` | `134.23` |
| `Live` | `Long` | `63.85` | 112,690,000.00 USD | 0.00 USD | 38,350.00 USD | `-34.53%` | `600.57` |
| `Live` | `Long` | `63.95` | 112,650,000.00 USD | 0.00 USD | 6,310.00 USD | `-34.43%` | `98.68` |
| `Live` | `Long` | `64.25` | 112,640,000.00 USD | 0.00 USD | 4,920.00 USD | `-34.12%` | `76.51` |
| `Live` | `Long` | `64.35` | 112,640,000.00 USD | 0.00 USD | 16,160.00 USD | `-34.02%` | `251.05` |
| `Live` | `Long` | `64.45` | 112,620,000.00 USD | 0.00 USD | 174,880.00 USD | `-33.92%` | `2,713.49` |
| `Live` | `Long` | `64.55` | 112,450,000.00 USD | 0.00 USD | 6,660.00 USD | `-33.82%` | `103.17` |
| `Live` | `Long` | `64.65` | 112,440,000.00 USD | 0.00 USD | 1,740.00 USD | `-33.71%` | `26.99` |
| `Live` | `Long` | `64.75` | 112,440,000.00 USD | 0.00 USD | 388,660.00 USD | `-33.61%` | `6,002.50` |
| `Live` | `Long` | `64.85` | 112,050,000.00 USD | 0.00 USD | 3,220.00 USD | `-33.51%` | `49.73` |
| `Live` | `Long` | `64.95` | 112,050,000.00 USD | 0.00 USD | 6,700.00 USD | `-33.41%` | `103.23` |
| `Live` | `Long` | `65.05` | 112,040,000.00 USD | 0.00 USD | 11,820.00 USD | `-33.30%` | `181.73` |
| `Live` | `Long` | `65.15` | 112,030,000.00 USD | 0.00 USD | 11,050.00 USD | `-33.20%` | `169.64` |
| `Live` | `Long` | `65.25` | 112,020,000.00 USD | 0.00 USD | 47,410.00 USD | `-33.10%` | `726.59` |
| `Live` | `Long` | `65.35` | 111,970,000.00 USD | 0.00 USD | 122,690.00 USD | `-33.00%` | `1,877.46` |
| `Live` | `Long` | `65.45` | 111,850,000.00 USD | 0.00 USD | 630.94 USD | `-32.89%` | `9.64` |
| `Live` | `Long` | `65.55` | 111,850,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-32.79%` | `20,133.26` |
| `Live` | `Long` | `65.65` | 110,530,000.00 USD | 0.00 USD | 58,050.00 USD | `-32.69%` | `884.16` |
| `Live` | `Long` | `65.75` | 110,470,000.00 USD | 0.00 USD | 5,230.00 USD | `-32.59%` | `79.50` |
| `Live` | `Long` | `65.85` | 110,470,000.00 USD | 0.00 USD | 30,200.00 USD | `-32.48%` | `458.58` |
| `Live` | `Long` | `65.95` | 110,440,000.00 USD | 0.00 USD | 7,020.00 USD | `-32.38%` | `106.39` |
| `Live` | `Long` | `66.05` | 110,430,000.00 USD | 0.00 USD | 12,130.00 USD | `-32.28%` | `183.69` |
| `Live` | `Long` | `66.15` | 110,420,000.00 USD | 0.00 USD | 10,580.00 USD | `-32.18%` | `159.91` |
| `Live` | `Long` | `66.25` | 110,410,000.00 USD | 0.00 USD | 15,730.00 USD | `-32.07%` | `237.49` |
| `Live` | `Long` | `66.35` | 110,390,000.00 USD | 0.00 USD | 1,580.00 USD | `-31.97%` | `23.83` |
| `Live` | `Long` | `66.45` | 110,390,000.00 USD | 0.00 USD | 2,290.00 USD | `-31.87%` | `34.45` |
| `Live` | `Long` | `66.55` | 110,390,000.00 USD | 0.00 USD | 42,780.00 USD | `-31.77%` | `642.79` |
| `Live` | `Long` | `66.65` | 110,340,000.00 USD | 0.00 USD | 729.82 USD | `-31.66%` | `10.95` |
| `Live` | `Long` | `66.75` | 110,340,000.00 USD | 0.00 USD | 7,360.00 USD | `-31.56%` | `110.22` |
| `Live` | `Long` | `66.85` | 110,330,000.00 USD | 0.00 USD | 2,050.00 USD | `-31.46%` | `30.61` |
| `Live` | `Long` | `66.95` | 110,330,000.00 USD | 0.00 USD | 1,530.00 USD | `-31.36%` | `22.91` |
| `Live` | `Long` | `67.05` | 110,330,000.00 USD | 0.00 USD | 33,390.00 USD | `-31.25%` | `497.96` |
| `Live` | `Long` | `67.15` | 110,300,000.00 USD | 0.00 USD | 2,510.00 USD | `-31.15%` | `37.39` |
| `Live` | `Long` | `67.25` | 110,300,000.00 USD | 0.00 USD | 19,700.00 USD | `-31.05%` | `292.97` |
| `Live` | `Long` | `67.35` | 110,280,000.00 USD | 0.00 USD | 22,240.00 USD | `-30.95%` | `330.25` |
| `Live` | `Long` | `67.45` | 110,250,000.00 USD | 0.00 USD | 45,280.00 USD | `-30.84%` | `671.29` |
| `Live` | `Long` | `67.55` | 110,210,000.00 USD | 0.00 USD | 3,340,000.00 USD | `-30.74%` | `49,416.19` |
| `Live` | `Long` | `67.65` | 106,870,000.00 USD | 0.00 USD | 173,850.00 USD | `-30.64%` | `2,569.81` |
| `Live` | `Long` | `67.75` | 106,700,000.00 USD | 0.00 USD | 4,020.00 USD | `-30.54%` | `59.38` |
| `Live` | `Long` | `67.85` | 106,690,000.00 USD | 0.00 USD | 28,230.00 USD | `-30.43%` | `416.13` |
| `Live` | `Long` | `67.95` | 106,660,000.00 USD | 0.00 USD | 1,310.00 USD | `-30.33%` | `19.28` |
| `Live` | `Long` | `68.05` | 106,660,000.00 USD | 0.00 USD | 12,260,000.00 USD | `-30.23%` | `180,174.62` |
| `Live` | `Long` | `68.15` | 94,400,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-30.13%` | `550,124.70` |
| `Live` | `Long` | `68.25` | 56,910,000.00 USD | 0.00 USD | 17,060.00 USD | `-30.02%` | `249.92` |
| `Live` | `Long` | `68.35` | 56,890,000.00 USD | 0.00 USD | 2,860.00 USD | `-29.92%` | `41.82` |
| `Live` | `Long` | `68.45` | 56,890,000.00 USD | 0.00 USD | 24,310.00 USD | `-29.82%` | `355.18` |
| `Live` | `Long` | `68.55` | 56,870,000.00 USD | 0.00 USD | 21,500.00 USD | `-29.72%` | `313.66` |
| `Live` | `Long` | `68.65` | 56,850,000.00 USD | 0.00 USD | 783,800.00 USD | `-29.61%` | `11,417.29` |
| `Live` | `Long` | `68.75` | 56,060,000.00 USD | 0.00 USD | 47,370.00 USD | `-29.51%` | `689.03` |
| `Live` | `Long` | `68.85` | 56,010,000.00 USD | 0.00 USD | 4,550.00 USD | `-29.41%` | `66.10` |
| `Live` | `Long` | `68.95` | 56,010,000.00 USD | 0.00 USD | 69,280.00 USD | `-29.31%` | `1,004.72` |
| `Live` | `Long` | `69.05` | 55,940,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-29.20%` | `15,051.69` |
| `Live` | `Long` | `69.15` | 54,900,000.00 USD | 0.00 USD | 20,880.00 USD | `-29.10%` | `301.89` |
| `Live` | `Long` | `69.25` | 54,880,000.00 USD | 0.00 USD | 7,370.00 USD | `-29.00%` | `106.49` |
| `Live` | `Long` | `69.35` | 54,870,000.00 USD | 0.00 USD | 509.03 USD | `-28.90%` | `7.34` |
| `Live` | `Long` | `69.45` | 54,870,000.00 USD | 0.00 USD | 14,370.00 USD | `-28.79%` | `206.85` |
| `Live` | `Long` | `69.55` | 54,860,000.00 USD | 0.00 USD | 11,710.00 USD | `-28.69%` | `168.33` |
| `Live` | `Long` | `69.65` | 54,850,000.00 USD | 0.00 USD | 1,990.00 USD | `-28.59%` | `28.61` |
| `Live` | `Long` | `69.75` | 54,840,000.00 USD | 0.00 USD | 19,890.00 USD | `-28.49%` | `285.09` |
| `Live` | `Long` | `69.85` | 54,820,000.00 USD | 0.00 USD | 47,550.00 USD | `-28.38%` | `680.77` |
| `Live` | `Long` | `69.95` | 54,780,000.00 USD | 0.00 USD | 8,800.00 USD | `-28.28%` | `125.81` |
| `Live` | `Long` | `70.05` | 54,770,000.00 USD | 0.00 USD | 682.99 USD | `-28.18%` | `9.75` |
| `Live` | `Long` | `70.15` | 54,770,000.00 USD | 0.00 USD | 11,700.00 USD | `-28.07%` | `166.85` |
| `Live` | `Long` | `70.25` | 54,760,000.00 USD | 0.00 USD | 190,720.00 USD | `-27.97%` | `2,714.91` |
| `Live` | `Long` | `70.35` | 54,560,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-27.87%` | `30,492.00` |
| `Live` | `Long` | `70.45` | 52,420,000.00 USD | 0.00 USD | 113,380.00 USD | `-27.77%` | `1,609.42` |
| `Live` | `Long` | `70.55` | 52,310,000.00 USD | 0.00 USD | 34,660.00 USD | `-27.66%` | `491.35` |
| `Live` | `Long` | `70.65` | 52,270,000.00 USD | 0.00 USD | 45,020.00 USD | `-27.56%` | `637.23` |
| `Live` | `Long` | `70.75` | 52,230,000.00 USD | 0.00 USD | 13,570.00 USD | `-27.46%` | `191.80` |
| `Live` | `Long` | `70.85` | 52,210,000.00 USD | 0.00 USD | 20,720.00 USD | `-27.36%` | `292.43` |
| `Live` | `Long` | `70.95` | 52,190,000.00 USD | 0.00 USD | 5,520.00 USD | `-27.25%` | `77.77` |
| `Live` | `Long` | `71.05` | 52,190,000.00 USD | 0.00 USD | 37,460.00 USD | `-27.15%` | `527.27` |
| `Live` | `Long` | `71.15` | 52,150,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-27.05%` | `19,716.69` |
| `Live` | `Long` | `71.25` | 50,750,000.00 USD | 0.00 USD | 11,640.00 USD | `-26.95%` | `163.34` |
| `Live` | `Long` | `71.35` | 50,730,000.00 USD | 0.00 USD | 21,320.00 USD | `-26.84%` | `298.83` |
| `Live` | `Long` | `71.45` | 50,710,000.00 USD | 0.00 USD | 16,710.00 USD | `-26.74%` | `233.93` |
| `Live` | `Long` | `71.55` | 50,700,000.00 USD | 0.00 USD | 44,020.00 USD | `-26.64%` | `615.22` |
| `Live` | `Long` | `71.65` | 50,650,000.00 USD | 0.00 USD | 460.71 USD | `-26.54%` | `6.43` |
| `Live` | `Long` | `71.75` | 50,650,000.00 USD | 0.00 USD | 532,080.00 USD | `-26.43%` | `7,415.81` |
| `Live` | `Long` | `71.85` | 50,120,000.00 USD | 0.00 USD | 2,130.00 USD | `-26.33%` | `29.71` |
| `Live` | `Long` | `71.95` | 50,120,000.00 USD | 0.00 USD | 40,950.00 USD | `-26.23%` | `569.21` |
| `Live` | `Long` | `72.05` | 50,080,000.00 USD | 0.00 USD | 13,460.00 USD | `-26.13%` | `186.87` |
| `Live` | `Long` | `72.15` | 50,060,000.00 USD | 0.00 USD | 145,290.00 USD | `-26.02%` | `2,013.70` |
| `Live` | `Long` | `72.25` | 49,920,000.00 USD | 0.00 USD | 41,150.00 USD | `-25.92%` | `569.59` |
| `Live` | `Long` | `72.35` | 49,880,000.00 USD | 0.00 USD | 6,370.00 USD | `-25.82%` | `87.99` |
| `Live` | `Long` | `72.45` | 49,870,000.00 USD | 0.00 USD | 8,260.00 USD | `-25.72%` | `114.04` |
| `Live` | `Long` | `72.55` | 49,860,000.00 USD | 0.00 USD | 12,330.00 USD | `-25.61%` | `169.91` |
| `Live` | `Long` | `72.65` | 49,850,000.00 USD | 0.00 USD | 92,150.00 USD | `-25.51%` | `1,268.39` |
| `Live` | `Long` | `72.75` | 49,760,000.00 USD | 0.00 USD | 19,820.00 USD | `-25.41%` | `272.49` |
| `Live` | `Long` | `72.85` | 49,740,000.00 USD | 0.00 USD | 1,230.00 USD | `-25.31%` | `16.88` |
| `Live` | `Long` | `72.95` | 49,740,000.00 USD | 0.00 USD | 8,740.00 USD | `-25.20%` | `119.81` |
| `Live` | `Long` | `73.05` | 49,730,000.00 USD | 0.00 USD | 16,410.00 USD | `-25.10%` | `224.67` |
| `Live` | `Long` | `73.15` | 49,710,000.00 USD | 0.00 USD | 62,460.00 USD | `-25.00%` | `853.85` |
| `Live` | `Long` | `73.25` | 49,650,000.00 USD | 0.00 USD | 26,770.00 USD | `-24.90%` | `365.48` |
| `Live` | `Long` | `73.35` | 49,620,000.00 USD | 0.00 USD | 3,410.00 USD | `-24.79%` | `46.52` |
| `Live` | `Long` | `73.45` | 49,620,000.00 USD | 0.00 USD | 536.92 USD | `-24.69%` | `7.31` |
| `Live` | `Long` | `73.55` | 49,620,000.00 USD | 0.00 USD | 18,920.00 USD | `-24.59%` | `257.27` |
| `Live` | `Long` | `73.65` | 49,600,000.00 USD | 0.00 USD | 164,120.00 USD | `-24.49%` | `2,228.37` |
| `Live` | `Long` | `73.75` | 49,440,000.00 USD | 0.00 USD | 65,320.00 USD | `-24.38%` | `885.75` |
| `Live` | `Long` | `73.85` | 49,370,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-24.28%` | `20,591.13` |
| `Live` | `Long` | `73.95` | 47,850,000.00 USD | 0.00 USD | 40,150.00 USD | `-24.18%` | `542.87` |
| `Live` | `Long` | `74.05` | 47,810,000.00 USD | 0.00 USD | 26,320.00 USD | `-24.08%` | `355.39` |
| `Live` | `Long` | `74.15` | 47,780,000.00 USD | 0.00 USD | 22,030.00 USD | `-23.97%` | `297.13` |
| `Live` | `Long` | `74.25` | 47,760,000.00 USD | 0.00 USD | 33,730.00 USD | `-23.87%` | `454.34` |
| `Live` | `Long` | `74.35` | 47,730,000.00 USD | 0.00 USD | 38,740.00 USD | `-23.77%` | `520.99` |
| `Live` | `Long` | `74.45` | 47,690,000.00 USD | 0.00 USD | 7,080.00 USD | `-23.67%` | `95.07` |
| `Live` | `Long` | `74.55` | 47,680,000.00 USD | 0.00 USD | 1,980.00 USD | `-23.56%` | `26.58` |
| `Live` | `Long` | `74.75` | 47,680,000.00 USD | 0.00 USD | 149,570.00 USD | `-23.36%` | `2,001.00` |
| `Live` | `Long` | `74.85` | 47,530,000.00 USD | 0.00 USD | 15,780.00 USD | `-23.26%` | `210.79` |
| `Live` | `Long` | `74.95` | 47,510,000.00 USD | 0.00 USD | 19,620.00 USD | `-23.15%` | `261.75` |
| `Live` | `Long` | `75.05` | 47,490,000.00 USD | 0.00 USD | 43,400.00 USD | `-23.05%` | `578.29` |
| `Live` | `Long` | `75.15` | 47,450,000.00 USD | 0.00 USD | 10,980.00 USD | `-22.95%` | `146.05` |
| `Live` | `Long` | `75.25` | 47,440,000.00 USD | 0.00 USD | 16,870.00 USD | `-22.85%` | `224.21` |
| `Live` | `Long` | `75.35` | 47,420,000.00 USD | 0.00 USD | 18,800.00 USD | `-22.74%` | `249.56` |
| `Live` | `Long` | `75.45` | 47,400,000.00 USD | 0.00 USD | 3,370.00 USD | `-22.64%` | `44.65` |
| `Live` | `Long` | `75.55` | 47,400,000.00 USD | 0.00 USD | 46,880.00 USD | `-22.54%` | `620.56` |
| `Live` | `Long` | `75.65` | 47,350,000.00 USD | 0.00 USD | 129,160.00 USD | `-22.44%` | `1,707.40` |
| `Live` | `Long` | `75.75` | 47,230,000.00 USD | 0.00 USD | 48,470.00 USD | `-22.33%` | `639.91` |
| `Live` | `Long` | `75.85` | 47,180,000.00 USD | 0.00 USD | 15,170.00 USD | `-22.23%` | `200.02` |
| `Live` | `Long` | `75.95` | 47,160,000.00 USD | 0.00 USD | 21,910.00 USD | `-22.13%` | `288.51` |
| `Live` | `Long` | `76.05` | 47,140,000.00 USD | 0.00 USD | 1,670,000.00 USD | `-22.03%` | `22,023.09` |
| `Live` | `Long` | `76.15` | 45,460,000.00 USD | 0.00 USD | 4,790.00 USD | `-21.92%` | `62.86` |
| `Live` | `Long` | `76.25` | 45,460,000.00 USD | 0.00 USD | 9,000.00 USD | `-21.82%` | `118.08` |
| `Live` | `Long` | `76.35` | 45,450,000.00 USD | 0.00 USD | 35,070.00 USD | `-21.72%` | `459.36` |
| `Live` | `Long` | `76.45` | 45,420,000.00 USD | 0.00 USD | 3,080.00 USD | `-21.62%` | `40.29` |
| `Live` | `Long` | `76.55` | 45,410,000.00 USD | 0.00 USD | 38,050.00 USD | `-21.51%` | `497.01` |
| `Live` | `Long` | `76.65` | 45,370,000.00 USD | 0.00 USD | 15,730.00 USD | `-21.41%` | `205.18` |
| `Live` | `Long` | `76.75` | 45,360,000.00 USD | 0.00 USD | 12,890.00 USD | `-21.31%` | `168.01` |
| `Live` | `Long` | `76.85` | 45,350,000.00 USD | 0.00 USD | 62,560.00 USD | `-21.21%` | `814.03` |
| `Live` | `Long` | `76.95` | 45,280,000.00 USD | 0.00 USD | 35,920.00 USD | `-21.10%` | `466.80` |
| `Live` | `Long` | `77.05` | 45,250,000.00 USD | 0.00 USD | 27,740.00 USD | `-21.00%` | `360.04` |
| `Live` | `Long` | `77.15` | 45,220,000.00 USD | 0.00 USD | 78,320.00 USD | `-20.90%` | `1,015.21` |
| `Live` | `Long` | `77.25` | 45,140,000.00 USD | 0.00 USD | 34,220.00 USD | `-20.80%` | `442.96` |
| `Live` | `Long` | `77.35` | 45,110,000.00 USD | 0.00 USD | 4,210.00 USD | `-20.69%` | `54.47` |
| `Live` | `Long` | `77.45` | 45,100,000.00 USD | 0.00 USD | 14,830.00 USD | `-20.59%` | `191.53` |
| `Live` | `Long` | `77.55` | 45,090,000.00 USD | 0.00 USD | 7,950.00 USD | `-20.49%` | `102.50` |
| `Live` | `Long` | `77.65` | 45,080,000.00 USD | 0.00 USD | 201,890.00 USD | `-20.39%` | `2,600.00` |
| `Live` | `Long` | `77.75` | 44,880,000.00 USD | 0.00 USD | 357,790.00 USD | `-20.28%` | `4,601.80` |
| `Live` | `Long` | `77.85` | 44,520,000.00 USD | 0.00 USD | 22,500.00 USD | `-20.18%` | `289.08` |
| `Live` | `Long` | `77.95` | 44,500,000.00 USD | 0.00 USD | 12,740.00 USD | `-20.08%` | `163.48` |
| `Live` | `Long` | `78.05` | 44,490,000.00 USD | 0.00 USD | 20,450.00 USD | `-19.97%` | `262.01` |
| `Live` | `Long` | `78.15` | 44,460,000.00 USD | 0.00 USD | 71,470.00 USD | `-19.87%` | `914.46` |
| `Live` | `Long` | `78.25` | 44,390,000.00 USD | 0.00 USD | 24,450.00 USD | `-19.77%` | `312.42` |
| `Live` | `Long` | `78.35` | 44,370,000.00 USD | 0.00 USD | 66,240.00 USD | `-19.67%` | `845.49` |
| `Live` | `Long` | `78.45` | 44,300,000.00 USD | 0.00 USD | 34,280.00 USD | `-19.56%` | `436.98` |
| `Live` | `Long` | `78.55` | 44,270,000.00 USD | 0.00 USD | 524,840.00 USD | `-19.46%` | `6,681.63` |
| `Live` | `Long` | `78.65` | 43,740,000.00 USD | 0.00 USD | 8,740.00 USD | `-19.36%` | `111.11` |
| `Live` | `Long` | `78.75` | 43,730,000.00 USD | 0.00 USD | 64,950.00 USD | `-19.26%` | `824.74` |
| `Live` | `Long` | `78.85` | 43,670,000.00 USD | 0.00 USD | 24,750.00 USD | `-19.15%` | `313.87` |
| `Live` | `Long` | `78.95` | 43,650,000.00 USD | 0.00 USD | 9,060.00 USD | `-19.05%` | `114.75` |
| `Live` | `Long` | `79.05` | 43,640,000.00 USD | 0.00 USD | 1,500.00 USD | `-18.95%` | `18.94` |
| `Live` | `Long` | `79.15` | 43,630,000.00 USD | 0.00 USD | 620,870.00 USD | `-18.85%` | `7,844.23` |
| `Live` | `Long` | `79.25` | 43,010,000.00 USD | 0.00 USD | 107,100.00 USD | `-18.74%` | `1,351.38` |
| `Live` | `Long` | `79.35` | 42,910,000.00 USD | 0.00 USD | 18,890.00 USD | `-18.64%` | `238.12` |
| `Live` | `Long` | `79.45` | 42,890,000.00 USD | 0.00 USD | 4,860.00 USD | `-18.54%` | `61.21` |
| `Live` | `Long` | `79.55` | 42,880,000.00 USD | 0.00 USD | 10,480.00 USD | `-18.44%` | `131.73` |
| `Live` | `Long` | `79.65` | 42,870,000.00 USD | 0.00 USD | 30,610.00 USD | `-18.33%` | `384.27` |
| `Live` | `Long` | `79.75` | 42,840,000.00 USD | 0.00 USD | 693.03 USD | `-18.23%` | `8.69` |
| `Live` | `Long` | `79.85` | 42,840,000.00 USD | 0.00 USD | 51,290.00 USD | `-18.13%` | `642.35` |
| `Live` | `Long` | `79.95` | 42,790,000.00 USD | 0.00 USD | 4,940.00 USD | `-18.03%` | `61.83` |
| `Live` | `Long` | `80.05` | 42,780,000.00 USD | 0.00 USD | 27,450.00 USD | `-17.92%` | `342.92` |
| `Live` | `Long` | `80.15` | 42,760,000.00 USD | 0.00 USD | 38,640.00 USD | `-17.82%` | `482.11` |
| `Live` | `Long` | `80.25` | 42,720,000.00 USD | 0.00 USD | 45,510.00 USD | `-17.72%` | `567.16` |
| `Live` | `Long` | `80.35` | 42,670,000.00 USD | 0.00 USD | 560,470.00 USD | `-17.62%` | `6,975.31` |
| `Live` | `Long` | `80.45` | 42,110,000.00 USD | 0.00 USD | 11,820.00 USD | `-17.51%` | `146.90` |
| `Live` | `Long` | `80.55` | 42,100,000.00 USD | 0.00 USD | 6,450.00 USD | `-17.41%` | `80.05` |
| `Live` | `Long` | `80.65` | 42,090,000.00 USD | 0.00 USD | 24,310.00 USD | `-17.31%` | `301.46` |
| `Live` | `Long` | `80.75` | 42,070,000.00 USD | 0.00 USD | 14,200.00 USD | `-17.21%` | `175.79` |
| `Live` | `Long` | `80.85` | 42,060,000.00 USD | 0.00 USD | 35,690.00 USD | `-17.10%` | `441.44` |
| `Live` | `Long` | `80.95` | 42,020,000.00 USD | 0.00 USD | 10,620.00 USD | `-17.00%` | `131.18` |
| `Live` | `Long` | `81.05` | 42,010,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-16.90%` | `28,469.30` |
| `Live` | `Long` | `81.15` | 39,700,000.00 USD | 0.00 USD | 766,000.00 USD | `-16.80%` | `9,439.28` |
| `Live` | `Long` | `81.25` | 38,940,000.00 USD | 0.00 USD | 18,710.00 USD | `-16.69%` | `230.22` |
| `Live` | `Long` | `81.35` | 38,920,000.00 USD | 0.00 USD | 82,790.00 USD | `-16.59%` | `1,017.76` |
| `Live` | `Long` | `81.45` | 38,830,000.00 USD | 0.00 USD | 59,690.00 USD | `-16.49%` | `732.84` |
| `Live` | `Long` | `81.55` | 38,780,000.00 USD | 0.00 USD | 24,020.00 USD | `-16.39%` | `294.49` |
| `Live` | `Long` | `81.65` | 38,750,000.00 USD | 0.00 USD | 16,470.00 USD | `-16.28%` | `201.74` |
| `Live` | `Long` | `81.75` | 38,730,000.00 USD | 0.00 USD | 81,300.00 USD | `-16.18%` | `994.48` |
| `Live` | `Long` | `81.85` | 38,650,000.00 USD | 0.00 USD | 37,370.00 USD | `-16.08%` | `456.57` |
| `Live` | `Long` | `81.95` | 38,620,000.00 USD | 0.00 USD | 16,500.00 USD | `-15.98%` | `201.33` |
| `Live` | `Long` | `82.05` | 38,600,000.00 USD | 0.00 USD | 211,400.00 USD | `-15.87%` | `2,576.44` |
| `Live` | `Long` | `82.15` | 38,390,000.00 USD | 0.00 USD | 800,060.00 USD | `-15.77%` | `9,739.04` |
| `Live` | `Long` | `82.25` | 37,590,000.00 USD | 0.00 USD | 163,410.00 USD | `-15.67%` | `1,986.78` |
| `Live` | `Long` | `82.35` | 37,420,000.00 USD | 0.00 USD | 31,900.00 USD | `-15.57%` | `387.43` |
| `Live` | `Long` | `82.45` | 37,390,000.00 USD | 0.00 USD | 212,870.00 USD | `-15.46%` | `2,581.78` |
| `Live` | `Long` | `82.55` | 37,180,000.00 USD | 0.00 USD | 41,380.00 USD | `-15.36%` | `501.24` |
| `Live` | `Long` | `82.65` | 37,140,000.00 USD | 0.00 USD | 104,530.00 USD | `-15.26%` | `1,264.73` |
| `Live` | `Long` | `82.75` | 37,030,000.00 USD | 0.00 USD | 33,040.00 USD | `-15.16%` | `399.25` |
| `Live` | `Long` | `82.85` | 37,000,000.00 USD | 0.00 USD | 19,850.00 USD | `-15.05%` | `239.60` |
| `Live` | `Long` | `82.95` | 36,980,000.00 USD | 0.00 USD | 25,410.00 USD | `-14.95%` | `306.30` |
| `Live` | `Long` | `83.05` | 36,960,000.00 USD | 0.00 USD | 79,640.00 USD | `-14.85%` | `958.93` |
| `Live` | `Long` | `83.15` | 36,880,000.00 USD | 0.00 USD | 24,720.00 USD | `-14.75%` | `297.26` |
| `Live` | `Long` | `83.25` | 36,850,000.00 USD | 0.00 USD | 15,340.00 USD | `-14.64%` | `184.29` |
| `Live` | `Long` | `83.35` | 36,840,000.00 USD | 0.00 USD | 55,090.00 USD | `-14.54%` | `660.91` |
| `Live` | `Long` | `83.45` | 36,780,000.00 USD | 0.00 USD | 53,590.00 USD | `-14.44%` | `642.15` |
| `Live` | `Long` | `83.55` | 36,730,000.00 USD | 0.00 USD | 10,910.00 USD | `-14.34%` | `130.55` |
| `Live` | `Long` | `83.65` | 36,720,000.00 USD | 0.00 USD | 68,150.00 USD | `-14.23%` | `814.70` |
| `Live` | `Long` | `83.75` | 36,650,000.00 USD | 0.00 USD | 1,700,000.00 USD | `-14.13%` | `20,305.88` |
| `Live` | `Long` | `83.85` | 34,950,000.00 USD | 0.00 USD | 219,130.00 USD | `-14.03%` | `2,613.33` |
| `Live` | `Long` | `83.95` | 34,730,000.00 USD | 0.00 USD | 62,100.00 USD | `-13.93%` | `739.73` |
| `Live` | `Long` | `84.05` | 34,670,000.00 USD | 0.00 USD | 174,990.00 USD | `-13.82%` | `2,082.03` |
| `Live` | `Long` | `84.15` | 34,490,000.00 USD | 0.00 USD | 79,210.00 USD | `-13.72%` | `941.24` |
| `Live` | `Long` | `84.25` | 34,410,000.00 USD | 0.00 USD | 45,260.00 USD | `-13.62%` | `537.21` |
| `Live` | `Long` | `84.35` | 34,370,000.00 USD | 0.00 USD | 42,940.00 USD | `-13.52%` | `509.02` |
| `Live` | `Long` | `84.45` | 34,320,000.00 USD | 0.00 USD | 115,750.00 USD | `-13.41%` | `1,370.62` |
| `Live` | `Long` | `84.55` | 34,210,000.00 USD | 0.00 USD | 481,260.00 USD | `-13.31%` | `5,692.06` |
| `Live` | `Long` | `84.65` | 33,730,000.00 USD | 0.00 USD | 64,650.00 USD | `-13.21%` | `763.76` |
| `Live` | `Long` | `84.75` | 33,660,000.00 USD | 0.00 USD | 48,990.00 USD | `-13.11%` | `578.01` |
| `Live` | `Long` | `84.85` | 33,610,000.00 USD | 0.00 USD | 6,300.00 USD | `-13.00%` | `74.29` |
| `Live` | `Long` | `84.95` | 33,610,000.00 USD | 0.00 USD | 3,780.00 USD | `-12.90%` | `44.49` |
| `Live` | `Long` | `85.05` | 33,600,000.00 USD | 0.00 USD | 20,170.00 USD | `-12.80%` | `237.17` |
| `Live` | `Long` | `85.15` | 33,580,000.00 USD | 0.00 USD | 63,110.00 USD | `-12.70%` | `741.15` |
| `Live` | `Long` | `85.25` | 33,520,000.00 USD | 0.00 USD | 567,940.00 USD | `-12.59%` | `6,662.08` |
| `Live` | `Long` | `85.35` | 32,950,000.00 USD | 0.00 USD | 41,540.00 USD | `-12.49%` | `486.67` |
| `Live` | `Long` | `85.45` | 32,910,000.00 USD | 0.00 USD | 27,730.00 USD | `-12.39%` | `324.52` |
| `Live` | `Long` | `85.55` | 32,880,000.00 USD | 0.00 USD | 14,630.00 USD | `-12.29%` | `171.02` |
| `Live` | `Long` | `85.65` | 32,870,000.00 USD | 0.00 USD | 16,210.00 USD | `-12.18%` | `189.27` |
| `Live` | `Long` | `85.75` | 32,850,000.00 USD | 0.00 USD | 5,920.00 USD | `-12.08%` | `69.02` |
| `Live` | `Long` | `85.85` | 32,850,000.00 USD | 0.00 USD | 40,200.00 USD | `-11.98%` | `468.21` |
| `Live` | `Long` | `85.95` | 32,810,000.00 USD | 0.00 USD | 60,980.00 USD | `-11.88%` | `709.45` |
| `Live` | `Long` | `86.05` | 32,740,000.00 USD | 0.00 USD | 57,960.00 USD | `-11.77%` | `673.59` |
| `Live` | `Long` | `86.15` | 32,690,000.00 USD | 0.00 USD | 116,560.00 USD | `-11.67%` | `1,352.95` |
| `Live` | `Long` | `86.25` | 32,570,000.00 USD | 0.00 USD | 12,230.00 USD | `-11.57%` | `141.81` |
| `Live` | `Long` | `86.35` | 32,560,000.00 USD | 0.00 USD | 21,350.00 USD | `-11.46%` | `247.28` |
| `Live` | `Long` | `86.45` | 32,540,000.00 USD | 0.00 USD | 34,960.00 USD | `-11.36%` | `404.38` |
| `Live` | `Long` | `86.55` | 32,500,000.00 USD | 0.00 USD | 17,960.00 USD | `-11.26%` | `207.50` |
| `Live` | `Long` | `86.65` | 32,480,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-11.16%` | `16,078.14` |
| `Live` | `Long` | `86.75` | 31,090,000.00 USD | 0.00 USD | 26,450.00 USD | `-11.05%` | `304.87` |
| `Live` | `Long` | `86.85` | 31,060,000.00 USD | 0.00 USD | 63,540.00 USD | `-10.95%` | `731.62` |
| `Live` | `Long` | `86.95` | 31,000,000.00 USD | 0.00 USD | 151,110.00 USD | `-10.85%` | `1,737.91` |
| `Live` | `Long` | `87.05` | 30,850,000.00 USD | 0.00 USD | 310,570.00 USD | `-10.75%` | `3,567.69` |
| `Live` | `Long` | `87.15` | 30,540,000.00 USD | 0.00 USD | 295,220.00 USD | `-10.64%` | `3,387.50` |
| `Live` | `Long` | `87.25` | 30,240,000.00 USD | 0.00 USD | 174,090.00 USD | `-10.54%` | `1,995.35` |
| `Live` | `Long` | `87.35` | 30,070,000.00 USD | 0.00 USD | 35,470.00 USD | `-10.44%` | `406.10` |
| `Live` | `Long` | `87.45` | 30,030,000.00 USD | 0.00 USD | 541,520.00 USD | `-10.34%` | `6,192.34` |
| `Live` | `Long` | `87.55` | 29,490,000.00 USD | 0.00 USD | 173,280.00 USD | `-10.23%` | `1,979.16` |
| `Live` | `Long` | `87.65` | 29,320,000.00 USD | 0.00 USD | 561,140.00 USD | `-10.13%` | `6,402.11` |
| `Live` | `Long` | `87.75` | 28,760,000.00 USD | 0.00 USD | 26,530.00 USD | `-10.03%` | `302.39` |
| `Live` | `Long` | `87.85` | 28,730,000.00 USD | 0.00 USD | 21,470.00 USD | `-9.93%` | `244.34` |
| `Live` | `Long` | `87.95` | 28,710,000.00 USD | 0.00 USD | 5,470.00 USD | `-9.82%` | `62.22` |
| `Live` | `Long` | `88.05` | 28,700,000.00 USD | 0.00 USD | 45,710.00 USD | `-9.72%` | `519.13` |
| `Live` | `Long` | `88.15` | 28,660,000.00 USD | 0.00 USD | 6,610.00 USD | `-9.62%` | `75.01` |
| `Live` | `Long` | `88.25` | 28,650,000.00 USD | 0.00 USD | 198,990.00 USD | `-9.52%` | `2,254.84` |
| `Live` | `Long` | `88.35` | 28,450,000.00 USD | 0.00 USD | 44,640.00 USD | `-9.41%` | `505.25` |
| `Live` | `Long` | `88.45` | 28,410,000.00 USD | 0.00 USD | 193,140.00 USD | `-9.31%` | `2,183.65` |
| `Live` | `Long` | `88.55` | 28,220,000.00 USD | 0.00 USD | 253,250.00 USD | `-9.21%` | `2,859.97` |
| `Live` | `Long` | `88.65` | 27,960,000.00 USD | 0.00 USD | 149,640.00 USD | `-9.11%` | `1,687.99` |
| `Live` | `Long` | `88.75` | 27,810,000.00 USD | 0.00 USD | 147,100.00 USD | `-9.00%` | `1,657.44` |
| `Live` | `Long` | `88.85` | 27,670,000.00 USD | 0.00 USD | 57,610.00 USD | `-8.90%` | `648.43` |
| `Live` | `Long` | `88.95` | 27,610,000.00 USD | 0.00 USD | 202,370.00 USD | `-8.80%` | `2,275.07` |
| `Live` | `Long` | `89.05` | 27,410,000.00 USD | 0.00 USD | 300,350.00 USD | `-8.70%` | `3,372.82` |
| `Live` | `Long` | `89.15` | 27,110,000.00 USD | 0.00 USD | 265,920.00 USD | `-8.59%` | `2,982.79` |
| `Live` | `Long` | `89.25` | 26,840,000.00 USD | 0.00 USD | 88,470.00 USD | `-8.49%` | `991.21` |
| `Live` | `Long` | `89.35` | 26,750,000.00 USD | 0.00 USD | 37,830.00 USD | `-8.39%` | `423.41` |
| `Live` | `Long` | `89.45` | 26,710,000.00 USD | 0.00 USD | 359,670.00 USD | `-8.29%` | `4,020.90` |
| `Live` | `Long` | `89.55` | 26,350,000.00 USD | 0.00 USD | 42,370.00 USD | `-8.18%` | `473.11` |
| `Live` | `Long` | `89.65` | 26,310,000.00 USD | 0.00 USD | 16,270.00 USD | `-8.08%` | `181.53` |
| `Live` | `Long` | `89.75` | 26,290,000.00 USD | 0.00 USD | 61,120.00 USD | `-7.98%` | `681.03` |
| `Live` | `Long` | `89.85` | 26,230,000.00 USD | 0.00 USD | 75,680.00 USD | `-7.88%` | `842.27` |
| `Live` | `Long` | `89.95` | 26,160,000.00 USD | 0.00 USD | 125,830.00 USD | `-7.77%` | `1,398.91` |
| `Live` | `Long` | `90.05` | 26,030,000.00 USD | 0.00 USD | 50,020.00 USD | `-7.67%` | `555.52` |
| `Live` | `Long` | `90.15` | 25,980,000.00 USD | 0.00 USD | 36,330.00 USD | `-7.57%` | `403.00` |
| `Live` | `Long` | `90.25` | 25,950,000.00 USD | 0.00 USD | 44,240.00 USD | `-7.47%` | `490.14` |
| `Live` | `Long` | `90.35` | 25,900,000.00 USD | 0.00 USD | 44,640.00 USD | `-7.36%` | `494.07` |
| `Live` | `Long` | `90.45` | 25,860,000.00 USD | 0.00 USD | 186,800.00 USD | `-7.26%` | `2,065.21` |
| `Live` | `Long` | `90.55` | 25,670,000.00 USD | 0.00 USD | 13,950.00 USD | `-7.16%` | `154.01` |
| `Live` | `Long` | `90.65` | 25,660,000.00 USD | 0.00 USD | 81,000.00 USD | `-7.06%` | `893.53` |
| `Live` | `Long` | `90.75` | 25,580,000.00 USD | 0.00 USD | 61,230.00 USD | `-6.95%` | `674.66` |
| `Live` | `Long` | `90.85` | 25,510,000.00 USD | 0.00 USD | 94,820.00 USD | `-6.85%` | `1,043.71` |
| `Live` | `Long` | `90.95` | 25,420,000.00 USD | 0.00 USD | 55,160.00 USD | `-6.75%` | `606.47` |
| `Live` | `Long` | `91.05` | 25,360,000.00 USD | 0.00 USD | 811,710.00 USD | `-6.65%` | `8,914.99` |
| `Live` | `Long` | `91.15` | 24,550,000.00 USD | 0.00 USD | 290,130.00 USD | `-6.54%` | `3,183.01` |
| `Live` | `Long` | `91.25` | 24,260,000.00 USD | 0.00 USD | 19,390.00 USD | `-6.44%` | `212.45` |
| `Live` | `Long` | `91.35` | 24,240,000.00 USD | 0.00 USD | 52,720.00 USD | `-6.34%` | `577.15` |
| `Live` | `Long` | `91.45` | 24,190,000.00 USD | 0.00 USD | 34,520.00 USD | `-6.24%` | `377.50` |
| `Live` | `Long` | `91.55` | 24,160,000.00 USD | 0.00 USD | 3,660,000.00 USD | `-6.13%` | `39,954.50` |
| `Live` | `Long` | `91.65` | 20,500,000.00 USD | 0.00 USD | 81,870.00 USD | `-6.03%` | `893.32` |
| `Live` | `Long` | `91.75` | 20,420,000.00 USD | 0.00 USD | 369,210.00 USD | `-5.93%` | `4,024.09` |
| `Live` | `Long` | `91.85` | 20,050,000.00 USD | 0.00 USD | 37,650.00 USD | `-5.83%` | `409.95` |
| `Live` | `Long` | `91.95` | 20,010,000.00 USD | 0.00 USD | 128,670.00 USD | `-5.72%` | `1,399.36` |
| `Live` | `Long` | `92.05` | 19,880,000.00 USD | 0.00 USD | 29,340.00 USD | `-5.62%` | `318.71` |
| `Live` | `Long` | `92.15` | 19,850,000.00 USD | 0.00 USD | 269,080.00 USD | `-5.52%` | `2,919.99` |
| `Live` | `Long` | `92.25` | 19,580,000.00 USD | 0.00 USD | 66,830.00 USD | `-5.42%` | `724.46` |
| `Live` | `Long` | `92.35` | 19,510,000.00 USD | 0.00 USD | 191,580.00 USD | `-5.31%` | `2,074.52` |
| `Live` | `Long` | `92.45` | 19,320,000.00 USD | 0.00 USD | 185,890.00 USD | `-5.21%` | `2,010.76` |
| `Live` | `Long` | `92.55` | 19,140,000.00 USD | 0.00 USD | 238,380.00 USD | `-5.11%` | `2,575.67` |
| `Live` | `Long` | `92.65` | 18,900,000.00 USD | 0.00 USD | 451,720.00 USD | `-5.01%` | `4,875.60` |
| `Live` | `Long` | `92.75` | 18,450,000.00 USD | 0.00 USD | 430,540.00 USD | `-4.90%` | `4,641.93` |
| `Live` | `Long` | `92.85` | 18,020,000.00 USD | 0.00 USD | 518,600.00 USD | `-4.80%` | `5,585.33` |
| `Live` | `Long` | `92.95` | 17,500,000.00 USD | 0.00 USD | 84,580.00 USD | `-4.70%` | `909.99` |
| `Live` | `Long` | `93.05` | 17,410,000.00 USD | 0.00 USD | 197,380.00 USD | `-4.60%` | `2,121.27` |
| `Live` | `Long` | `93.15` | 17,220,000.00 USD | 0.00 USD | 78,980.00 USD | `-4.49%` | `847.89` |
| `Live` | `Long` | `93.25` | 17,140,000.00 USD | 0.00 USD | 475,120.00 USD | `-4.39%` | `5,095.09` |
| `Live` | `Long` | `93.35` | 16,660,000.00 USD | 0.00 USD | 201,450.00 USD | `-4.29%` | `2,157.96` |
| `Live` | `Long` | `93.45` | 16,460,000.00 USD | 0.00 USD | 585,030.00 USD | `-4.19%` | `6,260.31` |
| `Live` | `Long` | `93.55` | 15,880,000.00 USD | 0.00 USD | 341,130.00 USD | `-4.08%` | `3,646.51` |
| `Live` | `Long` | `93.65` | 15,530,000.00 USD | 0.00 USD | 373,280.00 USD | `-3.98%` | `3,985.87` |
| `Live` | `Long` | `93.75` | 15,160,000.00 USD | 0.00 USD | 129,890.00 USD | `-3.88%` | `1,385.50` |
| `Live` | `Long` | `93.85` | 15,030,000.00 USD | 0.00 USD | 576,790.00 USD | `-3.78%` | `6,145.91` |
| `Live` | `Long` | `93.95` | 14,450,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-3.67%` | `24,129.85` |
| `Live` | `Long` | `94.05` | 12,190,000.00 USD | 0.00 USD | 264,200.00 USD | `-3.57%` | `2,809.12` |
| `Live` | `Long` | `94.15` | 11,920,000.00 USD | 0.00 USD | 183,590.00 USD | `-3.47%` | `1,949.97` |
| `Live` | `Long` | `94.25` | 11,740,000.00 USD | 0.00 USD | 37,910.00 USD | `-3.37%` | `402.22` |
| `Live` | `Long` | `94.35` | 11,700,000.00 USD | 0.00 USD | 208,080.00 USD | `-3.26%` | `2,205.36` |
| `Live` | `Long` | `94.45` | 11,490,000.00 USD | 0.00 USD | 958,060.00 USD | `-3.16%` | `10,143.53` |
| `Live` | `Long` | `94.55` | 10,540,000.00 USD | 0.00 USD | 559,630.00 USD | `-3.06%` | `5,918.87` |
| `Live` | `Long` | `94.65` | 9,980,000.00 USD | 0.00 USD | 8,510,000.00 USD | `-2.95%` | `89,870.90` |
| `Live` | `Short` | `94.75` | 26,420.00 USD | 26,420.00 USD | 0.00 USD | `-2.85%` | `278.84` |
| `Live` | `Long` | `94.85` | 1,470,000.00 USD | 0.00 USD | 803,260.00 USD | `-2.75%` | `8,468.79` |
| `Live` | `Long` | `94.95` | 666,650.00 USD | 0.00 USD | 237,840.00 USD | `-2.65%` | `2,504.90` |
| `Live` | `Long` | `95.05` | 428,810.00 USD | 0.00 USD | 222,650.00 USD | `-2.54%` | `2,342.43` |
| `Live` | `Long` | `95.15` | 206,160.00 USD | 0.00 USD | 20,190.00 USD | `-2.44%` | `212.19` |
| `Live` | `Long` | `95.25` | 185,970.00 USD | 0.00 USD | 142,840.00 USD | `-2.34%` | `1,499.59` |
| `Live` | `Long` | `95.35` | 43,140.00 USD | 0.00 USD | 9,410.00 USD | `-2.24%` | `98.74` |
| `Live` | `Long` | `95.45` | 33,720.00 USD | 0.00 USD | 17,100.00 USD | `-2.13%` | `179.18` |
| `Live` | `Long` | `95.55` | 16,620.00 USD | 0.00 USD | 11,290.00 USD | `-2.03%` | `118.13` |
| `Live` | `Long` | `95.85` | 5,330.00 USD | 0.00 USD | 5,330.00 USD | `-1.72%` | `55.63` |
| `Live` | `Short` | `96.35` | 86,570.00 USD | 60,150.00 USD | 0.00 USD | `-1.21%` | `624.28` |
| `Live` | `Short` | `97.65` | 91,960.00 USD | 5,390.00 USD | 0.00 USD | `+0.12%` | `55.23` |
| `Live` | `Short` | `98.55` | 95,150.00 USD | 3,190.00 USD | 0.00 USD | `+1.04%` | `32.39` |
| `Live` | `Short` | `98.65` | 95,780.00 USD | 624.45 USD | 0.00 USD | `+1.15%` | `6.33` |
| `Live` | `Short` | `98.85` | 96,000.00 USD | 217.47 USD | 0.00 USD | `+1.35%` | `2.20` |
| `Live` | `Short` | `99.05` | 98,350.00 USD | 2,350.00 USD | 0.00 USD | `+1.56%` | `23.76` |
| `Live` | `Short` | `99.15` | 284,200.00 USD | 185,850.00 USD | 0.00 USD | `+1.66%` | `1,874.42` |
| `Live` | `Short` | `99.25` | 360,800.00 USD | 76,600.00 USD | 0.00 USD | `+1.76%` | `771.77` |
| `Live` | `Short` | `99.35` | 422,720.00 USD | 61,920.00 USD | 0.00 USD | `+1.86%` | `623.24` |
| `Live` | `Short` | `99.45` | 458,390.00 USD | 35,680.00 USD | 0.00 USD | `+1.97%` | `358.76` |
| `Live` | `Short` | `99.55` | 472,530.00 USD | 14,140.00 USD | 0.00 USD | `+2.07%` | `142.01` |
| `Live` | `Short` | `99.65` | 478,180.00 USD | 5,650.00 USD | 0.00 USD | `+2.17%` | `56.71` |
| `Live` | `Short` | `99.75` | 489,860.00 USD | 11,680.00 USD | 0.00 USD | `+2.27%` | `117.11` |
| `Live` | `Short` | `99.85` | 580,360.00 USD | 90,500.00 USD | 0.00 USD | `+2.38%` | `906.36` |
| `Live` | `Short` | `99.95` | 625,610.00 USD | 45,240.00 USD | 0.00 USD | `+2.48%` | `452.66` |
| `Live` | `Short` | `100.05` | 633,640.00 USD | 8,030.00 USD | 0.00 USD | `+2.58%` | `80.24` |
| `Live` | `Short` | `100.15` | 643,810.00 USD | 10,180.00 USD | 0.00 USD | `+2.68%` | `101.62` |
| `Live` | `Short` | `100.35` | 644,610.00 USD | 799.79 USD | 0.00 USD | `+2.89%` | `7.97` |
| `Live` | `Short` | `100.65` | 666,420.00 USD | 21,810.00 USD | 0.00 USD | `+3.20%` | `216.69` |
| `Live` | `Short` | `100.75` | 698,000.00 USD | 31,580.00 USD | 0.00 USD | `+3.30%` | `313.47` |
| `Live` | `Short` | `100.85` | 702,050.00 USD | 4,040.00 USD | 0.00 USD | `+3.40%` | `40.09` |
| `Live` | `Short` | `100.95` | 714,310.00 USD | 12,260.00 USD | 0.00 USD | `+3.50%` | `121.44` |
| `Live` | `Short` | `101.05` | 714,540.00 USD | 230.39 USD | 0.00 USD | `+3.61%` | `2.28` |
| `Live` | `Short` | `101.15` | 717,920.00 USD | 3,380.00 USD | 0.00 USD | `+3.71%` | `33.46` |
| `Live` | `Short` | `101.25` | 718,200.00 USD | 275.40 USD | 0.00 USD | `+3.81%` | `2.72` |
| `Live` | `Short` | `101.35` | 722,170.00 USD | 3,970.00 USD | 0.00 USD | `+3.91%` | `39.17` |
| `Live` | `Short` | `101.55` | 722,980.00 USD | 814.43 USD | 0.00 USD | `+4.12%` | `8.02` |
| `Live` | `Short` | `101.65` | 724,810.00 USD | 1,820.00 USD | 0.00 USD | `+4.22%` | `17.95` |
| `Live` | `Short` | `102.05` | 729,490.00 USD | 4,690.00 USD | 0.00 USD | `+4.63%` | `45.92` |
| `Live` | `Short` | `102.35` | 735,730.00 USD | 6,240.00 USD | 0.00 USD | `+4.94%` | `60.95` |
| `Live` | `Short` | `102.45` | 735,850.00 USD | 116.79 USD | 0.00 USD | `+5.04%` | `1.14` |
| `Live` | `Short` | `102.55` | 736,500.00 USD | 648.12 USD | 0.00 USD | `+5.14%` | `6.32` |
| `Live` | `Short` | `102.65` | 736,720.00 USD | 223.78 USD | 0.00 USD | `+5.25%` | `2.18` |
| `Live` | `Short` | `102.95` | 739,800.00 USD | 3,080.00 USD | 0.00 USD | `+5.56%` | `29.92` |
| `Live` | `Short` | `103.05` | 742,260.00 USD | 2,460.00 USD | 0.00 USD | `+5.66%` | `23.84` |
| `Live` | `Short` | `103.15` | 753,250.00 USD | 11,000.00 USD | 0.00 USD | `+5.76%` | `106.62` |
| `Live` | `Short` | `103.35` | 754,310.00 USD | 1,050.00 USD | 0.00 USD | `+5.97%` | `10.18` |
| `Live` | `Short` | `103.45` | 754,440.00 USD | 129.31 USD | 0.00 USD | `+6.07%` | `1.25` |
| `Live` | `Short` | `103.55` | 765,610.00 USD | 11,180.00 USD | 0.00 USD | `+6.17%` | `107.94` |
| `Live` | `Short` | `103.75` | 769,610.00 USD | 4,000.00 USD | 0.00 USD | `+6.38%` | `38.53` |
| `Live` | `Short` | `103.85` | 792,310.00 USD | 22,700.00 USD | 0.00 USD | `+6.48%` | `218.58` |
| `Live` | `Short` | `104.05` | 793,980.00 USD | 1,670.00 USD | 0.00 USD | `+6.68%` | `16.03` |
| `Live` | `Short` | `104.15` | 795,040.00 USD | 1,060.00 USD | 0.00 USD | `+6.79%` | `10.20` |
| `Live` | `Short` | `104.25` | 886,860.00 USD | 91,820.00 USD | 0.00 USD | `+6.89%` | `880.78` |
| `Live` | `Short` | `104.35` | 887,490.00 USD | 625.06 USD | 0.00 USD | `+6.99%` | `5.99` |
| `Live` | `Short` | `104.45` | 890,330.00 USD | 2,850.00 USD | 0.00 USD | `+7.09%` | `27.25` |
| `Live` | `Short` | `104.55` | 902,680.00 USD | 12,340.00 USD | 0.00 USD | `+7.20%` | `118.07` |
| `Live` | `Short` | `104.65` | 1,530,000.00 USD | 630,930.00 USD | 0.00 USD | `+7.30%` | `6,028.99` |
| `Live` | `Short` | `104.75` | 1,530,000.00 USD | 199.02 USD | 0.00 USD | `+7.40%` | `1.90` |
| `Live` | `Short` | `104.95` | 1,530,000.00 USD | 1,060.00 USD | 0.00 USD | `+7.61%` | `10.14` |
| `Live` | `Short` | `105.25` | 1,540,000.00 USD | 3,350.00 USD | 0.00 USD | `+7.91%` | `31.87` |
| `Live` | `Short` | `105.35` | 1,540,000.00 USD | 431.94 USD | 0.00 USD | `+8.02%` | `4.10` |
| `Live` | `Short` | `105.45` | 2,170,000.00 USD | 636,160.00 USD | 0.00 USD | `+8.12%` | `6,032.82` |
| `Live` | `Short` | `105.55` | 2,180,000.00 USD | 4,180.00 USD | 0.00 USD | `+8.22%` | `39.61` |
| `Live` | `Short` | `105.95` | 2,180,000.00 USD | 266.99 USD | 0.00 USD | `+8.63%` | `2.52` |
| `Live` | `Short` | `106.05` | 2,180,000.00 USD | 1,420.00 USD | 0.00 USD | `+8.73%` | `13.39` |
| `Live` | `Short` | `106.15` | 2,190,000.00 USD | 5,380.00 USD | 0.00 USD | `+8.84%` | `50.65` |
| `Live` | `Short` | `106.25` | 2,190,000.00 USD | 435.62 USD | 0.00 USD | `+8.94%` | `4.10` |
| `Live` | `Short` | `106.35` | 2,190,000.00 USD | 651.93 USD | 0.00 USD | `+9.04%` | `6.13` |
| `Live` | `Short` | `106.45` | 2,190,000.00 USD | 696.18 USD | 0.00 USD | `+9.14%` | `6.54` |
| `Live` | `Short` | `106.85` | 2,670,000.00 USD | 478,970.00 USD | 0.00 USD | `+9.55%` | `4,482.65` |
| `Live` | `Short` | `106.95` | 2,670,000.00 USD | 291.97 USD | 0.00 USD | `+9.66%` | `2.73` |
| `Live` | `Short` | `107.05` | 2,680,000.00 USD | 12,400.00 USD | 0.00 USD | `+9.76%` | `115.88` |
| `Live` | `Short` | `107.15` | 2,680,000.00 USD | 613.97 USD | 0.00 USD | `+9.86%` | `5.73` |
| `Live` | `Short` | `107.25` | 2,720,000.00 USD | 35,170.00 USD | 0.00 USD | `+9.96%` | `327.97` |
| `Live` | `Short` | `107.35` | 2,910,000.00 USD | 198,170.00 USD | 0.00 USD | `+10.07%` | `1,846.00` |
| `Live` | `Short` | `107.45` | 2,970,000.00 USD | 53,960.00 USD | 0.00 USD | `+10.17%` | `502.17` |
| `Live` | `Short` | `107.65` | 2,970,000.00 USD | 1,820.00 USD | 0.00 USD | `+10.37%` | `16.87` |
| `Live` | `Short` | `107.75` | 2,980,000.00 USD | 5,840.00 USD | 0.00 USD | `+10.48%` | `54.18` |
| `Live` | `Short` | `107.85` | 2,980,000.00 USD | 106.77 USD | 0.00 USD | `+10.58%` | `0.99` |
| `Live` | `Short` | `108.05` | 2,980,000.00 USD | 1,080.00 USD | 0.00 USD | `+10.78%` | `10.04` |
| `Live` | `Short` | `108.15` | 2,980,000.00 USD | 1,150.00 USD | 0.00 USD | `+10.89%` | `10.66` |
| `Live` | `Short` | `108.35` | 2,980,000.00 USD | 3,690.00 USD | 0.00 USD | `+11.09%` | `34.03` |
| `Live` | `Short` | `108.45` | 3,100,000.00 USD | 119,130.00 USD | 0.00 USD | `+11.19%` | `1,098.52` |
| `Live` | `Short` | `108.55` | 3,100,000.00 USD | 117.23 USD | 0.00 USD | `+11.30%` | `1.08` |
| `Live` | `Short` | `108.65` | 3,110,000.00 USD | 5,050.00 USD | 0.00 USD | `+11.40%` | `46.45` |
| `Live` | `Short` | `108.75` | 3,110,000.00 USD | 6,560.00 USD | 0.00 USD | `+11.50%` | `60.30` |
| `Live` | `Short` | `108.85` | 3,120,000.00 USD | 3,230.00 USD | 0.00 USD | `+11.60%` | `29.68` |
| `Live` | `Short` | `108.95` | 3,120,000.00 USD | 955.49 USD | 0.00 USD | `+11.71%` | `8.77` |
| `Live` | `Short` | `109.05` | 3,130,000.00 USD | 11,060.00 USD | 0.00 USD | `+11.81%` | `101.42` |
| `Live` | `Short` | `109.15` | 3,150,000.00 USD | 22,380.00 USD | 0.00 USD | `+11.91%` | `205.03` |
| `Live` | `Short` | `109.25` | 3,150,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.01%` | `9.76` |
| `Live` | `Short` | `109.35` | 3,150,000.00 USD | 247.13 USD | 0.00 USD | `+12.12%` | `2.26` |
| `Live` | `Short` | `109.45` | 3,260,000.00 USD | 105,660.00 USD | 0.00 USD | `+12.22%` | `965.36` |
| `Live` | `Short` | `109.55` | 3,260,000.00 USD | 461.21 USD | 0.00 USD | `+12.32%` | `4.21` |
| `Live` | `Short` | `109.65` | 3,300,000.00 USD | 42,990.00 USD | 0.00 USD | `+12.42%` | `392.09` |
| `Live` | `Short` | `109.85` | 3,300,000.00 USD | 572.32 USD | 0.00 USD | `+12.63%` | `5.21` |
| `Live` | `Short` | `109.95` | 3,300,000.00 USD | 537.66 USD | 0.00 USD | `+12.73%` | `4.89` |
| `Live` | `Short` | `110.15` | 3,310,000.00 USD | 6,080.00 USD | 0.00 USD | `+12.94%` | `55.18` |
| `Live` | `Short` | `110.25` | 3,340,000.00 USD | 37,080.00 USD | 0.00 USD | `+13.04%` | `336.29` |
| `Live` | `Short` | `110.35` | 3,500,000.00 USD | 152,660.00 USD | 0.00 USD | `+13.14%` | `1,383.42` |
| `Live` | `Short` | `110.45` | 3,510,000.00 USD | 16,940.00 USD | 0.00 USD | `+13.24%` | `153.41` |
| `Live` | `Short` | `110.55` | 3,910,000.00 USD | 391,490.00 USD | 0.00 USD | `+13.35%` | `3,541.26` |
| `Live` | `Short` | `110.75` | 3,910,000.00 USD | 575.90 USD | 0.00 USD | `+13.55%` | `5.20` |
| `Live` | `Short` | `110.85` | 3,920,000.00 USD | 12,850.00 USD | 0.00 USD | `+13.66%` | `115.93` |
| `Live` | `Short` | `110.95` | 3,930,000.00 USD | 12,860.00 USD | 0.00 USD | `+13.76%` | `115.95` |
| `Live` | `Short` | `111.15` | 3,930,000.00 USD | 1,710.00 USD | 0.00 USD | `+13.96%` | `15.37` |
| `Live` | `Short` | `111.25` | 3,930,000.00 USD | 234.74 USD | 0.00 USD | `+14.07%` | `2.11` |
| `Live` | `Short` | `111.35` | 3,930,000.00 USD | 390.84 USD | 0.00 USD | `+14.17%` | `3.51` |
| `Live` | `Short` | `111.45` | 3,940,000.00 USD | 3,620.00 USD | 0.00 USD | `+14.27%` | `32.45` |
| `Live` | `Short` | `111.65` | 3,940,000.00 USD | 197.62 USD | 0.00 USD | `+14.48%` | `1.77` |
| `Live` | `Short` | `111.75` | 3,940,000.00 USD | 339.72 USD | 0.00 USD | `+14.58%` | `3.04` |
| `Live` | `Short` | `111.85` | 3,950,000.00 USD | 15,880.00 USD | 0.00 USD | `+14.68%` | `141.95` |
| `Live` | `Short` | `111.95` | 3,960,000.00 USD | 1,010.00 USD | 0.00 USD | `+14.78%` | `9.04` |
| `Live` | `Short` | `112.25` | 3,960,000.00 USD | 627.48 USD | 0.00 USD | `+15.09%` | `5.59` |
| `Live` | `Short` | `112.45` | 3,960,000.00 USD | 5,670.00 USD | 0.00 USD | `+15.30%` | `50.42` |
| `Live` | `Short` | `112.55` | 3,960,000.00 USD | 844.13 USD | 0.00 USD | `+15.40%` | `7.50` |
| `Live` | `Short` | `112.65` | 3,960,000.00 USD | 584.65 USD | 0.00 USD | `+15.50%` | `5.19` |
| `Live` | `Short` | `112.75` | 4,080,000.00 USD | 118,640.00 USD | 0.00 USD | `+15.60%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 4,080,000.00 USD | 1,460.00 USD | 0.00 USD | `+15.71%` | `12.91` |
| `Live` | `Short` | `112.95` | 4,090,000.00 USD | 11,290.00 USD | 0.00 USD | `+15.81%` | `100.00` |
| `Live` | `Short` | `113.05` | 4,360,000.00 USD | 263,100.00 USD | 0.00 USD | `+15.91%` | `2,327.32` |
| `Live` | `Short` | `113.15` | 4,370,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.01%` | `84.51` |
| `Live` | `Short` | `113.25` | 4,370,000.00 USD | 114.38 USD | 0.00 USD | `+16.12%` | `1.01` |
| `Live` | `Short` | `113.45` | 4,470,000.00 USD | 104,150.00 USD | 0.00 USD | `+16.32%` | `918.04` |
| `Live` | `Short` | `113.55` | 4,480,000.00 USD | 5,180.00 USD | 0.00 USD | `+16.42%` | `45.65` |
| `Live` | `Short` | `113.65` | 4,480,000.00 USD | 3,220.00 USD | 0.00 USD | `+16.53%` | `28.37` |
| `Live` | `Short` | `113.75` | 4,480,000.00 USD | 1,180.00 USD | 0.00 USD | `+16.63%` | `10.33` |
| `Live` | `Short` | `113.95` | 4,500,000.00 USD | 21,840.00 USD | 0.00 USD | `+16.83%` | `191.69` |
| `Live` | `Short` | `114.05` | 4,520,000.00 USD | 21,420.00 USD | 0.00 USD | `+16.94%` | `187.79` |
| `Live` | `Short` | `114.15` | 4,530,000.00 USD | 1,960.00 USD | 0.00 USD | `+17.04%` | `17.21` |
| `Live` | `Short` | `114.25` | 4,530,000.00 USD | 2,620.00 USD | 0.00 USD | `+17.14%` | `22.95` |
| `Live` | `Short` | `114.45` | 4,530,000.00 USD | 3,050.00 USD | 0.00 USD | `+17.35%` | `26.65` |
| `Live` | `Short` | `114.95` | 4,530,000.00 USD | 496.58 USD | 0.00 USD | `+17.86%` | `4.32` |
| `Live` | `Short` | `115.05` | 5,100,000.00 USD | 570,810.00 USD | 0.00 USD | `+17.96%` | `4,961.43` |
| `Live` | `Short` | `115.15` | 5,620,000.00 USD | 518,330.00 USD | 0.00 USD | `+18.06%` | `4,501.35` |
| `Live` | `Short` | `115.25` | 5,640,000.00 USD | 18,240.00 USD | 0.00 USD | `+18.17%` | `158.28` |
| `Live` | `Short` | `115.35` | 6,520,000.00 USD | 884,130.00 USD | 0.00 USD | `+18.27%` | `7,664.73` |
| `Live` | `Short` | `115.55` | 6,570,000.00 USD | 46,710.00 USD | 0.00 USD | `+18.47%` | `404.24` |
| `Live` | `Short` | `115.75` | 6,570,000.00 USD | 160.89 USD | 0.00 USD | `+18.68%` | `1.39` |
| `Live` | `Short` | `115.85` | 6,570,000.00 USD | 289.62 USD | 0.00 USD | `+18.78%` | `2.50` |
| `Live` | `Short` | `116.05` | 6,580,000.00 USD | 4,450.00 USD | 0.00 USD | `+18.99%` | `38.34` |
| `Live` | `Short` | `116.15` | 6,590,000.00 USD | 14,220.00 USD | 0.00 USD | `+19.09%` | `122.39` |
| `Live` | `Short` | `116.35` | 6,590,000.00 USD | 4,960.00 USD | 0.00 USD | `+19.29%` | `42.60` |
| `Live` | `Short` | `116.45` | 6,600,000.00 USD | 716.17 USD | 0.00 USD | `+19.40%` | `6.15` |
| `Live` | `Short` | `116.55` | 6,600,000.00 USD | 2,780.00 USD | 0.00 USD | `+19.50%` | `23.86` |
| `Live` | `Short` | `116.65` | 6,600,000.00 USD | 113.15 USD | 0.00 USD | `+19.60%` | `0.97` |
| `Live` | `Short` | `116.75` | 6,630,000.00 USD | 31,740.00 USD | 0.00 USD | `+19.70%` | `271.88` |
| `Live` | `Short` | `117.05` | 6,630,000.00 USD | 156.85 USD | 0.00 USD | `+20.01%` | `1.34` |
| `Live` | `Short` | `117.15` | 6,650,000.00 USD | 23,970.00 USD | 0.00 USD | `+20.11%` | `204.62` |
| `Live` | `Short` | `117.25` | 11,360,000.00 USD | 4,700,000.00 USD | 0.00 USD | `+20.22%` | `40,124.21` |
| `Live` | `Short` | `117.35` | 11,360,000.00 USD | 230.01 USD | 0.00 USD | `+20.32%` | `1.96` |
| `Live` | `Short` | `117.45` | 11,360,000.00 USD | 128.02 USD | 0.00 USD | `+20.42%` | `1.09` |
| `Live` | `Short` | `117.75` | 11,370,000.00 USD | 11,130.00 USD | 0.00 USD | `+20.73%` | `94.48` |
| `Live` | `Short` | `117.95` | 11,380,000.00 USD | 12,060.00 USD | 0.00 USD | `+20.93%` | `102.22` |
| `Live` | `Short` | `118.45` | 11,410,000.00 USD | 30,080.00 USD | 0.00 USD | `+21.45%` | `253.91` |
| `Live` | `Short` | `118.55` | 11,410,000.00 USD | 1,110.00 USD | 0.00 USD | `+21.55%` | `9.38` |
| `Live` | `Short` | `118.75` | 11,410,000.00 USD | 309.94 USD | 0.00 USD | `+21.75%` | `2.61` |
| `Live` | `Short` | `119.25` | 11,440,000.00 USD | 27,460.00 USD | 0.00 USD | `+22.27%` | `230.29` |
| `Live` | `Short` | `119.35` | 11,500,000.00 USD | 57,850.00 USD | 0.00 USD | `+22.37%` | `484.72` |
| `Live` | `Short` | `119.55` | 15,780,000.00 USD | 4,280,000.00 USD | 0.00 USD | `+22.58%` | `35,779.15` |
| `Live` | `Short` | `119.75` | 15,780,000.00 USD | 261.06 USD | 0.00 USD | `+22.78%` | `2.18` |
| `Live` | `Short` | `119.95` | 15,880,000.00 USD | 100,320.00 USD | 0.00 USD | `+22.99%` | `836.32` |
| `Live` | `Short` | `120.15` | 15,880,000.00 USD | 4,920.00 USD | 0.00 USD | `+23.19%` | `40.92` |
| `Live` | `Short` | `120.35` | 15,880,000.00 USD | 145.62 USD | 0.00 USD | `+23.40%` | `1.21` |
| `Live` | `Short` | `120.55` | 15,880,000.00 USD | 2,640.00 USD | 0.00 USD | `+23.60%` | `21.88` |
| `Live` | `Short` | `120.65` | 15,890,000.00 USD | 874.71 USD | 0.00 USD | `+23.70%` | `7.25` |
| `Live` | `Short` | `120.75` | 15,900,000.00 USD | 10,870.00 USD | 0.00 USD | `+23.81%` | `90.00` |
| `Live` | `Short` | `120.85` | 15,900,000.00 USD | 282.79 USD | 0.00 USD | `+23.91%` | `2.34` |
| `Live` | `Short` | `120.95` | 15,910,000.00 USD | 15,290.00 USD | 0.00 USD | `+24.01%` | `126.38` |
| `Live` | `Short` | `121.15` | 15,920,000.00 USD | 12,720.00 USD | 0.00 USD | `+24.22%` | `105.00` |
| `Live` | `Short` | `121.25` | 15,930,000.00 USD | 1,530.00 USD | 0.00 USD | `+24.32%` | `12.60` |
| `Live` | `Short` | `121.55` | 15,930,000.00 USD | 5,940.00 USD | 0.00 USD | `+24.63%` | `48.87` |
| `Live` | `Short` | `121.65` | 15,950,000.00 USD | 16,300.00 USD | 0.00 USD | `+24.73%` | `133.95` |
| `Live` | `Short` | `121.85` | 16,000,000.00 USD | 54,760.00 USD | 0.00 USD | `+24.93%` | `449.38` |
| `Live` | `Short` | `122.05` | 16,060,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.14%` | `460.06` |
| `Live` | `Short` | `122.15` | 16,060,000.00 USD | 169.79 USD | 0.00 USD | `+25.24%` | `1.39` |
| `Live` | `Short` | `122.25` | 16,060,000.00 USD | 2,200.00 USD | 0.00 USD | `+25.34%` | `17.99` |
| `Live` | `Short` | `122.45` | 16,080,000.00 USD | 17,500.00 USD | 0.00 USD | `+25.55%` | `142.95` |
| `Live` | `Short` | `122.65` | 16,080,000.00 USD | 116.52 USD | 0.00 USD | `+25.75%` | `0.95` |
| `Live` | `Short` | `122.95` | 16,080,000.00 USD | 2,790.00 USD | 0.00 USD | `+26.06%` | `22.66` |
| `Live` | `Short` | `123.35` | 16,080,000.00 USD | 2,330.00 USD | 0.00 USD | `+26.47%` | `18.92` |
| `Live` | `Short` | `123.45` | 31,340,000.00 USD | 15,260,000.00 USD | 0.00 USD | `+26.57%` | `123,605.21` |
| `Live` | `Short` | `123.55` | 31,350,000.00 USD | 3,430.00 USD | 0.00 USD | `+26.68%` | `27.73` |
| `Live` | `Short` | `124.05` | 31,350,000.00 USD | 586.76 USD | 0.00 USD | `+27.19%` | `4.73` |
| `Live` | `Short` | `124.25` | 31,360,000.00 USD | 17,600.00 USD | 0.00 USD | `+27.39%` | `141.62` |
| `Live` | `Short` | `124.45` | 32,220,000.00 USD | 859,810.00 USD | 0.00 USD | `+27.60%` | `6,908.91` |
| `Live` | `Short` | `124.65` | 32,230,000.00 USD | 675.60 USD | 0.00 USD | `+27.80%` | `5.42` |
| `Live` | `Short` | `124.75` | 32,230,000.00 USD | 5,920.00 USD | 0.00 USD | `+27.91%` | `47.43` |
| `Live` | `Short` | `124.95` | 32,270,000.00 USD | 33,830.00 USD | 0.00 USD | `+28.11%` | `270.71` |
| `Live` | `Short` | `125.25` | 32,270,000.00 USD | 2,420.00 USD | 0.00 USD | `+28.42%` | `19.35` |
| `Live` | `Short` | `125.35` | 32,270,000.00 USD | 5,910.00 USD | 0.00 USD | `+28.52%` | `47.15` |
| `Live` | `Short` | `125.45` | 32,280,000.00 USD | 3,760.00 USD | 0.00 USD | `+28.62%` | `30.00` |
| `Live` | `Short` | `125.75` | 32,280,000.00 USD | 1,930.00 USD | 0.00 USD | `+28.93%` | `15.31` |
| `Live` | `Short` | `125.85` | 32,290,000.00 USD | 6,200.00 USD | 0.00 USD | `+29.03%` | `49.29` |
| `Live` | `Short` | `125.95` | 32,290,000.00 USD | 110.84 USD | 0.00 USD | `+29.14%` | `0.88` |
| `Live` | `Short` | `126.05` | 32,290,000.00 USD | 810.50 USD | 0.00 USD | `+29.24%` | `6.43` |
| `Live` | `Short` | `126.15` | 32,290,000.00 USD | 470.54 USD | 0.00 USD | `+29.34%` | `3.73` |
| `Live` | `Short` | `126.35` | 32,290,000.00 USD | 305.77 USD | 0.00 USD | `+29.55%` | `2.42` |
| `Live` | `Short` | `126.65` | 32,320,000.00 USD | 32,990.00 USD | 0.00 USD | `+29.85%` | `260.47` |
| `Live` | `Short` | `126.75` | 32,330,000.00 USD | 8,670.00 USD | 0.00 USD | `+29.96%` | `68.39` |
| `Live` | `Short` | `126.85` | 32,330,000.00 USD | 2,100.00 USD | 0.00 USD | `+30.06%` | `16.55` |
| `Live` | `Short` | `126.95` | 32,390,000.00 USD | 56,490.00 USD | 0.00 USD | `+30.16%` | `445.01` |
| `Live` | `Short` | `127.05` | 32,390,000.00 USD | 2,030.00 USD | 0.00 USD | `+30.26%` | `16.01` |
| `Live` | `Short` | `127.35` | 32,410,000.00 USD | 16,190.00 USD | 0.00 USD | `+30.57%` | `127.13` |
| `Live` | `Short` | `127.65` | 32,410,000.00 USD | 4,840.00 USD | 0.00 USD | `+30.88%` | `37.89` |
| `Live` | `Short` | `127.75` | 32,670,000.00 USD | 255,500.00 USD | 0.00 USD | `+30.98%` | `2,000.00` |
| `Live` | `Short` | `127.85` | 32,670,000.00 USD | 4,200.00 USD | 0.00 USD | `+31.09%` | `32.88` |
| `Live` | `Short` | `127.95` | 32,680,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.19%` | `82.13` |
| `Live` | `Short` | `128.05` | 32,800,000.00 USD | 116,200.00 USD | 0.00 USD | `+31.29%` | `907.49` |
| `Live` | `Short` | `128.35` | 32,800,000.00 USD | 195.09 USD | 0.00 USD | `+31.60%` | `1.52` |
| `Live` | `Short` | `128.45` | 32,800,000.00 USD | 271.03 USD | 0.00 USD | `+31.70%` | `2.11` |
| `Live` | `Short` | `128.65` | 32,800,000.00 USD | 944.29 USD | 0.00 USD | `+31.91%` | `7.34` |
| `Live` | `Short` | `128.75` | 33,510,000.00 USD | 714,710.00 USD | 0.00 USD | `+32.01%` | `5,551.11` |
| `Live` | `Short` | `128.85` | 33,560,000.00 USD | 45,050.00 USD | 0.00 USD | `+32.11%` | `349.60` |
| `Live` | `Short` | `128.95` | 33,590,000.00 USD | 30,700.00 USD | 0.00 USD | `+32.21%` | `238.04` |
| `Live` | `Short` | `129.25` | 33,620,000.00 USD | 32,480.00 USD | 0.00 USD | `+32.52%` | `251.27` |
| `Live` | `Short` | `129.35` | 33,630,000.00 USD | 8,620.00 USD | 0.00 USD | `+32.62%` | `66.66` |
| `Live` | `Short` | `129.55` | 33,690,000.00 USD | 56,180.00 USD | 0.00 USD | `+32.83%` | `433.68` |
| `Live` | `Short` | `129.75` | 33,720,000.00 USD | 36,480.00 USD | 0.00 USD | `+33.03%` | `281.19` |
| `Live` | `Short` | `129.85` | 33,720,000.00 USD | 490.83 USD | 0.00 USD | `+33.14%` | `3.78` |
| `Live` | `Short` | `129.95` | 33,720,000.00 USD | 131.25 USD | 0.00 USD | `+33.24%` | `1.01` |
| `Live` | `Short` | `130.25` | 33,720,000.00 USD | 145.88 USD | 0.00 USD | `+33.55%` | `1.12` |
| `Live` | `Short` | `130.55` | 33,720,000.00 USD | 195.83 USD | 0.00 USD | `+33.85%` | `1.50` |
| `Live` | `Short` | `130.65` | 33,720,000.00 USD | 866.21 USD | 0.00 USD | `+33.96%` | `6.63` |
| `Live` | `Short` | `130.85` | 34,230,000.00 USD | 503,820.00 USD | 0.00 USD | `+34.16%` | `3,850.39` |
| `Live` | `Short` | `130.95` | 34,240,000.00 USD | 14,890.00 USD | 0.00 USD | `+34.26%` | `113.72` |
| `Live` | `Short` | `131.05` | 34,240,000.00 USD | 188.71 USD | 0.00 USD | `+34.37%` | `1.44` |
| `Live` | `Short` | `131.25` | 34,240,000.00 USD | 1,560.00 USD | 0.00 USD | `+34.57%` | `11.87` |
| `Live` | `Short` | `131.45` | 34,240,000.00 USD | 219.52 USD | 0.00 USD | `+34.78%` | `1.67` |
| `Live` | `Short` | `131.85` | 34,250,000.00 USD | 5,540.00 USD | 0.00 USD | `+35.19%` | `42.01` |
| `Live` | `Short` | `132.15` | 34,250,000.00 USD | 325.09 USD | 0.00 USD | `+35.49%` | `2.46` |
| `Live` | `Short` | `132.25` | 34,260,000.00 USD | 6,610.00 USD | 0.00 USD | `+35.60%` | `50.00` |
| `Live` | `Short` | `132.35` | 34,270,000.00 USD | 12,870.00 USD | 0.00 USD | `+35.70%` | `97.27` |
| `Live` | `Short` | `132.45` | 34,280,000.00 USD | 8,530.00 USD | 0.00 USD | `+35.80%` | `64.37` |
| `Live` | `Short` | `132.55` | 34,280,000.00 USD | 695.89 USD | 0.00 USD | `+35.90%` | `5.25` |
| `Live` | `Short` | `132.65` | 34,280,000.00 USD | 240.10 USD | 0.00 USD | `+36.01%` | `1.81` |
| `Live` | `Short` | `132.85` | 34,340,000.00 USD | 62,170.00 USD | 0.00 USD | `+36.21%` | `467.99` |
| `Live` | `Short` | `132.95` | 34,350,000.00 USD | 9,110.00 USD | 0.00 USD | `+36.31%` | `68.51` |
| `Live` | `Short` | `133.15` | 34,360,000.00 USD | 8,440.00 USD | 0.00 USD | `+36.52%` | `63.42` |
| `Live` | `Short` | `133.55` | 34,360,000.00 USD | 186.97 USD | 0.00 USD | `+36.93%` | `1.40` |
| `Live` | `Short` | `133.65` | 34,410,000.00 USD | 48,220.00 USD | 0.00 USD | `+37.03%` | `360.81` |
| `Live` | `Short` | `133.75` | 34,560,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.13%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 34,560,000.00 USD | 503.65 USD | 0.00 USD | `+37.34%` | `3.76` |
| `Live` | `Short` | `134.05` | 34,560,000.00 USD | 2,430.00 USD | 0.00 USD | `+37.44%` | `18.16` |
| `Live` | `Short` | `134.25` | 34,600,000.00 USD | 41,810.00 USD | 0.00 USD | `+37.65%` | `311.40` |
| `Live` | `Short` | `134.75` | 34,610,000.00 USD | 2,620.00 USD | 0.00 USD | `+38.16%` | `19.46` |
| `Live` | `Short` | `135.05` | 34,790,000.00 USD | 181,050.00 USD | 0.00 USD | `+38.47%` | `1,340.64` |
| `Live` | `Short` | `135.85` | 34,790,000.00 USD | 3,250.00 USD | 0.00 USD | `+39.29%` | `23.94` |
| `Live` | `Short` | `135.95` | 34,790,000.00 USD | 504.37 USD | 0.00 USD | `+39.39%` | `3.71` |
| `Live` | `Short` | `136.55` | 34,790,000.00 USD | 136.55 USD | 0.00 USD | `+40.01%` | `1.00` |
| `Live` | `Short` | `136.65` | 34,790,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.11%` | `8.14` |
| `Live` | `Short` | `137.05` | 34,790,000.00 USD | 836.00 USD | 0.00 USD | `+40.52%` | `6.10` |
| `Live` | `Short` | `137.15` | 34,790,000.00 USD | 809.19 USD | 0.00 USD | `+40.62%` | `5.90` |
| `Live` | `Short` | `137.55` | 39,910,000.00 USD | 5,120,000.00 USD | 0.00 USD | `+41.03%` | `37,198.39` |
| `Live` | `Short` | `137.85` | 40,450,000.00 USD | 537,620.00 USD | 0.00 USD | `+41.34%` | `3,900.00` |
| `Live` | `Short` | `138.05` | 40,450,000.00 USD | 1,270.00 USD | 0.00 USD | `+41.54%` | `9.20` |
| `Live` | `Short` | `138.15` | 40,540,000.00 USD | 86,640.00 USD | 0.00 USD | `+41.65%` | `627.11` |
| `Live` | `Short` | `138.25` | 40,670,000.00 USD | 136,610.00 USD | 0.00 USD | `+41.75%` | `988.12` |
| `Live` | `Short` | `138.35` | 40,690,000.00 USD | 18,980.00 USD | 0.00 USD | `+41.85%` | `137.20` |
| `Live` | `Short` | `138.55` | 40,900,000.00 USD | 207,490.00 USD | 0.00 USD | `+42.06%` | `1,497.60` |
| `Live` | `Short` | `138.65` | 40,910,000.00 USD | 14,900.00 USD | 0.00 USD | `+42.16%` | `107.50` |
| `Live` | `Short` | `138.75` | 43,000,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+42.26%` | `15,001.76` |
| `Live` | `Short` | `138.95` | 43,000,000.00 USD | 1,670.00 USD | 0.00 USD | `+42.47%` | `12.02` |
| `Live` | `Short` | `139.15` | 43,000,000.00 USD | 1,170.00 USD | 0.00 USD | `+42.67%` | `8.43` |
| `Live` | `Short` | `139.35` | 43,000,000.00 USD | 2,990.00 USD | 0.00 USD | `+42.88%` | `21.43` |
| `Live` | `Short` | `139.55` | 43,000,000.00 USD | 494.01 USD | 0.00 USD | `+43.08%` | `3.54` |
| `Live` | `Short` | `139.65` | 43,000,000.00 USD | 769.47 USD | 0.00 USD | `+43.18%` | `5.51` |
| `Live` | `Short` | `140.05` | 43,000,000.00 USD | 1,040.00 USD | 0.00 USD | `+43.59%` | `7.40` |
| `Live` | `Short` | `140.35` | 43,070,000.00 USD | 67,040.00 USD | 0.00 USD | `+43.90%` | `477.67` |
| `Live` | `Short` | `140.45` | 43,080,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.00%` | `34.66` |
| `Live` | `Short` | `140.55` | 43,080,000.00 USD | 8,030.00 USD | 0.00 USD | `+44.11%` | `57.16` |
| `Live` | `Short` | `140.65` | 43,080,000.00 USD | 209.57 USD | 0.00 USD | `+44.21%` | `1.49` |
| `Live` | `Short` | `140.95` | 44,160,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+44.52%` | `7,623.31` |
| `Live` | `Short` | `141.05` | 44,160,000.00 USD | 125.53 USD | 0.00 USD | `+44.62%` | `0.89` |
| `Live` | `Short` | `141.35` | 44,160,000.00 USD | 210.61 USD | 0.00 USD | `+44.93%` | `1.49` |
| `Live` | `Short` | `141.45` | 44,410,000.00 USD | 250,580.00 USD | 0.00 USD | `+45.03%` | `1,771.52` |
| `Live` | `Short` | `141.55` | 44,410,000.00 USD | 236.39 USD | 0.00 USD | `+45.13%` | `1.67` |
| `Live` | `Short` | `141.65` | 44,410,000.00 USD | 2,650.00 USD | 0.00 USD | `+45.23%` | `18.71` |
| `Live` | `Short` | `141.75` | 44,410,000.00 USD | 103.48 USD | 0.00 USD | `+45.34%` | `0.73` |
| `Live` | `Short` | `142.15` | 44,540,000.00 USD | 131,260.00 USD | 0.00 USD | `+45.75%` | `923.38` |
| `Live` | `Short` | `142.45` | 44,540,000.00 USD | 151.00 USD | 0.00 USD | `+46.05%` | `1.06` |
| `Live` | `Short` | `142.55` | 44,560,000.00 USD | 12,960.00 USD | 0.00 USD | `+46.16%` | `90.91` |
| `Live` | `Short` | `142.65` | 44,560,000.00 USD | 112.69 USD | 0.00 USD | `+46.26%` | `0.79` |
| `Live` | `Short` | `142.75` | 44,560,000.00 USD | 368.30 USD | 0.00 USD | `+46.36%` | `2.58` |
| `Live` | `Short` | `142.95` | 44,640,000.00 USD | 87,010.00 USD | 0.00 USD | `+46.57%` | `608.65` |
| `Live` | `Short` | `143.15` | 44,650,000.00 USD | 1,330.00 USD | 0.00 USD | `+46.77%` | `9.31` |
| `Live` | `Short` | `143.35` | 44,670,000.00 USD | 22,260.00 USD | 0.00 USD | `+46.98%` | `155.27` |
| `Live` | `Short` | `143.45` | 44,670,000.00 USD | 1,150.00 USD | 0.00 USD | `+47.08%` | `8.00` |
| `Live` | `Short` | `143.95` | 44,690,000.00 USD | 19,290.00 USD | 0.00 USD | `+47.59%` | `134.01` |
| `Live` | `Short` | `144.05` | 44,690,000.00 USD | 3,750.00 USD | 0.00 USD | `+47.70%` | `26.00` |
| `Live` | `Short` | `144.65` | 44,690,000.00 USD | 1,240.00 USD | 0.00 USD | `+48.31%` | `8.60` |
| `Live` | `Short` | `145.05` | 44,690,000.00 USD | 487.37 USD | 0.00 USD | `+48.72%` | `3.36` |
| `Live` | `Short` | `145.15` | 44,700,000.00 USD | 1,760.00 USD | 0.00 USD | `+48.82%` | `12.12` |
| `Live` | `Short` | `145.35` | 44,700,000.00 USD | 3,720.00 USD | 0.00 USD | `+49.03%` | `25.60` |
| `Live` | `Short` | `145.55` | 44,700,000.00 USD | 1,390.00 USD | 0.00 USD | `+49.23%` | `9.57` |
| `Live` | `Short` | `145.85` | 44,710,000.00 USD | 5,850.00 USD | 0.00 USD | `+49.54%` | `40.09` |
| `Live` | `Short` | `145.95` | 44,710,000.00 USD | 820.24 USD | 0.00 USD | `+49.64%` | `5.62` |
| `Live` | `Short` | `146.05` | 45,150,000.00 USD | 438,150.00 USD | 0.00 USD | `+49.75%` | `3,000.00` |
| `Live` | `Short` | `146.15` | 45,230,000.00 USD | 88,760.00 USD | 0.00 USD | `+49.85%` | `607.33` |
| `Live` | `Short` | `146.25` | 45,240,000.00 USD | 2,770.00 USD | 0.00 USD | `+49.95%` | `18.95` |
| `Live` | `Short` | `146.35` | 45,240,000.00 USD | 7,330.00 USD | 0.00 USD | `+50.05%` | `50.10` |
| `Live` | `Short` | `146.55` | 45,250,000.00 USD | 2,110.00 USD | 0.00 USD | `+50.26%` | `14.41` |
| `Live` | `Short` | `146.65` | 45,830,000.00 USD | 587,730.00 USD | 0.00 USD | `+50.36%` | `4,007.68` |
| `Live` | `Short` | `146.85` | 46,690,000.00 USD | 859,100.00 USD | 0.00 USD | `+50.57%` | `5,850.22` |
| `Live` | `Short` | `146.95` | 46,770,000.00 USD | 81,010.00 USD | 0.00 USD | `+50.67%` | `551.30` |
| `Live` | `Short` | `147.05` | 46,770,000.00 USD | 166.17 USD | 0.00 USD | `+50.77%` | `1.13` |
| `Live` | `Short` | `147.15` | 46,780,000.00 USD | 1,730.00 USD | 0.00 USD | `+50.87%` | `11.75` |
| `Live` | `Short` | `147.35` | 46,780,000.00 USD | 169.45 USD | 0.00 USD | `+51.08%` | `1.15` |
| `Live` | `Short` | `147.45` | 46,780,000.00 USD | 204.96 USD | 0.00 USD | `+51.18%` | `1.39` |
| `Live` | `Short` | `147.55` | 46,780,000.00 USD | 1,000.00 USD | 0.00 USD | `+51.28%` | `6.78` |
| `Live` | `Short` | `147.65` | 46,780,000.00 USD | 237.72 USD | 0.00 USD | `+51.39%` | `1.61` |
| `Live` | `Short` | `147.85` | 46,780,000.00 USD | 300.14 USD | 0.00 USD | `+51.59%` | `2.03` |
| `Live` | `Short` | `148.15` | 46,780,000.00 USD | 5,730.00 USD | 0.00 USD | `+51.90%` | `38.69` |
| `Live` | `Short` | `148.25` | 46,790,000.00 USD | 5,450.00 USD | 0.00 USD | `+52.00%` | `36.73` |
| `Live` | `Short` | `148.45` | 46,790,000.00 USD | 2,060.00 USD | 0.00 USD | `+52.21%` | `13.90` |
| `Live` | `Short` | `148.55` | 47,140,000.00 USD | 344,780.00 USD | 0.00 USD | `+52.31%` | `2,321.00` |
| `Live` | `Short` | `148.75` | 47,230,000.00 USD | 91,450.00 USD | 0.00 USD | `+52.51%` | `614.80` |
| `Live` | `Short` | `148.95` | 48,610,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+52.72%` | `9,292.14` |
| `Live` | `Short` | `149.55` | 48,610,000.00 USD | 116.65 USD | 0.00 USD | `+53.33%` | `0.78` |
| `Live` | `Short` | `149.65` | 48,630,000.00 USD | 16,030.00 USD | 0.00 USD | `+53.44%` | `107.15` |
| `Live` | `Short` | `149.95` | 49,750,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+53.74%` | `7,453.90` |
| `Live` | `Short` | `150.05` | 49,750,000.00 USD | 2,930.00 USD | 0.00 USD | `+53.85%` | `19.54` |
| `Live` | `Short` | `150.25` | 49,750,000.00 USD | 345.57 USD | 0.00 USD | `+54.05%` | `2.30` |
| `Live` | `Short` | `150.35` | 49,770,000.00 USD | 17,270.00 USD | 0.00 USD | `+54.15%` | `114.86` |
| `Live` | `Short` | `150.45` | 49,810,000.00 USD | 43,030.00 USD | 0.00 USD | `+54.26%` | `286.01` |
| `Live` | `Short` | `151.05` | 49,810,000.00 USD | 2,770.00 USD | 0.00 USD | `+54.87%` | `18.37` |
| `Live` | `Short` | `151.15` | 49,810,000.00 USD | 2,540.00 USD | 0.00 USD | `+54.97%` | `16.81` |
| `Live` | `Short` | `151.45` | 49,820,000.00 USD | 9,040.00 USD | 0.00 USD | `+55.28%` | `59.66` |
| `Live` | `Short` | `151.75` | 54,450,000.00 USD | 4,630,000.00 USD | 0.00 USD | `+55.59%` | `30,517.59` |
| `Live` | `Short` | `151.95` | 54,460,000.00 USD | 1,920.00 USD | 0.00 USD | `+55.80%` | `12.64` |
| `Live` | `Short` | `152.05` | 54,460,000.00 USD | 2,320.00 USD | 0.00 USD | `+55.90%` | `15.28` |
| `Live` | `Short` | `152.25` | 54,480,000.00 USD | 22,670.00 USD | 0.00 USD | `+56.10%` | `148.89` |
| `Live` | `Short` | `152.35` | 54,770,000.00 USD | 286,550.00 USD | 0.00 USD | `+56.21%` | `1,880.87` |
| `Live` | `Short` | `152.45` | 54,770,000.00 USD | 3,150.00 USD | 0.00 USD | `+56.31%` | `20.65` |
| `Live` | `Short` | `152.55` | 55,190,000.00 USD | 423,220.00 USD | 0.00 USD | `+56.41%` | `2,774.28` |
| `Live` | `Short` | `152.75` | 55,200,000.00 USD | 1,570.00 USD | 0.00 USD | `+56.62%` | `10.30` |
| `Live` | `Short` | `153.05` | 55,200,000.00 USD | 1,060.00 USD | 0.00 USD | `+56.92%` | `6.95` |
| `Live` | `Short` | `153.15` | 55,210,000.00 USD | 16,690.00 USD | 0.00 USD | `+57.03%` | `109.00` |
| `Live` | `Short` | `153.25` | 55,250,000.00 USD | 34,880.00 USD | 0.00 USD | `+57.13%` | `227.58` |
| `Live` | `Short` | `153.35` | 55,250,000.00 USD | 2,300.00 USD | 0.00 USD | `+57.23%` | `15.00` |
| `Live` | `Short` | `153.45` | 55,370,000.00 USD | 119,650.00 USD | 0.00 USD | `+57.33%` | `779.71` |
| `Live` | `Short` | `153.65` | 55,380,000.00 USD | 8,340.00 USD | 0.00 USD | `+57.54%` | `54.29` |
| `Live` | `Short` | `153.85` | 55,420,000.00 USD | 43,540.00 USD | 0.00 USD | `+57.74%` | `283.01` |
| `Live` | `Short` | `154.05` | 55,420,000.00 USD | 292.69 USD | 0.00 USD | `+57.95%` | `1.90` |
| `Live` | `Short` | `154.25` | 55,430,000.00 USD | 2,340.00 USD | 0.00 USD | `+58.15%` | `15.20` |
| `Live` | `Short` | `154.35` | 55,430,000.00 USD | 362.72 USD | 0.00 USD | `+58.26%` | `2.35` |
| `Live` | `Short` | `154.45` | 55,430,000.00 USD | 4,240.00 USD | 0.00 USD | `+58.36%` | `27.45` |
| `Live` | `Short` | `154.65` | 55,470,000.00 USD | 43,580.00 USD | 0.00 USD | `+58.56%` | `281.77` |
| `Live` | `Short` | `155.05` | 55,710,000.00 USD | 232,580.00 USD | 0.00 USD | `+58.97%` | `1,500.00` |
| `Live` | `Short` | `155.15` | 55,710,000.00 USD | 1,240.00 USD | 0.00 USD | `+59.08%` | `8.00` |
| `Live` | `Short` | `155.55` | 55,710,000.00 USD | 267.55 USD | 0.00 USD | `+59.49%` | `1.72` |
| `Live` | `Short` | `155.85` | 55,710,000.00 USD | 123.12 USD | 0.00 USD | `+59.79%` | `0.79` |
| `Live` | `Short` | `155.95` | 55,720,000.00 USD | 7,800.00 USD | 0.00 USD | `+59.90%` | `50.00` |
| `Live` | `Short` | `156.15` | 55,820,000.00 USD | 99,780.00 USD | 0.00 USD | `+60.10%` | `638.98` |
| `Live` | `Short` | `156.35` | 55,820,000.00 USD | 3,930.00 USD | 0.00 USD | `+60.31%` | `25.13` |
| `Live` | `Short` | `156.45` | 55,820,000.00 USD | 1,770.00 USD | 0.00 USD | `+60.41%` | `11.29` |
| `Live` | `Short` | `157.15` | 55,980,000.00 USD | 163,360.00 USD | 0.00 USD | `+61.13%` | `1,039.51` |
| `Live` | `Short` | `157.25` | 56,000,000.00 USD | 18,600.00 USD | 0.00 USD | `+61.23%` | `118.30` |
| `Live` | `Short` | `157.35` | 56,160,000.00 USD | 157,350.00 USD | 0.00 USD | `+61.33%` | `1,000.00` |
| `Live` | `Short` | `157.45` | 56,160,000.00 USD | 1,470.00 USD | 0.00 USD | `+61.43%` | `9.31` |
| `Live` | `Short` | `157.65` | 56,160,000.00 USD | 654.25 USD | 0.00 USD | `+61.64%` | `4.15` |
| `Live` | `Short` | `157.75` | 56,250,000.00 USD | 92,600.00 USD | 0.00 USD | `+61.74%` | `587.00` |
| `Live` | `Short` | `158.15` | 56,960,000.00 USD | 709,580.00 USD | 0.00 USD | `+62.15%` | `4,486.78` |
| `Live` | `Short` | `158.45` | 56,960,000.00 USD | 120.42 USD | 0.00 USD | `+62.46%` | `0.76` |
| `Live` | `Short` | `158.65` | 57,050,000.00 USD | 84,520.00 USD | 0.00 USD | `+62.66%` | `532.74` |
| `Live` | `Short` | `158.95` | 57,080,000.00 USD | 27,860.00 USD | 0.00 USD | `+62.97%` | `175.30` |
| `Live` | `Short` | `159.05` | 57,120,000.00 USD | 44,690.00 USD | 0.00 USD | `+63.07%` | `281.00` |
| `Live` | `Short` | `159.25` | 57,160,000.00 USD | 39,350.00 USD | 0.00 USD | `+63.28%` | `247.07` |
| `Live` | `Short` | `159.45` | 57,160,000.00 USD | 495.89 USD | 0.00 USD | `+63.48%` | `3.11` |
| `Live` | `Short` | `159.65` | 57,160,000.00 USD | 1,760.00 USD | 0.00 USD | `+63.69%` | `11.01` |
| `Live` | `Short` | `159.85` | 57,160,000.00 USD | 1,330.00 USD | 0.00 USD | `+63.89%` | `8.29` |
| `Live` | `Short` | `159.95` | 57,160,000.00 USD | 300.71 USD | 0.00 USD | `+64.00%` | `1.88` |
| `Live` | `Short` | `160.05` | 57,170,000.00 USD | 654.60 USD | 0.00 USD | `+64.10%` | `4.09` |
| `Live` | `Short` | `160.15` | 57,850,000.00 USD | 683,000.00 USD | 0.00 USD | `+64.20%` | `4,264.75` |
| `Live` | `Short` | `160.35` | 57,850,000.00 USD | 1,340.00 USD | 0.00 USD | `+64.41%` | `8.33` |
| `Live` | `Short` | `160.45` | 57,850,000.00 USD | 640.20 USD | 0.00 USD | `+64.51%` | `3.99` |
| `Live` | `Short` | `160.55` | 57,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+64.61%` | `6.60` |
| `Live` | `Short` | `160.95` | 57,850,000.00 USD | 260.74 USD | 0.00 USD | `+65.02%` | `1.62` |
| `Live` | `Short` | `161.05` | 57,850,000.00 USD | 2,240.00 USD | 0.00 USD | `+65.13%` | `13.93` |
| `Live` | `Short` | `161.35` | 57,860,000.00 USD | 1,530.00 USD | 0.00 USD | `+65.43%` | `9.51` |
| `Live` | `Short` | `161.55` | 57,860,000.00 USD | 410.34 USD | 0.00 USD | `+65.64%` | `2.54` |
| `Live` | `Short` | `161.75` | 58,180,000.00 USD | 323,500.00 USD | 0.00 USD | `+65.84%` | `2,000.00` |
| `Live` | `Short` | `161.95` | 58,320,000.00 USD | 144,610.00 USD | 0.00 USD | `+66.05%` | `892.95` |
| `Live` | `Short` | `162.25` | 58,320,000.00 USD | 120.06 USD | 0.00 USD | `+66.36%` | `0.74` |
| `Live` | `Short` | `162.55` | 58,470,000.00 USD | 142,940.00 USD | 0.00 USD | `+66.66%` | `879.39` |
| `Live` | `Short` | `163.55` | 58,470,000.00 USD | 3,160.00 USD | 0.00 USD | `+67.69%` | `19.33` |
| `Live` | `Short` | `163.85` | 58,470,000.00 USD | 786.48 USD | 0.00 USD | `+68.00%` | `4.80` |
| `Live` | `Short` | `163.95` | 58,490,000.00 USD | 16,950.00 USD | 0.00 USD | `+68.10%` | `103.36` |
| `Live` | `Short` | `164.45` | 58,490,000.00 USD | 822.25 USD | 0.00 USD | `+68.61%` | `5.00` |
| `Live` | `Short` | `164.65` | 58,510,000.00 USD | 16,470.00 USD | 0.00 USD | `+68.82%` | `100.00` |
| `Live` | `Short` | `164.75` | 58,710,000.00 USD | 207,840.00 USD | 0.00 USD | `+68.92%` | `1,261.56` |
| `Live` | `Short` | `165.15` | 58,710,000.00 USD | 198.18 USD | 0.00 USD | `+69.33%` | `1.20` |
| `Live` | `Short` | `165.35` | 58,790,000.00 USD | 72,750.00 USD | 0.00 USD | `+69.53%` | `440.00` |
| `Live` | `Short` | `165.45` | 58,790,000.00 USD | 827.25 USD | 0.00 USD | `+69.64%` | `5.00` |
| `Live` | `Short` | `166.25` | 58,800,000.00 USD | 14,070.00 USD | 0.00 USD | `+70.46%` | `84.61` |
| `Live` | `Short` | `166.65` | 58,870,000.00 USD | 67,790.00 USD | 0.00 USD | `+70.87%` | `406.80` |
| `Live` | `Short` | `166.75` | 58,870,000.00 USD | 3,440.00 USD | 0.00 USD | `+70.97%` | `20.63` |
| `Live` | `Short` | `166.85` | 58,900,000.00 USD | 27,020.00 USD | 0.00 USD | `+71.07%` | `161.92` |
| `Live` | `Short` | `167.65` | 58,900,000.00 USD | 115.68 USD | 0.00 USD | `+71.89%` | `0.69` |
| `Live` | `Short` | `167.75` | 58,900,000.00 USD | 1,890.00 USD | 0.00 USD | `+71.99%` | `11.27` |
| `Live` | `Short` | `167.85` | 59,000,000.00 USD | 95,710.00 USD | 0.00 USD | `+72.10%` | `570.19` |
| `Live` | `Short` | `167.95` | 59,000,000.00 USD | 122.60 USD | 0.00 USD | `+72.20%` | `0.73` |
| `Live` | `Short` | `168.25` | 59,000,000.00 USD | 1,170.00 USD | 0.00 USD | `+72.51%` | `6.95` |
| `Live` | `Short` | `168.35` | 59,020,000.00 USD | 19,740.00 USD | 0.00 USD | `+72.61%` | `117.24` |
| `Live` | `Short` | `168.65` | 59,340,000.00 USD | 325,850.00 USD | 0.00 USD | `+72.92%` | `1,932.10` |
| `Live` | `Short` | `168.75` | 59,360,000.00 USD | 20,240.00 USD | 0.00 USD | `+73.02%` | `119.95` |
| `Live` | `Short` | `169.85` | 59,360,000.00 USD | 152.87 USD | 0.00 USD | `+74.15%` | `0.90` |
| `Live` | `Short` | `171.35` | 59,550,000.00 USD | 181,940.00 USD | 0.00 USD | `+75.69%` | `1,061.79` |
| `Live` | `Short` | `171.45` | 59,550,000.00 USD | 111.44 USD | 0.00 USD | `+75.79%` | `0.65` |
| `Live` | `Short` | `172.05` | 59,550,000.00 USD | 209.90 USD | 0.00 USD | `+76.40%` | `1.22` |
| `Live` | `Short` | `172.35` | 97,460,000.00 USD | 37,920,000.00 USD | 0.00 USD | `+76.71%` | `220,000.19` |
| `Live` | `Short` | `172.45` | 97,520,000.00 USD | 51,730.00 USD | 0.00 USD | `+76.81%` | `300.00` |
| `Live` | `Short` | `172.55` | 97,640,000.00 USD | 124,210.00 USD | 0.00 USD | `+76.92%` | `719.84` |
| `Live` | `Short` | `172.65` | 97,640,000.00 USD | 3,570.00 USD | 0.00 USD | `+77.02%` | `20.70` |
| `Live` | `Short` | `172.75` | 98,650,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+77.12%` | `5,807.37` |
| `Live` | `Short` | `172.85` | 98,670,000.00 USD | 20,150.00 USD | 0.00 USD | `+77.22%` | `116.57` |
| `Live` | `Short` | `173.35` | 98,700,000.00 USD | 35,670.00 USD | 0.00 USD | `+77.74%` | `205.77` |
| `Live` | `Short` | `173.45` | 98,720,000.00 USD | 16,540.00 USD | 0.00 USD | `+77.84%` | `95.36` |
| `Live` | `Short` | `173.55` | 104,880,000.00 USD | 6,170,000.00 USD | 0.00 USD | `+77.94%` | `35,529.12` |
| `Live` | `Short` | `173.75` | 104,890,000.00 USD | 4,340.00 USD | 0.00 USD | `+78.15%` | `25.00` |
| `Live` | `Short` | `173.85` | 104,890,000.00 USD | 695.40 USD | 0.00 USD | `+78.25%` | `4.00` |
| `Live` | `Short` | `173.95` | 104,990,000.00 USD | 104,370.00 USD | 0.00 USD | `+78.35%` | `600.00` |
| `Live` | `Short` | `174.05` | 105,100,000.00 USD | 104,430.00 USD | 0.00 USD | `+78.45%` | `600.00` |
| `Live` | `Short` | `174.25` | 105,340,000.00 USD | 245,660.00 USD | 0.00 USD | `+78.66%` | `1,409.81` |
| `Live` | `Short` | `174.35` | 105,550,000.00 USD | 205,490.00 USD | 0.00 USD | `+78.76%` | `1,178.60` |
| `Live` | `Short` | `174.75` | 105,550,000.00 USD | 146.79 USD | 0.00 USD | `+79.17%` | `0.84` |
| `Live` | `Short` | `175.05` | 105,550,000.00 USD | 388.61 USD | 0.00 USD | `+79.48%` | `2.22` |
| `Live` | `Short` | `175.25` | 105,690,000.00 USD | 140,200.00 USD | 0.00 USD | `+79.68%` | `800.00` |
| `Live` | `Short` | `175.35` | 105,690,000.00 USD | 119.24 USD | 0.00 USD | `+79.79%` | `0.68` |
| `Live` | `Short` | `175.75` | 105,690,000.00 USD | 263.62 USD | 0.00 USD | `+80.20%` | `1.50` |
| `Live` | `Short` | `176.15` | 105,690,000.00 USD | 1,940.00 USD | 0.00 USD | `+80.61%` | `11.00` |
| `Live` | `Short` | `176.25` | 105,690,000.00 USD | 625.69 USD | 0.00 USD | `+80.71%` | `3.55` |
| `Live` | `Short` | `176.55` | 105,720,000.00 USD | 24,890.00 USD | 0.00 USD | `+81.02%` | `140.96` |
| `Live` | `Short` | `176.75` | 105,730,000.00 USD | 11,950.00 USD | 0.00 USD | `+81.22%` | `67.60` |
| `Live` | `Short` | `176.95` | 105,780,000.00 USD | 48,820.00 USD | 0.00 USD | `+81.43%` | `275.89` |
| `Live` | `Short` | `177.05` | 105,780,000.00 USD | 1,020.00 USD | 0.00 USD | `+81.53%` | `5.78` |
| `Live` | `Short` | `177.25` | 105,780,000.00 USD | 129.39 USD | 0.00 USD | `+81.74%` | `0.73` |
| `Live` | `Short` | `177.35` | 105,820,000.00 USD | 44,360.00 USD | 0.00 USD | `+81.84%` | `250.10` |
| `Live` | `Short` | `177.45` | 105,900,000.00 USD | 70,980.00 USD | 0.00 USD | `+81.94%` | `400.00` |
| `Live` | `Short` | `177.95` | 105,970,000.00 USD | 78,300.00 USD | 0.00 USD | `+82.45%` | `440.00` |
| `Live` | `Short` | `178.25` | 105,990,000.00 USD | 12,130.00 USD | 0.00 USD | `+82.76%` | `68.06` |
| `Live` | `Short` | `179.05` | 106,100,000.00 USD | 115,690.00 USD | 0.00 USD | `+83.58%` | `646.12` |
| `Live` | `Short` | `179.15` | 106,370,000.00 USD | 268,730.00 USD | 0.00 USD | `+83.68%` | `1,500.00` |
| `Live` | `Short` | `179.35` | 106,370,000.00 USD | 473.48 USD | 0.00 USD | `+83.89%` | `2.64` |
| `Live` | `Short` | `179.45` | 106,370,000.00 USD | 1,350.00 USD | 0.00 USD | `+83.99%` | `7.52` |
| `Live` | `Short` | `179.75` | 106,370,000.00 USD | 154.59 USD | 0.00 USD | `+84.30%` | `0.86` |
| `Live` | `Short` | `180.55` | 106,380,000.00 USD | 3,970.00 USD | 0.00 USD | `+85.12%` | `22.01` |
| `Live` | `Short` | `180.65` | 106,740,000.00 USD | 361,300.00 USD | 0.00 USD | `+85.22%` | `2,000.00` |
| `Live` | `Short` | `180.75` | 106,740,000.00 USD | 146.41 USD | 0.00 USD | `+85.32%` | `0.81` |
| `Live` | `Short` | `181.45` | 106,760,000.00 USD | 18,140.00 USD | 0.00 USD | `+86.04%` | `100.00` |
| `Live` | `Short` | `181.55` | 106,760,000.00 USD | 254.17 USD | 0.00 USD | `+86.14%` | `1.40` |
| `Live` | `Short` | `182.15` | 106,760,000.00 USD | 3,990.00 USD | 0.00 USD | `+86.76%` | `21.93` |
| `Live` | `Short` | `182.55` | 106,760,000.00 USD | 2,060.00 USD | 0.00 USD | `+87.17%` | `11.28` |
| `Live` | `Short` | `182.85` | 106,760,000.00 USD | 618.03 USD | 0.00 USD | `+87.48%` | `3.38` |
| `Live` | `Short` | `183.25` | 106,770,000.00 USD | 2,860.00 USD | 0.00 USD | `+87.89%` | `15.62` |
| `Live` | `Short` | `183.45` | 106,770,000.00 USD | 7,600.00 USD | 0.00 USD | `+88.09%` | `41.43` |
| `Live` | `Short` | `184.25` | 106,770,000.00 USD | 1,680.00 USD | 0.00 USD | `+88.91%` | `9.12` |
| `Live` | `Short` | `184.55` | 107,780,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+89.22%` | `5,464.86` |
| `Live` | `Short` | `184.95` | 107,950,000.00 USD | 165,230.00 USD | 0.00 USD | `+89.63%` | `893.35` |
| `Live` | `Short` | `185.05` | 107,950,000.00 USD | 980.76 USD | 0.00 USD | `+89.73%` | `5.30` |
| `Live` | `Short` | `185.25` | 107,950,000.00 USD | 737.29 USD | 0.00 USD | `+89.94%` | `3.98` |
| `Live` | `Short` | `185.45` | 107,950,000.00 USD | 2,770.00 USD | 0.00 USD | `+90.14%` | `14.94` |
| `Live` | `Short` | `185.65` | 107,950,000.00 USD | 384.30 USD | 0.00 USD | `+90.35%` | `2.07` |
| `Live` | `Short` | `187.15` | 107,950,000.00 USD | 671.87 USD | 0.00 USD | `+91.89%` | `3.59` |
| `Live` | `Short` | `187.25` | 107,960,000.00 USD | 2,100.00 USD | 0.00 USD | `+91.99%` | `11.24` |
| `Live` | `Short` | `187.35` | 107,970,000.00 USD | 9,690.00 USD | 0.00 USD | `+92.09%` | `51.72` |
| `Live` | `Short` | `187.85` | 107,970,000.00 USD | 1,560.00 USD | 0.00 USD | `+92.60%` | `8.32` |
| `Live` | `Short` | `188.25` | 107,970,000.00 USD | 5,340.00 USD | 0.00 USD | `+93.01%` | `28.34` |
| `Live` | `Short` | `188.35` | 107,980,000.00 USD | 2,660.00 USD | 0.00 USD | `+93.12%` | `14.12` |
| `Live` | `Short` | `188.55` | 107,980,000.00 USD | 231.92 USD | 0.00 USD | `+93.32%` | `1.23` |
| `Live` | `Short` | `188.75` | 108,260,000.00 USD | 283,050.00 USD | 0.00 USD | `+93.53%` | `1,499.60` |
| `Live` | `Short` | `188.95` | 108,260,000.00 USD | 1,450.00 USD | 0.00 USD | `+93.73%` | `7.69` |
| `Live` | `Short` | `189.25` | 108,260,000.00 USD | 456.09 USD | 0.00 USD | `+94.04%` | `2.41` |
| `Live` | `Short` | `189.65` | 108,640,000.00 USD | 379,420.00 USD | 0.00 USD | `+94.45%` | `2,000.62` |
| `Live` | `Short` | `189.75` | 108,680,000.00 USD | 37,950.00 USD | 0.00 USD | `+94.55%` | `200.00` |
| `Live` | `Short` | `189.85` | 108,900,000.00 USD | 225,680.00 USD | 0.00 USD | `+94.65%` | `1,188.73` |
| `Live` | `Short` | `189.95` | 109,190,000.00 USD | 284,930.00 USD | 0.00 USD | `+94.76%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 109,190,000.00 USD | 1,330.00 USD | 0.00 USD | `+94.96%` | `7.00` |
| `Live` | `Short` | `190.55` | 109,190,000.00 USD | 259.15 USD | 0.00 USD | `+95.37%` | `1.36` |
| `Live` | `Short` | `190.65` | 109,360,000.00 USD | 166,600.00 USD | 0.00 USD | `+95.47%` | `873.83` |
| `Live` | `Short` | `190.95` | 122,920,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+95.78%` | `71,044.42` |
| `Live` | `Short` | `191.25` | 122,920,000.00 USD | 175.95 USD | 0.00 USD | `+96.09%` | `0.92` |
| `Live` | `Short` | `191.45` | 122,920,000.00 USD | 1,370.00 USD | 0.00 USD | `+96.29%` | `7.13` |
| `Live` | `Short` | `191.55` | 122,930,000.00 USD | 2,910.00 USD | 0.00 USD | `+96.40%` | `15.17` |
| `Live` | `Short` | `191.75` | 122,930,000.00 USD | 253.11 USD | 0.00 USD | `+96.60%` | `1.32` |
| `Live` | `Short` | `191.95` | 122,930,000.00 USD | 322.48 USD | 0.00 USD | `+96.81%` | `1.68` |
| `Live` | `Short` | `192.55` | 123,730,000.00 USD | 799,080.00 USD | 0.00 USD | `+97.42%` | `4,150.00` |
| `Live` | `Short` | `193.15` | 123,730,000.00 USD | 3,980.00 USD | 0.00 USD | `+98.04%` | `20.60` |
| `Live` | `Short` | `193.35` | 123,730,000.00 USD | 378.97 USD | 0.00 USD | `+98.24%` | `1.96` |
| `Live` | `Short` | `193.55` | 123,850,000.00 USD | 115,120.00 USD | 0.00 USD | `+98.45%` | `594.80` |
| `Live` | `Short` | `193.95` | 123,990,000.00 USD | 140,910.00 USD | 0.00 USD | `+98.86%` | `726.51` |
| `Live` | `Short` | `194.15` | 124,080,000.00 USD | 88,880.00 USD | 0.00 USD | `+99.06%` | `457.80` |
| `Live` | `Short` | `194.55` | 124,080,000.00 USD | 8,670.00 USD | 0.00 USD | `+99.47%` | `44.54` |
| `Live` | `Short` | `194.75` | 124,110,000.00 USD | 20,290.00 USD | 0.00 USD | `+99.68%` | `104.17` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 9,810,000.00 USD | 0.00 USD | 14,030.00 USD | `-76.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 9,790,000.00 USD | 0.00 USD | 3,760.00 USD | `-74.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.15` | 9,790,000.00 USD | 0.00 USD | 103.82 USD | `-73.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 9,790,000.00 USD | 0.00 USD | 519.56 USD | `-69.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 9,790,000.00 USD | 0.00 USD | 499.56 USD | `-68.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 9,790,000.00 USD | 0.00 USD | 818.32 USD | `-66.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 9,790,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 9,790,000.00 USD | 0.00 USD | 201.74 USD | `-61.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 9,790,000.00 USD | 0.00 USD | 150.30 USD | `-60.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.65` | 9,790,000.00 USD | 0.00 USD | 206.00 USD | `-60.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 9,790,000.00 USD | 0.00 USD | 208.14 USD | `-59.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 9,790,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 9,780,000.00 USD | 0.00 USD | 157.01 USD | `-59.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 9,780,000.00 USD | 0.00 USD | 583.13 USD | `-58.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 9,780,000.00 USD | 0.00 USD | 121.81 USD | `-56.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 9,780,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 9,610,000.00 USD | 0.00 USD | 105.00 USD | `-55.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 9,610,000.00 USD | 0.00 USD | 63,450.00 USD | `-53.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 9,550,000.00 USD | 0.00 USD | 251.05 USD | `-52.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 9,550,000.00 USD | 0.00 USD | 143.25 USD | `-51.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 9,550,000.00 USD | 0.00 USD | 191.40 USD | `-50.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 9,550,000.00 USD | 0.00 USD | 103.35 USD | `-50.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 9,550,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 9,540,000.00 USD | 0.00 USD | 107.03 USD | `-48.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 9,540,000.00 USD | 0.00 USD | 102.62 USD | `-48.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 9,540,000.00 USD | 0.00 USD | 134.28 USD | `-47.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 9,540,000.00 USD | 0.00 USD | 3,950.00 USD | `-47.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 9,540,000.00 USD | 0.00 USD | 102.74 USD | `-46.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 9,540,000.00 USD | 0.00 USD | 126.12 USD | `-46.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 9,540,000.00 USD | 0.00 USD | 200.15 USD | `-45.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 9,540,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 9,510,000.00 USD | 0.00 USD | 1,980.00 USD | `-45.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 9,510,000.00 USD | 0.00 USD | 641.57 USD | `-44.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 9,510,000.00 USD | 0.00 USD | 139.87 USD | `-43.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 9,510,000.00 USD | 0.00 USD | 209.19 USD | `-43.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 9,510,000.00 USD | 0.00 USD | 894.56 USD | `-42.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 9,510,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 9,500,000.00 USD | 0.00 USD | 6,680.00 USD | `-41.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 9,500,000.00 USD | 0.00 USD | 158.48 USD | `-40.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 9,500,000.00 USD | 0.00 USD | 428.72 USD | `-40.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 9,500,000.00 USD | 0.00 USD | 236.20 USD | `-39.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 9,500,000.00 USD | 0.00 USD | 200.01 USD | `-39.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 9,500,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 9,500,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 9,490,000.00 USD | 0.00 USD | 32,240.00 USD | `-38.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 9,450,000.00 USD | 0.00 USD | 488.63 USD | `-38.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 9,450,000.00 USD | 0.00 USD | 258.90 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 9,450,000.00 USD | 0.00 USD | 6,200.00 USD | `-38.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 9,450,000.00 USD | 0.00 USD | 551.61 USD | `-37.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 9,450,000.00 USD | 0.00 USD | 18,360.00 USD | `-37.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 9,430,000.00 USD | 0.00 USD | 142.33 USD | `-37.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 9,430,000.00 USD | 0.00 USD | 100.78 USD | `-37.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 9,430,000.00 USD | 0.00 USD | 243.74 USD | `-36.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 9,430,000.00 USD | 0.00 USD | 4,640.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 9,420,000.00 USD | 0.00 USD | 136.98 USD | `-35.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 9,420,000.00 USD | 0.00 USD | 12,950.00 USD | `-35.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 9,410,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 9,410,000.00 USD | 0.00 USD | 222.55 USD | `-34.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 9,410,000.00 USD | 0.00 USD | 163.19 USD | `-34.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 9,410,000.00 USD | 0.00 USD | 129.70 USD | `-33.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 9,410,000.00 USD | 0.00 USD | 2,440.00 USD | `-33.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 9,400,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 9,400,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 9,400,000.00 USD | 0.00 USD | 9,140.00 USD | `-32.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 9,390,000.00 USD | 0.00 USD | 541.72 USD | `-31.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 9,390,000.00 USD | 0.00 USD | 335.25 USD | `-31.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 9,390,000.00 USD | 0.00 USD | 268.60 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.85` | 9,390,000.00 USD | 0.00 USD | 303.29 USD | `-30.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 9,390,000.00 USD | 0.00 USD | 195.30 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 9,390,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 9,380,000.00 USD | 0.00 USD | 359.04 USD | `-29.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 9,380,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 9,380,000.00 USD | 0.00 USD | 20,210.00 USD | `-29.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 9,360,000.00 USD | 0.00 USD | 172.18 USD | `-29.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 9,360,000.00 USD | 0.00 USD | 668.96 USD | `-29.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 9,360,000.00 USD | 0.00 USD | 107.96 USD | `-28.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 9,360,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 9,320,000.00 USD | 0.00 USD | 365.32 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 9,320,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 9,320,000.00 USD | 0.00 USD | 34,680.00 USD | `-28.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 9,280,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 9,280,000.00 USD | 0.00 USD | 562.80 USD | `-27.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 9,280,000.00 USD | 0.00 USD | 681.51 USD | `-27.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 9,270,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 9,270,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 9,270,000.00 USD | 0.00 USD | 265.02 USD | `-27.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 9,270,000.00 USD | 0.00 USD | 32,400.00 USD | `-26.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 9,230,000.00 USD | 0.00 USD | 289.37 USD | `-26.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 9,230,000.00 USD | 0.00 USD | 1,170.00 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 9,230,000.00 USD | 0.00 USD | 913.54 USD | `-26.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 9,230,000.00 USD | 0.00 USD | 2,770.00 USD | `-26.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 9,230,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 9,210,000.00 USD | 0.00 USD | 66,160.00 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 9,140,000.00 USD | 0.00 USD | 139.56 USD | `-24.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 9,140,000.00 USD | 0.00 USD | 510.95 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 9,140,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 9,140,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 9,130,000.00 USD | 0.00 USD | 331.00 USD | `-23.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 9,130,000.00 USD | 0.00 USD | 28,050.00 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 9,100,000.00 USD | 0.00 USD | 22,970.00 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,080,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,080,000.00 USD | 0.00 USD | 277.98 USD | `-22.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,080,000.00 USD | 0.00 USD | 10,650.00 USD | `-22.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,070,000.00 USD | 0.00 USD | 254.34 USD | `-21.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,070,000.00 USD | 0.00 USD | 486.47 USD | `-21.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 9,070,000.00 USD | 0.00 USD | 358.84 USD | `-21.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,070,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,060,000.00 USD | 0.00 USD | 536.55 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,060,000.00 USD | 0.00 USD | 251.74 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.95` | 9,060,000.00 USD | 0.00 USD | 320.11 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,060,000.00 USD | 0.00 USD | 3,210.00 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,060,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,050,000.00 USD | 0.00 USD | 282.96 USD | `-20.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,050,000.00 USD | 0.00 USD | 56,050.00 USD | `-19.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 8,990,000.00 USD | 0.00 USD | 494.69 USD | `-19.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 8,990,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 8,980,000.00 USD | 0.00 USD | 379.58 USD | `-19.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 8,970,000.00 USD | 0.00 USD | 4,660.00 USD | `-18.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 8,970,000.00 USD | 0.00 USD | 381.50 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 8,970,000.00 USD | 0.00 USD | 1,750.00 USD | `-18.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 8,970,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 8,960,000.00 USD | 0.00 USD | 238.95 USD | `-18.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 8,960,000.00 USD | 0.00 USD | 808.29 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 8,960,000.00 USD | 0.00 USD | 55,180.00 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 8,910,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 8,900,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 8,900,000.00 USD | 0.00 USD | 295.21 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 8,900,000.00 USD | 0.00 USD | 160.03 USD | `-16.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 8,900,000.00 USD | 0.00 USD | 1,390.00 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 8,900,000.00 USD | 0.00 USD | 71,590.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 8,830,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 8,820,000.00 USD | 0.00 USD | 684.31 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 8,820,000.00 USD | 0.00 USD | 264.34 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 8,820,000.00 USD | 0.00 USD | 2,780.00 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 8,820,000.00 USD | 0.00 USD | 12,040.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 8,810,000.00 USD | 0.00 USD | 1,320.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 8,800,000.00 USD | 0.00 USD | 6,610.00 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 8,800,000.00 USD | 0.00 USD | 239.47 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 8,800,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 8,780,000.00 USD | 0.00 USD | 405.57 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 8,780,000.00 USD | 0.00 USD | 421.09 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 8,780,000.00 USD | 0.00 USD | 1,370.00 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 8,780,000.00 USD | 0.00 USD | 1,320.00 USD | `-14.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 8,780,000.00 USD | 0.00 USD | 426.47 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 8,780,000.00 USD | 0.00 USD | 25,050.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 8,750,000.00 USD | 0.00 USD | 3,490.00 USD | `-13.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 8,750,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 8,740,000.00 USD | 0.00 USD | 165.52 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 8,740,000.00 USD | 0.00 USD | 169.95 USD | `-13.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 8,740,000.00 USD | 0.00 USD | 519.75 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 8,740,000.00 USD | 0.00 USD | 306.80 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 8,740,000.00 USD | 0.00 USD | 1,350.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 8,740,000.00 USD | 0.00 USD | 165,510.00 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 8,580,000.00 USD | 0.00 USD | 437.67 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 8,580,000.00 USD | 0.00 USD | 1,500.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 8,570,000.00 USD | 0.00 USD | 915.81 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 8,570,000.00 USD | 0.00 USD | 120.48 USD | `-12.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 8,570,000.00 USD | 0.00 USD | 105.23 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 8,570,000.00 USD | 0.00 USD | 310.05 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 8,570,000.00 USD | 0.00 USD | 142.34 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 8,570,000.00 USD | 0.00 USD | 1,370.00 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 8,570,000.00 USD | 0.00 USD | 604.23 USD | `-11.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 8,570,000.00 USD | 0.00 USD | 8,140.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 8,560,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 8,560,000.00 USD | 0.00 USD | 538.20 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 8,560,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 8,560,000.00 USD | 0.00 USD | 2,540.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 8,550,000.00 USD | 0.00 USD | 417.17 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 8,550,000.00 USD | 0.00 USD | 305.87 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 8,550,000.00 USD | 0.00 USD | 2,020.00 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 8,550,000.00 USD | 0.00 USD | 1,160.00 USD | `-10.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 8,550,000.00 USD | 0.00 USD | 132.16 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 8,550,000.00 USD | 0.00 USD | 297,900.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 8,250,000.00 USD | 0.00 USD | 435.75 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 8,250,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 8,240,000.00 USD | 0.00 USD | 436.75 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 8,240,000.00 USD | 0.00 USD | 730.21 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 8,240,000.00 USD | 0.00 USD | 316.93 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 8,240,000.00 USD | 0.00 USD | 2,880.00 USD | `-10.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 8,240,000.00 USD | 0.00 USD | 177.66 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 8,240,000.00 USD | 0.00 USD | 88,070.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 8,150,000.00 USD | 0.00 USD | 1,050.00 USD | `-9.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 8,150,000.00 USD | 0.00 USD | 8,860.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 8,140,000.00 USD | 0.00 USD | 29,150.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 8,110,000.00 USD | 0.00 USD | 1,010.00 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 8,110,000.00 USD | 0.00 USD | 7,610.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 8,100,000.00 USD | 0.00 USD | 27,220.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 8,080,000.00 USD | 0.00 USD | 53,250.00 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 8,020,000.00 USD | 0.00 USD | 95,650.00 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 7,930,000.00 USD | 0.00 USD | 141.43 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 7,930,000.00 USD | 0.00 USD | 8,910.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 7,920,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 7,910,000.00 USD | 0.00 USD | 960.33 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 7,910,000.00 USD | 0.00 USD | 615.62 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 7,910,000.00 USD | 0.00 USD | 13,620.00 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 7,900,000.00 USD | 0.00 USD | 348.35 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 7,900,000.00 USD | 0.00 USD | 173.02 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 7,900,000.00 USD | 0.00 USD | 105.01 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 7,900,000.00 USD | 0.00 USD | 20,850.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 7,870,000.00 USD | 0.00 USD | 86,920.00 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 7,790,000.00 USD | 0.00 USD | 619,060.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 7,170,000.00 USD | 0.00 USD | 180.30 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 7,170,000.00 USD | 0.00 USD | 13,600.00 USD | `-7.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 7,150,000.00 USD | 0.00 USD | 4,900.00 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 7,150,000.00 USD | 0.00 USD | 2,670.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 7,150,000.00 USD | 0.00 USD | 663.56 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 7,150,000.00 USD | 0.00 USD | 17,680.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 7,130,000.00 USD | 0.00 USD | 13,930.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 7,110,000.00 USD | 0.00 USD | 12,670.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 7,100,000.00 USD | 0.00 USD | 69,530.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 7,030,000.00 USD | 0.00 USD | 975.30 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 7,030,000.00 USD | 0.00 USD | 5,560.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 7,030,000.00 USD | 0.00 USD | 5,840.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 7,020,000.00 USD | 0.00 USD | 800.19 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 7,020,000.00 USD | 0.00 USD | 343,420.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 6,680,000.00 USD | 0.00 USD | 27,950.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 6,650,000.00 USD | 0.00 USD | 2,450.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 6,650,000.00 USD | 0.00 USD | 41,740.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 6,600,000.00 USD | 0.00 USD | 19,310.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 6,580,000.00 USD | 0.00 USD | 58,660.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 6,530,000.00 USD | 0.00 USD | 2,030.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 6,520,000.00 USD | 0.00 USD | 139.30 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 6,520,000.00 USD | 0.00 USD | 18,080.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 6,510,000.00 USD | 0.00 USD | 5,680.00 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 6,500,000.00 USD | 0.00 USD | 8,020.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 6,490,000.00 USD | 0.00 USD | 12,220.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 6,480,000.00 USD | 0.00 USD | 11,740.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 6,470,000.00 USD | 0.00 USD | 28,600.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 6,440,000.00 USD | 0.00 USD | 61,570.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 6,380,000.00 USD | 0.00 USD | 75,070.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 6,300,000.00 USD | 0.00 USD | 712.60 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 6,300,000.00 USD | 0.00 USD | 8,970.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 6,290,000.00 USD | 0.00 USD | 1,160.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 6,290,000.00 USD | 0.00 USD | 94,000.00 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 6,200,000.00 USD | 0.00 USD | 570,010.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 5,630,000.00 USD | 0.00 USD | 440,480.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 5,190,000.00 USD | 0.00 USD | 11,210.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 5,180,000.00 USD | 0.00 USD | 106,140.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 5,070,000.00 USD | 0.00 USD | 41,100.00 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 5,030,000.00 USD | 0.00 USD | 537,630.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 4,490,000.00 USD | 0.00 USD | 10,920.00 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 4,480,000.00 USD | 0.00 USD | 16,530.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 4,460,000.00 USD | 0.00 USD | 7,050.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 4,460,000.00 USD | 0.00 USD | 49,310.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 4,410,000.00 USD | 0.00 USD | 47,400.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 4,360,000.00 USD | 0.00 USD | 22,420.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 4,340,000.00 USD | 0.00 USD | 53,460.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 4,280,000.00 USD | 0.00 USD | 2,020,000.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 2,260,000.00 USD | 0.00 USD | 24,650.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 2,240,000.00 USD | 0.00 USD | 191,120.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 2,050,000.00 USD | 0.00 USD | 44,760.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 2,000,000.00 USD | 0.00 USD | 10,110.00 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 1,990,000.00 USD | 0.00 USD | 33,810.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 1,960,000.00 USD | 0.00 USD | 7,660.00 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 1,950,000.00 USD | 0.00 USD | 4,570.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 1,940,000.00 USD | 0.00 USD | 7,030.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 1,940,000.00 USD | 0.00 USD | 11,060.00 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 1,930,000.00 USD | 0.00 USD | 134.19 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 1,930,000.00 USD | 0.00 USD | 7,860.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 1,920,000.00 USD | 0.00 USD | 69,090.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 1,850,000.00 USD | 0.00 USD | 110,470.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 1,740,000.00 USD | 0.00 USD | 7,650.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 1,730,000.00 USD | 0.00 USD | 767.91 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 1,730,000.00 USD | 0.00 USD | 268,560.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 1,460,000.00 USD | 0.00 USD | 83,580.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 1,380,000.00 USD | 0.00 USD | 9,950.00 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 1,370,000.00 USD | 0.00 USD | 41,780.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 1,330,000.00 USD | 0.00 USD | 195,810.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 1,130,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 120,580.00 USD | 0.00 USD | 71,680.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 48,900.00 USD | 0.00 USD | 8,170.00 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.25` | 40,730.00 USD | 0.00 USD | 26,700.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.35` | 14,030.00 USD | 0.00 USD | 12,170.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.45` | 1,860.00 USD | 0.00 USD | 1,860.00 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 7,060.00 USD | 7,060.00 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 86,900.00 USD | 79,840.00 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 87,290.00 USD | 391.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 93,170.00 USD | 5,880.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 100,230.00 USD | 7,070.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 108,830.00 USD | 8,600.00 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 112,210.00 USD | 3,380.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 115,330.00 USD | 3,110.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 119,560.00 USD | 4,230.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 208,230.00 USD | 88,670.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 248,250.00 USD | 40,030.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 355,630.00 USD | 107,380.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 383,090.00 USD | 27,450.00 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 384,470.00 USD | 1,380.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 386,540.00 USD | 2,070.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 595,660.00 USD | 209,120.00 USD | 0.00 USD | `+1.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 602,000.00 USD | 6,330.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 602,110.00 USD | 113.15 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 609,790.00 USD | 7,680.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 611,690.00 USD | 1,910.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 615,300.00 USD | 3,610.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 616,270.00 USD | 970.59 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 626,170.00 USD | 9,900.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 629,260.00 USD | 3,100.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 633,680.00 USD | 4,420.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 707,600.00 USD | 73,920.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 714,160.00 USD | 6,560.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 729,360.00 USD | 15,200.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 734,110.00 USD | 4,750.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 734,910.00 USD | 800.59 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 735,230.00 USD | 313.72 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 735,390.00 USD | 165.07 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 735,600.00 USD | 202.51 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 736,300.00 USD | 703.93 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 739,100.00 USD | 2,800.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 1,270,000.00 USD | 534,200.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 1,350,000.00 USD | 72,690.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 1,350,000.00 USD | 3,080.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 1,360,000.00 USD | 10,250.00 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 1,370,000.00 USD | 7,070.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 1,400,000.00 USD | 38,380.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 1,400,000.00 USD | 116.90 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 1,410,000.00 USD | 863.86 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 1,410,000.00 USD | 1,470.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 1,410,000.00 USD | 1,120.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,480,000.00 USD | 68,860.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 1,490,000.00 USD | 17,560.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 1,500,000.00 USD | 5,170.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 2,160,000.00 USD | 656,670.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 2,170,000.00 USD | 12,690.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 2,200,000.00 USD | 35,120.00 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 2,210,000.00 USD | 10,450.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 2,220,000.00 USD | 1,810.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 2,240,000.00 USD | 21,080.00 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 2,240,000.00 USD | 3,430.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 2,280,000.00 USD | 43,520.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 2,450,000.00 USD | 166,600.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 2,560,000.00 USD | 109,970.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 2,570,000.00 USD | 8,580.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 2,570,000.00 USD | 3,760.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 2,580,000.00 USD | 7,280.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 2,580,000.00 USD | 2,660.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 2,600,000.00 USD | 17,460.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 2,850,000.00 USD | 246,130.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 2,910,000.00 USD | 59,260.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 2,920,000.00 USD | 18,170.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 2,930,000.00 USD | 1,980.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 2,930,000.00 USD | 733.92 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 2,930,000.00 USD | 146.09 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 2,930,000.00 USD | 5,400.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 2,950,000.00 USD | 15,280.00 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 2,970,000.00 USD | 21,730.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 2,970,000.00 USD | 1,100.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 2,980,000.00 USD | 5,900.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 3,000,000.00 USD | 25,930.00 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 3,060,000.00 USD | 59,180.00 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 3,090,000.00 USD | 27,500.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 3,090,000.00 USD | 1,210.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 3,090,000.00 USD | 1,110.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 3,090,000.00 USD | 1,680.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 3,100,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 3,100,000.00 USD | 235.60 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 3,110,000.00 USD | 10,860.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 3,120,000.00 USD | 11,960.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 3,120,000.00 USD | 101.71 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 3,170,000.00 USD | 46,190.00 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 3,180,000.00 USD | 9,970.00 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 3,180,000.00 USD | 935.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 3,260,000.00 USD | 82,230.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 3,290,000.00 USD | 26,280.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 3,290,000.00 USD | 8,020.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 3,290,000.00 USD | 355.14 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 3,400,000.00 USD | 110,390.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 3,410,000.00 USD | 1,000.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 3,440,000.00 USD | 29,910.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 3,450,000.00 USD | 17,970.00 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 3,450,000.00 USD | 1,200.00 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 3,470,000.00 USD | 20,190.00 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 3,480,000.00 USD | 698.85 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 3,480,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 3,540,000.00 USD | 58,100.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 3,610,000.00 USD | 72,030.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 3,610,000.00 USD | 164.86 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 3,620,000.00 USD | 4,420.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 3,620,000.00 USD | 930.53 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 3,680,000.00 USD | 63,540.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 3,750,000.00 USD | 68,190.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.25` | 3,750,000.00 USD | 1,240.00 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 3,770,000.00 USD | 15,750.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 3,770,000.00 USD | 4,500.00 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 3,790,000.00 USD | 16,860.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 3,790,000.00 USD | 2,310.00 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 3,790,000.00 USD | 2,120.00 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 3,800,000.00 USD | 3,260.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 3,840,000.00 USD | 42,240.00 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 3,860,000.00 USD | 21,010.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 3,870,000.00 USD | 8,620.00 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 7,940,000.00 USD | 4,070,000.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 7,980,000.00 USD | 44,780.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 8,000,000.00 USD | 19,080.00 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 8,000,000.00 USD | 1,170.00 USD | 0.00 USD | `+12.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 8,010,000.00 USD | 5,300.00 USD | 0.00 USD | `+12.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 8,010,000.00 USD | 4,370.00 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 8,020,000.00 USD | 1,210.00 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 8,020,000.00 USD | 583.83 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 8,510,000.00 USD | 493,530.00 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 8,510,000.00 USD | 340.36 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 8,520,000.00 USD | 6,610.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 8,520,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 8,520,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 8,530,000.00 USD | 10,820.00 USD | 0.00 USD | `+13.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 8,530,000.00 USD | 3,030.00 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 8,550,000.00 USD | 17,520.00 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 8,780,000.00 USD | 227,610.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 8,780,000.00 USD | 799.56 USD | 0.00 USD | `+13.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 8,780,000.00 USD | 1,300.00 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 8,790,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 8,790,000.00 USD | 842.56 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 8,790,000.00 USD | 5,780.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 8,790,000.00 USD | 106.07 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 8,810,000.00 USD | 13,510.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 8,810,000.00 USD | 2,100.00 USD | 0.00 USD | `+14.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.95` | 8,810,000.00 USD | 559.75 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 8,830,000.00 USD | 17,410.00 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 8,880,000.00 USD | 49,680.00 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 8,880,000.00 USD | 4,960.00 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 8,890,000.00 USD | 4,920.00 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 8,890,000.00 USD | 2,290.00 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 8,920,000.00 USD | 36,280.00 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 8,930,000.00 USD | 1,690.00 USD | 0.00 USD | `+15.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 8,930,000.00 USD | 586.82 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 9,010,000.00 USD | 81,750.00 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.15` | 9,010,000.00 USD | 427.71 USD | 0.00 USD | `+16.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 9,010,000.00 USD | 349.94 USD | 0.00 USD | `+16.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 9,140,000.00 USD | 128,070.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 9,140,000.00 USD | 655.74 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 9,160,000.00 USD | 25,440.00 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 9,160,000.00 USD | 230.71 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 9,160,000.00 USD | 257.07 USD | 0.00 USD | `+16.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 9,170,000.00 USD | 5,140.00 USD | 0.00 USD | `+16.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 9,170,000.00 USD | 1,970.00 USD | 0.00 USD | `+16.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 9,180,000.00 USD | 11,410.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 9,180,000.00 USD | 584.96 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 9,190,000.00 USD | 9,320.00 USD | 0.00 USD | `+17.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 9,190,000.00 USD | 343.35 USD | 0.00 USD | `+17.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 9,200,000.00 USD | 5,150.00 USD | 0.00 USD | `+17.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 9,210,000.00 USD | 11,800.00 USD | 0.00 USD | `+17.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 9,210,000.00 USD | 1,010.00 USD | 0.00 USD | `+17.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 9,210,000.00 USD | 2,750.00 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 9,300,000.00 USD | 81,650.00 USD | 0.00 USD | `+17.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 9,300,000.00 USD | 448.71 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 9,320,000.00 USD | 23,260.00 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 9,320,000.00 USD | 2,210.00 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 9,320,000.00 USD | 579.25 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 9,340,000.00 USD | 20,280.00 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 9,340,000.00 USD | 1,730.00 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 9,350,000.00 USD | 3,840.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 9,350,000.00 USD | 4,160.00 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 9,360,000.00 USD | 10,810.00 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 9,360,000.00 USD | 1,100.00 USD | 0.00 USD | `+19.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 9,370,000.00 USD | 3,580.00 USD | 0.00 USD | `+19.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 9,370,000.00 USD | 234.87 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 9,370,000.00 USD | 1,170.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 9,370,000.00 USD | 4,990.00 USD | 0.00 USD | `+20.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 9,370,000.00 USD | 686.50 USD | 0.00 USD | `+20.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 9,370,000.00 USD | 349.40 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 9,380,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 9,480,000.00 USD | 98,960.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 9,580,000.00 USD | 105,720.00 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 9,590,000.00 USD | 5,920.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 9,640,000.00 USD | 55,580.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 9,710,000.00 USD | 71,690.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 9,730,000.00 USD | 13,120.00 USD | 0.00 USD | `+21.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 9,730,000.00 USD | 2,830.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 9,740,000.00 USD | 12,610.00 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 9,740,000.00 USD | 707.15 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 9,820,000.00 USD | 70,980.00 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 9,820,000.00 USD | 593.25 USD | 0.00 USD | `+21.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 9,820,000.00 USD | 403.75 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 9,830,000.00 USD | 15,940.00 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 9,870,000.00 USD | 42,290.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 9,930,000.00 USD | 54,610.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 9,940,000.00 USD | 8,120.00 USD | 0.00 USD | `+22.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 9,940,000.00 USD | 2,050.00 USD | 0.00 USD | `+22.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 9,940,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 9,950,000.00 USD | 3,580.00 USD | 0.00 USD | `+22.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 9,950,000.00 USD | 615.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 10,070,000.00 USD | 125,500.00 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 10,110,000.00 USD | 37,630.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 10,110,000.00 USD | 458.21 USD | 0.00 USD | `+22.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 10,250,000.00 USD | 139,510.00 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 10,250,000.00 USD | 414.52 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 10,250,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 10,260,000.00 USD | 7,850.00 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 10,260,000.00 USD | 184.29 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 10,260,000.00 USD | 964.40 USD | 0.00 USD | `+23.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 10,260,000.00 USD | 191.83 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 10,270,000.00 USD | 2,150.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 10,270,000.00 USD | 650.17 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 10,290,000.00 USD | 20,950.00 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 10,290,000.00 USD | 122.36 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 10,300,000.00 USD | 8,780.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 10,310,000.00 USD | 11,570.00 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 10,320,000.00 USD | 7,860.00 USD | 0.00 USD | `+24.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 10,320,000.00 USD | 4,360.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 10,320,000.00 USD | 2,450.00 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 10,330,000.00 USD | 7,600.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 10,340,000.00 USD | 12,910.00 USD | 0.00 USD | `+25.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 10,540,000.00 USD | 195,460.00 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 10,540,000.00 USD | 2,690.00 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 10,780,000.00 USD | 235,280.00 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 10,830,000.00 USD | 52,330.00 USD | 0.00 USD | `+25.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 10,830,000.00 USD | 5,060.00 USD | 0.00 USD | `+25.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 10,840,000.00 USD | 7,020.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 10,850,000.00 USD | 11,000.00 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 10,850,000.00 USD | 235.68 USD | 0.00 USD | `+25.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 10,860,000.00 USD | 3,780.00 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 10,870,000.00 USD | 11,200.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 11,870,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+26.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 11,870,000.00 USD | 252.46 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 11,880,000.00 USD | 7,710.00 USD | 0.00 USD | `+26.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 11,880,000.00 USD | 6,790.00 USD | 0.00 USD | `+26.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 11,890,000.00 USD | 2,670.00 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 11,890,000.00 USD | 632.58 USD | 0.00 USD | `+26.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 11,900,000.00 USD | 11,600.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 11,910,000.00 USD | 11,530.00 USD | 0.00 USD | `+26.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 11,930,000.00 USD | 18,820.00 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 12,000,000.00 USD | 68,330.00 USD | 0.00 USD | `+27.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 12,000,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 12,000,000.00 USD | 151.59 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 12,000,000.00 USD | 4,110.00 USD | 0.00 USD | `+27.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 12,010,000.00 USD | 1,370.00 USD | 0.00 USD | `+27.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 12,010,000.00 USD | 7,330.00 USD | 0.00 USD | `+27.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 12,020,000.00 USD | 7,280.00 USD | 0.00 USD | `+27.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 12,020,000.00 USD | 344.59 USD | 0.00 USD | `+28.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 12,030,000.00 USD | 11,310.00 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 12,570,000.00 USD | 536,280.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 12,570,000.00 USD | 178.96 USD | 0.00 USD | `+28.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 12,570,000.00 USD | 311.87 USD | 0.00 USD | `+28.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 12,570,000.00 USD | 1,310.00 USD | 0.00 USD | `+28.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 12,570,000.00 USD | 3,320.00 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 12,590,000.00 USD | 16,280.00 USD | 0.00 USD | `+28.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 12,590,000.00 USD | 471.94 USD | 0.00 USD | `+29.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 12,590,000.00 USD | 209.08 USD | 0.00 USD | `+29.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 12,740,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 12,750,000.00 USD | 12,800.00 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 12,750,000.00 USD | 187.15 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 12,760,000.00 USD | 3,550.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 12,760,000.00 USD | 6,100.00 USD | 0.00 USD | `+29.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 12,950,000.00 USD | 190,580.00 USD | 0.00 USD | `+30.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 12,950,000.00 USD | 534.87 USD | 0.00 USD | `+30.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 12,960,000.00 USD | 4,290.00 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 12,960,000.00 USD | 5,000.00 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 12,960,000.00 USD | 362.81 USD | 0.00 USD | `+30.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 13,030,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 13,030,000.00 USD | 482.37 USD | 0.00 USD | `+31.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 13,070,000.00 USD | 48,740.00 USD | 0.00 USD | `+31.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 13,080,000.00 USD | 3,010.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 13,080,000.00 USD | 191.09 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.85` | 13,080,000.00 USD | 132.72 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 13,090,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 13,140,000.00 USD | 50,720.00 USD | 0.00 USD | `+32.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 13,160,000.00 USD | 15,330.00 USD | 0.00 USD | `+32.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 13,160,000.00 USD | 401.29 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 13,160,000.00 USD | 1,320.00 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 13,160,000.00 USD | 152.99 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 13,160,000.00 USD | 1,040.00 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 13,160,000.00 USD | 116.87 USD | 0.00 USD | `+33.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 13,190,000.00 USD | 26,350.00 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 13,190,000.00 USD | 1,760.00 USD | 0.00 USD | `+33.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 13,190,000.00 USD | 4,090.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 13,190,000.00 USD | 192.06 USD | 0.00 USD | `+33.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 13,200,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 13,200,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 13,210,000.00 USD | 10,140.00 USD | 0.00 USD | `+34.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 13,210,000.00 USD | 6,000.00 USD | 0.00 USD | `+34.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 13,220,000.00 USD | 5,950.00 USD | 0.00 USD | `+34.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 13,230,000.00 USD | 6,160.00 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 13,390,000.00 USD | 160,920.00 USD | 0.00 USD | `+34.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 13,390,000.00 USD | 144.93 USD | 0.00 USD | `+35.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 13,410,000.00 USD | 24,010.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 13,410,000.00 USD | 397.95 USD | 0.00 USD | `+36.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 13,420,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 13,420,000.00 USD | 3,910.00 USD | 0.00 USD | `+36.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 13,430,000.00 USD | 6,700.00 USD | 0.00 USD | `+36.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 13,430,000.00 USD | 509.96 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 13,430,000.00 USD | 191.88 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 13,430,000.00 USD | 237.36 USD | 0.00 USD | `+36.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 13,430,000.00 USD | 1,210.00 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 13,430,000.00 USD | 192.46 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 13,430,000.00 USD | 112.35 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 13,440,000.00 USD | 4,150.00 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 13,490,000.00 USD | 54,080.00 USD | 0.00 USD | `+37.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 13,490,000.00 USD | 331.60 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 13,690,000.00 USD | 195,540.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 13,690,000.00 USD | 647.28 USD | 0.00 USD | `+38.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 13,750,000.00 USD | 57,060.00 USD | 0.00 USD | `+38.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 13,750,000.00 USD | 7,560.00 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 13,760,000.00 USD | 1,890.00 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 13,760,000.00 USD | 192.25 USD | 0.00 USD | `+39.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 13,760,000.00 USD | 465.29 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 13,760,000.00 USD | 389.17 USD | 0.00 USD | `+40.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 13,760,000.00 USD | 826.57 USD | 0.00 USD | `+40.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 13,760,000.00 USD | 1,330.00 USD | 0.00 USD | `+40.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 13,760,000.00 USD | 2,910.00 USD | 0.00 USD | `+40.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 13,770,000.00 USD | 3,920.00 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 13,790,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 13,790,000.00 USD | 133.62 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 13,810,000.00 USD | 18,910.00 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 13,810,000.00 USD | 692.25 USD | 0.00 USD | `+41.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 13,810,000.00 USD | 406.24 USD | 0.00 USD | `+42.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 20,550,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+42.36%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 20,560,000.00 USD | 826.75 USD | 0.00 USD | `+42.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 22,760,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+42.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 22,760,000.00 USD | 7,530.00 USD | 0.00 USD | `+43.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 22,860,000.00 USD | 94,590.00 USD | 0.00 USD | `+43.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 22,960,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 22,960,000.00 USD | 990.88 USD | 0.00 USD | `+44.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 22,960,000.00 USD | 3,510.00 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 22,970,000.00 USD | 6,190.00 USD | 0.00 USD | `+44.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 22,970,000.00 USD | 796.07 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 22,970,000.00 USD | 826.73 USD | 0.00 USD | `+45.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 22,970,000.00 USD | 278.56 USD | 0.00 USD | `+46.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 23,320,000.00 USD | 346,420.00 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 23,530,000.00 USD | 215,510.00 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 23,530,000.00 USD | 528.96 USD | 0.00 USD | `+46.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 23,540,000.00 USD | 6,330.00 USD | 0.00 USD | `+47.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 23,540,000.00 USD | 415.44 USD | 0.00 USD | `+47.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 23,820,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 23,830,000.00 USD | 7,260.00 USD | 0.00 USD | `+48.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 23,830,000.00 USD | 791.78 USD | 0.00 USD | `+48.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 23,850,000.00 USD | 19,140.00 USD | 0.00 USD | `+48.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 23,850,000.00 USD | 209.16 USD | 0.00 USD | `+48.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 23,850,000.00 USD | 698.64 USD | 0.00 USD | `+49.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 24,040,000.00 USD | 190,100.00 USD | 0.00 USD | `+49.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 24,040,000.00 USD | 3,300.00 USD | 0.00 USD | `+49.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 24,040,000.00 USD | 1,020.00 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 24,050,000.00 USD | 1,500.00 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 24,080,000.00 USD | 37,700.00 USD | 0.00 USD | `+50.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 24,080,000.00 USD | 844.89 USD | 0.00 USD | `+51.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 24,090,000.00 USD | 4,610.00 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 24,090,000.00 USD | 3,100.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 25,430,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+51.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 25,430,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 25,430,000.00 USD | 773.95 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 25,430,000.00 USD | 549.99 USD | 0.00 USD | `+52.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 25,940,000.00 USD | 510,120.00 USD | 0.00 USD | `+52.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 26,300,000.00 USD | 352,280.00 USD | 0.00 USD | `+53.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 26,300,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 26,300,000.00 USD | 178.92 USD | 0.00 USD | `+54.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 26,300,000.00 USD | 1,360.00 USD | 0.00 USD | `+54.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 26,310,000.00 USD | 14,430.00 USD | 0.00 USD | `+54.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 26,320,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 26,320,000.00 USD | 411.94 USD | 0.00 USD | `+55.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.95` | 26,330,000.00 USD | 10,230.00 USD | 0.00 USD | `+55.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.15` | 26,340,000.00 USD | 12,000.00 USD | 0.00 USD | `+56.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 26,350,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 26,350,000.00 USD | 1,020.00 USD | 0.00 USD | `+57.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 26,360,000.00 USD | 12,000.00 USD | 0.00 USD | `+58.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 26,360,000.00 USD | 113.04 USD | 0.00 USD | `+58.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 26,360,000.00 USD | 1,830.00 USD | 0.00 USD | `+58.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 26,380,000.00 USD | 16,970.00 USD | 0.00 USD | `+59.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 26,380,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 26,390,000.00 USD | 6,480.00 USD | 0.00 USD | `+62.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 26,400,000.00 USD | 15,880.00 USD | 0.00 USD | `+62.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 26,410,000.00 USD | 692.30 USD | 0.00 USD | `+63.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 26,410,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 26,500,000.00 USD | 90,570.00 USD | 0.00 USD | `+64.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 26,500,000.00 USD | 281.84 USD | 0.00 USD | `+65.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 26,510,000.00 USD | 4,080.00 USD | 0.00 USD | `+67.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 26,590,000.00 USD | 82,530.00 USD | 0.00 USD | `+69.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 26,590,000.00 USD | 823.94 USD | 0.00 USD | `+69.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 26,590,000.00 USD | 211.39 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 26,590,000.00 USD | 307.19 USD | 0.00 USD | `+71.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 26,590,000.00 USD | 593.03 USD | 0.00 USD | `+71.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 26,590,000.00 USD | 1,440.00 USD | 0.00 USD | `+71.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 26,600,000.00 USD | 5,550.00 USD | 0.00 USD | `+72.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 26,600,000.00 USD | 495.09 USD | 0.00 USD | `+73.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 26,600,000.00 USD | 912.63 USD | 0.00 USD | `+74.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 26,640,000.00 USD | 42,840.00 USD | 0.00 USD | `+74.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 26,640,000.00 USD | 686.20 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 26,680,000.00 USD | 35,280.00 USD | 0.00 USD | `+76.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 26,680,000.00 USD | 703.60 USD | 0.00 USD | `+76.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 26,680,000.00 USD | 3,160.00 USD | 0.00 USD | `+77.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 26,730,000.00 USD | 52,520.00 USD | 0.00 USD | `+79.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 26,760,000.00 USD | 21,960.00 USD | 0.00 USD | `+79.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.55` | 26,760,000.00 USD | 1,450.00 USD | 0.00 USD | `+81.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 26,760,000.00 USD | 1,450.00 USD | 0.00 USD | `+81.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 26,760,000.00 USD | 1,840.00 USD | 0.00 USD | `+81.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.35` | 26,760,000.00 USD | 390.17 USD | 0.00 USD | `+81.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 26,760,000.00 USD | 2,990.00 USD | 0.00 USD | `+83.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 26,760,000.00 USD | 261.56 USD | 0.00 USD | `+83.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.85` | 26,760,000.00 USD | 109.71 USD | 0.00 USD | `+84.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 26,940,000.00 USD | 174,400.00 USD | 0.00 USD | `+84.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 26,940,000.00 USD | 2,440.00 USD | 0.00 USD | `+85.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 26,940,000.00 USD | 349.34 USD | 0.00 USD | `+86.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 26,960,000.00 USD | 19,620.00 USD | 0.00 USD | `+87.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 27,510,000.00 USD | 550,350.00 USD | 0.00 USD | `+88.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 27,540,000.00 USD | 29,420.00 USD | 0.00 USD | `+89.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 27,740,000.00 USD | 198,160.00 USD | 0.00 USD | `+91.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 27,880,000.00 USD | 141,190.00 USD | 0.00 USD | `+92.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 27,920,000.00 USD | 35,880.00 USD | 0.00 USD | `+94.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 27,920,000.00 USD | 744.27 USD | 0.00 USD | `+95.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 27,920,000.00 USD | 4,270.00 USD | 0.00 USD | `+98.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.05` | 27,920,000.00 USD | 1,760.00 USD | 0.00 USD | `+99.99%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `86.10` | 90,700,000.00 USD | 0.00 USD | 90,700,000.00 USD | 0.00 USD | 85,490.00 USD | 205,540.00 USD |
| `1D` | `86.30` | 90,410,000.00 USD | 0.00 USD | 90,410,000.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `86.30` | 98,710,000.00 USD | 0.00 USD | 98,710,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD |
| `1D` | `86.50` | 90,400,000.00 USD | 0.00 USD | 90,400,000.00 USD | 0.00 USD | 88,070.00 USD | 0.00 USD |
| `7D` | `86.50` | 98,560,000.00 USD | 0.00 USD | 98,560,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `1D` | `86.70` | 90,310,000.00 USD | 0.00 USD | 90,310,000.00 USD | 0.00 USD | 222,710.00 USD | 3,100.00 USD |
| `1D` | `86.90` | 90,090,000.00 USD | 0.00 USD | 90,090,000.00 USD | 139,770.00 USD | 174,950.00 USD | 4,330.00 USD |
| `7D` | `86.90` | 98,550,000.00 USD | 0.00 USD | 98,550,000.00 USD | 207,900.00 USD | 138,700.00 USD | 0.00 USD |
| `1D` | `87.10` | 89,770,000.00 USD | 0.00 USD | 89,770,000.00 USD | 19,160.00 USD | 0.00 USD | 48,920.00 USD |
| `7D` | `87.10` | 98,210,000.00 USD | 0.00 USD | 98,210,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD |
| `1D` | `87.30` | 89,700,000.00 USD | 0.00 USD | 89,700,000.00 USD | 8,750.00 USD | 163,550.00 USD | 154,040.00 USD |
| `7D` | `87.30` | 98,200,000.00 USD | 0.00 USD | 98,200,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD |
| `1D` | `87.50` | 89,370,000.00 USD | 0.00 USD | 89,370,000.00 USD | 10,160.00 USD | 12,060.00 USD | 2,850.00 USD |
| `7D` | `87.50` | 97,710,000.00 USD | 0.00 USD | 97,710,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD |
| `1D` | `87.70` | 89,350,000.00 USD | 0.00 USD | 89,350,000.00 USD | 0.00 USD | 99,990.00 USD | 195,990.00 USD |
| `7D` | `87.70` | 97,660,000.00 USD | 0.00 USD | 97,660,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD |
| `1D` | `87.90` | 89,050,000.00 USD | 0.00 USD | 89,050,000.00 USD | 22,290.00 USD | 258,430.00 USD | 818,590.00 USD |
| `7D` | `87.90` | 96,950,000.00 USD | 0.00 USD | 96,950,000.00 USD | 0.00 USD | 295,390.00 USD | 0.00 USD |
| `1D` | `88.50` | 87,950,000.00 USD | 0.00 USD | 87,950,000.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD |
| `1D` | `88.70` | 87,950,000.00 USD | 0.00 USD | 87,950,000.00 USD | 170,450.00 USD | 124,180.00 USD | 415,440.00 USD |
| `7D` | `88.70` | 96,660,000.00 USD | 0.00 USD | 96,660,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.90` | 87,240,000.00 USD | 0.00 USD | 87,240,000.00 USD | 143,140.00 USD | 53,480.00 USD | 216,100.00 USD |
| `7D` | `88.90` | 96,430,000.00 USD | 0.00 USD | 96,430,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD |
| `1D` | `89.10` | 86,830,000.00 USD | 0.00 USD | 86,830,000.00 USD | 160,900.00 USD | 63,750.00 USD | 1,330.00 USD |
| `7D` | `89.10` | 96,410,000.00 USD | 0.00 USD | 96,410,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD |
| `1D` | `89.30` | 86,600,000.00 USD | 0.00 USD | 86,600,000.00 USD | 10,500.00 USD | 83,100.00 USD | 3,850.00 USD |
| `7D` | `89.30` | 95,190,000.00 USD | 0.00 USD | 95,190,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD |
| `1D` | `89.50` | 86,500,000.00 USD | 0.00 USD | 86,500,000.00 USD | 130,890.00 USD | 55,430.00 USD | 266,870.00 USD |
| `7D` | `89.50` | 95,160,000.00 USD | 0.00 USD | 95,160,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD |
| `1D` | `89.70` | 86,050,000.00 USD | 0.00 USD | 86,050,000.00 USD | 705,660.00 USD | 362,180.00 USD | 343,790.00 USD |
| `7D` | `89.70` | 94,370,000.00 USD | 0.00 USD | 94,370,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD |
| `1D` | `89.90` | 84,640,000.00 USD | 0.00 USD | 84,640,000.00 USD | 397,980.00 USD | 328,910.00 USD | 405,440.00 USD |
| `7D` | `89.90` | 92,950,000.00 USD | 0.00 USD | 92,950,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `1D` | `90.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 597,590.00 USD | 530,230.00 USD | 464,430.00 USD |
| `7D` | `90.10` | 91,150,000.00 USD | 0.00 USD | 91,150,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `1D` | `90.30` | 81,910,000.00 USD | 0.00 USD | 81,910,000.00 USD | 373,160.00 USD | 370,710.00 USD | 437,780.00 USD |
| `7D` | `90.30` | 88,780,000.00 USD | 0.00 USD | 88,780,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `90.50` | 80,730,000.00 USD | 0.00 USD | 80,730,000.00 USD | 523,240.00 USD | 419,800.00 USD | 531,060.00 USD |
| `7D` | `90.50` | 86,700,000.00 USD | 0.00 USD | 86,700,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD |
| `1D` | `90.70` | 79,260,000.00 USD | 0.00 USD | 79,260,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `90.70` | 84,020,000.00 USD | 0.00 USD | 84,020,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `90.90` | 78,760,000.00 USD | 0.00 USD | 78,760,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `90.90` | 81,570,000.00 USD | 0.00 USD | 81,570,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `91.10` | 78,650,000.00 USD | 0.00 USD | 78,650,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `91.10` | 79,190,000.00 USD | 0.00 USD | 79,190,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `91.30` | 78,470,000.00 USD | 0.00 USD | 78,470,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD |
| `7D` | `91.30` | 77,280,000.00 USD | 0.00 USD | 77,280,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `91.50` | 78,320,000.00 USD | 0.00 USD | 78,320,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD |
| `7D` | `91.50` | 74,780,000.00 USD | 0.00 USD | 74,780,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD |
| `1D` | `91.70` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 107,440.00 USD | 112,260.00 USD | 514,930.00 USD |
| `7D` | `91.70` | 71,870,000.00 USD | 0.00 USD | 71,870,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `91.90` | 77,470,000.00 USD | 0.00 USD | 77,470,000.00 USD | 156,200.00 USD | 277,390.00 USD | 65,340.00 USD |
| `7D` | `91.90` | 70,230,000.00 USD | 0.00 USD | 70,230,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `1D` | `92.10` | 76,970,000.00 USD | 0.00 USD | 76,970,000.00 USD | 65,530.00 USD | 68,940.00 USD | 63,140.00 USD |
| `7D` | `92.10` | 67,820,000.00 USD | 0.00 USD | 67,820,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD |
| `1D` | `92.30` | 76,780,000.00 USD | 0.00 USD | 76,780,000.00 USD | 123,260.00 USD | 353,760.00 USD | 841,010.00 USD |
| `7D` | `92.30` | 66,120,000.00 USD | 0.00 USD | 66,120,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD |
| `1D` | `92.50` | 75,460,000.00 USD | 0.00 USD | 75,460,000.00 USD | 16,830.00 USD | 884,320.00 USD | 77,750.00 USD |
| `7D` | `92.50` | 63,770,000.00 USD | 0.00 USD | 63,770,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD |
| `1D` | `92.70` | 74,480,000.00 USD | 0.00 USD | 74,480,000.00 USD | 349,430.00 USD | 333,670.00 USD | 97,110.00 USD |
| `7D` | `92.70` | 62,000,000.00 USD | 0.00 USD | 62,000,000.00 USD | 671,470.00 USD | 168,780.00 USD | 70,750.00 USD |
| `1D` | `92.90` | 73,700,000.00 USD | 0.00 USD | 73,700,000.00 USD | 47,890.00 USD | 120,260.00 USD | 122,310.00 USD |
| `7D` | `92.90` | 61,090,000.00 USD | 0.00 USD | 61,090,000.00 USD | 0.00 USD | 74,260.00 USD | 0.00 USD |
| `1D` | `93.10` | 73,410,000.00 USD | 0.00 USD | 73,410,000.00 USD | 21,880.00 USD | 497,440.00 USD | 385,100.00 USD |
| `7D` | `93.10` | 61,010,000.00 USD | 0.00 USD | 61,010,000.00 USD | 31,020.00 USD | 630,650.00 USD | 1,000,000.00 USD |
| `1D` | `93.30` | 72,500,000.00 USD | 0.00 USD | 72,500,000.00 USD | 35,840.00 USD | 251,260.00 USD | 134,840.00 USD |
| `7D` | `93.30` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 145,070.00 USD | 66,280.00 USD | 468,690.00 USD |
| `1D` | `93.50` | 72,080,000.00 USD | 0.00 USD | 72,080,000.00 USD | 40,950.00 USD | 537,430.00 USD | 489,970.00 USD |
| `7D` | `93.50` | 58,670,000.00 USD | 0.00 USD | 58,670,000.00 USD | 93,960.00 USD | 1,260,000.00 USD | 1,450,000.00 USD |
| `1D` | `93.70` | 71,010,000.00 USD | 0.00 USD | 71,010,000.00 USD | 118,790.00 USD | 487,680.00 USD | 2,340,000.00 USD |
| `7D` | `93.70` | 55,870,000.00 USD | 0.00 USD | 55,870,000.00 USD | 270,240.00 USD | 954,120.00 USD | 120,980.00 USD |
| `1D` | `93.90` | 68,070,000.00 USD | 0.00 USD | 68,070,000.00 USD | 60,590.00 USD | 1,050,000.00 USD | 737,250.00 USD |
| `7D` | `93.90` | 54,530,000.00 USD | 0.00 USD | 54,530,000.00 USD | 168,420.00 USD | 56,340.00 USD | 23,050.00 USD |
| `1D` | `94.10` | 66,220,000.00 USD | 0.00 USD | 66,220,000.00 USD | 0.00 USD | 337,220.00 USD | 9,780.00 USD |
| `7D` | `94.10` | 54,280,000.00 USD | 0.00 USD | 54,280,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD |
| `1D` | `94.30` | 65,870,000.00 USD | 0.00 USD | 65,870,000.00 USD | 0.00 USD | 1,530,000.00 USD | 708,650.00 USD |
| `7D` | `94.30` | 52,700,000.00 USD | 0.00 USD | 52,700,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD |
| `1D` | `94.50` | 63,630,000.00 USD | 0.00 USD | 63,630,000.00 USD | 33,670.00 USD | 620,570.00 USD | 2,080,000.00 USD |
| `7D` | `94.50` | 51,980,000.00 USD | 0.00 USD | 51,980,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD |
| `1D` | `94.70` | 60,900,000.00 USD | 0.00 USD | 60,900,000.00 USD | 1,120,000.00 USD | 1,730,000.00 USD | 1,040,000.00 USD |
| `7D` | `94.70` | 50,900,000.00 USD | 0.00 USD | 50,900,000.00 USD | 1,600,000.00 USD | 238,650.00 USD | 0.00 USD |
| `1D` | `94.90` | 57,000,000.00 USD | 0.00 USD | 57,000,000.00 USD | 570,680.00 USD | 487,560.00 USD | 251,490.00 USD |
| `7D` | `94.90` | 49,060,000.00 USD | 0.00 USD | 49,060,000.00 USD | 1,100,000.00 USD | 2,260,000.00 USD | 0.00 USD |
| `1D` | `95.10` | 55,690,000.00 USD | 0.00 USD | 55,690,000.00 USD | 459,370.00 USD | 2,630,000.00 USD | 2,160,000.00 USD |
| `7D` | `95.10` | 45,700,000.00 USD | 0.00 USD | 45,700,000.00 USD | 198,380.00 USD | 1,270,000.00 USD | 2,770,000.00 USD |
| `1D` | `95.30` | 50,440,000.00 USD | 0.00 USD | 50,440,000.00 USD | 92,990.00 USD | 3,000,000.00 USD | 276,600.00 USD |
| `7D` | `95.30` | 41,460,000.00 USD | 0.00 USD | 41,460,000.00 USD | 678,330.00 USD | 445,310.00 USD | 838,770.00 USD |
| `1D` | `95.50` | 47,070,000.00 USD | 0.00 USD | 47,070,000.00 USD | 2,390,000.00 USD | 1,660,000.00 USD | 997,170.00 USD |
| `7D` | `95.50` | 39,490,000.00 USD | 0.00 USD | 39,490,000.00 USD | 1,200,000.00 USD | 3,810,000.00 USD | 2,880,000.00 USD |
| `1D` | `95.70` | 42,020,000.00 USD | 0.00 USD | 42,020,000.00 USD | 1,590,000.00 USD | 2,220,000.00 USD | 4,110,000.00 USD |
| `7D` | `95.70` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 4,060,000.00 USD | 1,480,000.00 USD | 10,200.00 USD |
| `1D` | `95.90` | 34,100,000.00 USD | 0.00 USD | 34,100,000.00 USD | 1,360,000.00 USD | 798,100.00 USD | 1,590,000.00 USD |
| `7D` | `95.90` | 26,060,000.00 USD | 0.00 USD | 26,060,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.10` | 30,350,000.00 USD | 0.00 USD | 30,350,000.00 USD | 2,430,000.00 USD | 1,340,000.00 USD | 402,770.00 USD |
| `7D` | `96.10` | 23,930,000.00 USD | 0.00 USD | 23,930,000.00 USD | 3,460,000.00 USD | 2,050,000.00 USD | 4,520,000.00 USD |
| `1D` | `96.30` | 26,170,000.00 USD | 0.00 USD | 26,170,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,290,000.00 USD |
| `7D` | `96.30` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 1,030,000.00 USD | 2,320,000.00 USD | 5,630,000.00 USD |
| `1D` | `96.50` | 23,270,000.00 USD | 0.00 USD | 23,270,000.00 USD | 0.00 USD | 1,770,000.00 USD | 6,550,000.00 USD |
| `7D` | `96.50` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD |
| `1D` | `96.70` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 0.00 USD | 4,380,000.00 USD | 10,010,000.00 USD |
| `1D` | `96.90` | 565,760.00 USD | 0.00 USD | 565,760.00 USD | 561,460.00 USD | 4,300.00 USD | 0.00 USD |
| `1D` | `97.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.10` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.30` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 146,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.30` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.50` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.50` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.70` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 5,590,000.00 USD | 0.00 USD | 24,790.00 USD |
| `7D` | `97.70` | 19,680,000.00 USD | 19,680,000.00 USD | 0.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.90` | 18,950,000.00 USD | 18,950,000.00 USD | 0.00 USD | 4,140,000.00 USD | 1,130,000.00 USD | 3,580,000.00 USD |
| `7D` | `97.90` | 45,230,000.00 USD | 45,230,000.00 USD | 0.00 USD | 11,920,000.00 USD | 5,860,000.00 USD | 7,770,000.00 USD |
| `1D` | `98.10` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 6,760,000.00 USD | 2,920,000.00 USD | 4,410,000.00 USD |
| `7D` | `98.10` | 80,140,000.00 USD | 80,140,000.00 USD | 0.00 USD | 9,820,000.00 USD | 9,540,000.00 USD | 15,550,000.00 USD |
| `1D` | `98.30` | 45,860,000.00 USD | 45,860,000.00 USD | 0.00 USD | 2,970,000.00 USD | 3,940,000.00 USD | 5,920,000.00 USD |
| `7D` | `98.30` | 96,710,000.00 USD | 96,710,000.00 USD | 0.00 USD | 43,030.00 USD | 6,830,000.00 USD | 9,700,000.00 USD |
| `1D` | `98.50` | 54,270,000.00 USD | 54,270,000.00 USD | 0.00 USD | 698,860.00 USD | 2,340,000.00 USD | 5,380,000.00 USD |
| `7D` | `98.50` | 102,860,000.00 USD | 102,860,000.00 USD | 0.00 USD | 1,040,000.00 USD | 5,110,000.00 USD | 0.00 USD |
| `1D` | `98.70` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 95,780.00 USD | 3,780,000.00 USD | 7,270,000.00 USD |
| `7D` | `98.70` | 102,890,000.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 28,080.00 USD | 0.00 USD |
| `1D` | `98.90` | 67,530,000.00 USD | 67,530,000.00 USD | 0.00 USD | 43,770.00 USD | 1,300,000.00 USD | 770,190.00 USD |
| `7D` | `98.90` | 105,430,000.00 USD | 105,430,000.00 USD | 0.00 USD | 57,310.00 USD | 1,040,000.00 USD | 1,440,000.00 USD |
| `1D` | `99.10` | 71,970,000.00 USD | 71,970,000.00 USD | 0.00 USD | 71,670.00 USD | 502,530.00 USD | 3,860,000.00 USD |
| `7D` | `99.10` | 106,570,000.00 USD | 106,570,000.00 USD | 0.00 USD | 179,190.00 USD | 124,230.00 USD | 838,770.00 USD |
| `1D` | `99.30` | 77,430,000.00 USD | 77,430,000.00 USD | 0.00 USD | 2,900,000.00 USD | 1,070,000.00 USD | 1,490,000.00 USD |
| `7D` | `99.30` | 111,700,000.00 USD | 111,700,000.00 USD | 0.00 USD | 0.00 USD | 2,230,000.00 USD | 2,890,000.00 USD |
| `1D` | `99.50` | 80,460,000.00 USD | 80,460,000.00 USD | 0.00 USD | 132,490.00 USD | 2,340,000.00 USD | 560,230.00 USD |
| `7D` | `99.50` | 115,440,000.00 USD | 115,440,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,480,000.00 USD | 16,920.00 USD |
| `1D` | `99.70` | 101,440,000.00 USD | 101,440,000.00 USD | 0.00 USD | 3,660,000.00 USD | 6,920,000.00 USD | 10,390,000.00 USD |
| `7D` | `99.70` | 117,450,000.00 USD | 117,450,000.00 USD | 0.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD |
| `1D` | `99.90` | 107,040,000.00 USD | 107,040,000.00 USD | 0.00 USD | 468,220.00 USD | 914,600.00 USD | 4,210,000.00 USD |
| `7D` | `99.90` | 124,600,000.00 USD | 124,600,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD |
| `1D` | `100.10` | 110,210,000.00 USD | 110,210,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,560,000.00 USD | 8,000.00 USD |
| `7D` | `100.10` | 127,990,000.00 USD | 127,990,000.00 USD | 0.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD |
| `1D` | `100.30` | 114,080,000.00 USD | 114,080,000.00 USD | 0.00 USD | 16,830.00 USD | 1,210,000.00 USD | 2,640,000.00 USD |
| `7D` | `100.30` | 130,840,000.00 USD | 130,840,000.00 USD | 0.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD |
| `1D` | `100.50` | 119,610,000.00 USD | 119,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 305,750.00 USD | 3,610,000.00 USD |
| `7D` | `100.50` | 137,780,000.00 USD | 137,780,000.00 USD | 0.00 USD | 2,500,000.00 USD | 128,740.00 USD | 4,310,000.00 USD |
| `1D` | `100.70` | 125,930,000.00 USD | 125,930,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,960,000.00 USD | 2,660,000.00 USD |
| `7D` | `100.70` | 139,160,000.00 USD | 139,160,000.00 USD | 0.00 USD | 133,340.00 USD | 1,240,000.00 USD | 0.00 USD |
| `1D` | `100.90` | 131,550,000.00 USD | 131,550,000.00 USD | 0.00 USD | 1,540,000.00 USD | 2,300,000.00 USD | 1,780,000.00 USD |
| `7D` | `100.90` | 152,250,000.00 USD | 152,250,000.00 USD | 0.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD |
| `1D` | `101.10` | 148,150,000.00 USD | 148,150,000.00 USD | 0.00 USD | 9,810,000.00 USD | 4,430,000.00 USD | 2,360,000.00 USD |
| `7D` | `101.10` | 162,020,000.00 USD | 162,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD |
| `1D` | `101.30` | 160,400,000.00 USD | 160,400,000.00 USD | 0.00 USD | 3,680,000.00 USD | 4,410,000.00 USD | 4,170,000.00 USD |
| `7D` | `101.30` | 182,590,000.00 USD | 182,590,000.00 USD | 0.00 USD | 7,310,000.00 USD | 4,280,000.00 USD | 8,980,000.00 USD |
| `1D` | `101.50` | 178,240,000.00 USD | 178,240,000.00 USD | 0.00 USD | 2,790,000.00 USD | 4,250,000.00 USD | 10,790,000.00 USD |
| `7D` | `101.50` | 197,860,000.00 USD | 197,860,000.00 USD | 0.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD |
| `1D` | `101.70` | 190,850,000.00 USD | 190,850,000.00 USD | 0.00 USD | 3,930,000.00 USD | 625,490.00 USD | 8,060,000.00 USD |
| `7D` | `101.70` | 207,210,000.00 USD | 207,210,000.00 USD | 0.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD |
| `1D` | `101.90` | 195,630,000.00 USD | 195,630,000.00 USD | 0.00 USD | 1,970,000.00 USD | 532,070.00 USD | 2,280,000.00 USD |
| `7D` | `101.90` | 215,210,000.00 USD | 215,210,000.00 USD | 0.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD |
| `1D` | `102.10` | 201,050,000.00 USD | 201,050,000.00 USD | 0.00 USD | 2,650,000.00 USD | 880,210.00 USD | 1,880,000.00 USD |
| `7D` | `102.10` | 219,850,000.00 USD | 219,850,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD |
| `1D` | `102.30` | 206,830,000.00 USD | 206,830,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,500,000.00 USD | 2,600,000.00 USD |
| `7D` | `102.30` | 225,900,000.00 USD | 225,900,000.00 USD | 0.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD |
| `1D` | `102.50` | 211,160,000.00 USD | 211,160,000.00 USD | 0.00 USD | 1,510,000.00 USD | 800,630.00 USD | 2,020,000.00 USD |
| `7D` | `102.50` | 229,560,000.00 USD | 229,560,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.70` | 213,090,000.00 USD | 213,090,000.00 USD | 0.00 USD | 1,270,000.00 USD | 658,410.00 USD | 3,170.00 USD |
| `7D` | `102.70` | 230,330,000.00 USD | 230,330,000.00 USD | 0.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD |
| `1D` | `102.90` | 217,990,000.00 USD | 217,990,000.00 USD | 0.00 USD | 1,520,000.00 USD | 1,880,000.00 USD | 1,490,000.00 USD |
| `7D` | `102.90` | 251,620,000.00 USD | 251,620,000.00 USD | 0.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD |
| `1D` | `103.10` | 224,010,000.00 USD | 224,010,000.00 USD | 0.00 USD | 2,660,000.00 USD | 1,770,000.00 USD | 1,600,000.00 USD |
| `7D` | `103.10` | 257,830,000.00 USD | 257,830,000.00 USD | 0.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD |
| `1D` | `103.30` | 227,370,000.00 USD | 227,370,000.00 USD | 0.00 USD | 1,020,000.00 USD | 1,010,000.00 USD | 1,320,000.00 USD |
| `7D` | `103.30` | 275,400,000.00 USD | 275,400,000.00 USD | 0.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD |
| `1D` | `103.50` | 236,860,000.00 USD | 236,860,000.00 USD | 0.00 USD | 3,000,000.00 USD | 1,940,000.00 USD | 4,560,000.00 USD |
| `7D` | `103.50` | 297,800,000.00 USD | 297,800,000.00 USD | 0.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD |
| `1D` | `103.70` | 244,920,000.00 USD | 244,920,000.00 USD | 0.00 USD | 2,940,000.00 USD | 1,990,000.00 USD | 3,130,000.00 USD |
| `7D` | `103.70` | 310,030,000.00 USD | 310,030,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.90` | 251,970,000.00 USD | 251,970,000.00 USD | 0.00 USD | 2,590,000.00 USD | 2,430,000.00 USD | 2,040,000.00 USD |
| `7D` | `103.90` | 328,060,000.00 USD | 328,060,000.00 USD | 0.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.10` | 261,000,000.00 USD | 261,000,000.00 USD | 0.00 USD | 3,500,000.00 USD | 2,320,000.00 USD | 3,210,000.00 USD |
| `7D` | `104.10` | 356,790,000.00 USD | 356,790,000.00 USD | 0.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD |
| `1D` | `104.30` | 266,130,000.00 USD | 266,130,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,720,000.00 USD | 1,640,000.00 USD |
| `7D` | `104.30` | 378,170,000.00 USD | 378,170,000.00 USD | 0.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD |
| `1D` | `104.50` | 271,120,000.00 USD | 271,120,000.00 USD | 0.00 USD | 1,950,000.00 USD | 1,380,000.00 USD | 1,660,000.00 USD |
| `7D` | `104.50` | 390,170,000.00 USD | 390,170,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD |
| `1D` | `104.70` | 277,040,000.00 USD | 277,040,000.00 USD | 0.00 USD | 1,690,000.00 USD | 983,560.00 USD | 3,250,000.00 USD |
| `7D` | `104.70` | 410,170,000.00 USD | 410,170,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD |
| `1D` | `104.90` | 278,520,000.00 USD | 278,520,000.00 USD | 0.00 USD | 383,880.00 USD | 458,320.00 USD | 640,140.00 USD |
| `7D` | `104.90` | 430,770,000.00 USD | 430,770,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.10` | 280,550,000.00 USD | 280,550,000.00 USD | 0.00 USD | 421,810.00 USD | 350,810.00 USD | 1,250,000.00 USD |
| `7D` | `105.10` | 443,980,000.00 USD | 443,980,000.00 USD | 0.00 USD | 5,580,000.00 USD | 4,800,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.30` | 280,640,000.00 USD | 280,640,000.00 USD | 0.00 USD | 2,590.00 USD | 87,920.00 USD | 0.00 USD |
| `7D` | `105.30` | 448,980,000.00 USD | 448,980,000.00 USD | 0.00 USD | 2,740,000.00 USD | 1,820,000.00 USD | 428,740.00 USD |
| `1D` | `105.50` | 281,110,000.00 USD | 281,110,000.00 USD | 0.00 USD | 169,670.00 USD | 196,610.00 USD | 107,830.00 USD |
| `7D` | `105.50` | 468,490,000.00 USD | 468,490,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD |
| `1D` | `105.70` | 281,480,000.00 USD | 281,480,000.00 USD | 0.00 USD | 106,090.00 USD | 231,960.00 USD | 29,710.00 USD |
| `7D` | `105.70` | 482,660,000.00 USD | 482,660,000.00 USD | 0.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD |
| `1D` | `105.90` | 282,470,000.00 USD | 282,470,000.00 USD | 0.00 USD | 215,940.00 USD | 631,980.00 USD | 138,120.00 USD |
| `7D` | `105.90` | 492,550,000.00 USD | 492,550,000.00 USD | 0.00 USD | 3,680,000.00 USD | 1,870,000.00 USD | 4,340,000.00 USD |
| `1D` | `106.10` | 283,980,000.00 USD | 283,980,000.00 USD | 0.00 USD | 716,050.00 USD | 528,260.00 USD | 268,330.00 USD |
| `7D` | `106.10` | 504,690,000.00 USD | 504,690,000.00 USD | 0.00 USD | 6,090,000.00 USD | 3,080,000.00 USD | 2,960,000.00 USD |
| `1D` | `106.30` | 284,840,000.00 USD | 284,840,000.00 USD | 0.00 USD | 188,620.00 USD | 376,430.00 USD | 293,410.00 USD |
| `7D` | `106.30` | 514,650,000.00 USD | 514,650,000.00 USD | 0.00 USD | 4,750,000.00 USD | 2,990,000.00 USD | 2,230,000.00 USD |
| `1D` | `106.50` | 285,810,000.00 USD | 285,810,000.00 USD | 0.00 USD | 504,400.00 USD | 258,940.00 USD | 212,730.00 USD |
| `7D` | `106.50` | 519,890,000.00 USD | 519,890,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,650,000.00 USD | 1,890,000.00 USD |
| `1D` | `106.70` | 287,870,000.00 USD | 287,870,000.00 USD | 0.00 USD | 513,150.00 USD | 225,990.00 USD | 1,320,000.00 USD |
| `7D` | `106.70` | 529,510,000.00 USD | 529,510,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,870,000.00 USD | 4,470,000.00 USD |
| `1D` | `106.90` | 288,220,000.00 USD | 288,220,000.00 USD | 0.00 USD | 10,160.00 USD | 95,900.00 USD | 239,010.00 USD |
| `7D` | `106.90` | 535,340,000.00 USD | 535,340,000.00 USD | 0.00 USD | 1,220,000.00 USD | 1,150,000.00 USD | 3,470,000.00 USD |
| `1D` | `107.10` | 289,060,000.00 USD | 289,060,000.00 USD | 0.00 USD | 88,570.00 USD | 218,500.00 USD | 528,780.00 USD |
| `7D` | `107.10` | 539,450,000.00 USD | 539,450,000.00 USD | 0.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD |
| `1D` | `107.30` | 289,250,000.00 USD | 289,250,000.00 USD | 0.00 USD | 22,290.00 USD | 60,380.00 USD | 110,290.00 USD |
| `7D` | `107.30` | 539,900,000.00 USD | 539,900,000.00 USD | 0.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD |
| `1D` | `107.50` | 290,150,000.00 USD | 290,150,000.00 USD | 0.00 USD | 0.00 USD | 198,050.00 USD | 708,290.00 USD |
| `7D` | `107.50` | 540,880,000.00 USD | 540,880,000.00 USD | 0.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD |
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
  * Total Open Interest: `5.98B` | Total OI Tokens: `61,713,253.0 SOL`
  * 1h OI Change: `-0.76%` | 4h OI Change: `-4.08%` | 24h OI Change: `-6.08%`
  * Exchange Breakdown: Binance=`994.86M` | Bybit=`619.04M` | OKX=`360.74M` | Hyperliquid=`549.59M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `44.04K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0047%` | **USDT OKX** | `0.0052%` |
| **USDT Bybit** | `-0.0037%` | **USDT KuCoin** | `0.0019%` |
| **USDT MEXC** | `0.0046%` | **USDT BingX** | `0.0052%` |
| **USDT Gate** | `0.0011%` | **USDT Bitget** | `0.0047%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `46.35%` | `53.65%` | `0.86` | 809,820,000.00 USD |
| `15M` | `Binance` | `53.68%` | `46.32%` | `1.16` | 255,050,000.00 USD |
| `15M` | `OKX` | `45.64%` | `54.36%` | `0.84` | 92,760,000.00 USD |
| `15M` | `Bybit` | `34.33%` | `65.67%` | `0.52` | 86,880,000.00 USD |
| `15M` | `KuCoin` | `46.35%` | `53.65%` | `0.86` | 2,510,000.00 USD |
| `15M` | `Gate` | `47.29%` | `52.71%` | `0.90` | 89,420,000.00 USD |
| `15M` | `Bitget` | `38.34%` | `61.66%` | `0.62` | 31,660,000.00 USD |
| `15M` | `BingX` | `42.85%` | `57.15%` | `0.75` | 5,800,000.00 USD |
| `15M` | `MEXC` | `32.61%` | `67.39%` | `0.48` | 23,690,000.00 USD |
| `15M` | `Bitunix` | `29.35%` | `70.65%` | `0.42` | 33,600,000.00 USD |
| `15M` | `Hyperliquid` | `35.86%` | `64.14%` | `0.56` | 43,020,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.2%` | `46.8%` | `1.14` | 2,380,000.00 USD |
| `15M` | `Crypto.com` | `53.2%` | `46.8%` | `1.14` | 5,090,000.00 USD |
| `15M` | `WhiteBIT` | `98.1%` | `1.9%` | `51.63` | 71,820,000.00 USD |
| `15M` | `HTX` | `42.16%` | `57.84%` | `0.73` | 2,260,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 38,650,000.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 1,840,000.00 USD |
| `15M` | `Kraken` | `62.91%` | `37.09%` | `1.70` | 8,370,000.00 USD |
| `15M` | `Aster` | `38.59%` | `61.41%` | `0.63` | 6,120,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.92%` | `44.08%` | `1.27` | 8,880,000.00 USD |
| `15M` | `Whale Positions` | `53.68%` | `46.32%` | `1.16` | 255,050,000.00 USD |
| `15M` | `Global Accounts` | `46.35%` | `53.65%` | `0.86` | 809,820,000.00 USD |
| `1H` | `SOL` | `49.69%` | `50.31%` | `0.99` | 237,350,000.00 USD |
| `1H` | `Binance` | `50.49%` | `49.51%` | `1.02` | 109,710,000.00 USD |
| `1H` | `OKX` | `51.82%` | `48.18%` | `1.08` | 26,980,000.00 USD |
| `1H` | `Bybit` | `42.6%` | `57.4%` | `0.74` | 29,370,000.00 USD |
| `1H` | `KuCoin` | `48.89%` | `51.11%` | `0.96` | 8,980,000.00 USD |
| `1H` | `Gate` | `43.04%` | `56.96%` | `0.76` | 5,490,000.00 USD |
| `1H` | `Bitget` | `44.02%` | `55.98%` | `0.79` | 13,360,000.00 USD |
| `1H` | `BingX` | `44.9%` | `55.1%` | `0.81` | 3,510,000.00 USD |
| `1H` | `MEXC` | `44.52%` | `55.48%` | `0.80` | 18,260,000.00 USD |
| `1H` | `Bitunix` | `49.42%` | `50.58%` | `0.98` | 7,690,000.00 USD |
| `1H` | `Hyperliquid` | `67.67%` | `32.33%` | `2.09` | 4,850,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.65%` | `41.35%` | `1.42` | 848,260.00 USD |
| `1H` | `Crypto.com` | `63.69%` | `36.31%` | `1.75` | 340,920.00 USD |
| `1H` | `WhiteBIT` | `99.27%` | `0.73%` | `135.99` | 4,620,000.00 USD |
| `1H` | `HTX` | `58.21%` | `41.79%` | `1.39` | 150,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.61%` | `54.39%` | `0.84` | 1,150,000.00 USD |
| `1H` | `Aster` | `31.79%` | `68.21%` | `0.47` | 1,760,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.92%` | `45.08%` | `1.22` | 278,120.00 USD |
| `1H` | `Whale Positions` | `50.49%` | `49.51%` | `1.02` | 109,710,000.00 USD |
| `1H` | `Global Accounts` | `49.69%` | `50.31%` | `0.99` | 237,350,000.00 USD |
| `4H` | `SOL` | `45.93%` | `54.07%` | `0.85` | 1,500,000,000.00 USD |
| `4H` | `Binance` | `46.27%` | `53.73%` | `0.86` | 585,430,000.00 USD |
| `4H` | `OKX` | `46.73%` | `53.27%` | `0.88` | 194,310,000.00 USD |
| `4H` | `Bybit` | `41.03%` | `58.97%` | `0.70` | 226,730,000.00 USD |
| `4H` | `KuCoin` | `47.1%` | `52.9%` | `0.89` | 30,350,000.00 USD |
| `4H` | `Gate` | `45.43%` | `54.57%` | `0.83` | 35,070,000.00 USD |
| `4H` | `Bitget` | `45.26%` | `54.74%` | `0.83` | 74,460,000.00 USD |
| `4H` | `BingX` | `37.56%` | `62.44%` | `0.60` | 24,670,000.00 USD |
| `4H` | `MEXC` | `44.3%` | `55.7%` | `0.80` | 143,290,000.00 USD |
| `4H` | `Bitunix` | `45.68%` | `54.32%` | `0.84` | 58,400,000.00 USD |
| `4H` | `Hyperliquid` | `45.44%` | `54.56%` | `0.83` | 73,080,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.25%` | `50.75%` | `0.97` | 6,170,000.00 USD |
| `4H` | `Crypto.com` | `54.89%` | `45.11%` | `1.22` | 2,550,000.00 USD |
| `4H` | `WhiteBIT` | `95.24%` | `4.76%` | `20.01` | 24,430,000.00 USD |
| `4H` | `HTX` | `52.21%` | `47.79%` | `1.09` | 993,680.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.12%` | `50.88%` | `0.97` | 8,260,000.00 USD |
| `4H` | `Aster` | `44.57%` | `55.43%` | `0.80` | 14,180,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.68%` | `49.32%` | `1.03` | 2,080,000.00 USD |
| `4H` | `Whale Positions` | `46.27%` | `53.73%` | `0.86` | 585,430,000.00 USD |
| `4H` | `Global Accounts` | `45.93%` | `54.07%` | `0.85` | 1,500,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `96.92` | `97.64` | `96.92` | `99.58` | `96.22` | 192,431,903.91 USD | 82,764,009.24 USD | 109,667,894.68 USD | -26,903,885.44 USD | `-13.98%` | `3B / 37S` |
| `5:00 UTC` | `96.70` | `96.08` | `96.70` | `97.16` | `94.82` | 215,726,671.39 USD | 100,520,655.67 USD | 115,206,015.72 USD | -14,685,360.05 USD | `-6.81%` | `2B / 14S` |
| `0:00 UTC` | `95.81` | `96.26` | `95.81` | `97.12` | `95.34` | 129,728,839.74 USD | 65,325,713.62 USD | 64,403,126.12 USD | 922,587.50 USD | `+0.71%` | `8B / 11S` |
| `5:00 UTC` | `97.38` | `97.38` | `97.38` | `97.88` | `96.80` | 101,047,979.53 USD | 36,621,270.69 USD | 64,426,708.83 USD | -27,805,438.14 USD | `-27.52%` | `3B / 13S` |
| `0:00 UTC` | `97.82` | `97.78` | `97.82` | `98.05` | `97.22` | 66,557,018.60 USD | 21,423,499.46 USD | 45,133,519.15 USD | -23,710,019.69 USD | `-35.62%` | `8B / 8S` |
| `5:00 UTC` | `97.38` | `97.35` | `97.38` | `97.77` | `97.00` | 50,034,040.48 USD | 24,592,177.20 USD | 25,441,863.28 USD | -849,686.07 USD | `-1.70%` | `18B / 3S` |
| `0:00 UTC` | `97.18` | `97.24` | `97.18` | `97.81` | `96.45` | 125,028,825.31 USD | 50,577,751.56 USD | 74,451,073.75 USD | -23,873,322.19 USD | `-19.09%` | `23B / 8S` |
| `5:00 UTC` | `97.41` | `97.23` | `97.41` | `97.50` | `96.77` | 61,370,185.01 USD | 39,379,012.75 USD | 21,991,172.26 USD | 17,387,840.49 USD | `+28.33%` | `8B / 1S` |
| `0:00 UTC` | `97.75` | `97.54` | `97.75` | `97.82` | `97.10` | 42,753,332.88 USD | 17,911,041.19 USD | 24,842,291.69 USD | -6,931,250.50 USD | `-16.21%` | `13B / 2S` |
| `5:00 UTC` | `97.12` | `97.13` | `97.12` | `97.41` | `96.90` | 12,613,283.30 USD | 6,017,909.02 USD | 6,595,374.29 USD | -577,465.27 USD | `-4.58%` | `6B / 11S` |

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
| `5m` | -1,600,000.00 USD | -4,950,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,980,000.00 USD | -18,960,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -6,370,000.00 USD | -7,410,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -21,230,000.00 USD | -27,240,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -28,000,000.00 USD | -143,190,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -57,300,000.00 USD | -284,780,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -62,160,000.00 USD | -322,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -53,170,000.00 USD | -311,890,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -45,210,000.00 USD | -351,240,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -38,040,000.00 USD | -380,340,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 31,990,000.00 USD | -578,500,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 4,220,000.00 USD | -2,150,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.60M` | 15m=`-3.98M` | 1h=`-21.23M` | 24h=`-38.04M`
* Futures Capital Netflows: 5m=`-4.95M` | 15m=`-18.96M` | 1h=`-27.24M` | 24h=`-380.34M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `96.54` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `94.98` (Risk Distance: `1.56` pts)
  * +2.5R Take Profit: `100.43`
  * Mathematical Lot Sizing: **`6.42 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `97.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.00` (Risk Distance: `1.56` pts)
  * +2.5R Take Profit: `93.55`
  * Mathematical Lot Sizing: **`6.42 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
