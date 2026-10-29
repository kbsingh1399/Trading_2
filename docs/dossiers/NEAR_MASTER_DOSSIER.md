# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.08` | **Live Ask Quote**: `4.11` | **Mid Price**: `4.09`
- **Spread Points**: `30.00` | **Spread BPS**: `73.30 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.38` | VWAP Z-Score: `-1.81` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0663` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `22.89` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.86` | Lower -3.00σ Band: `3.89`
  * Upper +2.51σ Band: `4.79` | Lower -2.51σ Band: `3.97`
  * Upper +2.01σ Band: `4.70` | Lower -2.01σ Band: `4.05`
  * Upper +2.00σ Band: `4.70` | Lower -2.00σ Band: `4.06`
  * Upper +1.28σ Band: `4.59` | Lower -1.28σ Band: `4.17`
  * Upper +1.00σ Band: `4.54` | Lower -1.00σ Band: `4.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.14` | EMA-20=`4.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.34` (Slope: `+0.0000`) | EMA-100=`4.41`
  * Institutional Anchors: EMA-144=`4.45` | EMA-200=`4.47` (Slope: `-0.8939`) | EMA-233=`4.48`
- **Range Boundaries**: 24H High=`4.74` | 24H Low=`4.04` | Weekly High=`4.80` | Weekly Low=`4.04`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.16` (Distance: `-1.51%`)
  * Point of Control (POC) = `4.09` (Distance: `+0.07%`)
  * Value Area Low (VAL) = `4.04` (Distance: `+1.51%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.65` | Weekly POC=`4.45` | Weekly VAL=`4.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`4.04`
  * London Session (08:00-16:00 UTC): High=`4.11` | Low=`4.08`
  * New York Session (13:00-21:00 UTC): High=`4.12` | Low=`4.07`
  * Initial Balance (First Hour): IB High=`4.11` | IB Low=`4.08`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.08` - `4.11`
  * Optimal Trade Entry (OTE 0.705): `4.10`
  * Structural Invalidation Anchor (0.786): `4.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.07` | `4.08` | `4.05` | `4.08` | `1,238,082` | 5,032,347.29 USD | -611,782.53 USD | `-12.16%` | -40,997,737.62 USD | `-0.95` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4.08` | `4.11` | `4.07` | `4.10` | `1,251,488` | 5,123,705.13 USD | 930,071.00 USD | `+18.15%` | -40,067,666.62 USD | `+1.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.10` | `4.10` | `4.09` | `4.09` | `146,550` | 600,233.21 USD | -217,075.45 USD | `-36.17%` | -40,284,742.07 USD | `-0.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.11` | `4.12` | `4.08` | `4.11` | `2,404,416` | 9,855,518.22 USD | -1,231,685.46 USD | `-12.50%` | -40,093,720.54 USD | `-0.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.11` | `4.11` | `4.05` | `4.10` | `3,529,853` | 14,401,077.57 USD | -362,603.70 USD | `-2.52%` | -40,456,324.23 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4.10` | `4.10` | `4.09` | `4.09` | `146,550` | 600,233.21 USD | -217,075.45 USD | `-36.17%` | -40,673,399.68 USD | `+0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4.17` | `4.28` | `4.12` | `4.15` | `18,917,752` | 79,175,981.42 USD | 886,549.86 USD | `+1.12%` | -38,736,880.09 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4.15` | `4.17` | `4.08` | `4.11` | `14,553,439` | 59,999,693.74 USD | -797,455.63 USD | `-1.33%` | -39,534,335.71 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.11` | `4.11` | `4.05` | `4.10` | `3,687,298` | 15,045,903.74 USD | -536,232.44 USD | `-3.56%` | -40,070,568.15 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.05` | `4.09` | `64,971,898` | 271,988,905.76 USD | -11,786,749.55 USD | `-4.33%` | -40,114,014.86 USD | `-0.73` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -27,473,639.56 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -28,567,348.59 USD | `+1.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.05` | `4.09` | `64,971,898` | 271,988,905.76 USD | -11,786,749.55 USD | `-4.33%` | -40,114,014.86 USD | `-0.73` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`4.09`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `70` | `0x7737...bf66` | `LONG` | 23,153,180.67 USD | `5,640,376.30` | `2.35` | `4.09` | `0.8396` | 9,881,277.85 USD | `+42.68%` | `10X Cross` |
