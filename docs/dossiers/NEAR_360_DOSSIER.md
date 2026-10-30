# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:27:43 IST` (`2026-10-30 10:57:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.33` | **Live Ask Quote**: `4.36` | **Mid Price**: `4.35`
- **Spread Points**: `29.00` | **Spread BPS**: `66.71 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.35` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.38` | Lower -3.00σ Band: `4.32`
  * Upper +2.51σ Band: `4.37` | Lower -2.51σ Band: `4.32`
  * Upper +2.01σ Band: `4.37` | Lower -2.01σ Band: `4.33`
  * Upper +2.00σ Band: `4.36` | Lower -2.00σ Band: `4.33`
  * Upper +1.28σ Band: `4.36` | Lower -1.28σ Band: `4.34`
  * Upper +1.00σ Band: `4.36` | Lower -1.00σ Band: `4.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.35` | EMA-20=`4.35` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.35` (Slope: `+0.0000`) | EMA-100=`4.35`
  * Institutional Anchors: EMA-144=`4.35` | EMA-200=`4.35` (Slope: `+0.0000`) | EMA-233=`4.35`
- **Range Boundaries**: 24H High=`4.39` | 24H Low=`4.30` | Weekly High=`4.43` | Weekly Low=`4.26`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.24` (Distance: `+2.67%`)
  * Point of Control (POC) = `4.07` (Distance: `+7.07%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+10.57%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.71` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.37` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.36` | Low=`4.30`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.33` - `4.36`
  * Optimal Trade Entry (OTE 0.705): `4.36`
  * Structural Invalidation Anchor (0.786): `4.38`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.34` | `4.35` | `4.34` | `4.35` | `651,870` | 2,832,830.53 USD | 731,291.50 USD | `+25.81%` | -6,770,918.04 USD | `+1.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.35` | `4.35` | `4.33` | `4.33` | `263,019` | 1,140,775.88 USD | -80,446.36 USD | `-7.05%` | -6,851,364.40 USD | `-0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4.33` | `4.35` | `4.33` | `4.35` | `273,882` | 1,188,281.86 USD | 485,629.42 USD | `+40.87%` | -6,365,734.98 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.33` | `4.37` | `4.32` | `4.32` | `1,582,402` | 6,865,250.12 USD | -433,944.66 USD | `-6.32%` | -7,820,591.21 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.32` | `4.35` | `4.32` | `4.35` | `1,820,116` | 7,895,783.86 USD | 2,079,303.28 USD | `+26.33%` | -5,741,287.93 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.35` | `4.35` | `4.33` | `4.35` | `537,912` | 2,333,458.62 USD | 409,583.94 USD | `+17.55%` | -5,331,703.99 USD | `-0.08` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4.25` | `4.39` | `4.24` | `4.36` | `15,226,975` | 65,865,283.41 USD | 8,809,838.63 USD | `+13.38%` | -7,440,212.42 USD | `+2.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.36` | `4.38` | `4.29` | `4.38` | `6,481,728` | 28,107,012.78 USD | 1,024,636.46 USD | `+3.65%` | -6,415,575.95 USD | `+0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `4.38` | `4.38` | `4.32` | `4.35` | `5,501,496` | 23,880,846.90 USD | 1,083,871.97 USD | `+4.54%` | -5,331,703.99 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.35` | `27,211,543` | 117,858,994.71 USD | 10,922,910.20 USD | `+9.27%` | -4,128,138.73 USD | `+1.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | 240,083.28 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -11,802,955.99 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.35` | `27,211,543` | 117,858,994.71 USD | 10,922,910.20 USD | `+9.27%` | -4,128,138.73 USD | `+1.62` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`4.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `56` | `0x7737...bf66` | `LONG` | 24,630,395.23 USD | `5,640,376.30` | `2.35` | `4.36` | `0.8452` | 11,358,492.40 USD | `+46.12%` | `10X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,664,735.56 USD | `4,507,262.50` | `4.21` | `4.36` | `6.35` | -689,638.85 USD | `-3.51%` | `5X Cross` |
| `122` | `0xb581...6f4f` | `LONG` | 15,724,080.00 USD | `3,600,000.00` | `5.19` | `4.36` | `0.000000` | -2,968,955.22 USD | `-18.88%` | `4X Cross` |
| `200` | `0xdd53...2b13` | `SHORT` | 10,476,401.69 USD | `2,400,202.00` | `2.31` | `4.36` | `28.59` | -4,930,553.13 USD | `-47.06%` | `3X Cross` |
| `248` | `0x77ee...2902` | `LONG` | 9,010,872.30 USD | `2,063,023.10` | `1.93` | `4.36` | `0.000000` | 5,019,676.36 USD | `+55.71%` | `10X Cross` |
| `339` | `0x7fda...17d1` | `SHORT` | 6,731,843.07 USD | `1,541,349.30` | `4.29` | `4.36` | `27.69` | -127,004.45 USD | `-1.89%` | `10X Cross` |
| `345` | `0x9df2...c665` | `SHORT` | 6,614,923.78 USD | `1,514,579.00` | `2.36` | `4.36` | `18.15` | -3,034,934.12 USD | `-45.88%` | `10X Cross` |
| `363` | `0xb83d...6e36` | `SHORT` | 6,314,352.87 USD | `1,445,759.10` | `5.19` | `4.36` | `73.93` | 1,195,096.07 USD | `+18.93%` | `3X Cross` |
| `381` | `0xb46b...538e` | `SHORT` | 5,831,372.80 USD | `1,336,000.00` | `4.33` | `4.36` | `7.41` | -46,508.74 USD | `-0.80%` | `10X Cross` |
| `446` | `0x60b0...991e` | `LONG` | 4,897,308.76 USD | `1,121,307.10` | `5.00` | `4.36` | `0.000000` | -704,115.67 USD | `-14.38%` | `10X Cross` |
| `488` | `0x781e...96b7` | `SHORT` | 4,538,705.76 USD | `1,039,604.60` | `2.45` | `4.36` | `7.50` | -1,994,368.57 USD | `-43.94%` | `10X Cross` |
| `557` | `0x4cae...7c34` | `LONG` | 3,978,811.64 USD | `910,587.40` | `3.98` | `4.36` | `3.04` | 357,116.36 USD | `+8.98%` | `10X Cross` |
| `559` | `0x45d2...4029` | `SHORT` | 3,969,985.70 USD | `909,400.00` | `3.26` | `4.36` | `48.45` | -1,003,835.80 USD | `-25.29%` | `10X Cross` |
| `795` | `0x005a...61fe` | `LONG` | 2,847,398.28 USD | `652,414.60` | `2.08` | `4.36` | `2.41` | 1,489,867.04 USD | `+52.32%` | `7X Cross` |
| `801` | `0xba5d...a352` | `SHORT` | 2,828,292.45 USD | `647,532.50` | `2.83` | `4.36` | `11.30` | -995,577.51 USD | `-35.20%` | `10X Cross` |
| `810` | `0xb695...a92d` | `SHORT` | 2,790,118.52 USD | `639,231.70` | `4.57` | `4.36` | `38.41` | 133,240.40 USD | `+4.78%` | `10X Cross` |
| `812` | `0xd1dd...9e85` | `SHORT` | 2,786,084.96 USD | `637,621.00` | `4.96` | `4.36` | `18.75` | 377,387.78 USD | `+13.55%` | `10X Cross` |
| `827` | `0x123d...3bff` | `SHORT` | 2,726,252.25 USD | `624,568.10` | `2.09` | `4.36` | `9.14` | -1,420,828.07 USD | `-52.12%` | `10X Cross` |
| `832` | `0xcf53...ee11` | `SHORT` | 2,715,141.81 USD | `621,598.40` | `5.07` | `4.36` | `25.05` | 437,028.44 USD | `+16.10%` | `10X Cross` |
| `954` | `0xbfc7...80b4` | `SHORT` | 2,319,992.10 USD | `531,000.00` | `2.01` | `4.36` | `7.11` | -1,254,792.71 USD | `-54.09%` | `10X Cross` |
| `1089` | `0xf382...578c` | `SHORT` | 1,986,988.88 USD | `454,948.80` | `4.32` | `4.36` | `6.37` | -23,484.37 USD | `-1.18%` | `10X Cross` |
| `1191` | `0x0eec...d4c5` | `LONG` | 1,854,819.16 USD | `424,686.70` | `4.02` | `4.36` | `2.04` | 147,529.47 USD | `+7.95%` | `10X Cross` |
| `1254` | `0xe097...d0fe` | `LONG` | 1,747,120.00 USD | `400,000.00` | `5.29` | `4.36` | `0.000000` | -369,667.30 USD | `-21.16%` | `10X Cross` |
| `1356` | `0xef96...9383` | `SHORT` | 1,581,262.86 USD | `362,433.90` | `4.50` | `4.36` | `13.71` | 49,603.15 USD | `+3.14%` | `10X Cross` |
| `1362` | `0x6e8f...4364` | `LONG` | 1,576,756.07 USD | `361,210.50` | `3.28` | `4.36` | `3.53` | 392,695.85 USD | `+24.91%` | `10X Cross` |
| `1413` | `0xcf67...eb24` | `LONG` | 1,528,625.00 USD | `350,000.00` | `1.98` | `4.36` | `1.49` | 837,007.12 USD | `+54.76%` | `10X Cross` |
| `1414` | `0xdf95...7d72` | `SHORT` | 1,528,501.91 USD | `350,220.40` | `4.23` | `4.36` | `109.88` | -46,259.23 USD | `-3.03%` | `10X Cross` |
| `1532` | `0xfc27...9d9d` | `SHORT` | 1,396,949.96 USD | `319,997.70` | `5.01` | `4.36` | `61.92` | 206,592.66 USD | `+14.79%` | `10X Cross` |
| `1541` | `0x089f...a4f8` | `LONG` | 1,392,432.58 USD | `319,043.30` | `4.06` | `4.36` | `0.000000` | 97,575.87 USD | `+7.01%` | `1X Cross` |
| `1587` | `0x17c3...a868` | `LONG` | 1,336,710.59 USD | `306,037.50` | `4.36` | `4.36` | `0.000000` | 1,557.61 USD | `+0.12%` | `3X Cross` |
| `1668` | `0xe065...0f85` | `SHORT` | 1,257,414.60 USD | `288,027.90` | `2.81` | `4.36` | `5.57` | -446,861.48 USD | `-35.54%` | `10X Cross` |
| `1872` | `0xff43...d924` | `LONG` | 1,089,654.72 USD | `249,474.50` | `4.64` | `4.36` | `3.28` | -68,388.96 USD | `-6.28%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.40` | 10,050.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.05K USD at 4.4010 USD [API] | `2026-10-29 12:09:30` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 9,012.52 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.01K USD at 4.4447 USD [API] | `2026-10-29 12:42:38` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 10.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.5165 USD [API] | `2026-10-29 13:17:08` |
| `ANNOUNCEMENT` | `INFO` | `4.47` | 5,384.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.38K USD at 4.4724 USD [API] | `2026-10-29 13:23:50` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 5,669.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.67K USD at 4.4366 USD [API] | `2026-10-29 13:34:47` |
| `ANNOUNCEMENT` | `INFO` | `4.56` | 237.36 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.24K USD at 4.5647 USD [API] | `2026-10-15 10:22:09` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 665.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.67K USD at 4.6864 USD [API] | `2026-10-02 18:08:41` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 7,080.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.08K USD at 4.4448 USD [API] | `2026-10-29 13:56:45` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 10,056.32 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.06K USD at 4.4438 USD [API] | `2026-10-29 14:09:11` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 5,685.75 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.69K USD at 4.4413 USD [API] | `2026-10-29 14:14:37` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 7,741.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.74K USD at 4.5888 USD [API] | `2026-10-29 17:02:52` |
| `ANNOUNCEMENT` | `INFO` | `4.58` | 5,821.25 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.82K USD at 4.5815 USD [API] | `2026-10-29 17:14:21` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 3,685.86 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.69K USD at 4.6876 USD [API] | `2026-10-18 14:31:48` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 661.89 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.66K USD at 5.0603 USD [API] | `2026-10-13 11:02:34` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 499.96 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 5.0603 USD [API] | `2026-10-13 11:02:34` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 10.63 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 5.0604 USD [API] | `2026-10-13 11:02:34` |
| `ANNOUNCEMENT` | `INFO` | `4.43` | 8,794.14 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.79K USD at 4.4332 USD [API] | `2026-10-29 18:35:02` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 9,970.06 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.97K USD at 4.4416 USD [API] | `2026-10-29 18:54:50` |
| `ANNOUNCEMENT` | `INFO` | `4.43` | 8,958.22 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.96K USD at 4.4260 USD [API] | `2026-10-29 19:00:12` |
| `ANNOUNCEMENT` | `INFO` | `4.39` | 1,857.76 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.86K USD at 4.3929 USD [API] | `2026-10-29 19:02:24` |
| `ANNOUNCEMENT` | `INFO` | `4.39` | 310.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.31K USD at 4.3929 USD [API] | `2026-10-29 19:02:24` |
| `ANNOUNCEMENT` | `INFO` | `4.41` | 6,024.63 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.02K USD at 4.4130 USD [API] | `2026-10-29 19:22:48` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 826.85 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.83K USD at 4.6400 USD [API] | `2026-10-29 15:33:28` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 867.22 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.87K USD at 4.6400 USD [API] | `2026-10-29 15:33:28` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 54.75 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.05K USD at 4.6400 USD [API] | `2026-10-29 15:33:28` |
| `ANNOUNCEMENT` | `INFO` | `4.39` | 17,404.42 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 17.40K USD at 4.3945 USD [API] | `2026-10-29 19:43:38` |
| `ANNOUNCEMENT` | `INFO` | `4.39` | 5,381.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.38K USD at 4.3906 USD [API] | `2026-10-29 19:44:00` |
| `ANNOUNCEMENT` | `INFO` | `4.37` | 4,961.90 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 4.96K USD at 4.3721 USD [API] | `2026-10-29 19:02:44` |
| `ANNOUNCEMENT` | `INFO` | `4.37` | 472.19 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.47K USD at 4.3721 USD [API] | `2026-10-29 19:02:44` |
| `ANNOUNCEMENT` | `INFO` | `4.37` | 121.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.12K USD at 4.3721 USD [API] | `2026-10-29 19:02:44` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 3,645.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 3.65K USD at 4.4158 USD [API] | `2026-10-29 18:35:55` |
| `ANNOUNCEMENT` | `INFO` | `4.36` | 5,896.55 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.90K USD at 4.3591 USD [API] | `2026-10-29 20:02:43` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.85%`) | Long MP=`4.26` (Vol: 910,700.00 USD, Dist: `--1.81%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.77%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.64%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.77%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.64%`)
  * 7D Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.91%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.55%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8850` | 411.70 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 22,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 22,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 2,810.00 USD | 22,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 6,620.00 USD | 22,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,450.00 USD | 22,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 22,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 3,690.00 USD | 22,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 2,560.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 22,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 34,960.00 USD | 22,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 4,330.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 5,740.00 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 18,980.00 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 1,690.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 6,930.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 26,620.00 USD | 22,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 1,730.00 USD | 22,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 2,390.00 USD | 22,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 9,630.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 4,940.00 USD | 22,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 150.90 USD | 22,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,040.00 USD | 22,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 20,460.00 USD | 22,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 15,020.00 USD | 22,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 3,370.00 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 425.59 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 379.76 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 28,340.00 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 179.96 USD | 22,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 22,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,130.00 USD | 22,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 2,200.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 12,760.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 22,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 77,850.00 USD | 22,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 4,710.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 1,130.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 2,690.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 5,440.00 USD | 22,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 13,180.00 USD | 22,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 21,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.49` | 74,750.00 USD | 21,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,920.00 USD | 21,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 2,640.00 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 6,190.00 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 20,570.00 USD | 21,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 2,630.00 USD | 21,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 1,980.00 USD | 21,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,380.00 USD | 21,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 753.39 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 3,760.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 3,420.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 617.72 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 9,620.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 603,680.00 USD | 21,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 929.23 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 5,000.00 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 8,910.00 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 105.14 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,250.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 17,220.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 2,230.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 91,410.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 529.05 USD | 21,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 21,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 21,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,840.00 USD | 21,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 1,400.00 USD | 21,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 14,720.00 USD | 21,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,750.00 USD | 21,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 39,130.00 USD | 21,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 1,120.00 USD | 21,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 21,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 2,280.00 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 37,250.00 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 856,120.00 USD | 20,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 12,900.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 398.72 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 323.36 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,640.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 39,180.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 8,860.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 13,270.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 18,600.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,100.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 10,540.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,510.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 18,310.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 2,140.00 USD | 19,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,110.00 USD | 19,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,530.00 USD | 19,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 188,810.00 USD | 19,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 93,620.00 USD | 19,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 3,530.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 12,830.00 USD | 19,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 19,420.00 USD | 19,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 25,570.00 USD | 19,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 8,450.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 21,160.00 USD | 19,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 3,020.00 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 117,220.00 USD | 19,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 2,040.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 72,840.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 5,120.00 USD | 19,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 221,220.00 USD | 19,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 12,250.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,330.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 13,770.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,670.00 USD | 19,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,100.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 26,590.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 1,580.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 35,720.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 7,680.00 USD | 19,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 115.20 USD | 19,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 183,000.00 USD | 19,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 1,870,000.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,320.00 USD | 17,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 160,000.00 USD | 17,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 281,230.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 4,590.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 12,520.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 9,240.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 15,850.00 USD | 16,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 425,370.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 346.32 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 33,330.00 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 2,440.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 670.94 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 7,890.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 2,050.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,910.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 80,250.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 2,450.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 24,310.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,950.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 27,700.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 169,690.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,600.00 USD | 15,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 7,260.00 USD | 15,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 13,910.00 USD | 15,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 164,840.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,880.00 USD | 15,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 28,380.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 1,960.00 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 458.96 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 64,490.00 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 350,290.00 USD | 15,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 398.77 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 47,860.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 12,340.00 USD | 15,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 90,180.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 4,780.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,350.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 10,910.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,790.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,540.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 18,770.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 868,330.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 8,470.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 112,920.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 4,500.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 11,820.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 245,610.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 50,370.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 18,090.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 13,510.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,380.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 148,680.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 5,270.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 11,160.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 116,780.00 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 26,540.00 USD | 13,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 26,810.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 1,220.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 141,830.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 86,530.00 USD | 13,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 130,870.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 48,380.00 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 163,550.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 25,870.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 31,050.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 11,560.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 35,950.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 22,930.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 81,350.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 181,270.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 2,860,000.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 306,920.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 112.17 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 8,790.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,110.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 64,820.00 USD | 9,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 20,190.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 4,050.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 39,060.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 869,330.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 4,080.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 133,000.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 132,030.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 24,690.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 10,380.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 77,700.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 22,160.00 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,210.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 24,110.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 54,650.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 40,370.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 41,460.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 103,060.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 390,990.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 6,570.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 29,310.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 26,840.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 151,120.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 16,150.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 116,220.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 267,390.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 48,130.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 33,810.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 42,800.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 19,410,000.00 USD | 19,410,000.00 USD | 18,870.00 USD | 0.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 21,970.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 19,350,000.00 USD | 19,350,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 77,190.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 19,120,000.00 USD | 19,120,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 159,350.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 19,030,000.00 USD | 19,030,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 570,020.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 18,800,000.00 USD | 18,800,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 7,550.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 18,740,000.00 USD | 18,740,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 1,340,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 18,540,000.00 USD | 18,540,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 52,750.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 18,260,000.00 USD | 18,260,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 23,850.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 18,240,000.00 USD | 18,240,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 63,970.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 18,130,000.00 USD | 18,130,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 102,890.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 17,990,000.00 USD | 17,990,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 114,340.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 17,770,000.00 USD | 17,770,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 1,670.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 17,720,000.00 USD | 17,720,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 333,140.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 17,550,000.00 USD | 17,550,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 20,750.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 17,460,000.00 USD | 17,460,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 171,100.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 17,290,000.00 USD | 17,290,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 95,680.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 17,170,000.00 USD | 17,170,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 224,510.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 17,170,000.00 USD | 17,170,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 93,310.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.70` | 17,080,000.00 USD | 17,080,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 79,950.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.71` | 16,940,000.00 USD | 16,940,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 11,810.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.72` | 16,810,000.00 USD | 16,810,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 224,430.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.73` | 16,810,000.00 USD | 16,810,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 119,590.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.74` | 16,700,000.00 USD | 16,700,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 25,820.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.75` | 16,410,000.00 USD | 16,410,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 150,270.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.76` | 16,220,000.00 USD | 16,220,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 65,080.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.77` | 16,160,000.00 USD | 16,160,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 29,390.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.78` | 16,110,000.00 USD | 16,110,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 59,430.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.79` | 15,950,000.00 USD | 15,950,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 37,390.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.80` | 15,760,000.00 USD | 15,760,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 570,030.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.81` | 15,700,000.00 USD | 15,700,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 14,090.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.82` | 15,700,000.00 USD | 15,700,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 134,350.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.83` | 15,650,000.00 USD | 15,650,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 171,380.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.84` | 15,540,000.00 USD | 15,540,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 116,490.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.85` | 15,500,000.00 USD | 15,500,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 22,330.00 USD | 998,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 18,260,000.00 USD | 18,260,000.00 USD | 225,350.00 USD | 214,520.00 USD | 91,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 15,370,000.00 USD | 15,370,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 71,550.00 USD | 976,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 17,730,000.00 USD | 17,730,000.00 USD | 53,480.00 USD | 58,230.00 USD | 188,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 15,150,000.00 USD | 15,150,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 7,870.00 USD | 904,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 17,430,000.00 USD | 17,430,000.00 USD | 35,520.00 USD | 26,560.00 USD | 224,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 14,890,000.00 USD | 14,890,000.00 USD | 110,160.00 USD | 86,900.00 USD | 118,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 175,650.00 USD | 896,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 17,150,000.00 USD | 17,150,000.00 USD | 397,250.00 USD | 100,370.00 USD | 258,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 14,570,000.00 USD | 14,570,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 93,930.00 USD | 721,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 16,390,000.00 USD | 16,390,000.00 USD | 33,540.00 USD | 53,910.00 USD | 248,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 14,430,000.00 USD | 14,430,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 8,860.00 USD | 627,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 16,050,000.00 USD | 16,050,000.00 USD | 378,850.00 USD | 120,100.00 USD | 304,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 14,080,000.00 USD | 14,080,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 132,720.00 USD | 618,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 15,250,000.00 USD | 15,250,000.00 USD | 342,280.00 USD | 13,670.00 USD | 124,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 13,840,000.00 USD | 13,840,000.00 USD | 176,970.00 USD | 66,710.00 USD | 105,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 2,050.00 USD | 485,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 14,770,000.00 USD | 14,770,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 3,320.00 USD | 483,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 14,460,000.00 USD | 14,460,000.00 USD | 144,900.00 USD | 53,060.00 USD | 137,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 13,470,000.00 USD | 13,470,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 22,630.00 USD | 480,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 14,120,000.00 USD | 14,120,000.00 USD | 103,590.00 USD | 0.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 13,410,000.00 USD | 13,410,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 55,290.00 USD | 457,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 13,990,000.00 USD | 13,990,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 13,400,000.00 USD | 13,400,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 2,110.00 USD | 402,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 13,880,000.00 USD | 13,880,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 13,230,000.00 USD | 13,230,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 26,000.00 USD | 400,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 13,700,000.00 USD | 13,700,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 12,990,000.00 USD | 12,990,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 1,070.00 USD | 374,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 13,510,000.00 USD | 13,510,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 12,210,000.00 USD | 12,210,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 160,840.00 USD | 373,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 13,310,000.00 USD | 13,310,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 11,800,000.00 USD | 11,800,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 13,260.00 USD | 212,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 13,110,000.00 USD | 13,110,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 10,850,000.00 USD | 10,850,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 275.83 USD | 199,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 12,730,000.00 USD | 12,730,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 9,980,000.00 USD | 9,980,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 2,110.00 USD | 198,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 12,410,000.00 USD | 12,410,000.00 USD | 66,220.00 USD | 59,350.00 USD | 324.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 9,300,000.00 USD | 9,300,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 24,650.00 USD | 196,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 12,290,000.00 USD | 12,290,000.00 USD | 70,930.00 USD | 21,940.00 USD | 183,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 8,710,000.00 USD | 8,710,000.00 USD | 321,230.00 USD | 0.00 USD | 492,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 21,310.00 USD | 172,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 12,010,000.00 USD | 12,010,000.00 USD | 348,930.00 USD | 23,720.00 USD | 232.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 7,900,000.00 USD | 7,900,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 54,890.00 USD | 150,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 11,640,000.00 USD | 11,640,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 1,200.00 USD | 96,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 11,070,000.00 USD | 11,070,000.00 USD | 358,380.00 USD | 205,460.00 USD | 334,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 2,640.00 USD | 94,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 10,170,000.00 USD | 10,170,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 8,310.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 9,690,000.00 USD | 9,690,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 7,020,000.00 USD | 7,020,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 19,450.00 USD | 83,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 9,210,000.00 USD | 9,210,000.00 USD | 4,790.00 USD | 89,650.00 USD | 141,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 6,160,000.00 USD | 6,160,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 25,410.00 USD | 64,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 8,980,000.00 USD | 8,980,000.00 USD | 122,090.00 USD | 138,540.00 USD | 345,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 25,170.00 USD | 296,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 16,830.00 USD | 39,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 8,370,000.00 USD | 8,370,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 5,810,000.00 USD | 5,810,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 10,570.00 USD | 22,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 8,010,000.00 USD | 8,010,000.00 USD | 159,720.00 USD | 0.00 USD | 398,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 5,620,000.00 USD | 5,620,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 2,230.00 USD | 11,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 7,460,000.00 USD | 7,460,000.00 USD | 139,890.00 USD | 29,960.00 USD | 125,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 5,230,000.00 USD | 5,230,000.00 USD | 238,150.00 USD | 244,270.00 USD | 345,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 652.84 USD | 9,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 7,160,000.00 USD | 7,160,000.00 USD | 526,070.00 USD | 109,290.00 USD | 367,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 4,400,000.00 USD | 4,400,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 8,730.00 USD | 8,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 6,160,000.00 USD | 6,160,000.00 USD | 340,550.00 USD | 100,580.00 USD | 379,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 22,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.17` | 5,340,000.00 USD | 5,340,000.00 USD | 340,700.00 USD | 296,330.00 USD | 310,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 4,050,000.00 USD | 4,050,000.00 USD | 252,690.00 USD | 84,340.00 USD | 78,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 4,390,000.00 USD | 4,390,000.00 USD | 389,120.00 USD | 69,910.00 USD | 201,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 3,640,000.00 USD | 3,640,000.00 USD | 227,940.00 USD | 0.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.19` | 3,730,000.00 USD | 3,730,000.00 USD | 148,260.00 USD | 138,280.00 USD | 244,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 3,320,000.00 USD | 3,320,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.20` | 3,200,000.00 USD | 3,200,000.00 USD | 31,500.00 USD | 40,570.00 USD | 131,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 2,880,000.00 USD | 2,880,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.21` | 2,990,000.00 USD | 2,990,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 2,190,000.00 USD | 2,190,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.22` | 2,190,000.00 USD | 2,190,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 1,740,000.00 USD | 1,740,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.23` | 1,990,000.00 USD | 1,990,000.00 USD | 113,770.00 USD | 129,320.00 USD | 274,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 1,060,000.00 USD | 1,060,000.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.24` | 15,550.00 USD | 15,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.24` | 1,470,000.00 USD | 1,470,000.00 USD | 127,260.00 USD | 98,020.00 USD | 125,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 873,040.00 USD | 873,040.00 USD | 0.00 USD | 45,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.25` | 1,120,000.00 USD | 1,120,000.00 USD | 251,300.00 USD | 25,800.00 USD | 328,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 827,270.00 USD | 827,270.00 USD | 3,390.00 USD | 0.00 USD | 156,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.26` | 517,070.00 USD | 517,070.00 USD | 120,080.00 USD | 15,130.00 USD | 85,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 667,350.00 USD | 667,350.00 USD | 458,850.00 USD | 0.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.27` | 296,250.00 USD | 296,250.00 USD | 0.00 USD | 44,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 35,350.00 USD | 35,350.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.28` | 251,390.00 USD | 251,390.00 USD | 4,310.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 10,540.00 USD | 10,540.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.29` | 218,290.00 USD | 218,290.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 5,150.00 USD | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.32` | 326.33 USD | 326.33 USD | 0.00 USD | 0.00 USD | 326.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 7,340.00 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 14,680.00 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.36` | 380,150.00 USD | 380,150.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 1,060,000.00 USD | 1,060,000.00 USD | 280,420.00 USD | 0.00 USD | 400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 458,540.00 USD | 458,540.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.38` | 1,700,000.00 USD | 1,700,000.00 USD | 3,030.00 USD | 0.00 USD | 640,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 948,640.00 USD | 948,640.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 2,610,000.00 USD | 2,610,000.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 2,030,000.00 USD | 2,030,000.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 180,760.00 USD | 196,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 3,680,000.00 USD | 3,680,000.00 USD | 541,780.00 USD | 118,310.00 USD | 408,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 3,190,000.00 USD | 3,190,000.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 5,150,000.00 USD | 5,150,000.00 USD | 450,080.00 USD | 331,840.00 USD | 689,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 3,720,000.00 USD | 3,720,000.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 5,770,000.00 USD | 5,770,000.00 USD | 128,340.00 USD | 240,270.00 USD | 253,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 4,420,000.00 USD | 4,420,000.00 USD | 404,280.00 USD | 117,350.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 1,930.00 USD | 198,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 6,680,000.00 USD | 6,680,000.00 USD | 335,950.00 USD | 135,430.00 USD | 443,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 5,030,000.00 USD | 5,030,000.00 USD | 293,250.00 USD | 88,400.00 USD | 228,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 3,540.00 USD | 201,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 7,800,000.00 USD | 7,800,000.00 USD | 276,510.00 USD | 385,410.00 USD | 457,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 5,870,000.00 USD | 5,870,000.00 USD | 455,890.00 USD | 143,990.00 USD | 246,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 358.27 USD | 202,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 8,160,000.00 USD | 8,160,000.00 USD | 76,860.00 USD | 153,510.00 USD | 124,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 36,680.00 USD | 238,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 8,260,000.00 USD | 8,260,000.00 USD | 4,580.00 USD | 65,940.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 6,210,000.00 USD | 6,210,000.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 1,370.00 USD | 240,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 8,630,000.00 USD | 8,630,000.00 USD | 222,670.00 USD | 25,190.00 USD | 120,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 6,780,000.00 USD | 6,780,000.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 17,400.00 USD | 257,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 9,140,000.00 USD | 9,140,000.00 USD | 246,890.00 USD | 116,490.00 USD | 150,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 7,060,000.00 USD | 7,060,000.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 2,970.00 USD | 260,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 10,100,000.00 USD | 10,100,000.00 USD | 310,660.00 USD | 242,590.00 USD | 403,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 7,490,000.00 USD | 7,490,000.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 22,680.00 USD | 283,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 10,880,000.00 USD | 10,880,000.00 USD | 427,290.00 USD | 118,600.00 USD | 237,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 8,090,000.00 USD | 8,090,000.00 USD | 376,770.00 USD | 223,580.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 7,940.00 USD | 291,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 11,850,000.00 USD | 11,850,000.00 USD | 314,310.00 USD | 162,710.00 USD | 489,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 8,250,000.00 USD | 8,250,000.00 USD | 77,780.00 USD | 0.00 USD | 80,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 9,560.00 USD | 300,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 12,590,000.00 USD | 12,590,000.00 USD | 351,620.00 USD | 99,830.00 USD | 286,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 8,710,000.00 USD | 8,710,000.00 USD | 230,020.00 USD | 0.00 USD | 225,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 7,110.00 USD | 307,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 13,400,000.00 USD | 13,400,000.00 USD | 505,320.00 USD | 22,430.00 USD | 280,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 9,690,000.00 USD | 9,690,000.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 7,320.00 USD | 315,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 13,750,000.00 USD | 13,750,000.00 USD | 17,740.00 USD | 164,990.00 USD | 167,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 10,930,000.00 USD | 10,930,000.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 10,070.00 USD | 325,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 13,890,000.00 USD | 13,890,000.00 USD | 3,110.00 USD | 34,450.00 USD | 108,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 558.34 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.55` | 14,110.00 USD | 339,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.56` | 14,330,000.00 USD | 14,330,000.00 USD | 112,410.00 USD | 32,800.00 USD | 288,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 11,420,000.00 USD | 11,420,000.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 8,790.00 USD | 348,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 14,670,000.00 USD | 14,670,000.00 USD | 175,730.00 USD | 70,180.00 USD | 99,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 11,960,000.00 USD | 11,960,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 15,700,000.00 USD | 15,700,000.00 USD | 376,930.00 USD | 99,430.00 USD | 554,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 12,090,000.00 USD | 12,090,000.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 1,800.00 USD | 349,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.59` | 16,310,000.00 USD | 16,310,000.00 USD | 420,560.00 USD | 75,460.00 USD | 109,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 13,800,000.00 USD | 13,800,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 16,480,000.00 USD | 16,480,000.00 USD | 48,970.00 USD | 50,860.00 USD | 66,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 13,920,000.00 USD | 13,920,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 16,630,000.00 USD | 16,630,000.00 USD | 64,820.00 USD | 7,560.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 13,930,000.00 USD | 13,930,000.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 16,770,000.00 USD | 16,770,000.00 USD | 95,000.00 USD | 31,380.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 14,060,000.00 USD | 14,060,000.00 USD | 134,680.00 USD | 0.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 51,690.00 USD | 401,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 16,770,000.00 USD | 16,770,000.00 USD | 2,310.00 USD | 0.00 USD | 422.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 14,280,000.00 USD | 14,280,000.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 150,270.00 USD | 551,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 16,930,000.00 USD | 16,930,000.00 USD | 106,430.00 USD | 11,270.00 USD | 41,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 14,820,000.00 USD | 14,820,000.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 852.82 USD | 552,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 17,680,000.00 USD | 17,680,000.00 USD | 203,560.00 USD | 52,020.00 USD | 486,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 15,240,000.00 USD | 15,240,000.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 756.44 USD | 553,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 18,460,000.00 USD | 18,460,000.00 USD | 202,480.00 USD | 309,340.00 USD | 277,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 15,560,000.00 USD | 15,560,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 7,880.00 USD | 561,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 18,810,000.00 USD | 18,810,000.00 USD | 88,400.00 USD | 0.00 USD | 259,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 54,640.00 USD | 616,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 19,010,000.00 USD | 19,010,000.00 USD | 59,560.00 USD | 106,120.00 USD | 36,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 16,520,000.00 USD | 16,520,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 1,030.00 USD | 617,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 19,400,000.00 USD | 19,400,000.00 USD | 168,270.00 USD | 49,160.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 16,670,000.00 USD | 16,670,000.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 617,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 19,740,000.00 USD | 19,740,000.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 16,990,000.00 USD | 16,990,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 6,960.00 USD | 624,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 20,790,000.00 USD | 20,790,000.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 17,480,000.00 USD | 17,480,000.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 21,020,000.00 USD | 21,020,000.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 17,690,000.00 USD | 17,690,000.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 12,800.00 USD | 637,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 21,190,000.00 USD | 21,190,000.00 USD | 110,530.00 USD | 25,210.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 17,760,000.00 USD | 17,760,000.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 3,850.00 USD | 640,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 21,580,000.00 USD | 21,580,000.00 USD | 68,200.00 USD | 141,320.00 USD | 176,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 18,150,000.00 USD | 18,150,000.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 111,130.00 USD | 752,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 21,990,000.00 USD | 21,990,000.00 USD | 100,320.00 USD | 141,340.00 USD | 171,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 18,700,000.00 USD | 18,700,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.76` | 22,140,000.00 USD | 22,140,000.00 USD | 32,610.00 USD | 56,290.00 USD | 56,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 20,040,000.00 USD | 20,040,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 95,300.00 USD | 847,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 22,340,000.00 USD | 22,340,000.00 USD | 46,010.00 USD | 85,030.00 USD | 76,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 20,950,000.00 USD | 20,950,000.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 1,730.00 USD | 849,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 22,490,000.00 USD | 22,490,000.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 22,080,000.00 USD | 22,080,000.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 849,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 22,690,000.00 USD | 22,690,000.00 USD | 98,120.00 USD | 39,920.00 USD | 59,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 23,210,000.00 USD | 23,210,000.00 USD | 804,240.00 USD | 249,310.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 850,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 23,140,000.00 USD | 23,140,000.00 USD | 186,880.00 USD | 128,280.00 USD | 138,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 24,800,000.00 USD | 24,800,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 23,150,000.00 USD | 23,150,000.00 USD | 0.00 USD | 8,950.00 USD | 210.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 25,430,000.00 USD | 25,430,000.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 5,780.00 USD | 856,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 23,280,000.00 USD | 23,280,000.00 USD | 20,630.00 USD | 78,640.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 28,190,000.00 USD | 28,190,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 2,360.00 USD | 858,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 23,290,000.00 USD | 23,290,000.00 USD | 2,490.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 29,840,000.00 USD | 29,840,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 860,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 23,410,000.00 USD | 23,410,000.00 USD | 21,320.00 USD | 76,320.00 USD | 16,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 30,330,000.00 USD | 30,330,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 871,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 32,370,000.00 USD | 32,370,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 33,780,000.00 USD | 33,780,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 259.79 USD | 871,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 34,810,000.00 USD | 34,810,000.00 USD | 234,740.00 USD | 136,820.00 USD | 660,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 36,030,000.00 USD | 36,030,000.00 USD | 428,040.00 USD | 0.00 USD | 789,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 872,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.91` | 674.44 USD | 873,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 893,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,590.00 USD | 896,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.93` | 12,300.00 USD | 908,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 488.56 USD | 909,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,370.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.04` | 118.83 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.08` | 6,860.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.09` | 6,650.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 51,430.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.16` | 2,580.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,940.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.24` | 17,260.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 17,380.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 6,220.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,070,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 298,680.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 142.44 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 37,990.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 313,840.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 914.65 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 419.04 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 12,190.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 128,840.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 12,780.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.53` | 1,270.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 532.69 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 5,420,000.00 USD | 8,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 8,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 8,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 481,600.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 16,050.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 198.97 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 310.95 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 112,780.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 162.98 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,650.00 USD | 9,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.96` | 29,860.00 USD | 9,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 23,320.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 7,290.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 28,250.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.14` | 1,870.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.16` | 12,760.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 35,350.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.22` | 2,010.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 526,230.00 USD | 10,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 262,530.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.29` | 5,360.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.29` | 336,800.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 2,000.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 173.47 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 29,100,000.00 USD | 39,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 39,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 24,040.00 USD | 39,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 39,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 7,670.00 USD | 39,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 39,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 1,240,000.00 USD | 41,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 42,100.00 USD | 41,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.63` | 2,090.00 USD | 41,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,940.00 USD | 41,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 41,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 41,520.00 USD | 41,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 37,150.00 USD | 41,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 388,480.00 USD | 41,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 42,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.83` | 187.69 USD | 42,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 42,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.86` | 623.81 USD | 42,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 42,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 7,900.00 USD | 42,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 94,030.00 USD | 42,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.00` | 24,680.00 USD | 42,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 42,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.16` | 16,010.00 USD | 42,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 17,040.00 USD | 42,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 1,150.00 USD | 42,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 3,770.00 USD | 42,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.28` | 2,260.00 USD | 42,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.30` | 54,790.00 USD | 43,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.32` | 3,880,000.00 USD | 46,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 14,160.00 USD | 46,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 777.09 USD | 46,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 106,000.00 USD | 47,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 9,960,000.00 USD | 57,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 481.82 USD | 57,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,570.00 USD | 57,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 7,840,000.00 USD | 64,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.55` | 115.59 USD | 64,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 9,100.00 USD | 64,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 45,910.00 USD | 64,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.64` | 17,820.00 USD | 64,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 46,030.00 USD | 64,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 64,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 4,450.00 USD | 64,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 1,200,000.00 USD | 66,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 33,830.00 USD | 66,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 66,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.76` | 1,680.00 USD | 66,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 66,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 12,000.00 USD | 66,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 66,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 66,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,580.00 USD | 66,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.07` | 6,460.00 USD | 66,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.09` | 97,280.00 USD | 66,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.20` | 951.44 USD | 66,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.29` | 165.07 USD | 66,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.34` | 96,080.00 USD | 66,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.35` | 25,310.00 USD | 66,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 191.79 USD | 66,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.43` | 1,220.00 USD | 66,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.44` | 8,770.00 USD | 66,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.47` | 816.99 USD | 66,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 6,640.00 USD | 66,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 25,490.00 USD | 66,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.52` | 17,500.00 USD | 66,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 34,680.00 USD | 66,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 127.17 USD | 66,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 124.76 USD | 66,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.59` | 432,220.00 USD | 67,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.60` | 240.66 USD | 67,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.61` | 54,210.00 USD | 67,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.62` | 4,950.00 USD | 67,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 2,320.00 USD | 67,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8850` | 22,540,000.00 USD | 0.00 USD | 411.70 USD | `-79.62%` | `465.20` |
