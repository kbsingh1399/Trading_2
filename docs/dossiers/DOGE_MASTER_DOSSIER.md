# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0785` | **Live Ask Quote**: `0.0806` | **Mid Price**: `0.0796`
- **Spread Points**: `21.00` | **Spread BPS**: `263.98 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0777` | VWAP Z-Score: `+0.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000446` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.81` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0805` | Lower -3.00σ Band: `0.0750`
  * Upper +2.51σ Band: `0.0800` | Lower -2.51σ Band: `0.0754`
  * Upper +2.01σ Band: `0.0796` | Lower -2.01σ Band: `0.0759`
  * Upper +2.00σ Band: `0.0796` | Lower -2.00σ Band: `0.0759`
  * Upper +1.28σ Band: `0.0789` | Lower -1.28σ Band: `0.0765`
  * Upper +1.00σ Band: `0.0786` | Lower -1.00σ Band: `0.0768`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0788` | EMA-20=`0.0786` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0781` (Slope: `+0.0000`) | EMA-100=`0.0780`
  * Institutional Anchors: EMA-144=`0.0778` | EMA-200=`0.0776` (Slope: `+0.2234`) | EMA-233=`0.0775`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0763` | Weekly High=`0.0803` | Weekly Low=`0.0755`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0787` (Distance: `+1.13%`)
  * Point of Control (POC) = `0.0767` (Distance: `+3.73%`)
  * Value Area Low (VAL) = `0.0764` (Distance: `+4.13%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `0.0792` - `0.0799`
  * Optimal Trade Entry (OTE 0.705): `0.0797`
  * Structural Invalidation Anchor (0.786): `0.0802`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0793` | `0.0796` | `0.0793` | `0.0796` | `14,626,774` | 1,161,568.77 USD | 411,406.89 USD | `+35.42%` | -8,849,274.35 USD | `+1.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0796` | `0.0796` | `0.0795` | `0.0796` | `17,142,570` | 1,363,964.78 USD | -95,035.73 USD | `-6.97%` | -8,944,310.08 USD | `+0.28` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.0796` | `0.0796` | `0.0796` | `0.0796` | `2,076,615` | 165,336.28 USD | 46,938.89 USD | `+28.39%` | -8,897,371.19 USD | `+0.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0800` | `0.0802` | `0.0795` | `0.0795` | `73,600,519` | 5,871,793.04 USD | -1,470,108.68 USD | `-25.04%` | -8,391,560.94 USD | `-1.94` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0795` | `0.0796` | `0.0792` | `0.0796` | `97,451,255` | 7,734,342.64 USD | -488,400.81 USD | `-6.31%` | -8,879,961.75 USD | `-0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0796` | `0.0796` | `0.0795` | `0.0796` | `19,627,760` | 1,561,842.76 USD | -15,573.30 USD | `-1.00%` | -8,895,535.05 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0806` | `0.0815` | `0.0799` | `0.0801` | `488,172,743` | 39,342,413.57 USD | -1,193,889.47 USD | `-3.03%` | -5,713,397.42 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0801` | `0.0802` | `0.0792` | `0.0796` | `261,755,492` | 20,864,959.87 USD | -2,385,280.59 USD | `-11.43%` | -8,098,678.01 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0796` | `0.0796` | `0.0795` | `0.0796` | `19,627,760` | 1,561,842.76 USD | -15,573.30 USD | `-1.00%` | -8,114,251.31 USD | `+0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0792` | `0.0796` | `769,200,228` | 61,740,879.60 USD | -3,623,061.80 USD | `-5.87%` | -9,477,518.14 USD | `-0.47` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0797` | `0.0799` | `0.0774` | `0.0778` | `998,970,852` | 78,232,937.14 USD | -7,024,064.25 USD | `-8.98%` | -3,060,763.89 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -7,420,203.26 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0792` | `0.0796` | `769,200,228` | 61,740,879.60 USD | -3,623,061.80 USD | `-5.87%` | -9,477,518.14 USD | `-0.47` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.0796` | `87880.0000` | 6,999.64 USD | 17,231.19 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0796` | `8913.0000` | 709.90 USD | 17,941.09 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0796` | `129223.0000` | 10,291.97 USD | 28,233.06 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0796` | `10000.0000` | 796.44 USD | 29,029.50 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0796` | `11884.0000` | 946.47 USD | 29,975.96 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0796` | `40434.0000` | 3,220.20 USD | 33,196.16 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0796` | `11884.0000` | 946.39 USD | 34,142.56 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0796` | `392259.0000` | 31,237.15 USD | 65,379.71 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0796` | `440622.0000` | 35,088.05 USD | 100,467.76 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0796` | `169798.0000` | 13,521.35 USD | 113,989.12 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0796` | `18015.0000` | 1,434.53 USD | 115,423.65 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0796` | `132464.0000` | 10,547.98 USD | 125,971.63 USD | `1 orders` | `-0.05%` | `-` |
| `ASK` | `0.0797` | `96995.0000` | 7,730.11 USD | 124,793.23 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `0.0797` | `18819.0000` | 1,499.78 USD | 117,063.12 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0797` | `27608.0000` | 2,200.19 USD | 115,563.34 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `18822.0000` | 1,499.98 USD | 113,363.15 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `184282.0000` | 14,685.80 USD | 111,863.16 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `436439.0000` | 34,780.26 USD | 97,177.36 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `102355.0000` | 8,156.67 USD | 62,397.10 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `18822.0000` | 1,499.91 USD | 54,240.43 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `18822.0000` | 1,499.89 USD | 52,740.53 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `51468.0000` | 4,101.33 USD | 51,240.64 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0797` | `30692.0000` | 2,445.72 USD | 47,139.31 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0797` | `11870.0000` | 945.86 USD | 44,693.59 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0797` | `3768.0000` | 300.25 USD | 43,747.73 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0797` | `129163.0000` | 10,291.97 USD | 43,447.48 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0797` | `236984.0000` | 18,882.89 USD | 33,155.51 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0797` | `147462.0000` | 11,749.62 USD | 14,272.62 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0797` | `5020.0000` | 399.98 USD | 2,523.00 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0797` | `16431.0000` | 1,309.17 USD | 2,123.02 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0797` | `5020.0000` | 399.97 USD | 813.84 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0797` | `5195.0000` | 413.87 USD | 413.87 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0797` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0797` | `16639.0000` | 1,325.56 USD | 1,325.56 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.0797` | `35038.0000` | 2,791.30 USD | 4,116.86 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0797` | `1034.0000` | 82.37 USD | 4,199.24 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0797` | `5021.0000` | 399.97 USD | 4,599.21 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0797` | `4488.0000` | 357.50 USD | 4,956.70 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0797` | `5022.0000` | 400.03 USD | 5,356.73 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0797` | `49330.0000` | 3,929.33 USD | 9,286.06 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0797` | `11870.0000` | 945.48 USD | 10,231.54 USD | `1 orders` | `-0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `301` | `0xb83d...6e36` | `SHORT` | 8,170,923.57 USD | `102,645,925.00` | `0.0946` | `0.0796` | `1.29` | 1,536,418.08 USD | `+18.80%` | `3X Cross` |
| `311` | `0xc63a...a3cd` | `LONG` | 7,963,400.00 USD | `100,000,000.00` | `0.0856` | `0.0796` | `0.000000` | -601,421.96 USD | `-7.55%` | `10X Cross` |
| `317` | `0x610b...b613` | `LONG` | 7,851,282.02 USD | `98,666,424.00` | `0.0872` | `0.0796` | `0.0577` | -748,899.88 USD | `-9.54%` | `5X Cross` |
| `589` | `0x5b5d...c060` | `SHORT` | 3,939,316.48 USD | `49,478,955.00` | `0.0946` | `0.0796` | `3.08` | 742,200.13 USD | `+18.84%` | `3X Cross` |
| `628` | `0xca49...53c8` | `SHORT` | 3,705,958.43 USD | `46,542,649.00` | `0.0929` | `0.0796` | `0.3461` | 620,086.25 USD | `+16.73%` | `10X Cross` |
| `644` | `0x45d2...4029` | `SHORT` | 3,617,045.25 USD | `45,426,000.00` | `0.0954` | `0.0796` | `0.8431` | 718,583.97 USD | `+19.87%` | `10X Cross` |
| `784` | `0xecb6...2b00` | `SHORT` | 2,972,316.55 USD | `37,355,208.00` | `0.0796` | `0.0796` | `0.8132` | 751.29 USD | `+0.03%` | `10X Cross` |
| `1177` | `0x458d...ab3b` | `LONG` | 1,945,907.61 USD | `24,454,063.00` | `0.1002` | `0.0796` | `0.0714` | -505,014.29 USD | `-25.95%` | `3X Isolated` |
| `1182` | `0xeadc...9d55` | `LONG` | 1,936,519.33 USD | `24,317,440.00` | `0.0926` | `0.0796` | `0.000000` | -315,075.24 USD | `-16.27%` | `10X Cross` |
| `1231` | `0x9aa5...58af` | `SHORT` | 1,871,015.81 USD | `23,500,500.00` | `0.0907` | `0.0796` | `0.3877` | 259,739.15 USD | `+13.88%` | `10X Cross` |
| `1328` | `0xf48f...10fe` | `LONG` | 1,705,454.23 USD | `21,424,497.00` | `0.0968` | `0.0796` | `0.0328` | -368,850.37 USD | `-21.63%` | `4X Cross` |
| `1361` | `0x9946...0852` | `SHORT` | 1,664,824.24 USD | `20,910,149.00` | `0.0871` | `0.0796` | `0.1277` | 155,731.15 USD | `+9.35%` | `10X Cross` |
| `1547` | `0xcac1...26b3` | `SHORT` | 1,443,059.21 USD | `18,126,835.00` | `0.0943` | `0.0796` | `0.4982` | 266,399.99 USD | `+18.46%` | `10X Cross` |
| `1592` | `0x0d6a...ca57` | `LONG` | 1,403,118.70 USD | `17,626,455.00` | `0.0875` | `0.0796` | `0.0626` | -138,986.26 USD | `-9.91%` | `3X Isolated` |
| `1633` | `0x4808...a82c` | `LONG` | 1,339,789.43 USD | `16,828,143.00` | `0.0883` | `0.0796` | `0.0631` | -146,683.55 USD | `-10.95%` | `3X Cross` |
| `1757` | `0x31ef...f715` | `LONG` | 1,212,620.72 USD | `15,230,102.00` | `0.0936` | `0.0796` | `0.0668` | -213,075.21 USD | `-17.57%` | `3X Isolated` |
| `1780` | `0xbfc7...80b4` | `SHORT` | 1,195,832.32 USD | `15,020,000.00` | `0.0920` | `0.0796` | `0.3637` | 186,566.97 USD | `+15.60%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 9,558.66 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0786 USD [API] | `2026-10-27 22:43:16` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0821` (Vol: 381,400.00 USD, Dist: `+3.29%`) | Long MP=`0.0767` (Vol: 519,500.00 USD, Dist: `--3.57%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 478,200.00 USD, Dist: `+3.29%`) | Long MP=`0.0774` (Vol: 691,800.00 USD, Dist: `--2.70%`)
  * 3D Horizon: Short MP=`0.0823` (Vol: 539,400.00 USD, Dist: `+3.49%`) | Long MP=`0.0765` (Vol: 660,700.00 USD, Dist: `--3.76%`)
  * 7D Horizon: Short MP=`0.0821` (Vol: 746,800.00 USD, Dist: `+3.30%`) | Long MP=`0.0762` (Vol: 928,700.00 USD, Dist: `--4.15%`)
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
| `Live` | `Long Liquidation` | `0.0696` | 14,930.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 4,800.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,250.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 791.79 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 2,510.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0706` | 93,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0712` | 23,380,000.00 USD | 23,380,000.00 USD | 43,330.00 USD | 18,990.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 23,270,000.00 USD | 23,270,000.00 USD | 38,060.00 USD | 57,110.00 USD | 37,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 23,140,000.00 USD | 23,140,000.00 USD | 28,200.00 USD | 31,500.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 757,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 23,070,000.00 USD | 23,070,000.00 USD | 1,730.00 USD | 3,280.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 755,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 23,030,000.00 USD | 23,030,000.00 USD | 69,050.00 USD | 17,690.00 USD | 26,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 560.88 USD | 747,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 22,910,000.00 USD | 22,910,000.00 USD | 22,320.00 USD | 11,700.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 746,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 22,860,000.00 USD | 22,860,000.00 USD | 63,040.00 USD | 41,450.00 USD | 50,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 744,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 22,700,000.00 USD | 22,700,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 734,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 22,670,000.00 USD | 22,670,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 733,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 22,570,000.00 USD | 22,570,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0722` | 22,510,000.00 USD | 22,510,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 10,450.00 USD | 709,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 22,430,000.00 USD | 22,430,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 163.73 USD | 699,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 22,320,000.00 USD | 22,320,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 598.51 USD | 698,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 22,190,000.00 USD | 22,190,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 698,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 22,030,000.00 USD | 22,030,000.00 USD | 31,660.00 USD | 0.00 USD | 73.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 697,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 22,000,000.00 USD | 22,000,000.00 USD | 20,420.00 USD | 0.00 USD | 310.25 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 452.21 USD | 697,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 21,980,000.00 USD | 21,980,000.00 USD | 15,580.00 USD | 802.30 USD | 382.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 1,230.00 USD | 696,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 21,960,000.00 USD | 21,960,000.00 USD | 17,820.00 USD | 0.00 USD | 18,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 21,930,000.00 USD | 21,930,000.00 USD | 14,450.00 USD | 0.00 USD | 83.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 622,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 21,910,000.00 USD | 21,910,000.00 USD | 42,980.00 USD | 0.00 USD | 187.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 612,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 21,870,000.00 USD | 21,870,000.00 USD | 42,110.00 USD | 0.00 USD | 127.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 610,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 21,830,000.00 USD | 21,830,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 21,820,000.00 USD | 21,820,000.00 USD | 4,580.00 USD | 0.00 USD | 42.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 604,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 21,810,000.00 USD | 21,810,000.00 USD | 24,100.00 USD | 0.00 USD | 258.52 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 597,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 21,790,000.00 USD | 21,790,000.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 593,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 21,780,000.00 USD | 21,780,000.00 USD | 44,590.00 USD | 0.00 USD | 941.89 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 588,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 21,730,000.00 USD | 21,730,000.00 USD | 34,830.00 USD | 0.00 USD | 126.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,630.00 USD | 577,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 21,700,000.00 USD | 21,700,000.00 USD | 39,050.00 USD | 0.00 USD | 183.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,570.00 USD | 572,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 21,660,000.00 USD | 21,660,000.00 USD | 32,900.00 USD | 0.00 USD | 1,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,080.00 USD | 558,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 21,620,000.00 USD | 21,620,000.00 USD | 37,860.00 USD | 0.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 5,960.00 USD | 103,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 21,580,000.00 USD | 21,580,000.00 USD | 36,340.00 USD | 0.00 USD | 46.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 97,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 21,550,000.00 USD | 21,550,000.00 USD | 37,380.00 USD | 27,500.00 USD | 518.75 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 3,870.00 USD | 96,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 21,480,000.00 USD | 21,480,000.00 USD | 42,800.00 USD | 1,840.00 USD | 15,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 311.95 USD | 92,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 21,420,000.00 USD | 21,420,000.00 USD | 106,370.00 USD | 57,220.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 780.39 USD | 92,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 21,230,000.00 USD | 21,230,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 91,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0747` | 20,690,000.00 USD | 20,690,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 90,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 20,240,000.00 USD | 20,240,000.00 USD | 169,810.00 USD | 65,720.00 USD | 99,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 19,900,000.00 USD | 19,900,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 1,370.00 USD | 89,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 19,550,000.00 USD | 19,550,000.00 USD | 233,830.00 USD | 83,730.00 USD | 121,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 451.13 USD | 88,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0751` | 19,110,000.00 USD | 19,110,000.00 USD | 267,370.00 USD | 82,120.00 USD | 65,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 14,540.00 USD | 88,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 18,700,000.00 USD | 18,700,000.00 USD | 126,420.00 USD | 19,450.00 USD | 85,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 3,910.00 USD | 73,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0753` | 18,470,000.00 USD | 18,470,000.00 USD | 132,200.00 USD | 72,710.00 USD | 30,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0754` | 617.57 USD | 69,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0754` | 18,230,000.00 USD | 18,230,000.00 USD | 95,400.00 USD | 62,330.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 69,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0755` | 18,050,000.00 USD | 18,050,000.00 USD | 123,840.00 USD | 15,650.00 USD | 68,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 17,850,000.00 USD | 17,850,000.00 USD | 177,070.00 USD | 147,310.00 USD | 112,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 356.24 USD | 64,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0757` | 17,410,000.00 USD | 17,410,000.00 USD | 91,080.00 USD | 44,210.00 USD | 103,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0757` | 3,270.00 USD | 64,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0758` | 17,170,000.00 USD | 17,170,000.00 USD | 75,340.00 USD | 42,570.00 USD | 31,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,540.00 USD | 61,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0759` | 17,020,000.00 USD | 17,020,000.00 USD | 109,410.00 USD | 72,180.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,320.00 USD | 55,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 16,830,000.00 USD | 16,830,000.00 USD | 255,670.00 USD | 289,180.00 USD | 216,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,690.00 USD | 23,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0761` | 16,070,000.00 USD | 16,070,000.00 USD | 487,980.00 USD | 429,570.00 USD | 274,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,130.00 USD | 21,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 14,880,000.00 USD | 14,880,000.00 USD | 525,440.00 USD | 268,260.00 USD | 236,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 5,710.00 USD | 20,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0763` | 13,850,000.00 USD | 13,850,000.00 USD | 362,330.00 USD | 142,160.00 USD | 197,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0764` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0764` | 13,140,000.00 USD | 13,140,000.00 USD | 419,700.00 USD | 349,280.00 USD | 92,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0765` | 9,890.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0765` | 12,280,000.00 USD | 12,280,000.00 USD | 553,690.00 USD | 223,110.00 USD | 313,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0766` | 11,190,000.00 USD | 11,190,000.00 USD | 621,080.00 USD | 274,850.00 USD | 279,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0767` | 10,020,000.00 USD | 10,020,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0768` | 9,460,000.00 USD | 9,460,000.00 USD | 426,850.00 USD | 236,860.00 USD | 141,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0769` | 242.54 USD | 5,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0769` | 8,660,000.00 USD | 8,660,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0770` | 330.81 USD | 4,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0770` | 8,170,000.00 USD | 8,170,000.00 USD | 296,720.00 USD | 91,840.00 USD | 269,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0770` | 109.41 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0771` | 7,510,000.00 USD | 7,510,000.00 USD | 231,550.00 USD | 266,030.00 USD | 189,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0772` | 6,820,000.00 USD | 6,820,000.00 USD | 169,730.00 USD | 297,590.00 USD | 334,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0773` | 6,020,000.00 USD | 6,020,000.00 USD | 272,980.00 USD | 149,960.00 USD | 240,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0774` | 5,350,000.00 USD | 5,350,000.00 USD | 165,350.00 USD | 97,350.00 USD | 108,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0775` | 4,980,000.00 USD | 4,980,000.00 USD | 181,290.00 USD | 12,820.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0776` | 4,770,000.00 USD | 4,770,000.00 USD | 106,410.00 USD | 237,880.00 USD | 232,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0777` | 4,200,000.00 USD | 4,200,000.00 USD | 48,260.00 USD | 159,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0778` | 3,990,000.00 USD | 3,990,000.00 USD | 36,200.00 USD | 40,050.00 USD | 186,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0779` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 4,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0780` | 3,720,000.00 USD | 3,720,000.00 USD | 185,540.00 USD | 34,820.00 USD | 319.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0781` | 3,500,000.00 USD | 3,500,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0782` | 3,450,000.00 USD | 3,450,000.00 USD | 44,780.00 USD | 75,640.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0783` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0784` | 4,390.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0784` | 3,200,000.00 USD | 3,200,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0785` | 2,640,000.00 USD | 2,640,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0786` | 2,300,000.00 USD | 2,300,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0787` | 1,770,000.00 USD | 1,770,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0788` | 1,180,000.00 USD | 1,180,000.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0789` | 759,170.00 USD | 759,170.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0790` | 529,120.00 USD | 529,120.00 USD | 200,610.00 USD | 137,240.00 USD | 50,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0791` | 140,690.00 USD | 140,690.00 USD | 76,010.00 USD | 3,690.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0792` | 30,970.00 USD | 30,970.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 381,280.00 USD | 381,280.00 USD | 260,570.00 USD | 120,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 762,560.00 USD | 762,560.00 USD | 260,570.00 USD | 120,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 778,820.00 USD | 778,820.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 1,180,000.00 USD | 1,180,000.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 1,670,000.00 USD | 1,670,000.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 1,690,000.00 USD | 1,690,000.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 70,050.00 USD | 40,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 2,670,000.00 USD | 2,670,000.00 USD | 439,160.00 USD | 26,410.00 USD | 399,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 3,360,000.00 USD | 3,360,000.00 USD | 419,190.00 USD | 269,160.00 USD | 81.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 3,760,000.00 USD | 3,760,000.00 USD | 180,570.00 USD | 100,400.00 USD | 118,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 166,420.00 USD | 436.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 4,280,000.00 USD | 4,280,000.00 USD | 61,690.00 USD | 24,650.00 USD | 269,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 4,540,000.00 USD | 4,540,000.00 USD | 27,080.00 USD | 18,240.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 4,960,000.00 USD | 4,960,000.00 USD | 22,430.00 USD | 18,210.00 USD | 386,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 5,530,000.00 USD | 5,530,000.00 USD | 249,400.00 USD | 201,730.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 6,400,000.00 USD | 6,400,000.00 USD | 441,880.00 USD | 245,220.00 USD | 189,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 7,050,000.00 USD | 7,050,000.00 USD | 361,650.00 USD | 152,470.00 USD | 130,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 7,830,000.00 USD | 7,830,000.00 USD | 298,910.00 USD | 161,880.00 USD | 322,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 8,530,000.00 USD | 8,530,000.00 USD | 171,350.00 USD | 368,950.00 USD | 156,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 9,520,000.00 USD | 9,520,000.00 USD | 215,860.00 USD | 275,570.00 USD | 499,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 10,240,000.00 USD | 10,240,000.00 USD | 383,530.00 USD | 167,310.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 10,830,000.00 USD | 10,830,000.00 USD | 265,050.00 USD | 195,320.00 USD | 127,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0823` | 121.40 USD | 4,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0823` | 11,030,000.00 USD | 11,030,000.00 USD | 178,250.00 USD | 17,180.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 11,540,000.00 USD | 11,540,000.00 USD | 167,370.00 USD | 202,010.00 USD | 137,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 12,660.00 USD | 17,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0825` | 11,760,000.00 USD | 11,760,000.00 USD | 112,270.00 USD | 82,760.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 12,040,000.00 USD | 12,040,000.00 USD | 48,700.00 USD | 25,070.00 USD | 203,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 12,160,000.00 USD | 12,160,000.00 USD | 109,990.00 USD | 10,730.00 USD | 344.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 12,580,000.00 USD | 12,580,000.00 USD | 287,480.00 USD | 59,370.00 USD | 74,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 13,000,000.00 USD | 13,000,000.00 USD | 262,740.00 USD | 88,990.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 13,520,000.00 USD | 13,520,000.00 USD | 257,210.00 USD | 110,610.00 USD | 151,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 13,740,000.00 USD | 13,740,000.00 USD | 110,360.00 USD | 64,510.00 USD | 42,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 14,160,000.00 USD | 14,160,000.00 USD | 241,940.00 USD | 91,440.00 USD | 86,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 14,420,000.00 USD | 14,420,000.00 USD | 158,790.00 USD | 68,410.00 USD | 33,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 14,770,000.00 USD | 14,770,000.00 USD | 154,940.00 USD | 60,550.00 USD | 133,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 15,160,000.00 USD | 15,160,000.00 USD | 124,490.00 USD | 184,470.00 USD | 78,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0835` | 205.70 USD | 29,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0836` | 15,550,000.00 USD | 15,550,000.00 USD | 83,690.00 USD | 84,520.00 USD | 223,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 29,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 15,840,000.00 USD | 15,840,000.00 USD | 191,180.00 USD | 61,550.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 30,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 16,110,000.00 USD | 16,110,000.00 USD | 145,530.00 USD | 76,380.00 USD | 48,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 16,170,000.00 USD | 16,170,000.00 USD | 67,620.00 USD | 0.00 USD | 671.64 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 30,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 16,230,000.00 USD | 16,230,000.00 USD | 35,250.00 USD | 15,480.00 USD | 425.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 16,260,000.00 USD | 16,260,000.00 USD | 32,120.00 USD | 2,010.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0842` | 462.91 USD | 31,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0842` | 16,340,000.00 USD | 16,340,000.00 USD | 30,040.00 USD | 0.00 USD | 46,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 16,370,000.00 USD | 16,370,000.00 USD | 33,670.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 16,460,000.00 USD | 16,460,000.00 USD | 84,020.00 USD | 0.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 16,480,000.00 USD | 16,480,000.00 USD | 22,140.00 USD | 0.00 USD | 85.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 16,570,000.00 USD | 16,570,000.00 USD | 71,490.00 USD | 16,670.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 31,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 16,590,000.00 USD | 16,590,000.00 USD | 18,780.00 USD | 0.00 USD | 507.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 16,610,000.00 USD | 16,610,000.00 USD | 21,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0849` | 16,630,000.00 USD | 16,630,000.00 USD | 15,210.00 USD | 0.00 USD | 406.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 16,650,000.00 USD | 16,650,000.00 USD | 22,320.00 USD | 0.00 USD | 131.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 31,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0851` | 16,690,000.00 USD | 16,690,000.00 USD | 26,040.00 USD | 11,000.00 USD | 63.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 16,700,000.00 USD | 16,700,000.00 USD | 12,910.00 USD | 737.47 USD | 503.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 16,760,000.00 USD | 16,760,000.00 USD | 35,960.00 USD | 13,190.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0855` | 16,910,000.00 USD | 16,910,000.00 USD | 64,150.00 USD | 45,460.00 USD | 36,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 17,050,000.00 USD | 17,050,000.00 USD | 92,490.00 USD | 32,810.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0857` | 17,150,000.00 USD | 17,150,000.00 USD | 50,540.00 USD | 18,030.00 USD | 27,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 17,230,000.00 USD | 17,230,000.00 USD | 48,130.00 USD | 36,780.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0859` | 17,370,000.00 USD | 17,370,000.00 USD | 72,260.00 USD | 20,870.00 USD | 39,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0860` | 17,450,000.00 USD | 17,450,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0861` | 17,510,000.00 USD | 17,510,000.00 USD | 20,430.00 USD | 0.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0862` | 17,580,000.00 USD | 17,580,000.00 USD | 33,780.00 USD | 29,080.00 USD | 11,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 34,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0864` | 17,630,000.00 USD | 17,630,000.00 USD | 22,510.00 USD | 20,050.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0865` | 17,680,000.00 USD | 17,680,000.00 USD | 31,770.00 USD | 1,280.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 17,740,000.00 USD | 17,740,000.00 USD | 25,410.00 USD | 16,310.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0867` | 17,820,000.00 USD | 17,820,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 17,870,000.00 USD | 17,870,000.00 USD | 8,080.00 USD | 9,300.00 USD | 34,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0869` | 17,900,000.00 USD | 17,900,000.00 USD | 12,960.00 USD | 8,560.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 17,930,000.00 USD | 17,930,000.00 USD | 30,380.00 USD | 1,130.00 USD | 0.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0871` | 18,060,000.00 USD | 18,060,000.00 USD | 38,060.00 USD | 57,110.00 USD | 37,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 18,130,000.00 USD | 18,130,000.00 USD | 28,200.00 USD | 31,500.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0873` | 18,180,000.00 USD | 18,180,000.00 USD | 1,730.00 USD | 3,280.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0875` | 18,200,000.00 USD | 18,200,000.00 USD | 25,790.00 USD | 1,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 9,620.00 USD | 44,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0876` | 18,290,000.00 USD | 18,290,000.00 USD | 43,260.00 USD | 15,980.00 USD | 26,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0877` | 18,350,000.00 USD | 18,350,000.00 USD | 22,320.00 USD | 11,700.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0878` | 18,500,000.00 USD | 18,500,000.00 USD | 63,040.00 USD | 41,450.00 USD | 50,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0879` | 18,530,000.00 USD | 18,530,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0880` | 18,630,000.00 USD | 18,630,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 44,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0881` | 18,690,000.00 USD | 18,690,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0882` | 18,760,000.00 USD | 18,760,000.00 USD | 25,340.00 USD | 15,630.00 USD | 27,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0883` | 18,870,000.00 USD | 18,870,000.00 USD | 26,840.00 USD | 73,610.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0884` | 18,980,000.00 USD | 18,980,000.00 USD | 8,850.00 USD | 17,780.00 USD | 84,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0886` | 19,060,000.00 USD | 19,060,000.00 USD | 48,870.00 USD | 18,070.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0887` | 19,130,000.00 USD | 19,130,000.00 USD | 22,710.00 USD | 22,450.00 USD | 19,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 44,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0888` | 19,140,000.00 USD | 19,140,000.00 USD | 16,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0889` | 19,150,000.00 USD | 19,150,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0890` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 802.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0891` | 19,170,000.00 USD | 19,170,000.00 USD | 2,580.00 USD | 0.00 USD | 18,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0893` | 19,190,000.00 USD | 19,190,000.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0894` | 19,220,000.00 USD | 19,220,000.00 USD | 24,750.00 USD | 0.00 USD | 127.67 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0896` | 871.86 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 46,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0160` | 15,880,000.00 USD | 0.00 USD | 3,930.00 USD | `-79.83%` | `244,573.00` |
| `Live` | `Long` | `0.0163` | 15,870,000.00 USD | 0.00 USD | 187.26 USD | `-79.46%` | `11,453.00` |
| `Live` | `Long` | `0.0164` | 15,870,000.00 USD | 0.00 USD | 407.02 USD | `-79.33%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 15,870,000.00 USD | 0.00 USD | 5,290.00 USD | `-79.21%` | `319,394.00` |
| `Live` | `Long` | `0.0169` | 15,870,000.00 USD | 0.00 USD | 292.61 USD | `-78.70%` | `17,263.00` |
| `Live` | `Long` | `0.0191` | 15,870,000.00 USD | 0.00 USD | 16,770.00 USD | `-76.07%` | `880,408.00` |
| `Live` | `Long` | `0.0193` | 15,850,000.00 USD | 0.00 USD | 291.59 USD | `-75.69%` | `15,069.00` |
| `Live` | `Long` | `0.0196` | 15,850,000.00 USD | 0.00 USD | 121.33 USD | `-75.44%` | `6,206.00` |
| `Live` | `Long` | `0.0208` | 15,850,000.00 USD | 0.00 USD | 4,660.00 USD | `-73.93%` | `224,650.00` |
| `Live` | `Long` | `0.0209` | 15,840,000.00 USD | 0.00 USD | 296.97 USD | `-73.68%` | `14,175.00` |
| `Live` | `Long` | `0.0210` | 15,840,000.00 USD | 0.00 USD | 295.48 USD | `-73.55%` | `14,037.00` |
| `Live` | `Long` | `0.0211` | 15,840,000.00 USD | 0.00 USD | 423.00 USD | `-73.43%` | `20,000.00` |
| `Live` | `Long` | `0.0232` | 15,840,000.00 USD | 0.00 USD | 4,720.00 USD | `-70.79%` | `202,860.00` |
| `Live` | `Long` | `0.0237` | 15,840,000.00 USD | 0.00 USD | 473.00 USD | `-70.29%` | `20,000.00` |
| `Live` | `Long` | `0.0242` | 15,840,000.00 USD | 0.00 USD | 11,860.00 USD | `-69.66%` | `491,018.00` |
| `Live` | `Long` | `0.0244` | 15,830,000.00 USD | 0.00 USD | 633.16 USD | `-69.28%` | `25,896.00` |
| `Live` | `Long` | `0.0261` | 15,830,000.00 USD | 0.00 USD | 450.41 USD | `-67.14%` | `17,224.00` |
| `Live` | `Long` | `0.0268` | 15,820,000.00 USD | 0.00 USD | 5,540.00 USD | `-66.27%` | `206,497.00` |
| `Live` | `Long` | `0.0270` | 15,820,000.00 USD | 0.00 USD | 740.40 USD | `-66.14%` | `27,473.00` |
| `Live` | `Long` | `0.0278` | 15,820,000.00 USD | 0.00 USD | 1,090.00 USD | `-65.01%` | `39,049.00` |
| `Live` | `Long` | `0.0279` | 15,820,000.00 USD | 0.00 USD | 1,730.00 USD | `-64.88%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 15,820,000.00 USD | 0.00 USD | 129.22 USD | `-64.25%` | `4,542.00` |
| `Live` | `Long` | `0.0290` | 15,820,000.00 USD | 0.00 USD | 2,320.00 USD | `-63.50%` | `80,000.00` |
| `Live` | `Long` | `0.0299` | 15,810,000.00 USD | 0.00 USD | 162.15 USD | `-62.50%` | `5,432.00` |
| `Live` | `Long` | `0.0301` | 15,810,000.00 USD | 0.00 USD | 4,040.00 USD | `-62.24%` | `134,443.00` |
| `Live` | `Long` | `0.0301` | 15,810,000.00 USD | 0.00 USD | 2,360.00 USD | `-62.12%` | `78,319.00` |
| `Live` | `Long` | `0.0306` | 15,810,000.00 USD | 0.00 USD | 137.41 USD | `-61.62%` | `4,498.00` |
| `Live` | `Long` | `0.0318` | 15,810,000.00 USD | 0.00 USD | 1,510.00 USD | `-60.11%` | `47,501.00` |
| `Live` | `Long` | `0.0321` | 15,810,000.00 USD | 0.00 USD | 688,800.00 USD | `-59.61%` | `21,424,497.00` |
| `Live` | `Long` | `0.0324` | 15,120,000.00 USD | 0.00 USD | 194.34 USD | `-59.23%` | `5,989.00` |
| `Live` | `Long` | `0.0330` | 15,120,000.00 USD | 0.00 USD | 1,650.00 USD | `-58.60%` | `50,000.00` |
| `Live` | `Long` | `0.0331` | 15,110,000.00 USD | 0.00 USD | 149.22 USD | `-58.48%` | `4,515.00` |
| `Live` | `Long` | `0.0338` | 15,110,000.00 USD | 0.00 USD | 1,690.00 USD | `-57.60%` | `50,000.00` |
| `Live` | `Long` | `0.0341` | 15,110,000.00 USD | 0.00 USD | 918.63 USD | `-57.09%` | `26,900.00` |
| `Live` | `Long` | `0.0343` | 15,110,000.00 USD | 0.00 USD | 32,540.00 USD | `-56.97%` | `950,000.00` |
| `Live` | `Long` | `0.0345` | 15,080,000.00 USD | 0.00 USD | 3,110.00 USD | `-56.59%` | `90,000.00` |
| `Live` | `Long` | `0.0350` | 15,080,000.00 USD | 0.00 USD | 17,480.00 USD | `-56.09%` | `500,000.00` |
| `Live` | `Long` | `0.0353` | 15,060,000.00 USD | 0.00 USD | 73,050.00 USD | `-55.59%` | `2,066,606.00` |
| `Live` | `Long` | `0.0355` | 14,990,000.00 USD | 0.00 USD | 4,340.00 USD | `-55.46%` | `122,306.00` |
| `Live` | `Long` | `0.0358` | 14,980,000.00 USD | 0.00 USD | 214.53 USD | `-54.96%` | `5,984.00` |
| `Live` | `Long` | `0.0362` | 14,980,000.00 USD | 0.00 USD | 980.96 USD | `-54.45%` | `27,061.00` |
| `Live` | `Long` | `0.0364` | 14,980,000.00 USD | 0.00 USD | 194.44 USD | `-54.33%` | `5,349.00` |
| `Live` | `Long` | `0.0369` | 14,980,000.00 USD | 0.00 USD | 28,590.00 USD | `-53.70%` | `775,729.00` |
| `Live` | `Long` | `0.0377` | 14,950,000.00 USD | 0.00 USD | 3,810.00 USD | `-52.70%` | `101,126.00` |
| `Live` | `Long` | `0.0381` | 14,950,000.00 USD | 0.00 USD | 246.45 USD | `-52.19%` | `6,477.00` |
| `Live` | `Long` | `0.0386` | 14,950,000.00 USD | 0.00 USD | 121.74 USD | `-51.56%` | `3,158.00` |
| `Live` | `Long` | `0.0387` | 14,950,000.00 USD | 0.00 USD | 928.92 USD | `-51.31%` | `23,972.00` |
| `Live` | `Long` | `0.0391` | 14,950,000.00 USD | 0.00 USD | 981.92 USD | `-50.81%` | `25,081.00` |
| `Live` | `Long` | `0.0393` | 14,950,000.00 USD | 0.00 USD | 221.10 USD | `-50.69%` | `5,633.00` |
| `Live` | `Long` | `0.0394` | 14,940,000.00 USD | 0.00 USD | 104,570.00 USD | `-50.56%` | `2,657,324.00` |
| `Live` | `Long` | `0.0404` | 14,840,000.00 USD | 0.00 USD | 115.12 USD | `-49.18%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 14,840,000.00 USD | 0.00 USD | 419.28 USD | `-48.80%` | `10,289.00` |
| `Live` | `Long` | `0.0413` | 14,840,000.00 USD | 0.00 USD | 2,070.00 USD | `-48.05%` | `50,080.00` |
| `Live` | `Long` | `0.0415` | 14,840,000.00 USD | 0.00 USD | 252.72 USD | `-47.92%` | `6,097.00` |
| `Live` | `Long` | `0.0415` | 14,840,000.00 USD | 0.00 USD | 1,030.00 USD | `-47.80%` | `24,809.00` |
| `Live` | `Long` | `0.0416` | 14,840,000.00 USD | 0.00 USD | 3,570.00 USD | `-47.67%` | `85,771.00` |
| `Live` | `Long` | `0.0420` | 14,830,000.00 USD | 0.00 USD | 671.41 USD | `-47.29%` | `16,005.00` |
| `Live` | `Long` | `0.0423` | 14,830,000.00 USD | 0.00 USD | 2,090.00 USD | `-46.92%` | `49,468.00` |
| `Live` | `Long` | `0.0423` | 14,830,000.00 USD | 0.00 USD | 59,790.00 USD | `-46.79%` | `1,411,805.00` |
| `Live` | `Long` | `0.0425` | 14,770,000.00 USD | 0.00 USD | 1,070.00 USD | `-46.66%` | `25,181.00` |
| `Live` | `Long` | `0.0425` | 14,770,000.00 USD | 0.00 USD | 1,010.00 USD | `-46.54%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 14,770,000.00 USD | 0.00 USD | 3,620.00 USD | `-46.41%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 14,760,000.00 USD | 0.00 USD | 859.00 USD | `-46.04%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 14,760,000.00 USD | 0.00 USD | 6,430.00 USD | `-45.66%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 14,760,000.00 USD | 0.00 USD | 2,450.00 USD | `-45.53%` | `56,456.00` |
| `Live` | `Long` | `0.0439` | 14,750,000.00 USD | 0.00 USD | 1,610.00 USD | `-44.91%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 14,750,000.00 USD | 0.00 USD | 750.58 USD | `-44.78%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 14,750,000.00 USD | 0.00 USD | 1,060.00 USD | `-44.65%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 14,750,000.00 USD | 0.00 USD | 101,440.00 USD | `-44.28%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 14,650,000.00 USD | 0.00 USD | 444.76 USD | `-43.90%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 14,650,000.00 USD | 0.00 USD | 248.63 USD | `-43.78%` | `5,556.00` |
| `Live` | `Long` | `0.0454` | 14,650,000.00 USD | 0.00 USD | 2,170.00 USD | `-42.90%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,650,000.00 USD | 0.00 USD | 32,650.00 USD | `-42.77%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,610,000.00 USD | 0.00 USD | 5,470.00 USD | `-42.52%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 14,610,000.00 USD | 0.00 USD | 4,500.00 USD | `-42.14%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,600,000.00 USD | 0.00 USD | 114.36 USD | `-42.02%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 14,600,000.00 USD | 0.00 USD | 2,650.00 USD | `-41.76%` | `57,146.00` |
| `Live` | `Long` | `0.0464` | 14,600,000.00 USD | 0.00 USD | 16,780.00 USD | `-41.64%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,580,000.00 USD | 0.00 USD | 109.49 USD | `-41.39%` | `2,347.00` |
| `Live` | `Long` | `0.0473` | 14,580,000.00 USD | 0.00 USD | 18,360.00 USD | `-40.63%` | `388,542.00` |
| `Live` | `Long` | `0.0474` | 14,570,000.00 USD | 0.00 USD | 593.13 USD | `-40.38%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 14,570,000.00 USD | 0.00 USD | 105.02 USD | `-40.13%` | `2,204.00` |
| `Live` | `Long` | `0.0478` | 14,570,000.00 USD | 0.00 USD | 259.23 USD | `-40.01%` | `5,429.00` |
| `Live` | `Long` | `0.0481` | 14,570,000.00 USD | 0.00 USD | 56,440.00 USD | `-39.63%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,510,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.50%` | `51,918.00` |
| `Live` | `Long` | `0.0483` | 14,510,000.00 USD | 0.00 USD | 2,280.00 USD | `-39.25%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,500,000.00 USD | 0.00 USD | 1,480.00 USD | `-39.13%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 14,500,000.00 USD | 0.00 USD | 315.50 USD | `-38.87%` | `6,485.00` |
| `Live` | `Long` | `0.0488` | 14,500,000.00 USD | 0.00 USD | 1,280.00 USD | `-38.62%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,500,000.00 USD | 0.00 USD | 5,470.00 USD | `-38.50%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,500,000.00 USD | 0.00 USD | 1,080.00 USD | `-38.37%` | `21,989.00` |
| `Live` | `Long` | `0.0493` | 14,490,000.00 USD | 0.00 USD | 1,420.00 USD | `-38.00%` | `28,854.00` |
| `Live` | `Long` | `0.0495` | 14,490,000.00 USD | 0.00 USD | 340.41 USD | `-37.87%` | `6,884.00` |
| `Live` | `Long` | `0.0495` | 14,490,000.00 USD | 0.00 USD | 18,690.00 USD | `-37.74%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,470,000.00 USD | 0.00 USD | 253.82 USD | `-37.49%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,470,000.00 USD | 0.00 USD | 501.50 USD | `-37.12%` | `10,020.00` |
| `Live` | `Long` | `0.0502` | 14,470,000.00 USD | 0.00 USD | 384.95 USD | `-36.99%` | `7,676.00` |
| `Live` | `Long` | `0.0503` | 14,470,000.00 USD | 0.00 USD | 5,410.00 USD | `-36.86%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,470,000.00 USD | 0.00 USD | 1,330.00 USD | `-36.74%` | `26,380.00` |
| `Live` | `Long` | `0.0505` | 14,470,000.00 USD | 0.00 USD | 646.42 USD | `-36.61%` | `12,813.00` |
| `Live` | `Long` | `0.0507` | 14,470,000.00 USD | 0.00 USD | 1,040.00 USD | `-36.36%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,460,000.00 USD | 0.00 USD | 5,350.00 USD | `-36.24%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,460,000.00 USD | 0.00 USD | 535.43 USD | `-35.99%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,460,000.00 USD | 0.00 USD | 566.65 USD | `-35.86%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,460,000.00 USD | 0.00 USD | 11,000.00 USD | `-35.73%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,450,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.61%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,450,000.00 USD | 0.00 USD | 385.13 USD | `-35.48%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,450,000.00 USD | 0.00 USD | 308.55 USD | `-35.36%` | `5,997.00` |
| `Live` | `Long` | `0.0515` | 14,450,000.00 USD | 0.00 USD | 296.26 USD | `-35.23%` | `5,747.00` |
| `Live` | `Long` | `0.0519` | 14,440,000.00 USD | 0.00 USD | 51,690.00 USD | `-34.85%` | `996,821.00` |
| `Live` | `Long` | `0.0520` | 14,390,000.00 USD | 0.00 USD | 1,480.00 USD | `-34.73%` | `28,553.00` |
| `Live` | `Long` | `0.0520` | 14,390,000.00 USD | 0.00 USD | 3,990.00 USD | `-34.60%` | `76,663.00` |
| `Live` | `Long` | `0.0522` | 14,390,000.00 USD | 0.00 USD | 275,090.00 USD | `-34.35%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,110,000.00 USD | 0.00 USD | 1,170.00 USD | `-34.10%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,110,000.00 USD | 0.00 USD | 5,640.00 USD | `-33.97%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,110,000.00 USD | 0.00 USD | 395.09 USD | `-33.85%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,110,000.00 USD | 0.00 USD | 2,110.00 USD | `-33.72%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,100,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.60%` | `23,863.00` |
| `Live` | `Long` | `0.0529` | 14,100,000.00 USD | 0.00 USD | 181,690.00 USD | `-33.47%` | `3,431,434.00` |
| `Live` | `Long` | `0.0532` | 13,920,000.00 USD | 0.00 USD | 8,770.00 USD | `-33.22%` | `165,000.00` |
| `Live` | `Long` | `0.0534` | 13,910,000.00 USD | 0.00 USD | 314,750.00 USD | `-32.84%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,600,000.00 USD | 0.00 USD | 1,690.00 USD | `-32.72%` | `31,629.00` |
| `Live` | `Long` | `0.0539` | 13,600,000.00 USD | 0.00 USD | 5,290.00 USD | `-32.22%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,590,000.00 USD | 0.00 USD | 2,290.00 USD | `-32.09%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,590,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.96%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,570,000.00 USD | 0.00 USD | 96,530.00 USD | `-31.84%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,480,000.00 USD | 0.00 USD | 237.95 USD | `-31.59%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,480,000.00 USD | 0.00 USD | 12,420.00 USD | `-31.46%` | `227,742.00` |
| `Live` | `Long` | `0.0546` | 13,460,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.34%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 13,460,000.00 USD | 0.00 USD | 188.07 USD | `-31.21%` | `3,435.00` |
| `Live` | `Long` | `0.0556` | 13,460,000.00 USD | 0.00 USD | 907.02 USD | `-30.21%` | `16,328.00` |
| `Live` | `Long` | `0.0561` | 13,460,000.00 USD | 0.00 USD | 39,500.00 USD | `-29.45%` | `703,392.00` |
| `Live` | `Long` | `0.0563` | 13,420,000.00 USD | 0.00 USD | 1,820.00 USD | `-29.33%` | `32,433.00` |
| `Live` | `Long` | `0.0563` | 13,420,000.00 USD | 0.00 USD | 47,560.00 USD | `-29.20%` | `844,065.00` |
| `Live` | `Long` | `0.0566` | 13,370,000.00 USD | 0.00 USD | 131.48 USD | `-28.95%` | `2,325.00` |
| `Live` | `Long` | `0.0566` | 13,370,000.00 USD | 0.00 USD | 610.80 USD | `-28.82%` | `10,782.00` |
| `Live` | `Long` | `0.0568` | 13,370,000.00 USD | 0.00 USD | 747.06 USD | `-28.70%` | `13,164.00` |
| `Live` | `Long` | `0.0570` | 13,370,000.00 USD | 0.00 USD | 421.03 USD | `-28.45%` | `7,393.00` |
| `Live` | `Long` | `0.0570` | 13,370,000.00 USD | 0.00 USD | 8,350.00 USD | `-28.32%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,360,000.00 USD | 0.00 USD | 644.99 USD | `-28.20%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,360,000.00 USD | 0.00 USD | 3,910.00 USD | `-27.94%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,360,000.00 USD | 0.00 USD | 15,970.00 USD | `-27.82%` | `277,921.00` |
| `Live` | `Long` | `0.0575` | 13,340,000.00 USD | 0.00 USD | 3,590.00 USD | `-27.69%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,340,000.00 USD | 0.00 USD | 10,990.00 USD | `-27.57%` | `190,602.00` |
| `Live` | `Long` | `0.0578` | 13,330,000.00 USD | 0.00 USD | 17,890.00 USD | `-27.44%` | `309,753.00` |
| `Live` | `Long` | `0.0578` | 13,310,000.00 USD | 0.00 USD | 5,710,000.00 USD | `-27.32%` | `98,734,536.00` |
| `Live` | `Long` | `0.0580` | 7,600,000.00 USD | 0.00 USD | 431.14 USD | `-27.06%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 7,600,000.00 USD | 0.00 USD | 447.17 USD | `-26.94%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 7,600,000.00 USD | 0.00 USD | 116.82 USD | `-26.69%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 7,600,000.00 USD | 0.00 USD | 172.78 USD | `-26.44%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 7,600,000.00 USD | 0.00 USD | 9,120.00 USD | `-26.19%` | `155,271.00` |
| `Live` | `Long` | `0.0588` | 7,590,000.00 USD | 0.00 USD | 715.85 USD | `-26.06%` | `12,164.00` |
| `Live` | `Long` | `0.0590` | 7,590,000.00 USD | 0.00 USD | 212.22 USD | `-25.93%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 7,590,000.00 USD | 0.00 USD | 26,980.00 USD | `-25.68%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 7,560,000.00 USD | 0.00 USD | 889.30 USD | `-25.43%` | `14,984.00` |
| `Live` | `Long` | `0.0595` | 7,560,000.00 USD | 0.00 USD | 3,660.00 USD | `-25.31%` | `61,626.00` |
| `Live` | `Long` | `0.0595` | 7,560,000.00 USD | 0.00 USD | 2,650.00 USD | `-25.18%` | `44,458.00` |
| `Live` | `Long` | `0.0599` | 7,550,000.00 USD | 0.00 USD | 4,560.00 USD | `-24.80%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 7,550,000.00 USD | 0.00 USD | 380.38 USD | `-24.68%` | `6,345.00` |
| `Live` | `Long` | `0.0600` | 7,550,000.00 USD | 0.00 USD | 11,540.00 USD | `-24.55%` | `192,164.00` |
| `Live` | `Long` | `0.0602` | 7,540,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.43%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 7,530,000.00 USD | 0.00 USD | 737.18 USD | `-24.17%` | `12,215.00` |
| `Live` | `Long` | `0.0604` | 7,530,000.00 USD | 0.00 USD | 2,730.00 USD | `-24.05%` | `45,226.00` |
| `Live` | `Long` | `0.0605` | 7,520,000.00 USD | 0.00 USD | 32,090.00 USD | `-23.92%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,490,000.00 USD | 0.00 USD | 1,080.00 USD | `-23.80%` | `17,849.00` |
| `Live` | `Long` | `0.0607` | 7,490,000.00 USD | 0.00 USD | 1,220.00 USD | `-23.67%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 717.73 USD | `-23.55%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 2,220.00 USD | `-23.42%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 913.21 USD | `-23.17%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 298.17 USD | `-23.04%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 655.16 USD | `-22.92%` | `10,679.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 368.58 USD | `-22.79%` | `5,998.00` |
| `Live` | `Long` | `0.0616` | 7,480,000.00 USD | 0.00 USD | 1,400.00 USD | `-22.67%` | `22,725.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 13,460.00 USD | `-22.54%` | `218,374.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 158.08 USD | `-22.42%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-22.04%` | `431,787.00` |
| `Live` | `Long` | `0.0622` | 7,440,000.00 USD | 0.00 USD | 1,820.00 USD | `-21.79%` | `29,227.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-21.66%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 3,470.00 USD | `-21.54%` | `55,505.00` |
| `Live` | `Long` | `0.0625` | 7,440,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-21.41%` | `17,642,013.00` |
| `Live` | `Long` | `0.0626` | 6,330,000.00 USD | 0.00 USD | 3,900.00 USD | `-21.29%` | `62,300.00` |
| `Live` | `Long` | `0.0628` | 6,330,000.00 USD | 0.00 USD | 461.78 USD | `-21.16%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,330,000.00 USD | 0.00 USD | 6,400.00 USD | `-21.03%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 255.95 USD | `-20.91%` | `4,066.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 3,080.00 USD | `-20.78%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,320,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-20.66%` | `17,355,385.00` |
| `Live` | `Long` | `0.0633` | 5,220,000.00 USD | 0.00 USD | 1,210.00 USD | `-20.53%` | `19,161.00` |
| `Live` | `Long` | `0.0634` | 5,220,000.00 USD | 0.00 USD | 12,890.00 USD | `-20.41%` | `203,485.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-20.28%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 280.95 USD | `-20.15%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,210,000.00 USD | 0.00 USD | 633.38 USD | `-20.03%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,210,000.00 USD | 0.00 USD | 8,670.00 USD | `-19.90%` | `136,018.00` |
| `Live` | `Long` | `0.0639` | 5,200,000.00 USD | 0.00 USD | 23,220.00 USD | `-19.78%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,170,000.00 USD | 0.00 USD | 1,360.00 USD | `-19.65%` | `21,194.00` |
| `Live` | `Long` | `0.0640` | 5,170,000.00 USD | 0.00 USD | 2,170.00 USD | `-19.53%` | `33,802.00` |
| `Live` | `Long` | `0.0641` | 5,170,000.00 USD | 0.00 USD | 633.29 USD | `-19.40%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,170,000.00 USD | 0.00 USD | 9,150.00 USD | `-19.27%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 2,170.00 USD | `-19.15%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 23,930.00 USD | `-19.02%` | `371,302.00` |
| `Live` | `Long` | `0.0646` | 5,130,000.00 USD | 0.00 USD | 6,350.00 USD | `-18.77%` | `98,215.00` |
| `Live` | `Long` | `0.0648` | 5,130,000.00 USD | 0.00 USD | 107,370.00 USD | `-18.65%` | `1,658,260.00` |
| `Live` | `Long` | `0.0649` | 5,020,000.00 USD | 0.00 USD | 10,520.00 USD | `-18.52%` | `162,199.00` |
| `Live` | `Long` | `0.0649` | 5,010,000.00 USD | 0.00 USD | 44,290.00 USD | `-18.40%` | `681,858.00` |
| `Live` | `Long` | `0.0651` | 4,970,000.00 USD | 0.00 USD | 2,380.00 USD | `-18.14%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,960,000.00 USD | 0.00 USD | 13,770.00 USD | `-18.02%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 4,950,000.00 USD | 0.00 USD | 6,530.00 USD | `-17.89%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,940,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.64%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 4,940,000.00 USD | 0.00 USD | 71,100.00 USD | `-17.39%` | `1,081,348.00` |
| `Live` | `Long` | `0.0659` | 4,870,000.00 USD | 0.00 USD | 14,870.00 USD | `-17.26%` | `225,881.00` |
| `Live` | `Long` | `0.0659` | 4,850,000.00 USD | 0.00 USD | 11,990.00 USD | `-17.14%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,840,000.00 USD | 0.00 USD | 339.48 USD | `-16.89%` | `5,132.00` |
| `Live` | `Long` | `0.0663` | 4,840,000.00 USD | 0.00 USD | 1,630.00 USD | `-16.76%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,840,000.00 USD | 0.00 USD | 27,760.00 USD | `-16.64%` | `418,455.00` |
| `Live` | `Long` | `0.0664` | 4,810,000.00 USD | 0.00 USD | 1,030.00 USD | `-16.51%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,810,000.00 USD | 0.00 USD | 66,720.00 USD | `-16.39%` | `1,002,594.00` |
| `Live` | `Long` | `0.0667` | 4,740,000.00 USD | 0.00 USD | 34,860.00 USD | `-16.26%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,710,000.00 USD | 0.00 USD | 1,490.00 USD | `-16.13%` | `22,334.00` |
| `Live` | `Long` | `0.0669` | 4,710,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-16.01%` | `15,241,324.00` |
| `Live` | `Long` | `0.0669` | 3,690,000.00 USD | 0.00 USD | 389.18 USD | `-15.88%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,690,000.00 USD | 0.00 USD | 6,240.00 USD | `-15.76%` | `93,089.00` |
| `Live` | `Long` | `0.0672` | 3,680,000.00 USD | 0.00 USD | 899.27 USD | `-15.63%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 196.64 USD | `-15.51%` | `2,924.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 96,400.00 USD | `-15.38%` | `1,431,289.00` |
| `Live` | `Long` | `0.0674` | 3,580,000.00 USD | 0.00 USD | 4,860.00 USD | `-15.25%` | `72,079.00` |
| `Live` | `Long` | `0.0675` | 3,580,000.00 USD | 0.00 USD | 310.73 USD | `-15.13%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,580,000.00 USD | 0.00 USD | 8,210.00 USD | `-15.00%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,570,000.00 USD | 0.00 USD | 5,100.00 USD | `-14.88%` | `75,221.00` |
| `Live` | `Long` | `0.0678` | 3,560,000.00 USD | 0.00 USD | 55,180.00 USD | `-14.75%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,510,000.00 USD | 0.00 USD | 20,030.00 USD | `-14.63%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,490,000.00 USD | 0.00 USD | 212.72 USD | `-14.50%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,490,000.00 USD | 0.00 USD | 1,680.00 USD | `-14.37%` | `24,721.00` |
| `Live` | `Long` | `0.0683` | 3,490,000.00 USD | 0.00 USD | 6,220.00 USD | `-14.25%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,480,000.00 USD | 0.00 USD | 1,290.00 USD | `-14.12%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,480,000.00 USD | 0.00 USD | 88,260.00 USD | `-14.00%` | `1,289,438.00` |
| `Live` | `Long` | `0.0685` | 3,390,000.00 USD | 0.00 USD | 4,690.00 USD | `-13.87%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,390,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.75%` | `20,568.00` |
| `Live` | `Long` | `0.0688` | 3,390,000.00 USD | 0.00 USD | 69,020.00 USD | `-13.62%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,320,000.00 USD | 0.00 USD | 517.48 USD | `-13.50%` | `7,516.00` |
| `Live` | `Long` | `0.0689` | 3,320,000.00 USD | 0.00 USD | 507,660.00 USD | `-13.37%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,810,000.00 USD | 0.00 USD | 3,670.00 USD | `-13.24%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,800,000.00 USD | 0.00 USD | 8,350.00 USD | `-13.12%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,800,000.00 USD | 0.00 USD | 52,390.00 USD | `-12.87%` | `755,504.00` |
| `Live` | `Long` | `0.0694` | 2,740,000.00 USD | 0.00 USD | 4,840.00 USD | `-12.74%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,740,000.00 USD | 0.00 USD | 106,510.00 USD | `-12.62%` | `1,531,348.00` |
| `Live` | `Long` | `0.0697` | 2,630,000.00 USD | 0.00 USD | 5,240.00 USD | `-12.49%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,630,000.00 USD | 0.00 USD | 3,420.00 USD | `-12.36%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,620,000.00 USD | 0.00 USD | 3,630.00 USD | `-12.24%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,620,000.00 USD | 0.00 USD | 9,500.00 USD | `-12.11%` | `135,877.00` |
| `Live` | `Long` | `0.0701` | 2,610,000.00 USD | 0.00 USD | 264.58 USD | `-11.99%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,610,000.00 USD | 0.00 USD | 1,590.00 USD | `-11.86%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 2,000.00 USD | `-11.74%` | `28,486.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 5,060.00 USD | `-11.61%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,600,000.00 USD | 0.00 USD | 216.56 USD | `-11.48%` | `3,074.00` |
| `Live` | `Long` | `0.0706` | 2,600,000.00 USD | 0.00 USD | 93,610.00 USD | `-11.36%` | `1,326,872.00` |
| `Live` | `Long` | `0.0707` | 2,510,000.00 USD | 0.00 USD | 536.00 USD | `-11.11%` | `7,576.00` |
| `Live` | `Long` | `0.0711` | 2,510,000.00 USD | 0.00 USD | 111.69 USD | `-10.73%` | `1,572.00` |
| `Live` | `Long` | `0.0712` | 2,510,000.00 USD | 0.00 USD | 2,600.00 USD | `-10.48%` | `36,465.00` |
| `Live` | `Long` | `0.0713` | 2,500,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-10.35%` | `24,460,119.00` |
| `Live` | `Long` | `0.0714` | 759,520.00 USD | 0.00 USD | 2,220.00 USD | `-10.23%` | `31,003.00` |
| `Live` | `Long` | `0.0716` | 757,300.00 USD | 0.00 USD | 8,120.00 USD | `-10.10%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 749,190.00 USD | 0.00 USD | 560.88 USD | `-9.98%` | `7,828.00` |
| `Live` | `Long` | `0.0717` | 748,630.00 USD | 0.00 USD | 1,520.00 USD | `-9.85%` | `21,127.00` |
| `Live` | `Long` | `0.0718` | 747,110.00 USD | 0.00 USD | 10,850.00 USD | `-9.73%` | `151,060.00` |
| `Live` | `Long` | `0.0720` | 736,260.00 USD | 0.00 USD | 778.93 USD | `-9.60%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 735,480.00 USD | 0.00 USD | 23,870.00 USD | `-9.47%` | `331,347.00` |
| `Live` | `Long` | `0.0722` | 711,610.00 USD | 0.00 USD | 5,720.00 USD | `-9.22%` | `79,141.00` |
| `Live` | `Long` | `0.0723` | 705,890.00 USD | 0.00 USD | 4,900.00 USD | `-9.10%` | `67,698.00` |
| `Live` | `Long` | `0.0725` | 700,990.00 USD | 0.00 USD | 598.51 USD | `-8.97%` | `8,261.00` |
| `Live` | `Long` | `0.0726` | 700,390.00 USD | 0.00 USD | 260.74 USD | `-8.85%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 700,130.00 USD | 0.00 USD | 948.37 USD | `-8.72%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 699,180.00 USD | 0.00 USD | 3,170.00 USD | `-8.60%` | `43,539.00` |
| `Live` | `Long` | `0.0728` | 696,010.00 USD | 0.00 USD | 646.11 USD | `-8.47%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 695,370.00 USD | 0.00 USD | 72,950.00 USD | `-8.34%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 622,420.00 USD | 0.00 USD | 10,300.00 USD | `-8.22%` | `141,047.00` |
| `Live` | `Long` | `0.0732` | 612,120.00 USD | 0.00 USD | 1,930.00 USD | `-8.09%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 610,190.00 USD | 0.00 USD | 5,410.00 USD | `-7.97%` | `73,796.00` |
| `Live` | `Long` | `0.0735` | 604,780.00 USD | 0.00 USD | 7,000.00 USD | `-7.72%` | `95,360.00` |
| `Live` | `Long` | `0.0736` | 597,780.00 USD | 0.00 USD | 4,060.00 USD | `-7.59%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 593,720.00 USD | 0.00 USD | 5,490.00 USD | `-7.46%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 588,230.00 USD | 0.00 USD | 10,390.00 USD | `-7.34%` | `140,949.00` |
| `Live` | `Long` | `0.0738` | 577,830.00 USD | 0.00 USD | 5,630.00 USD | `-7.21%` | `76,281.00` |
| `Live` | `Long` | `0.0740` | 572,200.00 USD | 0.00 USD | 13,570.00 USD | `-7.09%` | `183,446.00` |
| `Live` | `Long` | `0.0741` | 558,630.00 USD | 0.00 USD | 455,270.00 USD | `-6.96%` | `6,148,098.00` |
| `Live` | `Long` | `0.0741` | 103,370.00 USD | 0.00 USD | 777.39 USD | `-6.84%` | `10,484.00` |
| `Live` | `Long` | `0.0742` | 102,590.00 USD | 0.00 USD | 2,360.00 USD | `-6.71%` | `31,741.00` |
| `Live` | `Long` | `0.0743` | 100,230.00 USD | 0.00 USD | 2,140.00 USD | `-6.58%` | `28,845.00` |
| `Live` | `Long` | `0.0745` | 98,090.00 USD | 0.00 USD | 2,040.00 USD | `-6.46%` | `27,364.00` |
| `Live` | `Long` | `0.0746` | 96,050.00 USD | 0.00 USD | 581.34 USD | `-6.33%` | `7,798.00` |
| `Live` | `Long` | `0.0746` | 95,470.00 USD | 0.00 USD | 1,050.00 USD | `-6.21%` | `14,085.00` |
| `Live` | `Long` | `0.0747` | 94,420.00 USD | 0.00 USD | 359.77 USD | `-6.08%` | `4,813.00` |
| `Live` | `Long` | `0.0750` | 94,060.00 USD | 0.00 USD | 1,370.00 USD | `-5.83%` | `18,241.00` |
| `Live` | `Long` | `0.0751` | 92,690.00 USD | 0.00 USD | 451.13 USD | `-5.71%` | `6,011.00` |
| `Live` | `Long` | `0.0751` | 92,240.00 USD | 0.00 USD | 2,450.00 USD | `-5.58%` | `32,634.00` |
| `Live` | `Long` | `0.0752` | 89,790.00 USD | 0.00 USD | 3,910.00 USD | `-5.45%` | `51,995.00` |
| `Live` | `Long` | `0.0754` | 85,870.00 USD | 0.00 USD | 617.57 USD | `-5.33%` | `8,196.00` |
| `Live` | `Long` | `0.0755` | 85,260.00 USD | 0.00 USD | 4,060.00 USD | `-5.20%` | `53,747.00` |
| `Live` | `Long` | `0.0756` | 81,200.00 USD | 0.00 USD | 12,630.00 USD | `-5.08%` | `167,209.00` |
| `Live` | `Long` | `0.0756` | 68,570.00 USD | 0.00 USD | 356.24 USD | `-4.95%` | `4,709.00` |
| `Live` | `Long` | `0.0757` | 68,210.00 USD | 0.00 USD | 2,510.00 USD | `-4.83%` | `33,158.00` |
| `Live` | `Long` | `0.0759` | 65,700.00 USD | 0.00 USD | 5,070.00 USD | `-4.70%` | `66,803.00` |
| `Live` | `Long` | `0.0760` | 60,630.00 USD | 0.00 USD | 32,080.00 USD | `-4.57%` | `422,343.00` |
| `Live` | `Long` | `0.0761` | 28,560.00 USD | 0.00 USD | 1,690.00 USD | `-4.45%` | `22,243.00` |
| `Live` | `Long` | `0.0761` | 26,870.00 USD | 0.00 USD | 1,130.00 USD | `-4.32%` | `14,810.00` |
| `Live` | `Long` | `0.0762` | 25,740.00 USD | 0.00 USD | 181.93 USD | `-4.20%` | `2,386.00` |
| `Live` | `Long` | `0.0764` | 25,560.00 USD | 0.00 USD | 11,510.00 USD | `-4.07%` | `150,696.00` |
| `Live` | `Long` | `0.0765` | 14,050.00 USD | 0.00 USD | 9,890.00 USD | `-3.95%` | `129,368.00` |
| `Live` | `Long` | `0.0789` | 4,160.00 USD | 0.00 USD | 4,160.00 USD | `-0.93%` | `52,764.00` |
| `Live` | `Short` | `0.0805` | 145.88 USD | 145.88 USD | 0.00 USD | `+1.20%` | `1,811.00` |
| `Live` | `Short` | `0.0818` | 855.96 USD | 710.08 USD | 0.00 USD | `+2.71%` | `8,686.00` |
| `Live` | `Short` | `0.0829` | 28,140.00 USD | 27,290.00 USD | 0.00 USD | `+4.22%` | `328,961.00` |
| `Live` | `Short` | `0.0832` | 39,470.00 USD | 11,330.00 USD | 0.00 USD | `+4.47%` | `136,223.00` |
| `Live` | `Short` | `0.0835` | 39,680.00 USD | 205.70 USD | 0.00 USD | `+4.97%` | `2,462.00` |
| `Live` | `Short` | `0.0837` | 39,690.00 USD | 13.30 USD | 0.00 USD | `+5.10%` | `159.00` |
| `Live` | `Short` | `0.0838` | 41,260.00 USD | 1,570.00 USD | 0.00 USD | `+5.23%` | `18,767.00` |
| `Live` | `Short` | `0.0839` | 41,370.00 USD | 104.69 USD | 0.00 USD | `+5.48%` | `1,247.00` |
| `Live` | `Short` | `0.0840` | 58,880.00 USD | 17,520.00 USD | 0.00 USD | `+5.60%` | `208,401.00` |
| `Live` | `Short` | `0.0842` | 68,420.00 USD | 9,530.00 USD | 0.00 USD | `+5.73%` | `113,306.00` |
| `Live` | `Short` | `0.0843` | 68,520.00 USD | 104.72 USD | 0.00 USD | `+5.85%` | `1,243.00` |
| `Live` | `Short` | `0.0847` | 68,730.00 USD | 213.74 USD | 0.00 USD | `+6.36%` | `2,525.00` |
| `Live` | `Short` | `0.0851` | 68,950.00 USD | 214.75 USD | 0.00 USD | `+6.86%` | `2,525.00` |
| `Live` | `Short` | `0.0858` | 69,060.00 USD | 115.30 USD | 0.00 USD | `+7.86%` | `1,343.00` |
| `Live` | `Short` | `0.0862` | 71,410.00 USD | 2,340.00 USD | 0.00 USD | `+8.37%` | `27,165.00` |
| `Live` | `Short` | `0.0876` | 81,030.00 USD | 9,620.00 USD | 0.00 USD | `+10.00%` | `109,908.00` |
| `Live` | `Short` | `0.0881` | 81,500.00 USD | 465.17 USD | 0.00 USD | `+10.63%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 81,910.00 USD | 411.53 USD | 0.00 USD | `+11.51%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 82,330.00 USD | 418.80 USD | 0.00 USD | `+11.88%` | `4,703.00` |
| `Live` | `Short` | `0.0892` | 82,430.00 USD | 106.21 USD | 0.00 USD | `+12.14%` | `1,190.00` |
| `Live` | `Short` | `0.0895` | 82,720.00 USD | 285.70 USD | 0.00 USD | `+12.39%` | `3,194.00` |
| `Live` | `Short` | `0.0900` | 82,940.00 USD | 226.85 USD | 0.00 USD | `+13.02%` | `2,522.00` |
| `Live` | `Short` | `0.0902` | 83,820.00 USD | 878.67 USD | 0.00 USD | `+13.39%` | `9,736.00` |
| `Live` | `Short` | `0.0906` | 87,900.00 USD | 4,070.00 USD | 0.00 USD | `+13.77%` | `45,000.00` |
| `Live` | `Short` | `0.0909` | 91,410.00 USD | 3,510.00 USD | 0.00 USD | `+14.15%` | `38,669.00` |
| `Live` | `Short` | `0.0911` | 92,150.00 USD | 743.15 USD | 0.00 USD | `+14.52%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 96,200.00 USD | 4,040.00 USD | 0.00 USD | `+14.65%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 96,370.00 USD | 171.19 USD | 0.00 USD | `+14.77%` | `1,874.00` |
| `Live` | `Short` | `0.0917` | 96,710.00 USD | 344.43 USD | 0.00 USD | `+15.28%` | `3,754.00` |
| `Live` | `Short` | `0.0921` | 96,890.00 USD | 171.49 USD | 0.00 USD | `+15.65%` | `1,863.00` |
| `Live` | `Short` | `0.0927` | 97,070.00 USD | 188.75 USD | 0.00 USD | `+16.53%` | `2,035.00` |
| `Live` | `Short` | `0.0935` | 100,370.00 USD | 3,300.00 USD | 0.00 USD | `+17.41%` | `35,291.00` |
| `Live` | `Short` | `0.0949` | 100,950.00 USD | 573.84 USD | 0.00 USD | `+19.17%` | `6,050.00` |
| `Live` | `Short` | `0.0950` | 114,740.00 USD | 13,800.00 USD | 0.00 USD | `+19.30%` | `145,305.00` |
| `Live` | `Short` | `0.0951` | 228,920.00 USD | 114,180.00 USD | 0.00 USD | `+19.55%` | `1,200,000.00` |
| `Live` | `Short` | `0.0959` | 229,670.00 USD | 747.55 USD | 0.00 USD | `+20.55%` | `7,791.00` |
| `Live` | `Short` | `0.0961` | 230,280.00 USD | 609.59 USD | 0.00 USD | `+20.81%` | `6,340.00` |
| `Live` | `Short` | `0.0965` | 278,560.00 USD | 48,270.00 USD | 0.00 USD | `+21.31%` | `500,000.00` |
| `Live` | `Short` | `0.0979` | 317,750.00 USD | 39,190.00 USD | 0.00 USD | `+22.94%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 318,220.00 USD | 477.50 USD | 0.00 USD | `+23.44%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 328,740.00 USD | 10,510.00 USD | 0.00 USD | `+23.69%` | `106,785.00` |
| `Live` | `Short` | `0.1001` | 330,020.00 USD | 1,280.00 USD | 0.00 USD | `+25.71%` | `12,841.00` |
| `Live` | `Short` | `0.1014` | 338,650.00 USD | 8,630.00 USD | 0.00 USD | `+27.46%` | `85,018.00` |
| `Live` | `Short` | `0.1017` | 341,620.00 USD | 2,970.00 USD | 0.00 USD | `+27.72%` | `29,214.00` |
| `Live` | `Short` | `0.1017` | 341,800.00 USD | 178.77 USD | 0.00 USD | `+27.84%` | `1,757.00` |
| `Live` | `Short` | `0.1018` | 342,290.00 USD | 492.85 USD | 0.00 USD | `+27.97%` | `4,839.00` |
| `Live` | `Short` | `0.1061` | 348,400.00 USD | 6,110.00 USD | 0.00 USD | `+33.37%` | `57,554.00` |
| `Live` | `Short` | `0.1066` | 349,980.00 USD | 1,580.00 USD | 0.00 USD | `+34.00%` | `14,835.00` |
| `Live` | `Short` | `0.1072` | 353,190.00 USD | 3,210.00 USD | 0.00 USD | `+34.75%` | `29,960.00` |
| `Live` | `Short` | `0.1109` | 356,630.00 USD | 3,440.00 USD | 0.00 USD | `+39.27%` | `31,000.00` |
| `Live` | `Short` | `0.1127` | 356,840.00 USD | 214.15 USD | 0.00 USD | `+41.54%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 356,990.00 USD | 142.88 USD | 0.00 USD | `+41.91%` | `1,265.00` |
| `Live` | `Short` | `0.1130` | 359,350.00 USD | 2,370.00 USD | 0.00 USD | `+42.04%` | `20,943.00` |
| `Live` | `Short` | `0.1187` | 359,480.00 USD | 121.85 USD | 0.00 USD | `+49.07%` | `1,027.00` |
| `Live` | `Short` | `0.1212` | 359,840.00 USD | 363.75 USD | 0.00 USD | `+52.34%` | `3,000.00` |
| `Live` | `Short` | `0.1222` | 360,640.00 USD | 796.83 USD | 0.00 USD | `+53.60%` | `6,518.00` |
| `Live` | `Short` | `0.1255` | 362,150.00 USD | 1,520.00 USD | 0.00 USD | `+57.62%` | `12,089.00` |
| `Live` | `Short` | `0.1268` | 362,790.00 USD | 633.75 USD | 0.00 USD | `+59.25%` | `5,000.00` |
| `Live` | `Short` | `0.1270` | 362,900.00 USD | 108.80 USD | 0.00 USD | `+59.50%` | `857.00` |
| `Live` | `Short` | `0.1273` | 363,380.00 USD | 486.73 USD | 0.00 USD | `+60.01%` | `3,822.00` |
| `Live` | `Short` | `0.1286` | 3,050,000.00 USD | 2,690,000.00 USD | 0.00 USD | `+61.64%` | `20,910,149.00` |
| `Live` | `Short` | `0.1296` | 3,050,000.00 USD | 171.66 USD | 0.00 USD | `+62.90%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 3,060,000.00 USD | 2,140.00 USD | 0.00 USD | `+64.78%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 3,060,000.00 USD | 102.97 USD | 0.00 USD | `+65.66%` | `781.00` |
| `Live` | `Short` | `0.1338` | 3,060,000.00 USD | 205.31 USD | 0.00 USD | `+68.05%` | `1,535.00` |
| `Live` | `Short` | `0.1388` | 3,060,000.00 USD | 1,000.00 USD | 0.00 USD | `+74.33%` | `7,219.00` |
| `Live` | `Short` | `0.1394` | 3,080,000.00 USD | 22,620.00 USD | 0.00 USD | `+75.21%` | `162,180.00` |
| `Live` | `Short` | `0.1396` | 3,080,000.00 USD | 1,820.00 USD | 0.00 USD | `+75.33%` | `13,010.00` |
| `Live` | `Short` | `0.1404` | 3,080,000.00 USD | 663.63 USD | 0.00 USD | `+76.46%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 3,080,000.00 USD | 1,800.00 USD | 0.00 USD | `+77.34%` | `12,780.00` |
| `Live` | `Short` | `0.1436` | 3,080,000.00 USD | 677.99 USD | 0.00 USD | `+80.36%` | `4,723.00` |
| `Live` | `Short` | `0.1436` | 3,080,000.00 USD | 135.03 USD | 0.00 USD | `+80.49%` | `940.00` |
| `Live` | `Short` | `0.1479` | 3,090,000.00 USD | 8,360.00 USD | 0.00 USD | `+85.76%` | `56,553.00` |
| `Live` | `Short` | `0.1487` | 3,090,000.00 USD | 393.33 USD | 0.00 USD | `+86.77%` | `2,646.00` |
| `Live` | `Short` | `0.1489` | 3,100,000.00 USD | 2,380.00 USD | 0.00 USD | `+87.14%` | `16,000.00` |
| `Live` | `Short` | `0.1509` | 3,100,000.00 USD | 340.62 USD | 0.00 USD | `+89.53%` | `2,258.00` |
| `Live` | `Short` | `0.1514` | 3,150,000.00 USD | 56,670.00 USD | 0.00 USD | `+90.16%` | `374,415.00` |
| `Live` | `Short` | `0.1515` | 3,150,000.00 USD | 2,010.00 USD | 0.00 USD | `+90.41%` | `13,240.00` |
| `Live` | `Short` | `0.1525` | 3,160,000.00 USD | 267.55 USD | 0.00 USD | `+91.54%` | `1,755.00` |
| `Live` | `Short` | `0.1527` | 3,160,000.00 USD | 389.72 USD | 0.00 USD | `+91.79%` | `2,553.00` |
| `Live` | `Short` | `0.1535` | 3,190,000.00 USD | 30,270.00 USD | 0.00 USD | `+92.92%` | `197,142.00` |
| `Live` | `Short` | `0.1563` | 3,190,000.00 USD | 340.06 USD | 0.00 USD | `+96.44%` | `2,175.00` |
| `Live` | `Short` | `0.1570` | 3,190,000.00 USD | 4,830.00 USD | 0.00 USD | `+97.20%` | `30,755.00` |
| `Live` | `Short` | `0.1570` | 3,190,000.00 USD | 980.15 USD | 0.00 USD | `+97.32%` | `6,241.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 588,450.00 USD | 0.00 USD | 375.42 USD | `-67.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 588,070.00 USD | 0.00 USD | 409.59 USD | `-49.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 587,660.00 USD | 0.00 USD | 132.68 USD | `-48.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 587,530.00 USD | 0.00 USD | 286.87 USD | `-43.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 587,240.00 USD | 0.00 USD | 252.42 USD | `-41.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 586,990.00 USD | 0.00 USD | 468.67 USD | `-40.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 586,520.00 USD | 0.00 USD | 5,160.00 USD | `-38.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 581,360.00 USD | 0.00 USD | 920.48 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 580,440.00 USD | 0.00 USD | 1,860.00 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 578,580.00 USD | 0.00 USD | 175.41 USD | `-35.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 578,400.00 USD | 0.00 USD | 1,370.00 USD | `-30.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 577,030.00 USD | 0.00 USD | 437.58 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 576,590.00 USD | 0.00 USD | 752.54 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 575,840.00 USD | 0.00 USD | 9,830.00 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 566,010.00 USD | 0.00 USD | 1,270.00 USD | `-25.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 564,740.00 USD | 0.00 USD | 1,560.00 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 563,180.00 USD | 0.00 USD | 134.12 USD | `-24.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 563,050.00 USD | 0.00 USD | 8,800.00 USD | `-23.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 554,250.00 USD | 0.00 USD | 504.26 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 553,740.00 USD | 0.00 USD | 4,200.00 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 549,540.00 USD | 0.00 USD | 1,280.00 USD | `-21.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 548,260.00 USD | 0.00 USD | 920.18 USD | `-19.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 547,340.00 USD | 0.00 USD | 370.79 USD | `-19.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 546,970.00 USD | 0.00 USD | 1,130.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 545,840.00 USD | 0.00 USD | 362.24 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 545,480.00 USD | 0.00 USD | 3,140.00 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 542,340.00 USD | 0.00 USD | 1,200.00 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 541,140.00 USD | 0.00 USD | 996.31 USD | `-17.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 540,140.00 USD | 0.00 USD | 632.88 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 539,510.00 USD | 0.00 USD | 115.57 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 539,400.00 USD | 0.00 USD | 33,620.00 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 505,770.00 USD | 0.00 USD | 12,860.00 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 492,910.00 USD | 0.00 USD | 1,260.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 491,650.00 USD | 0.00 USD | 108.08 USD | `-15.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 491,540.00 USD | 0.00 USD | 2,960.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 488,580.00 USD | 0.00 USD | 1,430.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 487,150.00 USD | 0.00 USD | 7,990.00 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 479,160.00 USD | 0.00 USD | 8,580.00 USD | `-14.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 470,580.00 USD | 0.00 USD | 606.47 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 469,970.00 USD | 0.00 USD | 38,710.00 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 431,270.00 USD | 0.00 USD | 660.06 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 430,610.00 USD | 0.00 USD | 102.34 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 430,510.00 USD | 0.00 USD | 697.50 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 429,810.00 USD | 0.00 USD | 699.90 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 429,110.00 USD | 0.00 USD | 17,020.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 412,090.00 USD | 0.00 USD | 895.27 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 411,190.00 USD | 0.00 USD | 523.23 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 410,670.00 USD | 0.00 USD | 235.12 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 410,430.00 USD | 0.00 USD | 134.92 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 410,300.00 USD | 0.00 USD | 107,230.00 USD | `-10.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 303,070.00 USD | 0.00 USD | 12,930.00 USD | `-10.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 290,140.00 USD | 0.00 USD | 20,070.00 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 270,070.00 USD | 0.00 USD | 233.74 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 269,840.00 USD | 0.00 USD | 16,880.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 252,960.00 USD | 0.00 USD | 1,670.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 251,290.00 USD | 0.00 USD | 4,710.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 246,580.00 USD | 0.00 USD | 15,380.00 USD | `-9.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 231,190.00 USD | 0.00 USD | 413.42 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 230,780.00 USD | 0.00 USD | 703.43 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 230,080.00 USD | 0.00 USD | 621.12 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 229,460.00 USD | 0.00 USD | 1,700.00 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 227,760.00 USD | 0.00 USD | 29,060.00 USD | `-8.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 198,700.00 USD | 0.00 USD | 976.95 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 197,720.00 USD | 0.00 USD | 2,090.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 195,630.00 USD | 0.00 USD | 28,750.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 166,880.00 USD | 0.00 USD | 2,710.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 164,170.00 USD | 0.00 USD | 115.12 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 164,060.00 USD | 0.00 USD | 4,680.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 159,380.00 USD | 0.00 USD | 1,640.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 157,740.00 USD | 0.00 USD | 2,900.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 154,840.00 USD | 0.00 USD | 107.66 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 154,730.00 USD | 0.00 USD | 5,000.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 149,740.00 USD | 0.00 USD | 1,410.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 148,320.00 USD | 0.00 USD | 375.86 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 147,950.00 USD | 0.00 USD | 193.90 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 147,750.00 USD | 0.00 USD | 140.04 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 147,610.00 USD | 0.00 USD | 10,030.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 137,580.00 USD | 0.00 USD | 323.62 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 137,260.00 USD | 0.00 USD | 736.17 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 136,520.00 USD | 0.00 USD | 192.73 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 136,330.00 USD | 0.00 USD | 358.13 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 135,970.00 USD | 0.00 USD | 4,880.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 131,090.00 USD | 0.00 USD | 193.49 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 130,900.00 USD | 0.00 USD | 2,280.00 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 128,620.00 USD | 0.00 USD | 3,130.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 125,490.00 USD | 0.00 USD | 806.81 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0762` | 124,680.00 USD | 0.00 USD | 359.60 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0765` | 124,320.00 USD | 0.00 USD | 1,320.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 123,000.00 USD | 0.00 USD | 1,130.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 121,870.00 USD | 0.00 USD | 3,540.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0767` | 118,330.00 USD | 0.00 USD | 176.91 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0769` | 118,160.00 USD | 0.00 USD | 193.74 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0770` | 117,960.00 USD | 0.00 USD | 11,510.00 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0771` | 106,450.00 USD | 0.00 USD | 4,340.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0772` | 102,110.00 USD | 0.00 USD | 4,340.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0774` | 97,780.00 USD | 0.00 USD | 323.40 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 97,460.00 USD | 0.00 USD | 2,450.00 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 95,010.00 USD | 0.00 USD | 604.81 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0776` | 94,400.00 USD | 0.00 USD | 992.37 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0777` | 93,410.00 USD | 0.00 USD | 41,810.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0779` | 51,610.00 USD | 0.00 USD | 17,270.00 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 34,340.00 USD | 0.00 USD | 3,000.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 31,330.00 USD | 0.00 USD | 1,700.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0781` | 29,630.00 USD | 0.00 USD | 1,350.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0783` | 28,290.00 USD | 0.00 USD | 120.66 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0784` | 28,170.00 USD | 0.00 USD | 4,200.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 23,960.00 USD | 0.00 USD | 573.31 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 23,390.00 USD | 0.00 USD | 166.84 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0786` | 23,220.00 USD | 0.00 USD | 495.57 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0788` | 22,730.00 USD | 0.00 USD | 3,030.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0789` | 19,700.00 USD | 0.00 USD | 497.86 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 19,200.00 USD | 0.00 USD | 706.60 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 18,490.00 USD | 0.00 USD | 10,230.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0791` | 8,270.00 USD | 0.00 USD | 4,600.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0793` | 3,670.00 USD | 0.00 USD | 2,260.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0794` | 1,410.00 USD | 0.00 USD | 1,010.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0795` | 397.17 USD | 0.00 USD | 148.25 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0795` | 248.91 USD | 0.00 USD | 248.91 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 2,130.00 USD | 2,130.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 2,480.00 USD | 342.85 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 6,940.00 USD | 4,460.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 8,060.00 USD | 1,120.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 12,400.00 USD | 4,350.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 12,850.00 USD | 443.63 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 13,190.00 USD | 346.04 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 13,330.00 USD | 141.34 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 14,040.00 USD | 707.08 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 16,300.00 USD | 2,260.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 113,080.00 USD | 96,780.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 113,350.00 USD | 264.54 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 115,500.00 USD | 2,160.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 115,930.00 USD | 424.74 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 116,940.00 USD | 1,010.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 118,320.00 USD | 1,380.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 118,580.00 USD | 264.63 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 120,020.00 USD | 1,430.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 120,510.00 USD | 492.77 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 121,890.00 USD | 1,380.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 124,800.00 USD | 2,920.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 134,160.00 USD | 9,360.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 137,170.00 USD | 3,010.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 137,710.00 USD | 534.72 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 138,110.00 USD | 402.62 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 151,910.00 USD | 13,790.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 155,890.00 USD | 3,980.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 156,400.00 USD | 512.05 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 157,480.00 USD | 1,080.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 157,870.00 USD | 389.31 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 158,170.00 USD | 303.56 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 158,280.00 USD | 112.89 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 158,670.00 USD | 381.45 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 158,820.00 USD | 155.82 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 159,220.00 USD | 399.52 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 159,570.00 USD | 348.82 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 160,830.00 USD | 1,260.00 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 161,040.00 USD | 210.88 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,910,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,920,000.00 USD | 3,380.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,920,000.00 USD | 692.34 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,920,000.00 USD | 107.71 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,920,000.00 USD | 2,690.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,920,000.00 USD | 1,330.00 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,920,000.00 USD | 2,360.00 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,920,000.00 USD | 326.97 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,920,000.00 USD | 242.84 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,930,000.00 USD | 10,140.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 1,930,000.00 USD | 152.92 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,940,000.00 USD | 876.11 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,940,000.00 USD | 205.59 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,940,000.00 USD | 126.76 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,940,000.00 USD | 307.41 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,940,000.00 USD | 942.20 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,940,000.00 USD | 644.62 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 1,940,000.00 USD | 180.45 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,940,000.00 USD | 2,020.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,980,000.00 USD | 43,760.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0864` | 1,980,000.00 USD | 164.86 USD | 0.00 USD | `+8.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 1,980,000.00 USD | 1,080.00 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 1,990,000.00 USD | 384.06 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 1,990,000.00 USD | 1,840.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 1,990,000.00 USD | 117.71 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 1,990,000.00 USD | 111.61 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 1,990,000.00 USD | 571.18 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 1,990,000.00 USD | 375.94 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 1,990,000.00 USD | 627.55 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 1,990,000.00 USD | 211.04 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 1,990,000.00 USD | 108.36 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 1,990,000.00 USD | 543.32 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 1,990,000.00 USD | 1,820.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 1,990,000.00 USD | 2,080.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,010,000.00 USD | 17,680.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,010,000.00 USD | 1,810.00 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,010,000.00 USD | 1,640.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,020,000.00 USD | 5,340.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,020,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,020,000.00 USD | 224.86 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,040,000.00 USD | 20,540.00 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,040,000.00 USD | 114.93 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,040,000.00 USD | 840.47 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,040,000.00 USD | 173.36 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,050,000.00 USD | 4,690.00 USD | 0.00 USD | `+15.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,050,000.00 USD | 1,970.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,050,000.00 USD | 2,170.00 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,050,000.00 USD | 541.32 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,190,000.00 USD | 137,500.00 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,190,000.00 USD | 691.07 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,200,000.00 USD | 6,250.00 USD | 0.00 USD | `+16.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,210,000.00 USD | 13,480.00 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,210,000.00 USD | 734.82 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,210,000.00 USD | 1,230.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,210,000.00 USD | 184.09 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,210,000.00 USD | 1,120.00 USD | 0.00 USD | `+17.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,220,000.00 USD | 1,860.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,220,000.00 USD | 512.15 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,220,000.00 USD | 6,620.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,220,000.00 USD | 404.96 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,220,000.00 USD | 129.85 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,230,000.00 USD | 3,740.00 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,230,000.00 USD | 2,400.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,230,000.00 USD | 409.17 USD | 0.00 USD | `+20.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,230,000.00 USD | 203.74 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,230,000.00 USD | 2,800.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,230,000.00 USD | 1,320.00 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,230,000.00 USD | 694.56 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,240,000.00 USD | 940.91 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,240,000.00 USD | 2,980.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,240,000.00 USD | 104.99 USD | 0.00 USD | `+24.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,240,000.00 USD | 1,930.00 USD | 0.00 USD | `+24.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,240,000.00 USD | 1,490.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,240,000.00 USD | 1,090.00 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,240,000.00 USD | 438.96 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,240,000.00 USD | 973.76 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,360,000.00 USD | 113,580.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,360,000.00 USD | 175.59 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,360,000.00 USD | 588.78 USD | 0.00 USD | `+26.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,360,000.00 USD | 201.90 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,360,000.00 USD | 489.46 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,360,000.00 USD | 103.68 USD | 0.00 USD | `+27.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,360,000.00 USD | 203.70 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,360,000.00 USD | 3,810.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,370,000.00 USD | 11,200.00 USD | 0.00 USD | `+28.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,380,000.00 USD | 4,330.00 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,380,000.00 USD | 205.50 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,380,000.00 USD | 1,540.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,380,000.00 USD | 207.50 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,380,000.00 USD | 813.88 USD | 0.00 USD | `+30.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,410,000.00 USD | 23,160.00 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,410,000.00 USD | 781.51 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,410,000.00 USD | 209.30 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,410,000.00 USD | 1,440.00 USD | 0.00 USD | `+31.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,410,000.00 USD | 5,140.00 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,410,000.00 USD | 585.32 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,410,000.00 USD | 210.90 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,420,000.00 USD | 1,850.00 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,420,000.00 USD | 105.75 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,420,000.00 USD | 3,220.00 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,420,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,420,000.00 USD | 212.90 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,420,000.00 USD | 472.63 USD | 0.00 USD | `+34.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,420,000.00 USD | 214.50 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,420,000.00 USD | 1,040.00 USD | 0.00 USD | `+35.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,420,000.00 USD | 136.12 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,420,000.00 USD | 216.10 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,460,000.00 USD | 40,920.00 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,460,000.00 USD | 217.90 USD | 0.00 USD | `+36.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,460,000.00 USD | 219.70 USD | 0.00 USD | `+38.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,470,000.00 USD | 7,920.00 USD | 0.00 USD | `+38.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,470,000.00 USD | 154.22 USD | 0.00 USD | `+38.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,470,000.00 USD | 221.30 USD | 0.00 USD | `+39.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,470,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,500,000.00 USD | 24,440.00 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,500,000.00 USD | 223.10 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,500,000.00 USD | 2,120.00 USD | 0.00 USD | `+41.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,500,000.00 USD | 226.30 USD | 0.00 USD | `+42.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 351.57 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 950.34 USD | 0.00 USD | `+43.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,500,000.00 USD | 229.50 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,500,000.00 USD | 771.08 USD | 0.00 USD | `+44.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,500,000.00 USD | 230.90 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,500,000.00 USD | 288.18 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,500,000.00 USD | 619.10 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,500,000.00 USD | 1,250.00 USD | 0.00 USD | `+45.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,510,000.00 USD | 232.30 USD | 0.00 USD | `+45.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,510,000.00 USD | 1,600.00 USD | 0.00 USD | `+46.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,510,000.00 USD | 3,730.00 USD | 0.00 USD | `+47.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,510,000.00 USD | 676.22 USD | 0.00 USD | `+48.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,510,000.00 USD | 648.25 USD | 0.00 USD | `+48.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,520,000.00 USD | 1,510.00 USD | 0.00 USD | `+48.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,520,000.00 USD | 448.52 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,520,000.00 USD | 136.93 USD | 0.00 USD | `+48.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,520,000.00 USD | 433.07 USD | 0.00 USD | `+49.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+49.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,520,000.00 USD | 691.80 USD | 0.00 USD | `+50.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,640,000.00 USD | 118,550.00 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,640,000.00 USD | 143.22 USD | 0.00 USD | `+51.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,640,000.00 USD | 803.95 USD | 0.00 USD | `+51.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,640,000.00 USD | 1,380.00 USD | 0.00 USD | `+52.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,640,000.00 USD | 2,270.00 USD | 0.00 USD | `+53.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,640,000.00 USD | 871.99 USD | 0.00 USD | `+53.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,670,000.00 USD | 24,560.00 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,670,000.00 USD | 400.21 USD | 0.00 USD | `+59.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,680,000.00 USD | 13,850.00 USD | 0.00 USD | `+65.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,680,000.00 USD | 2,360.00 USD | 0.00 USD | `+65.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,690,000.00 USD | 4,160.00 USD | 0.00 USD | `+70.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,690,000.00 USD | 235.54 USD | 0.00 USD | `+75.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,690,000.00 USD | 1,160.00 USD | 0.00 USD | `+77.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,690,000.00 USD | 173.57 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,690,000.00 USD | 380.09 USD | 0.00 USD | `+78.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,710,000.00 USD | 17,150.00 USD | 0.00 USD | `+78.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,710,000.00 USD | 433.35 USD | 0.00 USD | `+81.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,710,000.00 USD | 3,640.00 USD | 0.00 USD | `+84.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,770,000.00 USD | 55,720.00 USD | 0.00 USD | `+85.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,770,000.00 USD | 2,120.00 USD | 0.00 USD | `+86.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,790,000.00 USD | 18,810.00 USD | 0.00 USD | `+88.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1532` | 2,790,000.00 USD | 4,750.00 USD | 0.00 USD | `+92.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1552` | 2,790,000.00 USD | 630.53 USD | 0.00 USD | `+94.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1590` | 2,800,000.00 USD | 2,670.00 USD | 0.00 USD | `+99.83%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0712` | 23,490,000.00 USD | 0.00 USD | 23,490,000.00 USD | 40,870.00 USD | 12,440.00 USD | 9,620.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 23,430,000.00 USD | 0.00 USD | 23,430,000.00 USD | 29,370.00 USD | 45,410.00 USD | 32,480.00 USD |
| `1D` | `0.0714` | 23,320,000.00 USD | 0.00 USD | 23,320,000.00 USD | 26,980.00 USD | 31,500.00 USD | 8,650.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 23,260,000.00 USD | 0.00 USD | 23,260,000.00 USD | 3,380.00 USD | 3,280.00 USD | 37,040.00 USD |
| `1D` | `0.0716` | 23,210,000.00 USD | 0.00 USD | 23,210,000.00 USD | 70,000.00 USD | 27,770.00 USD | 26,890.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 23,090,000.00 USD | 0.00 USD | 23,090,000.00 USD | 22,320.00 USD | 11,700.00 USD | 21,830.00 USD |
| `1D` | `0.0718` | 23,030,000.00 USD | 0.00 USD | 23,030,000.00 USD | 63,040.00 USD | 41,450.00 USD | 50,850.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `1D` | `0.0720` | 22,840,000.00 USD | 0.00 USD | 22,840,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 22,750,000.00 USD | 0.00 USD | 22,750,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0722` | 22,680,000.00 USD | 0.00 USD | 22,680,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,970.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 22,610,000.00 USD | 0.00 USD | 22,610,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,860.00 USD |
| `1D` | `0.0724` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,070.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 22,360,000.00 USD | 0.00 USD | 22,360,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,900.00 USD |
| `1D` | `0.0726` | 22,210,000.00 USD | 0.00 USD | 22,210,000.00 USD | 31,660.00 USD | 0.00 USD | 142.34 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 22,180,000.00 USD | 0.00 USD | 22,180,000.00 USD | 20,420.00 USD | 0.00 USD | 200.42 USD |
| `1D` | `0.0728` | 22,150,000.00 USD | 0.00 USD | 22,150,000.00 USD | 15,580.00 USD | 802.30 USD | 419.85 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 22,140,000.00 USD | 0.00 USD | 22,140,000.00 USD | 17,820.00 USD | 0.00 USD | 18,720.00 USD |
| `1D` | `0.0730` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 14,450.00 USD | 0.00 USD | 223.21 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 22,090,000.00 USD | 0.00 USD | 22,090,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD |
| `1D` | `0.0732` | 22,040,000.00 USD | 0.00 USD | 22,040,000.00 USD | 42,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0734` | 21,990,000.00 USD | 0.00 USD | 21,990,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 21,990,000.00 USD | 0.00 USD | 21,990,000.00 USD | 24,100.00 USD | 0.00 USD | 41.24 USD |
| `1D` | `0.0736` | 21,960,000.00 USD | 0.00 USD | 21,960,000.00 USD | 8,600.00 USD | 0.00 USD | 258.52 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 21,950,000.00 USD | 0.00 USD | 21,950,000.00 USD | 44,590.00 USD | 0.00 USD | 983.61 USD |
| `1D` | `0.0738` | 21,910,000.00 USD | 0.00 USD | 21,910,000.00 USD | 29,080.00 USD | 0.00 USD | 162.16 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 21,880,000.00 USD | 0.00 USD | 21,880,000.00 USD | 36,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0740` | 21,840,000.00 USD | 0.00 USD | 21,840,000.00 USD | 30,160.00 USD | 0.00 USD | 267.65 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 21,810,000.00 USD | 0.00 USD | 21,810,000.00 USD | 44,630.00 USD | 0.00 USD | 1,940.00 USD |
| `1D` | `0.0742` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 38,470.00 USD | 0.00 USD | 145.18 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 37,380.00 USD | 27,500.00 USD | 162.32 USD |
| `1D` | `0.0744` | 21,660,000.00 USD | 0.00 USD | 21,660,000.00 USD | 42,800.00 USD | 1,840.00 USD | 15,430.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 106,370.00 USD | 57,220.00 USD | 24,990.00 USD |
| `1D` | `0.0746` | 21,410,000.00 USD | 0.00 USD | 21,410,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,570.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,440.00 USD |
| `1D` | `0.0748` | 20,410,000.00 USD | 0.00 USD | 20,410,000.00 USD | 169,810.00 USD | 65,720.00 USD | 98,750.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 20,080,000.00 USD | 0.00 USD | 20,080,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,040.00 USD |
| `1D` | `0.0750` | 19,730,000.00 USD | 0.00 USD | 19,730,000.00 USD | 233,830.00 USD | 83,730.00 USD | 121,130.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 19,290,000.00 USD | 0.00 USD | 19,290,000.00 USD | 259,690.00 USD | 82,120.00 USD | 66,160.00 USD |
| `1D` | `0.0752` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 123,390.00 USD | 19,450.00 USD | 85,710.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 18,660,000.00 USD | 0.00 USD | 18,660,000.00 USD | 128,550.00 USD | 72,710.00 USD | 28,530.00 USD |
| `1D` | `0.0754` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 104,420.00 USD | 62,330.00 USD | 21,040.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 18,240,000.00 USD | 0.00 USD | 18,240,000.00 USD | 126,690.00 USD | 15,650.00 USD | 68,560.00 USD |
| `1D` | `0.0756` | 18,030,000.00 USD | 0.00 USD | 18,030,000.00 USD | 177,070.00 USD | 147,310.00 USD | 111,780.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 17,590,000.00 USD | 0.00 USD | 17,590,000.00 USD | 91,080.00 USD | 44,210.00 USD | 104,970.00 USD |
| `1D` | `0.0758` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 75,340.00 USD | 42,570.00 USD | 31,950.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 102,240.00 USD | 72,180.00 USD | 8,670.00 USD |
| `1D` | `0.0760` | 17,020,000.00 USD | 0.00 USD | 17,020,000.00 USD | 233,950.00 USD | 259,920.00 USD | 202,560.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 16,320,000.00 USD | 0.00 USD | 16,320,000.00 USD | 484,940.00 USD | 429,570.00 USD | 272,010.00 USD |
| `1D` | `0.0762` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 532,440.00 USD | 268,260.00 USD | 238,180.00 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 14,100,000.00 USD | 0.00 USD | 14,100,000.00 USD | 364,700.00 USD | 140,370.00 USD | 197,140.00 USD |
| `1D` | `0.0764` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 435,810.00 USD | 376,250.00 USD | 90,870.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 553,690.00 USD | 223,110.00 USD | 314,140.00 USD |
| `1D` | `0.0766` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 621,080.00 USD | 274,850.00 USD | 280,330.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,850.00 USD |
| `1D` | `0.0768` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 426,850.00 USD | 236,860.00 USD | 142,100.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,010.00 USD |
| `1D` | `0.0770` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,410.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 231,550.00 USD | 266,030.00 USD | 190,250.00 USD |
| `1D` | `0.0772` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 169,730.00 USD | 297,590.00 USD | 333,150.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 272,980.00 USD | 149,960.00 USD | 241,270.00 USD |
| `1D` | `0.0774` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 165,350.00 USD | 97,350.00 USD | 108,170.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 181,290.00 USD | 12,820.00 USD | 17,130.00 USD |
| `1D` | `0.0776` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 106,410.00 USD | 237,880.00 USD | 232,080.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 48,260.00 USD | 159,490.00 USD | 146.30 USD |
| `1D` | `0.0778` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 36,200.00 USD | 40,050.00 USD | 187,050.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 4,990.00 USD | 253.82 USD |
| `1D` | `0.0780` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 217,760.00 USD | 88,770.00 USD | 0.00 USD |
| `1D` | `0.0781` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD |
| `1D` | `0.0782` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 44,780.00 USD | 75,640.00 USD | 85,130.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD |
| `1D` | `0.0784` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD |
| `1D` | `0.0788` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 879,870.00 USD | 0.00 USD | 879,870.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD |
| `1D` | `0.0790` | 649,820.00 USD | 0.00 USD | 649,820.00 USD | 200,610.00 USD | 137,240.00 USD | 50,580.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 261,400.00 USD | 0.00 USD | 261,400.00 USD | 76,010.00 USD | 3,690.00 USD | 30,030.00 USD |
| `1D` | `0.0792` | 151,670.00 USD | 0.00 USD | 151,670.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 120,700.00 USD | 0.00 USD | 120,700.00 USD | 0.00 USD | 120,700.00 USD | 0.00 USD |
| `1D` | `0.0796` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |
| `1D` | `0.0796` | 32,520.00 USD | 32,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 430,800.00 USD | 430,800.00 USD | 0.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 585,480.00 USD | 585,480.00 USD | 0.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 928,500.00 USD | 928,500.00 USD | 0.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD |
| `1D` | `0.0800` | 934,100.00 USD | 934,100.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `1D` | `0.0804` | 945,010.00 USD | 945,010.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 948,530.00 USD | 948,530.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 70,050.00 USD | 40,790.00 USD |
| `1D` | `0.0808` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 403,310.00 USD | 23,520.00 USD | 372,960.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 419,190.00 USD | 269,160.00 USD | 0.00 USD |
| `1D` | `0.0810` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 180,570.00 USD | 100,400.00 USD | 118,770.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 162,830.00 USD | 0.00 USD |
| `1D` | `0.0812` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 93,910.00 USD | 78,610.00 USD | 269,820.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 27,080.00 USD | 18,240.00 USD | 209,180.00 USD |
| `1D` | `0.0814` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 22,430.00 USD | 18,210.00 USD | 386,300.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD |
| `1D` | `0.0816` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 441,880.00 USD | 245,220.00 USD | 189,500.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 361,650.00 USD | 152,470.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 298,910.00 USD | 161,880.00 USD | 321,810.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 171,350.00 USD | 368,950.00 USD | 156,890.00 USD |
| `1D` | `0.0820` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 215,860.00 USD | 275,570.00 USD | 499,340.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 383,530.00 USD | 167,310.00 USD | 171,040.00 USD |
| `1D` | `0.0822` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 265,050.00 USD | 195,320.00 USD | 127,580.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 171,080.00 USD | 17,180.00 USD | 8,520.00 USD |
| `1D` | `0.0824` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 145,660.00 USD | 172,750.00 USD | 123,910.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 109,230.00 USD | 82,760.00 USD | 21,620.00 USD |
| `1D` | `0.0826` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 55,700.00 USD | 25,070.00 USD | 204,980.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 112,370.00 USD | 8,940.00 USD | 55.02 USD |
| `1D` | `0.0828` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 303,590.00 USD | 86,340.00 USD | 75,070.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 262,740.00 USD | 88,990.00 USD | 72,740.00 USD |
| `1D` | `0.0830` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 257,210.00 USD | 110,610.00 USD | 152,140.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 102,690.00 USD | 64,510.00 USD | 42,470.00 USD |
| `1D` | `0.0832` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 238,910.00 USD | 91,440.00 USD | 86,220.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 155,140.00 USD | 68,410.00 USD | 31,430.00 USD |
| `1D` | `0.0834` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 163,970.00 USD | 60,550.00 USD | 135,070.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 127,340.00 USD | 184,470.00 USD | 78,760.00 USD |
| `1D` | `0.0836` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 83,690.00 USD | 84,520.00 USD | 221,700.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 191,180.00 USD | 61,550.00 USD | 34,400.00 USD |
| `1D` | `0.0838` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 145,530.00 USD | 76,380.00 USD | 48,790.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 67,620.00 USD | 0.00 USD | 639.31 USD |
| `1D` | `0.0840` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 35,250.00 USD | 15,480.00 USD | 584.63 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 32,120.00 USD | 2,010.00 USD | 709.20 USD |
| `1D` | `0.0842` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 30,040.00 USD | 0.00 USD | 47,110.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 33,670.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.0844` | 15,690,000.00 USD | 15,690,000.00 USD | 0.00 USD | 78,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 19,870.00 USD | 0.00 USD | 320.28 USD |
| `1D` | `0.0846` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 68,750.00 USD | 16,670.00 USD | 75.71 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 25,550.00 USD | 0.00 USD | 1,670.00 USD |
| `1D` | `0.0848` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 24,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0849` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 15,210.00 USD | 0.00 USD | 292.60 USD |
| `1D` | `0.0850` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 22,320.00 USD | 0.00 USD | 413.16 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0851` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 26,040.00 USD | 11,000.00 USD | 750.73 USD |
| `1D` | `0.0852` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.58 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0853` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 12,910.00 USD | 737.47 USD | 212.49 USD |
| `1D` | `0.0854` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 35,960.00 USD | 13,190.00 USD | 10,120.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0855` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD |
| `1D` | `0.0856` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 92,490.00 USD | 32,810.00 USD | 19,870.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0857` | 16,390,000.00 USD | 16,390,000.00 USD | 0.00 USD | 50,540.00 USD | 18,030.00 USD | 27,880.00 USD |
| `1D` | `0.0858` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 48,130.00 USD | 36,780.00 USD | 164.89 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0859` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 72,260.00 USD | 20,870.00 USD | 40,140.00 USD |
| `1D` | `0.0860` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 44,920.00 USD | 22,170.00 USD | 20,180.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0861` | 16,740,000.00 USD | 16,740,000.00 USD | 0.00 USD | 20,430.00 USD | 0.00 USD | 32,450.00 USD |
| `1D` | `0.0862` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0863` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 219.34 USD |
| `1D` | `0.0864` | 16,870,000.00 USD | 16,870,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,150.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0865` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 31,770.00 USD | 1,280.00 USD | 18,020.00 USD |
| `1D` | `0.0866` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 25,410.00 USD | 16,310.00 USD | 19,340.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `1D` | `0.0867` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 24,580.00 USD | 37,120.00 USD | 14,130.00 USD |
| `1D` | `0.0868` | 17,110,000.00 USD | 17,110,000.00 USD | 0.00 USD | 8,080.00 USD | 9,300.00 USD | 34,750.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `1D` | `0.0869` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 12,960.00 USD | 8,560.00 USD | 9,620.00 USD |
| `1D` | `0.0870` | 17,170,000.00 USD | 17,170,000.00 USD | 0.00 USD | 27,920.00 USD | 1,130.00 USD | 0.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0871` | 17,270,000.00 USD | 17,270,000.00 USD | 0.00 USD | 29,370.00 USD | 45,410.00 USD | 32,480.00 USD |
| `1D` | `0.0872` | 17,340,000.00 USD | 17,340,000.00 USD | 0.00 USD | 26,980.00 USD | 31,500.00 USD | 8,650.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `1D` | `0.0873` | 17,390,000.00 USD | 17,390,000.00 USD | 0.00 USD | 3,380.00 USD | 3,280.00 USD | 37,040.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0875` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 26,740.00 USD | 997.45 USD | 0.00 USD |
| `1D` | `0.0876` | 17,510,000.00 USD | 17,510,000.00 USD | 0.00 USD | 43,260.00 USD | 26,770.00 USD | 26,890.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0877` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 22,320.00 USD | 11,700.00 USD | 21,830.00 USD |
| `1D` | `0.0878` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 63,040.00 USD | 41,450.00 USD | 50,850.00 USD |
| `7D` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `1D` | `0.0879` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `1D` | `0.0880` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 0.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD |
| `1D` | `0.0881` | 17,910,000.00 USD | 17,910,000.00 USD | 0.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0882` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 25,340.00 USD | 15,630.00 USD | 27,970.00 USD |
| `7D` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 0.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD |
| `1D` | `0.0883` | 18,090,000.00 USD | 18,090,000.00 USD | 0.00 USD | 26,840.00 USD | 73,610.00 USD | 7,860.00 USD |
| `1D` | `0.0884` | 18,200,000.00 USD | 18,200,000.00 USD | 0.00 USD | 8,850.00 USD | 17,780.00 USD | 83,950.00 USD |
| `7D` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 0.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD |
| `1D` | `0.0886` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 48,870.00 USD | 18,070.00 USD | 13,500.00 USD |
| `7D` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 0.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD |
| `1D` | `0.0887` | 18,350,000.00 USD | 18,350,000.00 USD | 0.00 USD | 22,710.00 USD | 22,450.00 USD | 19,280.00 USD |
| `1D` | `0.0888` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 16,050.00 USD | 0.00 USD | 142.34 USD |
| `7D` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0889` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0890` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 802.30 USD | 0.00 USD |
| `7D` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD |
| `1D` | `0.0891` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 2,580.00 USD | 0.00 USD | 18,610.00 USD |
| `1D` | `0.0892` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101.53 USD |
| `7D` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD |
| `1D` | `0.0893` | 18,410,000.00 USD | 18,410,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0894` | 18,440,000.00 USD | 18,440,000.00 USD | 0.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `14,061,730,631.4 DOGE`
  * 1h OI Change: `-0.59%` | 4h OI Change: `-0.08%` | 24h OI Change: `-1.85%`
  * Exchange Breakdown: Binance=`271.12M` | Bybit=`111.69M` | OKX=`115.18M` | Hyperliquid=`80.42M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `44.03K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0096%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `53.31%` | `46.69%` | `1.14` | 16,170,000.00 USD |
| `15M` | `Binance` | `48.11%` | `51.89%` | `0.93` | 5,840,000.00 USD |
| `15M` | `OKX` | `56.7%` | `43.3%` | `1.31` | 3,160,000.00 USD |
| `15M` | `Bybit` | `75.14%` | `24.86%` | `3.02` | 1,470,000.00 USD |
| `15M` | `KuCoin` | `60.9%` | `39.1%` | `1.56` | 41,230.00 USD |
| `15M` | `Gate` | `50.5%` | `49.5%` | `1.02` | 2,950,000.00 USD |
| `15M` | `Bitget` | `43.45%` | `56.55%` | `0.77` | 169,010.00 USD |
| `15M` | `BingX` | `46.44%` | `53.56%` | `0.87` | 444,640.00 USD |
| `15M` | `MEXC` | `63%` | `37%` | `1.70` | 888,990.00 USD |
| `15M` | `Bitunix` | `52.39%` | `47.61%` | `1.10` | 449,880.00 USD |
| `15M` | `Hyperliquid` | `59.37%` | `40.63%` | `1.46` | 87,660.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `58.13%` | `41.87%` | `1.39` | 95,760.00 USD |
| `15M` | `Crypto.com` | `51.63%` | `48.37%` | `1.07` | 21,870.00 USD |
| `15M` | `WhiteBIT` | `38.16%` | `61.84%` | `0.62` | 370,110.00 USD |
| `15M` | `HTX` | `88.32%` | `11.68%` | `7.56` | 21,980.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `45.53%` | `54.47%` | `0.84` | 61,530.00 USD |
| `15M` | `Aster` | `20.92%` | `79.08%` | `0.26` | 107,920.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `25.75%` | `74.25%` | `0.35` | 1,990.00 USD |
| `15M` | `Whale Positions` | `48.11%` | `51.89%` | `0.93` | 5,840,000.00 USD |
| `15M` | `Global Accounts` | `53.31%` | `46.69%` | `1.14` | 16,170,000.00 USD |
| `1H` | `DOGE` | `47.44%` | `52.56%` | `0.90` | 69,030,000.00 USD |
| `1H` | `Binance` | `45.31%` | `54.69%` | `0.83` | 23,330,000.00 USD |
| `1H` | `OKX` | `52.91%` | `47.09%` | `1.12` | 16,330,000.00 USD |
| `1H` | `Bybit` | `52.64%` | `47.36%` | `1.11` | 5,350,000.00 USD |
| `1H` | `KuCoin` | `53.75%` | `46.25%` | `1.16` | 249,240.00 USD |
| `1H` | `Gate` | `48.28%` | `51.72%` | `0.93` | 10,050,000.00 USD |
| `1H` | `Bitget` | `43.07%` | `56.93%` | `0.76` | 1,100,000.00 USD |
| `1H` | `BingX` | `42.79%` | `57.21%` | `0.75` | 2,120,000.00 USD |
| `1H` | `MEXC` | `44.11%` | `55.89%` | `0.79` | 5,550,000.00 USD |
| `1H` | `Bitunix` | `46.94%` | `53.06%` | `0.88` | 1,940,000.00 USD |
| `1H` | `Hyperliquid` | `41.35%` | `58.65%` | `0.71` | 286,600.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.61%` | `47.39%` | `1.11` | 370,190.00 USD |
| `1H` | `Crypto.com` | `47.68%` | `52.32%` | `0.91` | 83,750.00 USD |
| `1H` | `WhiteBIT` | `21.77%` | `78.23%` | `0.28` | 1,410,000.00 USD |
| `1H` | `HTX` | `33.96%` | `66.04%` | `0.51` | 135,960.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.14%` | `55.86%` | `0.79` | 234,570.00 USD |
| `1H` | `Aster` | `38.81%` | `61.19%` | `0.63` | 476,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `11.23%` | `88.77%` | `0.13` | 22,090.00 USD |
| `1H` | `Whale Positions` | `45.31%` | `54.69%` | `0.83` | 23,330,000.00 USD |
| `1H` | `Global Accounts` | `47.44%` | `52.56%` | `0.90` | 69,030,000.00 USD |
| `4H` | `DOGE` | `49.61%` | `50.39%` | `0.98` | 212,340,000.00 USD |
| `4H` | `Binance` | `49.79%` | `50.21%` | `0.99` | 137,490,000.00 USD |
| `4H` | `OKX` | `50.48%` | `49.52%` | `1.02` | 12,740,000.00 USD |
| `4H` | `Bybit` | `52.02%` | `47.98%` | `1.08` | 6,470,000.00 USD |
| `4H` | `KuCoin` | `54.4%` | `45.6%` | `1.19` | 1,200,000.00 USD |
| `4H` | `Gate` | `50.82%` | `49.18%` | `1.03` | 19,320,000.00 USD |
| `4H` | `Bitget` | `45.55%` | `54.45%` | `0.84` | 4,000,000.00 USD |
| `4H` | `BingX` | `33.2%` | `66.8%` | `0.50` | 7,780,000.00 USD |
| `4H` | `MEXC` | `48.7%` | `51.3%` | `0.95` | 3,410,000.00 USD |
| `4H` | `Bitunix` | `50.11%` | `49.89%` | `1.00` | 6,040,000.00 USD |
| `4H` | `Hyperliquid` | `54.95%` | `45.05%` | `1.22` | 1,540,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.95%` | `47.05%` | `1.13` | 5,860,000.00 USD |
| `4H` | `Crypto.com` | `50.44%` | `49.56%` | `1.02` | 0.00 USD |
| `4H` | `WhiteBIT` | `47.8%` | `52.2%` | `0.92` | 906,670.00 USD |
| `4H` | `HTX` | `49.31%` | `50.69%` | `0.97` | 871,730.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.98%` | `54.02%` | `0.85` | 291,170.00 USD |
| `4H` | `Aster` | `47.1%` | `52.9%` | `0.89` | 1,850,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `20.8%` | `79.2%` | `0.26` | 2,580,000.00 USD |
| `4H` | `Whale Positions` | `49.79%` | `50.21%` | `0.99` | 137,490,000.00 USD |
| `4H` | `Global Accounts` | `49.61%` | `50.39%` | `0.98` | 212,340,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0804` | `0.0805` | `0.0804` | `0.0807` | `0.0802` | 7,554,604.29 USD | 4,072,091.15 USD | 3,482,513.14 USD | 589,578.01 USD | `+7.80%` | `10B / 4S` |
| `0:00 UTC` | `0.0808` | `0.0809` | `0.0808` | `0.0815` | `0.0804` | 18,574,379.74 USD | 9,613,153.94 USD | 8,961,225.80 USD | 651,928.14 USD | `+3.51%` | `14B / 9S` |
| `5:00 UTC` | `0.0807` | `0.0805` | `0.0807` | `0.0809` | `0.0802` | 9,552,151.73 USD | 4,610,293.53 USD | 4,941,858.20 USD | -331,564.68 USD | `-3.47%` | `6B / 12S` |
| `0:00 UTC` | `0.0801` | `0.0801` | `0.0801` | `0.0804` | `0.0799` | 7,702,082.98 USD | 2,993,499.68 USD | 4,708,583.30 USD | -1,715,083.61 USD | `-22.27%` | `2B / 6S` |
| `5:00 UTC` | `0.0802` | `0.0801` | `0.0802` | `0.0802` | `0.0799` | 3,513,799.11 USD | 1,857,314.90 USD | 1,656,484.22 USD | 200,830.68 USD | `+5.72%` | `2B / 5S` |
| `0:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0802` | `0.0799` | 4,173,492.18 USD | 1,857,641.00 USD | 2,315,851.18 USD | -458,210.19 USD | `-10.98%` | `2B / 1S` |
| `5:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0801` | `0.0799` | 3,085,332.02 USD | 1,558,385.55 USD | 1,526,946.46 USD | 31,439.09 USD | `+1.02%` | `2B / 2S` |
| `0:00 UTC` | `0.0796` | `0.0798` | `0.0796` | `0.0802` | `0.0795` | 5,871,793.04 USD | 2,200,842.18 USD | 3,670,950.86 USD | -1,470,108.68 USD | `-25.04%` | `4B / 23S` |
| `5:00 UTC` | `0.0793` | `0.0794` | `0.0793` | `0.0796` | `0.0792` | 7,734,342.64 USD | 3,622,970.91 USD | 4,111,371.72 USD | -488,400.81 USD | `-6.31%` | `4B / 4S` |
| `0:00 UTC` | `0.0796` | `0.0796` | `0.0796` | `0.0796` | `0.0795` | 885,259.69 USD | 385,739.87 USD | 499,519.82 USD | -113,779.95 USD | `-12.85%` | `2B / 4S` |

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
| `5m` | -64,970.00 USD | 349,780.00 USD | **`ACCUMULATION`** |
| `15m` | -116,690.00 USD | 916,310.00 USD | **`ACCUMULATION`** |
| `30m` | -844,040.00 USD | -1,100,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,230,000.00 USD | -1,330,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,850,000.00 USD | -6,290,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,110,000.00 USD | 930,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 710,820.00 USD | 3,420,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,460,000.00 USD | -2,880,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 335,770.00 USD | -6,540,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,250,000.00 USD | -11,100,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -40,790,000.00 USD | -123,420,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -267,390,000.00 USD | -749,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-64.97K` | 15m=`-116.69K` | 1h=`-1.23M` | 24h=`-2.25M`
* Futures Capital Netflows: 5m=`+349.78K` | 15m=`+916.31K` | 1h=`-1.33M` | 24h=`-11.10M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0787` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0823` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0682`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0802`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
