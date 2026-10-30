# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:45:52 IST` (`2026-10-30 11:15:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.32` | **Live Ask Quote**: `4.35` | **Mid Price**: `4.34`
- **Spread Points**: `31.00` | **Spread BPS**: `71.45 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.15` | VWAP Z-Score: `+1.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0527` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `61.33` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.59` | Lower -3.00σ Band: `3.71`
  * Upper +2.51σ Band: `4.52` | Lower -2.51σ Band: `3.79`
  * Upper +2.01σ Band: `4.45` | Lower -2.01σ Band: `3.86`
  * Upper +2.00σ Band: `4.45` | Lower -2.00σ Band: `3.86`
  * Upper +1.28σ Band: `4.34` | Lower -1.28σ Band: `3.97`
  * Upper +1.00σ Band: `4.30` | Lower -1.00σ Band: `4.01`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.33` | EMA-20=`4.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.25` (Slope: `+0.0000`) | EMA-100=`4.29`
  * Institutional Anchors: EMA-144=`4.33` | EMA-200=`4.38` (Slope: `-0.1652`) | EMA-233=`4.41`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.25` (Distance: `+2.15%`)
  * Point of Control (POC) = `4.07` (Distance: `+6.68%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+10.18%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.71` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.37` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.37` | Low=`4.30`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.32` - `4.36`
  * Optimal Trade Entry (OTE 0.705): `4.35`
  * Structural Invalidation Anchor (0.786): `4.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.38` | `4.38` | `4.35` | `4.36` | `603,484` | 2,633,752.60 USD | -508,403.64 USD | `-19.30%` | -5,363,441.95 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.36` | `4.36` | `4.34` | `4.35` | `286,206` | 1,246,358.91 USD | 135,862.82 USD | `+10.90%` | -5,227,579.14 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4.35` | `4.36` | `4.34` | `4.34` | `71,679` | 311,354.04 USD | -117,839.58 USD | `-37.85%` | -5,345,418.72 USD | `-0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.32` | `4.35` | `4.32` | `4.35` | `1,820,116` | 7,895,783.86 USD | 2,079,303.28 USD | `+26.33%` | -5,528,917.54 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.35` | `4.38` | `4.33` | `4.38` | `1,136,755` | 4,949,414.64 USD | 673,879.22 USD | `+13.62%` | -4,855,038.31 USD | `+0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.38` | `4.38` | `4.34` | `4.34` | `961,369` | 4,191,465.56 USD | -490,380.41 USD | `-11.70%` | -5,345,418.72 USD | `-0.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.36` | `4.38` | `4.29` | `4.38` | `6,481,728` | 28,107,012.78 USD | 1,024,636.46 USD | `+3.65%` | -5,216,573.84 USD | `+0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `4.38` | `4.38` | `4.32` | `4.38` | `6,100,339` | 26,496,802.91 USD | 1,348,167.25 USD | `+5.09%` | -3,868,406.58 USD | `+0.33` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.38` | `4.38` | `4.34` | `4.34` | `957,297` | 4,173,795.95 USD | -484,020.52 USD | `-11.60%` | -4,352,427.10 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.34` | `28,769,145` | 124,655,070.52 USD | 10,689,388.56 USD | `+8.58%` | -4,361,660.37 USD | `+1.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | 240,083.28 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -11,802,955.99 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.34` | `28,769,145` | 124,655,070.52 USD | 10,689,388.56 USD | `+8.58%` | -4,361,660.37 USD | `+1.61` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`4.34`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `57` | `0x7737...bf66` | `LONG` | 24,502,358.68 USD | `5,640,376.30` | `2.35` | `4.34` | `0.8422` | 11,230,455.86 USD | `+45.83%` | `10X Cross` |