| `138` | `0xb581...6f4f` | `LONG` | 14,739,120.00 USD | `3,600,000.00` | `5.19` | `4.09` | `0.000000` | -3,953,915.22 USD | `-26.83%` | `4X Cross` |
| `222` | `0xdd53...2b13` | `SHORT` | 9,853,789.29 USD | `2,400,202.00` | `2.31` | `4.09` | `29.56` | -4,307,940.73 USD | `-43.72%` | `3X Cross` |
| `257` | `0xefe4...194b` | `SHORT` | 9,007,019.75 USD | `2,193,944.50` | `4.41` | `4.09` | `10.30` | 678,989.45 USD | `+7.54%` | `5X Cross` |
| `278` | `0x77ee...2902` | `LONG` | 8,450,142.62 USD | `2,063,023.10` | `1.93` | `4.09` | `0.000000` | 4,458,946.68 USD | `+52.77%` | `10X Cross` |
| `390` | `0xb83d...6e36` | `SHORT` | 5,932,065.25 USD | `1,445,759.10` | `5.19` | `4.09` | `105.49` | 1,577,383.69 USD | `+26.59%` | `3X Cross` |
| `410` | `0xb46b...538e` | `SHORT` | 5,473,592.00 USD | `1,336,000.00` | `4.33` | `4.09` | `7.56` | 311,272.06 USD | `+5.69%` | `10X Cross` |
| `424` | `0x9df2...c665` | `SHORT` | 5,186,500.00 USD | `1,265,000.00` | `2.03` | `4.09` | `28.91` | -2,619,817.66 USD | `-50.51%` | `10X Cross` |
| `478` | `0x60b0...991e` | `LONG` | 4,584,912.60 USD | `1,121,307.10` | `5.00` | `4.09` | `0.000000` | -1,016,511.83 USD | `-22.17%` | `10X Cross` |
| `507` | `0xcac1...26b3` | `SHORT` | 4,393,760.04 USD | `1,073,743.90` | `2.48` | `4.09` | `12.25` | -1,733,816.57 USD | `-39.46%` | `10X Cross` |
| `517` | `0x781e...96b7` | `SHORT` | 4,264,977.87 USD | `1,039,604.60` | `2.45` | `4.09` | `7.52` | -1,720,640.68 USD | `-40.34%` | `10X Cross` |
| `603` | `0x45d2...4029` | `SHORT` | 3,726,539.32 USD | `909,400.00` | `3.26` | `4.09` | `49.30` | -760,389.42 USD | `-20.40%` | `10X Cross` |
| `618` | `0x4cae...7c34` | `LONG` | 3,686,665.52 USD | `900,086.80` | `3.52` | `4.09` | `2.97` | 514,264.54 USD | `+13.95%` | `10X Cross` |
| `627` | `0x7fda...17d1` | `SHORT` | 3,635,553.94 USD | `885,662.00` | `4.44` | `4.09` | `45.43` | 293,558.35 USD | `+8.07%` | `10X Cross` |
| `770` | `0x9aa5...58af` | `SHORT` | 2,970,767.63 USD | `723,977.10` | `4.78` | `4.09` | `16.55` | 488,865.56 USD | `+16.46%` | `10X Cross` |
| `851` | `0x005a...61fe` | `LONG` | 2,680,053.94 USD | `652,414.60` | `2.08` | `4.09` | `2.42` | 1,322,522.70 USD | `+49.35%` | `7X Cross` |
| `855` | `0xba5d...a352` | `SHORT` | 2,651,127.56 USD | `647,532.50` | `2.83` | `4.09` | `13.33` | -818,412.62 USD | `-30.87%` | `10X Cross` |
| `865` | `0xb695...a92d` | `SHORT` | 2,619,443.66 USD | `639,231.70` | `4.57` | `4.09` | `43.68` | 303,915.27 USD | `+11.60%` | `10X Cross` |
| `869` | `0xd1dd...9e85` | `SHORT` | 2,610,547.90 USD | `637,621.00` | `4.96` | `4.09` | `18.15` | 552,924.84 USD | `+21.18%` | `10X Cross` |
| `873` | `0x123d...3bff` | `SHORT` | 2,603,837.65 USD | `635,392.30` | `2.09` | `4.09` | `9.40` | -1,277,889.18 USD | `-49.08%` | `10X Cross` |
| `893` | `0xcf53...ee11` | `SHORT` | 2,548,553.44 USD | `621,598.40` | `5.07` | `4.09` | `24.89` | 603,616.81 USD | `+23.68%` | `10X Cross` |
| `1028` | `0xbfc7...80b4` | `SHORT` | 2,174,976.00 USD | `531,000.00` | `2.01` | `4.09` | `11.07` | -1,109,776.61 USD | `-51.02%` | `10X Cross` |
| `1165` | `0xef96...9383` | `SHORT` | 1,922,211.06 USD | `468,443.50` | `4.50` | `4.09` | `13.13` | 187,090.02 USD | `+9.73%` | `10X Cross` |
| `1345` | `0xe097...d0fe` | `LONG` | 1,640,000.00 USD | `400,000.00` | `5.29` | `4.09` | `0.000000` | -476,787.30 USD | `-29.07%` | `10X Cross` |
| `1402` | `0x2577...4897` | `LONG` | 1,575,781.21 USD | `383,878.10` | `4.14` | `4.09` | `0.000000` | -14,874.49 USD | `-0.94%` | `10X Cross` |
| `1483` | `0x6e8f...4364` | `LONG` | 1,482,075.58 USD | `361,210.50` | `3.28` | `4.09` | `3.58` | 298,015.35 USD | `+20.11%` | `10X Cross` |
| `1489` | `0xdf95...7d72` | `SHORT` | 1,469,710.19 USD | `358,038.00` | `4.23` | `4.09` | `111.29` | 45,621.08 USD | `+3.10%` | `10X Cross` |
| `1514` | `0xcf67...eb24` | `LONG` | 1,434,090.00 USD | `350,000.00` | `1.98` | `4.09` | `1.74` | 742,472.12 USD | `+51.77%` | `10X Cross` |
| `1632` | `0xfc27...9d9d` | `SHORT` | 1,313,718.56 USD | `319,997.70` | `5.01` | `4.09` | `57.31` | 289,824.06 USD | `+22.06%` | `10X Cross` |
| `1716` | `0x9836...457e` | `LONG` | 1,230,332.46 USD | `300,000.60` | `4.57` | `4.09` | `1.94` | -141,740.71 USD | `-11.52%` | `10X Cross` |
| `1728` | `0x17c3...a868` | `LONG` | 1,222,469.94 USD | `298,163.40` | `4.37` | `4.09` | `0.000000` | -81,578.27 USD | `-6.67%` | `3X Cross` |
| `1752` | `0xe065...0f85` | `SHORT` | 1,189,179.80 USD | `290,227.90` | `2.81` | `4.09` | `6.68` | -372,435.55 USD | `-31.32%` | `10X Cross` |
| `1809` | `0x023a...2355` | `SHORT` | 1,142,859.17 USD | `278,413.40` | `4.53` | `4.09` | `28.27` | 118,212.71 USD | `+10.34%` | `10X Cross` |
| `1956` | `0xff43...d924` | `LONG` | 1,021,847.55 USD | `249,474.50` | `4.64` | `4.09` | `3.28` | -136,196.13 USD | `-13.33%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.70` | 5,140.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.14K USD at 4.7038 USD [API] | `2026-10-28 19:01:55` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 6,417.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.42K USD at 4.7046 USD [API] | `2026-10-28 19:24:31` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 7,518.41 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.52K USD at 4.7043 USD [API] | `2026-10-28 19:27:03` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 10,227.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.23K USD at 4.7145 USD [API] | `2026-10-28 19:38:03` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 5,849.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.85K USD at 4.7276 USD [API] | `2026-10-28 19:44:06` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 6,258.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.26K USD at 4.7298 USD [API] | `2026-10-28 19:45:23` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 7,562.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.56K USD at 4.7859 USD [API] | `2026-10-28 20:03:05` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 257.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.26K USD at 4.7786 USD [API] | `2026-10-28 20:01:20` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 477.06 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.48K USD at 4.7754 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 387.71 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.39K USD at 4.7748 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 23,853.50 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 23.85K USD at 4.7707 USD [API] | `2026-10-28 20:05:14` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 8,946.97 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.95K USD at 4.7707 USD [API] | `2026-10-28 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 149.02 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.15K USD at 4.7764 USD [API] | `2026-10-28 20:05:44` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 6,889.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.89K USD at 4.7661 USD [API] | `2026-10-28 20:06:45` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 8,585.21 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 8.59K USD at 4.7754 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 954.79 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.95K USD at 5.9974 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 1,383.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.38K USD at 5.9973 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 1,383.46 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.38K USD at 5.9968 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 30.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.03K USD at 5.9968 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 917.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.92K USD at 5.9963 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 11,342.27 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 11.34K USD at 4.7771 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 9,007.26 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.01K USD at 4.7756 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 5,798.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.80K USD at 4.6895 USD [API] | `2026-10-28 20:24:43` |
| `ANNOUNCEMENT` | `INFO` | `4.67` | 5,826.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.83K USD at 4.6663 USD [API] | `2026-10-28 20:29:19` |
| `ANNOUNCEMENT` | `INFO` | `1.82` | 317.41 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.32K USD at 1.8200 USD [API] | `2026-06-28 17:35:22` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 8,432.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.43K USD at 4.6796 USD [API] | `2026-10-28 20:37:07` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 9,000.08 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.00K USD at 4.6795 USD [API] | `2026-10-28 20:37:07` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 11,342.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 11.34K USD at 4.6795 USD [API] | `2026-10-28 20:37:07` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 5,721.97 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.72K USD at 4.7017 USD [API] | `2026-10-28 20:52:09` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 9,007.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.01K USD at 4.7099 USD [API] | `2026-10-28 20:54:26` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 9,002.97 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.00K USD at 4.7099 USD [API] | `2026-10-28 20:54:26` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 10,254.32 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.25K USD at 4.7268 USD [API] | `2026-10-28 20:58:08` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,361.27 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.36K USD at 4.7761 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,359.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.36K USD at 4.7751 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 7,117.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.12K USD at 4.7390 USD [API] | `2026-10-28 20:59:25` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 3,062.76 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.06K USD at 4.7766 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 5,692.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.69K USD at 4.7358 USD [API] | `2026-10-28 22:09:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+7.63%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--0.70%`)
  * 48H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+7.66%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--0.68%`)
  * 3D Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+7.66%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--0.68%`)
  * 7D Horizon: Short MP=`5.03` (Vol: 852,900.00 USD, Dist: `+22.63%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--0.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8350` | 4,740,000.00 USD | 29,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 2,030.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 10,600.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 12,940.00 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 5,690.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 24,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 13,040.00 USD | 24,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 778.57 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,910.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 488.33 USD | 24,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 24,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 36,980.00 USD | 24,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 12,660.00 USD | 24,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 24,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 24,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 4,270.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 1,150.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 301.95 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 34,680.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,000.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 173.51 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 149.66 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 2,580.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 255.41 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 243.05 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 43,220.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 115,200.00 USD | 24,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 2,040.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 2,180.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 4,240.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 11,180.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 10,050.00 USD | 24,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 417.32 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 65,120.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 911.41 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 14,580.00 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 24,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 42,490.00 USD | 24,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 2,020.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 712.50 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 362,290.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 429.83 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,990.00 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 743.46 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 3,150.00 USD | 23,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 7,190.00 USD | 23,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 610.00 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 14,130.00 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 16,170.00 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 83,130.00 USD | 23,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 47,140.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 4,770.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 12,250.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,150.00 USD | 23,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 384.13 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 212.29 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 108.71 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 602,850.00 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 4,980.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 168.97 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,630.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 1,320.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,710.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 1,090.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 17,220.00 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 1,210.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 5,280.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 1,280.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 2,040.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 652.75 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 937.50 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,080.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 62,210.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 3,110.00 USD | 22,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 35,380.00 USD | 22,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 10,800.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 5,930.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 47,310.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 2,450.00 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 124,920.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 7,750.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 2,780.00 USD | 22,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 10,480.00 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,100.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 7,520.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,960.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 96,590.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 202.82 USD | 22,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,110.00 USD | 22,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 773.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 1,520.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 13,580.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 15,070.00 USD | 22,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 815.44 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 76,110.00 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 4,190.00 USD | 22,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 20,940.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 3,400.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 44,890.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 149,130.00 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 7,930.00 USD | 21,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 529.85 USD | 21,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 10,720.00 USD | 21,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 306,010.00 USD | 21,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,980.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 105,380.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 237,770.00 USD | 21,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 4,240.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 58,430.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 143.66 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 30,230.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 419,870.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 1,640.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 27,900.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570.00 USD | 20,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 1,770,000.00 USD | 20,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 273,060.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,680.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 4,260.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 137,190.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 11,160.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 340.81 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 19,450.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 1,110.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 8,240.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 121.98 USD | 18,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 19,460.00 USD | 18,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 698.39 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 10,920.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 5,800.00 USD | 18,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 53,870.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 11,910.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,570.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 75,100.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 21,590.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 17,370.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 224.44 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 25,170.00 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 9,050.00 USD | 18,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,970.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,580.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 1,760.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 7,280.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 6,230.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 120,220.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 15,010.00 USD | 18,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 27,130.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 42,810.00 USD | 18,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 47,240.00 USD | 18,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 1,670.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 6,730.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 719.84 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 26,980.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,560.00 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 6,310.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 11,780.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 260,210.00 USD | 17,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 10,470.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 4,240.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,860.00 USD | 17,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 8,570.00 USD | 17,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 378,680.00 USD | 17,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 52,190.00 USD | 17,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 101,800.00 USD | 17,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 1,330.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 93,010.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 191,130.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 61,920.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 1,010.00 USD | 16,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 2,710,000.00 USD | 16,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,050.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 11,090.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 22,840.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 366,890.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 10,410.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 11,290.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 27,700.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 149.63 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 103,780.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 245,370.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 13,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 13,960.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 146,750.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,540.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 45,400.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 20,110.00 USD | 12,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 9,680.00 USD | 12,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 37,690.00 USD | 12,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 11,350.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 7,580.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 10,030.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 5,350.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 630,260.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 6,250.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 104,290.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 13,860.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 25,260.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 53,140.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 17,670.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 18,010.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 33,820.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 842,170.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 2,680.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 209,990.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 141,170.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 29,280.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 24,800.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 64,220.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 40,110.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 137,860.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 569,260.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,450.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 844.34 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 76,570.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 181,600.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 5,290.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 23,970.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 9,830.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 9,260.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,440.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 105,220.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 74,160.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 24,030.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 45,750.00 USD | 9,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 11,870.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 129,140.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 163,400.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 254,870.00 USD | 8,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 377,070.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 15,510.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 34,970.00 USD | 8,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 1,330,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 11,730,000.00 USD | 11,730,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 45,700.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 11,340,000.00 USD | 11,340,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 150,210.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 11,230,000.00 USD | 11,230,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 29,400.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 11,120,000.00 USD | 11,120,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 45,760.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.63` | 5,300,000.00 USD | 5,300,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.63` | 10,900,000.00 USD | 10,900,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 50,630.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.64` | 5,270,000.00 USD | 5,270,000.00 USD | 152.80 USD | 5,040.00 USD | 4.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.64` | 10,840,000.00 USD | 10,840,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 55,690.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 5,260,000.00 USD | 5,260,000.00 USD | 386.30 USD | 0.00 USD | 77.58 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 10,710,000.00 USD | 10,710,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 26,080.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 5,260,000.00 USD | 5,260,000.00 USD | 291.38 USD | 0.00 USD | 6.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 10,610,000.00 USD | 10,610,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 912,270.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,260,000.00 USD | 5,260,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 10,440,000.00 USD | 10,440,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 257,380.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.68` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 271.33 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 111,250.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,230,000.00 USD | 5,230,000.00 USD | 23,960.00 USD | 0.00 USD | 9.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,330,000.00 USD | 10,330,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 112,450.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,210,000.00 USD | 5,210,000.00 USD | 39,190.00 USD | 0.00 USD | 55,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,240,000.00 USD | 10,240,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 64,270.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,110,000.00 USD | 5,110,000.00 USD | 430.40 USD | 0.00 USD | 6.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,100,000.00 USD | 10,100,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 194,120.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,110,000.00 USD | 5,110,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 9,970,000.00 USD | 9,970,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 28,060.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,110,000.00 USD | 5,110,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 9,970,000.00 USD | 9,970,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 5,760.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,090,000.00 USD | 5,090,000.00 USD | 94,200.00 USD | 33,110.00 USD | 43,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 9,870,000.00 USD | 9,870,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 58,120.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 9,580,000.00 USD | 9,580,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 80,510.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 9,510,000.00 USD | 9,510,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 65,500.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 4,880,000.00 USD | 4,880,000.00 USD | 187.12 USD | 5,330.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 9,440,000.00 USD | 9,440,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 127,760.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 4,880,000.00 USD | 4,880,000.00 USD | 106.91 USD | 4,490.00 USD | 29,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,400,000.00 USD | 9,400,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 49,180.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 4,840,000.00 USD | 4,840,000.00 USD | 472.79 USD | 0.00 USD | 231.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,320,000.00 USD | 9,320,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 139,870.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 4,840,000.00 USD | 4,840,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,230,000.00 USD | 9,230,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 7,720.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 4,840,000.00 USD | 4,840,000.00 USD | 54,290.00 USD | 0.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 25,230.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 11,960.00 USD | 583.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,190,000.00 USD | 9,190,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 53,580.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 4,760,000.00 USD | 4,760,000.00 USD | 1,150.00 USD | 18,900.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 158,690.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,150,000.00 USD | 9,150,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 96,570.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 4,720,000.00 USD | 4,720,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 21,270.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 4,710,000.00 USD | 4,710,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,140,000.00 USD | 9,140,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 26,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 4,640,000.00 USD | 4,640,000.00 USD | 1,690.00 USD | 11,800.00 USD | 743.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,070,000.00 USD | 9,070,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 22,850.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 4,630,000.00 USD | 4,630,000.00 USD | 106,680.00 USD | 6,860.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 8,980,000.00 USD | 8,980,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 108,570.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 4,470,000.00 USD | 4,470,000.00 USD | 112,840.00 USD | 37,150.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 8,760,000.00 USD | 8,760,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 5,490.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,300,000.00 USD | 4,300,000.00 USD | 31,410.00 USD | 10,910.00 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 8,710,000.00 USD | 8,710,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 10,170.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 4,240,000.00 USD | 4,240,000.00 USD | 32,140.00 USD | 35,760.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 8,460,000.00 USD | 8,460,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 37,980.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 4,130,000.00 USD | 4,130,000.00 USD | 148,140.00 USD | 26,030.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,380,000.00 USD | 8,380,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 723,590.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 29,900.00 USD | 39,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,160,000.00 USD | 8,160,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 202,910.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 3,860,000.00 USD | 3,860,000.00 USD | 64,710.00 USD | 14,940.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,070,000.00 USD | 8,070,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 33,430.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 3,760,000.00 USD | 3,760,000.00 USD | 95,940.00 USD | 5,610.00 USD | 97,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 7,860,000.00 USD | 7,860,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 599,170.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 3,560,000.00 USD | 3,560,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 7,830,000.00 USD | 7,830,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 218,010.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 3,420,000.00 USD | 3,420,000.00 USD | 190,720.00 USD | 66,010.00 USD | 105,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,330,000.00 USD | 7,330,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 477,730.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 3,050,000.00 USD | 3,050,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 6,730,000.00 USD | 6,730,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 151,930.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 2,800,000.00 USD | 2,800,000.00 USD | 413,960.00 USD | 106,190.00 USD | 136,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,050,000.00 USD | 6,050,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 223,790.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 2,150,000.00 USD | 2,150,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 5,810,000.00 USD | 5,810,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 57,890.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 1,920,000.00 USD | 1,920,000.00 USD | 112,570.00 USD | 72,850.00 USD | 126,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,200,000.00 USD | 5,200,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 73,860.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 1,610,000.00 USD | 1,610,000.00 USD | 180,340.00 USD | 50,310.00 USD | 108,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,270,000.00 USD | 4,270,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 128,600.00 USD | 979,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 1,270,000.00 USD | 1,270,000.00 USD | 189,730.00 USD | 55,650.00 USD | 267,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 3,650,000.00 USD | 3,650,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 20,250.00 USD | 850,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 759,140.00 USD | 759,140.00 USD | 105,670.00 USD | 48,960.00 USD | 211,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,210,000.00 USD | 3,210,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 120,800.00 USD | 830,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 393,130.00 USD | 393,130.00 USD | 2,370.00 USD | 46,690.00 USD | 95,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 2,330,000.00 USD | 2,330,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 24,810.00 USD | 709,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 248,290.00 USD | 248,290.00 USD | 0.00 USD | 27,150.00 USD | 126,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 1,830,000.00 USD | 1,830,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 324,890.00 USD | 685,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 95,010.00 USD | 95,010.00 USD | 0.00 USD | 72,110.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 1,260,000.00 USD | 1,260,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 90,340.00 USD | 360,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.08` | 506,800.00 USD | 506,800.00 USD | 506,300.00 USD | 0.00 USD | 506.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.08` | 1,010,000.00 USD | 1,010,000.00 USD | 506,300.00 USD | 0.00 USD | 506.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.08` | 356,630.00 USD | 356,630.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.08` | 713,260.00 USD | 713,260.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.09` | 931,780.00 USD | 931,780.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.10` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 509.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 1,070,000.00 USD | 1,070,000.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 269,820.00 USD | 269,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.11` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 59,250.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.12` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 80,980.00 USD | 228,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.13` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.14` | 1,610,000.00 USD | 1,610,000.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.14` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.15` | 1,670,000.00 USD | 1,670,000.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.17` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.18` | 1,890,000.00 USD | 1,890,000.00 USD | 129,470.00 USD | 17,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.19` | 2,250,000.00 USD | 2,250,000.00 USD | 174,270.00 USD | 0.00 USD | 185,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.20` | 6,930.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.20` | 1,820,000.00 USD | 1,820,000.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.21` | 2,320,000.00 USD | 2,320,000.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.22` | 2,520,000.00 USD | 2,520,000.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.23` | 3,200,000.00 USD | 3,200,000.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.24` | 3,880,000.00 USD | 3,880,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.25` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 4,440,000.00 USD | 4,440,000.00 USD | 60,530.00 USD | 173,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.27` | 5,290,000.00 USD | 5,290,000.00 USD | 677,660.00 USD | 24,620.00 USD | 152,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 4,400,000.00 USD | 4,400,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 9,850.00 USD | 16,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.28` | 5,930,000.00 USD | 5,930,000.00 USD | 314,270.00 USD | 30,410.00 USD | 288,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 6,310,000.00 USD | 6,310,000.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 207.39 USD | 16,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 6,270,000.00 USD | 6,270,000.00 USD | 152,480.00 USD | 32,690.00 USD | 161,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.30` | 6,510,000.00 USD | 6,510,000.00 USD | 32,410.00 USD | 45,120.00 USD | 163,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,830,000.00 USD | 6,830,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.30` | 2,770.00 USD | 19,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.31` | 6,930,000.00 USD | 6,930,000.00 USD | 304,920.00 USD | 13,580.00 USD | 94,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 7,260,000.00 USD | 7,260,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 2,280.00 USD | 22,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 7,090,000.00 USD | 7,090,000.00 USD | 86,850.00 USD | 73,400.00 USD | 19.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,910,000.00 USD | 7,910,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 10,090.00 USD | 32,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 7,520,000.00 USD | 7,520,000.00 USD | 255,620.00 USD | 93,880.00 USD | 87,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 8,030,000.00 USD | 8,030,000.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 1,450.00 USD | 33,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.34` | 8,050,000.00 USD | 8,050,000.00 USD | 270,720.00 USD | 140,540.00 USD | 114,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 8,210,000.00 USD | 8,210,000.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 8,680.00 USD | 42,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 8,140,000.00 USD | 8,140,000.00 USD | 855.62 USD | 0.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 5,540.00 USD | 47,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 8,260,000.00 USD | 8,260,000.00 USD | 84,400.00 USD | 12,310.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 8,440,000.00 USD | 8,440,000.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 8,490,000.00 USD | 8,490,000.00 USD | 52,520.00 USD | 46,860.00 USD | 131,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 6,680.00 USD | 54,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 9,340,000.00 USD | 9,340,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 25,830.00 USD | 80,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.39` | 9,670,000.00 USD | 9,670,000.00 USD | 399.48 USD | 17,360.00 USD | 310,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 9,350,000.00 USD | 9,350,000.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 14,050.00 USD | 94,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 10,070,000.00 USD | 10,070,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,950,000.00 USD | 9,950,000.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 95,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 10,440,000.00 USD | 10,440,000.00 USD | 196,820.00 USD | 112,990.00 USD | 63,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 53,320.00 USD | 149,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 47,240.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,930,000.00 USD | 10,930,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 104.87 USD | 149,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 10,640,000.00 USD | 10,640,000.00 USD | 5,100.00 USD | 49,400.00 USD | 95,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 11,210,000.00 USD | 11,210,000.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 25,500.00 USD | 174,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 11,430,000.00 USD | 11,430,000.00 USD | 154,480.00 USD | 339,100.00 USD | 292,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 11,480,000.00 USD | 11,480,000.00 USD | 649.63 USD | 50,720.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 11,490,000.00 USD | 11,490,000.00 USD | 704.30 USD | 9,070.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 175,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 11,530,000.00 USD | 11,530,000.00 USD | 210.23 USD | 16,700.00 USD | 18,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,810,000.00 USD | 11,810,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 1,260.00 USD | 176,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 11,740,000.00 USD | 11,740,000.00 USD | 117,480.00 USD | 73,240.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 15,150.00 USD | 191,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 12,300,000.00 USD | 12,300,000.00 USD | 252,600.00 USD | 155,000.00 USD | 150,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 12,140,000.00 USD | 12,140,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 90,180.00 USD | 281,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 12,850,000.00 USD | 12,850,000.00 USD | 361,560.00 USD | 65,710.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 12,720,000.00 USD | 12,720,000.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 268.05 USD | 282,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 13,650,000.00 USD | 13,650,000.00 USD | 186,860.00 USD | 307,580.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,800,000.00 USD | 12,800,000.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 14,270,000.00 USD | 14,270,000.00 USD | 287,830.00 USD | 88,150.00 USD | 242,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,940,000.00 USD | 12,940,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,100.00 USD | 300,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 15,040,000.00 USD | 15,040,000.00 USD | 487,540.00 USD | 0.00 USD | 281,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,920,000.00 USD | 13,920,000.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 15,760,000.00 USD | 15,760,000.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 300,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 22,540.00 USD | 196,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 16,380,000.00 USD | 16,380,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 15,640,000.00 USD | 15,640,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 16,690,000.00 USD | 16,690,000.00 USD | 177,440.00 USD | 70,180.00 USD | 67,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 16,190,000.00 USD | 16,190,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 18,150,000.00 USD | 18,150,000.00 USD | 506,750.00 USD | 73,690.00 USD | 876,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 16,320,000.00 USD | 16,320,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 19,130,000.00 USD | 19,130,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 17,910,000.00 USD | 17,910,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 9,190.00 USD | 309,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 19,340,000.00 USD | 19,340,000.00 USD | 54,450.00 USD | 84,420.00 USD | 67,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 18,030,000.00 USD | 18,030,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 310,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 19,470,000.00 USD | 19,470,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 18,030,000.00 USD | 18,030,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 19,620,000.00 USD | 19,620,000.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 18,170,000.00 USD | 18,170,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 203.50 USD | 310,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 19,620,000.00 USD | 19,620,000.00 USD | 1,040.00 USD | 0.00 USD | 335.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 18,390,000.00 USD | 18,390,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 493.16 USD | 311,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 20,030,000.00 USD | 20,030,000.00 USD | 334,190.00 USD | 11,270.00 USD | 61,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 18,910,000.00 USD | 18,910,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.65` | 21,100,000.00 USD | 21,100,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 19,330,000.00 USD | 19,330,000.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.66` | 22,080,000.00 USD | 22,080,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 19,640,000.00 USD | 19,640,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,390.00 USD | 435,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 22,640,000.00 USD | 22,640,000.00 USD | 184,440.00 USD | 0.00 USD | 377,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 23,250,000.00 USD | 23,250,000.00 USD | 345,840.00 USD | 81,340.00 USD | 177,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 20,600,000.00 USD | 20,600,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 23,750,000.00 USD | 23,750,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 20,690,000.00 USD | 20,690,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.70` | 24,100,000.00 USD | 24,100,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 21,010,000.00 USD | 21,010,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 13,050.00 USD | 448,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 25,060,000.00 USD | 25,060,000.00 USD | 365,580.00 USD | 284,360.00 USD | 316,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 21,420,000.00 USD | 21,420,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 460.18 USD | 449,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 25,360,000.00 USD | 25,360,000.00 USD | 5,440.00 USD | 187,480.00 USD | 103,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 21,610,000.00 USD | 21,610,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.73` | 25,510,000.00 USD | 25,510,000.00 USD | 52,120.00 USD | 37,010.00 USD | 60,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 21,670,000.00 USD | 21,670,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 21,990,000.00 USD | 21,990,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 22,530,000.00 USD | 22,530,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 154,870.00 USD | 604,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.76` | 23,880,000.00 USD | 23,880,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 64,260.00 USD | 668,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,780,000.00 USD | 24,780,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,050.00 USD | 675,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 26,140,000.00 USD | 26,140,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,530.00 USD | 679,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 27,170,000.00 USD | 27,170,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 681,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 28,760,000.00 USD | 28,760,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 29,390,000.00 USD | 29,390,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 473,730.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 32,160,000.00 USD | 32,160,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,810,000.00 USD | 33,810,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 23,580.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 34,300,000.00 USD | 34,300,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 41,300.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 36,320,000.00 USD | 36,320,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 37,730,000.00 USD | 37,730,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,790,000.00 USD | 38,790,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 12,510.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.88` | 40,370,000.00 USD | 40,370,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,960,000.00 USD | 40,960,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 42,100,000.00 USD | 42,100,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 43,540,000.00 USD | 43,540,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 346,720.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 45,270,000.00 USD | 45,270,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,830,000.00 USD | 46,830,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 556.67 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 48,160,000.00 USD | 48,160,000.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 49,460,000.00 USD | 49,460,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 50,700,000.00 USD | 50,700,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 51,080,000.00 USD | 51,080,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 51,740,000.00 USD | 51,740,000.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 5,090.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 52,090,000.00 USD | 52,090,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 20,430.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 52,790,000.00 USD | 52,790,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 54,620,000.00 USD | 54,620,000.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 56,070,000.00 USD | 56,070,000.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 57,190,000.00 USD | 57,190,000.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 926.94 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.04` | 58,280,000.00 USD | 58,280,000.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 59,730,000.00 USD | 59,730,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 5,020.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 60,410,000.00 USD | 60,410,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 61,580,000.00 USD | 61,580,000.00 USD | 358,750.00 USD | 137,080.00 USD | 673,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 62,100,000.00 USD | 62,100,000.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 1,090.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 62,640,000.00 USD | 62,640,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 63,030,000.00 USD | 63,030,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 63,620,000.00 USD | 63,620,000.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 1,640.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.12` | 64,190,000.00 USD | 64,190,000.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 64,760,000.00 USD | 64,760,000.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,080.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 65,200,000.00 USD | 65,200,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.15` | 65,750,000.00 USD | 65,750,000.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 66,270,000.00 USD | 66,270,000.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 2,900.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 66,940,000.00 USD | 66,940,000.00 USD | 280,710.00 USD | 85,040.00 USD | 309,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.18` | 67,200,000.00 USD | 67,200,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 67,420,000.00 USD | 67,420,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 1,040.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 67,670,000.00 USD | 67,670,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.21` | 67,900,000.00 USD | 67,900,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 1,040,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.22` | 67,970,000.00 USD | 67,970,000.00 USD | 52,130.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 68,020,000.00 USD | 68,020,000.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.25` | 1,110.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 853.50 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 257.38 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 114.37 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,600.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 90,820.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 23,600.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.39` | 20,300.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 35,680.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 1,050.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 291,860.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 88,100.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.49` | 62,250.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 77,760.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 40,180.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 715.30 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 56,250.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 334.26 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 40,990.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 127.49 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 2,670.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 56,160.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 7,330.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 281,130.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 2,720.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 1,260.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 693.33 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 2,380.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 45,180.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 42,740.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 378,690.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 5,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 18,080.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.55` | 51,310.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 454.95 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 103,110.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.64` | 6,080.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 1,980,000.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 3,380.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.76` | 1,240,000.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 36,120.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.86` | 649.17 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 46,020.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 164.55 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 7,660.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.96` | 191.26 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.07` | 192.87 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 9,850.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.16` | 1,790.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.20` | 5,720.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 68,550.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.28` | 576.91 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 1,630.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 88,860.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 107,860.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.49` | 1,160.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 7,790,000.00 USD | 17,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 16,790.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 4,220.00 USD | 17,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.55` | 10,090,000.00 USD | 27,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 794.91 USD | 27,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 27,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 26,770.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 576,600.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 1,440,000.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.68` | 160.62 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 495.94 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.76` | 38,700.00 USD | 29,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.80` | 2,840.00 USD | 29,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 334,500.00 USD | 30,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 28,790.00 USD | 30,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 13,850.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 1,800.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 30,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.12` | 2,690.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.15` | 190.01 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.21` | 248,640.00 USD | 30,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8350` | 29,430,000.00 USD | 0.00 USD | 4,740,000.00 USD | `-79.67%` | `5,680,532.50` |
