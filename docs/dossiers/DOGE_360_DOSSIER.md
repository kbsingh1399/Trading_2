# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-29 22:49:00 IST` (`2026-10-29 17:19:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0790` | **Live Ask Quote**: `0.0811` | **Mid Price**: `0.0801`
- **Spread Points**: `21.00` | **Spread BPS**: `262.34 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0777` | VWAP Z-Score: `+1.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000467` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.72` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0804` | Lower -3.00σ Band: `0.0749`
  * Upper +2.51σ Band: `0.0800` | Lower -2.51σ Band: `0.0754`
  * Upper +2.01σ Band: `0.0795` | Lower -2.01σ Band: `0.0758`
  * Upper +2.00σ Band: `0.0795` | Lower -2.00σ Band: `0.0758`
  * Upper +1.28σ Band: `0.0788` | Lower -1.28σ Band: `0.0765`
  * Upper +1.00σ Band: `0.0786` | Lower -1.00σ Band: `0.0767`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0790` | EMA-20=`0.0786` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0780` (Slope: `+0.0000`) | EMA-100=`0.0779`
  * Institutional Anchors: EMA-144=`0.0778` | EMA-200=`0.0776` (Slope: `+0.2237`) | EMA-233=`0.0775`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0763` | Weekly High=`0.0803` | Weekly Low=`0.0755`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0786` (Distance: `+1.80%`)
  * Point of Control (POC) = `0.0767` (Distance: `+4.39%`)
  * Value Area Low (VAL) = `0.0764` (Distance: `+4.79%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0789` | POC=`0.0786` | VAL=`0.0776`
  * Prior Day Extremes: PDH=`0.0798` | PDL=`0.0768` | PDC=`0.0791`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0781` | Weekly POC=`0.0761` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0794` | Low=`0.0763`
  * London Session (08:00-16:00 UTC): High=`0.0779` | Low=`0.0765`
  * New York Session (13:00-21:00 UTC): High=`0.0803` | Low=`0.0768`
  * Initial Balance (First Hour): IB High=`0.0779` | IB Low=`0.0772`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0797` - `0.0804`
  * Optimal Trade Entry (OTE 0.705): `0.0802`
  * Structural Invalidation Anchor (0.786): `0.0807`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0801` | `0.0802` | `0.0800` | `0.0801` | `13,753,905` | 1,101,212.60 USD | 112,766.15 USD | `+10.24%` | -4,526,941.74 USD | `+0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0801` | `0.0801` | `0.0799` | `0.0800` | `22,044,550` | 1,763,551.92 USD | -331,527.60 USD | `-18.80%` | -4,858,469.33 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0800` | `0.0801` | `0.0800` | `0.0801` | `14,294,991` | 1,144,547.06 USD | -196,570.82 USD | `-17.17%` | -5,055,040.15 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0803` | `0.0804` | `0.0799` | `0.0802` | `96,105,962` | 7,702,082.98 USD | -1,715,083.61 USD | `-22.27%` | -4,840,538.57 USD | `-2.63` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0802` | `0.0802` | `0.0799` | `0.0801` | `43,881,208` | 3,513,799.11 USD | 200,830.68 USD | `+5.72%` | -4,639,707.89 USD | `+0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0801` | `0.0802` | `0.0799` | `0.0801` | `50,093,446` | 4,009,311.58 USD | -415,332.26 USD | `-10.36%` | -5,055,040.15 USD | `-0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0799` | `0.0807` | `0.0797` | `0.0806` | `308,847,265` | 24,764,184.89 USD | 1,508,150.52 USD | `+6.09%` | -4,845,295.11 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0806` | `0.0815` | `0.0799` | `0.0801` | `488,172,743` | 39,342,413.57 USD | -1,193,889.47 USD | `-3.03%` | -6,039,184.58 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0801` | `0.0802` | `0.0799` | `0.0801` | `50,093,446` | 4,009,311.58 USD | -415,332.26 USD | `-10.36%` | -6,454,516.85 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0799` | `0.0801` | `538,083,949` | 43,337,121.08 USD | -1,623,502.05 USD | `-3.75%` | -7,477,958.40 USD | `-0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0797` | `0.0799` | `0.0774` | `0.0778` | `998,970,852` | 78,232,937.14 USD | -7,024,064.25 USD | `-8.98%` | -3,060,763.89 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -7,420,203.26 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0799` | `0.0801` | `538,083,949` | 43,337,121.08 USD | -1,623,502.05 USD | `-3.75%` | -7,477,958.40 USD | `-0.09` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.0801`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0801` | `18714.0000` | 1,499.93 USD | 133,341.30 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0801` | `174034.0000` | 13,948.48 USD | 131,841.37 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0801` | `14991.0000` | 1,201.48 USD | 117,892.89 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0801` | `10000.0000` | 801.46 USD | 116,691.41 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0801` | `11053.0000` | 885.84 USD | 115,889.95 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0801` | `938.0000` | 75.18 USD | 115,004.11 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0801` | `11053.0000` | 885.82 USD | 114,928.93 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0801` | `188779.0000` | 15,128.37 USD | 114,043.11 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0801` | `3507.0000` | 281.04 USD | 98,914.74 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0801` | `256372.0000` | 20,542.58 USD | 98,633.70 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `0.0801` | `303277.0000` | 24,300.68 USD | 78,091.12 USD | `15 orders` | `+0.01%` | `-` |
| `ASK` | `0.0801` | `156800.0000` | 12,563.76 USD | 53,790.45 USD | `14 orders` | `+0.01%` | `-` |
| `ASK` | `0.0801` | `161792.0000` | 12,963.58 USD | 41,226.69 USD | `15 orders` | `+0.00%` | `-` |
| `ASK` | `0.0801` | `156800.0000` | 12,563.44 USD | 28,263.11 USD | `14 orders` | `+0.00%` | `-` |
| `ASK` | `0.0801` | `156800.0000` | 12,563.29 USD | 15,699.66 USD | `14 orders` | `+0.00%` | `-` |
| `ASK` | `0.0801` | `39145.0000` | 3,136.38 USD | 3,136.38 USD | `3 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0801` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0801` | `37704.0000` | 3,020.88 USD | 3,020.88 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.0801` | `4922.0000` | 394.35 USD | 3,415.23 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.0801` | `19162.0000` | 1,535.09 USD | 4,950.32 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0801` | `4993.0000` | 399.98 USD | 5,350.30 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0801` | `127515.0000` | 10,214.97 USD | 15,565.28 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0801` | `35348.0000` | 2,831.59 USD | 18,396.86 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0801` | `3611.0000` | 289.25 USD | 18,686.11 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0801` | `69710.0000` | 5,583.91 USD | 24,270.02 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0801` | `4994.0000` | 400.01 USD | 24,670.04 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0801` | `54849.0000` | 4,393.30 USD | 29,063.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0801` | `97809.0000` | 7,834.11 USD | 36,897.44 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0801` | `127540.0000` | 10,214.93 USD | 47,112.38 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0801` | `32603.0000` | 2,611.14 USD | 49,723.52 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `0.0801` | `87404.0000` | 6,999.92 USD | 56,723.44 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0801` | `11040.0000` | 884.15 USD | 57,607.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0801` | `4995.0000` | 400.01 USD | 58,007.60 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0801` | `101208.0000` | 8,104.84 USD | 66,112.44 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0801` | `38275.0000` | 3,065.06 USD | 69,177.50 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `0.0801` | `315943.0000` | 25,300.40 USD | 94,477.90 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0801` | `236099.0000` | 18,905.86 USD | 113,383.77 USD | `2 orders` | `-0.06%` | `-` |
| `ASK` | `0.0802` | `39764.0000` | 3,187.24 USD | 149,835.21 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0802` | `106775.0000` | 8,558.34 USD | 146,647.96 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0802` | `24188.0000` | 1,938.72 USD | 138,089.63 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0802` | `35054.0000` | 2,809.61 USD | 136,150.91 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `305` | `0xb83d...6e36` | `SHORT` | 8,205,002.01 USD | `102,645,925.00` | `0.0946` | `0.0800` | `1.26` | 1,502,339.64 USD | `+18.31%` | `3X Cross` |
| `316` | `0xc63a...a3cd` | `LONG` | 8,002,500.00 USD | `100,000,000.00` | `0.0856` | `0.0800` | `0.000000` | -562,321.96 USD | `-7.03%` | `10X Cross` |
| `323` | `0x610b...b613` | `LONG` | 7,900,417.90 USD | `98,666,424.00` | `0.0872` | `0.0800` | `0.0575` | -699,764.00 USD | `-8.86%` | `5X Cross` |
| `605` | `0x5b5d...c060` | `SHORT` | 3,958,811.19 USD | `49,478,955.00` | `0.0946` | `0.0800` | `3.00` | 722,705.42 USD | `+18.26%` | `3X Cross` |
| `640` | `0xca49...53c8` | `SHORT` | 3,724,575.49 USD | `46,542,649.00` | `0.0929` | `0.0800` | `0.3419` | 601,469.19 USD | `+16.15%` | `10X Cross` |
| `656` | `0x45d2...4029` | `SHORT` | 3,631,627.00 USD | `45,426,000.00` | `0.0954` | `0.0800` | `0.8191` | 704,002.22 USD | `+19.39%` | `10X Cross` |
| `791` | `0xecb6...2b00` | `SHORT` | 3,010,396.21 USD | `37,618,197.00` | `0.0796` | `0.0800` | `0.9182` | -16,397.32 USD | `-0.54%` | `10X Cross` |
| `1183` | `0x458d...ab3b` | `LONG` | 1,954,490.99 USD | `24,454,063.00` | `0.1002` | `0.0800` | `0.0714` | -496,430.92 USD | `-25.40%` | `3X Isolated` |
| `1187` | `0xeadc...9d55` | `LONG` | 1,944,082.06 USD | `24,317,440.00` | `0.0926` | `0.0800` | `0.000000` | -307,512.52 USD | `-15.82%` | `10X Cross` |
| `1237` | `0x9aa5...58af` | `SHORT` | 1,881,544.03 USD | `23,500,500.00` | `0.0907` | `0.0800` | `0.3785` | 249,210.92 USD | `+13.25%` | `10X Cross` |
| `1339` | `0xf48f...10fe` | `LONG` | 1,712,567.17 USD | `21,424,497.00` | `0.0968` | `0.0800` | `0.0300` | -361,737.44 USD | `-21.12%` | `4X Cross` |
| `1368` | `0x9946...0852` | `SHORT` | 1,671,369.12 USD | `20,910,149.00` | `0.0871` | `0.0800` | `0.1262` | 149,186.27 USD | `+8.93%` | `10X Cross` |
| `1567` | `0xcac1...26b3` | `SHORT` | 1,448,968.56 USD | `18,126,835.00` | `0.0943` | `0.0800` | `0.4912` | 260,490.64 USD | `+17.98%` | `10X Cross` |
| `1608` | `0x0d6a...ca57` | `LONG` | 1,409,940.14 USD | `17,626,455.00` | `0.0875` | `0.0800` | `0.0626` | -132,164.82 USD | `-9.37%` | `3X Isolated` |
| `1659` | `0x4808...a82c` | `LONG` | 1,345,342.72 USD | `16,828,143.00` | `0.0883` | `0.0800` | `0.0631` | -141,130.26 USD | `-10.49%` | `3X Cross` |
| `1783` | `0x31ef...f715` | `LONG` | 1,217,585.73 USD | `15,230,102.00` | `0.0936` | `0.0800` | `0.0668` | -208,110.19 USD | `-17.09%` | `3X Isolated` |
| `1807` | `0xbfc7...80b4` | `SHORT` | 1,200,473.50 USD | `15,020,000.00` | `0.0920` | `0.0800` | `0.3537` | 181,925.79 USD | `+15.15%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0824` | 4,085.89 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 4.09K USD at 0.0824 USD [API] | `2026-10-08 15:23:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0824` | 49.95 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.05K USD at 0.0824 USD [API] | `2026-10-08 15:23:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0824` | 4,642.44 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 4.64K USD at 0.0824 USD [API] | `2026-10-08 15:23:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0784` | 7,000.07 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.00K USD at 0.0784 USD [API] | `2026-10-27 19:40:44` |
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 6,327.23 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 6.33K USD at 0.0783 USD [API] | `2026-10-27 19:53:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0797` (Vol: 489,300.00 USD, Dist: `+0.40%`) | Long MP=`0.0763` (Vol: 497,300.00 USD, Dist: `--3.83%`)
  * 48H Horizon: Short MP=`0.0813` (Vol: 542,300.00 USD, Dist: `+2.42%`) | Long MP=`0.0766` (Vol: 606,900.00 USD, Dist: `--3.49%`)
  * 3D Horizon: Short MP=`0.0813` (Vol: 643,700.00 USD, Dist: `+2.41%`) | Long MP=`0.0762` (Vol: 815,200.00 USD, Dist: `--3.95%`)
  * 7D Horizon: Short MP=`0.0818` (Vol: 832,600.00 USD, Dist: `+3.09%`) | Long MP=`0.0758` (Vol: 890,000.00 USD, Dist: `--4.48%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0181` | 4,050.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0191` | 16,890.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 397.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0202` | 285.63 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0208` | 3,900.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0210` | 658.04 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0211` | 126.67 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0230` | 11,270.00 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 345.98 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0233` | 1,870.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0237` | 473.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0240` | 1,160.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0245` | 131.20 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0250` | 1,900.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0271` | 1,060.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 3,600.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0278` | 126.49 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0285` | 21,410.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0289` | 3,880.00 USD | 15,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0291` | 731.11 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0296` | 1,480.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 2,360.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0302` | 648,090.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0321` | 174.10 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0323` | 146.06 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0328` | 1,560.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0328` | 67,890.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 33,750.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 3,060.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0341` | 924.13 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 5,140.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0353` | 909.52 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0357` | 191.23 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 18,430.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 1,860.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0374` | 3,780.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 2,570.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 98,260.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0384` | 1,110.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 236.87 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0394` | 3,380.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0410` | 395.70 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 61,470.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,070.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,010.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 279.18 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 6,430.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,720.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0442` | 239.69 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 1,950.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 6,780.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 8,460.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 323.89 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,010.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 47,600.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 15,570.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,800.00 USD | 14,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 14,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 310.82 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 311.56 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 635.71 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 287.06 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,330.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 2,900.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 726.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 5,200.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 647.44 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,690.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,770.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 314,750.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 20,280.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 87,240.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 22,670.00 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 237.95 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 2,510.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 175.44 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 679.36 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 38,870.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 1,820.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 48,170.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 1,910.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 380.01 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 1,430.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 3,630.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 421.03 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 644.99 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 5,670,000.00 USD | 13,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,590.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 5,170.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,660.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,830.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 5,320.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 380.38 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 548.46 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,970.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0611` | 73,370.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 665.54 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,400.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 13,460.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 30,490.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 33,240.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 3,470.00 USD | 7,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 168.28 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 1,320.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 1,450.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 8,670.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 43,440.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,360.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,050.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 6,350.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 86,870.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 9,910.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 22,520.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 71,100.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0660` | 339.83 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 339.48 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,600.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 66,550.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 778.51 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 389.18 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 94,360.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 196.64 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,580.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 80,080.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 5,400.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 23,050.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0682` | 1,680.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 4,690.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 1,620.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 69,020.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 517.48 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 3,670.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 50,720.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,160.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,840.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0695` | 60,410,000.00 USD | 60,410,000.00 USD | 275,490.00 USD | 222,260.00 USD | 212,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0696` | 14,930.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 59,700,000.00 USD | 59,700,000.00 USD | 100,230.00 USD | 61,080.00 USD | 187,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0697` | 59,350,000.00 USD | 59,350,000.00 USD | 41,960.00 USD | 87,540.00 USD | 77,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 4,800.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0698` | 59,140,000.00 USD | 59,140,000.00 USD | 127,350.00 USD | 103,870.00 USD | 70,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,250.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0699` | 58,840,000.00 USD | 58,840,000.00 USD | 172,730.00 USD | 101,580.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0700` | 58,500,000.00 USD | 58,500,000.00 USD | 87,550.00 USD | 110,810.00 USD | 85,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0701` | 58,220,000.00 USD | 58,220,000.00 USD | 115,700.00 USD | 8,980.00 USD | 55,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0702` | 58,040,000.00 USD | 58,040,000.00 USD | 100,200.00 USD | 38,000.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 791.79 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0703` | 57,850,000.00 USD | 57,850,000.00 USD | 85,670.00 USD | 23,160.00 USD | 747.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0704` | 57,740,000.00 USD | 57,740,000.00 USD | 91,490.00 USD | 55,790.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 2,510.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0705` | 57,570,000.00 USD | 57,570,000.00 USD | 81,490.00 USD | 84,030.00 USD | 59,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0706` | 93,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0706` | 57,350,000.00 USD | 57,350,000.00 USD | 15,880.00 USD | 20,950.00 USD | 45,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0707` | 57,270,000.00 USD | 57,270,000.00 USD | 168,600.00 USD | 48,670.00 USD | 98,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0708` | 56,950,000.00 USD | 56,950,000.00 USD | 10,780.00 USD | 30,220.00 USD | 342.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0709` | 56,910,000.00 USD | 56,910,000.00 USD | 44,800.00 USD | 68,720.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 56,760,000.00 USD | 56,760,000.00 USD | 189,250.00 USD | 50,450.00 USD | 61,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0711` | 56,460,000.00 USD | 56,460,000.00 USD | 138,080.00 USD | 106,700.00 USD | 38,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 56,180,000.00 USD | 56,180,000.00 USD | 109,400.00 USD | 41,030.00 USD | 952.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0713` | 56,030,000.00 USD | 56,030,000.00 USD | 120,050.00 USD | 68,300.00 USD | 59,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0714` | 55,780,000.00 USD | 55,780,000.00 USD | 115,970.00 USD | 74,740.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 757,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0715` | 55,530,000.00 USD | 55,530,000.00 USD | 129,130.00 USD | 0.00 USD | 31,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 755,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0716` | 55,370,000.00 USD | 55,370,000.00 USD | 186,200.00 USD | 42,190.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 560.88 USD | 747,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 24,510,000.00 USD | 24,510,000.00 USD | 80,570.00 USD | 27,450.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0717` | 55,100,000.00 USD | 55,100,000.00 USD | 153,600.00 USD | 1,810.00 USD | 50,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 746,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 24,360,000.00 USD | 24,360,000.00 USD | 63,040.00 USD | 40,570.00 USD | 50,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 54,900,000.00 USD | 54,900,000.00 USD | 64,100.00 USD | 39,280.00 USD | 48,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 744,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 24,200,000.00 USD | 24,200,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0719` | 54,750,000.00 USD | 54,750,000.00 USD | 162,420.00 USD | 51,730.00 USD | 51,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 734,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 24,170,000.00 USD | 24,170,000.00 USD | 48,000.00 USD | 1,230.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 54,480,000.00 USD | 54,480,000.00 USD | 115,550.00 USD | 72,080.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 733,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 24,090,000.00 USD | 24,090,000.00 USD | 33,000.00 USD | 10,770.00 USD | 146.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0721` | 54,240,000.00 USD | 54,240,000.00 USD | 91,320.00 USD | 58,090.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0722` | 24,040,000.00 USD | 24,040,000.00 USD | 29,680.00 USD | 15,630.00 USD | 28,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 54,060,000.00 USD | 54,060,000.00 USD | 76,700.00 USD | 4,070.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 10,450.00 USD | 709,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 23,970,000.00 USD | 23,970,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0723` | 53,940,000.00 USD | 53,940,000.00 USD | 154,040.00 USD | 7,890.00 USD | 45,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 163.73 USD | 699,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 23,860,000.00 USD | 23,860,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 53,740,000.00 USD | 53,740,000.00 USD | 133,990.00 USD | 7,390.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 598.51 USD | 698,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 23,720,000.00 USD | 23,720,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0725` | 53,550,000.00 USD | 53,550,000.00 USD | 177,800.00 USD | 33,630.00 USD | 651.74 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 698,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 23,570,000.00 USD | 23,570,000.00 USD | 31,660.00 USD | 0.00 USD | 317.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 53,330,000.00 USD | 53,330,000.00 USD | 99,500.00 USD | 82,410.00 USD | 64,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 697,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 23,540,000.00 USD | 23,540,000.00 USD | 20,420.00 USD | 0.00 USD | 285.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0727` | 53,090,000.00 USD | 53,090,000.00 USD | 139,640.00 USD | 0.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 452.21 USD | 697,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 23,520,000.00 USD | 23,520,000.00 USD | 15,580.00 USD | 802.30 USD | 261.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 52,950,000.00 USD | 52,950,000.00 USD | 49,930.00 USD | 89,490.00 USD | 139,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 1,230.00 USD | 696,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 23,500,000.00 USD | 23,500,000.00 USD | 17,820.00 USD | 0.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0729` | 52,670,000.00 USD | 52,670,000.00 USD | 88,690.00 USD | 55,500.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 23,460,000.00 USD | 23,460,000.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 52,520,000.00 USD | 52,520,000.00 USD | 105,630.00 USD | 11,900.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 622,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 23,450,000.00 USD | 23,450,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0731` | 52,400,000.00 USD | 52,400,000.00 USD | 176,670.00 USD | 203,190.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 612,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 23,400,000.00 USD | 23,400,000.00 USD | 42,110.00 USD | 0.00 USD | 86.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 51,960,000.00 USD | 51,960,000.00 USD | 620,130.00 USD | 453,660.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 610,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 23,360,000.00 USD | 23,360,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0733` | 50,860,000.00 USD | 50,860,000.00 USD | 289,650.00 USD | 18,570.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 23,350,000.00 USD | 23,350,000.00 USD | 6,120.00 USD | 0.00 USD | 301.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 50,510,000.00 USD | 50,510,000.00 USD | 342,630.00 USD | 172,240.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 604,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 23,340,000.00 USD | 23,340,000.00 USD | 25,370.00 USD | 0.00 USD | 336.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0735` | 49,970,000.00 USD | 49,970,000.00 USD | 252,620.00 USD | 244,020.00 USD | 137,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 597,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 23,320,000.00 USD | 23,320,000.00 USD | 9,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 49,340,000.00 USD | 49,340,000.00 USD | 392,100.00 USD | 244,990.00 USD | 229,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 593,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 23,310,000.00 USD | 23,310,000.00 USD | 47,420.00 USD | 0.00 USD | 625.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0737` | 48,470,000.00 USD | 48,470,000.00 USD | 340,530.00 USD | 126,240.00 USD | 172,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 588,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 23,260,000.00 USD | 23,260,000.00 USD | 39,420.00 USD | 0.00 USD | 604.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 47,830,000.00 USD | 47,830,000.00 USD | 390,250.00 USD | 258,710.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,630.00 USD | 577,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 23,220,000.00 USD | 23,220,000.00 USD | 37,380.00 USD | 0.00 USD | 98.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0739` | 47,040,000.00 USD | 47,040,000.00 USD | 523,610.00 USD | 388,780.00 USD | 147,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,570.00 USD | 572,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 23,180,000.00 USD | 23,180,000.00 USD | 29,230.00 USD | 0.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 45,980,000.00 USD | 45,980,000.00 USD | 631,590.00 USD | 498,260.00 USD | 422,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,080.00 USD | 558,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 23,150,000.00 USD | 23,150,000.00 USD | 37,860.00 USD | 0.00 USD | 856.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0741` | 44,430,000.00 USD | 44,430,000.00 USD | 401,620.00 USD | 636,410.00 USD | 454,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 5,960.00 USD | 103,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 23,110,000.00 USD | 23,110,000.00 USD | 35,050.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 42,940,000.00 USD | 42,940,000.00 USD | 614,090.00 USD | 186,930.00 USD | 485,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 97,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 23,080,000.00 USD | 23,080,000.00 USD | 37,380.00 USD | 27,500.00 USD | 269.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0743` | 41,650,000.00 USD | 41,650,000.00 USD | 226,940.00 USD | 547,750.00 USD | 528,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 3,870.00 USD | 96,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 23,010,000.00 USD | 23,010,000.00 USD | 41,590.00 USD | 1,840.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 40,350,000.00 USD | 40,350,000.00 USD | 293,650.00 USD | 339,640.00 USD | 134,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 311.95 USD | 92,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 22,950,000.00 USD | 22,950,000.00 USD | 103,370.00 USD | 57,220.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0745` | 39,580,000.00 USD | 39,580,000.00 USD | 475,750.00 USD | 324,390.00 USD | 205,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 780.39 USD | 92,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 22,770,000.00 USD | 22,770,000.00 USD | 237,520.00 USD | 175,410.00 USD | 125,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 38,580,000.00 USD | 38,580,000.00 USD | 726,840.00 USD | 775,280.00 USD | 367,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 91,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0747` | 22,230,000.00 USD | 22,230,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0747` | 36,710,000.00 USD | 36,710,000.00 USD | 700,250.00 USD | 785,240.00 USD | 292,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 90,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 21,770,000.00 USD | 21,770,000.00 USD | 171,870.00 USD | 65,720.00 USD | 99,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 34,930,000.00 USD | 34,930,000.00 USD | 790,190.00 USD | 324,980.00 USD | 184,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 21,440,000.00 USD | 21,440,000.00 USD | 195,850.00 USD | 144,960.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0749` | 33,630,000.00 USD | 33,630,000.00 USD | 565,400.00 USD | 124,000.00 USD | 136,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 1,370.00 USD | 89,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 21,090,000.00 USD | 21,090,000.00 USD | 235,680.00 USD | 83,730.00 USD | 121,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 32,800,000.00 USD | 32,800,000.00 USD | 594,740.00 USD | 328,340.00 USD | 87,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 451.13 USD | 88,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0751` | 20,650,000.00 USD | 20,650,000.00 USD | 277,260.00 USD | 82,120.00 USD | 66,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0751` | 31,790,000.00 USD | 31,790,000.00 USD | 711,020.00 USD | 471,800.00 USD | 102,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 14,540.00 USD | 88,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 20,220,000.00 USD | 20,220,000.00 USD | 124,190.00 USD | 19,450.00 USD | 85,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 30,510,000.00 USD | 30,510,000.00 USD | 781,620.00 USD | 613,570.00 USD | 642,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 3,910.00 USD | 73,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0753` | 19,990,000.00 USD | 19,990,000.00 USD | 127,320.00 USD | 72,710.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0753` | 28,470,000.00 USD | 28,470,000.00 USD | 513,580.00 USD | 354,150.00 USD | 394,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0754` | 617.57 USD | 69,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0754` | 19,760,000.00 USD | 19,760,000.00 USD | 95,400.00 USD | 62,330.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 27,210,000.00 USD | 27,210,000.00 USD | 306,180.00 USD | 610,950.00 USD | 339,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 69,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0755` | 19,580,000.00 USD | 19,580,000.00 USD | 122,130.00 USD | 15,650.00 USD | 69,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0755` | 25,950,000.00 USD | 25,950,000.00 USD | 670,760.00 USD | 794,430.00 USD | 392,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 19,380,000.00 USD | 19,380,000.00 USD | 180,500.00 USD | 157,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 24,090,000.00 USD | 24,090,000.00 USD | 901,040.00 USD | 1,260,000.00 USD | 876,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 356.24 USD | 64,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0757` | 18,920,000.00 USD | 18,920,000.00 USD | 152,450.00 USD | 44,790.00 USD | 104,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0757` | 21,060,000.00 USD | 21,060,000.00 USD | 764,320.00 USD | 1,040,000.00 USD | 628,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0757` | 3,270.00 USD | 64,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0758` | 18,620,000.00 USD | 18,620,000.00 USD | 74,730.00 USD | 42,980.00 USD | 31,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 18,620,000.00 USD | 18,620,000.00 USD | 675,880.00 USD | 568,850.00 USD | 910,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,540.00 USD | 61,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0759` | 18,470,000.00 USD | 18,470,000.00 USD | 116,240.00 USD | 85,920.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0759` | 16,470,000.00 USD | 16,470,000.00 USD | 504,200.00 USD | 819,420.00 USD | 304,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,320.00 USD | 55,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 18,260,000.00 USD | 18,260,000.00 USD | 285,080.00 USD | 289,180.00 USD | 215,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 14,840,000.00 USD | 14,840,000.00 USD | 980,060.00 USD | 846,650.00 USD | 632,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,690.00 USD | 23,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0761` | 17,470,000.00 USD | 17,470,000.00 USD | 477,110.00 USD | 391,680.00 USD | 272,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0761` | 12,380,000.00 USD | 12,380,000.00 USD | 886,790.00 USD | 569,460.00 USD | 472,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,130.00 USD | 21,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 16,330,000.00 USD | 16,330,000.00 USD | 510,560.00 USD | 248,230.00 USD | 177,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 10,450,000.00 USD | 10,450,000.00 USD | 309,500.00 USD | 473,290.00 USD | 312,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 5,710.00 USD | 20,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0763` | 15,390,000.00 USD | 15,390,000.00 USD | 360,900.00 USD | 139,670.00 USD | 198,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0763` | 9,350,000.00 USD | 9,350,000.00 USD | 639,910.00 USD | 247,960.00 USD | 102,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0764` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0764` | 14,700,000.00 USD | 14,700,000.00 USD | 396,130.00 USD | 346,900.00 USD | 91,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 8,360,000.00 USD | 8,360,000.00 USD | 796,120.00 USD | 232,730.00 USD | 166,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0765` | 9,890.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0765` | 13,860,000.00 USD | 13,860,000.00 USD | 551,690.00 USD | 223,110.00 USD | 314,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0765` | 7,170,000.00 USD | 7,170,000.00 USD | 554,010.00 USD | 105,240.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0766` | 12,770,000.00 USD | 12,770,000.00 USD | 619,080.00 USD | 272,640.00 USD | 279,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 6,320,000.00 USD | 6,320,000.00 USD | 389,230.00 USD | 407,670.00 USD | 188,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0767` | 11,600,000.00 USD | 11,600,000.00 USD | 238,180.00 USD | 103,410.00 USD | 214,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0767` | 5,340,000.00 USD | 5,340,000.00 USD | 575,100.00 USD | 232,660.00 USD | 330,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0768` | 11,040,000.00 USD | 11,040,000.00 USD | 380,970.00 USD | 173,700.00 USD | 141,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 4,200,000.00 USD | 4,200,000.00 USD | 146,960.00 USD | 67,680.00 USD | 124,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0769` | 242.54 USD | 5,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0769` | 10,350,000.00 USD | 10,350,000.00 USD | 227,680.00 USD | 170,840.00 USD | 38,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0769` | 3,860,000.00 USD | 3,860,000.00 USD | 133,640.00 USD | 100,180.00 USD | 177,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0770` | 330.81 USD | 4,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0770` | 9,910,000.00 USD | 9,910,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 3,450,000.00 USD | 3,450,000.00 USD | 177,520.00 USD | 80,840.00 USD | 292,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0770` | 109.41 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0771` | 9,250,000.00 USD | 9,250,000.00 USD | 231,550.00 USD | 266,030.00 USD | 189,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0771` | 2,900,000.00 USD | 2,900,000.00 USD | 80,530.00 USD | 229,090.00 USD | 107,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0772` | 8,560,000.00 USD | 8,560,000.00 USD | 169,730.00 USD | 318,140.00 USD | 333,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 2,480,000.00 USD | 2,480,000.00 USD | 176,460.00 USD | 444,720.00 USD | 171,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0773` | 7,740,000.00 USD | 7,740,000.00 USD | 394,320.00 USD | 151,140.00 USD | 241,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0773` | 1,690,000.00 USD | 1,690,000.00 USD | 810,310.00 USD | 335,090.00 USD | 281,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0774` | 6,960,000.00 USD | 6,960,000.00 USD | 165,350.00 USD | 98,170.00 USD | 108,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 260,170.00 USD | 260,170.00 USD | 51,030.00 USD | 36,700.00 USD | 133,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0775` | 6,580,000.00 USD | 6,580,000.00 USD | 181,290.00 USD | 12,820.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0775` | 39,430.00 USD | 39,430.00 USD | 0.00 USD | 23,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0776` | 6,370,000.00 USD | 6,370,000.00 USD | 106,410.00 USD | 237,880.00 USD | 232,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0777` | 5,800,000.00 USD | 5,800,000.00 USD | 18,430.00 USD | 56,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0778` | 5,720,000.00 USD | 5,720,000.00 USD | 6,440.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0780` | 5,650,000.00 USD | 5,650,000.00 USD | 138,400.00 USD | 30,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0781` | 5,480,000.00 USD | 5,480,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0781` | 16,040.00 USD | 16,040.00 USD | 0.00 USD | 16,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0782` | 5,430,000.00 USD | 5,430,000.00 USD | 44,780.00 USD | 71,230.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0782` | 18,880.00 USD | 18,880.00 USD | 0.00 USD | 17,660.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0782` | 37,750.00 USD | 37,750.00 USD | 0.00 USD | 17,660.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0783` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0783` | 44,400.00 USD | 44,400.00 USD | 0.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0784` | 4,390.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0784` | 5,180,000.00 USD | 5,180,000.00 USD | 175,750.00 USD | 6,130.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0784` | 144,040.00 USD | 144,040.00 USD | 0.00 USD | 99,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0785` | 4,840,000.00 USD | 4,840,000.00 USD | 168,930.00 USD | 66,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0785` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0786` | 4,600,000.00 USD | 4,600,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0786` | 1,410,000.00 USD | 1,410,000.00 USD | 91,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0787` | 4,080,000.00 USD | 4,080,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0787` | 2,530,000.00 USD | 2,530,000.00 USD | 1,000,000.00 USD | 122,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0788` | 3,490,000.00 USD | 3,490,000.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0788` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 115,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0789` | 3,070,000.00 USD | 3,070,000.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0790` | 2,830,000.00 USD | 2,830,000.00 USD | 200,610.00 USD | 137,240.00 USD | 50,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0790` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0791` | 2,450,000.00 USD | 2,450,000.00 USD | 76,010.00 USD | 3,690.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0791` | 2,840,000.00 USD | 2,840,000.00 USD | 50,940.00 USD | 91,430.00 USD | 47,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0792` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0792` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 73,810.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0793` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 33,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0793` | 3,940,000.00 USD | 3,940,000.00 USD | 467,940.00 USD | 277,070.00 USD | 241,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0794` | 2,270,000.00 USD | 2,270,000.00 USD | 466,850.00 USD | 243,180.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0794` | 4,380,000.00 USD | 4,380,000.00 USD | 195,640.00 USD | 175,880.00 USD | 75,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0795` | 1,470,000.00 USD | 1,470,000.00 USD | 260,570.00 USD | 131,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0795` | 4,730,000.00 USD | 4,730,000.00 USD | 164,240.00 USD | 130,050.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0796` | 1,080,000.00 USD | 1,080,000.00 USD | 117,990.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 5,250,000.00 USD | 5,250,000.00 USD | 334,830.00 USD | 108,640.00 USD | 75,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0797` | 942,710.00 USD | 942,710.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0797` | 5,630,000.00 USD | 5,630,000.00 USD | 284,990.00 USD | 46,270.00 USD | 43,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0798` | 544,430.00 USD | 544,430.00 USD | 0.00 USD | 164,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 6,080,000.00 USD | 6,080,000.00 USD | 315,270.00 USD | 90,910.00 USD | 46,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0799` | 380,190.00 USD | 380,190.00 USD | 169,980.00 USD | 38,900.00 USD | 171,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0799` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 75,020.00 USD | 202,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 145,420.00 USD | 145,420.00 USD | 0.00 USD | 145,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 290,840.00 USD | 290,840.00 USD | 0.00 USD | 145,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0800` | 6,800,000.00 USD | 6,800,000.00 USD | 53,640.00 USD | 0.00 USD | 386,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0802` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 8,180.00 USD | 102,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0803` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 29,400.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 301,750.00 USD | 301,750.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 7,140,000.00 USD | 7,140,000.00 USD | 95,670.00 USD | 98,500.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0805` | 7,290,000.00 USD | 7,290,000.00 USD | 132,140.00 USD | 11,950.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 305,270.00 USD | 305,270.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 7,600,000.00 USD | 7,600,000.00 USD | 114,280.00 USD | 171,680.00 USD | 28,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 416,290.00 USD | 416,290.00 USD | 0.00 USD | 70,050.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0807` | 9,600,000.00 USD | 9,600,000.00 USD | 897,170.00 USD | 778,530.00 USD | 325,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 1,350,000.00 USD | 1,350,000.00 USD | 503,640.00 USD | 26,410.00 USD | 400,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 12,110,000.00 USD | 12,110,000.00 USD | 1,120,000.00 USD | 813,630.00 USD | 575,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 1,950,000.00 USD | 1,950,000.00 USD | 405,610.00 USD | 193,380.00 USD | 81.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0809` | 14,360,000.00 USD | 14,360,000.00 USD | 826,560.00 USD | 917,760.00 USD | 500,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 2,160,000.00 USD | 2,160,000.00 USD | 150,810.00 USD | 60,350.00 USD | 475.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 16,000,000.00 USD | 16,000,000.00 USD | 977,340.00 USD | 266,420.00 USD | 399,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 161,440.00 USD | 233.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0811` | 17,370,000.00 USD | 17,370,000.00 USD | 602,750.00 USD | 351,410.00 USD | 417,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 2,620,000.00 USD | 2,620,000.00 USD | 14,540.00 USD | 19,910.00 USD | 270,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 18,970,000.00 USD | 18,970,000.00 USD | 1,200,000.00 USD | 200,500.00 USD | 191,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 2,880,000.00 USD | 2,880,000.00 USD | 27,080.00 USD | 18,240.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0813` | 20,490,000.00 USD | 20,490,000.00 USD | 780,410.00 USD | 335,050.00 USD | 406,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 3,300,000.00 USD | 3,300,000.00 USD | 22,430.00 USD | 13,790.00 USD | 386,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 21,850,000.00 USD | 21,850,000.00 USD | 317,750.00 USD | 557,910.00 USD | 481,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 3,860,000.00 USD | 3,860,000.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0815` | 23,300,000.00 USD | 23,300,000.00 USD | 672,460.00 USD | 340,150.00 USD | 439,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 4,520,000.00 USD | 4,520,000.00 USD | 351,830.00 USD | 118,890.00 USD | 189,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 24,830,000.00 USD | 24,830,000.00 USD | 824,560.00 USD | 543,650.00 USD | 169,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 5,060,000.00 USD | 5,060,000.00 USD | 361,650.00 USD | 108,010.00 USD | 68,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0817` | 26,750,000.00 USD | 26,750,000.00 USD | 1,000,000.00 USD | 529,040.00 USD | 381,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 5,850,000.00 USD | 5,850,000.00 USD | 301,490.00 USD | 161,880.00 USD | 322,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 27,670,000.00 USD | 27,670,000.00 USD | 413,640.00 USD | 321,200.00 USD | 188,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 6,540,000.00 USD | 6,540,000.00 USD | 171,350.00 USD | 368,950.00 USD | 156,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0819` | 28,580,000.00 USD | 28,580,000.00 USD | 431,190.00 USD | 214,760.00 USD | 258,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 7,550,000.00 USD | 7,550,000.00 USD | 216,710.00 USD | 285,850.00 USD | 499,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 29,830,000.00 USD | 29,830,000.00 USD | 389,040.00 USD | 467,190.00 USD | 392,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 8,330,000.00 USD | 8,330,000.00 USD | 446,510.00 USD | 167,900.00 USD | 170,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0821` | 31,300,000.00 USD | 31,300,000.00 USD | 985,600.00 USD | 315,920.00 USD | 168,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 8,920,000.00 USD | 8,920,000.00 USD | 268,440.00 USD | 195,730.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 32,020,000.00 USD | 32,020,000.00 USD | 321,980.00 USD | 282,340.00 USD | 114,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0823` | 121.40 USD | 4,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0823` | 9,150,000.00 USD | 9,150,000.00 USD | 185,080.00 USD | 30,920.00 USD | 9,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0823` | 32,670,000.00 USD | 32,670,000.00 USD | 346,280.00 USD | 238,960.00 USD | 70,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 9,690,000.00 USD | 9,690,000.00 USD | 198,500.00 USD | 202,010.00 USD | 137,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 33,540,000.00 USD | 33,540,000.00 USD | 471,470.00 USD | 226,290.00 USD | 169,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 12,660.00 USD | 17,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0825` | 9,860,000.00 USD | 9,860,000.00 USD | 101,400.00 USD | 44,860.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0825` | 34,280,000.00 USD | 34,280,000.00 USD | 317,900.00 USD | 268,580.00 USD | 153,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 10,040,000.00 USD | 10,040,000.00 USD | 35,890.00 USD | 5,050.00 USD | 144,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 34,790,000.00 USD | 34,790,000.00 USD | 330,240.00 USD | 73,020.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 10,160,000.00 USD | 10,160,000.00 USD | 110,260.00 USD | 8,240.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0827` | 35,300,000.00 USD | 35,300,000.00 USD | 253,490.00 USD | 104,450.00 USD | 144,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 10,560,000.00 USD | 10,560,000.00 USD | 265,750.00 USD | 56,990.00 USD | 74,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 35,920,000.00 USD | 35,920,000.00 USD | 496,290.00 USD | 59,010.00 USD | 71,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 10,980,000.00 USD | 10,980,000.00 USD | 260,740.00 USD | 88,990.00 USD | 72,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0829` | 36,440,000.00 USD | 36,440,000.00 USD | 294,720.00 USD | 58,970.00 USD | 162,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 11,500,000.00 USD | 11,500,000.00 USD | 258,970.00 USD | 108,400.00 USD | 151,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 36,860,000.00 USD | 36,860,000.00 USD | 128,010.00 USD | 147,000.00 USD | 148,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 11,720,000.00 USD | 11,720,000.00 USD | 116,480.00 USD | 64,510.00 USD | 43,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0831` | 37,490,000.00 USD | 37,490,000.00 USD | 346,900.00 USD | 119,240.00 USD | 158,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 12,030,000.00 USD | 12,030,000.00 USD | 193,840.00 USD | 28,280.00 USD | 85,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 38,140,000.00 USD | 38,140,000.00 USD | 313,100.00 USD | 258,020.00 USD | 80,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 12,230,000.00 USD | 12,230,000.00 USD | 153,900.00 USD | 46,180.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0833` | 38,870,000.00 USD | 38,870,000.00 USD | 413,110.00 USD | 230,970.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 12,580,000.00 USD | 12,580,000.00 USD | 154,940.00 USD | 60,550.00 USD | 134,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 39,370,000.00 USD | 39,370,000.00 USD | 216,670.00 USD | 135,260.00 USD | 144,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 12,970,000.00 USD | 12,970,000.00 USD | 122,780.00 USD | 184,470.00 USD | 79,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0835` | 39,870,000.00 USD | 39,870,000.00 USD | 258,370.00 USD | 107,380.00 USD | 128,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0835` | 205.70 USD | 29,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0836` | 13,360,000.00 USD | 13,360,000.00 USD | 83,690.00 USD | 84,520.00 USD | 222,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 40,210,000.00 USD | 40,210,000.00 USD | 104,940.00 USD | 90,690.00 USD | 146,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 29,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 13,650,000.00 USD | 13,650,000.00 USD | 189,580.00 USD | 61,550.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0837` | 40,650,000.00 USD | 40,650,000.00 USD | 262,200.00 USD | 158,180.00 USD | 27,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 30,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 13,910,000.00 USD | 13,910,000.00 USD | 141,530.00 USD | 76,380.00 USD | 48,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 40,820,000.00 USD | 40,820,000.00 USD | 100,250.00 USD | 64,030.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 13,980,000.00 USD | 13,980,000.00 USD | 67,620.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0839` | 40,980,000.00 USD | 40,980,000.00 USD | 96,540.00 USD | 64,060.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 30,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 14,030,000.00 USD | 14,030,000.00 USD | 35,090.00 USD | 15,480.00 USD | 780.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 41,120,000.00 USD | 41,120,000.00 USD | 127,750.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 14,070,000.00 USD | 14,070,000.00 USD | 33,390.00 USD | 2,010.00 USD | 629.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0841` | 41,200,000.00 USD | 41,200,000.00 USD | 78,440.00 USD | 0.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0842` | 462.91 USD | 31,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0842` | 14,150,000.00 USD | 14,150,000.00 USD | 31,430.00 USD | 0.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 41,360,000.00 USD | 41,360,000.00 USD | 122,190.00 USD | 33,520.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 14,190,000.00 USD | 14,190,000.00 USD | 36,500.00 USD | 0.00 USD | 611.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0843` | 41,530,000.00 USD | 41,530,000.00 USD | 115,430.00 USD | 44,120.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 14,270,000.00 USD | 14,270,000.00 USD | 88,610.00 USD | 0.00 USD | 922.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 41,800,000.00 USD | 41,800,000.00 USD | 135,060.00 USD | 64,360.00 USD | 74,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 14,300,000.00 USD | 14,300,000.00 USD | 20,470.00 USD | 0.00 USD | 255.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0845` | 41,970,000.00 USD | 41,970,000.00 USD | 76,690.00 USD | 30,660.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 14,380,000.00 USD | 14,380,000.00 USD | 67,820.00 USD | 16,670.00 USD | 778.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 42,200,000.00 USD | 42,200,000.00 USD | 110,690.00 USD | 76,890.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 31,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 14,400,000.00 USD | 14,400,000.00 USD | 18,780.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0847` | 42,510,000.00 USD | 42,510,000.00 USD | 159,740.00 USD | 113,280.00 USD | 38,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 14,420,000.00 USD | 14,420,000.00 USD | 20,660.00 USD | 0.00 USD | 818.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 42,840,000.00 USD | 42,840,000.00 USD | 166,870.00 USD | 67,150.00 USD | 101,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0849` | 14,440,000.00 USD | 14,440,000.00 USD | 15,210.00 USD | 0.00 USD | 269.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0849` | 43,230,000.00 USD | 43,230,000.00 USD | 126,210.00 USD | 145,370.00 USD | 111,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 14,460,000.00 USD | 14,460,000.00 USD | 21,120.00 USD | 0.00 USD | 319.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 43,620,000.00 USD | 43,620,000.00 USD | 147,740.00 USD | 61,080.00 USD | 188,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 31,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0851` | 14,490,000.00 USD | 14,490,000.00 USD | 23,040.00 USD | 11,000.00 USD | 185.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0851` | 43,850,000.00 USD | 43,850,000.00 USD | 59,990.00 USD | 87,540.00 USD | 77,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 14,510,000.00 USD | 14,510,000.00 USD | 12,910.00 USD | 737.47 USD | 574.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0853` | 44,010,000.00 USD | 44,010,000.00 USD | 84,580.00 USD | 55,780.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 14,570,000.00 USD | 14,570,000.00 USD | 34,680.00 USD | 13,190.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 44,220,000.00 USD | 44,220,000.00 USD | 111,900.00 USD | 48,090.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0855` | 14,710,000.00 USD | 14,710,000.00 USD | 64,150.00 USD | 45,460.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0855` | 44,580,000.00 USD | 44,580,000.00 USD | 185,600.00 USD | 101,580.00 USD | 70,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 14,860,000.00 USD | 14,860,000.00 USD | 92,490.00 USD | 32,810.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 44,880,000.00 USD | 44,880,000.00 USD | 105,420.00 USD | 110,810.00 USD | 86,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0857` | 14,950,000.00 USD | 14,950,000.00 USD | 50,540.00 USD | 18,030.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0857` | 45,070,000.00 USD | 45,070,000.00 USD | 124,090.00 USD | 8,980.00 USD | 56,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 15,040,000.00 USD | 15,040,000.00 USD | 48,130.00 USD | 36,780.00 USD | 419.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 45,240,000.00 USD | 45,240,000.00 USD | 83,590.00 USD | 38,000.00 USD | 49,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0859` | 15,170,000.00 USD | 15,170,000.00 USD | 72,260.00 USD | 20,870.00 USD | 40,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0859` | 45,350,000.00 USD | 45,350,000.00 USD | 85,670.00 USD | 23,160.00 USD | 747.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0860` | 15,260,000.00 USD | 15,260,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 45,500,000.00 USD | 45,500,000.00 USD | 72,910.00 USD | 55,790.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0861` | 15,310,000.00 USD | 15,310,000.00 USD | 20,430.00 USD | 0.00 USD | 32,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0861` | 45,720,000.00 USD | 45,720,000.00 USD | 81,490.00 USD | 84,030.00 USD | 59,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0862` | 15,390,000.00 USD | 15,390,000.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 45,810,000.00 USD | 45,810,000.00 USD | 15,880.00 USD | 20,950.00 USD | 45,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 34,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0864` | 15,430,000.00 USD | 15,430,000.00 USD | 22,510.00 USD | 20,050.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 45,920,000.00 USD | 45,920,000.00 USD | 64,760.00 USD | 21,830.00 USD | 27,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0865` | 15,480,000.00 USD | 15,480,000.00 USD | 31,770.00 USD | 1,280.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0865` | 46,120,000.00 USD | 46,120,000.00 USD | 103,840.00 USD | 26,840.00 USD | 71,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 15,550,000.00 USD | 15,550,000.00 USD | 26,440.00 USD | 16,310.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 46,160,000.00 USD | 46,160,000.00 USD | 10,780.00 USD | 30,220.00 USD | 342.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0867` | 15,620,000.00 USD | 15,620,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0867` | 46,300,000.00 USD | 46,300,000.00 USD | 37,230.00 USD | 68,720.00 USD | 36,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 15,690,000.00 USD | 15,690,000.00 USD | 24,660.00 USD | 9,540.00 USD | 34,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 46,580,000.00 USD | 46,580,000.00 USD | 166,800.00 USD | 50,450.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0869` | 15,720,000.00 USD | 15,720,000.00 USD | 13,960.00 USD | 8,720.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0869` | 46,810,000.00 USD | 46,810,000.00 USD | 86,030.00 USD | 106,700.00 USD | 38,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 15,760,000.00 USD | 15,760,000.00 USD | 33,110.00 USD | 6,620.00 USD | 295.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 46,920,000.00 USD | 46,920,000.00 USD | 64,420.00 USD | 41,030.00 USD | 815.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0871` | 15,910,000.00 USD | 15,910,000.00 USD | 50,960.00 USD | 57,110.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0871` | 47,130,000.00 USD | 47,130,000.00 USD | 81,270.00 USD | 68,300.00 USD | 58,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 15,960,000.00 USD | 15,960,000.00 USD | 27,110.00 USD | 16,340.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 47,320,000.00 USD | 47,320,000.00 USD | 67,390.00 USD | 74,740.00 USD | 52,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0873` | 15,980,000.00 USD | 15,980,000.00 USD | 1,730.00 USD | 1,460.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0873` | 47,450,000.00 USD | 47,450,000.00 USD | 100,710.00 USD | 0.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0875` | 16,010,000.00 USD | 16,010,000.00 USD | 25,220.00 USD | 717.80 USD | 545.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0875` | 47,530,000.00 USD | 47,530,000.00 USD | 28,810.00 USD | 18,590.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 9,620.00 USD | 44,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0876` | 16,080,000.00 USD | 16,080,000.00 USD | 33,830.00 USD | 15,030.00 USD | 26,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 47,680,000.00 USD | 47,680,000.00 USD | 117,620.00 USD | 23,600.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0877` | 16,140,000.00 USD | 16,140,000.00 USD | 21,520.00 USD | 11,700.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0877` | 47,800,000.00 USD | 47,800,000.00 USD | 67,300.00 USD | 1,810.00 USD | 47,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0878` | 16,290,000.00 USD | 16,290,000.00 USD | 63,040.00 USD | 40,570.00 USD | 50,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 47,890,000.00 USD | 47,890,000.00 USD | 6,280.00 USD | 39,280.00 USD | 46,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0879` | 16,320,000.00 USD | 16,320,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0879` | 48,060,000.00 USD | 48,060,000.00 USD | 73,130.00 USD | 41,910.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0880` | 16,400,000.00 USD | 16,400,000.00 USD | 48,000.00 USD | 1,230.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 48,120,000.00 USD | 48,120,000.00 USD | 38,400.00 USD | 27,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 44,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0881` | 16,450,000.00 USD | 16,450,000.00 USD | 33,000.00 USD | 10,770.00 USD | 146.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0881` | 48,230,000.00 USD | 48,230,000.00 USD | 20,400.00 USD | 58,090.00 USD | 24,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0882` | 16,520,000.00 USD | 16,520,000.00 USD | 25,340.00 USD | 15,630.00 USD | 28,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0883` | 16,630,000.00 USD | 16,630,000.00 USD | 26,840.00 USD | 73,610.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0884` | 16,740,000.00 USD | 16,740,000.00 USD | 8,850.00 USD | 17,780.00 USD | 84,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0886` | 16,820,000.00 USD | 16,820,000.00 USD | 48,870.00 USD | 18,070.00 USD | 13,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0887` | 16,880,000.00 USD | 16,880,000.00 USD | 22,710.00 USD | 22,450.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 44,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0888` | 16,900,000.00 USD | 16,900,000.00 USD | 16,050.00 USD | 0.00 USD | 243.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0889` | 16,900,000.00 USD | 16,900,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0890` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 802.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0891` | 16,920,000.00 USD | 16,920,000.00 USD | 2,580.00 USD | 0.00 USD | 18,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0893` | 16,950,000.00 USD | 16,950,000.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0894` | 16,970,000.00 USD | 16,970,000.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0896` | 871.86 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 46,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0907` | 7,590.00 USD | 54,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 1,040.00 USD | 55,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 59,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0914` | 171.19 USD | 59,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0917` | 344.43 USD | 59,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 60,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 5,090.00 USD | 65,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0935` | 3,300.00 USD | 68,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0940` | 926.30 USD | 69,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0949` | 14,360.00 USD | 83,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0951` | 114,180.00 USD | 197,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 198,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0965` | 48,270.00 USD | 246,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 39,190.00 USD | 286,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 286,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 10,510.00 USD | 297,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0994` | 1,280.00 USD | 298,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1012` | 1,710.00 USD | 300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 307,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 5,530.00 USD | 313,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 313,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1060` | 3,170.00 USD | 316,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 322,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1111` | 3,450.00 USD | 326,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1121` | 2,410.00 USD | 328,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1123` | 336.75 USD | 329,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 329,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 329,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 121.85 USD | 329,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1192` | 222.33 USD | 329,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 330,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1265` | 2,570,000.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1268` | 108.71 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1295` | 611.86 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1313` | 1,590.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1336` | 510.81 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1379` | 995.14 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1381` | 1,800.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1406` | 22,810.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,800.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1414` | 32,620.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1451` | 136.35 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1464` | 387.51 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1466` | 2,340.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,360.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1489` | 55,770.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1509` | 340.62 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 2,010.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 267.55 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 389.72 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 338.10 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 4,830.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 980.15 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1575` | 1,110.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 15,730,000.00 USD | 0.00 USD | 3,930.00 USD | `-79.96%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 15,730,000.00 USD | 0.00 USD | 407.02 USD | `-79.46%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 15,720,000.00 USD | 0.00 USD | 5,290.00 USD | `-79.34%` | `319,394.00` |
| `Live` | `Long` | `0.0181` | 15,720,000.00 USD | 0.00 USD | 4,050.00 USD | `-77.46%` | `224,650.00` |
| `Live` | `Long` | `0.0191` | 15,720,000.00 USD | 0.00 USD | 16,890.00 USD | `-76.22%` | `886,614.00` |
| `Live` | `Long` | `0.0198` | 15,700,000.00 USD | 0.00 USD | 397.00 USD | `-75.22%` | `20,000.00` |
| `Live` | `Long` | `0.0202` | 15,700,000.00 USD | 0.00 USD | 285.63 USD | `-74.84%` | `14,175.00` |
| `Live` | `Long` | `0.0208` | 15,700,000.00 USD | 0.00 USD | 3,900.00 USD | `-74.09%` | `187,979.00` |
| `Live` | `Long` | `0.0210` | 15,690,000.00 USD | 0.00 USD | 658.04 USD | `-73.72%` | `31,261.00` |
| `Live` | `Long` | `0.0211` | 15,690,000.00 USD | 0.00 USD | 126.67 USD | `-73.59%` | `5,989.00` |
| `Live` | `Long` | `0.0230` | 15,690,000.00 USD | 0.00 USD | 11,270.00 USD | `-71.35%` | `491,018.00` |
| `Live` | `Long` | `0.0232` | 15,680,000.00 USD | 0.00 USD | 345.98 USD | `-70.97%` | `14,881.00` |
| `Live` | `Long` | `0.0233` | 15,680,000.00 USD | 0.00 USD | 1,870.00 USD | `-70.85%` | `80,000.00` |
| `Live` | `Long` | `0.0237` | 15,680,000.00 USD | 0.00 USD | 473.00 USD | `-70.47%` | `20,000.00` |
| `Live` | `Long` | `0.0240` | 15,680,000.00 USD | 0.00 USD | 1,160.00 USD | `-69.97%` | `48,025.00` |
| `Live` | `Long` | `0.0245` | 15,680,000.00 USD | 0.00 USD | 131.20 USD | `-69.35%` | `5,344.00` |
| `Live` | `Long` | `0.0250` | 15,680,000.00 USD | 0.00 USD | 1,900.00 USD | `-68.72%` | `75,693.00` |
| `Live` | `Long` | `0.0271` | 15,680,000.00 USD | 0.00 USD | 1,060.00 USD | `-66.23%` | `39,049.00` |
| `Live` | `Long` | `0.0276` | 15,680,000.00 USD | 0.00 USD | 3,600.00 USD | `-65.60%` | `130,804.00` |
| `Live` | `Long` | `0.0278` | 15,670,000.00 USD | 0.00 USD | 126.49 USD | `-65.23%` | `4,542.00` |
| `Live` | `Long` | `0.0279` | 15,670,000.00 USD | 0.00 USD | 1,730.00 USD | `-65.10%` | `61,775.00` |
| `Live` | `Long` | `0.0285` | 15,670,000.00 USD | 0.00 USD | 21,410.00 USD | `-64.35%` | `750,000.00` |
| `Live` | `Long` | `0.0289` | 15,650,000.00 USD | 0.00 USD | 3,880.00 USD | `-63.98%` | `134,443.00` |
| `Live` | `Long` | `0.0291` | 15,640,000.00 USD | 0.00 USD | 731.11 USD | `-63.60%` | `25,081.00` |
| `Live` | `Long` | `0.0296` | 15,640,000.00 USD | 0.00 USD | 1,480.00 USD | `-62.98%` | `50,000.00` |
| `Live` | `Long` | `0.0301` | 15,640,000.00 USD | 0.00 USD | 2,360.00 USD | `-62.36%` | `78,319.00` |
| `Live` | `Long` | `0.0302` | 15,640,000.00 USD | 0.00 USD | 648,090.00 USD | `-62.23%` | `21,424,497.00` |
| `Live` | `Long` | `0.0306` | 14,990,000.00 USD | 0.00 USD | 137.41 USD | `-61.86%` | `4,498.00` |
| `Live` | `Long` | `0.0321` | 14,990,000.00 USD | 0.00 USD | 174.10 USD | `-59.98%` | `5,432.00` |
| `Live` | `Long` | `0.0323` | 14,990,000.00 USD | 0.00 USD | 146.06 USD | `-59.61%` | `4,515.00` |
| `Live` | `Long` | `0.0328` | 14,990,000.00 USD | 0.00 USD | 1,560.00 USD | `-59.11%` | `47,501.00` |
| `Live` | `Long` | `0.0328` | 14,990,000.00 USD | 0.00 USD | 67,890.00 USD | `-58.99%` | `2,066,606.00` |
| `Live` | `Long` | `0.0338` | 14,920,000.00 USD | 0.00 USD | 33,750.00 USD | `-57.86%` | `1,000,000.00` |
| `Live` | `Long` | `0.0340` | 14,890,000.00 USD | 0.00 USD | 3,060.00 USD | `-57.49%` | `90,000.00` |
| `Live` | `Long` | `0.0341` | 14,890,000.00 USD | 0.00 USD | 924.13 USD | `-57.36%` | `27,061.00` |
| `Live` | `Long` | `0.0345` | 14,880,000.00 USD | 0.00 USD | 5,140.00 USD | `-56.99%` | `149,206.00` |
| `Live` | `Long` | `0.0353` | 14,880,000.00 USD | 0.00 USD | 909.52 USD | `-55.86%` | `25,729.00` |
| `Live` | `Long` | `0.0357` | 14,880,000.00 USD | 0.00 USD | 191.23 USD | `-55.36%` | `5,349.00` |
| `Live` | `Long` | `0.0358` | 14,880,000.00 USD | 0.00 USD | 214.53 USD | `-55.24%` | `5,984.00` |
| `Live` | `Long` | `0.0369` | 14,880,000.00 USD | 0.00 USD | 18,430.00 USD | `-53.99%` | `500,000.00` |
| `Live` | `Long` | `0.0372` | 14,860,000.00 USD | 0.00 USD | 1,860.00 USD | `-53.62%` | `50,080.00` |
| `Live` | `Long` | `0.0374` | 14,860,000.00 USD | 0.00 USD | 3,780.00 USD | `-53.37%` | `101,126.00` |
| `Live` | `Long` | `0.0377` | 14,850,000.00 USD | 0.00 USD | 2,570.00 USD | `-52.99%` | `68,212.00` |
| `Live` | `Long` | `0.0379` | 14,850,000.00 USD | 0.00 USD | 98,260.00 USD | `-52.62%` | `2,589,112.00` |
| `Live` | `Long` | `0.0381` | 14,750,000.00 USD | 0.00 USD | 246.45 USD | `-52.49%` | `6,477.00` |
| `Live` | `Long` | `0.0384` | 14,750,000.00 USD | 0.00 USD | 1,110.00 USD | `-51.99%` | `28,854.00` |
| `Live` | `Long` | `0.0386` | 14,750,000.00 USD | 0.00 USD | 121.74 USD | `-51.87%` | `3,158.00` |
| `Live` | `Long` | `0.0389` | 14,750,000.00 USD | 0.00 USD | 236.87 USD | `-51.49%` | `6,097.00` |
| `Live` | `Long` | `0.0393` | 14,750,000.00 USD | 0.00 USD | 221.10 USD | `-50.99%` | `5,633.00` |
| `Live` | `Long` | `0.0394` | 14,750,000.00 USD | 0.00 USD | 3,380.00 USD | `-50.87%` | `85,771.00` |
| `Live` | `Long` | `0.0404` | 14,750,000.00 USD | 0.00 USD | 115.12 USD | `-49.50%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 14,750,000.00 USD | 0.00 USD | 419.28 USD | `-49.12%` | `10,289.00` |
| `Live` | `Long` | `0.0410` | 14,750,000.00 USD | 0.00 USD | 395.70 USD | `-48.87%` | `9,663.00` |
| `Live` | `Long` | `0.0415` | 14,750,000.00 USD | 0.00 USD | 1,030.00 USD | `-48.12%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 14,750,000.00 USD | 0.00 USD | 266.05 USD | `-47.62%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 14,750,000.00 USD | 0.00 USD | 61,470.00 USD | `-47.25%` | `1,454,956.00` |
| `Live` | `Long` | `0.0423` | 14,680,000.00 USD | 0.00 USD | 267.52 USD | `-47.12%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 14,680,000.00 USD | 0.00 USD | 1,070.00 USD | `-47.00%` | `25,181.00` |
| `Live` | `Long` | `0.0425` | 14,680,000.00 USD | 0.00 USD | 1,010.00 USD | `-46.87%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 14,680,000.00 USD | 0.00 USD | 3,620.00 USD | `-46.75%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 14,680,000.00 USD | 0.00 USD | 859.00 USD | `-46.37%` | `20,000.00` |
| `Live` | `Long` | `0.0430` | 14,680,000.00 USD | 0.00 USD | 279.18 USD | `-46.25%` | `6,485.00` |
| `Live` | `Long` | `0.0432` | 14,680,000.00 USD | 0.00 USD | 6,430.00 USD | `-46.00%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 14,670,000.00 USD | 0.00 USD | 2,720.00 USD | `-45.88%` | `62,704.00` |
| `Live` | `Long` | `0.0439` | 14,670,000.00 USD | 0.00 USD | 1,610.00 USD | `-45.25%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 14,670,000.00 USD | 0.00 USD | 750.58 USD | `-45.13%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 14,670,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.00%` | `24,073.00` |
| `Live` | `Long` | `0.0442` | 14,660,000.00 USD | 0.00 USD | 239.69 USD | `-44.88%` | `5,429.00` |
| `Live` | `Long` | `0.0444` | 14,660,000.00 USD | 0.00 USD | 101,440.00 USD | `-44.63%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 14,560,000.00 USD | 0.00 USD | 444.76 USD | `-44.25%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 14,560,000.00 USD | 0.00 USD | 248.63 USD | `-44.13%` | `5,556.00` |
| `Live` | `Long` | `0.0452` | 14,560,000.00 USD | 0.00 USD | 1,950.00 USD | `-43.50%` | `43,069.00` |
| `Live` | `Long` | `0.0454` | 14,560,000.00 USD | 0.00 USD | 2,170.00 USD | `-43.25%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,560,000.00 USD | 0.00 USD | 32,650.00 USD | `-43.13%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,520,000.00 USD | 0.00 USD | 6,780.00 USD | `-42.88%` | `148,286.00` |
| `Live` | `Long` | `0.0461` | 14,520,000.00 USD | 0.00 USD | 4,500.00 USD | `-42.50%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,510,000.00 USD | 0.00 USD | 114.36 USD | `-42.38%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 14,510,000.00 USD | 0.00 USD | 362.87 USD | `-42.13%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 14,510,000.00 USD | 0.00 USD | 16,780.00 USD | `-42.00%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,500,000.00 USD | 0.00 USD | 8,460.00 USD | `-41.88%` | `181,738.00` |
| `Live` | `Long` | `0.0466` | 14,490,000.00 USD | 0.00 USD | 109.49 USD | `-41.76%` | `2,347.00` |
| `Live` | `Long` | `0.0471` | 14,490,000.00 USD | 0.00 USD | 323.89 USD | `-41.26%` | `6,884.00` |
| `Live` | `Long` | `0.0473` | 14,490,000.00 USD | 0.00 USD | 3,010.00 USD | `-41.01%` | `63,783.00` |
| `Live` | `Long` | `0.0474` | 14,480,000.00 USD | 0.00 USD | 593.13 USD | `-40.76%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 14,480,000.00 USD | 0.00 USD | 105.02 USD | `-40.51%` | `2,204.00` |
| `Live` | `Long` | `0.0478` | 14,480,000.00 USD | 0.00 USD | 47,600.00 USD | `-40.38%` | `996,821.00` |
| `Live` | `Long` | `0.0479` | 14,440,000.00 USD | 0.00 USD | 15,570.00 USD | `-40.13%` | `324,759.00` |
| `Live` | `Long` | `0.0481` | 14,420,000.00 USD | 0.00 USD | 56,440.00 USD | `-40.01%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,360,000.00 USD | 0.00 USD | 2,800.00 USD | `-39.88%` | `58,093.00` |
| `Live` | `Long` | `0.0483` | 14,360,000.00 USD | 0.00 USD | 2,280.00 USD | `-39.63%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,360,000.00 USD | 0.00 USD | 1,480.00 USD | `-39.51%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 14,360,000.00 USD | 0.00 USD | 1,280.00 USD | `-39.01%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,360,000.00 USD | 0.00 USD | 5,470.00 USD | `-38.88%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,350,000.00 USD | 0.00 USD | 1,080.00 USD | `-38.76%` | `21,989.00` |
| `Live` | `Long` | `0.0491` | 14,350,000.00 USD | 0.00 USD | 310.82 USD | `-38.63%` | `6,324.00` |
| `Live` | `Long` | `0.0493` | 14,350,000.00 USD | 0.00 USD | 311.56 USD | `-38.51%` | `6,326.00` |
| `Live` | `Long` | `0.0495` | 14,350,000.00 USD | 0.00 USD | 18,690.00 USD | `-38.13%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,330,000.00 USD | 0.00 USD | 635.71 USD | `-37.88%` | `12,778.00` |
| `Live` | `Long` | `0.0500` | 14,330,000.00 USD | 0.00 USD | 287.06 USD | `-37.63%` | `5,747.00` |
| `Live` | `Long` | `0.0500` | 14,330,000.00 USD | 0.00 USD | 501.50 USD | `-37.51%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,330,000.00 USD | 0.00 USD | 5,410.00 USD | `-37.26%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,320,000.00 USD | 0.00 USD | 1,330.00 USD | `-37.14%` | `26,380.00` |
| `Live` | `Long` | `0.0505` | 14,320,000.00 USD | 0.00 USD | 334.89 USD | `-37.01%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,320,000.00 USD | 0.00 USD | 1,040.00 USD | `-36.76%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,320,000.00 USD | 0.00 USD | 5,350.00 USD | `-36.64%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,320,000.00 USD | 0.00 USD | 535.43 USD | `-36.39%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,320,000.00 USD | 0.00 USD | 566.65 USD | `-36.26%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,310,000.00 USD | 0.00 USD | 11,000.00 USD | `-36.14%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,300,000.00 USD | 0.00 USD | 1,490.00 USD | `-36.01%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,300,000.00 USD | 0.00 USD | 385.13 USD | `-35.89%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,300,000.00 USD | 0.00 USD | 2,900.00 USD | `-35.76%` | `56,376.00` |
| `Live` | `Long` | `0.0517` | 14,300,000.00 USD | 0.00 USD | 726.00 USD | `-35.39%` | `14,029.00` |
| `Live` | `Long` | `0.0520` | 14,300,000.00 USD | 0.00 USD | 277.72 USD | `-35.14%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,300,000.00 USD | 0.00 USD | 5,200.00 USD | `-35.01%` | `99,870.00` |
| `Live` | `Long` | `0.0522` | 14,290,000.00 USD | 0.00 USD | 275,090.00 USD | `-34.76%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,020,000.00 USD | 0.00 USD | 1,170.00 USD | `-34.51%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,020,000.00 USD | 0.00 USD | 5,640.00 USD | `-34.39%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,010,000.00 USD | 0.00 USD | 647.44 USD | `-34.26%` | `12,297.00` |
| `Live` | `Long` | `0.0527` | 14,010,000.00 USD | 0.00 USD | 2,110.00 USD | `-34.14%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,010,000.00 USD | 0.00 USD | 673.52 USD | `-34.01%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,010,000.00 USD | 0.00 USD | 181,690.00 USD | `-33.89%` | `3,431,434.00` |
| `Live` | `Long` | `0.0532` | 13,830,000.00 USD | 0.00 USD | 8,770.00 USD | `-33.64%` | `165,000.00` |
| `Live` | `Long` | `0.0534` | 13,820,000.00 USD | 0.00 USD | 314,750.00 USD | `-33.27%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,500,000.00 USD | 0.00 USD | 942.48 USD | `-33.14%` | `17,600.00` |
| `Live` | `Long` | `0.0539` | 13,500,000.00 USD | 0.00 USD | 20,280.00 USD | `-32.64%` | `375,926.00` |
| `Live` | `Long` | `0.0541` | 13,480,000.00 USD | 0.00 USD | 2,290.00 USD | `-32.52%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,480,000.00 USD | 0.00 USD | 87,240.00 USD | `-32.39%` | `1,611,038.00` |
| `Live` | `Long` | `0.0542` | 13,390,000.00 USD | 0.00 USD | 22,670.00 USD | `-32.27%` | `417,846.00` |
| `Live` | `Long` | `0.0544` | 13,370,000.00 USD | 0.00 USD | 237.95 USD | `-32.02%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,370,000.00 USD | 0.00 USD | 2,510.00 USD | `-31.89%` | `46,004.00` |
| `Live` | `Long` | `0.0546` | 13,370,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.77%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 13,360,000.00 USD | 0.00 USD | 188.07 USD | `-31.64%` | `3,435.00` |
| `Live` | `Long` | `0.0554` | 13,360,000.00 USD | 0.00 USD | 175.44 USD | `-30.77%` | `3,164.00` |
| `Live` | `Long` | `0.0556` | 13,360,000.00 USD | 0.00 USD | 907.02 USD | `-30.64%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 13,360,000.00 USD | 0.00 USD | 679.36 USD | `-30.27%` | `12,164.00` |
| `Live` | `Long` | `0.0561` | 13,360,000.00 USD | 0.00 USD | 38,870.00 USD | `-29.89%` | `692,198.00` |
| `Live` | `Long` | `0.0563` | 13,320,000.00 USD | 0.00 USD | 1,820.00 USD | `-29.77%` | `32,433.00` |
| `Live` | `Long` | `0.0563` | 13,320,000.00 USD | 0.00 USD | 48,170.00 USD | `-29.64%` | `854,847.00` |
| `Live` | `Long` | `0.0565` | 13,270,000.00 USD | 0.00 USD | 1,910.00 USD | `-29.52%` | `33,802.00` |
| `Live` | `Long` | `0.0566` | 13,270,000.00 USD | 0.00 USD | 131.48 USD | `-29.39%` | `2,325.00` |
| `Live` | `Long` | `0.0566` | 13,270,000.00 USD | 0.00 USD | 380.01 USD | `-29.27%` | `6,708.00` |
| `Live` | `Long` | `0.0568` | 13,270,000.00 USD | 0.00 USD | 1,430.00 USD | `-29.14%` | `25,279.00` |
| `Live` | `Long` | `0.0568` | 13,270,000.00 USD | 0.00 USD | 3,630.00 USD | `-29.02%` | `63,773.00` |
| `Live` | `Long` | `0.0570` | 13,270,000.00 USD | 0.00 USD | 421.03 USD | `-28.90%` | `7,393.00` |
| `Live` | `Long` | `0.0570` | 13,270,000.00 USD | 0.00 USD | 8,350.00 USD | `-28.77%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,260,000.00 USD | 0.00 USD | 644.99 USD | `-28.65%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,260,000.00 USD | 0.00 USD | 3,910.00 USD | `-28.40%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,250,000.00 USD | 0.00 USD | 5,670,000.00 USD | `-28.27%` | `98,666,424.00` |
| `Live` | `Long` | `0.0575` | 7,580,000.00 USD | 0.00 USD | 3,590.00 USD | `-28.15%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 7,580,000.00 USD | 0.00 USD | 10,600.00 USD | `-28.02%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 7,570,000.00 USD | 0.00 USD | 14,210.00 USD | `-27.90%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 7,560,000.00 USD | 0.00 USD | 3,940.00 USD | `-27.77%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 7,550,000.00 USD | 0.00 USD | 431.14 USD | `-27.52%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 7,550,000.00 USD | 0.00 USD | 447.17 USD | `-27.40%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 7,550,000.00 USD | 0.00 USD | 116.82 USD | `-27.15%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 7,550,000.00 USD | 0.00 USD | 172.78 USD | `-26.90%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 7,550,000.00 USD | 0.00 USD | 9,120.00 USD | `-26.65%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 7,540,000.00 USD | 0.00 USD | 212.22 USD | `-26.40%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 7,540,000.00 USD | 0.00 USD | 26,980.00 USD | `-26.15%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 7,510,000.00 USD | 0.00 USD | 5,170.00 USD | `-25.90%` | `87,060.00` |
| `Live` | `Long` | `0.0595` | 7,510,000.00 USD | 0.00 USD | 3,660.00 USD | `-25.77%` | `61,626.00` |
| `Live` | `Long` | `0.0595` | 7,510,000.00 USD | 0.00 USD | 2,830.00 USD | `-25.65%` | `47,585.00` |
| `Live` | `Long` | `0.0599` | 7,500,000.00 USD | 0.00 USD | 5,320.00 USD | `-25.27%` | `88,854.00` |
| `Live` | `Long` | `0.0600` | 7,500,000.00 USD | 0.00 USD | 380.38 USD | `-25.15%` | `6,345.00` |
| `Live` | `Long` | `0.0600` | 7,500,000.00 USD | 0.00 USD | 7,210.00 USD | `-25.02%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 7,490,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.90%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 7,480,000.00 USD | 0.00 USD | 548.46 USD | `-24.65%` | `9,088.00` |
| `Live` | `Long` | `0.0604` | 7,480,000.00 USD | 0.00 USD | 1,970.00 USD | `-24.53%` | `32,592.00` |
| `Live` | `Long` | `0.0605` | 7,480,000.00 USD | 0.00 USD | 32,090.00 USD | `-24.40%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,450,000.00 USD | 0.00 USD | 1,220.00 USD | `-24.15%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,450,000.00 USD | 0.00 USD | 717.73 USD | `-24.03%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,440,000.00 USD | 0.00 USD | 2,220.00 USD | `-23.90%` | `36,478.00` |
| `Live` | `Long` | `0.0611` | 7,440,000.00 USD | 0.00 USD | 73,370.00 USD | `-23.78%` | `1,201,845.00` |
| `Live` | `Long` | `0.0612` | 7,370,000.00 USD | 0.00 USD | 913.21 USD | `-23.65%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,370,000.00 USD | 0.00 USD | 665.54 USD | `-23.53%` | `10,866.00` |
| `Live` | `Long` | `0.0614` | 7,370,000.00 USD | 0.00 USD | 655.16 USD | `-23.40%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,370,000.00 USD | 0.00 USD | 1,400.00 USD | `-23.15%` | `22,725.00` |
| `Live` | `Long` | `0.0617` | 7,370,000.00 USD | 0.00 USD | 13,460.00 USD | `-23.03%` | `218,374.00` |
| `Live` | `Long` | `0.0617` | 7,350,000.00 USD | 0.00 USD | 158.08 USD | `-22.90%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,350,000.00 USD | 0.00 USD | 30,490.00 USD | `-22.53%` | `491,401.00` |
| `Live` | `Long` | `0.0622` | 7,320,000.00 USD | 0.00 USD | 33,240.00 USD | `-22.28%` | `534,019.00` |
| `Live` | `Long` | `0.0624` | 7,290,000.00 USD | 0.00 USD | 1,900.00 USD | `-22.15%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,290,000.00 USD | 0.00 USD | 3,470.00 USD | `-22.03%` | `55,505.00` |
| `Live` | `Long` | `0.0625` | 7,280,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-21.90%` | `17,642,013.00` |
| `Live` | `Long` | `0.0626` | 6,180,000.00 USD | 0.00 USD | 168.28 USD | `-21.78%` | `2,686.00` |
| `Live` | `Long` | `0.0628` | 6,180,000.00 USD | 0.00 USD | 1,320.00 USD | `-21.65%` | `20,979.00` |
| `Live` | `Long` | `0.0629` | 6,180,000.00 USD | 0.00 USD | 6,400.00 USD | `-21.53%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,170,000.00 USD | 0.00 USD | 3,080.00 USD | `-21.28%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,170,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-21.15%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 5,100,000.00 USD | 0.00 USD | 1,450.00 USD | `-21.03%` | `22,875.00` |
| `Live` | `Long` | `0.0634` | 5,100,000.00 USD | 0.00 USD | 12,660.00 USD | `-20.90%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 5,090,000.00 USD | 0.00 USD | 1,690.00 USD | `-20.78%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,090,000.00 USD | 0.00 USD | 280.95 USD | `-20.65%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,090,000.00 USD | 0.00 USD | 633.38 USD | `-20.53%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,090,000.00 USD | 0.00 USD | 8,670.00 USD | `-20.41%` | `136,018.00` |
| `Live` | `Long` | `0.0639` | 5,080,000.00 USD | 0.00 USD | 43,440.00 USD | `-20.28%` | `680,312.00` |
| `Live` | `Long` | `0.0640` | 5,040,000.00 USD | 0.00 USD | 1,360.00 USD | `-20.16%` | `21,194.00` |
| `Live` | `Long` | `0.0641` | 5,030,000.00 USD | 0.00 USD | 633.29 USD | `-19.91%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,030,000.00 USD | 0.00 USD | 9,150.00 USD | `-19.78%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,020,000.00 USD | 0.00 USD | 2,170.00 USD | `-19.66%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,020,000.00 USD | 0.00 USD | 23,050.00 USD | `-19.53%` | `357,682.00` |
| `Live` | `Long` | `0.0646` | 5,000,000.00 USD | 0.00 USD | 6,350.00 USD | `-19.28%` | `98,215.00` |
| `Live` | `Long` | `0.0648` | 4,990,000.00 USD | 0.00 USD | 86,870.00 USD | `-19.16%` | `1,341,590.00` |
| `Live` | `Long` | `0.0649` | 4,910,000.00 USD | 0.00 USD | 9,910.00 USD | `-19.03%` | `152,854.00` |
| `Live` | `Long` | `0.0649` | 4,900,000.00 USD | 0.00 USD | 22,520.00 USD | `-18.91%` | `346,692.00` |
| `Live` | `Long` | `0.0651` | 4,870,000.00 USD | 0.00 USD | 2,380.00 USD | `-18.66%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,870,000.00 USD | 0.00 USD | 13,770.00 USD | `-18.53%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 4,860,000.00 USD | 0.00 USD | 6,530.00 USD | `-18.41%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,850,000.00 USD | 0.00 USD | 5,340.00 USD | `-18.16%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 4,850,000.00 USD | 0.00 USD | 71,100.00 USD | `-17.91%` | `1,081,348.00` |
| `Live` | `Long` | `0.0659` | 4,770,000.00 USD | 0.00 USD | 14,600.00 USD | `-17.78%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,760,000.00 USD | 0.00 USD | 11,990.00 USD | `-17.66%` | `181,801.00` |
| `Live` | `Long` | `0.0660` | 4,750,000.00 USD | 0.00 USD | 339.83 USD | `-17.53%` | `5,145.00` |
| `Live` | `Long` | `0.0662` | 4,750,000.00 USD | 0.00 USD | 339.48 USD | `-17.41%` | `5,132.00` |
| `Live` | `Long` | `0.0663` | 4,750,000.00 USD | 0.00 USD | 1,630.00 USD | `-17.28%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,750,000.00 USD | 0.00 USD | 27,600.00 USD | `-17.16%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,720,000.00 USD | 0.00 USD | 1,030.00 USD | `-17.03%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,720,000.00 USD | 0.00 USD | 66,550.00 USD | `-16.91%` | `1,000,000.00` |
| `Live` | `Long` | `0.0667` | 4,650,000.00 USD | 0.00 USD | 34,860.00 USD | `-16.78%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,620,000.00 USD | 0.00 USD | 778.51 USD | `-16.66%` | `11,663.00` |
| `Live` | `Long` | `0.0669` | 4,610,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-16.53%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,600,000.00 USD | 0.00 USD | 389.18 USD | `-16.41%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,600,000.00 USD | 0.00 USD | 94,360.00 USD | `-16.28%` | `1,407,280.00` |
| `Live` | `Long` | `0.0672` | 3,500,000.00 USD | 0.00 USD | 899.27 USD | `-16.16%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,500,000.00 USD | 0.00 USD | 196.64 USD | `-16.04%` | `2,924.00` |
| `Live` | `Long` | `0.0673` | 3,500,000.00 USD | 0.00 USD | 15,580.00 USD | `-15.91%` | `231,289.00` |
| `Live` | `Long` | `0.0674` | 3,480,000.00 USD | 0.00 USD | 80,080.00 USD | `-15.79%` | `1,187,211.00` |
| `Live` | `Long` | `0.0675` | 3,400,000.00 USD | 0.00 USD | 310.73 USD | `-15.66%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,400,000.00 USD | 0.00 USD | 8,210.00 USD | `-15.54%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,400,000.00 USD | 0.00 USD | 5,400.00 USD | `-15.41%` | `79,670.00` |
| `Live` | `Long` | `0.0678` | 3,390,000.00 USD | 0.00 USD | 55,180.00 USD | `-15.29%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,340,000.00 USD | 0.00 USD | 23,050.00 USD | `-15.16%` | `339,202.00` |
| `Live` | `Long` | `0.0680` | 3,310,000.00 USD | 0.00 USD | 212.72 USD | `-15.04%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,310,000.00 USD | 0.00 USD | 1,680.00 USD | `-14.91%` | `24,721.00` |
| `Live` | `Long` | `0.0683` | 3,310,000.00 USD | 0.00 USD | 6,220.00 USD | `-14.79%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,300,000.00 USD | 0.00 USD | 1,290.00 USD | `-14.66%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,300,000.00 USD | 0.00 USD | 6,000.00 USD | `-14.54%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,300,000.00 USD | 0.00 USD | 4,690.00 USD | `-14.41%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,290,000.00 USD | 0.00 USD | 1,620.00 USD | `-14.29%` | `23,620.00` |
| `Live` | `Long` | `0.0688` | 3,290,000.00 USD | 0.00 USD | 69,020.00 USD | `-14.16%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,220,000.00 USD | 0.00 USD | 517.48 USD | `-14.04%` | `7,516.00` |
| `Live` | `Long` | `0.0689` | 3,220,000.00 USD | 0.00 USD | 507,660.00 USD | `-13.91%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,710,000.00 USD | 0.00 USD | 3,670.00 USD | `-13.79%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,710,000.00 USD | 0.00 USD | 8,350.00 USD | `-13.66%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,700,000.00 USD | 0.00 USD | 50,720.00 USD | `-13.54%` | `732,466.00` |
| `Live` | `Long` | `0.0693` | 2,650,000.00 USD | 0.00 USD | 2,160.00 USD | `-13.41%` | `31,211.00` |
| `Live` | `Long` | `0.0694` | 2,650,000.00 USD | 0.00 USD | 4,840.00 USD | `-13.29%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,640,000.00 USD | 0.00 USD | 14,930.00 USD | `-13.16%` | `214,659.00` |
| `Live` | `Long` | `0.0697` | 2,630,000.00 USD | 0.00 USD | 5,240.00 USD | `-13.04%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,620,000.00 USD | 0.00 USD | 4,800.00 USD | `-12.91%` | `68,831.00` |
| `Live` | `Long` | `0.0698` | 2,620,000.00 USD | 0.00 USD | 2,250.00 USD | `-12.79%` | `32,190.00` |
| `Live` | `Long` | `0.0699` | 2,620,000.00 USD | 0.00 USD | 9,500.00 USD | `-12.66%` | `135,877.00` |
| `Live` | `Long` | `0.0701` | 2,610,000.00 USD | 0.00 USD | 264.58 USD | `-12.54%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,610,000.00 USD | 0.00 USD | 1,590.00 USD | `-12.41%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 791.79 USD | `-12.29%` | `11,271.00` |
| `Live` | `Long` | `0.0703` | 2,600,000.00 USD | 0.00 USD | 5,060.00 USD | `-12.16%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,600,000.00 USD | 0.00 USD | 2,510.00 USD | `-12.04%` | `35,646.00` |
| `Live` | `Long` | `0.0706` | 2,600,000.00 USD | 0.00 USD | 93,610.00 USD | `-11.91%` | `1,326,872.00` |
| `Live` | `Long` | `0.0707` | 2,500,000.00 USD | 0.00 USD | 536.00 USD | `-11.67%` | `7,576.00` |
| `Live` | `Long` | `0.0712` | 2,500,000.00 USD | 0.00 USD | 389.38 USD | `-11.04%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,500,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-10.92%` | `24,460,119.00` |
| `Live` | `Long` | `0.0714` | 757,370.00 USD | 0.00 USD | 2,220.00 USD | `-10.79%` | `31,003.00` |
| `Live` | `Long` | `0.0716` | 755,160.00 USD | 0.00 USD | 8,120.00 USD | `-10.67%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 747,040.00 USD | 0.00 USD | 560.88 USD | `-10.54%` | `7,828.00` |
| `Live` | `Long` | `0.0717` | 746,480.00 USD | 0.00 USD | 1,520.00 USD | `-10.42%` | `21,127.00` |
| `Live` | `Long` | `0.0718` | 744,960.00 USD | 0.00 USD | 10,850.00 USD | `-10.29%` | `151,060.00` |
| `Live` | `Long` | `0.0720` | 734,110.00 USD | 0.00 USD | 778.93 USD | `-10.17%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 733,330.00 USD | 0.00 USD | 23,870.00 USD | `-10.04%` | `331,347.00` |
| `Live` | `Long` | `0.0722` | 709,460.00 USD | 0.00 USD | 10,450.00 USD | `-9.79%` | `144,576.00` |
| `Live` | `Long` | `0.0723` | 699,010.00 USD | 0.00 USD | 163.73 USD | `-9.67%` | `2,263.00` |
| `Live` | `Long` | `0.0725` | 698,850.00 USD | 0.00 USD | 598.51 USD | `-9.54%` | `8,261.00` |
| `Live` | `Long` | `0.0726` | 698,250.00 USD | 0.00 USD | 260.74 USD | `-9.42%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 697,990.00 USD | 0.00 USD | 948.37 USD | `-9.29%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 697,040.00 USD | 0.00 USD | 452.21 USD | `-9.17%` | `6,216.00` |
| `Live` | `Long` | `0.0728` | 696,590.00 USD | 0.00 USD | 1,230.00 USD | `-9.04%` | `16,952.00` |
| `Live` | `Long` | `0.0730` | 695,350.00 USD | 0.00 USD | 72,950.00 USD | `-8.92%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 622,400.00 USD | 0.00 USD | 10,300.00 USD | `-8.79%` | `141,047.00` |
| `Live` | `Long` | `0.0732` | 612,100.00 USD | 0.00 USD | 1,930.00 USD | `-8.67%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 610,170.00 USD | 0.00 USD | 5,410.00 USD | `-8.54%` | `73,796.00` |
| `Live` | `Long` | `0.0735` | 604,770.00 USD | 0.00 USD | 7,000.00 USD | `-8.29%` | `95,360.00` |
| `Live` | `Long` | `0.0736` | 597,760.00 USD | 0.00 USD | 4,060.00 USD | `-8.17%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 593,710.00 USD | 0.00 USD | 5,490.00 USD | `-8.04%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 588,210.00 USD | 0.00 USD | 10,390.00 USD | `-7.92%` | `140,949.00` |
| `Live` | `Long` | `0.0738` | 577,820.00 USD | 0.00 USD | 5,630.00 USD | `-7.79%` | `76,281.00` |
| `Live` | `Long` | `0.0740` | 572,180.00 USD | 0.00 USD | 13,570.00 USD | `-7.67%` | `183,446.00` |
| `Live` | `Long` | `0.0741` | 558,620.00 USD | 0.00 USD | 455,080.00 USD | `-7.54%` | `6,145,600.00` |
| `Live` | `Long` | `0.0741` | 103,540.00 USD | 0.00 USD | 5,960.00 USD | `-7.42%` | `80,332.00` |
| `Live` | `Long` | `0.0742` | 97,580.00 USD | 0.00 USD | 1,280.00 USD | `-7.30%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 96,300.00 USD | 0.00 USD | 3,870.00 USD | `-7.17%` | `52,019.00` |
| `Live` | `Long` | `0.0745` | 92,430.00 USD | 0.00 USD | 311.95 USD | `-7.05%` | `4,190.00` |
| `Live` | `Long` | `0.0746` | 92,120.00 USD | 0.00 USD | 780.39 USD | `-6.92%` | `10,468.00` |
| `Live` | `Long` | `0.0746` | 91,340.00 USD | 0.00 USD | 1,050.00 USD | `-6.80%` | `14,085.00` |
| `Live` | `Long` | `0.0747` | 90,290.00 USD | 0.00 USD | 359.77 USD | `-6.67%` | `4,813.00` |
| `Live` | `Long` | `0.0750` | 89,930.00 USD | 0.00 USD | 1,370.00 USD | `-6.42%` | `18,241.00` |
| `Live` | `Long` | `0.0751` | 88,560.00 USD | 0.00 USD | 451.13 USD | `-6.30%` | `6,011.00` |
| `Live` | `Long` | `0.0751` | 88,110.00 USD | 0.00 USD | 14,540.00 USD | `-6.17%` | `193,491.00` |
| `Live` | `Long` | `0.0752` | 73,570.00 USD | 0.00 USD | 3,910.00 USD | `-6.05%` | `51,995.00` |
| `Live` | `Long` | `0.0754` | 69,660.00 USD | 0.00 USD | 617.57 USD | `-5.92%` | `8,196.00` |
| `Live` | `Long` | `0.0755` | 69,040.00 USD | 0.00 USD | 4,060.00 USD | `-5.80%` | `53,747.00` |
| `Live` | `Long` | `0.0756` | 64,990.00 USD | 0.00 USD | 356.24 USD | `-5.55%` | `4,709.00` |
| `Live` | `Long` | `0.0757` | 64,630.00 USD | 0.00 USD | 3,270.00 USD | `-5.42%` | `43,197.00` |
| `Live` | `Long` | `0.0759` | 61,360.00 USD | 0.00 USD | 5,540.00 USD | `-5.30%` | `73,071.00` |
| `Live` | `Long` | `0.0760` | 55,820.00 USD | 0.00 USD | 32,320.00 USD | `-5.17%` | `425,602.00` |
| `Live` | `Long` | `0.0761` | 23,490.00 USD | 0.00 USD | 1,690.00 USD | `-5.05%` | `22,243.00` |
| `Live` | `Long` | `0.0761` | 21,800.00 USD | 0.00 USD | 1,130.00 USD | `-4.92%` | `14,810.00` |
| `Live` | `Long` | `0.0762` | 20,670.00 USD | 0.00 USD | 5,710.00 USD | `-4.80%` | `74,902.00` |
| `Live` | `Short` | `0.0764` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | `-4.67%` | `52,065.00` |
| `Live` | `Long` | `0.0765` | 14,960.00 USD | 0.00 USD | 9,890.00 USD | `-4.55%` | `129,368.00` |
| `Live` | `Long` | `0.0769` | 5,070.00 USD | 0.00 USD | 242.54 USD | `-4.05%` | `3,156.00` |
| `Live` | `Long` | `0.0770` | 4,830.00 USD | 0.00 USD | 330.81 USD | `-3.92%` | `4,299.00` |
| `Live` | `Long` | `0.0770` | 4,500.00 USD | 0.00 USD | 109.41 USD | `-3.80%` | `1,420.00` |
| `Live` | `Long` | `0.0784` | 4,390.00 USD | 0.00 USD | 4,390.00 USD | `-2.18%` | `56,000.00` |
| `Live` | `Short` | `0.0818` | 4,690.00 USD | 710.08 USD | 0.00 USD | `+2.07%` | `8,686.00` |
| `Live` | `Short` | `0.0823` | 4,810.00 USD | 121.40 USD | 0.00 USD | `+2.69%` | `1,476.00` |
| `Live` | `Short` | `0.0824` | 17,470.00 USD | 12,660.00 USD | 0.00 USD | `+2.94%` | `153,549.00` |
| `Live` | `Short` | `0.0832` | 28,790.00 USD | 11,330.00 USD | 0.00 USD | `+3.82%` | `136,223.00` |
| `Live` | `Short` | `0.0835` | 29,000.00 USD | 205.70 USD | 0.00 USD | `+4.32%` | `2,462.00` |
| `Live` | `Short` | `0.0837` | 29,290.00 USD | 293.44 USD | 0.00 USD | `+4.44%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 30,860.00 USD | 1,570.00 USD | 0.00 USD | `+4.57%` | `18,767.00` |
| `Live` | `Short` | `0.0839` | 30,970.00 USD | 104.69 USD | 0.00 USD | `+4.82%` | `1,247.00` |
| `Live` | `Short` | `0.0842` | 31,430.00 USD | 462.91 USD | 0.00 USD | `+5.07%` | `5,501.00` |
| `Live` | `Short` | `0.0843` | 31,540.00 USD | 104.72 USD | 0.00 USD | `+5.19%` | `1,243.00` |
| `Live` | `Short` | `0.0847` | 31,750.00 USD | 213.74 USD | 0.00 USD | `+5.69%` | `2,525.00` |
| `Live` | `Short` | `0.0851` | 31,970.00 USD | 214.75 USD | 0.00 USD | `+6.19%` | `2,525.00` |
| `Live` | `Short` | `0.0858` | 32,080.00 USD | 115.30 USD | 0.00 USD | `+7.19%` | `1,343.00` |
| `Live` | `Short` | `0.0862` | 34,420.00 USD | 2,340.00 USD | 0.00 USD | `+7.69%` | `27,165.00` |
| `Live` | `Short` | `0.0876` | 44,050.00 USD | 9,620.00 USD | 0.00 USD | `+9.31%` | `109,908.00` |
| `Live` | `Short` | `0.0881` | 44,510.00 USD | 465.17 USD | 0.00 USD | `+9.93%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 44,920.00 USD | 411.53 USD | 0.00 USD | `+10.81%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 45,340.00 USD | 418.80 USD | 0.00 USD | `+11.18%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 45,630.00 USD | 285.70 USD | 0.00 USD | `+11.68%` | `3,194.00` |
| `Live` | `Short` | `0.0896` | 46,500.00 USD | 871.86 USD | 0.00 USD | `+11.81%` | `9,736.00` |
| `Live` | `Short` | `0.0900` | 46,730.00 USD | 226.85 USD | 0.00 USD | `+12.31%` | `2,522.00` |
| `Live` | `Short` | `0.0907` | 54,320.00 USD | 7,590.00 USD | 0.00 USD | `+13.31%` | `83,669.00` |
| `Live` | `Short` | `0.0911` | 55,360.00 USD | 1,040.00 USD | 0.00 USD | `+13.81%` | `11,378.00` |
| `Live` | `Short` | `0.0912` | 59,400.00 USD | 4,040.00 USD | 0.00 USD | `+13.93%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 59,570.00 USD | 171.19 USD | 0.00 USD | `+14.05%` | `1,874.00` |
| `Live` | `Short` | `0.0917` | 59,920.00 USD | 344.43 USD | 0.00 USD | `+14.55%` | `3,754.00` |
| `Live` | `Short` | `0.0921` | 60,090.00 USD | 171.49 USD | 0.00 USD | `+14.93%` | `1,863.00` |
| `Live` | `Short` | `0.0921` | 65,180.00 USD | 5,090.00 USD | 0.00 USD | `+15.05%` | `55,267.00` |
| `Live` | `Short` | `0.0935` | 68,480.00 USD | 3,300.00 USD | 0.00 USD | `+16.68%` | `35,291.00` |
| `Live` | `Short` | `0.0940` | 69,400.00 USD | 926.30 USD | 0.00 USD | `+17.43%` | `9,849.00` |
| `Live` | `Short` | `0.0949` | 83,760.00 USD | 14,360.00 USD | 0.00 USD | `+18.42%` | `151,355.00` |
| `Live` | `Short` | `0.0951` | 197,940.00 USD | 114,180.00 USD | 0.00 USD | `+18.80%` | `1,200,000.00` |
| `Live` | `Short` | `0.0961` | 198,550.00 USD | 609.59 USD | 0.00 USD | `+20.05%` | `6,340.00` |
| `Live` | `Short` | `0.0965` | 246,830.00 USD | 48,270.00 USD | 0.00 USD | `+20.55%` | `500,000.00` |
| `Live` | `Short` | `0.0979` | 286,020.00 USD | 39,190.00 USD | 0.00 USD | `+22.17%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 286,490.00 USD | 477.50 USD | 0.00 USD | `+22.67%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 297,010.00 USD | 10,510.00 USD | 0.00 USD | `+22.92%` | `106,785.00` |
| `Live` | `Short` | `0.0994` | 298,280.00 USD | 1,280.00 USD | 0.00 USD | `+24.17%` | `12,841.00` |
| `Live` | `Short` | `0.1012` | 300,000.00 USD | 1,710.00 USD | 0.00 USD | `+26.29%` | `16,923.00` |
| `Live` | `Short` | `0.1014` | 307,620.00 USD | 7,630.00 USD | 0.00 USD | `+26.67%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 313,150.00 USD | 5,530.00 USD | 0.00 USD | `+26.91%` | `54,384.00` |
| `Live` | `Short` | `0.1018` | 313,640.00 USD | 492.85 USD | 0.00 USD | `+27.16%` | `4,839.00` |
| `Live` | `Short` | `0.1060` | 316,820.00 USD | 3,170.00 USD | 0.00 USD | `+32.28%` | `29,960.00` |
| `Live` | `Short` | `0.1061` | 322,930.00 USD | 6,110.00 USD | 0.00 USD | `+32.53%` | `57,554.00` |
| `Live` | `Short` | `0.1111` | 326,370.00 USD | 3,450.00 USD | 0.00 USD | `+38.78%` | `31,000.00` |
| `Live` | `Short` | `0.1121` | 328,780.00 USD | 2,410.00 USD | 0.00 USD | `+40.02%` | `21,480.00` |
| `Live` | `Short` | `0.1123` | 329,120.00 USD | 336.75 USD | 0.00 USD | `+40.15%` | `3,000.00` |
| `Live` | `Short` | `0.1127` | 329,330.00 USD | 214.15 USD | 0.00 USD | `+40.65%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 329,470.00 USD | 142.88 USD | 0.00 USD | `+41.02%` | `1,265.00` |
| `Live` | `Short` | `0.1187` | 329,600.00 USD | 121.85 USD | 0.00 USD | `+48.14%` | `1,027.00` |
| `Live` | `Short` | `0.1192` | 329,820.00 USD | 222.33 USD | 0.00 USD | `+48.76%` | `1,866.00` |
| `Live` | `Short` | `0.1222` | 330,620.00 USD | 796.83 USD | 0.00 USD | `+52.64%` | `6,518.00` |
| `Live` | `Short` | `0.1265` | 2,900,000.00 USD | 2,570,000.00 USD | 0.00 USD | `+58.00%` | `20,285,883.00` |
| `Live` | `Short` | `0.1268` | 2,900,000.00 USD | 108.71 USD | 0.00 USD | `+58.38%` | `857.00` |
| `Live` | `Short` | `0.1295` | 2,900,000.00 USD | 611.86 USD | 0.00 USD | `+61.75%` | `4,723.00` |
| `Live` | `Short` | `0.1296` | 2,900,000.00 USD | 171.66 USD | 0.00 USD | `+61.87%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 2,900,000.00 USD | 2,140.00 USD | 0.00 USD | `+63.75%` | `16,310.00` |
| `Live` | `Short` | `0.1313` | 2,900,000.00 USD | 1,590.00 USD | 0.00 USD | `+63.87%` | `12,089.00` |
| `Live` | `Short` | `0.1318` | 2,900,000.00 USD | 102.97 USD | 0.00 USD | `+64.62%` | `781.00` |
| `Live` | `Short` | `0.1336` | 2,900,000.00 USD | 510.81 USD | 0.00 USD | `+66.87%` | `3,822.00` |
| `Live` | `Short` | `0.1338` | 2,900,000.00 USD | 205.31 USD | 0.00 USD | `+66.99%` | `1,535.00` |
| `Live` | `Short` | `0.1379` | 2,900,000.00 USD | 995.14 USD | 0.00 USD | `+72.11%` | `7,219.00` |
| `Live` | `Short` | `0.1381` | 2,910,000.00 USD | 1,800.00 USD | 0.00 USD | `+72.49%` | `13,010.00` |
| `Live` | `Short` | `0.1404` | 2,910,000.00 USD | 663.63 USD | 0.00 USD | `+75.36%` | `4,725.00` |
| `Live` | `Short` | `0.1406` | 2,930,000.00 USD | 22,810.00 USD | 0.00 USD | `+75.61%` | `162,180.00` |
| `Live` | `Short` | `0.1411` | 2,930,000.00 USD | 1,800.00 USD | 0.00 USD | `+76.23%` | `12,780.00` |
| `Live` | `Short` | `0.1414` | 2,960,000.00 USD | 32,620.00 USD | 0.00 USD | `+76.61%` | `230,621.00` |
| `Live` | `Short` | `0.1451` | 2,960,000.00 USD | 136.35 USD | 0.00 USD | `+81.10%` | `940.00` |
| `Live` | `Short` | `0.1464` | 2,960,000.00 USD | 387.51 USD | 0.00 USD | `+82.85%` | `2,646.00` |
| `Live` | `Short` | `0.1466` | 2,970,000.00 USD | 2,340.00 USD | 0.00 USD | `+82.97%` | `16,000.00` |
| `Live` | `Short` | `0.1479` | 2,980,000.00 USD | 8,360.00 USD | 0.00 USD | `+84.60%` | `56,553.00` |
| `Live` | `Short` | `0.1489` | 3,030,000.00 USD | 55,770.00 USD | 0.00 USD | `+85.97%` | `374,415.00` |
| `Live` | `Short` | `0.1509` | 3,030,000.00 USD | 340.62 USD | 0.00 USD | `+88.34%` | `2,258.00` |
| `Live` | `Short` | `0.1515` | 3,030,000.00 USD | 2,010.00 USD | 0.00 USD | `+89.22%` | `13,240.00` |
| `Live` | `Short` | `0.1525` | 3,030,000.00 USD | 267.55 USD | 0.00 USD | `+90.34%` | `1,755.00` |
| `Live` | `Short` | `0.1527` | 3,030,000.00 USD | 389.72 USD | 0.00 USD | `+90.59%` | `2,553.00` |
| `Live` | `Short` | `0.1555` | 3,030,000.00 USD | 338.10 USD | 0.00 USD | `+94.09%` | `2,175.00` |
| `Live` | `Short` | `0.1570` | 3,040,000.00 USD | 4,830.00 USD | 0.00 USD | `+95.96%` | `30,755.00` |
| `Live` | `Short` | `0.1570` | 3,040,000.00 USD | 980.15 USD | 0.00 USD | `+96.08%` | `6,241.00` |
| `Live` | `Short` | `0.1575` | 3,040,000.00 USD | 1,110.00 USD | 0.00 USD | `+96.71%` | `7,071.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 600,850.00 USD | 0.00 USD | 375.42 USD | `-67.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 600,480.00 USD | 0.00 USD | 409.59 USD | `-50.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 600,070.00 USD | 0.00 USD | 132.68 USD | `-49.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 599,930.00 USD | 0.00 USD | 286.87 USD | `-43.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 599,650.00 USD | 0.00 USD | 252.42 USD | `-42.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 599,390.00 USD | 0.00 USD | 468.67 USD | `-41.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 598,930.00 USD | 0.00 USD | 5,160.00 USD | `-38.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 593,770.00 USD | 0.00 USD | 920.48 USD | `-38.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 592,850.00 USD | 0.00 USD | 1,860.00 USD | `-37.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 590,980.00 USD | 0.00 USD | 175.41 USD | `-35.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 590,810.00 USD | 0.00 USD | 1,370.00 USD | `-30.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 589,440.00 USD | 0.00 USD | 437.58 USD | `-30.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 589,000.00 USD | 0.00 USD | 752.54 USD | `-26.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 588,250.00 USD | 0.00 USD | 9,830.00 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 578,410.00 USD | 0.00 USD | 1,270.00 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 577,140.00 USD | 0.00 USD | 1,560.00 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 575,580.00 USD | 0.00 USD | 134.12 USD | `-24.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 575,450.00 USD | 0.00 USD | 8,800.00 USD | `-24.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 566,650.00 USD | 0.00 USD | 504.26 USD | `-22.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 566,150.00 USD | 0.00 USD | 4,200.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 561,940.00 USD | 0.00 USD | 1,280.00 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 560,670.00 USD | 0.00 USD | 920.18 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 559,740.00 USD | 0.00 USD | 370.79 USD | `-19.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 559,370.00 USD | 0.00 USD | 1,130.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 558,250.00 USD | 0.00 USD | 362.24 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 557,880.00 USD | 0.00 USD | 3,140.00 USD | `-18.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 554,740.00 USD | 0.00 USD | 1,200.00 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 553,540.00 USD | 0.00 USD | 996.31 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 552,550.00 USD | 0.00 USD | 632.88 USD | `-16.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 551,920.00 USD | 0.00 USD | 115.57 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 551,800.00 USD | 0.00 USD | 33,620.00 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 518,170.00 USD | 0.00 USD | 12,860.00 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 505,310.00 USD | 0.00 USD | 1,260.00 USD | `-15.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 504,050.00 USD | 0.00 USD | 108.08 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 503,940.00 USD | 0.00 USD | 2,960.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 500,980.00 USD | 0.00 USD | 1,430.00 USD | `-15.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 499,550.00 USD | 0.00 USD | 7,990.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 491,560.00 USD | 0.00 USD | 8,580.00 USD | `-15.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 482,980.00 USD | 0.00 USD | 606.47 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 482,380.00 USD | 0.00 USD | 38,710.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 443,670.00 USD | 0.00 USD | 660.06 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 443,010.00 USD | 0.00 USD | 102.34 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 442,910.00 USD | 0.00 USD | 697.50 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 442,210.00 USD | 0.00 USD | 699.90 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 441,510.00 USD | 0.00 USD | 17,020.00 USD | `-12.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 424,490.00 USD | 0.00 USD | 895.27 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 423,590.00 USD | 0.00 USD | 523.23 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 423,070.00 USD | 0.00 USD | 235.12 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 422,840.00 USD | 0.00 USD | 134.92 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 422,700.00 USD | 0.00 USD | 107,230.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 315,470.00 USD | 0.00 USD | 12,930.00 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 302,540.00 USD | 0.00 USD | 20,070.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 282,470.00 USD | 0.00 USD | 233.74 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 282,240.00 USD | 0.00 USD | 16,880.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 265,360.00 USD | 0.00 USD | 1,670.00 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 263,690.00 USD | 0.00 USD | 4,710.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 258,980.00 USD | 0.00 USD | 15,380.00 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 243,600.00 USD | 0.00 USD | 413.42 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 243,180.00 USD | 0.00 USD | 703.43 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 242,480.00 USD | 0.00 USD | 621.12 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 241,860.00 USD | 0.00 USD | 1,700.00 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 240,160.00 USD | 0.00 USD | 29,060.00 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 211,100.00 USD | 0.00 USD | 976.95 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 210,120.00 USD | 0.00 USD | 2,090.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 208,030.00 USD | 0.00 USD | 28,750.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 179,280.00 USD | 0.00 USD | 2,710.00 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 176,580.00 USD | 0.00 USD | 115.12 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 176,460.00 USD | 0.00 USD | 4,680.00 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 171,780.00 USD | 0.00 USD | 1,640.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 170,140.00 USD | 0.00 USD | 2,900.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 167,240.00 USD | 0.00 USD | 107.66 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 167,140.00 USD | 0.00 USD | 5,000.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 162,140.00 USD | 0.00 USD | 1,410.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 160,730.00 USD | 0.00 USD | 375.86 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 160,350.00 USD | 0.00 USD | 193.90 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 160,160.00 USD | 0.00 USD | 140.04 USD | `-6.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 160,020.00 USD | 0.00 USD | 10,030.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 149,990.00 USD | 0.00 USD | 323.62 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 149,660.00 USD | 0.00 USD | 736.17 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 148,930.00 USD | 0.00 USD | 192.73 USD | `-5.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 148,730.00 USD | 0.00 USD | 358.13 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 148,380.00 USD | 0.00 USD | 4,880.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 143,500.00 USD | 0.00 USD | 193.49 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 143,300.00 USD | 0.00 USD | 2,280.00 USD | `-5.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 141,020.00 USD | 0.00 USD | 3,130.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 137,890.00 USD | 0.00 USD | 806.81 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0762` | 137,080.00 USD | 0.00 USD | 359.60 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0765` | 136,720.00 USD | 0.00 USD | 1,320.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 135,400.00 USD | 0.00 USD | 1,130.00 USD | `-4.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 134,280.00 USD | 0.00 USD | 3,540.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0767` | 130,740.00 USD | 0.00 USD | 176.91 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0769` | 130,560.00 USD | 0.00 USD | 193.74 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0770` | 130,370.00 USD | 0.00 USD | 11,510.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0771` | 118,860.00 USD | 0.00 USD | 4,340.00 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0772` | 114,520.00 USD | 0.00 USD | 4,340.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0774` | 110,180.00 USD | 0.00 USD | 323.40 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 109,860.00 USD | 0.00 USD | 2,450.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 107,410.00 USD | 0.00 USD | 604.81 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0776` | 106,810.00 USD | 0.00 USD | 992.37 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0777` | 105,820.00 USD | 0.00 USD | 41,810.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0779` | 64,010.00 USD | 0.00 USD | 17,270.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 46,740.00 USD | 0.00 USD | 3,000.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 43,730.00 USD | 0.00 USD | 1,700.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0781` | 42,040.00 USD | 0.00 USD | 1,350.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0783` | 40,690.00 USD | 0.00 USD | 120.66 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0784` | 40,570.00 USD | 0.00 USD | 4,200.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 36,370.00 USD | 0.00 USD | 573.31 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 35,790.00 USD | 0.00 USD | 166.84 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0786` | 35,630.00 USD | 0.00 USD | 495.57 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0788` | 35,130.00 USD | 0.00 USD | 3,030.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0789` | 32,100.00 USD | 0.00 USD | 497.86 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 31,600.00 USD | 0.00 USD | 706.60 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 30,900.00 USD | 0.00 USD | 10,230.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0791` | 20,670.00 USD | 0.00 USD | 4,600.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0793` | 16,070.00 USD | 0.00 USD | 2,260.00 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0794` | 13,810.00 USD | 0.00 USD | 1,010.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0795` | 12,800.00 USD | 0.00 USD | 148.25 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0795` | 12,650.00 USD | 0.00 USD | 248.91 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0796` | 12,400.00 USD | 0.00 USD | 2,130.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0798` | 10,270.00 USD | 0.00 USD | 342.85 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0799` | 9,930.00 USD | 0.00 USD | 4,460.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0799` | 5,460.00 USD | 0.00 USD | 1,120.00 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0800` | 4,350.00 USD | 0.00 USD | 4,350.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 443.63 USD | 443.63 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 789.67 USD | 346.04 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 931.00 USD | 141.34 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 1,640.00 USD | 707.08 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 3,900.00 USD | 2,260.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 100,680.00 USD | 96,780.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 100,950.00 USD | 264.54 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 103,100.00 USD | 2,160.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 103,530.00 USD | 424.74 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 104,530.00 USD | 1,010.00 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 105,920.00 USD | 1,380.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 106,180.00 USD | 264.63 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 107,610.00 USD | 1,430.00 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 108,110.00 USD | 492.77 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 109,480.00 USD | 1,380.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 112,400.00 USD | 2,920.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 121,760.00 USD | 9,360.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 124,770.00 USD | 3,010.00 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 125,300.00 USD | 534.72 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 125,710.00 USD | 402.62 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 139,500.00 USD | 13,790.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 143,480.00 USD | 3,980.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 144,000.00 USD | 512.05 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 145,070.00 USD | 1,080.00 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 145,460.00 USD | 389.31 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 145,770.00 USD | 303.56 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 145,880.00 USD | 112.89 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 146,260.00 USD | 381.45 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 146,420.00 USD | 155.82 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 146,820.00 USD | 399.52 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 147,170.00 USD | 348.82 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 148,430.00 USD | 1,260.00 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 148,640.00 USD | 210.88 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,900,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,900,000.00 USD | 3,380.00 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,900,000.00 USD | 692.34 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,900,000.00 USD | 107.71 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,910,000.00 USD | 2,690.00 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,910,000.00 USD | 1,330.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,910,000.00 USD | 2,360.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,910,000.00 USD | 326.97 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,910,000.00 USD | 242.84 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,920,000.00 USD | 10,140.00 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 1,920,000.00 USD | 152.92 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,920,000.00 USD | 876.11 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,920,000.00 USD | 205.59 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,920,000.00 USD | 126.76 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,920,000.00 USD | 307.41 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,920,000.00 USD | 942.20 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,930,000.00 USD | 644.62 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 1,930,000.00 USD | 180.45 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,930,000.00 USD | 2,020.00 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,970,000.00 USD | 43,760.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0864` | 1,970,000.00 USD | 164.86 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 1,970,000.00 USD | 1,080.00 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 1,970,000.00 USD | 384.06 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 1,970,000.00 USD | 1,840.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 1,970,000.00 USD | 117.71 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 1,970,000.00 USD | 111.61 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 1,980,000.00 USD | 571.18 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 1,980,000.00 USD | 375.94 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 1,980,000.00 USD | 627.55 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 1,980,000.00 USD | 211.04 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 1,980,000.00 USD | 108.36 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 1,980,000.00 USD | 543.32 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 1,980,000.00 USD | 1,820.00 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 1,980,000.00 USD | 2,080.00 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,000,000.00 USD | 17,680.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,000,000.00 USD | 1,810.00 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,000,000.00 USD | 1,640.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,010,000.00 USD | 5,340.00 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,010,000.00 USD | 1,090.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,010,000.00 USD | 224.86 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,030,000.00 USD | 20,540.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,030,000.00 USD | 114.93 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,030,000.00 USD | 840.47 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,030,000.00 USD | 173.36 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,040,000.00 USD | 4,690.00 USD | 0.00 USD | `+14.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,040,000.00 USD | 1,970.00 USD | 0.00 USD | `+14.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,040,000.00 USD | 2,170.00 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,040,000.00 USD | 541.32 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,180,000.00 USD | 137,500.00 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,180,000.00 USD | 691.07 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,180,000.00 USD | 6,250.00 USD | 0.00 USD | `+15.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,200,000.00 USD | 13,480.00 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,200,000.00 USD | 734.82 USD | 0.00 USD | `+16.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,200,000.00 USD | 1,230.00 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,200,000.00 USD | 184.09 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,200,000.00 USD | 1,120.00 USD | 0.00 USD | `+17.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,200,000.00 USD | 1,860.00 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,200,000.00 USD | 512.15 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,210,000.00 USD | 6,620.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,210,000.00 USD | 404.96 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,210,000.00 USD | 129.85 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,210,000.00 USD | 3,740.00 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,220,000.00 USD | 2,400.00 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,220,000.00 USD | 409.17 USD | 0.00 USD | `+19.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,220,000.00 USD | 203.74 USD | 0.00 USD | `+20.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,220,000.00 USD | 2,800.00 USD | 0.00 USD | `+21.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,220,000.00 USD | 1,320.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,220,000.00 USD | 694.56 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,220,000.00 USD | 940.91 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,230,000.00 USD | 2,980.00 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,230,000.00 USD | 104.99 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,230,000.00 USD | 1,930.00 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,230,000.00 USD | 1,490.00 USD | 0.00 USD | `+24.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,230,000.00 USD | 1,090.00 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,230,000.00 USD | 438.96 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,230,000.00 USD | 973.76 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,350,000.00 USD | 113,580.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,350,000.00 USD | 175.59 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,350,000.00 USD | 588.78 USD | 0.00 USD | `+25.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,350,000.00 USD | 201.90 USD | 0.00 USD | `+26.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,350,000.00 USD | 489.46 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,350,000.00 USD | 103.68 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,350,000.00 USD | 203.70 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,350,000.00 USD | 3,810.00 USD | 0.00 USD | `+27.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,360,000.00 USD | 11,200.00 USD | 0.00 USD | `+27.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,370,000.00 USD | 4,330.00 USD | 0.00 USD | `+27.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,370,000.00 USD | 205.50 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,370,000.00 USD | 1,540.00 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,370,000.00 USD | 207.50 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,370,000.00 USD | 813.88 USD | 0.00 USD | `+30.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,390,000.00 USD | 23,160.00 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,390,000.00 USD | 781.51 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,390,000.00 USD | 209.30 USD | 0.00 USD | `+30.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,400,000.00 USD | 1,440.00 USD | 0.00 USD | `+30.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,400,000.00 USD | 5,140.00 USD | 0.00 USD | `+31.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,400,000.00 USD | 585.32 USD | 0.00 USD | `+31.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,400,000.00 USD | 210.90 USD | 0.00 USD | `+31.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,400,000.00 USD | 1,850.00 USD | 0.00 USD | `+31.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,400,000.00 USD | 105.75 USD | 0.00 USD | `+32.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,410,000.00 USD | 3,220.00 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,410,000.00 USD | 1,600.00 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,410,000.00 USD | 212.90 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,410,000.00 USD | 472.63 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,410,000.00 USD | 214.50 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,410,000.00 USD | 1,040.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,410,000.00 USD | 136.12 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,410,000.00 USD | 216.10 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,450,000.00 USD | 40,920.00 USD | 0.00 USD | `+35.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,450,000.00 USD | 217.90 USD | 0.00 USD | `+36.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,450,000.00 USD | 219.70 USD | 0.00 USD | `+37.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,460,000.00 USD | 7,920.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,460,000.00 USD | 154.22 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,460,000.00 USD | 221.30 USD | 0.00 USD | `+38.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,460,000.00 USD | 1,050.00 USD | 0.00 USD | `+38.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,490,000.00 USD | 24,440.00 USD | 0.00 USD | `+38.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,490,000.00 USD | 223.10 USD | 0.00 USD | `+39.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,490,000.00 USD | 2,120.00 USD | 0.00 USD | `+40.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,490,000.00 USD | 226.30 USD | 0.00 USD | `+41.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,490,000.00 USD | 351.57 USD | 0.00 USD | `+42.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,490,000.00 USD | 950.34 USD | 0.00 USD | `+42.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,490,000.00 USD | 229.50 USD | 0.00 USD | `+43.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,490,000.00 USD | 771.08 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,490,000.00 USD | 230.90 USD | 0.00 USD | `+44.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,490,000.00 USD | 288.18 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,490,000.00 USD | 619.10 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,490,000.00 USD | 1,250.00 USD | 0.00 USD | `+44.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,490,000.00 USD | 1,050.00 USD | 0.00 USD | `+44.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,490,000.00 USD | 232.30 USD | 0.00 USD | `+45.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,500,000.00 USD | 1,600.00 USD | 0.00 USD | `+45.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,500,000.00 USD | 3,730.00 USD | 0.00 USD | `+46.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,500,000.00 USD | 676.22 USD | 0.00 USD | `+47.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,500,000.00 USD | 648.25 USD | 0.00 USD | `+47.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,500,000.00 USD | 1,510.00 USD | 0.00 USD | `+47.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,500,000.00 USD | 448.52 USD | 0.00 USD | `+47.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,500,000.00 USD | 136.93 USD | 0.00 USD | `+48.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,500,000.00 USD | 433.07 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,510,000.00 USD | 691.80 USD | 0.00 USD | `+49.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,620,000.00 USD | 118,550.00 USD | 0.00 USD | `+49.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,620,000.00 USD | 143.22 USD | 0.00 USD | `+50.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,630,000.00 USD | 803.95 USD | 0.00 USD | `+50.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,630,000.00 USD | 1,380.00 USD | 0.00 USD | `+51.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,630,000.00 USD | 2,270.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,630,000.00 USD | 871.99 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,650,000.00 USD | 24,560.00 USD | 0.00 USD | `+58.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,650,000.00 USD | 400.21 USD | 0.00 USD | `+58.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,670,000.00 USD | 13,850.00 USD | 0.00 USD | `+64.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,670,000.00 USD | 2,360.00 USD | 0.00 USD | `+64.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,680,000.00 USD | 4,160.00 USD | 0.00 USD | `+69.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,680,000.00 USD | 235.54 USD | 0.00 USD | `+74.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,680,000.00 USD | 1,160.00 USD | 0.00 USD | `+76.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,680,000.00 USD | 173.57 USD | 0.00 USD | `+77.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,680,000.00 USD | 380.09 USD | 0.00 USD | `+77.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,690,000.00 USD | 17,150.00 USD | 0.00 USD | `+77.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,690,000.00 USD | 433.35 USD | 0.00 USD | `+80.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,700,000.00 USD | 3,640.00 USD | 0.00 USD | `+83.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,750,000.00 USD | 55,720.00 USD | 0.00 USD | `+84.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,760,000.00 USD | 2,120.00 USD | 0.00 USD | `+85.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,770,000.00 USD | 18,810.00 USD | 0.00 USD | `+87.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1532` | 2,780,000.00 USD | 4,750.00 USD | 0.00 USD | `+91.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1552` | 2,780,000.00 USD | 630.53 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1590` | 2,780,000.00 USD | 2,670.00 USD | 0.00 USD | `+98.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1600` | 2,780,000.00 USD | 131.40 USD | 0.00 USD | `+99.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1601` | 2,790,000.00 USD | 3,320.00 USD | 0.00 USD | `+99.96%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0695` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 275,490.00 USD | 222,260.00 USD | 212,870.00 USD |
| `7D` | `0.0696` | 59,700,000.00 USD | 0.00 USD | 59,700,000.00 USD | 100,230.00 USD | 61,080.00 USD | 187,260.00 USD |
| `7D` | `0.0697` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 41,960.00 USD | 87,540.00 USD | 77,050.00 USD |
| `7D` | `0.0698` | 59,140,000.00 USD | 0.00 USD | 59,140,000.00 USD | 127,350.00 USD | 103,870.00 USD | 70,680.00 USD |
| `7D` | `0.0699` | 58,840,000.00 USD | 0.00 USD | 58,840,000.00 USD | 172,730.00 USD | 101,580.00 USD | 64,460.00 USD |
| `7D` | `0.0700` | 58,500,000.00 USD | 0.00 USD | 58,500,000.00 USD | 87,550.00 USD | 110,810.00 USD | 85,510.00 USD |
| `7D` | `0.0701` | 58,220,000.00 USD | 0.00 USD | 58,220,000.00 USD | 115,700.00 USD | 8,980.00 USD | 55,400.00 USD |
| `7D` | `0.0702` | 58,040,000.00 USD | 0.00 USD | 58,040,000.00 USD | 100,200.00 USD | 38,000.00 USD | 50,380.00 USD |
| `7D` | `0.0703` | 57,850,000.00 USD | 0.00 USD | 57,850,000.00 USD | 85,670.00 USD | 23,160.00 USD | 747.55 USD |
| `7D` | `0.0704` | 57,740,000.00 USD | 0.00 USD | 57,740,000.00 USD | 91,490.00 USD | 55,790.00 USD | 17,160.00 USD |
| `7D` | `0.0705` | 57,570,000.00 USD | 0.00 USD | 57,570,000.00 USD | 81,490.00 USD | 84,030.00 USD | 59,310.00 USD |
| `7D` | `0.0706` | 57,350,000.00 USD | 0.00 USD | 57,350,000.00 USD | 15,880.00 USD | 20,950.00 USD | 45,310.00 USD |
| `7D` | `0.0707` | 57,270,000.00 USD | 0.00 USD | 57,270,000.00 USD | 168,600.00 USD | 48,670.00 USD | 98,440.00 USD |
| `7D` | `0.0708` | 56,950,000.00 USD | 0.00 USD | 56,950,000.00 USD | 10,780.00 USD | 30,220.00 USD | 342.91 USD |
| `7D` | `0.0709` | 56,910,000.00 USD | 0.00 USD | 56,910,000.00 USD | 44,800.00 USD | 68,720.00 USD | 36,160.00 USD |
| `7D` | `0.0710` | 56,760,000.00 USD | 0.00 USD | 56,760,000.00 USD | 189,250.00 USD | 50,450.00 USD | 61,030.00 USD |
| `7D` | `0.0711` | 56,460,000.00 USD | 0.00 USD | 56,460,000.00 USD | 138,080.00 USD | 106,700.00 USD | 38,750.00 USD |
| `7D` | `0.0712` | 56,180,000.00 USD | 0.00 USD | 56,180,000.00 USD | 109,400.00 USD | 41,030.00 USD | 952.84 USD |
| `7D` | `0.0713` | 56,030,000.00 USD | 0.00 USD | 56,030,000.00 USD | 120,050.00 USD | 68,300.00 USD | 59,380.00 USD |
| `7D` | `0.0714` | 55,780,000.00 USD | 0.00 USD | 55,780,000.00 USD | 115,970.00 USD | 74,740.00 USD | 53,640.00 USD |
| `7D` | `0.0715` | 55,530,000.00 USD | 0.00 USD | 55,530,000.00 USD | 129,130.00 USD | 0.00 USD | 31,330.00 USD |
| `7D` | `0.0716` | 55,370,000.00 USD | 0.00 USD | 55,370,000.00 USD | 186,200.00 USD | 42,190.00 USD | 42,050.00 USD |
| `1D` | `0.0717` | 24,720,000.00 USD | 0.00 USD | 24,720,000.00 USD | 80,570.00 USD | 27,450.00 USD | 48,720.00 USD |
| `7D` | `0.0717` | 55,100,000.00 USD | 0.00 USD | 55,100,000.00 USD | 153,600.00 USD | 1,810.00 USD | 50,090.00 USD |
| `1D` | `0.0718` | 24,560,000.00 USD | 0.00 USD | 24,560,000.00 USD | 63,040.00 USD | 40,570.00 USD | 50,790.00 USD |
| `7D` | `0.0718` | 54,900,000.00 USD | 0.00 USD | 54,900,000.00 USD | 64,100.00 USD | 39,280.00 USD | 48,670.00 USD |
| `1D` | `0.0719` | 24,410,000.00 USD | 0.00 USD | 24,410,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `7D` | `0.0719` | 54,750,000.00 USD | 0.00 USD | 54,750,000.00 USD | 162,420.00 USD | 51,730.00 USD | 51,680.00 USD |
| `1D` | `0.0720` | 24,380,000.00 USD | 0.00 USD | 24,380,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0720` | 54,480,000.00 USD | 0.00 USD | 54,480,000.00 USD | 115,550.00 USD | 72,080.00 USD | 52,210.00 USD |
| `1D` | `0.0721` | 24,280,000.00 USD | 0.00 USD | 24,280,000.00 USD | 33,000.00 USD | 10,770.00 USD | 12,510.00 USD |
| `7D` | `0.0721` | 54,240,000.00 USD | 0.00 USD | 54,240,000.00 USD | 91,320.00 USD | 58,090.00 USD | 27,780.00 USD |
| `1D` | `0.0722` | 24,230,000.00 USD | 0.00 USD | 24,230,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,970.00 USD |
| `7D` | `0.0722` | 54,060,000.00 USD | 0.00 USD | 54,060,000.00 USD | 76,700.00 USD | 4,070.00 USD | 37,120.00 USD |
| `1D` | `0.0723` | 24,150,000.00 USD | 0.00 USD | 24,150,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,860.00 USD |
| `7D` | `0.0723` | 53,940,000.00 USD | 0.00 USD | 53,940,000.00 USD | 154,040.00 USD | 7,890.00 USD | 45,940.00 USD |
| `1D` | `0.0724` | 24,040,000.00 USD | 0.00 USD | 24,040,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,070.00 USD |
| `7D` | `0.0724` | 53,740,000.00 USD | 0.00 USD | 53,740,000.00 USD | 133,990.00 USD | 7,390.00 USD | 48,290.00 USD |
| `1D` | `0.0725` | 23,910,000.00 USD | 0.00 USD | 23,910,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,900.00 USD |
| `7D` | `0.0725` | 53,550,000.00 USD | 0.00 USD | 53,550,000.00 USD | 177,800.00 USD | 33,630.00 USD | 651.74 USD |
| `1D` | `0.0726` | 23,750,000.00 USD | 0.00 USD | 23,750,000.00 USD | 31,660.00 USD | 0.00 USD | 142.34 USD |
| `7D` | `0.0726` | 53,330,000.00 USD | 0.00 USD | 53,330,000.00 USD | 99,500.00 USD | 82,410.00 USD | 64,010.00 USD |
| `1D` | `0.0727` | 23,720,000.00 USD | 0.00 USD | 23,720,000.00 USD | 20,420.00 USD | 0.00 USD | 200.42 USD |
| `7D` | `0.0727` | 53,090,000.00 USD | 0.00 USD | 53,090,000.00 USD | 139,640.00 USD | 0.00 USD | 1,160.00 USD |
| `1D` | `0.0728` | 23,700,000.00 USD | 0.00 USD | 23,700,000.00 USD | 15,580.00 USD | 802.30 USD | 419.85 USD |
| `7D` | `0.0728` | 52,950,000.00 USD | 0.00 USD | 52,950,000.00 USD | 49,930.00 USD | 89,490.00 USD | 139,530.00 USD |
| `1D` | `0.0729` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 17,820.00 USD | 0.00 USD | 18,720.00 USD |
| `7D` | `0.0729` | 52,670,000.00 USD | 0.00 USD | 52,670,000.00 USD | 88,690.00 USD | 55,500.00 USD | 2,240.00 USD |
| `1D` | `0.0730` | 23,640,000.00 USD | 0.00 USD | 23,640,000.00 USD | 14,450.00 USD | 0.00 USD | 223.21 USD |
| `7D` | `0.0730` | 52,520,000.00 USD | 0.00 USD | 52,520,000.00 USD | 105,630.00 USD | 11,900.00 USD | 1,280.00 USD |
| `1D` | `0.0731` | 23,630,000.00 USD | 0.00 USD | 23,630,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD |
| `7D` | `0.0731` | 52,400,000.00 USD | 0.00 USD | 52,400,000.00 USD | 176,670.00 USD | 203,190.00 USD | 63,020.00 USD |
| `1D` | `0.0732` | 23,590,000.00 USD | 0.00 USD | 23,590,000.00 USD | 42,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0732` | 51,960,000.00 USD | 0.00 USD | 51,960,000.00 USD | 620,130.00 USD | 453,660.00 USD | 30,500.00 USD |
| `1D` | `0.0733` | 23,540,000.00 USD | 0.00 USD | 23,540,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0733` | 50,860,000.00 USD | 0.00 USD | 50,860,000.00 USD | 289,650.00 USD | 18,570.00 USD | 40,440.00 USD |
| `1D` | `0.0734` | 23,530,000.00 USD | 0.00 USD | 23,530,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 342,630.00 USD | 172,240.00 USD | 22,980.00 USD |
| `1D` | `0.0735` | 23,530,000.00 USD | 0.00 USD | 23,530,000.00 USD | 24,100.00 USD | 0.00 USD | 41.24 USD |
| `7D` | `0.0735` | 49,970,000.00 USD | 0.00 USD | 49,970,000.00 USD | 252,620.00 USD | 244,020.00 USD | 137,160.00 USD |
| `1D` | `0.0736` | 23,500,000.00 USD | 0.00 USD | 23,500,000.00 USD | 9,980.00 USD | 0.00 USD | 258.52 USD |
| `7D` | `0.0736` | 49,340,000.00 USD | 0.00 USD | 49,340,000.00 USD | 392,100.00 USD | 244,990.00 USD | 229,880.00 USD |
| `1D` | `0.0737` | 23,490,000.00 USD | 0.00 USD | 23,490,000.00 USD | 47,420.00 USD | 0.00 USD | 983.61 USD |
| `7D` | `0.0737` | 48,470,000.00 USD | 0.00 USD | 48,470,000.00 USD | 340,530.00 USD | 126,240.00 USD | 172,530.00 USD |
| `1D` | `0.0738` | 23,450,000.00 USD | 0.00 USD | 23,450,000.00 USD | 39,420.00 USD | 0.00 USD | 725.86 USD |
| `7D` | `0.0738` | 47,830,000.00 USD | 0.00 USD | 47,830,000.00 USD | 390,250.00 USD | 258,710.00 USD | 137,740.00 USD |
| `1D` | `0.0739` | 23,410,000.00 USD | 0.00 USD | 23,410,000.00 USD | 37,380.00 USD | 0.00 USD | 33.30 USD |
| `7D` | `0.0739` | 47,040,000.00 USD | 0.00 USD | 47,040,000.00 USD | 523,610.00 USD | 388,780.00 USD | 147,140.00 USD |
| `1D` | `0.0740` | 23,370,000.00 USD | 0.00 USD | 23,370,000.00 USD | 29,230.00 USD | 0.00 USD | 267.65 USD |
| `7D` | `0.0740` | 45,980,000.00 USD | 0.00 USD | 45,980,000.00 USD | 631,590.00 USD | 498,260.00 USD | 422,600.00 USD |
| `1D` | `0.0741` | 23,340,000.00 USD | 0.00 USD | 23,340,000.00 USD | 37,860.00 USD | 0.00 USD | 2,410.00 USD |
| `7D` | `0.0741` | 44,430,000.00 USD | 0.00 USD | 44,430,000.00 USD | 401,620.00 USD | 636,410.00 USD | 454,290.00 USD |
| `1D` | `0.0742` | 23,300,000.00 USD | 0.00 USD | 23,300,000.00 USD | 35,050.00 USD | 0.00 USD | 145.18 USD |
| `7D` | `0.0742` | 42,940,000.00 USD | 0.00 USD | 42,940,000.00 USD | 614,090.00 USD | 186,930.00 USD | 485,600.00 USD |
| `1D` | `0.0743` | 23,260,000.00 USD | 0.00 USD | 23,260,000.00 USD | 37,380.00 USD | 27,500.00 USD | 162.32 USD |
| `7D` | `0.0743` | 41,650,000.00 USD | 0.00 USD | 41,650,000.00 USD | 226,940.00 USD | 547,750.00 USD | 528,640.00 USD |
| `1D` | `0.0744` | 23,200,000.00 USD | 0.00 USD | 23,200,000.00 USD | 41,590.00 USD | 1,840.00 USD | 15,430.00 USD |
| `7D` | `0.0744` | 40,350,000.00 USD | 0.00 USD | 40,350,000.00 USD | 293,650.00 USD | 339,640.00 USD | 134,100.00 USD |
| `1D` | `0.0745` | 23,140,000.00 USD | 0.00 USD | 23,140,000.00 USD | 105,300.00 USD | 57,220.00 USD | 24,900.00 USD |
| `7D` | `0.0745` | 39,580,000.00 USD | 0.00 USD | 39,580,000.00 USD | 475,750.00 USD | 324,390.00 USD | 205,550.00 USD |
| `1D` | `0.0746` | 22,950,000.00 USD | 0.00 USD | 22,950,000.00 USD | 237,520.00 USD | 175,410.00 USD | 125,570.00 USD |
| `7D` | `0.0746` | 38,580,000.00 USD | 0.00 USD | 38,580,000.00 USD | 726,840.00 USD | 775,280.00 USD | 367,080.00 USD |
| `1D` | `0.0747` | 22,410,000.00 USD | 0.00 USD | 22,410,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,440.00 USD |
| `7D` | `0.0747` | 36,710,000.00 USD | 0.00 USD | 36,710,000.00 USD | 700,250.00 USD | 785,240.00 USD | 292,540.00 USD |
| `1D` | `0.0748` | 21,960,000.00 USD | 0.00 USD | 21,960,000.00 USD | 169,810.00 USD | 65,720.00 USD | 98,750.00 USD |
| `7D` | `0.0748` | 34,930,000.00 USD | 0.00 USD | 34,930,000.00 USD | 790,190.00 USD | 324,980.00 USD | 184,930.00 USD |
| `1D` | `0.0749` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,040.00 USD |
| `7D` | `0.0749` | 33,630,000.00 USD | 0.00 USD | 33,630,000.00 USD | 565,400.00 USD | 124,000.00 USD | 136,380.00 USD |
| `1D` | `0.0750` | 21,270,000.00 USD | 0.00 USD | 21,270,000.00 USD | 235,680.00 USD | 83,730.00 USD | 121,130.00 USD |
| `7D` | `0.0750` | 32,800,000.00 USD | 0.00 USD | 32,800,000.00 USD | 594,740.00 USD | 328,340.00 USD | 87,170.00 USD |
| `1D` | `0.0751` | 20,830,000.00 USD | 0.00 USD | 20,830,000.00 USD | 277,260.00 USD | 82,120.00 USD | 66,910.00 USD |
| `7D` | `0.0751` | 31,790,000.00 USD | 0.00 USD | 31,790,000.00 USD | 711,020.00 USD | 471,800.00 USD | 102,000.00 USD |
| `1D` | `0.0752` | 20,410,000.00 USD | 0.00 USD | 20,410,000.00 USD | 124,190.00 USD | 19,450.00 USD | 85,750.00 USD |
| `7D` | `0.0752` | 30,510,000.00 USD | 0.00 USD | 30,510,000.00 USD | 781,620.00 USD | 613,570.00 USD | 642,030.00 USD |
| `1D` | `0.0753` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 127,320.00 USD | 72,710.00 USD | 28,530.00 USD |
| `7D` | `0.0753` | 28,470,000.00 USD | 0.00 USD | 28,470,000.00 USD | 513,580.00 USD | 354,150.00 USD | 394,590.00 USD |
| `1D` | `0.0754` | 19,950,000.00 USD | 0.00 USD | 19,950,000.00 USD | 95,400.00 USD | 62,330.00 USD | 21,670.00 USD |
| `7D` | `0.0754` | 27,210,000.00 USD | 0.00 USD | 27,210,000.00 USD | 306,180.00 USD | 610,950.00 USD | 339,700.00 USD |
| `1D` | `0.0755` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 122,130.00 USD | 15,650.00 USD | 68,560.00 USD |
| `7D` | `0.0755` | 25,950,000.00 USD | 0.00 USD | 25,950,000.00 USD | 670,760.00 USD | 794,430.00 USD | 392,050.00 USD |
| `1D` | `0.0756` | 19,560,000.00 USD | 0.00 USD | 19,560,000.00 USD | 177,070.00 USD | 157,590.00 USD | 111,780.00 USD |
| `7D` | `0.0756` | 24,090,000.00 USD | 0.00 USD | 24,090,000.00 USD | 901,040.00 USD | 1,260,000.00 USD | 876,520.00 USD |
| `1D` | `0.0757` | 19,120,000.00 USD | 0.00 USD | 19,120,000.00 USD | 106,380.00 USD | 44,790.00 USD | 104,970.00 USD |
| `7D` | `0.0757` | 21,060,000.00 USD | 0.00 USD | 21,060,000.00 USD | 764,320.00 USD | 1,040,000.00 USD | 628,410.00 USD |
| `1D` | `0.0758` | 18,860,000.00 USD | 0.00 USD | 18,860,000.00 USD | 77,300.00 USD | 42,980.00 USD | 31,840.00 USD |
| `7D` | `0.0758` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 675,880.00 USD | 568,850.00 USD | 910,610.00 USD |
| `1D` | `0.0759` | 18,710,000.00 USD | 0.00 USD | 18,710,000.00 USD | 116,240.00 USD | 85,920.00 USD | 9,610.00 USD |
| `7D` | `0.0759` | 16,470,000.00 USD | 0.00 USD | 16,470,000.00 USD | 504,200.00 USD | 819,420.00 USD | 304,400.00 USD |
| `1D` | `0.0760` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 285,080.00 USD | 289,180.00 USD | 216,150.00 USD |
| `7D` | `0.0760` | 14,840,000.00 USD | 0.00 USD | 14,840,000.00 USD | 980,060.00 USD | 846,650.00 USD | 632,210.00 USD |
| `1D` | `0.0761` | 17,710,000.00 USD | 0.00 USD | 17,710,000.00 USD | 477,110.00 USD | 391,680.00 USD | 272,010.00 USD |
| `7D` | `0.0761` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 886,790.00 USD | 569,460.00 USD | 472,950.00 USD |
| `1D` | `0.0762` | 16,570,000.00 USD | 0.00 USD | 16,570,000.00 USD | 510,560.00 USD | 248,230.00 USD | 179,730.00 USD |
| `7D` | `0.0762` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 309,500.00 USD | 473,290.00 USD | 312,370.00 USD |
| `1D` | `0.0763` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 360,900.00 USD | 139,670.00 USD | 197,140.00 USD |
| `7D` | `0.0763` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 639,910.00 USD | 247,960.00 USD | 102,280.00 USD |
| `1D` | `0.0764` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 396,130.00 USD | 346,900.00 USD | 90,870.00 USD |
| `7D` | `0.0764` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 796,120.00 USD | 232,730.00 USD | 166,140.00 USD |
| `1D` | `0.0765` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 551,690.00 USD | 223,110.00 USD | 314,140.00 USD |
| `7D` | `0.0765` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 554,010.00 USD | 105,240.00 USD | 189,820.00 USD |
| `1D` | `0.0766` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 620,360.00 USD | 272,640.00 USD | 280,190.00 USD |
| `7D` | `0.0766` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 389,230.00 USD | 407,670.00 USD | 188,220.00 USD |
| `1D` | `0.0767` | 11,830,000.00 USD | 0.00 USD | 11,830,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,850.00 USD |
| `7D` | `0.0767` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 575,100.00 USD | 232,660.00 USD | 330,110.00 USD |
| `1D` | `0.0768` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 407,610.00 USD | 236,860.00 USD | 142,100.00 USD |
| `7D` | `0.0768` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 146,960.00 USD | 67,680.00 USD | 124,240.00 USD |
| `1D` | `0.0769` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 227,680.00 USD | 170,840.00 USD | 70,010.00 USD |
| `7D` | `0.0769` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 133,640.00 USD | 100,180.00 USD | 177,930.00 USD |
| `1D` | `0.0770` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,410.00 USD |
| `7D` | `0.0770` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 177,520.00 USD | 80,840.00 USD | 292,850.00 USD |
| `1D` | `0.0771` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 231,550.00 USD | 266,030.00 USD | 190,250.00 USD |
| `7D` | `0.0771` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 80,530.00 USD | 229,090.00 USD | 107,220.00 USD |
| `1D` | `0.0772` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 169,730.00 USD | 318,140.00 USD | 333,150.00 USD |
| `7D` | `0.0772` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 176,460.00 USD | 444,720.00 USD | 171,150.00 USD |
| `1D` | `0.0773` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 302,180.00 USD | 151,140.00 USD | 241,270.00 USD |
| `7D` | `0.0773` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 810,310.00 USD | 335,090.00 USD | 281,070.00 USD |
| `1D` | `0.0774` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 165,350.00 USD | 98,170.00 USD | 108,170.00 USD |
| `7D` | `0.0774` | 260,170.00 USD | 0.00 USD | 260,170.00 USD | 51,030.00 USD | 36,700.00 USD | 133,010.00 USD |
| `1D` | `0.0775` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 181,290.00 USD | 12,820.00 USD | 17,130.00 USD |
| `7D` | `0.0775` | 39,430.00 USD | 0.00 USD | 39,430.00 USD | 0.00 USD | 23,390.00 USD | 0.00 USD |
| `1D` | `0.0776` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 106,410.00 USD | 237,880.00 USD | 232,080.00 USD |
| `1D` | `0.0777` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 18,430.00 USD | 56,290.00 USD | 146.30 USD |
| `1D` | `0.0778` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 6,440.00 USD | 0.00 USD | 68,580.00 USD |
| `1D` | `0.0779` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 253.82 USD |
| `1D` | `0.0780` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 138,400.00 USD | 30,070.00 USD | 0.00 USD |
| `1D` | `0.0781` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD |
| `7D` | `0.0781` | 16,040.00 USD | 0.00 USD | 16,040.00 USD | 0.00 USD | 16,040.00 USD | 0.00 USD |
| `1D` | `0.0782` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 44,780.00 USD | 71,230.00 USD | 85,130.00 USD |
| `7D` | `0.0782` | 18,880.00 USD | 18,880.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | 1,220.00 USD |
| `7D` | `0.0782` | 37,750.00 USD | 37,750.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | 1,220.00 USD |
| `1D` | `0.0783` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD |
| `7D` | `0.0783` | 44,400.00 USD | 44,400.00 USD | 0.00 USD | 0.00 USD | 6,650.00 USD | 0.00 USD |
| `1D` | `0.0784` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 229,040.00 USD | 132,460.00 USD | 158,340.00 USD |
| `7D` | `0.0784` | 144,040.00 USD | 144,040.00 USD | 0.00 USD | 0.00 USD | 99,640.00 USD | 0.00 USD |
| `1D` | `0.0785` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 168,930.00 USD | 66,050.00 USD | 61,840.00 USD |
| `7D` | `0.0785` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD |
| `1D` | `0.0786` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 91,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0787` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD |
| `7D` | `0.0787` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 1,000,000.00 USD | 122,780.00 USD | 0.00 USD |
| `1D` | `0.0788` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD |
| `7D` | `0.0788` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 115,040.00 USD |
| `1D` | `0.0789` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD |
| `1D` | `0.0790` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 200,610.00 USD | 137,240.00 USD | 50,580.00 USD |
| `7D` | `0.0790` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD |
| `1D` | `0.0791` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 76,010.00 USD | 3,690.00 USD | 30,030.00 USD |
| `7D` | `0.0791` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 50,940.00 USD | 91,430.00 USD | 47,070.00 USD |
| `1D` | `0.0792` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD |
| `7D` | `0.0792` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 73,810.00 USD | 39,590.00 USD |
| `1D` | `0.0793` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 33,790.00 USD | 0.00 USD |
| `7D` | `0.0793` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 467,940.00 USD | 277,070.00 USD | 241,850.00 USD |
| `1D` | `0.0794` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 466,850.00 USD | 243,180.00 USD | 93,060.00 USD |
| `7D` | `0.0794` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 195,640.00 USD | 175,880.00 USD | 75,250.00 USD |
| `1D` | `0.0795` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 260,570.00 USD | 131,430.00 USD | 0.00 USD |
| `7D` | `0.0795` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 164,240.00 USD | 130,050.00 USD | 55,700.00 USD |
| `1D` | `0.0796` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 117,990.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 334,830.00 USD | 108,640.00 USD | 75,520.00 USD |
| `1D` | `0.0797` | 905,540.00 USD | 0.00 USD | 905,540.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD |
| `7D` | `0.0797` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 284,990.00 USD | 46,270.00 USD | 43,700.00 USD |
| `1D` | `0.0798` | 507,260.00 USD | 0.00 USD | 507,260.00 USD | 0.00 USD | 164,240.00 USD | 0.00 USD |
| `7D` | `0.0798` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 315,270.00 USD | 90,910.00 USD | 46,450.00 USD |
| `1D` | `0.0799` | 343,020.00 USD | 0.00 USD | 343,020.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD |
| `7D` | `0.0799` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 75,020.00 USD | 202,590.00 USD |
| `1D` | `0.0800` | 5,610.00 USD | 5,610.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `1D` | `0.0800` | 11,210.00 USD | 11,210.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `7D` | `0.0800` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 53,640.00 USD | 0.00 USD | 386,060.00 USD |
| `7D` | `0.0802` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD | 102,290.00 USD |
| `7D` | `0.0803` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 0.00 USD | 29,400.00 USD | 5,200.00 USD |
| `1D` | `0.0804` | 22,120.00 USD | 22,120.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 95,670.00 USD | 98,500.00 USD | 4,520.00 USD |
| `7D` | `0.0805` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 132,140.00 USD | 11,950.00 USD | 2,250.00 USD |
| `1D` | `0.0806` | 25,640.00 USD | 25,640.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0806` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 114,280.00 USD | 171,680.00 USD | 28,690.00 USD |
| `1D` | `0.0807` | 136,480.00 USD | 136,480.00 USD | 0.00 USD | 0.00 USD | 70,050.00 USD | 40,790.00 USD |
| `7D` | `0.0807` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 897,170.00 USD | 778,530.00 USD | 325,250.00 USD |
| `1D` | `0.0808` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 503,640.00 USD | 26,410.00 USD | 400,010.00 USD |
| `7D` | `0.0808` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 1,120,000.00 USD | 813,630.00 USD | 575,890.00 USD |
| `1D` | `0.0809` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 405,610.00 USD | 193,380.00 USD | 0.00 USD |
| `7D` | `0.0809` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 826,560.00 USD | 917,760.00 USD | 500,140.00 USD |
| `1D` | `0.0810` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 150,810.00 USD | 60,350.00 USD | 293.28 USD |
| `7D` | `0.0810` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 977,340.00 USD | 266,420.00 USD | 399,480.00 USD |
| `1D` | `0.0811` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 161,440.00 USD | 0.00 USD |
| `7D` | `0.0811` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 602,750.00 USD | 351,410.00 USD | 417,740.00 USD |
| `1D` | `0.0812` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 14,540.00 USD | 19,910.00 USD | 269,820.00 USD |
| `7D` | `0.0812` | 18,970,000.00 USD | 18,970,000.00 USD | 0.00 USD | 1,200,000.00 USD | 200,500.00 USD | 191,640.00 USD |
| `1D` | `0.0813` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 27,080.00 USD | 18,240.00 USD | 209,180.00 USD |
| `7D` | `0.0813` | 20,490,000.00 USD | 20,490,000.00 USD | 0.00 USD | 780,410.00 USD | 335,050.00 USD | 406,360.00 USD |
| `1D` | `0.0814` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 22,430.00 USD | 13,790.00 USD | 386,300.00 USD |
| `7D` | `0.0814` | 21,850,000.00 USD | 21,850,000.00 USD | 0.00 USD | 317,750.00 USD | 557,910.00 USD | 481,750.00 USD |
| `1D` | `0.0815` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD |
| `7D` | `0.0815` | 23,300,000.00 USD | 23,300,000.00 USD | 0.00 USD | 672,460.00 USD | 340,150.00 USD | 439,270.00 USD |
| `1D` | `0.0816` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 405,120.00 USD | 245,220.00 USD | 189,500.00 USD |
| `7D` | `0.0816` | 24,830,000.00 USD | 24,830,000.00 USD | 0.00 USD | 824,560.00 USD | 543,650.00 USD | 169,410.00 USD |
| `1D` | `0.0817` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 361,650.00 USD | 108,010.00 USD | 130,180.00 USD |
| `7D` | `0.0817` | 26,750,000.00 USD | 26,750,000.00 USD | 0.00 USD | 1,000,000.00 USD | 529,040.00 USD | 381,250.00 USD |
| `1D` | `0.0818` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 298,910.00 USD | 161,880.00 USD | 321,810.00 USD |
| `7D` | `0.0818` | 27,670,000.00 USD | 27,670,000.00 USD | 0.00 USD | 413,640.00 USD | 321,200.00 USD | 188,240.00 USD |
| `1D` | `0.0819` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 171,350.00 USD | 368,950.00 USD | 156,890.00 USD |
| `7D` | `0.0819` | 28,580,000.00 USD | 28,580,000.00 USD | 0.00 USD | 431,190.00 USD | 214,760.00 USD | 258,880.00 USD |
| `1D` | `0.0820` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 215,860.00 USD | 285,850.00 USD | 499,340.00 USD |
| `7D` | `0.0820` | 29,830,000.00 USD | 29,830,000.00 USD | 0.00 USD | 389,040.00 USD | 467,190.00 USD | 392,670.00 USD |
| `1D` | `0.0821` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 400,440.00 USD | 167,900.00 USD | 171,040.00 USD |
| `7D` | `0.0821` | 31,300,000.00 USD | 31,300,000.00 USD | 0.00 USD | 985,600.00 USD | 315,920.00 USD | 168,920.00 USD |
| `1D` | `0.0822` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 268,440.00 USD | 195,730.00 USD | 127,580.00 USD |
| `7D` | `0.0822` | 32,020,000.00 USD | 32,020,000.00 USD | 0.00 USD | 321,980.00 USD | 282,340.00 USD | 114,660.00 USD |
| `1D` | `0.0823` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 185,080.00 USD | 30,920.00 USD | 9,460.00 USD |
| `7D` | `0.0823` | 32,670,000.00 USD | 32,670,000.00 USD | 0.00 USD | 346,280.00 USD | 238,960.00 USD | 70,490.00 USD |
| `1D` | `0.0824` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 198,500.00 USD | 202,010.00 USD | 137,490.00 USD |
| `7D` | `0.0824` | 33,540,000.00 USD | 33,540,000.00 USD | 0.00 USD | 471,470.00 USD | 226,290.00 USD | 169,450.00 USD |
| `1D` | `0.0825` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 101,400.00 USD | 44,860.00 USD | 21,620.00 USD |
| `7D` | `0.0825` | 34,280,000.00 USD | 34,280,000.00 USD | 0.00 USD | 317,900.00 USD | 268,580.00 USD | 153,540.00 USD |
| `1D` | `0.0826` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 33,820.00 USD | 5,050.00 USD | 146,520.00 USD |
| `7D` | `0.0826` | 34,790,000.00 USD | 34,790,000.00 USD | 0.00 USD | 330,240.00 USD | 73,020.00 USD | 112,220.00 USD |
| `1D` | `0.0827` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 108,560.00 USD | 8,240.00 USD | 55.02 USD |
| `7D` | `0.0827` | 35,300,000.00 USD | 35,300,000.00 USD | 0.00 USD | 253,490.00 USD | 104,450.00 USD | 144,170.00 USD |
| `1D` | `0.0828` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 265,750.00 USD | 56,990.00 USD | 75,070.00 USD |
| `7D` | `0.0828` | 35,920,000.00 USD | 35,920,000.00 USD | 0.00 USD | 496,290.00 USD | 59,010.00 USD | 71,010.00 USD |
| `1D` | `0.0829` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 260,740.00 USD | 88,990.00 USD | 72,740.00 USD |
| `7D` | `0.0829` | 36,440,000.00 USD | 36,440,000.00 USD | 0.00 USD | 294,720.00 USD | 58,970.00 USD | 162,950.00 USD |
| `1D` | `0.0830` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 260,260.00 USD | 108,400.00 USD | 152,000.00 USD |
| `7D` | `0.0830` | 36,860,000.00 USD | 36,860,000.00 USD | 0.00 USD | 128,010.00 USD | 147,000.00 USD | 148,110.00 USD |
| `1D` | `0.0831` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 116,480.00 USD | 64,510.00 USD | 43,220.00 USD |
| `7D` | `0.0831` | 37,490,000.00 USD | 37,490,000.00 USD | 0.00 USD | 346,900.00 USD | 119,240.00 USD | 158,490.00 USD |
| `1D` | `0.0832` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 220,480.00 USD | 91,440.00 USD | 86,260.00 USD |
| `7D` | `0.0832` | 38,140,000.00 USD | 38,140,000.00 USD | 0.00 USD | 313,100.00 USD | 258,020.00 USD | 80,310.00 USD |
| `1D` | `0.0833` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 153,900.00 USD | 46,180.00 USD | 31,430.00 USD |
| `7D` | `0.0833` | 38,870,000.00 USD | 38,870,000.00 USD | 0.00 USD | 413,110.00 USD | 230,970.00 USD | 91,610.00 USD |
| `1D` | `0.0834` | 12,610,000.00 USD | 12,610,000.00 USD | 0.00 USD | 154,940.00 USD | 60,550.00 USD | 135,700.00 USD |
| `7D` | `0.0834` | 39,370,000.00 USD | 39,370,000.00 USD | 0.00 USD | 216,670.00 USD | 135,260.00 USD | 144,430.00 USD |
| `1D` | `0.0835` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 122,780.00 USD | 184,470.00 USD | 78,760.00 USD |
| `7D` | `0.0835` | 39,870,000.00 USD | 39,870,000.00 USD | 0.00 USD | 258,370.00 USD | 107,380.00 USD | 128,930.00 USD |
| `1D` | `0.0836` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 83,690.00 USD | 84,520.00 USD | 221,700.00 USD |
| `7D` | `0.0836` | 40,210,000.00 USD | 40,210,000.00 USD | 0.00 USD | 104,940.00 USD | 90,690.00 USD | 146,420.00 USD |
| `1D` | `0.0837` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 189,580.00 USD | 61,550.00 USD | 34,400.00 USD |
| `7D` | `0.0837` | 40,650,000.00 USD | 40,650,000.00 USD | 0.00 USD | 262,200.00 USD | 158,180.00 USD | 27,040.00 USD |
| `1D` | `0.0838` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 144,100.00 USD | 76,380.00 USD | 48,680.00 USD |
| `7D` | `0.0838` | 40,820,000.00 USD | 40,820,000.00 USD | 0.00 USD | 100,250.00 USD | 64,030.00 USD | 1,250.00 USD |
| `1D` | `0.0839` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 67,620.00 USD | 0.00 USD | 639.31 USD |
| `7D` | `0.0839` | 40,980,000.00 USD | 40,980,000.00 USD | 0.00 USD | 96,540.00 USD | 64,060.00 USD | 3,660.00 USD |
| `1D` | `0.0840` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 33,540.00 USD | 15,480.00 USD | 584.63 USD |
| `7D` | `0.0840` | 41,120,000.00 USD | 41,120,000.00 USD | 0.00 USD | 127,750.00 USD | 0.00 USD | 4,330.00 USD |
| `1D` | `0.0841` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 32,120.00 USD | 2,010.00 USD | 709.20 USD |
| `7D` | `0.0841` | 41,200,000.00 USD | 41,200,000.00 USD | 0.00 USD | 78,440.00 USD | 0.00 USD | 8,350.00 USD |
| `1D` | `0.0842` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 31,430.00 USD | 0.00 USD | 47,110.00 USD |
| `7D` | `0.0842` | 41,360,000.00 USD | 41,360,000.00 USD | 0.00 USD | 122,190.00 USD | 33,520.00 USD | 1,880.00 USD |
| `1D` | `0.0843` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 36,500.00 USD | 0.00 USD | 1,560.00 USD |
| `7D` | `0.0843` | 41,530,000.00 USD | 41,530,000.00 USD | 0.00 USD | 115,430.00 USD | 44,120.00 USD | 5,030.00 USD |
| `1D` | `0.0844` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 88,610.00 USD | 0.00 USD | 563.70 USD |
| `7D` | `0.0844` | 41,800,000.00 USD | 41,800,000.00 USD | 0.00 USD | 135,060.00 USD | 64,360.00 USD | 74,320.00 USD |
| `1D` | `0.0845` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 20,470.00 USD | 0.00 USD | 353.58 USD |
| `7D` | `0.0845` | 41,970,000.00 USD | 41,970,000.00 USD | 0.00 USD | 76,690.00 USD | 30,660.00 USD | 58,930.00 USD |
| `1D` | `0.0846` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 67,820.00 USD | 16,670.00 USD | 75.71 USD |
| `7D` | `0.0846` | 42,200,000.00 USD | 42,200,000.00 USD | 0.00 USD | 110,690.00 USD | 76,890.00 USD | 42,600.00 USD |
| `1D` | `0.0847` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 18,780.00 USD | 0.00 USD | 2,140.00 USD |
| `7D` | `0.0847` | 42,510,000.00 USD | 42,510,000.00 USD | 0.00 USD | 159,740.00 USD | 113,280.00 USD | 38,330.00 USD |
| `1D` | `0.0848` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 20,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 42,840,000.00 USD | 42,840,000.00 USD | 0.00 USD | 166,870.00 USD | 67,150.00 USD | 101,960.00 USD |
| `1D` | `0.0849` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 15,210.00 USD | 0.00 USD | 292.60 USD |
| `7D` | `0.0849` | 43,230,000.00 USD | 43,230,000.00 USD | 0.00 USD | 126,210.00 USD | 145,370.00 USD | 111,470.00 USD |
| `1D` | `0.0850` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 21,120.00 USD | 0.00 USD | 413.16 USD |
| `7D` | `0.0850` | 43,620,000.00 USD | 43,620,000.00 USD | 0.00 USD | 147,740.00 USD | 61,080.00 USD | 188,130.00 USD |
| `1D` | `0.0851` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 24,960.00 USD | 11,000.00 USD | 665.45 USD |
| `7D` | `0.0851` | 43,850,000.00 USD | 43,850,000.00 USD | 0.00 USD | 59,990.00 USD | 87,540.00 USD | 77,800.00 USD |
| `1D` | `0.0852` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.58 USD |
| `1D` | `0.0853` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 12,910.00 USD | 737.47 USD | 212.49 USD |
| `7D` | `0.0853` | 44,010,000.00 USD | 44,010,000.00 USD | 0.00 USD | 84,580.00 USD | 55,780.00 USD | 24,100.00 USD |
| `1D` | `0.0854` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 34,680.00 USD | 13,190.00 USD | 10,120.00 USD |
| `7D` | `0.0854` | 44,220,000.00 USD | 44,220,000.00 USD | 0.00 USD | 111,900.00 USD | 48,090.00 USD | 50,710.00 USD |
| `1D` | `0.0855` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD |
| `7D` | `0.0855` | 44,580,000.00 USD | 44,580,000.00 USD | 0.00 USD | 185,600.00 USD | 101,580.00 USD | 70,120.00 USD |
| `1D` | `0.0856` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 92,490.00 USD | 32,810.00 USD | 19,870.00 USD |
| `7D` | `0.0856` | 44,880,000.00 USD | 44,880,000.00 USD | 0.00 USD | 105,420.00 USD | 110,810.00 USD | 86,100.00 USD |
| `1D` | `0.0857` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 50,540.00 USD | 18,030.00 USD | 27,880.00 USD |
| `7D` | `0.0857` | 45,070,000.00 USD | 45,070,000.00 USD | 0.00 USD | 124,090.00 USD | 8,980.00 USD | 56,020.00 USD |
| `1D` | `0.0858` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 48,130.00 USD | 36,780.00 USD | 164.89 USD |
| `7D` | `0.0858` | 45,240,000.00 USD | 45,240,000.00 USD | 0.00 USD | 83,590.00 USD | 38,000.00 USD | 49,650.00 USD |
| `1D` | `0.0859` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 72,260.00 USD | 20,870.00 USD | 40,140.00 USD |
| `7D` | `0.0859` | 45,350,000.00 USD | 45,350,000.00 USD | 0.00 USD | 85,670.00 USD | 23,160.00 USD | 747.55 USD |
| `1D` | `0.0860` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 44,920.00 USD | 22,170.00 USD | 20,180.00 USD |
| `7D` | `0.0860` | 45,500,000.00 USD | 45,500,000.00 USD | 0.00 USD | 72,910.00 USD | 55,790.00 USD | 17,160.00 USD |
| `1D` | `0.0861` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 20,430.00 USD | 0.00 USD | 32,450.00 USD |
| `7D` | `0.0861` | 45,720,000.00 USD | 45,720,000.00 USD | 0.00 USD | 81,490.00 USD | 84,030.00 USD | 59,310.00 USD |
| `1D` | `0.0862` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD |
| `7D` | `0.0862` | 45,810,000.00 USD | 45,810,000.00 USD | 0.00 USD | 15,880.00 USD | 20,950.00 USD | 45,310.00 USD |
| `1D` | `0.0863` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 219.34 USD |
| `1D` | `0.0864` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,150.00 USD |
| `7D` | `0.0864` | 45,920,000.00 USD | 45,920,000.00 USD | 0.00 USD | 64,760.00 USD | 21,830.00 USD | 27,390.00 USD |
| `1D` | `0.0865` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 31,770.00 USD | 1,280.00 USD | 18,020.00 USD |
| `7D` | `0.0865` | 46,120,000.00 USD | 46,120,000.00 USD | 0.00 USD | 103,840.00 USD | 26,840.00 USD | 71,050.00 USD |
| `1D` | `0.0866` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 25,410.00 USD | 16,310.00 USD | 19,340.00 USD |
| `7D` | `0.0866` | 46,160,000.00 USD | 46,160,000.00 USD | 0.00 USD | 10,780.00 USD | 30,220.00 USD | 342.91 USD |
| `1D` | `0.0867` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 24,580.00 USD | 37,120.00 USD | 14,130.00 USD |
| `7D` | `0.0867` | 46,300,000.00 USD | 46,300,000.00 USD | 0.00 USD | 37,230.00 USD | 68,720.00 USD | 36,050.00 USD |
| `1D` | `0.0868` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 9,000.00 USD | 9,540.00 USD | 34,750.00 USD |
| `7D` | `0.0868` | 46,580,000.00 USD | 46,580,000.00 USD | 0.00 USD | 166,800.00 USD | 50,450.00 USD | 60,890.00 USD |
| `1D` | `0.0869` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 13,960.00 USD | 8,720.00 USD | 9,620.00 USD |
| `7D` | `0.0869` | 46,810,000.00 USD | 46,810,000.00 USD | 0.00 USD | 86,030.00 USD | 106,700.00 USD | 38,750.00 USD |
| `1D` | `0.0870` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 33,110.00 USD | 6,620.00 USD | 375.99 USD |
| `7D` | `0.0870` | 46,920,000.00 USD | 46,920,000.00 USD | 0.00 USD | 64,420.00 USD | 41,030.00 USD | 815.18 USD |
| `1D` | `0.0871` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 50,960.00 USD | 57,110.00 USD | 37,920.00 USD |
| `7D` | `0.0871` | 47,130,000.00 USD | 47,130,000.00 USD | 0.00 USD | 81,270.00 USD | 68,300.00 USD | 58,660.00 USD |
| `1D` | `0.0872` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 27,110.00 USD | 16,340.00 USD | 8,650.00 USD |
| `7D` | `0.0872` | 47,320,000.00 USD | 47,320,000.00 USD | 0.00 USD | 67,390.00 USD | 74,740.00 USD | 52,540.00 USD |
| `1D` | `0.0873` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 1,730.00 USD | 1,460.00 USD | 13,660.00 USD |
| `7D` | `0.0873` | 47,450,000.00 USD | 47,450,000.00 USD | 0.00 USD | 100,710.00 USD | 0.00 USD | 29,740.00 USD |
| `1D` | `0.0875` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 25,220.00 USD | 717.80 USD | 0.00 USD |
| `7D` | `0.0875` | 47,530,000.00 USD | 47,530,000.00 USD | 0.00 USD | 28,810.00 USD | 18,590.00 USD | 28,420.00 USD |
| `1D` | `0.0876` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 33,830.00 USD | 15,030.00 USD | 26,890.00 USD |
| `7D` | `0.0876` | 47,680,000.00 USD | 47,680,000.00 USD | 0.00 USD | 117,620.00 USD | 23,600.00 USD | 13,170.00 USD |
| `1D` | `0.0877` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 21,520.00 USD | 11,700.00 USD | 21,830.00 USD |
| `7D` | `0.0877` | 47,800,000.00 USD | 47,800,000.00 USD | 0.00 USD | 67,300.00 USD | 1,810.00 USD | 47,480.00 USD |
| `1D` | `0.0878` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 63,040.00 USD | 40,570.00 USD | 50,790.00 USD |
| `7D` | `0.0878` | 47,890,000.00 USD | 47,890,000.00 USD | 0.00 USD | 6,280.00 USD | 39,280.00 USD | 46,510.00 USD |
| `1D` | `0.0879` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `7D` | `0.0879` | 48,060,000.00 USD | 48,060,000.00 USD | 0.00 USD | 73,130.00 USD | 41,910.00 USD | 48,470.00 USD |
| `1D` | `0.0880` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0880` | 48,120,000.00 USD | 48,120,000.00 USD | 0.00 USD | 38,400.00 USD | 27,140.00 USD | 0.00 USD |
| `1D` | `0.0881` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 33,000.00 USD | 10,770.00 USD | 12,510.00 USD |
| `7D` | `0.0881` | 48,230,000.00 USD | 48,230,000.00 USD | 0.00 USD | 20,400.00 USD | 58,090.00 USD | 24,890.00 USD |
| `1D` | `0.0882` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 25,340.00 USD | 15,630.00 USD | 27,970.00 USD |
| `1D` | `0.0883` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 26,840.00 USD | 73,610.00 USD | 7,860.00 USD |
| `1D` | `0.0884` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 8,850.00 USD | 17,780.00 USD | 83,950.00 USD |
| `1D` | `0.0886` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 48,870.00 USD | 18,070.00 USD | 13,500.00 USD |
| `1D` | `0.0887` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 22,710.00 USD | 22,450.00 USD | 19,280.00 USD |
| `1D` | `0.0888` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 16,050.00 USD | 0.00 USD | 142.34 USD |
| `1D` | `0.0889` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0890` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 0.00 USD | 802.30 USD | 0.00 USD |
| `1D` | `0.0891` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 2,580.00 USD | 0.00 USD | 18,610.00 USD |
| `1D` | `0.0892` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101.53 USD |
| `1D` | `0.0893` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0894` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.13B` | Total OI Tokens: `14,094,820,186.4 DOGE`
  * 1h OI Change: `-0.75%` | 4h OI Change: `+0.54%` | 24h OI Change: `-0.56%`
  * Exchange Breakdown: Binance=`273.44M` | Bybit=`114.13M` | OKX=`116.71M` | Hyperliquid=`81.03M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `44.49K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `36.44%` | `63.56%` | `0.57` | 8,290,000.00 USD |
| `15M` | `Binance` | `30.76%` | `69.24%` | `0.44` | 5,160,000.00 USD |
| `15M` | `OKX` | `25.69%` | `74.31%` | `0.35` | 586,420.00 USD |
| `15M` | `Bybit` | `29.3%` | `70.7%` | `0.41` | 239,380.00 USD |
| `15M` | `KuCoin` | `31.07%` | `68.93%` | `0.45` | 49,480.00 USD |
| `15M` | `Gate` | `68.55%` | `31.45%` | `2.18` | 889,660.00 USD |
| `15M` | `Bitget` | `40%` | `60%` | `0.67` | 169,440.00 USD |
| `15M` | `BingX` | `37.77%` | `62.23%` | `0.61` | 443,940.00 USD |
| `15M` | `MEXC` | `67.22%` | `32.78%` | `2.05` | 57,500.00 USD |
| `15M` | `Bitunix` | `20.83%` | `79.17%` | `0.26` | 255,780.00 USD |
| `15M` | `Hyperliquid` | `43.57%` | `56.43%` | `0.77` | 28,790.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.43%` | `43.57%` | `1.30` | 242,160.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 56,790.00 USD |
| `15M` | `HTX` | `52.67%` | `47.33%` | `1.11` | 23,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `21.41%` | `78.59%` | `0.27` | 4,680.00 USD |
| `15M` | `Aster` | `45.15%` | `54.85%` | `0.82` | 23,100.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.26%` | `49.74%` | `1.01` | 60,260.00 USD |
| `15M` | `Whale Positions` | `30.76%` | `69.24%` | `0.44` | 5,160,000.00 USD |
| `15M` | `Global Accounts` | `36.44%` | `63.56%` | `0.57` | 8,290,000.00 USD |
| `1H` | `DOGE` | `44.45%` | `55.55%` | `0.80` | 45,520,000.00 USD |
| `1H` | `Binance` | `45.25%` | `54.75%` | `0.83` | 29,340,000.00 USD |
| `1H` | `OKX` | `43.7%` | `56.3%` | `0.78` | 2,210,000.00 USD |
| `1H` | `Bybit` | `48.38%` | `51.62%` | `0.94` | 1,490,000.00 USD |
| `1H` | `KuCoin` | `41.43%` | `58.57%` | `0.71` | 192,520.00 USD |
| `1H` | `Gate` | `50.59%` | `49.41%` | `1.02` | 4,380,000.00 USD |
| `1H` | `Bitget` | `28.9%` | `71.1%` | `0.41` | 813,320.00 USD |
| `1H` | `BingX` | `18.89%` | `81.11%` | `0.23` | 2,110,000.00 USD |
| `1H` | `MEXC` | `45.28%` | `54.72%` | `0.83` | 613,120.00 USD |
| `1H` | `Bitunix` | `46.81%` | `53.19%` | `0.88` | 1,380,000.00 USD |
| `1H` | `Hyperliquid` | `50.23%` | `49.77%` | `1.01` | 412,750.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.14%` | `48.86%` | `1.05` | 894,480.00 USD |
| `1H` | `Crypto.com` | `50.3%` | `49.7%` | `1.01` | 0.00 USD |
| `1H` | `WhiteBIT` | `47.42%` | `52.58%` | `0.90` | 203,700.00 USD |
| `1H` | `HTX` | `49%` | `51%` | `0.96` | 315,400.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.86%` | `53.14%` | `0.88` | 17,660.00 USD |
| `1H` | `Aster` | `67.67%` | `32.33%` | `2.09` | 315,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `22.25%` | `77.75%` | `0.29` | 831,570.00 USD |
| `1H` | `Whale Positions` | `45.25%` | `54.75%` | `0.83` | 29,340,000.00 USD |
| `1H` | `Global Accounts` | `44.45%` | `55.55%` | `0.80` | 45,520,000.00 USD |
| `4H` | `DOGE` | `50.59%` | `49.41%` | `1.02` | 235,380,000.00 USD |
| `4H` | `Binance` | `50.71%` | `49.29%` | `1.03` | 154,250,000.00 USD |
| `4H` | `OKX` | `49.11%` | `50.89%` | `0.97` | 13,460,000.00 USD |
| `4H` | `Bybit` | `45.07%` | `54.93%` | `0.82` | 6,960,000.00 USD |
| `4H` | `KuCoin` | `49.53%` | `50.47%` | `0.98` | 1,300,000.00 USD |
| `4H` | `Gate` | `53.62%` | `46.38%` | `1.16` | 21,690,000.00 USD |
| `4H` | `Bitget` | `53.36%` | `46.64%` | `1.14` | 4,610,000.00 USD |
| `4H` | `BingX` | `45.75%` | `54.25%` | `0.84` | 7,630,000.00 USD |
| `4H` | `MEXC` | `52.91%` | `47.09%` | `1.12` | 3,590,000.00 USD |
| `4H` | `Bitunix` | `46.07%` | `53.93%` | `0.85` | 6,520,000.00 USD |
| `4H` | `Hyperliquid` | `48.87%` | `51.13%` | `0.96` | 2,070,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.14%` | `50.86%` | `0.97` | 6,070,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `92.41%` | `7.59%` | `12.18` | 989,340.00 USD |
| `4H` | `HTX` | `51.92%` | `48.08%` | `1.08` | 926,320.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.5%` | `46.5%` | `1.15` | 478,970.00 USD |
| `4H` | `Aster` | `46.91%` | `53.09%` | `0.88` | 2,110,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.97%` | `51.03%` | `0.96` | 2,710,000.00 USD |
| `4H` | `Whale Positions` | `50.71%` | `49.29%` | `1.03` | 154,250,000.00 USD |
| `4H` | `Global Accounts` | `50.59%` | `49.41%` | `1.02` | 235,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0799` | `0.0799` | `0.0799` | `0.0801` | `0.0796` | 5,436,862.42 USD | 2,702,362.01 USD | 2,734,500.41 USD | -32,138.40 USD | `-0.59%` | `9B / 8S` |
| `0:00 UTC` | `0.0802` | `0.0800` | `0.0802` | `0.0803` | `0.0797` | 6,917,479.71 USD | 3,663,380.43 USD | 3,254,099.27 USD | 409,281.16 USD | `+5.92%` | `12B / 8S` |
| `5:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0803` | `0.0798` | 4,372,559.79 USD | 2,097,742.47 USD | 2,274,817.31 USD | -177,074.84 USD | `-4.05%` | `5B / 8S` |
| `0:00 UTC` | `0.0802` | `0.0802` | `0.0802` | `0.0803` | `0.0798` | 5,919,541.11 USD | 3,302,953.65 USD | 2,616,587.46 USD | 686,366.19 USD | `+11.59%` | `9B / 2S` |
| `5:00 UTC` | `0.0804` | `0.0805` | `0.0804` | `0.0807` | `0.0802` | 7,554,604.29 USD | 4,072,091.15 USD | 3,482,513.14 USD | 589,578.01 USD | `+7.80%` | `10B / 4S` |
| `0:00 UTC` | `0.0808` | `0.0809` | `0.0808` | `0.0815` | `0.0804` | 18,574,379.74 USD | 9,613,153.94 USD | 8,961,225.80 USD | 651,928.14 USD | `+3.51%` | `14B / 9S` |
| `5:00 UTC` | `0.0807` | `0.0805` | `0.0807` | `0.0809` | `0.0802` | 9,552,151.73 USD | 4,610,293.53 USD | 4,941,858.20 USD | -331,564.68 USD | `-3.47%` | `6B / 12S` |
| `0:00 UTC` | `0.0801` | `0.0801` | `0.0801` | `0.0804` | `0.0799` | 7,702,082.98 USD | 2,993,499.68 USD | 4,708,583.30 USD | -1,715,083.61 USD | `-22.27%` | `2B / 6S` |
| `5:00 UTC` | `0.0802` | `0.0801` | `0.0802` | `0.0802` | `0.0799` | 3,513,799.11 USD | 1,857,314.90 USD | 1,656,484.22 USD | 200,830.68 USD | `+5.72%` | `2B / 5S` |
| `0:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0802` | `0.0799` | 3,259,757.88 USD | 1,407,185.05 USD | 1,852,572.83 USD | -445,387.78 USD | `-13.66%` | `2B / 4S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:51` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 20:12` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:47` | `Volume 100M DOGE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Volume 100M DOGE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.0786` | 17,000,000.00 USD | 0.00 USD |
| `10-28 17:27` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0799` | 0.00 USD | 0.00 USD |
| `10-28 16:36` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0800` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0803` | 0.00 USD | 0.00 USD |
| `10-28 15:16` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 15:13` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 13:51` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0804` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0802` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 100M DOGE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0797` | 0.00 USD | 0.00 USD |
| `10-28 07:56` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0793` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 07:07` | `Range 0.0002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.0794` | 74,000,000.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 25,510.00 USD | -47,330.00 USD | **`DISTRIBUTION`** |
| `15m` | -13,320.00 USD | -748,540.00 USD | **`DISTRIBUTION`** |
| `30m` | -466,630.00 USD | -1,280,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,420,000.00 USD | -5,330,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,300,000.00 USD | -864,090.00 USD | **`DISTRIBUTION`** |
| `4h` | -145,730.00 USD | 1,460,000.00 USD | **`ACCUMULATION`** |
| `6h` | 2,130,000.00 USD | 1,360,000.00 USD | **`ACCUMULATION`** |
| `8h` | 2,430,000.00 USD | -2,060,000.00 USD | **`ACCUMULATION`** |
| `12h` | 900,250.00 USD | -11,660,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -685,050.00 USD | -6,680,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -39,880,000.00 USD | -123,120,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -265,990,000.00 USD | -747,590,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+25.51K` | 15m=`-13.32K` | 1h=`-1.42M` | 24h=`-685.05K`
* Futures Capital Netflows: 5m=`-47.33K` | 15m=`-748.54K` | 1h=`-5.33M` | 24h=`-6.68M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0764` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0727` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0869`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0786` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0823` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0681`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0807`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
