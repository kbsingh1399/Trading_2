# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 04:16:49 IST` (`2026-10-29 22:46:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0751` | **Live Ask Quote**: `0.0772` | **Mid Price**: `0.0761`
- **Spread Points**: `21.00` | **Spread BPS**: `275.77 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0770` | VWAP Z-Score: `-1.26` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000731` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.85` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0814` | Lower -3.00σ Band: `0.0725`
  * Upper +2.51σ Band: `0.0807` | Lower -2.51σ Band: `0.0732`
  * Upper +2.01σ Band: `0.0799` | Lower -2.01σ Band: `0.0740`
  * Upper +2.00σ Band: `0.0799` | Lower -2.00σ Band: `0.0740`
  * Upper +1.28σ Band: `0.0789` | Lower -1.28σ Band: `0.0751`
  * Upper +1.00σ Band: `0.0784` | Lower -1.00σ Band: `0.0755`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0753` | EMA-20=`0.0762` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0771` (Slope: `+0.0000`) | EMA-100=`0.0774`
  * Institutional Anchors: EMA-144=`0.0775` | EMA-200=`0.0774` (Slope: `-0.3125`) | EMA-233=`0.0774`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0733` | Weekly High=`0.0803` | Weekly Low=`0.0733`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0753` (Distance: `+0.98%`)
  * Point of Control (POC) = `0.0750` (Distance: `+1.41%`)
  * Value Area Low (VAL) = `0.0746` (Distance: `+1.93%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0784` | Weekly POC=`0.0761` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0738`
  * London Session (08:00-16:00 UTC): High=`0.0765` | Low=`0.0758`
  * New York Session (13:00-21:00 UTC): High=`0.0766` | Low=`0.0757`
  * Initial Balance (First Hour): IB High=`0.0764` | IB Low=`0.0759`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0758` - `0.0765`
  * Optimal Trade Entry (OTE 0.705): `0.0763`
  * Structural Invalidation Anchor (0.786): `0.0768`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0761` | `0.0764` | `0.0760` | `0.0763` | `32,627,970` | 2,484,539.88 USD | 891.04 USD | `+0.04%` | -24,837,805.62 USD | `-0.04` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.0763` | `0.0764` | `0.0761` | `0.0761` | `29,461,620` | 2,246,916.24 USD | -274,465.77 USD | `-12.22%` | -25,112,271.39 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0761` | `0.0764` | `0.0760` | `0.0763` | `33,560,285` | 2,556,046.60 USD | -531,768.46 USD | `-20.80%` | -25,644,039.85 USD | `-0.57` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0761` | `0.0764` | `0.0754` | `0.0761` | `167,691,738` | 12,740,089.09 USD | 849,872.18 USD | `+6.67%` | -30,798,121.98 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0760` | `0.0764` | `0.0757` | `0.0761` | `181,962,630` | 13,833,535.23 USD | 6,041,388.94 USD | `+43.67%` | -24,756,733.04 USD | `+2.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0761` | `0.0764` | `0.0760` | `0.0763` | `34,542,487` | 2,630,988.86 USD | -594,163.89 USD | `-22.58%` | -25,350,896.93 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0792` | `0.0793` | `0.0742` | `0.0753` | `1,891,844,576` | 144,606,422.97 USD | -19,167,046.23 USD | `-13.25%` | -32,359,158.42 USD | `-4.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0753` | `0.0770` | `0.0749` | `0.0761` | `774,393,994` | 58,822,673.99 USD | 562,478.15 USD | `+0.96%` | -31,796,680.27 USD | `+0.43` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0761` | `0.0764` | `0.0754` | `0.0763` | `384,206,046` | 29,205,314.62 USD | 6,297,568.21 USD | `+21.56%` | -25,499,112.06 USD | `+1.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0763` | `3,049,470,042` | 232,560,051.17 USD | -12,245,519.41 USD | `-5.27%` | -25,070,944.92 USD | `-1.60` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -11,383,503.61 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -14,406,508.13 USD | `+1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0763` | `3,049,470,042` | 232,560,051.17 USD | -12,245,519.41 USD | `-5.27%` | -25,070,944.92 USD | `-1.60` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0761`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0761` | `523.0000` | 39.82 USD | 39.82 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0761` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0761` | `295607.0000` | 22,508.40 USD | 22,508.40 USD | `10 orders` | `-0.00%` | `-` |