| `Live` | `Long` | `0.8450` | 24,690,000.00 USD | 0.00 USD | 2,030.00 USD | `-79.42%` | `2,406.30` |
| `Live` | `Long` | `0.8550` | 24,690,000.00 USD | 0.00 USD | 10,600.00 USD | `-79.18%` | `12,395.50` |
| `Live` | `Long` | `0.8650` | 24,680,000.00 USD | 0.00 USD | 433.80 USD | `-78.94%` | `501.50` |
| `Live` | `Long` | `0.8750` | 24,680,000.00 USD | 0.00 USD | 12,940.00 USD | `-78.69%` | `14,783.90` |
| `Live` | `Long` | `0.8850` | 24,660,000.00 USD | 0.00 USD | 5,690.00 USD | `-78.45%` | `6,426.50` |
| `Live` | `Long` | `0.8950` | 24,660,000.00 USD | 0.00 USD | 38,570.00 USD | `-78.21%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 24,620,000.00 USD | 0.00 USD | 292.22 USD | `-77.96%` | `322.90` |
| `Live` | `Long` | `0.9150` | 24,620,000.00 USD | 0.00 USD | 13,040.00 USD | `-77.72%` | `14,246.80` |
| `Live` | `Long` | `0.9250` | 24,610,000.00 USD | 0.00 USD | 778.57 USD | `-77.47%` | `841.70` |
| `Live` | `Long` | `0.9550` | 24,610,000.00 USD | 0.00 USD | 1,910.00 USD | `-76.74%` | `2,001.60` |
| `Live` | `Long` | `0.9650` | 24,600,000.00 USD | 0.00 USD | 965.00 USD | `-76.50%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 24,600,000.00 USD | 0.00 USD | 707.53 USD | `-76.01%` | `718.30` |
| `Live` | `Long` | `0.9950` | 24,600,000.00 USD | 0.00 USD | 154,200.00 USD | `-75.77%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 24,450,000.00 USD | 0.00 USD | 488.33 USD | `-75.53%` | `485.90` |
| `Live` | `Long` | `1.02` | 24,450,000.00 USD | 0.00 USD | 10,250.00 USD | `-75.04%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 24,440,000.00 USD | 0.00 USD | 36,980.00 USD | `-74.80%` | `35,734.20` |
| `Live` | `Long` | `1.05` | 24,400,000.00 USD | 0.00 USD | 12,660.00 USD | `-74.31%` | `12,003.60` |
| `Live` | `Long` | `1.06` | 24,390,000.00 USD | 0.00 USD | 892.90 USD | `-74.07%` | `838.40` |
| `Live` | `Long` | `1.07` | 24,390,000.00 USD | 0.00 USD | 7,510.00 USD | `-73.82%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 24,380,000.00 USD | 0.00 USD | 216.89 USD | `-73.58%` | `199.90` |
| `Live` | `Long` | `1.10` | 24,380,000.00 USD | 0.00 USD | 4,270.00 USD | `-73.09%` | `3,866.20` |
| `Live` | `Long` | `1.11` | 24,380,000.00 USD | 0.00 USD | 1,150.00 USD | `-72.85%` | `1,031.60` |
| `Live` | `Long` | `1.12` | 24,370,000.00 USD | 0.00 USD | 301.95 USD | `-72.60%` | `268.40` |
| `Live` | `Long` | `1.14` | 24,370,000.00 USD | 0.00 USD | 4,960.00 USD | `-72.36%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 24,370,000.00 USD | 0.00 USD | 34,680.00 USD | `-72.12%` | `30,290.70` |
| `Live` | `Long` | `1.18` | 24,330,000.00 USD | 0.00 USD | 184.59 USD | `-71.39%` | `157.10` |
| `Live` | `Long` | `1.19` | 24,330,000.00 USD | 0.00 USD | 1,000.00 USD | `-71.14%` | `847.00` |
| `Live` | `Long` | `1.20` | 24,330,000.00 USD | 0.00 USD | 173.51 USD | `-70.90%` | `145.20` |
| `Live` | `Long` | `1.21` | 24,330,000.00 USD | 0.00 USD | 149.66 USD | `-70.66%` | `124.20` |
| `Live` | `Long` | `1.22` | 24,330,000.00 USD | 0.00 USD | 2,580.00 USD | `-70.41%` | `2,123.00` |
| `Live` | `Long` | `1.23` | 24,330,000.00 USD | 0.00 USD | 255.41 USD | `-70.17%` | `208.50` |
| `Live` | `Long` | `1.24` | 24,330,000.00 USD | 0.00 USD | 243.05 USD | `-69.93%` | `196.80` |
| `Live` | `Long` | `1.25` | 24,330,000.00 USD | 0.00 USD | 43,220.00 USD | `-69.68%` | `34,711.70` |
| `Live` | `Long` | `1.25` | 24,290,000.00 USD | 0.00 USD | 115,200.00 USD | `-69.44%` | `91,789.50` |
| `Live` | `Long` | `1.26` | 24,170,000.00 USD | 0.00 USD | 2,060.00 USD | `-69.20%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 24,170,000.00 USD | 0.00 USD | 2,390.00 USD | `-68.95%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 24,170,000.00 USD | 0.00 USD | 2,040.00 USD | `-68.71%` | `1,584.00` |
| `Live` | `Long` | `1.29` | 24,160,000.00 USD | 0.00 USD | 2,180.00 USD | `-68.46%` | `1,682.50` |
| `Live` | `Long` | `1.30` | 24,160,000.00 USD | 0.00 USD | 4,240.00 USD | `-68.22%` | `3,245.50` |
| `Live` | `Long` | `1.31` | 24,160,000.00 USD | 0.00 USD | 11,180.00 USD | `-67.98%` | `8,500.00` |
| `Live` | `Long` | `1.32` | 24,150,000.00 USD | 0.00 USD | 10,050.00 USD | `-67.73%` | `7,584.00` |
| `Live` | `Long` | `1.33` | 24,140,000.00 USD | 0.00 USD | 417.32 USD | `-67.49%` | `312.60` |
| `Live` | `Long` | `1.34` | 24,140,000.00 USD | 0.00 USD | 603.91 USD | `-67.25%` | `449.00` |
| `Live` | `Long` | `1.35` | 24,140,000.00 USD | 0.00 USD | 65,120.00 USD | `-67.00%` | `48,059.70` |
| `Live` | `Long` | `1.36` | 24,070,000.00 USD | 0.00 USD | 911.41 USD | `-66.76%` | `667.70` |
| `Live` | `Long` | `1.38` | 24,070,000.00 USD | 0.00 USD | 14,580.00 USD | `-66.52%` | `10,602.80` |
| `Live` | `Long` | `1.39` | 24,060,000.00 USD | 0.00 USD | 295.56 USD | `-66.27%` | `213.40` |
| `Live` | `Long` | `1.40` | 24,060,000.00 USD | 0.00 USD | 42,490.00 USD | `-66.03%` | `30,458.70` |
| `Live` | `Long` | `1.42` | 24,010,000.00 USD | 0.00 USD | 2,020.00 USD | `-65.54%` | `1,428.20` |
| `Live` | `Long` | `1.43` | 24,010,000.00 USD | 0.00 USD | 712.50 USD | `-65.30%` | `500.00` |
| `Live` | `Long` | `1.45` | 24,010,000.00 USD | 0.00 USD | 362,290.00 USD | `-64.81%` | `250,718.10` |
| `Live` | `Long` | `1.47` | 23,650,000.00 USD | 0.00 USD | 429.83 USD | `-64.32%` | `293.40` |
| `Live` | `Long` | `1.48` | 23,650,000.00 USD | 0.00 USD | 1,990.00 USD | `-64.08%` | `1,350.00` |
| `Live` | `Long` | `1.50` | 23,650,000.00 USD | 0.00 USD | 743.46 USD | `-63.59%` | `497.30` |
| `Live` | `Long` | `1.50` | 23,640,000.00 USD | 0.00 USD | 3,150.00 USD | `-63.35%` | `2,096.20` |
| `Live` | `Long` | `1.51` | 23,640,000.00 USD | 0.00 USD | 7,190.00 USD | `-63.11%` | `4,746.30` |
| `Live` | `Long` | `1.52` | 23,630,000.00 USD | 0.00 USD | 610.00 USD | `-62.86%` | `400.00` |
| `Live` | `Long` | `1.53` | 23,630,000.00 USD | 0.00 USD | 279.37 USD | `-62.62%` | `182.00` |
| `Live` | `Long` | `1.56` | 23,630,000.00 USD | 0.00 USD | 14,130.00 USD | `-61.89%` | `9,025.80` |
| `Live` | `Long` | `1.57` | 23,620,000.00 USD | 0.00 USD | 589.52 USD | `-61.65%` | `374.30` |
| `Live` | `Long` | `1.58` | 23,620,000.00 USD | 0.00 USD | 16,170.00 USD | `-61.40%` | `10,200.00` |
| `Live` | `Long` | `1.59` | 23,600,000.00 USD | 0.00 USD | 83,130.00 USD | `-61.16%` | `52,119.70` |
| `Live` | `Long` | `1.60` | 23,520,000.00 USD | 0.00 USD | 47,140.00 USD | `-60.92%` | `29,369.40` |
| `Live` | `Long` | `1.61` | 23,470,000.00 USD | 0.00 USD | 4,770.00 USD | `-60.67%` | `2,953.60` |
| `Live` | `Long` | `1.62` | 23,470,000.00 USD | 0.00 USD | 12,250.00 USD | `-60.43%` | `7,537.90` |
| `Live` | `Long` | `1.64` | 23,460,000.00 USD | 0.00 USD | 2,150.00 USD | `-60.19%` | `1,316.00` |
| `Live` | `Long` | `1.65` | 23,450,000.00 USD | 0.00 USD | 981.08 USD | `-59.94%` | `596.40` |
| `Live` | `Long` | `1.66` | 23,450,000.00 USD | 0.00 USD | 384.13 USD | `-59.70%` | `232.10` |
| `Live` | `Long` | `1.67` | 23,450,000.00 USD | 0.00 USD | 212.29 USD | `-59.45%` | `127.50` |
| `Live` | `Long` | `1.68` | 23,450,000.00 USD | 0.00 USD | 108.71 USD | `-59.21%` | `64.90` |
| `Live` | `Long` | `1.69` | 23,450,000.00 USD | 0.00 USD | 602,850.00 USD | `-58.97%` | `357,774.30` |
| `Live` | `Long` | `1.70` | 22,850,000.00 USD | 0.00 USD | 4,980.00 USD | `-58.72%` | `2,938.10` |
| `Live` | `Long` | `1.71` | 22,840,000.00 USD | 0.00 USD | 168.97 USD | `-58.48%` | `99.10` |
| `Live` | `Long` | `1.73` | 22,840,000.00 USD | 0.00 USD | 5,630.00 USD | `-57.99%` | `3,264.50` |
| `Live` | `Long` | `1.74` | 22,840,000.00 USD | 0.00 USD | 1,320.00 USD | `-57.75%` | `758.60` |
| `Live` | `Long` | `1.75` | 22,840,000.00 USD | 0.00 USD | 10,710.00 USD | `-57.26%` | `6,104.70` |
| `Live` | `Long` | `1.76` | 22,830,000.00 USD | 0.00 USD | 1,090.00 USD | `-57.02%` | `618.50` |
| `Live` | `Long` | `1.77` | 22,820,000.00 USD | 0.00 USD | 17,220.00 USD | `-56.78%` | `9,703.40` |
| `Live` | `Long` | `1.78` | 22,810,000.00 USD | 0.00 USD | 1,210.00 USD | `-56.53%` | `680.60` |
| `Live` | `Long` | `1.80` | 22,810,000.00 USD | 0.00 USD | 5,280.00 USD | `-56.05%` | `2,925.80` |
| `Live` | `Long` | `1.81` | 22,800,000.00 USD | 0.00 USD | 1,580.00 USD | `-55.80%` | `873.20` |
| `Live` | `Long` | `1.82` | 22,800,000.00 USD | 0.00 USD | 1,280.00 USD | `-55.56%` | `699.50` |
| `Live` | `Long` | `1.83` | 22,800,000.00 USD | 0.00 USD | 27,520.00 USD | `-55.31%` | `15,000.00` |
| `Live` | `Long` | `1.85` | 22,770,000.00 USD | 0.00 USD | 2,040.00 USD | `-54.83%` | `1,098.00` |
| `Live` | `Long` | `1.86` | 22,770,000.00 USD | 0.00 USD | 652.75 USD | `-54.58%` | `350.00` |
| `Live` | `Long` | `1.88` | 22,770,000.00 USD | 0.00 USD | 937.50 USD | `-54.34%` | `500.00` |
| `Live` | `Long` | `1.90` | 22,770,000.00 USD | 0.00 USD | 2,080.00 USD | `-53.85%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 22,760,000.00 USD | 0.00 USD | 62,210.00 USD | `-53.61%` | `32,656.30` |
| `Live` | `Long` | `1.92` | 22,700,000.00 USD | 0.00 USD | 3,110.00 USD | `-53.37%` | `1,623.00` |
| `Live` | `Long` | `1.93` | 22,700,000.00 USD | 0.00 USD | 35,380.00 USD | `-53.12%` | `18,379.00` |
| `Live` | `Long` | `1.94` | 22,660,000.00 USD | 0.00 USD | 10,800.00 USD | `-52.88%` | `5,583.80` |
| `Live` | `Long` | `1.95` | 22,650,000.00 USD | 0.00 USD | 2,740.00 USD | `-52.64%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 22,650,000.00 USD | 0.00 USD | 775.55 USD | `-52.39%` | `396.70` |
| `Live` | `Long` | `1.97` | 22,650,000.00 USD | 0.00 USD | 5,930.00 USD | `-52.15%` | `3,019.30` |
| `Live` | `Long` | `1.98` | 22,640,000.00 USD | 0.00 USD | 47,310.00 USD | `-51.91%` | `23,954.80` |
| `Live` | `Long` | `1.99` | 22,600,000.00 USD | 0.00 USD | 2,450.00 USD | `-51.66%` | `1,234.10` |
| `Live` | `Long` | `2.00` | 22,590,000.00 USD | 0.00 USD | 124,920.00 USD | `-51.17%` | `62,302.60` |
| `Live` | `Long` | `2.02` | 22,470,000.00 USD | 0.00 USD | 260.62 USD | `-50.69%` | `128.70` |
| `Live` | `Long` | `2.04` | 22,470,000.00 USD | 0.00 USD | 3,460.00 USD | `-50.20%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 22,470,000.00 USD | 0.00 USD | 7,750.00 USD | `-49.96%` | `3,769.20` |
| `Live` | `Long` | `2.08` | 22,460,000.00 USD | 0.00 USD | 2,780.00 USD | `-49.47%` | `1,342.10` |
| `Live` | `Long` | `2.08` | 22,450,000.00 USD | 0.00 USD | 10,480.00 USD | `-49.23%` | `5,026.30` |
| `Live` | `Long` | `2.10` | 22,440,000.00 USD | 0.00 USD | 1,100.00 USD | `-48.98%` | `527.40` |
| `Live` | `Long` | `2.10` | 22,440,000.00 USD | 0.00 USD | 7,520.00 USD | `-48.74%` | `3,572.20` |
| `Live` | `Long` | `2.12` | 22,440,000.00 USD | 0.00 USD | 11,960.00 USD | `-48.50%` | `5,657.20` |
| `Live` | `Long` | `2.12` | 22,420,000.00 USD | 0.00 USD | 96,590.00 USD | `-48.25%` | `45,454.50` |
| `Live` | `Long` | `2.13` | 22,330,000.00 USD | 0.00 USD | 202.82 USD | `-48.01%` | `95.00` |
| `Live` | `Long` | `2.15` | 22,330,000.00 USD | 0.00 USD | 2,110.00 USD | `-47.77%` | `983.60` |
| `Live` | `Long` | `2.15` | 22,320,000.00 USD | 0.00 USD | 773.00 USD | `-47.52%` | `358.70` |
| `Live` | `Long` | `2.17` | 22,320,000.00 USD | 0.00 USD | 1,520.00 USD | `-47.28%` | `704.10` |
| `Live` | `Long` | `2.17` | 22,320,000.00 USD | 0.00 USD | 13,580.00 USD | `-47.04%` | `6,244.90` |
| `Live` | `Long` | `2.19` | 22,310,000.00 USD | 0.00 USD | 15,070.00 USD | `-46.79%` | `6,894.90` |
| `Live` | `Long` | `2.19` | 22,290,000.00 USD | 0.00 USD | 815.44 USD | `-46.55%` | `371.50` |
| `Live` | `Long` | `2.21` | 22,290,000.00 USD | 0.00 USD | 76,110.00 USD | `-46.30%` | `34,517.30` |
| `Live` | `Long` | `2.21` | 22,220,000.00 USD | 0.00 USD | 4,190.00 USD | `-46.06%` | `1,890.30` |
| `Live` | `Long` | `2.23` | 22,210,000.00 USD | 0.00 USD | 20,940.00 USD | `-45.82%` | `9,410.30` |
| `Live` | `Long` | `2.23` | 22,190,000.00 USD | 0.00 USD | 3,400.00 USD | `-45.57%` | `1,519.40` |
| `Live` | `Long` | `2.25` | 22,190,000.00 USD | 0.00 USD | 44,890.00 USD | `-45.33%` | `19,993.70` |
| `Live` | `Long` | `2.25` | 22,140,000.00 USD | 0.00 USD | 149,130.00 USD | `-45.09%` | `66,134.90` |
| `Live` | `Long` | `2.27` | 21,990,000.00 USD | 0.00 USD | 7,930.00 USD | `-44.84%` | `3,500.00` |
| `Live` | `Long` | `2.27` | 21,990,000.00 USD | 0.00 USD | 529.85 USD | `-44.60%` | `232.90` |
| `Live` | `Long` | `2.29` | 21,990,000.00 USD | 0.00 USD | 10,720.00 USD | `-44.36%` | `4,693.20` |
| `Live` | `Long` | `2.29` | 21,980,000.00 USD | 0.00 USD | 306,010.00 USD | `-44.11%` | `133,336.20` |
| `Live` | `Long` | `2.31` | 21,670,000.00 USD | 0.00 USD | 1,980.00 USD | `-43.87%` | `859.80` |
| `Live` | `Long` | `2.31` | 21,670,000.00 USD | 0.00 USD | 105,380.00 USD | `-43.63%` | `45,522.10` |
| `Live` | `Long` | `2.33` | 21,560,000.00 USD | 0.00 USD | 237,770.00 USD | `-43.38%` | `102,265.00` |
| `Live` | `Long` | `2.33` | 21,320,000.00 USD | 0.00 USD | 4,240.00 USD | `-43.14%` | `1,817.80` |
| `Live` | `Long` | `2.35` | 21,320,000.00 USD | 0.00 USD | 58,430.00 USD | `-42.90%` | `24,917.90` |
| `Live` | `Long` | `2.35` | 21,260,000.00 USD | 0.00 USD | 143.66 USD | `-42.65%` | `61.00` |
| `Live` | `Long` | `2.37` | 21,260,000.00 USD | 0.00 USD | 30,230.00 USD | `-42.41%` | `12,783.60` |
| `Live` | `Long` | `2.38` | 21,230,000.00 USD | 0.00 USD | 419,870.00 USD | `-42.16%` | `176,789.20` |
| `Live` | `Long` | `2.38` | 20,810,000.00 USD | 0.00 USD | 1,640.00 USD | `-41.92%` | `688.50` |
| `Live` | `Long` | `2.40` | 20,810,000.00 USD | 0.00 USD | 27,900.00 USD | `-41.68%` | `11,648.10` |
| `Live` | `Long` | `2.40` | 20,780,000.00 USD | 0.00 USD | 1,570.00 USD | `-41.43%` | `654.00` |
| `Live` | `Long` | `2.42` | 20,780,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-41.19%` | `734,168.40` |
| `Live` | `Long` | `2.42` | 19,010,000.00 USD | 0.00 USD | 273,060.00 USD | `-40.95%` | `112,601.40` |
| `Live` | `Long` | `2.44` | 18,730,000.00 USD | 0.00 USD | 2,680.00 USD | `-40.70%` | `1,099.20` |
| `Live` | `Long` | `2.44` | 18,730,000.00 USD | 0.00 USD | 4,260.00 USD | `-40.46%` | `1,741.30` |
| `Live` | `Long` | `2.46` | 18,730,000.00 USD | 0.00 USD | 137,190.00 USD | `-40.22%` | `55,882.00` |
| `Live` | `Long` | `2.46` | 18,590,000.00 USD | 0.00 USD | 11,160.00 USD | `-39.97%` | `4,529.10` |
| `Live` | `Long` | `2.48` | 18,580,000.00 USD | 0.00 USD | 340.81 USD | `-39.73%` | `137.70` |
| `Live` | `Long` | `2.48` | 18,580,000.00 USD | 0.00 USD | 19,450.00 USD | `-39.49%` | `7,828.60` |
| `Live` | `Long` | `2.50` | 18,560,000.00 USD | 0.00 USD | 1,110.00 USD | `-39.24%` | `443.10` |
| `Live` | `Long` | `2.50` | 18,560,000.00 USD | 0.00 USD | 8,240.00 USD | `-39.00%` | `3,288.50` |
| `Live` | `Long` | `2.52` | 18,550,000.00 USD | 0.00 USD | 121.98 USD | `-38.76%` | `48.50` |
| `Live` | `Long` | `2.52` | 18,550,000.00 USD | 0.00 USD | 19,460.00 USD | `-38.51%` | `7,705.40` |
| `Live` | `Long` | `2.54` | 18,530,000.00 USD | 0.00 USD | 698.39 USD | `-38.27%` | `275.50` |
| `Live` | `Long` | `2.54` | 18,530,000.00 USD | 0.00 USD | 10,920.00 USD | `-38.03%` | `4,291.70` |
| `Live` | `Long` | `2.56` | 18,520,000.00 USD | 0.00 USD | 5,800.00 USD | `-37.78%` | `2,272.00` |
| `Live` | `Long` | `2.56` | 18,510,000.00 USD | 0.00 USD | 53,870.00 USD | `-37.54%` | `21,003.00` |
| `Live` | `Long` | `2.58` | 18,460,000.00 USD | 0.00 USD | 11,910.00 USD | `-37.29%` | `4,626.40` |
| `Live` | `Long` | `2.58` | 18,450,000.00 USD | 0.00 USD | 1,570.00 USD | `-37.05%` | `606.80` |
| `Live` | `Long` | `2.60` | 18,450,000.00 USD | 0.00 USD | 75,100.00 USD | `-36.81%` | `28,940.80` |
| `Live` | `Long` | `2.60` | 18,370,000.00 USD | 0.00 USD | 21,590.00 USD | `-36.56%` | `8,286.30` |
| `Live` | `Long` | `2.62` | 18,350,000.00 USD | 0.00 USD | 17,370.00 USD | `-36.32%` | `6,641.00` |
| `Live` | `Long` | `2.62` | 18,330,000.00 USD | 0.00 USD | 224.44 USD | `-36.08%` | `85.50` |
| `Live` | `Long` | `2.63` | 18,330,000.00 USD | 0.00 USD | 25,170.00 USD | `-35.83%` | `9,551.20` |
| `Live` | `Long` | `2.65` | 18,310,000.00 USD | 0.00 USD | 9,050.00 USD | `-35.59%` | `3,422.50` |
| `Live` | `Long` | `2.65` | 18,300,000.00 USD | 0.00 USD | 18,970.00 USD | `-35.35%` | `7,146.40` |
| `Live` | `Long` | `2.67` | 18,280,000.00 USD | 0.00 USD | 4,580.00 USD | `-35.10%` | `1,717.80` |
| `Live` | `Long` | `2.67` | 18,270,000.00 USD | 0.00 USD | 1,760.00 USD | `-34.86%` | `658.60` |
| `Live` | `Long` | `2.69` | 18,270,000.00 USD | 0.00 USD | 7,280.00 USD | `-34.62%` | `2,709.60` |
| `Live` | `Long` | `2.69` | 18,260,000.00 USD | 0.00 USD | 6,230.00 USD | `-34.37%` | `2,310.80` |
| `Live` | `Long` | `2.71` | 18,260,000.00 USD | 0.00 USD | 120,220.00 USD | `-34.13%` | `44,443.30` |
| `Live` | `Long` | `2.71` | 18,140,000.00 USD | 0.00 USD | 15,010.00 USD | `-33.89%` | `5,527.50` |
| `Live` | `Long` | `2.73` | 18,120,000.00 USD | 0.00 USD | 27,130.00 USD | `-33.64%` | `9,955.90` |
| `Live` | `Long` | `2.73` | 18,100,000.00 USD | 0.00 USD | 42,810.00 USD | `-33.40%` | `15,652.30` |
| `Live` | `Long` | `2.75` | 18,050,000.00 USD | 0.00 USD | 47,240.00 USD | `-33.15%` | `17,208.60` |
| `Live` | `Long` | `2.75` | 18,010,000.00 USD | 0.00 USD | 1,670.00 USD | `-32.91%` | `606.30` |
| `Live` | `Long` | `2.77` | 18,000,000.00 USD | 0.00 USD | 6,730.00 USD | `-32.67%` | `2,435.70` |
| `Live` | `Long` | `2.77` | 18,000,000.00 USD | 0.00 USD | 719.84 USD | `-32.42%` | `259.40` |
| `Live` | `Long` | `2.79` | 18,000,000.00 USD | 0.00 USD | 26,980.00 USD | `-32.18%` | `9,686.50` |
| `Live` | `Long` | `2.79` | 17,970,000.00 USD | 0.00 USD | 24,560.00 USD | `-31.94%` | `8,788.30` |
| `Live` | `Long` | `2.81` | 17,940,000.00 USD | 0.00 USD | 6,310.00 USD | `-31.69%` | `2,248.90` |
| `Live` | `Long` | `2.81` | 17,940,000.00 USD | 0.00 USD | 11,780.00 USD | `-31.45%` | `4,185.90` |
| `Live` | `Long` | `2.83` | 17,930,000.00 USD | 0.00 USD | 260,210.00 USD | `-31.21%` | `92,110.10` |
| `Live` | `Long` | `2.83` | 17,670,000.00 USD | 0.00 USD | 10,470.00 USD | `-30.96%` | `3,693.90` |
| `Live` | `Long` | `2.85` | 17,660,000.00 USD | 0.00 USD | 4,240.00 USD | `-30.72%` | `1,492.00` |
| `Live` | `Long` | `2.85` | 17,650,000.00 USD | 0.00 USD | 1,860.00 USD | `-30.48%` | `652.60` |
| `Live` | `Long` | `2.87` | 17,650,000.00 USD | 0.00 USD | 8,570.00 USD | `-30.23%` | `2,992.60` |
| `Live` | `Long` | `2.88` | 17,640,000.00 USD | 0.00 USD | 378,680.00 USD | `-29.99%` | `131,715.30` |
| `Live` | `Long` | `2.88` | 17,260,000.00 USD | 0.00 USD | 52,190.00 USD | `-29.75%` | `18,088.60` |
| `Live` | `Long` | `2.90` | 17,210,000.00 USD | 0.00 USD | 101,800.00 USD | `-29.50%` | `35,164.60` |
| `Live` | `Long` | `2.90` | 17,110,000.00 USD | 0.00 USD | 1,330.00 USD | `-29.26%` | `458.20` |
| `Live` | `Long` | `2.92` | 17,110,000.00 USD | 0.00 USD | 93,010.00 USD | `-29.01%` | `31,908.00` |
| `Live` | `Long` | `2.92` | 17,010,000.00 USD | 0.00 USD | 191,130.00 USD | `-28.77%` | `65,343.20` |
| `Live` | `Long` | `2.94` | 16,820,000.00 USD | 0.00 USD | 61,920.00 USD | `-28.53%` | `21,096.80` |
| `Live` | `Long` | `2.94` | 16,760,000.00 USD | 0.00 USD | 1,010.00 USD | `-28.28%` | `341.80` |
| `Live` | `Long` | `2.96` | 16,760,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-28.04%` | `916,282.50` |
| `Live` | `Long` | `2.96` | 14,050,000.00 USD | 0.00 USD | 1,050.00 USD | `-27.80%` | `354.20` |
| `Live` | `Long` | `2.98` | 14,050,000.00 USD | 0.00 USD | 11,090.00 USD | `-27.55%` | `3,729.00` |
| `Live` | `Long` | `2.98` | 14,040,000.00 USD | 0.00 USD | 22,840.00 USD | `-27.31%` | `7,650.30` |
| `Live` | `Long` | `3.00` | 14,020,000.00 USD | 0.00 USD | 366,890.00 USD | `-27.07%` | `122,501.30` |
| `Live` | `Long` | `3.00` | 13,650,000.00 USD | 0.00 USD | 10,410.00 USD | `-26.82%` | `3,463.30` |
| `Live` | `Long` | `3.02` | 13,640,000.00 USD | 0.00 USD | 11,290.00 USD | `-26.58%` | `3,743.00` |
| `Live` | `Long` | `3.02` | 13,630,000.00 USD | 0.00 USD | 27,700.00 USD | `-26.34%` | `9,158.30` |
| `Live` | `Long` | `3.04` | 13,600,000.00 USD | 0.00 USD | 149.63 USD | `-26.09%` | `49.30` |
| `Live` | `Long` | `3.04` | 13,600,000.00 USD | 0.00 USD | 103,780.00 USD | `-25.85%` | `34,081.60` |
| `Live` | `Long` | `3.06` | 13,500,000.00 USD | 0.00 USD | 245,370.00 USD | `-25.61%` | `80,317.70` |
| `Live` | `Long` | `3.06` | 13,250,000.00 USD | 0.00 USD | 115,550.00 USD | `-25.36%` | `37,700.70` |
| `Live` | `Long` | `3.08` | 13,140,000.00 USD | 0.00 USD | 13,960.00 USD | `-25.12%` | `4,539.80` |
| `Live` | `Long` | `3.08` | 13,120,000.00 USD | 0.00 USD | 146,750.00 USD | `-24.88%` | `47,569.50` |
| `Live` | `Long` | `3.10` | 12,980,000.00 USD | 0.00 USD | 5,540.00 USD | `-24.63%` | `1,790.00` |
| `Live` | `Long` | `3.10` | 12,970,000.00 USD | 0.00 USD | 45,400.00 USD | `-24.39%` | `14,621.80` |
| `Live` | `Long` | `3.12` | 12,920,000.00 USD | 0.00 USD | 20,110.00 USD | `-24.14%` | `6,454.90` |
| `Live` | `Long` | `3.12` | 12,900,000.00 USD | 0.00 USD | 9,680.00 USD | `-23.90%` | `3,098.90` |
| `Live` | `Long` | `3.13` | 12,900,000.00 USD | 0.00 USD | 37,690.00 USD | `-23.66%` | `12,023.00` |
| `Live` | `Long` | `3.15` | 12,860,000.00 USD | 0.00 USD | 11,350.00 USD | `-23.41%` | `3,610.40` |
| `Live` | `Long` | `3.15` | 12,850,000.00 USD | 0.00 USD | 7,580.00 USD | `-23.17%` | `2,404.10` |
| `Live` | `Long` | `3.17` | 12,840,000.00 USD | 0.00 USD | 10,030.00 USD | `-22.93%` | `3,169.30` |
| `Live` | `Long` | `3.17` | 12,830,000.00 USD | 0.00 USD | 5,350.00 USD | `-22.68%` | `1,685.30` |
| `Live` | `Long` | `3.19` | 12,820,000.00 USD | 0.00 USD | 630,260.00 USD | `-22.44%` | `197,882.60` |
| `Live` | `Long` | `3.19` | 12,190,000.00 USD | 0.00 USD | 6,250.00 USD | `-22.20%` | `1,956.90` |
| `Live` | `Long` | `3.21` | 12,190,000.00 USD | 0.00 USD | 104,290.00 USD | `-21.95%` | `32,540.90` |
| `Live` | `Long` | `3.21` | 12,080,000.00 USD | 0.00 USD | 13,860.00 USD | `-21.71%` | `4,311.80` |
| `Live` | `Long` | `3.23` | 12,070,000.00 USD | 0.00 USD | 25,260.00 USD | `-21.47%` | `7,832.00` |
| `Live` | `Long` | `3.23` | 12,040,000.00 USD | 0.00 USD | 53,140.00 USD | `-21.22%` | `16,428.00` |
| `Live` | `Long` | `3.25` | 11,990,000.00 USD | 0.00 USD | 17,670.00 USD | `-20.98%` | `5,446.00` |
| `Live` | `Long` | `3.25` | 11,970,000.00 USD | 0.00 USD | 18,010.00 USD | `-20.74%` | `5,533.70` |
| `Live` | `Long` | `3.27` | 11,950,000.00 USD | 0.00 USD | 33,820.00 USD | `-20.49%` | `10,358.60` |
| `Live` | `Long` | `3.27` | 11,920,000.00 USD | 0.00 USD | 842,170.00 USD | `-20.25%` | `257,151.40` |
| `Live` | `Long` | `3.29` | 11,080,000.00 USD | 0.00 USD | 2,680.00 USD | `-20.00%` | `815.20` |
| `Live` | `Long` | `3.29` | 11,080,000.00 USD | 0.00 USD | 209,990.00 USD | `-19.76%` | `63,730.70` |
| `Live` | `Long` | `3.31` | 10,870,000.00 USD | 0.00 USD | 141,170.00 USD | `-19.52%` | `42,712.80` |
| `Live` | `Long` | `3.31` | 10,720,000.00 USD | 0.00 USD | 29,280.00 USD | `-19.27%` | `8,832.80` |
| `Live` | `Long` | `3.33` | 10,700,000.00 USD | 0.00 USD | 24,800.00 USD | `-19.03%` | `7,457.50` |
| `Live` | `Long` | `3.33` | 10,670,000.00 USD | 0.00 USD | 64,220.00 USD | `-18.79%` | `19,257.60` |
| `Live` | `Long` | `3.35` | 10,610,000.00 USD | 0.00 USD | 40,110.00 USD | `-18.54%` | `11,992.50` |
| `Live` | `Long` | `3.37` | 10,570,000.00 USD | 0.00 USD | 137,860.00 USD | `-18.06%` | `40,969.90` |
| `Live` | `Long` | `3.38` | 10,430,000.00 USD | 0.00 USD | 569,260.00 USD | `-17.81%` | `168,670.20` |
| `Live` | `Long` | `3.38` | 9,860,000.00 USD | 0.00 USD | 44,450.00 USD | `-17.57%` | `13,131.00` |
| `Live` | `Long` | `3.40` | 9,810,000.00 USD | 0.00 USD | 844.34 USD | `-17.33%` | `248.70` |
| `Live` | `Long` | `3.40` | 9,810,000.00 USD | 0.00 USD | 76,570.00 USD | `-17.08%` | `22,488.20` |
| `Live` | `Long` | `3.42` | 9,740,000.00 USD | 0.00 USD | 181,600.00 USD | `-16.84%` | `53,175.70` |
| `Live` | `Long` | `3.42` | 9,560,000.00 USD | 0.00 USD | 5,290.00 USD | `-16.60%` | `1,545.80` |
| `Live` | `Long` | `3.44` | 9,550,000.00 USD | 0.00 USD | 23,970.00 USD | `-16.35%` | `6,978.10` |
| `Live` | `Long` | `3.44` | 9,530,000.00 USD | 0.00 USD | 9,830.00 USD | `-16.11%` | `2,854.00` |
| `Live` | `Long` | `3.46` | 9,520,000.00 USD | 0.00 USD | 9,260.00 USD | `-15.87%` | `2,680.00` |
| `Live` | `Long` | `3.46` | 9,510,000.00 USD | 0.00 USD | 14,440.00 USD | `-15.62%` | `4,167.90` |
| `Live` | `Long` | `3.48` | 9,490,000.00 USD | 0.00 USD | 105,220.00 USD | `-15.38%` | `30,278.00` |
| `Live` | `Long` | `3.48` | 9,390,000.00 USD | 0.00 USD | 74,160.00 USD | `-15.13%` | `21,278.40` |
| `Live` | `Long` | `3.50` | 9,310,000.00 USD | 0.00 USD | 24,030.00 USD | `-14.89%` | `6,876.20` |
| `Live` | `Long` | `3.50` | 9,290,000.00 USD | 0.00 USD | 45,750.00 USD | `-14.65%` | `13,052.80` |
| `Live` | `Long` | `3.52` | 9,240,000.00 USD | 0.00 USD | 11,870.00 USD | `-14.40%` | `3,376.50` |
| `Live` | `Long` | `3.52` | 9,230,000.00 USD | 0.00 USD | 129,140.00 USD | `-14.16%` | `36,636.80` |
| `Live` | `Long` | `3.54` | 9,100,000.00 USD | 0.00 USD | 163,400.00 USD | `-13.92%` | `46,223.90` |
| `Live` | `Long` | `3.54` | 8,940,000.00 USD | 0.00 USD | 254,870.00 USD | `-13.67%` | `71,894.70` |
| `Live` | `Long` | `3.56` | 8,680,000.00 USD | 0.00 USD | 377,070.00 USD | `-13.43%` | `106,066.40` |
| `Live` | `Long` | `3.56` | 8,310,000.00 USD | 0.00 USD | 15,510.00 USD | `-13.19%` | `4,350.10` |
| `Live` | `Long` | `3.58` | 8,290,000.00 USD | 0.00 USD | 34,970.00 USD | `-12.94%` | `9,781.50` |
| `Live` | `Long` | `3.58` | 8,260,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-12.70%` | `371,249.10` |
| `Live` | `Long` | `3.60` | 6,930,000.00 USD | 0.00 USD | 45,700.00 USD | `-12.46%` | `12,711.80` |
| `Live` | `Long` | `3.60` | 6,880,000.00 USD | 0.00 USD | 150,210.00 USD | `-12.21%` | `41,667.60` |
| `Live` | `Long` | `3.62` | 6,730,000.00 USD | 0.00 USD | 29,400.00 USD | `-11.97%` | `8,133.80` |
| `Live` | `Long` | `3.62` | 6,700,000.00 USD | 0.00 USD | 45,760.00 USD | `-11.73%` | `12,623.00` |
| `Live` | `Long` | `3.63` | 6,650,000.00 USD | 0.00 USD | 50,630.00 USD | `-11.48%` | `13,928.10` |
| `Live` | `Long` | `3.65` | 6,600,000.00 USD | 0.00 USD | 55,690.00 USD | `-11.24%` | `15,277.90` |
| `Live` | `Long` | `3.65` | 6,550,000.00 USD | 0.00 USD | 26,080.00 USD | `-10.99%` | `7,135.40` |
| `Live` | `Long` | `3.67` | 6,520,000.00 USD | 0.00 USD | 912,270.00 USD | `-10.75%` | `248,913.50` |
| `Live` | `Long` | `3.67` | 5,610,000.00 USD | 0.00 USD | 257,380.00 USD | `-10.51%` | `70,034.10` |
| `Live` | `Long` | `3.69` | 5,350,000.00 USD | 0.00 USD | 111,250.00 USD | `-10.26%` | `30,190.10` |
| `Live` | `Long` | `3.69` | 5,240,000.00 USD | 0.00 USD | 112,450.00 USD | `-10.02%` | `30,431.80` |
| `Live` | `Long` | `3.71` | 5,130,000.00 USD | 0.00 USD | 64,270.00 USD | `-9.78%` | `17,346.90` |
| `Live` | `Long` | `3.71` | 5,060,000.00 USD | 0.00 USD | 194,120.00 USD | `-9.53%` | `52,252.60` |
| `Live` | `Long` | `3.73` | 4,870,000.00 USD | 0.00 USD | 28,060.00 USD | `-9.29%` | `7,532.10` |
| `Live` | `Long` | `3.73` | 4,840,000.00 USD | 0.00 USD | 5,760.00 USD | `-9.05%` | `1,542.00` |
| `Live` | `Long` | `3.75` | 4,840,000.00 USD | 0.00 USD | 58,120.00 USD | `-8.80%` | `15,519.10` |
| `Live` | `Long` | `3.75` | 4,780,000.00 USD | 0.00 USD | 80,510.00 USD | `-8.56%` | `21,440.80` |
| `Live` | `Long` | `3.77` | 4,700,000.00 USD | 0.00 USD | 65,500.00 USD | `-8.32%` | `17,397.60` |
| `Live` | `Long` | `3.77` | 4,630,000.00 USD | 0.00 USD | 127,760.00 USD | `-8.07%` | `33,843.00` |
| `Live` | `Long` | `3.79` | 4,500,000.00 USD | 0.00 USD | 49,180.00 USD | `-7.83%` | `12,993.50` |
| `Live` | `Long` | `3.79` | 4,460,000.00 USD | 0.00 USD | 139,870.00 USD | `-7.59%` | `36,855.40` |
| `Live` | `Long` | `3.81` | 4,320,000.00 USD | 0.00 USD | 7,720.00 USD | `-7.34%` | `2,027.90` |
| `Live` | `Long` | `3.81` | 4,310,000.00 USD | 0.00 USD | 25,230.00 USD | `-7.10%` | `6,612.80` |
| `Live` | `Long` | `3.83` | 4,280,000.00 USD | 0.00 USD | 53,580.00 USD | `-6.85%` | `14,008.40` |
| `Live` | `Long` | `3.83` | 4,230,000.00 USD | 0.00 USD | 158,690.00 USD | `-6.61%` | `41,379.20` |
| `Live` | `Long` | `3.85` | 4,070,000.00 USD | 0.00 USD | 96,570.00 USD | `-6.37%` | `25,115.30` |
| `Live` | `Long` | `3.85` | 3,970,000.00 USD | 0.00 USD | 21,270.00 USD | `-6.12%` | `5,517.80` |
| `Live` | `Long` | `3.87` | 3,950,000.00 USD | 0.00 USD | 26,000.00 USD | `-5.88%` | `6,727.30` |
| `Live` | `Long` | `3.88` | 3,930,000.00 USD | 0.00 USD | 22,850.00 USD | `-5.64%` | `5,896.20` |
| `Live` | `Long` | `3.88` | 3,900,000.00 USD | 0.00 USD | 108,570.00 USD | `-5.39%` | `27,944.90` |
| `Live` | `Long` | `3.90` | 3,800,000.00 USD | 0.00 USD | 5,490.00 USD | `-5.15%` | `1,408.30` |
| `Live` | `Long` | `3.90` | 3,790,000.00 USD | 0.00 USD | 10,170.00 USD | `-4.91%` | `2,604.40` |
| `Live` | `Long` | `3.92` | 3,780,000.00 USD | 0.00 USD | 37,980.00 USD | `-4.66%` | `9,701.90` |
| `Live` | `Long` | `3.92` | 3,740,000.00 USD | 0.00 USD | 723,590.00 USD | `-4.42%` | `184,353.00` |
| `Live` | `Long` | `3.94` | 3,020,000.00 USD | 0.00 USD | 202,910.00 USD | `-4.18%` | `51,565.70` |
| `Live` | `Long` | `3.94` | 2,820,000.00 USD | 0.00 USD | 33,430.00 USD | `-3.93%` | `8,473.20` |
| `Live` | `Long` | `3.96` | 2,780,000.00 USD | 0.00 USD | 599,170.00 USD | `-3.69%` | `151,495.60` |
| `Live` | `Long` | `3.96` | 2,180,000.00 USD | 0.00 USD | 218,010.00 USD | `-3.45%` | `54,984.70` |
| `Live` | `Long` | `3.98` | 1,960,000.00 USD | 0.00 USD | 477,730.00 USD | `-3.20%` | `120,184.20` |
| `Live` | `Long` | `3.98` | 1,490,000.00 USD | 0.00 USD | 151,930.00 USD | `-2.96%` | `38,126.70` |
| `Live` | `Long` | `4.00` | 1,340,000.00 USD | 0.00 USD | 223,790.00 USD | `-2.72%` | `56,016.80` |
| `Live` | `Long` | `4.00` | 1,110,000.00 USD | 0.00 USD | 57,890.00 USD | `-2.47%` | `14,453.30` |
| `Live` | `Long` | `4.01` | 1,050,000.00 USD | 0.00 USD | 73,860.00 USD | `-2.23%` | `18,395.00` |
| `Live` | `Long` | `4.03` | 979,500.00 USD | 0.00 USD | 128,600.00 USD | `-1.98%` | `31,949.30` |
| `Live` | `Long` | `4.04` | 850,910.00 USD | 0.00 USD | 20,250.00 USD | `-1.74%` | `5,017.60` |
| `Live` | `Long` | `4.04` | 830,660.00 USD | 0.00 USD | 120,800.00 USD | `-1.50%` | `29,863.10` |
| `Live` | `Long` | `4.05` | 709,870.00 USD | 0.00 USD | 24,810.00 USD | `-1.25%` | `6,117.50` |
| `Live` | `Long` | `4.07` | 685,060.00 USD | 0.00 USD | 324,890.00 USD | `-1.01%` | `79,924.30` |
| `Live` | `Long` | `4.08` | 360,170.00 USD | 0.00 USD | 90,340.00 USD | `-0.77%` | `22,170.20` |
| `Live` | `Long` | `4.11` | 269,820.00 USD | 0.00 USD | 269,820.00 USD | `-0.04%` | `65,730.50` |
| `Live` | `Short` | `4.20` | 6,930.00 USD | 6,930.00 USD | 0.00 USD | `+2.16%` | `1,652.50` |
| `Live` | `Short` | `4.28` | 16,780.00 USD | 9,850.00 USD | 0.00 USD | `+4.10%` | `2,303.60` |
| `Live` | `Short` | `4.29` | 16,990.00 USD | 207.39 USD | 0.00 USD | `+4.35%` | `48.40` |
| `Live` | `Short` | `4.30` | 19,760.00 USD | 2,770.00 USD | 0.00 USD | `+4.83%` | `643.80` |
| `Live` | `Short` | `4.32` | 22,040.00 USD | 2,280.00 USD | 0.00 USD | `+5.08%` | `527.70` |
| `Live` | `Short` | `4.33` | 32,120.00 USD | 10,090.00 USD | 0.00 USD | `+5.32%` | `2,331.80` |
| `Live` | `Short` | `4.33` | 33,580.00 USD | 1,450.00 USD | 0.00 USD | `+5.56%` | `335.50` |
| `Live` | `Short` | `4.34` | 42,250.00 USD | 8,680.00 USD | 0.00 USD | `+5.81%` | `1,996.60` |
| `Live` | `Short` | `4.36` | 47,790.00 USD | 5,540.00 USD | 0.00 USD | `+6.05%` | `1,272.30` |
| `Live` | `Short` | `4.38` | 54,470.00 USD | 6,680.00 USD | 0.00 USD | `+6.54%` | `1,526.90` |
| `Live` | `Short` | `4.38` | 80,310.00 USD | 25,830.00 USD | 0.00 USD | `+6.78%` | `5,891.40` |
| `Live` | `Short` | `4.39` | 94,360.00 USD | 14,050.00 USD | 0.00 USD | `+7.03%` | `3,197.90` |
| `Live` | `Short` | `4.41` | 95,770.00 USD | 1,410.00 USD | 0.00 USD | `+7.27%` | `319.80` |
| `Live` | `Short` | `4.42` | 149,090.00 USD | 53,320.00 USD | 0.00 USD | `+7.51%` | `12,076.90` |
| `Live` | `Short` | `4.42` | 149,190.00 USD | 104.87 USD | 0.00 USD | `+7.76%` | `23.70` |
| `Live` | `Short` | `4.43` | 174,690.00 USD | 25,500.00 USD | 0.00 USD | `+8.00%` | `5,749.00` |
| `Live` | `Short` | `4.46` | 175,160.00 USD | 468.38 USD | 0.00 USD | `+8.73%` | `104.90` |
| `Live` | `Short` | `4.47` | 176,420.00 USD | 1,260.00 USD | 0.00 USD | `+8.97%` | `281.10` |
| `Live` | `Short` | `4.49` | 191,560.00 USD | 15,150.00 USD | 0.00 USD | `+9.22%` | `3,377.50` |
| `Live` | `Short` | `4.50` | 281,750.00 USD | 90,180.00 USD | 0.00 USD | `+9.46%` | `20,062.40` |
| `Live` | `Short` | `4.50` | 282,010.00 USD | 268.05 USD | 0.00 USD | `+9.70%` | `59.50` |
| `Live` | `Short` | `4.53` | 300,110.00 USD | 18,100.00 USD | 0.00 USD | `+10.19%` | `4,000.00` |
| `Live` | `Short` | `4.54` | 300,370.00 USD | 252.70 USD | 0.00 USD | `+10.68%` | `55.60` |
| `Live` | `Short` | `4.59` | 309,560.00 USD | 9,190.00 USD | 0.00 USD | `+11.90%` | `2,000.00` |
| `Live` | `Short` | `4.61` | 310,600.00 USD | 1,050.00 USD | 0.00 USD | `+12.14%` | `227.10` |
| `Live` | `Short` | `4.62` | 310,810.00 USD | 203.50 USD | 0.00 USD | `+12.63%` | `44.00` |
| `Live` | `Short` | `4.63` | 311,300.00 USD | 493.16 USD | 0.00 USD | `+12.87%` | `106.40` |
| `Live` | `Short` | `4.67` | 435,690.00 USD | 124,390.00 USD | 0.00 USD | `+13.60%` | `26,664.20` |
| `Live` | `Short` | `4.71` | 448,740.00 USD | 13,050.00 USD | 0.00 USD | `+14.57%` | `2,773.80` |
| `Live` | `Short` | `4.71` | 449,200.00 USD | 460.18 USD | 0.00 USD | `+14.82%` | `97.60` |
| `Live` | `Short` | `4.75` | 604,070.00 USD | 154,870.00 USD | 0.00 USD | `+15.79%` | `32,569.80` |
| `Live` | `Short` | `4.76` | 668,330.00 USD | 64,260.00 USD | 0.00 USD | `+16.04%` | `13,485.80` |
| `Live` | `Short` | `4.78` | 675,380.00 USD | 7,050.00 USD | 0.00 USD | `+16.28%` | `1,477.00` |
| `Live` | `Short` | `4.79` | 679,910.00 USD | 4,530.00 USD | 0.00 USD | `+16.52%` | `946.20` |
| `Live` | `Short` | `4.79` | 681,240.00 USD | 1,330.00 USD | 0.00 USD | `+16.77%` | `277.70` |
| `Live` | `Short` | `4.82` | 1,150,000.00 USD | 473,730.00 USD | 0.00 USD | `+17.25%` | `98,386.10` |
| `Live` | `Short` | `4.83` | 1,160,000.00 USD | 1,740.00 USD | 0.00 USD | `+17.50%` | `360.90` |
| `Live` | `Short` | `4.83` | 1,180,000.00 USD | 23,580.00 USD | 0.00 USD | `+17.74%` | `4,877.90` |
| `Live` | `Short` | `4.84` | 1,220,000.00 USD | 41,300.00 USD | 0.00 USD | `+17.98%` | `8,524.20` |
| `Live` | `Short` | `4.87` | 1,230,000.00 USD | 5,460.00 USD | 0.00 USD | `+18.47%` | `1,121.90` |
| `Live` | `Short` | `4.88` | 1,240,000.00 USD | 12,510.00 USD | 0.00 USD | `+18.71%` | `2,565.90` |
| `Live` | `Short` | `4.88` | 1,240,000.00 USD | 827.03 USD | 0.00 USD | `+18.96%` | `169.30` |
| `Live` | `Short` | `4.92` | 1,590,000.00 USD | 346,720.00 USD | 0.00 USD | `+19.69%` | `70,543.50` |
| `Live` | `Short` | `4.92` | 1,590,000.00 USD | 2,100.00 USD | 0.00 USD | `+19.93%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,590,000.00 USD | 556.67 USD | 0.00 USD | `+20.18%` | `112.80` |
| `Live` | `Short` | `4.96` | 1,590,000.00 USD | 342.89 USD | 0.00 USD | `+20.66%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,690,000.00 USD | 99,810.00 USD | 0.00 USD | `+21.15%` | `20,062.00` |
| `Live` | `Short` | `4.99` | 1,700,000.00 USD | 5,090.00 USD | 0.00 USD | `+21.39%` | `1,021.20` |
| `Live` | `Short` | `5.00` | 1,720,000.00 USD | 20,430.00 USD | 0.00 USD | `+21.64%` | `4,090.20` |
| `Live` | `Short` | `5.04` | 1,720,000.00 USD | 926.94 USD | 0.00 USD | `+22.61%` | `184.10` |
| `Live` | `Short` | `5.05` | 1,720,000.00 USD | 5,020.00 USD | 0.00 USD | `+23.10%` | `993.80` |
| `Live` | `Short` | `5.07` | 1,720,000.00 USD | 3,420.00 USD | 0.00 USD | `+23.34%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,730,000.00 USD | 1,090.00 USD | 0.00 USD | `+23.83%` | `214.10` |
| `Live` | `Short` | `5.12` | 1,730,000.00 USD | 1,640.00 USD | 0.00 USD | `+24.56%` | `320.50` |
| `Live` | `Short` | `5.12` | 1,730,000.00 USD | 2,560.00 USD | 0.00 USD | `+24.80%` | `500.00` |
| `Live` | `Short` | `5.13` | 1,730,000.00 USD | 1,080.00 USD | 0.00 USD | `+25.05%` | `210.70` |
| `Live` | `Short` | `5.17` | 1,730,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.78%` | `561.50` |
| `Live` | `Short` | `5.20` | 1,740,000.00 USD | 1,040.00 USD | 0.00 USD | `+26.51%` | `200.00` |
| `Live` | `Short` | `5.21` | 2,630,000.00 USD | 898,120.00 USD | 0.00 USD | `+26.75%` | `172,549.20` |
| `Live` | `Short` | `5.21` | 3,680,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+26.99%` | `200,000.00` |
| `Live` | `Short` | `5.22` | 3,750,000.00 USD | 72,110.00 USD | 0.00 USD | `+27.24%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 3,750,000.00 USD | 1,110.00 USD | 0.00 USD | `+27.72%` | `211.50` |
| `Live` | `Short` | `5.25` | 3,750,000.00 USD | 288.50 USD | 0.00 USD | `+27.97%` | `54.90` |
| `Live` | `Short` | `5.26` | 3,760,000.00 USD | 5,610.00 USD | 0.00 USD | `+28.21%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 3,760,000.00 USD | 853.50 USD | 0.00 USD | `+28.45%` | `161.80` |
| `Live` | `Short` | `5.29` | 3,760,000.00 USD | 257.38 USD | 0.00 USD | `+28.70%` | `48.70` |
| `Live` | `Short` | `5.29` | 3,760,000.00 USD | 114.37 USD | 0.00 USD | `+28.94%` | `21.60` |
| `Live` | `Short` | `5.30` | 3,760,000.00 USD | 524.66 USD | 0.00 USD | `+29.19%` | `98.90` |
| `Live` | `Short` | `5.32` | 3,760,000.00 USD | 718.59 USD | 0.00 USD | `+29.43%` | `135.20` |
| `Live` | `Short` | `5.33` | 3,760,000.00 USD | 1,600.00 USD | 0.00 USD | `+29.92%` | `300.00` |
| `Live` | `Short` | `5.34` | 3,850,000.00 USD | 90,820.00 USD | 0.00 USD | `+30.16%` | `16,992.10` |
| `Live` | `Short` | `5.36` | 3,870,000.00 USD | 23,600.00 USD | 0.00 USD | `+30.40%` | `4,406.20` |
| `Live` | `Short` | `5.39` | 3,890,000.00 USD | 20,300.00 USD | 0.00 USD | `+31.38%` | `3,762.90` |
| `Live` | `Short` | `5.41` | 3,930,000.00 USD | 35,680.00 USD | 0.00 USD | `+31.62%` | `6,601.20` |
| `Live` | `Short` | `5.43` | 3,930,000.00 USD | 962.54 USD | 0.00 USD | `+32.35%` | `177.10` |
| `Live` | `Short` | `5.45` | 3,930,000.00 USD | 1,050.00 USD | 0.00 USD | `+32.59%` | `192.10` |
| `Live` | `Short` | `5.46` | 4,220,000.00 USD | 291,860.00 USD | 0.00 USD | `+32.84%` | `53,503.40` |
| `Live` | `Short` | `5.47` | 4,310,000.00 USD | 88,100.00 USD | 0.00 USD | `+33.33%` | `16,090.90` |
| `Live` | `Short` | `5.49` | 4,370,000.00 USD | 62,250.00 USD | 0.00 USD | `+33.57%` | `11,349.70` |
| `Live` | `Short` | `5.50` | 4,450,000.00 USD | 77,760.00 USD | 0.00 USD | `+33.81%` | `14,151.00` |
| `Live` | `Short` | `5.51` | 4,490,000.00 USD | 40,180.00 USD | 0.00 USD | `+34.30%` | `7,284.90` |
| `Live` | `Short` | `5.54` | 4,490,000.00 USD | 209.22 USD | 0.00 USD | `+34.79%` | `37.80` |
| `Live` | `Short` | `5.54` | 4,490,000.00 USD | 715.30 USD | 0.00 USD | `+35.03%` | `129.00` |
| `Live` | `Short` | `5.57` | 4,500,000.00 USD | 8,670.00 USD | 0.00 USD | `+35.52%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,560,000.00 USD | 62,420.00 USD | 0.00 USD | `+35.76%` | `11,196.20` |
| `Live` | `Short` | `5.58` | 4,630,000.00 USD | 62,420.00 USD | 0.00 USD | `+36.00%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 4,630,000.00 USD | 686.51 USD | 0.00 USD | `+36.25%` | `122.70` |
| `Live` | `Short` | `5.62` | 4,680,000.00 USD | 56,250.00 USD | 0.00 USD | `+36.98%` | `10,000.00` |
| `Live` | `Short` | `5.67` | 4,680,000.00 USD | 211.30 USD | 0.00 USD | `+37.95%` | `37.30` |
| `Live` | `Short` | `5.67` | 4,680,000.00 USD | 334.26 USD | 0.00 USD | `+38.20%` | `58.90` |
| `Live` | `Short` | `5.68` | 4,710,000.00 USD | 26,090.00 USD | 0.00 USD | `+38.44%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 4,710,000.00 USD | 1,520.00 USD | 0.00 USD | `+38.68%` | `267.40` |
| `Live` | `Short` | `5.71` | 4,710,000.00 USD | 2,130.00 USD | 0.00 USD | `+39.17%` | `372.40` |
| `Live` | `Short` | `5.75` | 4,720,000.00 USD | 4,580.00 USD | 0.00 USD | `+39.90%` | `796.90` |
| `Live` | `Short` | `5.75` | 4,760,000.00 USD | 40,990.00 USD | 0.00 USD | `+40.14%` | `7,122.00` |
| `Live` | `Short` | `5.79` | 4,760,000.00 USD | 127.49 USD | 0.00 USD | `+41.12%` | `22.00` |
| `Live` | `Short` | `5.80` | 4,760,000.00 USD | 2,670.00 USD | 0.00 USD | `+41.36%` | `460.20` |
| `Live` | `Short` | `5.84` | 4,820,000.00 USD | 56,160.00 USD | 0.00 USD | `+42.34%` | `9,608.80` |
| `Live` | `Short` | `5.86` | 4,820,000.00 USD | 848.39 USD | 0.00 USD | `+42.58%` | `144.90` |
| `Live` | `Short` | `5.88` | 4,820,000.00 USD | 190.67 USD | 0.00 USD | `+43.31%` | `32.40` |
| `Live` | `Short` | `5.89` | 4,910,000.00 USD | 88,590.00 USD | 0.00 USD | `+43.55%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 4,920,000.00 USD | 7,330.00 USD | 0.00 USD | `+44.04%` | `1,238.80` |
| `Live` | `Short` | `5.95` | 4,920,000.00 USD | 1,400.00 USD | 0.00 USD | `+44.77%` | `234.80` |
| `Live` | `Short` | `6.03` | 4,940,000.00 USD | 23,060.00 USD | 0.00 USD | `+46.72%` | `3,827.40` |
| `Live` | `Short` | `6.07` | 5,220,000.00 USD | 281,130.00 USD | 0.00 USD | `+47.69%` | `46,352.80` |
| `Live` | `Short` | `6.08` | 5,230,000.00 USD | 5,920.00 USD | 0.00 USD | `+48.18%` | `973.10` |
| `Live` | `Short` | `6.09` | 5,260,000.00 USD | 37,510.00 USD | 0.00 USD | `+48.42%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 5,270,000.00 USD | 2,720.00 USD | 0.00 USD | `+48.67%` | `445.60` |
| `Live` | `Short` | `6.12` | 5,270,000.00 USD | 1,260.00 USD | 0.00 USD | `+49.15%` | `205.00` |
| `Live` | `Short` | `6.13` | 5,290,000.00 USD | 24,160.00 USD | 0.00 USD | `+49.40%` | `3,938.70` |
| `Live` | `Short` | `6.24` | 5,290,000.00 USD | 693.33 USD | 0.00 USD | `+51.83%` | `111.20` |
| `Live` | `Short` | `6.25` | 5,300,000.00 USD | 7,300.00 USD | 0.00 USD | `+52.08%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 5,300,000.00 USD | 2,380.00 USD | 0.00 USD | `+52.32%` | `380.20` |
| `Live` | `Short` | `6.28` | 5,300,000.00 USD | 397.84 USD | 0.00 USD | `+52.81%` | `63.40` |
| `Live` | `Short` | `6.32` | 5,300,000.00 USD | 310.70 USD | 0.00 USD | `+53.78%` | `49.20` |
| `Live` | `Short` | `6.33` | 5,300,000.00 USD | 382.00 USD | 0.00 USD | `+54.27%` | `60.30` |
| `Live` | `Short` | `6.34` | 5,300,000.00 USD | 214.46 USD | 0.00 USD | `+54.51%` | `33.80` |
| `Live` | `Short` | `6.37` | 5,350,000.00 USD | 45,180.00 USD | 0.00 USD | `+55.00%` | `7,097.50` |
| `Live` | `Short` | `6.38` | 5,350,000.00 USD | 288.15 USD | 0.00 USD | `+55.24%` | `45.20` |
| `Live` | `Short` | `6.38` | 5,350,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.49%` | `312.80` |
| `Live` | `Short` | `6.41` | 5,360,000.00 USD | 3,780.00 USD | 0.00 USD | `+55.97%` | `590.10` |
| `Live` | `Short` | `6.42` | 5,360,000.00 USD | 8,700.00 USD | 0.00 USD | `+56.22%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 5,360,000.00 USD | 346.95 USD | 0.00 USD | `+56.46%` | `54.00` |
| `Live` | `Short` | `6.43` | 5,410,000.00 USD | 42,740.00 USD | 0.00 USD | `+56.70%` | `6,641.70` |
| `Live` | `Short` | `6.45` | 5,790,000.00 USD | 378,690.00 USD | 0.00 USD | `+56.95%` | `58,756.80` |
| `Live` | `Short` | `6.46` | 5,790,000.00 USD | 7,150.00 USD | 0.00 USD | `+57.19%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 5,790,000.00 USD | 1,940.00 USD | 0.00 USD | `+57.43%` | `300.00` |
| `Live` | `Short` | `6.51` | 5,800,000.00 USD | 380.48 USD | 0.00 USD | `+58.65%` | `58.40` |
| `Live` | `Short` | `6.54` | 5,810,000.00 USD | 18,080.00 USD | 0.00 USD | `+59.14%` | `2,767.30` |
| `Live` | `Short` | `6.54` | 5,810,000.00 USD | 265.07 USD | 0.00 USD | `+59.38%` | `40.50` |
| `Live` | `Short` | `6.55` | 5,860,000.00 USD | 51,310.00 USD | 0.00 USD | `+59.62%` | `7,827.40` |
| `Live` | `Short` | `6.57` | 5,870,000.00 USD | 454.95 USD | 0.00 USD | `+59.87%` | `69.30` |
| `Live` | `Short` | `6.58` | 5,970,000.00 USD | 103,110.00 USD | 0.00 USD | `+60.11%` | `15,681.60` |
| `Live` | `Short` | `6.59` | 5,970,000.00 USD | 418.78 USD | 0.00 USD | `+60.60%` | `63.50` |
| `Live` | `Short` | `6.64` | 5,970,000.00 USD | 6,080.00 USD | 0.00 USD | `+61.82%` | `914.50` |
| `Live` | `Short` | `6.66` | 5,980,000.00 USD | 7,230.00 USD | 0.00 USD | `+62.06%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 7,960,000.00 USD | 1,980,000.00 USD | 0.00 USD | `+62.30%` | `296,453.00` |
| `Live` | `Short` | `6.67` | 7,960,000.00 USD | 200.25 USD | 0.00 USD | `+62.55%` | `30.00` |
| `Live` | `Short` | `6.72` | 8,070,000.00 USD | 115,670.00 USD | 0.00 USD | `+63.76%` | `17,200.00` |
| `Live` | `Short` | `6.75` | 8,080,000.00 USD | 3,380.00 USD | 0.00 USD | `+64.50%` | `501.00` |
| `Live` | `Short` | `6.76` | 9,320,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+64.74%` | `184,000.00` |
| `Live` | `Short` | `6.79` | 9,360,000.00 USD | 36,120.00 USD | 0.00 USD | `+65.23%` | `5,323.40` |
| `Live` | `Short` | `6.84` | 9,360,000.00 USD | 753.63 USD | 0.00 USD | `+66.69%` | `110.10` |
| `Live` | `Short` | `6.86` | 9,360,000.00 USD | 649.17 USD | 0.00 USD | `+66.93%` | `94.70` |
| `Live` | `Short` | `6.87` | 9,410,000.00 USD | 46,020.00 USD | 0.00 USD | `+67.17%` | `6,703.00` |
| `Live` | `Short` | `6.88` | 9,410,000.00 USD | 164.55 USD | 0.00 USD | `+67.66%` | `23.90` |
| `Live` | `Short` | `6.92` | 9,410,000.00 USD | 7,660.00 USD | 0.00 USD | `+68.64%` | `1,106.10` |
| `Live` | `Short` | `6.96` | 9,410,000.00 USD | 191.26 USD | 0.00 USD | `+69.37%` | `27.50` |
| `Live` | `Short` | `6.99` | 9,410,000.00 USD | 664.27 USD | 0.00 USD | `+70.10%` | `95.10` |
| `Live` | `Short` | `7.07` | 9,410,000.00 USD | 192.87 USD | 0.00 USD | `+72.04%` | `27.30` |
| `Live` | `Short` | `7.09` | 9,420,000.00 USD | 699.57 USD | 0.00 USD | `+72.77%` | `98.60` |
| `Live` | `Short` | `7.12` | 9,420,000.00 USD | 9,850.00 USD | 0.00 USD | `+73.26%` | `1,384.00` |
| `Live` | `Short` | `7.16` | 9,430,000.00 USD | 1,790.00 USD | 0.00 USD | `+74.24%` | `250.00` |
| `Live` | `Short` | `7.20` | 9,430,000.00 USD | 5,720.00 USD | 0.00 USD | `+75.21%` | `794.40` |
| `Live` | `Short` | `7.21` | 9,450,000.00 USD | 13,560.00 USD | 0.00 USD | `+75.70%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 9,510,000.00 USD | 68,550.00 USD | 0.00 USD | `+76.18%` | `9,475.40` |
| `Live` | `Short` | `7.28` | 9,520,000.00 USD | 576.91 USD | 0.00 USD | `+77.16%` | `79.30` |
| `Live` | `Short` | `7.33` | 9,520,000.00 USD | 1,320.00 USD | 0.00 USD | `+78.62%` | `180.00` |
| `Live` | `Short` | `7.38` | 9,520,000.00 USD | 1,630.00 USD | 0.00 USD | `+79.59%` | `220.40` |
| `Live` | `Short` | `7.41` | 9,610,000.00 USD | 88,860.00 USD | 0.00 USD | `+80.32%` | `12,000.00` |
| `Live` | `Short` | `7.46` | 9,710,000.00 USD | 107,860.00 USD | 0.00 USD | `+81.54%` | `14,467.60` |
| `Live` | `Short` | `7.49` | 9,720,000.00 USD | 1,160.00 USD | 0.00 USD | `+82.27%` | `154.80` |
| `Live` | `Short` | `7.50` | 17,510,000.00 USD | 7,790,000.00 USD | 0.00 USD | `+82.52%` | `1,039,604.60` |
| `Live` | `Short` | `7.50` | 17,520,000.00 USD | 16,790.00 USD | 0.00 USD | `+82.76%` | `2,237.40` |
| `Live` | `Short` | `7.53` | 17,530,000.00 USD | 4,220.00 USD | 0.00 USD | `+83.25%` | `561.20` |
| `Live` | `Short` | `7.55` | 27,620,000.00 USD | 10,090,000.00 USD | 0.00 USD | `+83.98%` | `1,336,000.00` |
| `Live` | `Short` | `7.58` | 27,620,000.00 USD | 794.91 USD | 0.00 USD | `+84.71%` | `104.80` |
| `Live` | `Short` | `7.63` | 27,640,000.00 USD | 19,210.00 USD | 0.00 USD | `+85.92%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 27,670,000.00 USD | 26,770.00 USD | 0.00 USD | `+86.41%` | `3,496.50` |
| `Live` | `Short` | `7.67` | 28,250,000.00 USD | 576,600.00 USD | 0.00 USD | `+86.66%` | `75,224.80` |
| `Live` | `Short` | `7.67` | 29,690,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+86.90%` | `188,000.00` |
| `Live` | `Short` | `7.68` | 29,690,000.00 USD | 160.62 USD | 0.00 USD | `+87.14%` | `20.90` |
| `Live` | `Short` | `7.72` | 29,690,000.00 USD | 495.94 USD | 0.00 USD | `+88.12%` | `64.20` |
| `Live` | `Short` | `7.75` | 29,690,000.00 USD | 629.67 USD | 0.00 USD | `+88.60%` | `81.30` |
| `Live` | `Short` | `7.76` | 29,730,000.00 USD | 38,700.00 USD | 0.00 USD | `+89.09%` | `4,983.50` |
| `Live` | `Short` | `7.80` | 29,730,000.00 USD | 2,840.00 USD | 0.00 USD | `+90.06%` | `364.40` |
| `Live` | `Short` | `7.87` | 30,070,000.00 USD | 334,500.00 USD | 0.00 USD | `+91.53%` | `42,529.90` |
| `Live` | `Short` | `7.88` | 30,090,000.00 USD | 28,790.00 USD | 0.00 USD | `+92.01%` | `3,650.70` |
| `Live` | `Short` | `7.92` | 30,110,000.00 USD | 13,850.00 USD | 0.00 USD | `+92.74%` | `1,750.00` |
| `Live` | `Short` | `7.92` | 30,110,000.00 USD | 1,800.00 USD | 0.00 USD | `+92.99%` | `226.70` |
| `Live` | `Short` | `7.95` | 30,120,000.00 USD | 6,120.00 USD | 0.00 USD | `+93.47%` | `769.80` |
| `Live` | `Short` | `7.96` | 30,250,000.00 USD | 134,240.00 USD | 0.00 USD | `+93.96%` | `16,854.30` |
| `Live` | `Short` | `7.99` | 30,250,000.00 USD | 399.25 USD | 0.00 USD | `+94.45%` | `50.00` |
| `Live` | `Short` | `8.03` | 30,690,000.00 USD | 435,420.00 USD | 0.00 USD | `+95.42%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 30,690,000.00 USD | 797.63 USD | 0.00 USD | `+96.40%` | `98.90` |
| `Live` | `Short` | `8.12` | 30,690,000.00 USD | 2,690.00 USD | 0.00 USD | `+97.86%` | `330.50` |
| `Live` | `Short` | `8.15` | 30,690,000.00 USD | 190.01 USD | 0.00 USD | `+98.59%` | `23.30` |
| `Live` | `Short` | `8.21` | 30,940,000.00 USD | 248,640.00 USD | 0.00 USD | `+100.05%` | `30,266.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.8250` | 3,400,000.00 USD | 0.00 USD | 209.80 USD | `-79.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 3,400,000.00 USD | 0.00 USD | 585.51 USD | `-75.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,400,000.00 USD | 0.00 USD | 331.54 USD | `-67.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,400,000.00 USD | 0.00 USD | 345.25 USD | `-67.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,400,000.00 USD | 0.00 USD | 5,640.00 USD | `-66.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,390,000.00 USD | 0.00 USD | 997.29 USD | `-66.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,390,000.00 USD | 0.00 USD | 139.83 USD | `-63.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,390,000.00 USD | 0.00 USD | 113.28 USD | `-62.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,390,000.00 USD | 0.00 USD | 4,000.00 USD | `-62.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,390,000.00 USD | 0.00 USD | 324.22 USD | `-62.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,390,000.00 USD | 0.00 USD | 4,590.00 USD | `-61.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,380,000.00 USD | 0.00 USD | 739.67 USD | `-60.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,380,000.00 USD | 0.00 USD | 1,740.00 USD | `-60.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,380,000.00 USD | 0.00 USD | 6,260.00 USD | `-60.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,370,000.00 USD | 0.00 USD | 167.50 USD | `-59.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,370,000.00 USD | 0.00 USD | 669.02 USD | `-58.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,370,000.00 USD | 0.00 USD | 105.88 USD | `-58.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,370,000.00 USD | 0.00 USD | 172.50 USD | `-57.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,370,000.00 USD | 0.00 USD | 10,650.00 USD | `-56.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,360,000.00 USD | 0.00 USD | 722.00 USD | `-56.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,360,000.00 USD | 0.00 USD | 259.00 USD | `-55.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,360,000.00 USD | 0.00 USD | 103.84 USD | `-55.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,360,000.00 USD | 0.00 USD | 109.00 USD | `-55.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,360,000.00 USD | 0.00 USD | 222.19 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,360,000.00 USD | 0.00 USD | 10,280.00 USD | `-54.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,350,000.00 USD | 0.00 USD | 558.36 USD | `-53.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,350,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,350,000.00 USD | 0.00 USD | 222.14 USD | `-52.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,350,000.00 USD | 0.00 USD | 279.50 USD | `-52.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,350,000.00 USD | 0.00 USD | 197.50 USD | `-51.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,350,000.00 USD | 0.00 USD | 935.66 USD | `-51.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,350,000.00 USD | 0.00 USD | 19,180.00 USD | `-51.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,330,000.00 USD | 0.00 USD | 3,020.00 USD | `-50.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,330,000.00 USD | 0.00 USD | 214.52 USD | `-50.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,320,000.00 USD | 0.00 USD | 1,200.00 USD | `-49.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,320,000.00 USD | 0.00 USD | 578.41 USD | `-49.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,320,000.00 USD | 0.00 USD | 18,070.00 USD | `-48.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,310,000.00 USD | 0.00 USD | 13,980.00 USD | `-48.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,290,000.00 USD | 0.00 USD | 107.23 USD | `-48.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,290,000.00 USD | 0.00 USD | 1,590.00 USD | `-48.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,290,000.00 USD | 0.00 USD | 6,970.00 USD | `-47.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,280,000.00 USD | 0.00 USD | 310.32 USD | `-47.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,280,000.00 USD | 0.00 USD | 1,170.00 USD | `-47.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,280,000.00 USD | 0.00 USD | 576.18 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,280,000.00 USD | 0.00 USD | 295.67 USD | `-46.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,280,000.00 USD | 0.00 USD | 2,940.00 USD | `-46.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,280,000.00 USD | 0.00 USD | 812.68 USD | `-46.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,280,000.00 USD | 0.00 USD | 1,440.00 USD | `-45.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,270,000.00 USD | 0.00 USD | 106.16 USD | `-45.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,270,000.00 USD | 0.00 USD | 6,270.00 USD | `-45.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,270,000.00 USD | 0.00 USD | 478.06 USD | `-45.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,270,000.00 USD | 0.00 USD | 540.88 USD | `-44.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,270,000.00 USD | 0.00 USD | 1,210.00 USD | `-44.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,270,000.00 USD | 0.00 USD | 759.76 USD | `-44.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,270,000.00 USD | 0.00 USD | 11,060.00 USD | `-44.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,250,000.00 USD | 0.00 USD | 3,690.00 USD | `-43.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,250,000.00 USD | 0.00 USD | 3,050.00 USD | `-43.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,250,000.00 USD | 0.00 USD | 467.00 USD | `-43.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,250,000.00 USD | 0.00 USD | 506.75 USD | `-42.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,250,000.00 USD | 0.00 USD | 214.27 USD | `-42.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,250,000.00 USD | 0.00 USD | 428.69 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,250,000.00 USD | 0.00 USD | 322.45 USD | `-41.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,250,000.00 USD | 0.00 USD | 108.25 USD | `-41.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,250,000.00 USD | 0.00 USD | 3,900.00 USD | `-41.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,240,000.00 USD | 0.00 USD | 799.04 USD | `-40.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,240,000.00 USD | 0.00 USD | 6,830.00 USD | `-40.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,230,000.00 USD | 0.00 USD | 137.16 USD | `-40.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,230,000.00 USD | 0.00 USD | 504.41 USD | `-39.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,230,000.00 USD | 0.00 USD | 963.93 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,230,000.00 USD | 0.00 USD | 3,690.00 USD | `-39.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,230,000.00 USD | 0.00 USD | 541.98 USD | `-38.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,230,000.00 USD | 0.00 USD | 108.75 USD | `-38.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,230,000.00 USD | 0.00 USD | 766.55 USD | `-38.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,230,000.00 USD | 0.00 USD | 1,010.00 USD | `-37.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,230,000.00 USD | 0.00 USD | 1,100.00 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,230,000.00 USD | 0.00 USD | 100.04 USD | `-37.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 3,230,000.00 USD | 0.00 USD | 31,240.00 USD | `-36.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 3,190,000.00 USD | 0.00 USD | 5,090.00 USD | `-36.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 3,190,000.00 USD | 0.00 USD | 226.57 USD | `-34.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,190,000.00 USD | 0.00 USD | 104.98 USD | `-34.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 3,190,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 3,180,000.00 USD | 0.00 USD | 107.21 USD | `-33.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,180,000.00 USD | 0.00 USD | 197.37 USD | `-33.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,180,000.00 USD | 0.00 USD | 8,390.00 USD | `-32.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,170,000.00 USD | 0.00 USD | 108.39 USD | `-32.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,170,000.00 USD | 0.00 USD | 435.95 USD | `-32.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,170,000.00 USD | 0.00 USD | 217.23 USD | `-32.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,170,000.00 USD | 0.00 USD | 437.98 USD | `-31.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 3,170,000.00 USD | 0.00 USD | 2,000.00 USD | `-31.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,170,000.00 USD | 0.00 USD | 8,250.00 USD | `-31.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,160,000.00 USD | 0.00 USD | 109.53 USD | `-30.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,160,000.00 USD | 0.00 USD | 437.00 USD | `-29.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,160,000.00 USD | 0.00 USD | 746.06 USD | `-29.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,160,000.00 USD | 0.00 USD | 2,900.00 USD | `-29.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,160,000.00 USD | 0.00 USD | 4,870.00 USD | `-29.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,150,000.00 USD | 0.00 USD | 696.98 USD | `-29.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,150,000.00 USD | 0.00 USD | 358.90 USD | `-28.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,150,000.00 USD | 0.00 USD | 15,370.00 USD | `-28.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,140,000.00 USD | 0.00 USD | 523.32 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 3,140,000.00 USD | 0.00 USD | 2,330.00 USD | `-27.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 3,130,000.00 USD | 0.00 USD | 13,770.00 USD | `-26.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,120,000.00 USD | 0.00 USD | 1,020.00 USD | `-26.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,120,000.00 USD | 0.00 USD | 345.76 USD | `-26.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,120,000.00 USD | 0.00 USD | 214.57 USD | `-26.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,120,000.00 USD | 0.00 USD | 109.42 USD | `-25.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 3,120,000.00 USD | 0.00 USD | 721.58 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 3,120,000.00 USD | 0.00 USD | 9,300.00 USD | `-24.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,110,000.00 USD | 0.00 USD | 8,530.00 USD | `-24.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,100,000.00 USD | 0.00 USD | 104.69 USD | `-23.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 3,100,000.00 USD | 0.00 USD | 315.69 USD | `-23.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,100,000.00 USD | 0.00 USD | 214.17 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,100,000.00 USD | 0.00 USD | 641.10 USD | `-23.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,100,000.00 USD | 0.00 USD | 212.06 USD | `-22.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,100,000.00 USD | 0.00 USD | 1,030.00 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 3,100,000.00 USD | 0.00 USD | 218.81 USD | `-22.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,100,000.00 USD | 0.00 USD | 25,410.00 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,070,000.00 USD | 0.00 USD | 144.67 USD | `-21.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 3,070,000.00 USD | 0.00 USD | 27,380.00 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 3,040,000.00 USD | 0.00 USD | 2,210.00 USD | `-20.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 3,040,000.00 USD | 0.00 USD | 104.81 USD | `-20.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 3,040,000.00 USD | 0.00 USD | 1,150.00 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 3,040,000.00 USD | 0.00 USD | 1,870.00 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 3,040,000.00 USD | 0.00 USD | 20,120.00 USD | `-19.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 3,020,000.00 USD | 0.00 USD | 240.67 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 3,020,000.00 USD | 0.00 USD | 465.50 USD | `-19.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 3,020,000.00 USD | 0.00 USD | 6,590.00 USD | `-18.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 3,010,000.00 USD | 0.00 USD | 505.76 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 3,010,000.00 USD | 0.00 USD | 73,220.00 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,940,000.00 USD | 0.00 USD | 12,850.00 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,920,000.00 USD | 0.00 USD | 8,490.00 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,920,000.00 USD | 0.00 USD | 12,580.00 USD | `-17.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,900,000.00 USD | 0.00 USD | 109.62 USD | `-16.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,900,000.00 USD | 0.00 USD | 506.22 USD | `-16.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,900,000.00 USD | 0.00 USD | 171.75 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,900,000.00 USD | 0.00 USD | 2,550.00 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,900,000.00 USD | 0.00 USD | 2,100.00 USD | `-15.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,900,000.00 USD | 0.00 USD | 1,300.00 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,900,000.00 USD | 0.00 USD | 1,950.00 USD | `-14.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,890,000.00 USD | 0.00 USD | 101,000.00 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,790,000.00 USD | 0.00 USD | 10,750.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,780,000.00 USD | 0.00 USD | 2,150.00 USD | `-13.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,780,000.00 USD | 0.00 USD | 5,000.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,780,000.00 USD | 0.00 USD | 173.48 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,780,000.00 USD | 0.00 USD | 333.68 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,770,000.00 USD | 0.00 USD | 72,860.00 USD | `-12.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,700,000.00 USD | 0.00 USD | 1,250.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,700,000.00 USD | 0.00 USD | 643.50 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,700,000.00 USD | 0.00 USD | 3,370.00 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,700,000.00 USD | 0.00 USD | 632.99 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,700,000.00 USD | 0.00 USD | 172.19 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,700,000.00 USD | 0.00 USD | 14,620.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,680,000.00 USD | 0.00 USD | 179.33 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,680,000.00 USD | 0.00 USD | 4,080.00 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,680,000.00 USD | 0.00 USD | 174.09 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,680,000.00 USD | 0.00 USD | 367.50 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,680,000.00 USD | 0.00 USD | 4,490.00 USD | `-10.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,670,000.00 USD | 0.00 USD | 4,370.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,670,000.00 USD | 0.00 USD | 32,560.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,640,000.00 USD | 0.00 USD | 6,110.00 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,630,000.00 USD | 0.00 USD | 1,470.00 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,630,000.00 USD | 0.00 USD | 46,570.00 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,580,000.00 USD | 0.00 USD | 28,820.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,550,000.00 USD | 0.00 USD | 20,990.00 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 2,530,000.00 USD | 0.00 USD | 7,120.00 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 2,520,000.00 USD | 0.00 USD | 3,940.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 2,520,000.00 USD | 0.00 USD | 359.57 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 2,520,000.00 USD | 0.00 USD | 1,900.00 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 2,520,000.00 USD | 0.00 USD | 18,550.00 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 2,500,000.00 USD | 0.00 USD | 18,470.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 2,480,000.00 USD | 0.00 USD | 1,560.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 2,480,000.00 USD | 0.00 USD | 2,990.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 2,480,000.00 USD | 0.00 USD | 11,670.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 2,460,000.00 USD | 0.00 USD | 4,360.00 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 2,460,000.00 USD | 0.00 USD | 2,460.00 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 2,460,000.00 USD | 0.00 USD | 38,820.00 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 2,420,000.00 USD | 0.00 USD | 6,600.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 2,410,000.00 USD | 0.00 USD | 1,310.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 2,410,000.00 USD | 0.00 USD | 33,410.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 2,380,000.00 USD | 0.00 USD | 2,940.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 2,370,000.00 USD | 0.00 USD | 64,530.00 USD | `-4.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 2,310,000.00 USD | 0.00 USD | 72,390.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 2,240,000.00 USD | 0.00 USD | 6,710.00 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 2,230,000.00 USD | 0.00 USD | 40,840.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 2,190,000.00 USD | 0.00 USD | 6,490.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,180,000.00 USD | 0.00 USD | 4,930.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,180,000.00 USD | 0.00 USD | 111,030.00 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,070,000.00 USD | 0.00 USD | 16,020.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,050,000.00 USD | 0.00 USD | 895,950.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 1,160,000.00 USD | 0.00 USD | 20,080.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 1,140,000.00 USD | 0.00 USD | 4,530.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 1,130,000.00 USD | 0.00 USD | 5,080.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 1,130,000.00 USD | 0.00 USD | 46,600.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 1,080,000.00 USD | 0.00 USD | 32,310.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 1,050,000.00 USD | 0.00 USD | 14,790.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,030,000.00 USD | 0.00 USD | 17,270.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,020,000.00 USD | 0.00 USD | 164,220.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 850,880.00 USD | 0.00 USD | 131,300.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 719,590.00 USD | 0.00 USD | 719,590.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 56,080.00 USD | 56,080.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 67,940.00 USD | 11,860.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.13` | 69,260.00 USD | 1,320.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.14` | 80,310.00 USD | 11,050.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.16` | 82,510.00 USD | 2,200.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 96,760.00 USD | 14,250.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 97,260.00 USD | 503.92 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 104,870.00 USD | 7,610.00 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 477,690.00 USD | 372,820.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 502,390.00 USD | 24,710.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 506,730.00 USD | 4,340.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 510,880.00 USD | 4,140.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 511,840.00 USD | 966.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 513,610.00 USD | 1,770.00 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 539,120.00 USD | 25,510.00 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 540,910.00 USD | 1,780.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 574,640.00 USD | 33,740.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 661,780.00 USD | 87,140.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 665,040.00 USD | 3,270.00 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 681,480.00 USD | 16,440.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 698,040.00 USD | 16,560.00 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 700,790.00 USD | 2,750.00 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 702,520.00 USD | 1,730.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 720,890.00 USD | 18,370.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 736,500.00 USD | 15,610.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 767,610.00 USD | 31,110.00 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 792,960.00 USD | 25,350.00 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 795,020.00 USD | 2,070.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 795,700.00 USD | 679.03 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 857,910.00 USD | 62,210.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 869,610.00 USD | 11,710.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 873,310.00 USD | 3,700.00 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 873,620.00 USD | 301.58 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 874,500.00 USD | 889.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 936,970.00 USD | 62,460.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 939,330.00 USD | 2,360.00 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 943,410.00 USD | 4,080.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,010,000.00 USD | 62,510.00 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,020,000.00 USD | 10,400.00 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,030,000.00 USD | 10,470.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,040,000.00 USD | 13,100.00 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,090,000.00 USD | 50,660.00 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,220,000.00 USD | 124,750.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,220,000.00 USD | 1,190.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,220,000.00 USD | 1,190.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,220,000.00 USD | 702.55 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,260,000.00 USD | 45,750.00 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,270,000.00 USD | 1,420.00 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,280,000.00 USD | 17,590.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,290,000.00 USD | 2,950.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,290,000.00 USD | 289.82 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,290,000.00 USD | 3,670.00 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,290,000.00 USD | 1,100.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,300,000.00 USD | 13,310.00 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,330,000.00 USD | 24,250.00 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,340,000.00 USD | 12,300.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,340,000.00 USD | 104.25 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,360,000.00 USD | 15,710.00 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,360,000.00 USD | 152.12 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,720,000.00 USD | 358,600.00 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,930,000.00 USD | 217,980.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,940,000.00 USD | 2,650.00 USD | 0.00 USD | `+15.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,020,000.00 USD | 84,180.00 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,030,000.00 USD | 6,160.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,050,000.00 USD | 27,130.00 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,140,000.00 USD | 87,650.00 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,140,000.00 USD | 2,640.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,980,000.00 USD | 837,120.00 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,980,000.00 USD | 559.58 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,160,000.00 USD | 175,060.00 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,180,000.00 USD | 20,970.00 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,190,000.00 USD | 13,730.00 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,190,000.00 USD | 283.33 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,200,000.00 USD | 11,760.00 USD | 0.00 USD | `+17.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,260,000.00 USD | 55,670.00 USD | 0.00 USD | `+18.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,280,000.00 USD | 22,380.00 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,290,000.00 USD | 10,610.00 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,310,000.00 USD | 19,620.00 USD | 0.00 USD | `+18.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,320,000.00 USD | 4,060.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,440,000.00 USD | 119,930.00 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,440,000.00 USD | 287.53 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,450,000.00 USD | 13,180.00 USD | 0.00 USD | `+19.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,460,000.00 USD | 8,600.00 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,460,000.00 USD | 313.51 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,460,000.00 USD | 5,070.00 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,510,000.00 USD | 47,350.00 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,510,000.00 USD | 187.06 USD | 0.00 USD | `+21.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,610,000.00 USD | 95,210.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,610,000.00 USD | 2,540.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,650,000.00 USD | 37,680.00 USD | 0.00 USD | `+21.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,670,000.00 USD | 25,080.00 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,680,000.00 USD | 5,030.00 USD | 0.00 USD | `+22.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,850,000.00 USD | 169,480.00 USD | 0.00 USD | `+22.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,850,000.00 USD | 104.94 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,900,000.00 USD | 53,680.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,900,000.00 USD | 4,730.00 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,990,000.00 USD | 88,030.00 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,880,000.00 USD | 882,870.00 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,880,000.00 USD | 547.20 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,930,000.00 USD | 52,730.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,940,000.00 USD | 12,790.00 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,940,000.00 USD | 113.26 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,940,000.00 USD | 179.72 USD | 0.00 USD | `+25.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,950,000.00 USD | 3,670.00 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,950,000.00 USD | 2,220.00 USD | 0.00 USD | `+25.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,950,000.00 USD | 575.38 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,950,000.00 USD | 327.58 USD | 0.00 USD | `+26.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,950,000.00 USD | 163.85 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 5,070,000.00 USD | 120,080.00 USD | 0.00 USD | `+26.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 5,100,000.00 USD | 33,260.00 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 5,100,000.00 USD | 1,710.00 USD | 0.00 USD | `+26.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 5,230,000.00 USD | 125,620.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 5,230,000.00 USD | 2,620.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,230,000.00 USD | 537.61 USD | 0.00 USD | `+27.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,660,000.00 USD | 425,700.00 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 5,660,000.00 USD | 5,540.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 5,660,000.00 USD | 589.22 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,660,000.00 USD | 733.03 USD | 0.00 USD | `+28.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,670,000.00 USD | 423.60 USD | 0.00 USD | `+28.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,680,000.00 USD | 10,930.00 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,680,000.00 USD | 381.09 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,680,000.00 USD | 961.16 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,680,000.00 USD | 1,570.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,690,000.00 USD | 6,220.00 USD | 0.00 USD | `+30.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,690,000.00 USD | 759.87 USD | 0.00 USD | `+30.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,690,000.00 USD | 225.33 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,690,000.00 USD | 438.60 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,730,000.00 USD | 47,710.00 USD | 0.00 USD | `+31.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,780,000.00 USD | 41,030.00 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,890,000.00 USD | 110,690.00 USD | 0.00 USD | `+31.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,890,000.00 USD | 270.75 USD | 0.00 USD | `+31.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,890,000.00 USD | 935.27 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,900,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,910,000.00 USD | 12,750.00 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,130,000.00 USD | 219,200.00 USD | 0.00 USD | `+33.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 6,170,000.00 USD | 35,450.00 USD | 0.00 USD | `+33.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 6,210,000.00 USD | 44,780.00 USD | 0.00 USD | `+33.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,210,000.00 USD | 1,180.00 USD | 0.00 USD | `+33.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,300,000.00 USD | 82,530.00 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,300,000.00 USD | 5,600.00 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,350,000.00 USD | 45,680.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,370,000.00 USD | 18,790.00 USD | 0.00 USD | `+34.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,440,000.00 USD | 74,260.00 USD | 0.00 USD | `+35.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,490,000.00 USD | 46,110.00 USD | 0.00 USD | `+35.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,500,000.00 USD | 14,320.00 USD | 0.00 USD | `+35.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,510,000.00 USD | 5,560.00 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,530,000.00 USD | 20,540.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,530,000.00 USD | 384.94 USD | 0.00 USD | `+36.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,530,000.00 USD | 573.39 USD | 0.00 USD | `+36.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,530,000.00 USD | 2,190.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,530,000.00 USD | 581.53 USD | 0.00 USD | `+37.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,530,000.00 USD | 491.11 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,530,000.00 USD | 3,290.00 USD | 0.00 USD | `+37.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,530,000.00 USD | 281.55 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,540,000.00 USD | 6,590.00 USD | 0.00 USD | `+38.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,550,000.00 USD | 5,860.00 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,660,000.00 USD | 116,610.00 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,670,000.00 USD | 2,210.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,670,000.00 USD | 5,720.00 USD | 0.00 USD | `+39.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,700,000.00 USD | 24,820.00 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,700,000.00 USD | 2,430.00 USD | 0.00 USD | `+40.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,700,000.00 USD | 1,850.00 USD | 0.00 USD | `+40.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,700,000.00 USD | 286.94 USD | 0.00 USD | `+40.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,710,000.00 USD | 7,120.00 USD | 0.00 USD | `+41.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,710,000.00 USD | 687.91 USD | 0.00 USD | `+41.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,710,000.00 USD | 1,970.00 USD | 0.00 USD | `+41.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+42.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,710,000.00 USD | 1,150.00 USD | 0.00 USD | `+42.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,710,000.00 USD | 1,190.00 USD | 0.00 USD | `+42.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,720,000.00 USD | 1,770.00 USD | 0.00 USD | `+42.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,720,000.00 USD | 3,450.00 USD | 0.00 USD | `+43.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,720,000.00 USD | 345.45 USD | 0.00 USD | `+43.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,780,000.00 USD | 58,220.00 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,780,000.00 USD | 1,670.00 USD | 0.00 USD | `+44.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,780,000.00 USD | 1,400.00 USD | 0.00 USD | `+44.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,930,000.00 USD | 144,250.00 USD | 0.00 USD | `+44.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,950,000.00 USD | 26,180.00 USD | 0.00 USD | `+45.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,960,000.00 USD | 5,440.00 USD | 0.00 USD | `+45.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,970,000.00 USD | 8,940.00 USD | 0.00 USD | `+45.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,090,000.00 USD | 119,340.00 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,090,000.00 USD | 3,000.00 USD | 0.00 USD | `+45.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,290,000.00 USD | 200,350.00 USD | 0.00 USD | `+46.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,300,000.00 USD | 13,610.00 USD | 0.00 USD | `+46.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,390,000.00 USD | 90,380.00 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,390,000.00 USD | 2,140.00 USD | 0.00 USD | `+46.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,400,000.00 USD | 3,300.00 USD | 0.00 USD | `+47.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,400,000.00 USD | 2,550.00 USD | 0.00 USD | `+47.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,400,000.00 USD | 425.76 USD | 0.00 USD | `+47.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,400,000.00 USD | 2,030.00 USD | 0.00 USD | `+47.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,410,000.00 USD | 4,120.00 USD | 0.00 USD | `+48.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,410,000.00 USD | 2,000.00 USD | 0.00 USD | `+48.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,470,000.00 USD | 61,050.00 USD | 0.00 USD | `+48.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,470,000.00 USD | 1,610.00 USD | 0.00 USD | `+48.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,470,000.00 USD | 1,200.00 USD | 0.00 USD | `+49.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,480,000.00 USD | 11,620.00 USD | 0.00 USD | `+49.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,490,000.00 USD | 1,940.00 USD | 0.00 USD | `+49.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,490,000.00 USD | 1,410.00 USD | 0.00 USD | `+50.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,490,000.00 USD | 4,010.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,500,000.00 USD | 3,960.00 USD | 0.00 USD | `+50.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,500,000.00 USD | 3,830.00 USD | 0.00 USD | `+50.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,570,000.00 USD | 66,120.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,570,000.00 USD | 1,890.00 USD | 0.00 USD | `+51.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,570,000.00 USD | 195.46 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,570,000.00 USD | 1,540.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,570,000.00 USD | 3,670.00 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,580,000.00 USD | 3,680.00 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,580,000.00 USD | 7,370.00 USD | 0.00 USD | `+53.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,580,000.00 USD | 310.70 USD | 0.00 USD | `+53.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,580,000.00 USD | 602.77 USD | 0.00 USD | `+54.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,590,000.00 USD | 449.79 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,590,000.00 USD | 1,760.00 USD | 0.00 USD | `+54.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,590,000.00 USD | 3,560.00 USD | 0.00 USD | `+55.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,590,000.00 USD | 3,230.00 USD | 0.00 USD | `+55.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,600,000.00 USD | 5,120.00 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,600,000.00 USD | 613.26 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,600,000.00 USD | 1,310.00 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,630,000.00 USD | 27,360.00 USD | 0.00 USD | `+58.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,630,000.00 USD | 234.54 USD | 0.00 USD | `+58.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,640,000.00 USD | 14,070.00 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,640,000.00 USD | 1,630.00 USD | 0.00 USD | `+60.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 7,650,000.00 USD | 1,370.00 USD | 0.00 USD | `+60.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,650,000.00 USD | 562.09 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,650,000.00 USD | 1,620.00 USD | 0.00 USD | `+61.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,650,000.00 USD | 3,220.00 USD | 0.00 USD | `+61.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,650,000.00 USD | 450.55 USD | 0.00 USD | `+62.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,650,000.00 USD | 3,060.00 USD | 0.00 USD | `+62.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,660,000.00 USD | 1,930.00 USD | 0.00 USD | `+62.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,660,000.00 USD | 3,070.00 USD | 0.00 USD | `+63.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,660,000.00 USD | 1,920.00 USD | 0.00 USD | `+63.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,660,000.00 USD | 3,120.00 USD | 0.00 USD | `+64.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,670,000.00 USD | 1,550.00 USD | 0.00 USD | `+64.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,670,000.00 USD | 3,080.00 USD | 0.00 USD | `+64.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,670,000.00 USD | 647.56 USD | 0.00 USD | `+65.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,670,000.00 USD | 1,420.00 USD | 0.00 USD | `+65.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,670,000.00 USD | 2,130.00 USD | 0.00 USD | `+65.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,680,000.00 USD | 3,140.00 USD | 0.00 USD | `+66.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,680,000.00 USD | 342.25 USD | 0.00 USD | `+66.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,680,000.00 USD | 1,830.00 USD | 0.00 USD | `+66.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,680,000.00 USD | 2,990.00 USD | 0.00 USD | `+67.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,680,000.00 USD | 2,970.00 USD | 0.00 USD | `+67.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,690,000.00 USD | 324.54 USD | 0.00 USD | `+68.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,690,000.00 USD | 504.21 USD | 0.00 USD | `+69.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,690,000.00 USD | 166.00 USD | 0.00 USD | `+69.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,690,000.00 USD | 4,190.00 USD | 0.00 USD | `+70.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,710,000.00 USD | 15,940.00 USD | 0.00 USD | `+70.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,710,000.00 USD | 1,750.00 USD | 0.00 USD | `+70.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,710,000.00 USD | 2,860.00 USD | 0.00 USD | `+71.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,710,000.00 USD | 264.31 USD | 0.00 USD | `+73.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,710,000.00 USD | 599.34 USD | 0.00 USD | `+73.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,710,000.00 USD | 193.19 USD | 0.00 USD | `+74.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,720,000.00 USD | 3,950.00 USD | 0.00 USD | `+74.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,720,000.00 USD | 1,940.00 USD | 0.00 USD | `+75.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,880,000.00 USD | 160,550.00 USD | 0.00 USD | `+76.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,880,000.00 USD | 1,290.00 USD | 0.00 USD | `+77.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,880,000.00 USD | 905.60 USD | 0.00 USD | `+78.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,880,000.00 USD | 1,730.00 USD | 0.00 USD | `+78.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,880,000.00 USD | 1,710.00 USD | 0.00 USD | `+79.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,890,000.00 USD | 7,870.00 USD | 0.00 USD | `+79.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,890,000.00 USD | 630.05 USD | 0.00 USD | `+80.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,890,000.00 USD | 1,410.00 USD | 0.00 USD | `+80.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,900,000.00 USD | 2,610.00 USD | 0.00 USD | `+80.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,900,000.00 USD | 6,000.00 USD | 0.00 USD | `+82.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,900,000.00 USD | 1,620.00 USD | 0.00 USD | `+83.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,910,000.00 USD | 4,640.00 USD | 0.00 USD | `+84.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,910,000.00 USD | 371.88 USD | 0.00 USD | `+85.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,910,000.00 USD | 2,510.00 USD | 0.00 USD | `+85.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,910,000.00 USD | 380.68 USD | 0.00 USD | `+86.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,910,000.00 USD | 133.12 USD | 0.00 USD | `+87.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,910,000.00 USD | 1,490.00 USD | 0.00 USD | `+89.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,910,000.00 USD | 1,470.00 USD | 0.00 USD | `+89.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,930,000.00 USD | 11,170.00 USD | 0.00 USD | `+89.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,960,000.00 USD | 34,360.00 USD | 0.00 USD | `+90.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,960,000.00 USD | 253.21 USD | 0.00 USD | `+90.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,960,000.00 USD | 100.29 USD | 0.00 USD | `+90.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 7,960,000.00 USD | 1,550.00 USD | 0.00 USD | `+91.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,970,000.00 USD | 10,610.00 USD | 0.00 USD | `+93.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,970,000.00 USD | 309.43 USD | 0.00 USD | `+94.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 8,020,000.00 USD | 47,520.00 USD | 0.00 USD | `+94.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 8,100,000.00 USD | 81,310.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 8,100,000.00 USD | 1,390.00 USD | 0.00 USD | `+97.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 8,100,000.00 USD | 216.90 USD | 0.00 USD | `+99.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 8,100,000.00 USD | 738.45 USD | 0.00 USD | `+99.81%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.59` | 11,730,000.00 USD | 0.00 USD | 11,730,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD |
| `7D` | `3.60` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 11,120,000.00 USD | 0.00 USD | 11,120,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `1D` | `3.63` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,710.00 USD |
| `7D` | `3.63` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `1D` | `3.64` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 152.80 USD | 5,040.00 USD | 4.94 USD |
| `7D` | `3.64` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD |
| `1D` | `3.65` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 386.30 USD | 0.00 USD | 77.58 USD |
| `7D` | `3.65` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD |
| `1D` | `3.66` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 291.38 USD | 0.00 USD | 6.38 USD |
| `7D` | `3.66` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD |
| `1D` | `3.67` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,440.00 USD |
| `7D` | `3.67` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD |
| `1D` | `3.68` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 271.33 USD |
| `1D` | `3.69` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 23,960.00 USD | 0.00 USD | 9.86 USD |
| `7D` | `3.69` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `1D` | `3.70` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 39,190.00 USD | 0.00 USD | 55,000.00 USD |
| `7D` | `3.70` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `1D` | `3.71` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 430.40 USD | 0.00 USD | 6.22 USD |
| `7D` | `3.71` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD |
| `1D` | `3.72` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD |
| `7D` | `3.72` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.73` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,660.00 USD |
| `7D` | `3.73` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 94,200.00 USD | 33,110.00 USD | 43,040.00 USD |
| `7D` | `3.74` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD |
| `1D` | `3.75` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3.75` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD |
| `1D` | `3.76` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD |
| `7D` | `3.76` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `1D` | `3.77` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 187.12 USD | 5,330.00 USD | 1,990.00 USD |
| `7D` | `3.77` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD |
| `1D` | `3.78` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 106.91 USD | 4,490.00 USD | 29,160.00 USD |
| `7D` | `3.78` | 9,400,000.00 USD | 0.00 USD | 9,400,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 472.79 USD | 0.00 USD | 231.52 USD |
| `7D` | `3.79` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD |
| `1D` | `3.80` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.80` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD |
| `1D` | `3.81` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 54,290.00 USD | 0.00 USD | 13,250.00 USD |
| `7D` | `3.81` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD |
| `1D` | `3.82` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 11,960.00 USD | 583.30 USD |
| `7D` | `3.82` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 1,150.00 USD | 18,900.00 USD | 18,440.00 USD |
| `7D` | `3.83` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD |
| `7D` | `3.84` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.85` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD |
| `7D` | `3.85` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `3.86` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,740.00 USD |
| `7D` | `3.86` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 1,690.00 USD | 11,800.00 USD | 743.88 USD |
| `7D` | `3.87` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD |
| `1D` | `3.88` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 106,680.00 USD | 6,860.00 USD | 41,580.00 USD |
| `7D` | `3.88` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 112,840.00 USD | 37,150.00 USD | 23,890.00 USD |
| `7D` | `3.89` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD |
| `1D` | `3.90` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 31,410.00 USD | 10,910.00 USD | 20,820.00 USD |
| `7D` | `3.90` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD |
| `1D` | `3.91` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 32,140.00 USD | 35,760.00 USD | 38,020.00 USD |
| `7D` | `3.91` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 148,140.00 USD | 26,030.00 USD | 31,900.00 USD |
| `7D` | `3.92` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD |
| `1D` | `3.93` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 29,900.00 USD | 39,260.00 USD |
| `7D` | `3.93` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD |
| `1D` | `3.94` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 64,710.00 USD | 14,940.00 USD | 17,980.00 USD |
| `7D` | `3.94` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD |
| `1D` | `3.95` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 95,940.00 USD | 5,610.00 USD | 97,310.00 USD |
| `7D` | `3.95` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD |
| `1D` | `3.96` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,950.00 USD |
| `7D` | `3.96` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD |
| `1D` | `3.97` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 190,720.00 USD | 66,010.00 USD | 105,360.00 USD |
| `7D` | `3.97` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD |
| `1D` | `3.98` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,820.00 USD |
| `7D` | `3.98` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD |
| `1D` | `3.99` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 413,960.00 USD | 106,190.00 USD | 136,510.00 USD |
| `7D` | `3.99` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD |
| `1D` | `4.00` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,480.00 USD |
| `7D` | `4.00` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 112,570.00 USD | 72,850.00 USD | 126,200.00 USD |
| `7D` | `4.01` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD |
| `1D` | `4.02` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 180,340.00 USD | 50,310.00 USD | 108,730.00 USD |
| `7D` | `4.02` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD |
| `1D` | `4.03` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 189,730.00 USD | 55,650.00 USD | 267,230.00 USD |
| `7D` | `4.03` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD |
| `1D` | `4.04` | 759,140.00 USD | 0.00 USD | 759,140.00 USD | 105,670.00 USD | 48,960.00 USD | 211,380.00 USD |
| `7D` | `4.04` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD |
| `1D` | `4.05` | 393,130.00 USD | 0.00 USD | 393,130.00 USD | 2,370.00 USD | 46,690.00 USD | 95,770.00 USD |
| `7D` | `4.05` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD |
| `1D` | `4.06` | 248,290.00 USD | 0.00 USD | 248,290.00 USD | 0.00 USD | 27,150.00 USD | 126,130.00 USD |
| `7D` | `4.06` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD |
| `1D` | `4.07` | 95,010.00 USD | 0.00 USD | 95,010.00 USD | 0.00 USD | 72,110.00 USD | 22,900.00 USD |
| `7D` | `4.07` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD |
| `1D` | `4.08` | 506,800.00 USD | 506,800.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 506.63 USD |
| `1D` | `4.08` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 506.63 USD |
| `7D` | `4.08` | 356,630.00 USD | 356,630.00 USD | 0.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `7D` | `4.08` | 713,260.00 USD | 713,260.00 USD | 0.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `7D` | `4.09` | 931,780.00 USD | 931,780.00 USD | 0.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD |
| `1D` | `4.10` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 509.39 USD |
| `7D` | `4.10` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `1D` | `4.11` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 59,250.00 USD | 1,270.00 USD |
| `1D` | `4.12` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 80,980.00 USD | 228,820.00 USD |
| `1D` | `4.13` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD |
| `1D` | `4.14` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.14` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD |
| `1D` | `4.15` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD |
| `1D` | `4.17` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD |
| `1D` | `4.18` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 129,470.00 USD | 17,040.00 USD | 0.00 USD |
| `1D` | `4.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 174,270.00 USD | 0.00 USD | 185,170.00 USD |
| `7D` | `4.20` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD |
| `1D` | `4.22` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD |
| `1D` | `4.23` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD |
| `1D` | `4.24` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD |
| `1D` | `4.25` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD |
| `7D` | `4.25` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD |
| `1D` | `4.26` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 60,530.00 USD | 173,320.00 USD | 0.00 USD |
| `7D` | `4.26` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 677,660.00 USD | 24,620.00 USD | 152,190.00 USD |
| `7D` | `4.27` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 314,270.00 USD | 30,410.00 USD | 288,520.00 USD |
| `7D` | `4.28` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD |
| `1D` | `4.29` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 152,480.00 USD | 32,690.00 USD | 161,990.00 USD |
| `7D` | `4.29` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 32,410.00 USD | 45,120.00 USD | 163,260.00 USD |
| `7D` | `4.30` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 304,920.00 USD | 13,580.00 USD | 94,870.00 USD |
| `7D` | `4.31` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 86,850.00 USD | 73,400.00 USD | 19.74 USD |
| `7D` | `4.32` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD |
| `1D` | `4.33` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 255,620.00 USD | 93,880.00 USD | 87,020.00 USD |
| `7D` | `4.33` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 270,720.00 USD | 140,540.00 USD | 114,780.00 USD |
| `7D` | `4.34` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD |
| `1D` | `4.35` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 855.62 USD | 0.00 USD | 85,420.00 USD |
| `7D` | `4.35` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 84,400.00 USD | 12,310.00 USD | 31,180.00 USD |
| `7D` | `4.36` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD |
| `1D` | `4.37` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 52,520.00 USD | 46,860.00 USD | 131,580.00 USD |
| `1D` | `4.38` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 248,590.00 USD | 34,500.00 USD | 559,190.00 USD |
| `7D` | `4.38` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 399.48 USD | 17,360.00 USD | 310,770.00 USD |
| `7D` | `4.39` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD |
| `1D` | `4.40` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 288,790.00 USD | 34,040.00 USD | 81,080.00 USD |
| `7D` | `4.40` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD |
| `1D` | `4.41` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 196,820.00 USD | 112,990.00 USD | 63,590.00 USD |
| `7D` | `4.41` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 47,240.00 USD | 1,320.00 USD |
| `7D` | `4.42` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 5,100.00 USD | 49,400.00 USD | 95,230.00 USD |
| `7D` | `4.43` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD |
| `1D` | `4.44` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 292,720.00 USD |
| `7D` | `4.44` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD |
| `1D` | `4.45` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 649.63 USD | 50,720.00 USD | 1,760.00 USD |
| `1D` | `4.46` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 704.30 USD | 9,070.00 USD | 3,140.00 USD |
| `7D` | `4.46` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD |
| `1D` | `4.47` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 210.23 USD | 16,700.00 USD | 18,240.00 USD |
| `7D` | `4.47` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 117,480.00 USD | 73,240.00 USD | 25,450.00 USD |
| `7D` | `4.48` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `4.49` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 252,600.00 USD | 155,000.00 USD | 150,370.00 USD |
| `7D` | `4.49` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 361,560.00 USD | 65,710.00 USD | 118,110.00 USD |
| `7D` | `4.50` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD |
| `1D` | `4.51` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 186,860.00 USD | 307,580.00 USD | 312,490.00 USD |
| `7D` | `4.51` | 12,800,000.00 USD | 12,800,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.52` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 287,830.00 USD | 88,150.00 USD | 242,940.00 USD |
| `7D` | `4.52` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 487,540.00 USD | 0.00 USD | 281,090.00 USD |
| `7D` | `4.53` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD |
| `1D` | `4.54` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD |
| `7D` | `4.54` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 196,080.00 USD |
| `1D` | `4.56` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD |
| `7D` | `4.56` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 67,910.00 USD |
| `7D` | `4.57` | 16,190,000.00 USD | 16,190,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD |
| `1D` | `4.58` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 506,750.00 USD | 73,690.00 USD | 876,090.00 USD |
| `7D` | `4.58` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 19,130,000.00 USD | 19,130,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 79,670.00 USD |
| `7D` | `4.59` | 17,910,000.00 USD | 17,910,000.00 USD | 0.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 19,340,000.00 USD | 19,340,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 67,260.00 USD |
| `7D` | `4.60` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 60,890.00 USD |
| `7D` | `4.61` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD |
| `7D` | `4.62` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `4.63` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 335.46 USD |
| `7D` | `4.63` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 334,190.00 USD | 11,270.00 USD | 61,860.00 USD |
| `7D` | `4.64` | 18,910,000.00 USD | 18,910,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD |
| `1D` | `4.65` | 21,100,000.00 USD | 21,100,000.00 USD | 0.00 USD | 423,550.00 USD | 52,020.00 USD | 600,630.00 USD |
| `7D` | `4.65` | 19,330,000.00 USD | 19,330,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `4.66` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 281,290.00 USD | 316,500.00 USD | 379,970.00 USD |
| `7D` | `4.66` | 19,640,000.00 USD | 19,640,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 22,640,000.00 USD | 22,640,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 377,750.00 USD |
| `7D` | `4.67` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 23,250,000.00 USD | 23,250,000.00 USD | 0.00 USD | 345,840.00 USD | 81,340.00 USD | 177,210.00 USD |
| `7D` | `4.68` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 23,750,000.00 USD | 23,750,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 254,450.00 USD |
| `7D` | `4.69` | 20,690,000.00 USD | 20,690,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD |
| `7D` | `4.70` | 21,010,000.00 USD | 21,010,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 25,060,000.00 USD | 25,060,000.00 USD | 0.00 USD | 365,580.00 USD | 284,360.00 USD | 316,400.00 USD |
| `7D` | `4.71` | 21,420,000.00 USD | 21,420,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `1D` | `4.72` | 25,360,000.00 USD | 25,360,000.00 USD | 0.00 USD | 5,440.00 USD | 187,480.00 USD | 103,550.00 USD |
| `7D` | `4.72` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 25,510,000.00 USD | 25,510,000.00 USD | 0.00 USD | 52,120.00 USD | 37,010.00 USD | 60,650.00 USD |
| `7D` | `4.73` | 21,670,000.00 USD | 21,670,000.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD |
| `7D` | `4.74` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `7D` | `4.75` | 22,530,000.00 USD | 22,530,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `7D` | `4.76` | 23,880,000.00 USD | 23,880,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `7D` | `4.77` | 24,780,000.00 USD | 24,780,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `7D` | `4.78` | 26,140,000.00 USD | 26,140,000.00 USD | 0.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD |
| `7D` | `4.79` | 27,170,000.00 USD | 27,170,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `7D` | `4.80` | 28,760,000.00 USD | 28,760,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `7D` | `4.81` | 29,390,000.00 USD | 29,390,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `7D` | `4.82` | 32,160,000.00 USD | 32,160,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 33,810,000.00 USD | 33,810,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 34,300,000.00 USD | 34,300,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 36,320,000.00 USD | 36,320,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 37,730,000.00 USD | 37,730,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 38,790,000.00 USD | 38,790,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `7D` | `4.88` | 40,370,000.00 USD | 40,370,000.00 USD | 0.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD |
| `7D` | `4.89` | 40,960,000.00 USD | 40,960,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `7D` | `4.90` | 42,100,000.00 USD | 42,100,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `7D` | `4.91` | 43,540,000.00 USD | 43,540,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `7D` | `4.92` | 45,270,000.00 USD | 45,270,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `7D` | `4.93` | 46,830,000.00 USD | 46,830,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `7D` | `4.94` | 48,160,000.00 USD | 48,160,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD |
| `7D` | `4.95` | 49,460,000.00 USD | 49,460,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `7D` | `4.96` | 50,700,000.00 USD | 50,700,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `7D` | `4.97` | 51,080,000.00 USD | 51,080,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `7D` | `4.98` | 51,740,000.00 USD | 51,740,000.00 USD | 0.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD |
| `7D` | `4.99` | 52,090,000.00 USD | 52,090,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `7D` | `5.00` | 52,790,000.00 USD | 52,790,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `7D` | `5.01` | 54,620,000.00 USD | 54,620,000.00 USD | 0.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD |
| `7D` | `5.02` | 56,070,000.00 USD | 56,070,000.00 USD | 0.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD |
| `7D` | `5.03` | 57,190,000.00 USD | 57,190,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD |
| `7D` | `5.04` | 58,280,000.00 USD | 58,280,000.00 USD | 0.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD |
| `7D` | `5.05` | 59,730,000.00 USD | 59,730,000.00 USD | 0.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD |
| `7D` | `5.06` | 60,410,000.00 USD | 60,410,000.00 USD | 0.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 61,580,000.00 USD | 61,580,000.00 USD | 0.00 USD | 358,750.00 USD | 137,080.00 USD | 673,800.00 USD |
| `7D` | `5.08` | 62,100,000.00 USD | 62,100,000.00 USD | 0.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD |
| `7D` | `5.09` | 62,640,000.00 USD | 62,640,000.00 USD | 0.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD |
| `7D` | `5.10` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 63,620,000.00 USD | 63,620,000.00 USD | 0.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD |
| `7D` | `5.12` | 64,190,000.00 USD | 64,190,000.00 USD | 0.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD |
| `7D` | `5.14` | 65,200,000.00 USD | 65,200,000.00 USD | 0.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD |
| `7D` | `5.15` | 65,750,000.00 USD | 65,750,000.00 USD | 0.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD |
| `7D` | `5.16` | 66,270,000.00 USD | 66,270,000.00 USD | 0.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 66,940,000.00 USD | 66,940,000.00 USD | 0.00 USD | 280,710.00 USD | 85,040.00 USD | 309,950.00 USD |
| `7D` | `5.18` | 67,200,000.00 USD | 67,200,000.00 USD | 0.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD |
| `7D` | `5.19` | 67,420,000.00 USD | 67,420,000.00 USD | 0.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD |
| `7D` | `5.20` | 67,670,000.00 USD | 67,670,000.00 USD | 0.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD |
| `7D` | `5.21` | 67,900,000.00 USD | 67,900,000.00 USD | 0.00 USD | 105,330.00 USD | 20,850.00 USD | 110,520.00 USD |
| `7D` | `5.22` | 67,970,000.00 USD | 67,970,000.00 USD | 0.00 USD | 52,130.00 USD | 13,410.00 USD | 398.26 USD |
| `7D` | `5.23` | 68,020,000.00 USD | 68,020,000.00 USD | 0.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.13B` | Total OI Tokens: `276,224,844.5 NEAR`
  * 1h OI Change: `-1.32%` | 4h OI Change: `-9.07%` | 24h OI Change: `-15.01%`
  * Exchange Breakdown: Binance=`215.63M` | Bybit=`150.30M` | OKX=`48.98M` | Hyperliquid=`227.90M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.63K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0025%` | **USDT OKX** | `0.0056%` |
