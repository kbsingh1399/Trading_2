# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 01:48:12 IST` (`2026-10-29 20:18:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0772` | **Live Ask Quote**: `0.0793` | **Mid Price**: `0.0783`
- **Spread Points**: `21.00` | **Spread BPS**: `268.37 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0778` | VWAP Z-Score: `+0.38` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000399` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.33` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0804` | Lower -3.00σ Band: `0.0751`
  * Upper +2.51σ Band: `0.0800` | Lower -2.51σ Band: `0.0755`
  * Upper +2.01σ Band: `0.0795` | Lower -2.01σ Band: `0.0760`
  * Upper +2.00σ Band: `0.0795` | Lower -2.00σ Band: `0.0760`
  * Upper +1.28σ Band: `0.0789` | Lower -1.28σ Band: `0.0766`
  * Upper +1.00σ Band: `0.0787` | Lower -1.00σ Band: `0.0769`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0782` | EMA-20=`0.0783` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0781` (Slope: `+0.0000`) | EMA-100=`0.0780`
  * Institutional Anchors: EMA-144=`0.0779` | EMA-200=`0.0777` (Slope: `+0.1010`) | EMA-233=`0.0776`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0763` | Weekly High=`0.0803` | Weekly Low=`0.0755`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0785` (Distance: `-0.29%`)
  * Point of Control (POC) = `0.0767` (Distance: `+2.10%`)
  * Value Area Low (VAL) = `0.0764` (Distance: `+2.50%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `0.0779` - `0.0786`
  * Optimal Trade Entry (OTE 0.705): `0.0784`
  * Structural Invalidation Anchor (0.786): `0.0789`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0792` | `0.0793` | `0.0781` | `0.0782` | `153,794,337` | 12,096,805.13 USD | -4,116,345.32 USD | `-34.03%` | -16,364,101.15 USD | `-4.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0781` | `0.0785` | `0.0779` | `0.0782` | `108,961,799` | 8,510,856.68 USD | 60,626.20 USD | `+0.71%` | -16,303,474.95 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.0782` | `0.0785` | `0.0780` | `0.0784` | `36,987,596` | 2,894,790.13 USD | 646,066.64 USD | `+22.32%` | -15,657,408.31 USD | `+0.79` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0791` | `0.0795` | `0.0791` | `0.0793` | `28,030,884` | 2,224,641.24 USD | 777,452.89 USD | `+34.95%` | -11,990,953.63 USD | `+1.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0793` | `0.0795` | `0.0792` | `0.0793` | `23,465,006` | 1,861,645.62 USD | -256,802.19 USD | `-13.79%` | -12,247,755.82 USD | `-0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0792` | `0.0793` | `0.0779` | `0.0784` | `299,759,777` | 23,503,709.39 USD | -3,408,395.04 USD | `-14.50%` | -15,656,150.86 USD | `-3.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0796` | `0.0797` | `0.0789` | `0.0793` | `184,672,867` | 14,645,934.56 USD | 790,590.21 USD | `+5.40%` | -12,311,241.21 USD | `+0.90` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.0793` | `0.0795` | `0.0790` | `0.0793` | `99,331,512` | 7,872,201.47 USD | -219,088.96 USD | `-2.78%` | -12,530,330.17 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0792` | `0.0793` | `0.0779` | `0.0784` | `299,759,777` | 23,503,709.39 USD | -3,408,395.04 USD | `-14.50%` | -15,938,725.21 USD | `-1.53` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0779` | `0.0784` | `299,770,528` | 23,504,552.06 USD | -3,407,552.37 USD | `-14.50%` | -16,232,977.88 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -11,383,503.61 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -14,406,508.13 USD | `+1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0779` | `0.0784` | `299,770,528` | 23,504,552.06 USD | -3,407,552.37 USD | `-14.50%` | -16,232,977.88 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0783`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0783` | `89339.0000` | 6,999.62 USD | 94,881.15 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0783` | `15071.0000` | 1,180.77 USD | 96,061.92 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0783` | `144390.0000` | 11,312.38 USD | 107,374.30 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0783` | `3888.0000` | 304.60 USD | 107,678.90 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0783` | `435789.0000` | 34,139.71 USD | 141,818.61 USD | `1 orders` | `-0.05%` | `-` |