| `BID` | `0.0761` | `5376.0000` | 409.34 USD | 22,917.74 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.0761` | `13410.0000` | 1,021.00 USD | 23,938.74 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0761` | `5254.0000` | 400.02 USD | 24,338.76 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0761` | `10410.0000` | 792.57 USD | 25,131.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0761` | `97897.0000` | 7,453.19 USD | 32,584.52 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0761` | `855115.0000` | 65,101.62 USD | 97,686.13 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0761` | `153237.0000` | 11,665.93 USD | 109,352.06 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0761` | `49661.0000` | 3,780.64 USD | 113,132.71 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0761` | `137848.0000` | 10,493.95 USD | 123,626.66 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0761` | `98564.0000` | 7,503.18 USD | 131,129.85 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0761` | `223560.0000` | 17,017.61 USD | 148,147.46 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0761` | `29235.0000` | 2,225.34 USD | 150,372.80 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `0.0761` | `183927.0000` | 13,999.42 USD | 164,372.22 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0761` | `10410.0000` | 792.34 USD | 165,164.55 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0761` | `147994.0000` | 11,263.97 USD | 176,428.52 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0761` | `119147.0000` | 9,068.16 USD | 185,496.68 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0761` | `10410.0000` | 792.27 USD | 186,288.96 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0761` | `196979.0000` | 14,991.09 USD | 201,280.04 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0761` | `172209.0000` | 13,105.79 USD | 214,385.84 USD | `4 orders` | `-0.05%` | `-` |
| `ASK` | `0.0762` | `7809.0000` | 594.93 USD | 55,096.90 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0762` | `19689.0000` | 1,499.95 USD | 54,501.97 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0762` | `92153.0000` | 7,020.31 USD | 53,002.02 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.0762` | `19689.0000` | 1,499.91 USD | 45,981.71 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0762` | `19689.0000` | 1,499.89 USD | 44,481.81 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0762` | `19689.0000` | 1,499.87 USD | 42,981.92 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0762` | `30102.0000` | 2,293.08 USD | 41,482.05 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `75948.0000` | 5,785.41 USD | 39,188.97 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `157450.0000` | 11,993.75 USD | 33,403.55 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `30101.0000` | 2,292.91 USD | 21,409.80 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `23293.0000` | 1,774.30 USD | 19,116.89 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `19692.0000` | 1,499.98 USD | 17,342.59 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `4965.0000` | 378.19 USD | 15,842.61 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0762` | `80652.0000` | 6,143.10 USD | 15,464.42 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0762` | `10000.0000` | 761.67 USD | 9,321.32 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0762` | `15818.0000` | 1,204.73 USD | 8,559.65 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0762` | `1034.0000` | 78.75 USD | 7,354.92 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0762` | `52546.0000` | 4,001.75 USD | 7,276.17 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0762` | `42475.0000` | 3,234.60 USD | 3,274.42 USD | `1 orders` | `+0.01%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `311` | `0xb83d...6e36` | `SHORT` | 7,819,771.86 USD | `102,645,925.00` | `0.0946` | `0.0763` | `1.48` | 1,887,569.79 USD | `+24.14%` | `3X Cross` |
| `316` | `0xc63a...a3cd` | `LONG` | 7,619,400.00 USD | `100,000,000.00` | `0.0856` | `0.0763` | `0.000000` | -945,421.96 USD | `-12.41%` | `10X Cross` |
| `318` | `0x610b...b613` | `LONG` | 7,519,170.84 USD | `98,666,424.00` | `0.0872` | `0.0763` | `0.0605` | -1,081,011.06 USD | `-14.38%` | `5X Cross` |
| `599` | `0x5b5d...c060` | `SHORT` | 3,771,483.87 USD | `49,478,955.00` | `0.0946` | `0.0763` | `3.50` | 910,032.74 USD | `+24.13%` | `3X Cross` |
| `637` | `0xca49...53c8` | `SHORT` | 3,552,740.03 USD | `46,542,649.00` | `0.0929` | `0.0763` | `0.3768` | 773,304.65 USD | `+21.77%` | `10X Cross` |
| `655` | `0x45d2...4029` | `SHORT` | 3,461,824.61 USD | `45,426,000.00` | `0.0954` | `0.0763` | `0.9540` | 873,804.61 USD | `+25.24%` | `10X Cross` |
| `789` | `0xecb6...2b00` | `SHORT` | 2,885,366.56 USD | `37,854,277.00` | `0.0795` | `0.0763` | `0.8046` | 122,883.09 USD | `+4.26%` | `10X Cross` |
| `1193` | `0x458d...ab3b` | `LONG` | 1,863,595.23 USD | `24,454,063.00` | `0.1002` | `0.0763` | `0.0714` | -587,326.67 USD | `-31.52%` | `3X Isolated` |
| `1198` | `0xeadc...9d55` | `LONG` | 1,854,569.56 USD | `24,317,440.00` | `0.0926` | `0.0763` | `0.000000` | -397,025.01 USD | `-21.41%` | `10X Cross` |
| `1277` | `0x9aa5...58af` | `SHORT` | 1,754,463.44 USD | `23,032,011.00` | `0.0907` | `0.0763` | `0.4621` | 333,814.32 USD | `+19.03%` | `10X Cross` |
| `1362` | `0xf48f...10fe` | `LONG` | 1,632,760.92 USD | `21,424,497.00` | `0.0968` | `0.0763` | `0.0473` | -441,543.69 USD | `-27.04%` | `4X Cross` |
| `1388` | `0x9946...0852` | `SHORT` | 1,593,499.72 USD | `20,910,149.00` | `0.0871` | `0.0763` | `0.1459` | 227,055.67 USD | `+14.25%` | `10X Cross` |
| `1581` | `0xcac1...26b3` | `SHORT` | 1,380,793.53 USD | `18,126,835.00` | `0.0943` | `0.0763` | `0.5439` | 328,665.67 USD | `+23.80%` | `10X Cross` |
| `1612` | `0x0d6a...ca57` | `LONG` | 1,342,836.22 USD | `17,626,455.00` | `0.0875` | `0.0763` | `0.0626` | -199,268.74 USD | `-14.84%` | `3X Isolated` |
| `1659` | `0x4808...a82c` | `LONG` | 1,283,011.28 USD | `16,828,143.00` | `0.0883` | `0.0763` | `0.0632` | -203,461.70 USD | `-15.86%` | `3X Cross` |
| `1791` | `0x31ef...f715` | `LONG` | 1,161,371.43 USD | `15,230,102.00` | `0.0936` | `0.0763` | `0.0668` | -264,324.50 USD | `-22.76%` | `3X Isolated` |
| `1811` | `0xbfc7...80b4` | `SHORT` | 1,145,154.84 USD | `15,020,000.00` | `0.0920` | `0.0763` | `0.3063` | 237,244.45 USD | `+20.72%` | `10X Cross` |
| `1943` | `0x7cee...fc93` | `SHORT` | 1,032,301.16 USD | `13,538,731.00` | `0.0869` | `0.0763` | `0.2716` | 143,700.24 USD | `+13.92%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 7,000.46 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.00K USD at 0.0789 USD [API] | `2026-10-28 14:00:34` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 10,241.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.24K USD at 0.0786 USD [API] | `2026-10-28 14:22:34` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 10,443.96 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.44K USD at 0.0789 USD [API] | `2026-10-28 14:31:03` |
| `ANNOUNCEMENT` | `INFO` | `0.0758` | 15,715.80 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 15.72K USD at 0.0758 USD [API] | `2026-10-24 14:18:09` |
| `ANNOUNCEMENT` | `INFO` | `0.0758` | 9,553.22 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 9.55K USD at 0.0758 USD [API] | `2026-10-24 14:18:09` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 13,883.91 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 13.88K USD at 0.0789 USD [API] | `2026-10-28 14:41:44` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 7,506.01 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.51K USD at 0.0792 USD [API] | `2026-10-28 15:00:33` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 30,939.27 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 30.94K USD at 0.0792 USD [API] | `2026-10-28 15:08:04` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 5,438.69 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.44K USD at 0.0792 USD [API] | `2026-10-28 15:48:57` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 5,133.82 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.13K USD at 0.0792 USD [API] | `2026-10-28 16:31:47` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 9,686.23 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.69K USD at 0.0795 USD [API] | `2026-10-28 18:04:27` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 8,154.59 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 8.15K USD at 0.0791 USD [API] | `2026-10-28 18:13:31` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 6,600.40 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 6.60K USD at 0.0792 USD [API] | `2026-10-28 18:12:49` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 9,449.67 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 9.45K USD at 0.0789 USD [API] | `2026-10-28 18:16:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0790` | 5,237.41 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.24K USD at 0.0790 USD [API] | `2026-10-28 18:24:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0790` | 5,433.07 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.43K USD at 0.0790 USD [API] | `2026-10-28 18:24:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0765` | 7,650.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 7.65K USD at 0.0765 USD [API] | `2026-10-18 19:35:41` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 8,647.64 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 8.65K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 9,027.52 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 9.03K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 149.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.15K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 24.94 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.02K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 193.44 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.19K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 310.50 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.31K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 118.50 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.12K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 125.95 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.13K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 49.98 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.05K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 400.02 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.40K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 120.65 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.12K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1035` | 6,582.21 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 6.58K USD at 0.1035 USD [API] | `2026-09-22 04:03:08` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 14,388.88 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 14.39K USD at 0.0796 USD [API] | `2026-10-28 18:51:18` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 15,662.71 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 15.66K USD at 0.0796 USD [API] | `2026-10-28 18:51:18` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0771` (Vol: 536,600.00 USD, Dist: `+1.30%`) | Long MP=`0.0741` (Vol: 536,600.00 USD, Dist: `--2.64%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 719,200.00 USD, Dist: `+7.78%`) | Long MP=`0.0741` (Vol: 536,600.00 USD, Dist: `--2.64%`)
  * 3D Horizon: Short MP=`0.0821` (Vol: 719,200.00 USD, Dist: `+7.78%`) | Long MP=`0.0741` (Vol: 369,600.00 USD, Dist: `--2.64%`)
  * 7D Horizon: Short MP=`0.0818` (Vol: 947,300.00 USD, Dist: `+7.36%`) | Long MP=`0.0742` (Vol: 544,900.00 USD, Dist: `--2.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0169` | 1,890.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0185` | 1,380.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 27,620.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 112.85 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0190` | 5,310.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 17,390.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0204` | 244.77 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0209` | 329.33 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0211` | 3,240.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 2,350.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0219` | 118.69 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0222` | 20,020.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0223` | 715.20 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 345.98 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0239` | 935.22 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0251` | 812.29 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0263` | 1,050.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0273` | 472.14 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0282` | 14,070.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 13,920.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0300` | 150.86 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 139.21 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0321` | 403.26 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0324` | 455.50 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0326` | 6,120.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 2,600.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 1,690.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 4,740.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 35,100.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 171.34 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0384` | 3,890.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 206.74 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 208.15 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 4,790.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 135.76 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0398` | 3,010.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0403` | 21,200.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 432.03 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 951.72 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0413` | 1,960.00 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0416` | 921.67 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0418` | 58,820.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 4,220.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,010.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 119,160.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,170.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 360.51 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 1,210.00 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 969,460.00 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 441.12 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0462` | 696.94 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 3,210.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 1,600.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 2,630.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,410.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 59,060.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 653.15 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 54,270.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 11,200.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 2,180.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 1,190.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 309.15 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 314.91 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 2,590.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 676.49 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 3,990.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 315,250.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 68,690.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 395.09 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 183,340.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0530` | 109,630.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 9,240.00 USD | 14,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 100.96 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 314,750.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 1,590.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 258.10 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 237.95 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 336.85 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 892.81 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0559` | 1,620.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 466.77 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 5,420.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 644.99 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,590.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 810.49 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 371.02 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 1,770.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,910.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,520.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 2,830.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 5,930,000.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 9,140.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 548.46 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,970.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 46,790.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 1,940.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,810.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 13,460.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0619` | 401.75 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 5,700.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 194.66 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 52,360.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 40,430.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 10,930.00 USD | 6,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,070,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 1,210.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 9,420.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,360.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,050.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 1,240.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 3,520.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 86,870.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 9,910.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 608.45 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,600.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 68,050.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 34,750.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 4,740.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,190.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0673` | 11,170,000.00 USD | 11,170,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,190.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0675` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 5,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0676` | 11,160,000.00 USD | 11,160,000.00 USD | 45,230.00 USD | 24,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 140,600.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 11,090,000.00 USD | 11,090,000.00 USD | 3,200.00 USD | 39,890.00 USD | 56,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 51,050.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 10,820,000.00 USD | 10,820,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 4,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 10,770,000.00 USD | 10,770,000.00 USD | 24,150.00 USD | 13,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 10,730,000.00 USD | 10,730,000.00 USD | 41,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 455.58 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 10,690,000.00 USD | 10,690,000.00 USD | 41,080.00 USD | 1,410.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 92,360.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 16,550.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 18,800.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 1,170.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 3,670.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 10,580,000.00 USD | 10,580,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,160.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,840.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 10,580,000.00 USD | 10,580,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0696` | 18,020.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 14,650.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 10,580,000.00 USD | 10,580,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,710.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 10,520,000.00 USD | 10,520,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 10,460,000.00 USD | 10,460,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 10,330,000.00 USD | 10,330,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 10,190,000.00 USD | 10,190,000.00 USD | 35,400.00 USD | 18,030.00 USD | 27,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 10,100,000.00 USD | 10,100,000.00 USD | 78,740.00 USD | 36,780.00 USD | 81.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 791.79 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 9,990,000.00 USD | 9,990,000.00 USD | 87,540.00 USD | 31,470.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 9,830,000.00 USD | 9,830,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 9,740,000.00 USD | 9,740,000.00 USD | 34,530.00 USD | 24,910.00 USD | 32,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 9,650,000.00 USD | 9,650,000.00 USD | 36,930.00 USD | 29,080.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0707` | 9,560,000.00 USD | 9,560,000.00 USD | 54,240.00 USD | 21,680.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 9,460,000.00 USD | 9,460,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 9,390,000.00 USD | 9,390,000.00 USD | 36,740.00 USD | 37,120.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0710` | 9,300,000.00 USD | 9,300,000.00 USD | 21,430.00 USD | 9,300.00 USD | 36,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0711` | 9,240,000.00 USD | 9,240,000.00 USD | 27,890.00 USD | 8,560.00 USD | 45,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,790.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 9,150,000.00 USD | 9,150,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 9,090,000.00 USD | 9,090,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 8,930,000.00 USD | 8,930,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 605.68 USD | 771,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 8,840,000.00 USD | 8,840,000.00 USD | 34,440.00 USD | 8,830.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 770,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 8,760,000.00 USD | 8,760,000.00 USD | 30,130.00 USD | 31,610.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 2,090.00 USD | 762,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 8,700,000.00 USD | 8,700,000.00 USD | 17,330.00 USD | 7,710.00 USD | 21,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 24,930.00 USD | 760,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 8,650,000.00 USD | 8,650,000.00 USD | 64,240.00 USD | 31,390.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 960.13 USD | 735,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 8,520,000.00 USD | 8,520,000.00 USD | 20,100.00 USD | 2,950.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 6,600.00 USD | 734,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 8,490,000.00 USD | 8,490,000.00 USD | 31,160.00 USD | 29,440.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,470.00 USD | 728,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 8,400,000.00 USD | 8,400,000.00 USD | 136,510.00 USD | 76,220.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 715,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,170,000.00 USD | 8,170,000.00 USD | 43,930.00 USD | 15,630.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 10,420.00 USD | 693,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,090,000.00 USD | 8,090,000.00 USD | 54,790.00 USD | 162,040.00 USD | 152,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 163.73 USD | 682,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 7,720,000.00 USD | 7,720,000.00 USD | 27,830.00 USD | 87,980.00 USD | 97,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 996.33 USD | 682,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 7,510,000.00 USD | 7,510,000.00 USD | 47,840.00 USD | 22,980.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 681,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 7,420,000.00 USD | 7,420,000.00 USD | 40,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 18,770.00 USD | 681,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 7,370,000.00 USD | 7,370,000.00 USD | 168,660.00 USD | 0.00 USD | 333,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 50,920.00 USD | 662,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 6,870,000.00 USD | 6,870,000.00 USD | 66,510.00 USD | 85,670.00 USD | 74,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 611,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 6,650,000.00 USD | 6,650,000.00 USD | 19,510.00 USD | 13,330.00 USD | 21,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 611,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 6,590,000.00 USD | 6,590,000.00 USD | 112,200.00 USD | 36,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,040.00 USD | 538,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 6,440,000.00 USD | 6,440,000.00 USD | 152,870.00 USD | 17,510.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 528,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 6,270,000.00 USD | 6,270,000.00 USD | 147,060.00 USD | 60,240.00 USD | 61,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 29,280.00 USD | 526,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,000,000.00 USD | 6,000,000.00 USD | 15,550.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 5,920,000.00 USD | 5,920,000.00 USD | 43,340.00 USD | 0.00 USD | 0.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 3,930.00 USD | 496,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 5,870,000.00 USD | 5,870,000.00 USD | 33,390.00 USD | 31,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,690.00 USD | 492,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 5,810,000.00 USD | 5,810,000.00 USD | 234,720.00 USD | 123,630.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 488,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,450,000.00 USD | 5,450,000.00 USD | 51,890.00 USD | 42,510.00 USD | 572.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,740.00 USD | 482,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,350,000.00 USD | 5,350,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 314.08 USD | 472,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 4,840,000.00 USD | 4,840,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,640.00 USD | 471,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,560,000.00 USD | 4,560,000.00 USD | 33,740.00 USD | 0.00 USD | 348.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,080.00 USD | 458,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,530,000.00 USD | 4,530,000.00 USD | 36,980.00 USD | 0.00 USD | 247.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 1,280.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,490,000.00 USD | 4,490,000.00 USD | 286,340.00 USD | 0.00 USD | 666,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,540,000.00 USD | 3,540,000.00 USD | 118,640.00 USD | 234,470.00 USD | 189,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 249.15 USD | 425.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,000,000.00 USD | 3,000,000.00 USD | 19,880.00 USD | 49,540.00 USD | 39,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 176.30 USD | 176.30 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,890,000.00 USD | 2,890,000.00 USD | 199,850.00 USD | 130,070.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,530,000.00 USD | 2,530,000.00 USD | 371,240.00 USD | 210,430.00 USD | 125,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,830,000.00 USD | 1,830,000.00 USD | 466,980.00 USD | 159,330.00 USD | 99,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,100,000.00 USD | 1,100,000.00 USD | 130,290.00 USD | 143,100.00 USD | 173,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 652,990.00 USD | 652,990.00 USD | 203,330.00 USD | 0.00 USD | 148,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 301,020.00 USD | 301,020.00 USD | 69,890.00 USD | 0.00 USD | 120,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 110,270.00 USD | 110,270.00 USD | 0.00 USD | 6,860.00 USD | 55.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 103,360.00 USD | 103,360.00 USD | 0.00 USD | 0.00 USD | 507.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 102,850.00 USD | 102,850.00 USD | 0.00 USD | 85,010.00 USD | 420.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0754` | 17,420.00 USD | 17,420.00 USD | 0.00 USD | 0.00 USD | 253.71 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 17,160.00 USD | 17,160.00 USD | 0.00 USD | 0.00 USD | 0.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0757` | 17,160.00 USD | 17,160.00 USD | 0.00 USD | 0.00 USD | 100.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0758` | 17,060.00 USD | 17,060.00 USD | 0.00 USD | 0.00 USD | 68.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0759` | 16,990.00 USD | 16,990.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0760` | 15,200.00 USD | 15,200.00 USD | 0.00 USD | 0.00 USD | 582.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0761` | 14,620.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | 850.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0762` | 13,770.00 USD | 13,770.00 USD | 0.00 USD | 0.00 USD | 551.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0763` | 13,220.00 USD | 13,220.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 326,310.00 USD | 326,310.00 USD | 0.00 USD | 325,960.00 USD | 352.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 652,630.00 USD | 652,630.00 USD | 0.00 USD | 325,960.00 USD | 352.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 910,340.00 USD | 910,340.00 USD | 0.00 USD | 257,590.00 USD | 125.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 2,040,000.00 USD | 2,040,000.00 USD | 765,870.00 USD | 360,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 2,450,000.00 USD | 2,450,000.00 USD | 211,710.00 USD | 199,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 3,320,000.00 USD | 3,320,000.00 USD | 357,460.00 USD | 0.00 USD | 513,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 3,990,000.00 USD | 3,990,000.00 USD | 181,440.00 USD | 341,350.00 USD | 148,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 4,610,000.00 USD | 4,610,000.00 USD | 272,760.00 USD | 93,300.00 USD | 254,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 5,270,000.00 USD | 5,270,000.00 USD | 216,410.00 USD | 232,340.00 USD | 212,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 6,230,000.00 USD | 6,230,000.00 USD | 286,340.00 USD | 0.00 USD | 666,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 6,610,000.00 USD | 6,610,000.00 USD | 65,160.00 USD | 169,730.00 USD | 148,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 26,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 6,860,000.00 USD | 6,860,000.00 USD | 155,740.00 USD | 72,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0776` | 7,100,000.00 USD | 7,100,000.00 USD | 190,100.00 USD | 47,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 205,390.00 USD | 264,690.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 8,110,000.00 USD | 8,110,000.00 USD | 16,790.00 USD | 202,930.00 USD | 275,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 85,950.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 8,440,000.00 USD | 8,440,000.00 USD | 69,890.00 USD | 31,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 8,620,000.00 USD | 8,620,000.00 USD | 113,060.00 USD | 68,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 8,630,000.00 USD | 8,630,000.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 8,960,000.00 USD | 8,960,000.00 USD | 8,010.00 USD | 184,740.00 USD | 142,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 9,360,000.00 USD | 9,360,000.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 9,710,000.00 USD | 9,710,000.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 10,240,000.00 USD | 10,240,000.00 USD | 179,570.00 USD | 117,040.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 11,180,000.00 USD | 11,180,000.00 USD | 298,820.00 USD | 307,550.00 USD | 333,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0788` | 11,510,000.00 USD | 11,510,000.00 USD | 75,490.00 USD | 181,170.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 11,950,000.00 USD | 11,950,000.00 USD | 234,900.00 USD | 123,220.00 USD | 82,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 12,090,000.00 USD | 12,090,000.00 USD | 102,120.00 USD | 39,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 12,360,000.00 USD | 12,360,000.00 USD | 152,950.00 USD | 63,280.00 USD | 50,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 12,500,000.00 USD | 12,500,000.00 USD | 104,950.00 USD | 18,870.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 12,660,000.00 USD | 12,660,000.00 USD | 75,420.00 USD | 41,370.00 USD | 37,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 12,740,000.00 USD | 12,740,000.00 USD | 10,150.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 12,930,000.00 USD | 12,930,000.00 USD | 174,010.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 13,450,000.00 USD | 13,450,000.00 USD | 191,110.00 USD | 89,760.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 13,670,000.00 USD | 13,670,000.00 USD | 51,440.00 USD | 164,620.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 14,250,000.00 USD | 14,250,000.00 USD | 191,450.00 USD | 193,600.00 USD | 196,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 14,360,000.00 USD | 14,360,000.00 USD | 4,510.00 USD | 5,610.00 USD | 98,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 14,370,000.00 USD | 14,370,000.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0803` | 558.06 USD | 558.06 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0803` | 14,410,000.00 USD | 14,410,000.00 USD | 9,970.00 USD | 0.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 14,440,000.00 USD | 14,440,000.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 14,580,000.00 USD | 14,580,000.00 USD | 56,220.00 USD | 37,230.00 USD | 43,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 14,840,000.00 USD | 14,840,000.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 15,300,000.00 USD | 15,300,000.00 USD | 214,730.00 USD | 208,070.00 USD | 41,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 16,380,000.00 USD | 16,380,000.00 USD | 419,500.00 USD | 131,030.00 USD | 522,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0809` | 4,530.00 USD | 5,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0809` | 17,200,000.00 USD | 17,200,000.00 USD | 477,790.00 USD | 336,610.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 17,810,000.00 USD | 17,810,000.00 USD | 293,220.00 USD | 180,540.00 USD | 132,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 18,140,000.00 USD | 18,140,000.00 USD | 83,280.00 USD | 241,410.00 USD | 202.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 18,520,000.00 USD | 18,520,000.00 USD | 144,600.00 USD | 99,490.00 USD | 137,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 18,800,000.00 USD | 18,800,000.00 USD | 49,290.00 USD | 23,210.00 USD | 212,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 19,200,000.00 USD | 19,200,000.00 USD | 25,120.00 USD | 79,960.00 USD | 292,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 19,690,000.00 USD | 19,690,000.00 USD | 233,650.00 USD | 95,270.00 USD | 159,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 20,420,000.00 USD | 20,420,000.00 USD | 360,380.00 USD | 194,790.00 USD | 177,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0817` | 428.01 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0817` | 20,980,000.00 USD | 20,980,000.00 USD | 301,230.00 USD | 127,050.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 241.90 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 21,720,000.00 USD | 21,720,000.00 USD | 269,340.00 USD | 161,260.00 USD | 310,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 22,340,000.00 USD | 22,340,000.00 USD | 174,640.00 USD | 312,480.00 USD | 128,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 23,020,000.00 USD | 23,020,000.00 USD | 136,010.00 USD | 202,840.00 USD | 343,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 23,480,000.00 USD | 23,480,000.00 USD | 210,590.00 USD | 79,630.00 USD | 170,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 24,070,000.00 USD | 24,070,000.00 USD | 262,170.00 USD | 169,200.00 USD | 155,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 24,420,000.00 USD | 24,420,000.00 USD | 270,850.00 USD | 75,420.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 265.58 USD | 6,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0824` | 25,000,000.00 USD | 25,000,000.00 USD | 151,910.00 USD | 226,510.00 USD | 199,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 25,280,000.00 USD | 25,280,000.00 USD | 127,790.00 USD | 122,020.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 25,700,000.00 USD | 25,700,000.00 USD | 150,570.00 USD | 84,820.00 USD | 190,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 25,800,000.00 USD | 25,800,000.00 USD | 52,670.00 USD | 48,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 26,170,000.00 USD | 26,170,000.00 USD | 225,780.00 USD | 75,940.00 USD | 64,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 26,550,000.00 USD | 26,550,000.00 USD | 201,220.00 USD | 111,290.00 USD | 72,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 26,910,000.00 USD | 26,910,000.00 USD | 169,540.00 USD | 84,690.00 USD | 97,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 27,040,000.00 USD | 27,040,000.00 USD | 81,580.00 USD | 11,280.00 USD | 43,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 9,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 27,360,000.00 USD | 27,360,000.00 USD | 172,190.00 USD | 66,230.00 USD | 79,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 27,700,000.00 USD | 27,700,000.00 USD | 119,590.00 USD | 55,260.00 USD | 165,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 5,700.00 USD | 15,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0834` | 28,050,000.00 USD | 28,050,000.00 USD | 127,020.00 USD | 94,190.00 USD | 126,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 107,580.00 USD | 161,030.00 USD | 64,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 48,890.00 USD | 61,760.00 USD | 144,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 15,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 28,830,000.00 USD | 28,830,000.00 USD | 136,710.00 USD | 17,710.00 USD | 33,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 17,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 29,110,000.00 USD | 29,110,000.00 USD | 179,510.00 USD | 70,030.00 USD | 34,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 7,970.00 USD | 25,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0839` | 29,190,000.00 USD | 29,190,000.00 USD | 49,420.00 USD | 16,550.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 29,250,000.00 USD | 29,250,000.00 USD | 13,720.00 USD | 15,480.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 29,280,000.00 USD | 29,280,000.00 USD | 23,380.00 USD | 2,010.00 USD | 850.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 29,350,000.00 USD | 29,350,000.00 USD | 22,710.00 USD | 0.00 USD | 46,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0843` | 29,380,000.00 USD | 29,380,000.00 USD | 33,600.00 USD | 0.00 USD | 41.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 29,460,000.00 USD | 29,460,000.00 USD | 79,050.00 USD | 0.00 USD | 352.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 29,480,000.00 USD | 29,480,000.00 USD | 18,230.00 USD | 0.00 USD | 349.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 29,570,000.00 USD | 29,570,000.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0847` | 29,580,000.00 USD | 29,580,000.00 USD | 11,040.00 USD | 0.00 USD | 85.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 29,590,000.00 USD | 29,590,000.00 USD | 11,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 723.94 USD | 25,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0849` | 29,600,000.00 USD | 29,600,000.00 USD | 5,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 29,610,000.00 USD | 29,610,000.00 USD | 14,840.00 USD | 0.00 USD | 75.11 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0851` | 29,690,000.00 USD | 29,690,000.00 USD | 35,100.00 USD | 24,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 29,700,000.00 USD | 29,700,000.00 USD | 860.43 USD | 737.47 USD | 9,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 29,730,000.00 USD | 29,730,000.00 USD | 14,260.00 USD | 9,580.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 25,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,250.00 USD | 30,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0871` | 2,530.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 33,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 33,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 33,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 34,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0911` | 743.15 USD | 34,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 38,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 39,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 39,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0934` | 189.97 USD | 40,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0935` | 2,190.00 USD | 42,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 13,800.00 USD | 56,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0953` | 51,910.00 USD | 108,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 933.20 USD | 108,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 109,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 139.74 USD | 109,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 110,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 1,890.00 USD | 112,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 119,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 122,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 123,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1032` | 1,330.00 USD | 124,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 130,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1066` | 3,300.00 USD | 133,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 134,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 137,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1125` | 1,930.00 USD | 139,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 139,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1128` | 3,380.00 USD | 143,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 143,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1163` | 152.42 USD | 143,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 106.19 USD | 143,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 144,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1262` | 121.73 USD | 144,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 144,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1288` | 1,560.00 USD | 146,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1290` | 930.89 USD | 147,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 147,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1310` | 1,200.00 USD | 148,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 150,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 150,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 151,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1343` | 34,710.00 USD | 185,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1368` | 134.97 USD | 185,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 186,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 29,030.00 USD | 215,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 217,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 217,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1442` | 432.45 USD | 218,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 219,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1457` | 3,050,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1475` | 1,950.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,300.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1510` | 140.23 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 11,500.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 16,630,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.91%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,620,000.00 USD | 0.00 USD | 407.02 USD | `-78.39%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,620,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.25%` | `319,394.00` |
| `Live` | `Long` | `0.0169` | 16,620,000.00 USD | 0.00 USD | 1,890.00 USD | `-77.73%` | `111,254.00` |
| `Live` | `Long` | `0.0185` | 16,620,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.76%` | `75,012.00` |
| `Live` | `Long` | `0.0186` | 16,610,000.00 USD | 0.00 USD | 27,620.00 USD | `-75.63%` | `1,488,849.00` |
| `Live` | `Long` | `0.0186` | 16,590,000.00 USD | 0.00 USD | 112.85 USD | `-75.49%` | `6,051.00` |
| `Live` | `Long` | `0.0190` | 16,590,000.00 USD | 0.00 USD | 5,310.00 USD | `-75.10%` | `280,072.00` |
| `Live` | `Long` | `0.0198` | 16,580,000.00 USD | 0.00 USD | 17,390.00 USD | `-74.05%` | `880,408.00` |
| `Live` | `Long` | `0.0204` | 16,560,000.00 USD | 0.00 USD | 244.77 USD | `-73.13%` | `11,969.00` |
| `Live` | `Long` | `0.0209` | 16,560,000.00 USD | 0.00 USD | 329.33 USD | `-72.60%` | `15,795.00` |
| `Live` | `Long` | `0.0211` | 16,560,000.00 USD | 0.00 USD | 3,240.00 USD | `-72.21%` | `153,201.00` |
| `Live` | `Long` | `0.0215` | 16,560,000.00 USD | 0.00 USD | 2,350.00 USD | `-71.68%` | `109,191.00` |
| `Live` | `Long` | `0.0219` | 16,560,000.00 USD | 0.00 USD | 118.69 USD | `-71.29%` | `5,432.00` |
| `Live` | `Long` | `0.0222` | 16,560,000.00 USD | 0.00 USD | 20,020.00 USD | `-70.76%` | `899,926.00` |
| `Live` | `Long` | `0.0223` | 16,540,000.00 USD | 0.00 USD | 715.20 USD | `-70.63%` | `32,000.00` |
| `Live` | `Long` | `0.0232` | 16,540,000.00 USD | 0.00 USD | 345.98 USD | `-69.45%` | `14,881.00` |
| `Live` | `Long` | `0.0239` | 16,540,000.00 USD | 0.00 USD | 935.22 USD | `-68.53%` | `39,049.00` |
| `Live` | `Long` | `0.0251` | 16,540,000.00 USD | 0.00 USD | 812.29 USD | `-66.95%` | `32,298.00` |
| `Live` | `Long` | `0.0263` | 16,540,000.00 USD | 0.00 USD | 1,050.00 USD | `-65.38%` | `40,000.00` |
| `Live` | `Long` | `0.0273` | 16,530,000.00 USD | 0.00 USD | 472.14 USD | `-64.06%` | `17,263.00` |
| `Live` | `Long` | `0.0279` | 16,530,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.27%` | `61,775.00` |
| `Live` | `Long` | `0.0282` | 16,530,000.00 USD | 0.00 USD | 14,070.00 USD | `-63.01%` | `500,000.00` |
| `Live` | `Long` | `0.0284` | 16,520,000.00 USD | 0.00 USD | 13,920.00 USD | `-62.75%` | `491,018.00` |
| `Live` | `Long` | `0.0300` | 16,500,000.00 USD | 0.00 USD | 150.86 USD | `-60.65%` | `5,037.00` |
| `Live` | `Long` | `0.0306` | 16,500,000.00 USD | 0.00 USD | 137.41 USD | `-59.86%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,500,000.00 USD | 0.00 USD | 139.21 USD | `-59.73%` | `4,542.00` |
| `Live` | `Long` | `0.0321` | 16,500,000.00 USD | 0.00 USD | 403.26 USD | `-57.76%` | `12,543.00` |
| `Live` | `Long` | `0.0324` | 16,500,000.00 USD | 0.00 USD | 455.50 USD | `-57.36%` | `14,037.00` |
| `Live` | `Long` | `0.0326` | 16,500,000.00 USD | 0.00 USD | 6,120.00 USD | `-57.23%` | `187,979.00` |
| `Live` | `Long` | `0.0331` | 16,500,000.00 USD | 0.00 USD | 2,600.00 USD | `-56.44%` | `78,319.00` |
| `Live` | `Long` | `0.0338` | 16,490,000.00 USD | 0.00 USD | 1,690.00 USD | `-55.65%` | `50,000.00` |
| `Live` | `Long` | `0.0352` | 16,490,000.00 USD | 0.00 USD | 4,740.00 USD | `-53.68%` | `134,443.00` |
| `Live` | `Long` | `0.0358` | 16,490,000.00 USD | 0.00 USD | 214.53 USD | `-52.89%` | `5,984.00` |
| `Live` | `Long` | `0.0369` | 16,490,000.00 USD | 0.00 USD | 35,100.00 USD | `-51.45%` | `950,000.00` |
| `Live` | `Long` | `0.0379` | 16,450,000.00 USD | 0.00 USD | 171.34 USD | `-50.14%` | `4,515.00` |
| `Live` | `Long` | `0.0381` | 16,450,000.00 USD | 0.00 USD | 246.45 USD | `-50.00%` | `6,477.00` |
| `Live` | `Long` | `0.0384` | 16,450,000.00 USD | 0.00 USD | 3,890.00 USD | `-49.48%` | `101,126.00` |
| `Live` | `Long` | `0.0386` | 16,450,000.00 USD | 0.00 USD | 121.74 USD | `-49.35%` | `3,158.00` |
| `Live` | `Long` | `0.0386` | 16,450,000.00 USD | 0.00 USD | 206.74 USD | `-49.22%` | `5,349.00` |
| `Live` | `Long` | `0.0389` | 16,450,000.00 USD | 0.00 USD | 208.15 USD | `-48.82%` | `5,344.00` |
| `Live` | `Long` | `0.0391` | 16,450,000.00 USD | 0.00 USD | 4,790.00 USD | `-48.56%` | `122,306.00` |
| `Live` | `Long` | `0.0393` | 16,440,000.00 USD | 0.00 USD | 221.10 USD | `-48.43%` | `5,633.00` |
| `Live` | `Long` | `0.0396` | 16,440,000.00 USD | 0.00 USD | 135.76 USD | `-47.90%` | `3,424.00` |
| `Live` | `Long` | `0.0398` | 16,440,000.00 USD | 0.00 USD | 3,010.00 USD | `-47.77%` | `75,693.00` |
| `Live` | `Long` | `0.0403` | 16,440,000.00 USD | 0.00 USD | 21,200.00 USD | `-47.11%` | `526,651.00` |
| `Live` | `Long` | `0.0404` | 16,420,000.00 USD | 0.00 USD | 115.12 USD | `-46.85%` | `2,846.00` |
| `Live` | `Long` | `0.0406` | 16,420,000.00 USD | 0.00 USD | 432.03 USD | `-46.59%` | `10,628.00` |
| `Live` | `Long` | `0.0408` | 16,420,000.00 USD | 0.00 USD | 951.72 USD | `-46.46%` | `23,355.00` |
| `Live` | `Long` | `0.0413` | 16,420,000.00 USD | 0.00 USD | 1,960.00 USD | `-45.80%` | `47,501.00` |
| `Live` | `Long` | `0.0415` | 16,410,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.41%` | `24,809.00` |
| `Live` | `Long` | `0.0416` | 16,410,000.00 USD | 0.00 USD | 921.67 USD | `-45.27%` | `22,129.00` |
| `Live` | `Long` | `0.0418` | 16,410,000.00 USD | 0.00 USD | 58,820.00 USD | `-45.01%` | `1,405,488.00` |
| `Live` | `Long` | `0.0420` | 16,350,000.00 USD | 0.00 USD | 266.05 USD | `-44.88%` | `6,342.00` |
| `Live` | `Long` | `0.0421` | 16,350,000.00 USD | 0.00 USD | 4,220.00 USD | `-44.62%` | `100,000.00` |
| `Live` | `Long` | `0.0423` | 16,350,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.49%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,350,000.00 USD | 0.00 USD | 267.52 USD | `-44.35%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,350,000.00 USD | 0.00 USD | 455.06 USD | `-44.22%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-44.09%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 16,350,000.00 USD | 0.00 USD | 3,620.00 USD | `-43.96%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 16,340,000.00 USD | 0.00 USD | 859.00 USD | `-43.57%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,340,000.00 USD | 0.00 USD | 119,160.00 USD | `-43.17%` | `2,755,040.00` |
| `Live` | `Long` | `0.0433` | 16,220,000.00 USD | 0.00 USD | 2,450.00 USD | `-43.04%` | `56,456.00` |
| `Live` | `Long` | `0.0439` | 16,220,000.00 USD | 0.00 USD | 1,610.00 USD | `-42.38%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,220,000.00 USD | 0.00 USD | 750.58 USD | `-42.25%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,220,000.00 USD | 0.00 USD | 1,170.00 USD | `-42.12%` | `26,467.00` |
| `Live` | `Long` | `0.0444` | 16,220,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.73%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,110,000.00 USD | 0.00 USD | 444.76 USD | `-41.33%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,110,000.00 USD | 0.00 USD | 360.51 USD | `-41.20%` | `8,056.00` |
| `Live` | `Long` | `0.0449` | 16,110,000.00 USD | 0.00 USD | 1,210.00 USD | `-41.07%` | `27,061.00` |
| `Live` | `Long` | `0.0452` | 16,110,000.00 USD | 0.00 USD | 969,460.00 USD | `-40.54%` | `21,424,497.00` |
| `Live` | `Long` | `0.0454` | 15,140,000.00 USD | 0.00 USD | 2,170.00 USD | `-40.28%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 15,140,000.00 USD | 0.00 USD | 32,650.00 USD | `-40.15%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 15,110,000.00 USD | 0.00 USD | 441.12 USD | `-40.02%` | `9,663.00` |
| `Live` | `Long` | `0.0457` | 15,110,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.89%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 15,100,000.00 USD | 0.00 USD | 4,500.00 USD | `-39.49%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 15,100,000.00 USD | 0.00 USD | 114.36 USD | `-39.36%` | `2,478.00` |
| `Live` | `Long` | `0.0462` | 15,100,000.00 USD | 0.00 USD | 696.94 USD | `-39.23%` | `15,069.00` |
| `Live` | `Long` | `0.0464` | 15,100,000.00 USD | 0.00 USD | 362.87 USD | `-39.10%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 15,100,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.97%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 15,080,000.00 USD | 0.00 USD | 109.49 USD | `-38.70%` | `2,347.00` |
| `Live` | `Long` | `0.0471` | 15,080,000.00 USD | 0.00 USD | 3,210.00 USD | `-38.18%` | `68,212.00` |
| `Live` | `Long` | `0.0473` | 15,080,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.92%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 15,080,000.00 USD | 0.00 USD | 2,630.00 USD | `-37.78%` | `55,613.00` |
| `Live` | `Long` | `0.0474` | 15,070,000.00 USD | 0.00 USD | 593.13 USD | `-37.65%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 15,070,000.00 USD | 0.00 USD | 105.02 USD | `-37.39%` | `2,204.00` |
| `Live` | `Long` | `0.0481` | 15,070,000.00 USD | 0.00 USD | 2,410.00 USD | `-36.86%` | `50,080.00` |
| `Live` | `Long` | `0.0481` | 15,070,000.00 USD | 0.00 USD | 59,060.00 USD | `-36.73%` | `1,226,627.00` |
| `Live` | `Long` | `0.0483` | 15,010,000.00 USD | 0.00 USD | 2,280.00 USD | `-36.47%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 15,010,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.34%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 15,010,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.81%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 15,010,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.68%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 15,000,000.00 USD | 0.00 USD | 1,080.00 USD | `-35.55%` | `21,989.00` |
| `Live` | `Long` | `0.0493` | 15,000,000.00 USD | 0.00 USD | 653.15 USD | `-35.16%` | `13,235.00` |
| `Live` | `Long` | `0.0495` | 15,000,000.00 USD | 0.00 USD | 18,690.00 USD | `-34.89%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,980,000.00 USD | 0.00 USD | 54,270.00 USD | `-34.63%` | `1,090,873.00` |
| `Live` | `Long` | `0.0498` | 14,930,000.00 USD | 0.00 USD | 11,200.00 USD | `-34.50%` | `224,650.00` |
| `Live` | `Long` | `0.0500` | 14,910,000.00 USD | 0.00 USD | 501.50 USD | `-34.24%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,910,000.00 USD | 0.00 USD | 5,410.00 USD | `-33.97%` | `107,572.00` |
| `Live` | `Long` | `0.0505` | 14,910,000.00 USD | 0.00 USD | 334.89 USD | `-33.71%` | `6,638.00` |
| `Live` | `Long` | `0.0505` | 14,910,000.00 USD | 0.00 USD | 2,180.00 USD | `-33.58%` | `43,069.00` |
| `Live` | `Long` | `0.0507` | 14,910,000.00 USD | 0.00 USD | 1,040.00 USD | `-33.45%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,900,000.00 USD | 0.00 USD | 5,350.00 USD | `-33.32%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,900,000.00 USD | 0.00 USD | 535.43 USD | `-33.05%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,900,000.00 USD | 0.00 USD | 566.65 USD | `-32.92%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,900,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.79%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,890,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.66%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,890,000.00 USD | 0.00 USD | 385.13 USD | `-32.53%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,890,000.00 USD | 0.00 USD | 1,190.00 USD | `-32.40%` | `23,207.00` |
| `Live` | `Long` | `0.0515` | 14,880,000.00 USD | 0.00 USD | 309.15 USD | `-32.27%` | `5,997.00` |
| `Live` | `Long` | `0.0517` | 14,880,000.00 USD | 0.00 USD | 314.91 USD | `-32.13%` | `6,097.00` |
| `Live` | `Long` | `0.0517` | 14,880,000.00 USD | 0.00 USD | 2,590.00 USD | `-32.00%` | `50,000.00` |
| `Live` | `Long` | `0.0520` | 14,880,000.00 USD | 0.00 USD | 676.49 USD | `-31.74%` | `13,022.00` |
| `Live` | `Long` | `0.0520` | 14,880,000.00 USD | 0.00 USD | 3,990.00 USD | `-31.61%` | `76,663.00` |
| `Live` | `Long` | `0.0522` | 14,880,000.00 USD | 0.00 USD | 315,250.00 USD | `-31.35%` | `6,033,568.00` |
| `Live` | `Long` | `0.0524` | 14,560,000.00 USD | 0.00 USD | 68,690.00 USD | `-31.21%` | `1,312,137.00` |
| `Live` | `Long` | `0.0524` | 14,490,000.00 USD | 0.00 USD | 1,170.00 USD | `-31.08%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,490,000.00 USD | 0.00 USD | 5,640.00 USD | `-30.95%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,490,000.00 USD | 0.00 USD | 395.09 USD | `-30.82%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,480,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.69%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,480,000.00 USD | 0.00 USD | 673.52 USD | `-30.56%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,480,000.00 USD | 0.00 USD | 183,340.00 USD | `-30.43%` | `3,462,426.00` |
| `Live` | `Long` | `0.0530` | 14,300,000.00 USD | 0.00 USD | 109,630.00 USD | `-30.29%` | `2,066,606.00` |
| `Live` | `Long` | `0.0532` | 14,190,000.00 USD | 0.00 USD | 9,240.00 USD | `-30.16%` | `173,844.00` |
| `Live` | `Long` | `0.0532` | 14,180,000.00 USD | 0.00 USD | 100.96 USD | `-30.03%` | `1,896.00` |
| `Live` | `Long` | `0.0534` | 14,180,000.00 USD | 0.00 USD | 314,750.00 USD | `-29.77%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,870,000.00 USD | 0.00 USD | 942.48 USD | `-29.64%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 13,860,000.00 USD | 0.00 USD | 1,590.00 USD | `-29.51%` | `29,631.00` |
| `Live` | `Long` | `0.0539` | 13,860,000.00 USD | 0.00 USD | 258.10 USD | `-29.24%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 13,860,000.00 USD | 0.00 USD | 5,290.00 USD | `-29.11%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,860,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.98%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,850,000.00 USD | 0.00 USD | 13,510.00 USD | `-28.85%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,840,000.00 USD | 0.00 USD | 96,530.00 USD | `-28.72%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,740,000.00 USD | 0.00 USD | 237.95 USD | `-28.46%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,740,000.00 USD | 0.00 USD | 336.85 USD | `-28.32%` | `6,175.00` |
| `Live` | `Long` | `0.0546` | 13,740,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.19%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,740,000.00 USD | 0.00 USD | 892.81 USD | `-28.06%` | `16,307.00` |
| `Live` | `Long` | `0.0556` | 13,740,000.00 USD | 0.00 USD | 907.02 USD | `-27.01%` | `16,328.00` |
| `Live` | `Long` | `0.0559` | 13,740,000.00 USD | 0.00 USD | 1,620.00 USD | `-26.48%` | `28,955.00` |
| `Live` | `Long` | `0.0561` | 13,740,000.00 USD | 0.00 USD | 466.77 USD | `-26.22%` | `8,313.00` |
| `Live` | `Long` | `0.0563` | 13,740,000.00 USD | 0.00 USD | 40,620.00 USD | `-26.09%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,700,000.00 USD | 0.00 USD | 5,420.00 USD | `-25.96%` | `96,244.00` |
| `Live` | `Long` | `0.0566` | 13,690,000.00 USD | 0.00 USD | 131.48 USD | `-25.70%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,690,000.00 USD | 0.00 USD | 568.50 USD | `-25.30%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,690,000.00 USD | 0.00 USD | 315.67 USD | `-25.17%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,690,000.00 USD | 0.00 USD | 8,350.00 USD | `-25.04%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,680,000.00 USD | 0.00 USD | 644.99 USD | `-24.91%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,680,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.64%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,680,000.00 USD | 0.00 USD | 3,590.00 USD | `-24.38%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,670,000.00 USD | 0.00 USD | 10,600.00 USD | `-24.25%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,660,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.12%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,650,000.00 USD | 0.00 USD | 3,940.00 USD | `-23.99%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,640,000.00 USD | 0.00 USD | 431.14 USD | `-23.72%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,640,000.00 USD | 0.00 USD | 810.49 USD | `-23.59%` | `13,938.00` |
| `Live` | `Long` | `0.0583` | 13,640,000.00 USD | 0.00 USD | 116.82 USD | `-23.33%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 13,640,000.00 USD | 0.00 USD | 172.78 USD | `-23.07%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,640,000.00 USD | 0.00 USD | 371.02 USD | `-22.94%` | `6,326.00` |
| `Live` | `Long` | `0.0587` | 13,640,000.00 USD | 0.00 USD | 9,120.00 USD | `-22.81%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 13,630,000.00 USD | 0.00 USD | 212.22 USD | `-22.54%` | `3,600.00` |
| `Live` | `Long` | `0.0590` | 13,630,000.00 USD | 0.00 USD | 1,770.00 USD | `-22.41%` | `30,000.00` |
| `Live` | `Long` | `0.0592` | 13,630,000.00 USD | 0.00 USD | 26,980.00 USD | `-22.28%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,600,000.00 USD | 0.00 USD | 546.26 USD | `-22.02%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,600,000.00 USD | 0.00 USD | 4,910.00 USD | `-21.89%` | `82,539.00` |
| `Live` | `Long` | `0.0595` | 13,600,000.00 USD | 0.00 USD | 3,520.00 USD | `-21.75%` | `59,115.00` |
| `Live` | `Long` | `0.0599` | 13,600,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.36%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 13,590,000.00 USD | 0.00 USD | 2,830.00 USD | `-21.23%` | `47,268.00` |
| `Live` | `Long` | `0.0600` | 13,590,000.00 USD | 0.00 USD | 5,930,000.00 USD | `-21.10%` | `98,786,512.00` |
| `Live` | `Long` | `0.0602` | 7,660,000.00 USD | 0.00 USD | 9,140.00 USD | `-20.97%` | `151,875.00` |
| `Live` | `Long` | `0.0604` | 7,650,000.00 USD | 0.00 USD | 548.46 USD | `-20.70%` | `9,088.00` |
| `Live` | `Long` | `0.0604` | 7,650,000.00 USD | 0.00 USD | 1,970.00 USD | `-20.57%` | `32,592.00` |
| `Live` | `Long` | `0.0605` | 7,650,000.00 USD | 0.00 USD | 32,090.00 USD | `-20.44%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,610,000.00 USD | 0.00 USD | 46,790.00 USD | `-20.18%` | `770,135.00` |
| `Live` | `Long` | `0.0609` | 7,570,000.00 USD | 0.00 USD | 1,940.00 USD | `-20.05%` | `31,875.00` |
| `Live` | `Long` | `0.0609` | 7,570,000.00 USD | 0.00 USD | 2,220.00 USD | `-19.91%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,560,000.00 USD | 0.00 USD | 913.21 USD | `-19.65%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,560,000.00 USD | 0.00 USD | 298.17 USD | `-19.52%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,560,000.00 USD | 0.00 USD | 655.16 USD | `-19.39%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,560,000.00 USD | 0.00 USD | 1,810.00 USD | `-19.13%` | `29,433.00` |
| `Live` | `Long` | `0.0617` | 7,560,000.00 USD | 0.00 USD | 13,460.00 USD | `-18.99%` | `218,374.00` |
| `Live` | `Long` | `0.0617` | 7,550,000.00 USD | 0.00 USD | 158.08 USD | `-18.86%` | `2,560.00` |
| `Live` | `Long` | `0.0619` | 7,550,000.00 USD | 0.00 USD | 401.75 USD | `-18.60%` | `6,485.00` |
| `Live` | `Long` | `0.0621` | 7,550,000.00 USD | 0.00 USD | 26,790.00 USD | `-18.47%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,520,000.00 USD | 0.00 USD | 5,700.00 USD | `-18.34%` | `91,708.00` |
| `Live` | `Long` | `0.0622` | 7,510,000.00 USD | 0.00 USD | 194.66 USD | `-18.21%` | `3,127.00` |
| `Live` | `Long` | `0.0624` | 7,510,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.07%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,510,000.00 USD | 0.00 USD | 52,360.00 USD | `-17.94%` | `838,403.00` |
| `Live` | `Long` | `0.0625` | 7,460,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.81%` | `17,647,786.00` |
| `Live` | `Long` | `0.0626` | 6,360,000.00 USD | 0.00 USD | 40,430.00 USD | `-17.68%` | `645,385.00` |
| `Live` | `Long` | `0.0628` | 6,310,000.00 USD | 0.00 USD | 461.78 USD | `-17.55%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,310,000.00 USD | 0.00 USD | 10,930.00 USD | `-17.42%` | `173,976.00` |
| `Live` | `Long` | `0.0630` | 6,300,000.00 USD | 0.00 USD | 3,080.00 USD | `-17.16%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,300,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-17.02%` | `16,914,273.00` |
| `Live` | `Long` | `0.0633` | 5,230,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.89%` | `19,161.00` |
| `Live` | `Long` | `0.0634` | 5,230,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.76%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 5,220,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.63%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,220,000.00 USD | 0.00 USD | 280.95 USD | `-16.50%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,220,000.00 USD | 0.00 USD | 633.38 USD | `-16.37%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,220,000.00 USD | 0.00 USD | 9,420.00 USD | `-16.24%` | `147,791.00` |
| `Live` | `Long` | `0.0639` | 5,210,000.00 USD | 0.00 USD | 23,220.00 USD | `-16.10%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,180,000.00 USD | 0.00 USD | 1,360.00 USD | `-15.97%` | `21,194.00` |
| `Live` | `Long` | `0.0641` | 5,180,000.00 USD | 0.00 USD | 633.29 USD | `-15.71%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,180,000.00 USD | 0.00 USD | 9,150.00 USD | `-15.58%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,170,000.00 USD | 0.00 USD | 2,170.00 USD | `-15.45%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,170,000.00 USD | 0.00 USD | 23,050.00 USD | `-15.32%` | `357,682.00` |
| `Live` | `Long` | `0.0645` | 5,150,000.00 USD | 0.00 USD | 1,240.00 USD | `-15.18%` | `19,135.00` |
| `Live` | `Long` | `0.0646` | 5,150,000.00 USD | 0.00 USD | 3,520.00 USD | `-15.05%` | `54,442.00` |
| `Live` | `Long` | `0.0648` | 5,140,000.00 USD | 0.00 USD | 86,870.00 USD | `-14.92%` | `1,341,590.00` |
| `Live` | `Long` | `0.0649` | 5,060,000.00 USD | 0.00 USD | 9,910.00 USD | `-14.79%` | `152,854.00` |
| `Live` | `Long` | `0.0649` | 5,050,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.66%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 5,020,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.40%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 5,020,000.00 USD | 0.00 USD | 13,770.00 USD | `-14.26%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 5,010,000.00 USD | 0.00 USD | 6,530.00 USD | `-14.13%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 5,000,000.00 USD | 0.00 USD | 5,340.00 USD | `-13.87%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 5,000,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.61%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,930,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.48%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,910,000.00 USD | 0.00 USD | 11,990.00 USD | `-13.34%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,900,000.00 USD | 0.00 USD | 608.45 USD | `-13.08%` | `9,198.00` |
| `Live` | `Long` | `0.0663` | 4,900,000.00 USD | 0.00 USD | 1,630.00 USD | `-12.95%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,900,000.00 USD | 0.00 USD | 27,600.00 USD | `-12.82%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,870,000.00 USD | 0.00 USD | 1,030.00 USD | `-12.69%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,870,000.00 USD | 0.00 USD | 68,050.00 USD | `-12.56%` | `1,022,557.00` |
| `Live` | `Long` | `0.0667` | 4,800,000.00 USD | 0.00 USD | 34,860.00 USD | `-12.42%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,770,000.00 USD | 0.00 USD | 34,750.00 USD | `-12.29%` | `520,562.00` |
| `Live` | `Long` | `0.0669` | 4,730,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-12.16%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,720,000.00 USD | 0.00 USD | 4,740.00 USD | `-12.03%` | `70,813.00` |
| `Live` | `Long` | `0.0670` | 3,710,000.00 USD | 0.00 USD | 9,190.00 USD | `-11.90%` | `136,993.00` |
| `Live` | `Long` | `0.0672` | 3,700,000.00 USD | 0.00 USD | 899.27 USD | `-11.77%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,700,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.64%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,690,000.00 USD | 0.00 USD | 96,190.00 USD | `-11.51%` | `1,428,139.00` |
| `Live` | `Long` | `0.0674` | 3,600,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.37%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,590,000.00 USD | 0.00 USD | 310.73 USD | `-11.24%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,590,000.00 USD | 0.00 USD | 8,210.00 USD | `-11.11%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,580,000.00 USD | 0.00 USD | 140,600.00 USD | `-10.98%` | `2,075,221.00` |
| `Live` | `Long` | `0.0678` | 3,440,000.00 USD | 0.00 USD | 55,180.00 USD | `-10.85%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,390,000.00 USD | 0.00 USD | 20,030.00 USD | `-10.72%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,370,000.00 USD | 0.00 USD | 212.72 USD | `-10.59%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,370,000.00 USD | 0.00 USD | 51,050.00 USD | `-10.45%` | `749,014.00` |
| `Live` | `Long` | `0.0683` | 3,320,000.00 USD | 0.00 USD | 6,220.00 USD | `-10.32%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,310,000.00 USD | 0.00 USD | 1,290.00 USD | `-10.19%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,310,000.00 USD | 0.00 USD | 6,000.00 USD | `-10.06%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,300,000.00 USD | 0.00 USD | 455.58 USD | `-9.93%` | `6,646.00` |
| `Live` | `Long` | `0.0687` | 3,300,000.00 USD | 0.00 USD | 92,360.00 USD | `-9.80%` | `1,345,411.00` |
| `Live` | `Long` | `0.0688` | 3,210,000.00 USD | 0.00 USD | 18,800.00 USD | `-9.67%` | `273,487.00` |
| `Live` | `Long` | `0.0688` | 3,190,000.00 USD | 0.00 USD | 1,170.00 USD | `-9.53%` | `17,063.00` |
| `Live` | `Long` | `0.0689` | 3,190,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.40%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,680,000.00 USD | 0.00 USD | 3,670.00 USD | `-9.27%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,680,000.00 USD | 0.00 USD | 8,350.00 USD | `-9.14%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,670,000.00 USD | 0.00 USD | 2,160.00 USD | `-8.88%` | `31,211.00` |
| `Live` | `Long` | `0.0694` | 2,670,000.00 USD | 0.00 USD | 4,840.00 USD | `-8.75%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,660,000.00 USD | 0.00 USD | 18,020.00 USD | `-8.61%` | `259,132.00` |
| `Live` | `Long` | `0.0697` | 2,650,000.00 USD | 0.00 USD | 14,650.00 USD | `-8.48%` | `210,384.00` |
| `Live` | `Long` | `0.0698` | 2,630,000.00 USD | 0.00 USD | 3,710.00 USD | `-8.35%` | `53,161.00` |
| `Live` | `Long` | `0.0698` | 2,630,000.00 USD | 0.00 USD | 3,630.00 USD | `-8.22%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,620,000.00 USD | 0.00 USD | 1,310.00 USD | `-8.09%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,620,000.00 USD | 0.00 USD | 264.58 USD | `-7.96%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,620,000.00 USD | 0.00 USD | 1,590.00 USD | `-7.83%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,620,000.00 USD | 0.00 USD | 791.79 USD | `-7.69%` | `11,271.00` |
| `Live` | `Long` | `0.0703` | 2,620,000.00 USD | 0.00 USD | 5,060.00 USD | `-7.56%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,620,000.00 USD | 0.00 USD | 216.56 USD | `-7.43%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,620,000.00 USD | 0.00 USD | 94,410.00 USD | `-7.04%` | `1,334,448.00` |
| `Live` | `Long` | `0.0712` | 2,520,000.00 USD | 0.00 USD | 1,790.00 USD | `-6.51%` | `25,184.00` |
| `Live` | `Long` | `0.0712` | 2,520,000.00 USD | 0.00 USD | 389.38 USD | `-6.38%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,520,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-6.25%` | `24,493,121.00` |
| `Live` | `Long` | `0.0714` | 771,360.00 USD | 0.00 USD | 605.68 USD | `-6.12%` | `8,477.00` |
| `Live` | `Long` | `0.0716` | 770,750.00 USD | 0.00 USD | 8,120.00 USD | `-5.99%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 762,640.00 USD | 0.00 USD | 2,090.00 USD | `-5.85%` | `29,152.00` |
| `Live` | `Long` | `0.0717` | 760,550.00 USD | 0.00 USD | 24,930.00 USD | `-5.72%` | `347,503.00` |
| `Live` | `Long` | `0.0718` | 735,620.00 USD | 0.00 USD | 960.13 USD | `-5.59%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 734,660.00 USD | 0.00 USD | 6,600.00 USD | `-5.46%` | `91,777.00` |
| `Live` | `Long` | `0.0721` | 728,050.00 USD | 0.00 USD | 12,470.00 USD | `-5.33%` | `173,007.00` |
| `Live` | `Long` | `0.0722` | 715,590.00 USD | 0.00 USD | 22,360.00 USD | `-5.20%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 693,230.00 USD | 0.00 USD | 10,420.00 USD | `-5.07%` | `144,197.00` |
| `Live` | `Long` | `0.0723` | 682,810.00 USD | 0.00 USD | 163.73 USD | `-4.94%` | `2,263.00` |
| `Live` | `Long` | `0.0725` | 682,650.00 USD | 0.00 USD | 996.33 USD | `-4.80%` | `13,752.00` |
| `Live` | `Long` | `0.0726` | 681,650.00 USD | 0.00 USD | 260.74 USD | `-4.67%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 681,390.00 USD | 0.00 USD | 18,770.00 USD | `-4.54%` | `258,364.00` |
| `Live` | `Long` | `0.0727` | 662,620.00 USD | 0.00 USD | 50,920.00 USD | `-4.41%` | `699,906.00` |
| `Live` | `Long` | `0.0728` | 611,700.00 USD | 0.00 USD | 646.11 USD | `-4.28%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 611,060.00 USD | 0.00 USD | 72,950.00 USD | `-4.15%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 538,110.00 USD | 0.00 USD | 10,040.00 USD | `-4.02%` | `137,397.00` |
| `Live` | `Long` | `0.0732` | 528,070.00 USD | 0.00 USD | 1,930.00 USD | `-3.88%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 526,140.00 USD | 0.00 USD | 29,280.00 USD | `-3.75%` | `399,671.00` |
| `Live` | `Long` | `0.0735` | 496,870.00 USD | 0.00 USD | 3,930.00 USD | `-3.49%` | `53,459.00` |
| `Live` | `Long` | `0.0736` | 492,940.00 USD | 0.00 USD | 4,690.00 USD | `-3.36%` | `63,750.00` |
| `Live` | `Long` | `0.0736` | 488,250.00 USD | 0.00 USD | 5,490.00 USD | `-3.23%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 482,760.00 USD | 0.00 USD | 10,740.00 USD | `-3.10%` | `145,658.00` |
| `Live` | `Long` | `0.0738` | 472,020.00 USD | 0.00 USD | 314.08 USD | `-2.96%` | `4,253.00` |
| `Live` | `Long` | `0.0740` | 471,700.00 USD | 0.00 USD | 13,640.00 USD | `-2.83%` | `184,392.00` |
| `Live` | `Long` | `0.0741` | 458,070.00 USD | 0.00 USD | 455,080.00 USD | `-2.70%` | `6,145,600.00` |
| `Live` | `Long` | `0.0741` | 2,990.00 USD | 0.00 USD | 1,280.00 USD | `-2.57%` | `17,295.00` |
| `Live` | `Long` | `0.0742` | 1,700.00 USD | 0.00 USD | 1,280.00 USD | `-2.44%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 425.44 USD | 0.00 USD | 249.15 USD | `-2.31%` | `3,351.00` |
| `Live` | `Long` | `0.0745` | 176.30 USD | 0.00 USD | 176.30 USD | `-2.18%` | `2,368.00` |
| `Live` | `Short` | `0.0803` | 558.06 USD | 558.06 USD | 0.00 USD | `+5.45%` | `6,954.00` |
| `Live` | `Short` | `0.0809` | 5,090.00 USD | 4,530.00 USD | 0.00 USD | `+6.23%` | `56,000.00` |
| `Live` | `Short` | `0.0817` | 5,510.00 USD | 428.01 USD | 0.00 USD | `+7.28%` | `5,242.00` |
| `Live` | `Short` | `0.0818` | 5,760.00 USD | 241.90 USD | 0.00 USD | `+7.42%` | `2,959.00` |
| `Live` | `Short` | `0.0824` | 6,020.00 USD | 265.58 USD | 0.00 USD | `+8.20%` | `3,225.00` |
| `Live` | `Short` | `0.0832` | 9,480.00 USD | 3,450.00 USD | 0.00 USD | `+9.26%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 15,170.00 USD | 5,700.00 USD | 0.00 USD | `+9.52%` | `68,328.00` |
| `Live` | `Short` | `0.0837` | 15,460.00 USD | 293.44 USD | 0.00 USD | `+9.91%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 17,040.00 USD | 1,570.00 USD | 0.00 USD | `+10.04%` | `18,767.00` |
| `Live` | `Short` | `0.0838` | 25,000.00 USD | 7,970.00 USD | 0.00 USD | `+10.18%` | `94,998.00` |
| `Live` | `Short` | `0.0848` | 25,730.00 USD | 723.94 USD | 0.00 USD | `+11.49%` | `8,532.00` |
| `Live` | `Short` | `0.0858` | 25,840.00 USD | 115.30 USD | 0.00 USD | `+12.80%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 30,090.00 USD | 4,250.00 USD | 0.00 USD | `+12.93%` | `49,397.00` |
| `Live` | `Short` | `0.0871` | 32,610.00 USD | 2,530.00 USD | 0.00 USD | `+14.38%` | `29,021.00` |
| `Live` | `Short` | `0.0881` | 33,080.00 USD | 465.17 USD | 0.00 USD | `+15.69%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 33,490.00 USD | 411.53 USD | 0.00 USD | `+16.61%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 33,910.00 USD | 418.80 USD | 0.00 USD | `+17.01%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 34,190.00 USD | 285.70 USD | 0.00 USD | `+17.53%` | `3,194.00` |
| `Live` | `Short` | `0.0911` | 34,940.00 USD | 743.15 USD | 0.00 USD | `+19.77%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 38,980.00 USD | 4,040.00 USD | 0.00 USD | `+19.90%` | `44,324.00` |
| `Live` | `Short` | `0.0921` | 39,150.00 USD | 171.49 USD | 0.00 USD | `+20.95%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 39,960.00 USD | 805.37 USD | 0.00 USD | `+22.40%` | `8,646.00` |
| `Live` | `Short` | `0.0934` | 40,150.00 USD | 189.97 USD | 0.00 USD | `+22.66%` | `2,035.00` |
| `Live` | `Short` | `0.0935` | 42,340.00 USD | 2,190.00 USD | 0.00 USD | `+22.79%` | `23,466.00` |
| `Live` | `Short` | `0.0950` | 56,140.00 USD | 13,800.00 USD | 0.00 USD | `+24.76%` | `145,305.00` |
| `Live` | `Short` | `0.0953` | 108,050.00 USD | 51,910.00 USD | 0.00 USD | `+25.15%` | `545,000.00` |
| `Live` | `Short` | `0.0959` | 108,980.00 USD | 933.20 USD | 0.00 USD | `+25.94%` | `9,736.00` |
| `Live` | `Short` | `0.0961` | 109,590.00 USD | 609.59 USD | 0.00 USD | `+26.34%` | `6,340.00` |
| `Live` | `Short` | `0.0974` | 109,730.00 USD | 139.74 USD | 0.00 USD | `+28.05%` | `1,434.00` |
| `Live` | `Short` | `0.0983` | 110,210.00 USD | 477.50 USD | 0.00 USD | `+29.10%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 112,100.00 USD | 1,890.00 USD | 0.00 USD | `+29.36%` | `19,213.00` |
| `Live` | `Short` | `0.1014` | 119,730.00 USD | 7,630.00 USD | 0.00 USD | `+33.30%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 122,700.00 USD | 2,970.00 USD | 0.00 USD | `+33.56%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 123,190.00 USD | 492.85 USD | 0.00 USD | `+33.83%` | `4,839.00` |
| `Live` | `Short` | `0.1032` | 124,510.00 USD | 1,330.00 USD | 0.00 USD | `+35.67%` | `12,841.00` |
| `Live` | `Short` | `0.1061` | 130,620.00 USD | 6,110.00 USD | 0.00 USD | `+39.48%` | `57,554.00` |
| `Live` | `Short` | `0.1066` | 133,930.00 USD | 3,300.00 USD | 0.00 USD | `+40.00%` | `31,000.00` |
| `Live` | `Short` | `0.1076` | 134,540.00 USD | 616.19 USD | 0.00 USD | `+41.45%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 137,780.00 USD | 3,240.00 USD | 0.00 USD | `+42.63%` | `29,849.00` |
| `Live` | `Short` | `0.1125` | 139,720.00 USD | 1,930.00 USD | 0.00 USD | `+47.89%` | `17,184.00` |
| `Live` | `Short` | `0.1127` | 139,930.00 USD | 214.15 USD | 0.00 USD | `+48.02%` | `1,901.00` |
| `Live` | `Short` | `0.1128` | 143,310.00 USD | 3,380.00 USD | 0.00 USD | `+48.15%` | `29,960.00` |
| `Live` | `Short` | `0.1129` | 143,450.00 USD | 142.88 USD | 0.00 USD | `+48.41%` | `1,265.00` |
| `Live` | `Short` | `0.1163` | 143,610.00 USD | 152.42 USD | 0.00 USD | `+52.88%` | `1,310.00` |
| `Live` | `Short` | `0.1187` | 143,710.00 USD | 106.19 USD | 0.00 USD | `+55.90%` | `895.00` |
| `Live` | `Short` | `0.1222` | 144,510.00 USD | 796.83 USD | 0.00 USD | `+60.63%` | `6,518.00` |
| `Live` | `Short` | `0.1262` | 144,630.00 USD | 121.73 USD | 0.00 USD | `+65.76%` | `965.00` |
| `Live` | `Short` | `0.1270` | 144,740.00 USD | 108.80 USD | 0.00 USD | `+66.81%` | `857.00` |
| `Live` | `Short` | `0.1288` | 146,300.00 USD | 1,560.00 USD | 0.00 USD | `+69.30%` | `12,089.00` |
| `Live` | `Short` | `0.1290` | 147,230.00 USD | 930.89 USD | 0.00 USD | `+69.43%` | `7,219.00` |
| `Live` | `Short` | `0.1296` | 147,400.00 USD | 171.66 USD | 0.00 USD | `+70.35%` | `1,324.00` |
| `Live` | `Short` | `0.1310` | 148,600.00 USD | 1,200.00 USD | 0.00 USD | `+72.19%` | `9,176.00` |
| `Live` | `Short` | `0.1311` | 150,740.00 USD | 2,140.00 USD | 0.00 USD | `+72.33%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 150,840.00 USD | 102.97 USD | 0.00 USD | `+73.25%` | `781.00` |
| `Live` | `Short` | `0.1338` | 151,050.00 USD | 205.31 USD | 0.00 USD | `+75.74%` | `1,535.00` |
| `Live` | `Short` | `0.1343` | 185,760.00 USD | 34,710.00 USD | 0.00 USD | `+76.53%` | `258,360.00` |
| `Live` | `Short` | `0.1368` | 185,890.00 USD | 134.97 USD | 0.00 USD | `+79.68%` | `987.00` |
| `Live` | `Short` | `0.1404` | 186,560.00 USD | 663.63 USD | 0.00 USD | `+84.55%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 215,580.00 USD | 29,030.00 USD | 0.00 USD | `+85.33%` | `205,781.00` |
| `Live` | `Short` | `0.1432` | 217,450.00 USD | 1,860.00 USD | 0.00 USD | `+88.22%` | `13,010.00` |
| `Live` | `Short` | `0.1441` | 217,640.00 USD | 196.63 USD | 0.00 USD | `+89.28%` | `1,365.00` |
| `Live` | `Short` | `0.1442` | 218,080.00 USD | 432.45 USD | 0.00 USD | `+89.41%` | `3,000.00` |
| `Live` | `Short` | `0.1444` | 219,620.00 USD | 1,540.00 USD | 0.00 USD | `+89.67%` | `10,691.00` |
| `Live` | `Short` | `0.1457` | 3,270,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+91.51%` | `20,910,149.00` |
| `Live` | `Short` | `0.1475` | 3,270,000.00 USD | 1,950.00 USD | 0.00 USD | `+93.87%` | `13,240.00` |
| `Live` | `Short` | `0.1479` | 3,280,000.00 USD | 8,300.00 USD | 0.00 USD | `+94.27%` | `56,144.00` |
| `Live` | `Short` | `0.1510` | 3,280,000.00 USD | 140.23 USD | 0.00 USD | `+98.34%` | `929.00` |
| `Live` | `Short` | `0.1515` | 3,290,000.00 USD | 11,500.00 USD | 0.00 USD | `+99.00%` | `75,941.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 517,800.00 USD | 0.00 USD | 375.42 USD | `-66.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 517,430.00 USD | 0.00 USD | 409.59 USD | `-47.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 517,020.00 USD | 0.00 USD | 132.68 USD | `-46.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 516,880.00 USD | 0.00 USD | 788.27 USD | `-45.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 516,100.00 USD | 0.00 USD | 527.05 USD | `-45.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 515,570.00 USD | 0.00 USD | 286.87 USD | `-40.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 515,280.00 USD | 0.00 USD | 252.42 USD | `-39.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 515,030.00 USD | 0.00 USD | 468.67 USD | `-38.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 514,560.00 USD | 0.00 USD | 5,160.00 USD | `-35.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 509,400.00 USD | 0.00 USD | 920.48 USD | `-35.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 508,480.00 USD | 0.00 USD | 1,730.00 USD | `-34.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 506,750.00 USD | 0.00 USD | 175.41 USD | `-32.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 506,580.00 USD | 0.00 USD | 2,670.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 503,900.00 USD | 0.00 USD | 1,370.00 USD | `-27.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 502,530.00 USD | 0.00 USD | 437.58 USD | `-26.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 502,090.00 USD | 0.00 USD | 752.54 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 501,340.00 USD | 0.00 USD | 9,830.00 USD | `-22.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 491,510.00 USD | 0.00 USD | 1,020.00 USD | `-22.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 490,490.00 USD | 0.00 USD | 668.84 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 489,820.00 USD | 0.00 USD | 8,800.00 USD | `-20.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 481,020.00 USD | 0.00 USD | 504.26 USD | `-18.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 480,520.00 USD | 0.00 USD | 2,280.00 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 478,240.00 USD | 0.00 USD | 1,280.00 USD | `-18.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 476,960.00 USD | 0.00 USD | 920.18 USD | `-15.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 476,040.00 USD | 0.00 USD | 412.42 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 475,630.00 USD | 0.00 USD | 1,130.00 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 474,500.00 USD | 0.00 USD | 362.24 USD | `-14.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 474,140.00 USD | 0.00 USD | 3,140.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 471,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 469,900.00 USD | 0.00 USD | 1,200.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 468,700.00 USD | 0.00 USD | 996.31 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 467,710.00 USD | 0.00 USD | 632.88 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 467,070.00 USD | 0.00 USD | 115.57 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 466,960.00 USD | 0.00 USD | 33,620.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 433,330.00 USD | 0.00 USD | 12,860.00 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 420,470.00 USD | 0.00 USD | 1,260.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 419,210.00 USD | 0.00 USD | 108.08 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 419,100.00 USD | 0.00 USD | 21,550.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 397,550.00 USD | 0.00 USD | 1,430.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 396,120.00 USD | 0.00 USD | 7,990.00 USD | `-10.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 388,130.00 USD | 0.00 USD | 8,580.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 379,550.00 USD | 0.00 USD | 606.47 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 378,940.00 USD | 0.00 USD | 345.95 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 378,600.00 USD | 0.00 USD | 38,710.00 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 339,890.00 USD | 0.00 USD | 660.06 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 339,230.00 USD | 0.00 USD | 102.34 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 339,130.00 USD | 0.00 USD | 1,120.00 USD | `-8.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 338,010.00 USD | 0.00 USD | 144.59 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 337,870.00 USD | 0.00 USD | 925.29 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 336,940.00 USD | 0.00 USD | 697.50 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 336,240.00 USD | 0.00 USD | 17,520.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 318,720.00 USD | 0.00 USD | 1,800.00 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 316,920.00 USD | 0.00 USD | 523.23 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 316,400.00 USD | 0.00 USD | 235.12 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 316,160.00 USD | 0.00 USD | 204.40 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 315,960.00 USD | 0.00 USD | 107,720.00 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 208,240.00 USD | 0.00 USD | 12,930.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 195,300.00 USD | 0.00 USD | 20,070.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 175,230.00 USD | 0.00 USD | 608.76 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 174,630.00 USD | 0.00 USD | 16,880.00 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 157,750.00 USD | 0.00 USD | 1,670.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 156,080.00 USD | 0.00 USD | 4,710.00 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 151,370.00 USD | 0.00 USD | 8,430.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 142,930.00 USD | 0.00 USD | 413.42 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 142,520.00 USD | 0.00 USD | 881.82 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 141,640.00 USD | 0.00 USD | 703.43 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 140,930.00 USD | 0.00 USD | 621.12 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 140,310.00 USD | 0.00 USD | 1,430.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 138,880.00 USD | 0.00 USD | 29,060.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 109,820.00 USD | 0.00 USD | 4,500.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 105,310.00 USD | 0.00 USD | 2,090.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 103,220.00 USD | 0.00 USD | 23,870.00 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 79,350.00 USD | 0.00 USD | 28,640.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 50,710.00 USD | 0.00 USD | 2,710.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 48,010.00 USD | 0.00 USD | 115.12 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 47,890.00 USD | 0.00 USD | 4,680.00 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 43,210.00 USD | 0.00 USD | 1,000.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 42,210.00 USD | 0.00 USD | 2,900.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 39,320.00 USD | 0.00 USD | 107.66 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 39,210.00 USD | 0.00 USD | 1,720.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 37,490.00 USD | 0.00 USD | 3,110.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 34,380.00 USD | 0.00 USD | 375.86 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 34,010.00 USD | 0.00 USD | 193.90 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 33,810.00 USD | 0.00 USD | 140.04 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 33,670.00 USD | 0.00 USD | 21,990.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 11,680.00 USD | 0.00 USD | 3,450.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 8,230.00 USD | 0.00 USD | 736.17 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 7,490.00 USD | 0.00 USD | 398.60 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 7,090.00 USD | 0.00 USD | 465.39 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 6,630.00 USD | 0.00 USD | 358.13 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 6,270.00 USD | 0.00 USD | 4,880.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 1,390.00 USD | 0.00 USD | 193.49 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 1,200.00 USD | 0.00 USD | 398.13 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 797.92 USD | 0.00 USD | 797.92 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 806.81 USD | 806.81 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 1,170.00 USD | 359.60 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 1,500.00 USD | 335.56 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 1,610.00 USD | 109.63 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 1,820.00 USD | 203.47 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 5,350.00 USD | 3,540.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 5,520.00 USD | 168.24 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 5,820.00 USD | 297.49 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 6,640.00 USD | 816.05 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 22,030.00 USD | 15,400.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 26,020.00 USD | 3,980.00 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 29,910.00 USD | 3,900.00 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 33,730.00 USD | 3,820.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 33,950.00 USD | 215.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 34,360.00 USD | 406.98 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 35,850.00 USD | 1,490.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 36,260.00 USD | 407.72 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 77,700.00 USD | 41,440.00 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 78,520.00 USD | 817.77 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 80,520.00 USD | 2,010.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 81,870.00 USD | 1,350.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 82,090.00 USD | 222.46 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 86,460.00 USD | 4,370.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 86,860.00 USD | 396.49 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 102,650.00 USD | 15,790.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 144,070.00 USD | 41,420.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 147,100.00 USD | 3,030.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 147,400.00 USD | 303.73 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 148,970.00 USD | 1,560.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 151,330.00 USD | 2,360.00 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 155,920.00 USD | 4,600.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 158,180.00 USD | 2,260.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 159,190.00 USD | 1,010.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 159,340.00 USD | 148.25 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 159,900.00 USD | 556.77 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 160,030.00 USD | 125.45 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 160,260.00 USD | 230.40 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 160,570.00 USD | 319.16 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 161,580.00 USD | 1,010.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 184,330.00 USD | 22,750.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 184,730.00 USD | 400.91 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 184,930.00 USD | 200.46 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 185,190.00 USD | 259.13 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 185,900.00 USD | 707.08 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 186,940.00 USD | 1,050.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 283,720.00 USD | 96,780.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 284,530.00 USD | 807.50 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 284,790.00 USD | 257.18 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 285,210.00 USD | 424.74 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 285,320.00 USD | 101.80 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 286,700.00 USD | 1,380.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 286,960.00 USD | 264.63 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 288,400.00 USD | 1,430.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 288,530.00 USD | 129.67 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 289,550.00 USD | 1,020.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 291,990.00 USD | 2,450.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 293,020.00 USD | 1,030.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 295,630.00 USD | 2,610.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 295,960.00 USD | 327.80 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 296,560.00 USD | 607.58 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 303,450.00 USD | 6,880.00 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 304,250.00 USD | 800.79 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 304,760.00 USD | 512.05 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 305,000.00 USD | 240.26 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 305,390.00 USD | 389.31 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 306,100.00 USD | 706.02 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 306,400.00 USD | 303.56 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 306,510.00 USD | 112.89 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 306,890.00 USD | 381.45 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 307,050.00 USD | 155.82 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 308,480.00 USD | 1,430.00 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 308,620.00 USD | 138.69 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 309,880.00 USD | 1,260.00 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 309,990.00 USD | 107.03 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,060,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,060,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,060,000.00 USD | 341.34 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,060,000.00 USD | 107.71 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,070,000.00 USD | 2,690.00 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,070,000.00 USD | 1,440.00 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,070,000.00 USD | 219.07 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,070,000.00 USD | 326.97 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,070,000.00 USD | 242.84 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,080,000.00 USD | 13,510.00 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 2,080,000.00 USD | 152.92 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,080,000.00 USD | 876.11 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,080,000.00 USD | 205.59 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,080,000.00 USD | 126.76 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,080,000.00 USD | 307.41 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,090,000.00 USD | 614.09 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,090,000.00 USD | 644.62 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 2,090,000.00 USD | 180.45 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,090,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,130,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,130,000.00 USD | 1,080.00 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,130,000.00 USD | 384.06 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,140,000.00 USD | 1,840.00 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,140,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,140,000.00 USD | 117.71 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,140,000.00 USD | 111.61 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,140,000.00 USD | 571.18 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,140,000.00 USD | 375.94 USD | 0.00 USD | `+15.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,140,000.00 USD | 627.55 USD | 0.00 USD | `+16.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,140,000.00 USD | 211.04 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,140,000.00 USD | 108.36 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,140,000.00 USD | 543.32 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,140,000.00 USD | 1,820.00 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,140,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,160,000.00 USD | 17,680.00 USD | 0.00 USD | `+17.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,160,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,170,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,170,000.00 USD | 5,630.00 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,170,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,170,000.00 USD | 224.86 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,190,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,190,000.00 USD | 114.93 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,190,000.00 USD | 679.12 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,190,000.00 USD | 173.36 USD | 0.00 USD | `+19.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,200,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,200,000.00 USD | 1,580.00 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,200,000.00 USD | 2,300.00 USD | 0.00 USD | `+21.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,200,000.00 USD | 541.32 USD | 0.00 USD | `+21.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,340,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,340,000.00 USD | 691.07 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,340,000.00 USD | 6,250.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,360,000.00 USD | 13,480.00 USD | 0.00 USD | `+21.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,360,000.00 USD | 734.82 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,360,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,360,000.00 USD | 184.09 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,360,000.00 USD | 1,120.00 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,360,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,360,000.00 USD | 512.15 USD | 0.00 USD | `+23.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,370,000.00 USD | 6,620.00 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,370,000.00 USD | 404.96 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,370,000.00 USD | 129.85 USD | 0.00 USD | `+25.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,370,000.00 USD | 3,740.00 USD | 0.00 USD | `+25.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,380,000.00 USD | 2,400.00 USD | 0.00 USD | `+26.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,380,000.00 USD | 409.17 USD | 0.00 USD | `+26.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,380,000.00 USD | 203.74 USD | 0.00 USD | `+26.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,380,000.00 USD | 2,800.00 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,380,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,380,000.00 USD | 694.56 USD | 0.00 USD | `+28.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,380,000.00 USD | 940.91 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,390,000.00 USD | 2,980.00 USD | 0.00 USD | `+30.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,390,000.00 USD | 104.99 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,390,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,390,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,390,000.00 USD | 1,090.00 USD | 0.00 USD | `+30.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,390,000.00 USD | 438.96 USD | 0.00 USD | `+30.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,390,000.00 USD | 973.76 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,500,000.00 USD | 111,100.00 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,500,000.00 USD | 175.59 USD | 0.00 USD | `+31.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,500,000.00 USD | 482.89 USD | 0.00 USD | `+32.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,500,000.00 USD | 201.90 USD | 0.00 USD | `+32.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,510,000.00 USD | 489.46 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,510,000.00 USD | 103.68 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,510,000.00 USD | 203.70 USD | 0.00 USD | `+33.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,510,000.00 USD | 3,810.00 USD | 0.00 USD | `+33.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,520,000.00 USD | 11,200.00 USD | 0.00 USD | `+34.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,520,000.00 USD | 4,330.00 USD | 0.00 USD | `+34.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,520,000.00 USD | 205.50 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,530,000.00 USD | 3,490.00 USD | 0.00 USD | `+35.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,530,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,530,000.00 USD | 207.50 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,530,000.00 USD | 813.88 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,550,000.00 USD | 23,160.00 USD | 0.00 USD | `+37.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,550,000.00 USD | 781.51 USD | 0.00 USD | `+37.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,550,000.00 USD | 209.30 USD | 0.00 USD | `+37.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,560,000.00 USD | 1,440.00 USD | 0.00 USD | `+37.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,560,000.00 USD | 5,140.00 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,560,000.00 USD | 585.32 USD | 0.00 USD | `+38.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,560,000.00 USD | 210.90 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,560,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,560,000.00 USD | 105.75 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,570,000.00 USD | 3,220.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,570,000.00 USD | 1,600.00 USD | 0.00 USD | `+39.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,570,000.00 USD | 212.90 USD | 0.00 USD | `+39.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,570,000.00 USD | 472.63 USD | 0.00 USD | `+40.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,570,000.00 USD | 214.50 USD | 0.00 USD | `+40.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,570,000.00 USD | 1,040.00 USD | 0.00 USD | `+41.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,570,000.00 USD | 136.12 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,570,000.00 USD | 216.10 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,610,000.00 USD | 40,920.00 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,610,000.00 USD | 217.90 USD | 0.00 USD | `+43.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,610,000.00 USD | 219.70 USD | 0.00 USD | `+44.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,620,000.00 USD | 7,920.00 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,620,000.00 USD | 154.22 USD | 0.00 USD | `+45.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,620,000.00 USD | 221.30 USD | 0.00 USD | `+45.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,620,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,650,000.00 USD | 24,440.00 USD | 0.00 USD | `+45.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,650,000.00 USD | 223.10 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,650,000.00 USD | 2,120.00 USD | 0.00 USD | `+47.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,650,000.00 USD | 226.30 USD | 0.00 USD | `+48.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,650,000.00 USD | 351.57 USD | 0.00 USD | `+49.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,650,000.00 USD | 950.34 USD | 0.00 USD | `+49.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,650,000.00 USD | 229.50 USD | 0.00 USD | `+50.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,650,000.00 USD | 771.08 USD | 0.00 USD | `+51.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,650,000.00 USD | 230.90 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,650,000.00 USD | 288.18 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,650,000.00 USD | 619.10 USD | 0.00 USD | `+52.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,650,000.00 USD | 1,250.00 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,650,000.00 USD | 1,050.00 USD | 0.00 USD | `+52.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,660,000.00 USD | 232.30 USD | 0.00 USD | `+52.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,660,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,660,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,660,000.00 USD | 3,730.00 USD | 0.00 USD | `+54.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,660,000.00 USD | 676.22 USD | 0.00 USD | `+54.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,660,000.00 USD | 648.25 USD | 0.00 USD | `+54.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,660,000.00 USD | 1,510.00 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,660,000.00 USD | 448.52 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,660,000.00 USD | 136.93 USD | 0.00 USD | `+55.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,660,000.00 USD | 124.58 USD | 0.00 USD | `+55.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,670,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,670,000.00 USD | 691.80 USD | 0.00 USD | `+57.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,780,000.00 USD | 117,860.00 USD | 0.00 USD | `+57.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,780,000.00 USD | 143.22 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,790,000.00 USD | 803.95 USD | 0.00 USD | `+58.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,790,000.00 USD | 1,380.00 USD | 0.00 USD | `+59.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,790,000.00 USD | 2,270.00 USD | 0.00 USD | `+60.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,790,000.00 USD | 871.99 USD | 0.00 USD | `+60.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,810,000.00 USD | 24,560.00 USD | 0.00 USD | `+66.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,810,000.00 USD | 400.21 USD | 0.00 USD | `+66.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,830,000.00 USD | 13,850.00 USD | 0.00 USD | `+73.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,830,000.00 USD | 2,360.00 USD | 0.00 USD | `+73.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,840,000.00 USD | 4,160.00 USD | 0.00 USD | `+78.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,840,000.00 USD | 114.70 USD | 0.00 USD | `+79.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,840,000.00 USD | 257.51 USD | 0.00 USD | `+83.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,840,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,840,000.00 USD | 173.57 USD | 0.00 USD | `+86.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,840,000.00 USD | 380.09 USD | 0.00 USD | `+86.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,850,000.00 USD | 17,150.00 USD | 0.00 USD | `+87.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,860,000.00 USD | 433.35 USD | 0.00 USD | `+89.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,860,000.00 USD | 3,640.00 USD | 0.00 USD | `+93.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,910,000.00 USD | 55,720.00 USD | 0.00 USD | `+94.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,920,000.00 USD | 2,120.00 USD | 0.00 USD | `+94.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,940,000.00 USD | 18,810.00 USD | 0.00 USD | `+97.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,940,000.00 USD | 1,620.00 USD | 0.00 USD | `+98.87%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0673` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0675` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 0.00 USD | 5,530.00 USD | 0.00 USD |
| `1D` | `0.0676` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 45,230.00 USD | 24,730.00 USD | 0.00 USD |
| `1D` | `0.0678` | 11,090,000.00 USD | 0.00 USD | 11,090,000.00 USD | 3,200.00 USD | 39,890.00 USD | 56,870.00 USD |
| `1D` | `0.0679` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD |
| `1D` | `0.0681` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 133,250.00 USD |
| `1D` | `0.0682` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,330.00 USD |
| `1D` | `0.0683` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 0.00 USD | 4,790.00 USD | 0.00 USD |
| `1D` | `0.0684` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 24,150.00 USD | 13,610.00 USD | 0.00 USD |
| `1D` | `0.0685` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 41,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0686` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 41,080.00 USD | 1,410.00 USD | 9,400.00 USD |
| `1D` | `0.0687` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 0.00 USD | 16,550.00 USD | 14,970.00 USD |
| `1D` | `0.0688` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0691` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD |
| `1D` | `0.0698` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,750.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,890.00 USD |
| `1D` | `0.0700` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 35,400.00 USD | 18,030.00 USD | 27,460.00 USD |
| `1D` | `0.0702` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 78,740.00 USD | 36,780.00 USD | 81.08 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 87,540.00 USD | 31,470.00 USD | 39,830.00 USD |
| `1D` | `0.0704` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,040.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 34,530.00 USD | 24,910.00 USD | 32,250.00 USD |
| `1D` | `0.0706` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 36,930.00 USD | 29,080.00 USD | 25,510.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 54,240.00 USD | 21,680.00 USD | 22,770.00 USD |
| `1D` | `0.0708` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 36,740.00 USD | 37,120.00 USD | 14,100.00 USD |
| `1D` | `0.0710` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 21,430.00 USD | 9,300.00 USD | 36,520.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 27,890.00 USD | 8,560.00 USD | 45,560.00 USD |
| `1D` | `0.0712` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,580.00 USD |
| `1D` | `0.0714` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 34,440.00 USD | 8,830.00 USD | 36,170.00 USD |
| `1D` | `0.0716` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 30,130.00 USD | 31,610.00 USD | 2,110.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 17,330.00 USD | 7,710.00 USD | 21,780.00 USD |
| `1D` | `0.0718` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 64,240.00 USD | 31,390.00 USD | 32,350.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 20,100.00 USD | 2,950.00 USD | 7,770.00 USD |
| `1D` | `0.0720` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 31,160.00 USD | 29,440.00 USD | 31,670.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 136,510.00 USD | 76,220.00 USD | 12,790.00 USD |
| `1D` | `0.0722` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 43,930.00 USD | 15,630.00 USD | 21,710.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 54,790.00 USD | 162,040.00 USD | 152,400.00 USD |
| `1D` | `0.0724` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 27,830.00 USD | 87,980.00 USD | 97,290.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 47,840.00 USD | 22,980.00 USD | 23,510.00 USD |
| `1D` | `0.0726` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 40,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 168,660.00 USD | 0.00 USD | 333,380.00 USD |
| `1D` | `0.0728` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 66,510.00 USD | 85,670.00 USD | 74,500.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 19,510.00 USD | 13,330.00 USD | 21,430.00 USD |
| `1D` | `0.0730` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 112,200.00 USD | 36,430.00 USD | 0.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 152,870.00 USD | 17,510.00 USD | 1,570.00 USD |
| `1D` | `0.0732` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 147,060.00 USD | 60,240.00 USD | 61,020.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 15,550.00 USD | 0.00 USD | 70,160.00 USD |
| `1D` | `0.0734` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 43,340.00 USD | 0.00 USD | 0.29 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 33,390.00 USD | 31,100.00 USD | 0.00 USD |
| `1D` | `0.0736` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 234,720.00 USD | 123,630.00 USD | 1,410.00 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 51,890.00 USD | 42,510.00 USD | 572.02 USD |
| `1D` | `0.0738` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,430.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,830.00 USD |
| `1D` | `0.0740` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 33,740.00 USD | 0.00 USD | 348.56 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 36,980.00 USD | 0.00 USD | 247.44 USD |
| `1D` | `0.0742` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 286,340.00 USD | 0.00 USD | 666,250.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 118,640.00 USD | 234,470.00 USD | 189,860.00 USD |
| `1D` | `0.0744` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 19,880.00 USD | 49,540.00 USD | 39,850.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 199,850.00 USD | 130,070.00 USD | 26,320.00 USD |
| `1D` | `0.0746` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 371,240.00 USD | 210,430.00 USD | 125,120.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 466,980.00 USD | 159,330.00 USD | 99,290.00 USD |
| `1D` | `0.0748` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 130,290.00 USD | 143,100.00 USD | 173,730.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 652,990.00 USD | 0.00 USD | 652,990.00 USD | 203,330.00 USD | 0.00 USD | 148,650.00 USD |
| `1D` | `0.0750` | 301,020.00 USD | 0.00 USD | 301,020.00 USD | 69,890.00 USD | 0.00 USD | 120,870.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 110,270.00 USD | 0.00 USD | 110,270.00 USD | 0.00 USD | 6,860.00 USD | 55.02 USD |
| `1D` | `0.0752` | 103,360.00 USD | 0.00 USD | 103,360.00 USD | 0.00 USD | 0.00 USD | 507.67 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 102,850.00 USD | 0.00 USD | 102,850.00 USD | 0.00 USD | 85,010.00 USD | 420.78 USD |
| `1D` | `0.0754` | 17,420.00 USD | 0.00 USD | 17,420.00 USD | 0.00 USD | 0.00 USD | 253.71 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0756` | 17,160.00 USD | 0.00 USD | 17,160.00 USD | 0.00 USD | 0.00 USD | 0.51 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 17,160.00 USD | 0.00 USD | 17,160.00 USD | 0.00 USD | 0.00 USD | 100.20 USD |
| `1D` | `0.0758` | 17,060.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 0.00 USD | 68.78 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 16,990.00 USD | 0.00 USD | 16,990.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD |
| `1D` | `0.0760` | 15,200.00 USD | 0.00 USD | 15,200.00 USD | 0.00 USD | 0.00 USD | 582.68 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 14,620.00 USD | 0.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | 850.68 USD |
| `1D` | `0.0762` | 13,770.00 USD | 0.00 USD | 13,770.00 USD | 0.00 USD | 0.00 USD | 551.79 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 13,220.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD |
| `1D` | `0.0764` | 326,310.00 USD | 326,310.00 USD | 0.00 USD | 0.00 USD | 325,960.00 USD | 352.16 USD |
| `1D` | `0.0764` | 652,630.00 USD | 652,630.00 USD | 0.00 USD | 0.00 USD | 325,960.00 USD | 352.16 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 910,340.00 USD | 910,340.00 USD | 0.00 USD | 0.00 USD | 257,590.00 USD | 125.25 USD |
| `1D` | `0.0766` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 765,870.00 USD | 360,800.00 USD | 0.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 211,710.00 USD | 199,540.00 USD | 0.00 USD |
| `1D` | `0.0768` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 357,460.00 USD | 0.00 USD | 513,840.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 181,440.00 USD | 341,350.00 USD | 148,860.00 USD |
| `1D` | `0.0770` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 272,760.00 USD | 93,300.00 USD | 254,140.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 216,410.00 USD | 232,340.00 USD | 212,270.00 USD |
| `1D` | `0.0772` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 286,340.00 USD | 0.00 USD | 666,690.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 65,160.00 USD | 169,730.00 USD | 148,750.00 USD |
| `1D` | `0.0774` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD | 26,660.00 USD | 0.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 155,740.00 USD | 72,850.00 USD | 0.00 USD |
| `1D` | `0.0776` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 190,100.00 USD | 47,010.00 USD | 0.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 205,390.00 USD | 264,690.00 USD | 47,950.00 USD |
| `1D` | `0.0778` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 16,790.00 USD | 202,930.00 USD | 275,210.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 85,950.00 USD | 140,320.00 USD |
| `1D` | `0.0780` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 69,890.00 USD | 31,980.00 USD | 0.00 USD |
| `1D` | `0.0781` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 113,060.00 USD | 68,670.00 USD | 0.00 USD |
| `1D` | `0.0782` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 8,010.00 USD | 184,740.00 USD | 142,180.00 USD |
| `1D` | `0.0784` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 179,570.00 USD | 117,040.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 298,820.00 USD | 307,550.00 USD | 333,120.00 USD |
| `1D` | `0.0788` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 75,490.00 USD | 181,170.00 USD | 74,380.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 234,900.00 USD | 123,220.00 USD | 82,210.00 USD |
| `1D` | `0.0790` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 102,120.00 USD | 39,680.00 USD | 0.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 152,950.00 USD | 63,280.00 USD | 50,750.00 USD |
| `1D` | `0.0792` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 104,950.00 USD | 18,870.00 USD | 23,510.00 USD |
| `1D` | `0.0794` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 75,420.00 USD | 41,370.00 USD | 37,430.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 10,150.00 USD | 0.00 USD | 70,160.00 USD |
| `1D` | `0.0796` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 191,110.00 USD | 89,760.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 51,440.00 USD | 164,620.00 USD | 1,410.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 191,450.00 USD | 193,600.00 USD | 196,780.00 USD |
| `1D` | `0.0800` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 4,510.00 USD | 5,610.00 USD | 98,580.00 USD |
| `1D` | `0.0802` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 36,660.00 USD |
| `1D` | `0.0804` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 56,220.00 USD | 37,230.00 USD | 43,920.00 USD |
| `1D` | `0.0806` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 214,730.00 USD | 208,070.00 USD | 41,410.00 USD |
| `1D` | `0.0808` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 419,500.00 USD | 131,030.00 USD | 522,160.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 477,790.00 USD | 336,610.00 USD | 12,350.00 USD |
| `1D` | `0.0810` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 293,220.00 USD | 180,540.00 USD | 132,170.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 83,280.00 USD | 241,410.00 USD | 202.70 USD |
| `1D` | `0.0812` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 144,600.00 USD | 99,490.00 USD | 137,330.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 49,290.00 USD | 23,210.00 USD | 212,400.00 USD |
| `1D` | `0.0814` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 25,120.00 USD | 79,960.00 USD | 292,790.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 233,650.00 USD | 95,270.00 USD | 159,930.00 USD |
| `1D` | `0.0816` | 20,420,000.00 USD | 20,420,000.00 USD | 0.00 USD | 360,380.00 USD | 194,790.00 USD | 177,750.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 301,230.00 USD | 127,050.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 21,720,000.00 USD | 21,720,000.00 USD | 0.00 USD | 269,340.00 USD | 161,260.00 USD | 310,440.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 22,340,000.00 USD | 22,340,000.00 USD | 0.00 USD | 174,640.00 USD | 312,480.00 USD | 128,390.00 USD |
| `1D` | `0.0820` | 23,020,000.00 USD | 23,020,000.00 USD | 0.00 USD | 136,010.00 USD | 202,840.00 USD | 343,910.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 23,480,000.00 USD | 23,480,000.00 USD | 0.00 USD | 210,590.00 USD | 79,630.00 USD | 170,450.00 USD |
| `1D` | `0.0822` | 24,070,000.00 USD | 24,070,000.00 USD | 0.00 USD | 262,170.00 USD | 169,200.00 USD | 155,950.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 24,420,000.00 USD | 24,420,000.00 USD | 0.00 USD | 270,850.00 USD | 75,420.00 USD | 8,720.00 USD |
| `1D` | `0.0824` | 25,000,000.00 USD | 25,000,000.00 USD | 0.00 USD | 151,910.00 USD | 226,510.00 USD | 199,270.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 25,280,000.00 USD | 25,280,000.00 USD | 0.00 USD | 127,790.00 USD | 122,020.00 USD | 27,800.00 USD |
| `1D` | `0.0826` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 150,570.00 USD | 84,820.00 USD | 190,220.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 25,800,000.00 USD | 25,800,000.00 USD | 0.00 USD | 52,670.00 USD | 48,230.00 USD | 0.00 USD |
| `1D` | `0.0828` | 26,170,000.00 USD | 26,170,000.00 USD | 0.00 USD | 225,780.00 USD | 75,940.00 USD | 64,660.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 26,550,000.00 USD | 26,550,000.00 USD | 0.00 USD | 201,220.00 USD | 111,290.00 USD | 72,360.00 USD |
| `1D` | `0.0830` | 26,910,000.00 USD | 26,910,000.00 USD | 0.00 USD | 169,540.00 USD | 84,690.00 USD | 97,880.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 27,040,000.00 USD | 27,040,000.00 USD | 0.00 USD | 81,580.00 USD | 11,280.00 USD | 43,650.00 USD |
| `1D` | `0.0832` | 27,360,000.00 USD | 27,360,000.00 USD | 0.00 USD | 172,190.00 USD | 66,230.00 USD | 79,760.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 27,700,000.00 USD | 27,700,000.00 USD | 0.00 USD | 119,590.00 USD | 55,260.00 USD | 165,230.00 USD |
| `1D` | `0.0834` | 28,050,000.00 USD | 28,050,000.00 USD | 0.00 USD | 127,020.00 USD | 94,190.00 USD | 126,910.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 0.00 USD | 107,580.00 USD | 161,030.00 USD | 64,140.00 USD |
| `1D` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 0.00 USD | 48,890.00 USD | 61,760.00 USD | 144,530.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 28,830,000.00 USD | 28,830,000.00 USD | 0.00 USD | 136,710.00 USD | 17,710.00 USD | 33,700.00 USD |
| `1D` | `0.0838` | 29,110,000.00 USD | 29,110,000.00 USD | 0.00 USD | 179,510.00 USD | 70,030.00 USD | 34,780.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 29,190,000.00 USD | 29,190,000.00 USD | 0.00 USD | 49,420.00 USD | 16,550.00 USD | 16,760.00 USD |
| `1D` | `0.0840` | 29,250,000.00 USD | 29,250,000.00 USD | 0.00 USD | 13,720.00 USD | 15,480.00 USD | 28,060.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 29,280,000.00 USD | 29,280,000.00 USD | 0.00 USD | 23,380.00 USD | 2,010.00 USD | 850.68 USD |
| `1D` | `0.0842` | 29,350,000.00 USD | 29,350,000.00 USD | 0.00 USD | 22,710.00 USD | 0.00 USD | 46,940.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 29,380,000.00 USD | 29,380,000.00 USD | 0.00 USD | 33,600.00 USD | 0.00 USD | 41.24 USD |
| `1D` | `0.0844` | 29,460,000.00 USD | 29,460,000.00 USD | 0.00 USD | 79,050.00 USD | 0.00 USD | 352.16 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 29,480,000.00 USD | 29,480,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | 349.44 USD |
| `1D` | `0.0846` | 29,570,000.00 USD | 29,570,000.00 USD | 0.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 85.28 USD |
| `1D` | `0.0848` | 29,590,000.00 USD | 29,590,000.00 USD | 0.00 USD | 11,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0849` | 29,600,000.00 USD | 29,600,000.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0850` | 29,610,000.00 USD | 29,610,000.00 USD | 0.00 USD | 14,840.00 USD | 0.00 USD | 75.11 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0851` | 29,690,000.00 USD | 29,690,000.00 USD | 0.00 USD | 35,100.00 USD | 24,590.00 USD | 16,440.00 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0853` | 29,700,000.00 USD | 29,700,000.00 USD | 0.00 USD | 860.43 USD | 737.47 USD | 9,890.00 USD |
| `1D` | `0.0854` | 29,730,000.00 USD | 29,730,000.00 USD | 0.00 USD | 14,260.00 USD | 9,580.00 USD | 9,610.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
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
  * Total Open Interest: `1.09B` | Total OI Tokens: `14,224,946,665.7 DOGE`
  * 1h OI Change: `+0.16%` | 4h OI Change: `-2.16%` | 24h OI Change: `-5.13%`
  * Exchange Breakdown: Binance=`255.70M` | Bybit=`108.29M` | OKX=`108.46M` | Hyperliquid=`76.77M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.08K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0063%` | **USDT OKX** | `0.0055%` |
| **USDT Bybit** | `-0.0115%` | **USDT KuCoin** | `-0.0003%` |
| **USDT MEXC** | `0.0065%` | **USDT BingX** | `0.0071%` |
| **USDT Gate** | `-0.0013%` | **USDT Bitget** | `0.0001%` |
| **CoinM Binance** | `0.0070%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `47.74%` | `52.26%` | `0.91` | 66,200,000.00 USD |
| `15M` | `Binance` | `50.63%` | `49.37%` | `1.03` | 40,670,000.00 USD |
| `15M` | `OKX` | `53.23%` | `46.77%` | `1.14` | 5,880,000.00 USD |
| `15M` | `Bybit` | `39.38%` | `60.62%` | `0.65` | 6,230,000.00 USD |
| `15M` | `KuCoin` | `44.45%` | `55.55%` | `0.80` | 157,460.00 USD |
| `15M` | `Gate` | `45.42%` | `54.58%` | `0.83` | 885,980.00 USD |
| `15M` | `Bitget` | `48.7%` | `51.3%` | `0.95` | 1,380,000.00 USD |
| `15M` | `BingX` | `41.4%` | `58.6%` | `0.71` | 754,420.00 USD |
| `15M` | `MEXC` | `61.88%` | `38.12%` | `1.62` | 721,010.00 USD |
| `15M` | `Bitunix` | `49.92%` | `50.08%` | `1.00` | 2,130,000.00 USD |
| `15M` | `Hyperliquid` | `30.03%` | `69.97%` | `0.43` | 4,650,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.93%` | `49.07%` | `1.04` | 346,840.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `26.65%` | `73.35%` | `0.36` | 216,390.00 USD |
| `15M` | `HTX` | `43.29%` | `56.71%` | `0.76` | 40,950.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.59%` | `53.41%` | `0.87` | 208,410.00 USD |
| `15M` | `Aster` | `32.35%` | `67.65%` | `0.48` | 1,400,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.59%` | `50.41%` | `0.98` | 527,510.00 USD |
| `15M` | `Whale Positions` | `50.63%` | `49.37%` | `1.03` | 40,670,000.00 USD |
| `15M` | `Global Accounts` | `47.74%` | `52.26%` | `0.91` | 66,200,000.00 USD |
| `1H` | `DOGE` | `49.04%` | `50.96%` | `0.96` | 258,810,000.00 USD |
| `1H` | `Binance` | `50.7%` | `49.3%` | `1.03` | 145,170,000.00 USD |
| `1H` | `OKX` | `54.6%` | `45.4%` | `1.20` | 18,940,000.00 USD |
| `1H` | `Bybit` | `46.51%` | `53.49%` | `0.87` | 32,730,000.00 USD |
| `1H` | `KuCoin` | `45.17%` | `54.83%` | `0.82` | 797,100.00 USD |
| `1H` | `Gate` | `47.66%` | `52.34%` | `0.91` | 5,650,000.00 USD |
| `1H` | `Bitget` | `47.71%` | `52.29%` | `0.91` | 4,240,000.00 USD |
| `1H` | `BingX` | `47.8%` | `52.2%` | `0.92` | 3,780,000.00 USD |
| `1H` | `MEXC` | `38.45%` | `61.55%` | `0.62` | 3,890,000.00 USD |
| `1H` | `Bitunix` | `50.69%` | `49.31%` | `1.03` | 6,630,000.00 USD |
| `1H` | `Hyperliquid` | `40.23%` | `59.77%` | `0.67` | 24,590,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.43%` | `47.57%` | `1.10` | 926,020.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `11.78%` | `88.22%` | `0.13` | 569,970.00 USD |
| `1H` | `HTX` | `29.87%` | `70.13%` | `0.43` | 557,970.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `71.65%` | `28.35%` | `2.53` | 1,730,000.00 USD |
| `1H` | `Aster` | `50.83%` | `49.17%` | `1.03` | 4,900,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.37%` | `54.63%` | `0.83` | 3,700,000.00 USD |
| `1H` | `Whale Positions` | `50.7%` | `49.3%` | `1.03` | 145,170,000.00 USD |
| `1H` | `Global Accounts` | `49.04%` | `50.96%` | `0.96` | 258,810,000.00 USD |
| `4H` | `DOGE` | `48.77%` | `51.23%` | `0.95` | 2,340,000,000.00 USD |
| `4H` | `Binance` | `48.8%` | `51.2%` | `0.95` | 1,340,000,000.00 USD |
| `4H` | `OKX` | `50.69%` | `49.31%` | `1.03` | 148,940,000.00 USD |
| `4H` | `Bybit` | `48.31%` | `51.69%` | `0.93` | 270,440,000.00 USD |
| `4H` | `KuCoin` | `45.76%` | `54.24%` | `0.84` | 13,440,000.00 USD |
| `4H` | `Gate` | `48.81%` | `51.19%` | `0.95` | 54,370,000.00 USD |
| `4H` | `Bitget` | `47.42%` | `52.58%` | `0.90` | 62,610,000.00 USD |
| `4H` | `BingX` | `48.57%` | `51.43%` | `0.94` | 23,370,000.00 USD |
| `4H` | `MEXC` | `48.38%` | `51.62%` | `0.94` | 32,260,000.00 USD |
| `4H` | `Bitunix` | `48.59%` | `51.41%` | `0.95` | 56,080,000.00 USD |
| `4H` | `Hyperliquid` | `48.41%` | `51.59%` | `0.94` | 234,780,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.28%` | `49.72%` | `1.01` | 14,620,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `40.2%` | `59.8%` | `0.67` | 4,110,000.00 USD |
| `4H` | `HTX` | `38.72%` | `61.28%` | `0.63` | 3,330,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.98%` | `51.02%` | `0.96` | 8,450,000.00 USD |
| `4H` | `Aster` | `49.62%` | `50.38%` | `0.98` | 49,350,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.52%` | `49.48%` | `1.02` | 27,040,000.00 USD |
| `4H` | `Whale Positions` | `48.8%` | `51.2%` | `0.95` | 1,340,000,000.00 USD |
| `4H` | `Global Accounts` | `48.77%` | `51.23%` | `0.95` | 2,340,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0785` | `0.0785` | `0.0785` | `0.0786` | `0.0783` | 4,602,184.99 USD | 2,513,950.11 USD | 2,088,234.88 USD | 425,715.23 USD | `+9.25%` | `2B / 3S` |
| `0:00 UTC` | `0.0760` | `0.0766` | `0.0760` | `0.0786` | `0.0752` | 55,822,204.41 USD | 22,894,150.54 USD | 32,928,053.87 USD | -10,033,903.33 USD | `-17.97%` | `2B / 33S` |
| `5:00 UTC` | `0.0757` | `0.0754` | `0.0757` | `0.0762` | `0.0742` | 60,549,155.39 USD | 27,187,435.52 USD | 33,361,719.87 USD | -6,174,284.35 USD | `-10.20%` | `1B / 21S` |
| `0:00 UTC` | `0.0753` | `0.0755` | `0.0753` | `0.0761` | `0.0749` | 29,212,143.58 USD | 15,504,806.30 USD | 13,707,337.28 USD | 1,797,469.02 USD | `+6.15%` | `8B / 1S` |
| `5:00 UTC` | `0.0766` | `0.0764` | `0.0766` | `0.0769` | `0.0759` | 15,471,814.11 USD | 7,521,434.27 USD | 7,950,379.84 USD | -428,945.57 USD | `-2.77%` | `7B / 6S` |
| `0:00 UTC` | `0.0768` | `0.0767` | `0.0768` | `0.0770` | `0.0762` | 6,979,124.86 USD | 3,191,852.39 USD | 3,787,272.47 USD | -595,420.08 USD | `-8.53%` | `11B / 14S` |
| `5:00 UTC` | `0.0761` | `0.0762` | `0.0761` | `0.0765` | `0.0760` | 7,159,591.43 USD | 3,474,483.11 USD | 3,685,108.33 USD | -210,625.22 USD | `-2.94%` | `4B / 7S` |
| `0:00 UTC` | `0.0760` | `0.0760` | `0.0760` | `0.0764` | `0.0754` | 12,740,089.09 USD | 6,794,980.63 USD | 5,945,108.46 USD | 849,872.18 USD | `+6.67%` | `14B / 1S` |
| `5:00 UTC` | `0.0759` | `0.0760` | `0.0759` | `0.0764` | `0.0757` | 13,833,535.23 USD | 9,937,462.08 USD | 3,896,073.14 USD | 6,041,388.94 USD | `+43.67%` | `12B / 6S` |
| `0:00 UTC` | `0.0765` | `0.0764` | `0.0765` | `0.0766` | `0.0760` | 14,631,963.36 USD | 4,172,641.89 USD | 10,459,321.47 USD | -6,286,679.58 USD | `-42.97%` | `10B / 13S` |

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
| `5m` | -115,740.00 USD | -164,610.00 USD | **`DISTRIBUTION`** |
| `15m` | -160,080.00 USD | 6,730,000.00 USD | **`ACCUMULATION`** |
| `30m` | 75,220.00 USD | 7,830,000.00 USD | **`ACCUMULATION`** |
| `1h` | 64,370.00 USD | 6,240,000.00 USD | **`ACCUMULATION`** |
| `2h` | -4,040,000.00 USD | -22,960,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,050,000.00 USD | -27,420,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -13,010,000.00 USD | -31,800,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,410,000.00 USD | -26,840,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -9,900,000.00 USD | -27,640,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -14,250,000.00 USD | -47,240,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -51,220,000.00 USD | -153,500,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -279,570,000.00 USD | -774,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-115.74K` | 15m=`-160.08K` | 1h=`+64.37K` | 24h=`-14.25M`
* Futures Capital Netflows: 5m=`-164.61K` | 15m=`+6.73M` | 1h=`+6.24M` | 24h=`-47.24M`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0746` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0706` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0851`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0753` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0793` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0648`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0768`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
