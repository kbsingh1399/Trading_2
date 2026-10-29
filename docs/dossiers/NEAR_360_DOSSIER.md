# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:06:25 IST` (`2026-10-29 20:36:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.29` | **Live Ask Quote**: `4.33` | **Mid Price**: `4.31`
- **Spread Points**: `31.00` | **Spread BPS**: `71.92 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.46` | VWAP Z-Score: `-1.20` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0505` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `34.81` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.75` | Lower -3.00σ Band: `4.16`
  * Upper +2.51σ Band: `4.70` | Lower -2.51σ Band: `4.21`
  * Upper +2.01σ Band: `4.66` | Lower -2.01σ Band: `4.26`
  * Upper +2.00σ Band: `4.65` | Lower -2.00σ Band: `4.26`
  * Upper +1.28σ Band: `4.58` | Lower -1.28σ Band: `4.33`
  * Upper +1.00σ Band: `4.56` | Lower -1.00σ Band: `4.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.39` | EMA-20=`4.43` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.45` (Slope: `+0.0000`) | EMA-100=`4.48`
  * Institutional Anchors: EMA-144=`4.50` | EMA-200=`4.51` (Slope: `-0.2875`) | EMA-233=`4.51`
- **Range Boundaries**: 24H High=`4.75` | 24H Low=`4.27` | Weekly High=`4.80` | Weekly Low=`4.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.54` (Distance: `-5.33%`)
  * Point of Control (POC) = `4.41` (Distance: `-2.42%`)
  * Value Area Low (VAL) = `4.29` (Distance: `+0.22%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.73` | POC=`4.68` | VAL=`4.61`
  * Prior Day Extremes: PDH=`4.80` | PDL=`4.53` | PDC=`4.71`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.62` | Weekly POC=`4.44` | Weekly VAL=`4.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.75` | Low=`4.39`
  * London Session (08:00-16:00 UTC): High=`4.50` | Low=`4.27`
  * New York Session (13:00-21:00 UTC): High=`4.67` | Low=`4.34`
  * Initial Balance (First Hour): IB High=`4.50` | IB Low=`4.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.29` - `4.33`
  * Optimal Trade Entry (OTE 0.705): `4.32`
  * Structural Invalidation Anchor (0.786): `4.34`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.36` | `4.37` | `4.34` | `4.35` | `355,683` | 1,547,645.33 USD | 126,733.00 USD | `+8.19%` | -26,922,914.39 USD | `+0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4.35` | `4.36` | `4.34` | `4.36` | `270,519` | 1,177,671.40 USD | 256,918.59 USD | `+21.82%` | -26,665,995.80 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.36` | `4.37` | `4.30` | `4.30` | `1,040,276` | 4,505,054.16 USD | -86,930.15 USD | `-1.93%` | -26,752,925.96 USD | `-0.33` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4.40` | `4.41` | `4.31` | `4.35` | `4,452,913` | 19,326,325.36 USD | -122,998.56 USD | `-0.64%` | -28,733,837.92 USD | `-0.10` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4.35` | `4.37` | `4.34` | `4.36` | `1,066,255` | 4,641,250.70 USD | 1,057,393.83 USD | `+22.78%` | -27,676,444.08 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.36` | `4.37` | `4.30` | `4.30` | `1,040,276` | 4,505,054.16 USD | -86,930.15 USD | `-1.93%` | -27,763,374.23 USD | `+0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.50` | `4.51` | `4.39` | `4.42` | `5,916,118` | 26,294,238.86 USD | -563,856.99 USD | `-2.14%` | -30,750,281.84 USD | `+0.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.42` | `4.43` | `4.38` | `4.40` | `4,517,639` | 19,883,976.65 USD | 1,294,805.24 USD | `+6.51%` | -29,455,476.60 USD | `+0.73` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4.40` | `4.41` | `4.30` | `4.30` | `6,559,444` | 28,472,630.23 USD | 847,465.12 USD | `+2.98%` | -28,608,011.48 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.30` | `4.30` | `6,730,338` | 29,207,349.64 USD | 441,335.96 USD | `+1.51%` | -27,885,929.35 USD | `+0.73` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -27,473,639.56 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -28,567,348.59 USD | `+1.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.30` | `4.30` | `6,730,338` | 29,207,349.64 USD | 441,335.96 USD | `+1.51%` | -27,885,929.35 USD | `+0.73` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`4.31`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:04:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `58` | `0x7737...bf66` | `LONG` | 24,581,887.99 USD | `5,640,376.30` | `2.35` | `4.30` | `0.9075` | 11,309,985.16 USD | `+46.01%` | `10X Cross` |
| `130` | `0xb581...6f4f` | `LONG` | 15,707,160.00 USD | `3,600,000.00` | `5.19` | `4.30` | `0.000000` | -2,985,875.22 USD | `-19.01%` | `4X Cross` |
| `216` | `0xdd53...2b13` | `SHORT` | 10,350,871.56 USD | `2,400,202.10` | `2.31` | `4.30` | `28.02` | -4,805,467.67 USD | `-46.43%` | `3X Cross` |
| `268` | `0x77ee...2902` | `LONG` | 8,978,689.14 USD | `2,063,023.10` | `1.93` | `4.30` | `0.2508` | 4,987,493.20 USD | `+55.55%` | `10X Cross` |
| `281` | `0xefe4...194b` | `SHORT` | 8,708,520.55 USD | `2,019,882.30` | `4.44` | `4.30` | `11.27` | 266,564.61 USD | `+3.06%` | `5X Cross` |
| `384` | `0xb83d...6e36` | `SHORT` | 6,287,317.17 USD | `1,445,759.10` | `5.19` | `4.30` | `95.45` | 1,222,131.77 USD | `+19.44%` | `3X Cross` |
| `405` | `0xb46b...538e` | `SHORT` | 5,737,652.40 USD | `1,336,000.00` | `4.33` | `4.30` | `7.37` | 47,211.66 USD | `+0.82%` | `10X Cross` |
| `429` | `0x9df2...c665` | `SHORT` | 5,432,732.25 USD | `1,265,000.00` | `2.03` | `4.30` | `27.77` | -2,866,049.91 USD | `-52.76%` | `10X Cross` |
| `434` | `0xb695...a92d` | `SHORT` | 5,319,876.31 USD | `1,233,422.90` | `4.57` | `4.30` | `27.39` | 320,860.60 USD | `+6.03%` | `10X Cross` |
| `471` | `0x60b0...991e` | `LONG` | 4,872,191.48 USD | `1,121,307.10` | `5.00` | `4.30` | `0.000000` | -729,232.95 USD | `-14.97%` | `10X Cross` |
| `485` | `0xcac1...26b3` | `SHORT` | 4,676,154.68 USD | `1,073,743.90` | `2.48` | `4.30` | `11.71` | -2,016,211.22 USD | `-43.12%` | `10X Cross` |
| `500` | `0x781e...96b7` | `SHORT` | 4,486,205.73 USD | `1,039,604.60` | `2.45` | `4.30` | `7.58` | -1,941,868.54 USD | `-43.29%` | `10X Cross` |
| `520` | `0xdf60...d3c7` | `LONG` | 4,345,000.00 USD | `1,000,000.00` | `4.70` | `4.30` | `3.91` | -354,277.29 USD | `-8.15%` | `8X Isolated` |
| `590` | `0x4cae...7c34` | `LONG` | 3,917,357.77 USD | `900,086.80` | `3.52` | `4.30` | `2.16` | 744,956.79 USD | `+19.02%` | `10X Cross` |
| `592` | `0x45d2...4029` | `SHORT` | 3,907,055.22 USD | `909,400.00` | `3.26` | `4.30` | `46.45` | -940,905.32 USD | `-24.08%` | `10X Cross` |
| `733` | `0x9aa5...58af` | `SHORT` | 3,154,295.83 USD | `723,977.10` | `4.78` | `4.30` | `15.12` | 305,337.36 USD | `+9.68%` | `10X Cross` |
| `811` | `0x005a...61fe` | `LONG` | 2,844,527.66 USD | `652,414.60` | `2.08` | `4.30` | `2.35` | 1,486,996.42 USD | `+52.28%` | `7X Cross` |
| `819` | `0xba5d...a352` | `SHORT` | 2,821,234.35 USD | `647,532.50` | `2.83` | `4.30` | `12.83` | -988,519.41 USD | `-35.04%` | `10X Cross` |
| `829` | `0xd1dd...9e85` | `SHORT` | 2,781,366.56 USD | `637,621.00` | `4.96` | `4.30` | `16.96` | 382,106.17 USD | `+13.74%` | `10X Cross` |
| `836` | `0x123d...3bff` | `SHORT` | 2,763,816.87 USD | `636,076.70` | `2.09` | `4.30` | `9.02` | -1,436,440.18 USD | `-51.97%` | `10X Cross` |
| `853` | `0xcf53...ee11` | `SHORT` | 2,677,472.95 USD | `621,598.40` | `5.07` | `4.30` | `24.58` | 474,697.30 USD | `+17.73%` | `10X Cross` |
| `950` | `0x5647...e7de` | `SHORT` | 2,381,115.54 USD | `545,864.50` | `4.69` | `4.30` | `12.82` | 177,475.91 USD | `+7.45%` | `10X Cross` |
| `972` | `0x590f...be1d` | `SHORT` | 2,318,506.65 USD | `539,012.10` | `4.41` | `4.30` | `4.54` | 55,987.74 USD | `+2.41%` | `10X Cross` |
| `981` | `0xbfc7...80b4` | `SHORT` | 2,307,141.90 USD | `531,000.00` | `2.01` | `4.30` | `13.16` | -1,241,942.51 USD | `-53.83%` | `10X Cross` |
| `1088` | `0xef96...9383` | `SHORT` | 2,048,947.69 USD | `476,034.50` | `4.50` | `4.30` | `12.75` | 94,534.03 USD | `+4.61%` | `10X Cross` |
| `1173` | `0xfc66...ca06` | `SHORT` | 1,941,168.81 USD | `450,994.10` | `4.59` | `4.30` | `79.87` | 130,307.30 USD | `+6.71%` | `10X Cross` |
| `1209` | `0x7fda...17d1` | `SHORT` | 1,873,140.55 USD | `435,472.30` | `4.83` | `4.30` | `91.21` | 228,443.87 USD | `+12.20%` | `10X Cross` |
| `1310` | `0xe097...d0fe` | `LONG` | 1,721,680.00 USD | `400,000.00` | `5.29` | `4.30` | `0.000000` | -395,107.30 USD | `-22.95%` | `10X Cross` |
| `1443` | `0x6e8f...4364` | `LONG` | 1,573,071.73 USD | `361,210.50` | `3.28` | `4.30` | `3.29` | 389,011.50 USD | `+24.73%` | `10X Cross` |
| `1458` | `0xdf95...7d72` | `SHORT` | 1,556,601.90 USD | `362,312.20` | `4.23` | `4.30` | `107.04` | -23,157.07 USD | `-1.49%` | `10X Cross` |
| `1484` | `0xcf67...eb24` | `LONG` | 1,527,365.00 USD | `350,000.00` | `1.98` | `4.30` | `1.17` | 835,747.12 USD | `+54.72%` | `10X Cross` |
| `1611` | `0xfc27...9d9d` | `SHORT` | 1,374,806.12 USD | `319,997.70` | `5.01` | `4.30` | `52.88` | 228,736.50 USD | `+16.64%` | `10X Cross` |
| `1717` | `0xe065...0f85` | `SHORT` | 1,261,234.68 USD | `290,227.90` | `2.81` | `4.30` | `6.39` | -444,490.43 USD | `-35.24%` | `10X Cross` |
| `1777` | `0x023a...2355` | `SHORT` | 1,191,225.11 USD | `277,374.20` | `4.59` | `4.30` | `33.37` | 82,179.17 USD | `+6.90%` | `10X Cross` |
| `1860` | `0xb69e...033a` | `LONG` | 1,121,414.77 USD | `257,081.40` | `4.61` | `4.30` | `2.84` | -62,640.09 USD | `-5.59%` | `10X Cross` |
| `1903` | `0xff43...d924` | `LONG` | 1,083,839.47 USD | `249,474.50` | `4.64` | `4.30` | `3.28` | -74,204.21 USD | `-6.85%` | `10X Isolated` |
| `1925` | `0x556f...03a9` | `LONG` | 1,066,048.51 USD | `248,409.30` | `4.32` | `4.30` | `1.86` | -8,257.39 USD | `-0.77%` | `5X Cross` |

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
  * 24H Horizon: Short MP=`4.54` (Vol: 539,200.00 USD, Dist: `+4.25%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--1.95%`)
  * 48H Horizon: Short MP=`4.53` (Vol: 539,200.00 USD, Dist: `+4.23%`) | Long MP=`4.24` (Vol: 596,900.00 USD, Dist: `--2.58%`)
  * 3D Horizon: Short MP=`4.83` (Vol: 541,200.00 USD, Dist: `+11.05%`) | Long MP=`4.24` (Vol: 689,000.00 USD, Dist: `--2.58%`)
  * 7D Horizon: Short MP=`4.41` (Vol: 793,100.00 USD, Dist: `+1.37%`) | Long MP=`4.23` (Vol: 1,400,000.00 USD, Dist: `--2.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8650` | 3,350.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 43,750.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 512.24 USD | 33,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,380.00 USD | 33,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 19,280.00 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 5,280,000.00 USD | 33,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 286.50 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 6,610.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 30,370.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 1,000.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 126.06 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 11,320.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 8,040.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 383,760.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 53,650.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 73,400.00 USD | 27,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 27,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 41,270.00 USD | 27,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 57,020.00 USD | 27,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 13,350.00 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 2,670.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 35,290.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 21,600.00 USD | 27,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 2,300.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 558.38 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 653.98 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 11,870.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 13,810.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 2,830.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 2,760.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 11,330.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 236.85 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 1,330.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 27,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 157.50 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 23,470.00 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 669.86 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 18,780.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 226.29 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 1,320.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,200.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 674.18 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 31,130.00 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 1,170.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 16,150.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 4,620.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 5,680.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 308.32 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 2,440.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,510.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 10,850.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 384.13 USD | 27,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 4,740.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,190.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 17,420.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 569.64 USD | 27,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 6,790.00 USD | 27,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,460.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 1,370.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 5,750.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 11,460.00 USD | 27,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 211.80 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 265,490.00 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 15,250.00 USD | 26,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 2,440.00 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 529.05 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 2,870.00 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 26,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,080.00 USD | 26,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 13,270.00 USD | 26,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 12,910.00 USD | 26,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 1,310.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,250.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 24,990.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 1,720,000.00 USD | 26,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 2,010.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 263.92 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 6,770.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 3,010.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 3,960.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 41,570.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 643.54 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 199,500.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 214,480.00 USD | 24,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 81,810.00 USD | 24,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 6,020.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 86,680.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 6,810.00 USD | 24,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 12,830.00 USD | 24,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 7,950.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,510.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 10,310.00 USD | 24,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 3,210.00 USD | 24,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 5,590.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 594.13 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 6,120.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 248.38 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 45,940.00 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,880.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 24,600.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 239.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 6,340.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 26,180.00 USD | 24,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 4,680.00 USD | 24,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 120,330.00 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 3,440.00 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 804.32 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 4,150.00 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,810.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 9,840.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 1,520,000.00 USD | 23,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 3,120.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 48,780.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,800.00 USD | 22,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 63,060.00 USD | 22,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 420,020.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 534.24 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 63,350.00 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 2,310.00 USD | 21,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 185,860.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 60,620.00 USD | 21,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 391,530.00 USD | 21,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 158,860.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 636,570.00 USD | 21,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 15,480.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 259,390.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 20,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,690.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,490.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 37,790.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 10,330.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 1,160.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 10,920.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 9,730.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 8,920.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 368.88 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 71,500.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 560.34 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 14,260.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 224.44 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 65,400.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 10,090.00 USD | 19,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 103,320.00 USD | 19,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,300.00 USD | 19,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 6,930.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 20,370.00 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 130,140.00 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 17,980.00 USD | 19,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 249,070.00 USD | 19,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 8,440.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,550.00 USD | 19,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 154.83 USD | 19,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 3,740.00 USD | 19,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 2,140.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,840.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 10,470.00 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 6,190.00 USD | 19,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 572.29 USD | 19,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 199,090.00 USD | 19,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,140.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 28,270.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,860.00 USD | 18,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 5,190.00 USD | 18,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 4,150.00 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 7,800.00 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,910.00 USD | 18,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 22,330.00 USD | 18,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 3,480.00 USD | 18,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 37,660.00 USD | 18,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 942.11 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 6,210.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 15,260.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 9,740.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 12,330.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 11,290.00 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 22,800.00 USD | 18,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 355,760.00 USD | 18,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 103,780.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 25,110.00 USD | 18,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 701,010.00 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 9,970.00 USD | 17,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 12,360.00 USD | 17,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,510.00 USD | 17,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 92,110.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 107,620.00 USD | 17,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 9,270.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 39,110.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 19,990.00 USD | 17,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,110.00 USD | 17,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 8,100.00 USD | 17,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 122,100.00 USD | 17,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 8,320.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 354.65 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 218,340.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 29,190.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 18,920.00 USD | 16,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 35,590.00 USD | 16,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 35,080.00 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 64,310.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 47,960.00 USD | 16,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 836,280.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 8,590.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,400,000.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 69,500.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 15,580.00 USD | 14,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 29,530.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 51,870.00 USD | 14,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 31,120.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 2,090.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 14,490.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 53,610.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 12,370.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 158,490.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 187,750.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 50,040.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 25,570.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 5,860.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 10,250.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 55,000.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 70,570.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 26,990.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 25,280.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 12,480.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 17,140.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 21,970.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 7,690.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 325,560.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 379,650.00 USD | 13,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 8,330.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 135,550.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 22,500.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 79,940.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 165,030.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 845.19 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 11,540.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 29,880.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 513,760.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 49,270.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 574,480.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 189,590.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 178,360.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 1,930.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 43,110.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 157,110.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 27,950.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 30,770.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 33,470.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 99,550.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 56,700.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 14,890.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 38,620.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 146,150.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 14,720.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 77,060.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 6,620.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 147,910.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 24,250.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 154,310.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.86` | 31,040,000.00 USD | 31,040,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 24,820.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 16,690,000.00 USD | 16,690,000.00 USD | 1,250.00 USD | 24,120.00 USD | 53,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 30,960,000.00 USD | 30,960,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 4,710.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 16,610,000.00 USD | 16,610,000.00 USD | 74,500.00 USD | 6,860.00 USD | 30,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 30,880,000.00 USD | 30,880,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 52,710.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 16,500,000.00 USD | 16,500,000.00 USD | 112,190.00 USD | 37,150.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 30,660,000.00 USD | 30,660,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 96,500.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 16,330,000.00 USD | 16,330,000.00 USD | 335.10 USD | 10,910.00 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 30,610,000.00 USD | 30,610,000.00 USD | 171,750.00 USD | 28,250.00 USD | 49,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 6,040.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 35,760.00 USD | 34,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 30,360,000.00 USD | 30,360,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,920,000.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 16,230,000.00 USD | 16,230,000.00 USD | 145,280.00 USD | 26,030.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 30,280,000.00 USD | 30,280,000.00 USD | 90,780.00 USD | 41,330.00 USD | 80,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 331,990.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 21,500.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 30,070,000.00 USD | 30,070,000.00 USD | 51,660.00 USD | 20,780.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 21,330.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 6,420.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 29,950,000.00 USD | 29,950,000.00 USD | 75,150.00 USD | 31,050.00 USD | 126,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 533,900.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 15,970,000.00 USD | 15,970,000.00 USD | 12,850.00 USD | 5,610.00 USD | 131.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 29,720,000.00 USD | 29,720,000.00 USD | 8,490.00 USD | 19,870.00 USD | 696.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 13,470.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 15,950,000.00 USD | 15,950,000.00 USD | 35,990.00 USD | 29,270.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 29,690,000.00 USD | 29,690,000.00 USD | 52,720.00 USD | 15,590.00 USD | 126,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 108,840.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 15,850,000.00 USD | 15,850,000.00 USD | 156,200.00 USD | 52,430.00 USD | 65,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 29,490,000.00 USD | 29,490,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 67,350.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 15,580,000.00 USD | 15,580,000.00 USD | 46,870.00 USD | 30,290.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 28,890,000.00 USD | 28,890,000.00 USD | 31,450.00 USD | 77,970.00 USD | 85,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 61,830.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 15,490,000.00 USD | 15,490,000.00 USD | 93,820.00 USD | 12,310.00 USD | 47,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 28,690,000.00 USD | 28,690,000.00 USD | 63,200.00 USD | 82,870.00 USD | 101,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 33,890.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 15,340,000.00 USD | 15,340,000.00 USD | 35,430.00 USD | 7,330.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 28,450,000.00 USD | 28,450,000.00 USD | 317,210.00 USD | 98,320.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 57,440.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 15,270,000.00 USD | 15,270,000.00 USD | 109,160.00 USD | 56,050.00 USD | 73,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 27,860,000.00 USD | 27,860,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 11,310.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 15,040,000.00 USD | 15,040,000.00 USD | 60,540.00 USD | 20,960.00 USD | 75,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 26,950,000.00 USD | 26,950,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 84,020.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 14,880,000.00 USD | 14,880,000.00 USD | 23,550.00 USD | 40,450.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 26,380,000.00 USD | 26,380,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 12,740.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 14,780,000.00 USD | 14,780,000.00 USD | 28,720.00 USD | 32,610.00 USD | 127,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 25,940,000.00 USD | 25,940,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 33,550.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 14,590,000.00 USD | 14,590,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 25,650,000.00 USD | 25,650,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 82,940.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 14,490,000.00 USD | 14,490,000.00 USD | 56,670.00 USD | 0.00 USD | 23,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 25,310,000.00 USD | 25,310,000.00 USD | 198,550.00 USD | 45,470.00 USD | 125,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 349,630.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 14,410,000.00 USD | 14,410,000.00 USD | 3,220.00 USD | 15,020.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 24,940,000.00 USD | 24,940,000.00 USD | 183,890.00 USD | 35,750.00 USD | 41,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 302,020.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 14,370,000.00 USD | 14,370,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 24,680,000.00 USD | 24,680,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 60,670.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 14,330,000.00 USD | 14,330,000.00 USD | 10,540.00 USD | 6,980.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 24,380,000.00 USD | 24,380,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 723,030.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 14,310,000.00 USD | 14,310,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 24,170,000.00 USD | 24,170,000.00 USD | 158,760.00 USD | 118,310.00 USD | 347,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 124,860.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 14,210,000.00 USD | 14,210,000.00 USD | 22,930.00 USD | 18,800.00 USD | 13,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 23,550,000.00 USD | 23,550,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 253,880.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 14,150,000.00 USD | 14,150,000.00 USD | 4,430.00 USD | 41,500.00 USD | 134,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 23,350,000.00 USD | 23,350,000.00 USD | 97,300.00 USD | 48,940.00 USD | 342,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 44,090.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 13,970,000.00 USD | 13,970,000.00 USD | 39,650.00 USD | 55,060.00 USD | 23,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 22,860,000.00 USD | 22,860,000.00 USD | 293,300.00 USD | 79,100.00 USD | 108,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 101,080.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 13,860,000.00 USD | 13,860,000.00 USD | 194,940.00 USD | 36,950.00 USD | 142,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 22,380,000.00 USD | 22,380,000.00 USD | 374,290.00 USD | 57,440.00 USD | 218,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 236,880.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 13,480,000.00 USD | 13,480,000.00 USD | 297,570.00 USD | 125,690.00 USD | 110,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 21,730,000.00 USD | 21,730,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 122,430.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 12,950,000.00 USD | 12,950,000.00 USD | 63,250.00 USD | 99,580.00 USD | 99,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 21,080,000.00 USD | 21,080,000.00 USD | 509,640.00 USD | 228,360.00 USD | 174,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 466,520.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 12,680,000.00 USD | 12,680,000.00 USD | 44,430.00 USD | 128,870.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 20,170,000.00 USD | 20,170,000.00 USD | 202,540.00 USD | 114,530.00 USD | 446,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 45,840.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.18` | 12,400,000.00 USD | 12,400,000.00 USD | 197,650.00 USD | 59,270.00 USD | 77,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 19,400,000.00 USD | 19,400,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.18` | 30,300.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.19` | 12,060,000.00 USD | 12,060,000.00 USD | 288,710.00 USD | 79,350.00 USD | 145,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 18,880,000.00 USD | 18,880,000.00 USD | 215,210.00 USD | 113,960.00 USD | 671,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.20` | 101,900.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.20` | 11,550,000.00 USD | 11,550,000.00 USD | 64,030.00 USD | 171,160.00 USD | 466,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 17,880,000.00 USD | 17,880,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 134,680.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.21` | 10,850,000.00 USD | 10,850,000.00 USD | 70,370.00 USD | 146,670.00 USD | 919.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 16,540,000.00 USD | 16,540,000.00 USD | 321,000.00 USD | 149,940.00 USD | 119,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 19,220.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 10,630,000.00 USD | 10,630,000.00 USD | 582,370.00 USD | 141,000.00 USD | 406,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 15,950,000.00 USD | 15,950,000.00 USD | 853,600.00 USD | 161,970.00 USD | 786,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.22` | 49,240.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.23` | 9,500,000.00 USD | 9,500,000.00 USD | 1,040,000.00 USD | 440,840.00 USD | 495,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 14,140,000.00 USD | 14,140,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.24` | 601,150.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.24` | 7,520,000.00 USD | 7,520,000.00 USD | 259,090.00 USD | 201,080.00 USD | 244,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 11,600,000.00 USD | 11,600,000.00 USD | 1,060,000.00 USD | 556,850.00 USD | 567,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 12,700.00 USD | 472,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.25` | 6,810,000.00 USD | 6,810,000.00 USD | 368,110.00 USD | 296,100.00 USD | 466,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 9,420,000.00 USD | 9,420,000.00 USD | 506,030.00 USD | 433,770.00 USD | 647,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 288,490.00 USD | 459,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.26` | 5,680,000.00 USD | 5,680,000.00 USD | 563,140.00 USD | 171,790.00 USD | 298,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 7,830,000.00 USD | 7,830,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.26` | 41,020.00 USD | 171,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.27` | 4,650,000.00 USD | 4,650,000.00 USD | 596,110.00 USD | 199,830.00 USD | 434,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 5,440,000.00 USD | 5,440,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.28` | 6,760.00 USD | 130,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 3,420,000.00 USD | 3,420,000.00 USD | 320,200.00 USD | 286,450.00 USD | 215,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 3,020,000.00 USD | 3,020,000.00 USD | 842,270.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 14,670.00 USD | 123,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.29` | 2,600,000.00 USD | 2,600,000.00 USD | 289,680.00 USD | 53,880.00 USD | 247,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 574,080.00 USD | 574,080.00 USD | 9,100.00 USD | 46,530.00 USD | 361.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 858.14 USD | 109,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.30` | 2,010,000.00 USD | 2,010,000.00 USD | 331,550.00 USD | 217,150.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.30` | 518,090.00 USD | 518,090.00 USD | 3,500.00 USD | 90,090.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.31` | 1,400,000.00 USD | 1,400,000.00 USD | 408,710.00 USD | 222,320.00 USD | 499,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.31` | 348,890.00 USD | 348,890.00 USD | 0.00 USD | 0.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.32` | 122.98 USD | 108,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 272,350.00 USD | 272,350.00 USD | 611.20 USD | 0.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 305,640.00 USD | 305,640.00 USD | 0.00 USD | 0.00 USD | 78,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 5,860.00 USD | 108,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.33` | 271,720.00 USD | 271,720.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.33` | 227,100.00 USD | 227,100.00 USD | 0.00 USD | 0.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 13,310.00 USD | 102,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.34` | 269,720.00 USD | 269,720.00 USD | 269,670.00 USD | 0.00 USD | 55.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 139,100.00 USD | 139,100.00 USD | 4,550.00 USD | 0.00 USD | 134,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.34` | 30,420.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.35` | 85,370.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 170,740.00 USD | 170,740.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.36` | 1,090.00 USD | 58,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 82,490.00 USD | 82,490.00 USD | 82,150.00 USD | 0.00 USD | 346.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.36` | 164,990.00 USD | 164,990.00 USD | 82,150.00 USD | 0.00 USD | 346.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 262,400.00 USD | 262,400.00 USD | 5,210.00 USD | 0.00 USD | 86,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.37` | 56,750.00 USD | 57,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.37` | 299,690.00 USD | 299,690.00 USD | 52,120.00 USD | 0.00 USD | 82,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 600.25 USD | 600.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 947,800.00 USD | 947,800.00 USD | 171,480.00 USD | 0.00 USD | 476,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 665,720.00 USD | 665,720.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 199,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 879,790.00 USD | 879,790.00 USD | 0.00 USD | 62,850.00 USD | 151,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 3,660.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 47.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 1,490,000.00 USD | 1,490,000.00 USD | 193,630.00 USD | 83,080.00 USD | 61,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 270,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 74.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 2,200,000.00 USD | 2,200,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.43` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 49,400.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 2,470,000.00 USD | 2,470,000.00 USD | 155,560.00 USD | 46,230.00 USD | 69,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 2,370,000.00 USD | 2,370,000.00 USD | 154,480.00 USD | 339,100.00 USD | 287,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 116,400.00 USD | 70,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 34,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.47` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 16,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 2,990,000.00 USD | 2,990,000.00 USD | 132,630.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.48` | 2,510,000.00 USD | 2,510,000.00 USD | 38,080.00 USD | 56,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 3,070,000.00 USD | 3,070,000.00 USD | 252,560.00 USD | 155,000.00 USD | 150,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 3,330,000.00 USD | 3,330,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.50` | 3,610,000.00 USD | 3,610,000.00 USD | 358,600.00 USD | 65,710.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 3,900,000.00 USD | 3,900,000.00 USD | 368,940.00 USD | 200,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.51` | 4,390,000.00 USD | 4,390,000.00 USD | 162,900.00 USD | 307,580.00 USD | 309,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 3,980,000.00 USD | 3,980,000.00 USD | 77,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 4,950,000.00 USD | 4,950,000.00 USD | 266,310.00 USD | 88,150.00 USD | 205,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.53` | 5,720,000.00 USD | 5,720,000.00 USD | 487,010.00 USD | 0.00 USD | 278,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 5,020,000.00 USD | 5,020,000.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 150,600.00 USD | 598,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.55` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 22,540.00 USD | 239,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 7,130,000.00 USD | 7,130,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 6,740,000.00 USD | 6,740,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 7,430,000.00 USD | 7,430,000.00 USD | 154,940.00 USD | 70,180.00 USD | 67,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 7,090,000.00 USD | 7,090,000.00 USD | 198,050.00 USD | 0.00 USD | 151,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 8,740,000.00 USD | 8,740,000.00 USD | 434,430.00 USD | 43,090.00 USD | 840,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 7,220,000.00 USD | 7,220,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 9,700,000.00 USD | 9,700,000.00 USD | 826,150.00 USD | 75,460.00 USD | 58,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 8,820,000.00 USD | 8,820,000.00 USD | 759,320.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 444.34 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 9,910,000.00 USD | 9,910,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 8,930,000.00 USD | 8,930,000.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 484.91 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 10,040,000.00 USD | 10,040,000.00 USD | 66,620.00 USD | 7,560.00 USD | 58,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 8,940,000.00 USD | 8,940,000.00 USD | 3,350.00 USD | 0.00 USD | 703.64 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 34,060.00 USD | 38,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.62` | 10,170,000.00 USD | 10,170,000.00 USD | 95,090.00 USD | 31,380.00 USD | 822.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 9,080,000.00 USD | 9,080,000.00 USD | 134,680.00 USD | 0.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 10,170,000.00 USD | 10,170,000.00 USD | 1,040.00 USD | 0.00 USD | 351.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 9,290,000.00 USD | 9,290,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 2,400.00 USD | 41,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 10,580,000.00 USD | 10,580,000.00 USD | 332,920.00 USD | 11,270.00 USD | 62,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 9,790,000.00 USD | 9,790,000.00 USD | 500,990.00 USD | 0.00 USD | 857.07 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 7,990.00 USD | 49,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 11,590,000.00 USD | 11,590,000.00 USD | 370,110.00 USD | 52,020.00 USD | 587,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 10,210,000.00 USD | 10,210,000.00 USD | 420,940.00 USD | 0.00 USD | 649.48 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 38,330.00 USD | 87,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 12,550,000.00 USD | 12,550,000.00 USD | 281,290.00 USD | 304,540.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 10,510,000.00 USD | 10,510,000.00 USD | 144,860.00 USD | 0.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,700.00 USD | 212,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 13,110,000.00 USD | 13,110,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 154.74 USD | 212,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 13,700,000.00 USD | 13,700,000.00 USD | 345,490.00 USD | 62,440.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 11,470,000.00 USD | 11,470,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 14,780.00 USD | 227,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 14,190,000.00 USD | 14,190,000.00 USD | 213,780.00 USD | 40,000.00 USD | 237,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 11,560,000.00 USD | 11,560,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 1,050.00 USD | 228,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 14,530,000.00 USD | 14,530,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 11,870,000.00 USD | 11,870,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 11,230.00 USD | 239,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 15,490,000.00 USD | 15,490,000.00 USD | 365,440.00 USD | 278,020.00 USD | 316,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 12,290,000.00 USD | 12,290,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 29,520.00 USD | 268,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 15,790,000.00 USD | 15,790,000.00 USD | 5,240.00 USD | 187,480.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 12,470,000.00 USD | 12,470,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 3,920.00 USD | 272,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 15,950,000.00 USD | 15,950,000.00 USD | 61,330.00 USD | 37,010.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 12,530,000.00 USD | 12,530,000.00 USD | 59,270.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 4,700.00 USD | 277,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 16,660,000.00 USD | 16,660,000.00 USD | 242,820.00 USD | 172,000.00 USD | 294,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 12,850,000.00 USD | 12,850,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 12,960.00 USD | 290,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 17,370,000.00 USD | 17,370,000.00 USD | 240,860.00 USD | 202,760.00 USD | 270,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 13,390,000.00 USD | 13,390,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 1,720.00 USD | 292,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 17,730,000.00 USD | 17,730,000.00 USD | 35,470.00 USD | 78,750.00 USD | 247,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 14,740,000.00 USD | 14,740,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.77` | 18,130,000.00 USD | 18,130,000.00 USD | 113,030.00 USD | 167,820.00 USD | 115,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 15,650,000.00 USD | 15,650,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,050.00 USD | 299,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 18,300,000.00 USD | 18,300,000.00 USD | 40,580.00 USD | 20,000.00 USD | 114,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 17,040,000.00 USD | 17,040,000.00 USD | 683,730.00 USD | 551,660.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 20,410.00 USD | 319,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 18,650,000.00 USD | 18,650,000.00 USD | 112,300.00 USD | 92,850.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 18,070,000.00 USD | 18,070,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 553,480.00 USD | 873,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 19,270,000.00 USD | 19,270,000.00 USD | 244,480.00 USD | 200,920.00 USD | 174,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 19,660,000.00 USD | 19,660,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 19,570,000.00 USD | 19,570,000.00 USD | 55,660.00 USD | 120,180.00 USD | 127,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 20,290,000.00 USD | 20,290,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 50,910.00 USD | 923,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 20,130,000.00 USD | 20,130,000.00 USD | 140,640.00 USD | 218,170.00 USD | 201,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 23,060,000.00 USD | 23,060,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 925,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 20,410,000.00 USD | 20,410,000.00 USD | 61,110.00 USD | 70,050.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 24,710,000.00 USD | 24,710,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 21,070.00 USD | 946,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 20,660,000.00 USD | 20,660,000.00 USD | 85,920.00 USD | 89,230.00 USD | 77,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 25,200,000.00 USD | 25,200,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.85` | 21,240,000.00 USD | 21,240,000.00 USD | 243,020.00 USD | 110,540.00 USD | 223,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 27,220,000.00 USD | 27,220,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.86` | 22,180.00 USD | 968,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.86` | 21,680,000.00 USD | 21,680,000.00 USD | 94,860.00 USD | 69,470.00 USD | 278,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 28,630,000.00 USD | 28,630,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 974,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.87` | 21,910,000.00 USD | 21,910,000.00 USD | 111,250.00 USD | 60,360.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.87` | 29,690,000.00 USD | 29,690,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 18,250.00 USD | 992,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.88` | 21,990,000.00 USD | 21,990,000.00 USD | 36,680.00 USD | 7,330.00 USD | 38,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 31,350,000.00 USD | 31,350,000.00 USD | 449,970.00 USD | 415,840.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 993,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.89` | 22,080,000.00 USD | 22,080,000.00 USD | 11,490.00 USD | 25,940.00 USD | 50,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.89` | 31,940,000.00 USD | 31,940,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.90` | 22,220,000.00 USD | 22,220,000.00 USD | 25,630.00 USD | 55,440.00 USD | 65,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 33,070,000.00 USD | 33,070,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.91` | 1,630.00 USD | 995,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.91` | 22,500,000.00 USD | 22,500,000.00 USD | 114,890.00 USD | 85,510.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 34,510,000.00 USD | 34,510,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.92` | 22,860,000.00 USD | 22,860,000.00 USD | 117,750.00 USD | 89,190.00 USD | 153,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.92` | 36,240,000.00 USD | 36,240,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 12,930.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 37,800,000.00 USD | 37,800,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 39,100,000.00 USD | 39,100,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 40,400,000.00 USD | 40,400,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 1,350,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 41,640,000.00 USD | 41,640,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 42,020,000.00 USD | 42,020,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 42,580,000.00 USD | 42,580,000.00 USD | 197,950.00 USD | 88,580.00 USD | 270,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 1,710.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 42,930,000.00 USD | 42,930,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 43,630,000.00 USD | 43,630,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 260.76 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.01` | 45,790,000.00 USD | 45,790,000.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.01` | 371,590.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.02` | 47,270,000.00 USD | 47,270,000.00 USD | 821,860.00 USD | 337,720.00 USD | 321,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 48,710,000.00 USD | 48,710,000.00 USD | 385,330.00 USD | 172,880.00 USD | 886,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 13,130.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.04` | 49,830,000.00 USD | 49,830,000.00 USD | 305,260.00 USD | 191,790.00 USD | 619,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,160.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.05` | 51,380,000.00 USD | 51,380,000.00 USD | 799,820.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 55,570.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 52,090,000.00 USD | 52,090,000.00 USD | 92,480.00 USD | 193,330.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 53,290,000.00 USD | 53,290,000.00 USD | 358,750.00 USD | 166,480.00 USD | 673,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 56,820.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.08` | 53,890,000.00 USD | 53,890,000.00 USD | 204,140.00 USD | 243,390.00 USD | 149,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 3,190.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 54,750,000.00 USD | 54,750,000.00 USD | 105,390.00 USD | 121,050.00 USD | 633,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 55,240,000.00 USD | 55,240,000.00 USD | 291,110.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 55,990,000.00 USD | 55,990,000.00 USD | 369,260.00 USD | 92,720.00 USD | 291,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 56,580,000.00 USD | 56,580,000.00 USD | 303,840.00 USD | 166,880.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,680.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 57,310,000.00 USD | 57,310,000.00 USD | 173,190.00 USD | 71,310.00 USD | 484,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 2,110.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 57,760,000.00 USD | 57,760,000.00 USD | 140,950.00 USD | 73,940.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.15` | 58,370,000.00 USD | 58,370,000.00 USD | 258,430.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 58,900,000.00 USD | 58,900,000.00 USD | 51,850.00 USD | 126,880.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 317.65 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 59,590,000.00 USD | 59,590,000.00 USD | 280,710.00 USD | 99,740.00 USD | 309,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 346.72 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.18` | 59,880,000.00 USD | 59,880,000.00 USD | 67,600.00 USD | 101,040.00 USD | 124,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 60,260,000.00 USD | 60,260,000.00 USD | 69,310.00 USD | 47,800.00 USD | 262,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 7,610.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 60,550,000.00 USD | 60,550,000.00 USD | 180,600.00 USD | 45,820.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,250.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.24` | 29,050.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 245.29 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 228.84 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 59,130.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 878.04 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 37,730.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 19,840.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 79,090.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 41,910.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 310.68 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 2,320.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 2,300.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 2,270.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 255,740.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 88,450.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 39,430.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 54,260.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 17,680.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.66` | 301.98 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 1,730.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 32,270.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 6,050.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.72` | 738.52 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 9,160.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 197.27 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.82` | 82,870.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 6,670.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 604.10 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 855.09 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 89,540.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.99` | 131.67 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 1,860.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.01` | 6,080.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.04` | 129,280.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 12,520.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.16` | 1,160,000.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 330,920.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 1,370.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,610.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 1,820,000.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.30` | 829.74 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 4,110.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 584,470.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 91,940.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 109.43 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.49` | 77,820.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.50` | 325.25 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 536.84 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 697.04 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 29,440.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 392,810.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 12,080.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 15,540.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 40,180.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 474.36 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,410.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 60,560.00 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.91` | 189.89 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 37,400.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.07` | 257.87 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 1,370.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.22` | 9,650,000.00 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.29` | 772.94 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.36` | 6,740.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 154.35 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 3,220.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 121,410.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 107,200.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 7,790,000.00 USD | 29,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 29,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 319,720.00 USD | 29,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 29,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 29,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.70` | 31,690.00 USD | 29,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 15,410.00 USD | 29,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 2,680.00 USD | 29,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 25,930.00 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 33,580.00 USD | 29,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.82` | 819.01 USD | 29,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 4,280.00 USD | 29,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 27,570.00 USD | 29,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 29,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 29,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.10` | 359.42 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.12` | 937,370.00 USD | 31,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.13` | 409,570.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.14` | 733,050.00 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 17,700.00 USD | 32,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 577.04 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.45` | 3,830.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 35,260.00 USD | 33,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 594.65 USD | 33,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.52` | 172,480.00 USD | 33,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 578.85 USD | 33,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 26,620.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 2,760.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 774.32 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.64` | 24,890.00 USD | 33,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 2,480.00 USD | 33,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.71` | 449,960.00 USD | 34,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.78` | 3,420,000.00 USD | 37,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8650` | 33,560,000.00 USD | 0.00 USD | 3,350.00 USD | `-80.37%` | `3,876.00` |