| `ASK` | `0.0784` | `111061.0000` | 8,707.74 USD | 201,644.11 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `1034.0000` | 81.07 USD | 192,936.37 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `145914.0000` | 11,439.95 USD | 192,855.30 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `546136.0000` | 42,817.61 USD | 181,415.35 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `40007.0000` | 3,136.55 USD | 138,597.74 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `534430.0000` | 41,898.78 USD | 135,461.20 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `35536.0000` | 2,785.95 USD | 93,562.42 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0784` | `19131.0000` | 1,499.81 USD | 90,776.47 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `141126.0000` | 11,063.71 USD | 89,276.65 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `413768.0000` | 32,437.34 USD | 78,212.94 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `37877.0000` | 2,969.33 USD | 45,775.60 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `80028.0000` | 6,273.64 USD | 42,806.27 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `19134.0000` | 1,499.95 USD | 36,532.63 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `152363.0000` | 11,943.89 USD | 35,032.68 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `19134.0000` | 1,499.91 USD | 23,088.79 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0784` | `111061.0000` | 8,705.96 USD | 21,588.88 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0784` | `45826.0000` | 3,592.21 USD | 12,882.92 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0784` | `59092.0000` | 4,632.04 USD | 9,290.71 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0784` | `7494.0000` | 587.42 USD | 4,658.66 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0784` | `51941.0000` | 4,071.24 USD | 4,071.24 USD | `2 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.0784` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0784` | `44946.0000` | 3,522.60 USD | 3,522.60 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0784` | `121946.0000` | 9,557.27 USD | 13,079.87 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0784` | `5104.0000` | 400.01 USD | 13,479.88 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0784` | `44796.0000` | 3,510.66 USD | 16,990.54 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0784` | `1034.0000` | 81.03 USD | 17,071.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0784` | `44800.0000` | 3,510.71 USD | 20,582.28 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0784` | `15071.0000` | 1,181.01 USD | 21,763.29 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0784` | `15070.0000` | 1,180.92 USD | 22,944.21 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0784` | `5105.0000` | 400.03 USD | 23,344.23 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0784` | `4758.0000` | 372.83 USD | 23,717.06 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0784` | `15070.0000` | 1,180.82 USD | 24,897.89 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0784` | `5105.0000` | 400.00 USD | 25,297.89 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0784` | `132679.0000` | 10,395.93 USD | 35,693.82 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0784` | `31990.0000` | 2,506.51 USD | 38,200.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0784` | `634077.0000` | 49,681.20 USD | 87,881.53 USD | `2 orders` | `-0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `305` | `0xb83d...6e36` | `SHORT` | 8,040,768.53 USD | `102,645,925.00` | `0.0946` | `0.0785` | `1.35` | 1,666,573.12 USD | `+20.73%` | `3X Cross` |
| `317` | `0xc63a...a3cd` | `LONG` | 7,839,400.00 USD | `100,000,000.00` | `0.0856` | `0.0785` | `0.000000` | -725,421.96 USD | `-9.25%` | `10X Cross` |
| `318` | `0x610b...b613` | `LONG` | 7,731,796.98 USD | `98,666,424.00` | `0.0872` | `0.0785` | `0.0592` | -868,384.92 USD | `-11.23%` | `5X Cross` |
| `597` | `0x5b5d...c060` | `SHORT` | 3,883,108.39 USD | `49,478,955.00` | `0.0946` | `0.0785` | `3.21` | 798,408.22 USD | `+20.56%` | `3X Cross` |
| `633` | `0xca49...53c8` | `SHORT` | 3,653,225.61 USD | `46,542,649.00` | `0.0929` | `0.0785` | `0.3578` | 672,819.07 USD | `+18.42%` | `10X Cross` |
| `642` | `0x45d2...4029` | `SHORT` | 3,564,214.81 USD | `45,426,000.00` | `0.0954` | `0.0785` | `0.8768` | 771,414.41 USD | `+21.64%` | `10X Cross` |
| `793` | `0xecb6...2b00` | `SHORT` | 2,911,971.19 USD | `37,113,140.00` | `0.0796` | `0.0785` | `0.8070` | 41,654.86 USD | `+1.43%` | `10X Cross` |
| `1189` | `0x458d...ab3b` | `LONG` | 1,915,780.20 USD | `24,454,063.00` | `0.1002` | `0.0785` | `0.0714` | -535,141.70 USD | `-27.93%` | `3X Isolated` |
| `1194` | `0xeadc...9d55` | `LONG` | 1,904,177.14 USD | `24,317,440.00` | `0.0926` | `0.0785` | `0.000000` | -347,417.43 USD | `-18.25%` | `10X Cross` |
| `1239` | `0x9aa5...58af` | `SHORT` | 1,840,817.67 USD | `23,500,500.00` | `0.0907` | `0.0785` | `0.4089` | 289,937.29 USD | `+15.75%` | `10X Cross` |
| `1336` | `0xf48f...10fe` | `LONG` | 1,679,252.07 USD | `21,424,497.00` | `0.0968` | `0.0785` | `0.0386` | -395,052.53 USD | `-23.53%` | `4X Cross` |
| `1378` | `0x9946...0852` | `SHORT` | 1,641,028.49 USD | `20,910,149.00` | `0.0871` | `0.0785` | `0.1362` | 179,526.90 USD | `+10.94%` | `10X Cross` |
| `1563` | `0xcac1...26b3` | `SHORT` | 1,420,726.95 USD | `18,126,835.00` | `0.0943` | `0.0785` | `0.5155` | 288,732.25 USD | `+20.32%` | `10X Cross` |
| `1607` | `0x0d6a...ca57` | `LONG` | 1,381,120.88 USD | `17,626,455.00` | `0.0875` | `0.0785` | `0.0626` | -160,984.08 USD | `-11.66%` | `3X Isolated` |
| `1647` | `0x4808...a82c` | `LONG` | 1,318,030.64 USD | `16,828,143.00` | `0.0883` | `0.0785` | `0.0632` | -168,442.34 USD | `-12.78%` | `3X Cross` |
| `1774` | `0x31ef...f715` | `LONG` | 1,192,897.74 USD | `15,230,102.00` | `0.0936` | `0.0785` | `0.0668` | -232,798.19 USD | `-19.52%` | `3X Isolated` |
| `1791` | `0xbfc7...80b4` | `SHORT` | 1,176,531.62 USD | `15,020,000.00` | `0.0920` | `0.0785` | `0.3883` | 205,867.67 USD | `+17.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 9,558.66 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0786 USD [API] | `2026-10-27 22:43:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0788` | 9,914.73 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.91K USD at 0.0788 USD [API] | `2026-10-27 23:22:55` |
| `ANNOUNCEMENT` | `INFO` | `0.0788` | 9,558.53 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0788 USD [API] | `2026-10-27 23:22:55` |
| `ANNOUNCEMENT` | `INFO` | `0.0788` | 7,000.06 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.00K USD at 0.0788 USD [API] | `2026-10-27 23:22:55` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0826` (Vol: 395,700.00 USD, Dist: `+4.14%`) | Long MP=`0.0767` (Vol: 519,500.00 USD, Dist: `--3.34%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 478,200.00 USD, Dist: `+3.53%`) | Long MP=`0.0774` (Vol: 691,800.00 USD, Dist: `--2.47%`)
  * 3D Horizon: Short MP=`0.0823` (Vol: 539,400.00 USD, Dist: `+3.74%`) | Long MP=`0.0765` (Vol: 660,700.00 USD, Dist: `--3.52%`)
  * 7D Horizon: Short MP=`0.0821` (Vol: 746,800.00 USD, Dist: `+3.55%`) | Long MP=`0.0762` (Vol: 988,700.00 USD, Dist: `--3.92%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0162` | 184.97 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0182` | 115.60 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0187` | 323.68 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0192` | 16,860.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0203` | 125.67 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0210` | 295.48 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 429.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0222` | 1,680.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 345.98 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0238` | 4,960.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0239` | 620.21 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0242` | 11,860.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 140.28 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0266` | 457.30 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0270` | 6,050.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 1,060.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 603.02 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 2,200.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 3,850.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0288` | 2,180.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0299` | 162.15 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 2,360.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0303` | 4,080.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 149.22 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0333` | 199.13 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 3,290.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 740,220.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 50,680.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 4,310.00 USD | 15,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 194.97 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 28,950.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0374` | 3,370.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0376` | 3,800.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 1,010.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 101,840.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 1,070.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0398` | 2,710.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 11,450.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0411` | 1,030.00 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 252.72 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 4,590.00 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 59,650.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 88,980.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 3,190.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,010.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 6,430.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 2,490.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 402.70 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 2,360.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 15,280.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,010.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,500.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 323.28 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0502` | 384.95 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,330.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 314.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 662.73 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 1,200.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 297.41 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 3,990.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 395.09 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,360.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,690.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 61,750.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 336.86 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 314,750.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 291.27 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 237.95 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 892.81 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 770.89 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 1,610.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 101.07 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 772.62 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 1,010.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 567.50 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 1,040.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 825.82 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 7,260.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 10,530.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 392.08 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 5,780,000.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 889.30 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,660.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,650.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 2,830.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 11,540.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,280.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 2,160.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,990.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 17,630.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0611` | 11,810.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,400.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 13,830.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 1,820.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 3,470.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 168.28 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 10,410.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 233.80 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 32,880.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 8,670.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,360.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,050.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 3,520.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 87,470.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 9,910.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0650` | 885.98 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 34,430.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 22,620.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 71,100.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 339.48 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,600.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 66,830.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 4,860.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 389.18 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,180.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 196.64 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,530.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 2,070.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 5,100.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0682` | 4,720.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 4,690.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 1,410.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 69,020.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 517.48 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 86,650.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 52,390.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 96,110.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0696` | 15,100.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,420.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 22,240,000.00 USD | 22,240,000.00 USD | 136,180.00 USD | 82,620.00 USD | 55,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 21,960,000.00 USD | 21,960,000.00 USD | 35,400.00 USD | 18,030.00 USD | 27,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 21,880,000.00 USD | 21,880,000.00 USD | 71,010.00 USD | 36,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 2,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 21,770,000.00 USD | 21,770,000.00 USD | 81,610.00 USD | 20,870.00 USD | 40,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 21,630,000.00 USD | 21,630,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 21,540,000.00 USD | 21,540,000.00 USD | 19,150.00 USD | 0.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0706` | 93,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0706` | 21,490,000.00 USD | 21,490,000.00 USD | 29,320.00 USD | 29,080.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0707` | 21,420,000.00 USD | 21,420,000.00 USD | 50,420.00 USD | 21,680.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 21,330,000.00 USD | 21,330,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 21,260,000.00 USD | 21,260,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0710` | 21,180,000.00 USD | 21,180,000.00 USD | 8,080.00 USD | 9,300.00 USD | 34,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0711` | 21,130,000.00 USD | 21,130,000.00 USD | 16,230.00 USD | 8,560.00 USD | 42,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0712` | 21,060,000.00 USD | 21,060,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 21,000,000.00 USD | 21,000,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 20,840,000.00 USD | 20,840,000.00 USD | 32,300.00 USD | 42,090.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 762,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 20,760,000.00 USD | 20,760,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 10,330.00 USD | 760,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 20,700,000.00 USD | 20,700,000.00 USD | 30,130.00 USD | 31,610.00 USD | 464.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 560.88 USD | 750,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 20,640,000.00 USD | 20,640,000.00 USD | 15,510.00 USD | 7,710.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 749,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 20,590,000.00 USD | 20,590,000.00 USD | 63,040.00 USD | 36,880.00 USD | 50,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 748,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 20,440,000.00 USD | 20,440,000.00 USD | 15,840.00 USD | 2,950.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 737,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 20,410,000.00 USD | 20,410,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 736,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 20,320,000.00 USD | 20,320,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0722` | 20,250,000.00 USD | 20,250,000.00 USD | 23,760.00 USD | 15,630.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 5,720.00 USD | 712,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 20,190,000.00 USD | 20,190,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 6,110.00 USD | 706,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 20,080,000.00 USD | 20,080,000.00 USD | 31,180.00 USD | 17,780.00 USD | 73,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 598.51 USD | 700,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 19,960,000.00 USD | 19,960,000.00 USD | 47,840.00 USD | 22,980.00 USD | 23,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 700,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 19,860,000.00 USD | 19,860,000.00 USD | 30,810.00 USD | 0.00 USD | 73.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 700,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 19,830,000.00 USD | 19,830,000.00 USD | 20,420.00 USD | 0.00 USD | 239.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 3,170.00 USD | 699,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 19,810,000.00 USD | 19,810,000.00 USD | 15,580.00 USD | 802.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 695,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 19,790,000.00 USD | 19,790,000.00 USD | 17,820.00 USD | 0.00 USD | 19,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 695,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 19,760,000.00 USD | 19,760,000.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 622,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 19,740,000.00 USD | 19,740,000.00 USD | 42,980.00 USD | 0.00 USD | 170.86 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 612,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 19,700,000.00 USD | 19,700,000.00 USD | 42,110.00 USD | 0.00 USD | 184.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 610,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 19,660,000.00 USD | 19,660,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 19,650,000.00 USD | 19,650,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 604,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 19,640,000.00 USD | 19,640,000.00 USD | 24,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 597,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 19,620,000.00 USD | 19,620,000.00 USD | 8,600.00 USD | 0.00 USD | 42.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 593,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 19,610,000.00 USD | 19,610,000.00 USD | 48,230.00 USD | 0.00 USD | 385.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 588,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 19,560,000.00 USD | 19,560,000.00 USD | 31,820.00 USD | 0.00 USD | 94.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,430.00 USD | 577,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 19,530,000.00 USD | 19,530,000.00 USD | 33,680.00 USD | 0.00 USD | 183.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,770.00 USD | 572,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 19,490,000.00 USD | 19,490,000.00 USD | 33,740.00 USD | 0.00 USD | 328.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,270.00 USD | 558,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 19,460,000.00 USD | 19,460,000.00 USD | 31,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 777.39 USD | 103,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 19,430,000.00 USD | 19,430,000.00 USD | 25,930.00 USD | 0.00 USD | 585.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 102,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 19,400,000.00 USD | 19,400,000.00 USD | 28,250.00 USD | 27,500.00 USD | 742.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 2,140.00 USD | 101,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 19,350,000.00 USD | 19,350,000.00 USD | 41,210.00 USD | 1,840.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,040.00 USD | 99,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 19,290,000.00 USD | 19,290,000.00 USD | 106,370.00 USD | 57,220.00 USD | 25,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,420.00 USD | 97,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 19,100,000.00 USD | 19,100,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 95,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0747` | 18,560,000.00 USD | 18,560,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 94,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 18,100,000.00 USD | 18,100,000.00 USD | 169,810.00 USD | 65,720.00 USD | 99,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 17,770,000.00 USD | 17,770,000.00 USD | 261,140.00 USD | 144,960.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 8,550.00 USD | 94,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 17,350,000.00 USD | 17,350,000.00 USD | 263,060.00 USD | 83,730.00 USD | 121,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 13,430.00 USD | 85,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0751` | 16,880,000.00 USD | 16,880,000.00 USD | 268,200.00 USD | 82,120.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 1,480.00 USD | 72,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 16,470,000.00 USD | 16,470,000.00 USD | 119,250.00 USD | 31,840.00 USD | 85,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 11,190.00 USD | 70,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0753` | 16,230,000.00 USD | 16,230,000.00 USD | 132,060.00 USD | 72,710.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0754` | 16,000,000.00 USD | 16,000,000.00 USD | 87,330.00 USD | 62,330.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 59,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0755` | 15,830,000.00 USD | 15,830,000.00 USD | 109,960.00 USD | 16,530.00 USD | 68,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 977.84 USD | 55,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0756` | 15,630,000.00 USD | 15,630,000.00 USD | 164,890.00 USD | 147,310.00 USD | 130,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 516.61 USD | 54,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0757` | 15,190,000.00 USD | 15,190,000.00 USD | 88,960.00 USD | 44,210.00 USD | 104,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0757` | 3,270.00 USD | 53,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0758` | 14,950,000.00 USD | 14,950,000.00 USD | 70,320.00 USD | 31,960.00 USD | 105,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,070.00 USD | 50,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0759` | 14,750,000.00 USD | 14,750,000.00 USD | 195,880.00 USD | 130,420.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,080.00 USD | 45,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 14,410,000.00 USD | 14,410,000.00 USD | 237,110.00 USD | 313,670.00 USD | 277,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,260.00 USD | 13,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0761` | 13,580,000.00 USD | 13,580,000.00 USD | 500,630.00 USD | 463,290.00 USD | 278,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 623.52 USD | 12,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 12,340,000.00 USD | 12,340,000.00 USD | 579,620.00 USD | 303,280.00 USD | 223,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 181.93 USD | 11,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0763` | 11,230,000.00 USD | 11,230,000.00 USD | 305,000.00 USD | 179,660.00 USD | 196,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0764` | 11,510.00 USD | 11,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0764` | 10,550,000.00 USD | 10,550,000.00 USD | 488,440.00 USD | 327,090.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0765` | 9,710,000.00 USD | 9,710,000.00 USD | 558,950.00 USD | 213,120.00 USD | 314,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0766` | 8,630,000.00 USD | 8,630,000.00 USD | 621,080.00 USD | 262,670.00 USD | 279,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0767` | 7,460,000.00 USD | 7,460,000.00 USD | 228,110.00 USD | 101,120.00 USD | 213,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0768` | 6,920,000.00 USD | 6,920,000.00 USD | 426,850.00 USD | 236,860.00 USD | 141,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0769` | 6,110,000.00 USD | 6,110,000.00 USD | 219,090.00 USD | 193,080.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0770` | 5,630,000.00 USD | 5,630,000.00 USD | 281,930.00 USD | 93,610.00 USD | 254,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0771` | 5,000,000.00 USD | 5,000,000.00 USD | 231,550.00 USD | 266,030.00 USD | 226,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0772` | 4,280,000.00 USD | 4,280,000.00 USD | 145,880.00 USD | 296,720.00 USD | 307,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0773` | 3,530,000.00 USD | 3,530,000.00 USD | 185,470.00 USD | 106,120.00 USD | 241,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0774` | 3,000,000.00 USD | 3,000,000.00 USD | 143,850.00 USD | 97,350.00 USD | 235,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0775` | 2,520,000.00 USD | 2,520,000.00 USD | 357,290.00 USD | 150,850.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0776` | 1,990,000.00 USD | 1,990,000.00 USD | 137,380.00 USD | 345,400.00 USD | 381,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0777` | 1,130,000.00 USD | 1,130,000.00 USD | 74,870.00 USD | 226,950.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0778` | 814,730.00 USD | 814,730.00 USD | 148,860.00 USD | 120,190.00 USD | 200,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0779` | 345,330.00 USD | 345,330.00 USD | 0.00 USD | 85,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0780` | 259,380.00 USD | 259,380.00 USD | 0.00 USD | 88,770.00 USD | 211.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0781` | 170,400.00 USD | 170,400.00 USD | 0.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0782` | 136,860.00 USD | 136,860.00 USD | 0.00 USD | 4,420.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0783` | 47,310.00 USD | 47,310.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 430,270.00 USD | 430,270.00 USD | 265,800.00 USD | 6,130.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 860,550.00 USD | 860,550.00 USD | 265,800.00 USD | 6,130.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 1,200,000.00 USD | 1,200,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 1,720,000.00 USD | 1,720,000.00 USD | 170,030.00 USD | 117,040.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 2,180,000.00 USD | 2,180,000.00 USD | 150,580.00 USD | 307,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0788` | 2,310,000.00 USD | 2,310,000.00 USD | 36,540.00 USD | 96,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 2,480,000.00 USD | 2,480,000.00 USD | 127,940.00 USD | 35,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 2,630,000.00 USD | 2,630,000.00 USD | 133,970.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 3,090,000.00 USD | 3,090,000.00 USD | 185,120.00 USD | 33,340.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 3,620,000.00 USD | 3,620,000.00 USD | 169,980.00 USD | 26,520.00 USD | 171,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 3,870,000.00 USD | 3,870,000.00 USD | 3,520.00 USD | 0.00 USD | 190,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 4,310,000.00 USD | 4,310,000.00 USD | 200,420.00 USD | 208,070.00 USD | 40,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 5,380,000.00 USD | 5,380,000.00 USD | 411,890.00 USD | 131,030.00 USD | 522,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 6,170,000.00 USD | 6,170,000.00 USD | 445,800.00 USD | 336,610.00 USD | 12,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 6,780,000.00 USD | 6,780,000.00 USD | 293,220.00 USD | 180,540.00 USD | 132,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 7,090,000.00 USD | 7,090,000.00 USD | 66,980.00 USD | 241,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 7,430,000.00 USD | 7,430,000.00 USD | 124,600.00 USD | 75,260.00 USD | 135,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 7,680,000.00 USD | 7,680,000.00 USD | 27,080.00 USD | 18,240.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0814` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0814` | 8,110,000.00 USD | 8,110,000.00 USD | 22,430.00 USD | 23,100.00 USD | 386,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 8,600,000.00 USD | 8,600,000.00 USD | 232,650.00 USD | 147,560.00 USD | 112,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 9,480,000.00 USD | 9,480,000.00 USD | 441,880.00 USD | 245,220.00 USD | 189,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 10,110,000.00 USD | 10,110,000.00 USD | 344,470.00 USD | 153,360.00 USD | 130,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 10,850,000.00 USD | 10,850,000.00 USD | 269,340.00 USD | 161,880.00 USD | 308,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 11,540,000.00 USD | 11,540,000.00 USD | 171,350.00 USD | 368,950.00 USD | 156,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 12,440,000.00 USD | 12,440,000.00 USD | 173,080.00 USD | 273,830.00 USD | 448,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 12,900,000.00 USD | 12,900,000.00 USD | 208,520.00 USD | 79,630.00 USD | 170,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 13,480,000.00 USD | 13,480,000.00 USD | 260,030.00 USD | 169,200.00 USD | 156,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 13,830,000.00 USD | 13,830,000.00 USD | 264,720.00 USD | 75,420.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 14,410,000.00 USD | 14,410,000.00 USD | 148,810.00 USD | 226,510.00 USD | 198,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 14,680,000.00 USD | 14,680,000.00 USD | 124,920.00 USD | 116,480.00 USD | 27,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 15,030,000.00 USD | 15,030,000.00 USD | 102,880.00 USD | 60,100.00 USD | 190,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 15,130,000.00 USD | 15,130,000.00 USD | 52,670.00 USD | 48,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 15,400,000.00 USD | 15,400,000.00 USD | 224,210.00 USD | 37,180.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 263.55 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0829` | 15,760,000.00 USD | 15,760,000.00 USD | 206,610.00 USD | 79,000.00 USD | 72,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0829` | 651.07 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0830` | 16,270,000.00 USD | 16,270,000.00 USD | 262,060.00 USD | 98,430.00 USD | 150,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 16,450,000.00 USD | 16,450,000.00 USD | 97,970.00 USD | 37,430.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 14,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 16,860,000.00 USD | 16,860,000.00 USD | 234,780.00 USD | 91,440.00 USD | 85,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 17,110,000.00 USD | 17,110,000.00 USD | 151,330.00 USD | 68,410.00 USD | 31,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 150.95 USD | 14,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0834` | 17,420,000.00 USD | 17,420,000.00 USD | 132,090.00 USD | 60,550.00 USD | 117,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 17,790,000.00 USD | 17,790,000.00 USD | 110,610.00 USD | 184,470.00 USD | 78,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0835` | 13,550.00 USD | 27,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0836` | 18,120,000.00 USD | 18,120,000.00 USD | 47,660.00 USD | 83,650.00 USD | 197,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 28,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 18,280,000.00 USD | 18,280,000.00 USD | 101,560.00 USD | 17,710.00 USD | 34,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 29,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 18,520,000.00 USD | 18,520,000.00 USD | 145,530.00 USD | 68,620.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 18,580,000.00 USD | 18,580,000.00 USD | 65,490.00 USD | 0.00 USD | 667.96 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 29,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 18,630,000.00 USD | 18,630,000.00 USD | 35,250.00 USD | 15,480.00 USD | 555.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0840` | 4,710.00 USD | 34,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0841` | 18,670,000.00 USD | 18,670,000.00 USD | 32,120.00 USD | 2,010.00 USD | 577.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 18,750,000.00 USD | 18,750,000.00 USD | 30,040.00 USD | 0.00 USD | 46,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 34,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 18,780,000.00 USD | 18,780,000.00 USD | 37,310.00 USD | 0.00 USD | 359.38 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 18,860,000.00 USD | 18,860,000.00 USD | 79,050.00 USD | 0.00 USD | 160.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 18,880,000.00 USD | 18,880,000.00 USD | 16,770.00 USD | 0.00 USD | 494.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 18,970,000.00 USD | 18,970,000.00 USD | 72,340.00 USD | 16,670.00 USD | 220.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 34,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 18,980,000.00 USD | 18,980,000.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 18,990,000.00 USD | 18,990,000.00 USD | 11,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0849` | 19,000,000.00 USD | 19,000,000.00 USD | 6,070.00 USD | 0.00 USD | 742.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 19,020,000.00 USD | 19,020,000.00 USD | 20,730.00 USD | 0.00 USD | 155.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 34,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0851` | 19,060,000.00 USD | 19,060,000.00 USD | 26,040.00 USD | 11,000.00 USD | 92.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 19,070,000.00 USD | 19,070,000.00 USD | 12,910.00 USD | 737.47 USD | 500.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 19,130,000.00 USD | 19,130,000.00 USD | 35,960.00 USD | 13,190.00 USD | 10,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0855` | 19,280,000.00 USD | 19,280,000.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 19,420,000.00 USD | 19,420,000.00 USD | 92,490.00 USD | 32,810.00 USD | 20,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0857` | 19,520,000.00 USD | 19,520,000.00 USD | 50,540.00 USD | 18,030.00 USD | 27,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 19,630,000.00 USD | 19,630,000.00 USD | 73,450.00 USD | 36,780.00 USD | 120.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 35,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0859` | 19,770,000.00 USD | 19,770,000.00 USD | 84,540.00 USD | 20,870.00 USD | 40,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0859` | 135.37 USD | 35,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0860` | 19,860,000.00 USD | 19,860,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0861` | 19,910,000.00 USD | 19,910,000.00 USD | 19,150.00 USD | 0.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 216.58 USD | 35,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0862` | 19,990,000.00 USD | 19,990,000.00 USD | 33,780.00 USD | 29,080.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 37,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0864` | 20,030,000.00 USD | 20,030,000.00 USD | 22,510.00 USD | 20,050.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0865` | 20,090,000.00 USD | 20,090,000.00 USD | 31,770.00 USD | 1,640.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 20,150,000.00 USD | 20,150,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0867` | 20,230,000.00 USD | 20,230,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 20,280,000.00 USD | 20,280,000.00 USD | 8,080.00 USD | 9,300.00 USD | 34,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0869` | 20,350,000.00 USD | 20,350,000.00 USD | 16,230.00 USD | 8,560.00 USD | 42,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 20,410,000.00 USD | 20,410,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0871` | 20,570,000.00 USD | 20,570,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 20,650,000.00 USD | 20,650,000.00 USD | 32,300.00 USD | 42,090.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0873` | 20,720,000.00 USD | 20,720,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0875` | 20,740,000.00 USD | 20,740,000.00 USD | 9,700.00 USD | 17,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0876` | 20,780,000.00 USD | 20,780,000.00 USD | 20,430.00 USD | 14,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0877` | 9,630.00 USD | 47,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0877` | 20,820,000.00 USD | 20,820,000.00 USD | 15,510.00 USD | 7,710.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0878` | 20,960,000.00 USD | 20,960,000.00 USD | 54,680.00 USD | 34,920.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 47,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 48,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0891` | 106.09 USD | 48,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 49,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0896` | 3,460.00 USD | 52,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 52,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 361.53 USD | 53,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 882.57 USD | 54,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0909` | 4,090.00 USD | 58,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0910` | 114.23 USD | 58,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 743.15 USD | 58,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0914` | 171.19 USD | 63,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0917` | 344.43 USD | 63,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 63,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0924` | 187.93 USD | 63,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0935` | 3,300.00 USD | 67,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0949` | 573.84 USD | 67,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 13,800.00 USD | 81,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0951` | 114,180.00 USD | 195,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 747.55 USD | 196,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 197,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0963` | 48,120.00 USD | 245,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 39,190.00 USD | 284,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 284,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 10,510.00 USD | 295,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1002` | 1,290.00 USD | 296,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1012` | 1,010.00 USD | 297,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1013` | 177.90 USD | 297,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 305,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 308,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 308,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1041` | 1,020.00 USD | 309,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 316,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1072` | 3,210.00 USD | 319,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,370.00 USD | 322,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1114` | 1,500.00 USD | 324,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1121` | 2,290.00 USD | 326,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 326,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 326,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 106.19 USD | 326,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1215` | 353.91 USD | 327,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 328,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1265` | 379.65 USD | 328,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 328,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1278` | 1,540.00 USD | 330,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 330,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 332,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 332,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1323` | 2,770,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1384` | 2,210.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1389` | 1,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,800.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1419` | 23,020.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1437` | 678.93 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,320.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1480` | 391.74 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1510` | 56,520.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 2,010.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 267.55 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 195.39 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 194.45 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1563` | 340.06 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 4,830.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 980.15 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 16,000,000.00 USD | 0.00 USD | 3,930.00 USD | `-79.75%` | `244,573.00` |
| `Live` | `Long` | `0.0162` | 15,990,000.00 USD | 0.00 USD | 184.97 USD | `-79.63%` | `11,453.00` |
| `Live` | `Long` | `0.0164` | 15,990,000.00 USD | 0.00 USD | 407.02 USD | `-79.25%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 15,990,000.00 USD | 0.00 USD | 5,290.00 USD | `-79.12%` | `319,394.00` |
| `Live` | `Long` | `0.0182` | 15,990,000.00 USD | 0.00 USD | 115.60 USD | `-76.98%` | `6,334.00` |
| `Live` | `Long` | `0.0187` | 15,990,000.00 USD | 0.00 USD | 323.68 USD | `-76.35%` | `17,263.00` |
| `Live` | `Long` | `0.0192` | 15,990,000.00 USD | 0.00 USD | 16,860.00 USD | `-75.84%` | `880,408.00` |
| `Live` | `Long` | `0.0203` | 15,970,000.00 USD | 0.00 USD | 125.67 USD | `-74.45%` | `6,206.00` |
| `Live` | `Long` | `0.0210` | 15,970,000.00 USD | 0.00 USD | 295.48 USD | `-73.44%` | `14,037.00` |
| `Live` | `Long` | `0.0215` | 15,970,000.00 USD | 0.00 USD | 429.00 USD | `-72.94%` | `20,000.00` |
| `Live` | `Long` | `0.0222` | 15,970,000.00 USD | 0.00 USD | 1,680.00 USD | `-71.93%` | `75,389.00` |
| `Live` | `Long` | `0.0232` | 15,970,000.00 USD | 0.00 USD | 345.98 USD | `-70.67%` | `14,881.00` |
| `Live` | `Long` | `0.0238` | 15,970,000.00 USD | 0.00 USD | 4,960.00 USD | `-69.91%` | `207,979.00` |
| `Live` | `Long` | `0.0239` | 15,960,000.00 USD | 0.00 USD | 620.21 USD | `-69.79%` | `25,896.00` |
| `Live` | `Long` | `0.0242` | 15,960,000.00 USD | 0.00 USD | 11,860.00 USD | `-69.53%` | `491,018.00` |
| `Live` | `Long` | `0.0262` | 15,950,000.00 USD | 0.00 USD | 140.28 USD | `-66.88%` | `5,344.00` |
| `Live` | `Long` | `0.0266` | 15,950,000.00 USD | 0.00 USD | 457.30 USD | `-66.51%` | `17,224.00` |
| `Live` | `Long` | `0.0270` | 15,950,000.00 USD | 0.00 USD | 6,050.00 USD | `-66.00%` | `224,650.00` |
| `Live` | `Long` | `0.0272` | 15,940,000.00 USD | 0.00 USD | 1,060.00 USD | `-65.75%` | `39,049.00` |
| `Live` | `Long` | `0.0272` | 15,940,000.00 USD | 0.00 USD | 603.02 USD | `-65.62%` | `22,129.00` |
| `Live` | `Long` | `0.0276` | 15,940,000.00 USD | 0.00 USD | 2,200.00 USD | `-65.24%` | `80,000.00` |
| `Live` | `Long` | `0.0279` | 15,940,000.00 USD | 0.00 USD | 1,730.00 USD | `-64.74%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 15,940,000.00 USD | 0.00 USD | 3,850.00 USD | `-64.11%` | `135,346.00` |
| `Live` | `Long` | `0.0288` | 15,930,000.00 USD | 0.00 USD | 2,180.00 USD | `-63.73%` | `75,693.00` |
| `Live` | `Long` | `0.0299` | 15,930,000.00 USD | 0.00 USD | 162.15 USD | `-62.34%` | `5,432.00` |
| `Live` | `Long` | `0.0301` | 15,930,000.00 USD | 0.00 USD | 2,360.00 USD | `-61.96%` | `78,319.00` |
| `Live` | `Long` | `0.0303` | 15,930,000.00 USD | 0.00 USD | 4,080.00 USD | `-61.71%` | `134,443.00` |
| `Live` | `Long` | `0.0306` | 15,920,000.00 USD | 0.00 USD | 137.41 USD | `-61.46%` | `4,498.00` |
| `Live` | `Long` | `0.0331` | 15,920,000.00 USD | 0.00 USD | 149.22 USD | `-58.31%` | `4,515.00` |
| `Live` | `Long` | `0.0333` | 15,920,000.00 USD | 0.00 USD | 199.13 USD | `-58.05%` | `5,989.00` |
| `Live` | `Long` | `0.0338` | 15,920,000.00 USD | 0.00 USD | 3,290.00 USD | `-57.42%` | `97,501.00` |
| `Live` | `Long` | `0.0345` | 15,920,000.00 USD | 0.00 USD | 740,220.00 USD | `-56.41%` | `21,424,497.00` |
| `Live` | `Long` | `0.0350` | 15,180,000.00 USD | 0.00 USD | 50,680.00 USD | `-55.91%` | `1,450,000.00` |
| `Live` | `Long` | `0.0352` | 15,130,000.00 USD | 0.00 USD | 4,310.00 USD | `-55.53%` | `122,306.00` |
| `Live` | `Long` | `0.0358` | 15,120,000.00 USD | 0.00 USD | 214.53 USD | `-54.77%` | `5,984.00` |
| `Live` | `Long` | `0.0365` | 15,120,000.00 USD | 0.00 USD | 194.97 USD | `-54.02%` | `5,349.00` |
| `Live` | `Long` | `0.0372` | 15,120,000.00 USD | 0.00 USD | 28,950.00 USD | `-53.01%` | `777,061.00` |
| `Live` | `Long` | `0.0374` | 15,100,000.00 USD | 0.00 USD | 3,370.00 USD | `-52.75%` | `90,000.00` |
| `Live` | `Long` | `0.0376` | 15,090,000.00 USD | 0.00 USD | 3,800.00 USD | `-52.63%` | `101,126.00` |
| `Live` | `Long` | `0.0381` | 15,090,000.00 USD | 0.00 USD | 246.45 USD | `-52.00%` | `6,477.00` |
| `Live` | `Long` | `0.0386` | 15,090,000.00 USD | 0.00 USD | 121.74 USD | `-51.37%` | `3,158.00` |
| `Live` | `Long` | `0.0391` | 15,090,000.00 USD | 0.00 USD | 1,010.00 USD | `-50.61%` | `25,729.00` |
| `Live` | `Long` | `0.0393` | 15,090,000.00 USD | 0.00 USD | 101,840.00 USD | `-50.48%` | `2,594,745.00` |
| `Live` | `Long` | `0.0396` | 14,990,000.00 USD | 0.00 USD | 1,070.00 USD | `-49.98%` | `26,900.00` |
| `Live` | `Long` | `0.0398` | 14,980,000.00 USD | 0.00 USD | 2,710.00 USD | `-49.85%` | `68,212.00` |
| `Live` | `Long` | `0.0404` | 14,980,000.00 USD | 0.00 USD | 115.12 USD | `-48.97%` | `2,846.00` |
| `Live` | `Long` | `0.0406` | 14,980,000.00 USD | 0.00 USD | 11,450.00 USD | `-48.72%` | `281,570.00` |
| `Live` | `Long` | `0.0408` | 14,970,000.00 USD | 0.00 USD | 419.28 USD | `-48.59%` | `10,289.00` |
| `Live` | `Long` | `0.0411` | 14,970,000.00 USD | 0.00 USD | 1,030.00 USD | `-48.09%` | `25,081.00` |
| `Live` | `Long` | `0.0415` | 14,970,000.00 USD | 0.00 USD | 252.72 USD | `-47.71%` | `6,097.00` |
| `Live` | `Long` | `0.0415` | 14,970,000.00 USD | 0.00 USD | 4,590.00 USD | `-47.58%` | `110,580.00` |
| `Live` | `Long` | `0.0420` | 14,960,000.00 USD | 0.00 USD | 266.05 USD | `-47.08%` | `6,342.00` |
| `Live` | `Long` | `0.0421` | 14,960,000.00 USD | 0.00 USD | 59,650.00 USD | `-46.83%` | `1,415,151.00` |
| `Live` | `Long` | `0.0423` | 14,900,000.00 USD | 0.00 USD | 88,980.00 USD | `-46.70%` | `2,106,106.00` |
| `Live` | `Long` | `0.0423` | 14,810,000.00 USD | 0.00 USD | 267.52 USD | `-46.57%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 14,810,000.00 USD | 0.00 USD | 3,190.00 USD | `-46.45%` | `75,261.00` |
| `Live` | `Long` | `0.0425` | 14,810,000.00 USD | 0.00 USD | 1,010.00 USD | `-46.32%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 14,810,000.00 USD | 0.00 USD | 3,620.00 USD | `-46.19%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 14,810,000.00 USD | 0.00 USD | 859.00 USD | `-45.82%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 14,810,000.00 USD | 0.00 USD | 6,430.00 USD | `-45.44%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 14,800,000.00 USD | 0.00 USD | 2,450.00 USD | `-45.31%` | `56,456.00` |
| `Live` | `Long` | `0.0439` | 14,800,000.00 USD | 0.00 USD | 1,610.00 USD | `-44.68%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 14,800,000.00 USD | 0.00 USD | 750.58 USD | `-44.55%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 14,790,000.00 USD | 0.00 USD | 1,060.00 USD | `-44.43%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 14,790,000.00 USD | 0.00 USD | 101,440.00 USD | `-44.05%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 14,690,000.00 USD | 0.00 USD | 444.76 USD | `-43.67%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 14,690,000.00 USD | 0.00 USD | 2,490.00 USD | `-43.55%` | `55,556.00` |
| `Live` | `Long` | `0.0454` | 14,690,000.00 USD | 0.00 USD | 2,170.00 USD | `-42.66%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,690,000.00 USD | 0.00 USD | 32,650.00 USD | `-42.54%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,650,000.00 USD | 0.00 USD | 5,470.00 USD | `-42.28%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 14,650,000.00 USD | 0.00 USD | 4,500.00 USD | `-41.91%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,640,000.00 USD | 0.00 USD | 402.70 USD | `-41.78%` | `8,726.00` |
| `Live` | `Long` | `0.0464` | 14,640,000.00 USD | 0.00 USD | 2,360.00 USD | `-41.53%` | `50,898.00` |
| `Live` | `Long` | `0.0464` | 14,640,000.00 USD | 0.00 USD | 16,780.00 USD | `-41.40%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,620,000.00 USD | 0.00 USD | 109.49 USD | `-41.15%` | `2,347.00` |
| `Live` | `Long` | `0.0471` | 14,620,000.00 USD | 0.00 USD | 15,280.00 USD | `-40.64%` | `324,759.00` |
| `Live` | `Long` | `0.0473` | 14,610,000.00 USD | 0.00 USD | 3,010.00 USD | `-40.39%` | `63,783.00` |
| `Live` | `Long` | `0.0474` | 14,610,000.00 USD | 0.00 USD | 593.13 USD | `-40.14%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 14,610,000.00 USD | 0.00 USD | 105.02 USD | `-39.89%` | `2,204.00` |
| `Live` | `Long` | `0.0481` | 14,610,000.00 USD | 0.00 USD | 56,440.00 USD | `-39.38%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,550,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.26%` | `51,918.00` |
| `Live` | `Long` | `0.0483` | 14,550,000.00 USD | 0.00 USD | 2,280.00 USD | `-39.00%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,540,000.00 USD | 0.00 USD | 1,480.00 USD | `-38.88%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 14,540,000.00 USD | 0.00 USD | 1,280.00 USD | `-38.37%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,540,000.00 USD | 0.00 USD | 5,470.00 USD | `-38.25%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,540,000.00 USD | 0.00 USD | 1,080.00 USD | `-38.12%` | `21,989.00` |
| `Live` | `Long` | `0.0495` | 14,530,000.00 USD | 0.00 USD | 18,690.00 USD | `-37.49%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,520,000.00 USD | 0.00 USD | 253.82 USD | `-37.24%` | `5,102.00` |
| `Live` | `Long` | `0.0498` | 14,520,000.00 USD | 0.00 USD | 323.28 USD | `-37.11%` | `6,485.00` |
| `Live` | `Long` | `0.0500` | 14,520,000.00 USD | 0.00 USD | 501.50 USD | `-36.86%` | `10,020.00` |
| `Live` | `Long` | `0.0502` | 14,520,000.00 USD | 0.00 USD | 384.95 USD | `-36.73%` | `7,676.00` |
| `Live` | `Long` | `0.0503` | 14,510,000.00 USD | 0.00 USD | 5,410.00 USD | `-36.61%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,510,000.00 USD | 0.00 USD | 1,330.00 USD | `-36.48%` | `26,380.00` |
| `Live` | `Long` | `0.0505` | 14,510,000.00 USD | 0.00 USD | 334.89 USD | `-36.35%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,510,000.00 USD | 0.00 USD | 1,040.00 USD | `-36.10%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,510,000.00 USD | 0.00 USD | 5,350.00 USD | `-35.98%` | `105,363.00` |
| `Live` | `Long` | `0.0508` | 14,500,000.00 USD | 0.00 USD | 314.00 USD | `-35.85%` | `6,175.00` |
| `Live` | `Long` | `0.0510` | 14,500,000.00 USD | 0.00 USD | 535.43 USD | `-35.72%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,500,000.00 USD | 0.00 USD | 566.65 USD | `-35.60%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,500,000.00 USD | 0.00 USD | 11,000.00 USD | `-35.47%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,490,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.35%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,490,000.00 USD | 0.00 USD | 385.13 USD | `-35.22%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,490,000.00 USD | 0.00 USD | 662.73 USD | `-35.09%` | `12,881.00` |
| `Live` | `Long` | `0.0517` | 14,490,000.00 USD | 0.00 USD | 1,200.00 USD | `-34.84%` | `23,207.00` |
| `Live` | `Long` | `0.0517` | 14,490,000.00 USD | 0.00 USD | 297.41 USD | `-34.71%` | `5,747.00` |
| `Live` | `Long` | `0.0520` | 14,480,000.00 USD | 0.00 USD | 277.72 USD | `-34.46%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,480,000.00 USD | 0.00 USD | 3,990.00 USD | `-34.34%` | `76,663.00` |
| `Live` | `Long` | `0.0522` | 14,480,000.00 USD | 0.00 USD | 275,090.00 USD | `-34.08%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,210,000.00 USD | 0.00 USD | 1,170.00 USD | `-33.83%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,200,000.00 USD | 0.00 USD | 5,640.00 USD | `-33.71%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,200,000.00 USD | 0.00 USD | 395.09 USD | `-33.58%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,200,000.00 USD | 0.00 USD | 2,360.00 USD | `-33.45%` | `44,828.00` |
| `Live` | `Long` | `0.0529` | 14,200,000.00 USD | 0.00 USD | 673.52 USD | `-33.33%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,200,000.00 USD | 0.00 USD | 181,690.00 USD | `-33.20%` | `3,431,434.00` |
| `Live` | `Long` | `0.0532` | 14,010,000.00 USD | 0.00 USD | 61,750.00 USD | `-32.95%` | `1,161,821.00` |
| `Live` | `Long` | `0.0532` | 13,950,000.00 USD | 0.00 USD | 336.86 USD | `-32.82%` | `6,326.00` |
| `Live` | `Long` | `0.0534` | 13,950,000.00 USD | 0.00 USD | 314,750.00 USD | `-32.57%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,640,000.00 USD | 0.00 USD | 942.48 USD | `-32.44%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 13,640,000.00 USD | 0.00 USD | 291.27 USD | `-32.32%` | `5,429.00` |
| `Live` | `Long` | `0.0539` | 13,640,000.00 USD | 0.00 USD | 5,290.00 USD | `-31.94%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,630,000.00 USD | 0.00 USD | 2,290.00 USD | `-31.81%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,630,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.69%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,610,000.00 USD | 0.00 USD | 96,530.00 USD | `-31.56%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,520,000.00 USD | 0.00 USD | 237.95 USD | `-31.31%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,520,000.00 USD | 0.00 USD | 3,230.00 USD | `-31.06%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,510,000.00 USD | 0.00 USD | 892.81 USD | `-30.93%` | `16,307.00` |
| `Live` | `Long` | `0.0549` | 13,510,000.00 USD | 0.00 USD | 770.89 USD | `-30.68%` | `14,029.00` |
| `Live` | `Long` | `0.0556` | 13,510,000.00 USD | 0.00 USD | 907.02 USD | `-29.92%` | `16,328.00` |
| `Live` | `Long` | `0.0556` | 13,510,000.00 USD | 0.00 USD | 1,610.00 USD | `-29.79%` | `28,854.00` |
| `Live` | `Long` | `0.0558` | 13,510,000.00 USD | 0.00 USD | 101.07 USD | `-29.67%` | `1,813.00` |
| `Live` | `Long` | `0.0561` | 13,510,000.00 USD | 0.00 USD | 772.62 USD | `-29.16%` | `13,760.00` |
| `Live` | `Long` | `0.0563` | 13,510,000.00 USD | 0.00 USD | 40,620.00 USD | `-29.04%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,470,000.00 USD | 0.00 USD | 351.85 USD | `-28.91%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,470,000.00 USD | 0.00 USD | 131.48 USD | `-28.66%` | `2,325.00` |
| `Live` | `Long` | `0.0566` | 13,470,000.00 USD | 0.00 USD | 1,010.00 USD | `-28.53%` | `17,849.00` |
| `Live` | `Long` | `0.0568` | 13,470,000.00 USD | 0.00 USD | 567.50 USD | `-28.41%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,470,000.00 USD | 0.00 USD | 1,040.00 USD | `-28.15%` | `18,175.00` |
| `Live` | `Long` | `0.0570` | 13,470,000.00 USD | 0.00 USD | 8,350.00 USD | `-28.03%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,460,000.00 USD | 0.00 USD | 825.82 USD | `-27.90%` | `14,450.00` |
| `Live` | `Long` | `0.0573` | 13,460,000.00 USD | 0.00 USD | 3,910.00 USD | `-27.65%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,450,000.00 USD | 0.00 USD | 7,260.00 USD | `-27.40%` | `126,103.00` |
| `Live` | `Long` | `0.0576` | 13,450,000.00 USD | 0.00 USD | 10,600.00 USD | `-27.27%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,430,000.00 USD | 0.00 USD | 14,210.00 USD | `-27.14%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,420,000.00 USD | 0.00 USD | 3,940.00 USD | `-27.02%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,420,000.00 USD | 0.00 USD | 10,530.00 USD | `-26.89%` | `181,738.00` |
| `Live` | `Long` | `0.0580` | 13,410,000.00 USD | 0.00 USD | 431.14 USD | `-26.77%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,410,000.00 USD | 0.00 USD | 447.17 USD | `-26.64%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,410,000.00 USD | 0.00 USD | 116.82 USD | `-26.39%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 13,410,000.00 USD | 0.00 USD | 392.08 USD | `-26.26%` | `6,708.00` |
| `Live` | `Long` | `0.0585` | 13,400,000.00 USD | 0.00 USD | 5,780,000.00 USD | `-26.14%` | `98,669,375.00` |
| `Live` | `Long` | `0.0587` | 7,630,000.00 USD | 0.00 USD | 9,120.00 USD | `-25.88%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 7,620,000.00 USD | 0.00 USD | 212.22 USD | `-25.63%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 7,620,000.00 USD | 0.00 USD | 26,980.00 USD | `-25.38%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 7,590,000.00 USD | 0.00 USD | 889.30 USD | `-25.13%` | `14,984.00` |
| `Live` | `Long` | `0.0595` | 7,590,000.00 USD | 0.00 USD | 3,660.00 USD | `-25.00%` | `61,626.00` |
| `Live` | `Long` | `0.0595` | 7,590,000.00 USD | 0.00 USD | 2,650.00 USD | `-24.87%` | `44,458.00` |
| `Live` | `Long` | `0.0599` | 7,580,000.00 USD | 0.00 USD | 2,110.00 USD | `-24.50%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 7,580,000.00 USD | 0.00 USD | 2,830.00 USD | `-24.37%` | `47,268.00` |
| `Live` | `Long` | `0.0600` | 7,580,000.00 USD | 0.00 USD | 11,540.00 USD | `-24.24%` | `192,164.00` |
| `Live` | `Long` | `0.0602` | 7,570,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.12%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 7,560,000.00 USD | 0.00 USD | 1,280.00 USD | `-23.86%` | `21,252.00` |
| `Live` | `Long` | `0.0604` | 7,560,000.00 USD | 0.00 USD | 2,160.00 USD | `-23.74%` | `35,719.00` |
| `Live` | `Long` | `0.0605` | 7,560,000.00 USD | 0.00 USD | 32,090.00 USD | `-23.61%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,520,000.00 USD | 0.00 USD | 1,990.00 USD | `-23.36%` | `32,714.00` |
| `Live` | `Long` | `0.0609` | 7,520,000.00 USD | 0.00 USD | 17,630.00 USD | `-23.23%` | `289,716.00` |
| `Live` | `Long` | `0.0609` | 7,500,000.00 USD | 0.00 USD | 2,220.00 USD | `-23.11%` | `36,478.00` |
| `Live` | `Long` | `0.0611` | 7,500,000.00 USD | 0.00 USD | 11,810.00 USD | `-22.98%` | `193,507.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 913.21 USD | `-22.86%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 298.17 USD | `-22.73%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 655.16 USD | `-22.60%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,490,000.00 USD | 0.00 USD | 1,400.00 USD | `-22.35%` | `22,725.00` |
| `Live` | `Long` | `0.0617` | 7,490,000.00 USD | 0.00 USD | 13,830.00 USD | `-22.22%` | `224,372.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 158.08 USD | `-22.10%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-21.72%` | `431,787.00` |
| `Live` | `Long` | `0.0622` | 7,450,000.00 USD | 0.00 USD | 1,820.00 USD | `-21.47%` | `29,227.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-21.34%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 3,470.00 USD | `-21.22%` | `55,505.00` |
| `Live` | `Long` | `0.0625` | 7,440,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-21.09%` | `17,642,013.00` |
| `Live` | `Long` | `0.0626` | 6,340,000.00 USD | 0.00 USD | 168.28 USD | `-20.96%` | `2,686.00` |
| `Live` | `Long` | `0.0628` | 6,330,000.00 USD | 0.00 USD | 461.78 USD | `-20.84%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,330,000.00 USD | 0.00 USD | 10,410.00 USD | `-20.71%` | `165,580.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 233.80 USD | `-20.58%` | `3,714.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 3,080.00 USD | `-20.46%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,320,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-20.33%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 5,260,000.00 USD | 0.00 USD | 32,880.00 USD | `-20.21%` | `519,887.00` |
| `Live` | `Long` | `0.0634` | 5,220,000.00 USD | 0.00 USD | 12,660.00 USD | `-20.08%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-19.95%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 280.95 USD | `-19.83%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,210,000.00 USD | 0.00 USD | 633.38 USD | `-19.70%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,210,000.00 USD | 0.00 USD | 8,670.00 USD | `-19.58%` | `136,018.00` |
| `Live` | `Long` | `0.0639` | 5,200,000.00 USD | 0.00 USD | 23,220.00 USD | `-19.45%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,180,000.00 USD | 0.00 USD | 1,360.00 USD | `-19.32%` | `21,194.00` |
| `Live` | `Long` | `0.0641` | 5,180,000.00 USD | 0.00 USD | 633.29 USD | `-19.07%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,170,000.00 USD | 0.00 USD | 9,150.00 USD | `-18.94%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,170,000.00 USD | 0.00 USD | 2,170.00 USD | `-18.82%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 23,050.00 USD | `-18.69%` | `357,682.00` |
| `Live` | `Long` | `0.0646` | 5,140,000.00 USD | 0.00 USD | 3,520.00 USD | `-18.44%` | `54,442.00` |
| `Live` | `Long` | `0.0648` | 5,140,000.00 USD | 0.00 USD | 87,470.00 USD | `-18.31%` | `1,350,935.00` |
| `Live` | `Long` | `0.0649` | 5,050,000.00 USD | 0.00 USD | 9,910.00 USD | `-18.19%` | `152,854.00` |
| `Live` | `Long` | `0.0649` | 5,040,000.00 USD | 0.00 USD | 21,910.00 USD | `-18.06%` | `337,347.00` |
| `Live` | `Long` | `0.0650` | 5,020,000.00 USD | 0.00 USD | 885.98 USD | `-17.94%` | `13,620.00` |
| `Live` | `Long` | `0.0651` | 5,020,000.00 USD | 0.00 USD | 2,380.00 USD | `-17.81%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 5,010,000.00 USD | 0.00 USD | 34,430.00 USD | `-17.68%` | `527,635.00` |
| `Live` | `Long` | `0.0654` | 4,980,000.00 USD | 0.00 USD | 6,530.00 USD | `-17.56%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,970,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.30%` | `81,453.00` |
| `Live` | `Long` | `0.0657` | 4,970,000.00 USD | 0.00 USD | 22,620.00 USD | `-17.18%` | `344,511.00` |
| `Live` | `Long` | `0.0658` | 4,950,000.00 USD | 0.00 USD | 71,100.00 USD | `-17.05%` | `1,081,348.00` |
| `Live` | `Long` | `0.0659` | 4,870,000.00 USD | 0.00 USD | 14,600.00 USD | `-16.93%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,860,000.00 USD | 0.00 USD | 11,990.00 USD | `-16.80%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,850,000.00 USD | 0.00 USD | 339.48 USD | `-16.55%` | `5,132.00` |
| `Live` | `Long` | `0.0663` | 4,850,000.00 USD | 0.00 USD | 1,630.00 USD | `-16.42%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,850,000.00 USD | 0.00 USD | 27,600.00 USD | `-16.30%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,820,000.00 USD | 0.00 USD | 1,030.00 USD | `-16.17%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,820,000.00 USD | 0.00 USD | 66,830.00 USD | `-16.04%` | `1,004,162.00` |
| `Live` | `Long` | `0.0667` | 4,750,000.00 USD | 0.00 USD | 34,860.00 USD | `-15.92%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,720,000.00 USD | 0.00 USD | 4,860.00 USD | `-15.79%` | `72,810.00` |
| `Live` | `Long` | `0.0669` | 4,710,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-15.66%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,690,000.00 USD | 0.00 USD | 389.18 USD | `-15.54%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,690,000.00 USD | 0.00 USD | 9,180.00 USD | `-15.41%` | `136,862.00` |
| `Live` | `Long` | `0.0672` | 3,680,000.00 USD | 0.00 USD | 899.27 USD | `-15.29%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 196.64 USD | `-15.16%` | `2,924.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 96,530.00 USD | `-15.03%` | `1,433,284.00` |
| `Live` | `Long` | `0.0674` | 3,580,000.00 USD | 0.00 USD | 2,070.00 USD | `-14.91%` | `30,756.00` |
| `Live` | `Long` | `0.0675` | 3,580,000.00 USD | 0.00 USD | 310.73 USD | `-14.78%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,580,000.00 USD | 0.00 USD | 8,210.00 USD | `-14.66%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,570,000.00 USD | 0.00 USD | 5,100.00 USD | `-14.53%` | `75,221.00` |
| `Live` | `Long` | `0.0678` | 3,570,000.00 USD | 0.00 USD | 55,180.00 USD | `-14.40%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,510,000.00 USD | 0.00 USD | 20,030.00 USD | `-14.28%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,490,000.00 USD | 0.00 USD | 212.72 USD | `-14.15%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,490,000.00 USD | 0.00 USD | 4,720.00 USD | `-14.02%` | `69,194.00` |
| `Live` | `Long` | `0.0683` | 3,490,000.00 USD | 0.00 USD | 6,220.00 USD | `-13.90%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,480,000.00 USD | 0.00 USD | 1,290.00 USD | `-13.77%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,480,000.00 USD | 0.00 USD | 6,000.00 USD | `-13.65%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,480,000.00 USD | 0.00 USD | 4,690.00 USD | `-13.52%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,470,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.39%` | `20,568.00` |
| `Live` | `Long` | `0.0688` | 3,470,000.00 USD | 0.00 USD | 69,020.00 USD | `-13.27%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,400,000.00 USD | 0.00 USD | 517.48 USD | `-13.14%` | `7,516.00` |
| `Live` | `Long` | `0.0689` | 3,400,000.00 USD | 0.00 USD | 507,660.00 USD | `-13.02%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,890,000.00 USD | 0.00 USD | 86,650.00 USD | `-12.89%` | `1,254,953.00` |
| `Live` | `Long` | `0.0692` | 2,810,000.00 USD | 0.00 USD | 8,350.00 USD | `-12.76%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,800,000.00 USD | 0.00 USD | 52,390.00 USD | `-12.51%` | `755,504.00` |
| `Live` | `Long` | `0.0694` | 2,740,000.00 USD | 0.00 USD | 96,110.00 USD | `-12.38%` | `1,383,860.00` |
| `Live` | `Long` | `0.0696` | 2,650,000.00 USD | 0.00 USD | 15,100.00 USD | `-12.26%` | `217,157.00` |
| `Live` | `Long` | `0.0697` | 2,630,000.00 USD | 0.00 USD | 5,240.00 USD | `-12.13%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,630,000.00 USD | 0.00 USD | 3,420.00 USD | `-12.01%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,620,000.00 USD | 0.00 USD | 3,630.00 USD | `-11.88%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,620,000.00 USD | 0.00 USD | 9,500.00 USD | `-11.75%` | `135,877.00` |
| `Live` | `Long` | `0.0701` | 2,610,000.00 USD | 0.00 USD | 264.58 USD | `-11.63%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,610,000.00 USD | 0.00 USD | 1,590.00 USD | `-11.50%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 2,000.00 USD | `-11.38%` | `28,486.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 5,060.00 USD | `-11.25%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,600,000.00 USD | 0.00 USD | 216.56 USD | `-11.12%` | `3,074.00` |
| `Live` | `Long` | `0.0706` | 2,600,000.00 USD | 0.00 USD | 93,610.00 USD | `-11.00%` | `1,326,872.00` |
| `Live` | `Long` | `0.0707` | 2,510,000.00 USD | 0.00 USD | 536.00 USD | `-10.74%` | `7,576.00` |
| `Live` | `Long` | `0.0712` | 2,510,000.00 USD | 0.00 USD | 389.38 USD | `-10.11%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,510,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-9.99%` | `24,461,691.00` |
| `Live` | `Long` | `0.0714` | 762,830.00 USD | 0.00 USD | 2,220.00 USD | `-9.86%` | `31,003.00` |
| `Live` | `Long` | `0.0716` | 760,620.00 USD | 0.00 USD | 10,330.00 USD | `-9.74%` | `144,420.00` |
| `Live` | `Long` | `0.0717` | 750,280.00 USD | 0.00 USD | 560.88 USD | `-9.61%` | `7,828.00` |
| `Live` | `Long` | `0.0717` | 749,720.00 USD | 0.00 USD | 1,520.00 USD | `-9.48%` | `21,127.00` |
| `Live` | `Long` | `0.0718` | 748,210.00 USD | 0.00 USD | 10,850.00 USD | `-9.36%` | `151,060.00` |
| `Live` | `Long` | `0.0720` | 737,350.00 USD | 0.00 USD | 778.93 USD | `-9.23%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 736,570.00 USD | 0.00 USD | 23,870.00 USD | `-9.10%` | `331,347.00` |
| `Live` | `Long` | `0.0722` | 712,700.00 USD | 0.00 USD | 5,720.00 USD | `-8.85%` | `79,141.00` |
| `Live` | `Long` | `0.0723` | 706,980.00 USD | 0.00 USD | 6,110.00 USD | `-8.73%` | `84,497.00` |
| `Live` | `Long` | `0.0725` | 700,870.00 USD | 0.00 USD | 598.51 USD | `-8.60%` | `8,261.00` |
| `Live` | `Long` | `0.0726` | 700,270.00 USD | 0.00 USD | 260.74 USD | `-8.47%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 700,010.00 USD | 0.00 USD | 948.37 USD | `-8.35%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 699,060.00 USD | 0.00 USD | 3,170.00 USD | `-8.22%` | `43,539.00` |
| `Live` | `Long` | `0.0728` | 695,890.00 USD | 0.00 USD | 646.11 USD | `-8.10%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 695,250.00 USD | 0.00 USD | 72,950.00 USD | `-7.97%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 622,300.00 USD | 0.00 USD | 10,300.00 USD | `-7.84%` | `141,047.00` |
| `Live` | `Long` | `0.0732` | 612,000.00 USD | 0.00 USD | 1,930.00 USD | `-7.72%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 610,070.00 USD | 0.00 USD | 5,410.00 USD | `-7.59%` | `73,796.00` |
| `Live` | `Long` | `0.0735` | 604,660.00 USD | 0.00 USD | 7,000.00 USD | `-7.34%` | `95,360.00` |
| `Live` | `Long` | `0.0736` | 597,660.00 USD | 0.00 USD | 4,060.00 USD | `-7.21%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 593,600.00 USD | 0.00 USD | 5,490.00 USD | `-7.09%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 588,110.00 USD | 0.00 USD | 10,390.00 USD | `-6.96%` | `140,949.00` |
| `Live` | `Long` | `0.0738` | 577,710.00 USD | 0.00 USD | 5,430.00 USD | `-6.83%` | `73,561.00` |
| `Live` | `Long` | `0.0740` | 572,280.00 USD | 0.00 USD | 13,770.00 USD | `-6.71%` | `186,166.00` |
| `Live` | `Long` | `0.0741` | 558,510.00 USD | 0.00 USD | 455,270.00 USD | `-6.58%` | `6,148,098.00` |
| `Live` | `Long` | `0.0741` | 103,250.00 USD | 0.00 USD | 777.39 USD | `-6.46%` | `10,484.00` |
| `Live` | `Long` | `0.0742` | 102,470.00 USD | 0.00 USD | 1,280.00 USD | `-6.33%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 101,190.00 USD | 0.00 USD | 2,140.00 USD | `-6.20%` | `28,845.00` |
| `Live` | `Long` | `0.0745` | 99,050.00 USD | 0.00 USD | 2,040.00 USD | `-6.08%` | `27,364.00` |
| `Live` | `Long` | `0.0746` | 97,010.00 USD | 0.00 USD | 1,420.00 USD | `-5.95%` | `19,020.00` |
| `Live` | `Long` | `0.0746` | 95,590.00 USD | 0.00 USD | 1,050.00 USD | `-5.82%` | `14,085.00` |
| `Live` | `Long` | `0.0747` | 94,540.00 USD | 0.00 USD | 359.77 USD | `-5.70%` | `4,813.00` |
| `Live` | `Long` | `0.0750` | 94,180.00 USD | 0.00 USD | 8,550.00 USD | `-5.45%` | `114,113.00` |
| `Live` | `Long` | `0.0751` | 85,630.00 USD | 0.00 USD | 13,430.00 USD | `-5.32%` | `178,888.00` |
| `Live` | `Long` | `0.0751` | 72,200.00 USD | 0.00 USD | 1,480.00 USD | `-5.19%` | `19,691.00` |
| `Live` | `Long` | `0.0752` | 70,720.00 USD | 0.00 USD | 11,190.00 USD | `-5.07%` | `148,660.00` |
| `Live` | `Long` | `0.0755` | 59,540.00 USD | 0.00 USD | 4,060.00 USD | `-4.82%` | `53,747.00` |
| `Live` | `Long` | `0.0756` | 55,480.00 USD | 0.00 USD | 977.84 USD | `-4.69%` | `12,943.00` |
| `Live` | `Long` | `0.0756` | 54,500.00 USD | 0.00 USD | 516.61 USD | `-4.56%` | `6,829.00` |
| `Live` | `Long` | `0.0757` | 53,990.00 USD | 0.00 USD | 3,270.00 USD | `-4.44%` | `43,197.00` |
| `Live` | `Long` | `0.0759` | 50,710.00 USD | 0.00 USD | 5,070.00 USD | `-4.31%` | `66,803.00` |
| `Live` | `Long` | `0.0760` | 45,650.00 USD | 0.00 USD | 32,080.00 USD | `-4.18%` | `422,343.00` |
| `Live` | `Long` | `0.0761` | 13,570.00 USD | 0.00 USD | 1,260.00 USD | `-4.06%` | `16,555.00` |
| `Live` | `Long` | `0.0761` | 12,310.00 USD | 0.00 USD | 623.52 USD | `-3.93%` | `8,188.00` |
| `Live` | `Long` | `0.0762` | 11,690.00 USD | 0.00 USD | 181.93 USD | `-3.81%` | `2,386.00` |
| `Live` | `Long` | `0.0764` | 11,510.00 USD | 0.00 USD | 11,510.00 USD | `-3.68%` | `150,696.00` |
| `Live` | `Short` | `0.0814` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | `+2.63%` | `13,050.00` |
| `Live` | `Short` | `0.0818` | 1,770.00 USD | 710.08 USD | 0.00 USD | `+3.13%` | `8,686.00` |
| `Live` | `Short` | `0.0828` | 2,040.00 USD | 263.55 USD | 0.00 USD | `+4.52%` | `3,181.00` |
| `Live` | `Short` | `0.0829` | 2,690.00 USD | 651.07 USD | 0.00 USD | `+4.65%` | `7,849.00` |
| `Live` | `Short` | `0.0832` | 14,010.00 USD | 11,330.00 USD | 0.00 USD | `+4.90%` | `136,223.00` |
| `Live` | `Short` | `0.0833` | 14,160.00 USD | 150.95 USD | 0.00 USD | `+5.15%` | `1,811.00` |
| `Live` | `Short` | `0.0835` | 27,720.00 USD | 13,550.00 USD | 0.00 USD | `+5.40%` | `162,200.00` |
| `Live` | `Short` | `0.0837` | 28,010.00 USD | 293.44 USD | 0.00 USD | `+5.53%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 29,580.00 USD | 1,570.00 USD | 0.00 USD | `+5.66%` | `18,767.00` |
| `Live` | `Short` | `0.0839` | 29,690.00 USD | 104.69 USD | 0.00 USD | `+5.91%` | `1,247.00` |
| `Live` | `Short` | `0.0840` | 34,400.00 USD | 4,710.00 USD | 0.00 USD | `+6.03%` | `56,093.00` |
| `Live` | `Short` | `0.0843` | 34,510.00 USD | 104.72 USD | 0.00 USD | `+6.29%` | `1,243.00` |
| `Live` | `Short` | `0.0847` | 34,720.00 USD | 213.74 USD | 0.00 USD | `+6.79%` | `2,525.00` |
| `Live` | `Short` | `0.0851` | 34,930.00 USD | 214.75 USD | 0.00 USD | `+7.30%` | `2,525.00` |
| `Live` | `Short` | `0.0858` | 35,050.00 USD | 115.30 USD | 0.00 USD | `+8.30%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 35,180.00 USD | 135.37 USD | 0.00 USD | `+8.43%` | `1,575.00` |
| `Live` | `Short` | `0.0862` | 35,400.00 USD | 216.58 USD | 0.00 USD | `+8.68%` | `2,514.00` |
| `Live` | `Short` | `0.0862` | 37,740.00 USD | 2,340.00 USD | 0.00 USD | `+8.81%` | `27,165.00` |
| `Live` | `Short` | `0.0877` | 47,380.00 USD | 9,630.00 USD | 0.00 USD | `+10.58%` | `109,908.00` |
| `Live` | `Short` | `0.0881` | 47,840.00 USD | 465.17 USD | 0.00 USD | `+11.08%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 48,250.00 USD | 411.53 USD | 0.00 USD | `+11.96%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 48,670.00 USD | 418.80 USD | 0.00 USD | `+12.34%` | `4,703.00` |
| `Live` | `Short` | `0.0891` | 48,780.00 USD | 106.09 USD | 0.00 USD | `+12.47%` | `1,190.00` |
| `Live` | `Short` | `0.0895` | 49,060.00 USD | 285.70 USD | 0.00 USD | `+12.85%` | `3,194.00` |
| `Live` | `Short` | `0.0896` | 52,530.00 USD | 3,460.00 USD | 0.00 USD | `+12.97%` | `38,669.00` |
| `Live` | `Short` | `0.0900` | 52,750.00 USD | 226.85 USD | 0.00 USD | `+13.48%` | `2,522.00` |
| `Live` | `Short` | `0.0905` | 53,120.00 USD | 361.53 USD | 0.00 USD | `+14.11%` | `3,997.00` |
| `Live` | `Short` | `0.0906` | 54,000.00 USD | 882.57 USD | 0.00 USD | `+14.36%` | `9,736.00` |
| `Live` | `Short` | `0.0909` | 58,090.00 USD | 4,090.00 USD | 0.00 USD | `+14.61%` | `45,000.00` |
| `Live` | `Short` | `0.0910` | 58,200.00 USD | 114.23 USD | 0.00 USD | `+14.74%` | `1,256.00` |
| `Live` | `Short` | `0.0911` | 58,940.00 USD | 743.15 USD | 0.00 USD | `+14.99%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 62,990.00 USD | 4,040.00 USD | 0.00 USD | `+15.12%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 63,160.00 USD | 171.19 USD | 0.00 USD | `+15.24%` | `1,874.00` |
| `Live` | `Short` | `0.0917` | 63,500.00 USD | 344.43 USD | 0.00 USD | `+15.75%` | `3,754.00` |
| `Live` | `Short` | `0.0921` | 63,680.00 USD | 171.49 USD | 0.00 USD | `+16.13%` | `1,863.00` |
| `Live` | `Short` | `0.0924` | 63,860.00 USD | 187.93 USD | 0.00 USD | `+16.50%` | `2,035.00` |
| `Live` | `Short` | `0.0935` | 67,160.00 USD | 3,300.00 USD | 0.00 USD | `+17.89%` | `35,291.00` |
| `Live` | `Short` | `0.0949` | 67,740.00 USD | 573.84 USD | 0.00 USD | `+19.66%` | `6,050.00` |
| `Live` | `Short` | `0.0950` | 81,530.00 USD | 13,800.00 USD | 0.00 USD | `+19.79%` | `145,305.00` |
| `Live` | `Short` | `0.0951` | 195,710.00 USD | 114,180.00 USD | 0.00 USD | `+20.04%` | `1,200,000.00` |
| `Live` | `Short` | `0.0959` | 196,460.00 USD | 747.55 USD | 0.00 USD | `+21.05%` | `7,791.00` |
| `Live` | `Short` | `0.0961` | 197,070.00 USD | 609.59 USD | 0.00 USD | `+21.30%` | `6,340.00` |
| `Live` | `Short` | `0.0963` | 245,190.00 USD | 48,120.00 USD | 0.00 USD | `+21.43%` | `500,000.00` |
| `Live` | `Short` | `0.0979` | 284,390.00 USD | 39,190.00 USD | 0.00 USD | `+23.44%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 284,860.00 USD | 477.50 USD | 0.00 USD | `+23.95%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 295,380.00 USD | 10,510.00 USD | 0.00 USD | `+24.20%` | `106,785.00` |
| `Live` | `Short` | `0.1002` | 296,660.00 USD | 1,290.00 USD | 0.00 USD | `+26.35%` | `12,841.00` |
| `Live` | `Short` | `0.1012` | 297,670.00 USD | 1,010.00 USD | 0.00 USD | `+27.61%` | `10,000.00` |
| `Live` | `Short` | `0.1013` | 297,850.00 USD | 177.90 USD | 0.00 USD | `+27.73%` | `1,757.00` |
| `Live` | `Short` | `0.1014` | 305,480.00 USD | 7,630.00 USD | 0.00 USD | `+27.99%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 308,450.00 USD | 2,970.00 USD | 0.00 USD | `+28.24%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 308,940.00 USD | 492.85 USD | 0.00 USD | `+28.49%` | `4,839.00` |
| `Live` | `Short` | `0.1041` | 309,960.00 USD | 1,020.00 USD | 0.00 USD | `+31.27%` | `9,849.00` |
| `Live` | `Short` | `0.1061` | 316,070.00 USD | 6,110.00 USD | 0.00 USD | `+33.91%` | `57,554.00` |
| `Live` | `Short` | `0.1072` | 319,290.00 USD | 3,210.00 USD | 0.00 USD | `+35.30%` | `29,960.00` |
| `Live` | `Short` | `0.1085` | 322,650.00 USD | 3,370.00 USD | 0.00 USD | `+36.94%` | `31,000.00` |
| `Live` | `Short` | `0.1114` | 324,150.00 USD | 1,500.00 USD | 0.00 USD | `+40.47%` | `13,431.00` |
| `Live` | `Short` | `0.1121` | 326,440.00 USD | 2,290.00 USD | 0.00 USD | `+41.48%` | `20,406.00` |
| `Live` | `Short` | `0.1127` | 326,650.00 USD | 214.15 USD | 0.00 USD | `+42.11%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 326,790.00 USD | 142.88 USD | 0.00 USD | `+42.49%` | `1,265.00` |
| `Live` | `Short` | `0.1187` | 326,900.00 USD | 106.19 USD | 0.00 USD | `+49.68%` | `895.00` |
| `Live` | `Short` | `0.1215` | 327,250.00 USD | 353.91 USD | 0.00 USD | `+53.22%` | `2,914.00` |
| `Live` | `Short` | `0.1222` | 328,050.00 USD | 796.83 USD | 0.00 USD | `+54.23%` | `6,518.00` |
| `Live` | `Short` | `0.1265` | 328,430.00 USD | 379.65 USD | 0.00 USD | `+59.65%` | `3,000.00` |
| `Live` | `Short` | `0.1270` | 328,540.00 USD | 108.80 USD | 0.00 USD | `+60.15%` | `857.00` |
| `Live` | `Short` | `0.1278` | 330,080.00 USD | 1,540.00 USD | 0.00 USD | `+61.16%` | `12,089.00` |
| `Live` | `Short` | `0.1296` | 330,250.00 USD | 171.66 USD | 0.00 USD | `+63.56%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 332,390.00 USD | 2,140.00 USD | 0.00 USD | `+65.45%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 332,500.00 USD | 102.97 USD | 0.00 USD | `+66.34%` | `781.00` |
| `Live` | `Short` | `0.1323` | 3,100,000.00 USD | 2,770,000.00 USD | 0.00 USD | `+66.84%` | `20,910,149.00` |
| `Live` | `Short` | `0.1338` | 3,100,000.00 USD | 205.31 USD | 0.00 USD | `+68.73%` | `1,535.00` |
| `Live` | `Short` | `0.1384` | 3,100,000.00 USD | 2,210.00 USD | 0.00 USD | `+74.54%` | `16,000.00` |
| `Live` | `Short` | `0.1389` | 3,100,000.00 USD | 1,000.00 USD | 0.00 USD | `+75.17%` | `7,219.00` |
| `Live` | `Short` | `0.1404` | 3,100,000.00 USD | 663.63 USD | 0.00 USD | `+77.19%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 3,100,000.00 USD | 1,800.00 USD | 0.00 USD | `+78.07%` | `12,780.00` |
| `Live` | `Short` | `0.1419` | 3,130,000.00 USD | 23,020.00 USD | 0.00 USD | `+79.08%` | `162,180.00` |
| `Live` | `Short` | `0.1432` | 3,130,000.00 USD | 1,860.00 USD | 0.00 USD | `+80.72%` | `13,010.00` |
| `Live` | `Short` | `0.1437` | 3,130,000.00 USD | 678.93 USD | 0.00 USD | `+81.35%` | `4,723.00` |
| `Live` | `Short` | `0.1479` | 3,140,000.00 USD | 8,320.00 USD | 0.00 USD | `+86.52%` | `56,294.00` |
| `Live` | `Short` | `0.1480` | 3,140,000.00 USD | 391.74 USD | 0.00 USD | `+86.77%` | `2,646.00` |
| `Live` | `Short` | `0.1510` | 3,190,000.00 USD | 56,520.00 USD | 0.00 USD | `+90.43%` | `374,415.00` |
| `Live` | `Short` | `0.1515` | 3,200,000.00 USD | 2,010.00 USD | 0.00 USD | `+91.19%` | `13,240.00` |
| `Live` | `Short` | `0.1525` | 3,200,000.00 USD | 267.55 USD | 0.00 USD | `+92.32%` | `1,755.00` |
| `Live` | `Short` | `0.1527` | 3,200,000.00 USD | 195.39 USD | 0.00 USD | `+92.58%` | `1,280.00` |
| `Live` | `Short` | `0.1527` | 3,200,000.00 USD | 194.45 USD | 0.00 USD | `+92.70%` | `1,273.00` |
| `Live` | `Short` | `0.1563` | 3,200,000.00 USD | 340.06 USD | 0.00 USD | `+97.24%` | `2,175.00` |
| `Live` | `Short` | `0.1570` | 3,200,000.00 USD | 4,830.00 USD | 0.00 USD | `+98.00%` | `30,755.00` |
| `Live` | `Short` | `0.1570` | 3,200,000.00 USD | 980.15 USD | 0.00 USD | `+98.13%` | `6,241.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 625,020.00 USD | 0.00 USD | 375.42 USD | `-67.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 624,640.00 USD | 0.00 USD | 409.59 USD | `-49.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 624,230.00 USD | 0.00 USD | 132.68 USD | `-48.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 624,100.00 USD | 0.00 USD | 788.27 USD | `-47.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 623,310.00 USD | 0.00 USD | 527.05 USD | `-47.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 622,790.00 USD | 0.00 USD | 286.87 USD | `-43.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 622,500.00 USD | 0.00 USD | 252.42 USD | `-41.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 622,250.00 USD | 0.00 USD | 468.67 USD | `-40.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 621,780.00 USD | 0.00 USD | 5,160.00 USD | `-38.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 616,620.00 USD | 0.00 USD | 920.48 USD | `-37.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 615,700.00 USD | 0.00 USD | 1,860.00 USD | `-36.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 613,840.00 USD | 0.00 USD | 175.41 USD | `-35.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 613,660.00 USD | 0.00 USD | 1,370.00 USD | `-30.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 612,290.00 USD | 0.00 USD | 437.58 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 611,850.00 USD | 0.00 USD | 752.54 USD | `-26.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 611,100.00 USD | 0.00 USD | 9,830.00 USD | `-25.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 601,270.00 USD | 0.00 USD | 1,210.00 USD | `-25.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 600,060.00 USD | 0.00 USD | 1,560.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 598,500.00 USD | 0.00 USD | 134.12 USD | `-23.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 598,370.00 USD | 0.00 USD | 8,800.00 USD | `-23.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 589,570.00 USD | 0.00 USD | 504.26 USD | `-21.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 589,060.00 USD | 0.00 USD | 2,280.00 USD | `-21.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 586,780.00 USD | 0.00 USD | 1,280.00 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 585,510.00 USD | 0.00 USD | 920.18 USD | `-19.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 584,580.00 USD | 0.00 USD | 370.79 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 584,210.00 USD | 0.00 USD | 1,130.00 USD | `-17.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 583,090.00 USD | 0.00 USD | 362.24 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 582,720.00 USD | 0.00 USD | 3,140.00 USD | `-17.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 579,580.00 USD | 0.00 USD | 1,200.00 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 578,380.00 USD | 0.00 USD | 996.31 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 577,390.00 USD | 0.00 USD | 632.88 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 576,760.00 USD | 0.00 USD | 115.57 USD | `-15.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 576,640.00 USD | 0.00 USD | 33,620.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 543,010.00 USD | 0.00 USD | 12,860.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 530,150.00 USD | 0.00 USD | 1,260.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 528,890.00 USD | 0.00 USD | 108.08 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 528,780.00 USD | 0.00 USD | 2,960.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 525,820.00 USD | 0.00 USD | 1,430.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 524,390.00 USD | 0.00 USD | 7,990.00 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 516,400.00 USD | 0.00 USD | 8,580.00 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 507,820.00 USD | 0.00 USD | 606.47 USD | `-14.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 507,220.00 USD | 0.00 USD | 38,710.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 468,510.00 USD | 0.00 USD | 660.06 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 467,850.00 USD | 0.00 USD | 102.34 USD | `-12.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 467,750.00 USD | 0.00 USD | 697.50 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 467,050.00 USD | 0.00 USD | 17,020.00 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 450,030.00 USD | 0.00 USD | 895.27 USD | `-11.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 449,130.00 USD | 0.00 USD | 523.23 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 448,610.00 USD | 0.00 USD | 235.12 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 448,380.00 USD | 0.00 USD | 107,230.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 341,150.00 USD | 0.00 USD | 12,930.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 328,220.00 USD | 0.00 USD | 20,070.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 308,150.00 USD | 0.00 USD | 608.76 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 307,540.00 USD | 0.00 USD | 16,880.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 290,660.00 USD | 0.00 USD | 1,670.00 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 288,990.00 USD | 0.00 USD | 4,710.00 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 284,280.00 USD | 0.00 USD | 8,570.00 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 275,710.00 USD | 0.00 USD | 413.42 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 275,300.00 USD | 0.00 USD | 881.82 USD | `-8.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 274,410.00 USD | 0.00 USD | 703.43 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 273,710.00 USD | 0.00 USD | 621.12 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 273,090.00 USD | 0.00 USD | 1,700.00 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 271,390.00 USD | 0.00 USD | 29,060.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 242,330.00 USD | 0.00 USD | 976.95 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 241,350.00 USD | 0.00 USD | 2,090.00 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 239,260.00 USD | 0.00 USD | 28,750.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 210,510.00 USD | 0.00 USD | 2,710.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 207,810.00 USD | 0.00 USD | 115.12 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 207,690.00 USD | 0.00 USD | 4,680.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 203,010.00 USD | 0.00 USD | 1,860.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 201,150.00 USD | 0.00 USD | 2,900.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 198,260.00 USD | 0.00 USD | 107.66 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 198,150.00 USD | 0.00 USD | 5,000.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 193,160.00 USD | 0.00 USD | 1,410.00 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 191,740.00 USD | 0.00 USD | 375.86 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 191,370.00 USD | 0.00 USD | 193.90 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 191,170.00 USD | 0.00 USD | 140.04 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 191,030.00 USD | 0.00 USD | 7,100.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 183,940.00 USD | 0.00 USD | 736.17 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 183,200.00 USD | 0.00 USD | 192.73 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 183,010.00 USD | 0.00 USD | 358.13 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 182,650.00 USD | 0.00 USD | 4,880.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 177,770.00 USD | 0.00 USD | 193.49 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 177,570.00 USD | 0.00 USD | 2,280.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 175,300.00 USD | 0.00 USD | 3,130.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 172,160.00 USD | 0.00 USD | 806.81 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0762` | 171,360.00 USD | 0.00 USD | 359.60 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0764` | 171,000.00 USD | 0.00 USD | 335.56 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0765` | 170,660.00 USD | 0.00 USD | 3,730.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 166,930.00 USD | 0.00 USD | 1,130.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 165,800.00 USD | 0.00 USD | 3,540.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0767` | 162,260.00 USD | 0.00 USD | 192.95 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0769` | 162,070.00 USD | 0.00 USD | 297.49 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0770` | 161,770.00 USD | 0.00 USD | 15,400.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0771` | 146,370.00 USD | 0.00 USD | 3,980.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0772` | 142,390.00 USD | 0.00 USD | 3,900.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0774` | 138,490.00 USD | 0.00 USD | 157.18 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 138,340.00 USD | 0.00 USD | 2,450.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 135,890.00 USD | 0.00 USD | 604.81 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0776` | 135,290.00 USD | 0.00 USD | 193.97 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0777` | 135,090.00 USD | 0.00 USD | 41,810.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0779` | 93,290.00 USD | 0.00 USD | 41,440.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 51,840.00 USD | 0.00 USD | 3,000.00 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 48,840.00 USD | 0.00 USD | 2,010.00 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0781` | 46,830.00 USD | 0.00 USD | 1,350.00 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0783` | 45,490.00 USD | 0.00 USD | 3,140.00 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0784` | 42,350.00 USD | 0.00 USD | 4,370.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 37,980.00 USD | 0.00 USD | 573.31 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 37,410.00 USD | 0.00 USD | 15,790.00 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0786` | 21,620.00 USD | 0.00 USD | 495.57 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0788` | 21,120.00 USD | 0.00 USD | 3,030.00 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0789` | 18,090.00 USD | 0.00 USD | 303.73 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 17,790.00 USD | 0.00 USD | 706.60 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 17,080.00 USD | 0.00 USD | 10,230.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0791` | 6,850.00 USD | 0.00 USD | 4,600.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0793` | 2,260.00 USD | 0.00 USD | 2,260.00 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 1,010.00 USD | 1,010.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 1,160.00 USD | 148.25 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 1,410.00 USD | 248.91 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 1,540.00 USD | 125.45 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 1,880.00 USD | 342.85 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 2,200.00 USD | 319.16 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 3,320.00 USD | 1,120.00 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 25,860.00 USD | 22,540.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 26,260.00 USD | 400.91 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 26,460.00 USD | 200.46 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 26,600.00 USD | 141.34 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 27,310.00 USD | 707.08 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 29,570.00 USD | 2,260.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 126,350.00 USD | 96,780.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 127,160.00 USD | 807.50 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 127,410.00 USD | 257.18 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 127,840.00 USD | 424.74 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 127,940.00 USD | 101.80 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 129,320.00 USD | 1,380.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 129,590.00 USD | 264.63 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 131,020.00 USD | 1,430.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 131,510.00 USD | 492.77 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 132,740.00 USD | 1,220.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 135,650.00 USD | 2,920.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 145,010.00 USD | 9,360.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 148,030.00 USD | 3,010.00 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 148,770.00 USD | 740.75 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 149,370.00 USD | 607.58 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 163,170.00 USD | 13,790.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 167,820.00 USD | 4,650.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 168,330.00 USD | 512.05 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 169,550.00 USD | 1,220.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 169,940.00 USD | 389.31 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 170,640.00 USD | 706.02 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 170,950.00 USD | 303.56 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 171,060.00 USD | 112.89 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 171,440.00 USD | 381.45 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 171,600.00 USD | 155.82 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 173,030.00 USD | 1,430.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 173,380.00 USD | 348.82 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 174,820.00 USD | 1,440.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 175,030.00 USD | 210.88 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,930,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,930,000.00 USD | 3,380.00 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,930,000.00 USD | 341.34 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,930,000.00 USD | 107.71 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,930,000.00 USD | 2,690.00 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,940,000.00 USD | 1,330.00 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,940,000.00 USD | 219.07 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,940,000.00 USD | 326.97 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,940,000.00 USD | 242.84 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,950,000.00 USD | 10,140.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 1,950,000.00 USD | 152.92 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,980,000.00 USD | 30,370.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,980,000.00 USD | 205.59 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,980,000.00 USD | 503.19 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,980,000.00 USD | 307.41 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,980,000.00 USD | 614.09 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,980,000.00 USD | 644.62 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 1,980,000.00 USD | 180.45 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,980,000.00 USD | 2,020.00 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,030,000.00 USD | 43,760.00 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,030,000.00 USD | 1,080.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,030,000.00 USD | 384.06 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,030,000.00 USD | 1,840.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,030,000.00 USD | 2,760.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,030,000.00 USD | 117.71 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,030,000.00 USD | 111.61 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,030,000.00 USD | 571.18 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,030,000.00 USD | 375.94 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,030,000.00 USD | 627.55 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,030,000.00 USD | 211.04 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,030,000.00 USD | 108.36 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,030,000.00 USD | 543.32 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,040,000.00 USD | 1,820.00 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,040,000.00 USD | 2,080.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,060,000.00 USD | 17,680.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,060,000.00 USD | 1,810.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,060,000.00 USD | 1,640.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,060,000.00 USD | 5,340.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,070,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,070,000.00 USD | 224.86 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,090,000.00 USD | 20,540.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,090,000.00 USD | 114.93 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,090,000.00 USD | 840.47 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,090,000.00 USD | 173.36 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,090,000.00 USD | 4,690.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,090,000.00 USD | 1,870.00 USD | 0.00 USD | `+15.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,100,000.00 USD | 2,170.00 USD | 0.00 USD | `+16.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,100,000.00 USD | 541.32 USD | 0.00 USD | `+16.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,230,000.00 USD | 137,500.00 USD | 0.00 USD | `+16.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,230,000.00 USD | 691.07 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,240,000.00 USD | 6,250.00 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,250,000.00 USD | 13,480.00 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,260,000.00 USD | 734.82 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,260,000.00 USD | 1,230.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,260,000.00 USD | 184.09 USD | 0.00 USD | `+17.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,260,000.00 USD | 1,120.00 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,260,000.00 USD | 1,860.00 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,260,000.00 USD | 512.15 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,270,000.00 USD | 6,620.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,270,000.00 USD | 404.96 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,270,000.00 USD | 129.85 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,270,000.00 USD | 3,740.00 USD | 0.00 USD | `+20.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,270,000.00 USD | 2,400.00 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,270,000.00 USD | 409.17 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,270,000.00 USD | 203.74 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,280,000.00 USD | 2,800.00 USD | 0.00 USD | `+22.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,280,000.00 USD | 1,320.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,280,000.00 USD | 694.56 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,280,000.00 USD | 940.91 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,280,000.00 USD | 2,980.00 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,280,000.00 USD | 104.99 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,280,000.00 USD | 1,930.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,290,000.00 USD | 1,490.00 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,290,000.00 USD | 1,090.00 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,290,000.00 USD | 438.96 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,290,000.00 USD | 973.76 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,400,000.00 USD | 113,580.00 USD | 0.00 USD | `+26.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,400,000.00 USD | 175.59 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,400,000.00 USD | 482.89 USD | 0.00 USD | `+27.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,400,000.00 USD | 201.90 USD | 0.00 USD | `+27.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,400,000.00 USD | 489.46 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,400,000.00 USD | 103.68 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,400,000.00 USD | 203.70 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,410,000.00 USD | 3,810.00 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,420,000.00 USD | 11,200.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,420,000.00 USD | 4,330.00 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,420,000.00 USD | 205.50 USD | 0.00 USD | `+29.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,430,000.00 USD | 3,490.00 USD | 0.00 USD | `+29.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,430,000.00 USD | 1,300.00 USD | 0.00 USD | `+30.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,430,000.00 USD | 207.50 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,430,000.00 USD | 813.88 USD | 0.00 USD | `+31.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,450,000.00 USD | 23,160.00 USD | 0.00 USD | `+31.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,450,000.00 USD | 781.51 USD | 0.00 USD | `+31.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 209.30 USD | 0.00 USD | `+32.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 1,440.00 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,460,000.00 USD | 5,140.00 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,460,000.00 USD | 585.32 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,460,000.00 USD | 210.90 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,460,000.00 USD | 1,850.00 USD | 0.00 USD | `+33.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,460,000.00 USD | 105.75 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,470,000.00 USD | 3,220.00 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,470,000.00 USD | 1,600.00 USD | 0.00 USD | `+34.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,470,000.00 USD | 212.90 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,470,000.00 USD | 472.63 USD | 0.00 USD | `+35.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,470,000.00 USD | 214.50 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,470,000.00 USD | 1,040.00 USD | 0.00 USD | `+35.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,470,000.00 USD | 136.12 USD | 0.00 USD | `+36.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,470,000.00 USD | 216.10 USD | 0.00 USD | `+36.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,510,000.00 USD | 40,920.00 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,510,000.00 USD | 217.90 USD | 0.00 USD | `+37.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,510,000.00 USD | 219.70 USD | 0.00 USD | `+38.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,520,000.00 USD | 7,920.00 USD | 0.00 USD | `+38.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,520,000.00 USD | 154.22 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,520,000.00 USD | 221.30 USD | 0.00 USD | `+39.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,550,000.00 USD | 24,440.00 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,550,000.00 USD | 223.10 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,550,000.00 USD | 2,120.00 USD | 0.00 USD | `+41.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,550,000.00 USD | 226.30 USD | 0.00 USD | `+42.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,550,000.00 USD | 351.57 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,550,000.00 USD | 950.34 USD | 0.00 USD | `+43.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,550,000.00 USD | 229.50 USD | 0.00 USD | `+44.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,550,000.00 USD | 771.08 USD | 0.00 USD | `+45.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,550,000.00 USD | 230.90 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,550,000.00 USD | 288.18 USD | 0.00 USD | `+45.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,550,000.00 USD | 619.10 USD | 0.00 USD | `+46.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,550,000.00 USD | 1,250.00 USD | 0.00 USD | `+46.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,550,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,550,000.00 USD | 232.30 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,560,000.00 USD | 1,600.00 USD | 0.00 USD | `+47.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,560,000.00 USD | 1,050.00 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,560,000.00 USD | 3,730.00 USD | 0.00 USD | `+47.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,560,000.00 USD | 676.22 USD | 0.00 USD | `+48.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,560,000.00 USD | 648.25 USD | 0.00 USD | `+48.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,560,000.00 USD | 1,510.00 USD | 0.00 USD | `+48.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,560,000.00 USD | 448.52 USD | 0.00 USD | `+49.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,560,000.00 USD | 136.93 USD | 0.00 USD | `+49.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,560,000.00 USD | 433.07 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,560,000.00 USD | 1,050.00 USD | 0.00 USD | `+50.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,570,000.00 USD | 691.80 USD | 0.00 USD | `+51.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,680,000.00 USD | 118,550.00 USD | 0.00 USD | `+51.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,680,000.00 USD | 143.22 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,690,000.00 USD | 803.95 USD | 0.00 USD | `+52.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,690,000.00 USD | 1,380.00 USD | 0.00 USD | `+52.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,690,000.00 USD | 2,270.00 USD | 0.00 USD | `+53.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,690,000.00 USD | 871.99 USD | 0.00 USD | `+54.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,710,000.00 USD | 24,560.00 USD | 0.00 USD | `+60.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,710,000.00 USD | 400.21 USD | 0.00 USD | `+60.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,730,000.00 USD | 13,850.00 USD | 0.00 USD | `+66.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,730,000.00 USD | 2,360.00 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,730,000.00 USD | 4,160.00 USD | 0.00 USD | `+71.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,740,000.00 USD | 235.54 USD | 0.00 USD | `+76.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,740,000.00 USD | 1,160.00 USD | 0.00 USD | `+78.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,740,000.00 USD | 173.57 USD | 0.00 USD | `+79.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,740,000.00 USD | 380.09 USD | 0.00 USD | `+79.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,750,000.00 USD | 17,150.00 USD | 0.00 USD | `+79.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,750,000.00 USD | 433.35 USD | 0.00 USD | `+82.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,760,000.00 USD | 3,640.00 USD | 0.00 USD | `+85.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,810,000.00 USD | 55,720.00 USD | 0.00 USD | `+86.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,820,000.00 USD | 2,120.00 USD | 0.00 USD | `+87.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,830,000.00 USD | 18,810.00 USD | 0.00 USD | `+89.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1532` | 2,840,000.00 USD | 4,750.00 USD | 0.00 USD | `+93.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1552` | 2,840,000.00 USD | 630.53 USD | 0.00 USD | `+95.73%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0700` | 22,240,000.00 USD | 0.00 USD | 22,240,000.00 USD | 136,180.00 USD | 82,620.00 USD | 55,680.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 21,960,000.00 USD | 0.00 USD | 21,960,000.00 USD | 35,400.00 USD | 18,030.00 USD | 27,560.00 USD |
| `1D` | `0.0702` | 21,880,000.00 USD | 0.00 USD | 21,880,000.00 USD | 71,010.00 USD | 36,780.00 USD | 0.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 21,770,000.00 USD | 0.00 USD | 21,770,000.00 USD | 81,610.00 USD | 20,870.00 USD | 40,010.00 USD |
| `1D` | `0.0704` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,040.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 21,540,000.00 USD | 0.00 USD | 21,540,000.00 USD | 19,150.00 USD | 0.00 USD | 32,230.00 USD |
| `1D` | `0.0706` | 21,490,000.00 USD | 0.00 USD | 21,490,000.00 USD | 29,320.00 USD | 29,080.00 USD | 11,370.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 50,420.00 USD | 21,680.00 USD | 22,780.00 USD |
| `1D` | `0.0708` | 21,330,000.00 USD | 0.00 USD | 21,330,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,100.00 USD |
| `1D` | `0.0710` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 8,080.00 USD | 9,300.00 USD | 34,600.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 21,130,000.00 USD | 0.00 USD | 21,130,000.00 USD | 16,230.00 USD | 8,560.00 USD | 42,280.00 USD |
| `1D` | `0.0712` | 21,060,000.00 USD | 0.00 USD | 21,060,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 21,000,000.00 USD | 0.00 USD | 21,000,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,410.00 USD |
| `1D` | `0.0714` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 32,300.00 USD | 42,090.00 USD | 8,660.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 20,760,000.00 USD | 0.00 USD | 20,760,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD |
| `1D` | `0.0716` | 20,700,000.00 USD | 0.00 USD | 20,700,000.00 USD | 30,130.00 USD | 31,610.00 USD | 464.50 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 20,640,000.00 USD | 0.00 USD | 20,640,000.00 USD | 15,510.00 USD | 7,710.00 USD | 21,830.00 USD |
| `1D` | `0.0718` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 63,040.00 USD | 36,880.00 USD | 50,630.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 15,840.00 USD | 2,950.00 USD | 7,440.00 USD |
| `1D` | `0.0720` | 20,410,000.00 USD | 0.00 USD | 20,410,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,890.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 20,320,000.00 USD | 0.00 USD | 20,320,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0722` | 20,250,000.00 USD | 0.00 USD | 20,250,000.00 USD | 23,760.00 USD | 15,630.00 USD | 21,710.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 20,190,000.00 USD | 0.00 USD | 20,190,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,630.00 USD |
| `1D` | `0.0724` | 20,080,000.00 USD | 0.00 USD | 20,080,000.00 USD | 31,180.00 USD | 17,780.00 USD | 73,820.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 19,960,000.00 USD | 0.00 USD | 19,960,000.00 USD | 47,840.00 USD | 22,980.00 USD | 23,730.00 USD |
| `1D` | `0.0726` | 19,860,000.00 USD | 0.00 USD | 19,860,000.00 USD | 30,810.00 USD | 0.00 USD | 73.63 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 19,830,000.00 USD | 0.00 USD | 19,830,000.00 USD | 20,420.00 USD | 0.00 USD | 239.30 USD |
| `1D` | `0.0728` | 19,810,000.00 USD | 0.00 USD | 19,810,000.00 USD | 15,580.00 USD | 802.30 USD | 0.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 19,790,000.00 USD | 0.00 USD | 19,790,000.00 USD | 17,820.00 USD | 0.00 USD | 19,050.00 USD |
| `1D` | `0.0730` | 19,760,000.00 USD | 0.00 USD | 19,760,000.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 19,740,000.00 USD | 0.00 USD | 19,740,000.00 USD | 42,980.00 USD | 0.00 USD | 170.86 USD |
| `1D` | `0.0732` | 19,700,000.00 USD | 0.00 USD | 19,700,000.00 USD | 42,110.00 USD | 0.00 USD | 184.68 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 19,660,000.00 USD | 0.00 USD | 19,660,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0734` | 19,650,000.00 USD | 0.00 USD | 19,650,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 19,640,000.00 USD | 0.00 USD | 19,640,000.00 USD | 24,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0736` | 19,620,000.00 USD | 0.00 USD | 19,620,000.00 USD | 8,600.00 USD | 0.00 USD | 42.62 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 19,610,000.00 USD | 0.00 USD | 19,610,000.00 USD | 48,230.00 USD | 0.00 USD | 385.08 USD |
| `1D` | `0.0738` | 19,560,000.00 USD | 0.00 USD | 19,560,000.00 USD | 31,820.00 USD | 0.00 USD | 94.48 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 19,530,000.00 USD | 0.00 USD | 19,530,000.00 USD | 33,680.00 USD | 0.00 USD | 183.57 USD |
| `1D` | `0.0740` | 19,490,000.00 USD | 0.00 USD | 19,490,000.00 USD | 33,740.00 USD | 0.00 USD | 328.65 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 19,460,000.00 USD | 0.00 USD | 19,460,000.00 USD | 31,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0742` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 25,930.00 USD | 0.00 USD | 585.38 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 28,250.00 USD | 27,500.00 USD | 742.24 USD |
| `1D` | `0.0744` | 19,350,000.00 USD | 0.00 USD | 19,350,000.00 USD | 41,210.00 USD | 1,840.00 USD | 15,170.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 19,290,000.00 USD | 0.00 USD | 19,290,000.00 USD | 106,370.00 USD | 57,220.00 USD | 25,000.00 USD |
| `1D` | `0.0746` | 19,100,000.00 USD | 0.00 USD | 19,100,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,600.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,570.00 USD |
| `1D` | `0.0748` | 18,100,000.00 USD | 0.00 USD | 18,100,000.00 USD | 169,810.00 USD | 65,720.00 USD | 99,030.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 261,140.00 USD | 144,960.00 USD | 8,200.00 USD |
| `1D` | `0.0750` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 263,060.00 USD | 83,730.00 USD | 121,310.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 16,880,000.00 USD | 0.00 USD | 16,880,000.00 USD | 268,200.00 USD | 82,120.00 USD | 65,260.00 USD |
| `1D` | `0.0752` | 16,470,000.00 USD | 0.00 USD | 16,470,000.00 USD | 119,250.00 USD | 31,840.00 USD | 85,770.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 132,060.00 USD | 72,710.00 USD | 28,450.00 USD |
| `1D` | `0.0754` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 87,330.00 USD | 62,330.00 USD | 19,370.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 109,960.00 USD | 16,530.00 USD | 68,340.00 USD |
| `1D` | `0.0756` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 164,890.00 USD | 147,310.00 USD | 130,800.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 88,960.00 USD | 44,210.00 USD | 104,040.00 USD |
| `1D` | `0.0758` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 70,320.00 USD | 31,960.00 USD | 105,830.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 195,880.00 USD | 130,420.00 USD | 9,180.00 USD |
| `1D` | `0.0760` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 237,110.00 USD | 313,670.00 USD | 277,340.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 13,580,000.00 USD | 0.00 USD | 13,580,000.00 USD | 500,630.00 USD | 463,290.00 USD | 278,250.00 USD |
| `1D` | `0.0762` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 579,620.00 USD | 303,280.00 USD | 223,540.00 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 305,000.00 USD | 179,660.00 USD | 196,770.00 USD |
| `1D` | `0.0764` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 488,440.00 USD | 327,090.00 USD | 24,970.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 558,950.00 USD | 213,120.00 USD | 314,060.00 USD |
| `1D` | `0.0766` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 621,080.00 USD | 262,670.00 USD | 279,700.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 228,110.00 USD | 101,120.00 USD | 213,720.00 USD |
| `1D` | `0.0768` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 426,850.00 USD | 236,860.00 USD | 141,940.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 219,090.00 USD | 193,080.00 USD | 69,820.00 USD |
| `1D` | `0.0770` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 281,930.00 USD | 93,610.00 USD | 254,150.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 231,550.00 USD | 266,030.00 USD | 226,370.00 USD |
| `1D` | `0.0772` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 145,880.00 USD | 296,720.00 USD | 307,740.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 185,470.00 USD | 106,120.00 USD | 241,380.00 USD |
| `1D` | `0.0774` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 143,850.00 USD | 97,350.00 USD | 235,830.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 357,290.00 USD | 150,850.00 USD | 16,770.00 USD |
| `1D` | `0.0776` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 137,380.00 USD | 345,400.00 USD | 381,410.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 74,870.00 USD | 226,950.00 USD | 12,350.00 USD |
| `1D` | `0.0778` | 814,730.00 USD | 0.00 USD | 814,730.00 USD | 148,860.00 USD | 120,190.00 USD | 200,350.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 345,330.00 USD | 0.00 USD | 345,330.00 USD | 0.00 USD | 85,950.00 USD | 0.00 USD |
| `1D` | `0.0780` | 259,380.00 USD | 0.00 USD | 259,380.00 USD | 0.00 USD | 88,770.00 USD | 211.07 USD |
| `1D` | `0.0781` | 170,400.00 USD | 0.00 USD | 170,400.00 USD | 0.00 USD | 33,540.00 USD | 0.00 USD |
| `1D` | `0.0782` | 136,860.00 USD | 0.00 USD | 136,860.00 USD | 0.00 USD | 4,420.00 USD | 85,130.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 47,310.00 USD | 0.00 USD | 47,310.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD |
| `1D` | `0.0784` | 430,270.00 USD | 430,270.00 USD | 0.00 USD | 265,800.00 USD | 6,130.00 USD | 158,340.00 USD |
| `1D` | `0.0784` | 860,550.00 USD | 860,550.00 USD | 0.00 USD | 265,800.00 USD | 6,130.00 USD | 158,340.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 170,030.00 USD | 117,040.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 150,580.00 USD | 307,550.00 USD | 0.00 USD |
| `1D` | `0.0788` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 36,540.00 USD | 96,300.00 USD | 0.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 127,940.00 USD | 35,430.00 USD | 0.00 USD |
| `1D` | `0.0790` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0796` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 133,970.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 185,120.00 USD | 33,340.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 169,980.00 USD | 26,520.00 USD | 171,300.00 USD |
| `1D` | `0.0800` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `1D` | `0.0802` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,660.00 USD |
| `1D` | `0.0804` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 190,570.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 200,420.00 USD | 208,070.00 USD | 40,950.00 USD |
| `1D` | `0.0808` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 411,890.00 USD | 131,030.00 USD | 522,200.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 445,800.00 USD | 336,610.00 USD | 12,430.00 USD |
| `1D` | `0.0810` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 293,220.00 USD | 180,540.00 USD | 132,320.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 66,980.00 USD | 241,410.00 USD | 0.00 USD |
| `1D` | `0.0812` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 124,600.00 USD | 75,260.00 USD | 135,920.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 27,080.00 USD | 18,240.00 USD | 208,970.00 USD |
| `1D` | `0.0814` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 22,430.00 USD | 23,100.00 USD | 386,300.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 232,650.00 USD | 147,560.00 USD | 112,390.00 USD |
| `1D` | `0.0816` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 441,880.00 USD | 245,220.00 USD | 189,600.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 344,470.00 USD | 153,360.00 USD | 130,280.00 USD |
| `1D` | `0.0818` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 269,340.00 USD | 161,880.00 USD | 308,300.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 171,350.00 USD | 368,950.00 USD | 156,330.00 USD |
| `1D` | `0.0820` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 173,080.00 USD | 273,830.00 USD | 448,160.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 208,520.00 USD | 79,630.00 USD | 170,520.00 USD |
| `1D` | `0.0822` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 260,030.00 USD | 169,200.00 USD | 156,280.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 264,720.00 USD | 75,420.00 USD | 8,610.00 USD |
| `1D` | `0.0824` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 148,810.00 USD | 226,510.00 USD | 198,850.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 124,920.00 USD | 116,480.00 USD | 27,810.00 USD |
| `1D` | `0.0826` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 102,880.00 USD | 60,100.00 USD | 190,080.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 52,670.00 USD | 48,230.00 USD | 0.00 USD |
| `1D` | `0.0828` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 224,210.00 USD | 37,180.00 USD | 8,700.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 206,610.00 USD | 79,000.00 USD | 72,510.00 USD |
| `1D` | `0.0830` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 262,060.00 USD | 98,430.00 USD | 150,900.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 97,970.00 USD | 37,430.00 USD | 42,650.00 USD |
| `1D` | `0.0832` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 234,780.00 USD | 91,440.00 USD | 85,750.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 17,110,000.00 USD | 17,110,000.00 USD | 0.00 USD | 151,330.00 USD | 68,410.00 USD | 31,870.00 USD |
| `1D` | `0.0834` | 17,420,000.00 USD | 17,420,000.00 USD | 0.00 USD | 132,090.00 USD | 60,550.00 USD | 117,470.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 17,790,000.00 USD | 17,790,000.00 USD | 0.00 USD | 110,610.00 USD | 184,470.00 USD | 78,220.00 USD |
| `1D` | `0.0836` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 47,660.00 USD | 83,650.00 USD | 197,110.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 101,560.00 USD | 17,710.00 USD | 34,230.00 USD |
| `1D` | `0.0838` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 145,530.00 USD | 68,620.00 USD | 25,510.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 65,490.00 USD | 0.00 USD | 667.96 USD |
| `1D` | `0.0840` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 35,250.00 USD | 15,480.00 USD | 555.36 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 32,120.00 USD | 2,010.00 USD | 577.28 USD |
| `1D` | `0.0842` | 18,750,000.00 USD | 18,750,000.00 USD | 0.00 USD | 30,040.00 USD | 0.00 USD | 46,990.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 18,780,000.00 USD | 18,780,000.00 USD | 0.00 USD | 37,310.00 USD | 0.00 USD | 359.38 USD |
| `1D` | `0.0844` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 79,050.00 USD | 0.00 USD | 160.56 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 18,880,000.00 USD | 18,880,000.00 USD | 0.00 USD | 16,770.00 USD | 0.00 USD | 494.94 USD |
| `1D` | `0.0846` | 18,970,000.00 USD | 18,970,000.00 USD | 0.00 USD | 72,340.00 USD | 16,670.00 USD | 220.48 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0848` | 18,990,000.00 USD | 18,990,000.00 USD | 0.00 USD | 11,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0849` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 6,070.00 USD | 0.00 USD | 742.24 USD |
| `1D` | `0.0850` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 20,730.00 USD | 0.00 USD | 155.29 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0851` | 19,060,000.00 USD | 19,060,000.00 USD | 0.00 USD | 26,040.00 USD | 11,000.00 USD | 92.43 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0853` | 19,070,000.00 USD | 19,070,000.00 USD | 0.00 USD | 12,910.00 USD | 737.47 USD | 500.73 USD |
| `1D` | `0.0854` | 19,130,000.00 USD | 19,130,000.00 USD | 0.00 USD | 35,960.00 USD | 13,190.00 USD | 10,260.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0855` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD |
| `1D` | `0.0856` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 92,490.00 USD | 32,810.00 USD | 20,090.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0857` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 50,540.00 USD | 18,030.00 USD | 27,640.00 USD |
| `1D` | `0.0858` | 19,630,000.00 USD | 19,630,000.00 USD | 0.00 USD | 73,450.00 USD | 36,780.00 USD | 120.36 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0859` | 19,770,000.00 USD | 19,770,000.00 USD | 0.00 USD | 84,540.00 USD | 20,870.00 USD | 40,310.00 USD |
| `1D` | `0.0860` | 19,860,000.00 USD | 19,860,000.00 USD | 0.00 USD | 44,920.00 USD | 22,170.00 USD | 20,040.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0861` | 19,910,000.00 USD | 19,910,000.00 USD | 0.00 USD | 19,150.00 USD | 0.00 USD | 32,230.00 USD |
| `1D` | `0.0862` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 33,780.00 USD | 29,080.00 USD | 11,370.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0864` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 4,990.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0865` | 20,090,000.00 USD | 20,090,000.00 USD | 0.00 USD | 31,770.00 USD | 1,640.00 USD | 17,790.00 USD |
| `1D` | `0.0866` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `1D` | `0.0867` | 20,230,000.00 USD | 20,230,000.00 USD | 0.00 USD | 24,580.00 USD | 37,120.00 USD | 14,230.00 USD |
| `1D` | `0.0868` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 8,080.00 USD | 9,300.00 USD | 34,600.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `1D` | `0.0869` | 20,350,000.00 USD | 20,350,000.00 USD | 0.00 USD | 16,230.00 USD | 8,560.00 USD | 42,280.00 USD |
| `1D` | `0.0870` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0871` | 20,570,000.00 USD | 20,570,000.00 USD | 0.00 USD | 35,120.00 USD | 58,130.00 USD | 62,410.00 USD |
| `1D` | `0.0872` | 20,650,000.00 USD | 20,650,000.00 USD | 0.00 USD | 32,300.00 USD | 42,090.00 USD | 8,660.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `1D` | `0.0873` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0875` | 20,740,000.00 USD | 20,740,000.00 USD | 0.00 USD | 9,700.00 USD | 17,190.00 USD | 0.00 USD |
| `1D` | `0.0876` | 20,780,000.00 USD | 20,780,000.00 USD | 0.00 USD | 20,430.00 USD | 14,420.00 USD | 0.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0877` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 15,510.00 USD | 7,710.00 USD | 21,730.00 USD |
| `1D` | `0.0878` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 54,680.00 USD | 34,920.00 USD | 50,560.00 USD |
| `7D` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `7D` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 0.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD |
| `7D` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 0.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD |
| `7D` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 0.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD |
| `7D` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 0.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD |
| `7D` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD |
| `7D` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD |
| `7D` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.11B` | Total OI Tokens: `14,110,400,086.5 DOGE`
  * 1h OI Change: `-0.76%` | 4h OI Change: `-2.61%` | 24h OI Change: `-3.46%`
  * Exchange Breakdown: Binance=`267.74M` | Bybit=`108.67M` | OKX=`114.32M` | Hyperliquid=`79.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `39.81K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0070%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0055%` | **USDT Bitget** | `0.0078%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `34.01%` | `65.99%` | `0.52` | 41,750,000.00 USD |
| `15M` | `Binance` | `31.75%` | `68.25%` | `0.47` | 28,160,000.00 USD |
| `15M` | `OKX` | `41.03%` | `58.97%` | `0.70` | 2,200,000.00 USD |
| `15M` | `Bybit` | `53%` | `47%` | `1.13` | 1,320,000.00 USD |
| `15M` | `KuCoin` | `62.62%` | `37.38%` | `1.68` | 196,660.00 USD |
| `15M` | `Gate` | `36.87%` | `63.13%` | `0.58` | 3,030,000.00 USD |
| `15M` | `Bitget` | `23.04%` | `76.96%` | `0.30` | 1,810,000.00 USD |
| `15M` | `BingX` | `46.38%` | `53.62%` | `0.86` | 673,700.00 USD |
| `15M` | `MEXC` | `35.64%` | `64.36%` | `0.55` | 453,810.00 USD |
| `15M` | `Bitunix` | `40.87%` | `59.13%` | `0.69` | 1,620,000.00 USD |
| `15M` | `Hyperliquid` | `39.81%` | `60.19%` | `0.66` | 295,540.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.95%` | `48.05%` | `1.08` | 946,380.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `80.6%` | `19.4%` | `4.15` | 111,890.00 USD |
| `15M` | `HTX` | `4.24%` | `95.76%` | `0.04` | 322,390.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `6.06%` | `93.94%` | `0.06` | 293,340.00 USD |
| `15M` | `Aster` | `41.65%` | `58.35%` | `0.71` | 296,890.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `37.07%` | `62.93%` | `0.59` | 33,220.00 USD |
| `15M` | `Whale Positions` | `31.75%` | `68.25%` | `0.47` | 28,160,000.00 USD |
| `15M` | `Global Accounts` | `34.01%` | `65.99%` | `0.52` | 41,750,000.00 USD |
| `1H` | `DOGE` | `45.72%` | `54.28%` | `0.84` | 50,930,000.00 USD |
| `1H` | `Binance` | `44.76%` | `55.24%` | `0.81` | 34,210,000.00 USD |
| `1H` | `OKX` | `49.36%` | `50.64%` | `0.97` | 2,670,000.00 USD |
| `1H` | `Bybit` | `45.59%` | `54.41%` | `0.84` | 1,510,000.00 USD |
| `1H` | `KuCoin` | `43.25%` | `56.75%` | `0.76` | 239,220.00 USD |
| `1H` | `Gate` | `47.71%` | `52.29%` | `0.91` | 3,430,000.00 USD |
| `1H` | `Bitget` | `38.45%` | `61.55%` | `0.62` | 1,880,000.00 USD |
| `1H` | `BingX` | `47.57%` | `52.43%` | `0.91` | 1,690,000.00 USD |
| `1H` | `MEXC` | `49.88%` | `50.12%` | `1.00` | 584,430.00 USD |
| `1H` | `Bitunix` | `38.14%` | `61.86%` | `0.62` | 1,830,000.00 USD |
| `1H` | `Hyperliquid` | `48.36%` | `51.64%` | `0.94` | 367,030.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `66.16%` | `33.84%` | `1.96` | 1,140,000.00 USD |
| `1H` | `Crypto.com` | `49.65%` | `50.35%` | `0.99` | 0.00 USD |
| `1H` | `WhiteBIT` | `26.28%` | `73.72%` | `0.36` | 231,260.00 USD |
| `1H` | `HTX` | `43.39%` | `56.61%` | `0.77` | 384,300.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.44%` | `55.56%` | `0.80` | 294,270.00 USD |
| `1H` | `Aster` | `41.07%` | `58.93%` | `0.70` | 344,520.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `23.49%` | `76.51%` | `0.31` | 125,320.00 USD |
| `1H` | `Whale Positions` | `44.76%` | `55.24%` | `0.81` | 34,210,000.00 USD |
| `1H` | `Global Accounts` | `45.72%` | `54.28%` | `0.84` | 50,930,000.00 USD |
| `4H` | `DOGE` | `46.54%` | `53.46%` | `0.87` | 149,000,000.00 USD |
| `4H` | `Binance` | `46.06%` | `53.94%` | `0.85` | 95,340,000.00 USD |
| `4H` | `OKX` | `48.89%` | `51.11%` | `0.96` | 8,820,000.00 USD |
| `4H` | `Bybit` | `47.14%` | `52.86%` | `0.89` | 4,620,000.00 USD |
| `4H` | `KuCoin` | `43.79%` | `56.21%` | `0.78` | 702,390.00 USD |
| `4H` | `Gate` | `48.89%` | `51.11%` | `0.96` | 11,120,000.00 USD |
| `4H` | `Bitget` | `36.43%` | `63.57%` | `0.57` | 4,480,000.00 USD |
| `4H` | `BingX` | `33.31%` | `66.69%` | `0.50` | 8,170,000.00 USD |
| `4H` | `MEXC` | `51.07%` | `48.93%` | `1.04` | 2,010,000.00 USD |
| `4H` | `Bitunix` | `44.08%` | `55.92%` | `0.79` | 4,640,000.00 USD |
| `4H` | `Hyperliquid` | `47.97%` | `52.03%` | `0.92` | 1,100,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.03%` | `42.97%` | `1.33` | 3,390,000.00 USD |
| `4H` | `Crypto.com` | `50.67%` | `49.33%` | `1.03` | 0.00 USD |
| `4H` | `WhiteBIT` | `35.3%` | `64.7%` | `0.55` | 813,030.00 USD |
| `4H` | `HTX` | `45.3%` | `54.7%` | `0.83` | 1,000,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.31%` | `54.69%` | `0.83` | 351,820.00 USD |
| `4H` | `Aster` | `42.16%` | `57.84%` | `0.73` | 1,200,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.29%` | `76.71%` | `0.30` | 1,220,000.00 USD |
| `4H` | `Whale Positions` | `46.06%` | `53.94%` | `0.85` | 95,340,000.00 USD |
| `4H` | `Global Accounts` | `46.54%` | `53.46%` | `0.87` | 149,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0793` | `0.0794` | `0.0793` | `0.0796` | `0.0792` | 7,734,342.64 USD | 3,622,970.91 USD | 4,111,371.72 USD | -488,400.81 USD | `-6.31%` | `4B / 4S` |
| `0:00 UTC` | `0.0795` | `0.0796` | `0.0795` | `0.0797` | `0.0794` | 2,831,870.97 USD | 1,358,858.88 USD | 1,473,012.09 USD | -114,153.20 USD | `-4.03%` | `5B / 6S` |
| `5:00 UTC` | `0.0795` | `0.0795` | `0.0795` | `0.0797` | `0.0793` | 3,357,728.54 USD | 1,747,237.98 USD | 1,610,490.56 USD | 136,747.43 USD | `+4.07%` | `3B / 4S` |
| `0:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0794` | `0.0789` | 5,383,971.27 USD | 2,616,260.04 USD | 2,767,711.23 USD | -151,451.19 USD | `-2.81%` | `3B / 9S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0790` | 3,072,363.78 USD | 1,995,905.48 USD | 1,076,458.30 USD | 919,447.18 USD | `+29.93%` | `17B / 6S` |
| `0:00 UTC` | `0.0792` | `0.0792` | `0.0792` | `0.0793` | `0.0791` | 2,162,354.33 USD | 812,153.86 USD | 1,350,200.47 USD | -538,046.61 USD | `-24.88%` | `2B / 9S` |
| `5:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0792` | `0.0790` | 1,623,560.28 USD | 710,933.62 USD | 912,626.66 USD | -201,693.05 USD | `-12.42%` | `1B / 6S` |
| `0:00 UTC` | `0.0794` | `0.0794` | `0.0794` | `0.0795` | `0.0791` | 2,224,641.24 USD | 1,501,047.07 USD | 723,594.17 USD | 777,452.89 USD | `+34.95%` | `11B / 0S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0792` | 1,861,645.62 USD | 802,421.72 USD | 1,059,223.91 USD | -256,802.19 USD | `-13.79%` | `3B / 2S` |
| `0:00 UTC` | `0.0785` | `0.0784` | `0.0785` | `0.0793` | `0.0779` | 21,780,552.20 USD | 8,917,728.34 USD | 12,862,823.86 USD | -3,945,095.53 USD | `-18.11%` | `6B / 42S` |

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
| `5m` | 106,060.00 USD | 1,890,000.00 USD | **`ACCUMULATION`** |
| `15m` | -2,100,000.00 USD | -5,580,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,070,000.00 USD | -5,640,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,200,000.00 USD | -5,520,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,040,000.00 USD | -5,090,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,520,000.00 USD | -13,060,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,150,000.00 USD | -4,090,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,500,000.00 USD | -7,090,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,500,000.00 USD | -7,710,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,250,000.00 USD | -22,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -43,190,000.00 USD | -129,850,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -269,640,000.00 USD | -752,210,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+106.06K` | 15m=`-2.10M` | 1h=`-2.20M` | 24h=`-7.25M`
* Futures Capital Netflows: 5m=`+1.89M` | 15m=`-5.58M` | 1h=`-5.52M` | 24h=`-22.52M`
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
  * `2026-10-30 01:36:17 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:40:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0728` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0869`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0785` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0822` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0680`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0789`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
