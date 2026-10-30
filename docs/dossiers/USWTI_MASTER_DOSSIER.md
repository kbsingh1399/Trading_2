# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 11:20:15 IST` (`2026-10-30 05:50:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.87` | **Live Ask Quote**: `103.92` | **Mid Price**: `103.89`
- **Spread Points**: `46.00` | **Spread BPS**: `4.43 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1,000.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `10.00 USD` | Point Value (0.01 Lot): `0.1000 USD`
  * Allowed Lot Sizing: Min Lot=`0.10` | Step Lot=`0.10` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `104.15` | VWAP Z-Score: `-0.87` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2932` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.07` | Lower -3.00σ Band: `102.24`
  * Upper +2.51σ Band: `105.75` | Lower -2.51σ Band: `102.56`
  * Upper +2.01σ Band: `105.44` | Lower -2.01σ Band: `102.87`
  * Upper +2.00σ Band: `105.43` | Lower -2.00σ Band: `102.88`
  * Upper +1.28σ Band: `104.97` | Lower -1.28σ Band: `103.34`
  * Upper +1.00σ Band: `104.79` | Lower -1.00σ Band: `103.52`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.74` | EMA-20=`103.75` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.36` (Slope: `+0.0000`) | EMA-100=`102.96`
  * Institutional Anchors: EMA-144=`102.76` | EMA-200=`102.54` (Slope: `+0.1591`) | EMA-233=`102.47`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.38` (Distance: `-0.46%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.50%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.81%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.22` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`103.98` | Low=`103.51`
  * New York Session (13:00-21:00 UTC): High=`104.52` | Low=`103.27`
  * Initial Balance (First Hour): IB High=`103.98` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.48` - `104.31`
  * Optimal Trade Entry (OTE 0.705): `104.10`
  * Structural Invalidation Anchor (0.786): `104.72`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.27` | `104.37` | `104.07` | `104.19` | `659` | 68,658.57 USD | -16,423.31 USD | `-23.92%` | 344,559.60 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.19` | `104.19` | `104.01` | `104.08` | `506` | 52,663.47 USD | -22,714.74 USD | `-43.13%` | 321,844.86 USD | `-0.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.09` | `104.19` | `104.06` | `104.13` | `339` | 35,299.73 USD | 6,275.51 USD | `+17.78%` | 328,120.37 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `104.92` | `105.25` | `104.75` | `104.77` | `1,722` | 180,408.77 USD | -111,535.28 USD | `-61.82%` | 827,877.53 USD | `-1.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.76` | `104.86` | `104.28` | `104.28` | `734` | 76,540.79 USD | -68,886.71 USD | `-90.00%` | 758,990.82 USD | `-1.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.27` | `104.37` | `104.01` | `104.13` | `1,504` | 156,610.02 USD | -56,432.10 USD | `-36.03%` | 702,558.72 USD | `-0.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `103.53` | `103.06` | `103.07` | `1,416` | 145,947.12 USD | -131,352.41 USD | `-90.00%` | 670,573.75 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.06` | `105.59` | `103.05` | `104.94` | `7,807` | 819,305.61 USD | 505,426.25 USD | `+61.69%` | 1,176,000.01 USD | `+1.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.92` | `105.25` | `103.91` | `103.99` | `4,862` | 505,599.38 USD | -397,014.28 USD | `-78.52%` | 778,985.73 USD | `-1.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,175,279.87 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -392,114.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,194,880.62 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,175,279.87 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 31,071,414.37 USD | `300,817.26` | `98.89` | `103.28` | `31.42` | 1,321,913.34 USD | `+4.25%` | `3X Cross` |
| `114` | `0x30af...393e` | `LONG` | 18,354,140.49 USD | `177,712.44` | `100.98` | `103.28` | `93.19` | 408,738.61 USD | `+2.23%` | `10X Isolated` |
| `289` | `0x7fda...17d1` | `SHORT` | 8,122,721.96 USD | `78,647.58` | `100.15` | `103.28` | `210.93` | -246,100.11 USD | `-3.03%` | `20X Cross` |
| `328` | `0x10e1...f4bd` | `LONG` | 6,984,400.58 USD | `67,625.88` | `84.36` | `103.28` | `58.53` | 1,279,170.19 USD | `+18.31%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,696,576.23 USD | `55,151.29` | `89.22` | `103.28` | `244.02` | -775,851.73 USD | `-13.62%` | `20X Cross` |
| `412` | `0x354b...6425` | `SHORT` | 5,390,335.54 USD | `52,191.47` | `102.88` | `103.28` | `307.96` | -21,041.00 USD | `-0.39%` | `8X Cross` |
| `486` | `0x4692...164f` | `SHORT` | 4,635,746.97 USD | `44,885.23` | `103.49` | `103.28` | `1499.24` | 9,410.59 USD | `+0.20%` | `5X Cross` |
| `493` | `0x5989...bc29` | `SHORT` | 4,512,480.74 USD | `43,691.72` | `99.48` | `103.28` | `113.23` | -166,173.84 USD | `-3.68%` | `10X Cross` |
| `539` | `0xd84a...c8a5` | `SHORT` | 4,131,600.00 USD | `40,000.00` | `101.97` | `103.28` | `119.15` | -52,970.00 USD | `-1.28%` | `20X Cross` |
| `543` | `0xd507...c948` | `LONG` | 4,111,421.57 USD | `39,808.50` | `93.57` | `103.28` | `82.63` | 386,346.16 USD | `+9.40%` | `7X Isolated` |
| `700` | `0xb5e7...eff1` | `SHORT` | 3,215,654.03 USD | `31,132.29` | `91.71` | `103.28` | `145.04` | -360,445.38 USD | `-11.21%` | `20X Cross` |
| `735` | `0xbd33...4200` | `SHORT` | 3,096,612.74 USD | `29,982.69` | `104.89` | `103.28` | `403.27` | 48,272.14 USD | `+1.56%` | `20X Cross` |
| `786` | `0xebe1...4070` | `LONG` | 2,892,117.21 USD | `27,999.97` | `101.87` | `103.28` | `0.000000` | 39,721.90 USD | `+1.37%` | `20X Cross` |
| `790` | `0x61d7...7dee` | `LONG` | 2,877,183.02 USD | `27,858.08` | `88.25` | `103.28` | `83.50` | 418,707.02 USD | `+14.55%` | `20X Cross` |
| `872` | `0xf0ae...2f74` | `SHORT` | 2,582,000.00 USD | `25,000.00` | `100.78` | `103.28` | `176.47` | -62,481.39 USD | `-2.42%` | `20X Cross` |
| `886` | `0x645b...87b8` | `SHORT` | 2,540,333.96 USD | `24,596.57` | `101.24` | `103.28` | `134.75` | -50,096.59 USD | `-1.97%` | `3X Isolated` |
| `989` | `0x40f2...6a9e` | `LONG` | 2,244,622.25 USD | `21,733.37` | `103.34` | `103.28` | `100.62` | -1,387.71 USD | `-0.06%` | `20X Cross` |
| `1076` | `0x9aa5...58af` | `SHORT` | 2,031,620.88 USD | `19,671.00` | `101.76` | `103.28` | `564.56` | -29,869.95 USD | `-1.47%` | `20X Cross` |
| `1249` | `0x4169...6f06` | `LONG` | 1,773,853.62 USD | `17,175.19` | `76.61` | `103.28` | `82.98` | 458,085.62 USD | `+25.82%` | `12X Isolated` |
| `1258` | `0x6788...98d4` | `SHORT` | 1,755,760.00 USD | `17,000.00` | `99.31` | `103.28` | `198.00` | -67,435.41 USD | `-3.84%` | `20X Cross` |
| `1303` | `0xa99c...40d5` | `SHORT` | 1,662,969.00 USD | `16,100.00` | `101.02` | `103.28` | `154.07` | -36,511.63 USD | `-2.20%` | `20X Cross` |
| `1316` | `0x1bf6...5bfa` | `SHORT` | 1,652,480.00 USD | `16,000.00` | `99.60` | `103.28` | `229.12` | -58,857.69 USD | `-3.56%` | `20X Cross` |
| `1390` | `0xe5dd...ecba` | `SHORT` | 1,567,596.44 USD | `15,178.12` | `102.71` | `103.28` | `146.07` | -8,658.65 USD | `-0.55%` | `20X Cross` |
| `1406` | `0x34ea...2f47` | `SHORT` | 1,549,350.00 USD | `15,000.00` | `99.80` | `103.28` | `197.55` | -52,348.69 USD | `-3.38%` | `20X Cross` |
| `1407` | `0x5d6f...6f8a` | `LONG` | 1,549,200.00 USD | `15,000.00` | `101.91` | `103.28` | `27.20` | 20,545.00 USD | `+1.33%` | `20X Cross` |
| `1451` | `0xfc27...9d9d` | `LONG` | 1,503,280.89 USD | `14,555.39` | `102.69` | `103.28` | `0.000000` | 8,621.91 USD | `+0.57%` | `20X Cross` |
| `1522` | `0xfb29...21dd` | `LONG` | 1,419,122.83 USD | `13,744.53` | `89.85` | `103.28` | `84.62` | 184,128.86 USD | `+12.97%` | `20X Cross` |
| `1547` | `0x6fa6...825e` | `SHORT` | 1,394,280.00 USD | `13,500.00` | `102.95` | `103.28` | `135.50` | -4,505.73 USD | `-0.32%` | `20X Isolated` |
| `1564` | `0xa9d9...b48e` | `SHORT` | 1,377,199.97 USD | `13,333.33` | `96.39` | `103.28` | `174.04` | -91,952.78 USD | `-6.68%` | `20X Cross` |
| `1615` | `0x936c...bb0f` | `SHORT` | 1,310,407.14 USD | `12,687.91` | `101.39` | `103.28` | `163.64` | -23,934.27 USD | `-1.83%` | `2X Isolated` |
| `1652` | `0x89c2...c94b` | `LONG` | 1,277,148.93 USD | `12,364.69` | `75.25` | `103.28` | `45.76` | 346,665.78 USD | `+27.14%` | `3X Isolated` |
| `1693` | `0xcd81...36e3` | `SHORT` | 1,246,086.84 USD | `12,063.96` | `97.96` | `103.28` | `109.11` | -64,247.92 USD | `-5.16%` | `20X Cross` |
| `1701` | `0x436c...b3d1` | `SHORT` | 1,239,360.00 USD | `12,000.00` | `101.05` | `103.28` | `207.49` | -26,700.17 USD | `-2.15%` | `20X Cross` |
| `1765` | `0x9dea...d617` | `LONG` | 1,177,474.42 USD | `11,400.80` | `90.37` | `103.28` | `7.89` | 147,200.69 USD | `+12.50%` | `20X Cross` |
| `1776` | `0x17c3...a868` | `LONG` | 1,167,858.40 USD | `11,306.60` | `95.13` | `103.28` | `64.99` | 92,211.54 USD | `+7.90%` | `3X Isolated` |
| `1823` | `0x8607...08d5` | `SHORT` | 1,135,883.97 USD | `10,998.10` | `92.18` | `103.28` | `135.02` | -122,094.27 USD | `-10.75%` | `4X Isolated` |
| `2008` | `0xce97...7e78` | `SHORT` | 1,007,692.65 USD | `9,757.84` | `103.23` | `103.28` | `120.87` | -341.70 USD | `-0.03%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,011.58 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.01K USD at 94.9130 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,931.10 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.93K USD at 94.9130 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 2,292.43 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.29K USD at 94.9130 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 3,821.71 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 3.82K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 2,292.36 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.29K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,931.88 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.93K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 2,292.84 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.29K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,108.41 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.11K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `84.31` | 5,111.99 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 5.11K USD at 84.3090 USD [API] | `2026-03-11 13:24:34` |
| `ANNOUNCEMENT` | `INFO` | `83.80` | 5,851.98 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 5.85K USD at 83.7960 USD [API] | `2026-03-10 14:40:53` |
| `ANNOUNCEMENT` | `INFO` | `86.06` | 13,470.35 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 13.47K USD at 86.0610 USD [API] | `2026-03-10 07:23:35` |
| `ANNOUNCEMENT` | `INFO` | `91.74` | 26,993.03 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 26.99K USD at 91.7400 USD [API] | `2026-03-09 19:19:31` |
| `ANNOUNCEMENT` | `INFO` | `91.77` | 40,765.73 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 40.77K USD at 91.7680 USD [API] | `2026-03-09 19:19:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.45%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.01%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.45%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--4.01%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.47%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--4.05%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.21%`) | Long MP=`99.12` (Vol: 8,700,000.00 USD, Dist: `--4.05%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.87` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.33` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-185.44K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `05:00:00` | `105.11` | `105.11` | `105.11` | `105.25` | `104.92` | 70,737.01 USD | 47,923.79 USD | 22,813.22 USD | 25,110.57 USD | `+35.50%` | `1B / 0S` |
| `05:00:00` | `103.99` | `103.99` | `103.99` | `105.25` | `103.91` | 505,599.38 USD | 54,292.55 USD | 451,306.83 USD | -397,014.28 USD | `-78.52%` | `0B / 1S` |
| `05:05:00` | `104.96` | `104.96` | `104.96` | `105.18` | `104.86` | 60,772.42 USD | 17,985.61 USD | 42,786.81 USD | -24,801.21 USD | `-40.81%` | `0B / 1S` |
| `05:10:00` | `104.77` | `104.77` | `104.77` | `105.06` | `104.75` | 49,240.49 USD | 7,268.83 USD | 41,971.66 USD | -34,702.82 USD | `-70.48%` | `0B / 1S` |
| `05:15:00` | `104.28` | `104.28` | `104.28` | `104.86` | `104.28` | 76,540.79 USD | 3,827.04 USD | 72,713.75 USD | -68,886.71 USD | `-90.00%` | `0B / 1S` |
| `05:15:00` | `104.69` | `104.69` | `104.69` | `104.86` | `104.66` | 23,870.46 USD | 6,496.76 USD | 17,373.70 USD | -10,876.93 USD | `-45.57%` | `0B / 1S` |
| `05:20:00` | `104.54` | `104.54` | `104.54` | `104.71` | `104.53` | 16,935.48 USD | 940.86 USD | 15,994.62 USD | -15,053.76 USD | `-88.89%` | `0B / 1S` |
| `05:25:00` | `104.28` | `104.28` | `104.28` | `104.53` | `104.28` | 35,871.98 USD | 1,793.60 USD | 34,078.38 USD | -32,284.78 USD | `-90.00%` | `0B / 1S` |
| `05:30:00` | `104.19` | `104.19` | `104.19` | `104.37` | `104.07` | 68,658.57 USD | 26,117.63 USD | 42,540.94 USD | -16,423.31 USD | `-23.92%` | `0B / 1S` |
| `05:30:00` | `104.13` | `104.13` | `104.13` | `104.37` | `104.01` | 156,610.02 USD | 50,088.96 USD | 106,521.06 USD | -56,432.10 USD | `-36.03%` | `0B / 1S` |
| `5:00 UTC` | `103.53` | `103.52` | `103.53` | `103.59` | `103.44` | 3,389,658.00 USD | 1,302,314.80 USD | 2,087,343.19 USD | -785,028.39 USD | `-23.16%` | `2B / 3S` |
| `0:00 UTC` | `103.50` | `103.53` | `103.50` | `103.66` | `103.41` | 4,898,115.03 USD | 2,100,565.02 USD | 2,797,550.01 USD | -696,984.99 USD | `-14.23%` | `4B / 8S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.38` | `103.38` | `103.44` | `103.31` | 5,199,824.51 USD | 3,341,152.42 USD | 1,858,672.10 USD | 1,482,480.32 USD | `+28.51%` | `3B / 2S` |
| `5:00 UTC` | `103.31` | `103.30` | `103.31` | `103.34` | `103.23` | 3,756,770.69 USD | 2,127,360.29 USD | 1,629,410.40 USD | 497,949.89 USD | `+13.25%` | `2B / 1S` |
| `0:00 UTC` | `103.25` | `103.28` | `103.25` | `103.37` | `103.23` | 2,263,324.74 USD | 1,120,957.51 USD | 1,142,367.23 USD | -21,409.73 USD | `-0.95%` | `3B / 0S` |
| `5:00 UTC` | `103.00` | `103.14` | `103.00` | `103.50` | `102.94` | 9,234,794.82 USD | 4,542,925.91 USD | 4,691,868.91 USD | -148,943.00 USD | `-1.61%` | `4B / 6S` |
| `0:00 UTC` | `103.09` | `103.10` | `103.09` | `103.19` | `103.05` | 2,687,690.44 USD | 1,506,949.94 USD | 1,180,740.51 USD | 326,209.43 USD | `+12.14%` | `2B / 0S` |
| `5:00 UTC` | `103.10` | `103.11` | `103.10` | `103.19` | `103.06` | 3,024,324.91 USD | 1,670,672.44 USD | 1,353,652.47 USD | 317,019.96 USD | `+10.48%` | `1B / 0S` |
| `0:00 UTC` | `103.31` | `103.23` | `103.31` | `103.38` | `103.03` | 4,035,943.94 USD | 2,343,962.47 USD | 1,691,981.47 USD | 651,981.00 USD | `+16.15%` | `10B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | WTI_OIL Macro Delta Flow: AGGRESSIVE BUY | `102.68` | 803,986.89 USD | 803,986.89 USD |
| `10-28 18:20` | `Volume 200K CL` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `102.21` | 51,000.00 USD | 0.00 USD |
| `10-28 11:54` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.96` | 0.00 USD | 0.00 USD |
| `10-28 07:12` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.50` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.05` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.63` (Risk Distance: `0.4209` pts)
  * +2.5R Take Profit: `104.11`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.42 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `104.80` (Risk Distance: `0.4209` pts)
  * +2.5R Take Profit: `103.32`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.42 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.72`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