| `93` | `0xefe4...194b` | `SHORT` | 19,576,393.22 USD | `4,507,262.50` | `4.21` | `4.34` | `6.33` | -601,296.50 USD | `-3.07%` | `5X Cross` |
| `124` | `0xb581...6f4f` | `LONG` | 15,636,600.00 USD | `3,600,000.00` | `5.19` | `4.34` | `0.000000` | -3,056,435.22 USD | `-19.55%` | `4X Cross` |
| `200` | `0xdd53...2b13` | `SHORT` | 10,425,277.39 USD | `2,400,202.00` | `2.31` | `4.34` | `28.63` | -4,879,428.83 USD | `-46.80%` | `3X Cross` |
| `257` | `0x77ee...2902` | `LONG` | 8,960,121.93 USD | `2,063,023.10` | `1.93` | `4.34` | `0.000000` | 4,968,925.99 USD | `+55.46%` | `10X Cross` |
| `338` | `0x7fda...17d1` | `SHORT` | 6,817,052.57 USD | `1,569,556.00` | `4.29` | `4.34` | `23.81` | -89,198.46 USD | `-1.31%` | `10X Cross` |
| `353` | `0x9df2...c665` | `SHORT` | 6,577,059.31 USD | `1,514,579.00` | `2.36` | `4.34` | `18.10` | -2,997,069.64 USD | `-45.57%` | `10X Cross` |
| `366` | `0xb83d...6e36` | `SHORT` | 6,278,208.89 USD | `1,445,759.10` | `5.19` | `4.34` | `74.31` | 1,231,240.05 USD | `+19.61%` | `3X Cross` |
| `387` | `0xb46b...538e` | `SHORT` | 5,802,916.00 USD | `1,336,000.00` | `4.33` | `4.34` | `7.39` | -18,051.94 USD | `-0.31%` | `10X Cross` |
| `451` | `0x60b0...991e` | `LONG` | 4,874,434.09 USD | `1,121,307.10` | `5.00` | `4.34` | `0.000000` | -726,990.34 USD | `-14.91%` | `10X Cross` |
| `494` | `0x781e...96b7` | `SHORT` | 4,515,938.42 USD | `1,039,604.60` | `2.45` | `4.34` | `7.51` | -1,971,601.23 USD | `-43.66%` | `10X Cross` |
| `565` | `0x4cae...7c34` | `LONG` | 3,954,863.20 USD | `910,587.40` | `3.98` | `4.34` | `3.04` | 333,167.91 USD | `+8.42%` | `10X Cross` |
| `566` | `0x45d2...4029` | `SHORT` | 3,950,342.66 USD | `909,400.00` | `3.26` | `4.34` | `48.50` | -984,192.76 USD | `-24.91%` | `10X Cross` |
| `805` | `0x005a...61fe` | `LONG` | 2,833,567.09 USD | `652,414.60` | `2.08` | `4.34` | `2.41` | 1,476,035.85 USD | `+52.09%` | `7X Cross` |
| `812` | `0xba5d...a352` | `SHORT` | 2,812,557.41 USD | `647,532.50` | `2.83` | `4.34` | `11.36` | -979,842.47 USD | `-34.84%` | `10X Cross` |
| `823` | `0xb695...a92d` | `SHORT` | 2,776,758.58 USD | `639,231.70` | `4.57` | `4.34` | `38.45` | 146,600.35 USD | `+5.28%` | `10X Cross` |
| `824` | `0xd1dd...9e85` | `SHORT` | 2,770,021.73 USD | `637,783.60` | `4.96` | `4.34` | `13.47` | 394,158.37 USD | `+14.23%` | `10X Cross` |
| `835` | `0x123d...3bff` | `SHORT` | 2,713,436.11 USD | `624,568.10` | `2.09` | `4.34` | `9.15` | -1,408,011.93 USD | `-51.89%` | `10X Cross` |
| `839` | `0xcf53...ee11` | `SHORT` | 2,700,534.25 USD | `621,598.40` | `5.07` | `4.34` | `25.07` | 451,636.00 USD | `+16.72%` | `10X Cross` |
| `961` | `0xbfc7...80b4` | `SHORT` | 2,306,398.50 USD | `531,000.00` | `2.01` | `4.34` | `7.10` | -1,241,199.11 USD | `-53.82%` | `10X Cross` |
| `1102` | `0xf382...578c` | `SHORT` | 1,975,615.16 USD | `454,948.80` | `4.32` | `4.34` | `6.37` | -12,110.65 USD | `-0.61%` | `10X Cross` |
| `1195` | `0x0eec...d4c5` | `LONG` | 1,851,629.58 USD | `426,318.60` | `4.02` | `4.34` | `2.05` | 137,244.32 USD | `+7.41%` | `10X Cross` |
| `1265` | `0xe097...d0fe` | `LONG` | 1,737,400.00 USD | `400,000.00` | `5.29` | `4.34` | `0.000000` | -379,387.30 USD | `-21.84%` | `10X Cross` |
| `1362` | `0xef96...9383` | `SHORT` | 1,575,282.70 USD | `362,433.90` | `4.50` | `4.34` | `13.67` | 55,583.31 USD | `+3.53%` | `10X Cross` |
| `1370` | `0x6e8f...4364` | `LONG` | 1,568,556.60 USD | `361,210.50` | `3.28` | `4.34` | `3.53` | 384,496.37 USD | `+24.51%` | `10X Cross` |
| `1419` | `0xdf95...7d72` | `SHORT` | 1,521,519.49 USD | `350,217.40` | `4.23` | `4.34` | `109.87` | -39,289.51 USD | `-2.58%` | `10X Cross` |
| `1420` | `0xcf67...eb24` | `LONG` | 1,521,240.00 USD | `350,000.00` | `1.98` | `4.34` | `1.50` | 829,622.12 USD | `+54.54%` | `10X Cross` |
| `1553` | `0xfc27...9d9d` | `SHORT` | 1,390,038.01 USD | `319,997.70` | `5.01` | `4.34` | `61.91` | 213,504.61 USD | `+15.36%` | `10X Cross` |
| `1557` | `0x089f...a4f8` | `LONG` | 1,385,668.86 USD | `319,043.30` | `4.06` | `4.34` | `0.000000` | 90,812.15 USD | `+6.55%` | `1X Cross` |
| `1599` | `0x17c3...a868` | `LONG` | 1,329,273.88 USD | `306,037.50` | `4.36` | `4.34` | `0.000000` | -5,879.10 USD | `-0.44%` | `3X Cross` |
| `1684` | `0xe065...0f85` | `SHORT` | 1,251,884.46 USD | `288,027.90` | `2.81` | `4.34` | `5.56` | -441,331.34 USD | `-35.25%` | `10X Cross` |
| `1884` | `0xff43...d924` | `LONG` | 1,083,592.49 USD | `249,474.50` | `4.64` | `4.34` | `3.28` | -74,451.19 USD | `-6.87%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `4.38` | 14.90 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.01K USD at 4.3826 USD [API] | `2026-10-29 19:46:11` |
| `ANNOUNCEMENT` | `INFO` | `4.37` | 5,884.83 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.88K USD at 4.3669 USD [API] | `2026-10-29 20:17:44` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 1,727.42 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.73K USD at 4.2960 USD [API] | `2026-10-29 20:35:36` |


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
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 1,650.00 USD | 21,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 21,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 914.48 USD | 21,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 7,970.00 USD | 21,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 1,250.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 184,880.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 8,590.00 USD | 21,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 112.77 USD | 21,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 21,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 21,250.00 USD | 21,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 2,940.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 4,330.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 19,530.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 13,410.00 USD | 21,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 1,570.00 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 178.20 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 27,080.00 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 54,270.00 USD | 21,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 2,470.00 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 147.18 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 23,010.00 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 7,200.00 USD | 21,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 3,150.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 1,610.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 14,030.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 7,490.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,580.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 165.11 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 2,040.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 4,060.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 4,660.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,000.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 12,760.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 4,410.00 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 1,080.00 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 79,170.00 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 869.25 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 14,540.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 521,920.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 3,300.00 USD | 20,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 2,260.00 USD | 20,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.49` | 2,970.00 USD | 20,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 74,750.00 USD | 20,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 21,520.00 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 1,440.00 USD | 20,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 1,980.00 USD | 20,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 8,620.00 USD | 20,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 191.64 USD | 20,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 1,230.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 2,600.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,190.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 1,430.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 12,900.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 12,900.00 USD | 20,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 12,850.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 593.25 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 1,820.00 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 6,990.00 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 6,430.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 892.74 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,250.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 9,610.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 2,330.00 USD | 20,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 20,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 3,040.00 USD | 20,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 20,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 921.21 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 984.26 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 34,600.00 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 10,530.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,080.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 288.61 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 192.46 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 154.77 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 34,400.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 3,190.00 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 2,190.00 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 3,990.00 USD | 20,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 34,960.00 USD | 20,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 317.01 USD | 20,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 3,950.00 USD | 20,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 18,610.00 USD | 20,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 6,820.00 USD | 20,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 2,130.00 USD | 20,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 31,940.00 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 349.35 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 878,740.00 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 12,110.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 24,370.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 2,500.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 204,510.00 USD | 19,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 17,810.00 USD | 19,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 5,370.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 2,140.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,110.00 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 857.04 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 279,280.00 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 64,960.00 USD | 18,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,090.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 15,220.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 25,780.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 189,380.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 8,130.00 USD | 18,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 968.27 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 118,720.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 1,400.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 5,080.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 91,400.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 6,790.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 6,510.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 233,830.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 39,350.00 USD | 18,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 13,380.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 2,940.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 324.28 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 1,580.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 35,890.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 10,610.00 USD | 17,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 115.20 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570,000.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 185,540.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 279,590.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,840.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 9,320.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 1,240.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 2,240.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 3,980.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 6,100.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 8,750.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 32,820.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 12,780.00 USD | 15,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 105.36 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 171,930.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 7,890.00 USD | 15,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,260.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 905.27 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 80,550.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 2,450.00 USD | 15,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 15,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 3,970.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 24,310.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 94,920.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 19,200.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 2,060.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,470.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 6,180.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 733.85 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 165,150.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,750.00 USD | 15,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 33,230.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 6,780.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 458.96 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 65,100.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 351,110.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 398.77 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 165,340.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 37,500.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 14,750.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 4,900.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 12,400.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,400.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 180.94 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 6,560.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 204,500.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 955,250.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 6,140.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 15,720.00 USD | 13,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 972.88 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 5,330.00 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 56,870.00 USD | 13,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 58,110.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 16,860.00 USD | 13,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 15,120.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 3,600.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 2,720,000.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 142,650.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 9,550.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 10,410.00 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 29,380.00 USD | 10,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 22,390.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 1,220.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 179,200.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 288,840.00 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 207,190.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 341.33 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 61,690.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 11,170.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 20,090.00 USD | 9,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 28,150.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,150.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 7,730.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,790.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,420.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 13,800.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 8,810.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 246,080.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 267.30 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 8,530.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,360.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 38,940.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 19,930.00 USD | 9,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 8,870.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 33,980.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 902,150.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 4,600.00 USD | 8,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 137,100.00 USD | 8,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 57,540.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 24,690.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 84,230.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 73,460.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 18,900.00 USD | 7,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 64,530.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 24,110.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,530.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 160,800.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 41,460.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 98,820.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 395,600.00 USD | 7,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 5,550.00 USD | 6,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 25,380.00 USD | 6,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 26,330.00 USD | 6,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 20,020.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 16,370.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 108,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 30,100.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 39,080.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 117,220.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 1,310,000.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 19,490,000.00 USD | 19,490,000.00 USD | 18,870.00 USD | 0.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 24,880.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 19,430,000.00 USD | 19,430,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 84,800.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 19,200,000.00 USD | 19,200,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 152,640.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 19,100,000.00 USD | 19,100,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 765,400.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 18,880,000.00 USD | 18,880,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 6,720.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 18,810,000.00 USD | 18,810,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 61,730.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 18,620,000.00 USD | 18,620,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 257,540.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 18,330,000.00 USD | 18,330,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 111,370.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 18,310,000.00 USD | 18,310,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 63,970.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 18,210,000.00 USD | 18,210,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 31,540.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 18,070,000.00 USD | 18,070,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 116,150.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 17,850,000.00 USD | 17,850,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 13,010.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 17,790,000.00 USD | 17,790,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 110,940.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 17,630,000.00 USD | 17,630,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 21,970.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 17,540,000.00 USD | 17,540,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 39,480.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 17,360,000.00 USD | 17,360,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 92,300.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 17,240,000.00 USD | 17,240,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 231,620.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 17,240,000.00 USD | 17,240,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 93,020.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.70` | 17,160,000.00 USD | 17,160,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 90,900.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.71` | 17,020,000.00 USD | 17,020,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 68,070.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.72` | 16,890,000.00 USD | 16,890,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 165,540.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.73` | 16,890,000.00 USD | 16,890,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 116,730.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.74` | 16,780,000.00 USD | 16,780,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,270.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.75` | 16,490,000.00 USD | 16,490,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 151,930.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.76` | 16,300,000.00 USD | 16,300,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 80,140.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.77` | 16,240,000.00 USD | 16,240,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 27,310.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.78` | 16,190,000.00 USD | 16,190,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 172,570.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.79` | 16,030,000.00 USD | 16,030,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 37,390.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.80` | 15,840,000.00 USD | 15,840,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 570,030.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.81` | 15,780,000.00 USD | 15,780,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 13,490.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.82` | 15,770,000.00 USD | 15,770,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 132,570.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.83` | 15,720,000.00 USD | 15,720,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 171,380.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.84` | 15,620,000.00 USD | 15,620,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 116,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.85` | 15,580,000.00 USD | 15,580,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 23,650.00 USD | 951,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 18,400,000.00 USD | 18,400,000.00 USD | 225,350.00 USD | 214,520.00 USD | 92,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 15,440,000.00 USD | 15,440,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 57,420.00 USD | 927,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 17,870,000.00 USD | 17,870,000.00 USD | 53,480.00 USD | 58,230.00 USD | 189,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 15,220,000.00 USD | 15,220,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 4,540.00 USD | 870,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 17,570,000.00 USD | 17,570,000.00 USD | 35,520.00 USD | 26,560.00 USD | 223,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 14,960,000.00 USD | 14,960,000.00 USD | 110,160.00 USD | 86,900.00 USD | 118,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 196,390.00 USD | 865,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 17,290,000.00 USD | 17,290,000.00 USD | 397,250.00 USD | 100,370.00 USD | 256,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 14,650,000.00 USD | 14,650,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 96,480.00 USD | 669,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 16,530,000.00 USD | 16,530,000.00 USD | 33,540.00 USD | 53,910.00 USD | 250,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 14,510,000.00 USD | 14,510,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 8,860.00 USD | 572,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 16,190,000.00 USD | 16,190,000.00 USD | 378,850.00 USD | 120,100.00 USD | 305,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 14,160,000.00 USD | 14,160,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 34,840.00 USD | 563,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 15,390,000.00 USD | 15,390,000.00 USD | 343,070.00 USD | 19,190.00 USD | 122,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 13,920,000.00 USD | 13,920,000.00 USD | 178,620.00 USD | 66,710.00 USD | 105,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 2,050.00 USD | 529,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 14,900,000.00 USD | 14,900,000.00 USD | 116,350.00 USD | 104,340.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 2,940.00 USD | 527,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 14,580,000.00 USD | 14,580,000.00 USD | 144,900.00 USD | 53,060.00 USD | 141,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 13,540,000.00 USD | 13,540,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 8,820.00 USD | 524,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 14,240,000.00 USD | 14,240,000.00 USD | 103,590.00 USD | 0.00 USD | 33,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 13,480,000.00 USD | 13,480,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 34,360.00 USD | 515,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 14,110,000.00 USD | 14,110,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 13,470,000.00 USD | 13,470,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 2,570.00 USD | 480,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 14,000,000.00 USD | 14,000,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 13,310,000.00 USD | 13,310,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 39,920.00 USD | 478,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 13,820,000.00 USD | 13,820,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 13,070,000.00 USD | 13,070,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 1,070.00 USD | 438,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 13,630,000.00 USD | 13,630,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 12,280,000.00 USD | 12,280,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 160,280.00 USD | 437,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 13,430,000.00 USD | 13,430,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 11,880,000.00 USD | 11,880,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 16,820.00 USD | 277,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 13,230,000.00 USD | 13,230,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 10,930,000.00 USD | 10,930,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 1,520.00 USD | 260,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 12,850,000.00 USD | 12,850,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 10,060,000.00 USD | 10,060,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 852.50 USD | 258,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 12,530,000.00 USD | 12,530,000.00 USD | 66,220.00 USD | 59,350.00 USD | 269.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 9,380,000.00 USD | 9,380,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 26,000.00 USD | 257,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 12,410,000.00 USD | 12,410,000.00 USD | 70,930.00 USD | 21,940.00 USD | 183,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 8,790,000.00 USD | 8,790,000.00 USD | 321,230.00 USD | 0.00 USD | 492,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 21,310.00 USD | 231,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 12,130,000.00 USD | 12,130,000.00 USD | 348,930.00 USD | 23,720.00 USD | 119.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 7,970,000.00 USD | 7,970,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 4,190.00 USD | 210,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 11,760,000.00 USD | 11,760,000.00 USD | 36,520.00 USD | 83,800.00 USD | 450,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 249.18 USD | 206,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 11,190,000.00 USD | 11,190,000.00 USD | 359,790.00 USD | 205,460.00 USD | 334,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 7,790,000.00 USD | 7,790,000.00 USD | 2,470.00 USD | 287,180.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 2,640.00 USD | 206,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 10,290,000.00 USD | 10,290,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 60,100.00 USD | 203,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 9,810,000.00 USD | 9,810,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 7,090,000.00 USD | 7,090,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 20,870.00 USD | 143,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 9,330,000.00 USD | 9,330,000.00 USD | 4,790.00 USD | 89,650.00 USD | 140,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 6,230,000.00 USD | 6,230,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 27,440.00 USD | 122,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 9,100,000.00 USD | 9,100,000.00 USD | 122,090.00 USD | 138,540.00 USD | 345,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 25,170.00 USD | 296,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 44,440.00 USD | 95,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 8,490,000.00 USD | 8,490,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 5,880,000.00 USD | 5,880,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.12` | 4,290.00 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 8,130,000.00 USD | 8,130,000.00 USD | 160,580.00 USD | 0.00 USD | 398,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 5,700,000.00 USD | 5,700,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 15,520.00 USD | 50,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 7,580,000.00 USD | 7,580,000.00 USD | 141,770.00 USD | 29,960.00 USD | 125,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 5,300,000.00 USD | 5,300,000.00 USD | 241,440.00 USD | 244,270.00 USD | 345,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 9,380.00 USD | 35,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 7,280,000.00 USD | 7,280,000.00 USD | 526,070.00 USD | 109,290.00 USD | 367,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 4,470,000.00 USD | 4,470,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.16` | 6,270,000.00 USD | 6,270,000.00 USD | 340,550.00 USD | 100,580.00 USD | 379,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 22,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.17` | 5,450,000.00 USD | 5,450,000.00 USD | 340,700.00 USD | 302,060.00 USD | 310,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 4,120,000.00 USD | 4,120,000.00 USD | 252,690.00 USD | 84,340.00 USD | 78,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 4,500,000.00 USD | 4,500,000.00 USD | 389,120.00 USD | 75,540.00 USD | 201,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 3,710,000.00 USD | 3,710,000.00 USD | 227,940.00 USD | 0.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.19` | 3,840,000.00 USD | 3,840,000.00 USD | 148,260.00 USD | 152,090.00 USD | 245,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 3,390,000.00 USD | 3,390,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.20` | 3,290,000.00 USD | 3,290,000.00 USD | 31,500.00 USD | 53,380.00 USD | 132,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 2,950,000.00 USD | 2,950,000.00 USD | 227,690.00 USD | 107,510.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.21` | 3,070,000.00 USD | 3,070,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 2,240,000.00 USD | 2,240,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.22` | 2,270,000.00 USD | 2,270,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 1,780,000.00 USD | 1,780,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.23` | 2,070,000.00 USD | 2,070,000.00 USD | 113,770.00 USD | 129,320.00 USD | 274,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 1,100,000.00 USD | 1,100,000.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.24` | 1,550,000.00 USD | 1,550,000.00 USD | 127,260.00 USD | 98,020.00 USD | 125,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 921,810.00 USD | 921,810.00 USD | 0.00 USD | 45,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.25` | 1,200,000.00 USD | 1,200,000.00 USD | 251,300.00 USD | 37,270.00 USD | 329,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 876,050.00 USD | 876,050.00 USD | 3,390.00 USD | 0.00 USD | 156,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.26` | 583,440.00 USD | 583,440.00 USD | 120,080.00 USD | 26,390.00 USD | 86,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 716,130.00 USD | 716,130.00 USD | 458,850.00 USD | 0.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.27` | 350,640.00 USD | 350,640.00 USD | 0.00 USD | 72,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 84,130.00 USD | 84,130.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.28` | 278,160.00 USD | 278,160.00 USD | 4,310.00 USD | 54,390.00 USD | 316.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 59,310.00 USD | 59,310.00 USD | 5,380.00 USD | 41,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.29` | 219,140.00 USD | 219,140.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 12,490.00 USD | 12,490.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 25,770.00 USD | 25,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.33` | 1,170.00 USD | 1,170.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 7,340.00 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.36` | 380,150.00 USD | 380,150.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.36` | 760,300.00 USD | 760,300.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 1,440,000.00 USD | 1,440,000.00 USD | 280,420.00 USD | 0.00 USD | 400,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 393,520.00 USD | 393,520.00 USD | 0.00 USD | 0.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.38` | 2,080,000.00 USD | 2,080,000.00 USD | 3,030.00 USD | 0.00 USD | 638,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 883,630.00 USD | 883,630.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 2,990,000.00 USD | 2,990,000.00 USD | 356,920.00 USD | 41,380.00 USD | 508,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 1,960,000.00 USD | 1,960,000.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 180,760.00 USD | 185,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 4,060,000.00 USD | 4,060,000.00 USD | 541,780.00 USD | 118,310.00 USD | 409,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 3,130,000.00 USD | 3,130,000.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 5,530,000.00 USD | 5,530,000.00 USD | 450,080.00 USD | 331,840.00 USD | 687,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 3,650,000.00 USD | 3,650,000.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 6,150,000.00 USD | 6,150,000.00 USD | 128,340.00 USD | 240,270.00 USD | 256,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 4,350,000.00 USD | 4,350,000.00 USD | 404,280.00 USD | 117,350.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 1,930.00 USD | 186,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 7,090,000.00 USD | 7,090,000.00 USD | 335,950.00 USD | 146,900.00 USD | 449,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 4,960,000.00 USD | 4,960,000.00 USD | 293,250.00 USD | 88,400.00 USD | 228,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 8,210,000.00 USD | 8,210,000.00 USD | 276,510.00 USD | 396,660.00 USD | 452,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 5,810,000.00 USD | 5,810,000.00 USD | 455,890.00 USD | 143,990.00 USD | 246,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 3,750.00 USD | 190,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 8,590,000.00 USD | 8,590,000.00 USD | 76,860.00 USD | 181,120.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 26,330.00 USD | 217,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 8,720,000.00 USD | 8,720,000.00 USD | 4,580.00 USD | 91,550.00 USD | 31,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 6,180,000.00 USD | 6,180,000.00 USD | 3,070.00 USD | 146,940.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 1,370.00 USD | 218,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 9,090,000.00 USD | 9,090,000.00 USD | 222,670.00 USD | 25,190.00 USD | 120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 6,750,000.00 USD | 6,750,000.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 104.27 USD | 218,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 9,600,000.00 USD | 9,600,000.00 USD | 246,890.00 USD | 116,490.00 USD | 149,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 7,040,000.00 USD | 7,040,000.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 17,480.00 USD | 236,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 10,560,000.00 USD | 10,560,000.00 USD | 310,660.00 USD | 242,590.00 USD | 405,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 7,470,000.00 USD | 7,470,000.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 22,680.00 USD | 258,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 11,350,000.00 USD | 11,350,000.00 USD | 427,290.00 USD | 118,600.00 USD | 241,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 8,070,000.00 USD | 8,070,000.00 USD | 376,770.00 USD | 223,580.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 3,460.00 USD | 262,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 12,320,000.00 USD | 12,320,000.00 USD | 314,310.00 USD | 168,440.00 USD | 487,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 8,230,000.00 USD | 8,230,000.00 USD | 77,780.00 USD | 0.00 USD | 80,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 9,590.00 USD | 271,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 13,060,000.00 USD | 13,060,000.00 USD | 351,620.00 USD | 105,450.00 USD | 286,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 8,680,000.00 USD | 8,680,000.00 USD | 230,020.00 USD | 0.00 USD | 225,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 7,710.00 USD | 279,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 13,880,000.00 USD | 13,880,000.00 USD | 505,320.00 USD | 36,240.00 USD | 278,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 9,660,000.00 USD | 9,660,000.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 31,290.00 USD | 310,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 14,240,000.00 USD | 14,240,000.00 USD | 17,740.00 USD | 177,790.00 USD | 168,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 10,920,000.00 USD | 10,920,000.00 USD | 2,730.00 USD | 20,720.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 22,920.00 USD | 333,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 14,390,000.00 USD | 14,390,000.00 USD | 3,110.00 USD | 34,450.00 USD | 108,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 558.34 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.55` | 925.58 USD | 334,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.56` | 14,820,000.00 USD | 14,820,000.00 USD | 112,410.00 USD | 32,800.00 USD | 288,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 11,410,000.00 USD | 11,410,000.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 56,500.00 USD | 391,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 15,170,000.00 USD | 15,170,000.00 USD | 176,590.00 USD | 70,180.00 USD | 98,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 11,960,000.00 USD | 11,960,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 4,720.00 USD | 395,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.58` | 16,200,000.00 USD | 16,200,000.00 USD | 378,810.00 USD | 99,430.00 USD | 554,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 12,090,000.00 USD | 12,090,000.00 USD | 47,670.00 USD | 0.00 USD | 86,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 16,750,000.00 USD | 16,750,000.00 USD | 360,700.00 USD | 75,460.00 USD | 109,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 13,800,000.00 USD | 13,800,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 919.00 USD | 396,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 16,910,000.00 USD | 16,910,000.00 USD | 48,970.00 USD | 50,860.00 USD | 67,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 13,920,000.00 USD | 13,920,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 16,560.00 USD | 413,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 17,060,000.00 USD | 17,060,000.00 USD | 64,820.00 USD | 7,560.00 USD | 76,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 13,930,000.00 USD | 13,930,000.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 17,210,000.00 USD | 17,210,000.00 USD | 95,000.00 USD | 31,380.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 14,060,000.00 USD | 14,060,000.00 USD | 134,680.00 USD | 0.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 52,360.00 USD | 465,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 17,210,000.00 USD | 17,210,000.00 USD | 2,310.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 14,280,000.00 USD | 14,280,000.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 14,110.00 USD | 479,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 17,370,000.00 USD | 17,370,000.00 USD | 107,080.00 USD | 11,270.00 USD | 43,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 14,820,000.00 USD | 14,820,000.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 852.82 USD | 480,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 18,120,000.00 USD | 18,120,000.00 USD | 204,970.00 USD | 52,020.00 USD | 485,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 15,250,000.00 USD | 15,250,000.00 USD | 423,410.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 756.44 USD | 481,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 18,910,000.00 USD | 18,910,000.00 USD | 202,480.00 USD | 309,340.00 USD | 276,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 15,560,000.00 USD | 15,560,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 5,560.00 USD | 486,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 19,250,000.00 USD | 19,250,000.00 USD | 88,400.00 USD | 0.00 USD | 259,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 54,290.00 USD | 541,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 19,450,000.00 USD | 19,450,000.00 USD | 59,560.00 USD | 106,120.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 16,520,000.00 USD | 16,520,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 3,220.00 USD | 544,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 19,840,000.00 USD | 19,840,000.00 USD | 168,270.00 USD | 49,160.00 USD | 168,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 16,680,000.00 USD | 16,680,000.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 544,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 20,180,000.00 USD | 20,180,000.00 USD | 69,690.00 USD | 97,490.00 USD | 175,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 16,990,000.00 USD | 16,990,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 158,500.00 USD | 703,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 21,230,000.00 USD | 21,230,000.00 USD | 390,710.00 USD | 298,900.00 USD | 353,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 17,480,000.00 USD | 17,480,000.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 2,360.00 USD | 705,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 21,460,000.00 USD | 21,460,000.00 USD | 2,370.00 USD | 181,280.00 USD | 49,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 17,690,000.00 USD | 17,690,000.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 12,800.00 USD | 718,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 21,630,000.00 USD | 21,630,000.00 USD | 110,530.00 USD | 25,210.00 USD | 35,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 17,760,000.00 USD | 17,760,000.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 9,530.00 USD | 727,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 22,020,000.00 USD | 22,020,000.00 USD | 68,200.00 USD | 141,320.00 USD | 176,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 18,150,000.00 USD | 18,150,000.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.75` | 22,430,000.00 USD | 22,430,000.00 USD | 100,320.00 USD | 141,340.00 USD | 171,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 18,700,000.00 USD | 18,700,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 142,760.00 USD | 870,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 22,580,000.00 USD | 22,580,000.00 USD | 32,610.00 USD | 56,290.00 USD | 56,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 20,050,000.00 USD | 20,050,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 610.40 USD | 871,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 22,780,000.00 USD | 22,780,000.00 USD | 46,010.00 USD | 85,030.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 20,950,000.00 USD | 20,950,000.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 1,730.00 USD | 872,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 22,930,000.00 USD | 22,930,000.00 USD | 37,290.00 USD | 20,000.00 USD | 86,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 22,080,000.00 USD | 22,080,000.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 95,840.00 USD | 968,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 23,120,000.00 USD | 23,120,000.00 USD | 98,120.00 USD | 39,920.00 USD | 59,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 23,210,000.00 USD | 23,210,000.00 USD | 804,240.00 USD | 249,310.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 970,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 23,580,000.00 USD | 23,580,000.00 USD | 187,680.00 USD | 133,800.00 USD | 138,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 24,800,000.00 USD | 24,800,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 14,070.00 USD | 457.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 25,430,000.00 USD | 25,430,000.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.82` | 23,730,000.00 USD | 23,730,000.00 USD | 20,630.00 USD | 78,640.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 28,200,000.00 USD | 28,200,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 971,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 23,740,000.00 USD | 23,740,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 29,850,000.00 USD | 29,850,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 973,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 30,340,000.00 USD | 30,340,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 984,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 32,370,000.00 USD | 32,370,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 33,780,000.00 USD | 33,780,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 259.79 USD | 984,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 34,810,000.00 USD | 34,810,000.00 USD | 234,740.00 USD | 136,820.00 USD | 660,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 67,280.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.88` | 36,030,000.00 USD | 36,030,000.00 USD | 428,040.00 USD | 0.00 USD | 789,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.91` | 674.44 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,590.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.93` | 12,300.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.95` | 5,310.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 488.56 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 123.13 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,370.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.99` | 571.28 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.00` | 42,870.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 51,250.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.16` | 2,580.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.20` | 142.34 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.21` | 600.14 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 17,380.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 308,480.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 1,070,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 301,100.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 443,770.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 38,710.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 1,030.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 914.65 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 419.04 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 7,840.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 86,640.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 3,980.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.53` | 1,270.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 1,590,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 64,880.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 532.69 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 7,320.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 16,050.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 198.63 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 310.95 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 112,650.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 162.98 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 130.35 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.93` | 1,810.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,650.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.96` | 29,860.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 101.92 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 31,130.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 30,720.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.14` | 12,740.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 35,350.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.20` | 1,770.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 253,590.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 528,250.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 1,180,000.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 28,890,000.00 USD | 36,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 36,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.36` | 30,100.00 USD | 36,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 2,900,000.00 USD | 39,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 39,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 75,610.00 USD | 39,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 2,000.00 USD | 39,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 39,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 39,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 372,430.00 USD | 40,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 40,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 40,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 40,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.49` | 23,550.00 USD | 40,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 40,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 40,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 3,980.00 USD | 40,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 19,670.00 USD | 40,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 37,550.00 USD | 40,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.64` | 41,130.00 USD | 40,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 40,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 40,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 40,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 709.28 USD | 40,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 41,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 90,830.00 USD | 41,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.83` | 187.69 USD | 41,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 41,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.86` | 623.81 USD | 41,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 41,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.89` | 15,430.00 USD | 41,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 41,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 1,220.00 USD | 41,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.05` | 3,750,000.00 USD | 45,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 35,380.00 USD | 45,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 45,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.18` | 1,010.00 USD | 45,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 45,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 1,150.00 USD | 45,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 3,770.00 USD | 45,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.26` | 8,530.00 USD | 45,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.28` | 111.31 USD | 45,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.29` | 4,230.00 USD | 45,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 45,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 12,920.00 USD | 45,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.39` | 9,880,000.00 USD | 55,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 106,620.00 USD | 55,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 55,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.49` | 7,790,000.00 USD | 63,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 49,760.00 USD | 63,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,570.00 USD | 63,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 56,890.00 USD | 63,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.59` | 2,640.00 USD | 63,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 1,650.00 USD | 63,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 63,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 26,080.00 USD | 63,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 63,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 1,200,000.00 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.83` | 27,360.00 USD | 64,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 64,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 253.58 USD | 64,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.97` | 25,520.00 USD | 64,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 6,790.00 USD | 64,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.00` | 96,110.00 USD | 64,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 65,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 4,660.00 USD | 65,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.10` | 12,260.00 USD | 65,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.20` | 951.44 USD | 65,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.23` | 51,880.00 USD | 65,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.28` | 103,990.00 USD | 65,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.29` | 165.07 USD | 65,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.32` | 3,600.00 USD | 65,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.35` | 25,310.00 USD | 65,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 191.79 USD | 65,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.47` | 816.99 USD | 65,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 6,640.00 USD | 65,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 453,180.00 USD | 65,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.52` | 1,230.00 USD | 65,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 34,680.00 USD | 65,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 127.17 USD | 65,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 124.76 USD | 65,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 1,380,000.00 USD | 67,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.60` | 240.66 USD | 67,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.63` | 63,320.00 USD | 67,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 2,320.00 USD | 67,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8950` | 21,810,000.00 USD | 0.00 USD | 38,570.00 USD | `-79.54%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 21,770,000.00 USD | 0.00 USD | 1,650.00 USD | `-79.31%` | `1,822.90` |
| `Live` | `Long` | `0.9150` | 21,770,000.00 USD | 0.00 USD | 11,370.00 USD | `-79.08%` | `12,425.00` |
| `Live` | `Long` | `0.9450` | 21,760,000.00 USD | 0.00 USD | 914.48 USD | `-78.39%` | `967.70` |
| `Live` | `Long` | `0.9550` | 21,760,000.00 USD | 0.00 USD | 7,970.00 USD | `-78.16%` | `8,350.00` |
| `Live` | `Long` | `0.9650` | 21,750,000.00 USD | 0.00 USD | 965.00 USD | `-77.94%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 21,750,000.00 USD | 0.00 USD | 1,250.00 USD | `-77.48%` | `1,272.10` |
| `Live` | `Long` | `0.9950` | 21,750,000.00 USD | 0.00 USD | 184,880.00 USD | `-77.25%` | `185,806.70` |
| `Live` | `Long` | `1.00` | 21,560,000.00 USD | 0.00 USD | 8,590.00 USD | `-77.02%` | `8,543.70` |
| `Live` | `Long` | `1.01` | 21,560,000.00 USD | 0.00 USD | 112.77 USD | `-76.79%` | `111.10` |
| `Live` | `Long` | `1.02` | 21,550,000.00 USD | 0.00 USD | 10,250.00 USD | `-76.56%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 21,540,000.00 USD | 0.00 USD | 21,250.00 USD | `-76.34%` | `20,528.30` |
| `Live` | `Long` | `1.04` | 21,520,000.00 USD | 0.00 USD | 2,940.00 USD | `-76.11%` | `2,816.90` |
| `Live` | `Long` | `1.05` | 21,520,000.00 USD | 0.00 USD | 4,330.00 USD | `-75.88%` | `4,108.90` |
| `Live` | `Long` | `1.06` | 21,520,000.00 USD | 0.00 USD | 19,530.00 USD | `-75.65%` | `18,334.00` |
| `Live` | `Long` | `1.07` | 21,500,000.00 USD | 0.00 USD | 13,410.00 USD | `-75.42%` | `12,477.50` |
| `Live` | `Long` | `1.08` | 21,480,000.00 USD | 0.00 USD | 216.89 USD | `-75.19%` | `199.90` |
| `Live` | `Long` | `1.11` | 21,480,000.00 USD | 0.00 USD | 1,570.00 USD | `-74.51%` | `1,412.40` |
| `Live` | `Long` | `1.12` | 21,480,000.00 USD | 0.00 USD | 178.20 USD | `-74.28%` | `158.40` |
| `Live` | `Long` | `1.14` | 21,480,000.00 USD | 0.00 USD | 4,960.00 USD | `-74.05%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 21,480,000.00 USD | 0.00 USD | 27,080.00 USD | `-73.82%` | `23,652.70` |
| `Live` | `Long` | `1.17` | 21,450,000.00 USD | 0.00 USD | 54,270.00 USD | `-73.36%` | `46,584.90` |
| `Live` | `Long` | `1.18` | 21,390,000.00 USD | 0.00 USD | 2,470.00 USD | `-73.13%` | `2,102.60` |
| `Live` | `Long` | `1.19` | 21,390,000.00 USD | 0.00 USD | 147.18 USD | `-72.91%` | `124.20` |
| `Live` | `Long` | `1.20` | 21,390,000.00 USD | 0.00 USD | 23,010.00 USD | `-72.68%` | `19,256.90` |
| `Live` | `Long` | `1.21` | 21,370,000.00 USD | 0.00 USD | 7,200.00 USD | `-72.45%` | `5,978.00` |
| `Live` | `Long` | `1.22` | 21,360,000.00 USD | 0.00 USD | 3,150.00 USD | `-72.22%` | `2,589.40` |
| `Live` | `Long` | `1.24` | 21,360,000.00 USD | 0.00 USD | 1,610.00 USD | `-71.76%` | `1,301.70` |
| `Live` | `Long` | `1.25` | 21,360,000.00 USD | 0.00 USD | 14,030.00 USD | `-71.53%` | `11,271.90` |
| `Live` | `Long` | `1.25` | 21,340,000.00 USD | 0.00 USD | 7,490.00 USD | `-71.31%` | `5,967.90` |
| `Live` | `Long` | `1.26` | 21,340,000.00 USD | 0.00 USD | 2,060.00 USD | `-71.08%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 21,330,000.00 USD | 0.00 USD | 2,580.00 USD | `-70.85%` | `2,026.80` |
| `Live` | `Long` | `1.28` | 21,330,000.00 USD | 0.00 USD | 169.23 USD | `-70.62%` | `131.70` |
| `Live` | `Long` | `1.29` | 21,330,000.00 USD | 0.00 USD | 165.11 USD | `-70.39%` | `127.50` |
| `Live` | `Long` | `1.30` | 21,330,000.00 USD | 0.00 USD | 116.80 USD | `-70.16%` | `89.50` |
| `Live` | `Long` | `1.31` | 21,330,000.00 USD | 0.00 USD | 2,040.00 USD | `-69.93%` | `1,553.20` |
| `Live` | `Long` | `1.32` | 21,330,000.00 USD | 0.00 USD | 4,060.00 USD | `-69.70%` | `3,064.40` |
| `Live` | `Long` | `1.33` | 21,320,000.00 USD | 0.00 USD | 4,660.00 USD | `-69.48%` | `3,487.70` |
| `Live` | `Long` | `1.34` | 21,320,000.00 USD | 0.00 USD | 603.91 USD | `-69.25%` | `449.00` |
| `Live` | `Long` | `1.35` | 21,320,000.00 USD | 0.00 USD | 2,000.00 USD | `-69.02%` | `1,474.80` |
| `Live` | `Long` | `1.39` | 21,320,000.00 USD | 0.00 USD | 12,760.00 USD | `-68.33%` | `9,213.40` |
| `Live` | `Long` | `1.40` | 21,300,000.00 USD | 0.00 USD | 4,410.00 USD | `-68.10%` | `3,164.20` |
| `Live` | `Long` | `1.41` | 21,300,000.00 USD | 0.00 USD | 1,080.00 USD | `-67.88%` | `766.80` |
| `Live` | `Long` | `1.42` | 21,300,000.00 USD | 0.00 USD | 79,170.00 USD | `-67.65%` | `55,947.80` |
| `Live` | `Long` | `1.43` | 21,220,000.00 USD | 0.00 USD | 869.25 USD | `-67.42%` | `610.00` |
| `Live` | `Long` | `1.45` | 21,220,000.00 USD | 0.00 USD | 14,540.00 USD | `-66.96%` | `10,061.70` |
| `Live` | `Long` | `1.46` | 21,200,000.00 USD | 0.00 USD | 521,920.00 USD | `-66.73%` | `358,706.60` |
| `Live` | `Long` | `1.47` | 20,680,000.00 USD | 0.00 USD | 3,300.00 USD | `-66.50%` | `2,249.20` |
| `Live` | `Long` | `1.48` | 20,680,000.00 USD | 0.00 USD | 2,260.00 USD | `-66.27%` | `1,530.90` |
| `Live` | `Long` | `1.49` | 20,680,000.00 USD | 0.00 USD | 2,970.00 USD | `-66.05%` | `2,000.00` |
| `Live` | `Long` | `1.50` | 20,670,000.00 USD | 0.00 USD | 74,750.00 USD | `-65.82%` | `50,000.00` |
| `Live` | `Long` | `1.51` | 20,600,000.00 USD | 0.00 USD | 454.50 USD | `-65.36%` | `300.00` |
| `Live` | `Long` | `1.53` | 20,600,000.00 USD | 0.00 USD | 279.37 USD | `-64.90%` | `182.00` |
| `Live` | `Long` | `1.56` | 20,600,000.00 USD | 0.00 USD | 21,520.00 USD | `-64.22%` | `13,748.90` |
| `Live` | `Long` | `1.57` | 20,580,000.00 USD | 0.00 USD | 1,440.00 USD | `-63.99%` | `914.30` |
| `Live` | `Long` | `1.58` | 20,580,000.00 USD | 0.00 USD | 1,980.00 USD | `-63.76%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 20,570,000.00 USD | 0.00 USD | 8,620.00 USD | `-63.53%` | `5,402.90` |
| `Live` | `Long` | `1.60` | 20,570,000.00 USD | 0.00 USD | 191.64 USD | `-63.30%` | `119.40` |
| `Live` | `Long` | `1.61` | 20,560,000.00 USD | 0.00 USD | 1,230.00 USD | `-63.07%` | `758.60` |
| `Live` | `Long` | `1.62` | 20,560,000.00 USD | 0.00 USD | 2,600.00 USD | `-62.85%` | `1,600.00` |
| `Live` | `Long` | `1.64` | 20,560,000.00 USD | 0.00 USD | 2,190.00 USD | `-62.62%` | `1,340.10` |
| `Live` | `Long` | `1.65` | 20,560,000.00 USD | 0.00 USD | 981.08 USD | `-62.39%` | `596.40` |
| `Live` | `Long` | `1.66` | 20,560,000.00 USD | 0.00 USD | 1,430.00 USD | `-62.16%` | `862.50` |
| `Live` | `Long` | `1.67` | 20,560,000.00 USD | 0.00 USD | 12,900.00 USD | `-61.93%` | `7,750.30` |
| `Live` | `Long` | `1.68` | 20,540,000.00 USD | 0.00 USD | 12,900.00 USD | `-61.70%` | `7,702.10` |
| `Live` | `Long` | `1.69` | 20,530,000.00 USD | 0.00 USD | 12,850.00 USD | `-61.47%` | `7,624.50` |
| `Live` | `Long` | `1.70` | 20,520,000.00 USD | 0.00 USD | 593.25 USD | `-61.24%` | `350.00` |
| `Live` | `Long` | `1.71` | 20,520,000.00 USD | 0.00 USD | 1,820.00 USD | `-61.02%` | `1,068.30` |
| `Live` | `Long` | `1.72` | 20,520,000.00 USD | 0.00 USD | 6,990.00 USD | `-60.79%` | `4,075.50` |
| `Live` | `Long` | `1.73` | 20,510,000.00 USD | 0.00 USD | 6,430.00 USD | `-60.56%` | `3,729.10` |
| `Live` | `Long` | `1.75` | 20,500,000.00 USD | 0.00 USD | 892.74 USD | `-60.10%` | `511.60` |
| `Live` | `Long` | `1.75` | 20,500,000.00 USD | 0.00 USD | 10,250.00 USD | `-59.87%` | `5,841.90` |
| `Live` | `Long` | `1.77` | 20,490,000.00 USD | 0.00 USD | 3,470.00 USD | `-59.42%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 20,490,000.00 USD | 0.00 USD | 9,610.00 USD | `-59.19%` | `5,384.50` |
| `Live` | `Long` | `1.80` | 20,480,000.00 USD | 0.00 USD | 2,330.00 USD | `-58.73%` | `1,288.30` |
| `Live` | `Long` | `1.81` | 20,480,000.00 USD | 0.00 USD | 1,580.00 USD | `-58.50%` | `873.20` |
| `Live` | `Long` | `1.82` | 20,470,000.00 USD | 0.00 USD | 3,040.00 USD | `-58.27%` | `1,668.20` |
| `Live` | `Long` | `1.83` | 20,470,000.00 USD | 0.00 USD | 27,520.00 USD | `-58.04%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 20,440,000.00 USD | 0.00 USD | 921.21 USD | `-57.82%` | `499.30` |
| `Live` | `Long` | `1.85` | 20,440,000.00 USD | 0.00 USD | 984.26 USD | `-57.59%` | `530.60` |
| `Live` | `Long` | `1.88` | 20,440,000.00 USD | 0.00 USD | 34,600.00 USD | `-57.13%` | `18,455.90` |
| `Live` | `Long` | `1.89` | 20,410,000.00 USD | 0.00 USD | 10,530.00 USD | `-56.90%` | `5,583.80` |
| `Live` | `Long` | `1.90` | 20,400,000.00 USD | 0.00 USD | 2,080.00 USD | `-56.67%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 20,390,000.00 USD | 0.00 USD | 288.61 USD | `-56.44%` | `151.50` |
| `Live` | `Long` | `1.92` | 20,390,000.00 USD | 0.00 USD | 192.46 USD | `-56.21%` | `100.50` |
| `Live` | `Long` | `1.93` | 20,390,000.00 USD | 0.00 USD | 154.77 USD | `-55.99%` | `80.40` |
| `Live` | `Long` | `1.94` | 20,390,000.00 USD | 0.00 USD | 34,400.00 USD | `-55.76%` | `17,777.30` |
| `Live` | `Long` | `1.95` | 20,360,000.00 USD | 0.00 USD | 3,190.00 USD | `-55.53%` | `1,640.10` |
| `Live` | `Long` | `1.96` | 20,360,000.00 USD | 0.00 USD | 2,190.00 USD | `-55.30%` | `1,120.20` |
| `Live` | `Long` | `1.97` | 20,350,000.00 USD | 0.00 USD | 3,990.00 USD | `-55.07%` | `2,031.40` |
| `Live` | `Long` | `1.98` | 20,350,000.00 USD | 0.00 USD | 34,960.00 USD | `-54.84%` | `17,702.90` |
| `Live` | `Long` | `2.00` | 20,310,000.00 USD | 0.00 USD | 317.01 USD | `-54.39%` | `158.90` |
| `Live` | `Long` | `2.00` | 20,310,000.00 USD | 0.00 USD | 3,950.00 USD | `-54.16%` | `1,969.50` |
| `Live` | `Long` | `2.02` | 20,310,000.00 USD | 0.00 USD | 18,610.00 USD | `-53.93%` | `9,237.10` |
| `Live` | `Long` | `2.02` | 20,290,000.00 USD | 0.00 USD | 6,820.00 USD | `-53.70%` | `3,366.90` |
| `Live` | `Long` | `2.04` | 20,290,000.00 USD | 0.00 USD | 2,130.00 USD | `-53.47%` | `1,045.80` |
| `Live` | `Long` | `2.04` | 20,280,000.00 USD | 0.00 USD | 31,940.00 USD | `-53.24%` | `15,618.60` |
| `Live` | `Long` | `2.06` | 20,250,000.00 USD | 0.00 USD | 349.35 USD | `-53.01%` | `170.00` |
| `Live` | `Long` | `2.06` | 20,250,000.00 USD | 0.00 USD | 878,740.00 USD | `-52.78%` | `425,539.70` |
| `Live` | `Long` | `2.08` | 19,370,000.00 USD | 0.00 USD | 12,110.00 USD | `-52.56%` | `5,834.50` |
| `Live` | `Long` | `2.08` | 19,360,000.00 USD | 0.00 USD | 24,370.00 USD | `-52.33%` | `11,689.80` |
| `Live` | `Long` | `2.10` | 19,340,000.00 USD | 0.00 USD | 2,500.00 USD | `-52.10%` | `1,191.50` |
| `Live` | `Long` | `2.10` | 19,330,000.00 USD | 0.00 USD | 204,510.00 USD | `-51.87%` | `97,152.60` |
| `Live` | `Long` | `2.12` | 19,130,000.00 USD | 0.00 USD | 17,810.00 USD | `-51.64%` | `8,419.80` |
| `Live` | `Long` | `2.12` | 19,110,000.00 USD | 0.00 USD | 5,370.00 USD | `-51.41%` | `2,527.30` |
| `Live` | `Long` | `2.13` | 19,110,000.00 USD | 0.00 USD | 2,140.00 USD | `-51.18%` | `1,000.80` |
| `Live` | `Long` | `2.15` | 19,100,000.00 USD | 0.00 USD | 2,110.00 USD | `-50.96%` | `983.60` |
| `Live` | `Long` | `2.15` | 19,100,000.00 USD | 0.00 USD | 857.04 USD | `-50.73%` | `397.70` |
| `Live` | `Long` | `2.17` | 19,100,000.00 USD | 0.00 USD | 279,280.00 USD | `-50.50%` | `128,995.90` |
| `Live` | `Long` | `2.17` | 18,820,000.00 USD | 0.00 USD | 64,960.00 USD | `-50.27%` | `29,865.80` |
| `Live` | `Long` | `2.19` | 18,760,000.00 USD | 0.00 USD | 10,090.00 USD | `-49.81%` | `4,596.20` |
| `Live` | `Long` | `2.21` | 18,750,000.00 USD | 0.00 USD | 15,220.00 USD | `-49.58%` | `6,904.60` |
| `Live` | `Long` | `2.21` | 18,730,000.00 USD | 0.00 USD | 25,780.00 USD | `-49.36%` | `11,638.90` |
| `Live` | `Long` | `2.23` | 18,700,000.00 USD | 0.00 USD | 189,380.00 USD | `-49.13%` | `85,114.40` |
| `Live` | `Long` | `2.23` | 18,520,000.00 USD | 0.00 USD | 8,130.00 USD | `-48.90%` | `3,638.70` |
| `Live` | `Long` | `2.25` | 18,510,000.00 USD | 0.00 USD | 968.27 USD | `-48.67%` | `431.30` |
| `Live` | `Long` | `2.25` | 18,510,000.00 USD | 0.00 USD | 118,720.00 USD | `-48.44%` | `52,646.90` |
| `Live` | `Long` | `2.27` | 18,390,000.00 USD | 0.00 USD | 1,400.00 USD | `-48.21%` | `619.70` |
| `Live` | `Long` | `2.27` | 18,390,000.00 USD | 0.00 USD | 5,080.00 USD | `-47.98%` | `2,233.40` |
| `Live` | `Long` | `2.29` | 18,380,000.00 USD | 0.00 USD | 91,400.00 USD | `-47.75%` | `39,999.50` |
| `Live` | `Long` | `2.29` | 18,290,000.00 USD | 0.00 USD | 6,790.00 USD | `-47.53%` | `2,957.90` |
| `Live` | `Long` | `2.31` | 18,280,000.00 USD | 0.00 USD | 6,510.00 USD | `-47.30%` | `2,825.80` |
| `Live` | `Long` | `2.31` | 18,280,000.00 USD | 0.00 USD | 233,830.00 USD | `-47.07%` | `101,005.00` |
| `Live` | `Long` | `2.33` | 18,040,000.00 USD | 0.00 USD | 39,350.00 USD | `-46.84%` | `16,923.50` |
| `Live` | `Long` | `2.33` | 18,000,000.00 USD | 0.00 USD | 13,380.00 USD | `-46.61%` | `5,731.40` |
| `Live` | `Long` | `2.35` | 17,990,000.00 USD | 0.00 USD | 2,940.00 USD | `-46.38%` | `1,253.90` |
| `Live` | `Long` | `2.35` | 17,990,000.00 USD | 0.00 USD | 324.28 USD | `-46.15%` | `137.70` |
| `Live` | `Long` | `2.37` | 17,990,000.00 USD | 0.00 USD | 1,580.00 USD | `-45.93%` | `667.80` |
| `Live` | `Long` | `2.38` | 17,990,000.00 USD | 0.00 USD | 35,890.00 USD | `-45.70%` | `15,111.30` |
| `Live` | `Long` | `2.38` | 17,950,000.00 USD | 0.00 USD | 10,610.00 USD | `-45.47%` | `4,447.80` |
| `Live` | `Long` | `2.40` | 17,940,000.00 USD | 0.00 USD | 115.20 USD | `-45.24%` | `48.10` |
| `Live` | `Long` | `2.40` | 17,940,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-45.01%` | `652,414.60` |
| `Live` | `Long` | `2.42` | 16,370,000.00 USD | 0.00 USD | 185,540.00 USD | `-44.78%` | `76,828.90` |
| `Live` | `Long` | `2.42` | 16,180,000.00 USD | 0.00 USD | 279,590.00 USD | `-44.55%` | `115,292.80` |
| `Live` | `Long` | `2.44` | 15,900,000.00 USD | 0.00 USD | 3,840.00 USD | `-44.33%` | `1,576.60` |
| `Live` | `Long` | `2.44` | 15,900,000.00 USD | 0.00 USD | 9,320.00 USD | `-44.10%` | `3,811.60` |
| `Live` | `Long` | `2.46` | 15,890,000.00 USD | 0.00 USD | 1,240.00 USD | `-43.87%` | `504.90` |
| `Live` | `Long` | `2.46` | 15,890,000.00 USD | 0.00 USD | 2,240.00 USD | `-43.64%` | `907.20` |
| `Live` | `Long` | `2.48` | 15,890,000.00 USD | 0.00 USD | 3,980.00 USD | `-43.41%` | `1,607.30` |
| `Live` | `Long` | `2.48` | 15,880,000.00 USD | 0.00 USD | 2,760.00 USD | `-43.18%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 15,880,000.00 USD | 0.00 USD | 6,100.00 USD | `-42.95%` | `2,443.10` |
| `Live` | `Long` | `2.50` | 15,870,000.00 USD | 0.00 USD | 8,750.00 USD | `-42.72%` | `3,494.30` |
| `Live` | `Long` | `2.52` | 15,870,000.00 USD | 0.00 USD | 32,820.00 USD | `-42.27%` | `12,998.20` |
| `Live` | `Long` | `2.54` | 15,830,000.00 USD | 0.00 USD | 12,780.00 USD | `-42.04%` | `5,041.50` |
| `Live` | `Long` | `2.54` | 15,820,000.00 USD | 0.00 USD | 105.36 USD | `-41.81%` | `41.40` |
| `Live` | `Long` | `2.56` | 15,820,000.00 USD | 0.00 USD | 171,930.00 USD | `-41.58%` | `67,292.30` |
| `Live` | `Long` | `2.56` | 15,650,000.00 USD | 0.00 USD | 7,890.00 USD | `-41.35%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 15,640,000.00 USD | 0.00 USD | 1,260.00 USD | `-41.12%` | `490.00` |
| `Live` | `Long` | `2.58` | 15,640,000.00 USD | 0.00 USD | 905.27 USD | `-40.90%` | `350.20` |
| `Live` | `Long` | `2.60` | 15,640,000.00 USD | 0.00 USD | 80,550.00 USD | `-40.67%` | `31,041.30` |
| `Live` | `Long` | `2.60` | 15,560,000.00 USD | 0.00 USD | 2,450.00 USD | `-40.44%` | `940.80` |
| `Live` | `Long` | `2.62` | 15,560,000.00 USD | 0.00 USD | 1,190.00 USD | `-40.21%` | `454.70` |
| `Live` | `Long` | `2.62` | 15,550,000.00 USD | 0.00 USD | 3,970.00 USD | `-39.98%` | `1,513.80` |
| `Live` | `Long` | `2.63` | 15,550,000.00 USD | 0.00 USD | 24,310.00 USD | `-39.75%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 15,530,000.00 USD | 0.00 USD | 94,920.00 USD | `-39.52%` | `35,887.80` |
| `Live` | `Long` | `2.65` | 15,430,000.00 USD | 0.00 USD | 19,200.00 USD | `-39.29%` | `7,230.40` |
| `Live` | `Long` | `2.67` | 15,410,000.00 USD | 0.00 USD | 2,060.00 USD | `-39.07%` | `771.50` |
| `Live` | `Long` | `2.67` | 15,410,000.00 USD | 0.00 USD | 4,470.00 USD | `-38.84%` | `1,670.60` |
| `Live` | `Long` | `2.69` | 15,410,000.00 USD | 0.00 USD | 6,180.00 USD | `-38.61%` | `2,301.20` |
| `Live` | `Long` | `2.69` | 15,400,000.00 USD | 0.00 USD | 733.85 USD | `-38.38%` | `272.30` |
| `Live` | `Long` | `2.71` | 15,400,000.00 USD | 0.00 USD | 165,150.00 USD | `-38.15%` | `61,054.60` |
| `Live` | `Long` | `2.71` | 15,230,000.00 USD | 0.00 USD | 11,750.00 USD | `-37.92%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 15,220,000.00 USD | 0.00 USD | 33,230.00 USD | `-37.69%` | `12,194.90` |
| `Live` | `Long` | `2.73` | 15,190,000.00 USD | 0.00 USD | 6,780.00 USD | `-37.47%` | `2,478.80` |
| `Live` | `Long` | `2.75` | 15,180,000.00 USD | 0.00 USD | 458.96 USD | `-37.24%` | `167.20` |
| `Live` | `Long` | `2.75` | 15,180,000.00 USD | 0.00 USD | 65,100.00 USD | `-37.01%` | `23,628.20` |
| `Live` | `Long` | `2.77` | 15,120,000.00 USD | 0.00 USD | 351,110.00 USD | `-36.78%` | `126,983.70` |
| `Live` | `Long` | `2.77` | 14,760,000.00 USD | 0.00 USD | 398.77 USD | `-36.55%` | `143.70` |
| `Live` | `Long` | `2.79` | 14,760,000.00 USD | 0.00 USD | 165,340.00 USD | `-36.32%` | `59,369.00` |
| `Live` | `Long` | `2.79` | 14,600,000.00 USD | 0.00 USD | 37,500.00 USD | `-36.09%` | `13,416.00` |
| `Live` | `Long` | `2.81` | 14,560,000.00 USD | 0.00 USD | 14,750.00 USD | `-35.87%` | `5,259.70` |
| `Live` | `Long` | `2.81` | 14,550,000.00 USD | 0.00 USD | 4,900.00 USD | `-35.64%` | `1,739.40` |
| `Live` | `Long` | `2.83` | 14,540,000.00 USD | 0.00 USD | 12,400.00 USD | `-35.41%` | `4,389.80` |
| `Live` | `Long` | `2.83` | 14,530,000.00 USD | 0.00 USD | 2,400.00 USD | `-35.18%` | `847.80` |
| `Live` | `Long` | `2.85` | 14,530,000.00 USD | 0.00 USD | 180.94 USD | `-34.95%` | `63.60` |
| `Live` | `Long` | `2.85` | 14,530,000.00 USD | 0.00 USD | 6,560.00 USD | `-34.72%` | `2,299.40` |
| `Live` | `Long` | `2.87` | 14,520,000.00 USD | 0.00 USD | 204,500.00 USD | `-34.49%` | `71,380.40` |
| `Live` | `Long` | `2.88` | 14,320,000.00 USD | 0.00 USD | 955,250.00 USD | `-34.26%` | `332,261.60` |
| `Live` | `Long` | `2.88` | 13,360,000.00 USD | 0.00 USD | 6,140.00 USD | `-34.04%` | `2,127.40` |
| `Live` | `Long` | `2.90` | 13,350,000.00 USD | 0.00 USD | 15,720.00 USD | `-33.81%` | `5,430.80` |
| `Live` | `Long` | `2.90` | 13,340,000.00 USD | 0.00 USD | 972.88 USD | `-33.58%` | `334.90` |
| `Live` | `Long` | `2.92` | 13,340,000.00 USD | 0.00 USD | 5,330.00 USD | `-33.35%` | `1,830.00` |
| `Live` | `Long` | `2.92` | 13,330,000.00 USD | 0.00 USD | 56,870.00 USD | `-33.12%` | `19,444.40` |
| `Live` | `Long` | `2.94` | 13,280,000.00 USD | 0.00 USD | 58,110.00 USD | `-32.89%` | `19,799.50` |
| `Live` | `Long` | `2.94` | 13,220,000.00 USD | 0.00 USD | 16,860.00 USD | `-32.66%` | `5,725.40` |
| `Live` | `Long` | `2.96` | 13,200,000.00 USD | 0.00 USD | 15,120.00 USD | `-32.44%` | `5,116.70` |
| `Live` | `Long` | `2.96` | 13,190,000.00 USD | 0.00 USD | 3,600.00 USD | `-32.21%` | `1,215.60` |
| `Live` | `Long` | `2.98` | 13,180,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-31.98%` | `914,616.50` |
| `Live` | `Long` | `2.98` | 10,460,000.00 USD | 0.00 USD | 142,650.00 USD | `-31.75%` | `47,788.00` |
| `Live` | `Long` | `3.00` | 10,320,000.00 USD | 0.00 USD | 9,550.00 USD | `-31.52%` | `3,188.80` |
| `Live` | `Long` | `3.00` | 10,310,000.00 USD | 0.00 USD | 10,410.00 USD | `-31.29%` | `3,463.30` |
| `Live` | `Long` | `3.02` | 10,300,000.00 USD | 0.00 USD | 29,380.00 USD | `-31.06%` | `9,744.00` |
| `Live` | `Long` | `3.02` | 10,270,000.00 USD | 0.00 USD | 22,390.00 USD | `-30.84%` | `7,402.10` |
| `Live` | `Long` | `3.04` | 10,250,000.00 USD | 0.00 USD | 1,220.00 USD | `-30.61%` | `402.10` |
| `Live` | `Long` | `3.04` | 10,250,000.00 USD | 0.00 USD | 179,200.00 USD | `-30.38%` | `58,849.10` |
| `Live` | `Long` | `3.06` | 10,070,000.00 USD | 0.00 USD | 288,840.00 USD | `-30.15%` | `94,545.20` |
| `Live` | `Long` | `3.06` | 9,780,000.00 USD | 0.00 USD | 207,190.00 USD | `-29.92%` | `67,599.40` |
| `Live` | `Long` | `3.08` | 9,570,000.00 USD | 0.00 USD | 341.33 USD | `-29.69%` | `111.00` |
| `Live` | `Long` | `3.08` | 9,570,000.00 USD | 0.00 USD | 61,690.00 USD | `-29.46%` | `19,996.60` |
| `Live` | `Long` | `3.10` | 9,510,000.00 USD | 0.00 USD | 11,170.00 USD | `-29.23%` | `3,607.80` |
| `Live` | `Long` | `3.10` | 9,500,000.00 USD | 0.00 USD | 20,090.00 USD | `-29.01%` | `6,469.30` |
| `Live` | `Long` | `3.12` | 9,480,000.00 USD | 0.00 USD | 28,150.00 USD | `-28.78%` | `9,037.60` |
| `Live` | `Long` | `3.12` | 9,450,000.00 USD | 0.00 USD | 8,150.00 USD | `-28.55%` | `2,608.20` |
| `Live` | `Long` | `3.13` | 9,440,000.00 USD | 0.00 USD | 7,730.00 USD | `-28.32%` | `2,467.10` |
| `Live` | `Long` | `3.15` | 9,430,000.00 USD | 0.00 USD | 23,790.00 USD | `-28.09%` | `7,565.00` |
| `Live` | `Long` | `3.15` | 9,410,000.00 USD | 0.00 USD | 1,420.00 USD | `-27.86%` | `450.00` |
| `Live` | `Long` | `3.17` | 9,410,000.00 USD | 0.00 USD | 13,800.00 USD | `-27.63%` | `4,360.50` |
| `Live` | `Long` | `3.17` | 9,390,000.00 USD | 0.00 USD | 8,810.00 USD | `-27.41%` | `2,774.60` |
| `Live` | `Long` | `3.19` | 9,380,000.00 USD | 0.00 USD | 246,080.00 USD | `-27.18%` | `77,261.40` |
| `Live` | `Long` | `3.21` | 9,140,000.00 USD | 0.00 USD | 267.30 USD | `-26.72%` | `83.40` |
| `Live` | `Long` | `3.21` | 9,140,000.00 USD | 0.00 USD | 8,530.00 USD | `-26.49%` | `2,652.50` |
| `Live` | `Long` | `3.23` | 9,130,000.00 USD | 0.00 USD | 23,360.00 USD | `-26.26%` | `7,244.80` |
| `Live` | `Long` | `3.23` | 9,110,000.00 USD | 0.00 USD | 38,940.00 USD | `-26.03%` | `12,036.00` |
| `Live` | `Long` | `3.25` | 9,070,000.00 USD | 0.00 USD | 19,930.00 USD | `-25.80%` | `6,143.10` |
| `Live` | `Long` | `3.25` | 9,050,000.00 USD | 0.00 USD | 8,870.00 USD | `-25.58%` | `2,723.60` |
| `Live` | `Long` | `3.27` | 9,040,000.00 USD | 0.00 USD | 33,980.00 USD | `-25.35%` | `10,407.00` |
| `Live` | `Long` | `3.27` | 9,000,000.00 USD | 0.00 USD | 902,150.00 USD | `-25.12%` | `275,464.50` |
| `Live` | `Long` | `3.29` | 8,100,000.00 USD | 0.00 USD | 4,600.00 USD | `-24.89%` | `1,401.50` |
| `Live` | `Long` | `3.29` | 8,100,000.00 USD | 0.00 USD | 137,100.00 USD | `-24.66%` | `41,607.50` |
| `Live` | `Long` | `3.31` | 7,960,000.00 USD | 0.00 USD | 57,540.00 USD | `-24.43%` | `17,409.80` |
| `Live` | `Long` | `3.31` | 7,900,000.00 USD | 0.00 USD | 24,690.00 USD | `-24.20%` | `7,448.70` |
| `Live` | `Long` | `3.33` | 7,880,000.00 USD | 0.00 USD | 84,230.00 USD | `-23.98%` | `25,331.20` |
| `Live` | `Long` | `3.33` | 7,790,000.00 USD | 0.00 USD | 73,460.00 USD | `-23.75%` | `22,026.40` |
| `Live` | `Long` | `3.35` | 7,720,000.00 USD | 0.00 USD | 18,900.00 USD | `-23.52%` | `5,650.40` |
| `Live` | `Long` | `3.35` | 7,700,000.00 USD | 0.00 USD | 64,530.00 USD | `-23.29%` | `19,233.90` |
| `Live` | `Long` | `3.37` | 7,640,000.00 USD | 0.00 USD | 24,110.00 USD | `-23.06%` | `7,163.70` |
| `Live` | `Long` | `3.38` | 7,610,000.00 USD | 0.00 USD | 44,530.00 USD | `-22.83%` | `13,193.90` |
| `Live` | `Long` | `3.38` | 7,570,000.00 USD | 0.00 USD | 160,800.00 USD | `-22.60%` | `47,504.70` |
| `Live` | `Long` | `3.40` | 7,410,000.00 USD | 0.00 USD | 41,460.00 USD | `-22.38%` | `12,212.30` |
| `Live` | `Long` | `3.40` | 7,370,000.00 USD | 0.00 USD | 98,820.00 USD | `-22.15%` | `29,022.40` |
| `Live` | `Long` | `3.42` | 7,270,000.00 USD | 0.00 USD | 395,600.00 USD | `-21.92%` | `115,842.40` |
| `Live` | `Long` | `3.42` | 6,870,000.00 USD | 0.00 USD | 5,550.00 USD | `-21.69%` | `1,619.40` |
| `Live` | `Long` | `3.44` | 6,870,000.00 USD | 0.00 USD | 25,380.00 USD | `-21.46%` | `7,389.40` |
| `Live` | `Long` | `3.44` | 6,840,000.00 USD | 0.00 USD | 26,330.00 USD | `-21.23%` | `7,642.20` |
| `Live` | `Long` | `3.46` | 6,820,000.00 USD | 0.00 USD | 20,020.00 USD | `-21.00%` | `5,793.30` |
| `Live` | `Long` | `3.46` | 6,800,000.00 USD | 0.00 USD | 16,370.00 USD | `-20.77%` | `4,724.70` |
| `Live` | `Long` | `3.48` | 6,780,000.00 USD | 0.00 USD | 108,000.00 USD | `-20.55%` | `31,078.50` |
| `Live` | `Long` | `3.48` | 6,670,000.00 USD | 0.00 USD | 30,100.00 USD | `-20.32%` | `8,635.80` |
| `Live` | `Long` | `3.50` | 6,640,000.00 USD | 0.00 USD | 39,080.00 USD | `-20.09%` | `11,181.50` |
| `Live` | `Long` | `3.50` | 6,600,000.00 USD | 0.00 USD | 117,220.00 USD | `-19.86%` | `33,443.80` |
| `Live` | `Long` | `3.52` | 6,480,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-19.63%` | `374,044.90` |
| `Live` | `Long` | `3.52` | 5,170,000.00 USD | 0.00 USD | 24,880.00 USD | `-19.40%` | `7,058.60` |
| `Live` | `Long` | `3.54` | 5,140,000.00 USD | 0.00 USD | 84,800.00 USD | `-19.17%` | `23,988.20` |
| `Live` | `Long` | `3.54` | 5,060,000.00 USD | 0.00 USD | 152,640.00 USD | `-18.95%` | `43,058.60` |
| `Live` | `Long` | `3.56` | 4,910,000.00 USD | 0.00 USD | 765,400.00 USD | `-18.72%` | `215,303.50` |
| `Live` | `Long` | `3.56` | 4,140,000.00 USD | 0.00 USD | 6,720.00 USD | `-18.49%` | `1,883.60` |
| `Live` | `Long` | `3.58` | 4,140,000.00 USD | 0.00 USD | 61,730.00 USD | `-18.26%` | `17,268.50` |
| `Live` | `Long` | `3.58` | 4,070,000.00 USD | 0.00 USD | 257,540.00 USD | `-18.03%` | `71,837.70` |
| `Live` | `Long` | `3.60` | 3,820,000.00 USD | 0.00 USD | 111,370.00 USD | `-17.80%` | `30,978.70` |
| `Live` | `Long` | `3.60` | 3,700,000.00 USD | 0.00 USD | 63,970.00 USD | `-17.57%` | `17,746.00` |
| `Live` | `Long` | `3.62` | 3,640,000.00 USD | 0.00 USD | 31,540.00 USD | `-17.34%` | `8,723.60` |
| `Live` | `Long` | `3.62` | 3,610,000.00 USD | 0.00 USD | 116,150.00 USD | `-17.12%` | `32,042.70` |
| `Live` | `Long` | `3.63` | 3,490,000.00 USD | 0.00 USD | 13,010.00 USD | `-16.89%` | `3,579.30` |
| `Live` | `Long` | `3.65` | 3,480,000.00 USD | 0.00 USD | 110,940.00 USD | `-16.66%` | `30,436.80` |
| `Live` | `Long` | `3.65` | 3,370,000.00 USD | 0.00 USD | 21,970.00 USD | `-16.43%` | `6,010.50` |
| `Live` | `Long` | `3.67` | 3,350,000.00 USD | 0.00 USD | 39,480.00 USD | `-16.20%` | `10,773.40` |
| `Live` | `Long` | `3.67` | 3,310,000.00 USD | 0.00 USD | 92,300.00 USD | `-15.97%` | `25,115.80` |
| `Live` | `Long` | `3.69` | 3,220,000.00 USD | 0.00 USD | 231,620.00 USD | `-15.74%` | `62,854.20` |
| `Live` | `Long` | `3.69` | 2,980,000.00 USD | 0.00 USD | 93,020.00 USD | `-15.52%` | `25,173.30` |
| `Live` | `Long` | `3.71` | 2,890,000.00 USD | 0.00 USD | 90,900.00 USD | `-15.29%` | `24,535.10` |
| `Live` | `Long` | `3.71` | 2,800,000.00 USD | 0.00 USD | 68,070.00 USD | `-15.06%` | `18,322.60` |
| `Live` | `Long` | `3.73` | 2,730,000.00 USD | 0.00 USD | 165,540.00 USD | `-14.83%` | `44,440.00` |
| `Live` | `Long` | `3.73` | 2,570,000.00 USD | 0.00 USD | 116,730.00 USD | `-14.60%` | `31,252.00` |
| `Live` | `Long` | `3.75` | 2,450,000.00 USD | 0.00 USD | 24,270.00 USD | `-14.37%` | `6,480.90` |
| `Live` | `Long` | `3.75` | 2,420,000.00 USD | 0.00 USD | 151,930.00 USD | `-14.14%` | `40,460.00` |
| `Live` | `Long` | `3.77` | 2,270,000.00 USD | 0.00 USD | 80,140.00 USD | `-13.92%` | `21,286.40` |
| `Live` | `Long` | `3.77` | 2,190,000.00 USD | 0.00 USD | 27,310.00 USD | `-13.69%` | `7,234.60` |
| `Live` | `Long` | `3.79` | 2,170,000.00 USD | 0.00 USD | 172,570.00 USD | `-13.46%` | `45,593.80` |
| `Live` | `Long` | `3.79` | 1,990,000.00 USD | 0.00 USD | 37,390.00 USD | `-13.23%` | `9,851.80` |
| `Live` | `Long` | `3.81` | 1,960,000.00 USD | 0.00 USD | 570,030.00 USD | `-13.00%` | `149,810.30` |
| `Live` | `Long` | `3.81` | 1,390,000.00 USD | 0.00 USD | 13,490.00 USD | `-12.77%` | `3,536.80` |
| `Live` | `Long` | `3.83` | 1,370,000.00 USD | 0.00 USD | 132,570.00 USD | `-12.54%` | `34,658.90` |
| `Live` | `Long` | `3.83` | 1,240,000.00 USD | 0.00 USD | 171,380.00 USD | `-12.31%` | `44,688.70` |
| `Live` | `Long` | `3.85` | 1,070,000.00 USD | 0.00 USD | 116,830.00 USD | `-12.09%` | `30,385.30` |
| `Live` | `Long` | `3.85` | 951,290.00 USD | 0.00 USD | 23,650.00 USD | `-11.86%` | `6,135.10` |
| `Live` | `Long` | `3.87` | 927,640.00 USD | 0.00 USD | 57,420.00 USD | `-11.63%` | `14,855.20` |
| `Live` | `Long` | `3.88` | 870,220.00 USD | 0.00 USD | 4,540.00 USD | `-11.40%` | `1,171.80` |
| `Live` | `Long` | `3.88` | 865,680.00 USD | 0.00 USD | 196,390.00 USD | `-11.17%` | `50,551.20` |
| `Live` | `Long` | `3.90` | 669,290.00 USD | 0.00 USD | 96,480.00 USD | `-10.94%` | `24,770.90` |
| `Live` | `Long` | `3.90` | 572,810.00 USD | 0.00 USD | 8,860.00 USD | `-10.71%` | `2,268.20` |
| `Live` | `Long` | `3.92` | 563,950.00 USD | 0.00 USD | 34,840.00 USD | `-10.49%` | `8,899.30` |
| `Live` | `Long` | `3.92` | 529,110.00 USD | 0.00 USD | 2,050.00 USD | `-10.26%` | `522.20` |
| `Live` | `Long` | `3.94` | 527,060.00 USD | 0.00 USD | 2,940.00 USD | `-10.03%` | `748.00` |
| `Live` | `Long` | `3.94` | 524,120.00 USD | 0.00 USD | 8,820.00 USD | `-9.80%` | `2,235.10` |
| `Live` | `Long` | `3.96` | 515,300.00 USD | 0.00 USD | 34,360.00 USD | `-9.57%` | `8,688.00` |
| `Live` | `Long` | `3.96` | 480,940.00 USD | 0.00 USD | 2,570.00 USD | `-9.34%` | `647.80` |
| `Live` | `Long` | `3.98` | 478,370.00 USD | 0.00 USD | 39,920.00 USD | `-9.11%` | `10,043.20` |
| `Live` | `Long` | `3.98` | 438,450.00 USD | 0.00 USD | 1,070.00 USD | `-8.89%` | `268.00` |
| `Live` | `Long` | `4.00` | 437,380.00 USD | 0.00 USD | 160,280.00 USD | `-8.66%` | `40,119.00` |
| `Live` | `Long` | `4.00` | 277,100.00 USD | 0.00 USD | 16,820.00 USD | `-8.43%` | `4,198.60` |
| `Live` | `Long` | `4.01` | 260,290.00 USD | 0.00 USD | 1,520.00 USD | `-8.20%` | `379.40` |
| `Live` | `Long` | `4.03` | 258,760.00 USD | 0.00 USD | 852.50 USD | `-7.97%` | `211.80` |
| `Live` | `Long` | `4.04` | 257,910.00 USD | 0.00 USD | 26,000.00 USD | `-7.74%` | `6,444.70` |
| `Live` | `Long` | `4.04` | 231,910.00 USD | 0.00 USD | 21,310.00 USD | `-7.51%` | `5,268.70` |
| `Live` | `Long` | `4.05` | 210,600.00 USD | 0.00 USD | 4,190.00 USD | `-7.28%` | `1,032.70` |
| `Live` | `Long` | `4.07` | 206,410.00 USD | 0.00 USD | 249.18 USD | `-7.06%` | `61.30` |
| `Live` | `Long` | `4.08` | 206,160.00 USD | 0.00 USD | 2,640.00 USD | `-6.83%` | `647.70` |
| `Live` | `Long` | `4.08` | 203,520.00 USD | 0.00 USD | 60,100.00 USD | `-6.60%` | `14,712.80` |
| `Live` | `Long` | `4.09` | 143,420.00 USD | 0.00 USD | 20,870.00 USD | `-6.37%` | `5,095.30` |
| `Live` | `Long` | `4.11` | 122,550.00 USD | 0.00 USD | 27,440.00 USD | `-6.14%` | `6,685.20` |
| `Live` | `Long` | `4.12` | 95,110.00 USD | 0.00 USD | 44,440.00 USD | `-5.91%` | `10,799.80` |
| `Live` | `Short` | `4.12` | 4,290.00 USD | 4,290.00 USD | 0.00 USD | `-5.68%` | `1,039.10` |
| `Live` | `Long` | `4.13` | 50,670.00 USD | 0.00 USD | 15,520.00 USD | `-5.46%` | `3,752.40` |
| `Live` | `Long` | `4.14` | 35,150.00 USD | 0.00 USD | 9,380.00 USD | `-5.23%` | `2,263.60` |
| `Live` | `Long` | `4.29` | 25,770.00 USD | 0.00 USD | 25,770.00 USD | `-1.80%` | `6,000.00` |
| `Live` | `Short` | `4.39` | 185,050.00 USD | 180,760.00 USD | 0.00 USD | `+0.49%` | `41,128.80` |
| `Live` | `Short` | `4.42` | 186,980.00 USD | 1,930.00 USD | 0.00 USD | `+1.18%` | `436.00` |
| `Live` | `Short` | `4.45` | 190,730.00 USD | 3,750.00 USD | 0.00 USD | `+1.63%` | `844.70` |
| `Live` | `Short` | `4.46` | 217,060.00 USD | 26,330.00 USD | 0.00 USD | `+1.86%` | `5,909.90` |
| `Live` | `Short` | `4.46` | 218,430.00 USD | 1,370.00 USD | 0.00 USD | `+2.09%` | `306.90` |
| `Live` | `Short` | `4.47` | 218,530.00 USD | 104.27 USD | 0.00 USD | `+2.32%` | `23.30` |
| `Live` | `Short` | `4.49` | 236,010.00 USD | 17,480.00 USD | 0.00 USD | `+2.55%` | `3,897.50` |
| `Live` | `Short` | `4.50` | 258,690.00 USD | 22,680.00 USD | 0.00 USD | `+2.78%` | `5,044.50` |
| `Live` | `Short` | `4.50` | 262,150.00 USD | 3,460.00 USD | 0.00 USD | `+3.00%` | `767.70` |
| `Live` | `Short` | `4.51` | 271,740.00 USD | 9,590.00 USD | 0.00 USD | `+3.23%` | `2,123.40` |
| `Live` | `Short` | `4.53` | 279,450.00 USD | 7,710.00 USD | 0.00 USD | `+3.46%` | `1,704.10` |
| `Live` | `Short` | `4.54` | 310,740.00 USD | 31,290.00 USD | 0.00 USD | `+3.69%` | `6,900.10` |
| `Live` | `Short` | `4.54` | 333,650.00 USD | 22,920.00 USD | 0.00 USD | `+3.92%` | `5,041.90` |
| `Live` | `Short` | `4.55` | 334,580.00 USD | 925.58 USD | 0.00 USD | `+4.15%` | `203.20` |
| `Live` | `Short` | `4.57` | 391,080.00 USD | 56,500.00 USD | 0.00 USD | `+4.38%` | `12,377.00` |
| `Live` | `Short` | `4.58` | 395,800.00 USD | 4,720.00 USD | 0.00 USD | `+4.60%` | `1,030.90` |
| `Live` | `Short` | `4.59` | 396,720.00 USD | 919.00 USD | 0.00 USD | `+5.06%` | `200.00` |
| `Live` | `Short` | `4.61` | 413,270.00 USD | 16,560.00 USD | 0.00 USD | `+5.29%` | `3,595.20` |
| `Live` | `Short` | `4.62` | 465,640.00 USD | 52,360.00 USD | 0.00 USD | `+5.75%` | `11,321.90` |
| `Live` | `Short` | `4.63` | 479,740.00 USD | 14,110.00 USD | 0.00 USD | `+5.98%` | `3,043.20` |
| `Live` | `Short` | `4.64` | 480,590.00 USD | 852.82 USD | 0.00 USD | `+6.21%` | `183.60` |
| `Live` | `Short` | `4.66` | 481,350.00 USD | 756.44 USD | 0.00 USD | `+6.43%` | `162.50` |
| `Live` | `Short` | `4.67` | 486,910.00 USD | 5,560.00 USD | 0.00 USD | `+6.66%` | `1,190.90` |
| `Live` | `Short` | `4.67` | 541,190.00 USD | 54,290.00 USD | 0.00 USD | `+6.89%` | `11,612.70` |
| `Live` | `Short` | `4.68` | 544,420.00 USD | 3,220.00 USD | 0.00 USD | `+7.12%` | `687.70` |
| `Live` | `Short` | `4.70` | 544,650.00 USD | 230.06 USD | 0.00 USD | `+7.35%` | `49.00` |
| `Live` | `Short` | `4.71` | 703,140.00 USD | 158,500.00 USD | 0.00 USD | `+7.58%` | `33,686.60` |
| `Live` | `Short` | `4.71` | 705,500.00 USD | 2,360.00 USD | 0.00 USD | `+7.81%` | `500.00` |
| `Live` | `Short` | `4.72` | 718,300.00 USD | 12,800.00 USD | 0.00 USD | `+8.03%` | `2,709.30` |
| `Live` | `Short` | `4.74` | 727,830.00 USD | 9,530.00 USD | 0.00 USD | `+8.26%` | `2,012.50` |
| `Live` | `Short` | `4.75` | 870,590.00 USD | 142,760.00 USD | 0.00 USD | `+8.72%` | `30,022.80` |
| `Live` | `Short` | `4.76` | 871,200.00 USD | 610.40 USD | 0.00 USD | `+8.95%` | `128.10` |
| `Live` | `Short` | `4.78` | 872,930.00 USD | 1,730.00 USD | 0.00 USD | `+9.18%` | `362.40` |
| `Live` | `Short` | `4.79` | 968,770.00 USD | 95,840.00 USD | 0.00 USD | `+9.41%` | `20,030.00` |
| `Live` | `Short` | `4.79` | 970,100.00 USD | 1,330.00 USD | 0.00 USD | `+9.64%` | `277.70` |
| `Live` | `Short` | `4.83` | 971,850.00 USD | 1,740.00 USD | 0.00 USD | `+10.32%` | `360.90` |
| `Live` | `Short` | `4.83` | 973,380.00 USD | 1,540.00 USD | 0.00 USD | `+10.55%` | `317.90` |
| `Live` | `Short` | `4.84` | 984,610.00 USD | 11,220.00 USD | 0.00 USD | `+10.78%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 984,870.00 USD | 259.79 USD | 0.00 USD | `+11.24%` | `53.40` |
| `Live` | `Short` | `4.88` | 1,050,000.00 USD | 67,280.00 USD | 0.00 USD | `+11.46%` | `13,800.00` |
| `Live` | `Short` | `4.88` | 1,050,000.00 USD | 827.03 USD | 0.00 USD | `+11.69%` | `169.30` |
| `Live` | `Short` | `4.91` | 1,050,000.00 USD | 674.44 USD | 0.00 USD | `+12.15%` | `137.50` |
| `Live` | `Short` | `4.92` | 1,070,000.00 USD | 20,720.00 USD | 0.00 USD | `+12.38%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,080,000.00 USD | 2,590.00 USD | 0.00 USD | `+12.61%` | `526.30` |
| `Live` | `Short` | `4.93` | 1,090,000.00 USD | 12,300.00 USD | 0.00 USD | `+12.84%` | `2,493.30` |
| `Live` | `Short` | `4.95` | 1,090,000.00 USD | 5,310.00 USD | 0.00 USD | `+13.06%` | `1,074.00` |
| `Live` | `Short` | `4.96` | 1,100,000.00 USD | 488.56 USD | 0.00 USD | `+13.29%` | `98.60` |
| `Live` | `Short` | `4.96` | 1,100,000.00 USD | 123.13 USD | 0.00 USD | `+13.52%` | `24.80` |
| `Live` | `Short` | `4.97` | 1,190,000.00 USD | 99,370.00 USD | 0.00 USD | `+13.75%` | `19,974.00` |
| `Live` | `Short` | `4.99` | 1,200,000.00 USD | 571.28 USD | 0.00 USD | `+13.98%` | `114.60` |
| `Live` | `Short` | `5.00` | 1,240,000.00 USD | 42,870.00 USD | 0.00 USD | `+14.21%` | `8,583.40` |
| `Live` | `Short` | `5.05` | 1,270,000.00 USD | 35,380.00 USD | 0.00 USD | `+15.58%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,280,000.00 USD | 3,420.00 USD | 0.00 USD | `+15.81%` | `675.80` |
| `Live` | `Short` | `5.12` | 1,330,000.00 USD | 51,250.00 USD | 0.00 USD | `+17.18%` | `10,000.00` |
| `Live` | `Short` | `5.16` | 1,330,000.00 USD | 2,580.00 USD | 0.00 USD | `+17.87%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,330,000.00 USD | 751.51 USD | 0.00 USD | `+18.09%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,330,000.00 USD | 142.34 USD | 0.00 USD | `+18.78%` | `27.40` |
| `Live` | `Short` | `5.21` | 1,330,000.00 USD | 600.14 USD | 0.00 USD | `+19.01%` | `115.30` |
| `Live` | `Short` | `5.25` | 1,330,000.00 USD | 143.71 USD | 0.00 USD | `+19.92%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,350,000.00 USD | 17,380.00 USD | 0.00 USD | `+20.15%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,360,000.00 USD | 5,610.00 USD | 0.00 USD | `+20.38%` | `1,066.10` |
| `Live` | `Short` | `5.29` | 1,360,000.00 USD | 134.77 USD | 0.00 USD | `+20.84%` | `25.50` |
| `Live` | `Short` | `5.30` | 1,360,000.00 USD | 524.66 USD | 0.00 USD | `+21.30%` | `98.90` |
| `Live` | `Short` | `5.33` | 1,660,000.00 USD | 308,480.00 USD | 0.00 USD | `+21.98%` | `57,822.40` |
| `Live` | `Short` | `5.34` | 2,730,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+22.21%` | `200,000.00` |
| `Live` | `Short` | `5.36` | 3,030,000.00 USD | 301,100.00 USD | 0.00 USD | `+22.44%` | `56,227.00` |
| `Live` | `Short` | `5.37` | 3,480,000.00 USD | 443,770.00 USD | 0.00 USD | `+22.67%` | `82,715.70` |
| `Live` | `Short` | `5.38` | 3,520,000.00 USD | 38,710.00 USD | 0.00 USD | `+22.90%` | `7,202.20` |
| `Live` | `Short` | `5.42` | 3,520,000.00 USD | 1,030.00 USD | 0.00 USD | `+23.81%` | `189.60` |
| `Live` | `Short` | `5.42` | 3,520,000.00 USD | 914.65 USD | 0.00 USD | `+24.04%` | `168.60` |
| `Live` | `Short` | `5.43` | 3,520,000.00 USD | 419.04 USD | 0.00 USD | `+24.27%` | `77.10` |
| `Live` | `Short` | `5.47` | 3,530,000.00 USD | 7,840.00 USD | 0.00 USD | `+25.18%` | `1,432.70` |
| `Live` | `Short` | `5.50` | 3,610,000.00 USD | 86,640.00 USD | 0.00 USD | `+25.64%` | `15,766.90` |
| `Live` | `Short` | `5.50` | 3,620,000.00 USD | 3,980.00 USD | 0.00 USD | `+25.87%` | `722.70` |
| `Live` | `Short` | `5.53` | 3,620,000.00 USD | 1,270.00 USD | 0.00 USD | `+26.33%` | `229.80` |
| `Live` | `Short` | `5.54` | 5,210,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+26.55%` | `288,065.70` |
| `Live` | `Short` | `5.57` | 5,220,000.00 USD | 8,670.00 USD | 0.00 USD | `+27.24%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 5,280,000.00 USD | 62,420.00 USD | 0.00 USD | `+27.70%` | `11,175.80` |
| `Live` | `Short` | `5.61` | 5,350,000.00 USD | 64,880.00 USD | 0.00 USD | `+28.16%` | `11,574.70` |
| `Live` | `Short` | `5.62` | 5,350,000.00 USD | 532.69 USD | 0.00 USD | `+28.61%` | `94.70` |
| `Live` | `Short` | `5.67` | 5,350,000.00 USD | 211.30 USD | 0.00 USD | `+29.53%` | `37.30` |
| `Live` | `Short` | `5.67` | 5,350,000.00 USD | 228.70 USD | 0.00 USD | `+29.76%` | `40.30` |
| `Live` | `Short` | `5.68` | 5,380,000.00 USD | 26,090.00 USD | 0.00 USD | `+29.98%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 5,380,000.00 USD | 1,520.00 USD | 0.00 USD | `+30.21%` | `267.40` |
| `Live` | `Short` | `5.71` | 5,380,000.00 USD | 2,130.00 USD | 0.00 USD | `+30.67%` | `372.40` |
| `Live` | `Short` | `5.75` | 5,390,000.00 USD | 7,320.00 USD | 0.00 USD | `+31.36%` | `1,274.10` |
| `Live` | `Short` | `5.75` | 5,390,000.00 USD | 286.02 USD | 0.00 USD | `+31.58%` | `49.70` |
| `Live` | `Short` | `5.79` | 5,400,000.00 USD | 16,050.00 USD | 0.00 USD | `+32.50%` | `2,769.00` |
| `Live` | `Short` | `5.83` | 5,400,000.00 USD | 198.63 USD | 0.00 USD | `+33.19%` | `34.10` |
| `Live` | `Short` | `5.84` | 5,400,000.00 USD | 310.95 USD | 0.00 USD | `+33.64%` | `53.20` |
| `Live` | `Short` | `5.86` | 5,410,000.00 USD | 848.39 USD | 0.00 USD | `+33.87%` | `144.90` |
| `Live` | `Short` | `5.88` | 5,410,000.00 USD | 190.67 USD | 0.00 USD | `+34.56%` | `32.40` |
| `Live` | `Short` | `5.89` | 5,520,000.00 USD | 112,650.00 USD | 0.00 USD | `+34.79%` | `19,109.80` |
| `Live` | `Short` | `5.91` | 5,520,000.00 USD | 162.98 USD | 0.00 USD | `+35.01%` | `27.60` |
| `Live` | `Short` | `5.92` | 5,520,000.00 USD | 189.28 USD | 0.00 USD | `+35.24%` | `32.00` |
| `Live` | `Short` | `5.92` | 5,520,000.00 USD | 130.35 USD | 0.00 USD | `+35.47%` | `22.00` |
| `Live` | `Short` | `5.93` | 5,520,000.00 USD | 1,810.00 USD | 0.00 USD | `+35.70%` | `305.00` |
| `Live` | `Short` | `5.95` | 5,620,000.00 USD | 103,650.00 USD | 0.00 USD | `+35.93%` | `17,434.80` |
| `Live` | `Short` | `5.96` | 5,650,000.00 USD | 29,860.00 USD | 0.00 USD | `+36.16%` | `5,014.50` |
| `Live` | `Short` | `6.00` | 5,650,000.00 USD | 101.92 USD | 0.00 USD | `+37.07%` | `17.00` |
| `Live` | `Short` | `6.00` | 5,690,000.00 USD | 31,130.00 USD | 0.00 USD | `+37.30%` | `5,183.90` |
| `Live` | `Short` | `6.07` | 5,690,000.00 USD | 740.54 USD | 0.00 USD | `+38.67%` | `122.10` |
| `Live` | `Short` | `6.08` | 5,690,000.00 USD | 5,920.00 USD | 0.00 USD | `+39.13%` | `973.10` |
| `Live` | `Short` | `6.09` | 5,730,000.00 USD | 37,510.00 USD | 0.00 USD | `+39.36%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 5,760,000.00 USD | 30,720.00 USD | 0.00 USD | `+40.27%` | `5,007.70` |
| `Live` | `Short` | `6.14` | 5,770,000.00 USD | 12,740.00 USD | 0.00 USD | `+40.50%` | `2,073.30` |
| `Live` | `Short` | `6.18` | 5,810,000.00 USD | 35,350.00 USD | 0.00 USD | `+41.42%` | `5,715.90` |
| `Live` | `Short` | `6.20` | 5,810,000.00 USD | 1,770.00 USD | 0.00 USD | `+41.65%` | `285.90` |
| `Live` | `Short` | `6.21` | 6,060,000.00 USD | 253,590.00 USD | 0.00 USD | `+41.87%` | `40,869.30` |
| `Live` | `Short` | `6.24` | 6,590,000.00 USD | 528,250.00 USD | 0.00 USD | `+42.56%` | `84,723.00` |
| `Live` | `Short` | `6.25` | 6,600,000.00 USD | 7,300.00 USD | 0.00 USD | `+42.79%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 7,780,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+43.02%` | `188,070.20` |
| `Live` | `Short` | `6.32` | 7,780,000.00 USD | 310.70 USD | 0.00 USD | `+44.39%` | `49.20` |
| `Live` | `Short` | `6.33` | 36,670,000.00 USD | 28,890,000.00 USD | 0.00 USD | `+44.85%` | `4,560,826.20` |
| `Live` | `Short` | `6.34` | 36,670,000.00 USD | 214.46 USD | 0.00 USD | `+45.07%` | `33.80` |
| `Live` | `Short` | `6.36` | 36,700,000.00 USD | 30,100.00 USD | 0.00 USD | `+45.30%` | `4,736.60` |
| `Live` | `Short` | `6.37` | 39,590,000.00 USD | 2,900,000.00 USD | 0.00 USD | `+45.53%` | `454,966.70` |
| `Live` | `Short` | `6.38` | 39,590,000.00 USD | 288.15 USD | 0.00 USD | `+45.76%` | `45.20` |
| `Live` | `Short` | `6.38` | 39,670,000.00 USD | 75,610.00 USD | 0.00 USD | `+45.99%` | `11,841.80` |
| `Live` | `Short` | `6.39` | 39,670,000.00 USD | 2,000.00 USD | 0.00 USD | `+46.22%` | `312.80` |
| `Live` | `Short` | `6.41` | 39,680,000.00 USD | 3,780.00 USD | 0.00 USD | `+46.45%` | `590.10` |
| `Live` | `Short` | `6.42` | 39,680,000.00 USD | 943.65 USD | 0.00 USD | `+46.68%` | `147.10` |
| `Live` | `Short` | `6.42` | 40,050,000.00 USD | 372,430.00 USD | 0.00 USD | `+46.90%` | `57,965.40` |
| `Live` | `Short` | `6.45` | 40,050,000.00 USD | 5,270.00 USD | 0.00 USD | `+47.36%` | `818.40` |
| `Live` | `Short` | `6.46` | 40,060,000.00 USD | 7,150.00 USD | 0.00 USD | `+47.59%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 40,060,000.00 USD | 1,940.00 USD | 0.00 USD | `+47.82%` | `300.00` |
| `Live` | `Short` | `6.49` | 40,090,000.00 USD | 23,550.00 USD | 0.00 USD | `+48.28%` | `3,631.30` |
| `Live` | `Short` | `6.51` | 40,090,000.00 USD | 380.48 USD | 0.00 USD | `+48.96%` | `58.40` |
| `Live` | `Short` | `6.54` | 40,090,000.00 USD | 265.07 USD | 0.00 USD | `+49.65%` | `40.50` |
| `Live` | `Short` | `6.58` | 40,090,000.00 USD | 3,980.00 USD | 0.00 USD | `+50.56%` | `604.30` |
| `Live` | `Short` | `6.59` | 40,110,000.00 USD | 19,670.00 USD | 0.00 USD | `+50.79%` | `2,982.20` |
| `Live` | `Short` | `6.62` | 40,150,000.00 USD | 37,550.00 USD | 0.00 USD | `+51.48%` | `5,668.40` |
| `Live` | `Short` | `6.64` | 40,190,000.00 USD | 41,130.00 USD | 0.00 USD | `+51.93%` | `6,190.00` |
| `Live` | `Short` | `6.66` | 40,200,000.00 USD | 7,230.00 USD | 0.00 USD | `+52.16%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 40,200,000.00 USD | 233.94 USD | 0.00 USD | `+52.39%` | `35.10` |
| `Live` | `Short` | `6.67` | 40,200,000.00 USD | 200.25 USD | 0.00 USD | `+52.62%` | `30.00` |
| `Live` | `Short` | `6.68` | 40,200,000.00 USD | 709.28 USD | 0.00 USD | `+52.85%` | `106.10` |
| `Live` | `Short` | `6.75` | 41,450,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+54.45%` | `184,501.00` |
| `Live` | `Short` | `6.79` | 41,540,000.00 USD | 90,830.00 USD | 0.00 USD | `+55.36%` | `13,367.10` |
| `Live` | `Short` | `6.83` | 41,540,000.00 USD | 187.69 USD | 0.00 USD | `+56.05%` | `27.50` |
| `Live` | `Short` | `6.84` | 41,540,000.00 USD | 753.63 USD | 0.00 USD | `+56.51%` | `110.10` |
| `Live` | `Short` | `6.86` | 41,540,000.00 USD | 623.81 USD | 0.00 USD | `+56.74%` | `91.00` |
| `Live` | `Short` | `6.87` | 41,540,000.00 USD | 2,650.00 USD | 0.00 USD | `+56.96%` | `386.60` |
| `Live` | `Short` | `6.89` | 41,560,000.00 USD | 15,430.00 USD | 0.00 USD | `+57.65%` | `2,237.40` |
| `Live` | `Short` | `6.92` | 41,560,000.00 USD | 6,920.00 USD | 0.00 USD | `+58.34%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 41,560,000.00 USD | 1,220.00 USD | 0.00 USD | `+59.71%` | `174.40` |
| `Live` | `Short` | `7.05` | 45,310,000.00 USD | 3,750,000.00 USD | 0.00 USD | `+61.31%` | `531,000.00` |
| `Live` | `Short` | `7.08` | 45,350,000.00 USD | 35,380.00 USD | 0.00 USD | `+61.77%` | `5,000.00` |
| `Live` | `Short` | `7.09` | 45,350,000.00 USD | 699.57 USD | 0.00 USD | `+62.22%` | `98.60` |
| `Live` | `Short` | `7.18` | 45,350,000.00 USD | 1,010.00 USD | 0.00 USD | `+64.28%` | `140.60` |
| `Live` | `Short` | `7.21` | 45,360,000.00 USD | 13,560.00 USD | 0.00 USD | `+64.97%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 45,360,000.00 USD | 1,150.00 USD | 0.00 USD | `+65.42%` | `159.30` |
| `Live` | `Short` | `7.25` | 45,370,000.00 USD | 3,770.00 USD | 0.00 USD | `+65.65%` | `520.00` |
| `Live` | `Short` | `7.26` | 45,370,000.00 USD | 8,530.00 USD | 0.00 USD | `+66.11%` | `1,173.80` |
| `Live` | `Short` | `7.28` | 45,370,000.00 USD | 111.31 USD | 0.00 USD | `+66.34%` | `15.30` |
| `Live` | `Short` | `7.29` | 45,380,000.00 USD | 4,230.00 USD | 0.00 USD | `+66.57%` | `581.20` |
| `Live` | `Short` | `7.33` | 45,380,000.00 USD | 1,320.00 USD | 0.00 USD | `+67.71%` | `180.00` |
| `Live` | `Short` | `7.38` | 45,390,000.00 USD | 12,920.00 USD | 0.00 USD | `+68.85%` | `1,750.00` |
| `Live` | `Short` | `7.39` | 55,270,000.00 USD | 9,880,000.00 USD | 0.00 USD | `+69.08%` | `1,336,000.00` |
| `Live` | `Short` | `7.43` | 55,380,000.00 USD | 106,620.00 USD | 0.00 USD | `+70.00%` | `14,340.70` |
| `Live` | `Short` | `7.46` | 55,380,000.00 USD | 1,420.00 USD | 0.00 USD | `+70.45%` | `191.10` |
| `Live` | `Short` | `7.49` | 63,170,000.00 USD | 7,790,000.00 USD | 0.00 USD | `+71.14%` | `1,040,314.60` |
| `Live` | `Short` | `7.50` | 63,220,000.00 USD | 49,760.00 USD | 0.00 USD | `+71.37%` | `6,639.00` |
| `Live` | `Short` | `7.53` | 63,220,000.00 USD | 1,570.00 USD | 0.00 USD | `+72.06%` | `208.40` |
| `Live` | `Short` | `7.58` | 63,280,000.00 USD | 56,890.00 USD | 0.00 USD | `+73.43%` | `7,500.00` |
| `Live` | `Short` | `7.59` | 63,280,000.00 USD | 2,640.00 USD | 0.00 USD | `+73.66%` | `347.20` |
| `Live` | `Short` | `7.62` | 63,280,000.00 USD | 1,650.00 USD | 0.00 USD | `+74.34%` | `216.50` |
| `Live` | `Short` | `7.63` | 63,300,000.00 USD | 19,210.00 USD | 0.00 USD | `+74.57%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 63,330,000.00 USD | 26,080.00 USD | 0.00 USD | `+75.03%` | `3,407.20` |
| `Live` | `Short` | `7.67` | 63,330,000.00 USD | 360.25 USD | 0.00 USD | `+75.26%` | `47.00` |
| `Live` | `Short` | `7.72` | 64,520,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+76.63%` | `154,780.70` |
| `Live` | `Short` | `7.74` | 64,520,000.00 USD | 505.87 USD | 0.00 USD | `+76.86%` | `65.40` |
| `Live` | `Short` | `7.75` | 64,520,000.00 USD | 629.67 USD | 0.00 USD | `+77.09%` | `81.30` |
| `Live` | `Short` | `7.83` | 64,550,000.00 USD | 27,360.00 USD | 0.00 USD | `+78.91%` | `3,496.50` |
| `Live` | `Short` | `7.87` | 64,550,000.00 USD | 2,980.00 USD | 0.00 USD | `+79.83%` | `378.70` |
| `Live` | `Short` | `7.88` | 64,550,000.00 USD | 253.58 USD | 0.00 USD | `+80.06%` | `32.20` |
| `Live` | `Short` | `7.95` | 64,560,000.00 USD | 6,120.00 USD | 0.00 USD | `+81.66%` | `769.80` |
| `Live` | `Short` | `7.97` | 64,580,000.00 USD | 25,520.00 USD | 0.00 USD | `+82.34%` | `3,200.00` |
| `Live` | `Short` | `7.99` | 64,590,000.00 USD | 6,790.00 USD | 0.00 USD | `+82.57%` | `850.00` |
| `Live` | `Short` | `8.00` | 64,690,000.00 USD | 96,110.00 USD | 0.00 USD | `+82.80%` | `12,020.90` |
| `Live` | `Short` | `8.03` | 65,120,000.00 USD | 435,420.00 USD | 0.00 USD | `+83.49%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 65,130,000.00 USD | 4,660.00 USD | 0.00 USD | `+84.40%` | `577.20` |
| `Live` | `Short` | `8.10` | 65,140,000.00 USD | 12,260.00 USD | 0.00 USD | `+85.09%` | `1,514.20` |
| `Live` | `Short` | `8.20` | 65,140,000.00 USD | 951.44 USD | 0.00 USD | `+87.37%` | `116.10` |
| `Live` | `Short` | `8.23` | 65,190,000.00 USD | 51,880.00 USD | 0.00 USD | `+88.29%` | `6,300.00` |
| `Live` | `Short` | `8.28` | 65,300,000.00 USD | 103,990.00 USD | 0.00 USD | `+89.20%` | `12,566.70` |
| `Live` | `Short` | `8.29` | 65,300,000.00 USD | 165.07 USD | 0.00 USD | `+89.66%` | `19.90` |
| `Live` | `Short` | `8.32` | 65,300,000.00 USD | 3,600.00 USD | 0.00 USD | `+90.35%` | `432.10` |
| `Live` | `Short` | `8.35` | 65,330,000.00 USD | 25,310.00 USD | 0.00 USD | `+90.80%` | `3,032.60` |
| `Live` | `Short` | `8.38` | 65,330,000.00 USD | 191.79 USD | 0.00 USD | `+91.49%` | `22.90` |
| `Live` | `Short` | `8.47` | 65,330,000.00 USD | 816.99 USD | 0.00 USD | `+93.78%` | `96.40` |
| `Live` | `Short` | `8.48` | 65,330,000.00 USD | 6,640.00 USD | 0.00 USD | `+94.00%` | `782.50` |
| `Live` | `Short` | `8.49` | 65,790,000.00 USD | 453,180.00 USD | 0.00 USD | `+94.23%` | `53,346.40` |
| `Live` | `Short` | `8.52` | 65,790,000.00 USD | 1,230.00 USD | 0.00 USD | `+94.69%` | `145.00` |
| `Live` | `Short` | `8.53` | 65,820,000.00 USD | 34,680.00 USD | 0.00 USD | `+94.92%` | `4,068.00` |
| `Live` | `Short` | `8.54` | 65,820,000.00 USD | 127.17 USD | 0.00 USD | `+95.15%` | `14.90` |
| `Live` | `Short` | `8.54` | 65,820,000.00 USD | 124.76 USD | 0.00 USD | `+95.38%` | `14.60` |
| `Live` | `Short` | `8.57` | 67,210,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+96.06%` | `161,429.40` |
| `Live` | `Short` | `8.60` | 67,210,000.00 USD | 240.66 USD | 0.00 USD | `+96.52%` | `28.00` |
| `Live` | `Short` | `8.63` | 67,270,000.00 USD | 63,320.00 USD | 0.00 USD | `+97.43%` | `7,333.30` |
| `Live` | `Short` | `8.68` | 67,270,000.00 USD | 2,320.00 USD | 0.00 USD | `+98.35%` | `267.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,520,000.00 USD | 0.00 USD | 585.51 USD | `-77.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,520,000.00 USD | 0.00 USD | 339.82 USD | `-76.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,520,000.00 USD | 0.00 USD | 196.58 USD | `-72.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,520,000.00 USD | 0.00 USD | 331.54 USD | `-69.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,520,000.00 USD | 0.00 USD | 345.25 USD | `-69.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,520,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,510,000.00 USD | 0.00 USD | 997.29 USD | `-68.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.49` | 3,510,000.00 USD | 0.00 USD | 582.71 USD | `-66.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,510,000.00 USD | 0.00 USD | 139.83 USD | `-65.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,510,000.00 USD | 0.00 USD | 113.28 USD | `-64.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,510,000.00 USD | 0.00 USD | 4,000.00 USD | `-64.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,510,000.00 USD | 0.00 USD | 950.26 USD | `-64.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,510,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,500,000.00 USD | 0.00 USD | 739.67 USD | `-63.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,500,000.00 USD | 0.00 USD | 1,740.00 USD | `-62.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,500,000.00 USD | 0.00 USD | 6,260.00 USD | `-62.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,490,000.00 USD | 0.00 USD | 345.40 USD | `-62.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,490,000.00 USD | 0.00 USD | 167.50 USD | `-61.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,490,000.00 USD | 0.00 USD | 669.02 USD | `-61.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,490,000.00 USD | 0.00 USD | 105.88 USD | `-61.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,490,000.00 USD | 0.00 USD | 172.50 USD | `-60.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,490,000.00 USD | 0.00 USD | 10,650.00 USD | `-59.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,480,000.00 USD | 0.00 USD | 722.00 USD | `-58.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,480,000.00 USD | 0.00 USD | 259.00 USD | `-58.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,480,000.00 USD | 0.00 USD | 103.84 USD | `-58.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,480,000.00 USD | 0.00 USD | 109.00 USD | `-58.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,480,000.00 USD | 0.00 USD | 222.19 USD | `-57.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,480,000.00 USD | 0.00 USD | 10,280.00 USD | `-56.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,470,000.00 USD | 0.00 USD | 558.36 USD | `-56.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,470,000.00 USD | 0.00 USD | 1,520.00 USD | `-55.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,470,000.00 USD | 0.00 USD | 222.14 USD | `-55.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,470,000.00 USD | 0.00 USD | 279.50 USD | `-55.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,470,000.00 USD | 0.00 USD | 197.50 USD | `-54.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,470,000.00 USD | 0.00 USD | 935.66 USD | `-54.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,470,000.00 USD | 0.00 USD | 18,860.00 USD | `-54.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,450,000.00 USD | 0.00 USD | 3,020.00 USD | `-53.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,440,000.00 USD | 0.00 USD | 214.52 USD | `-53.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,440,000.00 USD | 0.00 USD | 1,200.00 USD | `-53.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,440,000.00 USD | 0.00 USD | 578.41 USD | `-52.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,440,000.00 USD | 0.00 USD | 18,070.00 USD | `-52.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,420,000.00 USD | 0.00 USD | 108.62 USD | `-51.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,420,000.00 USD | 0.00 USD | 107.23 USD | `-51.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,420,000.00 USD | 0.00 USD | 1,590.00 USD | `-51.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,420,000.00 USD | 0.00 USD | 5,830.00 USD | `-50.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,420,000.00 USD | 0.00 USD | 310.32 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,420,000.00 USD | 0.00 USD | 1,170.00 USD | `-50.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,420,000.00 USD | 0.00 USD | 576.18 USD | `-50.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,410,000.00 USD | 0.00 USD | 295.67 USD | `-49.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,410,000.00 USD | 0.00 USD | 1,430.00 USD | `-49.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,410,000.00 USD | 0.00 USD | 812.68 USD | `-49.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,410,000.00 USD | 0.00 USD | 1,440.00 USD | `-49.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,410,000.00 USD | 0.00 USD | 106.16 USD | `-48.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,410,000.00 USD | 0.00 USD | 6,270.00 USD | `-48.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,400,000.00 USD | 0.00 USD | 478.06 USD | `-48.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,400,000.00 USD | 0.00 USD | 540.88 USD | `-48.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,400,000.00 USD | 0.00 USD | 867.46 USD | `-47.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,400,000.00 USD | 0.00 USD | 759.76 USD | `-47.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,400,000.00 USD | 0.00 USD | 11,060.00 USD | `-47.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,390,000.00 USD | 0.00 USD | 3,690.00 USD | `-47.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,390,000.00 USD | 0.00 USD | 10,280.00 USD | `-46.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,380,000.00 USD | 0.00 USD | 467.00 USD | `-46.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,380,000.00 USD | 0.00 USD | 506.75 USD | `-46.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,380,000.00 USD | 0.00 USD | 214.27 USD | `-45.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,380,000.00 USD | 0.00 USD | 428.69 USD | `-45.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,380,000.00 USD | 0.00 USD | 322.45 USD | `-45.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,370,000.00 USD | 0.00 USD | 108.25 USD | `-45.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,370,000.00 USD | 0.00 USD | 3,900.00 USD | `-45.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,370,000.00 USD | 0.00 USD | 799.04 USD | `-44.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,370,000.00 USD | 0.00 USD | 6,830.00 USD | `-44.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,360,000.00 USD | 0.00 USD | 137.16 USD | `-44.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,360,000.00 USD | 0.00 USD | 504.41 USD | `-43.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,360,000.00 USD | 0.00 USD | 963.93 USD | `-43.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,360,000.00 USD | 0.00 USD | 6,690.00 USD | `-42.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,360,000.00 USD | 0.00 USD | 541.98 USD | `-42.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,350,000.00 USD | 0.00 USD | 108.75 USD | `-42.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,350,000.00 USD | 0.00 USD | 766.55 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,350,000.00 USD | 0.00 USD | 7,110.00 USD | `-41.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,350,000.00 USD | 0.00 USD | 1,100.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,350,000.00 USD | 0.00 USD | 100.04 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 3,350,000.00 USD | 0.00 USD | 743.47 USD | `-40.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 3,340,000.00 USD | 0.00 USD | 5,090.00 USD | `-40.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 3,340,000.00 USD | 0.00 USD | 226.57 USD | `-38.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,340,000.00 USD | 0.00 USD | 104.98 USD | `-38.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,340,000.00 USD | 0.00 USD | 889.89 USD | `-38.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 3,340,000.00 USD | 0.00 USD | 7,270.00 USD | `-38.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 3,330,000.00 USD | 0.00 USD | 107.21 USD | `-37.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,330,000.00 USD | 0.00 USD | 197.37 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,330,000.00 USD | 0.00 USD | 8,110.00 USD | `-37.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,320,000.00 USD | 0.00 USD | 108.39 USD | `-36.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,320,000.00 USD | 0.00 USD | 435.95 USD | `-36.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,320,000.00 USD | 0.00 USD | 217.23 USD | `-36.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,320,000.00 USD | 0.00 USD | 437.98 USD | `-36.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 3,320,000.00 USD | 0.00 USD | 1,230.00 USD | `-35.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,320,000.00 USD | 0.00 USD | 8,380.00 USD | `-35.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,310,000.00 USD | 0.00 USD | 283.50 USD | `-35.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,310,000.00 USD | 0.00 USD | 109.53 USD | `-34.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,310,000.00 USD | 0.00 USD | 1,230.00 USD | `-34.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,310,000.00 USD | 0.00 USD | 1,960.00 USD | `-34.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,310,000.00 USD | 0.00 USD | 157.81 USD | `-34.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,310,000.00 USD | 0.00 USD | 3,170.00 USD | `-33.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,300,000.00 USD | 0.00 USD | 4,870.00 USD | `-33.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,300,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,300,000.00 USD | 0.00 USD | 493.15 USD | `-33.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,300,000.00 USD | 0.00 USD | 1,560.00 USD | `-32.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,300,000.00 USD | 0.00 USD | 24,200.00 USD | `-32.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,270,000.00 USD | 0.00 USD | 738.75 USD | `-32.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,270,000.00 USD | 0.00 USD | 523.32 USD | `-32.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 3,270,000.00 USD | 0.00 USD | 4,470.00 USD | `-31.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 3,270,000.00 USD | 0.00 USD | 12,170.00 USD | `-31.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,250,000.00 USD | 0.00 USD | 1,020.00 USD | `-31.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,250,000.00 USD | 0.00 USD | 214.57 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,250,000.00 USD | 0.00 USD | 249.08 USD | `-30.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,250,000.00 USD | 0.00 USD | 305.50 USD | `-30.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,250,000.00 USD | 0.00 USD | 109.42 USD | `-29.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 3,250,000.00 USD | 0.00 USD | 9,300.00 USD | `-29.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,240,000.00 USD | 0.00 USD | 583.44 USD | `-28.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,240,000.00 USD | 0.00 USD | 104.69 USD | `-28.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 3,240,000.00 USD | 0.00 USD | 315.69 USD | `-28.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,240,000.00 USD | 0.00 USD | 214.17 USD | `-28.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,240,000.00 USD | 0.00 USD | 329.07 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,240,000.00 USD | 0.00 USD | 4,210.00 USD | `-27.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 3,240,000.00 USD | 0.00 USD | 1,030.00 USD | `-27.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 3,240,000.00 USD | 0.00 USD | 218.81 USD | `-27.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,240,000.00 USD | 0.00 USD | 24,840.00 USD | `-26.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 3,210,000.00 USD | 0.00 USD | 144.67 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 3,210,000.00 USD | 0.00 USD | 273,030.00 USD | `-26.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,940,000.00 USD | 0.00 USD | 27,380.00 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,910,000.00 USD | 0.00 USD | 1,530.00 USD | `-25.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,910,000.00 USD | 0.00 USD | 104.81 USD | `-25.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,910,000.00 USD | 0.00 USD | 200.10 USD | `-25.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,910,000.00 USD | 0.00 USD | 1,480.00 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,910,000.00 USD | 0.00 USD | 1,870.00 USD | `-24.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,910,000.00 USD | 0.00 USD | 11,460.00 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,890,000.00 USD | 0.00 USD | 240.67 USD | `-24.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,890,000.00 USD | 0.00 USD | 306.56 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,890,000.00 USD | 0.00 USD | 1,670.00 USD | `-23.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,890,000.00 USD | 0.00 USD | 154,840.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,740,000.00 USD | 0.00 USD | 73,220.00 USD | `-23.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,660,000.00 USD | 0.00 USD | 19,600.00 USD | `-22.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,640,000.00 USD | 0.00 USD | 2,350.00 USD | `-22.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,640,000.00 USD | 0.00 USD | 8,490.00 USD | `-22.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,630,000.00 USD | 0.00 USD | 102,530.00 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,530,000.00 USD | 0.00 USD | 421.41 USD | `-21.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,530,000.00 USD | 0.00 USD | 4,350.00 USD | `-21.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,530,000.00 USD | 0.00 USD | 444.49 USD | `-21.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,530,000.00 USD | 0.00 USD | 2,550.00 USD | `-21.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,520,000.00 USD | 0.00 USD | 1,380.00 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,520,000.00 USD | 0.00 USD | 344.07 USD | `-20.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,520,000.00 USD | 0.00 USD | 28,240.00 USD | `-20.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,490,000.00 USD | 0.00 USD | 15,680.00 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,480,000.00 USD | 0.00 USD | 894.72 USD | `-20.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,480,000.00 USD | 0.00 USD | 70,870.00 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,410,000.00 USD | 0.00 USD | 21,320.00 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,380,000.00 USD | 0.00 USD | 3,700.00 USD | `-19.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,380,000.00 USD | 0.00 USD | 16,250.00 USD | `-19.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,360,000.00 USD | 0.00 USD | 5,130.00 USD | `-18.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,360,000.00 USD | 0.00 USD | 1,800.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,360,000.00 USD | 0.00 USD | 18,440.00 USD | `-18.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,340,000.00 USD | 0.00 USD | 76,640.00 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,260,000.00 USD | 0.00 USD | 1,610.00 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,260,000.00 USD | 0.00 USD | 331.46 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,260,000.00 USD | 0.00 USD | 56,250.00 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,200,000.00 USD | 0.00 USD | 43,440.00 USD | `-17.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,160,000.00 USD | 0.00 USD | 1,000.00 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,160,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,160,000.00 USD | 0.00 USD | 54,670.00 USD | `-16.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,100,000.00 USD | 0.00 USD | 8,000.00 USD | `-16.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,100,000.00 USD | 0.00 USD | 4,070.00 USD | `-16.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,090,000.00 USD | 0.00 USD | 367.50 USD | `-15.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,090,000.00 USD | 0.00 USD | 19,240.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,070,000.00 USD | 0.00 USD | 4,370.00 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,070,000.00 USD | 0.00 USD | 218,710.00 USD | `-15.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,850,000.00 USD | 0.00 USD | 6,300.00 USD | `-15.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,840,000.00 USD | 0.00 USD | 8,050.00 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,830,000.00 USD | 0.00 USD | 32,040.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,800,000.00 USD | 0.00 USD | 28,820.00 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,770,000.00 USD | 0.00 USD | 14,230.00 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,760,000.00 USD | 0.00 USD | 8,780.00 USD | `-13.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,750,000.00 USD | 0.00 USD | 1,190.00 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,750,000.00 USD | 0.00 USD | 2,190.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,750,000.00 USD | 0.00 USD | 44,700.00 USD | `-13.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,700,000.00 USD | 0.00 USD | 4,530.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,700,000.00 USD | 0.00 USD | 21,180.00 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,680,000.00 USD | 0.00 USD | 7,350.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,670,000.00 USD | 0.00 USD | 41,340.00 USD | `-12.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,630,000.00 USD | 0.00 USD | 10,050.00 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,620,000.00 USD | 0.00 USD | 3,130.00 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,620,000.00 USD | 0.00 USD | 6,580.00 USD | `-11.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,610,000.00 USD | 0.00 USD | 161,230.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,450,000.00 USD | 0.00 USD | 26,910.00 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,420,000.00 USD | 0.00 USD | 8,970.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,410,000.00 USD | 0.00 USD | 47,220.00 USD | `-10.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,360,000.00 USD | 0.00 USD | 1,310.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,360,000.00 USD | 0.00 USD | 6,910.00 USD | `-10.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,360,000.00 USD | 0.00 USD | 934.17 USD | `-10.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,360,000.00 USD | 0.00 USD | 4,950.00 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,350,000.00 USD | 0.00 USD | 3,180.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,350,000.00 USD | 0.00 USD | 13,690.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 1,330,000.00 USD | 0.00 USD | 317.60 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 1,330,000.00 USD | 0.00 USD | 42,280.00 USD | `-8.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 1,290,000.00 USD | 0.00 USD | 667.16 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 1,290,000.00 USD | 0.00 USD | 278,010.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 1,010,000.00 USD | 0.00 USD | 350.51 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 1,010,000.00 USD | 0.00 USD | 222,270.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 789,620.00 USD | 0.00 USD | 428.11 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 789,200.00 USD | 0.00 USD | 919.83 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 788,280.00 USD | 0.00 USD | 34,070.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 754,210.00 USD | 0.00 USD | 15,710.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 738,500.00 USD | 0.00 USD | 5,570.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 732,920.00 USD | 0.00 USD | 3,400.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 729,520.00 USD | 0.00 USD | 13,770.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 715,750.00 USD | 0.00 USD | 48,600.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 667,150.00 USD | 0.00 USD | 71,500.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 595,650.00 USD | 0.00 USD | 3,880.00 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 591,770.00 USD | 0.00 USD | 31,590.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 560,180.00 USD | 0.00 USD | 2,390.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 557,790.00 USD | 0.00 USD | 64,710.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 493,080.00 USD | 0.00 USD | 27,880.00 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 465,210.00 USD | 0.00 USD | 8,530.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 456,680.00 USD | 0.00 USD | 3,680.00 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 453,000.00 USD | 0.00 USD | 6,040.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 446,960.00 USD | 0.00 USD | 11,730.00 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 435,240.00 USD | 0.00 USD | 14,410.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 420,830.00 USD | 0.00 USD | 15,350.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 405,470.00 USD | 0.00 USD | 63,060.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 342,410.00 USD | 0.00 USD | 53,310.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 289,100.00 USD | 0.00 USD | 13,770.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 275,330.00 USD | 0.00 USD | 1,830.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 273,490.00 USD | 0.00 USD | 2,220.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 271,270.00 USD | 0.00 USD | 17,210.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 254,060.00 USD | 0.00 USD | 3,020.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 251,040.00 USD | 0.00 USD | 6,380.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 244,660.00 USD | 0.00 USD | 16,490.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 228,170.00 USD | 0.00 USD | 33,460.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 194,710.00 USD | 0.00 USD | 902.55 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 193,810.00 USD | 0.00 USD | 17,380.00 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.36` | 176,430.00 USD | 0.00 USD | 15,410.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.37` | 161,010.00 USD | 0.00 USD | 161,010.00 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 87,500.00 USD | 87,500.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 94,640.00 USD | 7,140.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 284,080.00 USD | 189,440.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 353,650.00 USD | 69,580.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 358,310.00 USD | 4,650.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 439,760.00 USD | 81,450.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 452,850.00 USD | 13,090.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 513,450.00 USD | 60,600.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 763,120.00 USD | 249,670.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 766,530.00 USD | 3,410.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 767,030.00 USD | 498.51 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 768,340.00 USD | 1,310.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 786,080.00 USD | 17,740.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 830,300.00 USD | 44,220.00 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 849,240.00 USD | 18,940.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 852,530.00 USD | 3,290.00 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 887,970.00 USD | 35,440.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 888,390.00 USD | 417.69 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 888,780.00 USD | 392.64 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 889,110.00 USD | 331.42 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 893,400.00 USD | 4,280.00 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 893,940.00 USD | 539.20 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 894,300.00 USD | 364.84 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,010,000.00 USD | 118,470.00 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,010,000.00 USD | 742.55 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,040,000.00 USD | 21,860.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 2,040,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 2,050,000.00 USD | 4,070.00 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 2,050,000.00 USD | 277.44 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 2,110,000.00 USD | 66,030.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 2,120,000.00 USD | 3,030.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 2,120,000.00 USD | 914.98 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 2,160,000.00 USD | 45,680.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,560,000.00 USD | 396,380.00 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,800,000.00 USD | 235,990.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,800,000.00 USD | 2,650.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,880,000.00 USD | 84,970.00 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,900,000.00 USD | 19,800.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,930,000.00 USD | 29,420.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,950,000.00 USD | 16,330.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,950,000.00 USD | 2,640.00 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,950,000.00 USD | 314.37 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,970,000.00 USD | 22,590.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,150,000.00 USD | 176,250.00 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,180,000.00 USD | 30,560.00 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,190,000.00 USD | 8,540.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,280,000.00 USD | 93,590.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,320,000.00 USD | 40,760.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,350,000.00 USD | 23,780.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,370,000.00 USD | 23,180.00 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,380,000.00 USD | 10,400.00 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,400,000.00 USD | 19,890.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,410,000.00 USD | 4,060.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,520,000.00 USD | 111,630.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,520,000.00 USD | 156.30 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,530,000.00 USD | 13,180.00 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,530,000.00 USD | 483.63 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,530,000.00 USD | 313.51 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,540,000.00 USD | 7,900.00 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,590,000.00 USD | 47,350.00 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,590,000.00 USD | 187.06 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,680,000.00 USD | 94,590.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,680,000.00 USD | 2,540.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,750,000.00 USD | 61,510.00 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,770,000.00 USD | 25,080.00 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,780,000.00 USD | 5,030.00 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,800,000.00 USD | 19,640.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,800,000.00 USD | 120.58 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,810,000.00 USD | 14,090.00 USD | 0.00 USD | `+15.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,820,000.00 USD | 5,860.00 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,900,000.00 USD | 87,450.00 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,910,000.00 USD | 5,460.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,910,000.00 USD | 178.33 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,980,000.00 USD | 70,250.00 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,990,000.00 USD | 15,350.00 USD | 0.00 USD | `+16.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,990,000.00 USD | 179.38 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,990,000.00 USD | 179.72 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,990,000.00 USD | 217.63 USD | 0.00 USD | `+17.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,000,000.00 USD | 493.85 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,000,000.00 USD | 575.38 USD | 0.00 USD | `+18.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,000,000.00 USD | 327.58 USD | 0.00 USD | `+18.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,000,000.00 USD | 163.85 USD | 0.00 USD | `+18.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,120,000.00 USD | 120,930.00 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,150,000.00 USD | 36,120.00 USD | 0.00 USD | `+19.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,150,000.00 USD | 1,710.00 USD | 0.00 USD | `+19.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,160,000.00 USD | 432.63 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,160,000.00 USD | 2,620.00 USD | 0.00 USD | `+19.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,160,000.00 USD | 537.61 USD | 0.00 USD | `+19.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,580,000.00 USD | 420,400.00 USD | 0.00 USD | `+20.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,580,000.00 USD | 278.52 USD | 0.00 USD | `+20.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,580,000.00 USD | 589.22 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,580,000.00 USD | 733.03 USD | 0.00 USD | `+20.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,580,000.00 USD | 423.60 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,590,000.00 USD | 12,620.00 USD | 0.00 USD | `+21.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,590,000.00 USD | 381.09 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,590,000.00 USD | 961.16 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,600,000.00 USD | 1,570.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,600,000.00 USD | 5,650.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,600,000.00 USD | 160.11 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,600,000.00 USD | 225.33 USD | 0.00 USD | `+22.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,600,000.00 USD | 438.60 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,610,000.00 USD | 6,610.00 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,650,000.00 USD | 40,710.00 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,670,000.00 USD | 21,220.00 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,680,000.00 USD | 4,330.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,680,000.00 USD | 639.61 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,680,000.00 USD | 1,710.00 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,690,000.00 USD | 13,690.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,780,000.00 USD | 87,720.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,810,000.00 USD | 30,110.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,810,000.00 USD | 863.89 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,810,000.00 USD | 1,040.00 USD | 0.00 USD | `+25.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,870,000.00 USD | 55,170.00 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 4,870,000.00 USD | 5,600.00 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 4,890,000.00 USD | 19,110.00 USD | 0.00 USD | `+26.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 4,910,000.00 USD | 18,790.00 USD | 0.00 USD | `+26.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 4,970,000.00 USD | 58,030.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,020,000.00 USD | 46,110.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,030,000.00 USD | 14,320.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,040,000.00 USD | 11,740.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,070,000.00 USD | 23,650.00 USD | 0.00 USD | `+27.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,070,000.00 USD | 384.94 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,070,000.00 USD | 2,530.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,070,000.00 USD | 347.06 USD | 0.00 USD | `+28.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,070,000.00 USD | 347.68 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,070,000.00 USD | 491.11 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,070,000.00 USD | 3,290.00 USD | 0.00 USD | `+29.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,070,000.00 USD | 281.55 USD | 0.00 USD | `+29.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,080,000.00 USD | 6,590.00 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,080,000.00 USD | 235.93 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,090,000.00 USD | 5,860.00 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,190,000.00 USD | 103,820.00 USD | 0.00 USD | `+30.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,190,000.00 USD | 705.23 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 5,200,000.00 USD | 5,720.00 USD | 0.00 USD | `+30.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,200,000.00 USD | 139.03 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,200,000.00 USD | 2,480.00 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 5,200,000.00 USD | 1,850.00 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 5,200,000.00 USD | 286.94 USD | 0.00 USD | `+32.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 5,210,000.00 USD | 7,120.00 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 5,210,000.00 USD | 329.13 USD | 0.00 USD | `+32.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,210,000.00 USD | 1,970.00 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,210,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 5,210,000.00 USD | 2,720.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 5,210,000.00 USD | 1,190.00 USD | 0.00 USD | `+33.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 5,220,000.00 USD | 1,770.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 5,220,000.00 USD | 3,450.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 5,220,000.00 USD | 345.45 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 5,240,000.00 USD | 24,040.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 5,250,000.00 USD | 1,670.00 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 5,250,000.00 USD | 1,020.00 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 5,400,000.00 USD | 153,150.00 USD | 0.00 USD | `+35.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 5,430,000.00 USD | 26,180.00 USD | 0.00 USD | `+36.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 5,430,000.00 USD | 5,440.00 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 5,440,000.00 USD | 8,940.00 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 5,560,000.00 USD | 119,340.00 USD | 0.00 USD | `+36.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 5,560,000.00 USD | 3,000.00 USD | 0.00 USD | `+37.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 5,760,000.00 USD | 195,580.00 USD | 0.00 USD | `+37.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 5,770,000.00 USD | 13,710.00 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 5,860,000.00 USD | 90,380.00 USD | 0.00 USD | `+37.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 5,860,000.00 USD | 2,050.00 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 5,870,000.00 USD | 3,300.00 USD | 0.00 USD | `+38.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 5,870,000.00 USD | 1,040.00 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 5,870,000.00 USD | 425.76 USD | 0.00 USD | `+38.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 5,870,000.00 USD | 4,120.00 USD | 0.00 USD | `+39.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 5,930,000.00 USD | 61,050.00 USD | 0.00 USD | `+39.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 5,940,000.00 USD | 1,610.00 USD | 0.00 USD | `+39.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 5,940,000.00 USD | 1,200.00 USD | 0.00 USD | `+40.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 5,940,000.00 USD | 420.32 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 5,940,000.00 USD | 4,010.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,010,000.00 USD | 66,060.00 USD | 0.00 USD | `+41.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,010,000.00 USD | 1,890.00 USD | 0.00 USD | `+42.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,010,000.00 USD | 195.46 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,010,000.00 USD | 289.93 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,010,000.00 USD | 116.16 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,020,000.00 USD | 7,310.00 USD | 0.00 USD | `+44.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,020,000.00 USD | 310.70 USD | 0.00 USD | `+44.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,020,000.00 USD | 325.62 USD | 0.00 USD | `+44.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,020,000.00 USD | 1,760.00 USD | 0.00 USD | `+45.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,020,000.00 USD | 3,230.00 USD | 0.00 USD | `+46.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,030,000.00 USD | 5,120.00 USD | 0.00 USD | `+46.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,030,000.00 USD | 1,310.00 USD | 0.00 USD | `+48.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,060,000.00 USD | 30,990.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,060,000.00 USD | 104.24 USD | 0.00 USD | `+48.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,070,000.00 USD | 13,580.00 USD | 0.00 USD | `+49.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,080,000.00 USD | 1,630.00 USD | 0.00 USD | `+50.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,080,000.00 USD | 1,370.00 USD | 0.00 USD | `+50.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,080,000.00 USD | 5,400.00 USD | 0.00 USD | `+51.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,080,000.00 USD | 1,620.00 USD | 0.00 USD | `+51.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,090,000.00 USD | 450.55 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,090,000.00 USD | 3,060.00 USD | 0.00 USD | `+52.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,090,000.00 USD | 3,070.00 USD | 0.00 USD | `+53.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,090,000.00 USD | 1,550.00 USD | 0.00 USD | `+54.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,090,000.00 USD | 647.56 USD | 0.00 USD | `+55.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,090,000.00 USD | 1,420.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,100,000.00 USD | 2,130.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 6,100,000.00 USD | 6,870.00 USD | 0.00 USD | `+56.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 6,100,000.00 USD | 342.25 USD | 0.00 USD | `+56.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 6,110,000.00 USD | 2,990.00 USD | 0.00 USD | `+56.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 6,110,000.00 USD | 324.54 USD | 0.00 USD | `+57.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 6,110,000.00 USD | 504.21 USD | 0.00 USD | `+58.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 6,110,000.00 USD | 166.00 USD | 0.00 USD | `+59.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 6,110,000.00 USD | 4,190.00 USD | 0.00 USD | `+59.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 6,130,000.00 USD | 13,480.00 USD | 0.00 USD | `+60.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 6,130,000.00 USD | 2,860.00 USD | 0.00 USD | `+61.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 6,130,000.00 USD | 264.31 USD | 0.00 USD | `+62.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 6,130,000.00 USD | 599.34 USD | 0.00 USD | `+63.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 6,130,000.00 USD | 193.19 USD | 0.00 USD | `+63.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 6,130,000.00 USD | 3,950.00 USD | 0.00 USD | `+64.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 6,140,000.00 USD | 1,940.00 USD | 0.00 USD | `+64.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 6,300,000.00 USD | 160,550.00 USD | 0.00 USD | `+65.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 6,300,000.00 USD | 1,290.00 USD | 0.00 USD | `+66.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 6,300,000.00 USD | 1,180.00 USD | 0.00 USD | `+67.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 6,300,000.00 USD | 630.05 USD | 0.00 USD | `+69.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 6,300,000.00 USD | 1,410.00 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 6,300,000.00 USD | 2,610.00 USD | 0.00 USD | `+69.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 6,310,000.00 USD | 7,630.00 USD | 0.00 USD | `+71.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 6,320,000.00 USD | 4,640.00 USD | 0.00 USD | `+73.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 6,320,000.00 USD | 371.88 USD | 0.00 USD | `+73.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 6,320,000.00 USD | 2,510.00 USD | 0.00 USD | `+74.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 6,320,000.00 USD | 380.68 USD | 0.00 USD | `+75.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 6,330,000.00 USD | 11,170.00 USD | 0.00 USD | `+78.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 6,360,000.00 USD | 34,360.00 USD | 0.00 USD | `+78.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 6,360,000.00 USD | 253.21 USD | 0.00 USD | `+78.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 6,360,000.00 USD | 100.29 USD | 0.00 USD | `+79.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 6,380,000.00 USD | 10,610.00 USD | 0.00 USD | `+82.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 6,380,000.00 USD | 309.43 USD | 0.00 USD | `+82.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.99` | 6,380,000.00 USD | 4,640.00 USD | 0.00 USD | `+82.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 6,420,000.00 USD | 36,300.00 USD | 0.00 USD | `+83.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 6,500,000.00 USD | 81,310.00 USD | 0.00 USD | `+83.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.15` | 6,500,000.00 USD | 2,150.00 USD | 0.00 USD | `+86.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 6,500,000.00 USD | 216.90 USD | 0.00 USD | `+87.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 6,500,000.00 USD | 1,990.00 USD | 0.00 USD | `+87.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 6,510,000.00 USD | 7,200.00 USD | 0.00 USD | `+87.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 6,510,000.00 USD | 998.65 USD | 0.00 USD | `+91.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 6,510,000.00 USD | 1,260.00 USD | 0.00 USD | `+91.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 6,610,000.00 USD | 103,010.00 USD | 0.00 USD | `+92.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 6,620,000.00 USD | 721.22 USD | 0.00 USD | `+93.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 6,620,000.00 USD | 5,130.00 USD | 0.00 USD | `+94.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 6,620,000.00 USD | 2,010.00 USD | 0.00 USD | `+96.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 6,620,000.00 USD | 809.17 USD | 0.00 USD | `+97.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 6,620,000.00 USD | 198.20 USD | 0.00 USD | `+97.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 6,630,000.00 USD | 3,670.00 USD | 0.00 USD | `+98.12%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.52` | 19,490,000.00 USD | 0.00 USD | 19,490,000.00 USD | 18,870.00 USD | 0.00 USD | 41,320.00 USD |
| `7D` | `3.53` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD |
| `7D` | `3.54` | 19,200,000.00 USD | 0.00 USD | 19,200,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD |
| `7D` | `3.55` | 19,100,000.00 USD | 0.00 USD | 19,100,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD |
| `7D` | `3.56` | 18,880,000.00 USD | 0.00 USD | 18,880,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD |
| `7D` | `3.57` | 18,810,000.00 USD | 0.00 USD | 18,810,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD |
| `7D` | `3.58` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD |
| `7D` | `3.59` | 18,330,000.00 USD | 0.00 USD | 18,330,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD |
| `7D` | `3.60` | 18,310,000.00 USD | 0.00 USD | 18,310,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 18,210,000.00 USD | 0.00 USD | 18,210,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `7D` | `3.63` | 17,850,000.00 USD | 0.00 USD | 17,850,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `7D` | `3.64` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD |
| `7D` | `3.65` | 17,630,000.00 USD | 0.00 USD | 17,630,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD |
| `7D` | `3.67` | 17,360,000.00 USD | 0.00 USD | 17,360,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD |
| `7D` | `3.68` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.69` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `7D` | `3.70` | 17,160,000.00 USD | 0.00 USD | 17,160,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `7D` | `3.71` | 17,020,000.00 USD | 0.00 USD | 17,020,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD |
| `7D` | `3.72` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `7D` | `3.73` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `7D` | `3.74` | 16,780,000.00 USD | 0.00 USD | 16,780,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD |
| `7D` | `3.75` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD |
| `7D` | `3.76` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `7D` | `3.77` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD |
| `7D` | `3.78` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD |
| `7D` | `3.79` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD |
| `7D` | `3.80` | 15,840,000.00 USD | 0.00 USD | 15,840,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD |
| `7D` | `3.81` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD |
| `7D` | `3.82` | 15,770,000.00 USD | 0.00 USD | 15,770,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `7D` | `3.83` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD |
| `7D` | `3.84` | 15,620,000.00 USD | 0.00 USD | 15,620,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD |
| `7D` | `3.85` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD |
| `1D` | `3.86` | 18,400,000.00 USD | 0.00 USD | 18,400,000.00 USD | 225,350.00 USD | 214,520.00 USD | 92,120.00 USD |
| `7D` | `3.86` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD |
| `1D` | `3.87` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 53,480.00 USD | 58,230.00 USD | 189,180.00 USD |
| `7D` | `3.87` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD |
| `1D` | `3.88` | 17,570,000.00 USD | 0.00 USD | 17,570,000.00 USD | 35,520.00 USD | 26,560.00 USD | 223,410.00 USD |
| `7D` | `3.88` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 110,160.00 USD | 86,900.00 USD | 118,540.00 USD |
| `1D` | `3.89` | 17,290,000.00 USD | 0.00 USD | 17,290,000.00 USD | 397,250.00 USD | 100,370.00 USD | 256,340.00 USD |
| `7D` | `3.89` | 14,650,000.00 USD | 0.00 USD | 14,650,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD |
| `1D` | `3.90` | 16,530,000.00 USD | 0.00 USD | 16,530,000.00 USD | 33,540.00 USD | 53,910.00 USD | 250,830.00 USD |
| `7D` | `3.90` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD |
| `1D` | `3.91` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 378,850.00 USD | 120,100.00 USD | 305,840.00 USD |
| `7D` | `3.91` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 343,070.00 USD | 19,190.00 USD | 122,430.00 USD |
| `7D` | `3.92` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 178,620.00 USD | 66,710.00 USD | 105,000.00 USD |
| `1D` | `3.93` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 116,350.00 USD | 104,340.00 USD | 99,850.00 USD |
| `7D` | `3.93` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD |
| `1D` | `3.94` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 144,900.00 USD | 53,060.00 USD | 141,970.00 USD |
| `7D` | `3.94` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3.95` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 103,590.00 USD | 0.00 USD | 33,070.00 USD |
| `7D` | `3.95` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `3.96` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,410.00 USD |
| `7D` | `3.96` | 13,470,000.00 USD | 0.00 USD | 13,470,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD |
| `1D` | `3.97` | 14,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,570.00 USD |
| `7D` | `3.97` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD |
| `1D` | `3.98` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,570.00 USD |
| `7D` | `3.98` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD |
| `1D` | `3.99` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,320.00 USD |
| `7D` | `3.99` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD |
| `1D` | `4.00` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,740.00 USD |
| `7D` | `4.00` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD |
| `1D` | `4.01` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,970.00 USD |
| `7D` | `4.01` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD |
| `1D` | `4.02` | 12,850,000.00 USD | 0.00 USD | 12,850,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,420.00 USD |
| `7D` | `4.02` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD |
| `1D` | `4.03` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 66,220.00 USD | 59,350.00 USD | 269.89 USD |
| `7D` | `4.03` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD |
| `1D` | `4.04` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 70,930.00 USD | 21,940.00 USD | 183,430.00 USD |
| `7D` | `4.04` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 321,230.00 USD | 0.00 USD | 492,530.00 USD |
| `1D` | `4.05` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 348,930.00 USD | 23,720.00 USD | 119.81 USD |
| `7D` | `4.05` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD |
| `1D` | `4.06` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 36,520.00 USD | 83,800.00 USD | 450,600.00 USD |
| `7D` | `4.06` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD |
| `1D` | `4.07` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 359,790.00 USD | 205,460.00 USD | 334,550.00 USD |
| `7D` | `4.07` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 2,470.00 USD | 287,180.00 USD | 166,640.00 USD |
| `1D` | `4.08` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,620.00 USD |
| `7D` | `4.08` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD |
| `1D` | `4.09` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,730.00 USD |
| `7D` | `4.09` | 7,090,000.00 USD | 0.00 USD | 7,090,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD |
| `1D` | `4.10` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 4,790.00 USD | 89,650.00 USD | 140,980.00 USD |
| `7D` | `4.10` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD |
| `1D` | `4.11` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 122,090.00 USD | 138,540.00 USD | 345,690.00 USD |
| `7D` | `4.11` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 0.00 USD | 25,170.00 USD | 296,050.00 USD |
| `1D` | `4.12` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,240.00 USD |
| `7D` | `4.12` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD |
| `1D` | `4.13` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 160,580.00 USD | 0.00 USD | 398,140.00 USD |
| `7D` | `4.13` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD |
| `1D` | `4.14` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 141,770.00 USD | 29,960.00 USD | 125,750.00 USD |
| `7D` | `4.14` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 241,440.00 USD | 244,270.00 USD | 345,750.00 USD |
| `1D` | `4.15` | 7,280,000.00 USD | 0.00 USD | 7,280,000.00 USD | 526,070.00 USD | 109,290.00 USD | 367,560.00 USD |
| `7D` | `4.15` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.16` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 340,550.00 USD | 100,580.00 USD | 379,060.00 USD |
| `7D` | `4.16` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 22,880.00 USD | 0.00 USD |
| `1D` | `4.17` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 340,700.00 USD | 302,060.00 USD | 310,300.00 USD |
| `7D` | `4.17` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 252,690.00 USD | 84,340.00 USD | 78,260.00 USD |
| `1D` | `4.18` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 389,120.00 USD | 75,540.00 USD | 201,490.00 USD |
| `7D` | `4.18` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 227,940.00 USD | 0.00 USD | 86,570.00 USD |
| `1D` | `4.19` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 148,260.00 USD | 152,090.00 USD | 245,080.00 USD |
| `7D` | `4.19` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 31,500.00 USD | 53,380.00 USD | 132,050.00 USD |
| `7D` | `4.20` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 227,690.00 USD | 107,510.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,300.00 USD |
| `7D` | `4.21` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD |
| `1D` | `4.22` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD |
| `7D` | `4.22` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD |
| `1D` | `4.23` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 113,770.00 USD | 129,320.00 USD | 274,180.00 USD |
| `7D` | `4.23` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.24` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 127,260.00 USD | 98,020.00 USD | 125,910.00 USD |
| `7D` | `4.24` | 921,810.00 USD | 0.00 USD | 921,810.00 USD | 0.00 USD | 45,760.00 USD | 0.00 USD |
| `1D` | `4.25` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 251,300.00 USD | 37,270.00 USD | 329,250.00 USD |
| `7D` | `4.25` | 876,050.00 USD | 0.00 USD | 876,050.00 USD | 3,390.00 USD | 0.00 USD | 156,530.00 USD |
| `1D` | `4.26` | 583,440.00 USD | 0.00 USD | 583,440.00 USD | 120,080.00 USD | 26,390.00 USD | 86,340.00 USD |
| `7D` | `4.26` | 716,130.00 USD | 0.00 USD | 716,130.00 USD | 458,850.00 USD | 0.00 USD | 173,150.00 USD |
| `1D` | `4.27` | 350,640.00 USD | 0.00 USD | 350,640.00 USD | 0.00 USD | 72,480.00 USD | 0.00 USD |
| `7D` | `4.27` | 84,130.00 USD | 0.00 USD | 84,130.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.28` | 278,160.00 USD | 0.00 USD | 278,160.00 USD | 4,310.00 USD | 54,390.00 USD | 316.62 USD |
| `7D` | `4.28` | 59,310.00 USD | 0.00 USD | 59,310.00 USD | 5,380.00 USD | 41,440.00 USD | 0.00 USD |
| `1D` | `4.29` | 219,140.00 USD | 0.00 USD | 219,140.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.29` | 12,490.00 USD | 0.00 USD | 12,490.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.33` | 1,170.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `4.34` | 7,340.00 USD | 0.00 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `4.36` | 380,150.00 USD | 380,150.00 USD | 0.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD |
| `1D` | `4.36` | 760,300.00 USD | 760,300.00 USD | 0.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD |
| `7D` | `4.36` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.37` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 280,420.00 USD | 0.00 USD | 400,530.00 USD |
| `7D` | `4.37` | 393,520.00 USD | 393,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 393,520.00 USD |
| `1D` | `4.38` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 3,030.00 USD | 0.00 USD | 638,650.00 USD |
| `7D` | `4.38` | 883,630.00 USD | 883,630.00 USD | 0.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 356,920.00 USD | 41,380.00 USD | 508,210.00 USD |
| `7D` | `4.39` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD |
| `1D` | `4.40` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 541,780.00 USD | 118,310.00 USD | 409,520.00 USD |
| `7D` | `4.40` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD |
| `1D` | `4.41` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 450,080.00 USD | 331,840.00 USD | 687,150.00 USD |
| `7D` | `4.41` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 128,340.00 USD | 240,270.00 USD | 256,450.00 USD |
| `7D` | `4.42` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 404,280.00 USD | 117,350.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 335,950.00 USD | 146,900.00 USD | 449,050.00 USD |
| `7D` | `4.43` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 293,250.00 USD | 88,400.00 USD | 228,310.00 USD |
| `1D` | `4.44` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 276,510.00 USD | 396,660.00 USD | 452,790.00 USD |
| `7D` | `4.44` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 455,890.00 USD | 143,990.00 USD | 246,120.00 USD |
| `1D` | `4.45` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 76,860.00 USD | 181,120.00 USD | 122,400.00 USD |
| `7D` | `4.45` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD |
| `1D` | `4.46` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 4,580.00 USD | 91,550.00 USD | 31,690.00 USD |
| `7D` | `4.46` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 3,070.00 USD | 146,940.00 USD | 2,350.00 USD |
| `1D` | `4.47` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 222,670.00 USD | 25,190.00 USD | 120,000.00 USD |
| `7D` | `4.47` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD |
| `1D` | `4.48` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 246,890.00 USD | 116,490.00 USD | 149,350.00 USD |
| `7D` | `4.48` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD |
| `1D` | `4.49` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 310,660.00 USD | 242,590.00 USD | 405,650.00 USD |
| `7D` | `4.49` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD |
| `1D` | `4.50` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 427,290.00 USD | 118,600.00 USD | 241,350.00 USD |
| `7D` | `4.50` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 376,770.00 USD | 223,580.00 USD | 2,050.00 USD |
| `1D` | `4.51` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 314,310.00 USD | 168,440.00 USD | 487,510.00 USD |
| `7D` | `4.51` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 80,400.00 USD |
| `1D` | `4.52` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 351,620.00 USD | 105,450.00 USD | 286,220.00 USD |
| `7D` | `4.52` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 230,020.00 USD | 0.00 USD | 225,430.00 USD |
| `1D` | `4.53` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 505,320.00 USD | 36,240.00 USD | 278,330.00 USD |
| `7D` | `4.53` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD |
| `1D` | `4.54` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 17,740.00 USD | 177,790.00 USD | 168,090.00 USD |
| `7D` | `4.54` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 2,730.00 USD | 20,720.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 3,110.00 USD | 34,450.00 USD | 108,750.00 USD |
| `7D` | `4.55` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 558.34 USD |
| `1D` | `4.56` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 112,410.00 USD | 32,800.00 USD | 288,710.00 USD |
| `7D` | `4.56` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD |
| `1D` | `4.57` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 176,590.00 USD | 70,180.00 USD | 98,690.00 USD |
| `7D` | `4.57` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD |
| `1D` | `4.58` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 378,810.00 USD | 99,430.00 USD | 554,210.00 USD |
| `7D` | `4.58` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 47,670.00 USD | 0.00 USD | 86,090.00 USD |
| `1D` | `4.59` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 360,700.00 USD | 75,460.00 USD | 109,580.00 USD |
| `7D` | `4.59` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD |
| `1D` | `4.60` | 16,910,000.00 USD | 16,910,000.00 USD | 0.00 USD | 48,970.00 USD | 50,860.00 USD | 67,720.00 USD |
| `7D` | `4.60` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD |
| `1D` | `4.61` | 17,060,000.00 USD | 17,060,000.00 USD | 0.00 USD | 64,820.00 USD | 7,560.00 USD | 76,000.00 USD |
| `7D` | `4.61` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `4.62` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 95,000.00 USD | 31,380.00 USD | 19,240.00 USD |
| `7D` | `4.62` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `4.63` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | 1,960.00 USD |
| `7D` | `4.63` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 107,080.00 USD | 11,270.00 USD | 43,790.00 USD |
| `7D` | `4.64` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD |
| `1D` | `4.65` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 204,970.00 USD | 52,020.00 USD | 485,030.00 USD |
| `7D` | `4.65` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 423,410.00 USD | 0.00 USD | 2,070.00 USD |
| `1D` | `4.66` | 18,910,000.00 USD | 18,910,000.00 USD | 0.00 USD | 202,480.00 USD | 309,340.00 USD | 276,820.00 USD |
| `7D` | `4.66` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 88,400.00 USD | 0.00 USD | 259,380.00 USD |
| `7D` | `4.67` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 19,450,000.00 USD | 19,450,000.00 USD | 0.00 USD | 59,560.00 USD | 106,120.00 USD | 35,340.00 USD |
| `7D` | `4.68` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD |
| `1D` | `4.69` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 168,270.00 USD | 49,160.00 USD | 168,690.00 USD |
| `7D` | `4.69` | 16,680,000.00 USD | 16,680,000.00 USD | 0.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 20,180,000.00 USD | 20,180,000.00 USD | 0.00 USD | 69,690.00 USD | 97,490.00 USD | 175,300.00 USD |
| `7D` | `4.70` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD |
| `1D` | `4.71` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 390,710.00 USD | 298,900.00 USD | 353,560.00 USD |
| `7D` | `4.71` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD |
| `1D` | `4.72` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 2,370.00 USD | 181,280.00 USD | 49,910.00 USD |
| `7D` | `4.72` | 17,690,000.00 USD | 17,690,000.00 USD | 0.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 21,630,000.00 USD | 21,630,000.00 USD | 0.00 USD | 110,530.00 USD | 25,210.00 USD | 35,700.00 USD |
| `7D` | `4.73` | 17,760,000.00 USD | 17,760,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD |
| `1D` | `4.74` | 22,020,000.00 USD | 22,020,000.00 USD | 0.00 USD | 68,200.00 USD | 141,320.00 USD | 176,280.00 USD |
| `7D` | `4.74` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD |
| `1D` | `4.75` | 22,430,000.00 USD | 22,430,000.00 USD | 0.00 USD | 100,320.00 USD | 141,340.00 USD | 171,320.00 USD |
| `7D` | `4.75` | 18,700,000.00 USD | 18,700,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `1D` | `4.76` | 22,580,000.00 USD | 22,580,000.00 USD | 0.00 USD | 32,610.00 USD | 56,290.00 USD | 56,880.00 USD |
| `7D` | `4.76` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD |
| `1D` | `4.77` | 22,780,000.00 USD | 22,780,000.00 USD | 0.00 USD | 46,010.00 USD | 85,030.00 USD | 76,340.00 USD |
| `7D` | `4.77` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 22,930,000.00 USD | 22,930,000.00 USD | 0.00 USD | 37,290.00 USD | 20,000.00 USD | 86,970.00 USD |
| `7D` | `4.78` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 23,120,000.00 USD | 23,120,000.00 USD | 0.00 USD | 98,120.00 USD | 39,920.00 USD | 59,070.00 USD |
| `7D` | `4.79` | 23,210,000.00 USD | 23,210,000.00 USD | 0.00 USD | 804,240.00 USD | 249,310.00 USD | 72,220.00 USD |
| `1D` | `4.80` | 23,580,000.00 USD | 23,580,000.00 USD | 0.00 USD | 187,680.00 USD | 133,800.00 USD | 138,860.00 USD |
| `7D` | `4.80` | 24,800,000.00 USD | 24,800,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 0.00 USD | 14,070.00 USD | 457.61 USD |
| `7D` | `4.81` | 25,430,000.00 USD | 25,430,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 23,730,000.00 USD | 23,730,000.00 USD | 0.00 USD | 20,630.00 USD | 78,640.00 USD | 35,260.00 USD |
| `7D` | `4.82` | 28,200,000.00 USD | 28,200,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 23,740,000.00 USD | 23,740,000.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `7D` | `4.83` | 29,850,000.00 USD | 29,850,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 30,340,000.00 USD | 30,340,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
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
  * Total Open Interest: `1.11B` | Total OI Tokens: `255,994,008.8 NEAR`
  * 1h OI Change: `+0.36%` | 4h OI Change: `-0.51%` | 24h OI Change: `-13.88%`
  * Exchange Breakdown: Binance=`199.67M` | Bybit=`147.91M` | OKX=`52.76M` | Hyperliquid=`241.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-126.36K` | Last 24h: `-22.13K` | Last 3d: `231.31K` | Last 7d: `198.53K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0018%` | **USDT OKX** | `-0.0226%` |
| **USDT Bybit** | `-0.0751%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0016%` | **USDT BingX** | `0.0014%` |
| **USDT Gate** | `-0.0025%` | **USDT Bitget** | `-0.0483%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `47.57%` | `52.43%` | `0.91` | 5,170,000.00 USD |
| `15M` | `Binance` | `51.58%` | `48.42%` | `1.07` | 1,760,000.00 USD |
| `15M` | `OKX` | `45.49%` | `54.51%` | `0.83` | 521,780.00 USD |
| `15M` | `Bybit` | `58.22%` | `41.78%` | `1.39` | 221,890.00 USD |
| `15M` | `KuCoin` | `43.69%` | `56.31%` | `0.78` | 15,240.00 USD |
| `15M` | `Gate` | `49.56%` | `50.44%` | `0.98` | 46,560.00 USD |
| `15M` | `Bitget` | `63.4%` | `36.6%` | `1.73` | 244,210.00 USD |
| `15M` | `BingX` | `72.7%` | `27.3%` | `2.66` | 168,810.00 USD |
| `15M` | `MEXC` | `42.33%` | `57.67%` | `0.73` | 1,450,000.00 USD |
| `15M` | `Bitunix` | `19.51%` | `80.49%` | `0.24` | 228,610.00 USD |
| `15M` | `Hyperliquid` | `58.53%` | `41.47%` | `1.41` | 37,040.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.16%` | `51.84%` | `0.93` | 338,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 53,680.00 USD |
| `15M` | `HTX` | `67.95%` | `32.05%` | `2.12` | 738.56 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `30.99%` | `69.01%` | `0.45` | 65,800.00 USD |
| `15M` | `Aster` | `41.57%` | `58.43%` | `0.71` | 10,070.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `96.78%` | `3.22%` | `30.06` | 11,990.00 USD |
| `15M` | `Whale Positions` | `51.58%` | `48.42%` | `1.07` | 1,760,000.00 USD |
| `15M` | `Global Accounts` | `47.57%` | `52.43%` | `0.91` | 5,170,000.00 USD |
| `1H` | `NEAR` | `48.98%` | `51.02%` | `0.96` | 22,520,000.00 USD |
| `1H` | `Binance` | `54.67%` | `45.33%` | `1.21` | 8,030,000.00 USD |
| `1H` | `OKX` | `49.64%` | `50.36%` | `0.99` | 2,180,000.00 USD |
| `1H` | `Bybit` | `56.68%` | `43.32%` | `1.31` | 1,470,000.00 USD |
| `1H` | `KuCoin` | `42.47%` | `57.53%` | `0.74` | 92,110.00 USD |
| `1H` | `Gate` | `38.06%` | `61.94%` | `0.61` | 235,480.00 USD |
| `1H` | `Bitget` | `57.17%` | `42.83%` | `1.33` | 1,030,000.00 USD |
| `1H` | `BingX` | `17.91%` | `82.09%` | `0.22` | 2,070,000.00 USD |
| `1H` | `MEXC` | `50.14%` | `49.86%` | `1.01` | 5,260,000.00 USD |
| `1H` | `Bitunix` | `44.44%` | `55.56%` | `0.80` | 616,950.00 USD |
| `1H` | `Hyperliquid` | `54.57%` | `45.43%` | `1.20` | 228,110.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.23%` | `50.77%` | `0.97` | 840,140.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `2.73%` | `97.27%` | `0.03` | 105,550.00 USD |
| `1H` | `HTX` | `52.29%` | `47.71%` | `1.10` | 2,650.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.19%` | `64.81%` | `0.54` | 245,260.00 USD |
| `1H` | `Aster` | `85.05%` | `14.95%` | `5.69` | 93,440.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `71.63%` | `28.37%` | `2.52` | 28,860.00 USD |
| `1H` | `Whale Positions` | `54.67%` | `45.33%` | `1.21` | 8,030,000.00 USD |
| `1H` | `Global Accounts` | `48.98%` | `51.02%` | `0.96` | 22,520,000.00 USD |
| `4H` | `NEAR` | `46.93%` | `53.07%` | `0.88` | 83,210,000.00 USD |
| `4H` | `Binance` | `49.36%` | `50.64%` | `0.97` | 28,470,000.00 USD |
| `4H` | `OKX` | `47.94%` | `52.06%` | `0.92` | 6,760,000.00 USD |
| `4H` | `Bybit` | `50.09%` | `49.91%` | `1.00` | 5,130,000.00 USD |
| `4H` | `KuCoin` | `49.15%` | `50.85%` | `0.97` | 451,090.00 USD |
| `4H` | `Gate` | `45.68%` | `54.32%` | `0.84` | 2,300,000.00 USD |
| `4H` | `Bitget` | `48.65%` | `51.35%` | `0.95` | 2,670,000.00 USD |
| `4H` | `BingX` | `27.69%` | `72.31%` | `0.38` | 5,090,000.00 USD |
| `4H` | `MEXC` | `49.57%` | `50.43%` | `0.98` | 19,320,000.00 USD |
| `4H` | `Bitunix` | `48.65%` | `51.35%` | `0.95` | 4,170,000.00 USD |
| `4H` | `Hyperliquid` | `42.65%` | `57.35%` | `0.74` | 1,160,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.92%` | `51.08%` | `0.96` | 3,990,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.54%` | `87.46%` | `0.14` | 2,110,000.00 USD |
| `4H` | `HTX` | `42.6%` | `57.4%` | `0.74` | 69,410.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.14%` | `47.86%` | `1.09` | 1,220,000.00 USD |
| `4H` | `Aster` | `81.99%` | `18.01%` | `4.55` | 184,230.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `60.4%` | `39.6%` | `1.53` | 120,160.00 USD |
| `4H` | `Whale Positions` | `49.36%` | `50.64%` | `0.97` | 28,470,000.00 USD |
| `4H` | `Global Accounts` | `46.93%` | `53.07%` | `0.88` | 83,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.31` | `4.35` | `4.31` | `4.39` | `4.31` | 11,576,553.35 USD | 6,334,405.32 USD | 5,242,148.03 USD | 1,092,257.28 USD | `+9.44%` | `19B / 4S` |
| `0:00 UTC` | `4.34` | `4.34` | `4.34` | `4.37` | `4.32` | 8,173,916.95 USD | 4,141,201.50 USD | 4,032,715.45 USD | 108,486.05 USD | `+1.33%` | `4B / 2S` |
| `5:00 UTC` | `4.32` | `4.32` | `4.32` | `4.34` | `4.31` | 8,060,413.67 USD | 4,212,890.12 USD | 3,847,523.55 USD | 365,366.56 USD | `+4.53%` | `0B / 2S` |
| `0:00 UTC` | `4.31` | `4.32` | `4.31` | `4.36` | `4.29` | 5,778,991.37 USD | 2,863,139.85 USD | 2,915,851.52 USD | -52,711.67 USD | `-0.91%` | `7B / 7S` |
| `5:00 UTC` | `4.36` | `4.36` | `4.36` | `4.38` | `4.34` | 6,093,690.79 USD | 3,348,593.15 USD | 2,745,097.64 USD | 603,495.51 USD | `+9.90%` | `4B / 5S` |
| `0:00 UTC` | `4.34` | `4.35` | `4.34` | `4.38` | `4.33` | 6,786,354.30 USD | 2,907,641.85 USD | 3,878,712.45 USD | -971,070.60 USD | `-14.31%` | `2B / 15S` |
| `5:00 UTC` | `4.33` | `4.34` | `4.33` | `4.37` | `4.32` | 6,865,250.12 USD | 3,215,652.73 USD | 3,649,597.39 USD | -433,944.66 USD | `-6.32%` | `2B / 6S` |
| `0:00 UTC` | `4.33` | `4.34` | `4.33` | `4.35` | `4.32` | 7,895,783.86 USD | 4,987,543.57 USD | 2,908,240.29 USD | 2,079,303.28 USD | `+26.33%` | `8B / 3S` |
| `5:00 UTC` | `4.34` | `4.35` | `4.34` | `4.38` | `4.33` | 4,949,414.64 USD | 2,811,646.93 USD | 2,137,767.71 USD | 673,879.22 USD | `+13.62%` | `14B / 1S` |
| `0:00 UTC` | `4.36` | `4.36` | `4.36` | `4.38` | `4.34` | 3,742,673.65 USD | 1,680,707.37 USD | 2,061,966.28 USD | -381,258.91 USD | `-10.19%` | `2B / 5S` |

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
| `5m` | -53,970.00 USD | 82,280.00 USD | **`ACCUMULATION`** |
| `15m` | -347,150.00 USD | -725,410.00 USD | **`DISTRIBUTION`** |
| `30m` | -489,070.00 USD | 901,710.00 USD | **`ACCUMULATION`** |
| `1h` | -467,550.00 USD | 930,800.00 USD | **`ACCUMULATION`** |
| `2h` | -850,840.00 USD | -2,800,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 9,020,000.00 USD | 4,530,000.00 USD | **`ACCUMULATION`** |
| `6h` | 14,520,000.00 USD | -1,140,000.00 USD | **`ACCUMULATION`** |
| `8h` | 19,080,000.00 USD | 15,680,000.00 USD | **`ACCUMULATION`** |
| `12h` | 19,100,000.00 USD | 2,240,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,510,000.00 USD | -29,930,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -58,840,000.00 USD | -132,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -231,070,000.00 USD | -678,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-53.97K` | 15m=`-347.15K` | 1h=`-467.55K` | 24h=`+2.51M`
* Futures Capital Netflows: 5m=`+82.28K` | 15m=`-725.41K` | 1h=`+930.80K` | 24h=`-29.93M`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3.83` (Risk Distance: `0.1097` pts)
  * +2.5R Take Profit: `4.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.36` (Risk Distance: `0.1097` pts)
  * +2.5R Take Profit: `3.97`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