| `Live` | `Long` | `0.8950` | 22,540,000.00 USD | 0.00 USD | 38,570.00 USD | `-79.39%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 22,500,000.00 USD | 0.00 USD | 292.22 USD | `-79.15%` | `322.90` |
| `Live` | `Long` | `0.9150` | 22,500,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.92%` | `12,425.00` |
| `Live` | `Long` | `0.9350` | 22,490,000.00 USD | 0.00 USD | 2,810.00 USD | `-78.46%` | `3,001.60` |
| `Live` | `Long` | `0.9450` | 22,490,000.00 USD | 0.00 USD | 6,620.00 USD | `-78.23%` | `7,000.00` |
| `Live` | `Long` | `0.9550` | 22,480,000.00 USD | 0.00 USD | 1,450.00 USD | `-78.00%` | `1,521.50` |
| `Live` | `Long` | `0.9650` | 22,480,000.00 USD | 0.00 USD | 965.00 USD | `-77.77%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,480,000.00 USD | 0.00 USD | 3,690.00 USD | `-77.31%` | `3,749.70` |
| `Live` | `Long` | `0.9950` | 22,470,000.00 USD | 0.00 USD | 154,200.00 USD | `-77.08%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 22,320,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.85%` | `2,543.70` |
| `Live` | `Long` | `1.02` | 22,320,000.00 USD | 0.00 USD | 10,250.00 USD | `-76.39%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 22,310,000.00 USD | 0.00 USD | 5,070.00 USD | `-76.16%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,300,000.00 USD | 0.00 USD | 34,960.00 USD | `-75.93%` | `33,454.20` |
| `Live` | `Long` | `1.05` | 22,270,000.00 USD | 0.00 USD | 4,330.00 USD | `-75.70%` | `4,108.90` |
| `Live` | `Long` | `1.06` | 22,260,000.00 USD | 0.00 USD | 892.90 USD | `-75.47%` | `838.40` |
| `Live` | `Long` | `1.07` | 22,260,000.00 USD | 0.00 USD | 5,740.00 USD | `-75.24%` | `5,342.20` |
| `Live` | `Long` | `1.08` | 22,260,000.00 USD | 0.00 USD | 216.89 USD | `-75.01%` | `199.90` |
| `Live` | `Long` | `1.10` | 22,260,000.00 USD | 0.00 USD | 18,980.00 USD | `-74.55%` | `17,179.40` |
| `Live` | `Long` | `1.11` | 22,240,000.00 USD | 0.00 USD | 1,690.00 USD | `-74.32%` | `1,513.70` |
| `Live` | `Long` | `1.12` | 22,240,000.00 USD | 0.00 USD | 6,930.00 USD | `-74.09%` | `6,158.40` |
| `Live` | `Long` | `1.14` | 22,230,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.86%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 22,220,000.00 USD | 0.00 USD | 26,620.00 USD | `-73.63%` | `23,252.70` |
| `Live` | `Long` | `1.16` | 22,200,000.00 USD | 0.00 USD | 1,730.00 USD | `-73.40%` | `1,500.00` |
| `Live` | `Long` | `1.17` | 22,200,000.00 USD | 0.00 USD | 2,390.00 USD | `-73.17%` | `2,054.80` |
| `Live` | `Long` | `1.18` | 22,190,000.00 USD | 0.00 USD | 9,630.00 USD | `-72.94%` | `8,196.50` |
| `Live` | `Long` | `1.21` | 22,180,000.00 USD | 0.00 USD | 4,940.00 USD | `-72.24%` | `4,103.20` |
| `Live` | `Long` | `1.22` | 22,180,000.00 USD | 0.00 USD | 150.90 USD | `-72.01%` | `124.20` |
| `Live` | `Long` | `1.23` | 22,180,000.00 USD | 0.00 USD | 1,040.00 USD | `-71.78%` | `847.00` |
| `Live` | `Long` | `1.25` | 22,180,000.00 USD | 0.00 USD | 20,460.00 USD | `-71.32%` | `16,436.80` |
| `Live` | `Long` | `1.25` | 22,160,000.00 USD | 0.00 USD | 15,020.00 USD | `-71.09%` | `11,969.60` |
| `Live` | `Long` | `1.26` | 22,140,000.00 USD | 0.00 USD | 2,060.00 USD | `-70.86%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 22,140,000.00 USD | 0.00 USD | 3,370.00 USD | `-70.63%` | `2,646.90` |
| `Live` | `Long` | `1.28` | 22,140,000.00 USD | 0.00 USD | 425.59 USD | `-70.40%` | `331.20` |
| `Live` | `Long` | `1.30` | 22,140,000.00 USD | 0.00 USD | 379.76 USD | `-69.94%` | `291.00` |
| `Live` | `Long` | `1.32` | 22,140,000.00 USD | 0.00 USD | 28,340.00 USD | `-69.48%` | `21,389.30` |
| `Live` | `Long` | `1.33` | 22,110,000.00 USD | 0.00 USD | 179.96 USD | `-69.25%` | `134.80` |
| `Live` | `Long` | `1.34` | 22,110,000.00 USD | 0.00 USD | 603.91 USD | `-69.02%` | `449.00` |
| `Live` | `Long` | `1.35` | 22,110,000.00 USD | 0.00 USD | 2,130.00 USD | `-68.79%` | `1,572.30` |
| `Live` | `Long` | `1.36` | 22,100,000.00 USD | 0.00 USD | 2,200.00 USD | `-68.56%` | `1,615.10` |
| `Live` | `Long` | `1.39` | 22,100,000.00 USD | 0.00 USD | 12,760.00 USD | `-68.10%` | `9,213.40` |
| `Live` | `Long` | `1.40` | 22,090,000.00 USD | 0.00 USD | 931.86 USD | `-67.87%` | `668.00` |
| `Live` | `Long` | `1.41` | 22,090,000.00 USD | 0.00 USD | 77,850.00 USD | `-67.64%` | `55,412.50` |
| `Live` | `Long` | `1.42` | 22,010,000.00 USD | 0.00 USD | 4,710.00 USD | `-67.41%` | `3,325.90` |
| `Live` | `Long` | `1.43` | 22,010,000.00 USD | 0.00 USD | 1,130.00 USD | `-67.18%` | `793.40` |
| `Live` | `Long` | `1.45` | 22,010,000.00 USD | 0.00 USD | 2,690.00 USD | `-66.72%` | `1,861.70` |
| `Live` | `Long` | `1.46` | 22,000,000.00 USD | 0.00 USD | 5,440.00 USD | `-66.49%` | `3,738.20` |
| `Live` | `Long` | `1.47` | 22,000,000.00 USD | 0.00 USD | 13,180.00 USD | `-66.26%` | `9,000.00` |
| `Live` | `Long` | `1.48` | 21,980,000.00 USD | 0.00 USD | 1,480.00 USD | `-66.03%` | `1,000.00` |
| `Live` | `Long` | `1.49` | 21,980,000.00 USD | 0.00 USD | 74,750.00 USD | `-65.80%` | `50,337.90` |
| `Live` | `Long` | `1.50` | 21,910,000.00 USD | 0.00 USD | 4,920.00 USD | `-65.56%` | `3,291.10` |
| `Live` | `Long` | `1.50` | 21,900,000.00 USD | 0.00 USD | 2,640.00 USD | `-65.33%` | `1,756.00` |
| `Live` | `Long` | `1.51` | 21,900,000.00 USD | 0.00 USD | 454.50 USD | `-65.10%` | `300.00` |
| `Live` | `Long` | `1.53` | 21,900,000.00 USD | 0.00 USD | 6,190.00 USD | `-64.64%` | `4,030.50` |
| `Live` | `Long` | `1.56` | 21,890,000.00 USD | 0.00 USD | 20,570.00 USD | `-63.95%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 21,870,000.00 USD | 0.00 USD | 2,630.00 USD | `-63.72%` | `1,669.90` |
| `Live` | `Long` | `1.58` | 21,870,000.00 USD | 0.00 USD | 1,980.00 USD | `-63.49%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 21,870,000.00 USD | 0.00 USD | 3,380.00 USD | `-63.26%` | `2,119.70` |
| `Live` | `Long` | `1.60` | 21,860,000.00 USD | 0.00 USD | 753.39 USD | `-63.03%` | `469.40` |
| `Live` | `Long` | `1.64` | 21,860,000.00 USD | 0.00 USD | 3,760.00 USD | `-62.34%` | `2,300.50` |
| `Live` | `Long` | `1.65` | 21,860,000.00 USD | 0.00 USD | 981.08 USD | `-62.11%` | `596.40` |
| `Live` | `Long` | `1.66` | 21,860,000.00 USD | 0.00 USD | 3,420.00 USD | `-61.88%` | `2,068.70` |
| `Live` | `Long` | `1.67` | 21,860,000.00 USD | 0.00 USD | 617.72 USD | `-61.65%` | `371.00` |
| `Live` | `Long` | `1.68` | 21,860,000.00 USD | 0.00 USD | 9,620.00 USD | `-61.42%` | `5,742.30` |
| `Live` | `Long` | `1.69` | 21,850,000.00 USD | 0.00 USD | 603,680.00 USD | `-61.19%` | `358,268.30` |
| `Live` | `Long` | `1.71` | 21,240,000.00 USD | 0.00 USD | 929.23 USD | `-60.73%` | `545.00` |
| `Live` | `Long` | `1.72` | 21,240,000.00 USD | 0.00 USD | 5,000.00 USD | `-60.50%` | `2,912.70` |
| `Live` | `Long` | `1.73` | 21,240,000.00 USD | 0.00 USD | 8,910.00 USD | `-60.27%` | `5,164.50` |
| `Live` | `Long` | `1.74` | 21,230,000.00 USD | 0.00 USD | 105.14 USD | `-60.04%` | `60.60` |
| `Live` | `Long` | `1.75` | 21,230,000.00 USD | 0.00 USD | 10,250.00 USD | `-59.58%` | `5,841.90` |
| `Live` | `Long` | `1.77` | 21,220,000.00 USD | 0.00 USD | 17,220.00 USD | `-59.12%` | `9,703.40` |
| `Live` | `Long` | `1.78` | 21,200,000.00 USD | 0.00 USD | 2,230.00 USD | `-58.89%` | `1,250.00` |
| `Live` | `Long` | `1.79` | 21,200,000.00 USD | 0.00 USD | 91,410.00 USD | `-58.65%` | `50,924.10` |
| `Live` | `Long` | `1.80` | 21,110,000.00 USD | 0.00 USD | 529.05 USD | `-58.42%` | `293.10` |
| `Live` | `Long` | `1.81` | 21,110,000.00 USD | 0.00 USD | 1,580.00 USD | `-58.19%` | `873.20` |
| `Live` | `Long` | `1.83` | 21,100,000.00 USD | 0.00 USD | 27,520.00 USD | `-57.73%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 21,080,000.00 USD | 0.00 USD | 1,840.00 USD | `-57.50%` | `995.20` |
| `Live` | `Long` | `1.85` | 21,070,000.00 USD | 0.00 USD | 1,400.00 USD | `-57.27%` | `755.00` |
| `Live` | `Long` | `1.88` | 21,070,000.00 USD | 0.00 USD | 14,720.00 USD | `-56.81%` | `7,852.10` |
| `Live` | `Long` | `1.90` | 21,060,000.00 USD | 0.00 USD | 2,750.00 USD | `-56.35%` | `1,450.00` |
| `Live` | `Long` | `1.91` | 21,060,000.00 USD | 0.00 USD | 39,130.00 USD | `-56.12%` | `20,538.40` |
| `Live` | `Long` | `1.93` | 21,020,000.00 USD | 0.00 USD | 1,120.00 USD | `-55.66%` | `579.70` |
| `Live` | `Long` | `1.95` | 21,020,000.00 USD | 0.00 USD | 2,740.00 USD | `-55.20%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 21,010,000.00 USD | 0.00 USD | 775.55 USD | `-54.97%` | `396.70` |
| `Live` | `Long` | `1.97` | 21,010,000.00 USD | 0.00 USD | 2,280.00 USD | `-54.74%` | `1,160.90` |
| `Live` | `Long` | `1.98` | 21,010,000.00 USD | 0.00 USD | 37,250.00 USD | `-54.51%` | `18,860.60` |
| `Live` | `Long` | `2.00` | 20,970,000.00 USD | 0.00 USD | 856,120.00 USD | `-53.82%` | `426,991.00` |
| `Live` | `Long` | `2.02` | 20,120,000.00 USD | 0.00 USD | 12,900.00 USD | `-53.59%` | `6,399.80` |
| `Live` | `Long` | `2.02` | 20,100,000.00 USD | 0.00 USD | 398.72 USD | `-53.36%` | `196.90` |
| `Live` | `Long` | `2.04` | 20,100,000.00 USD | 0.00 USD | 323.36 USD | `-53.13%` | `158.90` |
| `Live` | `Long` | `2.04` | 20,100,000.00 USD | 0.00 USD | 3,640.00 USD | `-52.90%` | `1,778.40` |
| `Live` | `Long` | `2.06` | 20,100,000.00 USD | 0.00 USD | 39,180.00 USD | `-52.67%` | `19,063.40` |
| `Live` | `Long` | `2.06` | 20,060,000.00 USD | 0.00 USD | 8,860.00 USD | `-52.44%` | `4,292.80` |
| `Live` | `Long` | `2.08` | 20,050,000.00 USD | 0.00 USD | 13,270.00 USD | `-52.21%` | `6,393.50` |
| `Live` | `Long` | `2.08` | 20,040,000.00 USD | 0.00 USD | 18,600.00 USD | `-51.98%` | `8,920.10` |
| `Live` | `Long` | `2.10` | 20,020,000.00 USD | 0.00 USD | 1,100.00 USD | `-51.74%` | `527.40` |
| `Live` | `Long` | `2.10` | 20,020,000.00 USD | 0.00 USD | 10,540.00 USD | `-51.51%` | `5,006.20` |
| `Live` | `Long` | `2.12` | 20,010,000.00 USD | 0.00 USD | 11,510.00 USD | `-51.28%` | `5,442.30` |
| `Live` | `Long` | `2.12` | 20,000,000.00 USD | 0.00 USD | 18,310.00 USD | `-51.05%` | `8,615.20` |
| `Live` | `Long` | `2.13` | 19,980,000.00 USD | 0.00 USD | 2,140.00 USD | `-50.82%` | `1,000.80` |
| `Live` | `Long` | `2.15` | 19,980,000.00 USD | 0.00 USD | 2,110.00 USD | `-50.59%` | `983.60` |
| `Live` | `Long` | `2.15` | 19,970,000.00 USD | 0.00 USD | 2,530.00 USD | `-50.36%` | `1,175.20` |
| `Live` | `Long` | `2.17` | 19,970,000.00 USD | 0.00 USD | 188,810.00 USD | `-50.13%` | `87,210.30` |
| `Live` | `Long` | `2.17` | 19,780,000.00 USD | 0.00 USD | 93,620.00 USD | `-49.90%` | `43,045.60` |
| `Live` | `Long` | `2.19` | 19,690,000.00 USD | 0.00 USD | 3,530.00 USD | `-49.67%` | `1,614.40` |
| `Live` | `Long` | `2.19` | 19,680,000.00 USD | 0.00 USD | 12,830.00 USD | `-49.44%` | `5,843.40` |
| `Live` | `Long` | `2.21` | 19,670,000.00 USD | 0.00 USD | 19,420.00 USD | `-49.21%` | `8,807.10` |
| `Live` | `Long` | `2.21` | 19,650,000.00 USD | 0.00 USD | 25,570.00 USD | `-48.98%` | `11,546.10` |
| `Live` | `Long` | `2.23` | 19,630,000.00 USD | 0.00 USD | 8,450.00 USD | `-48.75%` | `3,795.90` |
| `Live` | `Long` | `2.23` | 19,620,000.00 USD | 0.00 USD | 21,160.00 USD | `-48.52%` | `9,467.70` |
| `Live` | `Long` | `2.25` | 19,600,000.00 USD | 0.00 USD | 3,020.00 USD | `-48.29%` | `1,344.30` |
| `Live` | `Long` | `2.25` | 19,590,000.00 USD | 0.00 USD | 117,220.00 USD | `-48.06%` | `51,980.50` |
| `Live` | `Long` | `2.27` | 19,480,000.00 USD | 0.00 USD | 2,040.00 USD | `-47.83%` | `900.00` |
| `Live` | `Long` | `2.27` | 19,480,000.00 USD | 0.00 USD | 72,840.00 USD | `-47.60%` | `32,019.10` |
| `Live` | `Long` | `2.29` | 19,400,000.00 USD | 0.00 USD | 5,120.00 USD | `-47.37%` | `2,241.40` |
| `Live` | `Long` | `2.29` | 19,400,000.00 USD | 0.00 USD | 221,220.00 USD | `-47.14%` | `96,393.30` |
| `Live` | `Long` | `2.31` | 19,180,000.00 USD | 0.00 USD | 12,250.00 USD | `-46.91%` | `5,316.10` |
| `Live` | `Long` | `2.31` | 19,160,000.00 USD | 0.00 USD | 2,330.00 USD | `-46.68%` | `1,005.00` |
| `Live` | `Long` | `2.33` | 19,160,000.00 USD | 0.00 USD | 13,770.00 USD | `-46.45%` | `5,923.50` |
| `Live` | `Long` | `2.33` | 19,150,000.00 USD | 0.00 USD | 2,670.00 USD | `-46.22%` | `1,145.40` |
| `Live` | `Long` | `2.35` | 19,140,000.00 USD | 0.00 USD | 5,100.00 USD | `-45.99%` | `2,175.10` |
| `Live` | `Long` | `2.35` | 19,140,000.00 USD | 0.00 USD | 26,590.00 USD | `-45.76%` | `11,292.40` |
| `Live` | `Long` | `2.37` | 19,110,000.00 USD | 0.00 USD | 1,580.00 USD | `-45.53%` | `667.80` |
| `Live` | `Long` | `2.38` | 19,110,000.00 USD | 0.00 USD | 35,720.00 USD | `-45.30%` | `15,041.30` |
| `Live` | `Long` | `2.38` | 19,080,000.00 USD | 0.00 USD | 7,680.00 USD | `-45.07%` | `3,218.80` |
| `Live` | `Long` | `2.40` | 19,070,000.00 USD | 0.00 USD | 115.20 USD | `-44.83%` | `48.10` |
| `Live` | `Long` | `2.42` | 19,070,000.00 USD | 0.00 USD | 183,000.00 USD | `-44.37%` | `75,774.50` |
| `Live` | `Long` | `2.42` | 18,890,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-44.14%` | `769,602.00` |
| `Live` | `Long` | `2.44` | 17,020,000.00 USD | 0.00 USD | 2,320.00 USD | `-43.91%` | `953.50` |
| `Live` | `Long` | `2.44` | 17,020,000.00 USD | 0.00 USD | 160,000.00 USD | `-43.68%` | `65,440.70` |
| `Live` | `Long` | `2.46` | 16,860,000.00 USD | 0.00 USD | 281,230.00 USD | `-43.45%` | `114,554.40` |
| `Live` | `Long` | `2.46` | 16,580,000.00 USD | 0.00 USD | 4,590.00 USD | `-43.22%` | `1,862.10` |
| `Live` | `Long` | `2.48` | 16,570,000.00 USD | 0.00 USD | 12,520.00 USD | `-42.99%` | `5,058.20` |
| `Live` | `Long` | `2.48` | 16,560,000.00 USD | 0.00 USD | 9,240.00 USD | `-42.76%` | `3,719.70` |
| `Live` | `Long` | `2.50` | 16,550,000.00 USD | 0.00 USD | 15,850.00 USD | `-42.53%` | `6,351.10` |
| `Live` | `Long` | `2.50` | 16,530,000.00 USD | 0.00 USD | 425,370.00 USD | `-42.30%` | `169,806.80` |
| `Live` | `Long` | `2.52` | 16,110,000.00 USD | 0.00 USD | 346.32 USD | `-42.07%` | `137.70` |
| `Live` | `Long` | `2.52` | 16,110,000.00 USD | 0.00 USD | 33,330.00 USD | `-41.84%` | `13,198.20` |
| `Live` | `Long` | `2.54` | 16,070,000.00 USD | 0.00 USD | 395.71 USD | `-41.61%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,070,000.00 USD | 0.00 USD | 2,440.00 USD | `-41.38%` | `959.90` |
| `Live` | `Long` | `2.56` | 16,070,000.00 USD | 0.00 USD | 670.94 USD | `-41.15%` | `262.60` |
| `Live` | `Long` | `2.56` | 16,070,000.00 USD | 0.00 USD | 7,890.00 USD | `-40.92%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 16,060,000.00 USD | 0.00 USD | 2,050.00 USD | `-40.69%` | `796.50` |
| `Live` | `Long` | `2.58` | 16,060,000.00 USD | 0.00 USD | 1,910.00 USD | `-40.46%` | `739.30` |
| `Live` | `Long` | `2.60` | 16,060,000.00 USD | 0.00 USD | 80,250.00 USD | `-40.23%` | `30,925.80` |
| `Live` | `Long` | `2.60` | 15,980,000.00 USD | 0.00 USD | 2,450.00 USD | `-40.00%` | `940.80` |
| `Live` | `Long` | `2.62` | 15,980,000.00 USD | 0.00 USD | 1,190.00 USD | `-39.77%` | `454.70` |
| `Live` | `Long` | `2.63` | 15,970,000.00 USD | 0.00 USD | 24,310.00 USD | `-39.31%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 15,950,000.00 USD | 0.00 USD | 2,950.00 USD | `-39.08%` | `1,115.50` |
| `Live` | `Long` | `2.65` | 15,950,000.00 USD | 0.00 USD | 27,700.00 USD | `-38.85%` | `10,434.90` |
| `Live` | `Long` | `2.67` | 15,920,000.00 USD | 0.00 USD | 169,690.00 USD | `-38.62%` | `63,673.50` |
| `Live` | `Long` | `2.67` | 15,750,000.00 USD | 0.00 USD | 4,600.00 USD | `-38.39%` | `1,719.40` |
| `Live` | `Long` | `2.69` | 15,750,000.00 USD | 0.00 USD | 7,260.00 USD | `-38.16%` | `2,702.60` |
| `Live` | `Long` | `2.69` | 15,740,000.00 USD | 0.00 USD | 13,910.00 USD | `-37.92%` | `5,161.50` |
| `Live` | `Long` | `2.71` | 15,720,000.00 USD | 0.00 USD | 164,840.00 USD | `-37.69%` | `60,938.90` |
| `Live` | `Long` | `2.71` | 15,560,000.00 USD | 0.00 USD | 11,880.00 USD | `-37.46%` | `4,377.20` |
| `Live` | `Long` | `2.73` | 15,550,000.00 USD | 0.00 USD | 28,380.00 USD | `-37.23%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 15,520,000.00 USD | 0.00 USD | 1,960.00 USD | `-37.00%` | `715.80` |
| `Live` | `Long` | `2.75` | 15,520,000.00 USD | 0.00 USD | 458.96 USD | `-36.77%` | `167.20` |
| `Live` | `Long` | `2.75` | 15,520,000.00 USD | 0.00 USD | 64,490.00 USD | `-36.54%` | `23,408.80` |
| `Live` | `Long` | `2.77` | 15,450,000.00 USD | 0.00 USD | 350,290.00 USD | `-36.31%` | `126,687.80` |
| `Live` | `Long` | `2.77` | 15,100,000.00 USD | 0.00 USD | 398.77 USD | `-36.08%` | `143.70` |
| `Live` | `Long` | `2.79` | 15,100,000.00 USD | 0.00 USD | 47,860.00 USD | `-35.85%` | `17,186.00` |
| `Live` | `Long` | `2.79` | 15,050,000.00 USD | 0.00 USD | 12,340.00 USD | `-35.62%` | `4,416.00` |
| `Live` | `Long` | `2.81` | 15,040,000.00 USD | 0.00 USD | 90,180.00 USD | `-35.39%` | `32,148.50` |
| `Live` | `Long` | `2.81` | 14,950,000.00 USD | 0.00 USD | 4,780.00 USD | `-35.16%` | `1,698.90` |
| `Live` | `Long` | `2.83` | 14,950,000.00 USD | 0.00 USD | 2,350.00 USD | `-34.93%` | `832.70` |
| `Live` | `Long` | `2.83` | 14,940,000.00 USD | 0.00 USD | 10,910.00 USD | `-34.70%` | `3,847.80` |
| `Live` | `Long` | `2.85` | 14,930,000.00 USD | 0.00 USD | 3,790.00 USD | `-34.47%` | `1,333.60` |
| `Live` | `Long` | `2.85` | 14,930,000.00 USD | 0.00 USD | 3,540.00 USD | `-34.24%` | `1,240.70` |
| `Live` | `Long` | `2.87` | 14,930,000.00 USD | 0.00 USD | 18,770.00 USD | `-34.01%` | `6,552.50` |
| `Live` | `Long` | `2.88` | 14,910,000.00 USD | 0.00 USD | 868,330.00 USD | `-33.78%` | `302,028.00` |
| `Live` | `Long` | `2.88` | 14,040,000.00 USD | 0.00 USD | 8,470.00 USD | `-33.55%` | `2,934.40` |
| `Live` | `Long` | `2.90` | 14,030,000.00 USD | 0.00 USD | 112,920.00 USD | `-33.32%` | `39,005.40` |
| `Live` | `Long` | `2.90` | 13,920,000.00 USD | 0.00 USD | 4,500.00 USD | `-33.09%` | `1,547.90` |
| `Live` | `Long` | `2.92` | 13,910,000.00 USD | 0.00 USD | 11,820.00 USD | `-32.86%` | `4,055.30` |
| `Live` | `Long` | `2.92` | 13,900,000.00 USD | 0.00 USD | 245,610.00 USD | `-32.63%` | `83,969.90` |
| `Live` | `Long` | `2.94` | 13,660,000.00 USD | 0.00 USD | 50,370.00 USD | `-32.40%` | `17,161.30` |
| `Live` | `Long` | `2.94` | 13,610,000.00 USD | 0.00 USD | 18,090.00 USD | `-32.17%` | `6,142.40` |
| `Live` | `Long` | `2.96` | 13,590,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.94%` | `4,571.50` |
| `Live` | `Long` | `2.96` | 13,570,000.00 USD | 0.00 USD | 1,380.00 USD | `-31.71%` | `465.60` |
| `Live` | `Long` | `2.98` | 13,570,000.00 USD | 0.00 USD | 148,680.00 USD | `-31.48%` | `49,976.10` |
| `Live` | `Long` | `2.98` | 13,420,000.00 USD | 0.00 USD | 5,270.00 USD | `-31.24%` | `1,764.40` |
| `Live` | `Long` | `3.00` | 13,420,000.00 USD | 0.00 USD | 11,160.00 USD | `-31.01%` | `3,725.50` |
| `Live` | `Long` | `3.00` | 13,410,000.00 USD | 0.00 USD | 116,780.00 USD | `-30.78%` | `38,863.00` |
| `Live` | `Long` | `3.02` | 13,290,000.00 USD | 0.00 USD | 26,540.00 USD | `-30.55%` | `8,801.10` |
| `Live` | `Long` | `3.02` | 13,260,000.00 USD | 0.00 USD | 26,810.00 USD | `-30.32%` | `8,863.50` |
| `Live` | `Long` | `3.04` | 13,240,000.00 USD | 0.00 USD | 1,220.00 USD | `-30.09%` | `402.10` |
| `Live` | `Long` | `3.04` | 13,240,000.00 USD | 0.00 USD | 141,830.00 USD | `-29.86%` | `46,576.50` |
| `Live` | `Long` | `3.06` | 13,090,000.00 USD | 0.00 USD | 86,530.00 USD | `-29.63%` | `28,323.50` |
| `Live` | `Long` | `3.06` | 13,010,000.00 USD | 0.00 USD | 130,870.00 USD | `-29.40%` | `42,697.30` |
| `Live` | `Long` | `3.08` | 12,880,000.00 USD | 0.00 USD | 48,380.00 USD | `-28.94%` | `15,683.80` |
| `Live` | `Long` | `3.10` | 12,830,000.00 USD | 0.00 USD | 163,550.00 USD | `-28.71%` | `52,843.20` |
| `Live` | `Long` | `3.10` | 12,660,000.00 USD | 0.00 USD | 25,870.00 USD | `-28.48%` | `8,331.80` |
| `Live` | `Long` | `3.12` | 12,640,000.00 USD | 0.00 USD | 31,050.00 USD | `-28.25%` | `9,969.20` |
| `Live` | `Long` | `3.12` | 12,610,000.00 USD | 0.00 USD | 11,560.00 USD | `-28.02%` | `3,700.50` |
| `Live` | `Long` | `3.13` | 12,600,000.00 USD | 0.00 USD | 35,950.00 USD | `-27.79%` | `11,467.10` |
| `Live` | `Long` | `3.15` | 12,560,000.00 USD | 0.00 USD | 22,930.00 USD | `-27.56%` | `7,291.60` |
| `Live` | `Long` | `3.15` | 12,540,000.00 USD | 0.00 USD | 81,350.00 USD | `-27.33%` | `25,783.10` |
| `Live` | `Long` | `3.17` | 12,460,000.00 USD | 0.00 USD | 181,270.00 USD | `-27.10%` | `57,273.30` |
| `Live` | `Long` | `3.17` | 12,270,000.00 USD | 0.00 USD | 2,860,000.00 USD | `-26.87%` | `901,455.60` |
| `Live` | `Long` | `3.19` | 9,410,000.00 USD | 0.00 USD | 306,920.00 USD | `-26.64%` | `96,363.90` |
| `Live` | `Long` | `3.21` | 9,110,000.00 USD | 0.00 USD | 112.17 USD | `-26.18%` | `35.00` |
| `Live` | `Long` | `3.21` | 9,110,000.00 USD | 0.00 USD | 8,790.00 USD | `-25.95%` | `2,733.30` |
| `Live` | `Long` | `3.23` | 9,100,000.00 USD | 0.00 USD | 23,110.00 USD | `-25.72%` | `7,167.00` |
| `Live` | `Long` | `3.23` | 9,070,000.00 USD | 0.00 USD | 64,820.00 USD | `-25.49%` | `20,036.00` |
| `Live` | `Long` | `3.25` | 9,010,000.00 USD | 0.00 USD | 20,190.00 USD | `-25.26%` | `6,220.90` |
| `Live` | `Long` | `3.25` | 8,990,000.00 USD | 0.00 USD | 4,050.00 USD | `-25.03%` | `1,245.10` |
| `Live` | `Long` | `3.27` | 8,980,000.00 USD | 0.00 USD | 39,060.00 USD | `-24.80%` | `11,963.70` |
| `Live` | `Long` | `3.27` | 8,950,000.00 USD | 0.00 USD | 869,330.00 USD | `-24.57%` | `265,445.20` |
| `Live` | `Long` | `3.29` | 8,080,000.00 USD | 0.00 USD | 4,080.00 USD | `-24.33%` | `1,240.60` |
| `Live` | `Long` | `3.29` | 8,070,000.00 USD | 0.00 USD | 133,000.00 USD | `-24.10%` | `40,362.70` |
| `Live` | `Long` | `3.31` | 7,940,000.00 USD | 0.00 USD | 132,030.00 USD | `-23.87%` | `39,948.60` |
| `Live` | `Long` | `3.31` | 7,810,000.00 USD | 0.00 USD | 24,690.00 USD | `-23.64%` | `7,448.70` |
| `Live` | `Long` | `3.33` | 7,780,000.00 USD | 0.00 USD | 10,380.00 USD | `-23.41%` | `3,121.60` |
| `Live` | `Long` | `3.33` | 7,770,000.00 USD | 0.00 USD | 77,700.00 USD | `-23.18%` | `23,297.70` |
| `Live` | `Long` | `3.35` | 7,690,000.00 USD | 0.00 USD | 22,160.00 USD | `-22.95%` | `6,625.40` |
| `Live` | `Long` | `3.35` | 7,670,000.00 USD | 0.00 USD | 1,210.00 USD | `-22.72%` | `360.80` |
| `Live` | `Long` | `3.37` | 7,670,000.00 USD | 0.00 USD | 24,110.00 USD | `-22.49%` | `7,163.70` |
| `Live` | `Long` | `3.38` | 7,650,000.00 USD | 0.00 USD | 54,650.00 USD | `-22.26%` | `16,193.90` |
| `Live` | `Long` | `3.38` | 7,590,000.00 USD | 0.00 USD | 40,370.00 USD | `-22.03%` | `11,926.20` |
| `Live` | `Long` | `3.40` | 7,550,000.00 USD | 0.00 USD | 41,460.00 USD | `-21.80%` | `12,212.30` |
| `Live` | `Long` | `3.40` | 7,510,000.00 USD | 0.00 USD | 103,060.00 USD | `-21.57%` | `30,267.20` |
| `Live` | `Long` | `3.42` | 7,410,000.00 USD | 0.00 USD | 390,990.00 USD | `-21.34%` | `114,490.80` |
| `Live` | `Long` | `3.42` | 7,020,000.00 USD | 0.00 USD | 6,570.00 USD | `-21.11%` | `1,918.80` |
| `Live` | `Long` | `3.44` | 7,010,000.00 USD | 0.00 USD | 29,310.00 USD | `-20.88%` | `8,533.80` |
| `Live` | `Long` | `3.44` | 6,980,000.00 USD | 0.00 USD | 26,840.00 USD | `-20.65%` | `7,792.20` |
| `Live` | `Long` | `3.46` | 6,950,000.00 USD | 0.00 USD | 151,120.00 USD | `-20.42%` | `43,739.10` |
| `Live` | `Long` | `3.46` | 6,800,000.00 USD | 0.00 USD | 16,150.00 USD | `-20.19%` | `4,661.90` |
| `Live` | `Long` | `3.48` | 6,790,000.00 USD | 0.00 USD | 116,220.00 USD | `-19.96%` | `33,445.40` |
| `Live` | `Long` | `3.48` | 6,670,000.00 USD | 0.00 USD | 267,390.00 USD | `-19.73%` | `76,724.80` |
| `Live` | `Long` | `3.50` | 6,400,000.00 USD | 0.00 USD | 48,130.00 USD | `-19.50%` | `13,771.70` |
| `Live` | `Long` | `3.50` | 6,350,000.00 USD | 0.00 USD | 33,810.00 USD | `-19.27%` | `9,647.00` |
| `Live` | `Long` | `3.52` | 6,320,000.00 USD | 0.00 USD | 42,800.00 USD | `-19.04%` | `12,176.80` |
| `Live` | `Long` | `3.52` | 6,280,000.00 USD | 0.00 USD | 21,970.00 USD | `-18.81%` | `6,232.60` |
| `Live` | `Long` | `3.54` | 6,260,000.00 USD | 0.00 USD | 77,190.00 USD | `-18.58%` | `21,836.90` |
| `Live` | `Long` | `3.54` | 6,180,000.00 USD | 0.00 USD | 159,350.00 USD | `-18.35%` | `44,951.40` |
| `Live` | `Long` | `3.56` | 6,020,000.00 USD | 0.00 USD | 570,020.00 USD | `-18.12%` | `160,343.30` |
| `Live` | `Long` | `3.56` | 5,450,000.00 USD | 0.00 USD | 7,550.00 USD | `-17.89%` | `2,117.70` |
| `Live` | `Long` | `3.58` | 5,440,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-17.66%` | `373,566.50` |
| `Live` | `Long` | `3.58` | 4,110,000.00 USD | 0.00 USD | 52,750.00 USD | `-17.42%` | `14,714.40` |
| `Live` | `Long` | `3.60` | 4,050,000.00 USD | 0.00 USD | 23,850.00 USD | `-17.19%` | `6,633.20` |
| `Live` | `Long` | `3.60` | 4,030,000.00 USD | 0.00 USD | 63,970.00 USD | `-16.96%` | `17,746.00` |
| `Live` | `Long` | `3.62` | 3,970,000.00 USD | 0.00 USD | 102,890.00 USD | `-16.73%` | `28,462.50` |
| `Live` | `Long` | `3.62` | 3,860,000.00 USD | 0.00 USD | 114,340.00 USD | `-16.50%` | `31,542.70` |
| `Live` | `Long` | `3.63` | 3,750,000.00 USD | 0.00 USD | 1,670.00 USD | `-16.27%` | `458.20` |
| `Live` | `Long` | `3.65` | 3,750,000.00 USD | 0.00 USD | 333,140.00 USD | `-16.04%` | `91,395.10` |
| `Live` | `Long` | `3.65` | 3,410,000.00 USD | 0.00 USD | 20,750.00 USD | `-15.81%` | `5,676.60` |
| `Live` | `Long` | `3.67` | 3,390,000.00 USD | 0.00 USD | 171,100.00 USD | `-15.58%` | `46,685.60` |
| `Live` | `Long` | `3.67` | 3,220,000.00 USD | 0.00 USD | 95,680.00 USD | `-15.35%` | `26,036.10` |
| `Live` | `Long` | `3.69` | 3,130,000.00 USD | 0.00 USD | 224,510.00 USD | `-15.12%` | `60,924.30` |
| `Live` | `Long` | `3.69` | 2,900,000.00 USD | 0.00 USD | 93,310.00 USD | `-14.89%` | `25,252.00` |
| `Live` | `Long` | `3.71` | 2,810,000.00 USD | 0.00 USD | 79,950.00 USD | `-14.66%` | `21,579.30` |
| `Live` | `Long` | `3.71` | 2,730,000.00 USD | 0.00 USD | 11,810.00 USD | `-14.43%` | `3,180.20` |
| `Live` | `Long` | `3.73` | 2,720,000.00 USD | 0.00 USD | 224,430.00 USD | `-14.20%` | `60,250.20` |
| `Live` | `Long` | `3.73` | 2,490,000.00 USD | 0.00 USD | 119,590.00 USD | `-13.97%` | `32,019.80` |
| `Live` | `Long` | `3.75` | 2,370,000.00 USD | 0.00 USD | 25,820.00 USD | `-13.74%` | `6,895.80` |
| `Live` | `Long` | `3.75` | 2,350,000.00 USD | 0.00 USD | 150,270.00 USD | `-13.51%` | `40,017.50` |
| `Live` | `Long` | `3.77` | 2,200,000.00 USD | 0.00 USD | 65,080.00 USD | `-13.28%` | `17,286.40` |
| `Live` | `Long` | `3.77` | 2,130,000.00 USD | 0.00 USD | 29,390.00 USD | `-13.05%` | `7,786.10` |
| `Live` | `Long` | `3.79` | 2,100,000.00 USD | 0.00 USD | 59,430.00 USD | `-12.82%` | `15,701.60` |
| `Live` | `Long` | `3.79` | 2,040,000.00 USD | 0.00 USD | 37,390.00 USD | `-12.59%` | `9,851.70` |
| `Live` | `Long` | `3.81` | 2,010,000.00 USD | 0.00 USD | 570,030.00 USD | `-12.36%` | `149,810.30` |
| `Live` | `Long` | `3.81` | 1,440,000.00 USD | 0.00 USD | 14,090.00 USD | `-12.13%` | `3,694.00` |
| `Live` | `Long` | `3.83` | 1,420,000.00 USD | 0.00 USD | 134,350.00 USD | `-11.90%` | `35,123.90` |
| `Live` | `Long` | `3.83` | 1,290,000.00 USD | 0.00 USD | 171,380.00 USD | `-11.67%` | `44,688.70` |
| `Live` | `Long` | `3.85` | 1,120,000.00 USD | 0.00 USD | 116,490.00 USD | `-11.44%` | `30,296.00` |
| `Live` | `Long` | `3.85` | 998,740.00 USD | 0.00 USD | 22,330.00 USD | `-11.21%` | `5,792.70` |
| `Live` | `Long` | `3.87` | 976,410.00 USD | 0.00 USD | 71,550.00 USD | `-10.98%` | `18,512.20` |
| `Live` | `Long` | `3.88` | 904,860.00 USD | 0.00 USD | 7,870.00 USD | `-10.75%` | `2,030.50` |
| `Live` | `Long` | `3.88` | 896,990.00 USD | 0.00 USD | 175,650.00 USD | `-10.51%` | `45,213.00` |
| `Live` | `Long` | `3.90` | 721,340.00 USD | 0.00 USD | 93,930.00 USD | `-10.28%` | `24,116.30` |
| `Live` | `Long` | `3.90` | 627,410.00 USD | 0.00 USD | 8,860.00 USD | `-10.05%` | `2,268.20` |
| `Live` | `Long` | `3.92` | 618,550.00 USD | 0.00 USD | 132,720.00 USD | `-9.82%` | `33,899.30` |
| `Live` | `Long` | `3.92` | 485,830.00 USD | 0.00 USD | 2,050.00 USD | `-9.59%` | `522.20` |
| `Live` | `Long` | `3.94` | 483,780.00 USD | 0.00 USD | 3,320.00 USD | `-9.36%` | `844.50` |
| `Live` | `Long` | `3.94` | 480,460.00 USD | 0.00 USD | 22,630.00 USD | `-9.13%` | `5,736.60` |
| `Live` | `Long` | `3.96` | 457,830.00 USD | 0.00 USD | 55,290.00 USD | `-8.90%` | `13,979.20` |
| `Live` | `Long` | `3.96` | 402,540.00 USD | 0.00 USD | 2,110.00 USD | `-8.67%` | `533.00` |
| `Live` | `Long` | `3.98` | 400,430.00 USD | 0.00 USD | 26,000.00 USD | `-8.44%` | `6,541.70` |
| `Live` | `Long` | `3.98` | 374,420.00 USD | 0.00 USD | 1,070.00 USD | `-8.21%` | `268.00` |
| `Live` | `Long` | `4.00` | 373,360.00 USD | 0.00 USD | 160,840.00 USD | `-7.98%` | `40,260.30` |
| `Live` | `Long` | `4.00` | 212,520.00 USD | 0.00 USD | 13,260.00 USD | `-7.75%` | `3,311.20` |
| `Live` | `Long` | `4.01` | 199,250.00 USD | 0.00 USD | 275.83 USD | `-7.52%` | `68.70` |
| `Live` | `Long` | `4.03` | 198,980.00 USD | 0.00 USD | 2,110.00 USD | `-7.29%` | `524.90` |
| `Live` | `Long` | `4.04` | 196,870.00 USD | 0.00 USD | 24,650.00 USD | `-7.06%` | `6,108.60` |
| `Live` | `Long` | `4.04` | 172,220.00 USD | 0.00 USD | 21,310.00 USD | `-6.83%` | `5,268.70` |
| `Live` | `Long` | `4.05` | 150,910.00 USD | 0.00 USD | 54,890.00 USD | `-6.60%` | `13,535.60` |
| `Live` | `Long` | `4.07` | 96,020.00 USD | 0.00 USD | 1,200.00 USD | `-6.37%` | `295.00` |
| `Live` | `Long` | `4.08` | 94,820.00 USD | 0.00 USD | 2,640.00 USD | `-6.14%` | `647.70` |
| `Live` | `Long` | `4.08` | 92,180.00 USD | 0.00 USD | 8,310.00 USD | `-5.91%` | `2,034.10` |
| `Live` | `Long` | `4.09` | 83,870.00 USD | 0.00 USD | 19,450.00 USD | `-5.68%` | `4,748.50` |
| `Live` | `Long` | `4.11` | 64,430.00 USD | 0.00 USD | 25,410.00 USD | `-5.45%` | `6,191.00` |
| `Live` | `Long` | `4.12` | 39,010.00 USD | 0.00 USD | 16,830.00 USD | `-5.22%` | `4,089.40` |
| `Live` | `Long` | `4.12` | 22,180.00 USD | 0.00 USD | 10,570.00 USD | `-4.99%` | `2,562.30` |
| `Live` | `Long` | `4.13` | 11,610.00 USD | 0.00 USD | 2,230.00 USD | `-4.76%` | `539.70` |
| `Live` | `Long` | `4.14` | 9,380.00 USD | 0.00 USD | 652.84 USD | `-4.53%` | `157.50` |
| `Live` | `Long` | `4.16` | 8,730.00 USD | 0.00 USD | 8,730.00 USD | `-4.30%` | `2,101.20` |
| `Live` | `Short` | `4.24` | 15,550.00 USD | 15,550.00 USD | 0.00 USD | `-2.45%` | `3,670.90` |
| `Live` | `Short` | `4.39` | 196,310.00 USD | 180,760.00 USD | 0.00 USD | `+1.23%` | `41,128.80` |
| `Live` | `Short` | `4.42` | 198,240.00 USD | 1,930.00 USD | 0.00 USD | `+1.92%` | `436.00` |
| `Live` | `Short` | `4.43` | 201,770.00 USD | 3,540.00 USD | 0.00 USD | `+2.15%` | `797.70` |
| `Live` | `Short` | `4.45` | 202,130.00 USD | 358.27 USD | 0.00 USD | `+2.38%` | `80.60` |
| `Live` | `Short` | `4.46` | 238,820.00 USD | 36,680.00 USD | 0.00 USD | `+2.61%` | `8,234.00` |
| `Live` | `Short` | `4.46` | 240,190.00 USD | 1,370.00 USD | 0.00 USD | `+2.84%` | `306.90` |
| `Live` | `Short` | `4.47` | 257,580.00 USD | 17,400.00 USD | 0.00 USD | `+3.07%` | `3,887.90` |
| `Live` | `Short` | `4.49` | 260,560.00 USD | 2,970.00 USD | 0.00 USD | `+3.31%` | `663.30` |
| `Live` | `Short` | `4.50` | 283,230.00 USD | 22,680.00 USD | 0.00 USD | `+3.54%` | `5,044.50` |
| `Live` | `Short` | `4.50` | 291,180.00 USD | 7,940.00 USD | 0.00 USD | `+3.77%` | `1,763.30` |
| `Live` | `Short` | `4.51` | 300,730.00 USD | 9,560.00 USD | 0.00 USD | `+4.00%` | `2,116.70` |
| `Live` | `Short` | `4.53` | 307,850.00 USD | 7,110.00 USD | 0.00 USD | `+4.23%` | `1,572.30` |
| `Live` | `Short` | `4.54` | 315,170.00 USD | 7,320.00 USD | 0.00 USD | `+4.46%` | `1,614.30` |
| `Live` | `Short` | `4.54` | 325,240.00 USD | 10,070.00 USD | 0.00 USD | `+4.69%` | `2,215.40` |
| `Live` | `Short` | `4.55` | 339,350.00 USD | 14,110.00 USD | 0.00 USD | `+4.92%` | `3,098.50` |
| `Live` | `Short` | `4.57` | 348,140.00 USD | 8,790.00 USD | 0.00 USD | `+5.15%` | `1,925.70` |
| `Live` | `Short` | `4.58` | 349,940.00 USD | 1,800.00 USD | 0.00 USD | `+5.61%` | `391.60` |
| `Live` | `Short` | `4.62` | 401,630.00 USD | 51,690.00 USD | 0.00 USD | `+6.53%` | `11,176.20` |
| `Live` | `Short` | `4.63` | 551,900.00 USD | 150,270.00 USD | 0.00 USD | `+6.76%` | `32,421.00` |
| `Live` | `Short` | `4.64` | 552,750.00 USD | 852.82 USD | 0.00 USD | `+6.99%` | `183.60` |
| `Live` | `Short` | `4.66` | 553,510.00 USD | 756.44 USD | 0.00 USD | `+7.22%` | `162.50` |
| `Live` | `Short` | `4.67` | 561,390.00 USD | 7,880.00 USD | 0.00 USD | `+7.45%` | `1,688.80` |
| `Live` | `Short` | `4.67` | 616,030.00 USD | 54,640.00 USD | 0.00 USD | `+7.68%` | `11,687.70` |
| `Live` | `Short` | `4.68` | 617,060.00 USD | 1,030.00 USD | 0.00 USD | `+7.91%` | `220.50` |
| `Live` | `Short` | `4.70` | 617,290.00 USD | 230.06 USD | 0.00 USD | `+8.14%` | `49.00` |
| `Live` | `Short` | `4.71` | 624,250.00 USD | 6,960.00 USD | 0.00 USD | `+8.37%` | `1,479.20` |
| `Live` | `Short` | `4.72` | 637,050.00 USD | 12,800.00 USD | 0.00 USD | `+8.83%` | `2,709.30` |
| `Live` | `Short` | `4.74` | 640,900.00 USD | 3,850.00 USD | 0.00 USD | `+9.06%` | `812.50` |
| `Live` | `Short` | `4.75` | 752,030.00 USD | 111,130.00 USD | 0.00 USD | `+9.29%` | `23,421.00` |
| `Live` | `Short` | `4.76` | 847,330.00 USD | 95,300.00 USD | 0.00 USD | `+9.75%` | `20,000.00` |
| `Live` | `Short` | `4.78` | 849,060.00 USD | 1,730.00 USD | 0.00 USD | `+9.99%` | `362.40` |
| `Live` | `Short` | `4.79` | 849,210.00 USD | 143.55 USD | 0.00 USD | `+10.22%` | `30.00` |
| `Live` | `Short` | `4.79` | 850,540.00 USD | 1,330.00 USD | 0.00 USD | `+10.45%` | `277.70` |
| `Live` | `Short` | `4.82` | 856,320.00 USD | 5,780.00 USD | 0.00 USD | `+10.91%` | `1,200.00` |
| `Live` | `Short` | `4.83` | 858,670.00 USD | 2,360.00 USD | 0.00 USD | `+11.14%` | `489.00` |
| `Live` | `Short` | `4.83` | 860,210.00 USD | 1,540.00 USD | 0.00 USD | `+11.37%` | `317.90` |
| `Live` | `Short` | `4.84` | 871,430.00 USD | 11,220.00 USD | 0.00 USD | `+11.60%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 871,690.00 USD | 259.79 USD | 0.00 USD | `+12.06%` | `53.40` |
| `Live` | `Short` | `4.88` | 872,520.00 USD | 827.03 USD | 0.00 USD | `+12.52%` | `169.30` |
| `Live` | `Short` | `4.91` | 873,200.00 USD | 674.44 USD | 0.00 USD | `+12.98%` | `137.50` |
| `Live` | `Short` | `4.92` | 893,910.00 USD | 20,720.00 USD | 0.00 USD | `+13.21%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 896,500.00 USD | 2,590.00 USD | 0.00 USD | `+13.44%` | `526.30` |
| `Live` | `Short` | `4.93` | 908,810.00 USD | 12,300.00 USD | 0.00 USD | `+13.67%` | `2,493.30` |
| `Live` | `Short` | `4.96` | 909,300.00 USD | 488.56 USD | 0.00 USD | `+14.13%` | `98.60` |
| `Live` | `Short` | `4.97` | 1,010,000.00 USD | 99,370.00 USD | 0.00 USD | `+14.59%` | `19,974.00` |
| `Live` | `Short` | `5.04` | 1,010,000.00 USD | 118.83 USD | 0.00 USD | `+15.97%` | `23.60` |
| `Live` | `Short` | `5.05` | 1,040,000.00 USD | 35,380.00 USD | 0.00 USD | `+16.43%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,050,000.00 USD | 3,420.00 USD | 0.00 USD | `+16.66%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,050,000.00 USD | 6,860.00 USD | 0.00 USD | `+17.13%` | `1,349.30` |
| `Live` | `Short` | `5.09` | 1,060,000.00 USD | 6,650.00 USD | 0.00 USD | `+17.36%` | `1,306.10` |
| `Live` | `Short` | `5.12` | 1,110,000.00 USD | 51,430.00 USD | 0.00 USD | `+18.05%` | `10,034.70` |
| `Live` | `Short` | `5.16` | 1,120,000.00 USD | 2,580.00 USD | 0.00 USD | `+18.74%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,120,000.00 USD | 751.51 USD | 0.00 USD | `+18.97%` | `145.50` |
| `Live` | `Short` | `5.22` | 1,190,000.00 USD | 72,940.00 USD | 0.00 USD | `+20.35%` | `13,959.60` |
| `Live` | `Short` | `5.24` | 1,210,000.00 USD | 17,260.00 USD | 0.00 USD | `+20.58%` | `3,297.00` |
| `Live` | `Short` | `5.25` | 1,210,000.00 USD | 143.71 USD | 0.00 USD | `+20.81%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,220,000.00 USD | 17,380.00 USD | 0.00 USD | `+21.04%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,230,000.00 USD | 6,220.00 USD | 0.00 USD | `+21.27%` | `1,181.40` |
| `Live` | `Short` | `5.29` | 1,230,000.00 USD | 134.77 USD | 0.00 USD | `+21.73%` | `25.50` |
| `Live` | `Short` | `5.30` | 1,230,000.00 USD | 524.66 USD | 0.00 USD | `+22.19%` | `98.90` |
| `Live` | `Short` | `5.33` | 2,300,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+22.88%` | `200,053.70` |
| `Live` | `Short` | `5.34` | 2,600,000.00 USD | 298,680.00 USD | 0.00 USD | `+23.11%` | `55,879.90` |
| `Live` | `Short` | `5.36` | 2,600,000.00 USD | 142.44 USD | 0.00 USD | `+23.34%` | `26.60` |
| `Live` | `Short` | `5.38` | 2,630,000.00 USD | 37,990.00 USD | 0.00 USD | `+23.81%` | `7,068.80` |
| `Live` | `Short` | `5.42` | 2,950,000.00 USD | 313,840.00 USD | 0.00 USD | `+24.73%` | `57,958.30` |
| `Live` | `Short` | `5.42` | 2,950,000.00 USD | 914.65 USD | 0.00 USD | `+24.96%` | `168.60` |
| `Live` | `Short` | `5.43` | 2,950,000.00 USD | 419.04 USD | 0.00 USD | `+25.19%` | `77.10` |
| `Live` | `Short` | `5.47` | 2,960,000.00 USD | 12,190.00 USD | 0.00 USD | `+26.11%` | `2,226.70` |
| `Live` | `Short` | `5.50` | 3,090,000.00 USD | 128,840.00 USD | 0.00 USD | `+26.57%` | `23,447.00` |
| `Live` | `Short` | `5.50` | 3,100,000.00 USD | 12,780.00 USD | 0.00 USD | `+26.80%` | `2,322.30` |
| `Live` | `Short` | `5.53` | 3,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.26%` | `229.80` |
| `Live` | `Short` | `5.54` | 3,110,000.00 USD | 209.22 USD | 0.00 USD | `+27.49%` | `37.80` |
| `Live` | `Short` | `5.57` | 3,110,000.00 USD | 8,670.00 USD | 0.00 USD | `+28.18%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 3,180,000.00 USD | 62,420.00 USD | 0.00 USD | `+28.64%` | `11,175.80` |
| `Live` | `Short` | `5.62` | 3,180,000.00 USD | 532.69 USD | 0.00 USD | `+29.56%` | `94.70` |
| `Live` | `Short` | `5.67` | 8,600,000.00 USD | 5,420,000.00 USD | 0.00 USD | `+30.48%` | `957,107.60` |
| `Live` | `Short` | `5.67` | 8,600,000.00 USD | 228.70 USD | 0.00 USD | `+30.72%` | `40.30` |
| `Live` | `Short` | `5.68` | 8,620,000.00 USD | 26,090.00 USD | 0.00 USD | `+30.95%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 8,630,000.00 USD | 1,520.00 USD | 0.00 USD | `+31.18%` | `267.40` |
| `Live` | `Short` | `5.71` | 8,630,000.00 USD | 2,130.00 USD | 0.00 USD | `+31.64%` | `372.40` |
| `Live` | `Short` | `5.75` | 9,110,000.00 USD | 481,600.00 USD | 0.00 USD | `+32.33%` | `83,830.20` |
| `Live` | `Short` | `5.75` | 9,110,000.00 USD | 286.02 USD | 0.00 USD | `+32.56%` | `49.70` |
| `Live` | `Short` | `5.79` | 9,130,000.00 USD | 16,050.00 USD | 0.00 USD | `+33.48%` | `2,769.00` |
| `Live` | `Short` | `5.83` | 9,130,000.00 USD | 198.97 USD | 0.00 USD | `+34.40%` | `34.10` |
| `Live` | `Short` | `5.84` | 9,130,000.00 USD | 310.95 USD | 0.00 USD | `+34.63%` | `53.20` |
| `Live` | `Short` | `5.86` | 9,130,000.00 USD | 848.39 USD | 0.00 USD | `+34.86%` | `144.90` |
| `Live` | `Short` | `5.88` | 9,130,000.00 USD | 190.67 USD | 0.00 USD | `+35.55%` | `32.40` |
| `Live` | `Short` | `5.89` | 9,240,000.00 USD | 112,780.00 USD | 0.00 USD | `+35.78%` | `19,131.80` |
| `Live` | `Short` | `5.91` | 9,240,000.00 USD | 162.98 USD | 0.00 USD | `+36.01%` | `27.60` |
| `Live` | `Short` | `5.92` | 9,240,000.00 USD | 189.28 USD | 0.00 USD | `+36.24%` | `32.00` |
| `Live` | `Short` | `5.95` | 9,340,000.00 USD | 103,650.00 USD | 0.00 USD | `+36.93%` | `17,434.80` |
| `Live` | `Short` | `5.96` | 9,370,000.00 USD | 29,860.00 USD | 0.00 USD | `+37.16%` | `5,014.50` |
| `Live` | `Short` | `6.00` | 9,400,000.00 USD | 23,320.00 USD | 0.00 USD | `+38.32%` | `3,883.80` |
| `Live` | `Short` | `6.07` | 9,400,000.00 USD | 740.54 USD | 0.00 USD | `+39.70%` | `122.10` |
| `Live` | `Short` | `6.08` | 9,410,000.00 USD | 7,290.00 USD | 0.00 USD | `+40.16%` | `1,198.10` |
| `Live` | `Short` | `6.09` | 9,440,000.00 USD | 37,510.00 USD | 0.00 USD | `+40.39%` | `6,154.10` |
| `Live` | `Short` | `6.12` | 9,470,000.00 USD | 28,250.00 USD | 0.00 USD | `+41.08%` | `4,611.60` |
| `Live` | `Short` | `6.13` | 9,470,000.00 USD | 2,430.00 USD | 0.00 USD | `+41.31%` | `396.10` |
| `Live` | `Short` | `6.14` | 9,480,000.00 USD | 1,870.00 USD | 0.00 USD | `+41.54%` | `305.00` |
| `Live` | `Short` | `6.16` | 9,490,000.00 USD | 12,760.00 USD | 0.00 USD | `+41.77%` | `2,073.30` |
| `Live` | `Short` | `6.18` | 9,520,000.00 USD | 35,350.00 USD | 0.00 USD | `+42.46%` | `5,715.90` |
| `Live` | `Short` | `6.22` | 9,530,000.00 USD | 2,010.00 USD | 0.00 USD | `+43.38%` | `323.00` |
| `Live` | `Short` | `6.24` | 10,050,000.00 USD | 526,230.00 USD | 0.00 USD | `+43.61%` | `84,400.00` |
| `Live` | `Short` | `6.25` | 10,320,000.00 USD | 262,530.00 USD | 0.00 USD | `+43.84%` | `42,038.20` |
| `Live` | `Short` | `6.25` | 10,320,000.00 USD | 439.10 USD | 0.00 USD | `+44.07%` | `70.20` |
| `Live` | `Short` | `6.29` | 10,320,000.00 USD | 5,360.00 USD | 0.00 USD | `+44.77%` | `852.80` |
| `Live` | `Short` | `6.29` | 10,660,000.00 USD | 336,800.00 USD | 0.00 USD | `+45.00%` | `53,503.40` |
| `Live` | `Short` | `6.32` | 10,660,000.00 USD | 310.70 USD | 0.00 USD | `+45.46%` | `49.20` |
| `Live` | `Short` | `6.33` | 10,660,000.00 USD | 382.00 USD | 0.00 USD | `+45.92%` | `60.30` |
| `Live` | `Short` | `6.34` | 10,660,000.00 USD | 214.46 USD | 0.00 USD | `+46.15%` | `33.80` |
| `Live` | `Short` | `6.37` | 10,660,000.00 USD | 113.93 USD | 0.00 USD | `+46.61%` | `17.90` |
| `Live` | `Short` | `6.38` | 10,660,000.00 USD | 288.15 USD | 0.00 USD | `+46.84%` | `45.20` |
| `Live` | `Short` | `6.39` | 10,660,000.00 USD | 2,000.00 USD | 0.00 USD | `+47.30%` | `312.80` |
| `Live` | `Short` | `6.41` | 10,660,000.00 USD | 3,780.00 USD | 0.00 USD | `+47.53%` | `590.10` |
| `Live` | `Short` | `6.42` | 10,670,000.00 USD | 943.65 USD | 0.00 USD | `+47.76%` | `147.10` |
| `Live` | `Short` | `6.42` | 10,670,000.00 USD | 173.47 USD | 0.00 USD | `+47.99%` | `27.00` |
| `Live` | `Short` | `6.45` | 10,670,000.00 USD | 5,270.00 USD | 0.00 USD | `+48.45%` | `818.40` |
| `Live` | `Short` | `6.46` | 39,770,000.00 USD | 29,100,000.00 USD | 0.00 USD | `+48.68%` | `4,508,369.60` |
| `Live` | `Short` | `6.46` | 39,770,000.00 USD | 1,940.00 USD | 0.00 USD | `+48.91%` | `300.00` |
| `Live` | `Short` | `6.51` | 39,800,000.00 USD | 24,040.00 USD | 0.00 USD | `+50.06%` | `3,689.70` |
| `Live` | `Short` | `6.54` | 39,800,000.00 USD | 265.07 USD | 0.00 USD | `+50.75%` | `40.50` |
| `Live` | `Short` | `6.57` | 39,810,000.00 USD | 7,670.00 USD | 0.00 USD | `+51.22%` | `1,168.60` |
| `Live` | `Short` | `6.59` | 39,810,000.00 USD | 418.78 USD | 0.00 USD | `+51.91%` | `63.50` |
| `Live` | `Short` | `6.62` | 41,050,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+52.37%` | `188,000.00` |
| `Live` | `Short` | `6.62` | 41,090,000.00 USD | 42,100.00 USD | 0.00 USD | `+52.60%` | `6,354.10` |
| `Live` | `Short` | `6.63` | 41,090,000.00 USD | 2,090.00 USD | 0.00 USD | `+52.83%` | `315.60` |
| `Live` | `Short` | `6.66` | 41,100,000.00 USD | 7,940.00 USD | 0.00 USD | `+53.29%` | `1,193.00` |
| `Live` | `Short` | `6.67` | 41,100,000.00 USD | 233.94 USD | 0.00 USD | `+53.52%` | `35.10` |
| `Live` | `Short` | `6.67` | 41,140,000.00 USD | 41,520.00 USD | 0.00 USD | `+53.75%` | `6,220.00` |
| `Live` | `Short` | `6.68` | 41,180,000.00 USD | 37,150.00 USD | 0.00 USD | `+53.98%` | `5,556.90` |
| `Live` | `Short` | `6.71` | 41,570,000.00 USD | 388,480.00 USD | 0.00 USD | `+54.44%` | `57,938.40` |
| `Live` | `Short` | `6.75` | 42,820,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+55.59%` | `184,501.00` |
| `Live` | `Short` | `6.83` | 42,820,000.00 USD | 187.69 USD | 0.00 USD | `+57.20%` | `27.50` |
| `Live` | `Short` | `6.84` | 42,820,000.00 USD | 753.63 USD | 0.00 USD | `+57.66%` | `110.10` |
| `Live` | `Short` | `6.86` | 42,820,000.00 USD | 623.81 USD | 0.00 USD | `+57.89%` | `91.00` |
| `Live` | `Short` | `6.87` | 42,820,000.00 USD | 2,650.00 USD | 0.00 USD | `+58.13%` | `386.60` |
| `Live` | `Short` | `6.92` | 42,830,000.00 USD | 7,900.00 USD | 0.00 USD | `+59.51%` | `1,140.60` |
| `Live` | `Short` | `6.99` | 42,920,000.00 USD | 94,030.00 USD | 0.00 USD | `+60.89%` | `13,462.20` |
| `Live` | `Short` | `7.00` | 42,950,000.00 USD | 24,680.00 USD | 0.00 USD | `+61.35%` | `3,523.00` |
| `Live` | `Short` | `7.09` | 42,950,000.00 USD | 699.57 USD | 0.00 USD | `+63.42%` | `98.60` |
| `Live` | `Short` | `7.16` | 42,960,000.00 USD | 16,010.00 USD | 0.00 USD | `+64.80%` | `2,237.40` |
| `Live` | `Short` | `7.21` | 42,980,000.00 USD | 17,040.00 USD | 0.00 USD | `+66.19%` | `2,361.10` |
| `Live` | `Short` | `7.24` | 42,980,000.00 USD | 1,150.00 USD | 0.00 USD | `+66.65%` | `159.30` |
| `Live` | `Short` | `7.25` | 42,990,000.00 USD | 3,770.00 USD | 0.00 USD | `+66.88%` | `520.00` |
| `Live` | `Short` | `7.28` | 42,990,000.00 USD | 2,260.00 USD | 0.00 USD | `+67.57%` | `310.00` |
| `Live` | `Short` | `7.30` | 43,040,000.00 USD | 54,790.00 USD | 0.00 USD | `+68.26%` | `7,500.00` |
| `Live` | `Short` | `7.32` | 46,930,000.00 USD | 3,880,000.00 USD | 0.00 USD | `+68.49%` | `531,079.30` |
| `Live` | `Short` | `7.33` | 46,940,000.00 USD | 14,160.00 USD | 0.00 USD | `+68.95%` | `1,930.00` |
| `Live` | `Short` | `7.42` | 46,940,000.00 USD | 777.09 USD | 0.00 USD | `+70.79%` | `104.80` |
| `Live` | `Short` | `7.42` | 47,050,000.00 USD | 106,000.00 USD | 0.00 USD | `+71.02%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 57,010,000.00 USD | 9,960,000.00 USD | 0.00 USD | `+71.71%` | `1,336,191.10` |
| `Live` | `Short` | `7.50` | 57,010,000.00 USD | 481.82 USD | 0.00 USD | `+72.87%` | `64.20` |
| `Live` | `Short` | `7.53` | 57,010,000.00 USD | 1,570.00 USD | 0.00 USD | `+73.33%` | `208.40` |
| `Live` | `Short` | `7.54` | 64,850,000.00 USD | 7,840,000.00 USD | 0.00 USD | `+73.56%` | `1,040,428.20` |
| `Live` | `Short` | `7.55` | 64,850,000.00 USD | 115.59 USD | 0.00 USD | `+74.02%` | `15.30` |
| `Live` | `Short` | `7.62` | 64,860,000.00 USD | 9,100.00 USD | 0.00 USD | `+75.40%` | `1,194.40` |
| `Live` | `Short` | `7.63` | 64,910,000.00 USD | 45,910.00 USD | 0.00 USD | `+75.86%` | `6,012.60` |
| `Live` | `Short` | `7.64` | 64,920,000.00 USD | 17,820.00 USD | 0.00 USD | `+76.09%` | `2,330.50` |
| `Live` | `Short` | `7.66` | 64,970,000.00 USD | 46,030.00 USD | 0.00 USD | `+76.32%` | `6,012.80` |
| `Live` | `Short` | `7.67` | 64,970,000.00 USD | 360.25 USD | 0.00 USD | `+76.55%` | `47.00` |
| `Live` | `Short` | `7.71` | 64,980,000.00 USD | 4,450.00 USD | 0.00 USD | `+77.47%` | `577.20` |
| `Live` | `Short` | `7.72` | 66,170,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+77.93%` | `154,780.70` |
| `Live` | `Short` | `7.74` | 66,210,000.00 USD | 33,830.00 USD | 0.00 USD | `+78.16%` | `4,373.90` |
| `Live` | `Short` | `7.75` | 66,210,000.00 USD | 629.67 USD | 0.00 USD | `+78.39%` | `81.30` |
| `Live` | `Short` | `7.76` | 66,210,000.00 USD | 1,680.00 USD | 0.00 USD | `+78.86%` | `216.50` |
| `Live` | `Short` | `7.87` | 66,210,000.00 USD | 2,980.00 USD | 0.00 USD | `+81.16%` | `378.70` |
| `Live` | `Short` | `7.92` | 66,220,000.00 USD | 12,000.00 USD | 0.00 USD | `+82.54%` | `1,514.20` |
| `Live` | `Short` | `7.95` | 66,230,000.00 USD | 6,120.00 USD | 0.00 USD | `+83.00%` | `769.80` |
| `Live` | `Short` | `7.99` | 66,230,000.00 USD | 399.25 USD | 0.00 USD | `+83.92%` | `50.00` |
| `Live` | `Short` | `8.03` | 66,660,000.00 USD | 435,580.00 USD | 0.00 USD | `+84.84%` | `54,278.30` |
| `Live` | `Short` | `8.07` | 66,670,000.00 USD | 6,460.00 USD | 0.00 USD | `+86.00%` | `800.00` |
| `Live` | `Short` | `8.09` | 66,770,000.00 USD | 97,280.00 USD | 0.00 USD | `+86.23%` | `12,032.20` |
| `Live` | `Short` | `8.20` | 66,770,000.00 USD | 951.44 USD | 0.00 USD | `+88.76%` | `116.10` |
| `Live` | `Short` | `8.29` | 66,770,000.00 USD | 165.07 USD | 0.00 USD | `+91.06%` | `19.90` |
| `Live` | `Short` | `8.34` | 66,870,000.00 USD | 96,080.00 USD | 0.00 USD | `+91.98%` | `11,527.10` |
| `Live` | `Short` | `8.35` | 66,890,000.00 USD | 25,310.00 USD | 0.00 USD | `+92.21%` | `3,032.60` |
| `Live` | `Short` | `8.38` | 66,890,000.00 USD | 191.79 USD | 0.00 USD | `+92.91%` | `22.90` |
| `Live` | `Short` | `8.43` | 66,890,000.00 USD | 1,220.00 USD | 0.00 USD | `+94.06%` | `145.00` |
| `Live` | `Short` | `8.44` | 66,900,000.00 USD | 8,770.00 USD | 0.00 USD | `+94.29%` | `1,039.60` |
| `Live` | `Short` | `8.47` | 66,900,000.00 USD | 816.99 USD | 0.00 USD | `+95.21%` | `96.40` |
| `Live` | `Short` | `8.48` | 66,910,000.00 USD | 6,640.00 USD | 0.00 USD | `+95.44%` | `782.50` |
| `Live` | `Short` | `8.49` | 66,930,000.00 USD | 25,490.00 USD | 0.00 USD | `+95.67%` | `3,000.00` |
| `Live` | `Short` | `8.52` | 66,950,000.00 USD | 17,500.00 USD | 0.00 USD | `+96.13%` | `2,054.80` |
| `Live` | `Short` | `8.53` | 66,990,000.00 USD | 34,680.00 USD | 0.00 USD | `+96.36%` | `4,068.00` |
| `Live` | `Short` | `8.54` | 66,990,000.00 USD | 127.17 USD | 0.00 USD | `+96.59%` | `14.90` |
| `Live` | `Short` | `8.54` | 66,990,000.00 USD | 124.76 USD | 0.00 USD | `+96.82%` | `14.60` |
| `Live` | `Short` | `8.59` | 67,420,000.00 USD | 432,220.00 USD | 0.00 USD | `+97.74%` | `50,346.40` |
| `Live` | `Short` | `8.60` | 67,420,000.00 USD | 240.66 USD | 0.00 USD | `+97.97%` | `28.00` |
| `Live` | `Short` | `8.61` | 67,470,000.00 USD | 54,210.00 USD | 0.00 USD | `+98.20%` | `6,300.00` |
| `Live` | `Short` | `8.62` | 67,480,000.00 USD | 4,950.00 USD | 0.00 USD | `+98.43%` | `574.10` |
| `Live` | `Short` | `8.68` | 67,480,000.00 USD | 2,320.00 USD | 0.00 USD | `+99.82%` | `267.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,170,000.00 USD | 0.00 USD | 585.51 USD | `-76.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,170,000.00 USD | 0.00 USD | 339.82 USD | `-76.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,170,000.00 USD | 0.00 USD | 196.58 USD | `-72.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,170,000.00 USD | 0.00 USD | 331.54 USD | `-69.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,170,000.00 USD | 0.00 USD | 345.25 USD | `-68.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,170,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,160,000.00 USD | 0.00 USD | 997.29 USD | `-67.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.49` | 3,160,000.00 USD | 0.00 USD | 582.71 USD | `-65.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,160,000.00 USD | 0.00 USD | 139.83 USD | `-65.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,160,000.00 USD | 0.00 USD | 113.28 USD | `-64.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,160,000.00 USD | 0.00 USD | 4,000.00 USD | `-64.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,160,000.00 USD | 0.00 USD | 950.26 USD | `-64.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,150,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,150,000.00 USD | 0.00 USD | 739.67 USD | `-62.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,150,000.00 USD | 0.00 USD | 1,740.00 USD | `-62.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,150,000.00 USD | 0.00 USD | 6,260.00 USD | `-62.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,140,000.00 USD | 0.00 USD | 345.40 USD | `-61.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,140,000.00 USD | 0.00 USD | 167.50 USD | `-61.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,140,000.00 USD | 0.00 USD | 669.02 USD | `-60.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,140,000.00 USD | 0.00 USD | 105.88 USD | `-60.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,140,000.00 USD | 0.00 USD | 172.50 USD | `-60.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,140,000.00 USD | 0.00 USD | 10,650.00 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,130,000.00 USD | 0.00 USD | 722.00 USD | `-58.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,130,000.00 USD | 0.00 USD | 259.00 USD | `-58.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,130,000.00 USD | 0.00 USD | 103.84 USD | `-57.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,130,000.00 USD | 0.00 USD | 109.00 USD | `-57.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,130,000.00 USD | 0.00 USD | 222.19 USD | `-56.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,130,000.00 USD | 0.00 USD | 10,280.00 USD | `-56.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,120,000.00 USD | 0.00 USD | 558.36 USD | `-56.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,120,000.00 USD | 0.00 USD | 1,520.00 USD | `-55.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,120,000.00 USD | 0.00 USD | 222.14 USD | `-55.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,120,000.00 USD | 0.00 USD | 279.50 USD | `-55.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,120,000.00 USD | 0.00 USD | 197.50 USD | `-54.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,110,000.00 USD | 0.00 USD | 935.66 USD | `-54.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,110,000.00 USD | 0.00 USD | 18,860.00 USD | `-53.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,100,000.00 USD | 0.00 USD | 3,020.00 USD | `-53.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,090,000.00 USD | 0.00 USD | 214.52 USD | `-52.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,090,000.00 USD | 0.00 USD | 1,200.00 USD | `-52.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,090,000.00 USD | 0.00 USD | 578.41 USD | `-52.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,090,000.00 USD | 0.00 USD | 18,070.00 USD | `-51.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,070,000.00 USD | 0.00 USD | 108.62 USD | `-51.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,070,000.00 USD | 0.00 USD | 107.23 USD | `-51.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,070,000.00 USD | 0.00 USD | 1,590.00 USD | `-51.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,070,000.00 USD | 0.00 USD | 5,830.00 USD | `-50.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,060,000.00 USD | 0.00 USD | 310.32 USD | `-50.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,060,000.00 USD | 0.00 USD | 1,170.00 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,060,000.00 USD | 0.00 USD | 576.18 USD | `-49.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,060,000.00 USD | 0.00 USD | 295.67 USD | `-49.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,060,000.00 USD | 0.00 USD | 1,430.00 USD | `-49.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,060,000.00 USD | 0.00 USD | 812.68 USD | `-48.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,060,000.00 USD | 0.00 USD | 1,440.00 USD | `-48.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,060,000.00 USD | 0.00 USD | 106.16 USD | `-48.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,060,000.00 USD | 0.00 USD | 6,270.00 USD | `-48.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,050,000.00 USD | 0.00 USD | 478.06 USD | `-48.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,050,000.00 USD | 0.00 USD | 540.88 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,050,000.00 USD | 0.00 USD | 867.46 USD | `-47.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,050,000.00 USD | 0.00 USD | 759.76 USD | `-47.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,050,000.00 USD | 0.00 USD | 11,060.00 USD | `-47.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,040,000.00 USD | 0.00 USD | 3,690.00 USD | `-46.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,030,000.00 USD | 0.00 USD | 10,280.00 USD | `-46.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,020,000.00 USD | 0.00 USD | 467.00 USD | `-46.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,020,000.00 USD | 0.00 USD | 506.75 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,020,000.00 USD | 0.00 USD | 214.27 USD | `-45.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,020,000.00 USD | 0.00 USD | 428.69 USD | `-45.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,020,000.00 USD | 0.00 USD | 322.45 USD | `-45.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,020,000.00 USD | 0.00 USD | 108.25 USD | `-44.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,020,000.00 USD | 0.00 USD | 3,900.00 USD | `-44.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,020,000.00 USD | 0.00 USD | 799.04 USD | `-44.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,020,000.00 USD | 0.00 USD | 6,830.00 USD | `-43.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,010,000.00 USD | 0.00 USD | 137.16 USD | `-43.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,010,000.00 USD | 0.00 USD | 504.41 USD | `-42.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,010,000.00 USD | 0.00 USD | 963.93 USD | `-42.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,010,000.00 USD | 0.00 USD | 6,690.00 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,000,000.00 USD | 0.00 USD | 541.98 USD | `-42.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,000,000.00 USD | 0.00 USD | 108.75 USD | `-41.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,000,000.00 USD | 0.00 USD | 766.55 USD | `-41.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,000,000.00 USD | 0.00 USD | 7,110.00 USD | `-41.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,990,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,990,000.00 USD | 0.00 USD | 100.04 USD | `-40.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,990,000.00 USD | 0.00 USD | 743.47 USD | `-40.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,990,000.00 USD | 0.00 USD | 5,090.00 USD | `-39.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,990,000.00 USD | 0.00 USD | 226.57 USD | `-38.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,990,000.00 USD | 0.00 USD | 104.98 USD | `-38.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,990,000.00 USD | 0.00 USD | 889.89 USD | `-37.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,990,000.00 USD | 0.00 USD | 7,270.00 USD | `-37.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,980,000.00 USD | 0.00 USD | 107.21 USD | `-37.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,980,000.00 USD | 0.00 USD | 197.37 USD | `-36.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,980,000.00 USD | 0.00 USD | 8,110.00 USD | `-36.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,970,000.00 USD | 0.00 USD | 108.39 USD | `-36.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,970,000.00 USD | 0.00 USD | 435.95 USD | `-36.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,970,000.00 USD | 0.00 USD | 217.23 USD | `-35.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,970,000.00 USD | 0.00 USD | 437.98 USD | `-35.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,970,000.00 USD | 0.00 USD | 1,230.00 USD | `-35.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,970,000.00 USD | 0.00 USD | 8,380.00 USD | `-34.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,960,000.00 USD | 0.00 USD | 283.50 USD | `-34.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,960,000.00 USD | 0.00 USD | 109.53 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,960,000.00 USD | 0.00 USD | 1,230.00 USD | `-34.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,960,000.00 USD | 0.00 USD | 1,960.00 USD | `-33.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,960,000.00 USD | 0.00 USD | 157.81 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,960,000.00 USD | 0.00 USD | 2,900.00 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,950,000.00 USD | 0.00 USD | 4,870.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,950,000.00 USD | 0.00 USD | 1,320.00 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,950,000.00 USD | 0.00 USD | 493.15 USD | `-32.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,950,000.00 USD | 0.00 USD | 1,560.00 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,940,000.00 USD | 0.00 USD | 24,200.00 USD | `-32.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,920,000.00 USD | 0.00 USD | 738.75 USD | `-31.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,920,000.00 USD | 0.00 USD | 523.32 USD | `-31.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,920,000.00 USD | 0.00 USD | 4,470.00 USD | `-31.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,910,000.00 USD | 0.00 USD | 12,170.00 USD | `-30.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,900,000.00 USD | 0.00 USD | 1,020.00 USD | `-30.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,900,000.00 USD | 0.00 USD | 214.57 USD | `-30.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,900,000.00 USD | 0.00 USD | 249.08 USD | `-29.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,900,000.00 USD | 0.00 USD | 305.50 USD | `-29.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,900,000.00 USD | 0.00 USD | 109.42 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,900,000.00 USD | 0.00 USD | 9,300.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,890,000.00 USD | 0.00 USD | 8,570.00 USD | `-28.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,880,000.00 USD | 0.00 USD | 104.69 USD | `-28.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,880,000.00 USD | 0.00 USD | 315.69 USD | `-27.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,880,000.00 USD | 0.00 USD | 214.17 USD | `-27.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,880,000.00 USD | 0.00 USD | 329.07 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,880,000.00 USD | 0.00 USD | 4,210.00 USD | `-27.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,880,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,880,000.00 USD | 0.00 USD | 218.81 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,880,000.00 USD | 0.00 USD | 24,840.00 USD | `-26.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,850,000.00 USD | 0.00 USD | 144.67 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 2,850,000.00 USD | 0.00 USD | 273,030.00 USD | `-25.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,580,000.00 USD | 0.00 USD | 27,380.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,550,000.00 USD | 0.00 USD | 1,530.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,550,000.00 USD | 0.00 USD | 104.81 USD | `-24.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,550,000.00 USD | 0.00 USD | 200.10 USD | `-24.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,550,000.00 USD | 0.00 USD | 1,480.00 USD | `-24.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,550,000.00 USD | 0.00 USD | 1,870.00 USD | `-24.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,550,000.00 USD | 0.00 USD | 11,460.00 USD | `-23.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,530,000.00 USD | 0.00 USD | 240.67 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,530,000.00 USD | 0.00 USD | 306.56 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,530,000.00 USD | 0.00 USD | 1,670.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,530,000.00 USD | 0.00 USD | 73,220.00 USD | `-22.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,460,000.00 USD | 0.00 USD | 19,600.00 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,440,000.00 USD | 0.00 USD | 8,490.00 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,430,000.00 USD | 0.00 USD | 102,530.00 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,330,000.00 USD | 0.00 USD | 421.41 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,330,000.00 USD | 0.00 USD | 4,350.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,320,000.00 USD | 0.00 USD | 444.49 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,320,000.00 USD | 0.00 USD | 2,550.00 USD | `-20.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,320,000.00 USD | 0.00 USD | 1,380.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,320,000.00 USD | 0.00 USD | 344.07 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,320,000.00 USD | 0.00 USD | 24,320.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,290,000.00 USD | 0.00 USD | 19,170.00 USD | `-19.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,270,000.00 USD | 0.00 USD | 894.72 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,270,000.00 USD | 0.00 USD | 70,870.00 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,200,000.00 USD | 0.00 USD | 24,110.00 USD | `-19.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,180,000.00 USD | 0.00 USD | 3,700.00 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,180,000.00 USD | 0.00 USD | 16,250.00 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,160,000.00 USD | 0.00 USD | 5,130.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,150,000.00 USD | 0.00 USD | 1,800.00 USD | `-18.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,150,000.00 USD | 0.00 USD | 18,440.00 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,130,000.00 USD | 0.00 USD | 77,480.00 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,060,000.00 USD | 0.00 USD | 1,610.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,050,000.00 USD | 0.00 USD | 331.46 USD | `-17.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,050,000.00 USD | 0.00 USD | 58,330.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,000,000.00 USD | 0.00 USD | 632.99 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,000,000.00 USD | 0.00 USD | 1,000.00 USD | `-16.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,990,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,990,000.00 USD | 0.00 USD | 54,670.00 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,940,000.00 USD | 0.00 USD | 4,080.00 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,930,000.00 USD | 0.00 USD | 4,070.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,930,000.00 USD | 0.00 USD | 367.50 USD | `-15.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,930,000.00 USD | 0.00 USD | 19,240.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,910,000.00 USD | 0.00 USD | 4,370.00 USD | `-14.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,910,000.00 USD | 0.00 USD | 389,710.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,520,000.00 USD | 0.00 USD | 6,300.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,510,000.00 USD | 0.00 USD | 8,050.00 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,500,000.00 USD | 0.00 USD | 32,040.00 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,470,000.00 USD | 0.00 USD | 28,820.00 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,440,000.00 USD | 0.00 USD | 14,490.00 USD | `-13.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,430,000.00 USD | 0.00 USD | 8,780.00 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,420,000.00 USD | 0.00 USD | 1,190.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,420,000.00 USD | 0.00 USD | 1,780.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,420,000.00 USD | 0.00 USD | 166,450.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,250,000.00 USD | 0.00 USD | 4,530.00 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,240,000.00 USD | 0.00 USD | 21,180.00 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,220,000.00 USD | 0.00 USD | 7,350.00 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,220,000.00 USD | 0.00 USD | 41,340.00 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,130,000.00 USD | 0.00 USD | 5,890.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,130,000.00 USD | 0.00 USD | 6,580.00 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,120,000.00 USD | 0.00 USD | 161,230.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 957,570.00 USD | 0.00 USD | 26,910.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 930,660.00 USD | 0.00 USD | 8,970.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 921,700.00 USD | 0.00 USD | 47,220.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 874,480.00 USD | 0.00 USD | 1,310.00 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 873,160.00 USD | 0.00 USD | 6,910.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 866,260.00 USD | 0.00 USD | 934.17 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 865,320.00 USD | 0.00 USD | 5,090.00 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 860,230.00 USD | 0.00 USD | 396.29 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 859,840.00 USD | 0.00 USD | 25,410.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 834,420.00 USD | 0.00 USD | 317.60 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 834,100.00 USD | 0.00 USD | 42,280.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 791,820.00 USD | 0.00 USD | 667.16 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 791,150.00 USD | 0.00 USD | 189,510.00 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 601,650.00 USD | 0.00 USD | 350.51 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 601,300.00 USD | 0.00 USD | 58,180.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 543,120.00 USD | 0.00 USD | 428.11 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 542,690.00 USD | 0.00 USD | 919.83 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 541,770.00 USD | 0.00 USD | 34,070.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 507,700.00 USD | 0.00 USD | 15,710.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 491,990.00 USD | 0.00 USD | 5,760.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 486,240.00 USD | 0.00 USD | 3,400.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 482,830.00 USD | 0.00 USD | 13,580.00 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 469,250.00 USD | 0.00 USD | 49,120.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 420,120.00 USD | 0.00 USD | 65,790.00 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 354,330.00 USD | 0.00 USD | 3,880.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 350,450.00 USD | 0.00 USD | 31,590.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 318,860.00 USD | 0.00 USD | 2,390.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 316,470.00 USD | 0.00 USD | 69,250.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 247,220.00 USD | 0.00 USD | 19,470.00 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 227,750.00 USD | 0.00 USD | 8,530.00 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 219,220.00 USD | 0.00 USD | 3,680.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 215,540.00 USD | 0.00 USD | 1,680.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 213,860.00 USD | 0.00 USD | 23,600.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 190,270.00 USD | 0.00 USD | 14,410.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 175,860.00 USD | 0.00 USD | 15,350.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 160,500.00 USD | 0.00 USD | 63,060.00 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 97,440.00 USD | 0.00 USD | 13,050.00 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 84,390.00 USD | 0.00 USD | 20,990.00 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 63,400.00 USD | 0.00 USD | 494.74 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 62,910.00 USD | 0.00 USD | 2,220.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 60,690.00 USD | 0.00 USD | 17,360.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 43,330.00 USD | 0.00 USD | 282.18 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 43,050.00 USD | 0.00 USD | 1,910.00 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 41,140.00 USD | 0.00 USD | 39,760.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 1,380.00 USD | 0.00 USD | 182.52 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 1,190.00 USD | 0.00 USD | 1,190.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 17,380.00 USD | 17,380.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 32,790.00 USD | 15,410.00 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 193,810.00 USD | 161,010.00 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 283,440.00 USD | 89,630.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 285,170.00 USD | 1,730.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 477,520.00 USD | 192,350.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 521,670.00 USD | 44,150.00 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 525,340.00 USD | 3,670.00 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 541,720.00 USD | 16,370.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 592,020.00 USD | 50,300.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 601,300.00 USD | 9,280.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 642,620.00 USD | 41,330.00 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 646,030.00 USD | 3,410.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 646,530.00 USD | 498.51 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 647,840.00 USD | 1,310.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 663,800.00 USD | 15,960.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 708,030.00 USD | 44,220.00 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 726,960.00 USD | 18,940.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 833,980.00 USD | 107,010.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 854,450.00 USD | 20,470.00 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 854,760.00 USD | 312.24 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 855,150.00 USD | 392.64 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 855,540.00 USD | 388.48 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 859,820.00 USD | 4,280.00 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 860,580.00 USD | 759.73 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 860,950.00 USD | 364.84 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 979,650.00 USD | 118,700.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 980,390.00 USD | 742.55 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,000,000.00 USD | 21,860.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 2,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 2,010,000.00 USD | 4,070.00 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 2,020,000.00 USD | 1,240.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 2,090,000.00 USD | 77,690.00 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 2,100,000.00 USD | 3,030.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 2,100,000.00 USD | 914.98 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 2,100,000.00 USD | 152.12 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,500,000.00 USD | 397,590.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,730,000.00 USD | 235,990.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,730,000.00 USD | 2,650.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,820,000.00 USD | 84,970.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,870,000.00 USD | 49,950.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,900,000.00 USD | 29,420.00 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,910,000.00 USD | 13,030.00 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,910,000.00 USD | 2,640.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,910,000.00 USD | 314.37 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,940,000.00 USD | 22,590.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,110,000.00 USD | 176,250.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,140,000.00 USD | 30,560.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,150,000.00 USD | 8,540.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,250,000.00 USD | 93,590.00 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,290,000.00 USD | 40,760.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,310,000.00 USD | 27,630.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,340,000.00 USD | 23,180.00 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,350,000.00 USD | 10,400.00 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,370,000.00 USD | 19,890.00 USD | 0.00 USD | `+12.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,370,000.00 USD | 4,060.00 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,480,000.00 USD | 111,630.00 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,480,000.00 USD | 156.30 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,500,000.00 USD | 13,180.00 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,500,000.00 USD | 4,420.00 USD | 0.00 USD | `+13.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,500,000.00 USD | 313.51 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,510,000.00 USD | 7,900.00 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,560,000.00 USD | 47,350.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,560,000.00 USD | 187.06 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,650,000.00 USD | 92,570.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,650,000.00 USD | 2,540.00 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,710,000.00 USD | 63,070.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,740,000.00 USD | 25,080.00 USD | 0.00 USD | `+15.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,740,000.00 USD | 5,030.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,760,000.00 USD | 19,640.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,760,000.00 USD | 120.58 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,780,000.00 USD | 14,090.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,780,000.00 USD | 5,860.00 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,870,000.00 USD | 87,450.00 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,880,000.00 USD | 5,460.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,880,000.00 USD | 178.33 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,950,000.00 USD | 70,250.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,960,000.00 USD | 15,350.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,960,000.00 USD | 179.38 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,960,000.00 USD | 179.72 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,960,000.00 USD | 217.63 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 3,960,000.00 USD | 493.85 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,960,000.00 USD | 575.38 USD | 0.00 USD | `+18.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,970,000.00 USD | 327.58 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 3,970,000.00 USD | 163.85 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,090,000.00 USD | 120,930.00 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,120,000.00 USD | 38,230.00 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,130,000.00 USD | 1,710.00 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,130,000.00 USD | 432.63 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,130,000.00 USD | 2,620.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,130,000.00 USD | 537.61 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,550,000.00 USD | 420,400.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,550,000.00 USD | 278.52 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,550,000.00 USD | 589.22 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,550,000.00 USD | 733.03 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,550,000.00 USD | 423.60 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,560,000.00 USD | 12,620.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,570,000.00 USD | 381.09 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,570,000.00 USD | 961.16 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,570,000.00 USD | 1,570.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,570,000.00 USD | 5,650.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,570,000.00 USD | 160.11 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,570,000.00 USD | 225.33 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,570,000.00 USD | 438.60 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,580,000.00 USD | 6,610.00 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,620,000.00 USD | 40,880.00 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,640,000.00 USD | 21,220.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,650,000.00 USD | 4,330.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,650,000.00 USD | 639.61 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,650,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,660,000.00 USD | 13,690.00 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,660,000.00 USD | 1,020.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,750,000.00 USD | 87,720.00 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,780,000.00 USD | 30,110.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,780,000.00 USD | 863.89 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,780,000.00 USD | 1,040.00 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,760,000.00 USD | 972,790.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,760,000.00 USD | 5,600.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,780,000.00 USD | 19,110.00 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,800,000.00 USD | 18,790.00 USD | 0.00 USD | `+27.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,860,000.00 USD | 58,030.00 USD | 0.00 USD | `+27.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,900,000.00 USD | 46,110.00 USD | 0.00 USD | `+27.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,920,000.00 USD | 14,320.00 USD | 0.00 USD | `+28.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,930,000.00 USD | 11,740.00 USD | 0.00 USD | `+28.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,950,000.00 USD | 23,650.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,950,000.00 USD | 384.94 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,960,000.00 USD | 1,300.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,960,000.00 USD | 347.06 USD | 0.00 USD | `+29.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,960,000.00 USD | 347.68 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,960,000.00 USD | 491.11 USD | 0.00 USD | `+30.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,960,000.00 USD | 3,290.00 USD | 0.00 USD | `+30.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,960,000.00 USD | 281.55 USD | 0.00 USD | `+30.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,970,000.00 USD | 6,590.00 USD | 0.00 USD | `+30.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,970,000.00 USD | 235.93 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,970,000.00 USD | 5,860.00 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,080,000.00 USD | 103,820.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,080,000.00 USD | 705.23 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,080,000.00 USD | 5,720.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,080,000.00 USD | 139.03 USD | 0.00 USD | `+32.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,090,000.00 USD | 2,480.00 USD | 0.00 USD | `+32.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,090,000.00 USD | 1,850.00 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,090,000.00 USD | 286.94 USD | 0.00 USD | `+33.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,100,000.00 USD | 7,120.00 USD | 0.00 USD | `+33.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,100,000.00 USD | 329.13 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,100,000.00 USD | 1,970.00 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,100,000.00 USD | 2,720.00 USD | 0.00 USD | `+34.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,100,000.00 USD | 1,190.00 USD | 0.00 USD | `+34.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,100,000.00 USD | 1,770.00 USD | 0.00 USD | `+35.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,110,000.00 USD | 3,450.00 USD | 0.00 USD | `+35.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,110,000.00 USD | 345.45 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,130,000.00 USD | 23,750.00 USD | 0.00 USD | `+36.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,130,000.00 USD | 1,670.00 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,130,000.00 USD | 1,020.00 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,290,000.00 USD | 153,150.00 USD | 0.00 USD | `+36.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,310,000.00 USD | 26,180.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,320,000.00 USD | 5,440.00 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,330,000.00 USD | 8,940.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,450,000.00 USD | 119,340.00 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,450,000.00 USD | 3,000.00 USD | 0.00 USD | `+38.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,650,000.00 USD | 197,080.00 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,660,000.00 USD | 13,710.00 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 6,750,000.00 USD | 90,380.00 USD | 0.00 USD | `+38.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,750,000.00 USD | 2,050.00 USD | 0.00 USD | `+39.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,760,000.00 USD | 3,300.00 USD | 0.00 USD | `+39.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 6,760,000.00 USD | 1,040.00 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 6,760,000.00 USD | 425.76 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,760,000.00 USD | 4,120.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 6,820,000.00 USD | 61,050.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 6,830,000.00 USD | 1,610.00 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 6,830,000.00 USD | 1,200.00 USD | 0.00 USD | `+41.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 6,830,000.00 USD | 420.32 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 6,830,000.00 USD | 1,940.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 6,830,000.00 USD | 4,010.00 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,900,000.00 USD | 66,060.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,900,000.00 USD | 1,890.00 USD | 0.00 USD | `+43.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,900,000.00 USD | 195.46 USD | 0.00 USD | `+43.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,900,000.00 USD | 289.93 USD | 0.00 USD | `+43.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,900,000.00 USD | 116.16 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,910,000.00 USD | 7,310.00 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,910,000.00 USD | 310.70 USD | 0.00 USD | `+45.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,910,000.00 USD | 325.62 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,910,000.00 USD | 1,760.00 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,910,000.00 USD | 3,230.00 USD | 0.00 USD | `+47.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,920,000.00 USD | 5,120.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,920,000.00 USD | 1,310.00 USD | 0.00 USD | `+49.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,950,000.00 USD | 30,990.00 USD | 0.00 USD | `+49.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,950,000.00 USD | 611.11 USD | 0.00 USD | `+50.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,970,000.00 USD | 13,580.00 USD | 0.00 USD | `+50.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,970,000.00 USD | 1,630.00 USD | 0.00 USD | `+51.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,970,000.00 USD | 1,370.00 USD | 0.00 USD | `+51.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,970,000.00 USD | 5,400.00 USD | 0.00 USD | `+52.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,980,000.00 USD | 1,620.00 USD | 0.00 USD | `+52.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,980,000.00 USD | 450.55 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,980,000.00 USD | 3,060.00 USD | 0.00 USD | `+53.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,980,000.00 USD | 3,070.00 USD | 0.00 USD | `+54.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,980,000.00 USD | 1,550.00 USD | 0.00 USD | `+55.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,990,000.00 USD | 647.56 USD | 0.00 USD | `+56.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,990,000.00 USD | 1,420.00 USD | 0.00 USD | `+56.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,990,000.00 USD | 2,130.00 USD | 0.00 USD | `+56.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,000,000.00 USD | 6,870.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,000,000.00 USD | 342.25 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,000,000.00 USD | 2,990.00 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,000,000.00 USD | 2,970.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,000,000.00 USD | 324.54 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,000,000.00 USD | 504.21 USD | 0.00 USD | `+59.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,000,000.00 USD | 166.00 USD | 0.00 USD | `+60.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,010,000.00 USD | 4,190.00 USD | 0.00 USD | `+60.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,020,000.00 USD | 13,480.00 USD | 0.00 USD | `+61.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,020,000.00 USD | 2,860.00 USD | 0.00 USD | `+62.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,020,000.00 USD | 264.31 USD | 0.00 USD | `+63.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,020,000.00 USD | 599.34 USD | 0.00 USD | `+64.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,020,000.00 USD | 193.19 USD | 0.00 USD | `+64.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,030,000.00 USD | 3,950.00 USD | 0.00 USD | `+65.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,030,000.00 USD | 1,940.00 USD | 0.00 USD | `+66.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,190,000.00 USD | 160,550.00 USD | 0.00 USD | `+66.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,190,000.00 USD | 1,290.00 USD | 0.00 USD | `+67.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,190,000.00 USD | 1,180.00 USD | 0.00 USD | `+68.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,190,000.00 USD | 630.05 USD | 0.00 USD | `+70.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,200,000.00 USD | 1,410.00 USD | 0.00 USD | `+70.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,200,000.00 USD | 2,610.00 USD | 0.00 USD | `+70.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,210,000.00 USD | 7,630.00 USD | 0.00 USD | `+72.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,210,000.00 USD | 4,640.00 USD | 0.00 USD | `+74.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,210,000.00 USD | 371.88 USD | 0.00 USD | `+75.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,210,000.00 USD | 2,510.00 USD | 0.00 USD | `+75.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,210,000.00 USD | 380.68 USD | 0.00 USD | `+76.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,220,000.00 USD | 11,170.00 USD | 0.00 USD | `+79.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,260,000.00 USD | 34,360.00 USD | 0.00 USD | `+79.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,260,000.00 USD | 253.21 USD | 0.00 USD | `+80.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,260,000.00 USD | 100.29 USD | 0.00 USD | `+80.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,270,000.00 USD | 10,610.00 USD | 0.00 USD | `+83.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,270,000.00 USD | 309.43 USD | 0.00 USD | `+83.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.99` | 7,270,000.00 USD | 4,640.00 USD | 0.00 USD | `+83.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,310,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,390,000.00 USD | 81,310.00 USD | 0.00 USD | `+84.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.15` | 7,400,000.00 USD | 2,150.00 USD | 0.00 USD | `+87.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,400,000.00 USD | 216.90 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,400,000.00 USD | 1,990.00 USD | 0.00 USD | `+88.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,400,000.00 USD | 7,200.00 USD | 0.00 USD | `+88.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,410,000.00 USD | 998.65 USD | 0.00 USD | `+93.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,410,000.00 USD | 1,260.00 USD | 0.00 USD | `+93.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,510,000.00 USD | 103,010.00 USD | 0.00 USD | `+93.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 7,510,000.00 USD | 721.22 USD | 0.00 USD | `+94.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 7,520,000.00 USD | 5,130.00 USD | 0.00 USD | `+95.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 7,520,000.00 USD | 2,010.00 USD | 0.00 USD | `+98.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 7,520,000.00 USD | 198.20 USD | 0.00 USD | `+99.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 7,520,000.00 USD | 3,670.00 USD | 0.00 USD | `+99.59%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.52` | 19,410,000.00 USD | 0.00 USD | 19,410,000.00 USD | 18,870.00 USD | 0.00 USD | 41,320.00 USD |
| `7D` | `3.53` | 19,350,000.00 USD | 0.00 USD | 19,350,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD |
| `7D` | `3.54` | 19,120,000.00 USD | 0.00 USD | 19,120,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD |
| `7D` | `3.55` | 19,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD |
| `7D` | `3.56` | 18,800,000.00 USD | 0.00 USD | 18,800,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD |
| `7D` | `3.57` | 18,740,000.00 USD | 0.00 USD | 18,740,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD |
| `7D` | `3.58` | 18,540,000.00 USD | 0.00 USD | 18,540,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD |
| `7D` | `3.59` | 18,260,000.00 USD | 0.00 USD | 18,260,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD |
| `7D` | `3.60` | 18,240,000.00 USD | 0.00 USD | 18,240,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `7D` | `3.63` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `7D` | `3.64` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD |
| `7D` | `3.65` | 17,550,000.00 USD | 0.00 USD | 17,550,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD |
| `7D` | `3.67` | 17,290,000.00 USD | 0.00 USD | 17,290,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD |
| `7D` | `3.68` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.69` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `7D` | `3.70` | 17,080,000.00 USD | 0.00 USD | 17,080,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `7D` | `3.71` | 16,940,000.00 USD | 0.00 USD | 16,940,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD |
| `7D` | `3.72` | 16,810,000.00 USD | 0.00 USD | 16,810,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `7D` | `3.73` | 16,810,000.00 USD | 0.00 USD | 16,810,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `7D` | `3.74` | 16,700,000.00 USD | 0.00 USD | 16,700,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD |
| `7D` | `3.75` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD |
| `7D` | `3.76` | 16,220,000.00 USD | 0.00 USD | 16,220,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `7D` | `3.77` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD |
| `7D` | `3.78` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD |
| `7D` | `3.79` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD |
| `7D` | `3.80` | 15,760,000.00 USD | 0.00 USD | 15,760,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD |
| `7D` | `3.81` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD |
| `7D` | `3.82` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `7D` | `3.83` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD |
| `7D` | `3.84` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD |
| `7D` | `3.85` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD |
| `1D` | `3.86` | 18,660,000.00 USD | 0.00 USD | 18,660,000.00 USD | 225,350.00 USD | 214,520.00 USD | 91,120.00 USD |
| `7D` | `3.86` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD |
| `1D` | `3.87` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 53,480.00 USD | 58,230.00 USD | 188,360.00 USD |
| `7D` | `3.87` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD |
| `1D` | `3.88` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 35,520.00 USD | 26,560.00 USD | 224,940.00 USD |
| `7D` | `3.88` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 110,160.00 USD | 86,900.00 USD | 118,540.00 USD |
| `1D` | `3.89` | 17,550,000.00 USD | 0.00 USD | 17,550,000.00 USD | 397,250.00 USD | 100,370.00 USD | 258,260.00 USD |
| `7D` | `3.89` | 14,570,000.00 USD | 0.00 USD | 14,570,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD |
| `1D` | `3.90` | 16,790,000.00 USD | 0.00 USD | 16,790,000.00 USD | 33,540.00 USD | 53,910.00 USD | 248,420.00 USD |
| `7D` | `3.90` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD |
| `1D` | `3.91` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 378,850.00 USD | 120,100.00 USD | 304,610.00 USD |
| `7D` | `3.91` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 342,560.00 USD | 13,670.00 USD | 124,180.00 USD |
| `7D` | `3.92` | 13,840,000.00 USD | 0.00 USD | 13,840,000.00 USD | 176,970.00 USD | 66,710.00 USD | 105,000.00 USD |
| `1D` | `3.93` | 15,170,000.00 USD | 0.00 USD | 15,170,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD |
| `7D` | `3.93` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD |
| `1D` | `3.94` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 144,900.00 USD | 53,060.00 USD | 137,200.00 USD |
| `7D` | `3.94` | 13,470,000.00 USD | 0.00 USD | 13,470,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3.95` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 103,590.00 USD | 0.00 USD | 33,080.00 USD |
| `7D` | `3.95` | 13,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `3.96` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD |
| `7D` | `3.96` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD |
| `1D` | `3.97` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD |
| `7D` | `3.97` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD |
| `1D` | `3.98` | 14,100,000.00 USD | 0.00 USD | 14,100,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD |
| `7D` | `3.98` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD |
| `1D` | `3.99` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD |
| `7D` | `3.99` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD |
| `1D` | `4.00` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD |
| `7D` | `4.00` | 11,800,000.00 USD | 0.00 USD | 11,800,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD |
| `1D` | `4.01` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,850.00 USD |
| `7D` | `4.01` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD |
| `1D` | `4.02` | 13,130,000.00 USD | 0.00 USD | 13,130,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,360.00 USD |
| `7D` | `4.02` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD |
| `1D` | `4.03` | 12,810,000.00 USD | 0.00 USD | 12,810,000.00 USD | 66,220.00 USD | 59,350.00 USD | 324.38 USD |
| `7D` | `4.03` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD |
| `1D` | `4.04` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 70,930.00 USD | 21,940.00 USD | 183,540.00 USD |
| `7D` | `4.04` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 321,230.00 USD | 0.00 USD | 492,530.00 USD |
| `1D` | `4.05` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 348,930.00 USD | 23,720.00 USD | 232.83 USD |
| `7D` | `4.05` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD |
| `1D` | `4.06` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,950.00 USD |
| `7D` | `4.06` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD |
| `1D` | `4.07` | 11,470,000.00 USD | 0.00 USD | 11,470,000.00 USD | 359,020.00 USD | 205,460.00 USD | 334,500.00 USD |
| `7D` | `4.07` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD |
| `1D` | `4.08` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,890.00 USD |
| `7D` | `4.08` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD |
| `1D` | `4.09` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,490.00 USD |
| `7D` | `4.09` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD |
| `1D` | `4.10` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 4,790.00 USD | 89,650.00 USD | 141,400.00 USD |
| `7D` | `4.10` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD |
| `1D` | `4.11` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 122,090.00 USD | 138,540.00 USD | 345,730.00 USD |
| `7D` | `4.11` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 25,170.00 USD | 296,050.00 USD |
| `1D` | `4.12` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,300.00 USD |
| `7D` | `4.12` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD |
| `1D` | `4.13` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 159,720.00 USD | 0.00 USD | 398,490.00 USD |
| `7D` | `4.13` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD |
| `1D` | `4.14` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 140,730.00 USD | 29,960.00 USD | 125,370.00 USD |
| `7D` | `4.14` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 238,150.00 USD | 244,270.00 USD | 345,750.00 USD |
| `1D` | `4.15` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 526,070.00 USD | 109,290.00 USD | 367,560.00 USD |
| `7D` | `4.15` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.16` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 340,550.00 USD | 100,580.00 USD | 379,060.00 USD |
| `7D` | `4.16` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 0.00 USD | 22,880.00 USD | 0.00 USD |
| `1D` | `4.17` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 340,700.00 USD | 302,060.00 USD | 310,250.00 USD |
| `7D` | `4.17` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 252,690.00 USD | 84,340.00 USD | 78,260.00 USD |
| `1D` | `4.18` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 389,120.00 USD | 69,910.00 USD | 201,720.00 USD |
| `7D` | `4.18` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 227,940.00 USD | 0.00 USD | 86,570.00 USD |
| `1D` | `4.19` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 148,260.00 USD | 138,280.00 USD | 244,930.00 USD |
| `7D` | `4.19` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.20` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 31,500.00 USD | 40,570.00 USD | 131,830.00 USD |
| `7D` | `4.20` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD |
| `7D` | `4.21` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD |
| `1D` | `4.22` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD |
| `7D` | `4.22` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD |
| `1D` | `4.23` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 113,770.00 USD | 129,320.00 USD | 274,130.00 USD |
| `7D` | `4.23` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.24` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 127,260.00 USD | 98,020.00 USD | 125,490.00 USD |
| `7D` | `4.24` | 873,040.00 USD | 0.00 USD | 873,040.00 USD | 0.00 USD | 45,760.00 USD | 0.00 USD |
| `1D` | `4.25` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 251,300.00 USD | 37,270.00 USD | 328,950.00 USD |
| `7D` | `4.25` | 827,270.00 USD | 0.00 USD | 827,270.00 USD | 3,390.00 USD | 0.00 USD | 156,530.00 USD |
| `1D` | `4.26` | 897,220.00 USD | 0.00 USD | 897,220.00 USD | 120,080.00 USD | 15,130.00 USD | 85,610.00 USD |
| `7D` | `4.26` | 667,350.00 USD | 0.00 USD | 667,350.00 USD | 458,850.00 USD | 0.00 USD | 173,150.00 USD |
| `1D` | `4.27` | 676,400.00 USD | 0.00 USD | 676,400.00 USD | 0.00 USD | 44,870.00 USD | 0.00 USD |
| `7D` | `4.27` | 35,350.00 USD | 0.00 USD | 35,350.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.28` | 631,540.00 USD | 0.00 USD | 631,540.00 USD | 4,310.00 USD | 28,780.00 USD | 0.00 USD |
| `7D` | `4.28` | 10,540.00 USD | 0.00 USD | 10,540.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.29` | 598,440.00 USD | 0.00 USD | 598,440.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.29` | 5,150.00 USD | 0.00 USD | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.32` | 380,480.00 USD | 0.00 USD | 380,480.00 USD | 0.00 USD | 0.00 USD | 326.33 USD |
| `7D` | `4.34` | 7,340.00 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `7D` | `4.34` | 14,680.00 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `4.36` | 380,150.00 USD | 0.00 USD | 380,150.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD |
| `1D` | `4.37` | 680,420.00 USD | 680,420.00 USD | 0.00 USD | 280,420.00 USD | 0.00 USD | 400,000.00 USD |
| `1D` | `4.37` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 280,420.00 USD | 0.00 USD | 400,000.00 USD |
| `7D` | `4.37` | 458,540.00 USD | 458,540.00 USD | 0.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.38` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 3,030.00 USD | 0.00 USD | 640,700.00 USD |
| `7D` | `4.38` | 948,640.00 USD | 948,640.00 USD | 0.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD |
| `7D` | `4.39` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD |
| `1D` | `4.40` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 541,780.00 USD | 118,310.00 USD | 408,330.00 USD |
| `7D` | `4.40` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD |
| `1D` | `4.41` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 450,080.00 USD | 331,840.00 USD | 689,400.00 USD |
| `7D` | `4.41` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 128,340.00 USD | 240,270.00 USD | 253,280.00 USD |
| `7D` | `4.42` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 404,280.00 USD | 117,350.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 335,950.00 USD | 146,900.00 USD | 443,190.00 USD |
| `7D` | `4.43` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 293,250.00 USD | 88,400.00 USD | 228,310.00 USD |
| `1D` | `4.44` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 276,510.00 USD | 385,410.00 USD | 457,750.00 USD |
| `7D` | `4.44` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 455,890.00 USD | 143,990.00 USD | 246,120.00 USD |
| `1D` | `4.45` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 76,860.00 USD | 153,510.00 USD | 124,130.00 USD |
| `7D` | `4.45` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD |
| `1D` | `4.46` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 4,580.00 USD | 65,940.00 USD | 33,060.00 USD |
| `7D` | `4.46` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD |
| `1D` | `4.47` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 222,670.00 USD | 25,190.00 USD | 120,030.00 USD |
| `7D` | `4.47` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD |
| `1D` | `4.48` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 246,890.00 USD | 116,490.00 USD | 150,910.00 USD |
| `7D` | `4.48` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD |
| `1D` | `4.49` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 310,660.00 USD | 242,590.00 USD | 403,450.00 USD |
| `7D` | `4.49` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD |
| `1D` | `4.50` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 427,290.00 USD | 118,600.00 USD | 237,920.00 USD |
| `7D` | `4.50` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 376,770.00 USD | 223,580.00 USD | 2,050.00 USD |
| `1D` | `4.51` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 314,310.00 USD | 168,440.00 USD | 489,850.00 USD |
| `7D` | `4.51` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 80,400.00 USD |
| `1D` | `4.52` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 351,620.00 USD | 99,830.00 USD | 286,020.00 USD |
| `7D` | `4.52` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 230,020.00 USD | 0.00 USD | 225,430.00 USD |
| `1D` | `4.53` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 505,320.00 USD | 22,430.00 USD | 280,200.00 USD |
| `7D` | `4.53` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD |
| `1D` | `4.54` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 17,740.00 USD | 164,990.00 USD | 167,990.00 USD |
| `7D` | `4.54` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 3,110.00 USD | 34,450.00 USD | 108,750.00 USD |
| `7D` | `4.55` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 558.34 USD |
| `1D` | `4.56` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 112,410.00 USD | 32,800.00 USD | 288,580.00 USD |
| `7D` | `4.56` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD |
| `1D` | `4.57` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 175,730.00 USD | 70,180.00 USD | 99,620.00 USD |
| `7D` | `4.57` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD |
| `1D` | `4.58` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 377,780.00 USD | 99,430.00 USD | 554,780.00 USD |
| `7D` | `4.58` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD |
| `1D` | `4.59` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 404,460.00 USD | 75,460.00 USD | 109,360.00 USD |
| `7D` | `4.59` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD |
| `1D` | `4.60` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 48,970.00 USD | 50,860.00 USD | 66,480.00 USD |
| `7D` | `4.60` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD |
| `1D` | `4.61` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 64,820.00 USD | 7,560.00 USD | 76,320.00 USD |
| `7D` | `4.61` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `4.62` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 95,000.00 USD | 31,380.00 USD | 19,900.00 USD |
| `7D` | `4.62` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `4.63` | 17,080,000.00 USD | 17,080,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | 422.42 USD |
| `7D` | `4.63` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 106,430.00 USD | 11,270.00 USD | 41,640.00 USD |
| `7D` | `4.64` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD |
| `1D` | `4.65` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 204,190.00 USD | 52,020.00 USD | 486,520.00 USD |
| `7D` | `4.65` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD |
| `1D` | `4.66` | 18,770,000.00 USD | 18,770,000.00 USD | 0.00 USD | 202,480.00 USD | 309,340.00 USD | 277,010.00 USD |
| `7D` | `4.66` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 19,110,000.00 USD | 19,110,000.00 USD | 0.00 USD | 88,400.00 USD | 0.00 USD | 259,350.00 USD |
| `7D` | `4.67` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 59,560.00 USD | 106,120.00 USD | 36,990.00 USD |
| `7D` | `4.68` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD |
| `1D` | `4.69` | 19,700,000.00 USD | 19,700,000.00 USD | 0.00 USD | 168,270.00 USD | 49,160.00 USD | 168,810.00 USD |
| `7D` | `4.69` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD |
| `7D` | `4.70` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD |
| `1D` | `4.71` | 21,090,000.00 USD | 21,090,000.00 USD | 0.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD |
| `7D` | `4.71` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD |
| `1D` | `4.72` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD |
| `7D` | `4.72` | 17,690,000.00 USD | 17,690,000.00 USD | 0.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 21,490,000.00 USD | 21,490,000.00 USD | 0.00 USD | 110,530.00 USD | 25,210.00 USD | 35,540.00 USD |
| `7D` | `4.73` | 17,760,000.00 USD | 17,760,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD |
| `1D` | `4.74` | 21,880,000.00 USD | 21,880,000.00 USD | 0.00 USD | 68,200.00 USD | 141,320.00 USD | 176,260.00 USD |
| `7D` | `4.74` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD |
| `1D` | `4.75` | 22,290,000.00 USD | 22,290,000.00 USD | 0.00 USD | 100,320.00 USD | 141,340.00 USD | 171,270.00 USD |
| `7D` | `4.75` | 18,700,000.00 USD | 18,700,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `1D` | `4.76` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 32,610.00 USD | 56,290.00 USD | 56,910.00 USD |
| `7D` | `4.76` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD |
| `1D` | `4.77` | 22,650,000.00 USD | 22,650,000.00 USD | 0.00 USD | 46,010.00 USD | 85,030.00 USD | 76,330.00 USD |
| `7D` | `4.77` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD |
| `7D` | `4.78` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 22,990,000.00 USD | 22,990,000.00 USD | 0.00 USD | 98,120.00 USD | 39,920.00 USD | 59,380.00 USD |
| `7D` | `4.79` | 23,210,000.00 USD | 23,210,000.00 USD | 0.00 USD | 804,240.00 USD | 249,310.00 USD | 72,220.00 USD |
| `1D` | `4.80` | 23,440,000.00 USD | 23,440,000.00 USD | 0.00 USD | 187,170.00 USD | 128,280.00 USD | 138,770.00 USD |
| `7D` | `4.80` | 24,800,000.00 USD | 24,800,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 23,450,000.00 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 8,950.00 USD | 210.83 USD |
| `7D` | `4.81` | 25,430,000.00 USD | 25,430,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 23,590,000.00 USD | 23,590,000.00 USD | 0.00 USD | 20,630.00 USD | 78,640.00 USD | 35,260.00 USD |
| `7D` | `4.82` | 28,190,000.00 USD | 28,190,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 23,590,000.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `7D` | `4.83` | 29,840,000.00 USD | 29,840,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 30,330,000.00 USD | 30,330,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 32,370,000.00 USD | 32,370,000.00 USD | 0.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 33,780,000.00 USD | 33,780,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 34,810,000.00 USD | 34,810,000.00 USD | 0.00 USD | 234,740.00 USD | 136,820.00 USD | 660,890.00 USD |
| `7D` | `4.88` | 36,030,000.00 USD | 36,030,000.00 USD | 0.00 USD | 428,040.00 USD | 0.00 USD | 789,710.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `256,266,331.1 NEAR`
  * 1h OI Change: `-0.31%` | 4h OI Change: `-1.13%` | 24h OI Change: `-13.41%`
  * Exchange Breakdown: Binance=`201.54M` | Bybit=`148.79M` | OKX=`52.84M` | Hyperliquid=`243.39M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-131.60K` | Last 24h: `-22.13K` | Last 3d: `231.31K` | Last 7d: `198.53K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0009%` | **USDT OKX** | `-0.0244%` |
