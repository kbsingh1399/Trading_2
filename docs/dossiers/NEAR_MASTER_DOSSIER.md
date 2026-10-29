# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:41:04 IST` (`2026-10-29 23:11:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.05` | **Live Ask Quote**: `4.08` | **Mid Price**: `4.07`
- **Spread Points**: `29.00` | **Spread BPS**: `71.26 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.07` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.10` | Lower -3.00σ Band: `4.04`
  * Upper +2.51σ Band: `4.09` | Lower -2.51σ Band: `4.05`
  * Upper +2.01σ Band: `4.09` | Lower -2.01σ Band: `4.05`
  * Upper +2.00σ Band: `4.09` | Lower -2.00σ Band: `4.05`
  * Upper +1.28σ Band: `4.08` | Lower -1.28σ Band: `4.06`
  * Upper +1.00σ Band: `4.08` | Lower -1.00σ Band: `4.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.07` | EMA-20=`4.07` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.07` (Slope: `+0.0000`) | EMA-100=`4.07`
  * Institutional Anchors: EMA-144=`4.07` | EMA-200=`4.07` (Slope: `+0.0000`) | EMA-233=`4.07`
- **Range Boundaries**: 24H High=`4.11` | 24H Low=`4.03` | Weekly High=`4.15` | Weekly Low=`3.99`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.17` (Distance: `-2.30%`)
  * Point of Control (POC) = `4.09` (Distance: `-0.59%`)
  * Value Area Low (VAL) = `4.06` (Distance: `+0.31%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.65` | Weekly POC=`4.45` | Weekly VAL=`4.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`4.05`
  * London Session (08:00-16:00 UTC): High=`4.09` | Low=`4.05`
  * New York Session (13:00-21:00 UTC): High=`4.09` | Low=`4.05`
  * Initial Balance (First Hour): IB High=`4.08` | IB Low=`4.06`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.05` - `4.09`
  * Optimal Trade Entry (OTE 0.705): `4.08`
  * Structural Invalidation Anchor (0.786): `4.10`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.10` | `4.12` | `4.09` | `4.11` | `738,544` | 3,027,774.71 USD | -50,980.05 USD | `-1.68%` | -39,797,973.30 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4.11` | `4.11` | `4.06` | `4.07` | `1,040,283` | 4,245,025.16 USD | -680,892.16 USD | `-16.04%` | -40,478,865.46 USD | `-1.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.07` | `4.08` | `4.07` | `4.07` | `143,652` | 584,942.36 USD | -261,332.37 USD | `-44.68%` | -40,740,197.84 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.12` | `4.16` | `4.11` | `4.11` | `2,725,753` | 11,266,117.92 USD | -620,501.18 USD | `-5.51%` | -38,474,040.38 USD | `-0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.11` | `4.12` | `4.08` | `4.11` | `2,404,416` | 9,855,518.22 USD | -1,231,685.46 USD | `-12.50%` | -39,705,725.83 USD | `-0.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.11` | `4.11` | `4.06` | `4.07` | `1,189,667` | 4,853,308.00 USD | -948,839.15 USD | `-19.55%` | -40,654,564.98 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4.17` | `4.28` | `4.12` | `4.15` | `18,917,752` | 79,175,981.42 USD | 886,549.86 USD | `+1.12%` | -38,736,880.09 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4.15` | `4.17` | `4.08` | `4.11` | `14,553,439` | 59,999,693.74 USD | -797,455.63 USD | `-1.33%` | -39,534,335.71 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.11` | `4.11` | `4.06` | `4.07` | `1,183,935` | 4,829,967.52 USD | -942,224.53 USD | `-19.51%` | -40,476,560.25 USD | `+0.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.06` | `4.07` | `62,451,981` | 261,705,830.01 USD | -12,080,925.38 USD | `-4.62%` | -40,408,190.68 USD | `-0.76` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -27,473,639.56 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -28,567,348.59 USD | `+1.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.06` | `4.07` | `62,451,981` | 261,705,830.01 USD | -12,080,925.38 USD | `-4.62%` | -40,408,190.68 USD | `-0.76` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`4.07`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `70` | `0x7737...bf66` | `LONG` | 23,117,082.27 USD | `5,640,376.30` | `2.35` | `4.07` | `0.8369` | 9,845,179.44 USD | `+42.59%` | `10X Cross` |
| `138` | `0xb581...6f4f` | `LONG` | 14,796,360.00 USD | `3,600,000.00` | `5.19` | `4.07` | `0.000000` | -3,896,675.22 USD | `-26.34%` | `4X Cross` |
| `225` | `0xdd53...2b13` | `SHORT` | 9,778,902.99 USD | `2,400,202.00` | `2.31` | `4.07` | `29.76` | -4,233,054.43 USD | `-43.29%` | `3X Cross` |
| `281` | `0x77ee...2902` | `LONG` | 8,412,801.90 USD | `2,063,023.10` | `1.93` | `4.07` | `0.000000` | 4,421,605.97 USD | `+52.56%` | `10X Cross` |
| `283` | `0xefe4...194b` | `SHORT` | 8,289,012.83 USD | `2,033,365.10` | `4.44` | `4.07` | `10.83` | 741,004.93 USD | `+8.94%` | `5X Cross` |
| `394` | `0xb83d...6e36` | `SHORT` | 5,883,082.93 USD | `1,445,759.10` | `5.19` | `4.07` | `106.99` | 1,626,366.01 USD | `+27.64%` | `3X Cross` |
| `411` | `0xb46b...538e` | `SHORT` | 5,435,035.04 USD | `1,336,000.00` | `4.33` | `4.07` | `7.58` | 349,829.02 USD | `+6.44%` | `10X Cross` |
| `426` | `0x9df2...c665` | `SHORT` | 5,149,056.00 USD | `1,265,000.00` | `2.03` | `4.07` | `29.04` | -2,582,373.66 USD | `-50.15%` | `10X Cross` |
| `475` | `0x60b0...991e` | `LONG` | 4,594,892.23 USD | `1,121,307.10` | `5.00` | `4.07` | `0.000000` | -1,006,532.20 USD | `-21.91%` | `10X Cross` |
| `506` | `0xcac1...26b3` | `SHORT` | 4,376,966.68 USD | `1,073,743.90` | `2.48` | `4.07` | `12.24` | -1,717,023.22 USD | `-39.23%` | `10X Cross` |
| `517` | `0x781e...96b7` | `SHORT` | 4,234,829.34 USD | `1,039,604.60` | `2.45` | `4.07` | `7.53` | -1,690,492.15 USD | `-39.92%` | `10X Cross` |
| `603` | `0x45d2...4029` | `SHORT` | 3,713,262.08 USD | `909,400.00` | `3.26` | `4.07` | `49.39` | -747,112.18 USD | `-20.12%` | `10X Cross` |
| `615` | `0x4cae...7c34` | `LONG` | 3,670,463.96 USD | `900,086.80` | `3.52` | `4.07` | `3.09` | 498,062.98 USD | `+13.57%` | `10X Cross` |
| `668` | `0x7fda...17d1` | `SHORT` | 3,376,151.41 USD | `828,227.00` | `4.46` | `4.07` | `49.12` | 318,291.77 USD | `+9.43%` | `10X Cross` |
| `770` | `0x9aa5...58af` | `SHORT` | 2,951,191.29 USD | `723,977.10` | `4.78` | `4.07` | `16.73` | 508,441.90 USD | `+17.23%` | `10X Cross` |
| `848` | `0x005a...61fe` | `LONG` | 2,655,457.90 USD | `652,414.60` | `2.08` | `4.07` | `2.43` | 1,297,926.67 USD | `+48.88%` | `7X Cross` |
| `850` | `0xba5d...a352` | `SHORT` | 2,653,005.41 USD | `647,532.50` | `2.83` | `4.07` | `13.20` | -820,290.46 USD | `-30.92%` | `10X Cross` |
| `865` | `0xb695...a92d` | `SHORT` | 2,600,522.40 USD | `639,231.70` | `4.57` | `4.07` | `43.82` | 322,836.53 USD | `+12.41%` | `10X Cross` |
| `866` | `0xd1dd...9e85` | `SHORT` | 2,600,154.68 USD | `637,621.00` | `4.96` | `4.07` | `18.29` | 563,318.06 USD | `+21.66%` | `10X Cross` |
| `871` | `0x123d...3bff` | `SHORT` | 2,585,601.89 USD | `635,392.30` | `2.09` | `4.07` | `9.40` | -1,259,653.42 USD | `-48.72%` | `10X Cross` |
| `889` | `0xcf53...ee11` | `SHORT` | 2,533,945.88 USD | `621,598.40` | `5.07` | `4.07` | `24.94` | 618,224.37 USD | `+24.40%` | `10X Cross` |
| `1032` | `0xbfc7...80b4` | `SHORT` | 2,164,621.50 USD | `531,000.00` | `2.01` | `4.07` | `11.16` | -1,099,422.11 USD | `-50.79%` | `10X Cross` |
| `1176` | `0xef96...9383` | `SHORT` | 1,908,532.51 USD | `468,443.50` | `4.50` | `4.07` | `13.18` | 200,768.57 USD | `+10.52%` | `10X Cross` |
| `1352` | `0xe097...d0fe` | `LONG` | 1,630,544.00 USD | `400,000.00` | `5.29` | `4.07` | `0.000000` | -486,243.30 USD | `-29.82%` | `10X Cross` |
| `1489` | `0x6e8f...4364` | `LONG` | 1,469,043.10 USD | `361,210.50` | `3.28` | `4.07` | `3.60` | 284,982.88 USD | `+19.40%` | `10X Cross` |
| `1497` | `0xdf95...7d72` | `SHORT` | 1,457,107.25 USD | `358,038.00` | `4.23` | `4.07` | `112.42` | 58,224.02 USD | `+4.00%` | `10X Cross` |
| `1512` | `0xcf67...eb24` | `LONG` | 1,437,520.00 USD | `350,000.00` | `1.98` | `4.07` | `1.67` | 745,902.12 USD | `+51.89%` | `10X Cross` |
| `1639` | `0xfc27...9d9d` | `SHORT` | 1,304,470.62 USD | `319,997.70` | `5.01` | `4.07` | `57.96` | 299,072.00 USD | `+22.93%` | `10X Cross` |
| `1730` | `0x9836...457e` | `LONG` | 1,221,872.44 USD | `300,000.60` | `4.57` | `4.07` | `1.93` | -150,200.73 USD | `-12.29%` | `10X Cross` |
| `1735` | `0x17c3...a868` | `LONG` | 1,214,263.67 USD | `297,879.40` | `4.37` | `4.07` | `0.000000` | -88,619.25 USD | `-7.30%` | `3X Cross` |
| `1745` | `0x2577...4897` | `LONG` | 1,198,815.53 USD | `293,935.40` | `4.16` | `4.07` | `0.000000` | -24,920.68 USD | `-2.08%` | `10X Cross` |
| `1754` | `0xe065...0f85` | `SHORT` | 1,192,024.03 USD | `290,227.90` | `2.81` | `4.07` | `6.66` | -375,279.78 USD | `-31.48%` | `10X Cross` |
| `1779` | `0x023a...2355` | `SHORT` | 1,172,708.47 USD | `288,120.60` | `4.53` | `4.07` | `27.97` | 132,332.11 USD | `+11.28%` | `10X Cross` |
| `1956` | `0xff43...d924` | `LONG` | 1,025,365.14 USD | `249,474.50` | `4.64` | `4.07` | `3.28` | -132,678.53 USD | `-12.94%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.59` | 11,348.45 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 11.35K USD at 4.5934 USD [API] | `2026-10-28 16:38:51` |
| `ANNOUNCEMENT` | `INFO` | `4.60` | 9,832.24 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.83K USD at 4.6044 USD [API] | `2026-10-28 17:44:33` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 9,273.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.27K USD at 4.6100 USD [API] | `2026-10-28 17:54:59` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 5,803.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.80K USD at 4.5936 USD [API] | `2026-10-28 17:59:18` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 29,008.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 29.01K USD at 4.5936 USD [API] | `2026-10-28 17:59:18` |
| `ANNOUNCEMENT` | `INFO` | `4.65` | 5,635.55 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.64K USD at 4.6521 USD [API] | `2026-10-28 18:04:35` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 5,935.57 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.94K USD at 4.6055 USD [API] | `2026-10-28 18:11:25` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 9,990.95 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.99K USD at 4.6054 USD [API] | `2026-10-28 18:11:25` |
| `ANNOUNCEMENT` | `INFO` | `4.60` | 5,273.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.27K USD at 4.6043 USD [API] | `2026-10-28 18:22:01` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 5,885.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.89K USD at 4.7081 USD [API] | `2026-10-28 18:44:24` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 6,803.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.80K USD at 4.6850 USD [API] | `2026-10-28 18:52:00` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 8,107.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.11K USD at 4.6978 USD [API] | `2026-10-28 18:59:51` |
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
| `Live` | `Long Liquidation` | `0.8150` | 2,110.00 USD | 33,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 4,770,000.00 USD | 33,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 4,230.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 470.47 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,650.00 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 28,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 28,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 2,570.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,050.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 2,910.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 28,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 31,200.00 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,360.00 USD | 28,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,950.00 USD | 28,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 11,860.00 USD | 28,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 1,160.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 1,210.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 1,330.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 8,840.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 17,280.00 USD | 28,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,150.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 30,060.00 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 227.30 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 55,360.00 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 238.78 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 23,160.00 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 38,720.00 USD | 28,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 110,450.00 USD | 28,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 3,370.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 4,410.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 170.21 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,640.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 795.11 USD | 28,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 28,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 6,450.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 3,330.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 669.86 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 85,140.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,890.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 14,650.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 4,420.00 USD | 28,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 814.78 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 300.25 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 530,700.00 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 311.00 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 13,300.00 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 5,240.00 USD | 27,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,380.00 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 12,630.00 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 1,460.00 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 19,600.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 2,440.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 1,450.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 681.98 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 108.71 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 14,290.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 12,950.00 USD | 27,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 8,670.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 11,320.00 USD | 27,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 4,810.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 42,700.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 40,550.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,290.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 4,130.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 35,540.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,890.00 USD | 27,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 3,130.00 USD | 27,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 2,070.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 5,740.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 23,920.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 11,560.00 USD | 27,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 2,010.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 10,180.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 42,930.00 USD | 27,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 1,320.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 122,770.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 1,220.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 582.39 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 17,030.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 15,730.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 1,230.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 10,540.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 6,820.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 1,880.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 229,560.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,640.00 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 94,190.00 USD | 26,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 30,070.00 USD | 26,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 594.13 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 77,890.00 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 225,110.00 USD | 26,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 13,820.00 USD | 26,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 968.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 74,790.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 8,330.00 USD | 26,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,310.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 1,060.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 42,920.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 116,500.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 2,270.00 USD | 26,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 748.70 USD | 26,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 13,570.00 USD | 26,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 3,530.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 6,600.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,310.00 USD | 26,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,650.00 USD | 26,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,670.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 74,090.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,680.00 USD | 26,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 35,930.00 USD | 26,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 422,720.00 USD | 26,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 1,970.00 USD | 25,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570,000.00 USD | 25,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,110.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 203,420.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 282,760.00 USD | 23,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,540.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,990.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 13,230.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 5,740.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 19,070.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 140,910.00 USD | 23,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 4,450.00 USD | 23,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,780.00 USD | 23,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 1,550.00 USD | 23,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 18,360.00 USD | 23,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 6,380.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 10,920.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 412,400.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 8,730.00 USD | 22,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 860.82 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 2,330,000.00 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 69,910.00 USD | 20,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 3,950.00 USD | 20,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 4,200.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 24,310.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 9,840.00 USD | 20,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 20,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,680.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 375.84 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,860.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,300.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 132,990.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 19,350.00 USD | 20,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 38,030.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 3,350.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 42,880.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 154.83 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 3,880.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 1,360.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 214,990.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 10,470.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 14,230.00 USD | 19,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 7,890.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,760.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 367,060.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,550.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 8,140.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 929.20 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 7,370.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,780.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 213,920.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 85,170.00 USD | 19,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 3,960.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 155,560.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 1,010.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 166,480.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 15,880.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 180,710.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 387.15 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 375,800.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 11,290.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 20,840.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 8,140.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 106,550.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 28,140.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 13,160.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 4,930.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 45,890.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 22,050.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,330.00 USD | 17,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 38,380.00 USD | 17,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 5,540.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 214,120.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 83,740.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 7,320.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 7,310.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 134,880.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 20,150.00 USD | 17,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 27,070.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 71,220.00 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 17,490.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 58,930.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 37,970.00 USD | 17,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 836,670.00 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 2,680.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 134,710.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 138,120.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 22,780.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 32,280.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 63,800.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 577,220.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 3,860.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 2,020.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 36,990.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,450.00 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 5,390.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 76,100.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 190,450.00 USD | 15,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 93,990.00 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 28,770.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 2,340.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,550.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 6,650.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 112,700.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 687,230.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 1,280,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 24,560.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 37,050.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 251,330.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 79,900.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 460,870.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 368,760.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 5,440.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 37,650.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 39,740.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 25,250.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 154,780.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 42,940.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 11,830,000.00 USD | 11,830,000.00 USD | 147,810.00 USD | 44,040.00 USD | 165,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 13,470.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 11,480,000.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 20,820.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 11,420,000.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 72,880.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 11,280,000.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 45,600.00 USD | 11,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 6,480,000.00 USD | 6,480,000.00 USD | 620.25 USD | 0.00 USD | 18.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 11,190,000.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 218,940.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 6,480,000.00 USD | 6,480,000.00 USD | 16,560.00 USD | 3,070.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 11,020,000.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 622,270.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 130,530.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 6,450,000.00 USD | 6,450,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,900,000.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 188,240.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 6,430,000.00 USD | 6,430,000.00 USD | 39,190.00 USD | 0.00 USD | 55,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,820,000.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 47,380.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 6,330,000.00 USD | 6,330,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,680,000.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 40,480.00 USD | 9,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 6,330,000.00 USD | 6,330,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 10,550,000.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 37,230.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 6,330,000.00 USD | 6,330,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 10,550,000.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 21,540.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 6,310,000.00 USD | 6,310,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 10,440,000.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 58,120.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 10,150,000.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 78,040.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 10,080,000.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 54,900.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 6,110,000.00 USD | 6,110,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 10,020,000.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 11,510.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 6,100,000.00 USD | 6,100,000.00 USD | 106.91 USD | 6,570.00 USD | 29,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,970,000.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 81,910.00 USD | 9,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 176.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,900,000.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 129,010.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 6,060,000.00 USD | 6,060,000.00 USD | 3,940.00 USD | 0.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,810,000.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 136,040.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 6,060,000.00 USD | 6,060,000.00 USD | 53,860.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 18,470.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,770,000.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 35,730.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,980,000.00 USD | 5,980,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 163,840.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,720,000.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 67,130.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,940,000.00 USD | 5,940,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 16,580.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 5,930,000.00 USD | 5,930,000.00 USD | 1,450.00 USD | 12,320.00 USD | 54,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,720,000.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 160,010.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 5,860,000.00 USD | 5,860,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,640,000.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 19,300.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 5,850,000.00 USD | 5,850,000.00 USD | 106,100.00 USD | 6,860.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,550,000.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 173,540.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 5,700,000.00 USD | 5,700,000.00 USD | 112,840.00 USD | 37,150.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,340,000.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 96,380.00 USD | 8,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 5,520,000.00 USD | 5,520,000.00 USD | 1,400.00 USD | 10,910.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 9,280,000.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 2,130.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 35,760.00 USD | 39,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 9,030,000.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,950,000.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 5,410,000.00 USD | 5,410,000.00 USD | 148,140.00 USD | 26,030.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,960,000.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 372,020.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 21,500.00 USD | 38,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,730,000.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 127,720.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 5,150,000.00 USD | 5,150,000.00 USD | 64,710.00 USD | 14,940.00 USD | 20,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,640,000.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 687,490.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 5,050,000.00 USD | 5,050,000.00 USD | 95,940.00 USD | 5,610.00 USD | 95,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 8,430,000.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 38,270.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 4,850,000.00 USD | 4,850,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 8,400,000.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 246,650.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 4,710,000.00 USD | 4,710,000.00 USD | 190,720.00 USD | 66,010.00 USD | 102,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,910,000.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 505,940.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 4,350,000.00 USD | 4,350,000.00 USD | 132,570.00 USD | 43,880.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 7,300,000.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 152,750.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 4,160,000.00 USD | 4,160,000.00 USD | 349,680.00 USD | 106,190.00 USD | 138,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,630,000.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 234,780.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 3,560,000.00 USD | 3,560,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 6,380,000.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 61,540.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 3,340,000.00 USD | 3,340,000.00 USD | 112,570.00 USD | 56,050.00 USD | 129,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,770,000.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 39,230.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 3,040,000.00 USD | 3,040,000.00 USD | 180,340.00 USD | 50,310.00 USD | 107,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,850,000.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 375,020.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 2,700,000.00 USD | 2,700,000.00 USD | 189,730.00 USD | 55,650.00 USD | 266,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 4,230,000.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 23,890.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 2,190,000.00 USD | 2,190,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,780,000.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 107,490.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 1,830,000.00 USD | 1,830,000.00 USD | 136,520.00 USD | 46,690.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 2,900,000.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 91,310.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 1,550,000.00 USD | 1,550,000.00 USD | 258,250.00 USD | 27,150.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 2,410,000.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 549,980.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 1,140,000.00 USD | 1,140,000.00 USD | 175,040.00 USD | 72,110.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 1,840,000.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 138,060.00 USD | 938,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 868,990.00 USD | 868,990.00 USD | 506,300.00 USD | 253,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 575,150.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 17,870.00 USD | 800,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 109,630.00 USD | 109,630.00 USD | 10,540.00 USD | 99,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 218,520.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 692,300.00 USD | 782,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.10` | 143,210.00 USD | 143,210.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 286,420.00 USD | 286,420.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 55,720.00 USD | 89,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.11` | 59,250.00 USD | 59,250.00 USD | 0.00 USD | 59,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.11` | 118,490.00 USD | 118,490.00 USD | 0.00 USD | 59,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 231.67 USD | 34,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.12` | 428,160.00 USD | 428,160.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.13` | 589,600.00 USD | 589,600.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 33,970.00 USD | 33,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.17` | 642,110.00 USD | 642,110.00 USD | 0.00 USD | 0.00 USD | 52,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.18` | 788,630.00 USD | 788,630.00 USD | 129,470.00 USD | 17,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.18` | 2,010.00 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.19` | 1,150,000.00 USD | 1,150,000.00 USD | 174,270.00 USD | 0.00 USD | 185,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.21` | 1,230,000.00 USD | 1,230,000.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.22` | 1,400,000.00 USD | 1,400,000.00 USD | 67,980.00 USD | 27,150.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.23` | 2,040,000.00 USD | 2,040,000.00 USD | 171,410.00 USD | 468,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,720,000.00 USD | 2,720,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.25` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 64,520.00 USD | 255,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 3,270,000.00 USD | 3,270,000.00 USD | 59,900.00 USD | 177,500.00 USD | 248.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.27` | 4,130,000.00 USD | 4,130,000.00 USD | 677,660.00 USD | 24,620.00 USD | 152,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,760,000.00 USD | 4,760,000.00 USD | 313,700.00 USD | 30,410.00 USD | 288,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.29` | 5,110,000.00 USD | 5,110,000.00 USD | 152,480.00 USD | 32,690.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.30` | 5,350,000.00 USD | 5,350,000.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,760,000.00 USD | 5,760,000.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.32` | 5,920,000.00 USD | 5,920,000.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,360,000.00 USD | 6,360,000.00 USD | 255,140.00 USD | 93,880.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 6,890,000.00 USD | 6,890,000.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.35` | 6,970,000.00 USD | 6,970,000.00 USD | 422.41 USD | 0.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,360.00 USD | 5,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,100,000.00 USD | 7,100,000.00 USD | 84,400.00 USD | 12,310.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.37` | 47,330.00 USD | 52,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.37` | 7,330,000.00 USD | 7,330,000.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 367.06 USD | 53,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 8,170,000.00 USD | 8,170,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 3,610.00 USD | 56,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.39` | 8,500,000.00 USD | 8,500,000.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 905.81 USD | 57,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 8,900,000.00 USD | 8,900,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,790.00 USD | 59,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 9,280,000.00 USD | 9,280,000.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 309,400.00 USD | 368,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 9,730.00 USD | 378,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 9,480,000.00 USD | 9,480,000.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 799.63 USD | 379,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 10,260,000.00 USD | 10,260,000.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 6,320.00 USD | 385,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 10,320,000.00 USD | 10,320,000.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 10,330,000.00 USD | 10,330,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 386,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 16,700.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 8,430.00 USD | 394,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 10,580,000.00 USD | 10,580,000.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 11,140,000.00 USD | 11,140,000.00 USD | 252,410.00 USD | 155,000.00 USD | 150,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 17,170.00 USD | 411,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 11,680,000.00 USD | 11,680,000.00 USD | 361,560.00 USD | 65,710.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 18,080.00 USD | 429,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 12,490,000.00 USD | 12,490,000.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 47,410.00 USD | 477,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 13,110,000.00 USD | 13,110,000.00 USD | 287,830.00 USD | 88,150.00 USD | 242,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,100.00 USD | 495,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 13,880,000.00 USD | 13,880,000.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 14,590,000.00 USD | 14,590,000.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 495,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 15,210,000.00 USD | 15,210,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 15,530,000.00 USD | 15,530,000.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 16,980,000.00 USD | 16,980,000.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 17,960,000.00 USD | 17,960,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,170,000.00 USD | 18,170,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 496,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,300,000.00 USD | 18,300,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,450,000.00 USD | 18,450,000.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 41,900.00 USD | 538,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,450,000.00 USD | 18,450,000.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 493.16 USD | 538,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 18,860,000.00 USD | 18,860,000.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 116.59 USD | 539,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 19,940,000.00 USD | 19,940,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.66` | 20,920,000.00 USD | 20,920,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,390.00 USD | 663,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 21,480,000.00 USD | 21,480,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 22,080,000.00 USD | 22,080,000.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 22,590,000.00 USD | 22,590,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.70` | 22,930,000.00 USD | 22,930,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 1,940.00 USD | 665,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 23,900,000.00 USD | 23,900,000.00 USD | 365,580.00 USD | 284,360.00 USD | 316,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 24,190,000.00 USD | 24,190,000.00 USD | 5,440.00 USD | 187,480.00 USD | 103,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.73` | 24,310,000.00 USD | 24,310,000.00 USD | 52,120.00 USD | 0.00 USD | 60,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 335.95 USD | 665,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 154,870.00 USD | 820,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 85,580.00 USD | 906,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,050.00 USD | 913,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,530.00 USD | 917,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 6,460.00 USD | 924,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 473,730.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 4,530.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 16,630.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 15,160.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 140,840.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 556.67 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 210,290.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,160.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 55,570.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 60,790,000.00 USD | 60,790,000.00 USD | 358,750.00 USD | 137,080.00 USD | 673,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 61,310,000.00 USD | 61,310,000.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 4,130.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 61,860,000.00 USD | 61,860,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 62,240,000.00 USD | 62,240,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 62,830,000.00 USD | 62,830,000.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 63,400,000.00 USD | 63,400,000.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 63,970,000.00 USD | 63,970,000.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,080.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 64,410,000.00 USD | 64,410,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.14` | 82,200.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.15` | 64,960,000.00 USD | 64,960,000.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 65,480,000.00 USD | 65,480,000.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 317.65 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 66,150,000.00 USD | 66,150,000.00 USD | 280,710.00 USD | 85,040.00 USD | 309,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 3,620.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.18` | 66,410,000.00 USD | 66,410,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 66,630,000.00 USD | 66,630,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.20` | 66,880,000.00 USD | 66,880,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.21` | 67,120,000.00 USD | 67,120,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.22` | 67,180,000.00 USD | 67,180,000.00 USD | 52,130.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 67,230,000.00 USD | 67,230,000.00 USD | 0.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.24` | 21,060.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 544.38 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 257.38 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 114.37 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 1,140.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 29,250.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 19,710.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 25,310.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 41,910.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 60,180.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.39` | 20,300.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 35,680.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 1,050.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 627.98 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 77,760.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 1,380.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 64,190.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 6,190.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 300,420.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.64` | 56,450.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 942.09 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 334.26 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 66,300.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 2,010.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 2,700.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 55,580.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 128.37 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 199.31 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 271,610.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.96` | 486.74 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 1,830.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 24,380.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.17` | 1,910.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.17` | 308.75 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 1,540.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 1,270.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 369,650.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 41,340.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 47,710.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 2,560.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 831.97 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 1,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.55` | 1,930.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 87,890.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 51,780.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 13,340.00 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 803.13 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 35,590.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 10,770.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 15,540.00 USD | 7,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 789,370.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.74` | 5,130.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,690.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,960.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.89` | 68,950.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.91` | 189.89 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 2,420,000.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.95` | 38,370.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.00` | 1,160.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.04` | 558.67 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 670.95 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.22` | 63,550.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.29` | 1,370,000.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 90,250.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 16,640.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 14,890.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 107,860.00 USD | 13,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 10,030,000.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.57` | 7,860,000.00 USD | 31,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 2,630.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 491.45 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 161.45 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 327,090.00 USD | 31,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.78` | 72,540.00 USD | 31,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 2,920.00 USD | 31,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.80` | 32,560.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 1,800.00 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 31,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 31,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.14` | 983.92 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.15` | 190.01 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.18` | 362.97 USD | 32,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 32,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.23` | 24,700.00 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 21,470.00 USD | 32,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.27` | 87,280.00 USD | 32,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8150` | 29,440,000.00 USD | 0.00 USD | 1,600.00 USD | `-80.15%` | `1,966.20` |
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
| `7D` | `3.62` | 11,830,000.00 USD | 0.00 USD | 11,830,000.00 USD | 147,810.00 USD | 44,040.00 USD | 165,880.00 USD |
| `1D` | `3.63` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,710.00 USD |
| `7D` | `3.63` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `1D` | `3.64` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 152.80 USD | 5,040.00 USD | 4.94 USD |
| `7D` | `3.64` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD |
| `1D` | `3.65` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 386.30 USD | 0.00 USD | 77.58 USD |
| `7D` | `3.65` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD |
| `1D` | `3.66` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 291.38 USD | 0.00 USD | 6.38 USD |
| `7D` | `3.66` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD |
| `1D` | `3.67` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,440.00 USD |
| `7D` | `3.67` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD |
| `1D` | `3.68` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 271.33 USD |
| `1D` | `3.69` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 23,960.00 USD | 0.00 USD | 9.86 USD |
| `7D` | `3.69` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `1D` | `3.70` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 39,190.00 USD | 0.00 USD | 55,000.00 USD |
| `7D` | `3.70` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `1D` | `3.71` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 430.40 USD | 0.00 USD | 6.22 USD |
| `7D` | `3.71` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD |
| `1D` | `3.72` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD |
| `7D` | `3.72` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.73` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,660.00 USD |
| `7D` | `3.73` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 94,200.00 USD | 33,110.00 USD | 43,040.00 USD |
| `7D` | `3.74` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD |
| `1D` | `3.75` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3.75` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD |
| `1D` | `3.76` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD |
| `7D` | `3.76` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `1D` | `3.77` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 187.12 USD | 5,330.00 USD | 1,990.00 USD |
| `7D` | `3.77` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD |
| `1D` | `3.78` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 106.91 USD | 4,490.00 USD | 29,160.00 USD |
| `7D` | `3.78` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 472.79 USD | 0.00 USD | 231.52 USD |
| `7D` | `3.79` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD |
| `1D` | `3.80` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.80` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD |
| `1D` | `3.81` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 54,290.00 USD | 0.00 USD | 13,250.00 USD |
| `7D` | `3.81` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD |
| `1D` | `3.82` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 11,960.00 USD | 583.30 USD |
| `7D` | `3.82` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 1,150.00 USD | 18,900.00 USD | 18,440.00 USD |
| `7D` | `3.83` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD |
| `7D` | `3.84` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.85` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD |
| `7D` | `3.85` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `3.86` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,740.00 USD |
| `7D` | `3.86` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 1,690.00 USD | 11,800.00 USD | 743.88 USD |
| `7D` | `3.87` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD |
| `1D` | `3.88` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 106,680.00 USD | 6,860.00 USD | 41,580.00 USD |
| `7D` | `3.88` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 112,840.00 USD | 37,150.00 USD | 23,890.00 USD |
| `7D` | `3.89` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD |
| `1D` | `3.90` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 31,410.00 USD | 10,910.00 USD | 20,820.00 USD |
| `7D` | `3.90` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD |
| `1D` | `3.91` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 32,140.00 USD | 35,760.00 USD | 38,020.00 USD |
| `7D` | `3.91` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 148,140.00 USD | 26,030.00 USD | 31,900.00 USD |
| `7D` | `3.92` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD |
| `1D` | `3.93` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 29,900.00 USD | 39,260.00 USD |
| `7D` | `3.93` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD |
| `1D` | `3.94` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 64,710.00 USD | 14,940.00 USD | 17,980.00 USD |
| `7D` | `3.94` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD |
| `1D` | `3.95` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 95,940.00 USD | 5,610.00 USD | 97,310.00 USD |
| `7D` | `3.95` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD |
| `1D` | `3.96` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,950.00 USD |
| `7D` | `3.96` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD |
| `1D` | `3.97` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 190,720.00 USD | 66,010.00 USD | 105,360.00 USD |
| `7D` | `3.97` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD |
| `1D` | `3.98` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,820.00 USD |
| `7D` | `3.98` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD |
| `1D` | `3.99` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 413,960.00 USD | 106,190.00 USD | 136,510.00 USD |
| `7D` | `3.99` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD |
| `1D` | `4.00` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,480.00 USD |
| `7D` | `4.00` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 112,570.00 USD | 72,850.00 USD | 126,200.00 USD |
| `7D` | `4.01` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD |
| `1D` | `4.02` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 180,340.00 USD | 50,310.00 USD | 108,730.00 USD |
| `7D` | `4.02` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD |
| `1D` | `4.03` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 189,730.00 USD | 55,650.00 USD | 267,230.00 USD |
| `7D` | `4.03` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD |
| `1D` | `4.04` | 759,140.00 USD | 0.00 USD | 759,140.00 USD | 105,670.00 USD | 48,960.00 USD | 211,380.00 USD |
| `7D` | `4.04` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD |
| `1D` | `4.05` | 393,130.00 USD | 0.00 USD | 393,130.00 USD | 2,370.00 USD | 46,690.00 USD | 95,770.00 USD |
| `7D` | `4.05` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD |
| `1D` | `4.06` | 248,290.00 USD | 0.00 USD | 248,290.00 USD | 0.00 USD | 27,150.00 USD | 126,130.00 USD |
| `7D` | `4.06` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD |
| `1D` | `4.07` | 95,010.00 USD | 0.00 USD | 95,010.00 USD | 0.00 USD | 72,110.00 USD | 22,900.00 USD |
| `7D` | `4.07` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD |
| `1D` | `4.08` | 506,800.00 USD | 506,800.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 506.63 USD |
| `1D` | `4.08` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 506.63 USD |
| `7D` | `4.08` | 575,150.00 USD | 0.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `7D` | `4.09` | 218,520.00 USD | 0.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD |
| `1D` | `4.10` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 509.39 USD |
| `7D` | `4.10` | 143,210.00 USD | 143,210.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `7D` | `4.10` | 286,420.00 USD | 286,420.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `1D` | `4.11` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 59,250.00 USD | 1,270.00 USD |
| `1D` | `4.12` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 80,980.00 USD | 228,820.00 USD |
| `1D` | `4.13` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD |
| `1D` | `4.14` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD |
| `1D` | `4.15` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD |
| `1D` | `4.17` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD |
| `1D` | `4.18` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 129,470.00 USD | 17,040.00 USD | 0.00 USD |
| `1D` | `4.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 174,270.00 USD | 0.00 USD | 185,170.00 USD |
| `7D` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD |
| `1D` | `4.22` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD |
| `1D` | `4.23` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD |
| `1D` | `4.24` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD |
| `1D` | `4.25` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD |
| `7D` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD |
| `1D` | `4.26` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 60,530.00 USD | 173,320.00 USD | 0.00 USD |
| `7D` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 677,660.00 USD | 24,620.00 USD | 152,190.00 USD |
| `7D` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 314,270.00 USD | 30,410.00 USD | 288,520.00 USD |
| `7D` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD |
| `1D` | `4.29` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 152,480.00 USD | 32,690.00 USD | 161,990.00 USD |
| `7D` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 32,410.00 USD | 45,120.00 USD | 163,260.00 USD |
| `7D` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 304,920.00 USD | 13,580.00 USD | 94,870.00 USD |
| `7D` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 86,850.00 USD | 73,400.00 USD | 19.74 USD |
| `7D` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD |
| `1D` | `4.33` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 255,620.00 USD | 93,880.00 USD | 87,020.00 USD |
| `7D` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 270,720.00 USD | 140,540.00 USD | 114,780.00 USD |
| `7D` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD |
| `1D` | `4.35` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 855.62 USD | 0.00 USD | 85,420.00 USD |
| `7D` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 84,400.00 USD | 12,310.00 USD | 31,180.00 USD |
| `7D` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD |
| `1D` | `4.37` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 52,520.00 USD | 46,860.00 USD | 131,580.00 USD |
| `1D` | `4.38` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 248,590.00 USD | 34,500.00 USD | 559,190.00 USD |
| `7D` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 399.48 USD | 17,360.00 USD | 310,770.00 USD |
| `7D` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD |
| `1D` | `4.40` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 288,790.00 USD | 34,040.00 USD | 81,080.00 USD |
| `7D` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD |
| `1D` | `4.41` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 196,820.00 USD | 112,990.00 USD | 63,590.00 USD |
| `7D` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 47,240.00 USD | 1,320.00 USD |
| `7D` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 5,100.00 USD | 49,400.00 USD | 95,230.00 USD |
| `7D` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD |
| `1D` | `4.44` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 292,720.00 USD |
| `7D` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD |
| `1D` | `4.45` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 649.63 USD | 50,720.00 USD | 1,760.00 USD |
| `1D` | `4.46` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 704.30 USD | 9,070.00 USD | 3,140.00 USD |
| `7D` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD |
| `1D` | `4.47` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 210.23 USD | 16,700.00 USD | 18,240.00 USD |
| `7D` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 117,480.00 USD | 73,240.00 USD | 25,450.00 USD |
| `7D` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `4.49` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 252,600.00 USD | 155,000.00 USD | 150,370.00 USD |
| `7D` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 361,560.00 USD | 65,710.00 USD | 118,110.00 USD |
| `7D` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD |
| `1D` | `4.51` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 186,860.00 USD | 307,580.00 USD | 312,490.00 USD |
| `7D` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.52` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 287,830.00 USD | 88,150.00 USD | 242,940.00 USD |
| `7D` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 487,540.00 USD | 0.00 USD | 281,090.00 USD |
| `7D` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD |
| `1D` | `4.54` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD |
| `7D` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 196,080.00 USD |
| `1D` | `4.56` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD |
| `7D` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 67,910.00 USD |
| `7D` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD |
| `1D` | `4.58` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 506,750.00 USD | 73,690.00 USD | 876,090.00 USD |
| `7D` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 19,130,000.00 USD | 19,130,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 79,670.00 USD |
| `7D` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 19,340,000.00 USD | 19,340,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 67,260.00 USD |
| `7D` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 60,890.00 USD |
| `7D` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD |
| `7D` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `4.63` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 335.46 USD |
| `7D` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 334,190.00 USD | 11,270.00 USD | 61,860.00 USD |
| `7D` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD |
| `1D` | `4.65` | 21,100,000.00 USD | 21,100,000.00 USD | 0.00 USD | 423,550.00 USD | 52,020.00 USD | 600,630.00 USD |
| `7D` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `4.66` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 281,290.00 USD | 316,500.00 USD | 379,970.00 USD |
| `7D` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 22,640,000.00 USD | 22,640,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 377,750.00 USD |
| `7D` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 23,250,000.00 USD | 23,250,000.00 USD | 0.00 USD | 345,840.00 USD | 81,340.00 USD | 177,210.00 USD |
| `7D` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 23,750,000.00 USD | 23,750,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 254,450.00 USD |
| `7D` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD |
| `7D` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 25,060,000.00 USD | 25,060,000.00 USD | 0.00 USD | 365,580.00 USD | 284,360.00 USD | 316,400.00 USD |
| `7D` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `1D` | `4.72` | 25,360,000.00 USD | 25,360,000.00 USD | 0.00 USD | 5,440.00 USD | 187,480.00 USD | 103,550.00 USD |
| `7D` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 25,510,000.00 USD | 25,510,000.00 USD | 0.00 USD | 52,120.00 USD | 37,010.00 USD | 60,650.00 USD |
| `7D` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD |
| `7D` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `7D` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `7D` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `7D` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `7D` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 0.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD |
| `7D` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `7D` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `7D` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `7D` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `7D` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 0.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD |
| `7D` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `7D` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `7D` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `7D` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `7D` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `7D` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD |
| `7D` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `7D` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `7D` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `7D` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 0.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD |
| `7D` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `7D` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `7D` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 0.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD |
| `7D` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 0.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD |
| `7D` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD |
| `7D` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 0.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD |
| `7D` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 0.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD |
| `7D` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 0.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 60,790,000.00 USD | 60,790,000.00 USD | 0.00 USD | 358,750.00 USD | 137,080.00 USD | 673,800.00 USD |
| `7D` | `5.08` | 61,310,000.00 USD | 61,310,000.00 USD | 0.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD |
| `7D` | `5.09` | 61,860,000.00 USD | 61,860,000.00 USD | 0.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD |
| `7D` | `5.10` | 62,240,000.00 USD | 62,240,000.00 USD | 0.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 62,830,000.00 USD | 62,830,000.00 USD | 0.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD |
| `7D` | `5.12` | 63,400,000.00 USD | 63,400,000.00 USD | 0.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 63,970,000.00 USD | 63,970,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD |
| `7D` | `5.14` | 64,410,000.00 USD | 64,410,000.00 USD | 0.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD |
| `7D` | `5.15` | 64,960,000.00 USD | 64,960,000.00 USD | 0.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD |
| `7D` | `5.16` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 66,150,000.00 USD | 66,150,000.00 USD | 0.00 USD | 280,710.00 USD | 85,040.00 USD | 309,950.00 USD |
| `7D` | `5.18` | 66,410,000.00 USD | 66,410,000.00 USD | 0.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD |
| `7D` | `5.19` | 66,630,000.00 USD | 66,630,000.00 USD | 0.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD |
| `7D` | `5.20` | 66,880,000.00 USD | 66,880,000.00 USD | 0.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD |
| `7D` | `5.21` | 67,120,000.00 USD | 67,120,000.00 USD | 0.00 USD | 105,330.00 USD | 20,850.00 USD | 110,520.00 USD |
| `7D` | `5.22` | 67,180,000.00 USD | 67,180,000.00 USD | 0.00 USD | 52,130.00 USD | 13,410.00 USD | 398.26 USD |
| `7D` | `5.23` | 67,230,000.00 USD | 67,230,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 34,400.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `276,967,452.8 NEAR`
  * 1h OI Change: `-1.04%` | 4h OI Change: `-9.54%` | 24h OI Change: `-15.70%`
  * Exchange Breakdown: Binance=`213.98M` | Bybit=`149.28M` | OKX=`48.62M` | Hyperliquid=`224.40M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.99K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0014%` | **USDT OKX** | `0.0056%` |
| **USDT Bybit** | `-0.0023%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0012%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0058%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `38.04%` | `61.96%` | `0.61` | 11,750,000.00 USD |
| `15M` | `Binance` | `47.26%` | `52.74%` | `0.90` | 4,060,000.00 USD |
| `15M` | `OKX` | `38.67%` | `61.33%` | `0.63` | 1,490,000.00 USD |
| `15M` | `Bybit` | `31.42%` | `68.58%` | `0.46` | 1,490,000.00 USD |
| `15M` | `KuCoin` | `34.49%` | `65.51%` | `0.53` | 213,070.00 USD |
| `15M` | `Gate` | `14.37%` | `85.63%` | `0.17` | 1,080,000.00 USD |
| `15M` | `Bitget` | `45.78%` | `54.22%` | `0.84` | 575,480.00 USD |
| `15M` | `BingX` | `17.35%` | `82.65%` | `0.21` | 715,990.00 USD |
| `15M` | `MEXC` | `42.65%` | `57.35%` | `0.74` | 991,100.00 USD |
| `15M` | `Bitunix` | `56.52%` | `43.48%` | `1.30` | 298,690.00 USD |
| `15M` | `Hyperliquid` | `74.21%` | `25.79%` | `2.88` | 185,640.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `36.51%` | `63.49%` | `0.58` | 139,410.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `15.43%` | `84.57%` | `0.18` | 398,030.00 USD |
| `15M` | `HTX` | `66.06%` | `33.94%` | `1.95` | 16,850.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.27%` | `49.73%` | `1.01` | 43,900.00 USD |
| `15M` | `Aster` | `28.26%` | `71.74%` | `0.39` | 35,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `37.29%` | `62.71%` | `0.59` | 10,200.00 USD |
| `15M` | `Whale Positions` | `47.26%` | `52.74%` | `0.90` | 4,060,000.00 USD |
| `15M` | `Global Accounts` | `38.04%` | `61.96%` | `0.61` | 11,750,000.00 USD |
| `1H` | `NEAR` | `47.75%` | `52.25%` | `0.91` | 131,880,000.00 USD |
| `1H` | `Binance` | `50.91%` | `49.09%` | `1.04` | 53,660,000.00 USD |
| `1H` | `OKX` | `53.98%` | `46.02%` | `1.17` | 10,410,000.00 USD |
| `1H` | `Bybit` | `44.69%` | `55.31%` | `0.81` | 12,840,000.00 USD |
| `1H` | `KuCoin` | `42.04%` | `57.96%` | `0.73` | 554,460.00 USD |
| `1H` | `Gate` | `34.48%` | `65.52%` | `0.53` | 3,080,000.00 USD |
| `1H` | `Bitget` | `57.2%` | `42.8%` | `1.34` | 5,220,000.00 USD |
| `1H` | `BingX` | `37.01%` | `62.99%` | `0.59` | 2,020,000.00 USD |
| `1H` | `MEXC` | `41.01%` | `58.99%` | `0.70` | 22,830,000.00 USD |
| `1H` | `Bitunix` | `53.42%` | `46.58%` | `1.15` | 4,450,000.00 USD |
| `1H` | `Hyperliquid` | `54.48%` | `45.52%` | `1.20` | 9,470,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.9%` | `51.1%` | `0.96` | 2,980,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `12.81%` | `87.19%` | `0.15` | 2,020,000.00 USD |
| `1H` | `HTX` | `36.39%` | `63.61%` | `0.57` | 25,760.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.03%` | `55.97%` | `0.79` | 1,030,000.00 USD |
| `1H` | `Aster` | `60.76%` | `39.24%` | `1.55` | 388,360.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.02%` | `54.98%` | `0.82` | 878,800.00 USD |
| `1H` | `Whale Positions` | `50.91%` | `49.09%` | `1.04` | 53,660,000.00 USD |
| `1H` | `Global Accounts` | `47.75%` | `52.25%` | `0.91` | 131,880,000.00 USD |
| `4H` | `NEAR` | `46.01%` | `53.99%` | `0.85` | 334,260,000.00 USD |
| `4H` | `Binance` | `47.44%` | `52.56%` | `0.90` | 133,970,000.00 USD |
| `4H` | `OKX` | `49.73%` | `50.27%` | `0.99` | 45,690,000.00 USD |
| `4H` | `Bybit` | `45.4%` | `54.6%` | `0.83` | 45,260,000.00 USD |
| `4H` | `KuCoin` | `43.53%` | `56.47%` | `0.77` | 3,680,000.00 USD |
| `4H` | `Gate` | `43.77%` | `56.23%` | `0.78` | 7,850,000.00 USD |
| `4H` | `Bitget` | `46.94%` | `53.06%` | `0.88` | 20,810,000.00 USD |
| `4H` | `BingX` | `41.61%` | `58.39%` | `0.71` | 9,850,000.00 USD |
| `4H` | `MEXC` | `43.02%` | `56.98%` | `0.76` | 28,850,000.00 USD |
| `4H` | `Bitunix` | `45.15%` | `54.85%` | `0.82` | 13,160,000.00 USD |
| `4H` | `Hyperliquid` | `42.58%` | `57.42%` | `0.74` | 11,710,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `42.24%` | `57.76%` | `0.73` | 2,800,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `25.45%` | `74.55%` | `0.34` | 5,620,000.00 USD |
| `4H` | `HTX` | `48.32%` | `51.68%` | `0.93` | 707,650.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.32%` | `60.68%` | `0.65` | 2,440,000.00 USD |
| `4H` | `Aster` | `42.92%` | `57.08%` | `0.75` | 1,450,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.41%` | `52.59%` | `0.90` | 428,020.00 USD |
| `4H` | `Whale Positions` | `47.44%` | `52.56%` | `0.90` | 133,970,000.00 USD |
| `4H` | `Global Accounts` | `46.01%` | `53.99%` | `0.85` | 334,260,000.00 USD |


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
| `0:00 UTC` | `4.08` | `4.09` | `4.08` | `4.11` | `4.08` | 1,838,731.84 USD | 812,485.80 USD | 1,026,246.04 USD | -213,760.23 USD | `-11.63%` | `4B / 10S` |

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
| `5m` | -732,820.00 USD | -2,410,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -846,000.00 USD | -2,850,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,530,000.00 USD | -5,220,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,720,000.00 USD | -5,680,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,580,000.00 USD | -2,450,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -9,680,000.00 USD | -15,160,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -14,050,000.00 USD | -20,540,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -16,060,000.00 USD | -26,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -16,270,000.00 USD | -31,810,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -27,250,000.00 USD | -74,570,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -80,190,000.00 USD | -121,380,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -248,680,000.00 USD | -682,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-732.82K` | 15m=`-846.00K` | 1h=`-3.72M` | 24h=`-27.25M`
* Futures Capital Netflows: 5m=`-2.41M` | 15m=`-2.85M` | 1h=`-5.68M` | 24h=`-74.57M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.06` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2.82` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `7.17`
  * Mathematical Lot Sizing: **`8.04 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.17` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `5.41` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `1.06`
  * Mathematical Lot Sizing: **`8.04 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.10`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