| `Live` | `Long` | `0.8750` | 33,560,000.00 USD | 0.00 USD | 43,750.00 USD | `-80.14%` | `50,000.00` |
| `Live` | `Long` | `0.8850` | 33,510,000.00 USD | 0.00 USD | 512.24 USD | `-79.91%` | `578.80` |
| `Live` | `Long` | `0.8950` | 33,510,000.00 USD | 0.00 USD | 39,380.00 USD | `-79.69%` | `44,002.20` |
| `Live` | `Long` | `0.9050` | 33,470,000.00 USD | 0.00 USD | 292.22 USD | `-79.46%` | `322.90` |
| `Live` | `Long` | `0.9150` | 33,470,000.00 USD | 0.00 USD | 19,280.00 USD | `-79.23%` | `21,068.20` |
| `Live` | `Long` | `0.9350` | 33,450,000.00 USD | 0.00 USD | 5,280,000.00 USD | `-78.78%` | `5,651,256.90` |
| `Live` | `Long` | `0.9550` | 28,170,000.00 USD | 0.00 USD | 286.50 USD | `-78.32%` | `300.00` |
| `Live` | `Long` | `0.9650` | 28,170,000.00 USD | 0.00 USD | 6,610.00 USD | `-78.10%` | `6,847.00` |
| `Live` | `Long` | `0.9850` | 28,160,000.00 USD | 0.00 USD | 30,370.00 USD | `-77.64%` | `30,836.80` |
| `Live` | `Long` | `0.9950` | 28,130,000.00 USD | 0.00 USD | 154,200.00 USD | `-77.42%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 27,980,000.00 USD | 0.00 USD | 1,000.00 USD | `-77.19%` | `1,000.00` |
| `Live` | `Long` | `1.01` | 27,980,000.00 USD | 0.00 USD | 126.06 USD | `-76.96%` | `124.20` |
| `Live` | `Long` | `1.02` | 27,980,000.00 USD | 0.00 USD | 11,320.00 USD | `-76.74%` | `11,042.60` |
| `Live` | `Long` | `1.03` | 27,970,000.00 USD | 0.00 USD | 5,070.00 USD | `-76.51%` | `4,897.40` |
| `Live` | `Long` | `1.05` | 27,960,000.00 USD | 0.00 USD | 8,040.00 USD | `-76.05%` | `7,624.40` |
| `Live` | `Long` | `1.06` | 27,950,000.00 USD | 0.00 USD | 892.90 USD | `-75.83%` | `838.40` |
| `Live` | `Long` | `1.07` | 27,950,000.00 USD | 0.00 USD | 383,760.00 USD | `-75.60%` | `356,989.70` |
| `Live` | `Long` | `1.08` | 27,570,000.00 USD | 0.00 USD | 53,650.00 USD | `-75.37%` | `49,448.60` |
| `Live` | `Long` | `1.09` | 27,510,000.00 USD | 0.00 USD | 73,400.00 USD | `-75.15%` | `67,034.60` |
| `Live` | `Long` | `1.11` | 27,440,000.00 USD | 0.00 USD | 557.50 USD | `-74.69%` | `500.00` |
| `Live` | `Long` | `1.12` | 27,440,000.00 USD | 0.00 USD | 41,270.00 USD | `-74.47%` | `36,680.70` |
| `Live` | `Long` | `1.14` | 27,400,000.00 USD | 0.00 USD | 4,960.00 USD | `-74.24%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 27,390,000.00 USD | 0.00 USD | 57,020.00 USD | `-74.01%` | `49,797.70` |
| `Live` | `Long` | `1.18` | 27,340,000.00 USD | 0.00 USD | 184.59 USD | `-73.33%` | `157.10` |
| `Live` | `Long` | `1.19` | 27,340,000.00 USD | 0.00 USD | 13,350.00 USD | `-73.10%` | `11,269.30` |
| `Live` | `Long` | `1.20` | 27,320,000.00 USD | 0.00 USD | 2,670.00 USD | `-72.88%` | `2,236.30` |
| `Live` | `Long` | `1.21` | 27,320,000.00 USD | 0.00 USD | 35,290.00 USD | `-72.65%` | `29,290.40` |
| `Live` | `Long` | `1.22` | 27,290,000.00 USD | 0.00 USD | 21,600.00 USD | `-72.42%` | `17,777.30` |
| `Live` | `Long` | `1.24` | 27,260,000.00 USD | 0.00 USD | 2,300.00 USD | `-71.97%` | `1,860.10` |
| `Live` | `Long` | `1.25` | 27,260,000.00 USD | 0.00 USD | 558.38 USD | `-71.74%` | `448.50` |
| `Live` | `Long` | `1.25` | 27,260,000.00 USD | 0.00 USD | 653.98 USD | `-71.52%` | `521.10` |
| `Live` | `Long` | `1.26` | 27,260,000.00 USD | 0.00 USD | 11,870.00 USD | `-71.29%` | `9,380.90` |
| `Live` | `Long` | `1.27` | 27,250,000.00 USD | 0.00 USD | 2,390.00 USD | `-71.06%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 27,250,000.00 USD | 0.00 USD | 169.23 USD | `-70.83%` | `131.70` |
| `Live` | `Long` | `1.30` | 27,250,000.00 USD | 0.00 USD | 13,810.00 USD | `-70.38%` | `10,581.00` |
| `Live` | `Long` | `1.32` | 27,230,000.00 USD | 0.00 USD | 2,830.00 USD | `-69.93%` | `2,132.40` |
| `Live` | `Long` | `1.33` | 27,230,000.00 USD | 0.00 USD | 2,760.00 USD | `-69.70%` | `2,071.10` |
| `Live` | `Long` | `1.34` | 27,230,000.00 USD | 0.00 USD | 11,330.00 USD | `-69.47%` | `8,424.40` |
| `Live` | `Long` | `1.35` | 27,220,000.00 USD | 0.00 USD | 236.85 USD | `-69.25%` | `174.80` |
| `Live` | `Long` | `1.36` | 27,220,000.00 USD | 0.00 USD | 1,330.00 USD | `-69.02%` | `975.00` |
| `Live` | `Long` | `1.38` | 27,210,000.00 USD | 0.00 USD | 12,380.00 USD | `-68.79%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 27,200,000.00 USD | 0.00 USD | 295.56 USD | `-68.56%` | `213.40` |
| `Live` | `Long` | `1.40` | 27,200,000.00 USD | 0.00 USD | 157.50 USD | `-68.34%` | `112.90` |
| `Live` | `Long` | `1.41` | 27,200,000.00 USD | 0.00 USD | 23,470.00 USD | `-68.11%` | `16,703.50` |
| `Live` | `Long` | `1.42` | 27,180,000.00 USD | 0.00 USD | 669.86 USD | `-67.88%` | `473.40` |
| `Live` | `Long` | `1.43` | 27,180,000.00 USD | 0.00 USD | 18,780.00 USD | `-67.66%` | `13,181.20` |
| `Live` | `Long` | `1.45` | 27,160,000.00 USD | 0.00 USD | 226.29 USD | `-67.20%` | `156.60` |
| `Live` | `Long` | `1.47` | 27,160,000.00 USD | 0.00 USD | 1,320.00 USD | `-66.75%` | `900.20` |
| `Live` | `Long` | `1.48` | 27,160,000.00 USD | 0.00 USD | 1,480.00 USD | `-66.52%` | `1,000.00` |
| `Live` | `Long` | `1.50` | 27,160,000.00 USD | 0.00 USD | 4,200.00 USD | `-65.84%` | `2,793.80` |
| `Live` | `Long` | `1.51` | 27,150,000.00 USD | 0.00 USD | 674.18 USD | `-65.61%` | `445.00` |
| `Live` | `Long` | `1.52` | 27,150,000.00 USD | 0.00 USD | 31,130.00 USD | `-65.39%` | `20,415.60` |
| `Live` | `Long` | `1.53` | 27,120,000.00 USD | 0.00 USD | 1,170.00 USD | `-65.16%` | `760.90` |
| `Live` | `Long` | `1.56` | 27,120,000.00 USD | 0.00 USD | 16,150.00 USD | `-64.48%` | `10,320.00` |
| `Live` | `Long` | `1.57` | 27,100,000.00 USD | 0.00 USD | 589.52 USD | `-64.25%` | `374.30` |
| `Live` | `Long` | `1.58` | 27,100,000.00 USD | 0.00 USD | 4,620.00 USD | `-64.03%` | `2,914.40` |
| `Live` | `Long` | `1.59` | 27,100,000.00 USD | 0.00 USD | 5,680.00 USD | `-63.80%` | `3,560.50` |
| `Live` | `Long` | `1.60` | 27,090,000.00 USD | 0.00 USD | 308.32 USD | `-63.57%` | `192.10` |
| `Live` | `Long` | `1.62` | 27,090,000.00 USD | 0.00 USD | 2,440.00 USD | `-63.12%` | `1,500.00` |
| `Live` | `Long` | `1.64` | 27,090,000.00 USD | 0.00 USD | 2,510.00 USD | `-62.89%` | `1,534.80` |
| `Live` | `Long` | `1.65` | 27,090,000.00 USD | 0.00 USD | 10,850.00 USD | `-62.66%` | `6,596.40` |
| `Live` | `Long` | `1.66` | 27,080,000.00 USD | 0.00 USD | 384.13 USD | `-62.44%` | `232.10` |
| `Live` | `Long` | `1.67` | 27,070,000.00 USD | 0.00 USD | 4,740.00 USD | `-62.21%` | `2,845.90` |
| `Live` | `Long` | `1.68` | 27,070,000.00 USD | 0.00 USD | 1,190.00 USD | `-61.98%` | `708.70` |
| `Live` | `Long` | `1.69` | 27,070,000.00 USD | 0.00 USD | 17,420.00 USD | `-61.76%` | `10,336.30` |
| `Live` | `Long` | `1.71` | 27,050,000.00 USD | 0.00 USD | 569.64 USD | `-61.30%` | `334.10` |
| `Live` | `Long` | `1.72` | 27,050,000.00 USD | 0.00 USD | 6,790.00 USD | `-61.07%` | `3,960.10` |
| `Live` | `Long` | `1.73` | 27,040,000.00 USD | 0.00 USD | 5,460.00 USD | `-60.85%` | `3,164.50` |
| `Live` | `Long` | `1.74` | 27,040,000.00 USD | 0.00 USD | 1,370.00 USD | `-60.62%` | `790.10` |
| `Live` | `Long` | `1.75` | 27,040,000.00 USD | 0.00 USD | 5,750.00 USD | `-60.39%` | `3,296.80` |
| `Live` | `Long` | `1.75` | 27,030,000.00 USD | 0.00 USD | 11,460.00 USD | `-60.17%` | `6,531.00` |
| `Live` | `Long` | `1.76` | 27,020,000.00 USD | 0.00 USD | 211.80 USD | `-59.94%` | `120.00` |
| `Live` | `Long` | `1.77` | 27,020,000.00 USD | 0.00 USD | 265,490.00 USD | `-59.71%` | `149,570.20` |
| `Live` | `Long` | `1.78` | 26,750,000.00 USD | 0.00 USD | 15,250.00 USD | `-59.49%` | `8,544.50` |
| `Live` | `Long` | `1.79` | 26,740,000.00 USD | 0.00 USD | 2,440.00 USD | `-59.26%` | `1,358.90` |
| `Live` | `Long` | `1.80` | 26,740,000.00 USD | 0.00 USD | 529.05 USD | `-59.03%` | `293.10` |
| `Live` | `Long` | `1.81` | 26,740,000.00 USD | 0.00 USD | 2,870.00 USD | `-58.81%` | `1,581.20` |
| `Live` | `Long` | `1.83` | 26,730,000.00 USD | 0.00 USD | 27,520.00 USD | `-58.35%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 26,710,000.00 USD | 0.00 USD | 1,080.00 USD | `-58.12%` | `586.00` |
| `Live` | `Long` | `1.85` | 26,700,000.00 USD | 0.00 USD | 13,270.00 USD | `-57.90%` | `7,152.90` |
| `Live` | `Long` | `1.86` | 26,690,000.00 USD | 0.00 USD | 12,910.00 USD | `-57.67%` | `6,919.80` |
| `Live` | `Long` | `1.88` | 26,680,000.00 USD | 0.00 USD | 1,310.00 USD | `-57.44%` | `700.00` |
| `Live` | `Long` | `1.89` | 26,680,000.00 USD | 0.00 USD | 1,250.00 USD | `-57.22%` | `662.90` |
| `Live` | `Long` | `1.90` | 26,680,000.00 USD | 0.00 USD | 24,990.00 USD | `-56.99%` | `13,187.20` |
| `Live` | `Long` | `1.91` | 26,650,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-56.76%` | `902,334.80` |
| `Live` | `Long` | `1.92` | 24,930,000.00 USD | 0.00 USD | 2,010.00 USD | `-56.54%` | `1,049.80` |
| `Live` | `Long` | `1.93` | 24,930,000.00 USD | 0.00 USD | 263.92 USD | `-56.31%` | `137.10` |
| `Live` | `Long` | `1.94` | 24,930,000.00 USD | 0.00 USD | 6,770.00 USD | `-56.08%` | `3,500.00` |
| `Live` | `Long` | `1.95` | 24,920,000.00 USD | 0.00 USD | 3,010.00 USD | `-55.85%` | `1,549.50` |
| `Live` | `Long` | `1.96` | 24,920,000.00 USD | 0.00 USD | 775.55 USD | `-55.63%` | `396.70` |
| `Live` | `Long` | `1.97` | 24,920,000.00 USD | 0.00 USD | 3,960.00 USD | `-55.40%` | `2,014.70` |
| `Live` | `Long` | `1.98` | 24,920,000.00 USD | 0.00 USD | 41,570.00 USD | `-55.17%` | `21,047.20` |
| `Live` | `Long` | `1.99` | 24,870,000.00 USD | 0.00 USD | 643.54 USD | `-54.95%` | `324.20` |
| `Live` | `Long` | `2.00` | 24,870,000.00 USD | 0.00 USD | 199,500.00 USD | `-54.72%` | `100,000.00` |
| `Live` | `Long` | `2.00` | 24,670,000.00 USD | 0.00 USD | 214,480.00 USD | `-54.49%` | `106,974.60` |
| `Live` | `Long` | `2.02` | 24,460,000.00 USD | 0.00 USD | 81,810.00 USD | `-54.04%` | `40,398.40` |
| `Live` | `Long` | `2.04` | 24,380,000.00 USD | 0.00 USD | 6,020.00 USD | `-53.58%` | `2,943.70` |
| `Live` | `Long` | `2.06` | 24,370,000.00 USD | 0.00 USD | 86,680.00 USD | `-53.36%` | `42,179.40` |
| `Live` | `Long` | `2.08` | 24,280,000.00 USD | 0.00 USD | 6,810.00 USD | `-52.90%` | `3,280.90` |
| `Live` | `Long` | `2.08` | 24,280,000.00 USD | 0.00 USD | 12,830.00 USD | `-52.68%` | `6,152.90` |
| `Live` | `Long` | `2.10` | 24,260,000.00 USD | 0.00 USD | 7,950.00 USD | `-52.22%` | `3,778.30` |
| `Live` | `Long` | `2.12` | 24,260,000.00 USD | 0.00 USD | 11,510.00 USD | `-52.00%` | `5,442.30` |
| `Live` | `Long` | `2.12` | 24,250,000.00 USD | 0.00 USD | 10,310.00 USD | `-51.77%` | `4,850.30` |
| `Live` | `Long` | `2.13` | 24,240,000.00 USD | 0.00 USD | 3,210.00 USD | `-51.54%` | `1,504.40` |
| `Live` | `Long` | `2.15` | 24,230,000.00 USD | 0.00 USD | 5,590.00 USD | `-51.32%` | `2,607.20` |
| `Live` | `Long` | `2.15` | 24,230,000.00 USD | 0.00 USD | 594.13 USD | `-51.09%` | `275.70` |
| `Live` | `Long` | `2.17` | 24,230,000.00 USD | 0.00 USD | 6,120.00 USD | `-50.86%` | `2,825.90` |
| `Live` | `Long` | `2.17` | 24,220,000.00 USD | 0.00 USD | 248.38 USD | `-50.63%` | `114.20` |
| `Live` | `Long` | `2.19` | 24,220,000.00 USD | 0.00 USD | 45,940.00 USD | `-50.41%` | `21,023.20` |
| `Live` | `Long` | `2.19` | 24,170,000.00 USD | 0.00 USD | 10,880.00 USD | `-50.18%` | `4,955.90` |
| `Live` | `Long` | `2.21` | 24,160,000.00 USD | 0.00 USD | 24,600.00 USD | `-49.95%` | `11,156.10` |
| `Live` | `Long` | `2.21` | 24,140,000.00 USD | 0.00 USD | 239.00 USD | `-49.73%` | `107.90` |
| `Live` | `Long` | `2.23` | 24,140,000.00 USD | 0.00 USD | 6,340.00 USD | `-49.50%` | `2,850.30` |
| `Live` | `Long` | `2.23` | 24,130,000.00 USD | 0.00 USD | 26,180.00 USD | `-49.27%` | `11,712.40` |
| `Live` | `Long` | `2.25` | 24,110,000.00 USD | 0.00 USD | 4,680.00 USD | `-49.05%` | `2,083.40` |
| `Live` | `Long` | `2.25` | 24,100,000.00 USD | 0.00 USD | 120,330.00 USD | `-48.82%` | `53,360.80` |
| `Live` | `Long` | `2.27` | 23,980,000.00 USD | 0.00 USD | 3,440.00 USD | `-48.36%` | `1,513.80` |
| `Live` | `Long` | `2.29` | 23,980,000.00 USD | 0.00 USD | 804.32 USD | `-48.14%` | `352.00` |
| `Live` | `Long` | `2.29` | 23,980,000.00 USD | 0.00 USD | 4,150.00 USD | `-47.91%` | `1,810.40` |
| `Live` | `Long` | `2.31` | 23,970,000.00 USD | 0.00 USD | 2,810.00 USD | `-47.68%` | `1,219.90` |
| `Live` | `Long` | `2.31` | 23,970,000.00 USD | 0.00 USD | 9,840.00 USD | `-47.46%` | `4,250.90` |
| `Live` | `Long` | `2.33` | 23,960,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-47.23%` | `652,841.30` |
| `Live` | `Long` | `2.33` | 22,440,000.00 USD | 0.00 USD | 3,120.00 USD | `-47.00%` | `1,337.30` |
| `Live` | `Long` | `2.35` | 22,440,000.00 USD | 0.00 USD | 48,780.00 USD | `-46.78%` | `20,800.50` |
| `Live` | `Long` | `2.35` | 22,390,000.00 USD | 0.00 USD | 5,800.00 USD | `-46.55%` | `2,461.80` |
| `Live` | `Long` | `2.37` | 22,380,000.00 USD | 0.00 USD | 63,060.00 USD | `-46.32%` | `26,664.00` |
| `Live` | `Long` | `2.38` | 22,320,000.00 USD | 0.00 USD | 420,020.00 USD | `-46.10%` | `176,849.70` |
| `Live` | `Long` | `2.38` | 21,900,000.00 USD | 0.00 USD | 534.24 USD | `-45.87%` | `224.00` |
| `Live` | `Long` | `2.40` | 21,900,000.00 USD | 0.00 USD | 63,350.00 USD | `-45.64%` | `26,450.10` |
| `Live` | `Long` | `2.40` | 21,840,000.00 USD | 0.00 USD | 2,310.00 USD | `-45.41%` | `961.40` |
| `Live` | `Long` | `2.42` | 21,830,000.00 USD | 0.00 USD | 185,860.00 USD | `-45.19%` | `76,961.80` |
| `Live` | `Long` | `2.42` | 21,650,000.00 USD | 0.00 USD | 60,620.00 USD | `-44.96%` | `25,000.00` |
| `Live` | `Long` | `2.44` | 21,590,000.00 USD | 0.00 USD | 391,530.00 USD | `-44.73%` | `160,791.20` |
| `Live` | `Long` | `2.44` | 21,200,000.00 USD | 0.00 USD | 158,860.00 USD | `-44.51%` | `64,971.50` |
| `Live` | `Long` | `2.46` | 21,040,000.00 USD | 0.00 USD | 636,570.00 USD | `-44.28%` | `259,296.20` |
| `Live` | `Long` | `2.46` | 20,400,000.00 USD | 0.00 USD | 15,480.00 USD | `-44.05%` | `6,281.60` |
| `Live` | `Long` | `2.48` | 20,390,000.00 USD | 0.00 USD | 259,390.00 USD | `-43.83%` | `104,802.20` |
| `Live` | `Long` | `2.48` | 20,130,000.00 USD | 0.00 USD | 2,760.00 USD | `-43.60%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 20,120,000.00 USD | 0.00 USD | 7,690.00 USD | `-43.37%` | `3,081.30` |
| `Live` | `Long` | `2.50` | 20,120,000.00 USD | 0.00 USD | 7,490.00 USD | `-43.14%` | `2,989.20` |
| `Live` | `Long` | `2.52` | 20,110,000.00 USD | 0.00 USD | 37,790.00 USD | `-42.92%` | `15,025.00` |
| `Live` | `Long` | `2.52` | 20,070,000.00 USD | 0.00 USD | 10,330.00 USD | `-42.69%` | `4,089.30` |
| `Live` | `Long` | `2.54` | 20,060,000.00 USD | 0.00 USD | 1,160.00 USD | `-42.46%` | `458.00` |
| `Live` | `Long` | `2.54` | 20,060,000.00 USD | 0.00 USD | 10,920.00 USD | `-42.24%` | `4,291.70` |
| `Live` | `Long` | `2.56` | 20,050,000.00 USD | 0.00 USD | 9,730.00 USD | `-42.01%` | `3,808.10` |
| `Live` | `Long` | `2.56` | 20,040,000.00 USD | 0.00 USD | 8,920.00 USD | `-41.78%` | `3,477.60` |
| `Live` | `Long` | `2.58` | 20,030,000.00 USD | 0.00 USD | 368.88 USD | `-41.33%` | `142.70` |
| `Live` | `Long` | `2.60` | 20,030,000.00 USD | 0.00 USD | 71,500.00 USD | `-41.10%` | `27,553.00` |
| `Live` | `Long` | `2.60` | 19,960,000.00 USD | 0.00 USD | 560.34 USD | `-40.87%` | `215.10` |
| `Live` | `Long` | `2.62` | 19,960,000.00 USD | 0.00 USD | 14,260.00 USD | `-40.65%` | `5,454.70` |
| `Live` | `Long` | `2.62` | 19,940,000.00 USD | 0.00 USD | 224.44 USD | `-40.42%` | `85.50` |
| `Live` | `Long` | `2.63` | 19,940,000.00 USD | 0.00 USD | 65,400.00 USD | `-40.19%` | `24,818.10` |
| `Live` | `Long` | `2.65` | 19,880,000.00 USD | 0.00 USD | 10,090.00 USD | `-39.97%` | `3,813.20` |
| `Live` | `Long` | `2.65` | 19,870,000.00 USD | 0.00 USD | 18,510.00 USD | `-39.74%` | `6,972.60` |
| `Live` | `Long` | `2.67` | 19,850,000.00 USD | 0.00 USD | 103,320.00 USD | `-39.51%` | `38,770.30` |
| `Live` | `Long` | `2.67` | 19,750,000.00 USD | 0.00 USD | 4,300.00 USD | `-39.29%` | `1,606.20` |
| `Live` | `Long` | `2.69` | 19,740,000.00 USD | 0.00 USD | 6,930.00 USD | `-39.06%` | `2,579.60` |
| `Live` | `Long` | `2.69` | 19,730,000.00 USD | 0.00 USD | 20,370.00 USD | `-38.83%` | `7,559.00` |
| `Live` | `Long` | `2.71` | 19,710,000.00 USD | 0.00 USD | 130,140.00 USD | `-38.61%` | `48,109.40` |
| `Live` | `Long` | `2.71` | 19,580,000.00 USD | 0.00 USD | 17,980.00 USD | `-38.38%` | `6,622.10` |
| `Live` | `Long` | `2.73` | 19,570,000.00 USD | 0.00 USD | 249,070.00 USD | `-38.15%` | `91,402.20` |
| `Live` | `Long` | `2.73` | 19,320,000.00 USD | 0.00 USD | 8,440.00 USD | `-37.92%` | `3,085.00` |
| `Live` | `Long` | `2.75` | 19,310,000.00 USD | 0.00 USD | 39,550.00 USD | `-37.70%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 19,270,000.00 USD | 0.00 USD | 154.83 USD | `-37.47%` | `56.20` |
| `Live` | `Long` | `2.77` | 19,270,000.00 USD | 0.00 USD | 3,740.00 USD | `-37.24%` | `1,350.90` |
| `Live` | `Long` | `2.77` | 19,260,000.00 USD | 0.00 USD | 2,140.00 USD | `-37.02%` | `771.20` |
| `Live` | `Long` | `2.79` | 19,260,000.00 USD | 0.00 USD | 24,840.00 USD | `-36.79%` | `8,920.90` |
| `Live` | `Long` | `2.79` | 19,240,000.00 USD | 0.00 USD | 10,470.00 USD | `-36.56%` | `3,746.80` |
| `Live` | `Long` | `2.81` | 19,230,000.00 USD | 0.00 USD | 6,190.00 USD | `-36.34%` | `2,208.40` |
| `Live` | `Long` | `2.81` | 19,220,000.00 USD | 0.00 USD | 572.29 USD | `-36.11%` | `203.30` |
| `Live` | `Long` | `2.83` | 19,220,000.00 USD | 0.00 USD | 199,090.00 USD | `-35.88%` | `70,474.60` |
| `Live` | `Long` | `2.83` | 19,020,000.00 USD | 0.00 USD | 1,140.00 USD | `-35.65%` | `402.50` |
| `Live` | `Long` | `2.85` | 19,020,000.00 USD | 0.00 USD | 28,270.00 USD | `-35.43%` | `9,935.50` |
| `Live` | `Long` | `2.85` | 18,990,000.00 USD | 0.00 USD | 1,860.00 USD | `-35.20%` | `652.60` |
| `Live` | `Long` | `2.87` | 18,990,000.00 USD | 0.00 USD | 5,190.00 USD | `-34.97%` | `1,810.40` |
| `Live` | `Long` | `2.88` | 18,980,000.00 USD | 0.00 USD | 4,150.00 USD | `-34.75%` | `1,443.20` |
| `Live` | `Long` | `2.88` | 18,980,000.00 USD | 0.00 USD | 7,800.00 USD | `-34.52%` | `2,703.30` |
| `Live` | `Long` | `2.90` | 18,970,000.00 USD | 0.00 USD | 13,910.00 USD | `-34.29%` | `4,804.60` |
| `Live` | `Long` | `2.90` | 18,960,000.00 USD | 0.00 USD | 22,330.00 USD | `-34.07%` | `7,685.70` |
| `Live` | `Long` | `2.92` | 18,940,000.00 USD | 0.00 USD | 3,480.00 USD | `-33.84%` | `1,194.70` |
| `Live` | `Long` | `2.94` | 18,930,000.00 USD | 0.00 USD | 37,660.00 USD | `-33.38%` | `12,831.40` |
| `Live` | `Long` | `2.94` | 18,900,000.00 USD | 0.00 USD | 942.11 USD | `-33.16%` | `319.90` |
| `Live` | `Long` | `2.96` | 18,890,000.00 USD | 0.00 USD | 6,210.00 USD | `-32.70%` | `2,093.20` |
| `Live` | `Long` | `2.98` | 18,890,000.00 USD | 0.00 USD | 15,260.00 USD | `-32.48%` | `5,128.80` |
| `Live` | `Long` | `3.00` | 18,870,000.00 USD | 0.00 USD | 9,740.00 USD | `-32.02%` | `3,251.40` |
| `Live` | `Long` | `3.00` | 18,860,000.00 USD | 0.00 USD | 12,330.00 USD | `-31.80%` | `4,103.60` |
| `Live` | `Long` | `3.02` | 18,850,000.00 USD | 0.00 USD | 11,290.00 USD | `-31.57%` | `3,743.00` |
| `Live` | `Long` | `3.02` | 18,840,000.00 USD | 0.00 USD | 22,800.00 USD | `-31.34%` | `7,537.70` |
| `Live` | `Long` | `3.04` | 18,820,000.00 USD | 0.00 USD | 355,760.00 USD | `-31.12%` | `117,219.70` |
| `Live` | `Long` | `3.04` | 18,460,000.00 USD | 0.00 USD | 103,780.00 USD | `-30.89%` | `34,081.60` |
| `Live` | `Long` | `3.06` | 18,360,000.00 USD | 0.00 USD | 25,110.00 USD | `-30.66%` | `8,217.90` |
| `Live` | `Long` | `3.06` | 18,330,000.00 USD | 0.00 USD | 701,010.00 USD | `-30.43%` | `228,715.90` |
| `Live` | `Long` | `3.08` | 17,630,000.00 USD | 0.00 USD | 9,970.00 USD | `-30.21%` | `3,242.60` |
| `Live` | `Long` | `3.08` | 17,620,000.00 USD | 0.00 USD | 12,360.00 USD | `-29.98%` | `4,006.90` |
| `Live` | `Long` | `3.10` | 17,610,000.00 USD | 0.00 USD | 5,510.00 USD | `-29.75%` | `1,779.10` |
| `Live` | `Long` | `3.10` | 17,600,000.00 USD | 0.00 USD | 92,110.00 USD | `-29.53%` | `29,664.00` |
| `Live` | `Long` | `3.12` | 17,510,000.00 USD | 0.00 USD | 107,620.00 USD | `-29.30%` | `34,549.70` |
| `Live` | `Long` | `3.12` | 17,400,000.00 USD | 0.00 USD | 9,270.00 USD | `-29.07%` | `2,967.10` |
| `Live` | `Long` | `3.13` | 17,390,000.00 USD | 0.00 USD | 39,110.00 USD | `-28.85%` | `12,474.20` |
| `Live` | `Long` | `3.15` | 17,360,000.00 USD | 0.00 USD | 19,990.00 USD | `-28.62%` | `6,357.30` |
| `Live` | `Long` | `3.15` | 17,340,000.00 USD | 0.00 USD | 1,110.00 USD | `-28.39%` | `351.60` |
| `Live` | `Long` | `3.17` | 17,330,000.00 USD | 0.00 USD | 8,100.00 USD | `-28.16%` | `2,557.90` |
| `Live` | `Long` | `3.17` | 17,330,000.00 USD | 0.00 USD | 122,100.00 USD | `-27.94%` | `38,457.70` |
| `Live` | `Long` | `3.19` | 17,200,000.00 USD | 0.00 USD | 8,320.00 USD | `-27.71%` | `2,612.90` |
| `Live` | `Long` | `3.19` | 17,200,000.00 USD | 0.00 USD | 354.65 USD | `-27.48%` | `111.00` |
| `Live` | `Long` | `3.21` | 17,200,000.00 USD | 0.00 USD | 218,340.00 USD | `-27.26%` | `68,126.30` |
| `Live` | `Long` | `3.21` | 16,980,000.00 USD | 0.00 USD | 29,190.00 USD | `-27.03%` | `9,078.00` |
| `Live` | `Long` | `3.23` | 16,950,000.00 USD | 0.00 USD | 18,920.00 USD | `-26.80%` | `5,867.90` |
| `Live` | `Long` | `3.23` | 16,930,000.00 USD | 0.00 USD | 35,590.00 USD | `-26.58%` | `11,000.40` |
| `Live` | `Long` | `3.25` | 16,890,000.00 USD | 0.00 USD | 35,080.00 USD | `-26.35%` | `10,811.50` |
| `Live` | `Long` | `3.25` | 16,860,000.00 USD | 0.00 USD | 64,310.00 USD | `-26.12%` | `19,758.60` |
| `Live` | `Long` | `3.27` | 16,790,000.00 USD | 0.00 USD | 47,960.00 USD | `-25.89%` | `14,690.00` |
| `Live` | `Long` | `3.27` | 16,750,000.00 USD | 0.00 USD | 836,280.00 USD | `-25.67%` | `255,353.20` |
| `Live` | `Long` | `3.29` | 15,910,000.00 USD | 0.00 USD | 8,590.00 USD | `-25.44%` | `2,614.20` |
| `Live` | `Long` | `3.29` | 15,900,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-25.21%` | `426,178.00` |
| `Live` | `Long` | `3.31` | 14,500,000.00 USD | 0.00 USD | 69,500.00 USD | `-24.99%` | `21,027.40` |
| `Live` | `Long` | `3.31` | 14,430,000.00 USD | 0.00 USD | 15,580.00 USD | `-24.76%` | `4,698.50` |
| `Live` | `Long` | `3.33` | 14,410,000.00 USD | 0.00 USD | 29,530.00 USD | `-24.53%` | `8,882.40` |
| `Live` | `Long` | `3.33` | 14,380,000.00 USD | 0.00 USD | 51,870.00 USD | `-24.31%` | `15,552.70` |
| `Live` | `Long` | `3.35` | 14,330,000.00 USD | 0.00 USD | 31,120.00 USD | `-24.08%` | `9,303.10` |
| `Live` | `Long` | `3.37` | 14,300,000.00 USD | 0.00 USD | 2,090.00 USD | `-23.63%` | `622.40` |
| `Live` | `Long` | `3.38` | 14,300,000.00 USD | 0.00 USD | 14,490.00 USD | `-23.40%` | `4,293.30` |
| `Live` | `Long` | `3.38` | 14,280,000.00 USD | 0.00 USD | 53,610.00 USD | `-23.17%` | `15,836.30` |
| `Live` | `Long` | `3.40` | 14,230,000.00 USD | 0.00 USD | 12,370.00 USD | `-22.94%` | `3,644.70` |
| `Live` | `Long` | `3.40` | 14,220,000.00 USD | 0.00 USD | 158,490.00 USD | `-22.72%` | `46,545.00` |
| `Live` | `Long` | `3.42` | 14,060,000.00 USD | 0.00 USD | 187,750.00 USD | `-22.49%` | `54,978.40` |
| `Live` | `Long` | `3.42` | 13,870,000.00 USD | 0.00 USD | 50,040.00 USD | `-22.26%` | `14,608.80` |
| `Live` | `Long` | `3.44` | 13,820,000.00 USD | 0.00 USD | 25,570.00 USD | `-22.04%` | `7,445.20` |
| `Live` | `Long` | `3.44` | 13,790,000.00 USD | 0.00 USD | 5,860.00 USD | `-21.81%` | `1,702.30` |
| `Live` | `Long` | `3.46` | 13,790,000.00 USD | 0.00 USD | 10,250.00 USD | `-21.58%` | `2,966.00` |
| `Live` | `Long` | `3.46` | 13,780,000.00 USD | 0.00 USD | 55,000.00 USD | `-21.36%` | `15,874.00` |
| `Live` | `Long` | `3.48` | 13,720,000.00 USD | 0.00 USD | 70,570.00 USD | `-21.13%` | `20,307.20` |
| `Live` | `Long` | `3.48` | 13,650,000.00 USD | 0.00 USD | 26,990.00 USD | `-20.90%` | `7,746.00` |
| `Live` | `Long` | `3.50` | 13,630,000.00 USD | 0.00 USD | 25,280.00 USD | `-20.67%` | `7,234.60` |
| `Live` | `Long` | `3.50` | 13,600,000.00 USD | 0.00 USD | 12,480.00 USD | `-20.45%` | `3,559.80` |
| `Live` | `Long` | `3.52` | 13,590,000.00 USD | 0.00 USD | 17,140.00 USD | `-20.22%` | `4,876.50` |
| `Live` | `Long` | `3.52` | 13,570,000.00 USD | 0.00 USD | 21,970.00 USD | `-19.99%` | `6,232.40` |
| `Live` | `Long` | `3.54` | 13,550,000.00 USD | 0.00 USD | 7,690.00 USD | `-19.77%` | `2,174.60` |
| `Live` | `Long` | `3.54` | 13,540,000.00 USD | 0.00 USD | 325,560.00 USD | `-19.54%` | `91,835.00` |
| `Live` | `Long` | `3.56` | 13,220,000.00 USD | 0.00 USD | 379,650.00 USD | `-19.31%` | `106,791.90` |
| `Live` | `Long` | `3.56` | 12,840,000.00 USD | 0.00 USD | 8,330.00 USD | `-19.09%` | `2,337.60` |
| `Live` | `Long` | `3.58` | 12,830,000.00 USD | 0.00 USD | 135,550.00 USD | `-18.86%` | `37,916.80` |
| `Live` | `Long` | `3.58` | 12,690,000.00 USD | 0.00 USD | 22,500.00 USD | `-18.63%` | `6,276.90` |
| `Live` | `Long` | `3.60` | 12,670,000.00 USD | 0.00 USD | 79,940.00 USD | `-18.40%` | `22,236.30` |
| `Live` | `Long` | `3.60` | 12,590,000.00 USD | 0.00 USD | 165,030.00 USD | `-18.18%` | `45,778.50` |
| `Live` | `Long` | `3.62` | 12,420,000.00 USD | 0.00 USD | 845.19 USD | `-17.95%` | `233.80` |
| `Live` | `Long` | `3.62` | 12,420,000.00 USD | 0.00 USD | 11,540.00 USD | `-17.72%` | `3,182.90` |
| `Live` | `Long` | `3.63` | 12,410,000.00 USD | 0.00 USD | 29,880.00 USD | `-17.50%` | `8,219.00` |
| `Live` | `Long` | `3.65` | 12,380,000.00 USD | 0.00 USD | 513,760.00 USD | `-17.27%` | `140,950.00` |
| `Live` | `Long` | `3.65` | 11,870,000.00 USD | 0.00 USD | 49,270.00 USD | `-17.04%` | `13,480.20` |
| `Live` | `Long` | `3.67` | 11,820,000.00 USD | 0.00 USD | 574,480.00 USD | `-16.82%` | `156,746.40` |
| `Live` | `Long` | `3.67` | 11,250,000.00 USD | 0.00 USD | 189,590.00 USD | `-16.59%` | `51,588.50` |
| `Live` | `Long` | `3.69` | 11,060,000.00 USD | 0.00 USD | 178,360.00 USD | `-16.36%` | `48,400.40` |
| `Live` | `Long` | `3.69` | 10,880,000.00 USD | 0.00 USD | 1,930.00 USD | `-16.14%` | `522.70` |
| `Live` | `Long` | `3.71` | 10,880,000.00 USD | 0.00 USD | 43,110.00 USD | `-15.91%` | `11,636.20` |
| `Live` | `Long` | `3.71` | 10,830,000.00 USD | 0.00 USD | 157,110.00 USD | `-15.68%` | `42,290.20` |
| `Live` | `Long` | `3.73` | 10,670,000.00 USD | 0.00 USD | 27,950.00 USD | `-15.45%` | `7,502.60` |
| `Live` | `Long` | `3.73` | 10,650,000.00 USD | 0.00 USD | 30,770.00 USD | `-15.23%` | `8,239.50` |
| `Live` | `Long` | `3.75` | 10,620,000.00 USD | 0.00 USD | 33,470.00 USD | `-15.00%` | `8,937.00` |
| `Live` | `Long` | `3.75` | 10,580,000.00 USD | 0.00 USD | 99,550.00 USD | `-14.77%` | `26,512.10` |
| `Live` | `Long` | `3.77` | 10,480,000.00 USD | 0.00 USD | 56,700.00 USD | `-14.55%` | `15,059.10` |
| `Live` | `Long` | `3.77` | 10,430,000.00 USD | 0.00 USD | 14,890.00 USD | `-14.32%` | `3,944.40` |
| `Live` | `Long` | `3.79` | 10,410,000.00 USD | 0.00 USD | 38,620.00 USD | `-14.09%` | `10,202.90` |
| `Live` | `Long` | `3.79` | 10,370,000.00 USD | 0.00 USD | 146,150.00 USD | `-13.87%` | `38,511.40` |
| `Live` | `Long` | `3.81` | 10,230,000.00 USD | 0.00 USD | 14,720.00 USD | `-13.64%` | `3,868.60` |
| `Live` | `Long` | `3.81` | 10,210,000.00 USD | 0.00 USD | 77,060.00 USD | `-13.41%` | `20,198.50` |
| `Live` | `Long` | `3.83` | 10,140,000.00 USD | 0.00 USD | 6,620.00 USD | `-13.18%` | `1,732.00` |
| `Live` | `Long` | `3.83` | 10,130,000.00 USD | 0.00 USD | 147,910.00 USD | `-12.96%` | `38,568.30` |
| `Live` | `Long` | `3.85` | 9,980,000.00 USD | 0.00 USD | 24,250.00 USD | `-12.73%` | `6,305.60` |
| `Live` | `Long` | `3.85` | 9,960,000.00 USD | 0.00 USD | 154,310.00 USD | `-12.50%` | `40,028.50` |
| `Live` | `Long` | `3.87` | 9,800,000.00 USD | 0.00 USD | 24,820.00 USD | `-12.28%` | `6,422.20` |
| `Live` | `Long` | `3.88` | 9,780,000.00 USD | 0.00 USD | 4,710.00 USD | `-12.05%` | `1,215.80` |
| `Live` | `Long` | `3.88` | 9,770,000.00 USD | 0.00 USD | 52,710.00 USD | `-11.82%` | `13,566.50` |
| `Live` | `Long` | `3.90` | 9,720,000.00 USD | 0.00 USD | 96,500.00 USD | `-11.60%` | `24,776.00` |
| `Live` | `Long` | `3.90` | 9,620,000.00 USD | 0.00 USD | 6,040.00 USD | `-11.37%` | `1,548.00` |
| `Live` | `Long` | `3.92` | 9,620,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-11.14%` | `1,001,918.60` |
| `Live` | `Long` | `3.92` | 5,690,000.00 USD | 0.00 USD | 331,990.00 USD | `-10.91%` | `84,584.20` |
| `Live` | `Long` | `3.94` | 5,360,000.00 USD | 0.00 USD | 21,330.00 USD | `-10.69%` | `5,420.00` |
| `Live` | `Long` | `3.94` | 5,340,000.00 USD | 0.00 USD | 533,900.00 USD | `-10.46%` | `135,336.70` |
| `Live` | `Long` | `3.96` | 4,810,000.00 USD | 0.00 USD | 13,470.00 USD | `-10.23%` | `3,406.30` |
| `Live` | `Long` | `3.96` | 4,790,000.00 USD | 0.00 USD | 108,840.00 USD | `-10.01%` | `27,450.10` |
| `Live` | `Long` | `3.98` | 4,690,000.00 USD | 0.00 USD | 67,350.00 USD | `-9.78%` | `16,944.00` |
| `Live` | `Long` | `3.98` | 4,620,000.00 USD | 0.00 USD | 61,830.00 USD | `-9.55%` | `15,515.00` |
| `Live` | `Long` | `4.00` | 4,560,000.00 USD | 0.00 USD | 33,890.00 USD | `-9.33%` | `8,483.80` |
| `Live` | `Long` | `4.00` | 4,520,000.00 USD | 0.00 USD | 57,440.00 USD | `-9.10%` | `14,341.30` |
| `Live` | `Long` | `4.01` | 4,460,000.00 USD | 0.00 USD | 11,310.00 USD | `-8.87%` | `2,815.80` |
| `Live` | `Long` | `4.03` | 4,450,000.00 USD | 0.00 USD | 84,020.00 USD | `-8.65%` | `20,873.50` |
| `Live` | `Long` | `4.04` | 4,370,000.00 USD | 0.00 USD | 12,740.00 USD | `-8.42%` | `3,158.30` |
| `Live` | `Long` | `4.04` | 4,360,000.00 USD | 0.00 USD | 33,550.00 USD | `-8.19%` | `8,293.60` |
| `Live` | `Long` | `4.05` | 4,320,000.00 USD | 0.00 USD | 82,940.00 USD | `-7.96%` | `20,453.10` |
| `Live` | `Long` | `4.07` | 4,240,000.00 USD | 0.00 USD | 349,630.00 USD | `-7.74%` | `86,011.00` |
| `Live` | `Long` | `4.08` | 3,890,000.00 USD | 0.00 USD | 302,020.00 USD | `-7.51%` | `74,116.40` |
| `Live` | `Long` | `4.08` | 3,590,000.00 USD | 0.00 USD | 60,670.00 USD | `-7.28%` | `14,851.60` |
| `Live` | `Long` | `4.09` | 3,530,000.00 USD | 0.00 USD | 723,030.00 USD | `-7.06%` | `176,563.10` |
| `Live` | `Long` | `4.11` | 2,800,000.00 USD | 0.00 USD | 124,860.00 USD | `-6.83%` | `30,416.20` |
| `Live` | `Long` | `4.12` | 2,680,000.00 USD | 0.00 USD | 253,880.00 USD | `-6.60%` | `61,696.00` |
| `Live` | `Long` | `4.12` | 2,430,000.00 USD | 0.00 USD | 44,090.00 USD | `-6.38%` | `10,688.50` |
| `Live` | `Long` | `4.13` | 2,380,000.00 USD | 0.00 USD | 101,080.00 USD | `-6.15%` | `24,444.30` |
| `Live` | `Long` | `4.14` | 2,280,000.00 USD | 0.00 USD | 236,880.00 USD | `-5.92%` | `57,147.20` |
| `Live` | `Long` | `4.16` | 2,040,000.00 USD | 0.00 USD | 122,430.00 USD | `-5.69%` | `29,466.30` |
| `Live` | `Long` | `4.17` | 1,920,000.00 USD | 0.00 USD | 466,520.00 USD | `-5.47%` | `112,009.30` |
| `Live` | `Long` | `4.17` | 1,450,000.00 USD | 0.00 USD | 45,840.00 USD | `-5.24%` | `10,978.50` |
| `Live` | `Long` | `4.18` | 1,410,000.00 USD | 0.00 USD | 30,300.00 USD | `-5.01%` | `7,240.90` |
| `Live` | `Long` | `4.20` | 1,380,000.00 USD | 0.00 USD | 101,900.00 USD | `-4.79%` | `24,291.50` |
| `Live` | `Long` | `4.21` | 1,280,000.00 USD | 0.00 USD | 134,680.00 USD | `-4.56%` | `32,028.30` |
| `Live` | `Long` | `4.21` | 1,140,000.00 USD | 0.00 USD | 19,220.00 USD | `-4.33%` | `4,560.30` |
| `Live` | `Long` | `4.22` | 1,120,000.00 USD | 0.00 USD | 49,240.00 USD | `-4.11%` | `11,654.20` |
| `Live` | `Long` | `4.24` | 1,070,000.00 USD | 0.00 USD | 601,150.00 USD | `-3.88%` | `141,947.70` |
| `Live` | `Long` | `4.25` | 472,650.00 USD | 0.00 USD | 12,700.00 USD | `-3.65%` | `2,992.80` |
| `Live` | `Long` | `4.25` | 459,950.00 USD | 0.00 USD | 288,490.00 USD | `-3.42%` | `67,800.70` |
| `Live` | `Long` | `4.26` | 171,460.00 USD | 0.00 USD | 41,020.00 USD | `-3.20%` | `9,616.80` |
| `Live` | `Long` | `4.28` | 130,440.00 USD | 0.00 USD | 6,760.00 USD | `-2.97%` | `1,581.70` |
| `Live` | `Long` | `4.29` | 123,680.00 USD | 0.00 USD | 14,670.00 USD | `-2.74%` | `3,422.50` |
| `Live` | `Long` | `4.29` | 109,010.00 USD | 0.00 USD | 858.14 USD | `-2.52%` | `199.80` |
| `Live` | `Long` | `4.32` | 108,150.00 USD | 0.00 USD | 122.98 USD | `-2.06%` | `28.50` |
| `Live` | `Long` | `4.33` | 108,030.00 USD | 0.00 USD | 5,860.00 USD | `-1.84%` | `1,355.50` |
| `Live` | `Long` | `4.33` | 102,170.00 USD | 0.00 USD | 13,310.00 USD | `-1.61%` | `3,071.20` |
| `Live` | `Long` | `4.34` | 88,860.00 USD | 0.00 USD | 30,420.00 USD | `-1.38%` | `7,000.00` |
| `Live` | `Long` | `4.36` | 58,440.00 USD | 0.00 USD | 1,090.00 USD | `-1.16%` | `251.00` |
| `Live` | `Long` | `4.37` | 57,350.00 USD | 0.00 USD | 56,750.00 USD | `-0.93%` | `13,000.40` |
| `Live` | `Long` | `4.38` | 600.25 USD | 0.00 USD | 600.25 USD | `-0.70%` | `137.20` |
| `Live` | `Short` | `4.39` | 3,660.00 USD | 3,660.00 USD | 0.00 USD | `-0.25%` | `832.00` |
| `Live` | `Short` | `4.59` | 4,100.00 USD | 444.34 USD | 0.00 USD | `+4.29%` | `96.70` |
| `Live` | `Short` | `4.61` | 4,590.00 USD | 484.91 USD | 0.00 USD | `+4.52%` | `105.30` |
| `Live` | `Short` | `4.62` | 38,650.00 USD | 34,060.00 USD | 0.00 USD | `+4.75%` | `7,381.30` |
| `Live` | `Short` | `4.63` | 41,050.00 USD | 2,400.00 USD | 0.00 USD | `+5.20%` | `517.90` |
| `Live` | `Short` | `4.64` | 49,040.00 USD | 7,990.00 USD | 0.00 USD | `+5.43%` | `1,719.40` |
| `Live` | `Short` | `4.66` | 87,370.00 USD | 38,330.00 USD | 0.00 USD | `+5.65%` | `8,234.90` |
| `Live` | `Short` | `4.67` | 212,070.00 USD | 124,700.00 USD | 0.00 USD | `+5.88%` | `26,730.80` |
| `Live` | `Short` | `4.67` | 212,230.00 USD | 154.74 USD | 0.00 USD | `+6.11%` | `33.10` |
| `Live` | `Short` | `4.68` | 227,000.00 USD | 14,780.00 USD | 0.00 USD | `+6.33%` | `3,153.80` |
| `Live` | `Short` | `4.70` | 228,050.00 USD | 1,050.00 USD | 0.00 USD | `+6.56%` | `224.00` |
| `Live` | `Short` | `4.71` | 239,280.00 USD | 11,230.00 USD | 0.00 USD | `+6.79%` | `2,385.80` |
| `Live` | `Short` | `4.71` | 268,800.00 USD | 29,520.00 USD | 0.00 USD | `+7.02%` | `6,261.70` |
| `Live` | `Short` | `4.72` | 272,720.00 USD | 3,920.00 USD | 0.00 USD | `+7.24%` | `830.00` |
| `Live` | `Short` | `4.74` | 277,430.00 USD | 4,700.00 USD | 0.00 USD | `+7.47%` | `993.40` |
| `Live` | `Short` | `4.75` | 290,390.00 USD | 12,960.00 USD | 0.00 USD | `+7.70%` | `2,730.90` |
| `Live` | `Short` | `4.75` | 292,110.00 USD | 1,720.00 USD | 0.00 USD | `+7.92%` | `362.40` |
| `Live` | `Short` | `4.78` | 299,160.00 USD | 7,050.00 USD | 0.00 USD | `+8.38%` | `1,477.00` |
| `Live` | `Short` | `4.79` | 319,570.00 USD | 20,410.00 USD | 0.00 USD | `+8.60%` | `4,266.20` |
| `Live` | `Short` | `4.79` | 873,060.00 USD | 553,480.00 USD | 0.00 USD | `+8.83%` | `115,429.10` |
| `Live` | `Short` | `4.82` | 923,970.00 USD | 50,910.00 USD | 0.00 USD | `+9.29%` | `10,573.00` |
| `Live` | `Short` | `4.83` | 925,710.00 USD | 1,740.00 USD | 0.00 USD | `+9.51%` | `360.90` |
| `Live` | `Short` | `4.83` | 946,780.00 USD | 21,070.00 USD | 0.00 USD | `+9.74%` | `4,358.70` |
| `Live` | `Short` | `4.86` | 968,960.00 USD | 22,180.00 USD | 0.00 USD | `+10.19%` | `4,567.70` |
| `Live` | `Short` | `4.87` | 974,420.00 USD | 5,460.00 USD | 0.00 USD | `+10.42%` | `1,121.90` |
| `Live` | `Short` | `4.88` | 992,660.00 USD | 18,250.00 USD | 0.00 USD | `+10.65%` | `3,743.00` |
| `Live` | `Short` | `4.88` | 993,490.00 USD | 827.03 USD | 0.00 USD | `+10.87%` | `169.30` |
| `Live` | `Short` | `4.91` | 995,120.00 USD | 1,630.00 USD | 0.00 USD | `+11.33%` | `332.30` |
| `Live` | `Short` | `4.92` | 1,020,000.00 USD | 20,720.00 USD | 0.00 USD | `+11.55%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,030,000.00 USD | 12,930.00 USD | 0.00 USD | `+11.78%` | `2,625.70` |
| `Live` | `Short` | `4.93` | 1,030,000.00 USD | 157.43 USD | 0.00 USD | `+12.01%` | `31.90` |
| `Live` | `Short` | `4.96` | 2,380,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+12.46%` | `272,693.70` |
| `Live` | `Short` | `4.97` | 2,480,000.00 USD | 99,810.00 USD | 0.00 USD | `+12.92%` | `20,062.00` |
| `Live` | `Short` | `4.99` | 2,480,000.00 USD | 1,710.00 USD | 0.00 USD | `+13.14%` | `343.70` |
| `Live` | `Short` | `5.00` | 2,480,000.00 USD | 339.66 USD | 0.00 USD | `+13.37%` | `68.00` |
| `Live` | `Short` | `5.00` | 2,480,000.00 USD | 260.76 USD | 0.00 USD | `+13.60%` | `52.10` |
| `Live` | `Short` | `5.01` | 2,850,000.00 USD | 371,590.00 USD | 0.00 USD | `+13.82%` | `74,095.60` |
| `Live` | `Short` | `5.04` | 2,870,000.00 USD | 13,130.00 USD | 0.00 USD | `+14.28%` | `2,607.60` |
| `Live` | `Short` | `5.04` | 2,870,000.00 USD | 1,160.00 USD | 0.00 USD | `+14.51%` | `230.50` |
| `Live` | `Short` | `5.05` | 2,920,000.00 USD | 55,570.00 USD | 0.00 USD | `+14.73%` | `10,993.80` |
| `Live` | `Short` | `5.07` | 2,930,000.00 USD | 3,420.00 USD | 0.00 USD | `+14.96%` | `675.80` |
| `Live` | `Short` | `5.08` | 2,980,000.00 USD | 56,820.00 USD | 0.00 USD | `+15.19%` | `11,196.20` |
| `Live` | `Short` | `5.08` | 2,990,000.00 USD | 3,190.00 USD | 0.00 USD | `+15.41%` | `627.90` |
| `Live` | `Short` | `5.12` | 2,990,000.00 USD | 2,680.00 USD | 0.00 USD | `+16.32%` | `522.30` |
| `Live` | `Short` | `5.13` | 2,990,000.00 USD | 2,110.00 USD | 0.00 USD | `+16.55%` | `410.70` |
| `Live` | `Short` | `5.17` | 2,990,000.00 USD | 317.65 USD | 0.00 USD | `+17.23%` | `61.50` |
| `Live` | `Short` | `5.17` | 2,990,000.00 USD | 346.72 USD | 0.00 USD | `+17.46%` | `67.00` |
| `Live` | `Short` | `5.20` | 3,000,000.00 USD | 7,610.00 USD | 0.00 USD | `+17.91%` | `1,465.10` |
| `Live` | `Short` | `5.21` | 3,900,000.00 USD | 898,120.00 USD | 0.00 USD | `+18.14%` | `172,549.20` |
| `Live` | `Short` | `5.22` | 3,970,000.00 USD | 72,250.00 USD | 0.00 USD | `+18.59%` | `13,828.00` |
| `Live` | `Short` | `5.24` | 4,000,000.00 USD | 29,050.00 USD | 0.00 USD | `+18.82%` | `5,548.60` |
| `Live` | `Short` | `5.25` | 4,000,000.00 USD | 143.71 USD | 0.00 USD | `+19.04%` | `27.40` |
| `Live` | `Short` | `5.25` | 4,000,000.00 USD | 288.50 USD | 0.00 USD | `+19.27%` | `54.90` |
| `Live` | `Short` | `5.26` | 4,010,000.00 USD | 5,610.00 USD | 0.00 USD | `+19.50%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 4,010,000.00 USD | 245.29 USD | 0.00 USD | `+19.73%` | `46.50` |
| `Live` | `Short` | `5.29` | 4,010,000.00 USD | 228.84 USD | 0.00 USD | `+19.95%` | `43.30` |
| `Live` | `Short` | `5.29` | 4,070,000.00 USD | 59,130.00 USD | 0.00 USD | `+20.18%` | `11,166.70` |
| `Live` | `Short` | `5.30` | 4,070,000.00 USD | 524.66 USD | 0.00 USD | `+20.41%` | `98.90` |
| `Live` | `Short` | `5.32` | 4,070,000.00 USD | 878.04 USD | 0.00 USD | `+20.63%` | `165.20` |
| `Live` | `Short` | `5.33` | 4,100,000.00 USD | 37,730.00 USD | 0.00 USD | `+21.09%` | `7,072.30` |
| `Live` | `Short` | `5.34` | 4,120,000.00 USD | 19,840.00 USD | 0.00 USD | `+21.31%` | `3,711.90` |
| `Live` | `Short` | `5.36` | 4,200,000.00 USD | 79,090.00 USD | 0.00 USD | `+21.54%` | `14,770.30` |
| `Live` | `Short` | `5.37` | 4,250,000.00 USD | 41,910.00 USD | 0.00 USD | `+21.77%` | `7,811.90` |
| `Live` | `Short` | `5.38` | 4,250,000.00 USD | 310.68 USD | 0.00 USD | `+22.00%` | `57.80` |
| `Live` | `Short` | `5.43` | 4,250,000.00 USD | 2,320.00 USD | 0.00 USD | `+23.36%` | `427.10` |
| `Live` | `Short` | `5.45` | 4,250,000.00 USD | 2,300.00 USD | 0.00 USD | `+23.58%` | `422.30` |
| `Live` | `Short` | `5.46` | 4,250,000.00 USD | 2,270.00 USD | 0.00 USD | `+24.04%` | `415.20` |
| `Live` | `Short` | `5.47` | 4,510,000.00 USD | 255,740.00 USD | 0.00 USD | `+24.27%` | `46,710.50` |
| `Live` | `Short` | `5.50` | 4,600,000.00 USD | 88,450.00 USD | 0.00 USD | `+24.72%` | `16,097.30` |
| `Live` | `Short` | `5.51` | 4,640,000.00 USD | 39,430.00 USD | 0.00 USD | `+25.17%` | `7,150.20` |
| `Live` | `Short` | `5.54` | 4,640,000.00 USD | 209.22 USD | 0.00 USD | `+25.63%` | `37.80` |
| `Live` | `Short` | `5.57` | 4,640,000.00 USD | 8,670.00 USD | 0.00 USD | `+26.31%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,710,000.00 USD | 62,420.00 USD | 0.00 USD | `+26.76%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 4,760,000.00 USD | 54,260.00 USD | 0.00 USD | `+26.99%` | `9,697.40` |
| `Live` | `Short` | `5.61` | 4,780,000.00 USD | 17,680.00 USD | 0.00 USD | `+27.22%` | `3,153.90` |
| `Live` | `Short` | `5.66` | 4,780,000.00 USD | 301.98 USD | 0.00 USD | `+28.35%` | `53.40` |
| `Live` | `Short` | `5.67` | 4,780,000.00 USD | 211.30 USD | 0.00 USD | `+28.58%` | `37.30` |
| `Live` | `Short` | `5.67` | 4,780,000.00 USD | 1,730.00 USD | 0.00 USD | `+28.80%` | `305.00` |
| `Live` | `Short` | `5.68` | 4,810,000.00 USD | 32,270.00 USD | 0.00 USD | `+29.03%` | `5,676.90` |
| `Live` | `Short` | `5.70` | 4,820,000.00 USD | 6,050.00 USD | 0.00 USD | `+29.26%` | `1,061.60` |
| `Live` | `Short` | `5.71` | 4,820,000.00 USD | 2,130.00 USD | 0.00 USD | `+29.71%` | `372.40` |
| `Live` | `Short` | `5.72` | 4,820,000.00 USD | 738.52 USD | 0.00 USD | `+29.94%` | `129.00` |
| `Live` | `Short` | `5.75` | 4,830,000.00 USD | 9,160.00 USD | 0.00 USD | `+30.39%` | `1,594.40` |
| `Live` | `Short` | `5.75` | 4,830,000.00 USD | 286.02 USD | 0.00 USD | `+30.62%` | `49.70` |
| `Live` | `Short` | `5.79` | 4,830,000.00 USD | 197.27 USD | 0.00 USD | `+31.30%` | `34.10` |
| `Live` | `Short` | `5.82` | 4,920,000.00 USD | 82,870.00 USD | 0.00 USD | `+31.98%` | `14,251.90` |
| `Live` | `Short` | `5.84` | 4,920,000.00 USD | 6,670.00 USD | 0.00 USD | `+32.66%` | `1,141.30` |
| `Live` | `Short` | `5.86` | 4,920,000.00 USD | 370.62 USD | 0.00 USD | `+32.89%` | `63.30` |
| `Live` | `Short` | `5.87` | 4,920,000.00 USD | 604.10 USD | 0.00 USD | `+33.12%` | `103.00` |
| `Live` | `Short` | `5.88` | 4,920,000.00 USD | 855.09 USD | 0.00 USD | `+33.57%` | `145.30` |
| `Live` | `Short` | `5.89` | 5,010,000.00 USD | 89,540.00 USD | 0.00 USD | `+33.80%` | `15,189.10` |
| `Live` | `Short` | `5.92` | 5,010,000.00 USD | 189.28 USD | 0.00 USD | `+34.25%` | `32.00` |
| `Live` | `Short` | `5.95` | 5,010,000.00 USD | 1,400.00 USD | 0.00 USD | `+34.93%` | `234.80` |
| `Live` | `Short` | `5.99` | 5,020,000.00 USD | 131.67 USD | 0.00 USD | `+35.84%` | `22.00` |
| `Live` | `Short` | `6.00` | 5,020,000.00 USD | 1,860.00 USD | 0.00 USD | `+36.07%` | `310.00` |
| `Live` | `Short` | `6.01` | 5,020,000.00 USD | 6,080.00 USD | 0.00 USD | `+36.52%` | `1,010.60` |
| `Live` | `Short` | `6.03` | 5,050,000.00 USD | 23,060.00 USD | 0.00 USD | `+36.75%` | `3,827.40` |
| `Live` | `Short` | `6.04` | 5,180,000.00 USD | 129,280.00 USD | 0.00 USD | `+37.20%` | `21,385.70` |
| `Live` | `Short` | `6.07` | 5,180,000.00 USD | 740.54 USD | 0.00 USD | `+37.66%` | `122.10` |
| `Live` | `Short` | `6.08` | 5,180,000.00 USD | 5,920.00 USD | 0.00 USD | `+38.11%` | `973.10` |
| `Live` | `Short` | `6.09` | 5,220,000.00 USD | 37,510.00 USD | 0.00 USD | `+38.34%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 5,230,000.00 USD | 12,520.00 USD | 0.00 USD | `+38.56%` | `2,050.10` |
| `Live` | `Short` | `6.13` | 5,260,000.00 USD | 24,160.00 USD | 0.00 USD | `+39.25%` | `3,938.70` |
| `Live` | `Short` | `6.16` | 6,410,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+39.70%` | `188,000.00` |
| `Live` | `Short` | `6.18` | 6,740,000.00 USD | 330,920.00 USD | 0.00 USD | `+40.38%` | `53,503.40` |
| `Live` | `Short` | `6.21` | 6,750,000.00 USD | 1,370.00 USD | 0.00 USD | `+41.06%` | `220.40` |
| `Live` | `Short` | `6.25` | 6,750,000.00 USD | 7,610.00 USD | 0.00 USD | `+41.74%` | `1,218.90` |
| `Live` | `Short` | `6.25` | 6,750,000.00 USD | 439.10 USD | 0.00 USD | `+41.97%` | `70.20` |
| `Live` | `Short` | `6.28` | 8,580,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+42.42%` | `290,291.30` |
| `Live` | `Short` | `6.30` | 8,580,000.00 USD | 829.74 USD | 0.00 USD | `+43.10%` | `131.60` |
| `Live` | `Short` | `6.32` | 8,580,000.00 USD | 310.70 USD | 0.00 USD | `+43.33%` | `49.20` |
| `Live` | `Short` | `6.33` | 8,580,000.00 USD | 382.00 USD | 0.00 USD | `+43.78%` | `60.30` |
| `Live` | `Short` | `6.34` | 8,580,000.00 USD | 214.46 USD | 0.00 USD | `+44.01%` | `33.80` |
| `Live` | `Short` | `6.37` | 8,580,000.00 USD | 113.93 USD | 0.00 USD | `+44.47%` | `17.90` |
| `Live` | `Short` | `6.38` | 8,580,000.00 USD | 288.15 USD | 0.00 USD | `+44.69%` | `45.20` |
| `Live` | `Short` | `6.38` | 8,580,000.00 USD | 4,110.00 USD | 0.00 USD | `+44.92%` | `644.40` |
| `Live` | `Short` | `6.41` | 8,590,000.00 USD | 3,780.00 USD | 0.00 USD | `+45.37%` | `590.10` |
| `Live` | `Short` | `6.42` | 8,590,000.00 USD | 943.65 USD | 0.00 USD | `+45.60%` | `147.10` |
| `Live` | `Short` | `6.42` | 8,590,000.00 USD | 346.95 USD | 0.00 USD | `+45.83%` | `54.00` |
| `Live` | `Short` | `6.43` | 9,170,000.00 USD | 584,470.00 USD | 0.00 USD | `+46.05%` | `90,827.50` |
| `Live` | `Short` | `6.45` | 9,260,000.00 USD | 91,940.00 USD | 0.00 USD | `+46.28%` | `14,264.80` |
| `Live` | `Short` | `6.46` | 9,270,000.00 USD | 7,150.00 USD | 0.00 USD | `+46.51%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 9,270,000.00 USD | 1,940.00 USD | 0.00 USD | `+46.74%` | `300.00` |
| `Live` | `Short` | `6.47` | 9,270,000.00 USD | 109.43 USD | 0.00 USD | `+46.96%` | `16.90` |
| `Live` | `Short` | `6.49` | 9,350,000.00 USD | 77,820.00 USD | 0.00 USD | `+47.19%` | `12,000.00` |
| `Live` | `Short` | `6.50` | 9,350,000.00 USD | 325.25 USD | 0.00 USD | `+47.64%` | `50.00` |
| `Live` | `Short` | `6.51` | 9,350,000.00 USD | 536.84 USD | 0.00 USD | `+47.87%` | `82.40` |
| `Live` | `Short` | `6.54` | 9,350,000.00 USD | 697.04 USD | 0.00 USD | `+48.55%` | `106.50` |
| `Live` | `Short` | `6.59` | 9,380,000.00 USD | 29,440.00 USD | 0.00 USD | `+49.69%` | `4,463.60` |
| `Live` | `Short` | `6.66` | 9,770,000.00 USD | 392,810.00 USD | 0.00 USD | `+51.05%` | `59,025.30` |
| `Live` | `Short` | `6.67` | 9,790,000.00 USD | 12,080.00 USD | 0.00 USD | `+51.27%` | `1,812.80` |
| `Live` | `Short` | `6.67` | 9,790,000.00 USD | 200.25 USD | 0.00 USD | `+51.50%` | `30.00` |
| `Live` | `Short` | `6.71` | 9,800,000.00 USD | 15,540.00 USD | 0.00 USD | `+52.41%` | `2,314.50` |
| `Live` | `Short` | `6.72` | 9,920,000.00 USD | 115,670.00 USD | 0.00 USD | `+52.64%` | `17,200.00` |
| `Live` | `Short` | `6.75` | 11,170,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+53.32%` | `184,792.60` |
| `Live` | `Short` | `6.79` | 11,210,000.00 USD | 40,180.00 USD | 0.00 USD | `+54.23%` | `5,912.60` |
| `Live` | `Short` | `6.84` | 11,210,000.00 USD | 474.36 USD | 0.00 USD | `+55.36%` | `69.30` |
| `Live` | `Short` | `6.87` | 11,210,000.00 USD | 3,410.00 USD | 0.00 USD | `+55.81%` | `496.20` |
| `Live` | `Short` | `6.88` | 11,270,000.00 USD | 60,560.00 USD | 0.00 USD | `+56.27%` | `8,796.10` |
| `Live` | `Short` | `6.91` | 11,270,000.00 USD | 189.89 USD | 0.00 USD | `+56.72%` | `27.50` |
| `Live` | `Short` | `6.92` | 11,280,000.00 USD | 6,920.00 USD | 0.00 USD | `+57.18%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 11,280,000.00 USD | 664.27 USD | 0.00 USD | `+58.54%` | `95.10` |
| `Live` | `Short` | `7.03` | 11,320,000.00 USD | 37,400.00 USD | 0.00 USD | `+59.45%` | `5,323.40` |
| `Live` | `Short` | `7.07` | 11,320,000.00 USD | 257.87 USD | 0.00 USD | `+60.35%` | `36.50` |
| `Live` | `Short` | `7.08` | 11,320,000.00 USD | 1,370.00 USD | 0.00 USD | `+60.81%` | `193.30` |
| `Live` | `Short` | `7.21` | 11,330,000.00 USD | 13,560.00 USD | 0.00 USD | `+63.76%` | `1,879.60` |
| `Live` | `Short` | `7.22` | 20,980,000.00 USD | 9,650,000.00 USD | 0.00 USD | `+63.98%` | `1,336,000.00` |
| `Live` | `Short` | `7.24` | 20,990,000.00 USD | 4,910.00 USD | 0.00 USD | `+64.21%` | `679.30` |
| `Live` | `Short` | `7.29` | 20,990,000.00 USD | 772.94 USD | 0.00 USD | `+65.35%` | `106.10` |
| `Live` | `Short` | `7.33` | 20,990,000.00 USD | 1,320.00 USD | 0.00 USD | `+66.48%` | `180.00` |
| `Live` | `Short` | `7.36` | 21,000,000.00 USD | 6,740.00 USD | 0.00 USD | `+66.94%` | `917.00` |
| `Live` | `Short` | `7.38` | 21,000,000.00 USD | 154.35 USD | 0.00 USD | `+67.62%` | `20.90` |
| `Live` | `Short` | `7.41` | 21,000,000.00 USD | 3,220.00 USD | 0.00 USD | `+68.07%` | `434.40` |
| `Live` | `Short` | `7.42` | 21,120,000.00 USD | 121,410.00 USD | 0.00 USD | `+68.52%` | `16,351.90` |
| `Live` | `Short` | `7.46` | 21,120,000.00 USD | 1,420.00 USD | 0.00 USD | `+69.20%` | `191.10` |
| `Live` | `Short` | `7.47` | 21,230,000.00 USD | 107,200.00 USD | 0.00 USD | `+69.66%` | `14,340.70` |
| `Live` | `Short` | `7.50` | 29,020,000.00 USD | 7,790,000.00 USD | 0.00 USD | `+70.11%` | `1,039,604.60` |
| `Live` | `Short` | `7.53` | 29,020,000.00 USD | 1,610.00 USD | 0.00 USD | `+70.79%` | `214.00` |
| `Live` | `Short` | `7.58` | 29,340,000.00 USD | 319,720.00 USD | 0.00 USD | `+72.16%` | `42,151.20` |
| `Live` | `Short` | `7.63` | 29,360,000.00 USD | 19,210.00 USD | 0.00 USD | `+73.29%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 29,360,000.00 USD | 360.25 USD | 0.00 USD | `+73.97%` | `47.00` |
| `Live` | `Short` | `7.70` | 29,390,000.00 USD | 31,690.00 USD | 0.00 USD | `+74.65%` | `4,118.60` |
| `Live` | `Short` | `7.71` | 29,410,000.00 USD | 15,410.00 USD | 0.00 USD | `+74.88%` | `2,000.00` |
| `Live` | `Short` | `7.71` | 29,410,000.00 USD | 2,680.00 USD | 0.00 USD | `+75.11%` | `347.20` |
| `Live` | `Short` | `7.74` | 29,440,000.00 USD | 25,930.00 USD | 0.00 USD | `+75.56%` | `3,352.30` |
| `Live` | `Short` | `7.75` | 29,440,000.00 USD | 629.67 USD | 0.00 USD | `+75.79%` | `81.30` |
| `Live` | `Short` | `7.79` | 29,470,000.00 USD | 33,580.00 USD | 0.00 USD | `+76.92%` | `4,308.50` |
| `Live` | `Short` | `7.82` | 29,470,000.00 USD | 819.01 USD | 0.00 USD | `+77.38%` | `104.80` |
| `Live` | `Short` | `7.87` | 29,480,000.00 USD | 4,280.00 USD | 0.00 USD | `+78.51%` | `544.50` |
| `Live` | `Short` | `7.88` | 29,510,000.00 USD | 27,570.00 USD | 0.00 USD | `+78.96%` | `3,496.50` |
| `Live` | `Short` | `7.95` | 29,510,000.00 USD | 6,120.00 USD | 0.00 USD | `+80.33%` | `769.80` |
| `Live` | `Short` | `7.96` | 29,650,000.00 USD | 134,240.00 USD | 0.00 USD | `+80.78%` | `16,854.30` |
| `Live` | `Short` | `8.03` | 30,080,000.00 USD | 435,420.00 USD | 0.00 USD | `+82.14%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 30,080,000.00 USD | 797.63 USD | 0.00 USD | `+83.05%` | `98.90` |
| `Live` | `Short` | `8.10` | 30,080,000.00 USD | 359.42 USD | 0.00 USD | `+83.73%` | `44.40` |
| `Live` | `Short` | `8.12` | 31,020,000.00 USD | 937,370.00 USD | 0.00 USD | `+84.41%` | `115,368.10` |
| `Live` | `Short` | `8.13` | 31,430,000.00 USD | 409,570.00 USD | 0.00 USD | `+84.64%` | `50,346.40` |
| `Live` | `Short` | `8.14` | 32,160,000.00 USD | 733,050.00 USD | 0.00 USD | `+84.87%` | `90,000.00` |
| `Live` | `Short` | `8.22` | 32,160,000.00 USD | 103.64 USD | 0.00 USD | `+86.68%` | `12.60` |
| `Live` | `Short` | `8.26` | 32,180,000.00 USD | 17,700.00 USD | 0.00 USD | `+87.36%` | `2,144.60` |
| `Live` | `Short` | `8.37` | 33,280,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+89.86%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 33,280,000.00 USD | 577.04 USD | 0.00 USD | `+90.09%` | `68.90` |
| `Live` | `Short` | `8.45` | 33,280,000.00 USD | 3,830.00 USD | 0.00 USD | `+91.67%` | `454.00` |
| `Live` | `Short` | `8.46` | 33,320,000.00 USD | 35,260.00 USD | 0.00 USD | `+92.13%` | `4,165.50` |
| `Live` | `Short` | `8.49` | 33,320,000.00 USD | 594.65 USD | 0.00 USD | `+92.81%` | `70.00` |
| `Live` | `Short` | `8.52` | 33,490,000.00 USD | 172,480.00 USD | 0.00 USD | `+93.26%` | `20,256.10` |
| `Live` | `Short` | `8.53` | 33,490,000.00 USD | 578.85 USD | 0.00 USD | `+93.49%` | `67.90` |
| `Live` | `Short` | `8.54` | 33,520,000.00 USD | 26,620.00 USD | 0.00 USD | `+93.72%` | `3,118.80` |
| `Live` | `Short` | `8.54` | 33,520,000.00 USD | 2,760.00 USD | 0.00 USD | `+93.94%` | `323.50` |
| `Live` | `Short` | `8.57` | 33,520,000.00 USD | 774.32 USD | 0.00 USD | `+94.63%` | `90.30` |
| `Live` | `Short` | `8.64` | 33,550,000.00 USD | 24,890.00 USD | 0.00 USD | `+96.21%` | `2,878.90` |
| `Live` | `Short` | `8.68` | 33,550,000.00 USD | 2,480.00 USD | 0.00 USD | `+96.90%` | `286.00` |
| `Live` | `Short` | `8.71` | 34,000,000.00 USD | 449,960.00 USD | 0.00 USD | `+97.80%` | `51,630.00` |
| `Live` | `Short` | `8.78` | 37,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | `+99.16%` | `389,646.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 4,070,000.00 USD | 0.00 USD | 585.51 USD | `-77.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 4,070,000.00 USD | 0.00 USD | 331.54 USD | `-69.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 4,060,000.00 USD | 0.00 USD | 345.25 USD | `-69.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 4,060,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 4,060,000.00 USD | 0.00 USD | 997.29 USD | `-68.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 4,060,000.00 USD | 0.00 USD | 139.83 USD | `-65.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 4,060,000.00 USD | 0.00 USD | 113.28 USD | `-65.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 4,060,000.00 USD | 0.00 USD | 4,000.00 USD | `-64.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 4,050,000.00 USD | 0.00 USD | 324.22 USD | `-64.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 4,050,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 4,050,000.00 USD | 0.00 USD | 739.67 USD | `-63.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 4,050,000.00 USD | 0.00 USD | 1,740.00 USD | `-63.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 4,050,000.00 USD | 0.00 USD | 6,260.00 USD | `-62.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 4,040,000.00 USD | 0.00 USD | 669.02 USD | `-61.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 4,040,000.00 USD | 0.00 USD | 105.88 USD | `-61.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 4,040,000.00 USD | 0.00 USD | 172.50 USD | `-60.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 4,040,000.00 USD | 0.00 USD | 10,650.00 USD | `-59.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 4,030,000.00 USD | 0.00 USD | 722.00 USD | `-59.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 4,030,000.00 USD | 0.00 USD | 259.00 USD | `-58.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 4,030,000.00 USD | 0.00 USD | 103.84 USD | `-58.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 4,030,000.00 USD | 0.00 USD | 109.00 USD | `-58.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 4,030,000.00 USD | 0.00 USD | 222.19 USD | `-57.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 4,030,000.00 USD | 0.00 USD | 10,280.00 USD | `-57.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 4,020,000.00 USD | 0.00 USD | 558.36 USD | `-56.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 4,020,000.00 USD | 0.00 USD | 1,520.00 USD | `-56.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 4,010,000.00 USD | 0.00 USD | 222.14 USD | `-56.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 4,010,000.00 USD | 0.00 USD | 279.50 USD | `-55.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 4,010,000.00 USD | 0.00 USD | 197.50 USD | `-55.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,010,000.00 USD | 0.00 USD | 935.66 USD | `-54.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,010,000.00 USD | 0.00 USD | 18,860.00 USD | `-54.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,990,000.00 USD | 0.00 USD | 3,020.00 USD | `-54.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,990,000.00 USD | 0.00 USD | 214.52 USD | `-53.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,990,000.00 USD | 0.00 USD | 1,200.00 USD | `-53.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,990,000.00 USD | 0.00 USD | 578.41 USD | `-53.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,990,000.00 USD | 0.00 USD | 18,070.00 USD | `-52.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,970,000.00 USD | 0.00 USD | 13,980.00 USD | `-52.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,960,000.00 USD | 0.00 USD | 107.23 USD | `-52.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,960,000.00 USD | 0.00 USD | 1,590.00 USD | `-51.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,960,000.00 USD | 0.00 USD | 6,970.00 USD | `-51.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,950,000.00 USD | 0.00 USD | 310.32 USD | `-51.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,950,000.00 USD | 0.00 USD | 1,170.00 USD | `-50.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,950,000.00 USD | 0.00 USD | 576.18 USD | `-50.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,950,000.00 USD | 0.00 USD | 295.67 USD | `-50.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,950,000.00 USD | 0.00 USD | 2,940.00 USD | `-49.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,940,000.00 USD | 0.00 USD | 812.68 USD | `-49.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,940,000.00 USD | 0.00 USD | 1,440.00 USD | `-49.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,940,000.00 USD | 0.00 USD | 490.14 USD | `-49.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,940,000.00 USD | 0.00 USD | 13,490.00 USD | `-49.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,930,000.00 USD | 0.00 USD | 478.06 USD | `-48.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,930,000.00 USD | 0.00 USD | 540.88 USD | `-48.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,930,000.00 USD | 0.00 USD | 1,210.00 USD | `-48.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,920,000.00 USD | 0.00 USD | 759.76 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,920,000.00 USD | 0.00 USD | 15,550.00 USD | `-47.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,910,000.00 USD | 0.00 USD | 3,690.00 USD | `-47.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,900,000.00 USD | 0.00 USD | 3,050.00 USD | `-47.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,900,000.00 USD | 0.00 USD | 467.00 USD | `-47.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,900,000.00 USD | 0.00 USD | 506.75 USD | `-46.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,900,000.00 USD | 0.00 USD | 214.27 USD | `-46.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,900,000.00 USD | 0.00 USD | 428.69 USD | `-46.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,900,000.00 USD | 0.00 USD | 322.45 USD | `-45.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,900,000.00 USD | 0.00 USD | 108.25 USD | `-45.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,900,000.00 USD | 0.00 USD | 3,850.00 USD | `-45.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,900,000.00 USD | 0.00 USD | 799.04 USD | `-44.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,890,000.00 USD | 0.00 USD | 6,830.00 USD | `-44.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,890,000.00 USD | 0.00 USD | 137.16 USD | `-44.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,890,000.00 USD | 0.00 USD | 504.41 USD | `-43.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,890,000.00 USD | 0.00 USD | 963.93 USD | `-43.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,890,000.00 USD | 0.00 USD | 13,880.00 USD | `-43.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,870,000.00 USD | 0.00 USD | 541.98 USD | `-42.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,870,000.00 USD | 0.00 USD | 108.75 USD | `-42.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,870,000.00 USD | 0.00 USD | 766.55 USD | `-42.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,870,000.00 USD | 0.00 USD | 1,010.00 USD | `-42.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,870,000.00 USD | 0.00 USD | 1,100.00 USD | `-41.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,870,000.00 USD | 0.00 USD | 100.04 USD | `-41.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 3,870,000.00 USD | 0.00 USD | 5,090.00 USD | `-40.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 3,860,000.00 USD | 0.00 USD | 226.57 USD | `-39.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,860,000.00 USD | 0.00 USD | 104.98 USD | `-39.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 3,860,000.00 USD | 0.00 USD | 7,160.00 USD | `-38.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 3,860,000.00 USD | 0.00 USD | 107.21 USD | `-37.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,860,000.00 USD | 0.00 USD | 197.37 USD | `-37.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,860,000.00 USD | 0.00 USD | 8,390.00 USD | `-37.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,850,000.00 USD | 0.00 USD | 108.39 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,850,000.00 USD | 0.00 USD | 1,270.00 USD | `-37.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,850,000.00 USD | 0.00 USD | 217.23 USD | `-36.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,850,000.00 USD | 0.00 USD | 437.98 USD | `-36.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 3,850,000.00 USD | 0.00 USD | 2,000.00 USD | `-36.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,840,000.00 USD | 0.00 USD | 8,250.00 USD | `-35.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,840,000.00 USD | 0.00 USD | 109.53 USD | `-35.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.87` | 3,840,000.00 USD | 0.00 USD | 1,810.00 USD | `-34.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,830,000.00 USD | 0.00 USD | 437.00 USD | `-34.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,830,000.00 USD | 0.00 USD | 746.06 USD | `-34.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,830,000.00 USD | 0.00 USD | 4,870.00 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,830,000.00 USD | 0.00 USD | 696.98 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,830,000.00 USD | 0.00 USD | 358.90 USD | `-33.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,830,000.00 USD | 0.00 USD | 15,370.00 USD | `-33.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,810,000.00 USD | 0.00 USD | 523.32 USD | `-32.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 3,810,000.00 USD | 0.00 USD | 2,330.00 USD | `-32.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 3,810,000.00 USD | 0.00 USD | 16,090.00 USD | `-31.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,790,000.00 USD | 0.00 USD | 1,020.00 USD | `-31.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,790,000.00 USD | 0.00 USD | 345.76 USD | `-31.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,790,000.00 USD | 0.00 USD | 214.57 USD | `-31.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,790,000.00 USD | 0.00 USD | 109.42 USD | `-30.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 3,790,000.00 USD | 0.00 USD | 721.58 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 3,790,000.00 USD | 0.00 USD | 9,300.00 USD | `-29.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,780,000.00 USD | 0.00 USD | 104.69 USD | `-29.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 3,780,000.00 USD | 0.00 USD | 315.69 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,780,000.00 USD | 0.00 USD | 214.17 USD | `-28.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,780,000.00 USD | 0.00 USD | 641.10 USD | `-28.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,780,000.00 USD | 0.00 USD | 212.06 USD | `-28.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,780,000.00 USD | 0.00 USD | 1,030.00 USD | `-27.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 3,780,000.00 USD | 0.00 USD | 218.81 USD | `-27.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,780,000.00 USD | 0.00 USD | 31,570.00 USD | `-27.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,750,000.00 USD | 0.00 USD | 144.67 USD | `-27.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 3,750,000.00 USD | 0.00 USD | 2,020.00 USD | `-26.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 3,740,000.00 USD | 0.00 USD | 104.81 USD | `-25.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 3,740,000.00 USD | 0.00 USD | 1,150.00 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 3,740,000.00 USD | 0.00 USD | 1,070.00 USD | `-25.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 3,740,000.00 USD | 0.00 USD | 15,820.00 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 3,730,000.00 USD | 0.00 USD | 240.67 USD | `-24.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 3,730,000.00 USD | 0.00 USD | 306.56 USD | `-24.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 3,730,000.00 USD | 0.00 USD | 1,670.00 USD | `-24.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 3,720,000.00 USD | 0.00 USD | 505.76 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 3,720,000.00 USD | 0.00 USD | 73,220.00 USD | `-23.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 3,650,000.00 USD | 0.00 USD | 12,850.00 USD | `-23.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 3,640,000.00 USD | 0.00 USD | 8,490.00 USD | `-22.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 3,630,000.00 USD | 0.00 USD | 3,320.00 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 3,630,000.00 USD | 0.00 USD | 25,250.00 USD | `-22.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 3,600,000.00 USD | 0.00 USD | 506.22 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 3,600,000.00 USD | 0.00 USD | 171.75 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 3,600,000.00 USD | 0.00 USD | 2,550.00 USD | `-21.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 3,600,000.00 USD | 0.00 USD | 1,380.00 USD | `-21.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 3,600,000.00 USD | 0.00 USD | 344.07 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 3,590,000.00 USD | 0.00 USD | 1,950.00 USD | `-20.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 3,590,000.00 USD | 0.00 USD | 112,400.00 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 3,480,000.00 USD | 0.00 USD | 17,360.00 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 3,460,000.00 USD | 0.00 USD | 2,030.00 USD | `-19.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 3,460,000.00 USD | 0.00 USD | 12,040.00 USD | `-19.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 3,450,000.00 USD | 0.00 USD | 633.50 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 3,450,000.00 USD | 0.00 USD | 333.68 USD | `-19.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,450,000.00 USD | 0.00 USD | 72,860.00 USD | `-18.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,380,000.00 USD | 0.00 USD | 179.25 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,380,000.00 USD | 0.00 USD | 643.50 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,370,000.00 USD | 0.00 USD | 1,870.00 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,370,000.00 USD | 0.00 USD | 632.99 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,370,000.00 USD | 0.00 USD | 172.19 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 3,370,000.00 USD | 0.00 USD | 13,400.00 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,360,000.00 USD | 0.00 USD | 179.33 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,360,000.00 USD | 0.00 USD | 3,900.00 USD | `-17.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,350,000.00 USD | 0.00 USD | 174.09 USD | `-16.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,350,000.00 USD | 0.00 USD | 546.47 USD | `-16.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,350,000.00 USD | 0.00 USD | 836.50 USD | `-16.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,350,000.00 USD | 0.00 USD | 4,370.00 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,350,000.00 USD | 0.00 USD | 76,950.00 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,270,000.00 USD | 0.00 USD | 179.06 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,270,000.00 USD | 0.00 USD | 1,030.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,270,000.00 USD | 0.00 USD | 44,700.00 USD | `-15.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 3,230,000.00 USD | 0.00 USD | 180.13 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 3,230,000.00 USD | 0.00 USD | 18,440.00 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,210,000.00 USD | 0.00 USD | 6,850.00 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,200,000.00 USD | 0.00 USD | 3,940.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,200,000.00 USD | 0.00 USD | 359.57 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,200,000.00 USD | 0.00 USD | 1,900.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,190,000.00 USD | 0.00 USD | 1,420.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,190,000.00 USD | 0.00 USD | 18,780.00 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,170,000.00 USD | 0.00 USD | 23,420.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,150,000.00 USD | 0.00 USD | 2,240.00 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,150,000.00 USD | 0.00 USD | 2,100.00 USD | `-12.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,150,000.00 USD | 0.00 USD | 3,070.00 USD | `-12.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 3,140,000.00 USD | 0.00 USD | 2,640.00 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,140,000.00 USD | 0.00 USD | 5,730.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,130,000.00 USD | 0.00 USD | 4,990.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,130,000.00 USD | 0.00 USD | 1,310.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,130,000.00 USD | 0.00 USD | 32,470.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,100,000.00 USD | 0.00 USD | 4,950.00 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,090,000.00 USD | 0.00 USD | 123.24 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,090,000.00 USD | 0.00 USD | 1,420.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,090,000.00 USD | 0.00 USD | 187.78 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,090,000.00 USD | 0.00 USD | 14,250.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,070,000.00 USD | 0.00 USD | 2,350.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 3,070,000.00 USD | 0.00 USD | 4,570.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 3,070,000.00 USD | 0.00 USD | 3,950.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 3,060,000.00 USD | 0.00 USD | 513.36 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 3,060,000.00 USD | 0.00 USD | 248,710.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 2,810,000.00 USD | 0.00 USD | 5,440.00 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 2,810,000.00 USD | 0.00 USD | 4,510.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,800,000.00 USD | 0.00 USD | 2,100.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,800,000.00 USD | 0.00 USD | 7,600.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 2,800,000.00 USD | 0.00 USD | 1,850.00 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 2,790,000.00 USD | 0.00 USD | 485.36 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,790,000.00 USD | 0.00 USD | 504,780.00 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,290,000.00 USD | 0.00 USD | 74,820.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 2,210,000.00 USD | 0.00 USD | 1,370.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 2,210,000.00 USD | 0.00 USD | 722,820.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 1,490,000.00 USD | 0.00 USD | 3,150.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 1,490,000.00 USD | 0.00 USD | 10,440.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 1,480,000.00 USD | 0.00 USD | 351,730.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 1,120,000.00 USD | 0.00 USD | 1,910.00 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 1,120,000.00 USD | 0.00 USD | 36,660.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,090,000.00 USD | 0.00 USD | 2,830.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,080,000.00 USD | 0.00 USD | 31,360.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 1,050,000.00 USD | 0.00 USD | 25,690.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 1,030,000.00 USD | 0.00 USD | 34,210.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 990,920.00 USD | 0.00 USD | 143,590.00 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 847,320.00 USD | 0.00 USD | 51,290.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 796,030.00 USD | 0.00 USD | 53,170.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 742,860.00 USD | 0.00 USD | 47,940.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 694,920.00 USD | 0.00 USD | 23,910.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 671,010.00 USD | 0.00 USD | 37,490.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 633,530.00 USD | 0.00 USD | 15,070.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 618,460.00 USD | 0.00 USD | 22,700.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 595,760.00 USD | 0.00 USD | 12,220.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 583,550.00 USD | 0.00 USD | 1,880.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 581,670.00 USD | 0.00 USD | 21,480.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 560,180.00 USD | 0.00 USD | 68,200.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 491,990.00 USD | 0.00 USD | 5,390.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 486,600.00 USD | 0.00 USD | 7,550.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 479,040.00 USD | 0.00 USD | 142,930.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.36` | 336,120.00 USD | 0.00 USD | 753.85 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.37` | 335,360.00 USD | 0.00 USD | 93,230.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 242,130.00 USD | 0.00 USD | 100.62 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 242,030.00 USD | 0.00 USD | 48,030.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.39` | 194,000.00 USD | 0.00 USD | 123,630.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.41` | 70,370.00 USD | 0.00 USD | 70,370.00 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 14,620.00 USD | 14,620.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 16,900.00 USD | 2,280.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 17,330.00 USD | 428.86 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 17,820.00 USD | 494.28 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 44,160.00 USD | 26,340.00 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 50,630.00 USD | 6,480.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 50,790.00 USD | 151.70 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 95,940.00 USD | 45,160.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 111,070.00 USD | 15,120.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 120,620.00 USD | 9,550.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 133,710.00 USD | 13,100.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 188,800.00 USD | 55,080.00 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 320,560.00 USD | 131,760.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 355,570.00 USD | 35,020.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 361,760.00 USD | 6,190.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 377,790.00 USD | 16,030.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 423,540.00 USD | 45,750.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 425,200.00 USD | 1,660.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 425,330.00 USD | 128.66 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 446,270.00 USD | 20,930.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 457,680.00 USD | 11,410.00 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 457,930.00 USD | 255.30 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 501,890.00 USD | 43,960.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 502,640.00 USD | 750.17 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 523,520.00 USD | 20,880.00 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 912,550.00 USD | 389,020.00 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 912,650.00 USD | 104.25 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 922,750.00 USD | 10,100.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 923,190.00 USD | 446.96 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,370,000.00 USD | 447,830.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,590,000.00 USD | 222,660.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,600,000.00 USD | 3,650.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,770,000.00 USD | 173,390.00 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,790,000.00 USD | 18,750.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,820,000.00 USD | 28,300.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,830,000.00 USD | 14,250.00 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,840,000.00 USD | 10,230.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,680,000.00 USD | 833,790.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,680,000.00 USD | 1,550.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 2,860,000.00 USD | 180,220.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,870,000.00 USD | 7,720.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,880,000.00 USD | 13,340.00 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,880,000.00 USD | 1,210.00 USD | 0.00 USD | `+9.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 2,890,000.00 USD | 14,780.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 2,930,000.00 USD | 38,580.00 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 2,960,000.00 USD | 23,780.00 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,970,000.00 USD | 10,850.00 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,980,000.00 USD | 9,810.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 2,980,000.00 USD | 4,060.00 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,100,000.00 USD | 120,040.00 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,100,000.00 USD | 529.84 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,120,000.00 USD | 12,520.00 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,130,000.00 USD | 11,650.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,130,000.00 USD | 313.51 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,130,000.00 USD | 5,070.00 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,180,000.00 USD | 47,350.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,180,000.00 USD | 187.06 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,280,000.00 USD | 97,210.00 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,290,000.00 USD | 11,390.00 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,340,000.00 USD | 51,180.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,370,000.00 USD | 26,480.00 USD | 0.00 USD | `+13.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,370,000.00 USD | 5,140.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,550,000.00 USD | 176,320.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,550,000.00 USD | 104.94 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,600,000.00 USD | 50,950.00 USD | 0.00 USD | `+14.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,600,000.00 USD | 3,660.00 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,690,000.00 USD | 90,150.00 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,580,000.00 USD | 882,870.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,580,000.00 USD | 547.20 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,630,000.00 USD | 52,010.00 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,640,000.00 USD | 15,350.00 USD | 0.00 USD | `+16.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,640,000.00 USD | 113.26 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,650,000.00 USD | 10,650.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,660,000.00 USD | 3,670.00 USD | 0.00 USD | `+16.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,660,000.00 USD | 3,910.00 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,660,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,660,000.00 USD | 327.58 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,670,000.00 USD | 2,190.00 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,670,000.00 USD | 150.14 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,700,000.00 USD | 36,730.00 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,700,000.00 USD | 1,710.00 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,820,000.00 USD | 120,710.00 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,820,000.00 USD | 537.61 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,350,000.00 USD | 530,070.00 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 5,360,000.00 USD | 5,540.00 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 5,360,000.00 USD | 589.22 USD | 0.00 USD | `+19.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,360,000.00 USD | 733.03 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,360,000.00 USD | 693.64 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,430,000.00 USD | 69,810.00 USD | 0.00 USD | `+20.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,430,000.00 USD | 381.09 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,430,000.00 USD | 961.16 USD | 0.00 USD | `+20.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,440,000.00 USD | 1,570.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,440,000.00 USD | 6,220.00 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,550,000.00 USD | 108,270.00 USD | 0.00 USD | `+21.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,550,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,550,000.00 USD | 438.60 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,560,000.00 USD | 5,000.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,600,000.00 USD | 43,730.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,710,000.00 USD | 105,340.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,710,000.00 USD | 425.62 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,740,000.00 USD | 36,790.00 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,760,000.00 USD | 13,190.00 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,780,000.00 USD | 20,460.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,000,000.00 USD | 219,590.00 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 6,030,000.00 USD | 35,450.00 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 6,080,000.00 USD | 45,900.00 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,080,000.00 USD | 1,180.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,210,000.00 USD | 134,580.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,220,000.00 USD | 5,600.00 USD | 0.00 USD | `+25.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,270,000.00 USD | 45,680.00 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,280,000.00 USD | 18,790.00 USD | 0.00 USD | `+25.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,360,000.00 USD | 74,260.00 USD | 0.00 USD | `+25.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,410,000.00 USD | 49,440.00 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,420,000.00 USD | 14,320.00 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,430,000.00 USD | 5,560.00 USD | 0.00 USD | `+26.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,450,000.00 USD | 20,540.00 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,450,000.00 USD | 384.94 USD | 0.00 USD | `+26.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,450,000.00 USD | 4,170.00 USD | 0.00 USD | `+27.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,460,000.00 USD | 5,510.00 USD | 0.00 USD | `+27.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,460,000.00 USD | 581.53 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,460,000.00 USD | 295.23 USD | 0.00 USD | `+28.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,460,000.00 USD | 3,290.00 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,460,000.00 USD | 281.55 USD | 0.00 USD | `+28.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,470,000.00 USD | 9,380.00 USD | 0.00 USD | `+28.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,480,000.00 USD | 5,860.00 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,590,000.00 USD | 116,400.00 USD | 0.00 USD | `+29.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,600,000.00 USD | 2,210.00 USD | 0.00 USD | `+29.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,600,000.00 USD | 5,720.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,630,000.00 USD | 24,730.00 USD | 0.00 USD | `+30.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,630,000.00 USD | 2,430.00 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,630,000.00 USD | 286.94 USD | 0.00 USD | `+31.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,640,000.00 USD | 7,120.00 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,640,000.00 USD | 6,030.00 USD | 0.00 USD | `+31.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,640,000.00 USD | 1,970.00 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,650,000.00 USD | 3,100.00 USD | 0.00 USD | `+32.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,650,000.00 USD | 1,150.00 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,650,000.00 USD | 4,290.00 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,660,000.00 USD | 3,450.00 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,660,000.00 USD | 345.45 USD | 0.00 USD | `+33.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,710,000.00 USD | 51,960.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,710,000.00 USD | 1,790.00 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,710,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,850,000.00 USD | 136,500.00 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,870,000.00 USD | 19,370.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,870,000.00 USD | 5,620.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,880,000.00 USD | 9,410.00 USD | 0.00 USD | `+35.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,000,000.00 USD | 119,340.00 USD | 0.00 USD | `+35.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,010,000.00 USD | 3,000.00 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,120,000.00 USD | 118,500.00 USD | 0.00 USD | `+36.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,140,000.00 USD | 13,610.00 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,230,000.00 USD | 90,380.00 USD | 0.00 USD | `+36.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,230,000.00 USD | 2,030.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,230,000.00 USD | 3,300.00 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,240,000.00 USD | 2,550.00 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,240,000.00 USD | 425.76 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,240,000.00 USD | 2,030.00 USD | 0.00 USD | `+37.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,240,000.00 USD | 4,120.00 USD | 0.00 USD | `+38.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,240,000.00 USD | 2,000.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,310,000.00 USD | 61,050.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,310,000.00 USD | 6,870.00 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,310,000.00 USD | 1,200.00 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,330,000.00 USD | 11,620.00 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,330,000.00 USD | 1,940.00 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,330,000.00 USD | 1,410.00 USD | 0.00 USD | `+39.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,330,000.00 USD | 4,010.00 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,340,000.00 USD | 3,960.00 USD | 0.00 USD | `+40.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,340,000.00 USD | 3,830.00 USD | 0.00 USD | `+40.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,410,000.00 USD | 66,850.00 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,410,000.00 USD | 1,890.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,410,000.00 USD | 195.46 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,420,000.00 USD | 7,480.00 USD | 0.00 USD | `+41.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,420,000.00 USD | 3,670.00 USD | 0.00 USD | `+42.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,420,000.00 USD | 3,680.00 USD | 0.00 USD | `+42.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,430,000.00 USD | 7,370.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,430,000.00 USD | 412.37 USD | 0.00 USD | `+43.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,430,000.00 USD | 602.77 USD | 0.00 USD | `+43.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,430,000.00 USD | 449.79 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,440,000.00 USD | 2,810.00 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,440,000.00 USD | 3,560.00 USD | 0.00 USD | `+44.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,440,000.00 USD | 3,230.00 USD | 0.00 USD | `+45.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,450,000.00 USD | 5,120.00 USD | 0.00 USD | `+45.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,450,000.00 USD | 613.26 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,450,000.00 USD | 1,310.00 USD | 0.00 USD | `+47.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,490,000.00 USD | 43,090.00 USD | 0.00 USD | `+47.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,490,000.00 USD | 234.54 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,510,000.00 USD | 14,070.00 USD | 0.00 USD | `+48.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,510,000.00 USD | 1,630.00 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,510,000.00 USD | 2,390.00 USD | 0.00 USD | `+49.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,510,000.00 USD | 1,620.00 USD | 0.00 USD | `+50.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,520,000.00 USD | 1,970.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,520,000.00 USD | 3,220.00 USD | 0.00 USD | `+50.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.66` | 7,520,000.00 USD | 1,950.00 USD | 0.00 USD | `+51.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,520,000.00 USD | 450.55 USD | 0.00 USD | `+51.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,520,000.00 USD | 3,060.00 USD | 0.00 USD | `+51.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,530,000.00 USD | 1,930.00 USD | 0.00 USD | `+51.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,530,000.00 USD | 3,070.00 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,530,000.00 USD | 1,920.00 USD | 0.00 USD | `+52.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,530,000.00 USD | 3,120.00 USD | 0.00 USD | `+52.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,540,000.00 USD | 1,550.00 USD | 0.00 USD | `+53.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,540,000.00 USD | 3,080.00 USD | 0.00 USD | `+53.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,540,000.00 USD | 647.56 USD | 0.00 USD | `+54.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,540,000.00 USD | 1,420.00 USD | 0.00 USD | `+54.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,540,000.00 USD | 2,130.00 USD | 0.00 USD | `+54.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,550,000.00 USD | 3,140.00 USD | 0.00 USD | `+54.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,550,000.00 USD | 342.25 USD | 0.00 USD | `+55.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,550,000.00 USD | 1,830.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,550,000.00 USD | 2,990.00 USD | 0.00 USD | `+55.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,550,000.00 USD | 2,970.00 USD | 0.00 USD | `+56.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,550,000.00 USD | 391.51 USD | 0.00 USD | `+56.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,550,000.00 USD | 504.21 USD | 0.00 USD | `+57.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,550,000.00 USD | 166.00 USD | 0.00 USD | `+58.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,560,000.00 USD | 4,190.00 USD | 0.00 USD | `+58.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,570,000.00 USD | 15,610.00 USD | 0.00 USD | `+58.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,580,000.00 USD | 1,750.00 USD | 0.00 USD | `+59.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,580,000.00 USD | 2,860.00 USD | 0.00 USD | `+59.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,580,000.00 USD | 264.31 USD | 0.00 USD | `+61.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,580,000.00 USD | 599.34 USD | 0.00 USD | `+61.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,580,000.00 USD | 193.19 USD | 0.00 USD | `+62.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,580,000.00 USD | 3,950.00 USD | 0.00 USD | `+63.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,590,000.00 USD | 1,940.00 USD | 0.00 USD | `+63.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.22` | 7,590,000.00 USD | 1,770.00 USD | 0.00 USD | `+63.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,750,000.00 USD | 160,550.00 USD | 0.00 USD | `+64.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,750,000.00 USD | 1,750.00 USD | 0.00 USD | `+65.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,750,000.00 USD | 731.50 USD | 0.00 USD | `+66.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,750,000.00 USD | 1,730.00 USD | 0.00 USD | `+66.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,750,000.00 USD | 1,710.00 USD | 0.00 USD | `+67.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,760,000.00 USD | 7,870.00 USD | 0.00 USD | `+67.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,760,000.00 USD | 630.05 USD | 0.00 USD | `+67.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,770,000.00 USD | 2,610.00 USD | 0.00 USD | `+68.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,770,000.00 USD | 7,770.00 USD | 0.00 USD | `+70.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,780,000.00 USD | 1,620.00 USD | 0.00 USD | `+71.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,780,000.00 USD | 4,640.00 USD | 0.00 USD | `+71.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,780,000.00 USD | 371.88 USD | 0.00 USD | `+72.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,780,000.00 USD | 2,510.00 USD | 0.00 USD | `+72.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,780,000.00 USD | 380.68 USD | 0.00 USD | `+74.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,780,000.00 USD | 133.12 USD | 0.00 USD | `+74.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,780,000.00 USD | 1,490.00 USD | 0.00 USD | `+76.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,790,000.00 USD | 1,470.00 USD | 0.00 USD | `+76.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,800,000.00 USD | 11,170.00 USD | 0.00 USD | `+76.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,830,000.00 USD | 34,360.00 USD | 0.00 USD | `+77.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,830,000.00 USD | 399.35 USD | 0.00 USD | `+77.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,830,000.00 USD | 100.29 USD | 0.00 USD | `+77.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 7,830,000.00 USD | 1,550.00 USD | 0.00 USD | `+78.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,840,000.00 USD | 10,610.00 USD | 0.00 USD | `+80.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,840,000.00 USD | 309.43 USD | 0.00 USD | `+81.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,980,000.00 USD | 134,430.00 USD | 0.00 USD | `+81.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 8,060,000.00 USD | 81,310.00 USD | 0.00 USD | `+82.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 8,060,000.00 USD | 1,390.00 USD | 0.00 USD | `+84.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 8,060,000.00 USD | 216.90 USD | 0.00 USD | `+85.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 8,060,000.00 USD | 738.45 USD | 0.00 USD | `+86.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 8,060,000.00 USD | 1,350.00 USD | 0.00 USD | `+88.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 8,120,000.00 USD | 56,000.00 USD | 0.00 USD | `+90.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 8,120,000.00 USD | 1,260.00 USD | 0.00 USD | `+90.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 8,220,000.00 USD | 103,010.00 USD | 0.00 USD | `+90.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 8,230,000.00 USD | 1,330.00 USD | 0.00 USD | `+91.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 8,230,000.00 USD | 721.22 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 8,230,000.00 USD | 2,010.00 USD | 0.00 USD | `+95.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 8,230,000.00 USD | 596.33 USD | 0.00 USD | `+96.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 8,230,000.00 USD | 3,670.00 USD | 0.00 USD | `+96.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 8,240,000.00 USD | 5,270.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 8,240,000.00 USD | 1,600.00 USD | 0.00 USD | `+99.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 8,240,000.00 USD | 3,430.00 USD | 0.00 USD | `+99.85%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.86` | 31,040,000.00 USD | 0.00 USD | 31,040,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 16,690,000.00 USD | 0.00 USD | 16,690,000.00 USD | 1,250.00 USD | 24,120.00 USD | 53,950.00 USD |
| `7D` | `3.87` | 30,960,000.00 USD | 0.00 USD | 30,960,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD |
| `1D` | `3.88` | 16,610,000.00 USD | 0.00 USD | 16,610,000.00 USD | 74,500.00 USD | 6,860.00 USD | 30,440.00 USD |
| `7D` | `3.88` | 30,880,000.00 USD | 0.00 USD | 30,880,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 112,190.00 USD | 37,150.00 USD | 21,950.00 USD |
| `7D` | `3.89` | 30,660,000.00 USD | 0.00 USD | 30,660,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,220.00 USD |
| `1D` | `3.90` | 16,330,000.00 USD | 0.00 USD | 16,330,000.00 USD | 335.10 USD | 10,910.00 USD | 20,820.00 USD |
| `7D` | `3.90` | 30,610,000.00 USD | 0.00 USD | 30,610,000.00 USD | 171,750.00 USD | 28,250.00 USD | 49,490.00 USD |
| `1D` | `3.91` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 0.00 USD | 35,760.00 USD | 34,570.00 USD |
| `7D` | `3.91` | 30,360,000.00 USD | 0.00 USD | 30,360,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 145,280.00 USD | 26,030.00 USD | 30,180.00 USD |
| `7D` | `3.92` | 30,280,000.00 USD | 0.00 USD | 30,280,000.00 USD | 90,780.00 USD | 41,330.00 USD | 80,310.00 USD |
| `1D` | `3.93` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 0.00 USD | 21,500.00 USD | 11,530.00 USD |
| `7D` | `3.93` | 30,070,000.00 USD | 0.00 USD | 30,070,000.00 USD | 51,660.00 USD | 20,780.00 USD | 50,110.00 USD |
| `1D` | `3.94` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 0.00 USD | 6,420.00 USD | 16,960.00 USD |
| `7D` | `3.94` | 29,950,000.00 USD | 0.00 USD | 29,950,000.00 USD | 75,150.00 USD | 31,050.00 USD | 126,320.00 USD |
| `1D` | `3.95` | 15,970,000.00 USD | 0.00 USD | 15,970,000.00 USD | 12,850.00 USD | 5,610.00 USD | 131.75 USD |
| `7D` | `3.95` | 29,720,000.00 USD | 0.00 USD | 29,720,000.00 USD | 8,490.00 USD | 19,870.00 USD | 696.53 USD |
| `1D` | `3.96` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 35,990.00 USD | 29,270.00 USD | 34,820.00 USD |
| `7D` | `3.96` | 29,690,000.00 USD | 0.00 USD | 29,690,000.00 USD | 52,720.00 USD | 15,590.00 USD | 126,470.00 USD |
| `1D` | `3.97` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 156,200.00 USD | 52,430.00 USD | 65,830.00 USD |
| `7D` | `3.97` | 29,490,000.00 USD | 0.00 USD | 29,490,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD |
| `1D` | `3.98` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 46,870.00 USD | 30,290.00 USD | 10,090.00 USD |
| `7D` | `3.98` | 28,890,000.00 USD | 0.00 USD | 28,890,000.00 USD | 31,450.00 USD | 77,970.00 USD | 85,840.00 USD |
| `1D` | `3.99` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 93,820.00 USD | 12,310.00 USD | 47,420.00 USD |
| `7D` | `3.99` | 28,690,000.00 USD | 0.00 USD | 28,690,000.00 USD | 63,200.00 USD | 82,870.00 USD | 101,260.00 USD |
| `1D` | `4.00` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 35,430.00 USD | 7,330.00 USD | 19,440.00 USD |
| `7D` | `4.00` | 28,450,000.00 USD | 0.00 USD | 28,450,000.00 USD | 317,210.00 USD | 98,320.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 109,160.00 USD | 56,050.00 USD | 73,760.00 USD |
| `7D` | `4.01` | 27,860,000.00 USD | 0.00 USD | 27,860,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,560.00 USD |
| `1D` | `4.02` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 60,540.00 USD | 20,960.00 USD | 75,320.00 USD |
| `7D` | `4.02` | 26,950,000.00 USD | 0.00 USD | 26,950,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD |
| `1D` | `4.03` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 23,550.00 USD | 40,450.00 USD | 34,730.00 USD |
| `7D` | `4.03` | 26,380,000.00 USD | 0.00 USD | 26,380,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD |
| `1D` | `4.04` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 28,720.00 USD | 32,610.00 USD | 127,520.00 USD |
| `7D` | `4.04` | 25,940,000.00 USD | 0.00 USD | 25,940,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD |
| `1D` | `4.05` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,260.00 USD |
| `7D` | `4.05` | 25,650,000.00 USD | 0.00 USD | 25,650,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,910.00 USD |
| `1D` | `4.06` | 14,490,000.00 USD | 0.00 USD | 14,490,000.00 USD | 56,670.00 USD | 0.00 USD | 23,190.00 USD |
| `7D` | `4.06` | 25,310,000.00 USD | 0.00 USD | 25,310,000.00 USD | 198,550.00 USD | 45,470.00 USD | 125,420.00 USD |
| `1D` | `4.07` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 3,220.00 USD | 15,020.00 USD | 22,690.00 USD |
| `7D` | `4.07` | 24,940,000.00 USD | 0.00 USD | 24,940,000.00 USD | 183,890.00 USD | 35,750.00 USD | 41,640.00 USD |
| `1D` | `4.08` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 3,880.00 USD | 18,060.00 USD | 15,840.00 USD |
| `7D` | `4.08` | 24,680,000.00 USD | 0.00 USD | 24,680,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD |
| `1D` | `4.09` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 10,540.00 USD | 6,980.00 USD | 1,280.00 USD |
| `7D` | `4.09` | 24,380,000.00 USD | 0.00 USD | 24,380,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,250.00 USD |
| `1D` | `4.10` | 14,310,000.00 USD | 0.00 USD | 14,310,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,260.00 USD |
| `7D` | `4.10` | 24,170,000.00 USD | 0.00 USD | 24,170,000.00 USD | 158,760.00 USD | 118,310.00 USD | 347,450.00 USD |
| `1D` | `4.11` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 22,930.00 USD | 18,800.00 USD | 13,560.00 USD |
| `7D` | `4.11` | 23,550,000.00 USD | 0.00 USD | 23,550,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD |
| `1D` | `4.12` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 4,430.00 USD | 41,500.00 USD | 134,910.00 USD |
| `7D` | `4.12` | 23,350,000.00 USD | 0.00 USD | 23,350,000.00 USD | 97,300.00 USD | 48,940.00 USD | 342,160.00 USD |
| `1D` | `4.13` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 39,650.00 USD | 55,060.00 USD | 23,660.00 USD |
| `7D` | `4.13` | 22,860,000.00 USD | 0.00 USD | 22,860,000.00 USD | 293,300.00 USD | 79,100.00 USD | 108,330.00 USD |
| `1D` | `4.14` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 194,940.00 USD | 36,950.00 USD | 142,880.00 USD |
| `7D` | `4.14` | 22,380,000.00 USD | 0.00 USD | 22,380,000.00 USD | 374,290.00 USD | 57,440.00 USD | 218,300.00 USD |
| `1D` | `4.15` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 297,570.00 USD | 125,690.00 USD | 110,090.00 USD |
| `7D` | `4.15` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,920.00 USD |
| `1D` | `4.16` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 63,250.00 USD | 99,580.00 USD | 99,860.00 USD |
| `7D` | `4.16` | 21,080,000.00 USD | 0.00 USD | 21,080,000.00 USD | 509,640.00 USD | 228,360.00 USD | 174,580.00 USD |
| `1D` | `4.17` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 44,430.00 USD | 128,870.00 USD | 115,650.00 USD |
| `7D` | `4.17` | 20,170,000.00 USD | 0.00 USD | 20,170,000.00 USD | 202,540.00 USD | 114,530.00 USD | 446,940.00 USD |
| `1D` | `4.18` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 197,650.00 USD | 59,270.00 USD | 77,110.00 USD |
| `7D` | `4.18` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD |
| `1D` | `4.19` | 12,060,000.00 USD | 0.00 USD | 12,060,000.00 USD | 288,710.00 USD | 79,350.00 USD | 145,390.00 USD |
| `7D` | `4.19` | 18,880,000.00 USD | 0.00 USD | 18,880,000.00 USD | 215,210.00 USD | 113,960.00 USD | 671,560.00 USD |
| `1D` | `4.20` | 11,550,000.00 USD | 0.00 USD | 11,550,000.00 USD | 64,030.00 USD | 171,160.00 USD | 466,240.00 USD |
| `7D` | `4.20` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,970.00 USD |
| `1D` | `4.21` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 70,370.00 USD | 146,670.00 USD | 919.18 USD |
| `7D` | `4.21` | 16,540,000.00 USD | 0.00 USD | 16,540,000.00 USD | 321,000.00 USD | 149,940.00 USD | 119,650.00 USD |
| `1D` | `4.22` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 582,370.00 USD | 141,000.00 USD | 406,770.00 USD |
| `7D` | `4.22` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 853,600.00 USD | 161,970.00 USD | 786,170.00 USD |
| `1D` | `4.23` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 1,040,000.00 USD | 440,840.00 USD | 495,610.00 USD |
| `7D` | `4.23` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 739,630.00 USD |
| `1D` | `4.24` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 259,090.00 USD | 201,080.00 USD | 244,670.00 USD |
| `7D` | `4.24` | 11,600,000.00 USD | 0.00 USD | 11,600,000.00 USD | 1,060,000.00 USD | 556,850.00 USD | 567,750.00 USD |
| `1D` | `4.25` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 368,110.00 USD | 296,100.00 USD | 466,490.00 USD |
| `7D` | `4.25` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 506,030.00 USD | 433,770.00 USD | 647,490.00 USD |
| `1D` | `4.26` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 563,140.00 USD | 171,790.00 USD | 298,160.00 USD |
| `7D` | `4.26` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 596,110.00 USD | 199,830.00 USD | 434,190.00 USD |
| `7D` | `4.27` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD |
| `1D` | `4.28` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 320,200.00 USD | 286,450.00 USD | 215,060.00 USD |
| `7D` | `4.28` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 842,270.00 USD | 497,680.00 USD | 1,110,000.00 USD |
| `1D` | `4.29` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 289,680.00 USD | 53,880.00 USD | 247,250.00 USD |
| `7D` | `4.29` | 574,080.00 USD | 0.00 USD | 574,080.00 USD | 9,100.00 USD | 46,530.00 USD | 361.22 USD |
| `1D` | `4.30` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 331,550.00 USD | 217,150.00 USD | 56,610.00 USD |
| `7D` | `4.30` | 518,090.00 USD | 0.00 USD | 518,090.00 USD | 3,500.00 USD | 90,090.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 408,710.00 USD | 222,320.00 USD | 499,700.00 USD |
| `7D` | `4.31` | 348,890.00 USD | 0.00 USD | 348,890.00 USD | 0.00 USD | 0.00 USD | 43,250.00 USD |
| `1D` | `4.32` | 272,350.00 USD | 0.00 USD | 272,350.00 USD | 611.20 USD | 0.00 USD | 18.65 USD |
| `7D` | `4.32` | 305,640.00 USD | 0.00 USD | 305,640.00 USD | 0.00 USD | 0.00 USD | 78,540.00 USD |
| `1D` | `4.33` | 271,720.00 USD | 0.00 USD | 271,720.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.33` | 227,100.00 USD | 0.00 USD | 227,100.00 USD | 0.00 USD | 0.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 269,720.00 USD | 0.00 USD | 269,720.00 USD | 269,670.00 USD | 0.00 USD | 55.79 USD |
| `7D` | `4.34` | 139,100.00 USD | 0.00 USD | 139,100.00 USD | 4,550.00 USD | 0.00 USD | 134,560.00 USD |
| `7D` | `4.35` | 85,370.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `7D` | `4.35` | 170,740.00 USD | 170,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 82,490.00 USD | 82,490.00 USD | 0.00 USD | 82,150.00 USD | 0.00 USD | 346.42 USD |
| `1D` | `4.36` | 164,990.00 USD | 164,990.00 USD | 0.00 USD | 82,150.00 USD | 0.00 USD | 346.42 USD |
| `7D` | `4.36` | 262,400.00 USD | 262,400.00 USD | 0.00 USD | 5,210.00 USD | 0.00 USD | 86,450.00 USD |
| `1D` | `4.37` | 299,690.00 USD | 299,690.00 USD | 0.00 USD | 52,120.00 USD | 0.00 USD | 82,580.00 USD |
| `1D` | `4.38` | 947,800.00 USD | 947,800.00 USD | 0.00 USD | 171,480.00 USD | 0.00 USD | 476,630.00 USD |
| `7D` | `4.38` | 665,720.00 USD | 665,720.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 199,830.00 USD |
| `7D` | `4.39` | 879,790.00 USD | 879,790.00 USD | 0.00 USD | 0.00 USD | 62,850.00 USD | 151,220.00 USD |
| `1D` | `4.40` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.02 USD |
| `7D` | `4.40` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD |
| `1D` | `4.41` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 193,630.00 USD | 83,080.00 USD | 61,400.00 USD |
| `7D` | `4.41` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 270,480.00 USD |
| `1D` | `4.42` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74.42 USD |
| `7D` | `4.42` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 49,400.00 USD | 52,300.00 USD |
| `7D` | `4.43` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 155,560.00 USD | 46,230.00 USD | 69,230.00 USD |
| `1D` | `4.44` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 287,750.00 USD |
| `7D` | `4.44` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 70,120.00 USD |
| `1D` | `4.45` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 34,890.00 USD | 0.00 USD |
| `7D` | `4.46` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD |
| `1D` | `4.47` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 16,700.00 USD | 0.00 USD |
| `7D` | `4.47` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 132,630.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 38,080.00 USD | 56,220.00 USD | 0.00 USD |
| `1D` | `4.49` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 252,560.00 USD | 155,000.00 USD | 150,020.00 USD |
| `7D` | `4.49` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 358,600.00 USD | 65,710.00 USD | 117,630.00 USD |
| `7D` | `4.50` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 368,940.00 USD | 200,700.00 USD | 0.00 USD |
| `1D` | `4.51` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 162,900.00 USD | 307,580.00 USD | 309,910.00 USD |
| `7D` | `4.51` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.52` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 266,310.00 USD | 88,150.00 USD | 205,650.00 USD |
| `7D` | `4.52` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 487,010.00 USD | 0.00 USD | 278,550.00 USD |
| `7D` | `4.53` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD |
| `1D` | `4.54` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 150,600.00 USD | 598,910.00 USD |
| `7D` | `4.54` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 239,970.00 USD |
| `1D` | `4.56` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,550.00 USD |
| `7D` | `4.56` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 154,940.00 USD | 70,180.00 USD | 67,490.00 USD |
| `7D` | `4.57` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 198,050.00 USD | 0.00 USD | 151,550.00 USD |
| `1D` | `4.58` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 434,430.00 USD | 43,090.00 USD | 840,570.00 USD |
| `7D` | `4.58` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 58,820.00 USD |
| `7D` | `4.59` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 759,320.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD |
| `7D` | `4.60` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD |
| `1D` | `4.61` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 58,960.00 USD |
| `7D` | `4.61` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 703.64 USD |
| `1D` | `4.62` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 822.47 USD |
| `7D` | `4.62` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 1,710.00 USD |
| `1D` | `4.63` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 351.99 USD |
| `7D` | `4.63` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 332,920.00 USD | 11,270.00 USD | 62,070.00 USD |
| `7D` | `4.64` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 500,990.00 USD | 0.00 USD | 857.07 USD |
| `1D` | `4.65` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 370,110.00 USD | 52,020.00 USD | 587,000.00 USD |
| `7D` | `4.65` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 649.48 USD |
| `1D` | `4.66` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 281,290.00 USD | 304,540.00 USD | 379,880.00 USD |
| `7D` | `4.66` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 144,860.00 USD | 0.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 13,110,000.00 USD | 13,110,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD |
| `7D` | `4.67` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 345,490.00 USD | 62,440.00 USD | 175,700.00 USD |
| `7D` | `4.68` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 237,390.00 USD |
| `7D` | `4.69` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,640.00 USD |
| `7D` | `4.70` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 365,440.00 USD | 278,020.00 USD | 316,520.00 USD |
| `7D` | `4.71` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `1D` | `4.72` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 5,240.00 USD | 187,480.00 USD | 103,760.00 USD |
| `7D` | `4.72` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 15,950,000.00 USD | 15,950,000.00 USD | 0.00 USD | 61,330.00 USD | 37,010.00 USD | 61,240.00 USD |
| `7D` | `4.73` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 59,270.00 USD | 0.00 USD | 894.74 USD |
| `1D` | `4.74` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 242,820.00 USD | 172,000.00 USD | 294,980.00 USD |
| `7D` | `4.74` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `1D` | `4.75` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 240,860.00 USD | 202,760.00 USD | 270,100.00 USD |
| `7D` | `4.75` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,640.00 USD |
| `1D` | `4.76` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 35,470.00 USD | 78,750.00 USD | 247,610.00 USD |
| `7D` | `4.76` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `1D` | `4.77` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 113,030.00 USD | 167,820.00 USD | 115,620.00 USD |
| `7D` | `4.77` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 18,300,000.00 USD | 18,300,000.00 USD | 0.00 USD | 40,580.00 USD | 20,000.00 USD | 114,030.00 USD |
| `7D` | `4.78` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 683,730.00 USD | 551,660.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 18,650,000.00 USD | 18,650,000.00 USD | 0.00 USD | 112,300.00 USD | 92,850.00 USD | 142,330.00 USD |
| `7D` | `4.79` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `1D` | `4.80` | 19,270,000.00 USD | 19,270,000.00 USD | 0.00 USD | 244,480.00 USD | 200,920.00 USD | 174,150.00 USD |
| `7D` | `4.80` | 19,660,000.00 USD | 19,660,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 19,570,000.00 USD | 19,570,000.00 USD | 0.00 USD | 55,660.00 USD | 120,180.00 USD | 127,880.00 USD |
| `7D` | `4.81` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 140,640.00 USD | 218,170.00 USD | 201,190.00 USD |
| `7D` | `4.82` | 23,060,000.00 USD | 23,060,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 61,110.00 USD | 70,050.00 USD | 140,320.00 USD |
| `7D` | `4.83` | 24,710,000.00 USD | 24,710,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `1D` | `4.84` | 20,660,000.00 USD | 20,660,000.00 USD | 0.00 USD | 85,920.00 USD | 89,230.00 USD | 77,660.00 USD |
| `7D` | `4.84` | 25,200,000.00 USD | 25,200,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `1D` | `4.85` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 243,020.00 USD | 110,540.00 USD | 223,590.00 USD |
| `7D` | `4.85` | 27,220,000.00 USD | 27,220,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `1D` | `4.86` | 21,680,000.00 USD | 21,680,000.00 USD | 0.00 USD | 94,860.00 USD | 69,470.00 USD | 278,380.00 USD |
| `7D` | `4.86` | 28,630,000.00 USD | 28,630,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `1D` | `4.87` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 111,250.00 USD | 60,360.00 USD | 59,180.00 USD |
| `7D` | `4.87` | 29,690,000.00 USD | 29,690,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `1D` | `4.88` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 36,680.00 USD | 7,330.00 USD | 38,360.00 USD |
| `7D` | `4.88` | 31,350,000.00 USD | 31,350,000.00 USD | 0.00 USD | 449,970.00 USD | 415,840.00 USD | 792,630.00 USD |
| `1D` | `4.89` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 11,490.00 USD | 25,940.00 USD | 50,150.00 USD |
| `7D` | `4.89` | 31,940,000.00 USD | 31,940,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `1D` | `4.90` | 22,220,000.00 USD | 22,220,000.00 USD | 0.00 USD | 25,630.00 USD | 55,440.00 USD | 65,090.00 USD |
| `7D` | `4.90` | 33,070,000.00 USD | 33,070,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `1D` | `4.91` | 22,500,000.00 USD | 22,500,000.00 USD | 0.00 USD | 114,890.00 USD | 85,510.00 USD | 74,650.00 USD |
| `7D` | `4.91` | 34,510,000.00 USD | 34,510,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `1D` | `4.92` | 22,860,000.00 USD | 22,860,000.00 USD | 0.00 USD | 117,750.00 USD | 89,190.00 USD | 153,930.00 USD |
| `7D` | `4.92` | 36,240,000.00 USD | 36,240,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `7D` | `4.93` | 37,800,000.00 USD | 37,800,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `7D` | `4.94` | 39,100,000.00 USD | 39,100,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD |
| `7D` | `4.95` | 40,400,000.00 USD | 40,400,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `7D` | `4.96` | 41,640,000.00 USD | 41,640,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `7D` | `4.97` | 42,020,000.00 USD | 42,020,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `7D` | `4.98` | 42,580,000.00 USD | 42,580,000.00 USD | 0.00 USD | 197,950.00 USD | 88,580.00 USD | 270,990.00 USD |
| `7D` | `4.99` | 42,930,000.00 USD | 42,930,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `7D` | `5.00` | 43,630,000.00 USD | 43,630,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `7D` | `5.01` | 45,790,000.00 USD | 45,790,000.00 USD | 0.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD |
| `7D` | `5.02` | 47,270,000.00 USD | 47,270,000.00 USD | 0.00 USD | 821,860.00 USD | 337,720.00 USD | 321,220.00 USD |
| `7D` | `5.03` | 48,710,000.00 USD | 48,710,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 886,200.00 USD |
| `7D` | `5.04` | 49,830,000.00 USD | 49,830,000.00 USD | 0.00 USD | 305,260.00 USD | 191,790.00 USD | 619,470.00 USD |
| `7D` | `5.05` | 51,380,000.00 USD | 51,380,000.00 USD | 0.00 USD | 799,820.00 USD | 267,140.00 USD | 486,680.00 USD |
| `7D` | `5.06` | 52,090,000.00 USD | 52,090,000.00 USD | 0.00 USD | 92,480.00 USD | 193,330.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 53,290,000.00 USD | 53,290,000.00 USD | 0.00 USD | 358,750.00 USD | 166,480.00 USD | 673,800.00 USD |
| `7D` | `5.08` | 53,890,000.00 USD | 53,890,000.00 USD | 0.00 USD | 204,140.00 USD | 243,390.00 USD | 149,330.00 USD |
| `7D` | `5.09` | 54,750,000.00 USD | 54,750,000.00 USD | 0.00 USD | 105,390.00 USD | 121,050.00 USD | 633,580.00 USD |
| `7D` | `5.10` | 55,240,000.00 USD | 55,240,000.00 USD | 0.00 USD | 291,110.00 USD | 0.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 55,990,000.00 USD | 55,990,000.00 USD | 0.00 USD | 369,260.00 USD | 92,720.00 USD | 291,780.00 USD |
| `7D` | `5.12` | 56,580,000.00 USD | 56,580,000.00 USD | 0.00 USD | 303,840.00 USD | 166,880.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 57,310,000.00 USD | 57,310,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 484,250.00 USD |
| `7D` | `5.14` | 57,760,000.00 USD | 57,760,000.00 USD | 0.00 USD | 140,950.00 USD | 73,940.00 USD | 239,260.00 USD |
| `7D` | `5.15` | 58,370,000.00 USD | 58,370,000.00 USD | 0.00 USD | 258,430.00 USD | 82,350.00 USD | 267,910.00 USD |
| `7D` | `5.16` | 58,900,000.00 USD | 58,900,000.00 USD | 0.00 USD | 51,850.00 USD | 126,880.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 59,590,000.00 USD | 59,590,000.00 USD | 0.00 USD | 280,710.00 USD | 99,740.00 USD | 309,950.00 USD |
| `7D` | `5.18` | 59,880,000.00 USD | 59,880,000.00 USD | 0.00 USD | 67,600.00 USD | 101,040.00 USD | 124,290.00 USD |
| `7D` | `5.19` | 60,260,000.00 USD | 60,260,000.00 USD | 0.00 USD | 69,310.00 USD | 47,800.00 USD | 262,990.00 USD |
| `7D` | `5.20` | 60,550,000.00 USD | 60,550,000.00 USD | 0.00 USD | 180,600.00 USD | 45,820.00 USD | 65,030.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.24B` | Total OI Tokens: `283,502,143.3 NEAR`
  * 1h OI Change: `-1.13%` | 4h OI Change: `-6.11%` | 24h OI Change: `-7.14%`
  * Exchange Breakdown: Binance=`240.19M` | Bybit=`165.55M` | OKX=`51.84M` | Hyperliquid=`251.53M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `45.22K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
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
| `15M` | `NEAR` | `46.97%` | `53.03%` | `0.89` | 34,760,000.00 USD |
| `15M` | `Binance` | `48.91%` | `51.09%` | `0.96` | 11,330,000.00 USD |
| `15M` | `OKX` | `49.39%` | `50.61%` | `0.98` | 4,460,000.00 USD |
| `15M` | `Bybit` | `48.79%` | `51.21%` | `0.95` | 3,730,000.00 USD |
| `15M` | `KuCoin` | `47.81%` | `52.19%` | `0.92` | 181,250.00 USD |
| `15M` | `Gate` | `34.64%` | `65.36%` | `0.53` | 596,390.00 USD |
| `15M` | `Bitget` | `46.87%` | `53.13%` | `0.88` | 1,800,000.00 USD |
| `15M` | `BingX` | `46.22%` | `53.78%` | `0.86` | 3,500,000.00 USD |
| `15M` | `MEXC` | `31.06%` | `68.94%` | `0.45` | 2,220,000.00 USD |
| `15M` | `Bitunix` | `64.54%` | `35.46%` | `1.82` | 861,750.00 USD |
| `15M` | `Hyperliquid` | `52.07%` | `47.93%` | `1.09` | 3,400,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `15.44%` | `84.56%` | `0.18` | 746,660.00 USD |
| `15M` | `Crypto.com` | `5.18%` | `94.82%` | `0.05` | 1,340.00 USD |
| `15M` | `WhiteBIT` | `51.22%` | `48.78%` | `1.05` | 484,300.00 USD |
| `15M` | `HTX` | `35.3%` | `64.7%` | `0.55` | 12,750.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `26.01%` | `73.99%` | `0.35` | 860,180.00 USD |
| `15M` | `Aster` | `87.58%` | `12.42%` | `7.05` | 362,110.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `39.62%` | `60.38%` | `0.66` | 221,320.00 USD |
| `15M` | `Whale Positions` | `48.91%` | `51.09%` | `0.96` | 11,330,000.00 USD |
| `15M` | `Global Accounts` | `46.97%` | `53.03%` | `0.89` | 34,760,000.00 USD |
| `1H` | `NEAR` | `50.00%` | `50.00%` | `1.00` | 110,050,000.00 USD |
| `1H` | `Binance` | `51.61%` | `48.39%` | `1.07` | 40,260,000.00 USD |
| `1H` | `OKX` | `50.75%` | `49.25%` | `1.03` | 14,270,000.00 USD |
| `1H` | `Bybit` | `51.33%` | `48.67%` | `1.05` | 13,020,000.00 USD |
| `1H` | `KuCoin` | `38.67%` | `61.33%` | `0.63` | 773,280.00 USD |
| `1H` | `Gate` | `52.1%` | `47.9%` | `1.09` | 1,880,000.00 USD |
| `1H` | `Bitget` | `43.51%` | `56.49%` | `0.77` | 5,120,000.00 USD |
| `1H` | `BingX` | `48.04%` | `51.96%` | `0.92` | 7,220,000.00 USD |
| `1H` | `MEXC` | `40.12%` | `59.88%` | `0.67` | 7,530,000.00 USD |
| `1H` | `Bitunix` | `53.05%` | `46.95%` | `1.13` | 3,720,000.00 USD |
| `1H` | `Hyperliquid` | `49.62%` | `50.38%` | `0.98` | 9,320,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.97%` | `58.03%` | `0.72` | 1,510,000.00 USD |
| `1H` | `Crypto.com` | `75.61%` | `24.39%` | `3.10` | 13,130.00 USD |
| `1H` | `WhiteBIT` | `56.71%` | `43.29%` | `1.31` | 2,730,000.00 USD |
| `1H` | `HTX` | `51.53%` | `48.47%` | `1.06` | 53,020.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `59.79%` | `40.21%` | `1.49` | 1,030,000.00 USD |
| `1H` | `Aster` | `77.89%` | `22.11%` | `3.52` | 901,800.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `26.59%` | `73.41%` | `0.36` | 693,250.00 USD |
| `1H` | `Whale Positions` | `51.61%` | `48.39%` | `1.07` | 40,260,000.00 USD |
| `1H` | `Global Accounts` | `50.00%` | `50.00%` | `1.00` | 110,050,000.00 USD |
| `4H` | `NEAR` | `48.57%` | `51.43%` | `0.94` | 351,270,000.00 USD |
| `4H` | `Binance` | `50%` | `50%` | `1.00` | 133,810,000.00 USD |
| `4H` | `OKX` | `47.89%` | `52.11%` | `0.92` | 46,540,000.00 USD |
| `4H` | `Bybit` | `48.65%` | `51.35%` | `0.95` | 44,050,000.00 USD |
| `4H` | `KuCoin` | `44.78%` | `55.22%` | `0.81` | 2,950,000.00 USD |
| `4H` | `Gate` | `46.94%` | `53.06%` | `0.88` | 6,280,000.00 USD |
| `4H` | `Bitget` | `44.14%` | `55.86%` | `0.79` | 13,550,000.00 USD |
| `4H` | `BingX` | `45.56%` | `54.44%` | `0.84` | 19,170,000.00 USD |
| `4H` | `MEXC` | `49.68%` | `50.32%` | `0.99` | 22,020,000.00 USD |
| `4H` | `Bitunix` | `49.68%` | `50.32%` | `0.99` | 11,430,000.00 USD |
| `4H` | `Hyperliquid` | `37.62%` | `62.38%` | `0.60` | 26,900,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `45.66%` | `54.34%` | `0.84` | 3,070,000.00 USD |
| `4H` | `Crypto.com` | `63.83%` | `36.17%` | `1.76` | 19,940.00 USD |
| `4H` | `WhiteBIT` | `73.87%` | `26.13%` | `2.83` | 10,320,000.00 USD |
| `4H` | `HTX` | `51.75%` | `48.25%` | `1.07` | 239,570.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.68%` | `59.32%` | `0.69` | 6,610,000.00 USD |
| `4H` | `Aster` | `70.72%` | `29.28%` | `2.42` | 1,140,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.43%` | `49.57%` | `1.02` | 3,180,000.00 USD |
| `4H` | `Whale Positions` | `50%` | `50%` | `1.00` | 133,810,000.00 USD |
| `4H` | `Global Accounts` | `48.57%` | `51.43%` | `0.94` | 351,270,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.48` | `4.47` | `4.48` | `4.50` | `4.45` | 3,346,103.47 USD | 1,895,415.61 USD | 1,450,687.86 USD | 444,727.76 USD | `+13.29%` | `4B / 3S` |
| `0:00 UTC` | `4.43` | `4.43` | `4.43` | `4.46` | `4.40` | 9,612,896.64 USD | 4,376,656.36 USD | 5,236,240.29 USD | -859,583.93 USD | `-8.94%` | `5B / 19S` |
| `5:00 UTC` | `4.44` | `4.42` | `4.44` | `4.45` | `4.39` | 7,755,029.11 USD | 3,981,690.96 USD | 3,773,338.14 USD | 208,352.82 USD | `+2.69%` | `13B / 5S` |
| `0:00 UTC` | `4.39` | `4.40` | `4.39` | `4.43` | `4.38` | 7,242,328.79 USD | 3,238,308.88 USD | 4,004,019.90 USD | -765,711.02 USD | `-10.57%` | `3B / 12S` |
| `5:00 UTC` | `4.41` | `4.41` | `4.41` | `4.43` | `4.39` | 3,825,249.23 USD | 2,351,169.85 USD | 1,474,079.38 USD | 877,090.47 USD | `+22.93%` | `9B / 0S` |
| `0:00 UTC` | `4.40` | `4.41` | `4.40` | `4.42` | `4.38` | 4,175,868.12 USD | 2,209,978.23 USD | 1,965,889.90 USD | 244,088.33 USD | `+5.85%` | `6B / 6S` |
| `5:00 UTC` | `4.38` | `4.40` | `4.38` | `4.42` | `4.38` | 4,640,530.52 USD | 2,789,933.99 USD | 1,850,596.53 USD | 939,337.46 USD | `+20.24%` | `7B / 6S` |
| `0:00 UTC` | `4.33` | `4.34` | `4.33` | `4.41` | `4.31` | 19,326,312.32 USD | 9,601,663.40 USD | 9,724,648.92 USD | -122,985.52 USD | `-0.64%` | `6B / 20S` |
| `5:00 UTC` | `4.36` | `4.35` | `4.36` | `4.37` | `4.34` | 4,641,250.70 USD | 2,849,322.27 USD | 1,791,928.43 USD | 1,057,393.84 USD | `+22.78%` | `8B / 0S` |
| `0:00 UTC` | `4.36` | `4.36` | `4.36` | `4.36` | `4.35` | 413,320.83 USD | 274,757.70 USD | 138,563.12 USD | 136,194.58 USD | `+32.95%` | `4B / 1S` |

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
| `5m` | -131,510.00 USD | 1,240,000.00 USD | **`ACCUMULATION`** |
| `15m` | -444,140.00 USD | 1,690,000.00 USD | **`ACCUMULATION`** |
| `30m` | -876,320.00 USD | 3,380,000.00 USD | **`ACCUMULATION`** |
| `1h` | -1,540,000.00 USD | 3,990,000.00 USD | **`ACCUMULATION`** |
| `2h` | -3,440,000.00 USD | 6,990,000.00 USD | **`ACCUMULATION`** |
| `4h` | -7,540,000.00 USD | -2,490,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -6,700,000.00 USD | -5,250,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,860,000.00 USD | -8,640,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -9,310,000.00 USD | -4,070,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,360,000.00 USD | -51,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -72,650,000.00 USD | -93,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -240,250,000.00 USD | -663,110,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-131.51K` | 15m=`-444.14K` | 1h=`-1.54M` | 24h=`-18.36M`
* Futures Capital Netflows: 5m=`+1.24M` | 15m=`+1.69M` | 1h=`+3.99M` | 24h=`-51.61M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.29` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.19` (Risk Distance: `0.1071` pts)
  * +2.5R Take Profit: `4.56`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.54` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.65` (Risk Distance: `0.1071` pts)
  * +2.5R Take Profit: `4.28`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.34`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