| **USDT Bybit** | `-0.0800%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0008%` | **USDT BingX** | `0.0006%` |
| **USDT Gate** | `-0.0035%` | **USDT Bitget** | `-0.0487%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `55.58%` | `44.42%` | `1.25` | 15,060,000.00 USD |
| `15M` | `Binance` | `65.59%` | `34.41%` | `1.91` | 7,070,000.00 USD |
| `15M` | `OKX` | `51.15%` | `48.85%` | `1.05` | 977,280.00 USD |
| `15M` | `Bybit` | `60.4%` | `39.6%` | `1.53` | 1,710,000.00 USD |
| `15M` | `KuCoin` | `59.4%` | `40.6%` | `1.46` | 138,040.00 USD |
| `15M` | `Gate` | `48.91%` | `51.09%` | `0.96` | 324,460.00 USD |
| `15M` | `Bitget` | `33%` | `67%` | `0.49` | 642,760.00 USD |
| `15M` | `BingX` | `34.91%` | `65.09%` | `0.54` | 531,740.00 USD |
| `15M` | `MEXC` | `52.16%` | `47.84%` | `1.09` | 381,470.00 USD |
| `15M` | `Bitunix` | `59.43%` | `40.57%` | `1.46` | 238,530.00 USD |
| `15M` | `Hyperliquid` | `56.61%` | `43.39%` | `1.30` | 664,070.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.2%` | `52.8%` | `0.89` | 206,410.00 USD |
| `15M` | `Crypto.com` | `92.33%` | `7.67%` | `12.04` | 1,190.00 USD |
| `15M` | `WhiteBIT` | `37.31%` | `62.69%` | `0.60` | 1,640,000.00 USD |
| `15M` | `HTX` | `79.26%` | `20.74%` | `3.82` | 11,570.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `41.05%` | `58.95%` | `0.70` | 222,610.00 USD |
| `15M` | `Aster` | `3.85%` | `96.15%` | `0.04` | 256,510.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56%` | `44%` | `1.27` | 41,680.00 USD |
| `15M` | `Whale Positions` | `65.59%` | `34.41%` | `1.91` | 7,070,000.00 USD |
| `15M` | `Global Accounts` | `55.58%` | `44.42%` | `1.25` | 15,060,000.00 USD |
| `1H` | `NEAR` | `49.02%` | `50.98%` | `0.96` | 72,120,000.00 USD |
| `1H` | `Binance` | `52.17%` | `47.83%` | `1.09` | 28,330,000.00 USD |
| `1H` | `OKX` | `48.84%` | `51.16%` | `0.95` | 6,870,000.00 USD |
| `1H` | `Bybit` | `46.93%` | `53.07%` | `0.88` | 10,470,000.00 USD |
| `1H` | `KuCoin` | `54.91%` | `45.09%` | `1.22` | 670,120.00 USD |
| `1H` | `Gate` | `48.18%` | `51.82%` | `0.93` | 1,180,000.00 USD |
| `1H` | `Bitget` | `36.52%` | `63.48%` | `0.58` | 2,520,000.00 USD |
| `1H` | `BingX` | `44.15%` | `55.85%` | `0.79` | 3,880,000.00 USD |
| `1H` | `MEXC` | `57.53%` | `42.47%` | `1.35` | 1,810,000.00 USD |
| `1H` | `Bitunix` | `42.01%` | `57.99%` | `0.72` | 1,370,000.00 USD |
| `1H` | `Hyperliquid` | `59.19%` | `40.81%` | `1.45` | 7,200,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.67%` | `46.33%` | `1.16` | 461,370.00 USD |
| `1H` | `Crypto.com` | `61.46%` | `38.54%` | `1.59` | 5,570.00 USD |
| `1H` | `WhiteBIT` | `32.51%` | `67.49%` | `0.48` | 5,420,000.00 USD |
| `1H` | `HTX` | `53.83%` | `46.17%` | `1.17` | 46,430.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.35%` | `55.65%` | `0.80` | 1,210,000.00 USD |
| `1H` | `Aster` | `34.31%` | `65.69%` | `0.52` | 447,060.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.06%` | `45.94%` | `1.18` | 239,990.00 USD |
| `1H` | `Whale Positions` | `52.17%` | `47.83%` | `1.09` | 28,330,000.00 USD |
| `1H` | `Global Accounts` | `49.02%` | `50.98%` | `0.96` | 72,120,000.00 USD |
| `4H` | `NEAR` | `49.31%` | `50.69%` | `0.97` | 407,380,000.00 USD |
| `4H` | `Binance` | `52.46%` | `47.54%` | `1.10` | 173,940,000.00 USD |
| `4H` | `OKX` | `48.03%` | `51.97%` | `0.92` | 42,830,000.00 USD |
| `4H` | `Bybit` | `45.74%` | `54.26%` | `0.84` | 54,220,000.00 USD |
| `4H` | `KuCoin` | `54.01%` | `45.99%` | `1.17` | 4,080,000.00 USD |
| `4H` | `Gate` | `51.89%` | `48.11%` | `1.08` | 8,630,000.00 USD |
| `4H` | `Bitget` | `47.34%` | `52.66%` | `0.90` | 18,710,000.00 USD |
| `4H` | `BingX` | `42.63%` | `57.37%` | `0.74` | 19,730,000.00 USD |
| `4H` | `MEXC` | `48.99%` | `51.01%` | `0.96` | 14,270,000.00 USD |
| `4H` | `Bitunix` | `45.78%` | `54.22%` | `0.84` | 7,270,000.00 USD |
| `4H` | `Hyperliquid` | `51.44%` | `48.56%` | `1.06` | 38,090,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.23%` | `46.77%` | `1.14` | 1,810,000.00 USD |
| `4H` | `Crypto.com` | `57.58%` | `42.42%` | `1.36` | 68,390.00 USD |
| `4H` | `WhiteBIT` | `36.6%` | `63.4%` | `0.58` | 17,570,000.00 USD |
| `4H` | `HTX` | `58.97%` | `41.03%` | `1.44` | 450,870.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.88%` | `54.12%` | `0.85` | 2,590,000.00 USD |
| `4H` | `Aster` | `42.46%` | `57.54%` | `0.74` | 1,340,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.83%` | `47.17%` | `1.12` | 1,800,000.00 USD |
| `4H` | `Whale Positions` | `52.46%` | `47.54%` | `1.10` | 173,940,000.00 USD |
| `4H` | `Global Accounts` | `49.31%` | `50.69%` | `0.97` | 407,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4.33` | `4.33` | `4.33` | `4.35` | `4.31` | 8,553,382.74 USD | 3,656,231.21 USD | 4,897,151.53 USD | -1,240,920.31 USD | `-14.51%` | `1B / 5S` |
| `5:00 UTC` | `4.31` | `4.35` | `4.31` | `4.39` | `4.31` | 11,576,553.35 USD | 6,334,405.32 USD | 5,242,148.03 USD | 1,092,257.28 USD | `+9.44%` | `19B / 4S` |
| `0:00 UTC` | `4.34` | `4.34` | `4.34` | `4.37` | `4.32` | 8,173,916.95 USD | 4,141,201.50 USD | 4,032,715.45 USD | 108,486.05 USD | `+1.33%` | `4B / 2S` |
| `5:00 UTC` | `4.32` | `4.32` | `4.32` | `4.34` | `4.31` | 8,060,413.67 USD | 4,212,890.12 USD | 3,847,523.55 USD | 365,366.56 USD | `+4.53%` | `0B / 2S` |
| `0:00 UTC` | `4.31` | `4.32` | `4.31` | `4.36` | `4.29` | 5,778,991.37 USD | 2,863,139.85 USD | 2,915,851.52 USD | -52,711.67 USD | `-0.91%` | `7B / 7S` |
| `5:00 UTC` | `4.36` | `4.36` | `4.36` | `4.38` | `4.34` | 6,093,690.79 USD | 3,348,593.15 USD | 2,745,097.64 USD | 603,495.51 USD | `+9.90%` | `4B / 5S` |
| `0:00 UTC` | `4.34` | `4.35` | `4.34` | `4.38` | `4.33` | 6,786,354.30 USD | 2,907,641.85 USD | 3,878,712.45 USD | -971,070.60 USD | `-14.31%` | `2B / 15S` |
| `5:00 UTC` | `4.33` | `4.34` | `4.33` | `4.37` | `4.32` | 6,865,250.12 USD | 3,215,652.73 USD | 3,649,597.39 USD | -433,944.66 USD | `-6.32%` | `2B / 6S` |
| `0:00 UTC` | `4.33` | `4.34` | `4.33` | `4.35` | `4.32` | 7,895,783.86 USD | 4,987,543.57 USD | 2,908,240.29 USD | 2,079,303.28 USD | `+26.33%` | `8B / 3S` |
| `5:00 UTC` | `4.33` | `4.34` | `4.33` | `4.35` | `4.33` | 1,093,058.98 USD | 515,315.64 USD | 577,743.35 USD | -62,427.71 USD | `-5.71%` | `4B / 6S` |

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
| `5m` | 17,220.00 USD | -124,680.00 USD | **`DISTRIBUTION`** |
| `15m` | -27,380.00 USD | 2,330,000.00 USD | **`ACCUMULATION`** |
| `30m` | -109,450.00 USD | 1,950,000.00 USD | **`ACCUMULATION`** |
| `1h` | -239,970.00 USD | -165,610.00 USD | **`DISTRIBUTION`** |
| `2h` | 431,160.00 USD | -1,290,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 9,050,000.00 USD | 1,010,000.00 USD | **`ACCUMULATION`** |
| `6h` | 14,760,000.00 USD | -3,020,000.00 USD | **`ACCUMULATION`** |
| `8h` | 19,580,000.00 USD | 14,900,000.00 USD | **`ACCUMULATION`** |
| `12h` | 18,080,000.00 USD | -1,330,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,280,000.00 USD | -30,240,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -59,180,000.00 USD | -131,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -231,370,000.00 USD | -681,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+17.22K` | 15m=`-27.38K` | 1h=`-239.97K` | 24h=`+2.28M`
* Futures Capital Netflows: 5m=`-124.68K` | 15m=`+2.33M` | 1h=`-165.61K` | 24h=`-30.24M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3.94` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2.70` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `7.05`
  * Mathematical Lot Sizing: **`8.04 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.24` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `5.49` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `1.13`
  * Mathematical Lot Sizing: **`8.04 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