| **USDT Bybit** | `-0.0041%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0023%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0050%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `45.24%` | `54.76%` | `0.83` | 38,560,000.00 USD |
| `15M` | `Binance` | `48.44%` | `51.56%` | `0.94` | 15,500,000.00 USD |
| `15M` | `OKX` | `42.48%` | `57.52%` | `0.74` | 3,860,000.00 USD |
| `15M` | `Bybit` | `44.73%` | `55.27%` | `0.81` | 5,550,000.00 USD |
| `15M` | `KuCoin` | `51.64%` | `48.36%` | `1.07` | 236,090.00 USD |
| `15M` | `Gate` | `39.76%` | `60.24%` | `0.66` | 927,700.00 USD |
| `15M` | `Bitget` | `43.43%` | `56.57%` | `0.77` | 1,460,000.00 USD |
| `15M` | `BingX` | `50.14%` | `49.86%` | `1.01` | 3,170,000.00 USD |
| `15M` | `MEXC` | `38.75%` | `61.25%` | `0.63` | 1,430,000.00 USD |
| `15M` | `Bitunix` | `40.24%` | `59.76%` | `0.67` | 629,230.00 USD |
| `15M` | `Hyperliquid` | `29.96%` | `70.04%` | `0.43` | 4,460,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.35%` | `53.65%` | `0.86` | 63,900.00 USD |
| `15M` | `Crypto.com` | `66.03%` | `33.97%` | `1.94` | 1,890.00 USD |
| `15M` | `WhiteBIT` | `88.2%` | `11.8%` | `7.47` | 911,420.00 USD |
| `15M` | `HTX` | `18.39%` | `81.61%` | `0.23` | 17,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `28.45%` | `71.55%` | `0.40` | 174,420.00 USD |
| `15M` | `Aster` | `26.46%` | `73.54%` | `0.36` | 31,140.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.91%` | `55.09%` | `0.82` | 130,880.00 USD |
| `15M` | `Whale Positions` | `48.44%` | `51.56%` | `0.94` | 15,500,000.00 USD |
| `15M` | `Global Accounts` | `45.24%` | `54.76%` | `0.83` | 38,560,000.00 USD |
| `1H` | `NEAR` | `47.99%` | `52.01%` | `0.92` | 134,470,000.00 USD |
| `1H` | `Binance` | `49.37%` | `50.63%` | `0.98` | 51,180,000.00 USD |
| `1H` | `OKX` | `47.82%` | `52.18%` | `0.92` | 13,300,000.00 USD |
| `1H` | `Bybit` | `47.2%` | `52.8%` | `0.89` | 18,900,000.00 USD |
| `1H` | `KuCoin` | `46.1%` | `53.9%` | `0.86` | 603,240.00 USD |
| `1H` | `Gate` | `46.72%` | `53.28%` | `0.88` | 2,520,000.00 USD |
| `1H` | `Bitget` | `47.07%` | `52.93%` | `0.89` | 4,230,000.00 USD |
| `1H` | `BingX` | `50.07%` | `49.93%` | `1.00` | 6,810,000.00 USD |
| `1H` | `MEXC` | `40.2%` | `59.8%` | `0.67` | 7,570,000.00 USD |
| `1H` | `Bitunix` | `49.29%` | `50.71%` | `0.97` | 2,270,000.00 USD |
| `1H` | `Hyperliquid` | `42.35%` | `57.65%` | `0.73` | 21,490,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.46%` | `52.54%` | `0.90` | 627,580.00 USD |
| `1H` | `Crypto.com` | `50.29%` | `49.71%` | `1.01` | 4,780.00 USD |
| `1H` | `WhiteBIT` | `84.83%` | `15.17%` | `5.59` | 3,490,000.00 USD |
| `1H` | `HTX` | `42.45%` | `57.55%` | `0.74` | 50,600.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.37%` | `54.63%` | `0.83` | 716,240.00 USD |
| `1H` | `Aster` | `18.26%` | `81.74%` | `0.22` | 157,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `40.86%` | `59.14%` | `0.69` | 560,680.00 USD |
| `1H` | `Whale Positions` | `49.37%` | `50.63%` | `0.98` | 51,180,000.00 USD |
| `1H` | `Global Accounts` | `47.99%` | `52.01%` | `0.92` | 134,470,000.00 USD |
| `4H` | `NEAR` | `47.86%` | `52.14%` | `0.92` | 338,810,000.00 USD |
| `4H` | `Binance` | `48.05%` | `51.95%` | `0.92` | 135,600,000.00 USD |
| `4H` | `OKX` | `48.56%` | `51.44%` | `0.94` | 45,870,000.00 USD |
| `4H` | `Bybit` | `49.55%` | `50.45%` | `0.98` | 45,760,000.00 USD |
| `4H` | `KuCoin` | `49.92%` | `50.08%` | `1.00` | 3,740,000.00 USD |
| `4H` | `Gate` | `47.71%` | `52.29%` | `0.91` | 8,060,000.00 USD |
| `4H` | `Bitget` | `46.12%` | `53.88%` | `0.86` | 21,150,000.00 USD |
| `4H` | `BingX` | `44.05%` | `55.95%` | `0.79` | 10,630,000.00 USD |
| `4H` | `MEXC` | `46.53%` | `53.47%` | `0.87` | 29,160,000.00 USD |
| `4H` | `Bitunix` | `50.54%` | `49.46%` | `1.02` | 13,360,000.00 USD |
| `4H` | `Hyperliquid` | `43.42%` | `56.58%` | `0.77` | 11,870,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.6%` | `49.4%` | `1.02` | 2,850,000.00 USD |
| `4H` | `Crypto.com` | `50.12%` | `49.88%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `66.12%` | `33.88%` | `1.95` | 5,680,000.00 USD |
| `4H` | `HTX` | `46.9%` | `53.1%` | `0.88` | 708,400.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.24%` | `50.76%` | `0.97` | 2,430,000.00 USD |
| `4H` | `Aster` | `50.84%` | `49.16%` | `1.03` | 1,480,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.6%` | `55.4%` | `0.81` | 441,910.00 USD |
| `4H` | `Whale Positions` | `48.05%` | `51.95%` | `0.92` | 135,600,000.00 USD |
| `4H` | `Global Accounts` | `47.86%` | `52.14%` | `0.92` | 338,810,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.16` | `4.18` | `4.16` | `4.26` | `4.10` | 52,737,896.00 USD | 23,168,223.37 USD | 29,569,672.63 USD | -6,401,449.26 USD | `-12.14%` | `7B / 20S` |
| `0:00 UTC` | `4.15` | `4.16` | `4.15` | `4.21` | `4.12` | 38,451,702.31 USD | 19,031,443.49 USD | 19,420,258.82 USD | -388,815.33 USD | `-1.01%` | `3B / 6S` |
| `5:00 UTC` | `4.23` | `4.22` | `4.23` | `4.28` | `4.18` | 19,231,459.24 USD | 9,485,975.24 USD | 9,745,484.00 USD | -259,508.77 USD | `-1.35%` | `5B / 4S` |
| `0:00 UTC` | `4.24` | `4.23` | `4.24` | `4.26` | `4.18` | 9,925,749.34 USD | 5,368,569.39 USD | 4,557,179.95 USD | 811,389.45 USD | `+8.17%` | `5B / 13S` |
| `5:00 UTC` | `4.17` | `4.17` | `4.17` | `4.20` | `4.14` | 11,567,070.53 USD | 6,145,277.52 USD | 5,421,793.01 USD | 723,484.51 USD | `+6.25%` | `3B / 3S` |
| `0:00 UTC` | `4.10` | `4.12` | `4.10` | `4.17` | `4.08` | 24,831,581.83 USD | 12,210,682.44 USD | 12,620,899.39 USD | -410,216.95 USD | `-1.65%` | `7B / 10S` |
| `5:00 UTC` | `4.15` | `4.14` | `4.15` | `4.16` | `4.09` | 14,046,475.77 USD | 7,755,711.86 USD | 6,290,763.91 USD | 1,464,947.96 USD | `+10.43%` | `2B / 3S` |
| `0:00 UTC` | `4.13` | `4.13` | `4.13` | `4.16` | `4.11` | 11,266,117.92 USD | 5,322,808.37 USD | 5,943,309.55 USD | -620,501.18 USD | `-5.51%` | `3B / 3S` |
| `5:00 UTC` | `4.10` | `4.10` | `4.10` | `4.12` | `4.08` | 9,855,518.22 USD | 4,311,916.38 USD | 5,543,601.84 USD | -1,231,685.45 USD | `-12.50%` | `0B / 4S` |
| `0:00 UTC` | `4.07` | `4.07` | `4.07` | `4.11` | `4.05` | 11,208,987.95 USD | 5,093,297.61 USD | 6,115,690.35 USD | -1,022,392.74 USD | `-9.12%` | `5B / 10S` |

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
| `5m` | 96,270.00 USD | 834,840.00 USD | **`ACCUMULATION`** |
| `15m` | -1,110,000.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,100,000.00 USD | -3,340,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,990,000.00 USD | -2,550,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -5,030,000.00 USD | -4,960,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,060,000.00 USD | -15,600,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -14,480,000.00 USD | -19,520,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -16,830,000.00 USD | -27,430,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -16,520,000.00 USD | -31,650,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -27,480,000.00 USD | -73,950,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -80,530,000.00 USD | -121,010,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -249,800,000.00 USD | -682,430,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+96.27K` | 15m=`-1.11M` | 1h=`-1.99M` | 24h=`-27.48M`
* Futures Capital Netflows: 5m=`+834.84K` | 15m=`-1.65M` | 1h=`-2.55M` | 24h=`-73.95M`
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
  * Execution Entry: `4.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3.91` (Risk Distance: `0.1246` pts)
  * +2.5R Take Profit: `4.35`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.16` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.28` (Risk Distance: `0.1246` pts)
  * +2.5R Take Profit: `3.85`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
