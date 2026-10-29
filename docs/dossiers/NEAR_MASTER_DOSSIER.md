# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:59:36 IST` (`2026-10-29 19:29:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.40` | **Live Ask Quote**: `4.42` | **Mid Price**: `4.41`
- **Spread Points**: `28.00` | **Spread BPS**: `63.48 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.47` | VWAP Z-Score: `-0.94` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0508` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.67` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.76` | Lower -3.00σ Band: `4.18`
  * Upper +2.51σ Band: `4.71` | Lower -2.51σ Band: `4.23`
  * Upper +2.01σ Band: `4.66` | Lower -2.01σ Band: `4.27`
  * Upper +2.00σ Band: `4.66` | Lower -2.00σ Band: `4.27`
  * Upper +1.28σ Band: `4.59` | Lower -1.28σ Band: `4.34`
  * Upper +1.00σ Band: `4.57` | Lower -1.00σ Band: `4.37`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.45` | EMA-20=`4.48` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.47` (Slope: `+0.0000`) | EMA-100=`4.50`
  * Institutional Anchors: EMA-144=`4.51` | EMA-200=`4.52` (Slope: `-0.0633`) | EMA-233=`4.51`
- **Range Boundaries**: 24H High=`4.80` | 24H Low=`4.27` | Weekly High=`4.80` | Weekly Low=`4.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.62` (Distance: `-4.57%`)
  * Point of Control (POC) = `4.41` (Distance: `+0.04%`)
  * Value Area Low (VAL) = `4.37` (Distance: `+0.85%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `4.39` - `4.43`
  * Optimal Trade Entry (OTE 0.705): `4.42`
  * Structural Invalidation Anchor (0.786): `4.45`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.39` | `4.40` | `4.39` | `4.39` | `240,076` | 1,054,732.09 USD | 148,657.12 USD | `+14.09%` | -30,967,127.70 USD | `+0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4.39` | `4.41` | `4.39` | `4.40` | `200,584` | 882,112.06 USD | 240,334.58 USD | `+27.25%` | -30,726,793.12 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.40` | `4.41` | `4.40` | `4.41` | `214,458` | 945,291.05 USD | 286,307.97 USD | `+30.29%` | -30,440,485.15 USD | `+0.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.41` | `4.45` | `4.39` | `4.42` | `1,753,559` | 7,755,029.11 USD | 208,352.82 USD | `+2.69%` | -29,960,660.38 USD | `+0.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `4.42` | `4.43` | `4.38` | `4.39` | `1,647,197` | 7,242,328.79 USD | -765,711.02 USD | `-10.57%` | -30,726,371.41 USD | `-0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.39` | `4.41` | `4.39` | `4.41` | `411,979` | 1,813,892.22 USD | 516,554.59 USD | `+28.48%` | -30,209,816.82 USD | `+0.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4.60` | `4.60` | `4.45` | `4.50` | `7,767,140` | 35,143,644.65 USD | -731,523.30 USD | `-2.08%` | -33,127,039.77 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.50` | `4.51` | `4.39` | `4.42` | `5,916,118` | 26,294,238.86 USD | -563,856.99 USD | `-2.14%` | -33,690,896.76 USD | `+0.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.42` | `4.43` | `4.38` | `4.41` | `2,062,193` | 9,069,528.99 USD | -239,271.38 USD | `-2.64%` | -33,930,168.14 USD | `+0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -32,636,174.80 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -28,227,147.70 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.41` | `25,896,135` | 117,449,178.44 USD | -5,703,020.44 USD | `-4.86%` | -33,930,168.14 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.73` | `4.73` | `4.40` | `4.42` | `25,745,501` | 116,497,184.49 USD | -11,801,514.25 USD | `-10.13%` | -15,870,340.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -31,542,465.78 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -32,636,174.80 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -28,227,147.70 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.41` | `25,896,135` | 117,449,178.44 USD | -5,703,020.44 USD | `-4.86%` | -33,930,168.14 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`4.41`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `58` | `0x7737...bf66` | `LONG` | 24,902,656.19 USD | `5,640,376.30` | `2.35` | `4.43` | `0.9337` | 11,630,753.36 USD | `+46.70%` | `10X Cross` |
