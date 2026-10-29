# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-29 23:07:12 IST` (`2026-10-29 17:37:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0789` | **Live Ask Quote**: `0.0810` | **Mid Price**: `0.0799`
- **Spread Points**: `21.00` | **Spread BPS**: `262.66 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0777` | VWAP Z-Score: `+1.29` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000430` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `57.53` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0805` | Lower -3.00σ Band: `0.0749`
  * Upper +2.51σ Band: `0.0800` | Lower -2.51σ Band: `0.0754`
  * Upper +2.01σ Band: `0.0796` | Lower -2.01σ Band: `0.0758`
  * Upper +2.00σ Band: `0.0796` | Lower -2.00σ Band: `0.0759`
  * Upper +1.28σ Band: `0.0789` | Lower -1.28σ Band: `0.0765`
  * Upper +1.00σ Band: `0.0786` | Lower -1.00σ Band: `0.0768`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0790` | EMA-20=`0.0786` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0781` (Slope: `+0.0000`) | EMA-100=`0.0779`
  * Institutional Anchors: EMA-144=`0.0778` | EMA-200=`0.0776` (Slope: `+0.2371`) | EMA-233=`0.0775`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0763` | Weekly High=`0.0803` | Weekly Low=`0.0755`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0787` (Distance: `+1.64%`)
  * Point of Control (POC) = `0.0767` (Distance: `+4.26%`)
  * Value Area Low (VAL) = `0.0764` (Distance: `+4.66%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.0796` - `0.0803`
  * Optimal Trade Entry (OTE 0.705): `0.0801`
  * Structural Invalidation Anchor (0.786): `0.0806`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0800` | `0.0801` | `0.0799` | `0.0799` | `16,346,143` | 1,308,727.66 USD | -239,448.74 USD | `-18.30%` | -5,440,335.40 USD | `-0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0799` | `0.0801` | `0.0799` | `0.0800` | `15,138,929` | 1,210,864.33 USD | 150,912.79 USD | `+12.46%` | -5,289,422.61 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.0800` | `0.0801` | `0.0799` | `0.0800` | `12,556,875` | 1,005,307.70 USD | -70,187.20 USD | `-6.98%` | -5,359,609.82 USD | `-0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0802` | `0.0802` | `0.0799` | `0.0801` | `43,881,208` | 3,513,799.11 USD | 200,830.68 USD | `+5.72%` | -4,986,543.54 USD | `+0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0801` | `0.0802` | `0.0799` | `0.0799` | `52,144,598` | 4,173,492.18 USD | -458,210.19 USD | `-10.98%` | -5,444,753.73 USD | `-0.86` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0799` | `0.0801` | `0.0799` | `0.0800` | `27,695,804` | 2,216,172.03 USD | 80,725.59 USD | `+3.64%` | -5,364,028.14 USD | `-0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0799` | `0.0807` | `0.0797` | `0.0806` | `308,847,265` | 24,764,184.89 USD | 1,508,150.52 USD | `+6.09%` | -4,845,295.11 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0806` | `0.0815` | `0.0799` | `0.0801` | `488,172,743` | 39,342,413.57 USD | -1,193,889.47 USD | `-3.03%` | -6,039,184.58 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0801` | `0.0802` | `0.0799` | `0.0800` | `79,840,090` | 6,389,639.25 USD | -377,459.64 USD | `-5.91%` | -6,416,644.22 USD | `+0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0799` | `0.0800` | `568,013,145` | 45,732,077.78 USD | -1,571,374.07 USD | `-3.44%` | -7,425,830.41 USD | `-0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0797` | `0.0799` | `0.0774` | `0.0778` | `998,970,852` | 78,232,937.14 USD | -7,024,064.25 USD | `-8.98%` | -3,060,763.89 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -7,420,203.26 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0799` | `0.0800` | `568,013,145` | 45,732,077.78 USD | -1,571,374.07 USD | `-3.44%` | -7,425,830.41 USD | `-0.08` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.0799`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0799` | `145925.0000` | 11,666.41 USD | 136,156.96 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0799` | `11319.0000` | 904.92 USD | 137,061.88 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0799` | `11320.0000` | 904.99 USD | 137,966.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0799` | `2167.0000` | 173.24 USD | 138,140.11 USD | `2 orders` | `-0.03%` | `-` |
| `ASK` | `0.0800` | `96932.0000` | 7,756.69 USD | 146,923.29 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `18744.0000` | 1,499.91 USD | 139,166.59 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `53881.0000` | 4,311.56 USD | 137,666.68 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `18744.0000` | 1,499.88 USD | 133,355.12 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `253038.0000` | 20,247.59 USD | 131,855.25 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `321825.0000` | 25,751.47 USD | 111,607.65 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `128129.0000` | 10,252.37 USD | 85,856.18 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `0.0800` | `533079.0000` | 42,654.32 USD | 75,603.81 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.0800` | `42038.0000` | 3,363.63 USD | 32,949.49 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0800` | `130532.0000` | 10,444.00 USD | 29,585.87 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0800` | `16319.0000` | 1,305.68 USD | 19,141.87 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.0800` | `41612.0000` | 3,329.33 USD | 17,836.19 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0800` | `11320.0000` | 905.69 USD | 14,506.85 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0800` | `5000.0000` | 400.03 USD | 13,601.16 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0800` | `116938.0000` | 9,355.39 USD | 13,201.13 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0800` | `11320.0000` | 905.62 USD | 3,845.74 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0800` | `21808.0000` | 1,744.66 USD | 2,940.11 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0800` | `11320.0000` | 905.55 USD | 1,195.45 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0800` | `3369.0000` | 269.50 USD | 289.90 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0800` | `255.0000` | 20.39 USD | 20.39 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0800` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0800` | `435149.0000` | 34,799.30 USD | 34,799.30 USD | `16 orders` | `-0.00%` | `-` |
| `BID` | `0.0800` | `100800.0000` | 8,060.98 USD | 42,860.28 USD | `9 orders` | `-0.00%` | `-` |
| `BID` | `0.0800` | `142265.0000` | 11,376.79 USD | 54,237.07 USD | `10 orders` | `-0.00%` | `-` |
| `BID` | `0.0800` | `100800.0000` | 8,060.77 USD | 62,297.84 USD | `9 orders` | `-0.00%` | `-` |
| `BID` | `0.0800` | `22400.0000` | 1,791.26 USD | 64,089.10 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0800` | `26121.0000` | 2,088.79 USD | 66,177.89 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0800` | `8490.0000` | 678.90 USD | 66,856.80 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0800` | `47961.0000` | 3,835.11 USD | 70,691.90 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `0.0800` | `116721.0000` | 9,333.01 USD | 80,024.91 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0800` | `13493.0000` | 1,078.89 USD | 81,103.80 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0800` | `47471.0000` | 3,795.64 USD | 84,899.44 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0800` | `3125.0000` | 249.86 USD | 85,149.30 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0800` | `131811.0000` | 10,538.95 USD | 95,688.25 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0800` | `184147.0000` | 14,723.11 USD | 110,411.35 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `0.0800` | `142219.0000` | 11,370.69 USD | 121,782.05 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0800` | `33877.0000` | 2,708.50 USD | 124,490.55 USD | `1 orders` | `-0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `303` | `0xb83d...6e36` | `SHORT` | 8,210,544.89 USD | `102,645,925.00` | `0.0946` | `0.0800` | `1.26` | 1,496,796.76 USD | `+18.23%` | `3X Cross` |
| `312` | `0xc63a...a3cd` | `LONG` | 7,998,400.00 USD | `100,000,000.00` | `0.0856` | `0.0800` | `0.000000` | -566,421.96 USD | `-7.08%` | `10X Cross` |
| `319` | `0x610b...b613` | `LONG` | 7,890,748.59 USD | `98,666,424.00` | `0.0872` | `0.0800` | `0.0576` | -709,433.31 USD | `-8.99%` | `5X Cross` |
| `603` | `0x5b5d...c060` | `SHORT` | 3,958,069.01 USD | `49,478,955.00` | `0.0946` | `0.0800` | `3.01` | 723,447.60 USD | `+18.28%` | `3X Cross` |
| `637` | `0xca49...53c8` | `SHORT` | 3,722,294.90 USD | `46,542,649.00` | `0.0929` | `0.0800` | `0.3415` | 603,749.78 USD | `+16.22%` | `10X Cross` |
| `652` | `0x45d2...4029` | `SHORT` | 3,632,626.37 USD | `45,426,000.00` | `0.0954` | `0.0800` | `0.8252` | 703,002.85 USD | `+19.35%` | `10X Cross` |
| `792` | `0xecb6...2b00` | `SHORT` | 3,005,683.49 USD | `37,573,392.00` | `0.0796` | `0.0800` | `0.8783` | -15,250.59 USD | `-0.51%` | `10X Cross` |
| `1184` | `0x458d...ab3b` | `LONG` | 1,955,909.32 USD | `24,454,063.00` | `0.1002` | `0.0800` | `0.0714` | -495,012.58 USD | `-25.31%` | `3X Isolated` |
| `1189` | `0xeadc...9d55` | `LONG` | 1,945,249.30 USD | `24,317,440.00` | `0.0926` | `0.0800` | `0.000000` | -306,345.28 USD | `-15.75%` | `10X Cross` |
| `1236` | `0x9aa5...58af` | `SHORT` | 1,879,922.50 USD | `23,500,500.00` | `0.0907` | `0.0800` | `0.3804` | 250,832.46 USD | `+13.34%` | `10X Cross` |
| `1337` | `0xf48f...10fe` | `LONG` | 1,713,724.09 USD | `21,424,497.00` | `0.0968` | `0.0800` | `0.0300` | -360,580.52 USD | `-21.04%` | `4X Cross` |
| `1369` | `0x9946...0852` | `SHORT` | 1,672,707.37 USD | `20,910,149.00` | `0.0871` | `0.0800` | `0.1256` | 147,848.02 USD | `+8.84%` | `10X Cross` |
| `1566` | `0xcac1...26b3` | `SHORT` | 1,450,056.17 USD | `18,126,835.00` | `0.0943` | `0.0800` | `0.4919` | 259,403.03 USD | `+17.89%` | `10X Cross` |
| `1612` | `0x0d6a...ca57` | `LONG` | 1,409,922.51 USD | `17,626,455.00` | `0.0875` | `0.0800` | `0.0626` | -132,182.45 USD | `-9.38%` | `3X Isolated` |
| `1660` | `0x4808...a82c` | `LONG` | 1,346,167.30 USD | `16,828,143.00` | `0.0883` | `0.0800` | `0.0631` | -140,305.68 USD | `-10.42%` | `3X Cross` |
| `1783` | `0x31ef...f715` | `LONG` | 1,218,149.25 USD | `15,230,102.00` | `0.0936` | `0.0800` | `0.0668` | -207,546.68 USD | `-17.04%` | `3X Isolated` |
| `1809` | `0xbfc7...80b4` | `SHORT` | 1,201,524.90 USD | `15,020,000.00` | `0.0920` | `0.0800` | `0.3540` | 180,874.39 USD | `+15.05%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 9,558.66 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0786 USD [API] | `2026-10-27 22:43:16` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0821` (Vol: 381,400.00 USD, Dist: `+2.62%`) | Long MP=`0.0767` (Vol: 519,500.00 USD, Dist: `--4.20%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 478,200.00 USD, Dist: `+2.62%`) | Long MP=`0.0774` (Vol: 691,800.00 USD, Dist: `--3.33%`)
  * 3D Horizon: Short MP=`0.0823` (Vol: 539,400.00 USD, Dist: `+2.82%`) | Long MP=`0.0760` (Vol: 680,000.00 USD, Dist: `--5.01%`)
  * 7D Horizon: Short MP=`0.0821` (Vol: 746,800.00 USD, Dist: `+2.63%`) | Long MP=`0.0762` (Vol: 928,700.00 USD, Dist: `--4.78%`)
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
| `7D` | `Long Liquidation` | `0.0696` | 68,920,000.00 USD | 68,920,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 4,800.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0698` | 68,060,000.00 USD | 68,060,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,250.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0700` | 67,550,000.00 USD | 67,550,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0702` | 66,920,000.00 USD | 66,920,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 791.79 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0704` | 66,560,000.00 USD | 66,560,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 2,510.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0706` | 93,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0706` | 66,290,000.00 USD | 66,290,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0708` | 66,000,000.00 USD | 66,000,000.00 USD | 156,500.00 USD | 34,470.00 USD | 107,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 65,700,000.00 USD | 65,700,000.00 USD | 229,480.00 USD | 157,140.00 USD | 84,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 65,230,000.00 USD | 65,230,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0714` | 64,730,000.00 USD | 64,730,000.00 USD | 236,020.00 USD | 144,580.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 757,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 755,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0716` | 64,230,000.00 USD | 64,230,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 560.88 USD | 747,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 24,840,000.00 USD | 24,840,000.00 USD | 80,570.00 USD | 27,450.00 USD | 48,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 746,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 24,680,000.00 USD | 24,680,000.00 USD | 63,040.00 USD | 40,570.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 63,800,000.00 USD | 63,800,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 744,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 24,530,000.00 USD | 24,530,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 734,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 24,490,000.00 USD | 24,490,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 63,440,000.00 USD | 63,440,000.00 USD | 277,980.00 USD | 181,150.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 733,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 24,400,000.00 USD | 24,400,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0722` | 24,330,000.00 USD | 24,330,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 62,870,000.00 USD | 62,870,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 10,450.00 USD | 709,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 24,260,000.00 USD | 24,260,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 163.73 USD | 699,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 24,150,000.00 USD | 24,150,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 62,490,000.00 USD | 62,490,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 598.51 USD | 698,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 24,010,000.00 USD | 24,010,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 698,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 23,860,000.00 USD | 23,860,000.00 USD | 31,660.00 USD | 0.00 USD | 142.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 62,000,000.00 USD | 62,000,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 697,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 23,820,000.00 USD | 23,820,000.00 USD | 20,420.00 USD | 0.00 USD | 200.42 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 452.21 USD | 697,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 23,800,000.00 USD | 23,800,000.00 USD | 15,580.00 USD | 802.30 USD | 419.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 61,510,000.00 USD | 61,510,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 1,230.00 USD | 696,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 23,790,000.00 USD | 23,790,000.00 USD | 17,820.00 USD | 0.00 USD | 18,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 23,750,000.00 USD | 23,750,000.00 USD | 14,450.00 USD | 0.00 USD | 223.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 61,080,000.00 USD | 61,080,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 622,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 23,740,000.00 USD | 23,740,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 612,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 23,690,000.00 USD | 23,690,000.00 USD | 42,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 60,760,000.00 USD | 60,760,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 610,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 23,650,000.00 USD | 23,650,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 23,640,000.00 USD | 23,640,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 59,200,000.00 USD | 59,200,000.00 USD | 646,280.00 USD | 190,810.00 USD | 59,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 604,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 23,640,000.00 USD | 23,640,000.00 USD | 24,100.00 USD | 0.00 USD | 41.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 597,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 23,610,000.00 USD | 23,610,000.00 USD | 9,980.00 USD | 0.00 USD | 258.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 58,310,000.00 USD | 58,310,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 593,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 23,600,000.00 USD | 23,600,000.00 USD | 47,420.00 USD | 0.00 USD | 983.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 588,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 23,550,000.00 USD | 23,550,000.00 USD | 39,420.00 USD | 0.00 USD | 725.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 56,820,000.00 USD | 56,820,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,630.00 USD | 577,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 23,510,000.00 USD | 23,510,000.00 USD | 37,380.00 USD | 0.00 USD | 33.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,570.00 USD | 572,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 23,470,000.00 USD | 23,470,000.00 USD | 29,230.00 USD | 0.00 USD | 267.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 55,370,000.00 USD | 55,370,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,080.00 USD | 558,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 23,450,000.00 USD | 23,450,000.00 USD | 37,860.00 USD | 0.00 USD | 2,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 5,960.00 USD | 103,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 23,400,000.00 USD | 23,400,000.00 USD | 35,050.00 USD | 0.00 USD | 145.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 52,760,000.00 USD | 52,760,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 97,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 23,370,000.00 USD | 23,370,000.00 USD | 37,380.00 USD | 27,500.00 USD | 162.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 3,870.00 USD | 96,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 23,300,000.00 USD | 23,300,000.00 USD | 41,590.00 USD | 1,840.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 50,000,000.00 USD | 50,000,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 311.95 USD | 92,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 23,250,000.00 USD | 23,250,000.00 USD | 105,300.00 USD | 57,220.00 USD | 24,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 780.39 USD | 92,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 23,060,000.00 USD | 23,060,000.00 USD | 237,520.00 USD | 175,410.00 USD | 125,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 47,940,000.00 USD | 47,940,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 91,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0747` | 22,520,000.00 USD | 22,520,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 90,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 22,060,000.00 USD | 22,060,000.00 USD | 169,810.00 USD | 65,720.00 USD | 98,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 45,040,000.00 USD | 45,040,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 21,730,000.00 USD | 21,730,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 1,370.00 USD | 89,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 21,380,000.00 USD | 21,380,000.00 USD | 235,680.00 USD | 83,730.00 USD | 121,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 41,940,000.00 USD | 41,940,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 451.13 USD | 88,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0751` | 20,940,000.00 USD | 20,940,000.00 USD | 277,260.00 USD | 82,120.00 USD | 66,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 14,540.00 USD | 88,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 20,510,000.00 USD | 20,510,000.00 USD | 124,190.00 USD | 19,450.00 USD | 85,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 40,070,000.00 USD | 40,070,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 3,910.00 USD | 73,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0753` | 20,280,000.00 USD | 20,280,000.00 USD | 127,320.00 USD | 72,710.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0754` | 617.57 USD | 69,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0754` | 20,060,000.00 USD | 20,060,000.00 USD | 95,400.00 USD | 62,330.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 36,710,000.00 USD | 36,710,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 69,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0755` | 19,880,000.00 USD | 19,880,000.00 USD | 122,130.00 USD | 15,650.00 USD | 68,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 19,670,000.00 USD | 19,670,000.00 USD | 177,070.00 USD | 157,590.00 USD | 111,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 34,320,000.00 USD | 34,320,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 356.24 USD | 64,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0757` | 19,220,000.00 USD | 19,220,000.00 USD | 99,480.00 USD | 44,790.00 USD | 104,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0757` | 3,270.00 USD | 64,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0758` | 18,970,000.00 USD | 18,970,000.00 USD | 77,300.00 USD | 42,980.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 29,140,000.00 USD | 29,140,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,540.00 USD | 61,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0759` | 18,820,000.00 USD | 18,820,000.00 USD | 116,240.00 USD | 85,920.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,320.00 USD | 55,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 18,610,000.00 USD | 18,610,000.00 USD | 285,080.00 USD | 289,180.00 USD | 216,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 24,520,000.00 USD | 24,520,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,690.00 USD | 23,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0761` | 17,820,000.00 USD | 17,820,000.00 USD | 477,110.00 USD | 391,680.00 USD | 272,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,130.00 USD | 21,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 16,680,000.00 USD | 16,680,000.00 USD | 510,560.00 USD | 248,230.00 USD | 179,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 20,190,000.00 USD | 20,190,000.00 USD | 1,210,000.00 USD | 1,070,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 5,710.00 USD | 20,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0763` | 15,740,000.00 USD | 15,740,000.00 USD | 360,900.00 USD | 139,670.00 USD | 197,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0764` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0764` | 15,040,000.00 USD | 15,040,000.00 USD | 396,130.00 USD | 346,900.00 USD | 90,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 17,140,000.00 USD | 17,140,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0765` | 9,890.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0765` | 14,210,000.00 USD | 14,210,000.00 USD | 551,690.00 USD | 223,110.00 USD | 314,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0766` | 13,120,000.00 USD | 13,120,000.00 USD | 620,360.00 USD | 272,640.00 USD | 280,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 14,900,000.00 USD | 14,900,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0767` | 11,950,000.00 USD | 11,950,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0768` | 11,390,000.00 USD | 11,390,000.00 USD | 425,990.00 USD | 236,860.00 USD | 142,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 12,980,000.00 USD | 12,980,000.00 USD | 722,060.00 USD | 452,460.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0769` | 242.54 USD | 5,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0769` | 10,590,000.00 USD | 10,590,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0770` | 330.81 USD | 4,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0770` | 10,100,000.00 USD | 10,100,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 11,300,000.00 USD | 11,300,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0770` | 109.41 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0771` | 9,440,000.00 USD | 9,440,000.00 USD | 231,550.00 USD | 266,030.00 USD | 190,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0772` | 8,750,000.00 USD | 8,750,000.00 USD | 169,730.00 USD | 318,140.00 USD | 333,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 9,640,000.00 USD | 9,640,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0773` | 7,930,000.00 USD | 7,930,000.00 USD | 288,370.00 USD | 151,140.00 USD | 241,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0774` | 7,250,000.00 USD | 7,250,000.00 USD | 165,350.00 USD | 98,170.00 USD | 108,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 7,860,000.00 USD | 7,860,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0775` | 6,870,000.00 USD | 6,870,000.00 USD | 181,290.00 USD | 12,820.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0776` | 6,660,000.00 USD | 6,660,000.00 USD | 106,410.00 USD | 237,880.00 USD | 232,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 6,020,000.00 USD | 6,020,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0777` | 6,090,000.00 USD | 6,090,000.00 USD | 18,430.00 USD | 56,290.00 USD | 146.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0778` | 6,010,000.00 USD | 6,010,000.00 USD | 6,440.00 USD | 0.00 USD | 68,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 5,540,000.00 USD | 5,540,000.00 USD | 125,140.00 USD | 58,330.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0779` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 253.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0780` | 5,940,000.00 USD | 5,940,000.00 USD | 138,400.00 USD | 30,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0781` | 5,770,000.00 USD | 5,770,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0782` | 5,720,000.00 USD | 5,720,000.00 USD | 44,780.00 USD | 71,230.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0783` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0784` | 4,390.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0784` | 5,470,000.00 USD | 5,470,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 302,040.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0785` | 4,910,000.00 USD | 4,910,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0786` | 4,570,000.00 USD | 4,570,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 4,810,000.00 USD | 4,810,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0787` | 4,050,000.00 USD | 4,050,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0788` | 3,460,000.00 USD | 3,460,000.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 4,140,000.00 USD | 4,140,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0789` | 3,030,000.00 USD | 3,030,000.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0790` | 2,800,000.00 USD | 2,800,000.00 USD | 200,610.00 USD | 137,240.00 USD | 50,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 3,410,000.00 USD | 3,410,000.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0791` | 2,410,000.00 USD | 2,410,000.00 USD | 76,010.00 USD | 3,690.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0792` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0793` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 33,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0794` | 2,240,000.00 USD | 2,240,000.00 USD | 466,850.00 USD | 243,180.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 3,080,000.00 USD | 3,080,000.00 USD | 882,130.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0795` | 1,440,000.00 USD | 1,440,000.00 USD | 260,570.00 USD | 131,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0796` | 1,050,000.00 USD | 1,050,000.00 USD | 117,990.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0796` | 1,560,000.00 USD | 1,560,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0797` | 911,140.00 USD | 911,140.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0798` | 512,860.00 USD | 512,860.00 USD | 0.00 USD | 164,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0798` | 688,050.00 USD | 688,050.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0799` | 348,630.00 USD | 348,630.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0800` | 5,610.00 USD | 5,610.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 10,910.00 USD | 10,910.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 95,670.00 USD | 95,670.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 14,430.00 USD | 14,430.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 244,940.00 USD | 244,940.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 125,270.00 USD | 125,270.00 USD | 0.00 USD | 70,050.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 1,060,000.00 USD | 1,060,000.00 USD | 503,640.00 USD | 26,410.00 USD | 400,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 1,650,000.00 USD | 1,650,000.00 USD | 405,610.00 USD | 193,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 1,870,000.00 USD | 1,870,000.00 USD | 150,810.00 USD | 60,350.00 USD | 293.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 161,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 2,330,000.00 USD | 2,330,000.00 USD | 14,540.00 USD | 19,910.00 USD | 269,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 3,950,000.00 USD | 3,950,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 2,590,000.00 USD | 2,590,000.00 USD | 27,080.00 USD | 18,240.00 USD | 209,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 3,010,000.00 USD | 3,010,000.00 USD | 22,430.00 USD | 13,790.00 USD | 386,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 5,050,000.00 USD | 5,050,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 3,570,000.00 USD | 3,570,000.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 4,450,000.00 USD | 4,450,000.00 USD | 441,880.00 USD | 245,220.00 USD | 189,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 8,000,000.00 USD | 8,000,000.00 USD | 1,230,000.00 USD | 1,040,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 5,090,000.00 USD | 5,090,000.00 USD | 361,650.00 USD | 152,470.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 5,880,000.00 USD | 5,880,000.00 USD | 298,910.00 USD | 161,880.00 USD | 321,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 11,510,000.00 USD | 11,510,000.00 USD | 1,650,000.00 USD | 944,390.00 USD | 916,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 6,570,000.00 USD | 6,570,000.00 USD | 171,350.00 USD | 368,950.00 USD | 156,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 7,570,000.00 USD | 7,570,000.00 USD | 215,860.00 USD | 285,850.00 USD | 499,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 14,280,000.00 USD | 14,280,000.00 USD | 990,880.00 USD | 836,130.00 USD | 942,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 8,310,000.00 USD | 8,310,000.00 USD | 393,540.00 USD | 167,900.00 USD | 171,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 8,900,000.00 USD | 8,900,000.00 USD | 268,440.00 USD | 195,730.00 USD | 127,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 16,770,000.00 USD | 16,770,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0823` | 121.40 USD | 4,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0823` | 9,120,000.00 USD | 9,120,000.00 USD | 185,080.00 USD | 30,920.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 9,660,000.00 USD | 9,660,000.00 USD | 198,500.00 USD | 202,010.00 USD | 137,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 18,540,000.00 USD | 18,540,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 12,660.00 USD | 17,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0825` | 9,830,000.00 USD | 9,830,000.00 USD | 101,400.00 USD | 44,860.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 10,010,000.00 USD | 10,010,000.00 USD | 33,820.00 USD | 5,050.00 USD | 146,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 20,210,000.00 USD | 20,210,000.00 USD | 885,350.00 USD | 370,770.00 USD | 419,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 10,130,000.00 USD | 10,130,000.00 USD | 108,560.00 USD | 8,240.00 USD | 55.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 10,530,000.00 USD | 10,530,000.00 USD | 265,750.00 USD | 56,990.00 USD | 75,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 21,330,000.00 USD | 21,330,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 10,950,000.00 USD | 10,950,000.00 USD | 260,740.00 USD | 88,990.00 USD | 72,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 11,470,000.00 USD | 11,470,000.00 USD | 260,260.00 USD | 108,400.00 USD | 152,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 22,310,000.00 USD | 22,310,000.00 USD | 431,690.00 USD | 205,960.00 USD | 337,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 11,700,000.00 USD | 11,700,000.00 USD | 116,480.00 USD | 64,510.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 12,110,000.00 USD | 12,110,000.00 USD | 238,860.00 USD | 91,440.00 USD | 86,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 23,790,000.00 USD | 23,790,000.00 USD | 676,300.00 USD | 524,960.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 12,370,000.00 USD | 12,370,000.00 USD | 153,900.00 USD | 68,410.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 12,720,000.00 USD | 12,720,000.00 USD | 154,940.00 USD | 60,550.00 USD | 135,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 25,340,000.00 USD | 25,340,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 13,100,000.00 USD | 13,100,000.00 USD | 122,780.00 USD | 184,470.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0835` | 205.70 USD | 29,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0836` | 13,490,000.00 USD | 13,490,000.00 USD | 83,690.00 USD | 84,520.00 USD | 221,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 26,500,000.00 USD | 26,500,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 29,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 13,780,000.00 USD | 13,780,000.00 USD | 189,580.00 USD | 61,550.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 30,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 14,050,000.00 USD | 14,050,000.00 USD | 144,100.00 USD | 76,380.00 USD | 48,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 27,290,000.00 USD | 27,290,000.00 USD | 480,150.00 USD | 257,510.00 USD | 56,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 14,120,000.00 USD | 14,120,000.00 USD | 67,620.00 USD | 0.00 USD | 639.31 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 30,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 14,170,000.00 USD | 14,170,000.00 USD | 33,540.00 USD | 15,480.00 USD | 584.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 27,600,000.00 USD | 27,600,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 14,200,000.00 USD | 14,200,000.00 USD | 32,120.00 USD | 2,010.00 USD | 709.20 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0842` | 462.91 USD | 31,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0842` | 14,280,000.00 USD | 14,280,000.00 USD | 31,430.00 USD | 0.00 USD | 47,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 28,050,000.00 USD | 28,050,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 14,320,000.00 USD | 14,320,000.00 USD | 36,500.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 14,410,000.00 USD | 14,410,000.00 USD | 88,610.00 USD | 0.00 USD | 563.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 28,520,000.00 USD | 28,520,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 14,430,000.00 USD | 14,430,000.00 USD | 20,470.00 USD | 0.00 USD | 353.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 14,510,000.00 USD | 14,510,000.00 USD | 67,820.00 USD | 16,670.00 USD | 75.71 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 28,910,000.00 USD | 28,910,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 31,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 14,530,000.00 USD | 14,530,000.00 USD | 18,780.00 USD | 0.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 14,550,000.00 USD | 14,550,000.00 USD | 20,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 29,560,000.00 USD | 29,560,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0849` | 14,570,000.00 USD | 14,570,000.00 USD | 15,210.00 USD | 0.00 USD | 292.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 14,590,000.00 USD | 14,590,000.00 USD | 21,120.00 USD | 0.00 USD | 413.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 30,350,000.00 USD | 30,350,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 31,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0851` | 14,630,000.00 USD | 14,630,000.00 USD | 24,960.00 USD | 11,000.00 USD | 665.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0852` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 304.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 30,590,000.00 USD | 30,590,000.00 USD | 68,050.00 USD | 87,540.00 USD | 78,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 14,640,000.00 USD | 14,640,000.00 USD | 12,910.00 USD | 737.47 USD | 212.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 14,700,000.00 USD | 14,700,000.00 USD | 34,680.00 USD | 13,190.00 USD | 10,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 30,970,000.00 USD | 30,970,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0855` | 14,850,000.00 USD | 14,850,000.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 14,990,000.00 USD | 14,990,000.00 USD | 92,490.00 USD | 32,810.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 31,630,000.00 USD | 31,630,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0857` | 15,090,000.00 USD | 15,090,000.00 USD | 50,540.00 USD | 18,030.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 15,170,000.00 USD | 15,170,000.00 USD | 48,130.00 USD | 36,780.00 USD | 164.89 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 32,000,000.00 USD | 32,000,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0859` | 15,310,000.00 USD | 15,310,000.00 USD | 72,260.00 USD | 20,870.00 USD | 40,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0860` | 15,390,000.00 USD | 15,390,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 32,250,000.00 USD | 32,250,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0861` | 15,450,000.00 USD | 15,450,000.00 USD | 20,430.00 USD | 0.00 USD | 32,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0862` | 15,520,000.00 USD | 15,520,000.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 32,540,000.00 USD | 32,540,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 34,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0863` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 219.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0864` | 15,570,000.00 USD | 15,570,000.00 USD | 22,510.00 USD | 20,050.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 32,590,000.00 USD | 32,590,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0865` | 15,620,000.00 USD | 15,620,000.00 USD | 31,770.00 USD | 1,280.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 15,680,000.00 USD | 15,680,000.00 USD | 25,410.00 USD | 16,310.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 32,850,000.00 USD | 32,850,000.00 USD | 146,420.00 USD | 33,740.00 USD | 80,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0867` | 15,760,000.00 USD | 15,760,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 15,810,000.00 USD | 15,810,000.00 USD | 9,000.00 USD | 9,540.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 33,290,000.00 USD | 33,290,000.00 USD | 199,460.00 USD | 157,140.00 USD | 84,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0869` | 15,840,000.00 USD | 15,840,000.00 USD | 13,960.00 USD | 8,720.00 USD | 9,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 15,880,000.00 USD | 15,880,000.00 USD | 33,110.00 USD | 6,620.00 USD | 375.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 33,700,000.00 USD | 33,700,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0871` | 16,030,000.00 USD | 16,030,000.00 USD | 50,960.00 USD | 57,110.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 16,080,000.00 USD | 16,080,000.00 USD | 27,110.00 USD | 16,340.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 34,100,000.00 USD | 34,100,000.00 USD | 148,660.00 USD | 144,580.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0873` | 16,100,000.00 USD | 16,100,000.00 USD | 1,730.00 USD | 1,460.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 34,230,000.00 USD | 34,230,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0875` | 16,120,000.00 USD | 16,120,000.00 USD | 25,220.00 USD | 717.80 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 9,620.00 USD | 44,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0876` | 16,200,000.00 USD | 16,200,000.00 USD | 33,830.00 USD | 15,030.00 USD | 26,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 34,460,000.00 USD | 34,460,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0877` | 16,250,000.00 USD | 16,250,000.00 USD | 21,520.00 USD | 11,700.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0878` | 16,410,000.00 USD | 16,410,000.00 USD | 63,040.00 USD | 40,570.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 34,680,000.00 USD | 34,680,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0879` | 16,440,000.00 USD | 16,440,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0880` | 16,540,000.00 USD | 16,540,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 34,960,000.00 USD | 34,960,000.00 USD | 111,530.00 USD | 126,390.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 44,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0881` | 16,600,000.00 USD | 16,600,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0882` | 16,670,000.00 USD | 16,670,000.00 USD | 25,340.00 USD | 15,630.00 USD | 27,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0882` | 35,250,000.00 USD | 35,250,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0883` | 16,780,000.00 USD | 16,780,000.00 USD | 26,840.00 USD | 73,610.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0884` | 16,890,000.00 USD | 16,890,000.00 USD | 8,850.00 USD | 17,780.00 USD | 83,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 35,520,000.00 USD | 35,520,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0886` | 16,970,000.00 USD | 16,970,000.00 USD | 48,870.00 USD | 18,070.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 35,610,000.00 USD | 35,610,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0887` | 17,030,000.00 USD | 17,030,000.00 USD | 22,710.00 USD | 22,450.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 44,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0888` | 17,050,000.00 USD | 17,050,000.00 USD | 16,050.00 USD | 0.00 USD | 142.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0888` | 35,650,000.00 USD | 35,650,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0889` | 17,050,000.00 USD | 17,050,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0890` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 802.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 35,660,000.00 USD | 35,660,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0891` | 17,080,000.00 USD | 17,080,000.00 USD | 2,580.00 USD | 0.00 USD | 18,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0892` | 17,080,000.00 USD | 17,080,000.00 USD | 0.00 USD | 0.00 USD | 101.53 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0892` | 35,730,000.00 USD | 35,730,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0893` | 17,100,000.00 USD | 17,100,000.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0894` | 17,120,000.00 USD | 17,120,000.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0896` | 871.86 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 46,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 35,740,000.00 USD | 35,740,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.0696` | 68,920,000.00 USD | 0.00 USD | 68,920,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `7D` | `0.0698` | 68,060,000.00 USD | 0.00 USD | 68,060,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `7D` | `0.0700` | 67,550,000.00 USD | 0.00 USD | 67,550,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `7D` | `0.0702` | 66,920,000.00 USD | 0.00 USD | 66,920,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `7D` | `0.0704` | 66,560,000.00 USD | 0.00 USD | 66,560,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `7D` | `0.0706` | 66,290,000.00 USD | 0.00 USD | 66,290,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `7D` | `0.0708` | 66,000,000.00 USD | 0.00 USD | 66,000,000.00 USD | 156,500.00 USD | 34,470.00 USD | 107,870.00 USD |
| `7D` | `0.0710` | 65,700,000.00 USD | 0.00 USD | 65,700,000.00 USD | 229,480.00 USD | 157,140.00 USD | 84,250.00 USD |
| `7D` | `0.0712` | 65,230,000.00 USD | 0.00 USD | 65,230,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `7D` | `0.0714` | 64,730,000.00 USD | 0.00 USD | 64,730,000.00 USD | 236,020.00 USD | 144,580.00 USD | 113,330.00 USD |
| `7D` | `0.0716` | 64,230,000.00 USD | 0.00 USD | 64,230,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 24,840,000.00 USD | 0.00 USD | 24,840,000.00 USD | 80,570.00 USD | 27,450.00 USD | 48,720.00 USD |
| `1D` | `0.0718` | 24,680,000.00 USD | 0.00 USD | 24,680,000.00 USD | 63,040.00 USD | 40,570.00 USD | 50,790.00 USD |
| `7D` | `0.0718` | 63,800,000.00 USD | 0.00 USD | 63,800,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 24,530,000.00 USD | 0.00 USD | 24,530,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `1D` | `0.0720` | 24,490,000.00 USD | 0.00 USD | 24,490,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0720` | 63,440,000.00 USD | 0.00 USD | 63,440,000.00 USD | 277,980.00 USD | 181,150.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 24,400,000.00 USD | 0.00 USD | 24,400,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0722` | 24,330,000.00 USD | 0.00 USD | 24,330,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,970.00 USD |
| `7D` | `0.0722` | 62,870,000.00 USD | 0.00 USD | 62,870,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 24,260,000.00 USD | 0.00 USD | 24,260,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,860.00 USD |
| `1D` | `0.0724` | 24,150,000.00 USD | 0.00 USD | 24,150,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,070.00 USD |
| `7D` | `0.0724` | 62,490,000.00 USD | 0.00 USD | 62,490,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 24,010,000.00 USD | 0.00 USD | 24,010,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,900.00 USD |
| `1D` | `0.0726` | 23,860,000.00 USD | 0.00 USD | 23,860,000.00 USD | 31,660.00 USD | 0.00 USD | 142.34 USD |
| `7D` | `0.0726` | 62,000,000.00 USD | 0.00 USD | 62,000,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 23,820,000.00 USD | 0.00 USD | 23,820,000.00 USD | 20,420.00 USD | 0.00 USD | 200.42 USD |
| `1D` | `0.0728` | 23,800,000.00 USD | 0.00 USD | 23,800,000.00 USD | 15,580.00 USD | 802.30 USD | 419.85 USD |
| `7D` | `0.0728` | 61,510,000.00 USD | 0.00 USD | 61,510,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 23,790,000.00 USD | 0.00 USD | 23,790,000.00 USD | 17,820.00 USD | 0.00 USD | 18,720.00 USD |
| `1D` | `0.0730` | 23,750,000.00 USD | 0.00 USD | 23,750,000.00 USD | 14,450.00 USD | 0.00 USD | 223.21 USD |
| `7D` | `0.0730` | 61,080,000.00 USD | 0.00 USD | 61,080,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 23,740,000.00 USD | 0.00 USD | 23,740,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD |
| `1D` | `0.0732` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 42,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0732` | 60,760,000.00 USD | 0.00 USD | 60,760,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 23,650,000.00 USD | 0.00 USD | 23,650,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0734` | 23,640,000.00 USD | 0.00 USD | 23,640,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 59,200,000.00 USD | 0.00 USD | 59,200,000.00 USD | 646,280.00 USD | 190,810.00 USD | 59,090.00 USD |
| `1D` | `0.0735` | 23,640,000.00 USD | 0.00 USD | 23,640,000.00 USD | 24,100.00 USD | 0.00 USD | 41.24 USD |
| `1D` | `0.0736` | 23,610,000.00 USD | 0.00 USD | 23,610,000.00 USD | 9,980.00 USD | 0.00 USD | 258.52 USD |
| `7D` | `0.0736` | 58,310,000.00 USD | 0.00 USD | 58,310,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 23,600,000.00 USD | 0.00 USD | 23,600,000.00 USD | 47,420.00 USD | 0.00 USD | 983.61 USD |
| `1D` | `0.0738` | 23,550,000.00 USD | 0.00 USD | 23,550,000.00 USD | 39,420.00 USD | 0.00 USD | 725.86 USD |
| `7D` | `0.0738` | 56,820,000.00 USD | 0.00 USD | 56,820,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 23,510,000.00 USD | 0.00 USD | 23,510,000.00 USD | 37,380.00 USD | 0.00 USD | 33.30 USD |
| `1D` | `0.0740` | 23,470,000.00 USD | 0.00 USD | 23,470,000.00 USD | 29,230.00 USD | 0.00 USD | 267.65 USD |
| `7D` | `0.0740` | 55,370,000.00 USD | 0.00 USD | 55,370,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 23,450,000.00 USD | 0.00 USD | 23,450,000.00 USD | 37,860.00 USD | 0.00 USD | 2,410.00 USD |
| `1D` | `0.0742` | 23,400,000.00 USD | 0.00 USD | 23,400,000.00 USD | 35,050.00 USD | 0.00 USD | 145.18 USD |
| `7D` | `0.0742` | 52,760,000.00 USD | 0.00 USD | 52,760,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 23,370,000.00 USD | 0.00 USD | 23,370,000.00 USD | 37,380.00 USD | 27,500.00 USD | 162.32 USD |
| `1D` | `0.0744` | 23,300,000.00 USD | 0.00 USD | 23,300,000.00 USD | 41,590.00 USD | 1,840.00 USD | 15,430.00 USD |
| `7D` | `0.0744` | 50,000,000.00 USD | 0.00 USD | 50,000,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 23,250,000.00 USD | 0.00 USD | 23,250,000.00 USD | 105,300.00 USD | 57,220.00 USD | 24,900.00 USD |
| `1D` | `0.0746` | 23,060,000.00 USD | 0.00 USD | 23,060,000.00 USD | 237,520.00 USD | 175,410.00 USD | 125,570.00 USD |
| `7D` | `0.0746` | 47,940,000.00 USD | 0.00 USD | 47,940,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,320.00 USD |
| `1D` | `0.0747` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,440.00 USD |
| `1D` | `0.0748` | 22,060,000.00 USD | 0.00 USD | 22,060,000.00 USD | 169,810.00 USD | 65,720.00 USD | 98,750.00 USD |
| `7D` | `0.0748` | 45,040,000.00 USD | 0.00 USD | 45,040,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,370.00 USD |
| `1D` | `0.0749` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,040.00 USD |
| `1D` | `0.0750` | 21,380,000.00 USD | 0.00 USD | 21,380,000.00 USD | 235,680.00 USD | 83,730.00 USD | 121,130.00 USD |
| `7D` | `0.0750` | 41,940,000.00 USD | 0.00 USD | 41,940,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 20,940,000.00 USD | 0.00 USD | 20,940,000.00 USD | 277,260.00 USD | 82,120.00 USD | 66,910.00 USD |
| `1D` | `0.0752` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 124,190.00 USD | 19,450.00 USD | 85,750.00 USD |
| `7D` | `0.0752` | 40,070,000.00 USD | 0.00 USD | 40,070,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 127,320.00 USD | 72,710.00 USD | 28,530.00 USD |
| `1D` | `0.0754` | 20,060,000.00 USD | 0.00 USD | 20,060,000.00 USD | 95,400.00 USD | 62,330.00 USD | 21,670.00 USD |
| `7D` | `0.0754` | 36,710,000.00 USD | 0.00 USD | 36,710,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 19,880,000.00 USD | 0.00 USD | 19,880,000.00 USD | 122,130.00 USD | 15,650.00 USD | 68,560.00 USD |
| `1D` | `0.0756` | 19,670,000.00 USD | 0.00 USD | 19,670,000.00 USD | 177,070.00 USD | 157,590.00 USD | 111,780.00 USD |
| `7D` | `0.0756` | 34,320,000.00 USD | 0.00 USD | 34,320,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 19,220,000.00 USD | 0.00 USD | 19,220,000.00 USD | 99,480.00 USD | 44,790.00 USD | 104,970.00 USD |
| `1D` | `0.0758` | 18,970,000.00 USD | 0.00 USD | 18,970,000.00 USD | 77,300.00 USD | 42,980.00 USD | 31,840.00 USD |
| `7D` | `0.0758` | 29,140,000.00 USD | 0.00 USD | 29,140,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 18,820,000.00 USD | 0.00 USD | 18,820,000.00 USD | 116,240.00 USD | 85,920.00 USD | 9,610.00 USD |
| `1D` | `0.0760` | 18,610,000.00 USD | 0.00 USD | 18,610,000.00 USD | 285,080.00 USD | 289,180.00 USD | 216,150.00 USD |
| `7D` | `0.0760` | 24,520,000.00 USD | 0.00 USD | 24,520,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 17,820,000.00 USD | 0.00 USD | 17,820,000.00 USD | 477,110.00 USD | 391,680.00 USD | 272,010.00 USD |
| `1D` | `0.0762` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 510,560.00 USD | 248,230.00 USD | 179,730.00 USD |
| `7D` | `0.0762` | 20,190,000.00 USD | 0.00 USD | 20,190,000.00 USD | 1,210,000.00 USD | 1,070,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 360,900.00 USD | 139,670.00 USD | 197,140.00 USD |
| `1D` | `0.0764` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 396,130.00 USD | 346,900.00 USD | 90,870.00 USD |
| `7D` | `0.0764` | 17,140,000.00 USD | 0.00 USD | 17,140,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 551,690.00 USD | 223,110.00 USD | 314,140.00 USD |
| `1D` | `0.0766` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 620,360.00 USD | 272,640.00 USD | 280,190.00 USD |
| `7D` | `0.0766` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,400.00 USD |
| `1D` | `0.0767` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,850.00 USD |
| `1D` | `0.0768` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 425,990.00 USD | 236,860.00 USD | 142,100.00 USD |
| `7D` | `0.0768` | 12,980,000.00 USD | 0.00 USD | 12,980,000.00 USD | 722,060.00 USD | 452,460.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,010.00 USD |
| `1D` | `0.0770` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,410.00 USD |
| `7D` | `0.0770` | 11,300,000.00 USD | 0.00 USD | 11,300,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 231,550.00 USD | 266,030.00 USD | 190,250.00 USD |
| `1D` | `0.0772` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 169,730.00 USD | 318,140.00 USD | 333,150.00 USD |
| `7D` | `0.0772` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 288,370.00 USD | 151,140.00 USD | 241,270.00 USD |
| `1D` | `0.0774` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 165,350.00 USD | 98,170.00 USD | 108,170.00 USD |
| `7D` | `0.0774` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 181,290.00 USD | 12,820.00 USD | 17,130.00 USD |
| `1D` | `0.0776` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 106,410.00 USD | 237,880.00 USD | 232,080.00 USD |
| `7D` | `0.0776` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 18,430.00 USD | 56,290.00 USD | 146.30 USD |
| `1D` | `0.0778` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 6,440.00 USD | 0.00 USD | 68,580.00 USD |
| `7D` | `0.0778` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 125,140.00 USD | 58,330.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 253.82 USD |
| `1D` | `0.0780` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 138,400.00 USD | 30,070.00 USD | 0.00 USD |
| `1D` | `0.0781` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD |
| `1D` | `0.0782` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 44,780.00 USD | 71,230.00 USD | 85,130.00 USD |
| `7D` | `0.0782` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD |
| `1D` | `0.0784` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD |
| `7D` | `0.0784` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 0.00 USD | 302,040.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD |
| `1D` | `0.0788` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD |
| `7D` | `0.0788` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD |
| `1D` | `0.0790` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 200,610.00 USD | 137,240.00 USD | 50,580.00 USD |
| `7D` | `0.0790` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 76,010.00 USD | 3,690.00 USD | 30,030.00 USD |
| `1D` | `0.0792` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD |
| `1D` | `0.0793` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 33,790.00 USD | 0.00 USD |
| `1D` | `0.0794` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 466,850.00 USD | 243,180.00 USD | 93,060.00 USD |
| `7D` | `0.0794` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 882,130.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 260,570.00 USD | 131,430.00 USD | 0.00 USD |
| `1D` | `0.0796` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 117,990.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 911,140.00 USD | 0.00 USD | 911,140.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 512,860.00 USD | 0.00 USD | 512,860.00 USD | 0.00 USD | 164,240.00 USD | 0.00 USD |
| `7D` | `0.0798` | 688,050.00 USD | 0.00 USD | 688,050.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 348,630.00 USD | 0.00 USD | 348,630.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD |
| `1D` | `0.0800` | 5,610.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `7D` | `0.0800` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0801` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0804` | 10,910.00 USD | 10,910.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 95,670.00 USD | 95,670.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 14,430.00 USD | 14,430.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0806` | 244,940.00 USD | 244,940.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 125,270.00 USD | 125,270.00 USD | 0.00 USD | 0.00 USD | 70,050.00 USD | 40,790.00 USD |
| `1D` | `0.0808` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 503,640.00 USD | 26,410.00 USD | 400,010.00 USD |
| `7D` | `0.0808` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 405,610.00 USD | 193,380.00 USD | 0.00 USD |
| `1D` | `0.0810` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 150,810.00 USD | 60,350.00 USD | 293.28 USD |
| `7D` | `0.0810` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 161,440.00 USD | 0.00 USD |
| `1D` | `0.0812` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 14,540.00 USD | 19,910.00 USD | 269,820.00 USD |
| `7D` | `0.0812` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 27,080.00 USD | 18,240.00 USD | 209,180.00 USD |
| `1D` | `0.0814` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 22,430.00 USD | 13,790.00 USD | 386,300.00 USD |
| `7D` | `0.0814` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD |
| `1D` | `0.0816` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 441,880.00 USD | 245,220.00 USD | 189,500.00 USD |
| `7D` | `0.0816` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,040,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 361,650.00 USD | 152,470.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 298,910.00 USD | 161,880.00 USD | 321,810.00 USD |
| `7D` | `0.0818` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 1,650,000.00 USD | 944,390.00 USD | 916,730.00 USD |
| `1D` | `0.0819` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 171,350.00 USD | 368,950.00 USD | 156,890.00 USD |
| `1D` | `0.0820` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 215,860.00 USD | 285,850.00 USD | 499,340.00 USD |
| `7D` | `0.0820` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 942,520.00 USD |
| `1D` | `0.0821` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 393,540.00 USD | 167,900.00 USD | 171,040.00 USD |
| `1D` | `0.0822` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 268,440.00 USD | 195,730.00 USD | 127,580.00 USD |
| `7D` | `0.0822` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 185,080.00 USD | 30,920.00 USD | 9,460.00 USD |
| `1D` | `0.0824` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 198,500.00 USD | 202,010.00 USD | 137,490.00 USD |
| `7D` | `0.0824` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 101,400.00 USD | 44,860.00 USD | 21,620.00 USD |
| `1D` | `0.0826` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 33,820.00 USD | 5,050.00 USD | 146,520.00 USD |
| `7D` | `0.0826` | 20,210,000.00 USD | 20,210,000.00 USD | 0.00 USD | 885,350.00 USD | 370,770.00 USD | 419,800.00 USD |
| `1D` | `0.0827` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 108,560.00 USD | 8,240.00 USD | 55.02 USD |
| `1D` | `0.0828` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 265,750.00 USD | 56,990.00 USD | 75,070.00 USD |
| `7D` | `0.0828` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 260,740.00 USD | 88,990.00 USD | 72,740.00 USD |
| `1D` | `0.0830` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 260,260.00 USD | 108,400.00 USD | 152,000.00 USD |
| `7D` | `0.0830` | 22,310,000.00 USD | 22,310,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 337,880.00 USD |
| `1D` | `0.0831` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 116,480.00 USD | 64,510.00 USD | 43,220.00 USD |
| `1D` | `0.0832` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 238,860.00 USD | 91,440.00 USD | 86,260.00 USD |
| `7D` | `0.0832` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 676,300.00 USD | 524,960.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 153,900.00 USD | 68,410.00 USD | 31,430.00 USD |
| `1D` | `0.0834` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 154,940.00 USD | 60,550.00 USD | 135,700.00 USD |
| `7D` | `0.0834` | 25,340,000.00 USD | 25,340,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 122,780.00 USD | 184,470.00 USD | 78,760.00 USD |
| `1D` | `0.0836` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 83,690.00 USD | 84,520.00 USD | 221,700.00 USD |
| `7D` | `0.0836` | 26,500,000.00 USD | 26,500,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 189,580.00 USD | 61,550.00 USD | 34,400.00 USD |
| `1D` | `0.0838` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 144,100.00 USD | 76,380.00 USD | 48,680.00 USD |
| `7D` | `0.0838` | 27,290,000.00 USD | 27,290,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 56,160.00 USD |
| `1D` | `0.0839` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 67,620.00 USD | 0.00 USD | 639.31 USD |
| `1D` | `0.0840` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 33,540.00 USD | 15,480.00 USD | 584.63 USD |
| `7D` | `0.0840` | 27,600,000.00 USD | 27,600,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,510.00 USD |
| `1D` | `0.0841` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 32,120.00 USD | 2,010.00 USD | 709.20 USD |
| `1D` | `0.0842` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 31,430.00 USD | 0.00 USD | 47,110.00 USD |
| `7D` | `0.0842` | 28,050,000.00 USD | 28,050,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 36,500.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.0844` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 88,610.00 USD | 0.00 USD | 563.70 USD |
| `7D` | `0.0844` | 28,520,000.00 USD | 28,520,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 20,470.00 USD | 0.00 USD | 353.58 USD |
| `1D` | `0.0846` | 14,510,000.00 USD | 14,510,000.00 USD | 0.00 USD | 67,820.00 USD | 16,670.00 USD | 75.71 USD |
| `7D` | `0.0846` | 28,910,000.00 USD | 28,910,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 18,780.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `0.0848` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 20,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 29,560,000.00 USD | 29,560,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0849` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 15,210.00 USD | 0.00 USD | 292.60 USD |
| `1D` | `0.0850` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 21,120.00 USD | 0.00 USD | 413.16 USD |
| `7D` | `0.0850` | 30,350,000.00 USD | 30,350,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0851` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 24,960.00 USD | 11,000.00 USD | 665.45 USD |
| `1D` | `0.0852` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.58 USD |
| `7D` | `0.0852` | 30,590,000.00 USD | 30,590,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 78,410.00 USD |
| `1D` | `0.0853` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 12,910.00 USD | 737.47 USD | 212.49 USD |
| `1D` | `0.0854` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 34,680.00 USD | 13,190.00 USD | 10,120.00 USD |
| `7D` | `0.0854` | 30,970,000.00 USD | 30,970,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0855` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD |
| `1D` | `0.0856` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 92,490.00 USD | 32,810.00 USD | 19,870.00 USD |
| `7D` | `0.0856` | 31,630,000.00 USD | 31,630,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0857` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 50,540.00 USD | 18,030.00 USD | 27,880.00 USD |
| `1D` | `0.0858` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 48,130.00 USD | 36,780.00 USD | 164.89 USD |
| `7D` | `0.0858` | 32,000,000.00 USD | 32,000,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0859` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 72,260.00 USD | 20,870.00 USD | 40,140.00 USD |
| `1D` | `0.0860` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 44,920.00 USD | 22,170.00 USD | 20,180.00 USD |
| `7D` | `0.0860` | 32,250,000.00 USD | 32,250,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0861` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 20,430.00 USD | 0.00 USD | 32,450.00 USD |
| `1D` | `0.0862` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD |
| `7D` | `0.0862` | 32,540,000.00 USD | 32,540,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0863` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 219.34 USD |
| `1D` | `0.0864` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,150.00 USD |
| `7D` | `0.0864` | 32,590,000.00 USD | 32,590,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0865` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 31,770.00 USD | 1,280.00 USD | 18,020.00 USD |
| `1D` | `0.0866` | 15,680,000.00 USD | 15,680,000.00 USD | 0.00 USD | 25,410.00 USD | 16,310.00 USD | 19,340.00 USD |
| `7D` | `0.0866` | 32,850,000.00 USD | 32,850,000.00 USD | 0.00 USD | 146,420.00 USD | 33,740.00 USD | 80,480.00 USD |
| `1D` | `0.0867` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 24,580.00 USD | 37,120.00 USD | 14,130.00 USD |
| `1D` | `0.0868` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 9,000.00 USD | 9,540.00 USD | 34,750.00 USD |
| `7D` | `0.0868` | 33,290,000.00 USD | 33,290,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 84,000.00 USD |
| `1D` | `0.0869` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 13,960.00 USD | 8,720.00 USD | 9,620.00 USD |
| `1D` | `0.0870` | 15,880,000.00 USD | 15,880,000.00 USD | 0.00 USD | 33,110.00 USD | 6,620.00 USD | 375.99 USD |
| `7D` | `0.0870` | 33,700,000.00 USD | 33,700,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0871` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 50,960.00 USD | 57,110.00 USD | 37,920.00 USD |
| `1D` | `0.0872` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 27,110.00 USD | 16,340.00 USD | 8,650.00 USD |
| `7D` | `0.0872` | 34,100,000.00 USD | 34,100,000.00 USD | 0.00 USD | 148,660.00 USD | 144,580.00 USD | 112,220.00 USD |
| `1D` | `0.0873` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 1,730.00 USD | 1,460.00 USD | 13,660.00 USD |
| `7D` | `0.0874` | 34,230,000.00 USD | 34,230,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0875` | 16,120,000.00 USD | 16,120,000.00 USD | 0.00 USD | 25,220.00 USD | 717.80 USD | 0.00 USD |
| `1D` | `0.0876` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 33,830.00 USD | 15,030.00 USD | 26,890.00 USD |
| `7D` | `0.0876` | 34,460,000.00 USD | 34,460,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0877` | 16,250,000.00 USD | 16,250,000.00 USD | 0.00 USD | 21,520.00 USD | 11,700.00 USD | 21,830.00 USD |
| `1D` | `0.0878` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 63,040.00 USD | 40,570.00 USD | 50,790.00 USD |
| `7D` | `0.0878` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `1D` | `0.0879` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `1D` | `0.0880` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0880` | 34,960,000.00 USD | 34,960,000.00 USD | 0.00 USD | 111,530.00 USD | 126,390.00 USD | 51,000.00 USD |
| `1D` | `0.0881` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0882` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 25,340.00 USD | 15,630.00 USD | 27,970.00 USD |
| `7D` | `0.0882` | 35,250,000.00 USD | 35,250,000.00 USD | 0.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD |
| `1D` | `0.0883` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 26,840.00 USD | 73,610.00 USD | 7,860.00 USD |
| `1D` | `0.0884` | 16,890,000.00 USD | 16,890,000.00 USD | 0.00 USD | 8,850.00 USD | 17,780.00 USD | 83,950.00 USD |
| `7D` | `0.0884` | 35,520,000.00 USD | 35,520,000.00 USD | 0.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD |
| `1D` | `0.0886` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 48,870.00 USD | 18,070.00 USD | 13,500.00 USD |
| `7D` | `0.0886` | 35,610,000.00 USD | 35,610,000.00 USD | 0.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD |
| `1D` | `0.0887` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 22,710.00 USD | 22,450.00 USD | 19,280.00 USD |
| `1D` | `0.0888` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 16,050.00 USD | 0.00 USD | 142.34 USD |
| `7D` | `0.0888` | 35,650,000.00 USD | 35,650,000.00 USD | 0.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0889` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0890` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 0.00 USD | 802.30 USD | 0.00 USD |
| `7D` | `0.0890` | 35,660,000.00 USD | 35,660,000.00 USD | 0.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD |
| `1D` | `0.0891` | 17,080,000.00 USD | 17,080,000.00 USD | 0.00 USD | 2,580.00 USD | 0.00 USD | 18,610.00 USD |
| `1D` | `0.0892` | 17,080,000.00 USD | 17,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101.53 USD |
| `7D` | `0.0892` | 35,730,000.00 USD | 35,730,000.00 USD | 0.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD |
| `1D` | `0.0893` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0894` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0900` | 35,740,000.00 USD | 35,740,000.00 USD | 0.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.13B` | Total OI Tokens: `14,103,539,855.2 DOGE`
  * 1h OI Change: `-0.17%` | 4h OI Change: `+0.66%` | 24h OI Change: `-0.58%`
  * Exchange Breakdown: Binance=`273.30M` | Bybit=`114.00M` | OKX=`116.51M` | Hyperliquid=`80.95M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `44.53K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
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
| `15M` | `DOGE` | `48.74%` | `51.26%` | `0.95` | 48,380,000.00 USD |
| `15M` | `Binance` | `45.77%` | `54.23%` | `0.84` | 16,280,000.00 USD |
| `15M` | `OKX` | `45.13%` | `54.87%` | `0.82` | 5,310,000.00 USD |
| `15M` | `Bybit` | `50.09%` | `49.91%` | `1.00` | 3,300,000.00 USD |
| `15M` | `KuCoin` | `47.01%` | `52.99%` | `0.89` | 321,550.00 USD |
| `15M` | `Gate` | `56.19%` | `43.81%` | `1.28` | 5,750,000.00 USD |
| `15M` | `Bitget` | `43.78%` | `56.22%` | `0.78` | 1,400,000.00 USD |
| `15M` | `BingX` | `61.44%` | `38.56%` | `1.59` | 3,320,000.00 USD |
| `15M` | `MEXC` | `47.06%` | `52.94%` | `0.89` | 4,360,000.00 USD |
| `15M` | `Bitunix` | `59.17%` | `40.83%` | `1.45` | 3,620,000.00 USD |
| `15M` | `Hyperliquid` | `42.5%` | `57.5%` | `0.74` | 329,140.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `75.33%` | `24.67%` | `3.05` | 284,470.00 USD |
| `15M` | `Crypto.com` | `61%` | `39%` | `1.56` | 83,480.00 USD |
| `15M` | `WhiteBIT` | `12.57%` | `87.43%` | `0.14` | 1,850,000.00 USD |
| `15M` | `HTX` | `66.87%` | `33.13%` | `2.02` | 49,720.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `74.42%` | `25.58%` | `2.91` | 989,520.00 USD |
| `15M` | `Aster` | `32%` | `68%` | `0.47` | 602,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `47.96%` | `52.04%` | `0.92` | 525,410.00 USD |
| `15M` | `Whale Positions` | `45.77%` | `54.23%` | `0.84` | 16,280,000.00 USD |
| `15M` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 48,380,000.00 USD |
| `1H` | `DOGE` | `44.21%` | `55.79%` | `0.79` | 260,410,000.00 USD |
| `1H` | `Binance` | `44.92%` | `55.08%` | `0.82` | 94,140,000.00 USD |
| `1H` | `OKX` | `38.07%` | `61.93%` | `0.61` | 36,110,000.00 USD |
| `1H` | `Bybit` | `39.37%` | `60.63%` | `0.65` | 21,790,000.00 USD |
| `1H` | `KuCoin` | `40.41%` | `59.59%` | `0.68` | 1,860,000.00 USD |
| `1H` | `Gate` | `49.18%` | `50.82%` | `0.97` | 25,520,000.00 USD |
| `1H` | `Bitget` | `46.33%` | `53.67%` | `0.86` | 7,410,000.00 USD |
| `1H` | `BingX` | `52.69%` | `47.31%` | `1.11` | 11,470,000.00 USD |
| `1H` | `MEXC` | `56.49%` | `43.51%` | `1.30` | 19,910,000.00 USD |
| `1H` | `Bitunix` | `51.83%` | `48.17%` | `1.08` | 14,550,000.00 USD |
| `1H` | `Hyperliquid` | `38.02%` | `61.98%` | `0.61` | 3,940,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.24%` | `50.76%` | `0.97` | 3,490,000.00 USD |
| `1H` | `Crypto.com` | `50.11%` | `49.89%` | `1.00` | 475,670.00 USD |
| `1H` | `WhiteBIT` | `10.92%` | `89.08%` | `0.12` | 5,250,000.00 USD |
| `1H` | `HTX` | `31.73%` | `68.27%` | `0.46` | 583,320.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `32.89%` | `67.11%` | `0.49` | 7,420,000.00 USD |
| `1H` | `Aster` | `37.69%` | `62.31%` | `0.60` | 3,570,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.26%` | `67.74%` | `0.48` | 2,890,000.00 USD |
| `1H` | `Whale Positions` | `44.92%` | `55.08%` | `0.82` | 94,140,000.00 USD |
| `1H` | `Global Accounts` | `44.21%` | `55.79%` | `0.79` | 260,410,000.00 USD |
| `4H` | `DOGE` | `48.99%` | `51.01%` | `0.96` | 1,650,000,000.00 USD |
| `4H` | `Binance` | `49.47%` | `50.53%` | `0.98` | 539,550,000.00 USD |
| `4H` | `OKX` | `48.8%` | `51.2%` | `0.95` | 267,500,000.00 USD |
| `4H` | `Bybit` | `55.65%` | `44.35%` | `1.25` | 156,420,000.00 USD |
| `4H` | `KuCoin` | `52.73%` | `47.27%` | `1.12` | 12,580,000.00 USD |
| `4H` | `Gate` | `50.89%` | `49.11%` | `1.04` | 124,810,000.00 USD |
| `4H` | `Bitget` | `49.6%` | `50.4%` | `0.98` | 55,240,000.00 USD |
| `4H` | `BingX` | `46.35%` | `53.65%` | `0.86` | 93,590,000.00 USD |
| `4H` | `MEXC` | `43.86%` | `56.14%` | `0.78` | 152,560,000.00 USD |
| `4H` | `Bitunix` | `49.19%` | `50.81%` | `0.97` | 86,910,000.00 USD |
| `4H` | `Hyperliquid` | `52.71%` | `47.29%` | `1.11` | 45,330,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.87%` | `51.13%` | `0.96` | 23,390,000.00 USD |
| `4H` | `Crypto.com` | `50.06%` | `49.94%` | `1.00` | 3,320,000.00 USD |
| `4H` | `WhiteBIT` | `27.41%` | `72.59%` | `0.38` | 21,490,000.00 USD |
| `4H` | `HTX` | `56.93%` | `43.07%` | `1.32` | 2,580,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.85%` | `57.15%` | `0.75` | 35,050,000.00 USD |
| `4H` | `Aster` | `40.15%` | `59.85%` | `0.67` | 18,240,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.01%` | `43.99%` | `1.27` | 14,080,000.00 USD |
| `4H` | `Whale Positions` | `49.47%` | `50.53%` | `0.98` | 539,550,000.00 USD |
| `4H` | `Global Accounts` | `48.99%` | `51.01%` | `0.96` | 1,650,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0803` | `0.0798` | 4,372,559.79 USD | 2,097,742.47 USD | 2,274,817.31 USD | -177,074.84 USD | `-4.05%` | `5B / 8S` |
| `0:00 UTC` | `0.0802` | `0.0802` | `0.0802` | `0.0803` | `0.0798` | 5,919,541.11 USD | 3,302,953.65 USD | 2,616,587.46 USD | 686,366.19 USD | `+11.59%` | `9B / 2S` |
| `5:00 UTC` | `0.0804` | `0.0805` | `0.0804` | `0.0807` | `0.0802` | 7,554,604.29 USD | 4,072,091.15 USD | 3,482,513.14 USD | 589,578.01 USD | `+7.80%` | `10B / 4S` |
| `0:00 UTC` | `0.0808` | `0.0809` | `0.0808` | `0.0815` | `0.0804` | 18,574,379.74 USD | 9,613,153.94 USD | 8,961,225.80 USD | 651,928.14 USD | `+3.51%` | `14B / 9S` |
| `5:00 UTC` | `0.0807` | `0.0805` | `0.0807` | `0.0809` | `0.0802` | 9,552,151.73 USD | 4,610,293.53 USD | 4,941,858.20 USD | -331,564.68 USD | `-3.47%` | `6B / 12S` |
| `0:00 UTC` | `0.0801` | `0.0801` | `0.0801` | `0.0804` | `0.0799` | 7,702,082.98 USD | 2,993,499.68 USD | 4,708,583.30 USD | -1,715,083.61 USD | `-22.27%` | `2B / 6S` |
| `5:00 UTC` | `0.0802` | `0.0801` | `0.0802` | `0.0802` | `0.0799` | 3,513,799.11 USD | 1,857,314.90 USD | 1,656,484.22 USD | 200,830.68 USD | `+5.72%` | `2B / 5S` |
| `0:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0802` | `0.0799` | 4,173,492.18 USD | 1,857,641.00 USD | 2,315,851.18 USD | -458,210.19 USD | `-10.98%` | `2B / 1S` |
| `5:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0801` | `0.0799` | 3,085,332.02 USD | 1,558,385.55 USD | 1,526,946.46 USD | 31,439.09 USD | `+1.02%` | `2B / 2S` |
| `0:00 UTC` | `0.0802` | `0.0801` | `0.0802` | `0.0802` | `0.0799` | 592,964.00 USD | 369,913.77 USD | 223,050.23 USD | 146,863.55 USD | `+24.77%` | `2B / 5S` |

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
| `5m` | -39,440.00 USD | 467,380.00 USD | **`ACCUMULATION`** |
| `15m` | -133,270.00 USD | 335,490.00 USD | **`ACCUMULATION`** |
| `30m` | -136,160.00 USD | -15,730.00 USD | **`DISTRIBUTION`** |
| `1h` | -946,710.00 USD | -3,370,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,320,000.00 USD | -346,970.00 USD | **`DISTRIBUTION`** |
| `4h` | -271,030.00 USD | 979,090.00 USD | **`ACCUMULATION`** |
| `6h` | 1,890,000.00 USD | 2,860,000.00 USD | **`ACCUMULATION`** |
| `8h` | 2,230,000.00 USD | -907,540.00 USD | **`ACCUMULATION`** |
| `12h` | 785,000.00 USD | -9,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -982,920.00 USD | -6,940,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -39,870,000.00 USD | -122,750,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -265,870,000.00 USD | -747,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-39.44K` | 15m=`-133.27K` | 1h=`-946.71K` | 24h=`-982.92K`
* Futures Capital Netflows: 5m=`+467.38K` | 15m=`+335.49K` | 1h=`-3.37M` | 24h=`-6.94M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0806`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
