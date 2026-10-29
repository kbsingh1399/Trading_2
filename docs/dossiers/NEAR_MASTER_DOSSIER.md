# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:29:18 IST` (`2026-10-29 18:59:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.43` | **Live Ask Quote**: `4.46` | **Mid Price**: `4.44`
- **Spread Points**: `29.00` | **Spread BPS**: `65.26 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `4.47` | VWAP Z-Score: `-0.75` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0506` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `36.94` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.76` | Lower -3.00σ Band: `4.18`
  * Upper +2.51σ Band: `4.71` | Lower -2.51σ Band: `4.23`
  * Upper +2.01σ Band: `4.67` | Lower -2.01σ Band: `4.27`
  * Upper +2.00σ Band: `4.66` | Lower -2.00σ Band: `4.28`
  * Upper +1.28σ Band: `4.59` | Lower -1.28σ Band: `4.35`
  * Upper +1.00σ Band: `4.57` | Lower -1.00σ Band: `4.37`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.49` | EMA-20=`4.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.48` (Slope: `+0.0000`) | EMA-100=`4.50`
  * Institutional Anchors: EMA-144=`4.51` | EMA-200=`4.52` (Slope: `+0.0425`) | EMA-233=`4.52`
- **Range Boundaries**: 24H High=`4.80` | 24H Low=`4.27` | Weekly High=`4.80` | Weekly Low=`4.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.63` (Distance: `-4.10%`)
  * Point of Control (POC) = `4.41` (Distance: `+0.67%`)
  * Value Area Low (VAL) = `4.38` (Distance: `+1.27%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.73` | POC=`4.68` | VAL=`4.61`
  * Prior Day Extremes: PDH=`4.80` | PDL=`4.53` | PDC=`4.71`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.62` | Weekly POC=`4.44` | Weekly VAL=`4.41`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.75` | Low=`4.39`
  * London Session (08:00-16:00 UTC): High=`4.50` | Low=`4.27`
  * New York Session (13:00-21:00 UTC): High=`4.67` | Low=`4.34`
  * Initial Balance (First Hour): IB High=`4.50` | IB Low=`4.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.43` - `4.46`
  * Optimal Trade Entry (OTE 0.705): `4.45`
  * Structural Invalidation Anchor (0.786): `4.48`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.42` | `4.42` | `4.40` | `4.41` | `494,780` | 2,183,569.54 USD | -10,544.74 USD | `-0.48%` | -29,467,875.69 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `4.41` | `4.42` | `4.39` | `4.42` | `732,709` | 3,228,932.99 USD | 672,880.37 USD | `+20.84%` | -28,794,995.32 USD | `+0.99` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.42` | `4.45` | `4.42` | `4.44` | `634,458` | 2,812,877.88 USD | -315,206.03 USD | `-11.21%` | -29,110,201.35 USD | `-0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.49` | `4.50` | `4.45` | `4.46` | `747,879` | 3,346,103.47 USD | 444,727.76 USD | `+13.29%` | -28,697,392.56 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.46` | `4.46` | `4.40` | `4.41` | `2,172,637` | 9,612,896.64 USD | -859,583.93 USD | `-8.94%` | -29,556,976.49 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.41` | `4.45` | `4.39` | `4.44` | `1,365,987` | 6,036,573.99 USD | 362,520.59 USD | `+6.01%` | -29,194,455.90 USD | `+0.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.65` | `4.69` | `4.58` | `4.60` | `10,150,684` | 46,941,765.94 USD | -4,168,368.77 USD | `-8.88%` | -28,053,243.38 USD | `-0.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.60` | `4.60` | `4.45` | `4.50` | `7,767,140` | 35,143,644.65 USD | -731,523.30 USD | `-2.08%` | -28,784,766.68 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.50` | `4.51` | `4.39` | `4.44` | `5,528,546` | 24,575,783.74 USD | -409,689.22 USD | `-1.67%` | -29,194,455.90 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -32,636,174.80 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -28,227,147.70 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.39` | `4.44` | `23,447,550` | 106,666,431.21 USD | -5,314,427.54 USD | `-4.98%` | -33,541,575.24 USD | `+0.04` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.73` | `4.73` | `4.40` | `4.42` | `25,745,501` | 116,497,184.49 USD | -11,801,514.25 USD | `-10.13%` | -15,870,340.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -31,542,465.78 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -32,636,174.80 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -28,227,147.70 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.39` | `4.44` | `23,447,550` | 106,666,431.21 USD | -5,314,427.54 USD | `-4.98%` | -33,541,575.24 USD | `+0.04` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `58` | `0x7737...bf66` | `LONG` | 25,078,241.11 USD | `5,640,376.30` | `2.35` | `4.45` | `0.9405` | 11,806,338.28 USD | `+47.08%` | `10X Cross` |
| `128` | `0xb581...6f4f` | `LONG` | 15,986,880.00 USD | `3,600,000.00` | `5.19` | `4.45` | `0.000000` | -2,706,155.22 USD | `-16.93%` | `4X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,657,137.34 USD | `2,400,202.10` | `2.31` | `4.45` | `26.72` | -5,111,733.46 USD | `-47.97%` | `3X Cross` |
| `265` | `0x77ee...2902` | `LONG` | 9,156,934.33 USD | `2,063,023.10` | `1.93` | `4.45` | `0.3785` | 5,165,738.40 USD | `+56.41%` | `10X Cross` |
| `270` | `0xefe4...194b` | `SHORT` | 8,970,903.26 USD | `2,019,882.30` | `4.44` | `4.45` | `11.44` | 4,181.90 USD | `+0.05%` | `5X Cross` |
| `379` | `0xb83d...6e36` | `SHORT` | 6,421,902.89 USD | `1,445,759.10` | `5.19` | `4.45` | `90.97` | 1,087,546.05 USD | `+16.93%` | `3X Cross` |
| `402` | `0xb46b...538e` | `SHORT` | 5,931,973.60 USD | `1,336,000.00` | `4.33` | `4.45` | `7.22` | -147,109.54 USD | `-2.48%` | `10X Cross` |
| `422` | `0x9df2...c665` | `SHORT` | 5,618,990.85 USD | `1,265,000.00` | `2.03` | `4.45` | `26.53` | -3,052,308.51 USD | `-54.32%` | `10X Cross` |
| `431` | `0xb695...a92d` | `SHORT` | 5,476,521.02 USD | `1,233,422.90` | `4.57` | `4.45` | `26.28` | 164,215.90 USD | `+3.00%` | `10X Cross` |
| `466` | `0x60b0...991e` | `LONG` | 4,980,061.22 USD | `1,121,307.10` | `5.00` | `4.45` | `0.000000` | -621,363.21 USD | `-12.48%` | `10X Cross` |
| `484` | `0xcac1...26b3` | `SHORT` | 4,767,240.38 USD | `1,073,743.90` | `2.48` | `4.45` | `11.58` | -2,107,296.92 USD | `-44.20%` | `10X Cross` |
| `501` | `0x781e...96b7` | `SHORT` | 4,610,646.40 USD | `1,039,604.60` | `2.45` | `4.45` | `7.48` | -2,066,309.21 USD | `-44.82%` | `10X Cross` |
| `517` | `0xdf60...d3c7` | `LONG` | 4,440,900.00 USD | `1,000,000.00` | `4.70` | `4.45` | `3.91` | -258,377.29 USD | `-5.82%` | `8X Isolated` |
| `575` | `0x45d2...4029` | `SHORT` | 4,036,008.14 USD | `909,400.00` | `3.26` | `4.45` | `42.63` | -1,069,858.24 USD | `-26.51%` | `10X Cross` |
| `583` | `0x4cae...7c34` | `LONG` | 3,995,485.31 USD | `900,086.80` | `3.52` | `4.45` | `1.79` | 823,084.32 USD | `+20.60%` | `10X Cross` |
| `730` | `0x9aa5...58af` | `SHORT` | 3,214,458.32 USD | `723,977.10` | `4.78` | `4.45` | `14.66` | 245,174.87 USD | `+7.63%` | `10X Cross` |
| `811` | `0x005a...61fe` | `LONG` | 2,896,609.91 USD | `652,414.60` | `2.08` | `4.45` | `2.33` | 1,539,078.68 USD | `+53.13%` | `7X Cross` |
| `816` | `0xba5d...a352` | `SHORT` | 2,874,914.79 USD | `647,532.50` | `2.83` | `4.45` | `12.41` | -1,042,199.85 USD | `-36.25%` | `10X Cross` |
| `830` | `0xd1dd...9e85` | `SHORT` | 2,830,144.57 USD | `637,621.00` | `4.96` | `4.45` | `16.57` | 333,328.17 USD | `+11.78%` | `10X Cross` |
| `832` | `0x123d...3bff` | `SHORT` | 2,825,007.45 USD | `636,076.70` | `2.09` | `4.45` | `8.98` | -1,497,630.76 USD | `-53.01%` | `10X Cross` |
| `848` | `0xcf53...ee11` | `SHORT` | 2,757,410.50 USD | `621,598.40` | `5.07` | `4.45` | `24.14` | 394,759.75 USD | `+14.32%` | `10X Cross` |
| `944` | `0x5647...e7de` | `SHORT` | 2,422,546.65 USD | `545,864.50` | `4.69` | `4.45` | `12.47` | 136,044.80 USD | `+5.62%` | `10X Cross` |
| `953` | `0xfc66...ca06` | `SHORT` | 2,398,624.16 USD | `540,218.50` | `4.60` | `4.45` | `66.43` | 83,950.42 USD | `+3.50%` | `10X Cross` |
| `968` | `0xbfc7...80b4` | `SHORT` | 2,356,418.70 USD | `531,000.00` | `2.01` | `4.45` | `12.68` | -1,291,219.31 USD | `-54.80%` | `10X Cross` |
| `1061` | `0xef96...9383` | `SHORT` | 2,120,970.59 USD | `477,459.50` | `4.50` | `4.45` | `12.25` | 28,927.61 USD | `+1.36%` | `10X Cross` |
| `1072` | `0x7fda...17d1` | `SHORT` | 2,099,145.62 USD | `472,546.40` | `4.83` | `4.45` | `75.82` | 181,357.99 USD | `+8.64%` | `10X Cross` |
| `1289` | `0xe097...d0fe` | `LONG` | 1,774,880.00 USD | `400,000.00` | `5.29` | `4.45` | `0.000000` | -341,907.30 USD | `-19.26%` | `10X Cross` |
| `1421` | `0xdf95...7d72` | `SHORT` | 1,611,072.57 USD | `362,348.20` | `4.23` | `4.45` | `101.26` | -77,478.86 USD | `-4.81%` | `10X Cross` |
| `1427` | `0x6e8f...4364` | `LONG` | 1,604,457.31 USD | `361,210.50` | `3.28` | `4.45` | `3.29` | 420,397.08 USD | `+26.20%` | `10X Cross` |
| `1463` | `0xcf67...eb24` | `LONG` | 1,554,770.00 USD | `350,000.00` | `1.98` | `4.45` | `1.03` | 863,152.12 USD | `+55.52%` | `10X Cross` |
| `1559` | `0x590f...be1d` | `SHORT` | 1,431,065.40 USD | `322,675.40` | `4.53` | `4.45` | `4.84` | 31,968.91 USD | `+2.23%` | `10X Cross` |
| `1573` | `0xfc27...9d9d` | `SHORT` | 1,421,205.78 USD | `319,997.70` | `5.01` | `4.45` | `48.04` | 182,336.84 USD | `+12.83%` | `10X Cross` |
| `1701` | `0xe065...0f85` | `SHORT` | 1,289,250.38 USD | `290,227.90` | `2.81` | `4.45` | `6.28` | -472,506.13 USD | `-36.65%` | `10X Cross` |
| `1705` | `0x023a...2355` | `SHORT` | 1,287,083.92 USD | `289,740.20` | `4.60` | `4.45` | `32.01` | 45,612.19 USD | `+3.54%` | `10X Cross` |
| `1840` | `0xb69e...033a` | `LONG` | 1,140,927.25 USD | `257,081.40` | `4.61` | `4.45` | `2.46` | -43,127.61 USD | `-3.78%` | `10X Cross` |
| `1878` | `0xff43...d924` | `LONG` | 1,107,616.89 USD | `249,474.50` | `4.64` | `4.45` | `3.28` | -50,426.79 USD | `-4.55%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.69` | 7,460.25 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.46K USD at 4.6855 USD [API] | `2026-10-27 21:45:16` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 6,073.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.07K USD at 4.6855 USD [API] | `2026-10-27 21:45:16` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 2,061.57 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 2.06K USD at 4.7899 USD [API] | `2026-10-27 21:36:29` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 52.69 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.05K USD at 4.7899 USD [API] | `2026-10-27 21:36:29` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 17.72 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 4.7899 USD [API] | `2026-10-27 21:36:29` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 10,238.18 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.24K USD at 4.7945 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 8,970.50 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.97K USD at 4.6814 USD [API] | `2026-10-27 21:58:24` |
| `ANNOUNCEMENT` | `INFO` | `4.80` | 8,264.72 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 8.26K USD at 4.8020 USD [API] | `2026-10-27 21:38:12` |
| `ANNOUNCEMENT` | `INFO` | `4.80` | 9,012.08 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.01K USD at 4.7957 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 5,008.79 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.01K USD at 4.6798 USD [API] | `2026-10-27 22:04:55` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 7,438.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.44K USD at 4.6577 USD [API] | `2026-10-27 22:09:24` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 5,026.59 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.03K USD at 4.6577 USD [API] | `2026-10-27 22:09:23` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.84` (Vol: 505,500.00 USD, Dist: `+8.45%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--4.38%`)
  * 48H Horizon: Short MP=`4.83` (Vol: 541,200.00 USD, Dist: `+8.33%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--4.38%`)
  * 3D Horizon: Short MP=`4.83` (Vol: 541,200.00 USD, Dist: `+8.33%`) | Long MP=`4.26` (Vol: 618,400.00 USD, Dist: `--4.38%`)
  * 7D Horizon: Short MP=`5.02` (Vol: 897,800.00 USD, Dist: `+12.67%`) | Long MP=`4.23` (Vol: 1,400,000.00 USD, Dist: `--5.13%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8950` | 39,670.00 USD | 34,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 11,240.00 USD | 34,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 10,170.00 USD | 34,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 5,330,000.00 USD | 34,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 342,520.00 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 1,160.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 30,370.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,330.00 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 1,020.00 USD | 28,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 28,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,200.00 USD | 28,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 7,890.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 1,720.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 69,010.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 20,230.00 USD | 28,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 73,400.00 USD | 28,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 3,020.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 30,520.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 28,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 53,830.00 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 2,590.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 11,930.00 USD | 28,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 238.19 USD | 28,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 11,220.00 USD | 28,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 6,040.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 9,420.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,720.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 985.90 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 4,240.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 653.98 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 9,760.00 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 782.61 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 117.56 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 2,830.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 3,390.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 371.13 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 1,200.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 15,710.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 157.50 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 758.84 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 53,190.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 18,780.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 226.29 USD | 27,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.49` | 276.06 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,200.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 9,540.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 221.12 USD | 27,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 27,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 2,560.00 USD | 27,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 13,300.00 USD | 27,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 4,620.00 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 5,380.00 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 308.32 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 1,050.00 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,030.00 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 384.13 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 2,600.00 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 231.48 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 14,180.00 USD | 27,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 1,960.00 USD | 27,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 569.64 USD | 27,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,730.00 USD | 27,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 14,160.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 200,030.00 USD | 27,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 1,630,000.00 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 32,790.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 9,710.00 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 8,190.00 USD | 25,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 2,290.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 80,400.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 2,450.00 USD | 25,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 32,160.00 USD | 25,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,080.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 4,130.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 279.38 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 76,440.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 2,130.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,350.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 10,950.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 362.48 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 2,820.00 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 198,010.00 USD | 25,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 301,790.00 USD | 25,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 43,680.00 USD | 25,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 86,570.00 USD | 25,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 122,770.00 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 1,270.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 87,780.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 455.95 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 3,750.00 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 15,250.00 USD | 24,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 2,060.00 USD | 24,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 11,830.00 USD | 24,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 15,110.00 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 4,560.00 USD | 24,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 29,050.00 USD | 24,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 594.13 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 3,910.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 24,570.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 11,180.00 USD | 24,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 24,300.00 USD | 24,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 4,450.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 30,830.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 117,150.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 3,430.00 USD | 24,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 2,030.00 USD | 24,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 10,010.00 USD | 24,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 2,380.00 USD | 24,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,240.00 USD | 24,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,250.00 USD | 24,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 1,580,000.00 USD | 24,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 3,520.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 48,780.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,770.00 USD | 22,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 63,000.00 USD | 22,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 569,200.00 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 9,960.00 USD | 22,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 378.65 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 2,310.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 185,860.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 388,800.00 USD | 22,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 4,140.00 USD | 21,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 5,440.00 USD | 21,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 11,310.00 USD | 21,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 915,870.00 USD | 21,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 20,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 2,040.00 USD | 20,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,490.00 USD | 20,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 37,490.00 USD | 20,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 2,140.00 USD | 20,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 18,780.00 USD | 20,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 694.96 USD | 20,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 8,790.00 USD | 20,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 12,880.00 USD | 20,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,340.00 USD | 20,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 72,060.00 USD | 20,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 8,480.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 12,890.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 48,970.00 USD | 20,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 7,170.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 20,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 19,550.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 11,920.00 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 212,560.00 USD | 20,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 6,320.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 119,930.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,750.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 36,890.00 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 13,690.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,550.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 13,930.00 USD | 19,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 191,000.00 USD | 19,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 2,140.00 USD | 19,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,840.00 USD | 19,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 15,940.00 USD | 19,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 6,190.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 1,150.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,240.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,140.00 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 180.94 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 5,800.00 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 5,190.00 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 2,540.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 6,600.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,910.00 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 27,650.00 USD | 19,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 143,730.00 USD | 19,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 37,780.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 15,090.00 USD | 19,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 560,970.00 USD | 19,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 13,700.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 72,980.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 7,990.00 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 30,320.00 USD | 18,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 18,390.00 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 17,780.00 USD | 18,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 386,180.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 103,780.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 22,850.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,950.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 3,230.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 12,020.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 25,600.00 USD | 18,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 25,200.00 USD | 18,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 80,320.00 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,940.00 USD | 17,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 39,110.00 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 116,280.00 USD | 17,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,300.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 7,150.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 96,740.00 USD | 17,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 6,870.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 4,400.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 103,750.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 28,330.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,020.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 20,660.00 USD | 17,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 274,600.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 70,660.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 44,450.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 839,940.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 6,650.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,420,000.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 60,770.00 USD | 14,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 26,680.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 8,730.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 51,640.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 26,150.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 10,480.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 3,550.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 29,990.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 43,640.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 1,970.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 110,220.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 194,840.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 52,030.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 27,230.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 45,120.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 55,190.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 11,280.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 77,730.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 11,350.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 24,910.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 22,250.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 26,620.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 7,430.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 4,110.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 324,630.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 375,650.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 3,200.00 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 124,650.00 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 25,270.00 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 25,500.00 USD | 13,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 154,720.00 USD | 13,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 523,230.00 USD | 12,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 25,050.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 39,840.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 508,750.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 33,110.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 44,710.00 USD | 11,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 189,590.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 214,140.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 117,240.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 25,370.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 41,120.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 27,300.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 6,340.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 23,730.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 100,660.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 63,870.00 USD | 10,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 14,510.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 38,120.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 124,270.00 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 14,720.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 77,530.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 5,180.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 170,490.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 22,270.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 21,460.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.86` | 32,740,000.00 USD | 32,740,000.00 USD | 2,220.00 USD | 0.00 USD | 72,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 22,840.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.87` | 32,670,000.00 USD | 32,670,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 138,250.00 USD | 10,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.88` | 32,580,000.00 USD | 32,580,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 31,160.00 USD | 10,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.89` | 32,370,000.00 USD | 32,370,000.00 USD | 1,210.00 USD | 50,710.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 94,560.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.90` | 32,310,000.00 USD | 32,310,000.00 USD | 92,100.00 USD | 28,250.00 USD | 48,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 6,040.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.91` | 32,140,000.00 USD | 32,140,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,920,000.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.92` | 32,070,000.00 USD | 32,070,000.00 USD | 90,780.00 USD | 41,330.00 USD | 80,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 200,060.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.93` | 31,860,000.00 USD | 31,860,000.00 USD | 51,660.00 USD | 26,290.00 USD | 50,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 20,840.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 18,990,000.00 USD | 18,990,000.00 USD | 0.00 USD | 24,580.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 31,730,000.00 USD | 31,730,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 534,170.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 18,940,000.00 USD | 18,940,000.00 USD | 12,850.00 USD | 5,610.00 USD | 20.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 31,490,000.00 USD | 31,490,000.00 USD | 8,490.00 USD | 26,060.00 USD | 365.10 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 13,470.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 18,920,000.00 USD | 18,920,000.00 USD | 23,520.00 USD | 22,140.00 USD | 34,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 31,460,000.00 USD | 31,460,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 107,600.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 18,840,000.00 USD | 18,840,000.00 USD | 110,310.00 USD | 47,530.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 31,240,000.00 USD | 31,240,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 39,580.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 18,630,000.00 USD | 18,630,000.00 USD | 46,710.00 USD | 30,290.00 USD | 10,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 30,630,000.00 USD | 30,630,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 161,330.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 18,540,000.00 USD | 18,540,000.00 USD | 93,820.00 USD | 12,310.00 USD | 34,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 30,430,000.00 USD | 30,430,000.00 USD | 63,200.00 USD | 82,870.00 USD | 101,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 36,460.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 18,400,000.00 USD | 18,400,000.00 USD | 9,730.00 USD | 7,330.00 USD | 19,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 30,180,000.00 USD | 30,180,000.00 USD | 317,210.00 USD | 105,220.00 USD | 166,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 59,840.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 18,370,000.00 USD | 18,370,000.00 USD | 109,160.00 USD | 56,050.00 USD | 73,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 29,590,000.00 USD | 29,590,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 12,850.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 18,130,000.00 USD | 18,130,000.00 USD | 60,540.00 USD | 20,960.00 USD | 75,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 28,680,000.00 USD | 28,680,000.00 USD | 279,800.00 USD | 88,330.00 USD | 195,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 109,260.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 17,970,000.00 USD | 17,970,000.00 USD | 23,550.00 USD | 40,450.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 28,110,000.00 USD | 28,110,000.00 USD | 250,870.00 USD | 45,290.00 USD | 150,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 24,850.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 17,870,000.00 USD | 17,870,000.00 USD | 28,720.00 USD | 32,610.00 USD | 127,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 27,670,000.00 USD | 27,670,000.00 USD | 98,660.00 USD | 65,670.00 USD | 120,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 33,120.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 17,680,000.00 USD | 17,680,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 27,380,000.00 USD | 27,380,000.00 USD | 184,470.00 USD | 72,110.00 USD | 86,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 82,940.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 17,580,000.00 USD | 17,580,000.00 USD | 56,470.00 USD | 0.00 USD | 22,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 27,040,000.00 USD | 27,040,000.00 USD | 198,550.00 USD | 45,470.00 USD | 125,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 376,550.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 17,500,000.00 USD | 17,500,000.00 USD | 3,220.00 USD | 15,020.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 26,670,000.00 USD | 26,670,000.00 USD | 183,890.00 USD | 35,750.00 USD | 41,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 268,550.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 17,460,000.00 USD | 17,460,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 26,410,000.00 USD | 26,410,000.00 USD | 9,180.00 USD | 63,440.00 USD | 231,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 304,210.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 17,420,000.00 USD | 17,420,000.00 USD | 10,180.00 USD | 6,980.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 26,110,000.00 USD | 26,110,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 721,610.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 17,410,000.00 USD | 17,410,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 25,900,000.00 USD | 25,900,000.00 USD | 158,760.00 USD | 118,310.00 USD | 347,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 112,820.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 17,300,000.00 USD | 17,300,000.00 USD | 22,520.00 USD | 18,800.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 25,280,000.00 USD | 25,280,000.00 USD | 110,780.00 USD | 0.00 USD | 84,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 254,610.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 17,250,000.00 USD | 17,250,000.00 USD | 4,070.00 USD | 41,500.00 USD | 134,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 25,080,000.00 USD | 25,080,000.00 USD | 97,300.00 USD | 48,940.00 USD | 342,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 45,150.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 17,070,000.00 USD | 17,070,000.00 USD | 39,380.00 USD | 55,060.00 USD | 23,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 24,590,000.00 USD | 24,590,000.00 USD | 293,300.00 USD | 79,100.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 77,110.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 16,950,000.00 USD | 16,950,000.00 USD | 194,940.00 USD | 36,950.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 24,120,000.00 USD | 24,120,000.00 USD | 374,290.00 USD | 57,440.00 USD | 219,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 101,060.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 16,570,000.00 USD | 16,570,000.00 USD | 201,620.00 USD | 84,150.00 USD | 79,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 23,460,000.00 USD | 23,460,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 54,150.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 16,210,000.00 USD | 16,210,000.00 USD | 62,770.00 USD | 99,580.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 22,810,000.00 USD | 22,810,000.00 USD | 310,530.00 USD | 192,570.00 USD | 175,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 315,620.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 15,950,000.00 USD | 15,950,000.00 USD | 44,430.00 USD | 104,170.00 USD | 89,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 22,140,000.00 USD | 22,140,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 15,950.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.18` | 15,710,000.00 USD | 15,710,000.00 USD | 120,410.00 USD | 30,730.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 21,450,000.00 USD | 21,450,000.00 USD | 360,840.00 USD | 103,320.00 USD | 57,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.18` | 370,570.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.19` | 15,500,000.00 USD | 15,500,000.00 USD | 288,170.00 USD | 79,350.00 USD | 145,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 20,930,000.00 USD | 20,930,000.00 USD | 215,210.00 USD | 113,960.00 USD | 672,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.20` | 248,620.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.20` | 14,990,000.00 USD | 14,990,000.00 USD | 92,210.00 USD | 162,810.00 USD | 486,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 19,930,000.00 USD | 19,930,000.00 USD | 337,660.00 USD | 122,960.00 USD | 883,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 284,680.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.21` | 14,250,000.00 USD | 14,250,000.00 USD | 70,020.00 USD | 118,560.00 USD | 977.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 18,580,000.00 USD | 18,580,000.00 USD | 321,000.00 USD | 149,940.00 USD | 119,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 41,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 14,060,000.00 USD | 14,060,000.00 USD | 528,380.00 USD | 123,170.00 USD | 389,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 17,990,000.00 USD | 17,990,000.00 USD | 853,600.00 USD | 161,970.00 USD | 786,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.22` | 471,560.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.23` | 13,020,000.00 USD | 13,020,000.00 USD | 777,240.00 USD | 345,510.00 USD | 375,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 16,190,000.00 USD | 16,190,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 740,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.24` | 83,020.00 USD | 709,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.24` | 11,520,000.00 USD | 11,520,000.00 USD | 281,780.00 USD | 220,350.00 USD | 260,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 13,650,000.00 USD | 13,650,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 13,710.00 USD | 626,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.25` | 10,760,000.00 USD | 10,760,000.00 USD | 426,030.00 USD | 239,130.00 USD | 413,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 11,930,000.00 USD | 11,930,000.00 USD | 350,470.00 USD | 433,770.00 USD | 653,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 274,960.00 USD | 612,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.26` | 9,680,000.00 USD | 9,680,000.00 USD | 334,790.00 USD | 114,720.00 USD | 281,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 10,500,000.00 USD | 10,500,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 357,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.26` | 47,120.00 USD | 337,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.27` | 8,950,000.00 USD | 8,950,000.00 USD | 626,730.00 USD | 199,830.00 USD | 464,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 8,100,000.00 USD | 8,100,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 31,480.00 USD | 31,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 7,660,000.00 USD | 7,660,000.00 USD | 320,200.00 USD | 294,950.00 USD | 214,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 5,680,000.00 USD | 5,680,000.00 USD | 842,270.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 10,850.00 USD | 290,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.29` | 6,830,000.00 USD | 6,830,000.00 USD | 289,680.00 USD | 37,190.00 USD | 247,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 3,230,000.00 USD | 3,230,000.00 USD | 9,100.00 USD | 46,530.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 11,380.00 USD | 42,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.30` | 6,250,000.00 USD | 6,250,000.00 USD | 293,470.00 USD | 160,930.00 USD | 56,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.30` | 3,170,000.00 USD | 3,170,000.00 USD | 3,500.00 USD | 90,090.00 USD | 79,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.30` | 11,670.00 USD | 279,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.31` | 5,740,000.00 USD | 5,740,000.00 USD | 300,730.00 USD | 186,670.00 USD | 465,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.31` | 3,000,000.00 USD | 3,000,000.00 USD | 88,750.00 USD | 0.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 4,170.00 USD | 47,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 4,790,000.00 USD | 4,790,000.00 USD | 431,560.00 USD | 132,350.00 USD | 193,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 2,860,000.00 USD | 2,860,000.00 USD | 169,820.00 USD | 158,570.00 USD | 78,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 43,570.00 USD | 268,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.33` | 4,030,000.00 USD | 4,030,000.00 USD | 373,930.00 USD | 85,110.00 USD | 155,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.33` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 112,660.00 USD | 89,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 12,880.00 USD | 224,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.34` | 3,420,000.00 USD | 3,420,000.00 USD | 269,670.00 USD | 123,090.00 USD | 342,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 2,260,000.00 USD | 2,260,000.00 USD | 75,930.00 USD | 161,050.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.34` | 30,420.00 USD | 211,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.35` | 2,680,000.00 USD | 2,680,000.00 USD | 117,840.00 USD | 83,060.00 USD | 143,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.35` | 1,880,000.00 USD | 1,880,000.00 USD | 362,610.00 USD | 39,140.00 USD | 89,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.36` | 1,550.00 USD | 181,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.36` | 2,340,000.00 USD | 2,340,000.00 USD | 82,150.00 USD | 51,640.00 USD | 118,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.36` | 1,390,000.00 USD | 1,390,000.00 USD | 5,210.00 USD | 0.00 USD | 88,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.37` | 10,330.00 USD | 179,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.37` | 2,090,000.00 USD | 2,090,000.00 USD | 52,120.00 USD | 66,510.00 USD | 82,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.37` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 538.42 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 126,420.00 USD | 169,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.38` | 1,890,000.00 USD | 1,890,000.00 USD | 171,480.00 USD | 81,750.00 USD | 476,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.38` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 141,930.00 USD | 263,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 7,460.00 USD | 42,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.39` | 1,160,000.00 USD | 1,160,000.00 USD | 206,130.00 USD | 288,340.00 USD | 199,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.39` | 888,950.00 USD | 888,950.00 USD | 0.00 USD | 62,850.00 USD | 153,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.39` | 14,870.00 USD | 35,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.40` | 462,230.00 USD | 462,230.00 USD | 0.00 USD | 0.00 USD | 462,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.40` | 672,310.00 USD | 672,310.00 USD | 0.00 USD | 0.00 USD | 401,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.41` | 355.92 USD | 20,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 72,170.00 USD | 72,170.00 USD | 1,720.00 USD | 0.00 USD | 70,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 144,350.00 USD | 144,350.00 USD | 1,720.00 USD | 0.00 USD | 70,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.41` | 270,480.00 USD | 270,480.00 USD | 0.00 USD | 0.00 USD | 270,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.42` | 665.34 USD | 20,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 220,240.00 USD | 220,240.00 USD | 0.00 USD | 0.00 USD | 75,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 182,060.00 USD | 182,060.00 USD | 6,060.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 364,110.00 USD | 364,110.00 USD | 6,060.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.42` | 9,760.00 USD | 19,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 323,540.00 USD | 323,540.00 USD | 0.00 USD | 103,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 481,480.00 USD | 481,480.00 USD | 0.00 USD | 46,230.00 USD | 71,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.43` | 970.38 USD | 9,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 1,110,000.00 USD | 1,110,000.00 USD | 259,230.00 USD | 282,030.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 669,950.00 USD | 669,950.00 USD | 0.00 USD | 116,400.00 USD | 72,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.45` | 4,260.00 USD | 8,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 34,890.00 USD | 6.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 732,060.00 USD | 732,060.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 1,000,000.00 USD | 1,000,000.00 USD | 132,630.00 USD | 135,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.49` | 2,130.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 1,350,000.00 USD | 1,350,000.00 USD | 49,360.00 USD | 77,810.00 USD | 84,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 1,340,000.00 USD | 1,340,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.50` | 1,520,000.00 USD | 1,520,000.00 USD | 129,140.00 USD | 41,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 1,670,000.00 USD | 1,670,000.00 USD | 169,820.00 USD | 164,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.50` | 2,450.00 USD | 2,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 2,170,000.00 USD | 2,170,000.00 USD | 162,900.00 USD | 282,880.00 USD | 200,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 2,520,000.00 USD | 2,520,000.00 USD | 189,070.00 USD | 44,490.00 USD | 118,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 33,490.00 USD | 80,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 3,110,000.00 USD | 3,110,000.00 USD | 306,530.00 USD | 0.00 USD | 278,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 2,720,000.00 USD | 2,720,000.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 150,600.00 USD | 702,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.55` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 22,540.00 USD | 315,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 4,690,000.00 USD | 4,690,000.00 USD | 79,110.00 USD | 24,450.00 USD | 288,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 4,440,000.00 USD | 4,440,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 4,930,000.00 USD | 4,930,000.00 USD | 135,640.00 USD | 42,070.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 4,790,000.00 USD | 4,790,000.00 USD | 198,050.00 USD | 0.00 USD | 151,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 6,160,000.00 USD | 6,160,000.00 USD | 380,450.00 USD | 25,260.00 USD | 823,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 4,920,000.00 USD | 4,920,000.00 USD | 44,380.00 USD | 0.00 USD | 85,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 6,940,000.00 USD | 6,940,000.00 USD | 711,420.00 USD | 63,210.00 USD | 332.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 6,510,000.00 USD | 6,510,000.00 USD | 759,320.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 510.50 USD | 81,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 7,100,000.00 USD | 7,100,000.00 USD | 53,970.00 USD | 84,420.00 USD | 25,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 6,630,000.00 USD | 6,630,000.00 USD | 3,460.00 USD | 112,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 7,200,000.00 USD | 7,200,000.00 USD | 66,620.00 USD | 0.00 USD | 26,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 6,630,000.00 USD | 6,630,000.00 USD | 3,350.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 7,230,000.00 USD | 7,230,000.00 USD | 4,840.00 USD | 31,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 6,770,000.00 USD | 6,770,000.00 USD | 134,680.00 USD | 0.00 USD | 336.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 7,230,000.00 USD | 7,230,000.00 USD | 500.90 USD | 0.00 USD | 54.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 6,980,000.00 USD | 6,980,000.00 USD | 213,490.00 USD | 0.00 USD | 272.08 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 515.41 USD | 81,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 7,640,000.00 USD | 7,640,000.00 USD | 332,240.00 USD | 11,270.00 USD | 61,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 7,480,000.00 USD | 7,480,000.00 USD | 500,990.00 USD | 0.00 USD | 429.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.65` | 8,650,000.00 USD | 8,650,000.00 USD | 370,110.00 USD | 52,020.00 USD | 587,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 7,910,000.00 USD | 7,910,000.00 USD | 420,940.00 USD | 0.00 USD | 601.71 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.66` | 9,610,000.00 USD | 9,610,000.00 USD | 281,290.00 USD | 304,540.00 USD | 379,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 8,200,000.00 USD | 8,200,000.00 USD | 144,860.00 USD | 0.00 USD | 153,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.67` | 10,170,000.00 USD | 10,170,000.00 USD | 184,090.00 USD | 0.00 USD | 377,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 10,760,000.00 USD | 10,760,000.00 USD | 345,490.00 USD | 62,440.00 USD | 175,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 9,170,000.00 USD | 9,170,000.00 USD | 381,910.00 USD | 83,630.00 USD | 452,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 11,250,000.00 USD | 11,250,000.00 USD | 213,780.00 USD | 40,000.00 USD | 237,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 9,260,000.00 USD | 9,260,000.00 USD | 2,450.00 USD | 0.00 USD | 89,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.70` | 11,590,000.00 USD | 11,590,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 9,570,000.00 USD | 9,570,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 28,640.00 USD | 110,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 12,550,000.00 USD | 12,550,000.00 USD | 365,040.00 USD | 278,020.00 USD | 316,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 9,980,000.00 USD | 9,980,000.00 USD | 178,360.00 USD | 232,800.00 USD | 456.30 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 58,280.00 USD | 168,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 12,850,000.00 USD | 12,850,000.00 USD | 4,880.00 USD | 187,480.00 USD | 103,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 10,170,000.00 USD | 10,170,000.00 USD | 7,140.00 USD | 0.00 USD | 180,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 55,980.00 USD | 224,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 13,010,000.00 USD | 13,010,000.00 USD | 61,330.00 USD | 37,010.00 USD | 61,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 10,230,000.00 USD | 10,230,000.00 USD | 59,270.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 4,030.00 USD | 228,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 13,710,000.00 USD | 13,710,000.00 USD | 242,820.00 USD | 172,000.00 USD | 294,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 10,550,000.00 USD | 10,550,000.00 USD | 14,750.00 USD | 173,100.00 USD | 130,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 2,000.00 USD | 230,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 14,380,000.00 USD | 14,380,000.00 USD | 202,480.00 USD | 188,800.00 USD | 270,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 11,090,000.00 USD | 11,090,000.00 USD | 17,340.00 USD | 185,060.00 USD | 342,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 1,720.00 USD | 232,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 14,740,000.00 USD | 14,740,000.00 USD | 35,470.00 USD | 78,750.00 USD | 247,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 12,360,000.00 USD | 12,360,000.00 USD | 946,180.00 USD | 46,890.00 USD | 274,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 6,920.00 USD | 239,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 15,130,000.00 USD | 15,130,000.00 USD | 113,030.00 USD | 177,160.00 USD | 105,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 13,270,000.00 USD | 13,270,000.00 USD | 731,680.00 USD | 73,410.00 USD | 103,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 19,270.00 USD | 258,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 15,330,000.00 USD | 15,330,000.00 USD | 40,580.00 USD | 45,900.00 USD | 114,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 14,690,000.00 USD | 14,690,000.00 USD | 683,730.00 USD | 584,230.00 USD | 152,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,860.00 USD | 263,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 15,890,000.00 USD | 15,890,000.00 USD | 294,950.00 USD | 125,610.00 USD | 133,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 15,720,000.00 USD | 15,720,000.00 USD | 713,060.00 USD | 249,310.00 USD | 70,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 81,420.00 USD | 344,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 16,730,000.00 USD | 16,730,000.00 USD | 355,770.00 USD | 315,950.00 USD | 174,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 17,320,000.00 USD | 17,320,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.80` | 104.75 USD | 344,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.81` | 17,390,000.00 USD | 17,390,000.00 USD | 405,810.00 USD | 120,180.00 USD | 127,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 17,950,000.00 USD | 17,950,000.00 USD | 400,070.00 USD | 125,900.00 USD | 103,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 66,830.00 USD | 411,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 18,280,000.00 USD | 18,280,000.00 USD | 274,470.00 USD | 214,840.00 USD | 407,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 20,710,000.00 USD | 20,710,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 12,110.00 USD | 423,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 18,860,000.00 USD | 18,860,000.00 USD | 212,270.00 USD | 70,050.00 USD | 290,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 22,360,000.00 USD | 22,360,000.00 USD | 822,860.00 USD | 85,680.00 USD | 740,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 16,980.00 USD | 440,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 19,090,000.00 USD | 19,090,000.00 USD | 73,450.00 USD | 82,100.00 USD | 77,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 22,850,000.00 USD | 22,850,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 8,560.00 USD | 449,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.85` | 19,650,000.00 USD | 19,650,000.00 USD | 197,130.00 USD | 148,110.00 USD | 210,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 24,870,000.00 USD | 24,870,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.86` | 29,210.00 USD | 478,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.86` | 20,210,000.00 USD | 20,210,000.00 USD | 166,350.00 USD | 69,470.00 USD | 328,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 26,280,000.00 USD | 26,280,000.00 USD | 444,810.00 USD | 162,380.00 USD | 801,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 483,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.87` | 20,600,000.00 USD | 20,600,000.00 USD | 227,900.00 USD | 113,470.00 USD | 46,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.87` | 27,350,000.00 USD | 27,350,000.00 USD | 264,730.00 USD | 136,820.00 USD | 661,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 15,490.00 USD | 499,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.88` | 20,820,000.00 USD | 20,820,000.00 USD | 10,980.00 USD | 20,280.00 USD | 194,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 29,070,000.00 USD | 29,070,000.00 USD | 449,970.00 USD | 480,980.00 USD | 793,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 100,540.00 USD | 599,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.89` | 21,060,000.00 USD | 21,060,000.00 USD | 113,710.00 USD | 46,470.00 USD | 77,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.89` | 29,660,000.00 USD | 29,660,000.00 USD | 213,960.00 USD | 100,850.00 USD | 273,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.90` | 21,660,000.00 USD | 21,660,000.00 USD | 81,280.00 USD | 112,960.00 USD | 404,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 30,800,000.00 USD | 30,800,000.00 USD | 450,550.00 USD | 145,910.00 USD | 542,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.91` | 22,190,000.00 USD | 22,190,000.00 USD | 290,660.00 USD | 85,510.00 USD | 150,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 32,230,000.00 USD | 32,230,000.00 USD | 637,320.00 USD | 208,910.00 USD | 589,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 23,000.00 USD | 622,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.92` | 22,720,000.00 USD | 22,720,000.00 USD | 186,460.00 USD | 89,190.00 USD | 257,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.92` | 33,960,000.00 USD | 33,960,000.00 USD | 576,460.00 USD | 277,640.00 USD | 878,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 12,930.00 USD | 635,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.93` | 23,070,000.00 USD | 23,070,000.00 USD | 117,390.00 USD | 72,670.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.93` | 35,520,000.00 USD | 35,520,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 636,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.94` | 23,360,000.00 USD | 23,360,000.00 USD | 50,810.00 USD | 65,310.00 USD | 171,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.94` | 36,820,000.00 USD | 36,820,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.95` | 23,530,000.00 USD | 23,530,000.00 USD | 105,320.00 USD | 12,690.00 USD | 46,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 38,120,000.00 USD | 38,120,000.00 USD | 468,360.00 USD | 161,040.00 USD | 669,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 4,170.00 USD | 640,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.96` | 23,670,000.00 USD | 23,670,000.00 USD | 94,690.00 USD | 21,750.00 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.96` | 39,360,000.00 USD | 39,360,000.00 USD | 607,770.00 USD | 214,910.00 USD | 411,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 55,960.00 USD | 696,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.97` | 23,790,000.00 USD | 23,790,000.00 USD | 6,540.00 USD | 15,020.00 USD | 100,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 39,740,000.00 USD | 39,740,000.00 USD | 198,220.00 USD | 72,330.00 USD | 112,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 100,620.00 USD | 796,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.98` | 23,830,000.00 USD | 23,830,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.98` | 40,300,000.00 USD | 40,300,000.00 USD | 197,950.00 USD | 88,580.00 USD | 273,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 1,710.00 USD | 798,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.99` | 23,920,000.00 USD | 23,920,000.00 USD | 1,730.00 USD | 6,980.00 USD | 82,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.99` | 40,650,000.00 USD | 40,650,000.00 USD | 133,330.00 USD | 103,060.00 USD | 118,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 798,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.00` | 23,920,000.00 USD | 23,920,000.00 USD | 718.70 USD | 0.00 USD | 6.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.00` | 41,360,000.00 USD | 41,360,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 528.03 USD | 799,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.01` | 23,940,000.00 USD | 23,940,000.00 USD | 14,980.00 USD | 10,080.00 USD | 40.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 43,560,000.00 USD | 43,560,000.00 USD | 781,840.00 USD | 340,150.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.01` | 240,500.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.02` | 24,010,000.00 USD | 24,010,000.00 USD | 13,280.00 USD | 0.00 USD | 59,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 45,050,000.00 USD | 45,050,000.00 USD | 821,860.00 USD | 337,720.00 USD | 321,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `5.03` | 24,060,000.00 USD | 24,060,000.00 USD | 15,180.00 USD | 18,800.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 46,730,000.00 USD | 46,730,000.00 USD | 564,790.00 USD | 231,540.00 USD | 886,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `5.04` | 24,060,000.00 USD | 24,060,000.00 USD | 2,770.00 USD | 0.00 USD | 78.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 48,170,000.00 USD | 48,170,000.00 USD | 305,260.00 USD | 253,720.00 USD | 880,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,360.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.05` | 24,140,000.00 USD | 24,140,000.00 USD | 34,080.00 USD | 14,380.00 USD | 23,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 50,170,000.00 USD | 50,170,000.00 USD | 901,830.00 USD | 367,860.00 USD | 734,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 5,020.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.06` | 24,170,000.00 USD | 24,170,000.00 USD | 1,440.00 USD | 8,000.00 USD | 23,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.06` | 50,880,000.00 USD | 50,880,000.00 USD | 92,480.00 USD | 193,330.00 USD | 421,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 166,550.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.07` | 24,170,000.00 USD | 24,170,000.00 USD | 332.61 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.07` | 52,080,000.00 USD | 52,080,000.00 USD | 358,750.00 USD | 166,480.00 USD | 673,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 28,850.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.08` | 24,330,000.00 USD | 24,330,000.00 USD | 61,310.00 USD | 46,580.00 USD | 48,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 52,740,000.00 USD | 52,740,000.00 USD | 204,140.00 USD | 308,520.00 USD | 148,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 3,190.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 53,600,000.00 USD | 53,600,000.00 USD | 105,390.00 USD | 121,050.00 USD | 632,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.09` | 4,170.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.10` | 54,170,000.00 USD | 54,170,000.00 USD | 291,110.00 USD | 78,890.00 USD | 202,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 54,950,000.00 USD | 54,950,000.00 USD | 369,260.00 USD | 120,290.00 USD | 291,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 55,540,000.00 USD | 55,540,000.00 USD | 303,840.00 USD | 166,880.00 USD | 116,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 56,380,000.00 USD | 56,380,000.00 USD | 262,920.00 USD | 100,640.00 USD | 483,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,080.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 57,000,000.00 USD | 57,000,000.00 USD | 140,950.00 USD | 104,910.00 USD | 369,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.14` | 1,120,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.15` | 57,830,000.00 USD | 57,830,000.00 USD | 309,440.00 USD | 132,710.00 USD | 391,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 58,360,000.00 USD | 58,360,000.00 USD | 54,280.00 USD | 126,880.00 USD | 348,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 9,610.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 59,060,000.00 USD | 59,060,000.00 USD | 282,930.00 USD | 99,740.00 USD | 309,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 346.72 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.18` | 59,380,000.00 USD | 59,380,000.00 USD | 67,600.00 USD | 133,610.00 USD | 124,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.18` | 866.93 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.19` | 59,760,000.00 USD | 59,760,000.00 USD | 72,580.00 USD | 47,800.00 USD | 263,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 1,570.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 60,050,000.00 USD | 60,050,000.00 USD | 140,770.00 USD | 80,310.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.24` | 34,570.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 50,560.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 245.29 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 228.84 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 878.04 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 19,840.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 45,380.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 77,900.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 1,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 252,230.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 2,180.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 2,270.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 88,450.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 9,490.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 39,430.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 53,090.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 17,680.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.66` | 301.98 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 11,350.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 2,410.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 32,270.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 5,110.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.72` | 2,760.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.74` | 1,660,000.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 5,320.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.78` | 196.93 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 9,420.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.82` | 1,860.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 6,670.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 66,820.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 604.10 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 96,610.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.96` | 1,850.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.99` | 131.67 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 128,210.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.01` | 6,340.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.05` | 1,180,000.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 6,460.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 12,520.00 USD | 7,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 7,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.22` | 333,060.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,610.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.29` | 75,420.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 884.37 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 85,200.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 584,470.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 21,590.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 637.79 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.50` | 144.84 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 536.84 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 1,020.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 14,680.00 USD | 8,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 17,930.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 1,370.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.74` | 1,680.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.78` | 1,960.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 40,170.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,410.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 7,120.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.93` | 61,000.00 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 919.23 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 9,030.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 1,370.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 37,880.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.13` | 413,390.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.20` | 9,610,000.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.26` | 770.82 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 8,050.00 USD | 20,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.36` | 119.89 USD | 20,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 154.14 USD | 20,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 38,300.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 2,480.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,900.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 106,570.00 USD | 20,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 122,230.00 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.49` | 7,780,000.00 USD | 28,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 28,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 28,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 28,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 15,410.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 2,690.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 812.72 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 33,580.00 USD | 28,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.82` | 26,200.00 USD | 28,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 28,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 28,880.00 USD | 28,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.91` | 333,210.00 USD | 28,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 28,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 28,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.01` | 923,880.00 USD | 29,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 30,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 30,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.09` | 727,650.00 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.13` | 409,570.00 USD | 31,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.19` | 17,550.00 USD | 31,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 31,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 24,760.00 USD | 31,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 577.04 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.40` | 3,820.00 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 879.51 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 594.65 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 578.85 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 8,530.00 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 4,950.00 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.56` | 239.82 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 583.96 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.59` | 16,260.00 USD | 32,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.62` | 2,850.00 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.66` | 447,370.00 USD | 32,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 2,320.00 USD | 32,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.69` | 3,770.00 USD | 32,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.71` | 1,880,000.00 USD | 34,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.79` | 1,530,000.00 USD | 36,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.84` | 19,980.00 USD | 36,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.85` | 6,380.00 USD | 36,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.87` | 5,000.00 USD | 36,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.91` | 867.43 USD | 36,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.95` | 647,770.00 USD | 37,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.96` | 17,370.00 USD | 37,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.96` | 19,880.00 USD | 37,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.97` | 5,710,000.00 USD | 42,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.01` | 190.91 USD | 42,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.02` | 180,300.00 USD | 42,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8950` | 34,230,000.00 USD | 0.00 USD | 39,670.00 USD | `-80.14%` | `44,325.10` |
| `Live` | `Long` | `0.9050` | 34,190,000.00 USD | 0.00 USD | 11,240.00 USD | `-79.92%` | `12,425.00` |
| `Live` | `Long` | `0.9350` | 34,180,000.00 USD | 0.00 USD | 10,170.00 USD | `-79.26%` | `10,880.60` |
| `Live` | `Long` | `0.9450` | 34,170,000.00 USD | 0.00 USD | 5,330,000.00 USD | `-79.03%` | `5,640,376.30` |
| `Live` | `Long` | `0.9650` | 28,840,000.00 USD | 0.00 USD | 342,520.00 USD | `-78.59%` | `354,943.20` |
| `Live` | `Long` | `0.9750` | 28,490,000.00 USD | 0.00 USD | 1,160.00 USD | `-78.37%` | `1,187.80` |
| `Live` | `Long` | `0.9850` | 28,490,000.00 USD | 0.00 USD | 30,370.00 USD | `-78.15%` | `30,836.80` |
| `Live` | `Long` | `0.9950` | 28,460,000.00 USD | 0.00 USD | 154,330.00 USD | `-77.93%` | `155,110.00` |
| `Live` | `Long` | `1.01` | 28,310,000.00 USD | 0.00 USD | 1,020.00 USD | `-77.48%` | `1,000.00` |
| `Live` | `Long` | `1.02` | 28,310,000.00 USD | 0.00 USD | 10,250.00 USD | `-77.26%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 28,300,000.00 USD | 0.00 USD | 5,200.00 USD | `-77.04%` | `5,021.60` |
| `Live` | `Long` | `1.05` | 28,290,000.00 USD | 0.00 USD | 7,890.00 USD | `-76.59%` | `7,479.20` |
| `Live` | `Long` | `1.06` | 28,280,000.00 USD | 0.00 USD | 1,720.00 USD | `-76.37%` | `1,616.10` |
| `Live` | `Long` | `1.07` | 28,280,000.00 USD | 0.00 USD | 69,010.00 USD | `-76.15%` | `64,195.20` |
| `Live` | `Long` | `1.08` | 28,210,000.00 USD | 0.00 USD | 20,230.00 USD | `-75.93%` | `18,641.00` |
| `Live` | `Long` | `1.09` | 28,190,000.00 USD | 0.00 USD | 73,400.00 USD | `-75.71%` | `67,034.60` |
| `Live` | `Long` | `1.10` | 28,120,000.00 USD | 0.00 USD | 3,020.00 USD | `-75.48%` | `2,734.20` |
| `Live` | `Long` | `1.11` | 28,120,000.00 USD | 0.00 USD | 557.50 USD | `-75.26%` | `500.00` |
| `Live` | `Long` | `1.12` | 28,120,000.00 USD | 0.00 USD | 30,520.00 USD | `-75.04%` | `27,128.40` |
| `Live` | `Long` | `1.14` | 28,090,000.00 USD | 0.00 USD | 4,960.00 USD | `-74.82%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 28,080,000.00 USD | 0.00 USD | 53,830.00 USD | `-74.60%` | `47,009.60` |
| `Live` | `Long` | `1.16` | 28,030,000.00 USD | 0.00 USD | 2,590.00 USD | `-74.38%` | `2,245.90` |
| `Live` | `Long` | `1.18` | 28,020,000.00 USD | 0.00 USD | 11,930.00 USD | `-73.93%` | `10,157.10` |
| `Live` | `Long` | `1.19` | 28,010,000.00 USD | 0.00 USD | 238.19 USD | `-73.71%` | `201.00` |
| `Live` | `Long` | `1.20` | 28,010,000.00 USD | 0.00 USD | 11,220.00 USD | `-73.49%` | `9,393.20` |
| `Live` | `Long` | `1.21` | 28,000,000.00 USD | 0.00 USD | 6,040.00 USD | `-73.27%` | `5,013.60` |
| `Live` | `Long` | `1.22` | 27,990,000.00 USD | 0.00 USD | 9,420.00 USD | `-73.04%` | `7,750.30` |
| `Live` | `Long` | `1.23` | 27,990,000.00 USD | 0.00 USD | 1,720.00 USD | `-72.82%` | `1,400.00` |
| `Live` | `Long` | `1.24` | 27,980,000.00 USD | 0.00 USD | 985.90 USD | `-72.60%` | `798.30` |
| `Live` | `Long` | `1.25` | 27,980,000.00 USD | 0.00 USD | 4,240.00 USD | `-72.38%` | `3,402.10` |
| `Live` | `Long` | `1.25` | 27,980,000.00 USD | 0.00 USD | 653.98 USD | `-72.16%` | `521.10` |
| `Live` | `Long` | `1.26` | 27,980,000.00 USD | 0.00 USD | 2,060.00 USD | `-71.94%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 27,980,000.00 USD | 0.00 USD | 2,390.00 USD | `-71.71%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 27,970,000.00 USD | 0.00 USD | 169.23 USD | `-71.49%` | `131.70` |
| `Live` | `Long` | `1.29` | 27,970,000.00 USD | 0.00 USD | 9,760.00 USD | `-71.27%` | `7,537.90` |
| `Live` | `Long` | `1.30` | 27,960,000.00 USD | 0.00 USD | 782.61 USD | `-71.05%` | `599.70` |
| `Live` | `Long` | `1.31` | 27,960,000.00 USD | 0.00 USD | 117.56 USD | `-70.83%` | `89.40` |
| `Live` | `Long` | `1.32` | 27,960,000.00 USD | 0.00 USD | 2,830.00 USD | `-70.60%` | `2,132.40` |
| `Live` | `Long` | `1.33` | 27,960,000.00 USD | 0.00 USD | 3,390.00 USD | `-70.38%` | `2,536.10` |
| `Live` | `Long` | `1.34` | 27,960,000.00 USD | 0.00 USD | 603.91 USD | `-70.16%` | `449.00` |
| `Live` | `Long` | `1.35` | 27,960,000.00 USD | 0.00 USD | 371.13 USD | `-69.94%` | `273.90` |
| `Live` | `Long` | `1.36` | 27,960,000.00 USD | 0.00 USD | 1,200.00 USD | `-69.72%` | `875.90` |
| `Live` | `Long` | `1.38` | 27,950,000.00 USD | 0.00 USD | 15,710.00 USD | `-69.49%` | `11,422.20` |
| `Live` | `Long` | `1.39` | 27,940,000.00 USD | 0.00 USD | 295.56 USD | `-69.27%` | `213.40` |
| `Live` | `Long` | `1.40` | 27,940,000.00 USD | 0.00 USD | 157.50 USD | `-69.05%` | `112.90` |
| `Live` | `Long` | `1.41` | 27,940,000.00 USD | 0.00 USD | 758.84 USD | `-68.83%` | `540.10` |
| `Live` | `Long` | `1.42` | 27,940,000.00 USD | 0.00 USD | 53,190.00 USD | `-68.61%` | `37,592.50` |
| `Live` | `Long` | `1.43` | 27,880,000.00 USD | 0.00 USD | 18,780.00 USD | `-68.39%` | `13,181.20` |
| `Live` | `Long` | `1.45` | 27,870,000.00 USD | 0.00 USD | 226.29 USD | `-67.94%` | `156.60` |
| `Live` | `Long` | `1.48` | 27,860,000.00 USD | 0.00 USD | 1,480.00 USD | `-67.28%` | `1,000.00` |
| `Live` | `Long` | `1.49` | 27,860,000.00 USD | 0.00 USD | 276.06 USD | `-67.05%` | `185.90` |
| `Live` | `Long` | `1.50` | 27,860,000.00 USD | 0.00 USD | 4,200.00 USD | `-66.61%` | `2,793.80` |
| `Live` | `Long` | `1.51` | 27,860,000.00 USD | 0.00 USD | 9,540.00 USD | `-66.39%` | `6,300.00` |
| `Live` | `Long` | `1.52` | 27,850,000.00 USD | 0.00 USD | 221.12 USD | `-66.17%` | `145.00` |
| `Live` | `Long` | `1.53` | 27,850,000.00 USD | 0.00 USD | 279.37 USD | `-65.94%` | `182.00` |
| `Live` | `Long` | `1.55` | 27,850,000.00 USD | 0.00 USD | 2,560.00 USD | `-65.50%` | `1,647.80` |
| `Live` | `Long` | `1.56` | 27,850,000.00 USD | 0.00 USD | 13,300.00 USD | `-65.28%` | `8,501.00` |
| `Live` | `Long` | `1.57` | 27,830,000.00 USD | 0.00 USD | 589.52 USD | `-65.06%` | `374.30` |
| `Live` | `Long` | `1.58` | 27,830,000.00 USD | 0.00 USD | 4,620.00 USD | `-64.84%` | `2,914.40` |
| `Live` | `Long` | `1.59` | 27,830,000.00 USD | 0.00 USD | 5,380.00 USD | `-64.61%` | `3,374.60` |
| `Live` | `Long` | `1.60` | 27,820,000.00 USD | 0.00 USD | 308.32 USD | `-64.39%` | `192.10` |
| `Live` | `Long` | `1.62` | 27,820,000.00 USD | 0.00 USD | 1,050.00 USD | `-63.95%` | `643.80` |
| `Live` | `Long` | `1.64` | 27,820,000.00 USD | 0.00 USD | 2,030.00 USD | `-63.73%` | `1,241.00` |
| `Live` | `Long` | `1.65` | 27,820,000.00 USD | 0.00 USD | 981.08 USD | `-63.50%` | `596.40` |
| `Live` | `Long` | `1.66` | 27,820,000.00 USD | 0.00 USD | 384.13 USD | `-63.28%` | `232.10` |
| `Live` | `Long` | `1.67` | 27,820,000.00 USD | 0.00 USD | 2,600.00 USD | `-63.06%` | `1,564.40` |
| `Live` | `Long` | `1.68` | 27,820,000.00 USD | 0.00 USD | 231.48 USD | `-62.84%` | `138.20` |
| `Live` | `Long` | `1.69` | 27,810,000.00 USD | 0.00 USD | 14,180.00 USD | `-62.62%` | `8,413.40` |
| `Live` | `Long` | `1.70` | 27,800,000.00 USD | 0.00 USD | 1,960.00 USD | `-62.40%` | `1,156.20` |
| `Live` | `Long` | `1.71` | 27,800,000.00 USD | 0.00 USD | 569.64 USD | `-62.17%` | `334.10` |
| `Live` | `Long` | `1.73` | 27,800,000.00 USD | 0.00 USD | 5,730.00 USD | `-61.73%` | `3,323.40` |
| `Live` | `Long` | `1.74` | 27,790,000.00 USD | 0.00 USD | 14,160.00 USD | `-61.51%` | `8,164.20` |
| `Live` | `Long` | `1.75` | 27,780,000.00 USD | 0.00 USD | 200,030.00 USD | `-61.29%` | `114,628.20` |
| `Live` | `Long` | `1.75` | 27,580,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-61.06%` | `926,614.80` |
| `Live` | `Long` | `1.76` | 25,950,000.00 USD | 0.00 USD | 32,790.00 USD | `-60.84%` | `18,575.90` |
| `Live` | `Long` | `1.77` | 25,920,000.00 USD | 0.00 USD | 9,710.00 USD | `-60.62%` | `5,471.50` |
| `Live` | `Long` | `1.78` | 25,910,000.00 USD | 0.00 USD | 8,190.00 USD | `-60.40%` | `4,586.00` |
| `Live` | `Long` | `1.79` | 25,900,000.00 USD | 0.00 USD | 2,290.00 USD | `-60.18%` | `1,274.90` |
| `Live` | `Long` | `1.80` | 25,900,000.00 USD | 0.00 USD | 80,400.00 USD | `-59.95%` | `44,543.20` |
| `Live` | `Long` | `1.81` | 25,820,000.00 USD | 0.00 USD | 2,450.00 USD | `-59.73%` | `1,351.60` |
| `Live` | `Long` | `1.83` | 25,820,000.00 USD | 0.00 USD | 32,160.00 USD | `-59.29%` | `17,525.80` |
| `Live` | `Long` | `1.84` | 25,780,000.00 USD | 0.00 USD | 1,080.00 USD | `-59.07%` | `586.00` |
| `Live` | `Long` | `1.85` | 25,780,000.00 USD | 0.00 USD | 4,130.00 USD | `-58.85%` | `2,227.40` |
| `Live` | `Long` | `1.86` | 25,780,000.00 USD | 0.00 USD | 279.38 USD | `-58.62%` | `149.80` |
| `Live` | `Long` | `1.88` | 25,780,000.00 USD | 0.00 USD | 76,440.00 USD | `-58.40%` | `40,769.70` |
| `Live` | `Long` | `1.89` | 25,700,000.00 USD | 0.00 USD | 2,130.00 USD | `-58.18%` | `1,130.60` |
| `Live` | `Long` | `1.90` | 25,700,000.00 USD | 0.00 USD | 2,350.00 USD | `-57.96%` | `1,239.40` |
| `Live` | `Long` | `1.91` | 25,700,000.00 USD | 0.00 USD | 10,950.00 USD | `-57.74%` | `5,748.00` |
| `Live` | `Long` | `1.93` | 25,690,000.00 USD | 0.00 USD | 362.48 USD | `-57.29%` | `188.30` |
| `Live` | `Long` | `1.94` | 25,690,000.00 USD | 0.00 USD | 2,820.00 USD | `-57.07%` | `1,457.70` |
| `Live` | `Long` | `1.95` | 25,680,000.00 USD | 0.00 USD | 198,010.00 USD | `-56.85%` | `101,806.80` |
| `Live` | `Long` | `1.97` | 25,490,000.00 USD | 0.00 USD | 301,790.00 USD | `-56.41%` | `153,580.80` |
| `Live` | `Long` | `1.98` | 25,180,000.00 USD | 0.00 USD | 43,680.00 USD | `-56.18%` | `22,116.40` |
| `Live` | `Long` | `1.99` | 25,140,000.00 USD | 0.00 USD | 86,570.00 USD | `-55.96%` | `43,609.70` |
| `Live` | `Long` | `2.00` | 25,050,000.00 USD | 0.00 USD | 122,770.00 USD | `-55.52%` | `61,234.30` |
| `Live` | `Long` | `2.02` | 24,930,000.00 USD | 0.00 USD | 1,270.00 USD | `-55.07%` | `628.70` |
| `Live` | `Long` | `2.04` | 24,930,000.00 USD | 0.00 USD | 3,460.00 USD | `-54.63%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 24,930,000.00 USD | 0.00 USD | 87,780.00 USD | `-54.41%` | `42,716.60` |
| `Live` | `Long` | `2.06` | 24,840,000.00 USD | 0.00 USD | 455.95 USD | `-54.19%` | `220.80` |
| `Live` | `Long` | `2.08` | 24,840,000.00 USD | 0.00 USD | 3,750.00 USD | `-53.96%` | `1,809.30` |
| `Live` | `Long` | `2.08` | 24,830,000.00 USD | 0.00 USD | 15,250.00 USD | `-53.74%` | `7,312.90` |
| `Live` | `Long` | `2.10` | 24,820,000.00 USD | 0.00 USD | 2,060.00 USD | `-53.52%` | `983.60` |
| `Live` | `Long` | `2.10` | 24,820,000.00 USD | 0.00 USD | 11,830.00 USD | `-53.30%` | `5,620.60` |
| `Live` | `Long` | `2.12` | 24,800,000.00 USD | 0.00 USD | 15,110.00 USD | `-53.08%` | `7,142.00` |
| `Live` | `Long` | `2.12` | 24,790,000.00 USD | 0.00 USD | 4,560.00 USD | `-52.86%` | `2,145.50` |
| `Live` | `Long` | `2.13` | 24,790,000.00 USD | 0.00 USD | 29,050.00 USD | `-52.63%` | `13,607.20` |
| `Live` | `Long` | `2.15` | 24,760,000.00 USD | 0.00 USD | 594.13 USD | `-52.19%` | `275.70` |
| `Live` | `Long` | `2.17` | 24,760,000.00 USD | 0.00 USD | 3,910.00 USD | `-51.97%` | `1,806.00` |
| `Live` | `Long` | `2.19` | 24,750,000.00 USD | 0.00 USD | 24,570.00 USD | `-51.52%` | `11,245.20` |
| `Live` | `Long` | `2.19` | 24,730,000.00 USD | 0.00 USD | 11,180.00 USD | `-51.30%` | `5,093.60` |
| `Live` | `Long` | `2.21` | 24,720,000.00 USD | 0.00 USD | 24,300.00 USD | `-51.08%` | `11,018.40` |
| `Live` | `Long` | `2.23` | 24,690,000.00 USD | 0.00 USD | 4,450.00 USD | `-50.64%` | `2,000.00` |
| `Live` | `Long` | `2.23` | 24,690,000.00 USD | 0.00 USD | 30,830.00 USD | `-50.41%` | `13,795.80` |
| `Live` | `Long` | `2.25` | 24,660,000.00 USD | 0.00 USD | 117,150.00 USD | `-49.97%` | `51,951.00` |
| `Live` | `Long` | `2.27` | 24,540,000.00 USD | 0.00 USD | 3,430.00 USD | `-49.75%` | `1,513.80` |
| `Live` | `Long` | `2.27` | 24,540,000.00 USD | 0.00 USD | 2,030.00 USD | `-49.53%` | `891.50` |
| `Live` | `Long` | `2.29` | 24,530,000.00 USD | 0.00 USD | 10,010.00 USD | `-49.31%` | `4,379.10` |
| `Live` | `Long` | `2.29` | 24,520,000.00 USD | 0.00 USD | 2,380.00 USD | `-49.08%` | `1,036.90` |
| `Live` | `Long` | `2.31` | 24,520,000.00 USD | 0.00 USD | 2,240.00 USD | `-48.86%` | `972.60` |
| `Live` | `Long` | `2.31` | 24,520,000.00 USD | 0.00 USD | 1,250.00 USD | `-48.64%` | `540.20` |
| `Live` | `Long` | `2.33` | 24,520,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-48.42%` | `678,411.30` |
| `Live` | `Long` | `2.33` | 22,940,000.00 USD | 0.00 USD | 3,520.00 USD | `-48.20%` | `1,508.40` |
| `Live` | `Long` | `2.35` | 22,940,000.00 USD | 0.00 USD | 48,780.00 USD | `-47.97%` | `20,800.50` |
| `Live` | `Long` | `2.35` | 22,890,000.00 USD | 0.00 USD | 5,770.00 USD | `-47.75%` | `2,449.40` |
| `Live` | `Long` | `2.37` | 22,880,000.00 USD | 0.00 USD | 63,000.00 USD | `-47.53%` | `26,640.40` |
| `Live` | `Long` | `2.38` | 22,820,000.00 USD | 0.00 USD | 569,200.00 USD | `-47.31%` | `239,665.10` |
| `Live` | `Long` | `2.38` | 22,250,000.00 USD | 0.00 USD | 9,960.00 USD | `-47.09%` | `4,176.50` |
| `Live` | `Long` | `2.40` | 22,240,000.00 USD | 0.00 USD | 378.65 USD | `-46.87%` | `158.10` |
| `Live` | `Long` | `2.40` | 22,240,000.00 USD | 0.00 USD | 2,310.00 USD | `-46.64%` | `961.40` |
| `Live` | `Long` | `2.42` | 22,240,000.00 USD | 0.00 USD | 185,860.00 USD | `-46.42%` | `76,961.80` |
| `Live` | `Long` | `2.42` | 22,050,000.00 USD | 0.00 USD | 388,800.00 USD | `-46.20%` | `160,328.60` |
| `Live` | `Long` | `2.44` | 21,660,000.00 USD | 0.00 USD | 4,140.00 USD | `-45.98%` | `1,698.40` |
| `Live` | `Long` | `2.46` | 21,660,000.00 USD | 0.00 USD | 5,440.00 USD | `-45.53%` | `2,217.90` |
| `Live` | `Long` | `2.46` | 21,650,000.00 USD | 0.00 USD | 11,310.00 USD | `-45.31%` | `4,587.40` |
| `Live` | `Long` | `2.48` | 21,640,000.00 USD | 0.00 USD | 915,870.00 USD | `-45.09%` | `370,049.30` |
| `Live` | `Long` | `2.48` | 20,730,000.00 USD | 0.00 USD | 2,760.00 USD | `-44.87%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 20,720,000.00 USD | 0.00 USD | 2,040.00 USD | `-44.65%` | `818.30` |
| `Live` | `Long` | `2.50` | 20,720,000.00 USD | 0.00 USD | 7,490.00 USD | `-44.42%` | `2,989.20` |
| `Live` | `Long` | `2.52` | 20,710,000.00 USD | 0.00 USD | 37,490.00 USD | `-43.98%` | `14,849.30` |
| `Live` | `Long` | `2.54` | 20,680,000.00 USD | 0.00 USD | 2,140.00 USD | `-43.76%` | `842.50` |
| `Live` | `Long` | `2.54` | 20,670,000.00 USD | 0.00 USD | 18,780.00 USD | `-43.54%` | `7,377.70` |
| `Live` | `Long` | `2.56` | 20,660,000.00 USD | 0.00 USD | 694.96 USD | `-43.32%` | `272.00` |
| `Live` | `Long` | `2.56` | 20,650,000.00 USD | 0.00 USD | 8,790.00 USD | `-43.09%` | `3,427.60` |
| `Live` | `Long` | `2.58` | 20,650,000.00 USD | 0.00 USD | 12,880.00 USD | `-42.87%` | `5,000.00` |
| `Live` | `Long` | `2.58` | 20,630,000.00 USD | 0.00 USD | 1,340.00 USD | `-42.65%` | `519.30` |
| `Live` | `Long` | `2.60` | 20,630,000.00 USD | 0.00 USD | 72,060.00 USD | `-42.43%` | `27,768.10` |
| `Live` | `Long` | `2.60` | 20,560,000.00 USD | 0.00 USD | 8,480.00 USD | `-42.21%` | `3,256.60` |
| `Live` | `Long` | `2.62` | 20,550,000.00 USD | 0.00 USD | 1,190.00 USD | `-41.98%` | `454.70` |
| `Live` | `Long` | `2.62` | 20,550,000.00 USD | 0.00 USD | 12,890.00 USD | `-41.76%` | `4,908.70` |
| `Live` | `Long` | `2.63` | 20,540,000.00 USD | 0.00 USD | 48,970.00 USD | `-41.54%` | `18,584.90` |
| `Live` | `Long` | `2.65` | 20,490,000.00 USD | 0.00 USD | 7,170.00 USD | `-41.32%` | `2,709.70` |
| `Live` | `Long` | `2.65` | 20,480,000.00 USD | 0.00 USD | 18,510.00 USD | `-41.10%` | `6,972.60` |
| `Live` | `Long` | `2.67` | 20,460,000.00 USD | 0.00 USD | 19,550.00 USD | `-40.88%` | `7,334.70` |
| `Live` | `Long` | `2.67` | 20,440,000.00 USD | 0.00 USD | 11,920.00 USD | `-40.65%` | `4,455.50` |
| `Live` | `Long` | `2.69` | 20,430,000.00 USD | 0.00 USD | 212,560.00 USD | `-40.43%` | `79,166.30` |
| `Live` | `Long` | `2.69` | 20,220,000.00 USD | 0.00 USD | 6,320.00 USD | `-40.21%` | `2,346.30` |
| `Live` | `Long` | `2.71` | 20,210,000.00 USD | 0.00 USD | 119,930.00 USD | `-39.99%` | `44,335.90` |
| `Live` | `Long` | `2.71` | 20,090,000.00 USD | 0.00 USD | 11,750.00 USD | `-39.77%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 20,080,000.00 USD | 0.00 USD | 36,890.00 USD | `-39.54%` | `13,537.90` |
| `Live` | `Long` | `2.73` | 20,040,000.00 USD | 0.00 USD | 13,690.00 USD | `-39.32%` | `5,005.70` |
| `Live` | `Long` | `2.75` | 20,030,000.00 USD | 0.00 USD | 39,550.00 USD | `-39.10%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 19,990,000.00 USD | 0.00 USD | 13,930.00 USD | `-38.88%` | `5,056.20` |
| `Live` | `Long` | `2.77` | 19,980,000.00 USD | 0.00 USD | 191,000.00 USD | `-38.66%` | `69,076.40` |
| `Live` | `Long` | `2.77` | 19,790,000.00 USD | 0.00 USD | 2,140.00 USD | `-38.43%` | `771.20` |
| `Live` | `Long` | `2.79` | 19,780,000.00 USD | 0.00 USD | 24,840.00 USD | `-38.21%` | `8,920.90` |
| `Live` | `Long` | `2.79` | 19,760,000.00 USD | 0.00 USD | 15,940.00 USD | `-37.99%` | `5,703.70` |
| `Live` | `Long` | `2.81` | 19,740,000.00 USD | 0.00 USD | 6,190.00 USD | `-37.77%` | `2,208.40` |
| `Live` | `Long` | `2.81` | 19,740,000.00 USD | 0.00 USD | 1,150.00 USD | `-37.55%` | `406.90` |
| `Live` | `Long` | `2.83` | 19,740,000.00 USD | 0.00 USD | 2,240.00 USD | `-37.33%` | `792.20` |
| `Live` | `Long` | `2.83` | 19,730,000.00 USD | 0.00 USD | 1,140.00 USD | `-37.10%` | `402.50` |
| `Live` | `Long` | `2.85` | 19,730,000.00 USD | 0.00 USD | 180.94 USD | `-36.88%` | `63.60` |
| `Live` | `Long` | `2.85` | 19,730,000.00 USD | 0.00 USD | 5,800.00 USD | `-36.66%` | `2,031.60` |
| `Live` | `Long` | `2.87` | 19,730,000.00 USD | 0.00 USD | 5,190.00 USD | `-36.44%` | `1,810.40` |
| `Live` | `Long` | `2.88` | 19,720,000.00 USD | 0.00 USD | 2,540.00 USD | `-36.22%` | `883.20` |
| `Live` | `Long` | `2.88` | 19,720,000.00 USD | 0.00 USD | 6,600.00 USD | `-35.99%` | `2,286.30` |
| `Live` | `Long` | `2.90` | 19,710,000.00 USD | 0.00 USD | 13,910.00 USD | `-35.77%` | `4,804.60` |
| `Live` | `Long` | `2.90` | 19,700,000.00 USD | 0.00 USD | 27,650.00 USD | `-35.55%` | `9,517.60` |
| `Live` | `Long` | `2.92` | 19,670,000.00 USD | 0.00 USD | 143,730.00 USD | `-35.33%` | `49,307.50` |
| `Live` | `Long` | `2.94` | 19,530,000.00 USD | 0.00 USD | 37,780.00 USD | `-34.88%` | `12,871.30` |
| `Live` | `Long` | `2.96` | 19,490,000.00 USD | 0.00 USD | 15,090.00 USD | `-34.44%` | `5,105.70` |
| `Live` | `Long` | `2.96` | 19,470,000.00 USD | 0.00 USD | 560,970.00 USD | `-34.22%` | `189,196.30` |
| `Live` | `Long` | `2.98` | 18,910,000.00 USD | 0.00 USD | 13,700.00 USD | `-34.00%` | `4,604.60` |
| `Live` | `Long` | `2.98` | 18,900,000.00 USD | 0.00 USD | 72,980.00 USD | `-33.78%` | `24,449.30` |
| `Live` | `Long` | `3.00` | 18,830,000.00 USD | 0.00 USD | 7,990.00 USD | `-33.55%` | `2,666.40` |
| `Live` | `Long` | `3.00` | 18,820,000.00 USD | 0.00 USD | 30,320.00 USD | `-33.33%` | `10,090.40` |
| `Live` | `Long` | `3.02` | 18,790,000.00 USD | 0.00 USD | 18,390.00 USD | `-33.11%` | `6,099.10` |
| `Live` | `Long` | `3.02` | 18,770,000.00 USD | 0.00 USD | 17,780.00 USD | `-32.89%` | `5,878.00` |
| `Live` | `Long` | `3.04` | 18,750,000.00 USD | 0.00 USD | 386,180.00 USD | `-32.67%` | `127,241.20` |
| `Live` | `Long` | `3.04` | 18,370,000.00 USD | 0.00 USD | 103,780.00 USD | `-32.44%` | `34,081.60` |
| `Live` | `Long` | `3.06` | 18,260,000.00 USD | 0.00 USD | 22,850.00 USD | `-32.22%` | `7,480.60` |
| `Live` | `Long` | `3.06` | 18,240,000.00 USD | 0.00 USD | 115,950.00 USD | `-32.00%` | `37,831.90` |
| `Live` | `Long` | `3.08` | 18,120,000.00 USD | 0.00 USD | 3,230.00 USD | `-31.78%` | `1,050.40` |
| `Live` | `Long` | `3.08` | 18,120,000.00 USD | 0.00 USD | 12,020.00 USD | `-31.56%` | `3,896.60` |
| `Live` | `Long` | `3.10` | 18,110,000.00 USD | 0.00 USD | 25,600.00 USD | `-31.34%` | `8,272.60` |
| `Live` | `Long` | `3.10` | 18,080,000.00 USD | 0.00 USD | 25,200.00 USD | `-31.11%` | `8,116.40` |
| `Live` | `Long` | `3.12` | 18,060,000.00 USD | 0.00 USD | 80,320.00 USD | `-30.89%` | `25,784.10` |
| `Live` | `Long` | `3.12` | 17,980,000.00 USD | 0.00 USD | 8,940.00 USD | `-30.67%` | `2,861.40` |
| `Live` | `Long` | `3.13` | 17,970,000.00 USD | 0.00 USD | 39,110.00 USD | `-30.45%` | `12,474.20` |
| `Live` | `Long` | `3.15` | 17,930,000.00 USD | 0.00 USD | 116,280.00 USD | `-30.23%` | `36,973.10` |
| `Live` | `Long` | `3.15` | 17,810,000.00 USD | 0.00 USD | 1,300.00 USD | `-30.00%` | `411.70` |
| `Live` | `Long` | `3.17` | 17,810,000.00 USD | 0.00 USD | 7,150.00 USD | `-29.78%` | `2,258.50` |
| `Live` | `Long` | `3.17` | 17,800,000.00 USD | 0.00 USD | 96,740.00 USD | `-29.56%` | `30,470.70` |
| `Live` | `Long` | `3.19` | 17,710,000.00 USD | 0.00 USD | 6,870.00 USD | `-29.34%` | `2,157.90` |
| `Live` | `Long` | `3.19` | 17,700,000.00 USD | 0.00 USD | 4,400.00 USD | `-29.12%` | `1,377.10` |
| `Live` | `Long` | `3.21` | 17,700,000.00 USD | 0.00 USD | 103,750.00 USD | `-28.89%` | `32,372.50` |
| `Live` | `Long` | `3.21` | 17,590,000.00 USD | 0.00 USD | 28,330.00 USD | `-28.67%` | `8,811.80` |
| `Live` | `Long` | `3.23` | 17,560,000.00 USD | 0.00 USD | 23,020.00 USD | `-28.45%` | `7,139.20` |
| `Live` | `Long` | `3.23` | 17,540,000.00 USD | 0.00 USD | 20,660.00 USD | `-28.23%` | `6,386.90` |
| `Live` | `Long` | `3.25` | 17,520,000.00 USD | 0.00 USD | 274,600.00 USD | `-28.01%` | `84,623.10` |
| `Live` | `Long` | `3.25` | 17,240,000.00 USD | 0.00 USD | 70,660.00 USD | `-27.79%` | `21,708.70` |
| `Live` | `Long` | `3.27` | 17,170,000.00 USD | 0.00 USD | 44,450.00 USD | `-27.56%` | `13,613.60` |
| `Live` | `Long` | `3.27` | 17,130,000.00 USD | 0.00 USD | 839,940.00 USD | `-27.34%` | `256,469.30` |
| `Live` | `Long` | `3.29` | 16,290,000.00 USD | 0.00 USD | 6,650.00 USD | `-27.12%` | `2,023.40` |
| `Live` | `Long` | `3.29` | 16,280,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-26.90%` | `430,379.90` |
| `Live` | `Long` | `3.31` | 14,870,000.00 USD | 0.00 USD | 60,770.00 USD | `-26.68%` | `18,388.20` |
| `Live` | `Long` | `3.31` | 14,800,000.00 USD | 0.00 USD | 26,680.00 USD | `-26.45%` | `8,049.10` |
| `Live` | `Long` | `3.33` | 14,780,000.00 USD | 0.00 USD | 8,730.00 USD | `-26.23%` | `2,624.30` |
| `Live` | `Long` | `3.33` | 14,770,000.00 USD | 0.00 USD | 51,640.00 USD | `-26.01%` | `15,484.10` |
| `Live` | `Long` | `3.35` | 14,720,000.00 USD | 0.00 USD | 26,150.00 USD | `-25.79%` | `7,819.00` |
| `Live` | `Long` | `3.35` | 14,690,000.00 USD | 0.00 USD | 10,480.00 USD | `-25.57%` | `3,124.00` |
| `Live` | `Long` | `3.37` | 14,680,000.00 USD | 0.00 USD | 3,550.00 USD | `-25.34%` | `1,054.40` |
| `Live` | `Long` | `3.38` | 14,680,000.00 USD | 0.00 USD | 29,990.00 USD | `-25.12%` | `8,887.40` |
| `Live` | `Long` | `3.38` | 14,650,000.00 USD | 0.00 USD | 43,640.00 USD | `-24.90%` | `12,892.50` |
| `Live` | `Long` | `3.40` | 14,600,000.00 USD | 0.00 USD | 1,970.00 USD | `-24.68%` | `579.20` |
| `Live` | `Long` | `3.40` | 14,600,000.00 USD | 0.00 USD | 110,220.00 USD | `-24.46%` | `32,371.50` |
| `Live` | `Long` | `3.42` | 14,490,000.00 USD | 0.00 USD | 194,840.00 USD | `-24.24%` | `57,055.20` |
| `Live` | `Long` | `3.42` | 14,300,000.00 USD | 0.00 USD | 52,030.00 USD | `-24.01%` | `15,191.70` |
| `Live` | `Long` | `3.44` | 14,240,000.00 USD | 0.00 USD | 27,230.00 USD | `-23.79%` | `7,925.90` |
| `Live` | `Long` | `3.44` | 14,220,000.00 USD | 0.00 USD | 45,120.00 USD | `-23.57%` | `13,097.30` |
| `Live` | `Long` | `3.46` | 14,170,000.00 USD | 0.00 USD | 55,190.00 USD | `-23.35%` | `15,973.50` |
| `Live` | `Long` | `3.46` | 14,120,000.00 USD | 0.00 USD | 11,280.00 USD | `-23.13%` | `3,255.00` |
| `Live` | `Long` | `3.48` | 14,110,000.00 USD | 0.00 USD | 77,730.00 USD | `-22.90%` | `22,369.60` |
| `Live` | `Long` | `3.48` | 14,030,000.00 USD | 0.00 USD | 11,350.00 USD | `-22.68%` | `3,257.90` |
| `Live` | `Long` | `3.50` | 14,020,000.00 USD | 0.00 USD | 24,910.00 USD | `-22.46%` | `7,127.50` |
| `Live` | `Long` | `3.50` | 13,990,000.00 USD | 0.00 USD | 22,250.00 USD | `-22.24%` | `6,347.00` |
| `Live` | `Long` | `3.52` | 13,970,000.00 USD | 0.00 USD | 26,620.00 USD | `-22.02%` | `7,572.70` |
| `Live` | `Long` | `3.52` | 13,940,000.00 USD | 0.00 USD | 7,430.00 USD | `-21.80%` | `2,107.30` |
| `Live` | `Long` | `3.54` | 13,940,000.00 USD | 0.00 USD | 4,110.00 USD | `-21.57%` | `1,163.30` |
| `Live` | `Long` | `3.54` | 13,930,000.00 USD | 0.00 USD | 324,630.00 USD | `-21.35%` | `91,575.00` |
| `Live` | `Long` | `3.56` | 13,610,000.00 USD | 0.00 USD | 375,650.00 USD | `-21.13%` | `105,669.00` |
| `Live` | `Long` | `3.56` | 13,230,000.00 USD | 0.00 USD | 3,200.00 USD | `-20.91%` | `897.90` |
| `Live` | `Long` | `3.58` | 13,230,000.00 USD | 0.00 USD | 124,650.00 USD | `-20.69%` | `34,865.90` |
| `Live` | `Long` | `3.58` | 13,100,000.00 USD | 0.00 USD | 25,270.00 USD | `-20.46%` | `7,048.70` |
| `Live` | `Long` | `3.60` | 13,080,000.00 USD | 0.00 USD | 25,500.00 USD | `-20.24%` | `7,093.90` |
| `Live` | `Long` | `3.60` | 13,050,000.00 USD | 0.00 USD | 154,720.00 USD | `-20.02%` | `42,917.70` |
| `Live` | `Long` | `3.62` | 12,900,000.00 USD | 0.00 USD | 523,230.00 USD | `-19.80%` | `144,738.70` |
| `Live` | `Long` | `3.62` | 12,370,000.00 USD | 0.00 USD | 25,050.00 USD | `-19.58%` | `6,909.30` |
| `Live` | `Long` | `3.63` | 12,350,000.00 USD | 0.00 USD | 39,840.00 USD | `-19.35%` | `10,960.00` |
| `Live` | `Long` | `3.65` | 12,310,000.00 USD | 0.00 USD | 508,750.00 USD | `-19.13%` | `139,575.80` |
| `Live` | `Long` | `3.65` | 11,800,000.00 USD | 0.00 USD | 33,110.00 USD | `-18.91%` | `9,059.60` |
| `Live` | `Long` | `3.67` | 11,770,000.00 USD | 0.00 USD | 44,710.00 USD | `-18.69%` | `12,199.40` |
| `Live` | `Long` | `3.67` | 11,720,000.00 USD | 0.00 USD | 189,590.00 USD | `-18.47%` | `51,588.50` |
| `Live` | `Long` | `3.69` | 11,530,000.00 USD | 0.00 USD | 214,140.00 USD | `-18.25%` | `58,110.30` |
| `Live` | `Long` | `3.69` | 11,320,000.00 USD | 0.00 USD | 117,240.00 USD | `-18.02%` | `31,730.00` |
| `Live` | `Long` | `3.71` | 11,200,000.00 USD | 0.00 USD | 25,370.00 USD | `-17.80%` | `6,848.80` |
| `Live` | `Long` | `3.71` | 11,180,000.00 USD | 0.00 USD | 41,120.00 USD | `-17.58%` | `11,069.60` |
| `Live` | `Long` | `3.73` | 11,140,000.00 USD | 0.00 USD | 27,300.00 USD | `-17.36%` | `7,328.00` |
| `Live` | `Long` | `3.73` | 11,110,000.00 USD | 0.00 USD | 6,340.00 USD | `-17.14%` | `1,697.50` |
| `Live` | `Long` | `3.75` | 11,100,000.00 USD | 0.00 USD | 23,730.00 USD | `-16.91%` | `6,335.40` |
| `Live` | `Long` | `3.75` | 11,080,000.00 USD | 0.00 USD | 100,660.00 USD | `-16.69%` | `26,805.90` |
| `Live` | `Long` | `3.77` | 10,980,000.00 USD | 0.00 USD | 63,870.00 USD | `-16.47%` | `16,963.70` |
| `Live` | `Long` | `3.77` | 10,910,000.00 USD | 0.00 USD | 14,510.00 USD | `-16.25%` | `3,844.90` |
| `Live` | `Long` | `3.79` | 10,900,000.00 USD | 0.00 USD | 38,120.00 USD | `-16.03%` | `10,072.00` |
| `Live` | `Long` | `3.79` | 10,860,000.00 USD | 0.00 USD | 124,270.00 USD | `-15.81%` | `32,746.10` |
| `Live` | `Long` | `3.81` | 10,740,000.00 USD | 0.00 USD | 14,720.00 USD | `-15.58%` | `3,868.60` |
| `Live` | `Long` | `3.81` | 10,720,000.00 USD | 0.00 USD | 77,530.00 USD | `-15.36%` | `20,323.20` |
| `Live` | `Long` | `3.83` | 10,640,000.00 USD | 0.00 USD | 5,180.00 USD | `-15.14%` | `1,354.50` |
| `Live` | `Long` | `3.83` | 10,640,000.00 USD | 0.00 USD | 170,490.00 USD | `-14.92%` | `44,457.20` |
| `Live` | `Long` | `3.85` | 10,470,000.00 USD | 0.00 USD | 22,270.00 USD | `-14.70%` | `5,792.60` |
| `Live` | `Long` | `3.85` | 10,450,000.00 USD | 0.00 USD | 21,460.00 USD | `-14.47%` | `5,567.80` |
| `Live` | `Long` | `3.87` | 10,420,000.00 USD | 0.00 USD | 22,840.00 USD | `-14.25%` | `5,909.10` |
| `Live` | `Long` | `3.88` | 10,400,000.00 USD | 0.00 USD | 138,250.00 USD | `-14.03%` | `35,676.50` |
| `Live` | `Long` | `3.88` | 10,260,000.00 USD | 0.00 USD | 31,160.00 USD | `-13.81%` | `8,020.30` |
| `Live` | `Long` | `3.90` | 10,230,000.00 USD | 0.00 USD | 94,560.00 USD | `-13.59%` | `24,276.00` |
| `Live` | `Long` | `3.90` | 10,140,000.00 USD | 0.00 USD | 6,040.00 USD | `-13.36%` | `1,548.00` |
| `Live` | `Long` | `3.92` | 10,130,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-13.14%` | `1,001,918.60` |
| `Live` | `Long` | `3.92` | 6,210,000.00 USD | 0.00 USD | 200,060.00 USD | `-12.92%` | `50,971.00` |
| `Live` | `Long` | `3.94` | 6,010,000.00 USD | 0.00 USD | 20,840.00 USD | `-12.70%` | `5,295.30` |
| `Live` | `Long` | `3.94` | 5,990,000.00 USD | 0.00 USD | 534,170.00 USD | `-12.48%` | `135,404.20` |
| `Live` | `Long` | `3.96` | 5,450,000.00 USD | 0.00 USD | 13,470.00 USD | `-12.26%` | `3,406.30` |
| `Live` | `Long` | `3.96` | 5,440,000.00 USD | 0.00 USD | 107,600.00 USD | `-12.03%` | `27,138.20` |
| `Live` | `Long` | `3.98` | 5,330,000.00 USD | 0.00 USD | 39,580.00 USD | `-11.81%` | `9,958.20` |
| `Live` | `Long` | `3.98` | 5,290,000.00 USD | 0.00 USD | 161,330.00 USD | `-11.59%` | `40,484.10` |
| `Live` | `Long` | `4.00` | 5,130,000.00 USD | 0.00 USD | 36,460.00 USD | `-11.37%` | `9,126.90` |
| `Live` | `Long` | `4.00` | 5,100,000.00 USD | 0.00 USD | 59,840.00 USD | `-11.15%` | `14,941.70` |
| `Live` | `Long` | `4.01` | 5,040,000.00 USD | 0.00 USD | 12,850.00 USD | `-10.92%` | `3,199.60` |
| `Live` | `Long` | `4.03` | 5,020,000.00 USD | 0.00 USD | 109,260.00 USD | `-10.70%` | `27,146.40` |
| `Live` | `Long` | `4.04` | 4,910,000.00 USD | 0.00 USD | 24,850.00 USD | `-10.48%` | `6,158.30` |
| `Live` | `Long` | `4.04` | 4,890,000.00 USD | 0.00 USD | 33,120.00 USD | `-10.26%` | `8,187.20` |
| `Live` | `Long` | `4.05` | 4,860,000.00 USD | 0.00 USD | 82,940.00 USD | `-10.04%` | `20,453.10` |
| `Live` | `Long` | `4.07` | 4,770,000.00 USD | 0.00 USD | 376,550.00 USD | `-9.81%` | `92,631.20` |
| `Live` | `Long` | `4.08` | 4,400,000.00 USD | 0.00 USD | 268,550.00 USD | `-9.59%` | `65,901.80` |
| `Live` | `Long` | `4.08` | 4,130,000.00 USD | 0.00 USD | 304,210.00 USD | `-9.37%` | `74,469.60` |
| `Live` | `Long` | `4.09` | 3,820,000.00 USD | 0.00 USD | 721,610.00 USD | `-9.15%` | `176,218.30` |
| `Live` | `Long` | `4.11` | 3,100,000.00 USD | 0.00 USD | 112,820.00 USD | `-8.93%` | `27,483.50` |
| `Live` | `Long` | `4.12` | 2,990,000.00 USD | 0.00 USD | 254,610.00 USD | `-8.71%` | `61,873.30` |
| `Live` | `Long` | `4.12` | 2,730,000.00 USD | 0.00 USD | 45,150.00 USD | `-8.48%` | `10,945.40` |
| `Live` | `Long` | `4.13` | 2,690,000.00 USD | 0.00 USD | 77,110.00 USD | `-8.26%` | `18,647.10` |
| `Live` | `Long` | `4.14` | 2,610,000.00 USD | 0.00 USD | 101,060.00 USD | `-8.04%` | `24,380.50` |
| `Live` | `Long` | `4.16` | 2,510,000.00 USD | 0.00 USD | 54,150.00 USD | `-7.82%` | `13,033.30` |
| `Live` | `Long` | `4.17` | 2,460,000.00 USD | 0.00 USD | 315,620.00 USD | `-7.60%` | `75,778.00` |
| `Live` | `Long` | `4.17` | 2,140,000.00 USD | 0.00 USD | 15,950.00 USD | `-7.37%` | `3,820.50` |
| `Live` | `Long` | `4.18` | 2,130,000.00 USD | 0.00 USD | 370,570.00 USD | `-7.15%` | `88,548.30` |
| `Live` | `Long` | `4.20` | 1,760,000.00 USD | 0.00 USD | 248,620.00 USD | `-6.93%` | `59,266.90` |
| `Live` | `Long` | `4.21` | 1,510,000.00 USD | 0.00 USD | 284,680.00 USD | `-6.71%` | `67,700.20` |
| `Live` | `Long` | `4.21` | 1,220,000.00 USD | 0.00 USD | 41,000.00 USD | `-6.49%` | `9,726.40` |
| `Live` | `Long` | `4.22` | 1,180,000.00 USD | 0.00 USD | 471,560.00 USD | `-6.27%` | `111,612.80` |
| `Live` | `Long` | `4.24` | 709,400.00 USD | 0.00 USD | 83,020.00 USD | `-6.04%` | `19,603.20` |
| `Live` | `Long` | `4.25` | 626,380.00 USD | 0.00 USD | 13,710.00 USD | `-5.82%` | `3,229.40` |
| `Live` | `Long` | `4.25` | 612,670.00 USD | 0.00 USD | 274,960.00 USD | `-5.60%` | `64,621.10` |
| `Live` | `Long` | `4.26` | 337,710.00 USD | 0.00 USD | 47,120.00 USD | `-5.38%` | `11,047.10` |
| `Live` | `Short` | `4.28` | 31,480.00 USD | 31,480.00 USD | 0.00 USD | `-5.16%` | `7,364.10` |
| `Live` | `Long` | `4.29` | 290,590.00 USD | 0.00 USD | 10,850.00 USD | `-4.93%` | `2,531.20` |
| `Live` | `Short` | `4.29` | 42,860.00 USD | 11,380.00 USD | 0.00 USD | `-4.71%` | `2,650.30` |
| `Live` | `Long` | `4.30` | 279,740.00 USD | 0.00 USD | 11,670.00 USD | `-4.49%` | `2,710.40` |
| `Live` | `Short` | `4.32` | 47,040.00 USD | 4,170.00 USD | 0.00 USD | `-4.27%` | `966.80` |
| `Live` | `Long` | `4.33` | 268,080.00 USD | 0.00 USD | 43,570.00 USD | `-4.05%` | `10,074.20` |
| `Live` | `Long` | `4.33` | 224,510.00 USD | 0.00 USD | 12,880.00 USD | `-3.82%` | `2,971.20` |
| `Live` | `Long` | `4.34` | 211,630.00 USD | 0.00 USD | 30,420.00 USD | `-3.60%` | `7,000.00` |
| `Live` | `Long` | `4.36` | 181,210.00 USD | 0.00 USD | 1,550.00 USD | `-3.38%` | `356.10` |
| `Live` | `Long` | `4.37` | 179,660.00 USD | 0.00 USD | 10,330.00 USD | `-3.16%` | `2,367.10` |
| `Live` | `Long` | `4.38` | 169,330.00 USD | 0.00 USD | 126,420.00 USD | `-2.94%` | `28,895.90` |
| `Live` | `Long` | `4.38` | 42,910.00 USD | 0.00 USD | 7,460.00 USD | `-2.72%` | `1,700.50` |
| `Live` | `Long` | `4.39` | 35,450.00 USD | 0.00 USD | 14,870.00 USD | `-2.49%` | `3,382.60` |
| `Live` | `Long` | `4.41` | 20,580.00 USD | 0.00 USD | 355.92 USD | `-2.27%` | `80.80` |
| `Live` | `Long` | `4.42` | 20,230.00 USD | 0.00 USD | 665.34 USD | `-2.05%` | `150.70` |
| `Live` | `Long` | `4.42` | 19,560.00 USD | 0.00 USD | 9,760.00 USD | `-1.83%` | `2,205.10` |
| `Live` | `Long` | `4.43` | 9,810.00 USD | 0.00 USD | 970.38 USD | `-1.61%` | `218.80` |
| `Live` | `Long` | `4.45` | 8,840.00 USD | 0.00 USD | 4,260.00 USD | `-1.38%` | `957.40` |
| `Live` | `Long` | `4.49` | 4,580.00 USD | 0.00 USD | 2,130.00 USD | `-0.50%` | `474.40` |
| `Live` | `Long` | `4.50` | 2,450.00 USD | 0.00 USD | 2,450.00 USD | `-0.05%` | `544.30` |
| `Live` | `Short` | `4.53` | 80,520.00 USD | 33,490.00 USD | 0.00 USD | `+0.39%` | `7,400.20` |
| `Live` | `Short` | `4.59` | 81,030.00 USD | 510.50 USD | 0.00 USD | `+1.94%` | `111.10` |
| `Live` | `Short` | `4.63` | 81,550.00 USD | 515.41 USD | 0.00 USD | `+2.83%` | `111.20` |
| `Live` | `Short` | `4.71` | 110,180.00 USD | 28,640.00 USD | 0.00 USD | `+4.38%` | `6,086.40` |
| `Live` | `Short` | `4.71` | 168,470.00 USD | 58,280.00 USD | 0.00 USD | `+4.61%` | `12,361.40` |
| `Live` | `Short` | `4.72` | 224,450.00 USD | 55,980.00 USD | 0.00 USD | `+4.83%` | `11,848.10` |
| `Live` | `Short` | `4.74` | 228,480.00 USD | 4,030.00 USD | 0.00 USD | `+5.05%` | `851.40` |
| `Live` | `Short` | `4.75` | 230,480.00 USD | 2,000.00 USD | 0.00 USD | `+5.27%` | `420.80` |
| `Live` | `Short` | `4.75` | 232,200.00 USD | 1,720.00 USD | 0.00 USD | `+5.49%` | `362.40` |
| `Live` | `Short` | `4.76` | 239,130.00 USD | 6,920.00 USD | 0.00 USD | `+5.72%` | `1,453.20` |
| `Live` | `Short` | `4.78` | 258,390.00 USD | 19,270.00 USD | 0.00 USD | `+5.94%` | `4,035.10` |
| `Live` | `Short` | `4.79` | 263,250.00 USD | 4,860.00 USD | 0.00 USD | `+6.16%` | `1,015.50` |
| `Live` | `Short` | `4.79` | 344,670.00 USD | 81,420.00 USD | 0.00 USD | `+6.38%` | `16,979.20` |
| `Live` | `Short` | `4.80` | 344,770.00 USD | 104.75 USD | 0.00 USD | `+6.60%` | `21.80` |
| `Live` | `Short` | `4.82` | 411,610.00 USD | 66,830.00 USD | 0.00 USD | `+6.82%` | `13,880.40` |
| `Live` | `Short` | `4.83` | 423,720.00 USD | 12,110.00 USD | 0.00 USD | `+7.05%` | `2,510.50` |
| `Live` | `Short` | `4.83` | 440,700.00 USD | 16,980.00 USD | 0.00 USD | `+7.27%` | `3,512.50` |
| `Live` | `Short` | `4.84` | 449,260.00 USD | 8,560.00 USD | 0.00 USD | `+7.49%` | `1,765.90` |
| `Live` | `Short` | `4.86` | 478,470.00 USD | 29,210.00 USD | 0.00 USD | `+7.71%` | `6,017.30` |
| `Live` | `Short` | `4.87` | 483,930.00 USD | 5,460.00 USD | 0.00 USD | `+7.93%` | `1,121.90` |
| `Live` | `Short` | `4.88` | 499,420.00 USD | 15,490.00 USD | 0.00 USD | `+8.16%` | `3,177.10` |
| `Live` | `Short` | `4.88` | 599,960.00 USD | 100,540.00 USD | 0.00 USD | `+8.38%` | `20,581.30` |
| `Live` | `Short` | `4.92` | 622,960.00 USD | 23,000.00 USD | 0.00 USD | `+9.04%` | `4,679.80` |
| `Live` | `Short` | `4.92` | 635,890.00 USD | 12,930.00 USD | 0.00 USD | `+9.26%` | `2,625.70` |
| `Live` | `Short` | `4.93` | 636,050.00 USD | 157.43 USD | 0.00 USD | `+9.49%` | `31.90` |
| `Live` | `Short` | `4.96` | 640,220.00 USD | 4,170.00 USD | 0.00 USD | `+9.93%` | `842.00` |
| `Live` | `Short` | `4.96` | 696,180.00 USD | 55,960.00 USD | 0.00 USD | `+10.15%` | `11,270.30` |
| `Live` | `Short` | `4.97` | 796,800.00 USD | 100,620.00 USD | 0.00 USD | `+10.37%` | `20,226.00` |
| `Live` | `Short` | `4.99` | 798,520.00 USD | 1,710.00 USD | 0.00 USD | `+10.60%` | `343.70` |
| `Live` | `Short` | `5.00` | 798,860.00 USD | 339.66 USD | 0.00 USD | `+10.82%` | `68.00` |
| `Live` | `Short` | `5.00` | 799,380.00 USD | 528.03 USD | 0.00 USD | `+11.04%` | `105.50` |
| `Live` | `Short` | `5.01` | 1,040,000.00 USD | 240,500.00 USD | 0.00 USD | `+11.26%` | `47,955.70` |
| `Live` | `Short` | `5.04` | 1,040,000.00 USD | 1,360.00 USD | 0.00 USD | `+11.93%` | `269.60` |
| `Live` | `Short` | `5.05` | 1,050,000.00 USD | 5,020.00 USD | 0.00 USD | `+12.15%` | `993.80` |
| `Live` | `Short` | `5.07` | 1,210,000.00 USD | 166,550.00 USD | 0.00 USD | `+12.37%` | `32,883.20` |
| `Live` | `Short` | `5.08` | 1,240,000.00 USD | 28,850.00 USD | 0.00 USD | `+12.59%` | `5,683.80` |
| `Live` | `Short` | `5.08` | 1,240,000.00 USD | 3,190.00 USD | 0.00 USD | `+12.81%` | `627.90` |
| `Live` | `Short` | `5.09` | 1,250,000.00 USD | 4,170.00 USD | 0.00 USD | `+13.04%` | `819.40` |
| `Live` | `Short` | `5.12` | 1,250,000.00 USD | 2,560.00 USD | 0.00 USD | `+13.70%` | `500.00` |
| `Live` | `Short` | `5.13` | 1,250,000.00 USD | 1,080.00 USD | 0.00 USD | `+13.92%` | `210.70` |
| `Live` | `Short` | `5.14` | 2,370,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+14.15%` | `216,880.40` |
| `Live` | `Short` | `5.17` | 2,380,000.00 USD | 9,610.00 USD | 0.00 USD | `+14.59%` | `1,861.50` |
| `Live` | `Short` | `5.17` | 2,380,000.00 USD | 346.72 USD | 0.00 USD | `+14.81%` | `67.00` |
| `Live` | `Short` | `5.18` | 2,380,000.00 USD | 866.93 USD | 0.00 USD | `+15.03%` | `167.20` |
| `Live` | `Short` | `5.20` | 2,380,000.00 USD | 1,570.00 USD | 0.00 USD | `+15.25%` | `302.50` |
| `Live` | `Short` | `5.21` | 3,280,000.00 USD | 898,120.00 USD | 0.00 USD | `+15.48%` | `172,549.20` |
| `Live` | `Short` | `5.22` | 3,350,000.00 USD | 72,110.00 USD | 0.00 USD | `+15.92%` | `13,800.00` |
| `Live` | `Short` | `5.24` | 3,390,000.00 USD | 34,570.00 USD | 0.00 USD | `+16.14%` | `6,603.20` |
| `Live` | `Short` | `5.25` | 3,390,000.00 USD | 143.71 USD | 0.00 USD | `+16.36%` | `27.40` |
| `Live` | `Short` | `5.25` | 3,390,000.00 USD | 288.50 USD | 0.00 USD | `+16.59%` | `54.90` |
| `Live` | `Short` | `5.26` | 3,440,000.00 USD | 50,560.00 USD | 0.00 USD | `+16.81%` | `9,603.50` |
| `Live` | `Short` | `5.28` | 3,440,000.00 USD | 245.29 USD | 0.00 USD | `+17.03%` | `46.50` |
| `Live` | `Short` | `5.29` | 3,440,000.00 USD | 228.84 USD | 0.00 USD | `+17.25%` | `43.30` |
| `Live` | `Short` | `5.30` | 3,440,000.00 USD | 524.66 USD | 0.00 USD | `+17.70%` | `98.90` |
| `Live` | `Short` | `5.32` | 3,440,000.00 USD | 878.04 USD | 0.00 USD | `+17.92%` | `165.20` |
| `Live` | `Short` | `5.34` | 3,460,000.00 USD | 19,840.00 USD | 0.00 USD | `+18.58%` | `3,711.90` |
| `Live` | `Short` | `5.36` | 3,500,000.00 USD | 45,380.00 USD | 0.00 USD | `+18.80%` | `8,474.10` |
| `Live` | `Short` | `5.38` | 3,580,000.00 USD | 77,900.00 USD | 0.00 USD | `+19.25%` | `14,493.40` |
| `Live` | `Short` | `5.42` | 3,580,000.00 USD | 1,000.00 USD | 0.00 USD | `+20.36%` | `184.80` |
| `Live` | `Short` | `5.43` | 3,830,000.00 USD | 252,230.00 USD | 0.00 USD | `+20.58%` | `46,407.80` |
| `Live` | `Short` | `5.45` | 3,840,000.00 USD | 2,180.00 USD | 0.00 USD | `+20.80%` | `400.00` |
| `Live` | `Short` | `5.46` | 3,840,000.00 USD | 2,270.00 USD | 0.00 USD | `+21.25%` | `415.20` |
| `Live` | `Short` | `5.50` | 3,930,000.00 USD | 88,450.00 USD | 0.00 USD | `+21.91%` | `16,097.30` |
| `Live` | `Short` | `5.50` | 3,940,000.00 USD | 9,490.00 USD | 0.00 USD | `+22.13%` | `1,723.30` |
| `Live` | `Short` | `5.51` | 3,980,000.00 USD | 39,430.00 USD | 0.00 USD | `+22.35%` | `7,150.20` |
| `Live` | `Short` | `5.54` | 3,980,000.00 USD | 209.22 USD | 0.00 USD | `+22.80%` | `37.80` |
| `Live` | `Short` | `5.54` | 4,030,000.00 USD | 53,090.00 USD | 0.00 USD | `+23.02%` | `9,574.70` |
| `Live` | `Short` | `5.57` | 4,040,000.00 USD | 8,670.00 USD | 0.00 USD | `+23.46%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,100,000.00 USD | 62,420.00 USD | 0.00 USD | `+23.91%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 4,100,000.00 USD | 686.51 USD | 0.00 USD | `+24.13%` | `122.70` |
| `Live` | `Short` | `5.61` | 4,120,000.00 USD | 17,680.00 USD | 0.00 USD | `+24.35%` | `3,153.90` |
| `Live` | `Short` | `5.66` | 4,120,000.00 USD | 301.98 USD | 0.00 USD | `+25.46%` | `53.40` |
| `Live` | `Short` | `5.67` | 4,130,000.00 USD | 11,350.00 USD | 0.00 USD | `+25.68%` | `2,002.70` |
| `Live` | `Short` | `5.67` | 4,130,000.00 USD | 2,410.00 USD | 0.00 USD | `+25.90%` | `423.80` |
| `Live` | `Short` | `5.68` | 4,170,000.00 USD | 32,270.00 USD | 0.00 USD | `+26.13%` | `5,676.90` |
| `Live` | `Short` | `5.70` | 4,170,000.00 USD | 5,110.00 USD | 0.00 USD | `+26.35%` | `897.40` |
| `Live` | `Short` | `5.71` | 4,170,000.00 USD | 2,130.00 USD | 0.00 USD | `+26.79%` | `372.40` |
| `Live` | `Short` | `5.72` | 4,180,000.00 USD | 2,760.00 USD | 0.00 USD | `+27.01%` | `482.40` |
| `Live` | `Short` | `5.74` | 5,840,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+27.24%` | `290,227.90` |
| `Live` | `Short` | `5.75` | 5,850,000.00 USD | 5,320.00 USD | 0.00 USD | `+27.46%` | `925.90` |
| `Live` | `Short` | `5.75` | 5,850,000.00 USD | 286.02 USD | 0.00 USD | `+27.68%` | `49.70` |
| `Live` | `Short` | `5.78` | 5,850,000.00 USD | 196.93 USD | 0.00 USD | `+28.12%` | `34.10` |
| `Live` | `Short` | `5.80` | 5,860,000.00 USD | 9,420.00 USD | 0.00 USD | `+28.79%` | `1,622.40` |
| `Live` | `Short` | `5.82` | 5,860,000.00 USD | 1,860.00 USD | 0.00 USD | `+29.01%` | `320.50` |
| `Live` | `Short` | `5.84` | 5,860,000.00 USD | 6,670.00 USD | 0.00 USD | `+29.68%` | `1,141.30` |
| `Live` | `Short` | `5.86` | 5,930,000.00 USD | 66,820.00 USD | 0.00 USD | `+29.90%` | `11,413.00` |
| `Live` | `Short` | `5.87` | 5,930,000.00 USD | 604.10 USD | 0.00 USD | `+30.12%` | `103.00` |
| `Live` | `Short` | `5.88` | 5,930,000.00 USD | 190.67 USD | 0.00 USD | `+30.56%` | `32.40` |
| `Live` | `Short` | `5.89` | 6,030,000.00 USD | 96,610.00 USD | 0.00 USD | `+30.78%` | `16,389.10` |
| `Live` | `Short` | `5.92` | 6,030,000.00 USD | 189.28 USD | 0.00 USD | `+31.23%` | `32.00` |
| `Live` | `Short` | `5.95` | 6,030,000.00 USD | 1,400.00 USD | 0.00 USD | `+31.89%` | `234.80` |
| `Live` | `Short` | `5.96` | 6,030,000.00 USD | 1,850.00 USD | 0.00 USD | `+32.34%` | `310.00` |
| `Live` | `Short` | `5.99` | 6,030,000.00 USD | 131.67 USD | 0.00 USD | `+32.78%` | `22.00` |
| `Live` | `Short` | `6.00` | 6,160,000.00 USD | 128,210.00 USD | 0.00 USD | `+33.00%` | `21,385.70` |
| `Live` | `Short` | `6.01` | 6,170,000.00 USD | 6,340.00 USD | 0.00 USD | `+33.45%` | `1,054.70` |
| `Live` | `Short` | `6.03` | 6,190,000.00 USD | 23,060.00 USD | 0.00 USD | `+33.67%` | `3,827.40` |
| `Live` | `Short` | `6.05` | 7,370,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+34.33%` | `194,699.40` |
| `Live` | `Short` | `6.07` | 7,370,000.00 USD | 740.54 USD | 0.00 USD | `+34.56%` | `122.10` |
| `Live` | `Short` | `6.08` | 7,380,000.00 USD | 6,460.00 USD | 0.00 USD | `+35.00%` | `1,062.10` |
| `Live` | `Short` | `6.09` | 7,410,000.00 USD | 37,510.00 USD | 0.00 USD | `+35.22%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 7,430,000.00 USD | 12,520.00 USD | 0.00 USD | `+35.44%` | `2,050.10` |
| `Live` | `Short` | `6.13` | 7,430,000.00 USD | 2,430.00 USD | 0.00 USD | `+36.11%` | `396.10` |
| `Live` | `Short` | `6.22` | 7,760,000.00 USD | 333,060.00 USD | 0.00 USD | `+38.11%` | `53,503.40` |
| `Live` | `Short` | `6.25` | 7,770,000.00 USD | 7,610.00 USD | 0.00 USD | `+38.55%` | `1,218.90` |
| `Live` | `Short` | `6.25` | 7,770,000.00 USD | 439.10 USD | 0.00 USD | `+38.77%` | `70.20` |
| `Live` | `Short` | `6.29` | 7,840,000.00 USD | 75,420.00 USD | 0.00 USD | `+39.44%` | `12,000.00` |
| `Live` | `Short` | `6.32` | 7,840,000.00 USD | 310.70 USD | 0.00 USD | `+40.10%` | `49.20` |
| `Live` | `Short` | `6.33` | 7,850,000.00 USD | 884.37 USD | 0.00 USD | `+40.55%` | `139.60` |
| `Live` | `Short` | `6.34` | 7,850,000.00 USD | 214.46 USD | 0.00 USD | `+40.77%` | `33.80` |
| `Live` | `Short` | `6.37` | 7,930,000.00 USD | 85,200.00 USD | 0.00 USD | `+41.21%` | `13,385.00` |
| `Live` | `Short` | `6.38` | 7,930,000.00 USD | 288.15 USD | 0.00 USD | `+41.43%` | `45.20` |
| `Live` | `Short` | `6.38` | 7,930,000.00 USD | 2,000.00 USD | 0.00 USD | `+41.66%` | `312.80` |
| `Live` | `Short` | `6.41` | 7,940,000.00 USD | 3,780.00 USD | 0.00 USD | `+42.10%` | `590.10` |
| `Live` | `Short` | `6.42` | 7,940,000.00 USD | 943.65 USD | 0.00 USD | `+42.32%` | `147.10` |
| `Live` | `Short` | `6.42` | 7,940,000.00 USD | 346.95 USD | 0.00 USD | `+42.54%` | `54.00` |
| `Live` | `Short` | `6.43` | 8,520,000.00 USD | 584,470.00 USD | 0.00 USD | `+42.77%` | `90,827.50` |
| `Live` | `Short` | `6.45` | 8,530,000.00 USD | 5,270.00 USD | 0.00 USD | `+42.99%` | `818.40` |
| `Live` | `Short` | `6.46` | 8,550,000.00 USD | 21,590.00 USD | 0.00 USD | `+43.21%` | `3,344.50` |
| `Live` | `Short` | `6.46` | 8,550,000.00 USD | 1,940.00 USD | 0.00 USD | `+43.43%` | `300.00` |
| `Live` | `Short` | `6.47` | 8,550,000.00 USD | 637.79 USD | 0.00 USD | `+43.65%` | `98.50` |
| `Live` | `Short` | `6.50` | 8,550,000.00 USD | 144.84 USD | 0.00 USD | `+44.10%` | `22.30` |
| `Live` | `Short` | `6.51` | 8,550,000.00 USD | 536.84 USD | 0.00 USD | `+44.54%` | `82.40` |
| `Live` | `Short` | `6.54` | 8,550,000.00 USD | 1,020.00 USD | 0.00 USD | `+45.21%` | `156.50` |
| `Live` | `Short` | `6.59` | 8,570,000.00 USD | 14,680.00 USD | 0.00 USD | `+46.31%` | `2,226.20` |
| `Live` | `Short` | `6.66` | 8,590,000.00 USD | 17,930.00 USD | 0.00 USD | `+47.65%` | `2,693.80` |
| `Live` | `Short` | `6.67` | 8,590,000.00 USD | 1,370.00 USD | 0.00 USD | `+47.87%` | `205.90` |
| `Live` | `Short` | `6.67` | 8,590,000.00 USD | 200.25 USD | 0.00 USD | `+48.09%` | `30.00` |
| `Live` | `Short` | `6.72` | 8,700,000.00 USD | 115,670.00 USD | 0.00 USD | `+49.20%` | `17,200.00` |
| `Live` | `Short` | `6.74` | 8,710,000.00 USD | 1,680.00 USD | 0.00 USD | `+49.42%` | `250.00` |
| `Live` | `Short` | `6.75` | 9,950,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+49.86%` | `184,570.30` |
| `Live` | `Short` | `6.78` | 9,950,000.00 USD | 1,960.00 USD | 0.00 USD | `+50.31%` | `288.80` |
| `Live` | `Short` | `6.79` | 9,990,000.00 USD | 40,170.00 USD | 0.00 USD | `+50.53%` | `5,920.00` |
| `Live` | `Short` | `6.87` | 10,000,000.00 USD | 3,410.00 USD | 0.00 USD | `+52.31%` | `496.20` |
| `Live` | `Short` | `6.92` | 10,010,000.00 USD | 7,120.00 USD | 0.00 USD | `+53.64%` | `1,027.50` |
| `Live` | `Short` | `6.93` | 10,070,000.00 USD | 61,000.00 USD | 0.00 USD | `+53.86%` | `8,796.10` |
| `Live` | `Short` | `6.99` | 10,070,000.00 USD | 919.23 USD | 0.00 USD | `+54.97%` | `131.60` |
| `Live` | `Short` | `7.03` | 10,080,000.00 USD | 9,030.00 USD | 0.00 USD | `+55.85%` | `1,285.90` |
| `Live` | `Short` | `7.08` | 10,080,000.00 USD | 1,370.00 USD | 0.00 USD | `+57.19%` | `193.30` |
| `Live` | `Short` | `7.12` | 10,120,000.00 USD | 37,880.00 USD | 0.00 USD | `+57.85%` | `5,323.40` |
| `Live` | `Short` | `7.13` | 10,530,000.00 USD | 413,390.00 USD | 0.00 USD | `+58.30%` | `57,938.40` |
| `Live` | `Short` | `7.20` | 20,140,000.00 USD | 9,610,000.00 USD | 0.00 USD | `+59.63%` | `1,336,000.00` |
| `Live` | `Short` | `7.21` | 20,150,000.00 USD | 13,560.00 USD | 0.00 USD | `+60.07%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 20,160,000.00 USD | 4,910.00 USD | 0.00 USD | `+60.51%` | `679.30` |
| `Live` | `Short` | `7.26` | 20,160,000.00 USD | 770.82 USD | 0.00 USD | `+61.18%` | `106.10` |
| `Live` | `Short` | `7.33` | 20,170,000.00 USD | 8,050.00 USD | 0.00 USD | `+62.73%` | `1,097.00` |
| `Live` | `Short` | `7.36` | 20,170,000.00 USD | 119.89 USD | 0.00 USD | `+63.18%` | `16.30` |
| `Live` | `Short` | `7.38` | 20,170,000.00 USD | 154.14 USD | 0.00 USD | `+63.62%` | `20.90` |
| `Live` | `Short` | `7.43` | 20,210,000.00 USD | 38,300.00 USD | 0.00 USD | `+64.95%` | `5,151.20` |
| `Live` | `Short` | `7.45` | 20,210,000.00 USD | 2,480.00 USD | 0.00 USD | `+65.17%` | `332.70` |
| `Live` | `Short` | `7.46` | 20,210,000.00 USD | 1,900.00 USD | 0.00 USD | `+65.39%` | `255.30` |
| `Live` | `Short` | `7.46` | 20,320,000.00 USD | 106,570.00 USD | 0.00 USD | `+65.62%` | `14,276.50` |
| `Live` | `Short` | `7.47` | 20,440,000.00 USD | 122,230.00 USD | 0.00 USD | `+65.84%` | `16,351.90` |
| `Live` | `Short` | `7.49` | 28,220,000.00 USD | 7,780,000.00 USD | 0.00 USD | `+66.06%` | `1,039,604.60` |
| `Live` | `Short` | `7.53` | 28,220,000.00 USD | 1,610.00 USD | 0.00 USD | `+66.95%` | `214.00` |
| `Live` | `Short` | `7.63` | 28,240,000.00 USD | 19,210.00 USD | 0.00 USD | `+69.39%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 28,240,000.00 USD | 360.25 USD | 0.00 USD | `+70.05%` | `47.00` |
| `Live` | `Short` | `7.71` | 28,260,000.00 USD | 15,410.00 USD | 0.00 USD | `+70.94%` | `2,000.00` |
| `Live` | `Short` | `7.74` | 28,260,000.00 USD | 2,690.00 USD | 0.00 USD | `+71.61%` | `347.20` |
| `Live` | `Short` | `7.75` | 28,260,000.00 USD | 629.67 USD | 0.00 USD | `+71.83%` | `81.30` |
| `Live` | `Short` | `7.75` | 28,260,000.00 USD | 812.72 USD | 0.00 USD | `+72.05%` | `104.80` |
| `Live` | `Short` | `7.79` | 28,300,000.00 USD | 33,580.00 USD | 0.00 USD | `+72.94%` | `4,308.50` |
| `Live` | `Short` | `7.82` | 28,320,000.00 USD | 26,200.00 USD | 0.00 USD | `+73.38%` | `3,352.30` |
| `Live` | `Short` | `7.87` | 28,330,000.00 USD | 2,980.00 USD | 0.00 USD | `+74.49%` | `378.70` |
| `Live` | `Short` | `7.88` | 28,350,000.00 USD | 28,880.00 USD | 0.00 USD | `+74.93%` | `3,662.30` |
| `Live` | `Short` | `7.91` | 28,690,000.00 USD | 333,210.00 USD | 0.00 USD | `+75.38%` | `42,151.20` |
| `Live` | `Short` | `7.95` | 28,690,000.00 USD | 6,120.00 USD | 0.00 USD | `+76.27%` | `769.80` |
| `Live` | `Short` | `7.96` | 28,830,000.00 USD | 134,240.00 USD | 0.00 USD | `+76.71%` | `16,854.30` |
| `Live` | `Short` | `8.01` | 29,750,000.00 USD | 923,880.00 USD | 0.00 USD | `+77.60%` | `115,412.50` |
| `Live` | `Short` | `8.03` | 30,190,000.00 USD | 435,420.00 USD | 0.00 USD | `+78.04%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 30,190,000.00 USD | 797.63 USD | 0.00 USD | `+78.93%` | `98.90` |
| `Live` | `Short` | `8.09` | 30,920,000.00 USD | 727,650.00 USD | 0.00 USD | `+79.37%` | `90,000.00` |
| `Live` | `Short` | `8.13` | 31,320,000.00 USD | 409,570.00 USD | 0.00 USD | `+80.48%` | `50,346.40` |
| `Live` | `Short` | `8.19` | 31,340,000.00 USD | 17,550.00 USD | 0.00 USD | `+81.59%` | `2,144.60` |
| `Live` | `Short` | `8.22` | 31,340,000.00 USD | 103.64 USD | 0.00 USD | `+82.48%` | `12.60` |
| `Live` | `Short` | `8.26` | 31,370,000.00 USD | 24,760.00 USD | 0.00 USD | `+83.14%` | `3,000.00` |
| `Live` | `Short` | `8.37` | 32,470,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+85.58%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 32,470,000.00 USD | 577.04 USD | 0.00 USD | `+85.81%` | `68.90` |
| `Live` | `Short` | `8.40` | 32,470,000.00 USD | 3,820.00 USD | 0.00 USD | `+86.47%` | `454.00` |
| `Live` | `Short` | `8.46` | 32,470,000.00 USD | 879.51 USD | 0.00 USD | `+87.80%` | `103.90` |
| `Live` | `Short` | `8.49` | 32,470,000.00 USD | 594.65 USD | 0.00 USD | `+88.47%` | `70.00` |
| `Live` | `Short` | `8.53` | 32,470,000.00 USD | 578.85 USD | 0.00 USD | `+89.13%` | `67.90` |
| `Live` | `Short` | `8.54` | 32,480,000.00 USD | 8,530.00 USD | 0.00 USD | `+89.36%` | `999.50` |
| `Live` | `Short` | `8.54` | 32,490,000.00 USD | 4,950.00 USD | 0.00 USD | `+89.58%` | `579.60` |
| `Live` | `Short` | `8.56` | 32,490,000.00 USD | 239.82 USD | 0.00 USD | `+90.02%` | `28.00` |
| `Live` | `Short` | `8.57` | 32,490,000.00 USD | 583.96 USD | 0.00 USD | `+90.24%` | `68.10` |
| `Live` | `Short` | `8.59` | 32,500,000.00 USD | 16,260.00 USD | 0.00 USD | `+90.46%` | `1,894.30` |
| `Live` | `Short` | `8.62` | 32,510,000.00 USD | 2,850.00 USD | 0.00 USD | `+91.35%` | `330.80` |
| `Live` | `Short` | `8.66` | 32,950,000.00 USD | 447,370.00 USD | 0.00 USD | `+92.24%` | `51,630.00` |
| `Live` | `Short` | `8.68` | 32,960,000.00 USD | 2,320.00 USD | 0.00 USD | `+92.46%` | `267.10` |
| `Live` | `Short` | `8.69` | 32,960,000.00 USD | 3,770.00 USD | 0.00 USD | `+92.68%` | `434.40` |
| `Live` | `Short` | `8.71` | 34,840,000.00 USD | 1,880,000.00 USD | 0.00 USD | `+93.13%` | `215,700.00` |
| `Live` | `Short` | `8.79` | 36,370,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+94.90%` | `174,091.10` |
| `Live` | `Short` | `8.84` | 36,390,000.00 USD | 19,980.00 USD | 0.00 USD | `+96.01%` | `2,261.80` |
| `Live` | `Short` | `8.85` | 36,390,000.00 USD | 6,380.00 USD | 0.00 USD | `+96.23%` | `721.60` |
| `Live` | `Short` | `8.87` | 36,400,000.00 USD | 5,000.00 USD | 0.00 USD | `+96.68%` | `564.00` |
| `Live` | `Short` | `8.91` | 36,400,000.00 USD | 867.43 USD | 0.00 USD | `+97.79%` | `97.30` |
| `Live` | `Short` | `8.95` | 37,050,000.00 USD | 647,770.00 USD | 0.00 USD | `+98.45%` | `72,416.70` |
| `Live` | `Short` | `8.96` | 37,070,000.00 USD | 17,370.00 USD | 0.00 USD | `+98.67%` | `1,940.10` |
| `Live` | `Short` | `8.96` | 37,090,000.00 USD | 19,880.00 USD | 0.00 USD | `+98.90%` | `2,217.40` |
| `Live` | `Short` | `8.97` | 42,790,000.00 USD | 5,710,000.00 USD | 0.00 USD | `+99.12%` | `636,076.70` |
| `Live` | `Short` | `9.01` | 42,790,000.00 USD | 190.91 USD | 0.00 USD | `+99.78%` | `21.20` |
| `Live` | `Short` | `9.02` | 42,970,000.00 USD | 180,300.00 USD | 0.00 USD | `+100.00%` | `20,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 4,490,000.00 USD | 0.00 USD | 585.51 USD | `-77.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 4,490,000.00 USD | 0.00 USD | 345.25 USD | `-69.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 4,490,000.00 USD | 0.00 USD | 5,640.00 USD | `-69.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 4,480,000.00 USD | 0.00 USD | 997.29 USD | `-69.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 4,480,000.00 USD | 0.00 USD | 139.83 USD | `-66.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 4,480,000.00 USD | 0.00 USD | 113.28 USD | `-65.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 4,480,000.00 USD | 0.00 USD | 4,000.00 USD | `-65.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 4,480,000.00 USD | 0.00 USD | 324.22 USD | `-65.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 4,480,000.00 USD | 0.00 USD | 4,590.00 USD | `-64.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 4,470,000.00 USD | 0.00 USD | 739.67 USD | `-64.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 4,470,000.00 USD | 0.00 USD | 1,740.00 USD | `-63.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 4,470,000.00 USD | 0.00 USD | 669.02 USD | `-62.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 4,470,000.00 USD | 0.00 USD | 105.88 USD | `-62.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 4,470,000.00 USD | 0.00 USD | 172.50 USD | `-61.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 4,470,000.00 USD | 0.00 USD | 10,650.00 USD | `-60.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 4,460,000.00 USD | 0.00 USD | 722.00 USD | `-59.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 4,460,000.00 USD | 0.00 USD | 259.00 USD | `-59.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 4,460,000.00 USD | 0.00 USD | 103.84 USD | `-59.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 4,460,000.00 USD | 0.00 USD | 109.00 USD | `-59.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 4,460,000.00 USD | 0.00 USD | 222.19 USD | `-58.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 4,460,000.00 USD | 0.00 USD | 10,280.00 USD | `-58.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 4,450,000.00 USD | 0.00 USD | 558.36 USD | `-57.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 4,440,000.00 USD | 0.00 USD | 1,520.00 USD | `-57.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 4,440,000.00 USD | 0.00 USD | 222.14 USD | `-57.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 4,440,000.00 USD | 0.00 USD | 279.50 USD | `-56.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 4,440,000.00 USD | 0.00 USD | 197.50 USD | `-56.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,440,000.00 USD | 0.00 USD | 935.66 USD | `-55.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,440,000.00 USD | 0.00 USD | 18,860.00 USD | `-55.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 4,420,000.00 USD | 0.00 USD | 3,020.00 USD | `-55.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 4,420,000.00 USD | 0.00 USD | 214.52 USD | `-54.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 4,420,000.00 USD | 0.00 USD | 1,200.00 USD | `-54.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 4,420,000.00 USD | 0.00 USD | 578.41 USD | `-54.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 4,420,000.00 USD | 0.00 USD | 18,070.00 USD | `-53.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 4,400,000.00 USD | 0.00 USD | 13,980.00 USD | `-53.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 4,390,000.00 USD | 0.00 USD | 107.23 USD | `-53.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 4,390,000.00 USD | 0.00 USD | 1,590.00 USD | `-52.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 4,380,000.00 USD | 0.00 USD | 6,970.00 USD | `-52.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 4,380,000.00 USD | 0.00 USD | 310.32 USD | `-52.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 4,380,000.00 USD | 0.00 USD | 1,170.00 USD | `-51.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 4,380,000.00 USD | 0.00 USD | 576.18 USD | `-51.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 4,370,000.00 USD | 0.00 USD | 295.67 USD | `-51.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 4,370,000.00 USD | 0.00 USD | 2,940.00 USD | `-51.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 4,370,000.00 USD | 0.00 USD | 812.68 USD | `-50.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 4,370,000.00 USD | 0.00 USD | 1,440.00 USD | `-50.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 4,370,000.00 USD | 0.00 USD | 490.14 USD | `-50.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 4,370,000.00 USD | 0.00 USD | 13,490.00 USD | `-50.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 4,360,000.00 USD | 0.00 USD | 478.06 USD | `-49.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 4,350,000.00 USD | 0.00 USD | 540.88 USD | `-49.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 4,350,000.00 USD | 0.00 USD | 1,210.00 USD | `-49.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 4,350,000.00 USD | 0.00 USD | 759.76 USD | `-49.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 4,350,000.00 USD | 0.00 USD | 23,020.00 USD | `-49.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 4,330,000.00 USD | 0.00 USD | 3,690.00 USD | `-48.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 4,330,000.00 USD | 0.00 USD | 3,050.00 USD | `-48.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 4,320,000.00 USD | 0.00 USD | 467.00 USD | `-48.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 4,320,000.00 USD | 0.00 USD | 506.75 USD | `-47.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 4,320,000.00 USD | 0.00 USD | 214.27 USD | `-47.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 4,320,000.00 USD | 0.00 USD | 428.69 USD | `-47.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 4,320,000.00 USD | 0.00 USD | 322.45 USD | `-47.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 4,320,000.00 USD | 0.00 USD | 108.25 USD | `-46.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 4,320,000.00 USD | 0.00 USD | 3,850.00 USD | `-46.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 4,320,000.00 USD | 0.00 USD | 799.04 USD | `-46.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 4,320,000.00 USD | 0.00 USD | 6,830.00 USD | `-45.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 4,310,000.00 USD | 0.00 USD | 137.16 USD | `-45.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 4,310,000.00 USD | 0.00 USD | 504.41 USD | `-45.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 4,310,000.00 USD | 0.00 USD | 963.93 USD | `-44.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 4,310,000.00 USD | 0.00 USD | 13,880.00 USD | `-44.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 4,290,000.00 USD | 0.00 USD | 541.98 USD | `-44.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 4,290,000.00 USD | 0.00 USD | 108.75 USD | `-43.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 4,290,000.00 USD | 0.00 USD | 766.55 USD | `-43.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 4,290,000.00 USD | 0.00 USD | 1,010.00 USD | `-43.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 4,290,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 4,290,000.00 USD | 0.00 USD | 100.04 USD | `-42.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 4,290,000.00 USD | 0.00 USD | 5,090.00 USD | `-41.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 4,280,000.00 USD | 0.00 USD | 226.57 USD | `-40.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 4,280,000.00 USD | 0.00 USD | 104.98 USD | `-40.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 4,280,000.00 USD | 0.00 USD | 329.33 USD | `-40.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 4,280,000.00 USD | 0.00 USD | 7,160.00 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 4,280,000.00 USD | 0.00 USD | 107.21 USD | `-39.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 4,280,000.00 USD | 0.00 USD | 197.37 USD | `-39.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 4,280,000.00 USD | 0.00 USD | 8,390.00 USD | `-38.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 4,270,000.00 USD | 0.00 USD | 108.39 USD | `-38.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 4,270,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 4,270,000.00 USD | 0.00 USD | 14,140.00 USD | `-38.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 4,250,000.00 USD | 0.00 USD | 437.98 USD | `-37.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 4,250,000.00 USD | 0.00 USD | 2,000.00 USD | `-37.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 4,250,000.00 USD | 0.00 USD | 8,250.00 USD | `-37.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 4,240,000.00 USD | 0.00 USD | 109.53 USD | `-36.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.87` | 4,240,000.00 USD | 0.00 USD | 1,810.00 USD | `-36.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 4,240,000.00 USD | 0.00 USD | 437.00 USD | `-36.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 4,240,000.00 USD | 0.00 USD | 746.06 USD | `-35.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 4,240,000.00 USD | 0.00 USD | 4,870.00 USD | `-35.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 4,230,000.00 USD | 0.00 USD | 696.98 USD | `-35.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 4,230,000.00 USD | 0.00 USD | 358.90 USD | `-35.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 4,230,000.00 USD | 0.00 USD | 15,370.00 USD | `-34.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 4,220,000.00 USD | 0.00 USD | 523.32 USD | `-34.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 4,220,000.00 USD | 0.00 USD | 2,330.00 USD | `-34.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 4,210,000.00 USD | 0.00 USD | 16,090.00 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 4,200,000.00 USD | 0.00 USD | 1,020.00 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 4,200,000.00 USD | 0.00 USD | 345.76 USD | `-32.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 4,200,000.00 USD | 0.00 USD | 214.57 USD | `-32.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 4,200,000.00 USD | 0.00 USD | 109.42 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 4,200,000.00 USD | 0.00 USD | 721.58 USD | `-31.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 4,200,000.00 USD | 0.00 USD | 9,300.00 USD | `-31.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 4,190,000.00 USD | 0.00 USD | 104.69 USD | `-30.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 4,190,000.00 USD | 0.00 USD | 315.69 USD | `-30.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 4,190,000.00 USD | 0.00 USD | 214.17 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 4,190,000.00 USD | 0.00 USD | 641.10 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 4,190,000.00 USD | 0.00 USD | 212.06 USD | `-29.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 4,190,000.00 USD | 0.00 USD | 1,030.00 USD | `-29.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 4,180,000.00 USD | 0.00 USD | 218.81 USD | `-29.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 4,180,000.00 USD | 0.00 USD | 31,570.00 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 4,150,000.00 USD | 0.00 USD | 144.67 USD | `-28.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 4,150,000.00 USD | 0.00 USD | 21,850.00 USD | `-28.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 4,130,000.00 USD | 0.00 USD | 1,880.00 USD | `-27.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 4,130,000.00 USD | 0.00 USD | 104.81 USD | `-27.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 4,130,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 4,130,000.00 USD | 0.00 USD | 1,070.00 USD | `-26.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 4,130,000.00 USD | 0.00 USD | 15,820.00 USD | `-26.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 4,110,000.00 USD | 0.00 USD | 240.67 USD | `-26.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 4,110,000.00 USD | 0.00 USD | 306.56 USD | `-26.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 4,110,000.00 USD | 0.00 USD | 1,670.00 USD | `-26.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 4,110,000.00 USD | 0.00 USD | 505.76 USD | `-25.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 4,110,000.00 USD | 0.00 USD | 73,220.00 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 4,030,000.00 USD | 0.00 USD | 12,850.00 USD | `-25.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 4,020,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 4,010,000.00 USD | 0.00 USD | 107,490.00 USD | `-24.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 3,910,000.00 USD | 0.00 USD | 25,250.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 3,880,000.00 USD | 0.00 USD | 506.22 USD | `-24.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 3,880,000.00 USD | 0.00 USD | 103.05 USD | `-23.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 3,880,000.00 USD | 0.00 USD | 2,550.00 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 3,880,000.00 USD | 0.00 USD | 1,380.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 3,880,000.00 USD | 0.00 USD | 344.07 USD | `-23.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 3,880,000.00 USD | 0.00 USD | 112,400.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 3,760,000.00 USD | 0.00 USD | 17,360.00 USD | `-22.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 3,750,000.00 USD | 0.00 USD | 2,030.00 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 3,740,000.00 USD | 0.00 USD | 12,040.00 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 3,730,000.00 USD | 0.00 USD | 633.50 USD | `-21.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 3,730,000.00 USD | 0.00 USD | 333.68 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,730,000.00 USD | 0.00 USD | 72,860.00 USD | `-20.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,660,000.00 USD | 0.00 USD | 179.25 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,660,000.00 USD | 0.00 USD | 643.50 USD | `-20.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,660,000.00 USD | 0.00 USD | 1,870.00 USD | `-20.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,660,000.00 USD | 0.00 USD | 632.99 USD | `-19.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,650,000.00 USD | 0.00 USD | 172.19 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 3,650,000.00 USD | 0.00 USD | 13,400.00 USD | `-19.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,640,000.00 USD | 0.00 USD | 1,260.00 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,640,000.00 USD | 0.00 USD | 3,900.00 USD | `-18.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,640,000.00 USD | 0.00 USD | 174.09 USD | `-18.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,640,000.00 USD | 0.00 USD | 367.50 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,640,000.00 USD | 0.00 USD | 9,210.00 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,630,000.00 USD | 0.00 USD | 4,370.00 USD | `-18.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,620,000.00 USD | 0.00 USD | 17,930.00 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,600,000.00 USD | 0.00 USD | 1,440.00 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,600,000.00 USD | 0.00 USD | 1,030.00 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,600,000.00 USD | 0.00 USD | 44,700.00 USD | `-17.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 3,560,000.00 USD | 0.00 USD | 18,440.00 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,540,000.00 USD | 0.00 USD | 6,850.00 USD | `-16.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,530,000.00 USD | 0.00 USD | 3,940.00 USD | `-16.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,530,000.00 USD | 0.00 USD | 189,250.00 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,340,000.00 USD | 0.00 USD | 1,900.00 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,340,000.00 USD | 0.00 USD | 1,420.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,340,000.00 USD | 0.00 USD | 18,070.00 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,320,000.00 USD | 0.00 USD | 23,060.00 USD | `-15.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,290,000.00 USD | 0.00 USD | 2,240.00 USD | `-14.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,290,000.00 USD | 0.00 USD | 2,100.00 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,290,000.00 USD | 0.00 USD | 3,070.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 3,290,000.00 USD | 0.00 USD | 2,460.00 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,280,000.00 USD | 0.00 USD | 5,550.00 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,280,000.00 USD | 0.00 USD | 4,990.00 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,270,000.00 USD | 0.00 USD | 1,310.00 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,270,000.00 USD | 0.00 USD | 42,000.00 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,230,000.00 USD | 0.00 USD | 2,070.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,230,000.00 USD | 0.00 USD | 1,120.00 USD | `-12.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,230,000.00 USD | 0.00 USD | 1,420.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,230,000.00 USD | 0.00 USD | 187.78 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,230,000.00 USD | 0.00 USD | 13,970.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,210,000.00 USD | 0.00 USD | 301,690.00 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,910,000.00 USD | 0.00 USD | 4,570.00 USD | `-11.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,910,000.00 USD | 0.00 USD | 3,950.00 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,900,000.00 USD | 0.00 USD | 513.36 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,900,000.00 USD | 0.00 USD | 248,940.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 2,650,000.00 USD | 0.00 USD | 5,440.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 2,650,000.00 USD | 0.00 USD | 4,510.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,640,000.00 USD | 0.00 USD | 2,100.00 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,640,000.00 USD | 0.00 USD | 6,930.00 USD | `-10.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 2,630,000.00 USD | 0.00 USD | 1,850.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 2,630,000.00 USD | 0.00 USD | 860.56 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,630,000.00 USD | 0.00 USD | 504,780.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,130,000.00 USD | 0.00 USD | 74,820.00 USD | `-9.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 2,050,000.00 USD | 0.00 USD | 1,250.00 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 2,050,000.00 USD | 0.00 USD | 29,060.00 USD | `-8.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 2,020,000.00 USD | 0.00 USD | 2,900.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 2,020,000.00 USD | 0.00 USD | 10,440.00 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 2,010,000.00 USD | 0.00 USD | 351,730.00 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 1,660,000.00 USD | 0.00 USD | 1,910.00 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 1,650,000.00 USD | 0.00 USD | 37,410.00 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,620,000.00 USD | 0.00 USD | 4,290.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,610,000.00 USD | 0.00 USD | 31,660.00 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 1,580,000.00 USD | 0.00 USD | 22,340.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 1,560,000.00 USD | 0.00 USD | 34,010.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,520,000.00 USD | 0.00 USD | 150,260.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,370,000.00 USD | 0.00 USD | 6,750.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 1,370,000.00 USD | 0.00 USD | 91,900.00 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 1,270,000.00 USD | 0.00 USD | 30,510.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 1,240,000.00 USD | 0.00 USD | 44,410.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 1,200,000.00 USD | 0.00 USD | 33,310.00 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 1,170,000.00 USD | 0.00 USD | 7,980.00 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 1,160,000.00 USD | 0.00 USD | 160,810.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 997,660.00 USD | 0.00 USD | 24,640.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 973,020.00 USD | 0.00 USD | 61,710.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 911,310.00 USD | 0.00 USD | 2,670.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 908,640.00 USD | 0.00 USD | 53,330.00 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 855,310.00 USD | 0.00 USD | 77,370.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 777,940.00 USD | 0.00 USD | 9,680.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 768,260.00 USD | 0.00 USD | 107,060.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.36` | 661,200.00 USD | 0.00 USD | 14,950.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.37` | 646,240.00 USD | 0.00 USD | 41,730.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 604,520.00 USD | 0.00 USD | 1,070.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 603,450.00 USD | 0.00 USD | 24,440.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.39` | 579,010.00 USD | 0.00 USD | 21,970.00 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.41` | 557,040.00 USD | 0.00 USD | 70,370.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 486,660.00 USD | 0.00 USD | 14,620.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 472,050.00 USD | 0.00 USD | 128,040.00 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.43` | 344,010.00 USD | 0.00 USD | 30,970.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.45` | 313,040.00 USD | 0.00 USD | 3,300.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.46` | 309,740.00 USD | 0.00 USD | 24,650.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.46` | 285,090.00 USD | 0.00 USD | 9,320.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.47` | 275,770.00 USD | 0.00 USD | 223.75 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 275,550.00 USD | 0.00 USD | 1,060.00 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.50` | 274,480.00 USD | 0.00 USD | 10,340.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.50` | 264,140.00 USD | 0.00 USD | 264,140.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 154,150.00 USD | 154,150.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 158,800.00 USD | 4,650.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 162,140.00 USD | 3,340.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 197,160.00 USD | 35,020.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 322,880.00 USD | 125,720.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 324,930.00 USD | 2,050.00 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 327,990.00 USD | 3,060.00 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 336,500.00 USD | 8,520.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 340,840.00 USD | 4,330.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 343,810.00 USD | 2,970.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 344,860.00 USD | 1,050.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 396,150.00 USD | 51,290.00 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 491,260.00 USD | 95,110.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 542,650.00 USD | 51,390.00 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 563,460.00 USD | 20,820.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 958,170.00 USD | 394,710.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 959,030.00 USD | 855.06 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 969,120.00 USD | 10,100.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 969,420.00 USD | 294.85 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,450,000.00 USD | 482,190.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,450,000.00 USD | 1,700.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,460,000.00 USD | 3,850.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,610,000.00 USD | 155,610.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,660,000.00 USD | 45,150.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,690,000.00 USD | 28,170.00 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,720,000.00 USD | 38,580.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,820,000.00 USD | 97,870.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,660,000.00 USD | 833,790.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,660,000.00 USD | 6,080.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 2,790,000.00 USD | 126,400.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,800,000.00 USD | 8,200.00 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,960,000.00 USD | 164,420.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,960,000.00 USD | 1,210.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 2,970,000.00 USD | 11,760.00 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,020,000.00 USD | 43,120.00 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,050,000.00 USD | 28,220.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,060,000.00 USD | 10,850.00 USD | 0.00 USD | `+8.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,070,000.00 USD | 9,920.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,070,000.00 USD | 4,060.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,180,000.00 USD | 111,870.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,180,000.00 USD | 529.84 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,200,000.00 USD | 12,520.00 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,210,000.00 USD | 12,130.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,210,000.00 USD | 114.72 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,210,000.00 USD | 3,180.00 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,260,000.00 USD | 47,350.00 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,260,000.00 USD | 187.06 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,350,000.00 USD | 96,060.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,370,000.00 USD | 11,390.00 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,510,000.00 USD | 141,350.00 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,530,000.00 USD | 26,480.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,540,000.00 USD | 5,140.00 USD | 0.00 USD | `+11.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,670,000.00 USD | 132,490.00 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,670,000.00 USD | 219.46 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,720,000.00 USD | 50,950.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,730,000.00 USD | 3,550.00 USD | 0.00 USD | `+12.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,820,000.00 USD | 90,150.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,700,000.00 USD | 882,870.00 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,700,000.00 USD | 547.20 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,750,000.00 USD | 51,930.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,770,000.00 USD | 15,350.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,770,000.00 USD | 113.26 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,780,000.00 USD | 8,600.00 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,780,000.00 USD | 3,670.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,780,000.00 USD | 3,770.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,780,000.00 USD | 1,200.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,780,000.00 USD | 327.58 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,790,000.00 USD | 2,190.00 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,790,000.00 USD | 5,960.00 USD | 0.00 USD | `+15.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,820,000.00 USD | 29,930.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,820,000.00 USD | 1,710.00 USD | 0.00 USD | `+15.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,950,000.00 USD | 120,710.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,950,000.00 USD | 9,820.00 USD | 0.00 USD | `+16.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,960,000.00 USD | 537.61 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,510,000.00 USD | 556,340.00 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 5,520,000.00 USD | 5,540.00 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 5,520,000.00 USD | 589.22 USD | 0.00 USD | `+17.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,520,000.00 USD | 733.03 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,520,000.00 USD | 693.64 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,570,000.00 USD | 52,560.00 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,580,000.00 USD | 3,090.00 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,580,000.00 USD | 961.16 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,580,000.00 USD | 2,020.00 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,580,000.00 USD | 6,220.00 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,690,000.00 USD | 107,860.00 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,700,000.00 USD | 9,950.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,700,000.00 USD | 438.60 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,710,000.00 USD | 6,080.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,750,000.00 USD | 43,730.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,870,000.00 USD | 114,380.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,870,000.00 USD | 425.62 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,900,000.00 USD | 36,790.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 5,910,000.00 USD | 4,750.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,920,000.00 USD | 13,190.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,940,000.00 USD | 20,460.00 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,160,000.00 USD | 219,590.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 6,200,000.00 USD | 35,450.00 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 6,240,000.00 USD | 45,900.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,240,000.00 USD | 1,180.00 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,410,000.00 USD | 163,340.00 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,410,000.00 USD | 5,600.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,460,000.00 USD | 45,680.00 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,480,000.00 USD | 18,790.00 USD | 0.00 USD | `+22.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,560,000.00 USD | 81,240.00 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,610,000.00 USD | 49,440.00 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,620,000.00 USD | 14,320.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,630,000.00 USD | 5,560.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,650,000.00 USD | 20,540.00 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,650,000.00 USD | 384.94 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,670,000.00 USD | 16,530.00 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,670,000.00 USD | 5,510.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,670,000.00 USD | 581.53 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,670,000.00 USD | 295.23 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,680,000.00 USD | 3,290.00 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,680,000.00 USD | 281.55 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,690,000.00 USD | 9,380.00 USD | 0.00 USD | `+25.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,690,000.00 USD | 2,840.00 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,690,000.00 USD | 5,860.00 USD | 0.00 USD | `+26.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,810,000.00 USD | 116,400.00 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,810,000.00 USD | 2,210.00 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,820,000.00 USD | 5,720.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,840,000.00 USD | 24,700.00 USD | 0.00 USD | `+27.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,850,000.00 USD | 2,430.00 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,850,000.00 USD | 286.94 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,850,000.00 USD | 2,900.00 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,860,000.00 USD | 7,120.00 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,860,000.00 USD | 6,030.00 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,860,000.00 USD | 1,970.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,870,000.00 USD | 3,100.00 USD | 0.00 USD | `+29.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,870,000.00 USD | 1,150.00 USD | 0.00 USD | `+29.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,870,000.00 USD | 2,960.00 USD | 0.00 USD | `+29.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,870,000.00 USD | 3,450.00 USD | 0.00 USD | `+30.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,870,000.00 USD | 345.45 USD | 0.00 USD | `+30.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.89` | 6,880,000.00 USD | 2,950.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,930,000.00 USD | 51,980.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,930,000.00 USD | 1,790.00 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,930,000.00 USD | 1,400.00 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 7,070,000.00 USD | 133,540.00 USD | 0.00 USD | `+31.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,540,000.00 USD | 469,530.00 USD | 0.00 USD | `+32.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,540,000.00 USD | 5,620.00 USD | 0.00 USD | `+32.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 7,550,000.00 USD | 9,410.00 USD | 0.00 USD | `+32.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,670,000.00 USD | 119,340.00 USD | 0.00 USD | `+32.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,670,000.00 USD | 3,000.00 USD | 0.00 USD | `+33.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,810,000.00 USD | 133,160.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,820,000.00 USD | 13,610.00 USD | 0.00 USD | `+33.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,880,000.00 USD | 60,250.00 USD | 0.00 USD | `+33.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,880,000.00 USD | 2,380.00 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,890,000.00 USD | 3,300.00 USD | 0.00 USD | `+34.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,890,000.00 USD | 2,550.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,890,000.00 USD | 425.76 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,890,000.00 USD | 2,030.00 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,890,000.00 USD | 4,120.00 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,900,000.00 USD | 2,000.00 USD | 0.00 USD | `+35.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,960,000.00 USD | 61,050.00 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,960,000.00 USD | 6,870.00 USD | 0.00 USD | `+35.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,970,000.00 USD | 1,200.00 USD | 0.00 USD | `+36.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,980,000.00 USD | 11,620.00 USD | 0.00 USD | `+36.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,980,000.00 USD | 1,940.00 USD | 0.00 USD | `+36.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,980,000.00 USD | 1,410.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,990,000.00 USD | 4,010.00 USD | 0.00 USD | `+37.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,990,000.00 USD | 3,960.00 USD | 0.00 USD | `+37.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,990,000.00 USD | 3,830.00 USD | 0.00 USD | `+37.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 8,060,000.00 USD | 66,850.00 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 8,060,000.00 USD | 1,890.00 USD | 0.00 USD | `+37.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 8,060,000.00 USD | 195.46 USD | 0.00 USD | `+38.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 8,070,000.00 USD | 7,480.00 USD | 0.00 USD | `+38.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 8,070,000.00 USD | 3,670.00 USD | 0.00 USD | `+39.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 8,080,000.00 USD | 3,680.00 USD | 0.00 USD | `+39.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 8,080,000.00 USD | 7,370.00 USD | 0.00 USD | `+39.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 8,080,000.00 USD | 412.37 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 8,090,000.00 USD | 602.77 USD | 0.00 USD | `+40.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 8,090,000.00 USD | 449.79 USD | 0.00 USD | `+40.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 8,090,000.00 USD | 2,810.00 USD | 0.00 USD | `+40.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 8,090,000.00 USD | 3,560.00 USD | 0.00 USD | `+41.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 8,100,000.00 USD | 3,230.00 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 8,100,000.00 USD | 6,880.00 USD | 0.00 USD | `+42.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.42` | 8,100,000.00 USD | 2,120.00 USD | 0.00 USD | `+42.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 8,100,000.00 USD | 613.26 USD | 0.00 USD | `+42.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.49` | 8,110,000.00 USD | 2,080.00 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 8,120,000.00 USD | 10,590.00 USD | 0.00 USD | `+44.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 8,160,000.00 USD | 43,090.00 USD | 0.00 USD | `+44.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 8,160,000.00 USD | 234.54 USD | 0.00 USD | `+44.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 8,170,000.00 USD | 14,070.00 USD | 0.00 USD | `+45.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 8,180,000.00 USD | 1,630.00 USD | 0.00 USD | `+46.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 8,180,000.00 USD | 2,390.00 USD | 0.00 USD | `+46.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 8,180,000.00 USD | 1,620.00 USD | 0.00 USD | `+46.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 8,180,000.00 USD | 1,970.00 USD | 0.00 USD | `+46.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 8,190,000.00 USD | 3,220.00 USD | 0.00 USD | `+47.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.66` | 8,190,000.00 USD | 1,950.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 8,190,000.00 USD | 450.55 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 8,190,000.00 USD | 3,060.00 USD | 0.00 USD | `+48.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 8,190,000.00 USD | 1,930.00 USD | 0.00 USD | `+48.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 8,200,000.00 USD | 3,070.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 8,200,000.00 USD | 1,920.00 USD | 0.00 USD | `+48.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 8,200,000.00 USD | 3,120.00 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 8,200,000.00 USD | 1,550.00 USD | 0.00 USD | `+49.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 8,210,000.00 USD | 3,080.00 USD | 0.00 USD | `+50.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 8,210,000.00 USD | 647.56 USD | 0.00 USD | `+50.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 8,210,000.00 USD | 1,420.00 USD | 0.00 USD | `+50.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 8,210,000.00 USD | 2,130.00 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 8,210,000.00 USD | 3,140.00 USD | 0.00 USD | `+51.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 8,210,000.00 USD | 342.25 USD | 0.00 USD | `+51.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 8,220,000.00 USD | 1,830.00 USD | 0.00 USD | `+52.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 8,220,000.00 USD | 2,990.00 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 8,220,000.00 USD | 2,970.00 USD | 0.00 USD | `+52.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 8,220,000.00 USD | 391.51 USD | 0.00 USD | `+53.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 8,220,000.00 USD | 504.21 USD | 0.00 USD | `+54.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.96` | 8,220,000.00 USD | 1,900.00 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 8,220,000.00 USD | 166.00 USD | 0.00 USD | `+54.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 8,230,000.00 USD | 4,190.00 USD | 0.00 USD | `+54.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 8,250,000.00 USD | 17,380.00 USD | 0.00 USD | `+55.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 8,250,000.00 USD | 1,750.00 USD | 0.00 USD | `+55.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 8,250,000.00 USD | 2,860.00 USD | 0.00 USD | `+56.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 8,250,000.00 USD | 236.31 USD | 0.00 USD | `+56.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 8,250,000.00 USD | 1,840.00 USD | 0.00 USD | `+57.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 8,250,000.00 USD | 264.31 USD | 0.00 USD | `+57.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 8,250,000.00 USD | 599.34 USD | 0.00 USD | `+58.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 8,250,000.00 USD | 193.19 USD | 0.00 USD | `+58.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 8,260,000.00 USD | 3,950.00 USD | 0.00 USD | `+59.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 8,260,000.00 USD | 1,870.00 USD | 0.00 USD | `+60.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.22` | 8,260,000.00 USD | 1,770.00 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 8,420,000.00 USD | 160,550.00 USD | 0.00 USD | `+60.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 8,420,000.00 USD | 1,750.00 USD | 0.00 USD | `+61.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 8,420,000.00 USD | 731.50 USD | 0.00 USD | `+62.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 8,430,000.00 USD | 1,730.00 USD | 0.00 USD | `+62.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 8,430,000.00 USD | 1,710.00 USD | 0.00 USD | `+63.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 8,440,000.00 USD | 7,870.00 USD | 0.00 USD | `+63.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 8,440,000.00 USD | 630.05 USD | 0.00 USD | `+64.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 8,440,000.00 USD | 2,610.00 USD | 0.00 USD | `+64.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 8,450,000.00 USD | 7,900.00 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 8,450,000.00 USD | 1,620.00 USD | 0.00 USD | `+67.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 8,450,000.00 USD | 4,640.00 USD | 0.00 USD | `+68.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 8,450,000.00 USD | 371.88 USD | 0.00 USD | `+68.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 8,460,000.00 USD | 2,510.00 USD | 0.00 USD | `+68.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 8,460,000.00 USD | 380.68 USD | 0.00 USD | `+70.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 8,460,000.00 USD | 133.12 USD | 0.00 USD | `+70.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 8,460,000.00 USD | 1,490.00 USD | 0.00 USD | `+72.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 8,460,000.00 USD | 1,470.00 USD | 0.00 USD | `+72.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 8,470,000.00 USD | 11,170.00 USD | 0.00 USD | `+72.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 8,500,000.00 USD | 34,360.00 USD | 0.00 USD | `+73.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 8,510,000.00 USD | 399.35 USD | 0.00 USD | `+73.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 8,510,000.00 USD | 100.29 USD | 0.00 USD | `+73.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 8,510,000.00 USD | 1,550.00 USD | 0.00 USD | `+74.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 8,520,000.00 USD | 10,610.00 USD | 0.00 USD | `+76.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 8,520,000.00 USD | 309.43 USD | 0.00 USD | `+76.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 8,650,000.00 USD | 134,570.00 USD | 0.00 USD | `+77.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 8,730,000.00 USD | 81,310.00 USD | 0.00 USD | `+78.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 8,730,000.00 USD | 1,390.00 USD | 0.00 USD | `+80.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 8,740,000.00 USD | 216.90 USD | 0.00 USD | `+81.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 8,740,000.00 USD | 738.45 USD | 0.00 USD | `+82.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 8,740,000.00 USD | 1,350.00 USD | 0.00 USD | `+84.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 8,790,000.00 USD | 56,000.00 USD | 0.00 USD | `+86.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 8,790,000.00 USD | 1,260.00 USD | 0.00 USD | `+86.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 8,900,000.00 USD | 103,010.00 USD | 0.00 USD | `+86.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 8,900,000.00 USD | 1,330.00 USD | 0.00 USD | `+87.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 8,900,000.00 USD | 721.22 USD | 0.00 USD | `+87.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 8,900,000.00 USD | 2,010.00 USD | 0.00 USD | `+90.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 8,900,000.00 USD | 596.33 USD | 0.00 USD | `+92.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 8,910,000.00 USD | 3,670.00 USD | 0.00 USD | `+92.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 8,910,000.00 USD | 1,600.00 USD | 0.00 USD | `+95.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 8,910,000.00 USD | 3,430.00 USD | 0.00 USD | `+95.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 8,910,000.00 USD | 1,950.00 USD | 0.00 USD | `+97.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 8,990,000.00 USD | 78,870.00 USD | 0.00 USD | `+99.78%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.86` | 32,740,000.00 USD | 0.00 USD | 32,740,000.00 USD | 2,220.00 USD | 0.00 USD | 72,260.00 USD |
| `7D` | `3.87` | 32,670,000.00 USD | 0.00 USD | 32,670,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD |
| `7D` | `3.88` | 32,580,000.00 USD | 0.00 USD | 32,580,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,170.00 USD |
| `7D` | `3.89` | 32,370,000.00 USD | 0.00 USD | 32,370,000.00 USD | 1,210.00 USD | 50,710.00 USD | 2,140.00 USD |
| `7D` | `3.90` | 32,310,000.00 USD | 0.00 USD | 32,310,000.00 USD | 92,100.00 USD | 28,250.00 USD | 48,790.00 USD |
| `7D` | `3.91` | 32,140,000.00 USD | 0.00 USD | 32,140,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD |
| `7D` | `3.92` | 32,070,000.00 USD | 0.00 USD | 32,070,000.00 USD | 90,780.00 USD | 41,330.00 USD | 80,130.00 USD |
| `7D` | `3.93` | 31,860,000.00 USD | 0.00 USD | 31,860,000.00 USD | 51,660.00 USD | 26,290.00 USD | 50,310.00 USD |
| `1D` | `3.94` | 19,510,000.00 USD | 0.00 USD | 19,510,000.00 USD | 0.00 USD | 24,580.00 USD | 28,530.00 USD |
| `7D` | `3.94` | 31,730,000.00 USD | 0.00 USD | 31,730,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,850.00 USD |
| `1D` | `3.95` | 19,450,000.00 USD | 0.00 USD | 19,450,000.00 USD | 12,850.00 USD | 5,610.00 USD | 20.40 USD |
| `7D` | `3.95` | 31,490,000.00 USD | 0.00 USD | 31,490,000.00 USD | 8,490.00 USD | 26,060.00 USD | 365.10 USD |
| `1D` | `3.96` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 23,520.00 USD | 22,140.00 USD | 34,810.00 USD |
| `7D` | `3.96` | 31,460,000.00 USD | 0.00 USD | 31,460,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,120.00 USD |
| `1D` | `3.97` | 19,350,000.00 USD | 0.00 USD | 19,350,000.00 USD | 126,760.00 USD | 47,530.00 USD | 53,080.00 USD |
| `7D` | `3.97` | 31,240,000.00 USD | 0.00 USD | 31,240,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,580.00 USD |
| `1D` | `3.98` | 19,130,000.00 USD | 0.00 USD | 19,130,000.00 USD | 46,710.00 USD | 30,290.00 USD | 10,120.00 USD |
| `7D` | `3.98` | 30,630,000.00 USD | 0.00 USD | 30,630,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,800.00 USD |
| `1D` | `3.99` | 19,040,000.00 USD | 0.00 USD | 19,040,000.00 USD | 93,820.00 USD | 12,310.00 USD | 34,750.00 USD |
| `7D` | `3.99` | 30,430,000.00 USD | 0.00 USD | 30,430,000.00 USD | 63,200.00 USD | 82,870.00 USD | 101,750.00 USD |
| `1D` | `4.00` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 35,430.00 USD | 7,330.00 USD | 19,170.00 USD |
| `7D` | `4.00` | 30,180,000.00 USD | 0.00 USD | 30,180,000.00 USD | 317,210.00 USD | 105,220.00 USD | 166,340.00 USD |
| `1D` | `4.01` | 18,840,000.00 USD | 0.00 USD | 18,840,000.00 USD | 109,160.00 USD | 56,050.00 USD | 73,690.00 USD |
| `7D` | `4.01` | 29,590,000.00 USD | 0.00 USD | 29,590,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,160.00 USD |
| `1D` | `4.02` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 60,540.00 USD | 20,960.00 USD | 75,420.00 USD |
| `7D` | `4.02` | 28,680,000.00 USD | 0.00 USD | 28,680,000.00 USD | 279,800.00 USD | 88,330.00 USD | 195,130.00 USD |
| `1D` | `4.03` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 23,550.00 USD | 40,450.00 USD | 34,680.00 USD |
| `7D` | `4.03` | 28,110,000.00 USD | 0.00 USD | 28,110,000.00 USD | 250,870.00 USD | 45,290.00 USD | 150,400.00 USD |
| `1D` | `4.04` | 18,340,000.00 USD | 0.00 USD | 18,340,000.00 USD | 28,720.00 USD | 32,610.00 USD | 127,520.00 USD |
| `7D` | `4.04` | 27,670,000.00 USD | 0.00 USD | 27,670,000.00 USD | 98,660.00 USD | 65,670.00 USD | 120,810.00 USD |
| `1D` | `4.05` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,170.00 USD |
| `7D` | `4.05` | 27,380,000.00 USD | 0.00 USD | 27,380,000.00 USD | 184,470.00 USD | 72,110.00 USD | 86,110.00 USD |
| `1D` | `4.06` | 18,050,000.00 USD | 0.00 USD | 18,050,000.00 USD | 56,470.00 USD | 0.00 USD | 22,940.00 USD |
| `7D` | `4.06` | 27,040,000.00 USD | 0.00 USD | 27,040,000.00 USD | 198,550.00 USD | 45,470.00 USD | 125,060.00 USD |
| `1D` | `4.07` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 3,220.00 USD | 15,020.00 USD | 22,820.00 USD |
| `7D` | `4.07` | 26,670,000.00 USD | 0.00 USD | 26,670,000.00 USD | 183,890.00 USD | 35,750.00 USD | 41,400.00 USD |
| `1D` | `4.08` | 17,930,000.00 USD | 0.00 USD | 17,930,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,720.00 USD |
| `7D` | `4.08` | 26,410,000.00 USD | 0.00 USD | 26,410,000.00 USD | 9,180.00 USD | 63,440.00 USD | 231,470.00 USD |
| `1D` | `4.09` | 17,890,000.00 USD | 0.00 USD | 17,890,000.00 USD | 10,180.00 USD | 6,980.00 USD | 1,330.00 USD |
| `7D` | `4.09` | 26,110,000.00 USD | 0.00 USD | 26,110,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,000.00 USD |
| `1D` | `4.10` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,230.00 USD |
| `7D` | `4.10` | 25,900,000.00 USD | 0.00 USD | 25,900,000.00 USD | 158,760.00 USD | 118,310.00 USD | 347,600.00 USD |
| `1D` | `4.11` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 22,520.00 USD | 18,800.00 USD | 13,600.00 USD |
| `7D` | `4.11` | 25,280,000.00 USD | 0.00 USD | 25,280,000.00 USD | 110,780.00 USD | 0.00 USD | 84,500.00 USD |
| `1D` | `4.12` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 4,070.00 USD | 41,500.00 USD | 134,770.00 USD |
| `7D` | `4.12` | 25,080,000.00 USD | 0.00 USD | 25,080,000.00 USD | 97,300.00 USD | 48,940.00 USD | 342,940.00 USD |
| `1D` | `4.13` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 39,380.00 USD | 55,060.00 USD | 23,530.00 USD |
| `7D` | `4.13` | 24,590,000.00 USD | 0.00 USD | 24,590,000.00 USD | 293,300.00 USD | 79,100.00 USD | 107,270.00 USD |
| `1D` | `4.14` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 194,940.00 USD | 36,950.00 USD | 142,750.00 USD |
| `7D` | `4.14` | 24,120,000.00 USD | 0.00 USD | 24,120,000.00 USD | 374,290.00 USD | 57,440.00 USD | 219,190.00 USD |
| `1D` | `4.15` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 201,620.00 USD | 84,150.00 USD | 79,370.00 USD |
| `7D` | `4.15` | 23,460,000.00 USD | 0.00 USD | 23,460,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,790.00 USD |
| `1D` | `4.16` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 62,770.00 USD | 99,580.00 USD | 99,850.00 USD |
| `7D` | `4.16` | 22,810,000.00 USD | 0.00 USD | 22,810,000.00 USD | 310,530.00 USD | 192,570.00 USD | 175,040.00 USD |
| `1D` | `4.17` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 44,430.00 USD | 104,170.00 USD | 89,350.00 USD |
| `7D` | `4.17` | 22,140,000.00 USD | 0.00 USD | 22,140,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,090.00 USD |
| `1D` | `4.18` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 120,410.00 USD | 30,730.00 USD | 53,690.00 USD |
| `7D` | `4.18` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 360,840.00 USD | 103,320.00 USD | 57,070.00 USD |
| `1D` | `4.19` | 15,980,000.00 USD | 0.00 USD | 15,980,000.00 USD | 288,170.00 USD | 79,350.00 USD | 145,290.00 USD |
| `7D` | `4.19` | 20,930,000.00 USD | 0.00 USD | 20,930,000.00 USD | 215,210.00 USD | 113,960.00 USD | 672,780.00 USD |
| `1D` | `4.20` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 63,550.00 USD | 162,810.00 USD | 466,350.00 USD |
| `7D` | `4.20` | 19,930,000.00 USD | 0.00 USD | 19,930,000.00 USD | 337,660.00 USD | 122,960.00 USD | 883,770.00 USD |
| `1D` | `4.21` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 51,570.00 USD | 118,560.00 USD | 1,040.00 USD |
| `7D` | `4.21` | 18,580,000.00 USD | 0.00 USD | 18,580,000.00 USD | 321,000.00 USD | 149,940.00 USD | 119,310.00 USD |
| `1D` | `4.22` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 528,380.00 USD | 123,170.00 USD | 389,430.00 USD |
| `7D` | `4.22` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 853,600.00 USD | 161,970.00 USD | 786,440.00 USD |
| `1D` | `4.23` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 818,350.00 USD | 345,510.00 USD | 375,300.00 USD |
| `7D` | `4.23` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 740,840.00 USD |
| `1D` | `4.24` | 12,020,000.00 USD | 0.00 USD | 12,020,000.00 USD | 281,780.00 USD | 220,350.00 USD | 284,640.00 USD |
| `7D` | `4.24` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,800.00 USD |
| `1D` | `4.25` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 426,030.00 USD | 239,130.00 USD | 413,040.00 USD |
| `7D` | `4.25` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 350,470.00 USD | 433,770.00 USD | 653,480.00 USD |
| `1D` | `4.26` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 425,040.00 USD | 114,720.00 USD | 281,340.00 USD |
| `7D` | `4.26` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 357,510.00 USD |
| `1D` | `4.27` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 626,730.00 USD | 199,830.00 USD | 464,240.00 USD |
| `7D` | `4.27` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD |
| `1D` | `4.28` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 320,200.00 USD | 294,950.00 USD | 214,670.00 USD |
| `7D` | `4.28` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 842,270.00 USD | 497,680.00 USD | 1,110,000.00 USD |
| `1D` | `4.29` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 289,680.00 USD | 37,190.00 USD | 247,450.00 USD |
| `7D` | `4.29` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 9,100.00 USD | 46,530.00 USD | 1,260.00 USD |
| `1D` | `4.30` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 293,470.00 USD | 160,930.00 USD | 56,630.00 USD |
| `7D` | `4.30` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 3,500.00 USD | 90,090.00 USD | 79,470.00 USD |
| `1D` | `4.31` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 300,730.00 USD | 186,670.00 USD | 465,080.00 USD |
| `7D` | `4.31` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 88,750.00 USD | 0.00 USD | 46,130.00 USD |
| `1D` | `4.32` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 513,790.00 USD | 132,350.00 USD | 193,170.00 USD |
| `7D` | `4.32` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 169,820.00 USD | 158,570.00 USD | 78,540.00 USD |
| `1D` | `4.33` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 373,930.00 USD | 85,110.00 USD | 203,110.00 USD |
| `7D` | `4.33` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 112,660.00 USD | 89,000.00 USD |
| `1D` | `4.34` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 269,670.00 USD | 123,090.00 USD | 342,720.00 USD |
| `7D` | `4.34` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 75,930.00 USD | 161,050.00 USD | 137,740.00 USD |
| `1D` | `4.35` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 298,330.00 USD | 83,060.00 USD | 143,730.00 USD |
| `7D` | `4.35` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 362,610.00 USD | 39,140.00 USD | 89,710.00 USD |
| `1D` | `4.36` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 82,150.00 USD | 51,640.00 USD | 118,020.00 USD |
| `7D` | `4.36` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 5,210.00 USD | 0.00 USD | 88,860.00 USD |
| `1D` | `4.37` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 52,120.00 USD | 66,510.00 USD | 82,550.00 USD |
| `7D` | `4.37` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 538.42 USD |
| `1D` | `4.38` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 171,480.00 USD | 81,750.00 USD | 476,670.00 USD |
| `7D` | `4.38` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 141,930.00 USD | 263,590.00 USD |
| `1D` | `4.39` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 206,130.00 USD | 288,340.00 USD | 199,830.00 USD |
| `7D` | `4.39` | 888,950.00 USD | 0.00 USD | 888,950.00 USD | 0.00 USD | 62,850.00 USD | 153,790.00 USD |
| `1D` | `4.40` | 534,480.00 USD | 0.00 USD | 534,480.00 USD | 0.00 USD | 0.00 USD | 462,230.00 USD |
| `7D` | `4.40` | 672,310.00 USD | 0.00 USD | 672,310.00 USD | 0.00 USD | 0.00 USD | 401,830.00 USD |
| `1D` | `4.41` | 72,250.00 USD | 0.00 USD | 72,250.00 USD | 1,720.00 USD | 0.00 USD | 70,450.00 USD |
| `7D` | `4.41` | 270,480.00 USD | 0.00 USD | 270,480.00 USD | 0.00 USD | 0.00 USD | 270,480.00 USD |
| `1D` | `4.42` | 74.42 USD | 0.00 USD | 74.42 USD | 0.00 USD | 0.00 USD | 74.42 USD |
| `7D` | `4.42` | 182,060.00 USD | 182,060.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 175,990.00 USD |
| `7D` | `4.42` | 364,110.00 USD | 364,110.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 103,300.00 USD | 103,300.00 USD | 0.00 USD | 0.00 USD | 103,300.00 USD | 0.00 USD |
| `1D` | `4.43` | 206,600.00 USD | 206,600.00 USD | 0.00 USD | 0.00 USD | 103,300.00 USD | 0.00 USD |
| `7D` | `4.43` | 481,480.00 USD | 481,480.00 USD | 0.00 USD | 0.00 USD | 46,230.00 USD | 71,140.00 USD |
| `1D` | `4.44` | 729,840.00 USD | 729,840.00 USD | 0.00 USD | 0.00 USD | 282,030.00 USD | 241,210.00 USD |
| `7D` | `4.44` | 669,950.00 USD | 669,950.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 72,070.00 USD |
| `1D` | `4.45` | 764,740.00 USD | 764,740.00 USD | 0.00 USD | 0.00 USD | 34,890.00 USD | 6.04 USD |
| `7D` | `4.46` | 732,060.00 USD | 732,060.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD |
| `7D` | `4.47` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 132,630.00 USD | 135,940.00 USD | 0.00 USD |
| `1D` | `4.49` | 976,660.00 USD | 976,660.00 USD | 0.00 USD | 49,360.00 USD | 77,810.00 USD | 84,760.00 USD |
| `7D` | `4.49` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 211,380.00 USD | 41,210.00 USD | 0.00 USD |
| `7D` | `4.50` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 169,820.00 USD | 164,910.00 USD | 0.00 USD |
| `1D` | `4.51` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 162,900.00 USD | 282,880.00 USD | 248,730.00 USD |
| `1D` | `4.52` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 189,070.00 USD | 44,490.00 USD | 118,200.00 USD |
| `7D` | `4.52` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 487,010.00 USD | 0.00 USD | 278,620.00 USD |
| `7D` | `4.53` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD |
| `1D` | `4.54` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 150,600.00 USD | 702,170.00 USD |
| `7D` | `4.54` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 315,060.00 USD |
| `1D` | `4.56` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 79,110.00 USD | 24,450.00 USD | 288,390.00 USD |
| `7D` | `4.56` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 135,640.00 USD | 42,070.00 USD | 67,290.00 USD |
| `7D` | `4.57` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 198,050.00 USD | 0.00 USD | 151,220.00 USD |
| `1D` | `4.58` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 380,450.00 USD | 25,260.00 USD | 823,160.00 USD |
| `7D` | `4.58` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,610.00 USD |
| `1D` | `4.59` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 752,530.00 USD | 63,210.00 USD | 332.40 USD |
| `7D` | `4.59` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 759,320.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 53,970.00 USD | 84,420.00 USD | 49,590.00 USD |
| `7D` | `4.60` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 0.00 USD |
| `1D` | `4.61` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 66,620.00 USD | 0.00 USD | 26,740.00 USD |
| `7D` | `4.61` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `4.62` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 46.88 USD |
| `7D` | `4.62` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 336.39 USD |
| `1D` | `4.63` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 500.90 USD | 0.00 USD | 103.94 USD |
| `7D` | `4.63` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 272.08 USD |
| `1D` | `4.64` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 332,240.00 USD | 11,270.00 USD | 61,770.00 USD |
| `7D` | `4.64` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 500,990.00 USD | 0.00 USD | 429.40 USD |
| `1D` | `4.65` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 370,110.00 USD | 52,020.00 USD | 587,290.00 USD |
| `7D` | `4.65` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 601.71 USD |
| `1D` | `4.66` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 281,290.00 USD | 304,540.00 USD | 379,740.00 USD |
| `7D` | `4.66` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 144,860.00 USD | 0.00 USD | 153,720.00 USD |
| `1D` | `4.67` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 184,090.00 USD | 0.00 USD | 377,700.00 USD |
| `7D` | `4.67` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,130.00 USD |
| `1D` | `4.68` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 345,490.00 USD | 62,440.00 USD | 175,520.00 USD |
| `7D` | `4.68` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 452,220.00 USD |
| `1D` | `4.69` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 237,530.00 USD |
| `7D` | `4.69` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 89,020.00 USD |
| `1D` | `4.70` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD |
| `7D` | `4.70` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 365,040.00 USD | 278,020.00 USD | 316,400.00 USD |
| `7D` | `4.71` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 456.30 USD |
| `1D` | `4.72` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 4,880.00 USD | 187,480.00 USD | 103,690.00 USD |
| `7D` | `4.72` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,100.00 USD |
| `1D` | `4.73` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 61,330.00 USD | 37,010.00 USD | 61,550.00 USD |
| `7D` | `4.73` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 59,270.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4.74` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 242,820.00 USD | 172,000.00 USD | 294,670.00 USD |
| `7D` | `4.74` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 130,300.00 USD |
| `1D` | `4.75` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 202,480.00 USD | 188,800.00 USD | 270,190.00 USD |
| `7D` | `4.75` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 342,090.00 USD |
| `1D` | `4.76` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 35,470.00 USD | 78,750.00 USD | 247,600.00 USD |
| `7D` | `4.76` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 946,180.00 USD | 46,890.00 USD | 274,820.00 USD |
| `1D` | `4.77` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 113,030.00 USD | 177,160.00 USD | 105,150.00 USD |
| `7D` | `4.77` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 103,170.00 USD |
| `1D` | `4.78` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 40,580.00 USD | 20,000.00 USD | 114,020.00 USD |
| `7D` | `4.78` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 683,730.00 USD | 584,230.00 USD | 152,900.00 USD |
| `1D` | `4.79` | 15,950,000.00 USD | 15,950,000.00 USD | 0.00 USD | 294,950.00 USD | 125,610.00 USD | 133,020.00 USD |
| `7D` | `4.79` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 70,610.00 USD |
| `1D` | `4.80` | 16,800,000.00 USD | 16,800,000.00 USD | 0.00 USD | 355,770.00 USD | 315,950.00 USD | 174,270.00 USD |
| `7D` | `4.80` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,690.00 USD |
| `1D` | `4.81` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 405,810.00 USD | 120,180.00 USD | 127,770.00 USD |
| `7D` | `4.81` | 17,950,000.00 USD | 17,950,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 103,470.00 USD |
| `1D` | `4.82` | 18,350,000.00 USD | 18,350,000.00 USD | 0.00 USD | 274,470.00 USD | 214,840.00 USD | 407,480.00 USD |
| `7D` | `4.82` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 212,270.00 USD | 70,050.00 USD | 290,360.00 USD |
| `7D` | `4.83` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 740,870.00 USD |
| `1D` | `4.84` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 73,450.00 USD | 82,100.00 USD | 77,670.00 USD |
| `7D` | `4.84` | 22,850,000.00 USD | 22,850,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,500.00 USD |
| `1D` | `4.85` | 19,730,000.00 USD | 19,730,000.00 USD | 0.00 USD | 213,580.00 USD | 148,110.00 USD | 210,850.00 USD |
| `7D` | `4.85` | 24,870,000.00 USD | 24,870,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,170,000.00 USD |
| `1D` | `4.86` | 20,170,000.00 USD | 20,170,000.00 USD | 0.00 USD | 94,700.00 USD | 69,470.00 USD | 278,380.00 USD |
| `7D` | `4.86` | 26,280,000.00 USD | 26,280,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 801,880.00 USD |
| `1D` | `4.87` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 181,750.00 USD | 113,470.00 USD | 46,730.00 USD |
| `7D` | `4.87` | 27,350,000.00 USD | 27,350,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 661,850.00 USD |
| `1D` | `4.88` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 36,680.00 USD | 7,330.00 USD | 194,050.00 USD |
| `7D` | `4.88` | 29,070,000.00 USD | 29,070,000.00 USD | 0.00 USD | 449,970.00 USD | 480,980.00 USD | 793,400.00 USD |
| `1D` | `4.89` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 113,710.00 USD | 46,470.00 USD | 77,150.00 USD |
| `7D` | `4.89` | 29,660,000.00 USD | 29,660,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 273,230.00 USD |
| `1D` | `4.90` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 81,280.00 USD | 112,960.00 USD | 404,660.00 USD |
| `7D` | `4.90` | 30,800,000.00 USD | 30,800,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 542,250.00 USD |
| `1D` | `4.91` | 22,110,000.00 USD | 22,110,000.00 USD | 0.00 USD | 290,660.00 USD | 85,510.00 USD | 150,790.00 USD |
| `7D` | `4.91` | 32,230,000.00 USD | 32,230,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 589,200.00 USD |
| `1D` | `4.92` | 22,650,000.00 USD | 22,650,000.00 USD | 0.00 USD | 186,460.00 USD | 89,190.00 USD | 257,240.00 USD |
| `7D` | `4.92` | 33,960,000.00 USD | 33,960,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 878,000.00 USD |
| `1D` | `4.93` | 23,000,000.00 USD | 23,000,000.00 USD | 0.00 USD | 117,390.00 USD | 72,670.00 USD | 164,600.00 USD |
| `7D` | `4.93` | 35,520,000.00 USD | 35,520,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,840.00 USD |
| `1D` | `4.94` | 23,290,000.00 USD | 23,290,000.00 USD | 0.00 USD | 50,810.00 USD | 65,310.00 USD | 171,160.00 USD |
| `7D` | `4.94` | 36,820,000.00 USD | 36,820,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 659,000.00 USD |
| `1D` | `4.95` | 23,450,000.00 USD | 23,450,000.00 USD | 0.00 USD | 105,320.00 USD | 12,690.00 USD | 46,630.00 USD |
| `7D` | `4.95` | 38,120,000.00 USD | 38,120,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 669,460.00 USD |
| `1D` | `4.96` | 23,590,000.00 USD | 23,590,000.00 USD | 0.00 USD | 94,690.00 USD | 21,750.00 USD | 23,100.00 USD |
| `7D` | `4.96` | 39,360,000.00 USD | 39,360,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 411,520.00 USD |
| `1D` | `4.97` | 23,710,000.00 USD | 23,710,000.00 USD | 0.00 USD | 6,540.00 USD | 15,020.00 USD | 100,580.00 USD |
| `7D` | `4.97` | 39,740,000.00 USD | 39,740,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 112,110.00 USD |
| `1D` | `4.98` | 23,750,000.00 USD | 23,750,000.00 USD | 0.00 USD | 3,880.00 USD | 18,060.00 USD | 15,770.00 USD |
| `7D` | `4.98` | 40,300,000.00 USD | 40,300,000.00 USD | 0.00 USD | 197,950.00 USD | 88,580.00 USD | 273,860.00 USD |
| `1D` | `4.99` | 23,840,000.00 USD | 23,840,000.00 USD | 0.00 USD | 1,730.00 USD | 6,980.00 USD | 82,020.00 USD |
| `7D` | `4.99` | 40,650,000.00 USD | 40,650,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 118,190.00 USD |
| `1D` | `5.00` | 23,840,000.00 USD | 23,840,000.00 USD | 0.00 USD | 718.70 USD | 0.00 USD | 6.68 USD |
| `7D` | `5.00` | 41,360,000.00 USD | 41,360,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,140.00 USD |
| `1D` | `5.01` | 23,870,000.00 USD | 23,870,000.00 USD | 0.00 USD | 14,980.00 USD | 10,080.00 USD | 40.98 USD |
| `7D` | `5.01` | 43,560,000.00 USD | 43,560,000.00 USD | 0.00 USD | 781,840.00 USD | 340,150.00 USD | 1,090,000.00 USD |
| `1D` | `5.02` | 23,940,000.00 USD | 23,940,000.00 USD | 0.00 USD | 13,280.00 USD | 0.00 USD | 59,040.00 USD |
| `7D` | `5.02` | 45,050,000.00 USD | 45,050,000.00 USD | 0.00 USD | 821,860.00 USD | 337,720.00 USD | 321,090.00 USD |
| `1D` | `5.03` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 15,180.00 USD | 18,800.00 USD | 12,390.00 USD |
| `7D` | `5.03` | 46,730,000.00 USD | 46,730,000.00 USD | 0.00 USD | 564,790.00 USD | 231,540.00 USD | 886,030.00 USD |
| `1D` | `5.04` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 2,770.00 USD | 0.00 USD | 78.05 USD |
| `7D` | `5.04` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 305,260.00 USD | 253,720.00 USD | 880,400.00 USD |
| `1D` | `5.05` | 24,060,000.00 USD | 24,060,000.00 USD | 0.00 USD | 34,080.00 USD | 14,380.00 USD | 23,030.00 USD |
| `7D` | `5.05` | 50,170,000.00 USD | 50,170,000.00 USD | 0.00 USD | 901,830.00 USD | 367,860.00 USD | 734,250.00 USD |
| `1D` | `5.06` | 24,090,000.00 USD | 24,090,000.00 USD | 0.00 USD | 1,440.00 USD | 8,000.00 USD | 23,290.00 USD |
| `7D` | `5.06` | 50,880,000.00 USD | 50,880,000.00 USD | 0.00 USD | 92,480.00 USD | 193,330.00 USD | 421,120.00 USD |
| `1D` | `5.07` | 24,090,000.00 USD | 24,090,000.00 USD | 0.00 USD | 332.61 USD | 0.00 USD | 0.00 USD |
| `7D` | `5.07` | 52,080,000.00 USD | 52,080,000.00 USD | 0.00 USD | 358,750.00 USD | 166,480.00 USD | 673,530.00 USD |
| `1D` | `5.08` | 24,250,000.00 USD | 24,250,000.00 USD | 0.00 USD | 61,310.00 USD | 46,580.00 USD | 48,710.00 USD |
| `7D` | `5.08` | 52,740,000.00 USD | 52,740,000.00 USD | 0.00 USD | 204,140.00 USD | 308,520.00 USD | 148,800.00 USD |
| `7D` | `5.09` | 53,600,000.00 USD | 53,600,000.00 USD | 0.00 USD | 105,390.00 USD | 121,050.00 USD | 632,200.00 USD |
| `7D` | `5.10` | 54,170,000.00 USD | 54,170,000.00 USD | 0.00 USD | 291,110.00 USD | 78,890.00 USD | 202,220.00 USD |
| `7D` | `5.11` | 54,950,000.00 USD | 54,950,000.00 USD | 0.00 USD | 369,260.00 USD | 120,290.00 USD | 291,630.00 USD |
| `7D` | `5.12` | 55,540,000.00 USD | 55,540,000.00 USD | 0.00 USD | 303,840.00 USD | 166,880.00 USD | 116,230.00 USD |
| `7D` | `5.13` | 56,380,000.00 USD | 56,380,000.00 USD | 0.00 USD | 262,920.00 USD | 100,640.00 USD | 483,720.00 USD |
| `7D` | `5.14` | 57,000,000.00 USD | 57,000,000.00 USD | 0.00 USD | 140,950.00 USD | 104,910.00 USD | 369,880.00 USD |
| `7D` | `5.15` | 57,830,000.00 USD | 57,830,000.00 USD | 0.00 USD | 309,440.00 USD | 132,710.00 USD | 391,460.00 USD |
| `7D` | `5.16` | 58,360,000.00 USD | 58,360,000.00 USD | 0.00 USD | 54,280.00 USD | 126,880.00 USD | 348,110.00 USD |
| `7D` | `5.17` | 59,060,000.00 USD | 59,060,000.00 USD | 0.00 USD | 282,930.00 USD | 99,740.00 USD | 309,340.00 USD |
| `7D` | `5.18` | 59,380,000.00 USD | 59,380,000.00 USD | 0.00 USD | 67,600.00 USD | 133,610.00 USD | 124,620.00 USD |
| `7D` | `5.19` | 59,760,000.00 USD | 59,760,000.00 USD | 0.00 USD | 72,580.00 USD | 47,800.00 USD | 263,610.00 USD |
| `7D` | `5.20` | 60,050,000.00 USD | 60,050,000.00 USD | 0.00 USD | 140,770.00 USD | 80,310.00 USD | 65,030.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.26B` | Total OI Tokens: `282,765,780.2 NEAR`
  * 1h OI Change: `-0.61%` | 4h OI Change: `-3.06%` | 24h OI Change: `-5.88%`
  * Exchange Breakdown: Binance=`243.11M` | Bybit=`169.70M` | OKX=`52.88M` | Hyperliquid=`256.19M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `46.03K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `50.92%` | `49.08%` | `1.04` | 3,520,000.00 USD |
| `15M` | `Binance` | `60.83%` | `39.17%` | `1.55` | 921,060.00 USD |
| `15M` | `OKX` | `65.96%` | `34.04%` | `1.94` | 242,840.00 USD |
| `15M` | `Bybit` | `66.22%` | `33.78%` | `1.96` | 114,860.00 USD |
| `15M` | `KuCoin` | `43.88%` | `56.12%` | `0.78` | 8,870.00 USD |
| `15M` | `Gate` | `44.01%` | `55.99%` | `0.79` | 27,790.00 USD |
| `15M` | `Bitget` | `36.25%` | `63.75%` | `0.57` | 48,230.00 USD |
| `15M` | `BingX` | `49.22%` | `50.78%` | `0.97` | 918,930.00 USD |
| `15M` | `MEXC` | `55.07%` | `44.93%` | `1.23` | 389,210.00 USD |
| `15M` | `Bitunix` | `55.45%` | `44.55%` | `1.24` | 66,440.00 USD |
| `15M` | `Hyperliquid` | `33.81%` | `66.19%` | `0.51` | 7,330.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.26%` | `44.74%` | `1.24` | 452,920.00 USD |
| `15M` | `Crypto.com` | `98.56%` | `1.44%` | `68.44` | 1,780.00 USD |
| `15M` | `WhiteBIT` | `0.1%` | `99.9%` | `0.00` | 285,850.00 USD |
| `15M` | `HTX` | `51.11%` | `48.89%` | `1.05` | 828.66 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `25.19%` | `74.81%` | `0.34` | 3,740.00 USD |
| `15M` | `Aster` | `0.14%` | `99.86%` | `0.00` | 24,650.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `67.23%` | `32.77%` | `2.05` | 891.14 USD |
| `15M` | `Whale Positions` | `60.83%` | `39.17%` | `1.55` | 921,060.00 USD |
| `15M` | `Global Accounts` | `50.92%` | `49.08%` | `1.04` | 3,520,000.00 USD |
| `1H` | `NEAR` | `45.51%` | `54.49%` | `0.84` | 14,520,000.00 USD |
| `1H` | `Binance` | `50.45%` | `49.55%` | `1.02` | 4,200,000.00 USD |
| `1H` | `OKX` | `60.8%` | `39.2%` | `1.55` | 924,820.00 USD |
| `1H` | `Bybit` | `47.84%` | `52.16%` | `0.92` | 696,030.00 USD |
| `1H` | `KuCoin` | `44.26%` | `55.74%` | `0.79` | 206,880.00 USD |
| `1H` | `Gate` | `45.04%` | `54.96%` | `0.82` | 183,350.00 USD |
| `1H` | `Bitget` | `43.36%` | `56.64%` | `0.77` | 149,670.00 USD |
| `1H` | `BingX` | `46.39%` | `53.61%` | `0.87` | 3,420,000.00 USD |
| `1H` | `MEXC` | `49.43%` | `50.57%` | `0.98` | 939,850.00 USD |
| `1H` | `Bitunix` | `44.73%` | `55.27%` | `0.81` | 394,110.00 USD |
| `1H` | `Hyperliquid` | `15.41%` | `84.59%` | `0.18` | 101,630.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.31%` | `46.69%` | `1.14` | 2,030,000.00 USD |
| `1H` | `Crypto.com` | `78.96%` | `21.04%` | `3.75` | 3,000.00 USD |
| `1H` | `WhiteBIT` | `0.02%` | `99.98%` | `0.00` | 1,200,000.00 USD |
| `1H` | `HTX` | `46.89%` | `53.11%` | `0.88` | 3,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.88%` | `47.12%` | `1.12` | 36,660.00 USD |
| `1H` | `Aster` | `0.88%` | `99.12%` | `0.01` | 25,210.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `64.51%` | `35.49%` | `1.82` | 9,390.00 USD |
| `1H` | `Whale Positions` | `50.45%` | `49.55%` | `1.02` | 4,200,000.00 USD |
| `1H` | `Global Accounts` | `45.51%` | `54.49%` | `0.84` | 14,520,000.00 USD |
| `4H` | `NEAR` | `46.93%` | `53.07%` | `0.88` | 145,390,000.00 USD |
| `4H` | `Binance` | `47.41%` | `52.59%` | `0.90` | 53,490,000.00 USD |
| `4H` | `OKX` | `42.63%` | `57.37%` | `0.74` | 21,420,000.00 USD |
| `4H` | `Bybit` | `45.68%` | `54.32%` | `0.84` | 18,410,000.00 USD |
| `4H` | `KuCoin` | `52.54%` | `47.46%` | `1.11` | 2,250,000.00 USD |
| `4H` | `Gate` | `52.11%` | `47.89%` | `1.09` | 4,100,000.00 USD |
| `4H` | `Bitget` | `49.18%` | `50.82%` | `0.97` | 6,790,000.00 USD |
| `4H` | `BingX` | `45.55%` | `54.45%` | `0.84` | 5,770,000.00 USD |
| `4H` | `MEXC` | `44.4%` | `55.6%` | `0.80` | 15,530,000.00 USD |
| `4H` | `Bitunix` | `52.91%` | `47.09%` | `1.12` | 5,220,000.00 USD |
| `4H` | `Hyperliquid` | `46.06%` | `53.94%` | `0.85` | 4,230,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 1,030,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `63.47%` | `36.53%` | `1.74` | 4,820,000.00 USD |
| `4H` | `HTX` | `46.96%` | `53.04%` | `0.89` | 185,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `36.89%` | `63.11%` | `0.58` | 1,610,000.00 USD |
| `4H` | `Aster` | `32.59%` | `67.41%` | `0.48` | 337,770.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.09%` | `56.91%` | `0.76` | 201,660.00 USD |
| `4H` | `Whale Positions` | `47.41%` | `52.59%` | `0.90` | 53,490,000.00 USD |
| `4H` | `Global Accounts` | `46.93%` | `53.07%` | `0.88` | 145,390,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4.60` | `4.61` | `4.60` | `4.63` | `4.59` | 10,770,688.98 USD | 5,544,543.35 USD | 5,226,145.63 USD | 318,397.72 USD | `+2.96%` | `2B / 4S` |
| `5:00 UTC` | `4.58` | `4.59` | `4.58` | `4.61` | `4.58` | 6,667,677.12 USD | 2,970,627.70 USD | 3,697,049.42 USD | -726,421.72 USD | `-10.89%` | `2B / 5S` |
| `0:00 UTC` | `4.57` | `4.58` | `4.57` | `4.60` | `4.56` | 7,120,500.63 USD | 2,702,175.30 USD | 4,418,325.32 USD | -1,716,150.02 USD | `-24.10%` | `2B / 10S` |
| `5:00 UTC` | `4.57` | `4.56` | `4.57` | `4.58` | `4.55` | 4,633,928.94 USD | 2,745,228.28 USD | 1,888,700.65 USD | 856,527.63 USD | `+18.48%` | `5B / 1S` |
| `0:00 UTC` | `4.56` | `4.53` | `4.56` | `4.58` | `4.48` | 11,435,880.79 USD | 4,658,038.22 USD | 6,777,842.57 USD | -2,119,804.34 USD | `-18.54%` | `11B / 24S` |
| `5:00 UTC` | `4.48` | `4.48` | `4.48` | `4.50` | `4.45` | 11,953,334.30 USD | 7,100,618.87 USD | 4,852,715.43 USD | 2,247,903.44 USD | `+18.81%` | `10B / 5S` |
| `0:00 UTC` | `4.50` | `4.49` | `4.50` | `4.51` | `4.48` | 5,580,209.64 USD | 2,611,428.00 USD | 2,968,781.64 USD | -357,353.64 USD | `-6.40%` | `4B / 2S` |
| `5:00 UTC` | `4.48` | `4.47` | `4.48` | `4.50` | `4.45` | 3,346,103.47 USD | 1,895,415.61 USD | 1,450,687.86 USD | 444,727.76 USD | `+13.29%` | `4B / 3S` |
| `0:00 UTC` | `4.43` | `4.43` | `4.43` | `4.46` | `4.40` | 9,612,896.64 USD | 4,376,656.36 USD | 5,236,240.29 USD | -859,583.93 USD | `-8.94%` | `5B / 19S` |
| `5:00 UTC` | `4.41` | `4.41` | `4.41` | `4.43` | `4.39` | 4,212,630.28 USD | 2,557,439.64 USD | 1,655,190.64 USD | 902,249.00 USD | `+21.42%` | `12B / 2S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:10` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.65` | 100,000.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4.64` | 0.00 USD | 0.00 USD |
| `10-28 20:33` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.63` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.57` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.54` | 0.00 USD | 0.00 USD |
| `10-28 19:51` | `Volume 2.0M NEAR` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.54` | 0.00 USD | 0.00 USD |
| `10-28 19:32` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.61` | 185,000.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 2.0M NEAR` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.65` | 419,000.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 2.0M NEAR` | `Trapped longs` | **`BEARISH`** | Failed breakout | `4.65` | 419,000.00 USD | 0.00 USD |
| `10-28 18:51` | `Volume 2.0M NEAR` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.59` | 469,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.61` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4.62` | 0.00 USD | 0.00 USD |
| `10-28 17:34` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.66` | 0.00 USD | 0.00 USD |
| `10-28 17:34` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.64` | 209,000.00 USD | 0.00 USD |
| `10-28 16:42` | `Volume 2.0M NEAR` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.65` | 0.00 USD | 0.00 USD |
| `10-28 14:29` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.72` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Volume 2.0M NEAR` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.76` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.75` | 145,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.02` | `Trapped longs` | **`BEARISH`** | Failed breakout | `4.75` | 145,000.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.71` | 84,000.00 USD | 0.00 USD |
| `10-28 06:42` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.65` | 0.00 USD | 0.00 USD |
| `10-28 06:42` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.63` | 166,000.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 2.0M NEAR` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.63` | 374,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.65` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 44,940.00 USD | 544,910.00 USD | **`ACCUMULATION`** |
| `15m` | -1,510,000.00 USD | 1,170,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,160,000.00 USD | -1,200,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,290,000.00 USD | 2,390,000.00 USD | **`ACCUMULATION`** |
| `2h` | -4,600,000.00 USD | -6,600,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,550,000.00 USD | -10,670,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,140,000.00 USD | -10,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,980,000.00 USD | -11,150,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 531,520.00 USD | -12,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -15,050,000.00 USD | -62,230,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -70,130,000.00 USD | -95,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -236,400,000.00 USD | -665,010,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+44.94K` | 15m=`-1.51M` | 1h=`-2.29M` | 24h=`-15.05M`
* Futures Capital Netflows: 5m=`+544.91K` | 15m=`+1.17M` | 1h=`+2.39M` | 24h=`-62.23M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.38` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.28` (Risk Distance: `0.1043` pts)
  * +2.5R Take Profit: `4.64`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.73` (Risk Distance: `0.1043` pts)
  * +2.5R Take Profit: `4.37`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