| `128` | `0xb581...6f4f` | `LONG` | 15,944,400.00 USD | `3,600,000.00` | `5.19` | `4.43` | `0.000000` | -2,748,635.22 USD | `-17.24%` | `4X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,636,975.65 USD | `2,400,202.10` | `2.31` | `4.43` | `26.85` | -5,091,571.76 USD | `-47.87%` | `3X Cross` |
| `264` | `0x77ee...2902` | `LONG` | 9,140,017.54 USD | `2,063,023.10` | `1.93` | `4.43` | `0.3810` | 5,148,821.61 USD | `+56.33%` | `10X Cross` |
| `270` | `0xefe4...194b` | `SHORT` | 8,948,886.54 USD | `2,019,882.30` | `4.44` | `4.43` | `11.46` | 26,198.61 USD | `+0.29%` | `5X Cross` |
| `379` | `0xb83d...6e36` | `SHORT` | 6,406,447.72 USD | `1,445,759.10` | `5.19` | `4.43` | `91.45` | 1,103,001.22 USD | `+17.22%` | `3X Cross` |
| `402` | `0xb46b...538e` | `SHORT` | 5,914,472.00 USD | `1,336,000.00` | `4.33` | `4.43` | `7.22` | -129,607.94 USD | `-2.19%` | `10X Cross` |
| `422` | `0x9df2...c665` | `SHORT` | 5,605,468.00 USD | `1,265,000.00` | `2.03` | `4.43` | `26.75` | -3,038,785.66 USD | `-54.21%` | `10X Cross` |
| `431` | `0xb695...a92d` | `SHORT` | 5,460,363.18 USD | `1,233,422.90` | `4.57` | `4.43` | `26.30` | 180,373.74 USD | `+3.30%` | `10X Cross` |
| `465` | `0x60b0...991e` | `LONG` | 4,968,399.63 USD | `1,121,307.10` | `5.00` | `4.43` | `0.000000` | -633,024.80 USD | `-12.74%` | `10X Cross` |
| `484` | `0xcac1...26b3` | `SHORT` | 4,755,826.48 USD | `1,073,743.90` | `2.48` | `4.43` | `11.62` | -2,095,883.02 USD | `-44.07%` | `10X Cross` |
| `499` | `0x781e...96b7` | `SHORT` | 4,605,864.22 USD | `1,039,604.60` | `2.45` | `4.43` | `7.49` | -2,061,527.03 USD | `-44.76%` | `10X Cross` |
| `517` | `0xdf60...d3c7` | `LONG` | 4,419,900.00 USD | `1,000,000.00` | `4.70` | `4.43` | `3.91` | -279,377.29 USD | `-6.32%` | `8X Isolated` |
| `574` | `0x45d2...4029` | `SHORT` | 4,024,549.70 USD | `909,400.00` | `3.26` | `4.43` | `43.07` | -1,058,399.80 USD | `-26.30%` | `10X Cross` |
| `582` | `0x4cae...7c34` | `LONG` | 3,987,744.56 USD | `900,086.80` | `3.52` | `4.43` | `1.87` | 815,343.58 USD | `+20.45%` | `10X Cross` |
| `731` | `0x9aa5...58af` | `SHORT` | 3,207,001.36 USD | `723,977.10` | `4.78` | `4.43` | `14.70` | 252,631.83 USD | `+7.88%` | `10X Cross` |
| `813` | `0x005a...61fe` | `LONG` | 2,889,674.75 USD | `652,414.60` | `2.08` | `4.43` | `2.33` | 1,532,143.51 USD | `+53.02%` | `7X Cross` |
| `817` | `0xba5d...a352` | `SHORT` | 2,867,144.40 USD | `647,532.50` | `2.83` | `4.43` | `12.46` | -1,034,429.46 USD | `-36.08%` | `10X Cross` |
| `828` | `0xd1dd...9e85` | `SHORT` | 2,824,916.08 USD | `637,621.00` | `4.96` | `4.43` | `16.60` | 338,556.66 USD | `+11.98%` | `10X Cross` |
| `832` | `0x123d...3bff` | `SHORT` | 2,818,074.21 USD | `636,076.70` | `2.09` | `4.43` | `8.97` | -1,490,697.52 USD | `-52.90%` | `10X Cross` |
| `845` | `0xcf53...ee11` | `SHORT` | 2,750,883.72 USD | `621,598.40` | `5.07` | `4.43` | `24.15` | 401,286.53 USD | `+14.59%` | `10X Cross` |
| `944` | `0x5647...e7de` | `SHORT` | 2,418,398.08 USD | `545,864.50` | `4.69` | `4.43` | `12.56` | 140,193.37 USD | `+5.80%` | `10X Cross` |
| `968` | `0xbfc7...80b4` | `SHORT` | 2,351,799.00 USD | `531,000.00` | `2.01` | `4.43` | `12.71` | -1,286,599.61 USD | `-54.71%` | `10X Cross` |
| `987` | `0xfc66...ca06` | `SHORT` | 2,330,884.08 USD | `525,957.10` | `4.60` | `4.43` | `68.17` | 86,152.22 USD | `+3.70%` | `10X Cross` |
| `1065` | `0xef96...9383` | `SHORT` | 2,115,575.30 USD | `477,459.50` | `4.50` | `4.43` | `12.37` | 34,322.90 USD | `+1.62%` | `10X Cross` |
| `1104` | `0x7fda...17d1` | `SHORT` | 2,044,834.73 USD | `461,546.30` | `4.83` | `4.43` | `78.37` | 182,582.52 USD | `+8.93%` | `10X Cross` |
| `1289` | `0xe097...d0fe` | `LONG` | 1,770,200.00 USD | `400,000.00` | `5.29` | `4.43` | `0.000000` | -346,587.30 USD | `-19.58%` | `10X Cross` |
| `1425` | `0xdf95...7d72` | `SHORT` | 1,605,831.81 USD | `362,351.20` | `4.23` | `4.43` | `101.67` | -72,223.04 USD | `-4.50%` | `10X Cross` |
| `1430` | `0x6e8f...4364` | `LONG` | 1,600,126.39 USD | `361,210.50` | `3.28` | `4.43` | `3.29` | 416,066.17 USD | `+26.00%` | `10X Cross` |
| `1465` | `0xcf67...eb24` | `LONG` | 1,550,815.00 USD | `350,000.00` | `1.98` | `4.43` | `1.04` | 859,197.12 USD | `+55.40%` | `10X Cross` |
| `1561` | `0x590f...be1d` | `SHORT` | 1,427,999.98 USD | `322,675.40` | `4.53` | `4.43` | `4.84` | 35,034.33 USD | `+2.45%` | `10X Cross` |
| `1568` | `0xfc27...9d9d` | `SHORT` | 1,417,333.81 USD | `319,997.70` | `5.01` | `4.43` | `48.09` | 186,208.81 USD | `+13.14%` | `10X Cross` |
| `1705` | `0xe065...0f85` | `SHORT` | 1,285,970.80 USD | `290,227.90` | `2.81` | `4.43` | `6.28` | -469,226.56 USD | `-36.49%` | `10X Cross` |
| `1730` | `0x023a...2355` | `SHORT` | 1,259,809.49 USD | `284,355.70` | `4.60` | `4.43` | `32.77` | 47,811.75 USD | `+3.80%` | `10X Cross` |
| `1845` | `0xb69e...033a` | `LONG` | 1,139,307.64 USD | `257,081.40` | `4.61` | `4.43` | `2.45` | -44,747.23 USD | `-3.93%` | `10X Cross` |
| `1881` | `0xff43...d924` | `LONG` | 1,105,271.82 USD | `249,474.50` | `4.64` | `4.43` | `3.28` | -52,771.85 USD | `-4.77%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`4.53` (Vol: 539,200.00 USD, Dist: `+2.49%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--3.62%`)
  * 48H Horizon: Short MP=`4.83` (Vol: 541,200.00 USD, Dist: `+9.19%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--3.62%`)
  * 3D Horizon: Short MP=`4.83` (Vol: 541,200.00 USD, Dist: `+9.19%`) | Long MP=`4.26` (Vol: 618,400.00 USD, Dist: `--3.62%`)
  * 7D Horizon: Short MP=`5.02` (Vol: 897,800.00 USD, Dist: `+13.56%`) | Long MP=`4.23` (Vol: 1,400,000.00 USD, Dist: `--4.38%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8850` | 335.24 USD | 34,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,610.00 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,480.00 USD | 34,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 5,220,000.00 USD | 34,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 10,360.00 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 31,780.00 USD | 28,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 54,520.00 USD | 28,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 28,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 3,010.00 USD | 28,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 11,320.00 USD | 28,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 28,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 4,760.00 USD | 28,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 7,890.00 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 28,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 36,060.00 USD | 28,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 937.11 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 73,400.00 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 1,940.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 394,400.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 28,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 65,390.00 USD | 28,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 42,180.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 6,100.00 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 1,690.00 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 21,600.00 USD | 28,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 741.25 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 558.38 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 653.98 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 5,310.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 5,410.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 3,870.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 1,710.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 11,030.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 10,450.00 USD | 28,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 795.11 USD | 28,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,780.00 USD | 28,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 157.50 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 10,870.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 669.86 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 18,780.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 226.29 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 1,320.00 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,710.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 2,130.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 892.73 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 13,300.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 4,620.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,380.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 2,480.00 USD | 27,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 118.38 USD | 27,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 1,280.00 USD | 27,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,030.00 USD | 27,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 10,850.00 USD | 27,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 34,480.00 USD | 27,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 489.18 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,110.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 13,340.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 4,110.00 USD | 27,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 28,480.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 1,960.00 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 7,840.00 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 20,820.00 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 169,070.00 USD | 27,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 13,040.00 USD | 27,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 209,110.00 USD | 27,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 7,750.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 18,950.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 36,220.00 USD | 27,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 2,820.00 USD | 27,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 27,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,080.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 1,670,000.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 37,570.00 USD | 25,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 9,540.00 USD | 25,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,580.00 USD | 25,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,080.00 USD | 25,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 4,610.00 USD | 25,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 24,310.00 USD | 25,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 263.92 USD | 25,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 195,950.00 USD | 25,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 5,220.00 USD | 25,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 7,060.00 USD | 25,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 48,300.00 USD | 25,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 10,120.00 USD | 25,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 122,770.00 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 25,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 25,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 86,680.00 USD | 25,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 1,110.00 USD | 25,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 1,670.00 USD | 25,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 14,690.00 USD | 25,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 2,060.00 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 8,080.00 USD | 25,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 15,800.00 USD | 25,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 9,100.00 USD | 25,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 93,110.00 USD | 25,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 295.37 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 594.13 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 87,590.00 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 55,150.00 USD | 24,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,880.00 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 30,530.00 USD | 24,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 6,830.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 26,180.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 4,680.00 USD | 24,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 116,120.00 USD | 24,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 5,370.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 6,280.00 USD | 24,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 7,740.00 USD | 24,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,190.00 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 643.33 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 1,520,000.00 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 110,550.00 USD | 23,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,530.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 63,180.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 419,690.00 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 534.24 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 258.90 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 163,220.00 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 187,230.00 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 485.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 391,370.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 1,370.00 USD | 21,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 9,780.00 USD | 21,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 282,300.00 USD | 21,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 66,430.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 2,860.00 USD | 21,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,990.00 USD | 21,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 48,480.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 10,070.00 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 13,590.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 2,270.00 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 15,080.00 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 673,980.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 2,140.00 USD | 20,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 72,270.00 USD | 20,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 2,850.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 49,410.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 6,000.00 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 19,240.00 USD | 20,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 205,280.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,860.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,410.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 121,400.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 24,380.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 35,870.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 4,680.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,550.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 1,180.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 15,710.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 15,790.00 USD | 19,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,840.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 10,470.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 8,450.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 194,070.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,240.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 15,320.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 180.94 USD | 19,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 7,450.00 USD | 19,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 5,190.00 USD | 19,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 6,950.00 USD | 19,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 7,800.00 USD | 19,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 148,440.00 USD | 19,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 23,400.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 4,340.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 40,600.00 USD | 19,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 980.69 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 6,010.00 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 171.08 USD | 19,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 12,440.00 USD | 19,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 1,750.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,240.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 15,180.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 18,390.00 USD | 19,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 15,250.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 355,110.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 111,160.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 25,110.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 119,700.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 27,690.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 17,650.00 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 27,340.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 131,140.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 669,930.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,940.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 37,230.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 4,270.00 USD | 17,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 3,150.00 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 8,100.00 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 97,060.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 7,230.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 9,250.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 133,350.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 29,060.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 136,780.00 USD | 17,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,240.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 30,180.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 62,810.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 36,160.00 USD | 17,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 849,770.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 5,410.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,400,000.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 57,870.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 35,940.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 8,580.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 54,520.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 27,810.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 10,060.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 10,020.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 14,490.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 50,420.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 97,200.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 187,750.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 1,630.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 27,580.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 56,170.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 11,280.00 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 13,460.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 63,440.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 26,390.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 21,380.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 30,270.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 18,980.00 USD | 14,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 18,620.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 13,540.00 USD | 14,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 371,900.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 383,850.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 3,890.00 USD | 13,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 127,050.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 15,690.00 USD | 13,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 28,200.00 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 219,620.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 845.19 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 12,800.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 33,510.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 63,620.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 497,010.00 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 44,710.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 191,470.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 708,220.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 63,930.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 24,830.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 155,330.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 27,770.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 16,490.00 USD | 11,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,740.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 99,750.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 55,510.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 15,590.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 39,510.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 124,720.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 16,220.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 72,110.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 5,180.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 147,910.00 USD | 10,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 25,330.00 USD | 10,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 13,750.00 USD | 10,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.87` | 20,660.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.88` | 6,350.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.88` | 31,960,000.00 USD | 31,960,000.00 USD | 161,060.00 USD | 8,890.00 USD | 131,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 38,930.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.89` | 31,660,000.00 USD | 31,660,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 95,040.00 USD | 10,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.90` | 31,600,000.00 USD | 31,600,000.00 USD | 92,100.00 USD | 28,250.00 USD | 49,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 34,810.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.91` | 31,430,000.00 USD | 31,430,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,920,000.00 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.92` | 31,360,000.00 USD | 31,360,000.00 USD | 90,780.00 USD | 41,330.00 USD | 80,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 335,320.00 USD | 6,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 19,240,000.00 USD | 19,240,000.00 USD | 123,490.00 USD | 39,240.00 USD | 32,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 31,150,000.00 USD | 31,150,000.00 USD | 51,660.00 USD | 26,290.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 20,840.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 19,040,000.00 USD | 19,040,000.00 USD | 0.00 USD | 3,080.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 31,020,000.00 USD | 31,020,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 533,900.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 19,020,000.00 USD | 19,020,000.00 USD | 12,850.00 USD | 5,610.00 USD | 51.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 30,780,000.00 USD | 30,780,000.00 USD | 8,490.00 USD | 26,060.00 USD | 696.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 129,040.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 19,010,000.00 USD | 19,010,000.00 USD | 23,520.00 USD | 29,270.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 30,740,000.00 USD | 30,740,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 106,970.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 18,920,000.00 USD | 18,920,000.00 USD | 143,510.00 USD | 52,430.00 USD | 53,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 30,530,000.00 USD | 30,530,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 39,580.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 18,670,000.00 USD | 18,670,000.00 USD | 46,870.00 USD | 30,290.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 29,920,000.00 USD | 29,920,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 62,150.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 18,580,000.00 USD | 18,580,000.00 USD | 93,820.00 USD | 12,310.00 USD | 47,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 29,720,000.00 USD | 29,720,000.00 USD | 63,200.00 USD | 82,870.00 USD | 101,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 55,050.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 18,430,000.00 USD | 18,430,000.00 USD | 35,430.00 USD | 7,330.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 29,470,000.00 USD | 29,470,000.00 USD | 317,210.00 USD | 105,220.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 56,690.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 18,370,000.00 USD | 18,370,000.00 USD | 109,160.00 USD | 56,050.00 USD | 73,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 28,880,000.00 USD | 28,880,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 12,210.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 18,130,000.00 USD | 18,130,000.00 USD | 60,540.00 USD | 20,960.00 USD | 75,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 27,970,000.00 USD | 27,970,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 84,020.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 17,970,000.00 USD | 17,970,000.00 USD | 23,550.00 USD | 40,450.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 27,400,000.00 USD | 27,400,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 16,950.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 17,870,000.00 USD | 17,870,000.00 USD | 28,720.00 USD | 32,610.00 USD | 127,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 26,960,000.00 USD | 26,960,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 29,550.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 17,680,000.00 USD | 17,680,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 26,670,000.00 USD | 26,670,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 82,940.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 17,580,000.00 USD | 17,580,000.00 USD | 56,470.00 USD | 0.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 26,330,000.00 USD | 26,330,000.00 USD | 198,550.00 USD | 45,470.00 USD | 125,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 341,730.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 17,500,000.00 USD | 17,500,000.00 USD | 3,220.00 USD | 15,020.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 25,960,000.00 USD | 25,960,000.00 USD | 183,890.00 USD | 35,750.00 USD | 41,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 294,770.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 17,460,000.00 USD | 17,460,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 25,700,000.00 USD | 25,700,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 485,270.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 17,420,000.00 USD | 17,420,000.00 USD | 10,540.00 USD | 6,980.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 25,400,000.00 USD | 25,400,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 721,930.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 17,410,000.00 USD | 17,410,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 25,190,000.00 USD | 25,190,000.00 USD | 158,760.00 USD | 118,310.00 USD | 347,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 100,830.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 17,300,000.00 USD | 17,300,000.00 USD | 22,520.00 USD | 18,800.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 24,570,000.00 USD | 24,570,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 254,500.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 17,250,000.00 USD | 17,250,000.00 USD | 4,430.00 USD | 41,500.00 USD | 134,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 24,370,000.00 USD | 24,370,000.00 USD | 97,300.00 USD | 48,940.00 USD | 342,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 43,650.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 17,070,000.00 USD | 17,070,000.00 USD | 39,380.00 USD | 55,060.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 23,880,000.00 USD | 23,880,000.00 USD | 293,300.00 USD | 79,100.00 USD | 108,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 77,110.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 16,950,000.00 USD | 16,950,000.00 USD | 194,940.00 USD | 36,950.00 USD | 142,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 23,400,000.00 USD | 23,400,000.00 USD | 374,290.00 USD | 57,440.00 USD | 218,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 101,060.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 16,570,000.00 USD | 16,570,000.00 USD | 201,620.00 USD | 84,150.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 22,750,000.00 USD | 22,750,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 56,390.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 16,210,000.00 USD | 16,210,000.00 USD | 63,250.00 USD | 99,580.00 USD | 99,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 22,100,000.00 USD | 22,100,000.00 USD | 310,530.00 USD | 192,570.00 USD | 174,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 313,240.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 15,950,000.00 USD | 15,950,000.00 USD | 44,430.00 USD | 104,170.00 USD | 89,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 21,420,000.00 USD | 21,420,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 15,990.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.18` | 15,710,000.00 USD | 15,710,000.00 USD | 120,410.00 USD | 30,730.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 20,740,000.00 USD | 20,740,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.18` | 370,180.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.19` | 15,500,000.00 USD | 15,500,000.00 USD | 288,170.00 USD | 79,350.00 USD | 145,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 20,210,000.00 USD | 20,210,000.00 USD | 215,210.00 USD | 113,960.00 USD | 671,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.20` | 166,390.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.20` | 14,990,000.00 USD | 14,990,000.00 USD | 64,030.00 USD | 162,810.00 USD | 466,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 19,210,000.00 USD | 19,210,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 137,600.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.21` | 14,300,000.00 USD | 14,300,000.00 USD | 51,570.00 USD | 146,670.00 USD | 919.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 17,870,000.00 USD | 17,870,000.00 USD | 321,000.00 USD | 149,940.00 USD | 119,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 12,290.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 14,100,000.00 USD | 14,100,000.00 USD | 528,380.00 USD | 141,000.00 USD | 406,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 17,280,000.00 USD | 17,280,000.00 USD | 853,600.00 USD | 161,970.00 USD | 786,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.22` | 51,120.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.23` | 13,020,000.00 USD | 13,020,000.00 USD | 860,230.00 USD | 357,760.00 USD | 375,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 15,480,000.00 USD | 15,480,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.24` | 594,020.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.24` | 11,430,000.00 USD | 11,430,000.00 USD | 281,350.00 USD | 220,350.00 USD | 227,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 12,930,000.00 USD | 12,930,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 49,450.00 USD | 681,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.25` | 10,700,000.00 USD | 10,700,000.00 USD | 394,570.00 USD | 246,700.00 USD | 414,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 11,220,000.00 USD | 11,220,000.00 USD | 350,470.00 USD | 433,770.00 USD | 647,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 372,320.00 USD | 632,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.26` | 9,640,000.00 USD | 9,640,000.00 USD | 425,040.00 USD | 114,720.00 USD | 281,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 9,790,000.00 USD | 9,790,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.26` | 76,230.00 USD | 259,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.27` | 8,820,000.00 USD | 8,820,000.00 USD | 626,730.00 USD | 199,830.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 7,400,000.00 USD | 7,400,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.28` | 6,760.00 USD | 183,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 7,530,000.00 USD | 7,530,000.00 USD | 320,200.00 USD | 294,950.00 USD | 215,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 4,980,000.00 USD | 4,980,000.00 USD | 842,270.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 14,650.00 USD | 176,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.29` | 6,700,000.00 USD | 6,700,000.00 USD | 289,680.00 USD | 37,190.00 USD | 247,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 2,530,000.00 USD | 2,530,000.00 USD | 9,100.00 USD | 46,530.00 USD | 361.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 11,800.00 USD | 162,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.30` | 6,130,000.00 USD | 6,130,000.00 USD | 293,470.00 USD | 217,150.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.30` | 2,480,000.00 USD | 2,480,000.00 USD | 3,500.00 USD | 90,090.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.30` | 15,940.00 USD | 150,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.31` | 5,560,000.00 USD | 5,560,000.00 USD | 300,730.00 USD | 222,320.00 USD | 499,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.31` | 2,310,000.00 USD | 2,310,000.00 USD | 88,750.00 USD | 0.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.32` | 122.98 USD | 134,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 4,540,000.00 USD | 4,540,000.00 USD | 597,550.00 USD | 156,850.00 USD | 193,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 2,180,000.00 USD | 2,180,000.00 USD | 169,820.00 USD | 158,570.00 USD | 78,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 11,390.00 USD | 134,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.33` | 3,590,000.00 USD | 3,590,000.00 USD | 373,930.00 USD | 85,110.00 USD | 202,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.33` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 112,660.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 13,320.00 USD | 123,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.34` | 2,930,000.00 USD | 2,930,000.00 USD | 269,670.00 USD | 138,220.00 USD | 406,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 1,570,000.00 USD | 1,570,000.00 USD | 75,930.00 USD | 161,050.00 USD | 134,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.34` | 30,420.00 USD | 109,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.35` | 2,110,000.00 USD | 2,110,000.00 USD | 298,330.00 USD | 83,060.00 USD | 143,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.35` | 1,200,000.00 USD | 1,200,000.00 USD | 362,610.00 USD | 39,140.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.36` | 1,090.00 USD | 79,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.36` | 1,590,000.00 USD | 1,590,000.00 USD | 82,150.00 USD | 51,640.00 USD | 118,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.36` | 709,050.00 USD | 709,050.00 USD | 5,210.00 USD | 0.00 USD | 86,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.37` | 261.90 USD | 78,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.37` | 1,340,000.00 USD | 1,340,000.00 USD | 52,120.00 USD | 66,510.00 USD | 82,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 60,310.00 USD | 77,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.38` | 1,140,000.00 USD | 1,140,000.00 USD | 171,480.00 USD | 81,750.00 USD | 476,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.38` | 617,390.00 USD | 617,390.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 6,680.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.39` | 406,000.00 USD | 406,000.00 USD | 206,130.00 USD | 0.00 USD | 199,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.39` | 214,070.00 USD | 214,070.00 USD | 0.00 USD | 62,850.00 USD | 151,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.39` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 105.06 USD | 105.06 USD | 0.00 USD | 0.00 USD | 105.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.40` | 210.12 USD | 210.12 USD | 0.00 USD | 0.00 USD | 105.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 400,190.00 USD | 400,190.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 800,380.00 USD | 800,380.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 72,450.00 USD | 72,450.00 USD | 1,720.00 USD | 0.00 USD | 70,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 270,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 72,530.00 USD | 72,530.00 USD | 0.00 USD | 0.00 USD | 74.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 1,250,000.00 USD | 1,250,000.00 USD | 6,060.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 46,230.00 USD | 69,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 595,450.00 USD | 595,450.00 USD | 0.00 USD | 282,030.00 USD | 240,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 116,400.00 USD | 70,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 8,890.00 USD | 8,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 630,340.00 USD | 630,340.00 USD | 0.00 USD | 34,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.47` | 630,380.00 USD | 630,380.00 USD | 0.00 USD | 0.00 USD | 41.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 1,890,000.00 USD | 1,890,000.00 USD | 132,630.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.48` | 686,600.00 USD | 686,600.00 USD | 0.00 USD | 56,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 1,010.00 USD | 9,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 968,780.00 USD | 968,780.00 USD | 49,360.00 USD | 113,460.00 USD | 119,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 2,220,000.00 USD | 2,220,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.50` | 1,330,000.00 USD | 1,330,000.00 USD | 295,140.00 USD | 65,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 2,560,000.00 USD | 2,560,000.00 USD | 169,820.00 USD | 164,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.51` | 2,020,000.00 USD | 2,020,000.00 USD | 162,900.00 USD | 282,880.00 USD | 248,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 109.71 USD | 10,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 2,460,000.00 USD | 2,460,000.00 USD | 189,070.00 USD | 59,620.00 USD | 182,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.53` | 3,220,000.00 USD | 3,220,000.00 USD | 487,010.00 USD | 0.00 USD | 278,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 3,600,000.00 USD | 3,600,000.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 150,600.00 USD | 702,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 39,540.00 USD | 49,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 22,540.00 USD | 315,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 4,800,000.00 USD | 4,800,000.00 USD | 79,110.00 USD | 24,450.00 USD | 288,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 5,330,000.00 USD | 5,330,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 5,080,000.00 USD | 5,080,000.00 USD | 135,640.00 USD | 70,180.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 5,680,000.00 USD | 5,680,000.00 USD | 198,050.00 USD | 0.00 USD | 151,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 6,340,000.00 USD | 6,340,000.00 USD | 380,450.00 USD | 43,090.00 USD | 840,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 5,810,000.00 USD | 5,810,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 7,210,000.00 USD | 7,210,000.00 USD | 794,410.00 USD | 75,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 7,400,000.00 USD | 7,400,000.00 USD | 759,320.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 7,400,000.00 USD | 7,400,000.00 USD | 54,450.00 USD | 84,420.00 USD | 48,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 7,520,000.00 USD | 7,520,000.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 7,530,000.00 USD | 7,530,000.00 USD | 66,620.00 USD | 7,560.00 USD | 58,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 7,520,000.00 USD | 7,520,000.00 USD | 3,350.00 USD | 0.00 USD | 703.64 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 347.51 USD | 49,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.62` | 7,660,000.00 USD | 7,660,000.00 USD | 95,090.00 USD | 31,380.00 USD | 822.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 7,660,000.00 USD | 7,660,000.00 USD | 134,680.00 USD | 0.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 7,660,000.00 USD | 7,660,000.00 USD | 500.90 USD | 0.00 USD | 290.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 7,870,000.00 USD | 7,870,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 3,620.00 USD | 53,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 8,060,000.00 USD | 8,060,000.00 USD | 332,720.00 USD | 11,270.00 USD | 61,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 8,370,000.00 USD | 8,370,000.00 USD | 500,990.00 USD | 0.00 USD | 612.20 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 346.98 USD | 53,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 9,070,000.00 USD | 9,070,000.00 USD | 370,110.00 USD | 52,020.00 USD | 587,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 8,790,000.00 USD | 8,790,000.00 USD | 420,940.00 USD | 0.00 USD | 649.48 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 2,260.00 USD | 56,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 10,040,000.00 USD | 10,040,000.00 USD | 281,290.00 USD | 304,540.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 9,090,000.00 USD | 9,090,000.00 USD | 144,860.00 USD | 0.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,490.00 USD | 180,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 10,600,000.00 USD | 10,600,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 12,100.00 USD | 192,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 11,190,000.00 USD | 11,190,000.00 USD | 345,490.00 USD | 62,440.00 USD | 175,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 10,050,000.00 USD | 10,050,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 15,080.00 USD | 207,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 11,680,000.00 USD | 11,680,000.00 USD | 213,780.00 USD | 40,000.00 USD | 237,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 10,140,000.00 USD | 10,140,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 1,050.00 USD | 208,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 12,020,000.00 USD | 12,020,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 10,460,000.00 USD | 10,460,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 13,890.00 USD | 222,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 12,980,000.00 USD | 12,980,000.00 USD | 365,040.00 USD | 278,020.00 USD | 316,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 10,870,000.00 USD | 10,870,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 26,610.00 USD | 249,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 13,270,000.00 USD | 13,270,000.00 USD | 5,240.00 USD | 187,480.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 11,050,000.00 USD | 11,050,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 3,920.00 USD | 253,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 13,430,000.00 USD | 13,430,000.00 USD | 61,330.00 USD | 37,010.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 11,110,000.00 USD | 11,110,000.00 USD | 59,270.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 4,700.00 USD | 257,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 14,140,000.00 USD | 14,140,000.00 USD | 242,820.00 USD | 172,000.00 USD | 294,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 11,430,000.00 USD | 11,430,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 14,620.00 USD | 272,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 14,800,000.00 USD | 14,800,000.00 USD | 202,480.00 USD | 188,800.00 USD | 270,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 11,980,000.00 USD | 11,980,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 7,370.00 USD | 279,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 15,170,000.00 USD | 15,170,000.00 USD | 35,470.00 USD | 78,750.00 USD | 247,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 13,240,000.00 USD | 13,240,000.00 USD | 946,180.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.77` | 15,560,000.00 USD | 15,560,000.00 USD | 113,030.00 USD | 177,160.00 USD | 105,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 14,150,000.00 USD | 14,150,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,160.00 USD | 287,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 15,740,000.00 USD | 15,740,000.00 USD | 40,580.00 USD | 20,000.00 USD | 114,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 15,570,000.00 USD | 15,570,000.00 USD | 683,730.00 USD | 584,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 20,410.00 USD | 307,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 16,290,000.00 USD | 16,290,000.00 USD | 294,950.00 USD | 125,610.00 USD | 132,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 16,610,000.00 USD | 16,610,000.00 USD | 713,060.00 USD | 249,310.00 USD | 71,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 65,100.00 USD | 372,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 17,140,000.00 USD | 17,140,000.00 USD | 355,770.00 USD | 315,950.00 USD | 174,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 18,200,000.00 USD | 18,200,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 17,570,000.00 USD | 17,570,000.00 USD | 184,590.00 USD | 120,180.00 USD | 127,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 18,820,000.00 USD | 18,820,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 54,980.00 USD | 427,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 18,470,000.00 USD | 18,470,000.00 USD | 274,470.00 USD | 214,840.00 USD | 407,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 21,590,000.00 USD | 21,590,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 429,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 19,040,000.00 USD | 19,040,000.00 USD | 212,270.00 USD | 70,050.00 USD | 290,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 23,240,000.00 USD | 23,240,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,580,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 19,280,000.00 USD | 19,280,000.00 USD | 73,450.00 USD | 89,230.00 USD | 77,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 23,730,000.00 USD | 23,730,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.85` | 19,870,000.00 USD | 19,870,000.00 USD | 230,330.00 USD | 153,010.00 USD | 210,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 25,750,000.00 USD | 25,750,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.86` | 22,180.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.86` | 20,320,000.00 USD | 20,320,000.00 USD | 94,860.00 USD | 69,470.00 USD | 278,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 27,160,000.00 USD | 27,160,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.87` | 20,670,000.00 USD | 20,670,000.00 USD | 181,750.00 USD | 113,470.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.87` | 28,230,000.00 USD | 28,230,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 15,490.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.88` | 20,910,000.00 USD | 20,910,000.00 USD | 36,680.00 USD | 7,330.00 USD | 194,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 29,950,000.00 USD | 29,950,000.00 USD | 449,970.00 USD | 480,980.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.89` | 21,120,000.00 USD | 21,120,000.00 USD | 113,710.00 USD | 46,470.00 USD | 50,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.89` | 30,540,000.00 USD | 30,540,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.90` | 21,540,000.00 USD | 21,540,000.00 USD | 81,280.00 USD | 112,960.00 USD | 229,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 31,670,000.00 USD | 31,670,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.91` | 2,370.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.91` | 21,880,000.00 USD | 21,880,000.00 USD | 180,050.00 USD | 85,510.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 33,110,000.00 USD | 33,110,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 23,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.92` | 22,410,000.00 USD | 22,410,000.00 USD | 186,460.00 USD | 89,190.00 USD | 257,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.92` | 34,840,000.00 USD | 34,840,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 12,930.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.93` | 22,770,000.00 USD | 22,770,000.00 USD | 117,390.00 USD | 72,670.00 USD | 164,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.93` | 36,400,000.00 USD | 36,400,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.94` | 23,060,000.00 USD | 23,060,000.00 USD | 50,810.00 USD | 65,310.00 USD | 171,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.94` | 37,700,000.00 USD | 37,700,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.95` | 1,720.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.95` | 23,220,000.00 USD | 23,220,000.00 USD | 104,460.00 USD | 12,690.00 USD | 46,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 39,000,000.00 USD | 39,000,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 4,170.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.96` | 23,360,000.00 USD | 23,360,000.00 USD | 94,690.00 USD | 21,750.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.96` | 40,240,000.00 USD | 40,240,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 1,180.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.97` | 23,480,000.00 USD | 23,480,000.00 USD | 6,540.00 USD | 15,020.00 USD | 100,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 40,620,000.00 USD | 40,620,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.98` | 23,520,000.00 USD | 23,520,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.98` | 41,180,000.00 USD | 41,180,000.00 USD | 197,950.00 USD | 88,580.00 USD | 270,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 1,820.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.99` | 23,610,000.00 USD | 23,610,000.00 USD | 1,730.00 USD | 6,980.00 USD | 82,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.99` | 41,530,000.00 USD | 41,530,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.00` | 23,610,000.00 USD | 23,610,000.00 USD | 718.70 USD | 0.00 USD | 6.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.00` | 42,230,000.00 USD | 42,230,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 260.76 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.01` | 23,640,000.00 USD | 23,640,000.00 USD | 14,980.00 USD | 10,080.00 USD | 31.11 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 44,440,000.00 USD | 44,440,000.00 USD | 781,840.00 USD | 340,150.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `5.02` | 23,710,000.00 USD | 23,710,000.00 USD | 13,280.00 USD | 0.00 USD | 58,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 45,920,000.00 USD | 45,920,000.00 USD | 821,860.00 USD | 337,720.00 USD | 321,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.03` | 161,840.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.03` | 23,750,000.00 USD | 23,750,000.00 USD | 14,530.00 USD | 18,800.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 47,610,000.00 USD | 47,610,000.00 USD | 564,790.00 USD | 231,540.00 USD | 886,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `5.04` | 23,760,000.00 USD | 23,760,000.00 USD | 2,770.00 USD | 0.00 USD | 132.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 49,050,000.00 USD | 49,050,000.00 USD | 305,260.00 USD | 253,720.00 USD | 879,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,160.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.05` | 23,830,000.00 USD | 23,830,000.00 USD | 34,080.00 USD | 14,380.00 USD | 23,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 51,050,000.00 USD | 51,050,000.00 USD | 901,830.00 USD | 367,860.00 USD | 735,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 267,320.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `5.06` | 23,860,000.00 USD | 23,860,000.00 USD | 0.00 USD | 8,000.00 USD | 23,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.06` | 51,760,000.00 USD | 51,760,000.00 USD | 92,480.00 USD | 193,330.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 52,960,000.00 USD | 52,960,000.00 USD | 358,750.00 USD | 166,480.00 USD | 673,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 53,620,000.00 USD | 53,620,000.00 USD | 204,140.00 USD | 308,520.00 USD | 149,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 3,190.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 54,480,000.00 USD | 54,480,000.00 USD | 105,390.00 USD | 121,050.00 USD | 633,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 55,040,000.00 USD | 55,040,000.00 USD | 291,110.00 USD | 68,980.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.11` | 407.38 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.11` | 55,820,000.00 USD | 55,820,000.00 USD | 369,260.00 USD | 120,290.00 USD | 291,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 56,410,000.00 USD | 56,410,000.00 USD | 303,840.00 USD | 166,880.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,680.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 57,250,000.00 USD | 57,250,000.00 USD | 262,920.00 USD | 100,640.00 USD | 484,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,080.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 57,870,000.00 USD | 57,870,000.00 USD | 140,950.00 USD | 104,910.00 USD | 369,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.14` | 1,030.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.15` | 58,700,000.00 USD | 58,700,000.00 USD | 309,440.00 USD | 132,710.00 USD | 392,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 59,230,000.00 USD | 59,230,000.00 USD | 54,280.00 USD | 126,880.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 10,490.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 59,920,000.00 USD | 59,920,000.00 USD | 280,710.00 USD | 99,740.00 USD | 309,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 58,290.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.18` | 60,250,000.00 USD | 60,250,000.00 USD | 67,600.00 USD | 133,610.00 USD | 124,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 60,630,000.00 USD | 60,630,000.00 USD | 72,580.00 USD | 47,800.00 USD | 261,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.20` | 60,920,000.00 USD | 60,920,000.00 USD | 140,770.00 USD | 80,310.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.24` | 288.97 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 28,960.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 7,990.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 245.29 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 228.84 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 878.04 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 37,660.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 19,840.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 103,540.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 77,900.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 179.03 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 2,300.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 12,610.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 60,390.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.49` | 256,080.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 88,450.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 634.73 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 115,890.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 17,680.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.66` | 301.98 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 14,960.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 32,270.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 6,050.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.72` | 1,830.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 7,320.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.76` | 65,430.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 943.53 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 5,540.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 4,830.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 6,670.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 604.10 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 89,540.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.93` | 670.06 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.99` | 131.67 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.01` | 6,350.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 151,910.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.04` | 1,870.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 13,760.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 12,520.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 1,150,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.20` | 331,450.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,610.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 1,670.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 1,840,000.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 808.35 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 87,350.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 584,470.00 USD | 9,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 9,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,660.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 109.43 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 536.84 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 326.75 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 697.04 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 78,780.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 14,680.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 14,780.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 1,370.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 10,930.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 15,540.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 117,610.00 USD | 9,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 40,180.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.80` | 471.59 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 15,860.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 401,150.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.91` | 189.89 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.93` | 61,000.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 46,430.00 USD | 11,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 1,370.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 9,670,000.00 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 264.81 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.28` | 6,670.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 154.76 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 106,570.00 USD | 20,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.49` | 480.54 USD | 20,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 7,800,000.00 USD | 28,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 124,660.00 USD | 28,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 28,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 28,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.68` | 18,040.00 USD | 28,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 25,930.00 USD | 28,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 28,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 34,830.00 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.83` | 821.11 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 29,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.91` | 333,210.00 USD | 29,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 29,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 27,810.00 USD | 29,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 354.53 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 29,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.04` | 926,980.00 USD | 30,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.05` | 161,100.00 USD | 31,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 31,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.10` | 153.00 USD | 31,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.14` | 410,070.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.18` | 735,750.00 USD | 32,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 32,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 3,590.00 USD | 32,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 577.04 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.41` | 285.27 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 236.74 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 3,850.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 594.65 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.51` | 25,510.00 USD | 33,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 578.85 USD | 33,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 1,010.00 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 4,950.00 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.55` | 18,350.00 USD | 33,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 774.32 USD | 33,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.61` | 16,300.00 USD | 33,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.66` | 8,530.00 USD | 33,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 450,210.00 USD | 33,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.72` | 1,880,000.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.78` | 1,270.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.84` | 19,980.00 USD | 35,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.85` | 6,380.00 USD | 35,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8850` | 34,260,000.00 USD | 0.00 USD | 335.24 USD | `-80.01%` | `378.80` |
| `Live` | `Long` | `0.8950` | 34,250,000.00 USD | 0.00 USD | 39,610.00 USD | `-79.78%` | `44,259.70` |
| `Live` | `Long` | `0.9150` | 34,220,000.00 USD | 0.00 USD | 11,480.00 USD | `-79.33%` | `12,550.50` |
| `Live` | `Long` | `0.9250` | 34,200,000.00 USD | 0.00 USD | 5,220,000.00 USD | `-79.10%` | `5,640,376.30` |
| `Live` | `Long` | `0.9350` | 28,990,000.00 USD | 0.00 USD | 10,360.00 USD | `-78.88%` | `11,080.60` |
| `Live` | `Long` | `0.9650` | 28,980,000.00 USD | 0.00 USD | 31,780.00 USD | `-78.20%` | `32,933.00` |
| `Live` | `Long` | `0.9850` | 28,940,000.00 USD | 0.00 USD | 54,520.00 USD | `-77.75%` | `55,350.40` |
| `Live` | `Long` | `0.9950` | 28,890,000.00 USD | 0.00 USD | 154,200.00 USD | `-77.52%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 28,740,000.00 USD | 0.00 USD | 3,010.00 USD | `-77.30%` | `3,000.00` |
| `Live` | `Long` | `1.02` | 28,730,000.00 USD | 0.00 USD | 11,320.00 USD | `-76.84%` | `11,042.60` |
| `Live` | `Long` | `1.03` | 28,720,000.00 USD | 0.00 USD | 5,070.00 USD | `-76.62%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 28,720,000.00 USD | 0.00 USD | 4,760.00 USD | `-76.39%` | `4,557.50` |
| `Live` | `Long` | `1.05` | 28,710,000.00 USD | 0.00 USD | 7,890.00 USD | `-76.17%` | `7,479.20` |
| `Live` | `Long` | `1.06` | 28,700,000.00 USD | 0.00 USD | 892.90 USD | `-75.94%` | `838.40` |
| `Live` | `Long` | `1.07` | 28,700,000.00 USD | 0.00 USD | 36,060.00 USD | `-75.71%` | `33,539.70` |
| `Live` | `Long` | `1.08` | 28,670,000.00 USD | 0.00 USD | 937.11 USD | `-75.49%` | `863.70` |
| `Live` | `Long` | `1.09` | 28,670,000.00 USD | 0.00 USD | 73,400.00 USD | `-75.26%` | `67,034.60` |
| `Live` | `Long` | `1.10` | 28,590,000.00 USD | 0.00 USD | 1,940.00 USD | `-75.04%` | `1,756.00` |
| `Live` | `Long` | `1.11` | 28,590,000.00 USD | 0.00 USD | 557.50 USD | `-74.81%` | `500.00` |
| `Live` | `Long` | `1.12` | 28,590,000.00 USD | 0.00 USD | 394,400.00 USD | `-74.58%` | `350,578.40` |
| `Live` | `Long` | `1.14` | 28,200,000.00 USD | 0.00 USD | 4,960.00 USD | `-74.36%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 28,190,000.00 USD | 0.00 USD | 65,390.00 USD | `-74.13%` | `57,112.40` |
| `Live` | `Long` | `1.18` | 28,130,000.00 USD | 0.00 USD | 184.59 USD | `-73.46%` | `157.10` |
| `Live` | `Long` | `1.19` | 28,120,000.00 USD | 0.00 USD | 42,180.00 USD | `-73.23%` | `35,591.50` |
| `Live` | `Long` | `1.20` | 28,080,000.00 USD | 0.00 USD | 6,100.00 USD | `-73.00%` | `5,106.00` |
| `Live` | `Long` | `1.21` | 28,080,000.00 USD | 0.00 USD | 1,690.00 USD | `-72.78%` | `1,400.00` |
| `Live` | `Long` | `1.22` | 28,070,000.00 USD | 0.00 USD | 21,600.00 USD | `-72.55%` | `17,777.30` |
| `Live` | `Long` | `1.24` | 28,050,000.00 USD | 0.00 USD | 741.25 USD | `-72.10%` | `600.20` |
| `Live` | `Long` | `1.25` | 28,050,000.00 USD | 0.00 USD | 558.38 USD | `-71.87%` | `448.50` |
| `Live` | `Long` | `1.25` | 28,050,000.00 USD | 0.00 USD | 653.98 USD | `-71.65%` | `521.10` |
| `Live` | `Long` | `1.26` | 28,050,000.00 USD | 0.00 USD | 5,310.00 USD | `-71.42%` | `4,201.20` |
| `Live` | `Long` | `1.27` | 28,050,000.00 USD | 0.00 USD | 2,390.00 USD | `-71.20%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 28,040,000.00 USD | 0.00 USD | 169.23 USD | `-70.97%` | `131.70` |
| `Live` | `Long` | `1.30` | 28,040,000.00 USD | 0.00 USD | 116.80 USD | `-70.52%` | `89.50` |
| `Live` | `Long` | `1.31` | 28,040,000.00 USD | 0.00 USD | 5,410.00 USD | `-70.29%` | `4,111.30` |
| `Live` | `Long` | `1.32` | 28,040,000.00 USD | 0.00 USD | 3,870.00 USD | `-70.07%` | `2,923.50` |
| `Live` | `Long` | `1.33` | 28,030,000.00 USD | 0.00 USD | 1,710.00 USD | `-69.84%` | `1,280.00` |
| `Live` | `Long` | `1.34` | 28,030,000.00 USD | 0.00 USD | 11,030.00 USD | `-69.61%` | `8,199.30` |
| `Live` | `Long` | `1.35` | 28,020,000.00 USD | 0.00 USD | 10,450.00 USD | `-69.39%` | `7,712.70` |
| `Live` | `Long` | `1.36` | 28,010,000.00 USD | 0.00 USD | 795.11 USD | `-69.16%` | `582.50` |
| `Live` | `Long` | `1.38` | 28,010,000.00 USD | 0.00 USD | 12,780.00 USD | `-68.94%` | `9,293.40` |
| `Live` | `Long` | `1.39` | 28,000,000.00 USD | 0.00 USD | 295.56 USD | `-68.71%` | `213.40` |
| `Live` | `Long` | `1.40` | 28,000,000.00 USD | 0.00 USD | 157.50 USD | `-68.49%` | `112.90` |
| `Live` | `Long` | `1.41` | 28,000,000.00 USD | 0.00 USD | 10,870.00 USD | `-68.26%` | `7,736.30` |
| `Live` | `Long` | `1.42` | 27,990,000.00 USD | 0.00 USD | 669.86 USD | `-68.03%` | `473.40` |
| `Live` | `Long` | `1.43` | 27,990,000.00 USD | 0.00 USD | 18,780.00 USD | `-67.81%` | `13,181.20` |
| `Live` | `Long` | `1.45` | 27,970,000.00 USD | 0.00 USD | 226.29 USD | `-67.36%` | `156.60` |
| `Live` | `Long` | `1.47` | 27,970,000.00 USD | 0.00 USD | 1,320.00 USD | `-66.90%` | `900.20` |
| `Live` | `Long` | `1.48` | 27,970,000.00 USD | 0.00 USD | 1,480.00 USD | `-66.68%` | `1,000.00` |
| `Live` | `Long` | `1.50` | 27,960,000.00 USD | 0.00 USD | 4,710.00 USD | `-66.00%` | `3,132.00` |
| `Live` | `Long` | `1.51` | 27,960,000.00 USD | 0.00 USD | 454.50 USD | `-65.77%` | `300.00` |
| `Live` | `Long` | `1.52` | 27,960,000.00 USD | 0.00 USD | 2,130.00 USD | `-65.55%` | `1,399.90` |
| `Live` | `Long` | `1.53` | 27,960,000.00 USD | 0.00 USD | 279.37 USD | `-65.32%` | `182.00` |
| `Live` | `Long` | `1.55` | 27,960,000.00 USD | 0.00 USD | 892.73 USD | `-64.87%` | `574.10` |
| `Live` | `Long` | `1.56` | 27,960,000.00 USD | 0.00 USD | 13,300.00 USD | `-64.64%` | `8,501.00` |
| `Live` | `Long` | `1.57` | 27,940,000.00 USD | 0.00 USD | 589.52 USD | `-64.42%` | `374.30` |
| `Live` | `Long` | `1.58` | 27,940,000.00 USD | 0.00 USD | 4,620.00 USD | `-64.19%` | `2,914.40` |
| `Live` | `Long` | `1.59` | 27,940,000.00 USD | 0.00 USD | 3,380.00 USD | `-63.97%` | `2,119.70` |
| `Live` | `Long` | `1.60` | 27,930,000.00 USD | 0.00 USD | 2,480.00 USD | `-63.74%` | `1,546.10` |
| `Live` | `Long` | `1.61` | 27,930,000.00 USD | 0.00 USD | 118.38 USD | `-63.52%` | `73.30` |
| `Live` | `Long` | `1.62` | 27,930,000.00 USD | 0.00 USD | 1,280.00 USD | `-63.29%` | `790.10` |
| `Live` | `Long` | `1.64` | 27,930,000.00 USD | 0.00 USD | 2,030.00 USD | `-63.06%` | `1,241.00` |
| `Live` | `Long` | `1.65` | 27,930,000.00 USD | 0.00 USD | 10,850.00 USD | `-62.84%` | `6,596.40` |
| `Live` | `Long` | `1.66` | 27,920,000.00 USD | 0.00 USD | 34,480.00 USD | `-62.61%` | `20,833.60` |
| `Live` | `Long` | `1.67` | 27,880,000.00 USD | 0.00 USD | 489.18 USD | `-62.39%` | `293.80` |
| `Live` | `Long` | `1.68` | 27,880,000.00 USD | 0.00 USD | 1,110.00 USD | `-62.16%` | `664.90` |
| `Live` | `Long` | `1.69` | 27,880,000.00 USD | 0.00 USD | 13,340.00 USD | `-61.93%` | `7,914.10` |
| `Live` | `Long` | `1.70` | 27,870,000.00 USD | 0.00 USD | 4,110.00 USD | `-61.71%` | `2,422.20` |
| `Live` | `Long` | `1.71` | 27,860,000.00 USD | 0.00 USD | 28,480.00 USD | `-61.48%` | `16,703.50` |
| `Live` | `Long` | `1.72` | 27,830,000.00 USD | 0.00 USD | 1,960.00 USD | `-61.26%` | `1,143.10` |
| `Live` | `Long` | `1.73` | 27,830,000.00 USD | 0.00 USD | 7,840.00 USD | `-61.03%` | `4,542.50` |
| `Live` | `Long` | `1.74` | 27,820,000.00 USD | 0.00 USD | 20,820.00 USD | `-60.80%` | `12,000.00` |
| `Live` | `Long` | `1.75` | 27,800,000.00 USD | 0.00 USD | 169,070.00 USD | `-60.58%` | `96,890.70` |
| `Live` | `Long` | `1.75` | 27,630,000.00 USD | 0.00 USD | 13,040.00 USD | `-60.35%` | `7,431.00` |
| `Live` | `Long` | `1.76` | 27,620,000.00 USD | 0.00 USD | 209,110.00 USD | `-60.13%` | `118,476.40` |
| `Live` | `Long` | `1.77` | 27,410,000.00 USD | 0.00 USD | 7,750.00 USD | `-59.90%` | `4,367.20` |
| `Live` | `Long` | `1.78` | 27,400,000.00 USD | 0.00 USD | 18,950.00 USD | `-59.67%` | `10,616.10` |
| `Live` | `Long` | `1.80` | 27,390,000.00 USD | 0.00 USD | 36,220.00 USD | `-59.22%` | `20,064.10` |
| `Live` | `Long` | `1.81` | 27,350,000.00 USD | 0.00 USD | 2,820.00 USD | `-59.00%` | `1,555.40` |
| `Live` | `Long` | `1.83` | 27,350,000.00 USD | 0.00 USD | 27,520.00 USD | `-58.55%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 27,320,000.00 USD | 0.00 USD | 1,080.00 USD | `-58.32%` | `586.00` |
| `Live` | `Long` | `1.85` | 27,320,000.00 USD | 0.00 USD | 1,670,000.00 USD | `-58.09%` | `902,410.40` |
| `Live` | `Long` | `1.86` | 25,640,000.00 USD | 0.00 USD | 37,570.00 USD | `-57.87%` | `20,146.80` |
| `Live` | `Long` | `1.88` | 25,610,000.00 USD | 0.00 USD | 9,540.00 USD | `-57.64%` | `5,086.00` |
| `Live` | `Long` | `1.89` | 25,600,000.00 USD | 0.00 USD | 1,580.00 USD | `-57.42%` | `837.20` |
| `Live` | `Long` | `1.90` | 25,600,000.00 USD | 0.00 USD | 2,080.00 USD | `-57.19%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 25,590,000.00 USD | 0.00 USD | 4,610.00 USD | `-56.96%` | `2,418.00` |
| `Live` | `Long` | `1.92` | 25,590,000.00 USD | 0.00 USD | 24,310.00 USD | `-56.74%` | `12,696.90` |
| `Live` | `Long` | `1.93` | 25,560,000.00 USD | 0.00 USD | 263.92 USD | `-56.51%` | `137.10` |
| `Live` | `Long` | `1.94` | 25,560,000.00 USD | 0.00 USD | 195,950.00 USD | `-56.29%` | `101,265.60` |
| `Live` | `Long` | `1.95` | 25,370,000.00 USD | 0.00 USD | 5,220.00 USD | `-56.06%` | `2,685.00` |
| `Live` | `Long` | `1.97` | 25,360,000.00 USD | 0.00 USD | 7,060.00 USD | `-55.61%` | `3,591.40` |
| `Live` | `Long` | `1.98` | 25,360,000.00 USD | 0.00 USD | 48,300.00 USD | `-55.38%` | `24,457.80` |
| `Live` | `Long` | `2.00` | 25,310,000.00 USD | 0.00 USD | 10,120.00 USD | `-54.93%` | `5,074.60` |
| `Live` | `Long` | `2.00` | 25,300,000.00 USD | 0.00 USD | 122,770.00 USD | `-54.70%` | `61,234.30` |
| `Live` | `Long` | `2.02` | 25,170,000.00 USD | 0.00 USD | 260.62 USD | `-54.25%` | `128.70` |
| `Live` | `Long` | `2.04` | 25,170,000.00 USD | 0.00 USD | 3,460.00 USD | `-53.80%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 25,170,000.00 USD | 0.00 USD | 86,680.00 USD | `-53.58%` | `42,179.40` |
| `Live` | `Long` | `2.06` | 25,080,000.00 USD | 0.00 USD | 1,110.00 USD | `-53.35%` | `537.20` |
| `Live` | `Long` | `2.08` | 25,080,000.00 USD | 0.00 USD | 1,670.00 USD | `-53.12%` | `804.90` |
| `Live` | `Long` | `2.08` | 25,080,000.00 USD | 0.00 USD | 14,690.00 USD | `-52.90%` | `7,045.90` |
| `Live` | `Long` | `2.10` | 25,070,000.00 USD | 0.00 USD | 2,060.00 USD | `-52.67%` | `983.60` |
| `Live` | `Long` | `2.10` | 25,060,000.00 USD | 0.00 USD | 8,080.00 USD | `-52.45%` | `3,840.50` |
| `Live` | `Long` | `2.12` | 25,060,000.00 USD | 0.00 USD | 15,800.00 USD | `-52.22%` | `7,468.10` |
| `Live` | `Long` | `2.12` | 25,040,000.00 USD | 0.00 USD | 9,100.00 USD | `-51.99%` | `4,280.50` |
| `Live` | `Long` | `2.13` | 25,030,000.00 USD | 0.00 USD | 93,110.00 USD | `-51.77%` | `43,609.70` |
| `Live` | `Long` | `2.15` | 24,940,000.00 USD | 0.00 USD | 295.37 USD | `-51.54%` | `137.70` |
| `Live` | `Long` | `2.15` | 24,940,000.00 USD | 0.00 USD | 594.13 USD | `-51.32%` | `275.70` |
| `Live` | `Long` | `2.17` | 24,940,000.00 USD | 0.00 USD | 87,590.00 USD | `-50.86%` | `40,269.70` |
| `Live` | `Long` | `2.19` | 24,850,000.00 USD | 0.00 USD | 55,150.00 USD | `-50.64%` | `25,238.40` |
| `Live` | `Long` | `2.19` | 24,800,000.00 USD | 0.00 USD | 10,880.00 USD | `-50.41%` | `4,955.90` |
| `Live` | `Long` | `2.21` | 24,780,000.00 USD | 0.00 USD | 30,530.00 USD | `-50.19%` | `13,844.30` |
| `Live` | `Long` | `2.23` | 24,750,000.00 USD | 0.00 USD | 6,830.00 USD | `-49.73%` | `3,069.00` |
| `Live` | `Long` | `2.23` | 24,750,000.00 USD | 0.00 USD | 26,180.00 USD | `-49.51%` | `11,712.40` |
| `Live` | `Long` | `2.25` | 24,720,000.00 USD | 0.00 USD | 4,680.00 USD | `-49.28%` | `2,083.40` |
| `Live` | `Long` | `2.25` | 24,720,000.00 USD | 0.00 USD | 116,120.00 USD | `-49.06%` | `51,494.60` |
| `Live` | `Long` | `2.29` | 24,600,000.00 USD | 0.00 USD | 5,370.00 USD | `-48.38%` | `2,352.00` |
| `Live` | `Long` | `2.29` | 24,590,000.00 USD | 0.00 USD | 6,280.00 USD | `-48.15%` | `2,735.60` |
| `Live` | `Long` | `2.31` | 24,590,000.00 USD | 0.00 USD | 7,740.00 USD | `-47.93%` | `3,358.60` |
| `Live` | `Long` | `2.31` | 24,580,000.00 USD | 0.00 USD | 2,190.00 USD | `-47.70%` | `946.00` |
| `Live` | `Long` | `2.33` | 24,580,000.00 USD | 0.00 USD | 643.33 USD | `-47.48%` | `276.70` |
| `Live` | `Long` | `2.33` | 24,580,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-47.25%` | `653,002.20` |
| `Live` | `Long` | `2.35` | 23,050,000.00 USD | 0.00 USD | 110,550.00 USD | `-47.02%` | `47,142.50` |
| `Live` | `Long` | `2.35` | 22,940,000.00 USD | 0.00 USD | 5,530.00 USD | `-46.80%` | `2,348.10` |
| `Live` | `Long` | `2.37` | 22,940,000.00 USD | 0.00 USD | 63,180.00 USD | `-46.57%` | `26,713.50` |
| `Live` | `Long` | `2.38` | 22,870,000.00 USD | 0.00 USD | 419,690.00 USD | `-46.35%` | `176,713.40` |
| `Live` | `Long` | `2.38` | 22,450,000.00 USD | 0.00 USD | 534.24 USD | `-46.12%` | `224.00` |
| `Live` | `Long` | `2.40` | 22,450,000.00 USD | 0.00 USD | 258.90 USD | `-45.89%` | `108.10` |
| `Live` | `Long` | `2.40` | 22,450,000.00 USD | 0.00 USD | 163,220.00 USD | `-45.67%` | `67,865.60` |
| `Live` | `Long` | `2.42` | 22,290,000.00 USD | 0.00 USD | 187,230.00 USD | `-45.44%` | `77,526.00` |
| `Live` | `Long` | `2.42` | 22,100,000.00 USD | 0.00 USD | 485.00 USD | `-45.22%` | `200.00` |
| `Live` | `Long` | `2.44` | 22,100,000.00 USD | 0.00 USD | 391,370.00 USD | `-44.99%` | `160,725.70` |
| `Live` | `Long` | `2.46` | 21,710,000.00 USD | 0.00 USD | 1,370.00 USD | `-44.54%` | `556.20` |
| `Live` | `Long` | `2.46` | 21,710,000.00 USD | 0.00 USD | 9,780.00 USD | `-44.31%` | `3,967.70` |
| `Live` | `Long` | `2.48` | 21,700,000.00 USD | 0.00 USD | 282,300.00 USD | `-44.09%` | `114,061.30` |
| `Live` | `Long` | `2.48` | 21,420,000.00 USD | 0.00 USD | 66,430.00 USD | `-43.86%` | `26,732.20` |
| `Live` | `Long` | `2.50` | 21,350,000.00 USD | 0.00 USD | 2,860.00 USD | `-43.63%` | `1,144.50` |
| `Live` | `Long` | `2.50` | 21,350,000.00 USD | 0.00 USD | 7,990.00 USD | `-43.41%` | `3,189.20` |
| `Live` | `Long` | `2.52` | 21,340,000.00 USD | 0.00 USD | 48,480.00 USD | `-43.18%` | `19,276.90` |
| `Live` | `Long` | `2.52` | 21,290,000.00 USD | 0.00 USD | 10,070.00 USD | `-42.96%` | `3,987.90` |
| `Live` | `Long` | `2.54` | 21,280,000.00 USD | 0.00 USD | 395.71 USD | `-42.73%` | `156.10` |
| `Live` | `Long` | `2.54` | 21,280,000.00 USD | 0.00 USD | 13,590.00 USD | `-42.51%` | `5,341.70` |
| `Live` | `Long` | `2.56` | 21,270,000.00 USD | 0.00 USD | 2,270.00 USD | `-42.28%` | `887.10` |
| `Live` | `Long` | `2.56` | 21,270,000.00 USD | 0.00 USD | 15,080.00 USD | `-42.05%` | `5,877.60` |
| `Live` | `Long` | `2.58` | 21,250,000.00 USD | 0.00 USD | 673,980.00 USD | `-41.83%` | `261,740.80` |
| `Live` | `Long` | `2.58` | 20,580,000.00 USD | 0.00 USD | 2,140.00 USD | `-41.60%` | `829.10` |
| `Live` | `Long` | `2.60` | 20,570,000.00 USD | 0.00 USD | 72,270.00 USD | `-41.38%` | `27,850.30` |
| `Live` | `Long` | `2.62` | 20,500,000.00 USD | 0.00 USD | 1,190.00 USD | `-40.92%` | `454.70` |
| `Live` | `Long` | `2.62` | 20,500,000.00 USD | 0.00 USD | 2,850.00 USD | `-40.70%` | `1,085.50` |
| `Live` | `Long` | `2.63` | 20,500,000.00 USD | 0.00 USD | 49,410.00 USD | `-40.47%` | `18,750.30` |
| `Live` | `Long` | `2.65` | 20,450,000.00 USD | 0.00 USD | 6,000.00 USD | `-40.25%` | `2,268.00` |
| `Live` | `Long` | `2.65` | 20,440,000.00 USD | 0.00 USD | 18,510.00 USD | `-40.02%` | `6,972.60` |
| `Live` | `Long` | `2.67` | 20,420,000.00 USD | 0.00 USD | 19,240.00 USD | `-39.79%` | `7,219.00` |
| `Live` | `Long` | `2.67` | 20,400,000.00 USD | 0.00 USD | 205,280.00 USD | `-39.57%` | `76,740.30` |
| `Live` | `Long` | `2.69` | 20,200,000.00 USD | 0.00 USD | 4,860.00 USD | `-39.34%` | `1,809.60` |
| `Live` | `Long` | `2.69` | 20,190,000.00 USD | 0.00 USD | 4,410.00 USD | `-39.12%` | `1,636.30` |
| `Live` | `Long` | `2.71` | 20,190,000.00 USD | 0.00 USD | 121,400.00 USD | `-38.89%` | `44,881.10` |
| `Live` | `Long` | `2.71` | 20,070,000.00 USD | 0.00 USD | 24,380.00 USD | `-38.66%` | `8,978.90` |
| `Live` | `Long` | `2.73` | 20,040,000.00 USD | 0.00 USD | 35,870.00 USD | `-38.44%` | `13,164.00` |
| `Live` | `Long` | `2.73` | 20,010,000.00 USD | 0.00 USD | 4,680.00 USD | `-38.21%` | `1,710.70` |
| `Live` | `Long` | `2.75` | 20,000,000.00 USD | 0.00 USD | 39,550.00 USD | `-37.99%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 19,960,000.00 USD | 0.00 USD | 1,180.00 USD | `-37.76%` | `430.10` |
| `Live` | `Long` | `2.77` | 19,960,000.00 USD | 0.00 USD | 15,710.00 USD | `-37.54%` | `5,680.80` |
| `Live` | `Long` | `2.77` | 19,950,000.00 USD | 0.00 USD | 15,790.00 USD | `-37.31%` | `5,690.40` |
| `Live` | `Long` | `2.79` | 19,930,000.00 USD | 0.00 USD | 24,840.00 USD | `-37.08%` | `8,920.90` |
| `Live` | `Long` | `2.79` | 19,910,000.00 USD | 0.00 USD | 10,470.00 USD | `-36.86%` | `3,746.80` |
| `Live` | `Long` | `2.81` | 19,900,000.00 USD | 0.00 USD | 8,450.00 USD | `-36.63%` | `3,012.70` |
| `Live` | `Long` | `2.81` | 19,890,000.00 USD | 0.00 USD | 194,070.00 USD | `-36.41%` | `68,942.20` |
| `Live` | `Long` | `2.83` | 19,690,000.00 USD | 0.00 USD | 2,240.00 USD | `-36.18%` | `792.20` |
| `Live` | `Long` | `2.83` | 19,690,000.00 USD | 0.00 USD | 15,320.00 USD | `-35.95%` | `5,402.50` |
| `Live` | `Long` | `2.85` | 19,680,000.00 USD | 0.00 USD | 180.94 USD | `-35.73%` | `63.60` |
| `Live` | `Long` | `2.85` | 19,680,000.00 USD | 0.00 USD | 7,450.00 USD | `-35.50%` | `2,609.50` |
| `Live` | `Long` | `2.87` | 19,670,000.00 USD | 0.00 USD | 5,190.00 USD | `-35.28%` | `1,810.40` |
| `Live` | `Long` | `2.88` | 19,660,000.00 USD | 0.00 USD | 6,950.00 USD | `-35.05%` | `2,419.00` |
| `Live` | `Long` | `2.88` | 19,660,000.00 USD | 0.00 USD | 7,800.00 USD | `-34.82%` | `2,703.30` |
| `Live` | `Long` | `2.90` | 19,650,000.00 USD | 0.00 USD | 148,440.00 USD | `-34.60%` | `51,274.00` |
| `Live` | `Long` | `2.90` | 19,500,000.00 USD | 0.00 USD | 23,400.00 USD | `-34.37%` | `8,055.50` |
| `Live` | `Long` | `2.92` | 19,480,000.00 USD | 0.00 USD | 4,340.00 USD | `-34.15%` | `1,490.10` |
| `Live` | `Long` | `2.94` | 19,470,000.00 USD | 0.00 USD | 40,600.00 USD | `-33.69%` | `13,831.40` |
| `Live` | `Long` | `2.94` | 19,430,000.00 USD | 0.00 USD | 980.69 USD | `-33.47%` | `333.00` |
| `Live` | `Long` | `2.96` | 19,430,000.00 USD | 0.00 USD | 6,010.00 USD | `-33.24%` | `2,035.50` |
| `Live` | `Long` | `2.96` | 19,420,000.00 USD | 0.00 USD | 171.08 USD | `-33.02%` | `57.70` |
| `Live` | `Long` | `2.98` | 19,420,000.00 USD | 0.00 USD | 12,440.00 USD | `-32.79%` | `4,181.50` |
| `Live` | `Long` | `2.98` | 19,410,000.00 USD | 0.00 USD | 1,750.00 USD | `-32.57%` | `585.00` |
| `Live` | `Long` | `3.00` | 19,410,000.00 USD | 0.00 USD | 2,240.00 USD | `-32.34%` | `748.50` |
| `Live` | `Long` | `3.00` | 19,410,000.00 USD | 0.00 USD | 15,180.00 USD | `-32.11%` | `5,050.90` |
| `Live` | `Long` | `3.02` | 19,390,000.00 USD | 0.00 USD | 18,390.00 USD | `-31.89%` | `6,099.10` |
| `Live` | `Long` | `3.02` | 19,370,000.00 USD | 0.00 USD | 15,250.00 USD | `-31.66%` | `5,041.70` |
| `Live` | `Long` | `3.04` | 19,360,000.00 USD | 0.00 USD | 355,110.00 USD | `-31.44%` | `117,003.30` |
| `Live` | `Long` | `3.04` | 19,000,000.00 USD | 0.00 USD | 111,160.00 USD | `-31.21%` | `36,504.70` |
| `Live` | `Long` | `3.06` | 18,890,000.00 USD | 0.00 USD | 25,110.00 USD | `-30.98%` | `8,217.90` |
| `Live` | `Long` | `3.06` | 18,870,000.00 USD | 0.00 USD | 119,700.00 USD | `-30.76%` | `39,052.40` |
| `Live` | `Long` | `3.08` | 18,750,000.00 USD | 0.00 USD | 27,690.00 USD | `-30.53%` | `9,004.70` |
| `Live` | `Long` | `3.08` | 18,720,000.00 USD | 0.00 USD | 17,650.00 USD | `-30.31%` | `5,719.80` |
| `Live` | `Long` | `3.10` | 18,700,000.00 USD | 0.00 USD | 27,340.00 USD | `-30.08%` | `8,832.20` |
| `Live` | `Long` | `3.10` | 18,680,000.00 USD | 0.00 USD | 131,140.00 USD | `-29.85%` | `42,233.70` |
| `Live` | `Long` | `3.12` | 18,540,000.00 USD | 0.00 USD | 669,930.00 USD | `-29.63%` | `215,064.90` |
| `Live` | `Long` | `3.12` | 17,870,000.00 USD | 0.00 USD | 8,940.00 USD | `-29.40%` | `2,861.40` |
| `Live` | `Long` | `3.13` | 17,870,000.00 USD | 0.00 USD | 37,230.00 USD | `-29.18%` | `11,874.20` |
| `Live` | `Long` | `3.15` | 17,830,000.00 USD | 0.00 USD | 4,270.00 USD | `-28.95%` | `1,357.30` |
| `Live` | `Long` | `3.15` | 17,820,000.00 USD | 0.00 USD | 3,150.00 USD | `-28.72%` | `997.30` |
| `Live` | `Long` | `3.17` | 17,820,000.00 USD | 0.00 USD | 8,100.00 USD | `-28.50%` | `2,557.90` |
| `Live` | `Long` | `3.17` | 17,810,000.00 USD | 0.00 USD | 97,060.00 USD | `-28.27%` | `30,569.70` |
| `Live` | `Long` | `3.19` | 17,720,000.00 USD | 0.00 USD | 7,230.00 USD | `-28.05%` | `2,268.90` |
| `Live` | `Long` | `3.19` | 17,710,000.00 USD | 0.00 USD | 9,250.00 USD | `-27.82%` | `2,894.30` |
| `Live` | `Long` | `3.21` | 17,700,000.00 USD | 0.00 USD | 133,350.00 USD | `-27.60%` | `41,607.60` |
| `Live` | `Long` | `3.21` | 17,570,000.00 USD | 0.00 USD | 29,060.00 USD | `-27.37%` | `9,038.30` |
| `Live` | `Long` | `3.23` | 17,540,000.00 USD | 0.00 USD | 136,780.00 USD | `-27.14%` | `42,412.00` |
| `Live` | `Long` | `3.23` | 17,400,000.00 USD | 0.00 USD | 23,240.00 USD | `-26.92%` | `7,184.60` |
| `Live` | `Long` | `3.25` | 17,380,000.00 USD | 0.00 USD | 30,180.00 USD | `-26.69%` | `9,300.10` |
| `Live` | `Long` | `3.25` | 17,350,000.00 USD | 0.00 USD | 62,810.00 USD | `-26.47%` | `19,296.40` |
| `Live` | `Long` | `3.27` | 17,280,000.00 USD | 0.00 USD | 36,160.00 USD | `-26.24%` | `11,076.10` |
| `Live` | `Long` | `3.27` | 17,250,000.00 USD | 0.00 USD | 849,770.00 USD | `-26.01%` | `259,472.10` |
| `Live` | `Long` | `3.29` | 16,400,000.00 USD | 0.00 USD | 5,410.00 USD | `-25.79%` | `1,647.10` |
| `Live` | `Long` | `3.29` | 16,390,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-25.56%` | `425,178.00` |
| `Live` | `Long` | `3.31` | 14,990,000.00 USD | 0.00 USD | 57,870.00 USD | `-25.34%` | `17,508.90` |
| `Live` | `Long` | `3.31` | 14,930,000.00 USD | 0.00 USD | 35,940.00 USD | `-25.11%` | `10,841.20` |
| `Live` | `Long` | `3.33` | 14,900,000.00 USD | 0.00 USD | 8,580.00 USD | `-24.88%` | `2,581.10` |
| `Live` | `Long` | `3.33` | 14,890,000.00 USD | 0.00 USD | 54,520.00 USD | `-24.66%` | `16,349.00` |
| `Live` | `Long` | `3.35` | 14,830,000.00 USD | 0.00 USD | 27,810.00 USD | `-24.43%` | `8,312.60` |
| `Live` | `Long` | `3.35` | 14,810,000.00 USD | 0.00 USD | 10,060.00 USD | `-24.21%` | `3,000.00` |
| `Live` | `Long` | `3.37` | 14,800,000.00 USD | 0.00 USD | 10,020.00 USD | `-23.98%` | `2,977.70` |
| `Live` | `Long` | `3.38` | 14,790,000.00 USD | 0.00 USD | 14,490.00 USD | `-23.75%` | `4,293.30` |
| `Live` | `Long` | `3.38` | 14,770,000.00 USD | 0.00 USD | 50,420.00 USD | `-23.53%` | `14,895.60` |
| `Live` | `Long` | `3.40` | 14,720,000.00 USD | 0.00 USD | 97,200.00 USD | `-23.08%` | `28,546.80` |
| `Live` | `Long` | `3.42` | 14,620,000.00 USD | 0.00 USD | 187,750.00 USD | `-22.85%` | `54,978.40` |
| `Live` | `Long` | `3.42` | 14,440,000.00 USD | 0.00 USD | 1,630.00 USD | `-22.63%` | `476.50` |
| `Live` | `Long` | `3.44` | 14,440,000.00 USD | 0.00 USD | 27,580.00 USD | `-22.40%` | `8,030.20` |
| `Live` | `Long` | `3.44` | 14,410,000.00 USD | 0.00 USD | 56,170.00 USD | `-22.17%` | `16,305.60` |
| `Live` | `Long` | `3.46` | 14,350,000.00 USD | 0.00 USD | 11,280.00 USD | `-21.95%` | `3,266.00` |
| `Live` | `Long` | `3.46` | 14,340,000.00 USD | 0.00 USD | 13,460.00 USD | `-21.72%` | `3,885.70` |
| `Live` | `Long` | `3.48` | 14,330,000.00 USD | 0.00 USD | 63,440.00 USD | `-21.50%` | `18,256.60` |
| `Live` | `Long` | `3.48` | 14,260,000.00 USD | 0.00 USD | 26,390.00 USD | `-21.27%` | `7,571.50` |
| `Live` | `Long` | `3.50` | 14,240,000.00 USD | 0.00 USD | 21,380.00 USD | `-21.04%` | `6,116.20` |
| `Live` | `Long` | `3.50` | 14,220,000.00 USD | 0.00 USD | 30,270.00 USD | `-20.82%` | `8,635.40` |
| `Live` | `Long` | `3.52` | 14,190,000.00 USD | 0.00 USD | 18,980.00 USD | `-20.59%` | `5,399.90` |
| `Live` | `Long` | `3.52` | 14,170,000.00 USD | 0.00 USD | 18,620.00 USD | `-20.37%` | `5,281.80` |
| `Live` | `Long` | `3.54` | 14,150,000.00 USD | 0.00 USD | 13,540.00 USD | `-20.14%` | `3,831.10` |
| `Live` | `Long` | `3.54` | 14,130,000.00 USD | 0.00 USD | 371,900.00 USD | `-19.91%` | `104,909.20` |
| `Live` | `Long` | `3.56` | 13,760,000.00 USD | 0.00 USD | 383,850.00 USD | `-19.69%` | `107,974.30` |
| `Live` | `Long` | `3.56` | 13,380,000.00 USD | 0.00 USD | 3,890.00 USD | `-19.46%` | `1,092.50` |
| `Live` | `Long` | `3.58` | 13,370,000.00 USD | 0.00 USD | 127,050.00 USD | `-19.24%` | `35,537.30` |
| `Live` | `Long` | `3.58` | 13,250,000.00 USD | 0.00 USD | 15,690.00 USD | `-19.01%` | `4,376.20` |
| `Live` | `Long` | `3.60` | 13,230,000.00 USD | 0.00 USD | 28,200.00 USD | `-18.78%` | `7,843.90` |
| `Live` | `Long` | `3.60` | 13,200,000.00 USD | 0.00 USD | 219,620.00 USD | `-18.56%` | `60,920.90` |
| `Live` | `Long` | `3.62` | 12,980,000.00 USD | 0.00 USD | 845.19 USD | `-18.33%` | `233.80` |
| `Live` | `Long` | `3.62` | 12,980,000.00 USD | 0.00 USD | 12,800.00 USD | `-18.11%` | `3,531.90` |
| `Live` | `Long` | `3.63` | 12,970,000.00 USD | 0.00 USD | 33,510.00 USD | `-17.88%` | `9,218.60` |
| `Live` | `Long` | `3.65` | 12,940,000.00 USD | 0.00 USD | 63,620.00 USD | `-17.66%` | `17,454.60` |
| `Live` | `Long` | `3.65` | 12,870,000.00 USD | 0.00 USD | 497,010.00 USD | `-17.43%` | `135,979.60` |
| `Live` | `Long` | `3.67` | 12,380,000.00 USD | 0.00 USD | 44,710.00 USD | `-17.20%` | `12,199.40` |
| `Live` | `Long` | `3.67` | 12,330,000.00 USD | 0.00 USD | 191,470.00 USD | `-16.98%` | `52,101.90` |
| `Live` | `Long` | `3.69` | 12,140,000.00 USD | 0.00 USD | 708,220.00 USD | `-16.75%` | `192,188.90` |
| `Live` | `Long` | `3.69` | 11,430,000.00 USD | 0.00 USD | 63,930.00 USD | `-16.53%` | `17,302.90` |
| `Live` | `Long` | `3.71` | 11,370,000.00 USD | 0.00 USD | 24,830.00 USD | `-16.30%` | `6,700.90` |
| `Live` | `Long` | `3.71` | 11,340,000.00 USD | 0.00 USD | 155,330.00 USD | `-16.07%` | `41,811.30` |
| `Live` | `Long` | `3.73` | 11,190,000.00 USD | 0.00 USD | 27,770.00 USD | `-15.85%` | `7,453.90` |
| `Live` | `Long` | `3.73` | 11,160,000.00 USD | 0.00 USD | 16,490.00 USD | `-15.62%` | `4,414.60` |
| `Live` | `Long` | `3.75` | 11,140,000.00 USD | 0.00 USD | 24,740.00 USD | `-15.40%` | `6,604.90` |
| `Live` | `Long` | `3.75` | 11,120,000.00 USD | 0.00 USD | 99,750.00 USD | `-15.17%` | `26,565.90` |
| `Live` | `Long` | `3.77` | 11,020,000.00 USD | 0.00 USD | 55,510.00 USD | `-14.94%` | `14,744.70` |
| `Live` | `Long` | `3.77` | 10,960,000.00 USD | 0.00 USD | 15,590.00 USD | `-14.72%` | `4,130.60` |
| `Live` | `Long` | `3.79` | 10,950,000.00 USD | 0.00 USD | 39,510.00 USD | `-14.49%` | `10,438.50` |
| `Live` | `Long` | `3.79` | 10,910,000.00 USD | 0.00 USD | 124,720.00 USD | `-14.27%` | `32,863.20` |
| `Live` | `Long` | `3.81` | 10,780,000.00 USD | 0.00 USD | 16,220.00 USD | `-14.04%` | `4,264.00` |
| `Live` | `Long` | `3.81` | 10,770,000.00 USD | 0.00 USD | 72,110.00 USD | `-13.81%` | `18,902.20` |
| `Live` | `Long` | `3.83` | 10,700,000.00 USD | 0.00 USD | 5,180.00 USD | `-13.59%` | `1,354.50` |
| `Live` | `Long` | `3.83` | 10,690,000.00 USD | 0.00 USD | 147,910.00 USD | `-13.36%` | `38,568.30` |
| `Live` | `Long` | `3.85` | 10,540,000.00 USD | 0.00 USD | 25,330.00 USD | `-13.14%` | `6,588.90` |
| `Live` | `Long` | `3.85` | 10,520,000.00 USD | 0.00 USD | 13,750.00 USD | `-12.91%` | `3,567.80` |
| `Live` | `Long` | `3.87` | 10,500,000.00 USD | 0.00 USD | 20,660.00 USD | `-12.68%` | `5,346.30` |
| `Live` | `Long` | `3.88` | 10,480,000.00 USD | 0.00 USD | 6,350.00 USD | `-12.46%` | `1,638.60` |
| `Live` | `Long` | `3.88` | 10,480,000.00 USD | 0.00 USD | 38,930.00 USD | `-12.23%` | `10,020.30` |
| `Live` | `Long` | `3.90` | 10,440,000.00 USD | 0.00 USD | 95,040.00 USD | `-12.01%` | `24,400.70` |
| `Live` | `Long` | `3.90` | 10,340,000.00 USD | 0.00 USD | 34,810.00 USD | `-11.78%` | `8,915.20` |
| `Live` | `Long` | `3.92` | 10,310,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-11.56%` | `1,001,918.60` |
| `Live` | `Long` | `3.92` | 6,390,000.00 USD | 0.00 USD | 335,320.00 USD | `-11.33%` | `85,431.70` |
| `Live` | `Long` | `3.94` | 6,050,000.00 USD | 0.00 USD | 20,840.00 USD | `-11.10%` | `5,295.30` |
| `Live` | `Long` | `3.94` | 6,030,000.00 USD | 0.00 USD | 533,900.00 USD | `-10.88%` | `135,336.70` |
| `Live` | `Long` | `3.96` | 5,490,000.00 USD | 0.00 USD | 129,040.00 USD | `-10.65%` | `32,626.90` |
| `Live` | `Long` | `3.96` | 5,370,000.00 USD | 0.00 USD | 106,970.00 USD | `-10.43%` | `26,977.40` |
| `Live` | `Long` | `3.98` | 5,260,000.00 USD | 0.00 USD | 39,580.00 USD | `-10.20%` | `9,958.20` |
| `Live` | `Long` | `3.98` | 5,220,000.00 USD | 0.00 USD | 62,150.00 USD | `-9.97%` | `15,596.50` |
| `Live` | `Long` | `4.00` | 5,160,000.00 USD | 0.00 USD | 55,050.00 USD | `-9.75%` | `13,779.80` |
| `Live` | `Long` | `4.00` | 5,100,000.00 USD | 0.00 USD | 56,690.00 USD | `-9.52%` | `14,154.60` |
| `Live` | `Long` | `4.01` | 5,050,000.00 USD | 0.00 USD | 12,210.00 USD | `-9.30%` | `3,040.40` |
| `Live` | `Long` | `4.03` | 5,030,000.00 USD | 0.00 USD | 84,020.00 USD | `-9.07%` | `20,873.50` |
| `Live` | `Long` | `4.04` | 4,950,000.00 USD | 0.00 USD | 16,950.00 USD | `-8.84%` | `4,200.30` |
| `Live` | `Long` | `4.04` | 4,930,000.00 USD | 0.00 USD | 29,550.00 USD | `-8.62%` | `7,306.00` |
| `Live` | `Long` | `4.05` | 4,900,000.00 USD | 0.00 USD | 82,940.00 USD | `-8.39%` | `20,453.10` |
| `Live` | `Long` | `4.07` | 4,820,000.00 USD | 0.00 USD | 341,730.00 USD | `-8.17%` | `84,065.90` |
| `Live` | `Long` | `4.08` | 4,480,000.00 USD | 0.00 USD | 294,770.00 USD | `-7.94%` | `72,337.00` |
| `Live` | `Long` | `4.08` | 4,180,000.00 USD | 0.00 USD | 485,270.00 USD | `-7.71%` | `118,793.30` |
| `Live` | `Long` | `4.09` | 3,700,000.00 USD | 0.00 USD | 721,930.00 USD | `-7.49%` | `176,294.40` |
| `Live` | `Long` | `4.11` | 2,980,000.00 USD | 0.00 USD | 100,830.00 USD | `-7.26%` | `24,563.00` |
| `Live` | `Long` | `4.12` | 2,880,000.00 USD | 0.00 USD | 254,500.00 USD | `-7.04%` | `61,847.80` |
| `Live` | `Long` | `4.12` | 2,620,000.00 USD | 0.00 USD | 43,650.00 USD | `-6.81%` | `10,582.50` |
| `Live` | `Long` | `4.13` | 2,580,000.00 USD | 0.00 USD | 77,110.00 USD | `-6.59%` | `18,647.10` |
| `Live` | `Long` | `4.14` | 2,500,000.00 USD | 0.00 USD | 101,060.00 USD | `-6.36%` | `24,380.50` |
| `Live` | `Long` | `4.16` | 2,400,000.00 USD | 0.00 USD | 56,390.00 USD | `-6.13%` | `13,570.80` |
| `Live` | `Long` | `4.17` | 2,340,000.00 USD | 0.00 USD | 313,240.00 USD | `-5.91%` | `75,208.60` |
| `Live` | `Long` | `4.17` | 2,030,000.00 USD | 0.00 USD | 15,990.00 USD | `-5.68%` | `3,830.30` |
| `Live` | `Long` | `4.18` | 2,010,000.00 USD | 0.00 USD | 370,180.00 USD | `-5.46%` | `88,454.40` |
| `Live` | `Long` | `4.20` | 1,640,000.00 USD | 0.00 USD | 166,390.00 USD | `-5.23%` | `39,664.60` |
| `Live` | `Long` | `4.21` | 1,480,000.00 USD | 0.00 USD | 137,600.00 USD | `-5.00%` | `32,723.10` |
| `Live` | `Long` | `4.21` | 1,340,000.00 USD | 0.00 USD | 12,290.00 USD | `-4.78%` | `2,916.30` |
| `Live` | `Long` | `4.22` | 1,330,000.00 USD | 0.00 USD | 51,120.00 USD | `-4.55%` | `12,099.90` |
| `Live` | `Long` | `4.24` | 1,280,000.00 USD | 0.00 USD | 594,020.00 USD | `-4.33%` | `140,264.70` |
| `Live` | `Long` | `4.25` | 681,730.00 USD | 0.00 USD | 49,450.00 USD | `-4.10%` | `11,648.00` |
| `Live` | `Long` | `4.25` | 632,280.00 USD | 0.00 USD | 372,320.00 USD | `-3.87%` | `87,501.00` |
| `Live` | `Long` | `4.26` | 259,970.00 USD | 0.00 USD | 76,230.00 USD | `-3.65%` | `17,873.50` |
| `Live` | `Long` | `4.28` | 183,740.00 USD | 0.00 USD | 6,760.00 USD | `-3.42%` | `1,581.70` |
| `Live` | `Long` | `4.29` | 176,980.00 USD | 0.00 USD | 14,650.00 USD | `-3.20%` | `3,418.00` |
| `Live` | `Long` | `4.29` | 162,330.00 USD | 0.00 USD | 11,800.00 USD | `-2.97%` | `2,746.30` |
| `Live` | `Long` | `4.30` | 150,530.00 USD | 0.00 USD | 15,940.00 USD | `-2.74%` | `3,703.80` |
| `Live` | `Long` | `4.32` | 134,590.00 USD | 0.00 USD | 122.98 USD | `-2.52%` | `28.50` |
| `Live` | `Long` | `4.33` | 134,470.00 USD | 0.00 USD | 11,390.00 USD | `-2.29%` | `2,633.30` |
| `Live` | `Long` | `4.33` | 123,080.00 USD | 0.00 USD | 13,320.00 USD | `-2.07%` | `3,072.50` |
| `Live` | `Long` | `4.34` | 109,760.00 USD | 0.00 USD | 30,420.00 USD | `-1.84%` | `7,000.00` |
| `Live` | `Long` | `4.36` | 79,340.00 USD | 0.00 USD | 1,090.00 USD | `-1.62%` | `251.00` |
| `Live` | `Long` | `4.37` | 78,250.00 USD | 0.00 USD | 261.90 USD | `-1.39%` | `60.00` |
| `Live` | `Long` | `4.38` | 77,990.00 USD | 0.00 USD | 60,310.00 USD | `-1.16%` | `13,785.60` |
| `Live` | `Long` | `4.38` | 17,680.00 USD | 0.00 USD | 6,680.00 USD | `-0.94%` | `1,522.70` |
| `Live` | `Long` | `4.39` | 11,000.00 USD | 0.00 USD | 11,000.00 USD | `-0.71%` | `2,502.60` |
| `Live` | `Short` | `4.45` | 8,890.00 USD | 8,890.00 USD | 0.00 USD | `+0.42%` | `2,000.00` |
| `Live` | `Short` | `4.49` | 9,900.00 USD | 1,010.00 USD | 0.00 USD | `+1.32%` | `225.40` |
| `Live` | `Short` | `4.51` | 10,010.00 USD | 109.71 USD | 0.00 USD | `+2.00%` | `24.30` |
| `Live` | `Short` | `4.54` | 49,550.00 USD | 39,540.00 USD | 0.00 USD | `+2.68%` | `8,699.10` |
| `Live` | `Short` | `4.62` | 49,900.00 USD | 347.51 USD | 0.00 USD | `+4.26%` | `75.30` |
| `Live` | `Short` | `4.63` | 53,520.00 USD | 3,620.00 USD | 0.00 USD | `+4.71%` | `781.40` |
| `Live` | `Short` | `4.64` | 53,860.00 USD | 346.98 USD | 0.00 USD | `+4.94%` | `74.70` |
| `Live` | `Short` | `4.66` | 56,130.00 USD | 2,260.00 USD | 0.00 USD | `+5.16%` | `486.20` |
| `Live` | `Short` | `4.67` | 180,610.00 USD | 124,490.00 USD | 0.00 USD | `+5.39%` | `26,685.00` |
| `Live` | `Short` | `4.67` | 192,710.00 USD | 12,100.00 USD | 0.00 USD | `+5.61%` | `2,588.10` |
| `Live` | `Short` | `4.68` | 207,790.00 USD | 15,080.00 USD | 0.00 USD | `+5.84%` | `3,219.20` |
| `Live` | `Short` | `4.70` | 208,850.00 USD | 1,050.00 USD | 0.00 USD | `+6.07%` | `224.00` |
| `Live` | `Short` | `4.71` | 222,740.00 USD | 13,890.00 USD | 0.00 USD | `+6.29%` | `2,952.40` |
| `Live` | `Short` | `4.71` | 249,350.00 USD | 26,610.00 USD | 0.00 USD | `+6.52%` | `5,643.40` |
| `Live` | `Short` | `4.72` | 253,270.00 USD | 3,920.00 USD | 0.00 USD | `+6.74%` | `830.00` |
| `Live` | `Short` | `4.74` | 257,970.00 USD | 4,700.00 USD | 0.00 USD | `+6.97%` | `993.40` |
| `Live` | `Short` | `4.75` | 272,590.00 USD | 14,620.00 USD | 0.00 USD | `+7.20%` | `3,080.90` |
| `Live` | `Short` | `4.75` | 279,960.00 USD | 7,370.00 USD | 0.00 USD | `+7.42%` | `1,550.00` |
| `Live` | `Short` | `4.78` | 287,120.00 USD | 7,160.00 USD | 0.00 USD | `+7.87%` | `1,498.90` |
| `Live` | `Short` | `4.79` | 307,530.00 USD | 20,410.00 USD | 0.00 USD | `+8.10%` | `4,266.20` |
| `Live` | `Short` | `4.79` | 372,630.00 USD | 65,100.00 USD | 0.00 USD | `+8.32%` | `13,576.70` |
| `Live` | `Short` | `4.82` | 427,620.00 USD | 54,980.00 USD | 0.00 USD | `+8.78%` | `11,419.20` |
| `Live` | `Short` | `4.83` | 429,360.00 USD | 1,740.00 USD | 0.00 USD | `+9.00%` | `360.90` |
| `Live` | `Short` | `4.83` | 2,010,000.00 USD | 1,580,000.00 USD | 0.00 USD | `+9.23%` | `326,187.90` |
| `Live` | `Short` | `4.86` | 2,030,000.00 USD | 22,180.00 USD | 0.00 USD | `+9.68%` | `4,567.70` |
| `Live` | `Short` | `4.87` | 2,030,000.00 USD | 5,460.00 USD | 0.00 USD | `+9.91%` | `1,121.90` |
| `Live` | `Short` | `4.88` | 2,050,000.00 USD | 15,490.00 USD | 0.00 USD | `+10.13%` | `3,177.10` |
| `Live` | `Short` | `4.88` | 2,050,000.00 USD | 827.03 USD | 0.00 USD | `+10.36%` | `169.30` |
| `Live` | `Short` | `4.91` | 2,050,000.00 USD | 2,370.00 USD | 0.00 USD | `+10.81%` | `483.80` |
| `Live` | `Short` | `4.92` | 2,080,000.00 USD | 23,000.00 USD | 0.00 USD | `+11.04%` | `4,679.80` |
| `Live` | `Short` | `4.92` | 2,090,000.00 USD | 12,930.00 USD | 0.00 USD | `+11.26%` | `2,625.70` |
| `Live` | `Short` | `4.93` | 2,090,000.00 USD | 157.43 USD | 0.00 USD | `+11.49%` | `31.90` |
| `Live` | `Short` | `4.95` | 2,090,000.00 USD | 1,720.00 USD | 0.00 USD | `+11.71%` | `348.60` |
| `Live` | `Short` | `4.96` | 2,090,000.00 USD | 4,170.00 USD | 0.00 USD | `+11.94%` | `842.00` |
| `Live` | `Short` | `4.96` | 2,100,000.00 USD | 1,180.00 USD | 0.00 USD | `+12.17%` | `237.50` |
| `Live` | `Short` | `4.97` | 2,200,000.00 USD | 99,810.00 USD | 0.00 USD | `+12.39%` | `20,062.00` |
| `Live` | `Short` | `4.99` | 2,200,000.00 USD | 1,820.00 USD | 0.00 USD | `+12.62%` | `364.10` |
| `Live` | `Short` | `5.00` | 2,200,000.00 USD | 339.66 USD | 0.00 USD | `+12.84%` | `68.00` |
| `Live` | `Short` | `5.00` | 2,200,000.00 USD | 260.76 USD | 0.00 USD | `+13.07%` | `52.10` |
| `Live` | `Short` | `5.03` | 2,360,000.00 USD | 161,840.00 USD | 0.00 USD | `+13.52%` | `32,207.40` |
| `Live` | `Short` | `5.04` | 2,360,000.00 USD | 1,160.00 USD | 0.00 USD | `+13.97%` | `230.50` |
| `Live` | `Short` | `5.05` | 2,630,000.00 USD | 267,320.00 USD | 0.00 USD | `+14.20%` | `52,882.00` |
| `Live` | `Short` | `5.07` | 2,630,000.00 USD | 3,420.00 USD | 0.00 USD | `+14.42%` | `675.80` |
| `Live` | `Short` | `5.08` | 2,640,000.00 USD | 3,190.00 USD | 0.00 USD | `+14.88%` | `627.90` |
| `Live` | `Short` | `5.11` | 2,640,000.00 USD | 407.38 USD | 0.00 USD | `+15.33%` | `79.80` |
| `Live` | `Short` | `5.12` | 2,640,000.00 USD | 2,680.00 USD | 0.00 USD | `+15.78%` | `522.30` |
| `Live` | `Short` | `5.13` | 2,640,000.00 USD | 1,080.00 USD | 0.00 USD | `+16.01%` | `210.70` |
| `Live` | `Short` | `5.14` | 2,640,000.00 USD | 1,030.00 USD | 0.00 USD | `+16.23%` | `200.00` |
| `Live` | `Short` | `5.17` | 2,650,000.00 USD | 10,490.00 USD | 0.00 USD | `+16.68%` | `2,031.30` |
| `Live` | `Short` | `5.17` | 2,710,000.00 USD | 58,290.00 USD | 0.00 USD | `+16.91%` | `11,263.20` |
| `Live` | `Short` | `5.21` | 3,610,000.00 USD | 898,120.00 USD | 0.00 USD | `+17.59%` | `172,549.20` |
| `Live` | `Short` | `5.22` | 3,680,000.00 USD | 72,110.00 USD | 0.00 USD | `+18.04%` | `13,800.00` |
| `Live` | `Short` | `5.24` | 3,680,000.00 USD | 288.97 USD | 0.00 USD | `+18.26%` | `55.20` |
| `Live` | `Short` | `5.25` | 3,710,000.00 USD | 28,960.00 USD | 0.00 USD | `+18.49%` | `5,520.80` |
| `Live` | `Short` | `5.25` | 3,720,000.00 USD | 7,990.00 USD | 0.00 USD | `+18.72%` | `1,520.00` |
| `Live` | `Short` | `5.26` | 3,720,000.00 USD | 5,610.00 USD | 0.00 USD | `+18.94%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 3,720,000.00 USD | 245.29 USD | 0.00 USD | `+19.17%` | `46.50` |
| `Live` | `Short` | `5.29` | 3,720,000.00 USD | 228.84 USD | 0.00 USD | `+19.39%` | `43.30` |
| `Live` | `Short` | `5.30` | 3,720,000.00 USD | 524.66 USD | 0.00 USD | `+19.85%` | `98.90` |
| `Live` | `Short` | `5.32` | 3,720,000.00 USD | 878.04 USD | 0.00 USD | `+20.07%` | `165.20` |
| `Live` | `Short` | `5.33` | 3,760,000.00 USD | 37,660.00 USD | 0.00 USD | `+20.30%` | `7,072.30` |
| `Live` | `Short` | `5.34` | 3,780,000.00 USD | 19,840.00 USD | 0.00 USD | `+20.75%` | `3,711.90` |
| `Live` | `Short` | `5.36` | 3,890,000.00 USD | 103,540.00 USD | 0.00 USD | `+20.98%` | `19,335.80` |
| `Live` | `Short` | `5.38` | 3,960,000.00 USD | 77,900.00 USD | 0.00 USD | `+21.43%` | `14,493.40` |
| `Live` | `Short` | `5.42` | 3,960,000.00 USD | 179.03 USD | 0.00 USD | `+22.56%` | `33.00` |
| `Live` | `Short` | `5.43` | 3,960,000.00 USD | 962.54 USD | 0.00 USD | `+22.78%` | `177.10` |
| `Live` | `Short` | `5.45` | 3,970,000.00 USD | 2,300.00 USD | 0.00 USD | `+23.01%` | `422.30` |
| `Live` | `Short` | `5.46` | 3,980,000.00 USD | 12,610.00 USD | 0.00 USD | `+23.24%` | `2,311.50` |
| `Live` | `Short` | `5.46` | 4,040,000.00 USD | 60,390.00 USD | 0.00 USD | `+23.46%` | `11,051.10` |
| `Live` | `Short` | `5.49` | 4,300,000.00 USD | 256,080.00 USD | 0.00 USD | `+23.91%` | `46,687.50` |
| `Live` | `Short` | `5.50` | 4,380,000.00 USD | 88,450.00 USD | 0.00 USD | `+24.14%` | `16,097.30` |
| `Live` | `Short` | `5.50` | 4,380,000.00 USD | 634.73 USD | 0.00 USD | `+24.36%` | `115.30` |
| `Live` | `Short` | `5.51` | 4,420,000.00 USD | 38,800.00 USD | 0.00 USD | `+24.59%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 4,420,000.00 USD | 209.22 USD | 0.00 USD | `+25.04%` | `37.80` |
| `Live` | `Short` | `5.57` | 4,430,000.00 USD | 8,670.00 USD | 0.00 USD | `+25.72%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,550,000.00 USD | 115,890.00 USD | 0.00 USD | `+26.17%` | `20,750.50` |
| `Live` | `Short` | `5.59` | 4,550,000.00 USD | 686.51 USD | 0.00 USD | `+26.40%` | `122.70` |
| `Live` | `Short` | `5.61` | 4,570,000.00 USD | 17,680.00 USD | 0.00 USD | `+26.62%` | `3,153.90` |
| `Live` | `Short` | `5.66` | 4,570,000.00 USD | 301.98 USD | 0.00 USD | `+27.75%` | `53.40` |
| `Live` | `Short` | `5.67` | 4,580,000.00 USD | 14,960.00 USD | 0.00 USD | `+27.98%` | `2,641.30` |
| `Live` | `Short` | `5.67` | 4,580,000.00 USD | 228.70 USD | 0.00 USD | `+28.21%` | `40.30` |
| `Live` | `Short` | `5.68` | 4,610,000.00 USD | 32,270.00 USD | 0.00 USD | `+28.43%` | `5,676.90` |
| `Live` | `Short` | `5.70` | 4,620,000.00 USD | 6,050.00 USD | 0.00 USD | `+28.66%` | `1,061.60` |
| `Live` | `Short` | `5.71` | 4,620,000.00 USD | 2,130.00 USD | 0.00 USD | `+29.11%` | `372.40` |
| `Live` | `Short` | `5.72` | 4,620,000.00 USD | 1,830.00 USD | 0.00 USD | `+29.33%` | `320.50` |
| `Live` | `Short` | `5.75` | 4,630,000.00 USD | 7,320.00 USD | 0.00 USD | `+29.79%` | `1,273.90` |
| `Live` | `Short` | `5.75` | 4,630,000.00 USD | 286.02 USD | 0.00 USD | `+30.01%` | `49.70` |
| `Live` | `Short` | `5.76` | 4,700,000.00 USD | 65,430.00 USD | 0.00 USD | `+30.24%` | `11,349.70` |
| `Live` | `Short` | `5.79` | 4,700,000.00 USD | 943.53 USD | 0.00 USD | `+30.69%` | `163.10` |
| `Live` | `Short` | `5.83` | 4,700,000.00 USD | 5,540.00 USD | 0.00 USD | `+31.59%` | `950.80` |
| `Live` | `Short` | `5.83` | 4,710,000.00 USD | 4,830.00 USD | 0.00 USD | `+31.82%` | `828.00` |
| `Live` | `Short` | `5.84` | 4,720,000.00 USD | 6,670.00 USD | 0.00 USD | `+32.05%` | `1,141.30` |
| `Live` | `Short` | `5.86` | 4,720,000.00 USD | 370.62 USD | 0.00 USD | `+32.27%` | `63.30` |
| `Live` | `Short` | `5.87` | 4,720,000.00 USD | 604.10 USD | 0.00 USD | `+32.50%` | `103.00` |
| `Live` | `Short` | `5.88` | 4,720,000.00 USD | 190.67 USD | 0.00 USD | `+32.95%` | `32.40` |
| `Live` | `Short` | `5.89` | 4,810,000.00 USD | 89,540.00 USD | 0.00 USD | `+33.18%` | `15,189.10` |
| `Live` | `Short` | `5.92` | 4,810,000.00 USD | 189.28 USD | 0.00 USD | `+33.63%` | `32.00` |
| `Live` | `Short` | `5.93` | 4,810,000.00 USD | 670.06 USD | 0.00 USD | `+34.08%` | `112.90` |
| `Live` | `Short` | `5.95` | 4,810,000.00 USD | 1,400.00 USD | 0.00 USD | `+34.30%` | `234.80` |
| `Live` | `Short` | `5.99` | 4,810,000.00 USD | 131.67 USD | 0.00 USD | `+35.21%` | `22.00` |
| `Live` | `Short` | `6.01` | 4,810,000.00 USD | 6,350.00 USD | 0.00 USD | `+35.89%` | `1,055.10` |
| `Live` | `Short` | `6.03` | 4,970,000.00 USD | 151,910.00 USD | 0.00 USD | `+36.11%` | `25,213.10` |
| `Live` | `Short` | `6.04` | 4,970,000.00 USD | 1,870.00 USD | 0.00 USD | `+36.56%` | `310.00` |
| `Live` | `Short` | `6.07` | 4,970,000.00 USD | 740.54 USD | 0.00 USD | `+37.02%` | `122.10` |
| `Live` | `Short` | `6.08` | 4,980,000.00 USD | 13,760.00 USD | 0.00 USD | `+37.47%` | `2,262.10` |
| `Live` | `Short` | `6.09` | 5,020,000.00 USD | 37,510.00 USD | 0.00 USD | `+37.69%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 5,030,000.00 USD | 12,520.00 USD | 0.00 USD | `+37.92%` | `2,050.10` |
| `Live` | `Short` | `6.12` | 6,180,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+38.37%` | `188,000.00` |
| `Live` | `Short` | `6.13` | 6,210,000.00 USD | 24,160.00 USD | 0.00 USD | `+38.60%` | `3,938.70` |
| `Live` | `Short` | `6.20` | 6,540,000.00 USD | 331,450.00 USD | 0.00 USD | `+39.95%` | `53,503.40` |
| `Live` | `Short` | `6.25` | 6,550,000.00 USD | 7,610.00 USD | 0.00 USD | `+41.08%` | `1,218.90` |
| `Live` | `Short` | `6.25` | 6,550,000.00 USD | 439.10 USD | 0.00 USD | `+41.31%` | `70.20` |
| `Live` | `Short` | `6.32` | 6,550,000.00 USD | 310.70 USD | 0.00 USD | `+42.66%` | `49.20` |
| `Live` | `Short` | `6.33` | 6,550,000.00 USD | 1,670.00 USD | 0.00 USD | `+42.89%` | `264.70` |
| `Live` | `Short` | `6.33` | 8,390,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+43.12%` | `290,288.20` |
| `Live` | `Short` | `6.34` | 8,390,000.00 USD | 214.46 USD | 0.00 USD | `+43.34%` | `33.80` |
| `Live` | `Short` | `6.37` | 8,390,000.00 USD | 113.93 USD | 0.00 USD | `+43.79%` | `17.90` |
| `Live` | `Short` | `6.38` | 8,390,000.00 USD | 808.35 USD | 0.00 USD | `+44.02%` | `126.80` |
| `Live` | `Short` | `6.38` | 8,480,000.00 USD | 87,350.00 USD | 0.00 USD | `+44.24%` | `13,679.90` |
| `Live` | `Short` | `6.41` | 8,480,000.00 USD | 3,780.00 USD | 0.00 USD | `+44.70%` | `590.10` |
| `Live` | `Short` | `6.42` | 8,480,000.00 USD | 943.65 USD | 0.00 USD | `+44.92%` | `147.10` |
| `Live` | `Short` | `6.42` | 8,480,000.00 USD | 346.95 USD | 0.00 USD | `+45.15%` | `54.00` |
| `Live` | `Short` | `6.43` | 9,070,000.00 USD | 584,470.00 USD | 0.00 USD | `+45.37%` | `90,827.50` |
| `Live` | `Short` | `6.45` | 9,070,000.00 USD | 5,270.00 USD | 0.00 USD | `+45.60%` | `818.40` |
| `Live` | `Short` | `6.46` | 9,080,000.00 USD | 7,660.00 USD | 0.00 USD | `+45.83%` | `1,186.40` |
| `Live` | `Short` | `6.46` | 9,080,000.00 USD | 1,940.00 USD | 0.00 USD | `+46.05%` | `300.00` |
| `Live` | `Short` | `6.47` | 9,080,000.00 USD | 109.43 USD | 0.00 USD | `+46.28%` | `16.90` |
| `Live` | `Short` | `6.51` | 9,080,000.00 USD | 536.84 USD | 0.00 USD | `+47.18%` | `82.40` |
| `Live` | `Short` | `6.54` | 9,080,000.00 USD | 326.75 USD | 0.00 USD | `+47.63%` | `50.00` |
| `Live` | `Short` | `6.54` | 9,080,000.00 USD | 697.04 USD | 0.00 USD | `+47.86%` | `106.50` |
| `Live` | `Short` | `6.57` | 9,160,000.00 USD | 78,780.00 USD | 0.00 USD | `+48.31%` | `12,000.00` |
| `Live` | `Short` | `6.59` | 9,180,000.00 USD | 14,680.00 USD | 0.00 USD | `+48.99%` | `2,226.20` |
| `Live` | `Short` | `6.61` | 9,190,000.00 USD | 14,780.00 USD | 0.00 USD | `+49.21%` | `2,237.40` |
| `Live` | `Short` | `6.66` | 9,200,000.00 USD | 7,230.00 USD | 0.00 USD | `+50.34%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 9,200,000.00 USD | 1,370.00 USD | 0.00 USD | `+50.57%` | `205.90` |
| `Live` | `Short` | `6.67` | 9,210,000.00 USD | 10,930.00 USD | 0.00 USD | `+50.80%` | `1,636.90` |
| `Live` | `Short` | `6.71` | 9,230,000.00 USD | 15,540.00 USD | 0.00 USD | `+51.70%` | `2,314.50` |
| `Live` | `Short` | `6.72` | 9,340,000.00 USD | 117,610.00 USD | 0.00 USD | `+51.93%` | `17,488.80` |
| `Live` | `Short` | `6.75` | 10,590,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+52.60%` | `184,501.00` |
| `Live` | `Short` | `6.79` | 10,630,000.00 USD | 40,180.00 USD | 0.00 USD | `+53.51%` | `5,912.60` |
| `Live` | `Short` | `6.80` | 10,630,000.00 USD | 471.59 USD | 0.00 USD | `+53.73%` | `69.30` |
| `Live` | `Short` | `6.84` | 10,650,000.00 USD | 15,860.00 USD | 0.00 USD | `+54.64%` | `2,317.20` |
| `Live` | `Short` | `6.87` | 11,050,000.00 USD | 401,150.00 USD | 0.00 USD | `+55.09%` | `58,434.60` |
| `Live` | `Short` | `6.91` | 11,050,000.00 USD | 189.89 USD | 0.00 USD | `+55.99%` | `27.50` |
| `Live` | `Short` | `6.92` | 11,060,000.00 USD | 6,920.00 USD | 0.00 USD | `+56.44%` | `1,000.00` |
| `Live` | `Short` | `6.93` | 11,120,000.00 USD | 61,000.00 USD | 0.00 USD | `+56.67%` | `8,796.10` |
| `Live` | `Short` | `6.99` | 11,120,000.00 USD | 664.27 USD | 0.00 USD | `+57.80%` | `95.10` |
| `Live` | `Short` | `7.03` | 11,160,000.00 USD | 46,430.00 USD | 0.00 USD | `+58.70%` | `6,609.30` |
| `Live` | `Short` | `7.08` | 11,170,000.00 USD | 1,370.00 USD | 0.00 USD | `+60.06%` | `193.30` |
| `Live` | `Short` | `7.21` | 11,180,000.00 USD | 13,560.00 USD | 0.00 USD | `+63.00%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 20,850,000.00 USD | 9,670,000.00 USD | 0.00 USD | `+63.45%` | `1,336,785.40` |
| `Live` | `Short` | `7.25` | 20,850,000.00 USD | 264.81 USD | 0.00 USD | `+63.90%` | `36.50` |
| `Live` | `Short` | `7.28` | 20,860,000.00 USD | 6,670.00 USD | 0.00 USD | `+64.35%` | `917.00` |
| `Live` | `Short` | `7.33` | 20,860,000.00 USD | 1,320.00 USD | 0.00 USD | `+65.71%` | `180.00` |
| `Live` | `Short` | `7.41` | 20,860,000.00 USD | 154.76 USD | 0.00 USD | `+67.29%` | `20.90` |
| `Live` | `Short` | `7.46` | 20,860,000.00 USD | 1,420.00 USD | 0.00 USD | `+68.42%` | `191.10` |
| `Live` | `Short` | `7.46` | 20,970,000.00 USD | 106,570.00 USD | 0.00 USD | `+68.64%` | `14,276.50` |
| `Live` | `Short` | `7.49` | 20,970,000.00 USD | 480.54 USD | 0.00 USD | `+69.10%` | `64.20` |
| `Live` | `Short` | `7.50` | 28,770,000.00 USD | 7,800,000.00 USD | 0.00 USD | `+69.55%` | `1,039,604.60` |
| `Live` | `Short` | `7.53` | 28,890,000.00 USD | 124,660.00 USD | 0.00 USD | `+70.00%` | `16,565.90` |
| `Live` | `Short` | `7.63` | 28,910,000.00 USD | 19,210.00 USD | 0.00 USD | `+72.48%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 28,910,000.00 USD | 360.25 USD | 0.00 USD | `+73.16%` | `47.00` |
| `Live` | `Short` | `7.68` | 28,930,000.00 USD | 18,040.00 USD | 0.00 USD | `+73.61%` | `2,347.20` |
| `Live` | `Short` | `7.74` | 28,960,000.00 USD | 25,930.00 USD | 0.00 USD | `+74.74%` | `3,352.30` |
| `Live` | `Short` | `7.75` | 28,960,000.00 USD | 629.67 USD | 0.00 USD | `+74.97%` | `81.30` |
| `Live` | `Short` | `7.79` | 28,990,000.00 USD | 34,830.00 USD | 0.00 USD | `+75.87%` | `4,474.30` |
| `Live` | `Short` | `7.83` | 28,990,000.00 USD | 821.11 USD | 0.00 USD | `+77.00%` | `104.80` |
| `Live` | `Short` | `7.87` | 29,000,000.00 USD | 2,980.00 USD | 0.00 USD | `+77.68%` | `378.70` |
| `Live` | `Short` | `7.91` | 29,330,000.00 USD | 333,210.00 USD | 0.00 USD | `+78.58%` | `42,151.20` |
| `Live` | `Short` | `7.95` | 29,340,000.00 USD | 6,120.00 USD | 0.00 USD | `+79.49%` | `769.80` |
| `Live` | `Short` | `7.96` | 29,360,000.00 USD | 27,810.00 USD | 0.00 USD | `+79.71%` | `3,496.50` |
| `Live` | `Short` | `7.96` | 29,500,000.00 USD | 134,240.00 USD | 0.00 USD | `+79.94%` | `16,854.30` |
| `Live` | `Short` | `7.99` | 29,500,000.00 USD | 354.53 USD | 0.00 USD | `+80.39%` | `44.40` |
| `Live` | `Short` | `8.03` | 29,930,000.00 USD | 435,420.00 USD | 0.00 USD | `+81.29%` | `54,257.40` |
| `Live` | `Short` | `8.04` | 30,860,000.00 USD | 926,980.00 USD | 0.00 USD | `+81.52%` | `115,368.10` |
| `Live` | `Short` | `8.05` | 31,020,000.00 USD | 161,100.00 USD | 0.00 USD | `+81.97%` | `20,000.00` |
| `Live` | `Short` | `8.06` | 31,020,000.00 USD | 797.63 USD | 0.00 USD | `+82.20%` | `98.90` |
| `Live` | `Short` | `8.10` | 31,020,000.00 USD | 153.00 USD | 0.00 USD | `+82.88%` | `18.90` |
| `Live` | `Short` | `8.14` | 31,430,000.00 USD | 410,070.00 USD | 0.00 USD | `+84.01%` | `50,346.40` |
| `Live` | `Short` | `8.18` | 32,170,000.00 USD | 735,750.00 USD | 0.00 USD | `+84.68%` | `90,000.00` |
| `Live` | `Short` | `8.22` | 32,170,000.00 USD | 103.64 USD | 0.00 USD | `+85.81%` | `12.60` |
| `Live` | `Short` | `8.26` | 32,170,000.00 USD | 3,590.00 USD | 0.00 USD | `+86.49%` | `434.40` |
| `Live` | `Short` | `8.37` | 33,270,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+88.98%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 33,270,000.00 USD | 577.04 USD | 0.00 USD | `+89.20%` | `68.90` |
| `Live` | `Short` | `8.41` | 33,270,000.00 USD | 285.27 USD | 0.00 USD | `+90.11%` | `33.90` |
| `Live` | `Short` | `8.46` | 33,270,000.00 USD | 236.74 USD | 0.00 USD | `+91.01%` | `28.00` |
| `Live` | `Short` | `8.48` | 33,280,000.00 USD | 3,850.00 USD | 0.00 USD | `+91.69%` | `454.00` |
| `Live` | `Short` | `8.49` | 33,280,000.00 USD | 594.65 USD | 0.00 USD | `+91.91%` | `70.00` |
| `Live` | `Short` | `8.51` | 33,300,000.00 USD | 25,510.00 USD | 0.00 USD | `+92.14%` | `3,000.00` |
| `Live` | `Short` | `8.53` | 33,300,000.00 USD | 578.85 USD | 0.00 USD | `+92.59%` | `67.90` |
| `Live` | `Short` | `8.54` | 33,310,000.00 USD | 1,010.00 USD | 0.00 USD | `+92.82%` | `118.80` |
| `Live` | `Short` | `8.54` | 33,310,000.00 USD | 4,950.00 USD | 0.00 USD | `+93.04%` | `579.60` |
| `Live` | `Short` | `8.55` | 33,330,000.00 USD | 18,350.00 USD | 0.00 USD | `+93.27%` | `2,144.60` |
| `Live` | `Short` | `8.57` | 33,330,000.00 USD | 774.32 USD | 0.00 USD | `+93.72%` | `90.30` |
| `Live` | `Short` | `8.61` | 33,350,000.00 USD | 16,300.00 USD | 0.00 USD | `+94.40%` | `1,894.30` |
| `Live` | `Short` | `8.66` | 33,350,000.00 USD | 8,530.00 USD | 0.00 USD | `+95.75%` | `984.60` |
| `Live` | `Short` | `8.68` | 33,800,000.00 USD | 450,210.00 USD | 0.00 USD | `+95.98%` | `51,897.10` |
| `Live` | `Short` | `8.72` | 35,690,000.00 USD | 1,880,000.00 USD | 0.00 USD | `+97.11%` | `215,700.00` |
| `Live` | `Short` | `8.78` | 35,690,000.00 USD | 1,270.00 USD | 0.00 USD | `+98.24%` | `145.00` |
| `Live` | `Short` | `8.84` | 35,710,000.00 USD | 19,980.00 USD | 0.00 USD | `+99.59%` | `2,261.80` |
| `Live` | `Short` | `8.85` | 35,710,000.00 USD | 6,380.00 USD | 0.00 USD | `+99.82%` | `721.60` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,420,000.00 USD | 0.00 USD | 585.51 USD | `-77.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,420,000.00 USD | 0.00 USD | 331.54 USD | `-69.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,420,000.00 USD | 0.00 USD | 345.25 USD | `-69.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,420,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,410,000.00 USD | 0.00 USD | 997.29 USD | `-68.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,410,000.00 USD | 0.00 USD | 139.83 USD | `-65.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,410,000.00 USD | 0.00 USD | 113.28 USD | `-65.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,410,000.00 USD | 0.00 USD | 4,000.00 USD | `-65.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,410,000.00 USD | 0.00 USD | 324.22 USD | `-64.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,410,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,400,000.00 USD | 0.00 USD | 739.67 USD | `-63.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,400,000.00 USD | 0.00 USD | 1,740.00 USD | `-63.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,400,000.00 USD | 0.00 USD | 669.02 USD | `-61.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,400,000.00 USD | 0.00 USD | 105.88 USD | `-61.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,400,000.00 USD | 0.00 USD | 172.50 USD | `-61.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,400,000.00 USD | 0.00 USD | 10,650.00 USD | `-59.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,390,000.00 USD | 0.00 USD | 722.00 USD | `-59.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,390,000.00 USD | 0.00 USD | 259.00 USD | `-59.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,390,000.00 USD | 0.00 USD | 103.84 USD | `-58.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,390,000.00 USD | 0.00 USD | 109.00 USD | `-58.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,390,000.00 USD | 0.00 USD | 222.19 USD | `-57.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,390,000.00 USD | 0.00 USD | 10,280.00 USD | `-57.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,380,000.00 USD | 0.00 USD | 558.36 USD | `-56.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,380,000.00 USD | 0.00 USD | 1,520.00 USD | `-56.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,380,000.00 USD | 0.00 USD | 222.14 USD | `-56.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,380,000.00 USD | 0.00 USD | 279.50 USD | `-56.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,370,000.00 USD | 0.00 USD | 197.50 USD | `-55.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,370,000.00 USD | 0.00 USD | 935.66 USD | `-54.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,370,000.00 USD | 0.00 USD | 18,860.00 USD | `-54.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,350,000.00 USD | 0.00 USD | 3,020.00 USD | `-54.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,350,000.00 USD | 0.00 USD | 214.52 USD | `-53.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,350,000.00 USD | 0.00 USD | 1,200.00 USD | `-53.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,350,000.00 USD | 0.00 USD | 578.41 USD | `-53.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,350,000.00 USD | 0.00 USD | 18,070.00 USD | `-52.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,330,000.00 USD | 0.00 USD | 13,980.00 USD | `-52.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,320,000.00 USD | 0.00 USD | 107.23 USD | `-52.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,320,000.00 USD | 0.00 USD | 1,590.00 USD | `-51.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,320,000.00 USD | 0.00 USD | 6,970.00 USD | `-51.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,310,000.00 USD | 0.00 USD | 310.32 USD | `-51.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,310,000.00 USD | 0.00 USD | 1,170.00 USD | `-51.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,310,000.00 USD | 0.00 USD | 576.18 USD | `-50.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,310,000.00 USD | 0.00 USD | 295.67 USD | `-50.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,310,000.00 USD | 0.00 USD | 2,940.00 USD | `-50.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,300,000.00 USD | 0.00 USD | 812.68 USD | `-49.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,300,000.00 USD | 0.00 USD | 1,440.00 USD | `-49.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,300,000.00 USD | 0.00 USD | 490.14 USD | `-49.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,300,000.00 USD | 0.00 USD | 13,490.00 USD | `-49.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,290,000.00 USD | 0.00 USD | 478.06 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,290,000.00 USD | 0.00 USD | 540.88 USD | `-48.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,290,000.00 USD | 0.00 USD | 1,210.00 USD | `-48.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,290,000.00 USD | 0.00 USD | 759.76 USD | `-48.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,280,000.00 USD | 0.00 USD | 15,550.00 USD | `-48.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,270,000.00 USD | 0.00 USD | 3,690.00 USD | `-47.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,270,000.00 USD | 0.00 USD | 3,050.00 USD | `-47.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,260,000.00 USD | 0.00 USD | 467.00 USD | `-47.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,260,000.00 USD | 0.00 USD | 506.75 USD | `-47.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,260,000.00 USD | 0.00 USD | 214.27 USD | `-46.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,260,000.00 USD | 0.00 USD | 428.69 USD | `-46.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,260,000.00 USD | 0.00 USD | 322.45 USD | `-46.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,260,000.00 USD | 0.00 USD | 108.25 USD | `-45.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,260,000.00 USD | 0.00 USD | 3,850.00 USD | `-45.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,260,000.00 USD | 0.00 USD | 799.04 USD | `-45.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,260,000.00 USD | 0.00 USD | 6,830.00 USD | `-44.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,250,000.00 USD | 0.00 USD | 137.16 USD | `-44.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,250,000.00 USD | 0.00 USD | 504.41 USD | `-44.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,250,000.00 USD | 0.00 USD | 963.93 USD | `-43.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,250,000.00 USD | 0.00 USD | 13,880.00 USD | `-43.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,230,000.00 USD | 0.00 USD | 541.98 USD | `-43.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,230,000.00 USD | 0.00 USD | 108.75 USD | `-42.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,230,000.00 USD | 0.00 USD | 766.55 USD | `-42.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,230,000.00 USD | 0.00 USD | 1,010.00 USD | `-42.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,230,000.00 USD | 0.00 USD | 1,100.00 USD | `-41.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,230,000.00 USD | 0.00 USD | 100.04 USD | `-41.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 3,230,000.00 USD | 0.00 USD | 5,090.00 USD | `-40.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 3,220,000.00 USD | 0.00 USD | 226.57 USD | `-39.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,220,000.00 USD | 0.00 USD | 104.98 USD | `-39.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,220,000.00 USD | 0.00 USD | 329.33 USD | `-39.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 3,220,000.00 USD | 0.00 USD | 7,160.00 USD | `-38.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 3,220,000.00 USD | 0.00 USD | 107.21 USD | `-38.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,220,000.00 USD | 0.00 USD | 197.37 USD | `-37.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,220,000.00 USD | 0.00 USD | 8,390.00 USD | `-37.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,210,000.00 USD | 0.00 USD | 108.39 USD | `-37.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,210,000.00 USD | 0.00 USD | 1,270.00 USD | `-37.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,210,000.00 USD | 0.00 USD | 217.23 USD | `-37.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,210,000.00 USD | 0.00 USD | 437.98 USD | `-36.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 3,210,000.00 USD | 0.00 USD | 2,000.00 USD | `-36.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,200,000.00 USD | 0.00 USD | 8,250.00 USD | `-36.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,200,000.00 USD | 0.00 USD | 109.53 USD | `-35.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.87` | 3,200,000.00 USD | 0.00 USD | 1,810.00 USD | `-35.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,190,000.00 USD | 0.00 USD | 437.00 USD | `-35.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,190,000.00 USD | 0.00 USD | 746.06 USD | `-34.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,190,000.00 USD | 0.00 USD | 4,870.00 USD | `-34.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,190,000.00 USD | 0.00 USD | 696.98 USD | `-34.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,190,000.00 USD | 0.00 USD | 358.90 USD | `-33.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,190,000.00 USD | 0.00 USD | 15,370.00 USD | `-33.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,170,000.00 USD | 0.00 USD | 523.32 USD | `-33.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 3,170,000.00 USD | 0.00 USD | 2,330.00 USD | `-32.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 3,170,000.00 USD | 0.00 USD | 16,130.00 USD | `-32.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,150,000.00 USD | 0.00 USD | 1,020.00 USD | `-31.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,150,000.00 USD | 0.00 USD | 345.76 USD | `-31.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,150,000.00 USD | 0.00 USD | 214.57 USD | `-31.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,150,000.00 USD | 0.00 USD | 109.42 USD | `-30.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 3,150,000.00 USD | 0.00 USD | 721.58 USD | `-30.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 3,150,000.00 USD | 0.00 USD | 9,300.00 USD | `-29.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,140,000.00 USD | 0.00 USD | 104.69 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 3,140,000.00 USD | 0.00 USD | 315.69 USD | `-29.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,140,000.00 USD | 0.00 USD | 214.17 USD | `-28.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,140,000.00 USD | 0.00 USD | 641.10 USD | `-28.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,140,000.00 USD | 0.00 USD | 212.06 USD | `-28.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,140,000.00 USD | 0.00 USD | 1,030.00 USD | `-28.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 3,140,000.00 USD | 0.00 USD | 218.81 USD | `-28.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,140,000.00 USD | 0.00 USD | 31,570.00 USD | `-27.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,110,000.00 USD | 0.00 USD | 144.67 USD | `-27.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 3,110,000.00 USD | 0.00 USD | 21,850.00 USD | `-27.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 3,080,000.00 USD | 0.00 USD | 2,020.00 USD | `-26.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 3,080,000.00 USD | 0.00 USD | 104.81 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 3,080,000.00 USD | 0.00 USD | 1,150.00 USD | `-25.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 3,080,000.00 USD | 0.00 USD | 1,070.00 USD | `-25.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 3,080,000.00 USD | 0.00 USD | 15,820.00 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 3,060,000.00 USD | 0.00 USD | 240.67 USD | `-25.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 3,060,000.00 USD | 0.00 USD | 306.56 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 3,060,000.00 USD | 0.00 USD | 1,670.00 USD | `-24.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 3,060,000.00 USD | 0.00 USD | 505.76 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 3,060,000.00 USD | 0.00 USD | 73,220.00 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,990,000.00 USD | 0.00 USD | 12,850.00 USD | `-23.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,980,000.00 USD | 0.00 USD | 8,490.00 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,970,000.00 USD | 0.00 USD | 3,320.00 USD | `-23.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,960,000.00 USD | 0.00 USD | 25,250.00 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,940,000.00 USD | 0.00 USD | 506.22 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,940,000.00 USD | 0.00 USD | 171.75 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,940,000.00 USD | 0.00 USD | 2,550.00 USD | `-22.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,940,000.00 USD | 0.00 USD | 1,380.00 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,930,000.00 USD | 0.00 USD | 344.07 USD | `-21.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,930,000.00 USD | 0.00 USD | 1,950.00 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,930,000.00 USD | 0.00 USD | 112,400.00 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,820,000.00 USD | 0.00 USD | 17,360.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,800,000.00 USD | 0.00 USD | 2,030.00 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,800,000.00 USD | 0.00 USD | 12,040.00 USD | `-19.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,790,000.00 USD | 0.00 USD | 633.50 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,790,000.00 USD | 0.00 USD | 333.68 USD | `-19.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,790,000.00 USD | 0.00 USD | 72,860.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,710,000.00 USD | 0.00 USD | 179.25 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,710,000.00 USD | 0.00 USD | 643.50 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,710,000.00 USD | 0.00 USD | 1,870.00 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,710,000.00 USD | 0.00 USD | 632.99 USD | `-18.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,710,000.00 USD | 0.00 USD | 172.19 USD | `-18.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,710,000.00 USD | 0.00 USD | 13,400.00 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,700,000.00 USD | 0.00 USD | 179.33 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,700,000.00 USD | 0.00 USD | 3,900.00 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,690,000.00 USD | 0.00 USD | 174.09 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,690,000.00 USD | 0.00 USD | 546.47 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,690,000.00 USD | 0.00 USD | 4,370.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,690,000.00 USD | 0.00 USD | 18,110.00 USD | `-16.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,670,000.00 USD | 0.00 USD | 179.06 USD | `-16.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,670,000.00 USD | 0.00 USD | 1,030.00 USD | `-15.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,670,000.00 USD | 0.00 USD | 44,700.00 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,620,000.00 USD | 0.00 USD | 180.13 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,620,000.00 USD | 0.00 USD | 18,440.00 USD | `-15.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 2,610,000.00 USD | 0.00 USD | 6,850.00 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 2,600,000.00 USD | 0.00 USD | 3,940.00 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 2,590,000.00 USD | 0.00 USD | 359.57 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 2,590,000.00 USD | 0.00 USD | 1,900.00 USD | `-14.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 2,590,000.00 USD | 0.00 USD | 1,420.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 2,590,000.00 USD | 0.00 USD | 18,780.00 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 2,570,000.00 USD | 0.00 USD | 23,420.00 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 2,550,000.00 USD | 0.00 USD | 2,240.00 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 2,550,000.00 USD | 0.00 USD | 2,100.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 2,540,000.00 USD | 0.00 USD | 3,070.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 2,540,000.00 USD | 0.00 USD | 2,640.00 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 2,540,000.00 USD | 0.00 USD | 5,730.00 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 2,530,000.00 USD | 0.00 USD | 4,990.00 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 2,530,000.00 USD | 0.00 USD | 1,310.00 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 2,530,000.00 USD | 0.00 USD | 43,310.00 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 2,480,000.00 USD | 0.00 USD | 4,950.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 2,480,000.00 USD | 0.00 USD | 123.24 USD | `-11.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 2,480,000.00 USD | 0.00 USD | 1,420.00 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 2,480,000.00 USD | 0.00 USD | 187.78 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 2,480,000.00 USD | 0.00 USD | 14,250.00 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 2,460,000.00 USD | 0.00 USD | 1,960.00 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,460,000.00 USD | 0.00 USD | 4,570.00 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,460,000.00 USD | 0.00 USD | 3,950.00 USD | `-9.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,450,000.00 USD | 0.00 USD | 513.36 USD | `-9.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,450,000.00 USD | 0.00 USD | 248,860.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 2,200,000.00 USD | 0.00 USD | 5,440.00 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 2,200,000.00 USD | 0.00 USD | 4,510.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,190,000.00 USD | 0.00 USD | 2,100.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,190,000.00 USD | 0.00 USD | 7,600.00 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 2,180,000.00 USD | 0.00 USD | 1,850.00 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 2,180,000.00 USD | 0.00 USD | 485.36 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,180,000.00 USD | 0.00 USD | 504,780.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,680,000.00 USD | 0.00 USD | 74,820.00 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 1,600,000.00 USD | 0.00 USD | 1,370.00 USD | `-7.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 1,600,000.00 USD | 0.00 USD | 29,060.00 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 1,570,000.00 USD | 0.00 USD | 2,380.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 1,570,000.00 USD | 0.00 USD | 10,440.00 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 1,560,000.00 USD | 0.00 USD | 352,160.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 1,210,000.00 USD | 0.00 USD | 1,910.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 1,200,000.00 USD | 0.00 USD | 37,410.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,170,000.00 USD | 0.00 USD | 2,830.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,160,000.00 USD | 0.00 USD | 29,390.00 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 1,130,000.00 USD | 0.00 USD | 25,690.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 1,110,000.00 USD | 0.00 USD | 34,210.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,070,000.00 USD | 0.00 USD | 133,630.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 940,160.00 USD | 0.00 USD | 42,690.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 897,470.00 USD | 0.00 USD | 77,430.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 820,040.00 USD | 0.00 USD | 44,620.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 775,410.00 USD | 0.00 USD | 23,050.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 752,360.00 USD | 0.00 USD | 33,310.00 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 719,050.00 USD | 0.00 USD | 15,070.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 703,980.00 USD | 0.00 USD | 32,080.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 671,890.00 USD | 0.00 USD | 24,640.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 647,260.00 USD | 0.00 USD | 2,740.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 644,520.00 USD | 0.00 USD | 3,340.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 641,180.00 USD | 0.00 USD | 53,440.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 587,750.00 USD | 0.00 USD | 61,250.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 526,500.00 USD | 0.00 USD | 11,370.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 515,140.00 USD | 0.00 USD | 150,240.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.36` | 364,890.00 USD | 0.00 USD | 14,710.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.37` | 350,190.00 USD | 0.00 USD | 93,230.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 256,950.00 USD | 0.00 USD | 100.62 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 256,850.00 USD | 0.00 USD | 48,030.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.39` | 208,830.00 USD | 0.00 USD | 123,630.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.41` | 85,200.00 USD | 0.00 USD | 70,370.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 14,820.00 USD | 0.00 USD | 14,620.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 204.88 USD | 0.00 USD | 204.88 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 30,970.00 USD | 30,970.00 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 34,270.00 USD | 3,300.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 34,610.00 USD | 344.82 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 48,110.00 USD | 13,500.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 48,260.00 USD | 151.70 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 93,110.00 USD | 44,850.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 105,030.00 USD | 11,920.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 114,100.00 USD | 9,070.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 134,120.00 USD | 20,020.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 136,230.00 USD | 2,120.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 136,540.00 USD | 303.85 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 171,550.00 USD | 35,020.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 172,040.00 USD | 489.66 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 188,580.00 USD | 16,540.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 234,330.00 USD | 45,750.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 234,540.00 USD | 209.99 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 244,610.00 USD | 10,070.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 264,890.00 USD | 20,280.00 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 276,300.00 USD | 11,410.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 276,560.00 USD | 255.30 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 320,520.00 USD | 43,960.00 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 331,280.00 USD | 10,760.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 352,160.00 USD | 20,880.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 741,180.00 USD | 389,020.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 741,280.00 USD | 104.25 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 751,380.00 USD | 10,100.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 751,680.00 USD | 294.85 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,210,000.00 USD | 455,300.00 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,430,000.00 USD | 222,660.00 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,430,000.00 USD | 3,310.00 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,590,000.00 USD | 156,800.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,630,000.00 USD | 36,430.00 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,650,000.00 USD | 28,300.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,670,000.00 USD | 14,020.00 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,680,000.00 USD | 10,230.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,510,000.00 USD | 834,580.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,530,000.00 USD | 14,320.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 2,710,000.00 USD | 180,010.00 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,720,000.00 USD | 7,720.00 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,730,000.00 USD | 13,170.00 USD | 0.00 USD | `+9.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,730,000.00 USD | 1,210.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 2,740,000.00 USD | 14,560.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 2,790,000.00 USD | 42,050.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 2,810,000.00 USD | 23,780.00 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,820,000.00 USD | 10,850.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,830,000.00 USD | 9,810.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 2,830,000.00 USD | 4,060.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 2,950,000.00 USD | 120,040.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 2,960,000.00 USD | 529.84 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 2,970,000.00 USD | 12,520.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 2,980,000.00 USD | 11,650.00 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 2,980,000.00 USD | 114.72 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 2,980,000.00 USD | 205.63 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,030,000.00 USD | 47,350.00 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,030,000.00 USD | 187.06 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,120,000.00 USD | 95,210.00 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,130,000.00 USD | 11,390.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,180,000.00 USD | 48,530.00 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,210,000.00 USD | 26,480.00 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,210,000.00 USD | 5,140.00 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,390,000.00 USD | 179,120.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,390,000.00 USD | 219.46 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,440,000.00 USD | 50,950.00 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,450,000.00 USD | 3,550.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,540,000.00 USD | 90,150.00 USD | 0.00 USD | `+14.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,420,000.00 USD | 882,870.00 USD | 0.00 USD | `+14.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,420,000.00 USD | 547.20 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,470,000.00 USD | 51,790.00 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,490,000.00 USD | 15,350.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,490,000.00 USD | 113.26 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,500,000.00 USD | 10,650.00 USD | 0.00 USD | `+16.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,500,000.00 USD | 3,670.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,510,000.00 USD | 3,770.00 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,510,000.00 USD | 1,200.00 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,510,000.00 USD | 327.58 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,510,000.00 USD | 2,190.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,510,000.00 USD | 150.14 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,550,000.00 USD | 36,730.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,550,000.00 USD | 1,710.00 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,670,000.00 USD | 120,710.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,680,000.00 USD | 9,820.00 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,680,000.00 USD | 537.61 USD | 0.00 USD | `+18.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,210,000.00 USD | 530,070.00 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 5,220,000.00 USD | 5,540.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 5,220,000.00 USD | 589.22 USD | 0.00 USD | `+19.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,220,000.00 USD | 733.03 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,220,000.00 USD | 693.64 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,270,000.00 USD | 51,450.00 USD | 0.00 USD | `+19.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,270,000.00 USD | 381.09 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,270,000.00 USD | 961.16 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,270,000.00 USD | 1,570.00 USD | 0.00 USD | `+20.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,280,000.00 USD | 6,220.00 USD | 0.00 USD | `+20.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,390,000.00 USD | 108,270.00 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,390,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,390,000.00 USD | 438.60 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,400,000.00 USD | 6,080.00 USD | 0.00 USD | `+21.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,440,000.00 USD | 43,730.00 USD | 0.00 USD | `+21.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,550,000.00 USD | 115,240.00 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,550,000.00 USD | 425.62 USD | 0.00 USD | `+22.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,590,000.00 USD | 36,790.00 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 5,600,000.00 USD | 4,750.00 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,610,000.00 USD | 13,190.00 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,630,000.00 USD | 20,460.00 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,850,000.00 USD | 219,590.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,890,000.00 USD | 35,450.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,930,000.00 USD | 45,900.00 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,930,000.00 USD | 1,180.00 USD | 0.00 USD | `+24.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,070,000.00 USD | 134,580.00 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,070,000.00 USD | 5,600.00 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,120,000.00 USD | 45,680.00 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,140,000.00 USD | 18,790.00 USD | 0.00 USD | `+25.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,220,000.00 USD | 81,240.00 USD | 0.00 USD | `+25.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,270,000.00 USD | 49,440.00 USD | 0.00 USD | `+25.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,280,000.00 USD | 14,320.00 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,290,000.00 USD | 5,560.00 USD | 0.00 USD | `+25.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,310,000.00 USD | 20,540.00 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,310,000.00 USD | 384.94 USD | 0.00 USD | `+26.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,310,000.00 USD | 4,170.00 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,320,000.00 USD | 5,510.00 USD | 0.00 USD | `+27.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,320,000.00 USD | 581.53 USD | 0.00 USD | `+27.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,320,000.00 USD | 295.23 USD | 0.00 USD | `+27.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,320,000.00 USD | 3,290.00 USD | 0.00 USD | `+27.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,320,000.00 USD | 281.55 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,330,000.00 USD | 9,380.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,330,000.00 USD | 2,840.00 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,340,000.00 USD | 5,860.00 USD | 0.00 USD | `+28.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,460,000.00 USD | 116,400.00 USD | 0.00 USD | `+28.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,460,000.00 USD | 2,210.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,460,000.00 USD | 5,720.00 USD | 0.00 USD | `+29.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,490,000.00 USD | 24,730.00 USD | 0.00 USD | `+30.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,490,000.00 USD | 2,430.00 USD | 0.00 USD | `+30.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,490,000.00 USD | 286.94 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,500,000.00 USD | 2,900.00 USD | 0.00 USD | `+30.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,500,000.00 USD | 7,120.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,510,000.00 USD | 6,030.00 USD | 0.00 USD | `+31.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,510,000.00 USD | 1,970.00 USD | 0.00 USD | `+31.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,510,000.00 USD | 3,100.00 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,510,000.00 USD | 1,150.00 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,520,000.00 USD | 2,960.00 USD | 0.00 USD | `+32.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,520,000.00 USD | 3,450.00 USD | 0.00 USD | `+32.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,520,000.00 USD | 345.45 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.89` | 6,520,000.00 USD | 2,950.00 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,580,000.00 USD | 51,920.00 USD | 0.00 USD | `+33.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,580,000.00 USD | 1,790.00 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,580,000.00 USD | 1,400.00 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,710,000.00 USD | 133,540.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,730,000.00 USD | 19,370.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,740,000.00 USD | 5,620.00 USD | 0.00 USD | `+34.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,750,000.00 USD | 9,410.00 USD | 0.00 USD | `+34.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,870,000.00 USD | 119,710.00 USD | 0.00 USD | `+35.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,870,000.00 USD | 3,000.00 USD | 0.00 USD | `+35.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,000,000.00 USD | 133,160.00 USD | 0.00 USD | `+35.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,020,000.00 USD | 13,610.00 USD | 0.00 USD | `+35.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,100,000.00 USD | 87,250.00 USD | 0.00 USD | `+36.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,110,000.00 USD | 2,010.00 USD | 0.00 USD | `+36.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,110,000.00 USD | 3,300.00 USD | 0.00 USD | `+36.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,110,000.00 USD | 2,550.00 USD | 0.00 USD | `+36.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,110,000.00 USD | 425.76 USD | 0.00 USD | `+37.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,110,000.00 USD | 2,030.00 USD | 0.00 USD | `+37.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,120,000.00 USD | 4,120.00 USD | 0.00 USD | `+37.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,120,000.00 USD | 2,000.00 USD | 0.00 USD | `+37.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,180,000.00 USD | 61,050.00 USD | 0.00 USD | `+37.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,190,000.00 USD | 6,870.00 USD | 0.00 USD | `+38.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,190,000.00 USD | 1,200.00 USD | 0.00 USD | `+38.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,200,000.00 USD | 11,620.00 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,200,000.00 USD | 1,940.00 USD | 0.00 USD | `+39.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,200,000.00 USD | 1,410.00 USD | 0.00 USD | `+39.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,210,000.00 USD | 4,010.00 USD | 0.00 USD | `+39.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,210,000.00 USD | 3,960.00 USD | 0.00 USD | `+39.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,220,000.00 USD | 3,830.00 USD | 0.00 USD | `+39.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,280,000.00 USD | 66,850.00 USD | 0.00 USD | `+40.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,290,000.00 USD | 1,890.00 USD | 0.00 USD | `+40.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,290,000.00 USD | 195.46 USD | 0.00 USD | `+40.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,290,000.00 USD | 7,480.00 USD | 0.00 USD | `+40.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,300,000.00 USD | 3,670.00 USD | 0.00 USD | `+41.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,300,000.00 USD | 3,680.00 USD | 0.00 USD | `+42.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,310,000.00 USD | 7,370.00 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,310,000.00 USD | 412.37 USD | 0.00 USD | `+42.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,310,000.00 USD | 602.77 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,310,000.00 USD | 449.79 USD | 0.00 USD | `+43.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,310,000.00 USD | 2,810.00 USD | 0.00 USD | `+43.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,320,000.00 USD | 3,560.00 USD | 0.00 USD | `+44.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,320,000.00 USD | 3,230.00 USD | 0.00 USD | `+44.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,320,000.00 USD | 5,120.00 USD | 0.00 USD | `+44.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,320,000.00 USD | 613.26 USD | 0.00 USD | `+45.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.49` | 7,330,000.00 USD | 2,080.00 USD | 0.00 USD | `+46.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,330,000.00 USD | 1,310.00 USD | 0.00 USD | `+46.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,370,000.00 USD | 43,090.00 USD | 0.00 USD | `+46.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,370,000.00 USD | 234.54 USD | 0.00 USD | `+47.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,390,000.00 USD | 14,070.00 USD | 0.00 USD | `+47.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,390,000.00 USD | 1,630.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,390,000.00 USD | 2,390.00 USD | 0.00 USD | `+49.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,390,000.00 USD | 1,620.00 USD | 0.00 USD | `+49.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,390,000.00 USD | 1,970.00 USD | 0.00 USD | `+49.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,400,000.00 USD | 3,220.00 USD | 0.00 USD | `+50.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.66` | 7,400,000.00 USD | 1,950.00 USD | 0.00 USD | `+50.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,400,000.00 USD | 450.55 USD | 0.00 USD | `+50.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,400,000.00 USD | 3,060.00 USD | 0.00 USD | `+50.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,400,000.00 USD | 1,930.00 USD | 0.00 USD | `+51.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,410,000.00 USD | 3,070.00 USD | 0.00 USD | `+51.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,410,000.00 USD | 1,920.00 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,410,000.00 USD | 3,120.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,410,000.00 USD | 1,550.00 USD | 0.00 USD | `+52.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,420,000.00 USD | 3,080.00 USD | 0.00 USD | `+53.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,420,000.00 USD | 647.56 USD | 0.00 USD | `+53.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,420,000.00 USD | 1,420.00 USD | 0.00 USD | `+53.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,420,000.00 USD | 2,130.00 USD | 0.00 USD | `+53.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,420,000.00 USD | 3,140.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,420,000.00 USD | 342.25 USD | 0.00 USD | `+54.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,430,000.00 USD | 1,830.00 USD | 0.00 USD | `+54.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,430,000.00 USD | 2,990.00 USD | 0.00 USD | `+55.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,430,000.00 USD | 2,970.00 USD | 0.00 USD | `+55.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,430,000.00 USD | 391.51 USD | 0.00 USD | `+55.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,430,000.00 USD | 504.21 USD | 0.00 USD | `+56.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,430,000.00 USD | 166.00 USD | 0.00 USD | `+57.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,440,000.00 USD | 4,190.00 USD | 0.00 USD | `+57.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,450,000.00 USD | 15,610.00 USD | 0.00 USD | `+58.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,450,000.00 USD | 1,750.00 USD | 0.00 USD | `+58.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,460,000.00 USD | 2,860.00 USD | 0.00 USD | `+59.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 7,460,000.00 USD | 236.31 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 7,460,000.00 USD | 1,840.00 USD | 0.00 USD | `+60.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,460,000.00 USD | 264.31 USD | 0.00 USD | `+60.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,460,000.00 USD | 599.34 USD | 0.00 USD | `+61.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,460,000.00 USD | 193.19 USD | 0.00 USD | `+61.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,460,000.00 USD | 3,950.00 USD | 0.00 USD | `+62.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,470,000.00 USD | 1,940.00 USD | 0.00 USD | `+63.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.22` | 7,470,000.00 USD | 1,770.00 USD | 0.00 USD | `+63.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,630,000.00 USD | 160,550.00 USD | 0.00 USD | `+63.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,630,000.00 USD | 1,750.00 USD | 0.00 USD | `+64.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,630,000.00 USD | 731.50 USD | 0.00 USD | `+65.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,630,000.00 USD | 1,730.00 USD | 0.00 USD | `+65.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,630,000.00 USD | 1,710.00 USD | 0.00 USD | `+66.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,640,000.00 USD | 7,870.00 USD | 0.00 USD | `+66.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,640,000.00 USD | 630.05 USD | 0.00 USD | `+67.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,650,000.00 USD | 2,610.00 USD | 0.00 USD | `+67.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,650,000.00 USD | 7,900.00 USD | 0.00 USD | `+69.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,660,000.00 USD | 1,620.00 USD | 0.00 USD | `+70.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,660,000.00 USD | 4,640.00 USD | 0.00 USD | `+71.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,660,000.00 USD | 371.88 USD | 0.00 USD | `+71.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,660,000.00 USD | 2,510.00 USD | 0.00 USD | `+72.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,660,000.00 USD | 380.68 USD | 0.00 USD | `+73.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,660,000.00 USD | 133.12 USD | 0.00 USD | `+73.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,660,000.00 USD | 1,490.00 USD | 0.00 USD | `+75.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,670,000.00 USD | 1,470.00 USD | 0.00 USD | `+75.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,680,000.00 USD | 11,170.00 USD | 0.00 USD | `+76.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,710,000.00 USD | 34,360.00 USD | 0.00 USD | `+76.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,710,000.00 USD | 399.35 USD | 0.00 USD | `+76.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,710,000.00 USD | 100.29 USD | 0.00 USD | `+77.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 7,710,000.00 USD | 1,550.00 USD | 0.00 USD | `+77.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,720,000.00 USD | 10,610.00 USD | 0.00 USD | `+79.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,720,000.00 USD | 309.43 USD | 0.00 USD | `+80.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,860,000.00 USD | 134,600.00 USD | 0.00 USD | `+80.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,940,000.00 USD | 81,310.00 USD | 0.00 USD | `+81.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 7,940,000.00 USD | 1,390.00 USD | 0.00 USD | `+83.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,940,000.00 USD | 216.90 USD | 0.00 USD | `+84.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,940,000.00 USD | 738.45 USD | 0.00 USD | `+85.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 7,940,000.00 USD | 1,350.00 USD | 0.00 USD | `+88.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 8,000,000.00 USD | 56,000.00 USD | 0.00 USD | `+89.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 8,000,000.00 USD | 1,260.00 USD | 0.00 USD | `+89.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 8,100,000.00 USD | 103,010.00 USD | 0.00 USD | `+89.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 8,110,000.00 USD | 1,330.00 USD | 0.00 USD | `+90.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 8,110,000.00 USD | 721.22 USD | 0.00 USD | `+91.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 8,110,000.00 USD | 2,010.00 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 8,110,000.00 USD | 596.33 USD | 0.00 USD | `+95.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 8,110,000.00 USD | 3,670.00 USD | 0.00 USD | `+95.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 8,120,000.00 USD | 5,270.00 USD | 0.00 USD | `+98.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 8,120,000.00 USD | 1,600.00 USD | 0.00 USD | `+98.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 8,120,000.00 USD | 3,430.00 USD | 0.00 USD | `+98.92%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.88` | 31,950,000.00 USD | 0.00 USD | 31,950,000.00 USD | 161,060.00 USD | 8,890.00 USD | 131,700.00 USD |
| `7D` | `3.89` | 31,650,000.00 USD | 0.00 USD | 31,650,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,220.00 USD |
| `7D` | `3.90` | 31,600,000.00 USD | 0.00 USD | 31,600,000.00 USD | 92,100.00 USD | 28,250.00 USD | 49,490.00 USD |
| `7D` | `3.91` | 31,430,000.00 USD | 0.00 USD | 31,430,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD |
| `7D` | `3.92` | 31,350,000.00 USD | 0.00 USD | 31,350,000.00 USD | 90,780.00 USD | 41,330.00 USD | 80,150.00 USD |
| `1D` | `3.93` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 123,490.00 USD | 39,240.00 USD | 32,250.00 USD |
| `7D` | `3.93` | 31,140,000.00 USD | 0.00 USD | 31,140,000.00 USD | 51,660.00 USD | 20,780.00 USD | 50,110.00 USD |
| `1D` | `3.94` | 19,040,000.00 USD | 0.00 USD | 19,040,000.00 USD | 0.00 USD | 3,080.00 USD | 16,960.00 USD |
| `7D` | `3.94` | 31,020,000.00 USD | 0.00 USD | 31,020,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,320.00 USD |
| `1D` | `3.95` | 19,020,000.00 USD | 0.00 USD | 19,020,000.00 USD | 12,850.00 USD | 5,610.00 USD | 58.68 USD |
| `7D` | `3.95` | 30,780,000.00 USD | 0.00 USD | 30,780,000.00 USD | 8,490.00 USD | 26,060.00 USD | 696.53 USD |
| `1D` | `3.96` | 19,010,000.00 USD | 0.00 USD | 19,010,000.00 USD | 23,520.00 USD | 29,270.00 USD | 34,850.00 USD |
| `7D` | `3.96` | 30,740,000.00 USD | 0.00 USD | 30,740,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,370.00 USD |
| `1D` | `3.97` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 143,510.00 USD | 52,430.00 USD | 53,060.00 USD |
| `7D` | `3.97` | 30,530,000.00 USD | 0.00 USD | 30,530,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD |
| `1D` | `3.98` | 18,670,000.00 USD | 0.00 USD | 18,670,000.00 USD | 46,870.00 USD | 30,290.00 USD | 10,070.00 USD |
| `7D` | `3.98` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,840.00 USD |
| `1D` | `3.99` | 18,580,000.00 USD | 0.00 USD | 18,580,000.00 USD | 93,820.00 USD | 12,310.00 USD | 47,600.00 USD |
| `7D` | `3.99` | 29,720,000.00 USD | 0.00 USD | 29,720,000.00 USD | 63,200.00 USD | 82,870.00 USD | 101,260.00 USD |
| `1D` | `4.00` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 35,430.00 USD | 7,330.00 USD | 19,160.00 USD |
| `7D` | `4.00` | 29,470,000.00 USD | 0.00 USD | 29,470,000.00 USD | 317,210.00 USD | 105,220.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 18,370,000.00 USD | 0.00 USD | 18,370,000.00 USD | 109,160.00 USD | 56,050.00 USD | 73,710.00 USD |
| `7D` | `4.01` | 28,880,000.00 USD | 0.00 USD | 28,880,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,560.00 USD |
| `1D` | `4.02` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 60,540.00 USD | 20,960.00 USD | 75,230.00 USD |
| `7D` | `4.02` | 27,970,000.00 USD | 0.00 USD | 27,970,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD |
| `1D` | `4.03` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 23,550.00 USD | 40,450.00 USD | 34,830.00 USD |
| `7D` | `4.03` | 27,400,000.00 USD | 0.00 USD | 27,400,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD |
| `1D` | `4.04` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 28,720.00 USD | 32,610.00 USD | 127,750.00 USD |
| `7D` | `4.04` | 26,960,000.00 USD | 0.00 USD | 26,960,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD |
| `1D` | `4.05` | 17,680,000.00 USD | 0.00 USD | 17,680,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,200.00 USD |
| `7D` | `4.05` | 26,670,000.00 USD | 0.00 USD | 26,670,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,910.00 USD |
| `1D` | `4.06` | 17,580,000.00 USD | 0.00 USD | 17,580,000.00 USD | 56,470.00 USD | 0.00 USD | 22,940.00 USD |
| `7D` | `4.06` | 26,330,000.00 USD | 0.00 USD | 26,330,000.00 USD | 198,550.00 USD | 45,470.00 USD | 125,170.00 USD |
| `1D` | `4.07` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 3,220.00 USD | 15,020.00 USD | 22,800.00 USD |
| `7D` | `4.07` | 25,960,000.00 USD | 0.00 USD | 25,960,000.00 USD | 183,890.00 USD | 35,750.00 USD | 41,640.00 USD |
| `1D` | `4.08` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,540.00 USD |
| `7D` | `4.08` | 25,700,000.00 USD | 0.00 USD | 25,700,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD |
| `1D` | `4.09` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 10,540.00 USD | 6,980.00 USD | 1,150.00 USD |
| `7D` | `4.09` | 25,400,000.00 USD | 0.00 USD | 25,400,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,250.00 USD |
| `1D` | `4.10` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,330.00 USD |
| `7D` | `4.10` | 25,190,000.00 USD | 0.00 USD | 25,190,000.00 USD | 158,760.00 USD | 118,310.00 USD | 347,450.00 USD |
| `1D` | `4.11` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 22,520.00 USD | 18,800.00 USD | 13,730.00 USD |
| `7D` | `4.11` | 24,570,000.00 USD | 0.00 USD | 24,570,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD |
| `1D` | `4.12` | 17,250,000.00 USD | 0.00 USD | 17,250,000.00 USD | 4,430.00 USD | 41,500.00 USD | 135,050.00 USD |
| `7D` | `4.12` | 24,370,000.00 USD | 0.00 USD | 24,370,000.00 USD | 97,300.00 USD | 48,940.00 USD | 342,160.00 USD |
| `1D` | `4.13` | 17,070,000.00 USD | 0.00 USD | 17,070,000.00 USD | 39,380.00 USD | 55,060.00 USD | 23,580.00 USD |
| `7D` | `4.13` | 23,880,000.00 USD | 0.00 USD | 23,880,000.00 USD | 293,300.00 USD | 79,100.00 USD | 108,000.00 USD |
| `1D` | `4.14` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 194,940.00 USD | 36,950.00 USD | 142,710.00 USD |
| `7D` | `4.14` | 23,400,000.00 USD | 0.00 USD | 23,400,000.00 USD | 374,290.00 USD | 57,440.00 USD | 218,300.00 USD |
| `1D` | `4.15` | 16,570,000.00 USD | 0.00 USD | 16,570,000.00 USD | 201,620.00 USD | 84,150.00 USD | 79,190.00 USD |
| `7D` | `4.15` | 22,750,000.00 USD | 0.00 USD | 22,750,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,920.00 USD |
| `1D` | `4.16` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 63,250.00 USD | 99,580.00 USD | 99,840.00 USD |
| `7D` | `4.16` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 310,530.00 USD | 192,570.00 USD | 174,580.00 USD |
| `1D` | `4.17` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 44,430.00 USD | 104,170.00 USD | 89,370.00 USD |
| `7D` | `4.17` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,940.00 USD |
| `1D` | `4.18` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 120,410.00 USD | 30,730.00 USD | 53,670.00 USD |
| `7D` | `4.18` | 20,740,000.00 USD | 0.00 USD | 20,740,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD |
| `1D` | `4.19` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 288,170.00 USD | 79,350.00 USD | 145,490.00 USD |
| `7D` | `4.19` | 20,210,000.00 USD | 0.00 USD | 20,210,000.00 USD | 215,210.00 USD | 113,960.00 USD | 671,560.00 USD |
| `1D` | `4.20` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 64,030.00 USD | 162,810.00 USD | 466,050.00 USD |
| `7D` | `4.20` | 19,210,000.00 USD | 0.00 USD | 19,210,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,970.00 USD |
| `1D` | `4.21` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 51,570.00 USD | 146,670.00 USD | 1,180.00 USD |
| `7D` | `4.21` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 321,000.00 USD | 149,940.00 USD | 119,650.00 USD |
| `1D` | `4.22` | 14,100,000.00 USD | 0.00 USD | 14,100,000.00 USD | 528,380.00 USD | 141,000.00 USD | 406,680.00 USD |
| `7D` | `4.22` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 853,600.00 USD | 161,970.00 USD | 786,170.00 USD |
| `1D` | `4.23` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 859,820.00 USD | 357,760.00 USD | 375,410.00 USD |
| `7D` | `4.23` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 739,630.00 USD |
| `1D` | `4.24` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 281,350.00 USD | 220,350.00 USD | 227,130.00 USD |
| `7D` | `4.24` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,750.00 USD |
| `1D` | `4.25` | 10,700,000.00 USD | 0.00 USD | 10,700,000.00 USD | 394,150.00 USD | 246,700.00 USD | 414,300.00 USD |
| `7D` | `4.25` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 350,470.00 USD | 433,770.00 USD | 647,490.00 USD |
| `1D` | `4.26` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 425,040.00 USD | 114,720.00 USD | 281,230.00 USD |
| `7D` | `4.26` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 626,730.00 USD | 199,830.00 USD | 464,730.00 USD |
| `7D` | `4.27` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD |
| `1D` | `4.28` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 320,200.00 USD | 294,950.00 USD | 214,690.00 USD |
| `7D` | `4.28` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 842,270.00 USD | 497,680.00 USD | 1,110,000.00 USD |
| `1D` | `4.29` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 289,680.00 USD | 37,190.00 USD | 247,550.00 USD |
| `7D` | `4.29` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 9,100.00 USD | 46,530.00 USD | 361.22 USD |
| `1D` | `4.30` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 293,470.00 USD | 217,150.00 USD | 56,580.00 USD |
| `7D` | `4.30` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 3,500.00 USD | 90,090.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 300,730.00 USD | 222,320.00 USD | 499,620.00 USD |
| `7D` | `4.31` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 88,750.00 USD | 0.00 USD | 43,250.00 USD |
| `1D` | `4.32` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 597,550.00 USD | 156,850.00 USD | 193,250.00 USD |
| `7D` | `4.32` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 169,820.00 USD | 158,570.00 USD | 78,540.00 USD |
| `1D` | `4.33` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 373,930.00 USD | 85,110.00 USD | 202,810.00 USD |
| `7D` | `4.33` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 112,660.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 269,670.00 USD | 138,220.00 USD | 406,710.00 USD |
| `7D` | `4.34` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 75,930.00 USD | 161,050.00 USD | 134,560.00 USD |
| `1D` | `4.35` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 298,330.00 USD | 83,060.00 USD | 144,020.00 USD |
| `7D` | `4.35` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 362,610.00 USD | 39,140.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 82,150.00 USD | 51,640.00 USD | 118,020.00 USD |
| `7D` | `4.36` | 709,050.00 USD | 0.00 USD | 709,050.00 USD | 5,210.00 USD | 0.00 USD | 86,450.00 USD |
| `1D` | `4.37` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 52,120.00 USD | 66,510.00 USD | 82,620.00 USD |
| `1D` | `4.38` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 171,480.00 USD | 81,750.00 USD | 476,590.00 USD |
| `7D` | `4.38` | 617,390.00 USD | 0.00 USD | 617,390.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 406,130.00 USD | 0.00 USD | 406,130.00 USD | 206,130.00 USD | 0.00 USD | 199,760.00 USD |
| `7D` | `4.39` | 214,070.00 USD | 0.00 USD | 214,070.00 USD | 0.00 USD | 62,850.00 USD | 151,220.00 USD |
| `1D` | `4.40` | 238.22 USD | 0.00 USD | 238.22 USD | 0.00 USD | 0.00 USD | 238.22 USD |
| `7D` | `4.40` | 400,190.00 USD | 400,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD |
| `7D` | `4.40` | 800,380.00 USD | 800,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD |
| `1D` | `4.41` | 72,150.00 USD | 72,150.00 USD | 0.00 USD | 1,720.00 USD | 0.00 USD | 70,430.00 USD |
| `1D` | `4.41` | 144,300.00 USD | 144,300.00 USD | 0.00 USD | 1,720.00 USD | 0.00 USD | 70,430.00 USD |
| `7D` | `4.41` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 270,480.00 USD |
| `7D` | `4.42` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 175,990.00 USD |
| `7D` | `4.43` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 46,230.00 USD | 69,230.00 USD |
| `1D` | `4.44` | 667,200.00 USD | 667,200.00 USD | 0.00 USD | 0.00 USD | 282,030.00 USD | 240,870.00 USD |
| `7D` | `4.44` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 70,120.00 USD |
| `1D` | `4.45` | 702,260.00 USD | 702,260.00 USD | 0.00 USD | 0.00 USD | 34,890.00 USD | 171.14 USD |
| `1D` | `4.46` | 702,330.00 USD | 702,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76.64 USD |
| `7D` | `4.46` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD |
| `7D` | `4.47` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 132,630.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 758,550.00 USD | 758,550.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD | 0.00 USD |
| `1D` | `4.49` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 49,360.00 USD | 113,460.00 USD | 119,730.00 USD |
| `7D` | `4.49` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 295,140.00 USD | 65,710.00 USD | 52.10 USD |
| `7D` | `4.50` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 169,820.00 USD | 164,910.00 USD | 0.00 USD |
| `1D` | `4.51` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 162,900.00 USD | 282,880.00 USD | 248,730.00 USD |
| `1D` | `4.52` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 189,070.00 USD | 59,620.00 USD | 182,210.00 USD |
| `7D` | `4.52` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 487,010.00 USD | 0.00 USD | 278,430.00 USD |
| `7D` | `4.53` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD |
| `1D` | `4.54` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 150,600.00 USD | 702,410.00 USD |
| `7D` | `4.54` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 315,220.00 USD |
| `1D` | `4.56` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 79,110.00 USD | 24,450.00 USD | 288,540.00 USD |
| `7D` | `4.56` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 135,640.00 USD | 70,180.00 USD | 67,290.00 USD |
| `7D` | `4.57` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 198,050.00 USD | 0.00 USD | 151,220.00 USD |
| `1D` | `4.58` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 380,450.00 USD | 43,090.00 USD | 840,430.00 USD |
| `7D` | `4.58` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 794,410.00 USD | 75,460.00 USD | 94.84 USD |
| `7D` | `4.59` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 759,320.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 49,450.00 USD |
| `7D` | `4.60` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD |
| `1D` | `4.61` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 59,150.00 USD |
| `7D` | `4.61` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 703.64 USD |
| `1D` | `4.62` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 1,010.00 USD |
| `7D` | `4.62` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 1,710.00 USD |
| `1D` | `4.63` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 500.90 USD | 0.00 USD | 54.94 USD |
| `7D` | `4.63` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 332,720.00 USD | 11,270.00 USD | 61,930.00 USD |
| `7D` | `4.64` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 500,990.00 USD | 0.00 USD | 612.20 USD |
| `1D` | `4.65` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 370,110.00 USD | 52,020.00 USD | 587,340.00 USD |
| `7D` | `4.65` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 649.48 USD |
| `1D` | `4.66` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 281,290.00 USD | 304,540.00 USD | 379,520.00 USD |
| `7D` | `4.66` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 144,860.00 USD | 0.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 378,010.00 USD |
| `7D` | `4.67` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 345,490.00 USD | 62,440.00 USD | 175,570.00 USD |
| `7D` | `4.68` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 237,460.00 USD |
| `7D` | `4.69` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,540.00 USD |
| `7D` | `4.70` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 365,040.00 USD | 278,020.00 USD | 316,630.00 USD |
| `7D` | `4.71` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `1D` | `4.72` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 5,240.00 USD | 187,480.00 USD | 103,670.00 USD |
| `7D` | `4.72` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 61,330.00 USD | 37,010.00 USD | 61,410.00 USD |
| `7D` | `4.73` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 59,270.00 USD | 0.00 USD | 894.74 USD |
| `1D` | `4.74` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 242,820.00 USD | 172,000.00 USD | 294,540.00 USD |
| `7D` | `4.74` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `1D` | `4.75` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 202,480.00 USD | 188,800.00 USD | 270,350.00 USD |
| `7D` | `4.75` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,640.00 USD |
| `1D` | `4.76` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 35,470.00 USD | 78,750.00 USD | 247,670.00 USD |
| `7D` | `4.76` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 946,180.00 USD | 46,890.00 USD | 272,560.00 USD |
| `1D` | `4.77` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 113,030.00 USD | 177,160.00 USD | 105,170.00 USD |
| `7D` | `4.77` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 40,580.00 USD | 20,000.00 USD | 113,990.00 USD |
| `7D` | `4.78` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 683,730.00 USD | 584,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 294,950.00 USD | 103,580.00 USD | 132,950.00 USD |
| `7D` | `4.79` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 71,960.00 USD |
| `1D` | `4.80` | 17,190,000.00 USD | 17,190,000.00 USD | 0.00 USD | 355,770.00 USD | 315,950.00 USD | 174,090.00 USD |
| `7D` | `4.80` | 18,200,000.00 USD | 18,200,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 184,590.00 USD | 120,180.00 USD | 127,930.00 USD |
| `7D` | `4.81` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 274,470.00 USD | 214,840.00 USD | 407,470.00 USD |
| `7D` | `4.82` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 212,270.00 USD | 70,050.00 USD | 290,470.00 USD |
| `7D` | `4.83` | 23,240,000.00 USD | 23,240,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `1D` | `4.84` | 19,330,000.00 USD | 19,330,000.00 USD | 0.00 USD | 73,450.00 USD | 89,230.00 USD | 77,650.00 USD |
| `7D` | `4.84` | 23,730,000.00 USD | 23,730,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `1D` | `4.85` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 230,330.00 USD | 153,010.00 USD | 210,730.00 USD |
| `7D` | `4.85` | 25,750,000.00 USD | 25,750,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `1D` | `4.86` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 94,860.00 USD | 69,470.00 USD | 278,460.00 USD |
| `7D` | `4.86` | 27,160,000.00 USD | 27,160,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `1D` | `4.87` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 181,750.00 USD | 113,470.00 USD | 59,340.00 USD |
| `7D` | `4.87` | 28,230,000.00 USD | 28,230,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `1D` | `4.88` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 36,680.00 USD | 7,330.00 USD | 194,030.00 USD |
| `7D` | `4.88` | 29,950,000.00 USD | 29,950,000.00 USD | 0.00 USD | 449,970.00 USD | 480,980.00 USD | 792,630.00 USD |
| `1D` | `4.89` | 21,160,000.00 USD | 21,160,000.00 USD | 0.00 USD | 113,710.00 USD | 35,450.00 USD | 50,500.00 USD |
| `7D` | `4.89` | 30,540,000.00 USD | 30,540,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `1D` | `4.90` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 81,280.00 USD | 112,960.00 USD | 228,550.00 USD |
| `7D` | `4.90` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `1D` | `4.91` | 21,920,000.00 USD | 21,920,000.00 USD | 0.00 USD | 180,050.00 USD | 85,510.00 USD | 74,840.00 USD |
| `7D` | `4.91` | 33,110,000.00 USD | 33,110,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `1D` | `4.92` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 186,460.00 USD | 89,190.00 USD | 257,130.00 USD |
| `7D` | `4.92` | 34,840,000.00 USD | 34,840,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `1D` | `4.93` | 22,810,000.00 USD | 22,810,000.00 USD | 0.00 USD | 117,390.00 USD | 72,670.00 USD | 164,530.00 USD |
| `7D` | `4.93` | 36,400,000.00 USD | 36,400,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `1D` | `4.94` | 23,100,000.00 USD | 23,100,000.00 USD | 0.00 USD | 49,980.00 USD | 65,310.00 USD | 171,370.00 USD |
| `7D` | `4.94` | 37,700,000.00 USD | 37,700,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD |
| `1D` | `4.95` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 104,460.00 USD | 12,690.00 USD | 46,530.00 USD |
| `7D` | `4.95` | 39,000,000.00 USD | 39,000,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `1D` | `4.96` | 23,400,000.00 USD | 23,400,000.00 USD | 0.00 USD | 93,850.00 USD | 21,750.00 USD | 23,140.00 USD |
| `7D` | `4.96` | 40,240,000.00 USD | 40,240,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `1D` | `4.97` | 23,520,000.00 USD | 23,520,000.00 USD | 0.00 USD | 6,540.00 USD | 15,020.00 USD | 100,590.00 USD |
| `7D` | `4.97` | 40,620,000.00 USD | 40,620,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `1D` | `4.98` | 23,560,000.00 USD | 23,560,000.00 USD | 0.00 USD | 3,880.00 USD | 18,060.00 USD | 15,540.00 USD |
| `7D` | `4.98` | 41,180,000.00 USD | 41,180,000.00 USD | 0.00 USD | 197,950.00 USD | 88,580.00 USD | 270,990.00 USD |
| `1D` | `4.99` | 23,650,000.00 USD | 23,650,000.00 USD | 0.00 USD | 1,730.00 USD | 6,980.00 USD | 82,150.00 USD |
| `7D` | `4.99` | 41,530,000.00 USD | 41,530,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `1D` | `5.00` | 23,650,000.00 USD | 23,650,000.00 USD | 0.00 USD | 718.70 USD | 0.00 USD | 6.68 USD |
| `7D` | `5.00` | 42,230,000.00 USD | 42,230,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `1D` | `5.01` | 23,670,000.00 USD | 23,670,000.00 USD | 0.00 USD | 14,360.00 USD | 10,080.00 USD | 45.10 USD |
| `7D` | `5.01` | 44,390,000.00 USD | 44,390,000.00 USD | 0.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD |
| `1D` | `5.02` | 23,750,000.00 USD | 23,750,000.00 USD | 0.00 USD | 13,280.00 USD | 0.00 USD | 58,950.00 USD |
| `7D` | `5.02` | 45,870,000.00 USD | 45,870,000.00 USD | 0.00 USD | 821,860.00 USD | 337,720.00 USD | 321,220.00 USD |
| `1D` | `5.03` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 14,530.00 USD | 18,800.00 USD | 12,380.00 USD |
| `7D` | `5.03` | 47,550,000.00 USD | 47,550,000.00 USD | 0.00 USD | 564,790.00 USD | 231,540.00 USD | 886,200.00 USD |
| `1D` | `5.04` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 248.51 USD |
| `7D` | `5.04` | 48,990,000.00 USD | 48,990,000.00 USD | 0.00 USD | 305,260.00 USD | 253,720.00 USD | 879,760.00 USD |
| `1D` | `5.05` | 23,870,000.00 USD | 23,870,000.00 USD | 0.00 USD | 34,080.00 USD | 14,380.00 USD | 22,960.00 USD |
| `7D` | `5.05` | 51,000,000.00 USD | 51,000,000.00 USD | 0.00 USD | 901,830.00 USD | 367,860.00 USD | 735,210.00 USD |
| `1D` | `5.06` | 23,900,000.00 USD | 23,900,000.00 USD | 0.00 USD | 0.00 USD | 8,000.00 USD | 23,250.00 USD |
| `7D` | `5.06` | 51,700,000.00 USD | 51,700,000.00 USD | 0.00 USD | 92,480.00 USD | 193,330.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 52,900,000.00 USD | 52,900,000.00 USD | 0.00 USD | 358,750.00 USD | 166,480.00 USD | 673,800.00 USD |
| `7D` | `5.08` | 53,560,000.00 USD | 53,560,000.00 USD | 0.00 USD | 204,140.00 USD | 308,520.00 USD | 149,330.00 USD |
| `7D` | `5.09` | 54,420,000.00 USD | 54,420,000.00 USD | 0.00 USD | 105,390.00 USD | 121,050.00 USD | 633,580.00 USD |
| `7D` | `5.10` | 54,980,000.00 USD | 54,980,000.00 USD | 0.00 USD | 291,110.00 USD | 68,980.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 55,740,000.00 USD | 55,740,000.00 USD | 0.00 USD | 369,260.00 USD | 92,720.00 USD | 291,780.00 USD |
| `7D` | `5.12` | 56,320,000.00 USD | 56,320,000.00 USD | 0.00 USD | 303,840.00 USD | 166,880.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 262,920.00 USD | 100,640.00 USD | 484,250.00 USD |
| `7D` | `5.14` | 57,790,000.00 USD | 57,790,000.00 USD | 0.00 USD | 140,950.00 USD | 104,910.00 USD | 369,400.00 USD |
| `7D` | `5.15` | 58,620,000.00 USD | 58,620,000.00 USD | 0.00 USD | 309,440.00 USD | 132,710.00 USD | 392,170.00 USD |
| `7D` | `5.16` | 59,150,000.00 USD | 59,150,000.00 USD | 0.00 USD | 51,850.00 USD | 126,880.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 59,840,000.00 USD | 59,840,000.00 USD | 0.00 USD | 280,710.00 USD | 99,740.00 USD | 309,950.00 USD |
| `7D` | `5.18` | 60,160,000.00 USD | 60,160,000.00 USD | 0.00 USD | 67,600.00 USD | 133,610.00 USD | 124,390.00 USD |
| `7D` | `5.19` | 60,550,000.00 USD | 60,550,000.00 USD | 0.00 USD | 72,580.00 USD | 47,800.00 USD | 261,940.00 USD |
| `7D` | `5.20` | 60,830,000.00 USD | 60,830,000.00 USD | 0.00 USD | 140,770.00 USD | 80,310.00 USD | 65,030.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.25B` | Total OI Tokens: `283,071,837.1 NEAR`
  * 1h OI Change: `-0.67%` | 4h OI Change: `-3.91%` | 24h OI Change: `-6.39%`
  * Exchange Breakdown: Binance=`242.16M` | Bybit=`168.40M` | OKX=`52.82M` | Hyperliquid=`255.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `45.85K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
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
| `15M` | `NEAR` | `68.09%` | `31.91%` | `2.13` | 3,720,000.00 USD |
| `15M` | `Binance` | `58.84%` | `41.16%` | `1.43` | 1,260,000.00 USD |
| `15M` | `OKX` | `82.08%` | `17.92%` | `4.58` | 631,560.00 USD |
| `15M` | `Bybit` | `76.78%` | `23.22%` | `3.31` | 432,570.00 USD |
| `15M` | `KuCoin` | `63.22%` | `36.78%` | `1.72` | 19,250.00 USD |
| `15M` | `Gate` | `69.83%` | `30.17%` | `2.31` | 31,940.00 USD |
| `15M` | `Bitget` | `82.32%` | `17.68%` | `4.66` | 108,180.00 USD |
| `15M` | `BingX` | `52.54%` | `47.46%` | `1.11` | 161,340.00 USD |
| `15M` | `MEXC` | `43.47%` | `56.53%` | `0.77` | 304,550.00 USD |
| `15M` | `Bitunix` | `70.06%` | `29.94%` | `2.34` | 129,580.00 USD |
| `15M` | `Hyperliquid` | `95.53%` | `4.47%` | `21.37` | 238,470.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.05%` | `49.95%` | `1.00` | 42,880.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `70.93%` | `29.07%` | `2.44` | 319,950.00 USD |
| `15M` | `HTX` | `0.66%` | `99.34%` | `0.01` | 3,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `92.94%` | `7.06%` | `13.16` | 35,280.00 USD |
| `15M` | `Aster` | `25.34%` | `74.66%` | `0.34` | 1,460.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `25.46%` | `74.54%` | `0.34` | 180.96 USD |
| `15M` | `Whale Positions` | `58.84%` | `41.16%` | `1.43` | 1,260,000.00 USD |
| `15M` | `Global Accounts` | `68.09%` | `31.91%` | `2.13` | 3,720,000.00 USD |
| `1H` | `NEAR` | `52.82%` | `47.18%` | `1.12` | 24,530,000.00 USD |
| `1H` | `Binance` | `51.13%` | `48.87%` | `1.05` | 9,460,000.00 USD |
| `1H` | `OKX` | `58.63%` | `41.37%` | `1.42` | 3,290,000.00 USD |
| `1H` | `Bybit` | `51.83%` | `48.17%` | `1.08` | 3,430,000.00 USD |
| `1H` | `KuCoin` | `58.93%` | `41.07%` | `1.43` | 495,330.00 USD |
| `1H` | `Gate` | `59.01%` | `40.99%` | `1.44` | 615,240.00 USD |
| `1H` | `Bitget` | `55.75%` | `44.25%` | `1.26` | 827,140.00 USD |
| `1H` | `BingX` | `47.4%` | `52.6%` | `0.90` | 1,620,000.00 USD |
| `1H` | `MEXC` | `46.39%` | `53.61%` | `0.87` | 1,900,000.00 USD |
| `1H` | `Bitunix` | `48.22%` | `51.78%` | `0.93` | 837,130.00 USD |
| `1H` | `Hyperliquid` | `44.54%` | `55.46%` | `0.80` | 438,470.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.76%` | `48.24%` | `1.07` | 162,320.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `69.42%` | `30.58%` | `2.27` | 1,110,000.00 USD |
| `1H` | `HTX` | `48.3%` | `51.7%` | `0.93` | 34,330.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `82.21%` | `17.79%` | `4.62` | 190,480.00 USD |
| `1H` | `Aster` | `13.11%` | `86.89%` | `0.15` | 102,960.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.75%` | `44.25%` | `1.26` | 9,320.00 USD |
| `1H` | `Whale Positions` | `51.13%` | `48.87%` | `1.05` | 9,460,000.00 USD |
| `1H` | `Global Accounts` | `52.82%` | `47.18%` | `1.12` | 24,530,000.00 USD |
| `4H` | `NEAR` | `47.08%` | `52.92%` | `0.89` | 138,730,000.00 USD |
| `4H` | `Binance` | `46.8%` | `53.2%` | `0.88` | 51,110,000.00 USD |
| `4H` | `OKX` | `43.32%` | `56.68%` | `0.76` | 21,010,000.00 USD |
| `4H` | `Bybit` | `46.96%` | `53.04%` | `0.89` | 17,570,000.00 USD |
| `4H` | `KuCoin` | `53.09%` | `46.91%` | `1.13` | 1,960,000.00 USD |
| `4H` | `Gate` | `53.79%` | `46.21%` | `1.16` | 3,880,000.00 USD |
| `4H` | `Bitget` | `51.69%` | `48.31%` | `1.07` | 6,400,000.00 USD |
| `4H` | `BingX` | `46.86%` | `53.14%` | `0.88` | 5,180,000.00 USD |
| `4H` | `MEXC` | `43.73%` | `56.27%` | `0.78` | 14,340,000.00 USD |
| `4H` | `Bitunix` | `53.02%` | `46.98%` | `1.13` | 5,020,000.00 USD |
| `4H` | `Hyperliquid` | `43.78%` | `56.22%` | `0.78` | 4,020,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `44.45%` | `55.55%` | `0.80` | 933,610.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `64.34%` | `35.66%` | `1.80` | 5,010,000.00 USD |
| `4H` | `HTX` | `45.8%` | `54.2%` | `0.85` | 177,250.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `37.58%` | `62.42%` | `0.60` | 1,620,000.00 USD |
| `4H` | `Aster` | `28.21%` | `71.79%` | `0.39` | 300,230.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.88%` | `61.12%` | `0.64` | 186,200.00 USD |
| `4H` | `Whale Positions` | `46.8%` | `53.2%` | `0.88` | 51,110,000.00 USD |
| `4H` | `Global Accounts` | `47.08%` | `52.92%` | `0.89` | 138,730,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4.57` | `4.58` | `4.57` | `4.60` | `4.56` | 7,120,500.63 USD | 2,702,175.30 USD | 4,418,325.32 USD | -1,716,150.02 USD | `-24.10%` | `2B / 10S` |
| `5:00 UTC` | `4.57` | `4.56` | `4.57` | `4.58` | `4.55` | 4,633,928.94 USD | 2,745,228.28 USD | 1,888,700.65 USD | 856,527.63 USD | `+18.48%` | `5B / 1S` |
| `0:00 UTC` | `4.56` | `4.53` | `4.56` | `4.58` | `4.48` | 11,435,880.79 USD | 4,658,038.22 USD | 6,777,842.57 USD | -2,119,804.34 USD | `-18.54%` | `11B / 24S` |
| `5:00 UTC` | `4.48` | `4.48` | `4.48` | `4.50` | `4.45` | 11,953,334.30 USD | 7,100,618.87 USD | 4,852,715.43 USD | 2,247,903.44 USD | `+18.81%` | `10B / 5S` |
| `0:00 UTC` | `4.50` | `4.49` | `4.50` | `4.51` | `4.48` | 5,580,209.64 USD | 2,611,428.00 USD | 2,968,781.64 USD | -357,353.64 USD | `-6.40%` | `4B / 2S` |
| `5:00 UTC` | `4.48` | `4.47` | `4.48` | `4.50` | `4.45` | 3,346,103.47 USD | 1,895,415.61 USD | 1,450,687.86 USD | 444,727.76 USD | `+13.29%` | `4B / 3S` |
| `0:00 UTC` | `4.43` | `4.43` | `4.43` | `4.46` | `4.40` | 9,612,896.64 USD | 4,376,656.36 USD | 5,236,240.29 USD | -859,583.93 USD | `-8.94%` | `5B / 19S` |
| `5:00 UTC` | `4.44` | `4.42` | `4.44` | `4.45` | `4.39` | 7,755,029.11 USD | 3,981,690.96 USD | 3,773,338.14 USD | 208,352.82 USD | `+2.69%` | `13B / 5S` |
| `0:00 UTC` | `4.39` | `4.40` | `4.39` | `4.43` | `4.38` | 7,242,328.79 USD | 3,238,308.88 USD | 4,004,019.90 USD | -765,711.02 USD | `-10.57%` | `3B / 12S` |
| `5:00 UTC` | `4.40` | `4.40` | `4.40` | `4.41` | `4.39` | 937,135.77 USD | 596,282.62 USD | 340,853.15 USD | 255,429.47 USD | `+27.26%` | `4B / 0S` |

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
| `5m` | 145,970.00 USD | 490,200.00 USD | **`ACCUMULATION`** |
| `15m` | 256,880.00 USD | 1,200,000.00 USD | **`ACCUMULATION`** |
| `30m` | -502,510.00 USD | -923,230.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,650,000.00 USD | -2,130,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,340,000.00 USD | -3,860,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,270,000.00 USD | -11,360,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,020,000.00 USD | -14,960,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,300,000.00 USD | -12,250,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -3,770,000.00 USD | -8,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -16,640,000.00 USD | -64,360,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -70,690,000.00 USD | -102,100,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -238,640,000.00 USD | -662,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+145.97K` | 15m=`+256.88K` | 1h=`-2.65M` | 24h=`-16.64M`
* Futures Capital Netflows: 5m=`+490.20K` | 15m=`+1.20M` | 1h=`-2.13M` | 24h=`-64.36M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.37` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.27` (Risk Distance: `0.1030` pts)
  * +2.5R Take Profit: `4.63`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.62` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.72` (Risk Distance: `0.1030` pts)
  * +2.5R Take Profit: `4.36`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.45`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
