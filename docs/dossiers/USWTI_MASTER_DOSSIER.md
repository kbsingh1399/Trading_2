# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 11:44:30 IST` (`2026-10-30 06:14:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.01` | **Live Ask Quote**: `104.04` | **Mid Price**: `104.02`
- **Spread Points**: `30.00` | **Spread BPS**: `2.88 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.13` | VWAP Z-Score: `-0.34` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3008` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.46` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.97` | Lower -3.00σ Band: `102.29`
  * Upper +2.51σ Band: `105.67` | Lower -2.51σ Band: `102.59`
  * Upper +2.01σ Band: `105.36` | Lower -2.01σ Band: `102.90`
  * Upper +2.00σ Band: `105.36` | Lower -2.00σ Band: `102.90`
  * Upper +1.28σ Band: `104.92` | Lower -1.28σ Band: `103.35`
  * Upper +1.00σ Band: `104.74` | Lower -1.00σ Band: `103.52`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.80` | EMA-20=`103.78` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.40` (Slope: `+0.0000`) | EMA-100=`103.00`
  * Institutional Anchors: EMA-144=`102.79` | EMA-200=`102.57` (Slope: `+0.1533`) | EMA-233=`102.50`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.31` (Distance: `-0.24%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.66%`)
  * Value Area Low (VAL) = `103.07` (Distance: `+0.96%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.22` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.12` | Low=`103.51`
  * New York Session (13:00-21:00 UTC): High=`104.65` | Low=`103.40`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.61` - `104.44`
  * Optimal Trade Entry (OTE 0.705): `104.23`
  * Structural Invalidation Anchor (0.786): `104.86`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.00` | `104.05` | `103.94` | `104.03` | `276` | 28,710.90 USD | 11,621.08 USD | `+40.48%` | 390,605.47 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.03` | `104.13` | `104.03` | `104.11` | `208` | 21,653.84 USD | 13,106.27 USD | `+60.53%` | 403,711.74 USD | `+0.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.10` | `104.11` | `104.00` | `104.03` | `108` | 11,235.24 USD | -6,106.11 USD | `-54.35%` | 397,605.63 USD | `-0.21` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.27` | `104.37` | `104.01` | `104.13` | `1,504` | 156,610.02 USD | -56,432.10 USD | `-36.03%` | 824,804.22 USD | `-0.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.13` | `104.19` | `103.91` | `103.99` | `902` | 93,798.98 USD | -42,544.54 USD | `-45.36%` | 782,259.69 USD | `-0.55` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.00` | `104.13` | `103.94` | `104.03` | `592` | 61,585.76 USD | 3,328.96 USD | `+5.41%` | 785,588.65 USD | `+0.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `103.06` | `105.59` | `103.05` | `104.94` | `7,807` | 819,305.61 USD | 505,426.25 USD | `+61.69%` | 1,244,230.76 USD | `+1.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.92` | `105.25` | `103.91` | `103.99` | `4,862` | 505,599.38 USD | -397,014.28 USD | `-78.52%` | 847,216.48 USD | `-1.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `104.00` | `104.13` | `103.75` | `103.82` | `2,020` | 209,716.40 USD | -114,516.19 USD | `-54.61%` | 732,700.28 USD | `-0.47` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 31,062,389.85 USD | `300,817.26` | `98.89` | `103.25` | `31.42` | 1,312,888.82 USD | `+4.23%` | `3X Cross` |
| `114` | `0x30af...393e` | `LONG` | 18,350,586.24 USD | `177,712.44` | `100.98` | `103.25` | `93.19` | 405,184.36 USD | `+2.21%` | `10X Isolated` |
| `287` | `0x7fda...17d1` | `SHORT` | 8,121,149.01 USD | `78,647.58` | `100.15` | `103.25` | `210.01` | -244,527.16 USD | `-3.01%` | `20X Cross` |
| `328` | `0x10e1...f4bd` | `LONG` | 6,983,048.06 USD | `67,625.88` | `84.36` | `103.25` | `58.53` | 1,277,817.68 USD | `+18.30%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,694,921.69 USD | `55,151.29` | `89.22` | `103.25` | `240.02` | -774,197.20 USD | `-13.59%` | `20X Cross` |
| `412` | `0x354b...6425` | `SHORT` | 5,380,516.88 USD | `52,106.50` | `102.88` | `103.25` | `309.25` | -19,964.61 USD | `-0.37%` | `8X Cross` |
| `486` | `0x4692...164f` | `SHORT` | 4,588,699.99 USD | `44,438.31` | `103.48` | `103.25` | `1522.30` | 9,885.85 USD | `+0.22%` | `5X Cross` |
| `490` | `0x5989...bc29` | `SHORT` | 4,511,606.90 USD | `43,691.72` | `99.48` | `103.25` | `113.23` | -165,300.00 USD | `-3.66%` | `10X Cross` |
| `538` | `0xd84a...c8a5` | `SHORT` | 4,130,400.00 USD | `40,000.00` | `101.97` | `103.25` | `119.16` | -51,770.00 USD | `-1.25%` | `20X Cross` |
| `542` | `0xd507...c948` | `LONG` | 4,110,625.40 USD | `39,808.50` | `93.57` | `103.25` | `82.63` | 385,549.99 USD | `+9.38%` | `7X Isolated` |
| `703` | `0xb5e7...eff1` | `SHORT` | 3,214,720.06 USD | `31,132.29` | `91.71` | `103.25` | `144.85` | -359,511.41 USD | `-11.18%` | `20X Cross` |
| `739` | `0xbd33...4200` | `SHORT` | 3,096,013.09 USD | `29,982.69` | `104.89` | `103.25` | `403.27` | 48,871.79 USD | `+1.58%` | `20X Cross` |
| `789` | `0xebe1...4070` | `LONG` | 2,891,277.21 USD | `27,999.97` | `101.87` | `103.25` | `0.000000` | 38,881.90 USD | `+1.34%` | `20X Cross` |
| `794` | `0x61d7...7dee` | `LONG` | 2,876,625.86 USD | `27,858.08` | `88.25` | `103.25` | `83.50` | 418,149.86 USD | `+14.54%` | `20X Cross` |
| `872` | `0xf0ae...2f74` | `SHORT` | 2,581,500.00 USD | `25,000.00` | `100.78` | `103.25` | `176.65` | -61,981.39 USD | `-2.40%` | `20X Cross` |
| `883` | `0x645b...87b8` | `SHORT` | 2,539,842.02 USD | `24,596.57` | `101.24` | `103.25` | `134.75` | -49,604.66 USD | `-1.95%` | `3X Isolated` |
| `983` | `0x40f2...6a9e` | `LONG` | 2,244,187.58 USD | `21,733.37` | `103.34` | `103.25` | `100.59` | -1,822.38 USD | `-0.08%` | `20X Cross` |
| `1074` | `0x9aa5...58af` | `SHORT` | 2,031,227.46 USD | `19,671.00` | `101.76` | `103.25` | `569.86` | -29,476.53 USD | `-1.45%` | `20X Cross` |
| `1248` | `0x4169...6f06` | `LONG` | 1,773,510.12 USD | `17,175.19` | `76.61` | `103.25` | `82.98` | 457,742.12 USD | `+25.81%` | `12X Isolated` |
| `1259` | `0x6788...98d4` | `SHORT` | 1,755,420.00 USD | `17,000.00` | `99.31` | `103.25` | `197.76` | -67,095.41 USD | `-3.82%` | `20X Cross` |
| `1308` | `0xa99c...40d5` | `SHORT` | 1,662,486.00 USD | `16,100.00` | `101.02` | `103.25` | `153.48` | -36,028.63 USD | `-2.17%` | `20X Cross` |
| `1316` | `0x1bf6...5bfa` | `SHORT` | 1,652,160.00 USD | `16,000.00` | `99.60` | `103.25` | `227.85` | -58,537.69 USD | `-3.54%` | `20X Cross` |
| `1386` | `0xe5dd...ecba` | `SHORT` | 1,567,292.88 USD | `15,178.12` | `102.71` | `103.25` | `146.02` | -8,355.09 USD | `-0.53%` | `20X Cross` |
| `1396` | `0x34ea...2f47` | `SHORT` | 1,548,900.00 USD | `15,000.00` | `99.80` | `103.25` | `198.44` | -51,898.69 USD | `-3.35%` | `20X Cross` |
| `1397` | `0x5d6f...6f8a` | `LONG` | 1,548,900.00 USD | `15,000.00` | `101.91` | `103.25` | `27.21` | 20,245.00 USD | `+1.31%` | `20X Cross` |
| `1443` | `0xfc27...9d9d` | `LONG` | 1,502,989.78 USD | `14,555.39` | `102.69` | `103.25` | `0.000000` | 8,330.80 USD | `+0.55%` | `20X Cross` |
| `1512` | `0xfb29...21dd` | `LONG` | 1,419,397.72 USD | `13,744.53` | `89.85` | `103.25` | `84.64` | 184,403.76 USD | `+12.99%` | `20X Cross` |
| `1535` | `0x6fa6...825e` | `SHORT` | 1,394,010.00 USD | `13,500.00` | `102.95` | `103.25` | `135.50` | -4,235.73 USD | `-0.30%` | `20X Isolated` |
| `1556` | `0xa9d9...b48e` | `SHORT` | 1,376,799.97 USD | `13,333.33` | `96.39` | `103.25` | `173.93` | -91,552.78 USD | `-6.65%` | `20X Cross` |
| `1609` | `0x936c...bb0f` | `SHORT` | 1,310,153.38 USD | `12,687.91` | `101.39` | `103.25` | `163.64` | -23,680.51 USD | `-1.81%` | `2X Isolated` |
| `1645` | `0x89c2...c94b` | `LONG` | 1,276,777.99 USD | `12,364.69` | `75.25` | `103.25` | `45.76` | 346,294.84 USD | `+27.12%` | `3X Isolated` |
| `1681` | `0xcd81...36e3` | `SHORT` | 1,245,724.92 USD | `12,063.96` | `97.96` | `103.25` | `108.90` | -63,886.00 USD | `-5.13%` | `20X Cross` |
| `1688` | `0x436c...b3d1` | `SHORT` | 1,239,120.00 USD | `12,000.00` | `101.05` | `103.25` | `207.59` | -26,460.17 USD | `-2.14%` | `20X Cross` |
| `1751` | `0x9dea...d617` | `LONG` | 1,177,246.40 USD | `11,400.80` | `90.37` | `103.25` | `8.11` | 146,972.68 USD | `+12.48%` | `20X Cross` |
| `1766` | `0x17c3...a868` | `LONG` | 1,167,519.21 USD | `11,306.60` | `95.13` | `103.25` | `64.99` | 91,872.34 USD | `+7.87%` | `3X Isolated` |
| `1808` | `0x8607...08d5` | `SHORT` | 1,135,664.01 USD | `10,998.10` | `92.18` | `103.25` | `135.02` | -121,874.31 USD | `-10.73%` | `4X Isolated` |
| `1985` | `0xce97...7e78` | `SHORT` | 1,010,718.59 USD | `9,788.09` | `103.23` | `103.25` | `120.87` | -240.18 USD | `-0.02%` | `5X Isolated` |

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
| `Envelope` | `Long Liquidation` | `103.17` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.67` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-178.69K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
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
| `05:30:00` | `104.19` | `104.19` | `104.19` | `104.37` | `104.07` | 68,658.57 USD | 26,117.63 USD | 42,540.94 USD | -16,423.31 USD | `-23.92%` | `0B / 1S` |
| `05:35:00` | `104.08` | `104.08` | `104.08` | `104.19` | `104.01` | 52,663.47 USD | 14,974.37 USD | 37,689.10 USD | -22,714.74 USD | `-43.13%` | `0B / 1S` |
| `05:40:00` | `104.13` | `104.13` | `104.13` | `104.19` | `104.06` | 35,299.73 USD | 20,787.62 USD | 14,512.11 USD | 6,275.51 USD | `+17.78%` | `1B / 0S` |
| `05:45:00` | `104.03` | `104.03` | `104.03` | `104.19` | `104.01` | 31,313.03 USD | 4,965.35 USD | 26,347.68 USD | -21,382.33 USD | `-68.29%` | `0B / 1S` |
| `05:45:00` | `103.99` | `103.99` | `103.99` | `104.19` | `103.91` | 93,798.98 USD | 25,627.22 USD | 68,171.76 USD | -42,544.54 USD | `-45.36%` | `0B / 1S` |
| `05:50:00` | `103.96` | `103.96` | `103.96` | `104.12` | `103.92` | 29,940.48 USD | 7,485.12 USD | 22,455.36 USD | -14,970.24 USD | `-50.00%` | `0B / 1S` |
| `05:55:00` | `103.99` | `103.99` | `103.99` | `104.11` | `103.91` | 32,548.87 USD | 16,274.43 USD | 16,274.44 USD | -0.00 USD | `-0.00%` | `0B / 1S` |
| `06:00:00` | `104.03` | `104.03` | `104.03` | `104.05` | `103.94` | 28,710.90 USD | 20,165.99 USD | 8,544.91 USD | 11,621.08 USD | `+40.48%` | `1B / 0S` |
| `06:00:00` | `103.82` | `103.82` | `103.82` | `104.13` | `103.75` | 209,716.40 USD | 47,600.10 USD | 162,116.30 USD | -114,516.19 USD | `-54.61%` | `0B / 1S` |
| `06:00:00` | `104.03` | `104.03` | `104.03` | `104.13` | `103.94` | 61,585.76 USD | 32,457.36 USD | 29,128.40 USD | 3,328.96 USD | `+5.41%` | `1B / 0S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.38` | `103.38` | `103.44` | `103.31` | 5,199,824.51 USD | 3,341,152.42 USD | 1,858,672.10 USD | 1,482,480.32 USD | `+28.51%` | `3B / 2S` |
| `5:00 UTC` | `103.31` | `103.30` | `103.31` | `103.34` | `103.23` | 3,756,770.69 USD | 2,127,360.29 USD | 1,629,410.40 USD | 497,949.89 USD | `+13.25%` | `2B / 1S` |
| `0:00 UTC` | `103.25` | `103.28` | `103.25` | `103.37` | `103.23` | 2,263,324.74 USD | 1,120,957.51 USD | 1,142,367.23 USD | -21,409.73 USD | `-0.95%` | `3B / 0S` |
| `5:00 UTC` | `103.00` | `103.14` | `103.00` | `103.50` | `102.94` | 9,234,794.82 USD | 4,542,925.91 USD | 4,691,868.91 USD | -148,943.00 USD | `-1.61%` | `4B / 6S` |
| `0:00 UTC` | `103.09` | `103.10` | `103.09` | `103.19` | `103.05` | 2,687,690.44 USD | 1,506,949.94 USD | 1,180,740.51 USD | 326,209.43 USD | `+12.14%` | `2B / 0S` |
| `5:00 UTC` | `103.10` | `103.11` | `103.10` | `103.19` | `103.06` | 3,024,324.91 USD | 1,670,672.44 USD | 1,353,652.47 USD | 317,019.96 USD | `+10.48%` | `1B / 0S` |
| `0:00 UTC` | `103.31` | `103.29` | `103.31` | `103.48` | `103.03` | 6,474,098.12 USD | 3,535,065.19 USD | 2,939,032.93 USD | 596,032.26 USD | `+9.21%` | `13B / 4S` |
| `5:00 UTC` | `103.52` | `103.51` | `103.52` | `103.65` | `103.40` | 5,786,936.58 USD | 3,197,963.81 USD | 2,588,972.77 USD | 608,991.03 USD | `+10.52%` | `7B / 1S` |
| `0:00 UTC` | `103.40` | `103.39` | `103.40` | `103.52` | `103.28` | 2,687,670.13 USD | 1,440,900.66 USD | 1,246,769.47 USD | 194,131.19 USD | `+7.22%` | `5B / 2S` |

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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.07` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.66` (Risk Distance: `0.4059` pts)
  * +2.5R Take Profit: `104.08`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.41 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.31` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `104.71` (Risk Distance: `0.4059` pts)
  * +2.5R Take Profit: `103.29`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.41 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.86`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
