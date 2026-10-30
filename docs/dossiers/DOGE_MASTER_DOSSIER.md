# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 09:40:21 IST` (`2026-10-30 04:10:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0746` | **Live Ask Quote**: `0.0767` | **Mid Price**: `0.0756`
- **Spread Points**: `21.00` | **Spread BPS**: `277.59 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0731` | VWAP Z-Score: `+2.50` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000680` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.09` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0753` | Lower -3.00σ Band: `0.0709`
  * Upper +2.51σ Band: `0.0749` | Lower -2.51σ Band: `0.0712`
  * Upper +2.01σ Band: `0.0745` | Lower -2.01σ Band: `0.0716`
  * Upper +2.00σ Band: `0.0745` | Lower -2.00σ Band: `0.0716`
  * Upper +1.28σ Band: `0.0740` | Lower -1.28σ Band: `0.0721`
  * Upper +1.00σ Band: `0.0738` | Lower -1.00σ Band: `0.0723`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0741` | EMA-20=`0.0742` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0752` (Slope: `+0.0000`) | EMA-100=`0.0762`
  * Institutional Anchors: EMA-144=`0.0765` | EMA-200=`0.0768` (Slope: `-0.5011`) | EMA-233=`0.0769`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `-0.09%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.02%`)
  * Value Area Low (VAL) = `0.0732` (Distance: `+3.40%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0788` | Weekly POC=`0.0762` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0760` | Low=`0.0753`
  * New York Session (13:00-21:00 UTC): High=`0.0761` | Low=`0.0752`
  * Initial Balance (First Hour): IB High=`0.0759` | IB Low=`0.0754`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0753` - `0.0760`
  * Optimal Trade Entry (OTE 0.705): `0.0758`
  * Structural Invalidation Anchor (0.786): `0.0763`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0758` | `0.0759` | `0.0758` | `0.0759` | `17,366,293` | 1,317,054.60 USD | -312,178.10 USD | `-23.70%` | -34,351,786.60 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.0759` | `0.0761` | `0.0758` | `0.0761` | `31,271,963` | 2,375,180.82 USD | 530,613.53 USD | `+22.34%` | -33,821,173.07 USD | `+0.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0761` | `0.0761` | `0.0761` | `0.0761` | `436,027` | 33,181.33 USD | 33,171.29 USD | `+99.97%` | -33,788,001.78 USD | `-0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0751` | `0.0754` | `0.0750` | `0.0754` | `41,572,141` | 3,128,035.72 USD | 530,944.71 USD | `+16.97%` | -34,443,714.67 USD | `+0.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0754` | `0.0759` | `0.0754` | `0.0759` | `68,387,065` | 5,177,761.26 USD | 39,345.50 USD | `+0.76%` | -34,404,369.16 USD | `+0.29` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.0759` | `0.0761` | `0.0758` | `0.0761` | `31,707,990` | 2,408,362.15 USD | 563,784.82 USD | `+23.41%` | -33,840,584.34 USD | `+0.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0743` | `0.0746` | `0.0733` | `0.0740` | `386,101,231` | 28,593,595.00 USD | -713,201.79 USD | `-2.49%` | -37,137,890.46 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0740` | `0.0752` | `0.0736` | `0.0750` | `319,578,594` | 23,850,098.79 USD | 1,220,777.97 USD | `+5.12%` | -35,917,112.48 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0750` | `0.0761` | `0.0749` | `0.0761` | `203,550,908` | 15,362,014.49 USD | 2,076,528.14 USD | `+13.52%` | -33,840,584.34 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -5,801,361.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -28,841,087.48 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0761` | `2,035,476,784` | 150,770,946.04 USD | -4,999,496.87 USD | `-3.32%` | -33,840,584.34 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -7,382,443.88 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -2,793,692.45 USD | `+1.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -5,801,361.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -28,841,087.48 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0761` | `2,035,476,784` | 150,770,946.04 USD | -4,999,496.87 USD | `-3.32%` | -33,840,584.34 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.0756`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0758` | `463764.0000` | 35,170.47 USD | 132,601.20 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `17597.0000` | 1,334.49 USD | 97,430.73 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `173021.0000` | 13,120.87 USD | 96,096.24 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `278916.0000` | 21,150.20 USD | 82,975.37 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `157504.0000` | 11,943.37 USD | 61,825.17 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `19825.0000` | 1,503.29 USD | 49,881.80 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `87473.0000` | 6,632.82 USD | 48,378.51 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `532.0000` | 40.34 USD | 41,745.69 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `1539.0000` | 116.69 USD | 41,705.35 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `102382.0000` | 7,762.81 USD | 41,588.66 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `52655.0000` | 3,992.35 USD | 33,825.85 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `19782.0000` | 1,499.83 USD | 29,833.50 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `76972.0000` | 5,835.63 USD | 28,333.67 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `105176.0000` | 7,973.81 USD | 22,498.03 USD | `11 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `77469.0000` | 5,873.16 USD | 14,524.22 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `11067.0000` | 839.01 USD | 8,651.06 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `47922.0000` | 3,633.01 USD | 7,812.05 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `6098.0000` | 462.29 USD | 4,179.04 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `3000.0000` | 227.43 USD | 3,716.75 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `46029.0000` | 3,489.32 USD | 3,489.32 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0758` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0758` | `16006.0000` | 1,213.29 USD | 1,213.29 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0758` | `13193.0000` | 999.99 USD | 2,213.28 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `17604.0000` | 1,334.31 USD | 3,547.59 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `3276.0000` | 248.30 USD | 3,795.89 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `5278.0000` | 400.02 USD | 4,195.92 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `13197.0000` | 1,000.20 USD | 5,196.12 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `22676.0000` | 1,718.59 USD | 6,914.71 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `92362.0000` | 6,999.93 USD | 13,914.64 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `10000.0000` | 757.87 USD | 14,672.51 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `2690.0000` | 203.86 USD | 14,876.37 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `10000.0000` | 757.85 USD | 15,634.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `17604.0000` | 1,334.07 USD | 16,968.29 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `148506.0000` | 11,253.93 USD | 28,222.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `17598.0000` | 1,333.54 USD | 29,555.76 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `426152.0000` | 32,292.52 USD | 61,848.28 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `17509.0000` | 1,326.76 USD | 63,175.05 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `123168.0000` | 9,332.93 USD | 72,507.98 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `3914.0000` | 296.58 USD | 72,804.55 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `52426.0000` | 3,972.37 USD | 76,776.92 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `452004.0000` | 34,247.89 USD | 111,024.81 USD | `2 orders` | `-0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `305` | `0xb83d...6e36` | `SHORT` | 7,775,736.76 USD | `102,645,925.00` | `0.0946` | `0.0757` | `1.35` | 1,931,604.89 USD | `+24.84%` | `3X Cross` |
| `311` | `0xc63a...a3cd` | `LONG` | 7,567,500.00 USD | `100,000,000.00` | `0.0856` | `0.0757` | `0.000000` | -997,321.96 USD | `-13.18%` | `10X Cross` |
| `315` | `0x610b...b613` | `LONG` | 7,478,717.61 USD | `98,666,424.00` | `0.0872` | `0.0757` | `0.0605` | -1,121,464.30 USD | `-15.00%` | `5X Cross` |
| `600` | `0x5b5d...c060` | `SHORT` | 3,747,090.74 USD | `49,478,955.00` | `0.0946` | `0.0757` | `3.29` | 934,425.87 USD | `+24.94%` | `3X Cross` |
| `630` | `0xca49...53c8` | `SHORT` | 3,522,301.13 USD | `46,542,649.00` | `0.0929` | `0.0757` | `0.3951` | 803,743.55 USD | `+22.82%` | `10X Cross` |
| `645` | `0x45d2...4029` | `SHORT` | 3,437,794.25 USD | `45,426,000.00` | `0.0954` | `0.0757` | `0.9836` | 897,834.97 USD | `+26.12%` | `10X Cross` |
| `682` | `0xecb6...2b00` | `SHORT` | 3,234,922.85 USD | `42,733,459.00` | `0.0789` | `0.0757` | `0.6720` | 136,461.37 USD | `+4.22%` | `10X Cross` |
| `1185` | `0x458d...ab3b` | `LONG` | 1,853,569.07 USD | `24,454,063.00` | `0.1002` | `0.0757` | `0.0714` | -597,352.84 USD | `-32.23%` | `3X Isolated` |
| `1191` | `0xeadc...9d55` | `LONG` | 1,841,584.05 USD | `24,317,440.00` | `0.0926` | `0.0757` | `0.000000` | -410,010.53 USD | `-22.26%` | `10X Cross` |
| `1332` | `0xf48f...10fe` | `LONG` | 1,622,969.92 USD | `21,424,497.00` | `0.0968` | `0.0757` | `0.0466` | -451,334.68 USD | `-27.81%` | `4X Cross` |
| `1515` | `0x9946...0852` | `SHORT` | 1,418,538.89 USD | `18,738,955.00` | `0.0871` | `0.0757` | `0.1621` | 212,980.11 USD | `+15.01%` | `10X Cross` |
| `1539` | `0x9aa5...58af` | `SHORT` | 1,395,841.56 USD | `18,444,239.00` | `0.0907` | `0.0757` | `0.5685` | 276,469.82 USD | `+19.81%` | `10X Cross` |
| `1562` | `0xcac1...26b3` | `SHORT` | 1,373,198.39 USD | `18,126,835.00` | `0.0943` | `0.0757` | `0.5537` | 336,260.81 USD | `+24.49%` | `10X Cross` |
| `1590` | `0x0d6a...ca57` | `LONG` | 1,335,045.33 USD | `17,626,455.00` | `0.0875` | `0.0757` | `0.0626` | -207,059.63 USD | `-15.51%` | `3X Isolated` |
| `1645` | `0x4808...a82c` | `LONG` | 1,277,256.05 USD | `16,828,143.00` | `0.0883` | `0.0757` | `0.0632` | -209,216.93 USD | `-16.38%` | `3X Cross` |
| `1790` | `0x31ef...f715` | `LONG` | 1,153,451.77 USD | `15,230,102.00` | `0.0936` | `0.0757` | `0.0668` | -272,244.15 USD | `-23.60%` | `3X Isolated` |
| `1810` | `0xbfc7...80b4` | `SHORT` | 1,136,698.58 USD | `15,020,000.00` | `0.0920` | `0.0757` | `0.1909` | 245,700.71 USD | `+21.62%` | `10X Cross` |
| `1895` | `0x7cee...fc93` | `SHORT` | 1,060,525.24 USD | `14,013,468.00` | `0.0863` | `0.0757` | `0.2705` | 148,352.12 USD | `+13.99%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 7,598.95 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.60K USD at 0.0799 USD [API] | `2026-10-29 00:28:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0155` | 1,390.00 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0185` | 1,090.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0193` | 1,860.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0194` | 1,170.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0197` | 628.80 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0199` | 4,990.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0208` | 810.27 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0214` | 10,680.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0243` | 225.11 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 369.37 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0246` | 152.98 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0256` | 4,070.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 1,970.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 3,070.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0282` | 563.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 152.04 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0294` | 463.58 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 27,480.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0309` | 684.83 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0321` | 3,510.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0333` | 573.99 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 780.85 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 13,620.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 1,140.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 421.91 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 6,680.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 5,520.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0367` | 221.77 USD | 16,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0367` | 4,940.00 USD | 16,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 1,250.00 USD | 16,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 36,740.00 USD | 16,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 546.74 USD | 16,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 2,370.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0394` | 211.02 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 178.57 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 75,870.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 1,910.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 8,830.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 10,120.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 4,960.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 216,270.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 13,010.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 5,240.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,370.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 6,480.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0467` | 451.75 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0469` | 4,700.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,180.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 925.74 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 71,390.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,330.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 42,370.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 104,040.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 267.52 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 52,340.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0502` | 120.06 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 10,280.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,360.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 1,090,000.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 2,680.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 308.55 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 1,190.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 7,510.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 5,350.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 315,250.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 2,230.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 10,260.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 182,740.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 12,030.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,420.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 1,890.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 1,590.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 14,430.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 3,290.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 28,620.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 2,840.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 6,290.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 38,870.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 1,820.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 178.61 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 749.76 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 567.50 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 359.24 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 6,430.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 441.75 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 347,440.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 19,490.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 5,280.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,520.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,940.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 25,990.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 4,560.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 1,130.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 830.97 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 548.46 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 6,160.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 6,090,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0619` | 17,440.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,420.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 870.40 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 8,460.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,430.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,310,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 905.97 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 4,770.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 5,600.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 2,100.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 150.01 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 17,700.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,390.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,280.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,180.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 4,720.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0660` | 2,510.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 7,620.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,190.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,370.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 11,450.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 14,030.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 11,770,000.00 USD | 11,770,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,560.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 11,640,000.00 USD | 11,640,000.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 134,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 117.29 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 11,500,000.00 USD | 11,500,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 20,340.00 USD | 723.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 49,510.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 11,430,000.00 USD | 11,430,000.00 USD | 24,150.00 USD | 15,070.00 USD | 584.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 80,430.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 11,390,000.00 USD | 11,390,000.00 USD | 41,510.00 USD | 12,720.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 13,120.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 11,320,000.00 USD | 11,320,000.00 USD | 41,080.00 USD | 1,410.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 595.81 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 11,260,000.00 USD | 11,260,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 870.75 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 10,310.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 11,200,000.00 USD | 11,200,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,970.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 11,200,000.00 USD | 11,200,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 11,200,000.00 USD | 11,200,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 4,720.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 11,140,000.00 USD | 11,140,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 38,610.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 11,080,000.00 USD | 11,080,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 10,950,000.00 USD | 10,950,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 10,810,000.00 USD | 10,810,000.00 USD | 35,400.00 USD | 18,030.00 USD | 29,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,310.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 10,720,000.00 USD | 10,720,000.00 USD | 78,740.00 USD | 36,780.00 USD | 164.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 10,610,000.00 USD | 10,610,000.00 USD | 87,540.00 USD | 31,470.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 10,450,000.00 USD | 10,450,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 10,360,000.00 USD | 10,360,000.00 USD | 41,490.00 USD | 24,910.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 10,260,000.00 USD | 10,260,000.00 USD | 36,930.00 USD | 29,080.00 USD | 26,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 423.90 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 10,170,000.00 USD | 10,170,000.00 USD | 54,240.00 USD | 21,680.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 10,070,000.00 USD | 10,070,000.00 USD | 25,410.00 USD | 16,310.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0708` | 94,010.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0709` | 10,000,000.00 USD | 10,000,000.00 USD | 36,740.00 USD | 37,120.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 9,910,000.00 USD | 9,910,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 9,660.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 9,840,000.00 USD | 9,840,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 2,160.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 9,770,000.00 USD | 9,770,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 9,700,000.00 USD | 9,700,000.00 USD | 35,120.00 USD | 58,130.00 USD | 67,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 9,540,000.00 USD | 9,540,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 213.78 USD | 391,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 9,440,000.00 USD | 9,440,000.00 USD | 34,440.00 USD | 8,830.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 391,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 9,360,000.00 USD | 9,360,000.00 USD | 24,840.00 USD | 31,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,170.00 USD | 383,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 9,300,000.00 USD | 9,300,000.00 USD | 10,910.00 USD | 7,710.00 USD | 21,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,270.00 USD | 382,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 9,260,000.00 USD | 9,260,000.00 USD | 67,080.00 USD | 31,390.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,070.00 USD | 360,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 9,130,000.00 USD | 9,130,000.00 USD | 10,150.00 USD | 0.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 359,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 9,120,000.00 USD | 9,120,000.00 USD | 31,160.00 USD | 29,440.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,160.00 USD | 357,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 9,030,000.00 USD | 9,030,000.00 USD | 136,510.00 USD | 76,220.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 345,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,800,000.00 USD | 8,800,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 322,050.00 USD | 322,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,720,000.00 USD | 8,720,000.00 USD | 54,790.00 USD | 162,040.00 USD | 153,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 626.77 USD | 626.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 8,350,000.00 USD | 8,350,000.00 USD | 27,830.00 USD | 87,980.00 USD | 92,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0725` | 8,140,000.00 USD | 8,140,000.00 USD | 54,140.00 USD | 22,980.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 8,040,000.00 USD | 8,040,000.00 USD | 51,960.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 7,980,000.00 USD | 7,980,000.00 USD | 168,660.00 USD | 0.00 USD | 345,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 7,470,000.00 USD | 7,470,000.00 USD | 66,510.00 USD | 85,670.00 USD | 75,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 7,240,000.00 USD | 7,240,000.00 USD | 19,510.00 USD | 82,260.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,110,000.00 USD | 7,110,000.00 USD | 112,200.00 USD | 54,520.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 6,940,000.00 USD | 6,940,000.00 USD | 152,870.00 USD | 49,300.00 USD | 43,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 6,700,000.00 USD | 6,700,000.00 USD | 154,930.00 USD | 60,240.00 USD | 81,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,400,000.00 USD | 6,400,000.00 USD | 15,550.00 USD | 0.00 USD | 71,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 6,310,000.00 USD | 6,310,000.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 6,270,000.00 USD | 6,270,000.00 USD | 33,390.00 USD | 31,100.00 USD | 299.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 6,200,000.00 USD | 6,200,000.00 USD | 234,720.00 USD | 123,630.00 USD | 1.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,850,000.00 USD | 5,850,000.00 USD | 51,890.00 USD | 42,510.00 USD | 636.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,750,000.00 USD | 5,750,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,230,000.00 USD | 5,230,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,960,000.00 USD | 4,960,000.00 USD | 33,740.00 USD | 0.00 USD | 267.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,930,000.00 USD | 4,930,000.00 USD | 36,980.00 USD | 0.00 USD | 560.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,890,000.00 USD | 4,890,000.00 USD | 286,340.00 USD | 0.00 USD | 684,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,920,000.00 USD | 3,920,000.00 USD | 118,640.00 USD | 234,470.00 USD | 190,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,380,000.00 USD | 3,380,000.00 USD | 19,880.00 USD | 187,400.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 3,110,000.00 USD | 3,110,000.00 USD | 199,850.00 USD | 166,270.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,720,000.00 USD | 2,720,000.00 USD | 371,240.00 USD | 274,020.00 USD | 211,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,860,000.00 USD | 1,860,000.00 USD | 466,980.00 USD | 159,330.00 USD | 131,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,100,000.00 USD | 1,100,000.00 USD | 130,290.00 USD | 143,100.00 USD | 194,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 635,760.00 USD | 635,760.00 USD | 203,330.00 USD | 0.00 USD | 149,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 282,960.00 USD | 282,960.00 USD | 69,890.00 USD | 0.00 USD | 120,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 92,290.00 USD | 92,290.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 85,440.00 USD | 85,440.00 USD | 0.00 USD | 85,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0760` | 424.91 USD | 424.91 USD | 0.00 USD | 0.00 USD | 424.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 412.85 USD | 412.85 USD | 0.00 USD | 0.00 USD | 412.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 825.70 USD | 825.70 USD | 0.00 USD | 0.00 USD | 412.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 14,210.00 USD | 14,210.00 USD | 0.00 USD | 13,220.00 USD | 168.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 340,180.00 USD | 340,180.00 USD | 0.00 USD | 325,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 598,420.00 USD | 598,420.00 USD | 0.00 USD | 257,590.00 USD | 656.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,710,000.00 USD | 1,710,000.00 USD | 745,930.00 USD | 360,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 2,060,000.00 USD | 2,060,000.00 USD | 169,980.00 USD | 188,260.00 USD | 502.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,930,000.00 USD | 2,930,000.00 USD | 351,760.00 USD | 0.00 USD | 514,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 3,600,000.00 USD | 3,600,000.00 USD | 181,440.00 USD | 341,350.00 USD | 148,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 4,220,000.00 USD | 4,220,000.00 USD | 272,760.00 USD | 93,300.00 USD | 253,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 4,880,000.00 USD | 4,880,000.00 USD | 216,410.00 USD | 232,340.00 USD | 212,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 5,850,000.00 USD | 5,850,000.00 USD | 286,340.00 USD | 0.00 USD | 685,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 6,240,000.00 USD | 6,240,000.00 USD | 65,160.00 USD | 169,730.00 USD | 149,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 164,510.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 3,830.00 USD | 3,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0775` | 6,690,000.00 USD | 6,690,000.00 USD | 155,740.00 USD | 109,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 7,070,000.00 USD | 7,070,000.00 USD | 190,100.00 USD | 110,600.00 USD | 86,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 205,390.00 USD | 264,690.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 8,140,000.00 USD | 8,140,000.00 USD | 16,790.00 USD | 202,930.00 USD | 295,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 85,950.00 USD | 140,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 8,470,000.00 USD | 8,470,000.00 USD | 69,890.00 USD | 31,980.00 USD | 253.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 8,650,000.00 USD | 8,650,000.00 USD | 113,060.00 USD | 68,670.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 8,660,000.00 USD | 8,660,000.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 9,000,000.00 USD | 9,000,000.00 USD | 8,010.00 USD | 184,740.00 USD | 145,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0784` | 723.88 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0784` | 9,390,000.00 USD | 9,390,000.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 9,740,000.00 USD | 9,740,000.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 10,280,000.00 USD | 10,280,000.00 USD | 191,180.00 USD | 117,040.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 11,230,000.00 USD | 11,230,000.00 USD | 298,820.00 USD | 307,550.00 USD | 344,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 4,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 11,560,000.00 USD | 11,560,000.00 USD | 75,490.00 USD | 181,170.00 USD | 75,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 12,090,000.00 USD | 12,090,000.00 USD | 234,900.00 USD | 192,150.00 USD | 96,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 12,250,000.00 USD | 12,250,000.00 USD | 102,120.00 USD | 57,780.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 12,590,000.00 USD | 12,590,000.00 USD | 152,950.00 USD | 95,070.00 USD | 95,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 12,750,000.00 USD | 12,750,000.00 USD | 104,950.00 USD | 18,870.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0793` | 423.67 USD | 5,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0794` | 12,930,000.00 USD | 12,930,000.00 USD | 92,580.00 USD | 41,370.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 13,010,000.00 USD | 13,010,000.00 USD | 10,150.00 USD | 0.00 USD | 73,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 13,200,000.00 USD | 13,200,000.00 USD | 174,010.00 USD | 0.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0796` | 309,520.00 USD | 314,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0797` | 13,730,000.00 USD | 13,730,000.00 USD | 191,110.00 USD | 89,760.00 USD | 242,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 13,950,000.00 USD | 13,950,000.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 14,520,000.00 USD | 14,520,000.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 14,630,000.00 USD | 14,630,000.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0800` | 113.67 USD | 314,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0801` | 14,640,000.00 USD | 14,640,000.00 USD | 6,300.00 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 14,650,000.00 USD | 14,650,000.00 USD | 7,730.00 USD | 1,770.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 14,700,000.00 USD | 14,700,000.00 USD | 9,970.00 USD | 0.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 14,720,000.00 USD | 14,720,000.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 14,860,000.00 USD | 14,860,000.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0805` | 435.61 USD | 315,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0806` | 15,120,000.00 USD | 15,120,000.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 15,590,000.00 USD | 15,590,000.00 USD | 221,690.00 USD | 208,070.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 16,670,000.00 USD | 16,670,000.00 USD | 419,500.00 USD | 131,030.00 USD | 523,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 17,490,000.00 USD | 17,490,000.00 USD | 477,790.00 USD | 336,610.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 18,100,000.00 USD | 18,100,000.00 USD | 293,220.00 USD | 180,540.00 USD | 133,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 18,430,000.00 USD | 18,430,000.00 USD | 83,280.00 USD | 241,410.00 USD | 875.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 18,790,000.00 USD | 18,790,000.00 USD | 144,600.00 USD | 99,490.00 USD | 120,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 19,070,000.00 USD | 19,070,000.00 USD | 49,290.00 USD | 23,210.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 19,470,000.00 USD | 19,470,000.00 USD | 29,840.00 USD | 79,960.00 USD | 292,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 19,820,000.00 USD | 19,820,000.00 USD | 150,190.00 USD | 72,710.00 USD | 124,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 20,540,000.00 USD | 20,540,000.00 USD | 348,980.00 USD | 194,790.00 USD | 177,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 21,100,000.00 USD | 21,100,000.00 USD | 301,230.00 USD | 127,050.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 21,840,000.00 USD | 21,840,000.00 USD | 269,340.00 USD | 161,260.00 USD | 308,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 315,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 22,460,000.00 USD | 22,460,000.00 USD | 174,640.00 USD | 312,480.00 USD | 128,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 23,140,000.00 USD | 23,140,000.00 USD | 136,010.00 USD | 202,840.00 USD | 344,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 23,600,000.00 USD | 23,600,000.00 USD | 210,590.00 USD | 79,630.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 24,190,000.00 USD | 24,190,000.00 USD | 262,170.00 USD | 169,200.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 24,540,000.00 USD | 24,540,000.00 USD | 270,850.00 USD | 75,420.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 25,120,000.00 USD | 25,120,000.00 USD | 151,910.00 USD | 226,510.00 USD | 198,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 25,400,000.00 USD | 25,400,000.00 USD | 127,790.00 USD | 122,020.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 25,820,000.00 USD | 25,820,000.00 USD | 150,570.00 USD | 84,820.00 USD | 190,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 25,920,000.00 USD | 25,920,000.00 USD | 49,040.00 USD | 48,230.00 USD | 399.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 26,270,000.00 USD | 26,270,000.00 USD | 216,200.00 USD | 75,940.00 USD | 58,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 26,640,000.00 USD | 26,640,000.00 USD | 182,720.00 USD | 111,290.00 USD | 72,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 26,960,000.00 USD | 26,960,000.00 USD | 140,600.00 USD | 84,690.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 27,030,000.00 USD | 27,030,000.00 USD | 39,850.00 USD | 0.00 USD | 24,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,580.00 USD | 319,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 27,340,000.00 USD | 27,340,000.00 USD | 171,130.00 USD | 66,230.00 USD | 80,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 319,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 27,680,000.00 USD | 27,680,000.00 USD | 119,590.00 USD | 55,260.00 USD | 165,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 28,030,000.00 USD | 28,030,000.00 USD | 127,020.00 USD | 94,190.00 USD | 126,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 104,680.00 USD | 176,580.00 USD | 65,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 48,890.00 USD | 63,220.00 USD | 144,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 320,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 28,850,000.00 USD | 28,850,000.00 USD | 129,000.00 USD | 30,430.00 USD | 51,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 321,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 29,120,000.00 USD | 29,120,000.00 USD | 168,220.00 USD | 70,030.00 USD | 38,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 29,210,000.00 USD | 29,210,000.00 USD | 52,570.00 USD | 16,550.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 29,270,000.00 USD | 29,270,000.00 USD | 13,720.00 USD | 15,480.00 USD | 28,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 29,290,000.00 USD | 29,290,000.00 USD | 23,380.00 USD | 2,010.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 29,360,000.00 USD | 29,360,000.00 USD | 22,710.00 USD | 0.00 USD | 46,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0843` | 29,400,000.00 USD | 29,400,000.00 USD | 33,600.00 USD | 0.00 USD | 634.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 29,470,000.00 USD | 29,470,000.00 USD | 79,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 29,490,000.00 USD | 29,490,000.00 USD | 18,230.00 USD | 0.00 USD | 264.53 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0846` | 110,220.00 USD | 431,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0846` | 29,580,000.00 USD | 29,580,000.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 128.58 USD | 432,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 29,590,000.00 USD | 29,590,000.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 1,150.00 USD | 433,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 433,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,450.00 USD | 437,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 437,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 127.82 USD | 438,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 438,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 438,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 439,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 439,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 446,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 447,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 452,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 452,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 453,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 493,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0946` | 4,260.00 USD | 497,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 522,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0954` | 194.24 USD | 522,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0955` | 47,770.00 USD | 570,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 1,160.00 USD | 571,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 571,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 571,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 952.67 USD | 572,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 573,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 580,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 583,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 584,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1047` | 6,300.00 USD | 590,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 596,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 597,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 600,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1095` | 1,760.00 USD | 602,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 602,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 602,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1142` | 154.22 USD | 602,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1158` | 131.49 USD | 603,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 603,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 604,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1277` | 921.51 USD | 604,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1291` | 124.63 USD | 605,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 605,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1300` | 44,510.00 USD | 649,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 651,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 651,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 652,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1351` | 34,920.00 USD | 687,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1371` | 6,220.00 USD | 693,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1383` | 22,420.00 USD | 715,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 100.35 USD | 715,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 716,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1419` | 989.83 USD | 717,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1426` | 2,000.00 USD | 719,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 721,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1436` | 4,010.00 USD | 725,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 725,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 727,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1472` | 6,420.00 USD | 733,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,260.00 USD | 741,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1482` | 23,820.00 USD | 765,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1492` | 1,980.00 USD | 767,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0158` | 16,690,000.00 USD | 0.00 USD | 3,940.00 USD | `-79.29%` | `250,000.00` |
| `Live` | `Long` | `0.0160` | 16,680,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.89%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,680,000.00 USD | 0.00 USD | 407.02 USD | `-78.37%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,680,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.23%` | `319,394.00` |
| `Live` | `Long` | `0.0176` | 16,670,000.00 USD | 0.00 USD | 1,050.00 USD | `-76.79%` | `59,317.00` |
| `Live` | `Long` | `0.0186` | 16,670,000.00 USD | 0.00 USD | 251.46 USD | `-75.47%` | `13,483.00` |
| `Live` | `Long` | `0.0188` | 16,670,000.00 USD | 0.00 USD | 603.20 USD | `-75.21%` | `32,000.00` |
| `Live` | `Long` | `0.0198` | 16,670,000.00 USD | 0.00 USD | 1,490.00 USD | `-73.89%` | `75,012.00` |
| `Live` | `Long` | `0.0204` | 16,670,000.00 USD | 0.00 USD | 2,280.00 USD | `-73.10%` | `111,254.00` |
| `Live` | `Long` | `0.0215` | 16,670,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.66%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,650,000.00 USD | 0.00 USD | 541.25 USD | `-71.53%` | `25,000.00` |
| `Live` | `Long` | `0.0227` | 16,650,000.00 USD | 0.00 USD | 141.19 USD | `-70.08%` | `6,206.00` |
| `Live` | `Long` | `0.0231` | 16,650,000.00 USD | 0.00 USD | 900.08 USD | `-69.69%` | `39,049.00` |
| `Live` | `Long` | `0.0232` | 16,650,000.00 USD | 0.00 USD | 278.28 USD | `-69.42%` | `11,969.00` |
| `Live` | `Long` | `0.0237` | 16,650,000.00 USD | 0.00 USD | 2,580.00 USD | `-68.90%` | `109,191.00` |
| `Live` | `Long` | `0.0242` | 16,640,000.00 USD | 0.00 USD | 12,460.00 USD | `-68.24%` | `515,795.00` |
| `Live` | `Long` | `0.0244` | 16,630,000.00 USD | 0.00 USD | 369.37 USD | `-67.98%` | `15,169.00` |
| `Live` | `Long` | `0.0254` | 16,630,000.00 USD | 0.00 USD | 4,020.00 USD | `-66.66%` | `158,606.00` |
| `Live` | `Long` | `0.0256` | 16,630,000.00 USD | 0.00 USD | 22,920.00 USD | `-66.27%` | `893,720.00` |
| `Live` | `Long` | `0.0262` | 16,610,000.00 USD | 0.00 USD | 140.28 USD | `-65.48%` | `5,344.00` |
| `Live` | `Long` | `0.0265` | 16,600,000.00 USD | 0.00 USD | 529.00 USD | `-65.21%` | `20,000.00` |
| `Live` | `Long` | `0.0267` | 16,600,000.00 USD | 0.00 USD | 161.26 USD | `-64.95%` | `6,051.00` |
| `Live` | `Long` | `0.0268` | 16,600,000.00 USD | 0.00 USD | 1,000.00 USD | `-64.69%` | `37,344.00` |
| `Live` | `Long` | `0.0272` | 16,600,000.00 USD | 0.00 USD | 880.12 USD | `-64.16%` | `32,298.00` |
| `Live` | `Long` | `0.0278` | 16,600,000.00 USD | 0.00 USD | 4,250.00 USD | `-63.50%` | `153,201.00` |
| `Live` | `Long` | `0.0279` | 16,600,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.24%` | `61,775.00` |
| `Live` | `Long` | `0.0306` | 16,600,000.00 USD | 0.00 USD | 137.41 USD | `-59.82%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,600,000.00 USD | 0.00 USD | 265.80 USD | `-59.56%` | `8,644.00` |
| `Live` | `Long` | `0.0319` | 16,600,000.00 USD | 0.00 USD | 549.83 USD | `-58.11%` | `17,263.00` |
| `Live` | `Long` | `0.0330` | 16,600,000.00 USD | 0.00 USD | 757.85 USD | `-56.67%` | `23,000.00` |
| `Live` | `Long` | `0.0336` | 16,590,000.00 USD | 0.00 USD | 49,950.00 USD | `-55.88%` | `1,488,849.00` |
| `Live` | `Long` | `0.0336` | 16,540,000.00 USD | 0.00 USD | 393.23 USD | `-55.74%` | `11,686.00` |
| `Live` | `Long` | `0.0340` | 16,540,000.00 USD | 0.00 USD | 476.56 USD | `-55.35%` | `14,037.00` |
| `Live` | `Long` | `0.0340` | 16,540,000.00 USD | 0.00 USD | 6,400.00 USD | `-55.22%` | `187,979.00` |
| `Live` | `Long` | `0.0348` | 16,540,000.00 USD | 0.00 USD | 13,540.00 USD | `-54.30%` | `389,633.00` |
| `Live` | `Long` | `0.0350` | 16,520,000.00 USD | 0.00 USD | 4,710.00 USD | `-53.90%` | `134,443.00` |
| `Live` | `Long` | `0.0355` | 16,520,000.00 USD | 0.00 USD | 700.21 USD | `-53.38%` | `19,752.00` |
| `Live` | `Long` | `0.0358` | 16,520,000.00 USD | 0.00 USD | 214.53 USD | `-52.85%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,520,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.72%` | `233,408.00` |
| `Live` | `Long` | `0.0372` | 16,510,000.00 USD | 0.00 USD | 35,290.00 USD | `-51.14%` | `950,000.00` |
| `Live` | `Long` | `0.0381` | 16,470,000.00 USD | 0.00 USD | 1,600.00 USD | `-49.96%` | `41,929.00` |
| `Live` | `Long` | `0.0382` | 16,470,000.00 USD | 0.00 USD | 1,810.00 USD | `-49.83%` | `47,501.00` |
| `Live` | `Long` | `0.0384` | 16,470,000.00 USD | 0.00 USD | 353.40 USD | `-49.56%` | `9,215.00` |
| `Live` | `Long` | `0.0386` | 16,470,000.00 USD | 0.00 USD | 121.74 USD | `-49.30%` | `3,158.00` |
| `Live` | `Long` | `0.0386` | 16,470,000.00 USD | 0.00 USD | 206.74 USD | `-49.17%` | `5,349.00` |
| `Live` | `Long` | `0.0393` | 16,470,000.00 USD | 0.00 USD | 2,180.00 USD | `-48.38%` | `55,633.00` |
| `Live` | `Long` | `0.0399` | 16,470,000.00 USD | 0.00 USD | 103.31 USD | `-47.46%` | `2,586.00` |
| `Live` | `Long` | `0.0401` | 16,470,000.00 USD | 0.00 USD | 4,020.00 USD | `-47.20%` | `100,000.00` |
| `Live` | `Long` | `0.0404` | 16,460,000.00 USD | 0.00 USD | 56,970.00 USD | `-46.80%` | `1,408,334.00` |
| `Live` | `Long` | `0.0408` | 16,410,000.00 USD | 0.00 USD | 419.28 USD | `-46.41%` | `10,289.00` |
| `Live` | `Long` | `0.0411` | 16,410,000.00 USD | 0.00 USD | 5,020.00 USD | `-46.01%` | `122,306.00` |
| `Live` | `Long` | `0.0411` | 16,400,000.00 USD | 0.00 USD | 34,120.00 USD | `-45.88%` | `829,067.00` |
| `Live` | `Long` | `0.0415` | 16,370,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.35%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 16,370,000.00 USD | 0.00 USD | 266.05 USD | `-44.83%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,370,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.43%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,360,000.00 USD | 0.00 USD | 267.52 USD | `-44.30%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,360,000.00 USD | 0.00 USD | 44,200.00 USD | `-44.17%` | `1,041,287.00` |
| `Live` | `Long` | `0.0425` | 16,320,000.00 USD | 0.00 USD | 883.34 USD | `-44.04%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,320,000.00 USD | 0.00 USD | 8,550.00 USD | `-43.91%` | `200,534.00` |
| `Live` | `Long` | `0.0430` | 16,310,000.00 USD | 0.00 USD | 859.00 USD | `-43.51%` | `20,000.00` |
| `Live` | `Long` | `0.0430` | 16,310,000.00 USD | 0.00 USD | 27,590.00 USD | `-43.38%` | `640,910.00` |
| `Live` | `Long` | `0.0432` | 16,280,000.00 USD | 0.00 USD | 954.87 USD | `-43.25%` | `22,129.00` |
| `Live` | `Long` | `0.0432` | 16,280,000.00 USD | 0.00 USD | 122,100.00 USD | `-43.12%` | `2,823,089.00` |
| `Live` | `Long` | `0.0433` | 16,160,000.00 USD | 0.00 USD | 2,450.00 USD | `-42.99%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 16,160,000.00 USD | 0.00 USD | 149.46 USD | `-42.59%` | `3,424.00` |
| `Live` | `Long` | `0.0439` | 16,160,000.00 USD | 0.00 USD | 1,610.00 USD | `-42.33%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,160,000.00 USD | 0.00 USD | 750.58 USD | `-42.20%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,150,000.00 USD | 0.00 USD | 1,060.00 USD | `-42.07%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,150,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.67%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,050,000.00 USD | 0.00 USD | 444.76 USD | `-41.28%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,050,000.00 USD | 0.00 USD | 248.63 USD | `-41.15%` | `5,556.00` |
| `Live` | `Long` | `0.0449` | 16,050,000.00 USD | 0.00 USD | 810.81 USD | `-40.88%` | `18,038.00` |
| `Live` | `Long` | `0.0452` | 16,050,000.00 USD | 0.00 USD | 967,320.00 USD | `-40.62%` | `21,424,497.00` |
| `Live` | `Long` | `0.0454` | 15,080,000.00 USD | 0.00 USD | 27,930.00 USD | `-40.36%` | `615,937.00` |
| `Live` | `Long` | `0.0454` | 15,060,000.00 USD | 0.00 USD | 2,610.00 USD | `-40.23%` | `57,510.00` |
| `Live` | `Long` | `0.0456` | 15,050,000.00 USD | 0.00 USD | 32,650.00 USD | `-40.09%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 15,020,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.83%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 15,010,000.00 USD | 0.00 USD | 789.72 USD | `-39.70%` | `17,224.00` |
| `Live` | `Long` | `0.0459` | 15,010,000.00 USD | 0.00 USD | 689.25 USD | `-39.57%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 15,010,000.00 USD | 0.00 USD | 25,960.00 USD | `-39.44%` | `563,730.00` |
| `Live` | `Long` | `0.0461` | 14,990,000.00 USD | 0.00 USD | 95,490.00 USD | `-39.31%` | `2,069,084.00` |
| `Live` | `Long` | `0.0464` | 14,890,000.00 USD | 0.00 USD | 362.87 USD | `-39.04%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 14,890,000.00 USD | 0.00 USD | 18,030.00 USD | `-38.91%` | `388,263.00` |
| `Live` | `Long` | `0.0466` | 14,870,000.00 USD | 0.00 USD | 13,640.00 USD | `-38.65%` | `292,347.00` |
| `Live` | `Long` | `0.0469` | 14,860,000.00 USD | 0.00 USD | 1,210.00 USD | `-38.38%` | `25,729.00` |
| `Live` | `Long` | `0.0471` | 14,860,000.00 USD | 0.00 USD | 2,360.00 USD | `-38.12%` | `50,080.00` |
| `Live` | `Long` | `0.0473` | 14,860,000.00 USD | 0.00 USD | 3,010.00 USD | `-37.86%` | `63,783.00` |
| `Live` | `Long` | `0.0476` | 14,850,000.00 USD | 0.00 USD | 105.02 USD | `-37.33%` | `2,204.00` |
| `Live` | `Long` | `0.0479` | 14,850,000.00 USD | 0.00 USD | 1,290.00 USD | `-36.94%` | `26,900.00` |
| `Live` | `Long` | `0.0481` | 14,850,000.00 USD | 0.00 USD | 56,440.00 USD | `-36.81%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,800,000.00 USD | 0.00 USD | 2,330.00 USD | `-36.67%` | `48,418.00` |
| `Live` | `Long` | `0.0483` | 14,790,000.00 USD | 0.00 USD | 2,280.00 USD | `-36.41%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,790,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.28%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 14,790,000.00 USD | 0.00 USD | 506.45 USD | `-36.02%` | `10,410.00` |
| `Live` | `Long` | `0.0488` | 14,790,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.75%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,790,000.00 USD | 0.00 USD | 16,470.00 USD | `-35.62%` | `336,491.00` |
| `Live` | `Long` | `0.0491` | 14,770,000.00 USD | 0.00 USD | 1,080.00 USD | `-35.49%` | `21,989.00` |
| `Live` | `Long` | `0.0496` | 14,770,000.00 USD | 0.00 USD | 314.48 USD | `-34.70%` | `6,334.00` |
| `Live` | `Long` | `0.0498` | 14,770,000.00 USD | 0.00 USD | 8,470.00 USD | `-34.57%` | `170,271.00` |
| `Live` | `Long` | `0.0500` | 14,760,000.00 USD | 0.00 USD | 501.50 USD | `-34.18%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,760,000.00 USD | 0.00 USD | 5,410.00 USD | `-33.91%` | `107,572.00` |
| `Live` | `Long` | `0.0505` | 14,750,000.00 USD | 0.00 USD | 334.89 USD | `-33.65%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,750,000.00 USD | 0.00 USD | 1,040.00 USD | `-33.39%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,750,000.00 USD | 0.00 USD | 5,660.00 USD | `-33.26%` | `111,460.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 535.43 USD | `-32.99%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 566.65 USD | `-32.86%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,750,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.73%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,740,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.60%` | `29,005.00` |
| `Live` | `Long` | `0.0515` | 14,730,000.00 USD | 0.00 USD | 308.55 USD | `-32.33%` | `5,997.00` |
| `Live` | `Long` | `0.0517` | 14,730,000.00 USD | 0.00 USD | 931.86 USD | `-31.94%` | `18,007.00` |
| `Live` | `Long` | `0.0519` | 14,730,000.00 USD | 0.00 USD | 7,900.00 USD | `-31.81%` | `152,446.00` |
| `Live` | `Long` | `0.0520` | 14,730,000.00 USD | 0.00 USD | 277.72 USD | `-31.68%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,720,000.00 USD | 0.00 USD | 5,350.00 USD | `-31.55%` | `102,859.00` |
| `Live` | `Long` | `0.0522` | 14,720,000.00 USD | 0.00 USD | 315,950.00 USD | `-31.28%` | `6,046,803.00` |
| `Live` | `Long` | `0.0524` | 14,400,000.00 USD | 0.00 USD | 2,230.00 USD | `-31.02%` | `42,425.00` |
| `Live` | `Long` | `0.0525` | 14,400,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.89%` | `119,430.00` |
| `Live` | `Long` | `0.0527` | 14,400,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.62%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,390,000.00 USD | 0.00 USD | 673.52 USD | `-30.49%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,390,000.00 USD | 0.00 USD | 187,290.00 USD | `-30.36%` | `3,537,023.00` |
| `Live` | `Long` | `0.0532` | 14,200,000.00 USD | 0.00 USD | 9,840.00 USD | `-30.10%` | `185,175.00` |
| `Live` | `Long` | `0.0532` | 14,200,000.00 USD | 0.00 USD | 11,120.00 USD | `-29.97%` | `208,846.00` |
| `Live` | `Long` | `0.0534` | 14,180,000.00 USD | 0.00 USD | 1,240.00 USD | `-29.84%` | `23,207.00` |
| `Live` | `Long` | `0.0534` | 14,180,000.00 USD | 0.00 USD | 1,890.00 USD | `-29.70%` | `35,411.00` |
| `Live` | `Long` | `0.0536` | 14,180,000.00 USD | 0.00 USD | 4,820.00 USD | `-29.57%` | `89,958.00` |
| `Live` | `Long` | `0.0537` | 14,180,000.00 USD | 0.00 USD | 6,420.00 USD | `-29.44%` | `119,631.00` |
| `Live` | `Long` | `0.0537` | 14,170,000.00 USD | 0.00 USD | 257.62 USD | `-29.31%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 14,170,000.00 USD | 0.00 USD | 5,290.00 USD | `-29.05%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 14,160,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.92%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 14,160,000.00 USD | 0.00 USD | 3,030.00 USD | `-28.78%` | `55,906.00` |
| `Live` | `Long` | `0.0542` | 14,160,000.00 USD | 0.00 USD | 96,530.00 USD | `-28.65%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 14,060,000.00 USD | 0.00 USD | 341.67 USD | `-28.39%` | `6,275.00` |
| `Live` | `Long` | `0.0546` | 14,060,000.00 USD | 0.00 USD | 2,510.00 USD | `-28.26%` | `46,004.00` |
| `Live` | `Long` | `0.0546` | 14,060,000.00 USD | 0.00 USD | 1,420.00 USD | `-28.13%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 14,060,000.00 USD | 0.00 USD | 188.07 USD | `-27.99%` | `3,435.00` |
| `Live` | `Long` | `0.0551` | 14,060,000.00 USD | 0.00 USD | 1,760.00 USD | `-27.47%` | `31,888.00` |
| `Live` | `Long` | `0.0556` | 14,060,000.00 USD | 0.00 USD | 907.02 USD | `-26.94%` | `16,328.00` |
| `Live` | `Long` | `0.0556` | 14,060,000.00 USD | 0.00 USD | 4,010.00 USD | `-26.81%` | `72,076.00` |
| `Live` | `Long` | `0.0561` | 14,050,000.00 USD | 0.00 USD | 8,410.00 USD | `-26.28%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 14,040,000.00 USD | 0.00 USD | 63,470.00 USD | `-26.15%` | `1,130,362.00` |
| `Live` | `Long` | `0.0563` | 13,980,000.00 USD | 0.00 USD | 1,820.00 USD | `-26.02%` | `32,433.00` |
| `Live` | `Long` | `0.0563` | 13,980,000.00 USD | 0.00 USD | 351.85 USD | `-25.89%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,980,000.00 USD | 0.00 USD | 131.48 USD | `-25.63%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,980,000.00 USD | 0.00 USD | 567.50 USD | `-25.36%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,980,000.00 USD | 0.00 USD | 315.67 USD | `-25.10%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,980,000.00 USD | 0.00 USD | 10,800.00 USD | `-24.97%` | `189,387.00` |
| `Live` | `Long` | `0.0571` | 13,970,000.00 USD | 0.00 USD | 814.04 USD | `-24.84%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,960,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.58%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,960,000.00 USD | 0.00 USD | 7,630.00 USD | `-24.31%` | `132,603.00` |
| `Live` | `Long` | `0.0576` | 13,950,000.00 USD | 0.00 USD | 10,600.00 USD | `-24.18%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,940,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.05%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,930,000.00 USD | 0.00 USD | 3,940.00 USD | `-23.92%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,920,000.00 USD | 0.00 USD | 441.75 USD | `-23.79%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,920,000.00 USD | 0.00 USD | 431.14 USD | `-23.65%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,920,000.00 USD | 0.00 USD | 447.17 USD | `-23.52%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,920,000.00 USD | 0.00 USD | 582.50 USD | `-23.39%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,920,000.00 USD | 0.00 USD | 116.82 USD | `-23.26%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 13,920,000.00 USD | 0.00 USD | 5,840.00 USD | `-23.13%` | `100,000.00` |
| `Live` | `Long` | `0.0585` | 13,920,000.00 USD | 0.00 USD | 172.78 USD | `-23.00%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,920,000.00 USD | 0.00 USD | 305.15 USD | `-22.73%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,920,000.00 USD | 0.00 USD | 212.22 USD | `-22.47%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,920,000.00 USD | 0.00 USD | 26,980.00 USD | `-22.21%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,890,000.00 USD | 0.00 USD | 546.26 USD | `-21.94%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,890,000.00 USD | 0.00 USD | 4,140.00 USD | `-21.81%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,880,000.00 USD | 0.00 USD | 3,300.00 USD | `-21.68%` | `55,392.00` |
| `Live` | `Long` | `0.0597` | 13,880,000.00 USD | 0.00 USD | 16,800.00 USD | `-21.55%` | `281,570.00` |
| `Live` | `Long` | `0.0599` | 13,860,000.00 USD | 0.00 USD | 4,560.00 USD | `-21.29%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 13,860,000.00 USD | 0.00 USD | 1,230.00 USD | `-21.16%` | `20,496.00` |
| `Live` | `Long` | `0.0600` | 13,860,000.00 USD | 0.00 USD | 7,210.00 USD | `-21.02%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,850,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.89%` | `141,093.00` |
| `Live` | `Long` | `0.0602` | 13,840,000.00 USD | 0.00 USD | 356,270.00 USD | `-20.76%` | `5,913,227.00` |
| `Live` | `Long` | `0.0604` | 13,490,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-20.63%` | `98,675,512.00` |
| `Live` | `Long` | `0.0605` | 7,530,000.00 USD | 0.00 USD | 32,090.00 USD | `-20.37%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,500,000.00 USD | 0.00 USD | 622.63 USD | `-20.24%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 7,500,000.00 USD | 0.00 USD | 2,070.00 USD | `-20.10%` | `34,109.00` |
| `Live` | `Long` | `0.0609` | 7,500,000.00 USD | 0.00 USD | 717.73 USD | `-19.97%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,500,000.00 USD | 0.00 USD | 5,110.00 USD | `-19.84%` | `83,914.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 629.72 USD | `-19.58%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 298.17 USD | `-19.45%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 655.16 USD | `-19.31%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,490,000.00 USD | 0.00 USD | 1,890.00 USD | `-19.05%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,490,000.00 USD | 0.00 USD | 11,510.00 USD | `-18.92%` | `186,736.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 548.71 USD | `-18.79%` | `8,886.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-18.39%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,450,000.00 USD | 0.00 USD | 345.86 USD | `-18.26%` | `5,565.00` |
| `Live` | `Long` | `0.0622` | 7,450,000.00 USD | 0.00 USD | 1,210.00 USD | `-18.13%` | `19,518.00` |
| `Live` | `Long` | `0.0624` | 7,450,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.00%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 43,620.00 USD | `-17.87%` | `698,435.00` |
| `Live` | `Long` | `0.0625` | 7,400,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.74%` | `17,630,450.00` |
| `Live` | `Long` | `0.0626` | 6,300,000.00 USD | 0.00 USD | 1,250.00 USD | `-17.60%` | `19,891.00` |
| `Live` | `Long` | `0.0628` | 6,300,000.00 USD | 0.00 USD | 10,210.00 USD | `-17.47%` | `162,702.00` |
| `Live` | `Long` | `0.0629` | 6,290,000.00 USD | 0.00 USD | 6,400.00 USD | `-17.34%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,280,000.00 USD | 0.00 USD | 2,530.00 USD | `-17.08%` | `40,193.00` |
| `Live` | `Long` | `0.0631` | 6,280,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-16.95%` | `20,783,139.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.82%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.68%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.55%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-16.42%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 4,770.00 USD | `-16.29%` | `74,997.00` |
| `Live` | `Long` | `0.0638` | 4,940,000.00 USD | 0.00 USD | 5,600.00 USD | `-16.16%` | `87,791.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 23,220.00 USD | `-16.03%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.90%` | `31,194.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 150.01 USD | `-15.76%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 17,100.00 USD | `-15.63%` | `266,578.00` |
| `Live` | `Long` | `0.0643` | 4,890,000.00 USD | 0.00 USD | 9,990.00 USD | `-15.50%` | `155,456.00` |
| `Live` | `Long` | `0.0644` | 4,880,000.00 USD | 0.00 USD | 76,280.00 USD | `-15.37%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,810,000.00 USD | 0.00 USD | 27,180.00 USD | `-15.24%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,780,000.00 USD | 0.00 USD | 631.94 USD | `-15.11%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,780,000.00 USD | 0.00 USD | 162,920.00 USD | `-14.84%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,620,000.00 USD | 0.00 USD | 8,800.00 USD | `-14.71%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,610,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.58%` | `337,347.00` |
| `Live` | `Long` | `0.0650` | 4,590,000.00 USD | 0.00 USD | 2,470.00 USD | `-14.45%` | `38,008.00` |
| `Live` | `Long` | `0.0651` | 4,580,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.32%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,580,000.00 USD | 0.00 USD | 13,770.00 USD | `-14.19%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,570,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.79%` | `118,852.00` |
| `Live` | `Long` | `0.0658` | 4,560,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.53%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.40%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,480,000.00 USD | 0.00 USD | 9,600.00 USD | `-13.26%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,470,000.00 USD | 0.00 USD | 2,280.00 USD | `-13.00%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,470,000.00 USD | 0.00 USD | 1,630.00 USD | `-12.87%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,470,000.00 USD | 0.00 USD | 17,410.00 USD | `-12.74%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,450,000.00 USD | 0.00 USD | 1,270.00 USD | `-12.61%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,450,000.00 USD | 0.00 USD | 34,860.00 USD | `-12.34%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 7,620.00 USD | `-12.21%` | `114,225.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-12.08%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-11.95%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,260,000.00 USD | 0.00 USD | 9,050.00 USD | `-11.82%` | `134,979.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.56%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 15,370.00 USD | `-11.42%` | `228,139.00` |
| `Live` | `Long` | `0.0674` | 3,220,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.29%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,220,000.00 USD | 0.00 USD | 112,780.00 USD | `-11.16%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,110,000.00 USD | 0.00 USD | 12,880.00 USD | `-11.03%` | `190,436.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 4,290.00 USD | `-10.90%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 34,090.00 USD | `-10.77%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,060,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.63%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,040,000.00 USD | 0.00 USD | 212.72 USD | `-10.50%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,040,000.00 USD | 0.00 USD | 117.29 USD | `-10.37%` | `1,721.00` |
| `Live` | `Long` | `0.0683` | 3,040,000.00 USD | 0.00 USD | 55,650.00 USD | `-10.24%` | `815,403.00` |
| `Live` | `Long` | `0.0684` | 2,990,000.00 USD | 0.00 USD | 80,430.00 USD | `-9.98%` | `1,174,961.00` |
| `Live` | `Long` | `0.0685` | 2,900,000.00 USD | 0.00 USD | 13,120.00 USD | `-9.85%` | `191,414.00` |
| `Live` | `Long` | `0.0687` | 2,890,000.00 USD | 0.00 USD | 34,970.00 USD | `-9.71%` | `509,405.00` |
| `Live` | `Long` | `0.0688` | 2,860,000.00 USD | 0.00 USD | 16,210.00 USD | `-9.58%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,840,000.00 USD | 0.00 USD | 870.75 USD | `-9.45%` | `12,647.00` |
| `Live` | `Long` | `0.0689` | 2,840,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.32%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,330,000.00 USD | 0.00 USD | 6,960.00 USD | `-9.19%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,320,000.00 USD | 0.00 USD | 13,510.00 USD | `-9.06%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 9,970.00 USD | `-8.92%` | `144,028.00` |
| `Live` | `Long` | `0.0693` | 2,300,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.79%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,300,000.00 USD | 0.00 USD | 4,980.00 USD | `-8.66%` | `71,770.00` |
| `Live` | `Long` | `0.0697` | 2,290,000.00 USD | 0.00 USD | 5,240.00 USD | `-8.40%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 11,090.00 USD | `-8.27%` | `158,931.00` |
| `Live` | `Long` | `0.0698` | 2,280,000.00 USD | 0.00 USD | 3,630.00 USD | `-8.14%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,270,000.00 USD | 0.00 USD | 1,310.00 USD | `-8.00%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,270,000.00 USD | 0.00 USD | 9,620.00 USD | `-7.87%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,260,000.00 USD | 0.00 USD | 8,310.00 USD | `-7.74%` | `118,427.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 1,480.00 USD | `-7.61%` | `21,015.00` |
| `Live` | `Long` | `0.0703` | 2,250,000.00 USD | 0.00 USD | 4,360.00 USD | `-7.48%` | `61,923.00` |
| `Live` | `Long` | `0.0704` | 2,250,000.00 USD | 0.00 USD | 216.56 USD | `-7.35%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 423.90 USD | `-7.08%` | `6,000.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 94,410.00 USD | `-6.95%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,150,000.00 USD | 0.00 USD | 821.60 USD | `-6.69%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,150,000.00 USD | 0.00 USD | 5,240.00 USD | `-6.56%` | `73,732.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 2,160.00 USD | `-6.43%` | `30,362.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 802.06 USD | `-6.29%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,150,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-6.16%` | `24,500,580.00` |
| `Live` | `Long` | `0.0714` | 397,120.00 USD | 0.00 USD | 5,410.00 USD | `-6.03%` | `75,723.00` |
| `Live` | `Long` | `0.0716` | 391,710.00 USD | 0.00 USD | 8,120.00 USD | `-5.90%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 383,590.00 USD | 0.00 USD | 1,170.00 USD | `-5.77%` | `16,291.00` |
| `Live` | `Long` | `0.0717` | 382,420.00 USD | 0.00 USD | 22,270.00 USD | `-5.64%` | `310,316.00` |
| `Live` | `Long` | `0.0718` | 360,160.00 USD | 0.00 USD | 1,070.00 USD | `-5.51%` | `14,951.00` |
| `Live` | `Long` | `0.0720` | 359,080.00 USD | 0.00 USD | 1,900.00 USD | `-5.37%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 357,190.00 USD | 0.00 USD | 12,160.00 USD | `-5.24%` | `168,703.00` |
| `Live` | `Long` | `0.0722` | 345,030.00 USD | 0.00 USD | 22,360.00 USD | `-5.11%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 322,680.00 USD | 0.00 USD | 322,050.00 USD | `-4.98%` | `4,457,443.00` |
| `Live` | `Long` | `0.0723` | 626.77 USD | 0.00 USD | 626.77 USD | `-4.85%` | `8,663.00` |
| `Live` | `Short` | `0.0770` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | `+1.20%` | `42,311.00` |
| `Live` | `Short` | `0.0775` | 3,500.00 USD | 240.95 USD | 0.00 USD | `+1.99%` | `3,107.00` |
| `Live` | `Short` | `0.0788` | 3,610.00 USD | 113.24 USD | 0.00 USD | `+3.57%` | `1,438.00` |
| `Live` | `Short` | `0.0793` | 4,030.00 USD | 423.67 USD | 0.00 USD | `+4.23%` | `5,346.00` |
| `Live` | `Short` | `0.0808` | 4,250.00 USD | 215.60 USD | 0.00 USD | `+6.20%` | `2,670.00` |
| `Live` | `Short` | `0.0809` | 4,470.00 USD | 215.87 USD | 0.00 USD | `+6.33%` | `2,670.00` |
| `Live` | `Short` | `0.0810` | 4,580.00 USD | 118.33 USD | 0.00 USD | `+6.59%` | `1,460.00` |
| `Live` | `Short` | `0.0819` | 4,960.00 USD | 380.85 USD | 0.00 USD | `+7.65%` | `4,653.00` |
| `Live` | `Short` | `0.0832` | 8,420.00 USD | 3,450.00 USD | 0.00 USD | `+9.36%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 8,920.00 USD | 500.17 USD | 0.00 USD | `+9.49%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 9,210.00 USD | 293.44 USD | 0.00 USD | `+10.01%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 10,780.00 USD | 1,570.00 USD | 0.00 USD | `+10.15%` | `18,767.00` |
| `Live` | `Short` | `0.0847` | 10,910.00 USD | 128.58 USD | 0.00 USD | `+11.33%` | `1,519.00` |
| `Live` | `Short` | `0.0848` | 11,340.00 USD | 426.71 USD | 0.00 USD | `+11.59%` | `5,029.00` |
| `Live` | `Short` | `0.0858` | 11,450.00 USD | 115.30 USD | 0.00 USD | `+12.91%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 15,910.00 USD | 4,450.00 USD | 0.00 USD | `+13.04%` | `51,791.00` |
| `Live` | `Short` | `0.0871` | 16,040.00 USD | 138.58 USD | 0.00 USD | `+14.49%` | `1,592.00` |
| `Live` | `Short` | `0.0881` | 16,510.00 USD | 465.17 USD | 0.00 USD | `+15.80%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 16,920.00 USD | 411.53 USD | 0.00 USD | `+16.72%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 17,340.00 USD | 418.80 USD | 0.00 USD | `+17.12%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 17,630.00 USD | 285.70 USD | 0.00 USD | `+17.64%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 24,390.00 USD | 6,760.00 USD | 0.00 USD | `+18.96%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 25,700.00 USD | 1,310.00 USD | 0.00 USD | `+19.22%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 30,640.00 USD | 4,940.00 USD | 0.00 USD | `+19.88%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 30,810.00 USD | 171.49 USD | 0.00 USD | `+21.06%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 31,610.00 USD | 805.37 USD | 0.00 USD | `+22.51%` | `8,646.00` |
| `Live` | `Short` | `0.0943` | 32,750.00 USD | 1,140.00 USD | 0.00 USD | `+23.95%` | `12,089.00` |
| `Live` | `Short` | `0.0944` | 72,460.00 USD | 39,700.00 USD | 0.00 USD | `+24.09%` | `420,808.00` |
| `Live` | `Short` | `0.0948` | 76,720.00 USD | 4,260.00 USD | 0.00 USD | `+24.61%` | `45,000.00` |
| `Live` | `Short` | `0.0950` | 101,190.00 USD | 24,460.00 USD | 0.00 USD | `+24.88%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 101,950.00 USD | 761.26 USD | 0.00 USD | `+25.01%` | `8,009.00` |
| `Live` | `Short` | `0.0955` | 150,850.00 USD | 48,900.00 USD | 0.00 USD | `+25.66%` | `511,771.00` |
| `Live` | `Short` | `0.0961` | 151,460.00 USD | 609.59 USD | 0.00 USD | `+26.45%` | `6,340.00` |
| `Live` | `Short` | `0.0974` | 151,580.00 USD | 121.23 USD | 0.00 USD | `+28.16%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 152,050.00 USD | 477.50 USD | 0.00 USD | `+29.22%` | `4,860.00` |
| `Live` | `Short` | `0.0995` | 154,960.00 USD | 2,910.00 USD | 0.00 USD | `+30.92%` | `29,217.00` |
| `Live` | `Short` | `0.1002` | 155,160.00 USD | 201.80 USD | 0.00 USD | `+31.71%` | `2,015.00` |
| `Live` | `Short` | `0.1014` | 162,790.00 USD | 7,630.00 USD | 0.00 USD | `+33.42%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 165,760.00 USD | 2,970.00 USD | 0.00 USD | `+33.69%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 166,250.00 USD | 492.85 USD | 0.00 USD | `+33.95%` | `4,839.00` |
| `Live` | `Short` | `0.1023` | 169,430.00 USD | 3,170.00 USD | 0.00 USD | `+34.61%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 175,540.00 USD | 6,110.00 USD | 0.00 USD | `+39.60%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 176,150.00 USD | 616.19 USD | 0.00 USD | `+41.58%` | `5,724.00` |
| `Live` | `Short` | `0.1084` | 178,010.00 USD | 1,860.00 USD | 0.00 USD | `+42.50%` | `17,184.00` |
| `Live` | `Short` | `0.1085` | 181,250.00 USD | 3,240.00 USD | 0.00 USD | `+42.76%` | `29,849.00` |
| `Live` | `Short` | `0.1127` | 181,470.00 USD | 214.15 USD | 0.00 USD | `+48.15%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 181,610.00 USD | 142.88 USD | 0.00 USD | `+48.55%` | `1,265.00` |
| `Live` | `Short` | `0.1158` | 181,740.00 USD | 131.49 USD | 0.00 USD | `+52.36%` | `1,135.00` |
| `Live` | `Short` | `0.1218` | 184,120.00 USD | 2,370.00 USD | 0.00 USD | `+60.25%` | `19,483.00` |
| `Live` | `Short` | `0.1222` | 184,750.00 USD | 637.53 USD | 0.00 USD | `+60.78%` | `5,215.00` |
| `Live` | `Short` | `0.1236` | 184,870.00 USD | 119.32 USD | 0.00 USD | `+62.62%` | `965.00` |
| `Live` | `Short` | `0.1249` | 186,110.00 USD | 1,240.00 USD | 0.00 USD | `+64.20%` | `9,926.00` |
| `Live` | `Short` | `0.1270` | 186,220.00 USD | 108.80 USD | 0.00 USD | `+66.96%` | `857.00` |
| `Live` | `Short` | `0.1283` | 187,150.00 USD | 926.56 USD | 0.00 USD | `+68.80%` | `7,219.00` |
| `Live` | `Short` | `0.1296` | 187,320.00 USD | 171.66 USD | 0.00 USD | `+70.51%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 189,460.00 USD | 2,140.00 USD | 0.00 USD | `+72.48%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 189,560.00 USD | 102.97 USD | 0.00 USD | `+73.40%` | `781.00` |
| `Live` | `Short` | `0.1325` | 234,890.00 USD | 45,330.00 USD | 0.00 USD | `+74.19%` | `342,231.00` |
| `Live` | `Short` | `0.1336` | 269,390.00 USD | 34,500.00 USD | 0.00 USD | `+75.64%` | `258,360.00` |
| `Live` | `Short` | `0.1338` | 269,600.00 USD | 205.31 USD | 0.00 USD | `+75.90%` | `1,535.00` |
| `Live` | `Short` | `0.1346` | 269,730.00 USD | 134.42 USD | 0.00 USD | `+76.96%` | `999.00` |
| `Live` | `Short` | `0.1378` | 275,980.00 USD | 6,240.00 USD | 0.00 USD | `+81.16%` | `45,319.00` |
| `Live` | `Short` | `0.1384` | 298,430.00 USD | 22,450.00 USD | 0.00 USD | `+82.08%` | `162,180.00` |
| `Live` | `Short` | `0.1404` | 298,530.00 USD | 100.35 USD | 0.00 USD | `+84.58%` | `715.00` |
| `Live` | `Short` | `0.1404` | 299,190.00 USD | 663.63 USD | 0.00 USD | `+84.72%` | `4,725.00` |
| `Live` | `Short` | `0.1432` | 301,060.00 USD | 1,860.00 USD | 0.00 USD | `+88.40%` | `13,010.00` |
| `Live` | `Short` | `0.1434` | 302,960.00 USD | 1,900.00 USD | 0.00 USD | `+88.66%` | `13,240.00` |
| `Live` | `Short` | `0.1441` | 303,150.00 USD | 196.63 USD | 0.00 USD | `+89.45%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 304,700.00 USD | 1,540.00 USD | 0.00 USD | `+89.84%` | `10,691.00` |
| `Live` | `Short` | `0.1470` | 306,760.00 USD | 2,060.00 USD | 0.00 USD | `+93.40%` | `14,000.00` |
| `Live` | `Short` | `0.1472` | 307,200.00 USD | 441.45 USD | 0.00 USD | `+93.53%` | `3,000.00` |
| `Live` | `Short` | `0.1479` | 315,380.00 USD | 8,180.00 USD | 0.00 USD | `+94.45%` | `55,317.00` |
| `Live` | `Short` | `0.1487` | 321,860.00 USD | 6,480.00 USD | 0.00 USD | `+95.50%` | `43,601.00` |
| `Live` | `Short` | `0.1500` | 345,990.00 USD | 24,130.00 USD | 0.00 USD | `+97.34%` | `160,802.00` |
| `Live` | `Short` | `0.1515` | 347,310.00 USD | 1,320.00 USD | 0.00 USD | `+99.31%` | `8,712.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 946,080.00 USD | 0.00 USD | 375.42 USD | `-66.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 945,700.00 USD | 0.00 USD | 409.59 USD | `-47.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 945,290.00 USD | 0.00 USD | 132.68 USD | `-46.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 945,160.00 USD | 0.00 USD | 788.27 USD | `-45.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 944,370.00 USD | 0.00 USD | 527.05 USD | `-45.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 943,850.00 USD | 0.00 USD | 286.87 USD | `-40.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 943,560.00 USD | 0.00 USD | 252.42 USD | `-39.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 943,310.00 USD | 0.00 USD | 468.67 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 942,840.00 USD | 0.00 USD | 5,160.00 USD | `-35.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 937,680.00 USD | 0.00 USD | 920.48 USD | `-35.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 936,760.00 USD | 0.00 USD | 236.01 USD | `-34.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 936,520.00 USD | 0.00 USD | 175.41 USD | `-32.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 936,350.00 USD | 0.00 USD | 242.96 USD | `-32.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 936,110.00 USD | 0.00 USD | 2,670.00 USD | `-28.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 933,430.00 USD | 0.00 USD | 1,370.00 USD | `-27.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 932,060.00 USD | 0.00 USD | 437.58 USD | `-26.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 931,620.00 USD | 0.00 USD | 752.54 USD | `-23.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 930,870.00 USD | 0.00 USD | 9,830.00 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 921,040.00 USD | 0.00 USD | 952.91 USD | `-22.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 920,080.00 USD | 0.00 USD | 668.84 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 919,420.00 USD | 0.00 USD | 273.90 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 919,140.00 USD | 0.00 USD | 8,800.00 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 910,340.00 USD | 0.00 USD | 218.94 USD | `-20.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 910,120.00 USD | 0.00 USD | 504.26 USD | `-18.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 909,620.00 USD | 0.00 USD | 2,470.00 USD | `-18.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 907,150.00 USD | 0.00 USD | 118.27 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 907,030.00 USD | 0.00 USD | 1,280.00 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 905,750.00 USD | 0.00 USD | 1,820.00 USD | `-16.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 903,930.00 USD | 0.00 USD | 1,340.00 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 902,590.00 USD | 0.00 USD | 386.70 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 902,210.00 USD | 0.00 USD | 644.50 USD | `-15.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 901,560.00 USD | 0.00 USD | 19,520.00 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 882,050.00 USD | 0.00 USD | 1,410.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 880,640.00 USD | 0.00 USD | 3,140.00 USD | `-13.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 877,500.00 USD | 0.00 USD | 1,100.00 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 876,400.00 USD | 0.00 USD | 1,200.00 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 875,200.00 USD | 0.00 USD | 996.31 USD | `-13.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 874,200.00 USD | 0.00 USD | 909.85 USD | `-11.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 873,290.00 USD | 0.00 USD | 115.57 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 873,180.00 USD | 0.00 USD | 33,620.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 839,550.00 USD | 0.00 USD | 12,860.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 826,690.00 USD | 0.00 USD | 1,540.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 825,150.00 USD | 0.00 USD | 108.08 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 825,040.00 USD | 0.00 USD | 19,540.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 805,500.00 USD | 0.00 USD | 1,430.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 804,070.00 USD | 0.00 USD | 7,990.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 796,080.00 USD | 0.00 USD | 8,580.00 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 787,500.00 USD | 0.00 USD | 4,970.00 USD | `-10.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 782,530.00 USD | 0.00 USD | 3,100.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 779,440.00 USD | 0.00 USD | 160.31 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 779,280.00 USD | 0.00 USD | 38,710.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 740,570.00 USD | 0.00 USD | 295,640.00 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 444,930.00 USD | 0.00 USD | 2,590.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 442,350.00 USD | 0.00 USD | 533.09 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 441,810.00 USD | 0.00 USD | 378.50 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 441,430.00 USD | 0.00 USD | 925.29 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 440,510.00 USD | 0.00 USD | 797.80 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 439,710.00 USD | 0.00 USD | 11,920.00 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 427,790.00 USD | 0.00 USD | 141.77 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 427,650.00 USD | 0.00 USD | 895.27 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 426,760.00 USD | 0.00 USD | 523.23 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 426,230.00 USD | 0.00 USD | 468.88 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 425,770.00 USD | 0.00 USD | 235.12 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 425,530.00 USD | 0.00 USD | 1,090.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 424,440.00 USD | 0.00 USD | 71,660.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 352,780.00 USD | 0.00 USD | 497.62 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 352,280.00 USD | 0.00 USD | 20,330.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 331,950.00 USD | 0.00 USD | 608.76 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 331,340.00 USD | 0.00 USD | 16,880.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 314,470.00 USD | 0.00 USD | 265.67 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 314,200.00 USD | 0.00 USD | 1,670.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 312,530.00 USD | 0.00 USD | 4,210.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 308,320.00 USD | 0.00 USD | 13,550.00 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 294,770.00 USD | 0.00 USD | 413.42 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 294,360.00 USD | 0.00 USD | 138,380.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 155,980.00 USD | 0.00 USD | 849.15 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 155,130.00 USD | 0.00 USD | 34,460.00 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 120,660.00 USD | 0.00 USD | 2,030.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 118,640.00 USD | 0.00 USD | 3,400.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 115,240.00 USD | 0.00 USD | 29,060.00 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 86,170.00 USD | 0.00 USD | 4,110.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 82,060.00 USD | 0.00 USD | 2,090.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 79,970.00 USD | 0.00 USD | 1,950.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 78,020.00 USD | 0.00 USD | 535.16 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 77,480.00 USD | 0.00 USD | 123.40 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 77,360.00 USD | 0.00 USD | 397.76 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 76,960.00 USD | 0.00 USD | 398.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 76,560.00 USD | 0.00 USD | 797.39 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 75,770.00 USD | 0.00 USD | 27,920.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 47,850.00 USD | 0.00 USD | 1,640.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 46,210.00 USD | 0.00 USD | 7,330.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 38,880.00 USD | 0.00 USD | 2,900.00 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 35,980.00 USD | 0.00 USD | 415.62 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 35,570.00 USD | 0.00 USD | 16,520.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 19,050.00 USD | 0.00 USD | 398.54 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 18,650.00 USD | 0.00 USD | 375.86 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 18,280.00 USD | 0.00 USD | 399.17 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 17,880.00 USD | 0.00 USD | 140.04 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 17,740.00 USD | 0.00 USD | 6,280.00 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 11,460.00 USD | 0.00 USD | 3,450.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 8,010.00 USD | 0.00 USD | 736.17 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 7,270.00 USD | 0.00 USD | 406.95 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 6,860.00 USD | 0.00 USD | 221.00 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 6,640.00 USD | 0.00 USD | 407.73 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 6,240.00 USD | 0.00 USD | 408.57 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 5,830.00 USD | 0.00 USD | 408.81 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 5,420.00 USD | 0.00 USD | 4,520.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 902.23 USD | 0.00 USD | 504.10 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 398.13 USD | 0.00 USD | 398.13 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 113.01 USD | 113.01 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 919.82 USD | 806.81 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 1,730.00 USD | 814.81 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 5,510.00 USD | 3,770.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 5,620.00 USD | 109.63 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 6,860.00 USD | 1,250.00 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 7,050.00 USD | 183.50 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 7,890.00 USD | 843.94 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 8,390.00 USD | 502.52 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 9,210.00 USD | 816.05 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 9,480.00 USD | 266.52 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 11,720.00 USD | 2,240.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 11,960.00 USD | 240.02 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 15,890.00 USD | 3,930.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 16,300.00 USD | 407.23 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 16,620.00 USD | 321.13 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 18,110.00 USD | 1,490.00 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 18,520.00 USD | 407.72 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 18,850.00 USD | 329.23 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 19,150.00 USD | 303.77 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 19,340.00 USD | 186.07 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 22,420.00 USD | 3,080.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 23,610.00 USD | 1,200.00 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 27,980.00 USD | 4,370.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 28,140.00 USD | 157.14 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 28,270.00 USD | 130.71 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 69,880.00 USD | 41,610.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 72,910.00 USD | 3,030.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 73,680.00 USD | 773.68 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 74,360.00 USD | 673.60 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 82,220.00 USD | 7,860.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 86,820.00 USD | 4,600.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 92,080.00 USD | 5,270.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 99,900.00 USD | 7,820.00 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 100,220.00 USD | 312.56 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 100,670.00 USD | 455.34 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 100,800.00 USD | 125.45 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 101,030.00 USD | 230.40 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 101,350.00 USD | 319.16 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 102,350.00 USD | 1,010.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 125,100.00 USD | 22,750.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 125,500.00 USD | 400.91 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 125,700.00 USD | 200.46 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 125,960.00 USD | 259.13 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 126,670.00 USD | 707.08 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 135,680.00 USD | 9,010.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 232,460.00 USD | 96,780.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 233,270.00 USD | 807.50 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 233,520.00 USD | 257.18 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 233,950.00 USD | 424.74 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 234,050.00 USD | 101.80 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 235,430.00 USD | 1,380.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 237,460.00 USD | 2,030.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 238,890.00 USD | 1,430.00 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 239,020.00 USD | 129.67 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 240,040.00 USD | 1,020.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 242,490.00 USD | 2,450.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 243,510.00 USD | 1,030.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 246,530.00 USD | 3,020.00 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 246,860.00 USD | 327.80 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 247,320.00 USD | 457.92 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 248,010.00 USD | 691.29 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 248,810.00 USD | 800.79 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 249,320.00 USD | 512.05 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 249,820.00 USD | 495.36 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 250,210.00 USD | 389.31 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 250,360.00 USD | 154.58 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 250,670.00 USD | 303.56 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 250,780.00 USD | 112.89 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 251,160.00 USD | 381.45 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 251,320.00 USD | 155.82 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 295,700.00 USD | 44,390.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 295,840.00 USD | 138.69 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 297,100.00 USD | 1,260.00 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 297,210.00 USD | 107.03 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,040,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,040,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,050,000.00 USD | 1,470.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,050,000.00 USD | 107.71 USD | 0.00 USD | `+10.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,050,000.00 USD | 2,690.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,050,000.00 USD | 529.92 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,050,000.00 USD | 219.07 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,050,000.00 USD | 242.84 USD | 0.00 USD | `+11.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,060,000.00 USD | 10,140.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,060,000.00 USD | 876.11 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,060,000.00 USD | 812.54 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,060,000.00 USD | 126.76 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,060,000.00 USD | 307.41 USD | 0.00 USD | `+12.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,060,000.00 USD | 614.09 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,060,000.00 USD | 859.50 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,070,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,110,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,110,000.00 USD | 123.94 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,110,000.00 USD | 271.53 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,110,000.00 USD | 857.15 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,110,000.00 USD | 1,840.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,110,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,110,000.00 USD | 117.71 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,120,000.00 USD | 111.61 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,120,000.00 USD | 571.18 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,120,000.00 USD | 375.94 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,120,000.00 USD | 627.55 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,120,000.00 USD | 211.04 USD | 0.00 USD | `+16.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,120,000.00 USD | 108.36 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,120,000.00 USD | 543.32 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,120,000.00 USD | 1,820.00 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,120,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,140,000.00 USD | 17,680.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,140,000.00 USD | 1,370.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,150,000.00 USD | 5,630.00 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,150,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,150,000.00 USD | 224.86 USD | 0.00 USD | `+18.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,170,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,170,000.00 USD | 114.93 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,170,000.00 USD | 679.12 USD | 0.00 USD | `+19.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,170,000.00 USD | 173.36 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,170,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,170,000.00 USD | 1,480.00 USD | 0.00 USD | `+20.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,170,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,170,000.00 USD | 541.32 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,310,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,310,000.00 USD | 691.07 USD | 0.00 USD | `+21.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,320,000.00 USD | 6,250.00 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,330,000.00 USD | 13,480.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,330,000.00 USD | 734.82 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,330,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,330,000.00 USD | 105.00 USD | 0.00 USD | `+22.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,340,000.00 USD | 184.09 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,340,000.00 USD | 1,120.00 USD | 0.00 USD | `+23.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,340,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,340,000.00 USD | 1,070.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,340,000.00 USD | 512.15 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,350,000.00 USD | 6,620.00 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,350,000.00 USD | 404.96 USD | 0.00 USD | `+24.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,350,000.00 USD | 129.85 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,350,000.00 USD | 3,740.00 USD | 0.00 USD | `+25.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,350,000.00 USD | 409.17 USD | 0.00 USD | `+26.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,350,000.00 USD | 203.74 USD | 0.00 USD | `+27.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,350,000.00 USD | 2,800.00 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,360,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,360,000.00 USD | 694.56 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,360,000.00 USD | 940.91 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,360,000.00 USD | 2,980.00 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,360,000.00 USD | 104.99 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,360,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,360,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,360,000.00 USD | 1,090.00 USD | 0.00 USD | `+30.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,360,000.00 USD | 438.96 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,370,000.00 USD | 973.76 USD | 0.00 USD | `+31.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,380,000.00 USD | 10,000.00 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,380,000.00 USD | 175.59 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,380,000.00 USD | 2,060.00 USD | 0.00 USD | `+31.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,380,000.00 USD | 482.89 USD | 0.00 USD | `+32.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,380,000.00 USD | 201.90 USD | 0.00 USD | `+32.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,380,000.00 USD | 489.46 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,380,000.00 USD | 103.68 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,380,000.00 USD | 2,590.00 USD | 0.00 USD | `+33.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,390,000.00 USD | 3,810.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,400,000.00 USD | 11,200.00 USD | 0.00 USD | `+34.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,400,000.00 USD | 4,330.00 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,400,000.00 USD | 205.50 USD | 0.00 USD | `+35.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,410,000.00 USD | 3,490.00 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,410,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,410,000.00 USD | 207.50 USD | 0.00 USD | `+36.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,410,000.00 USD | 813.88 USD | 0.00 USD | `+37.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,430,000.00 USD | 23,160.00 USD | 0.00 USD | `+37.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,430,000.00 USD | 781.51 USD | 0.00 USD | `+37.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,430,000.00 USD | 209.30 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,430,000.00 USD | 1,440.00 USD | 0.00 USD | `+37.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,440,000.00 USD | 5,140.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,440,000.00 USD | 585.32 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,440,000.00 USD | 210.90 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,440,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,440,000.00 USD | 105.75 USD | 0.00 USD | `+39.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,440,000.00 USD | 3,220.00 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,450,000.00 USD | 1,600.00 USD | 0.00 USD | `+39.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,450,000.00 USD | 212.90 USD | 0.00 USD | `+40.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,450,000.00 USD | 472.63 USD | 0.00 USD | `+40.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,450,000.00 USD | 214.50 USD | 0.00 USD | `+41.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,450,000.00 USD | 1,040.00 USD | 0.00 USD | `+41.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,450,000.00 USD | 136.12 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,450,000.00 USD | 216.10 USD | 0.00 USD | `+42.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,450,000.00 USD | 1,010.00 USD | 0.00 USD | `+43.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,450,000.00 USD | 217.90 USD | 0.00 USD | `+43.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,450,000.00 USD | 219.70 USD | 0.00 USD | `+44.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,460,000.00 USD | 7,920.00 USD | 0.00 USD | `+44.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,460,000.00 USD | 154.22 USD | 0.00 USD | `+45.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,460,000.00 USD | 221.30 USD | 0.00 USD | `+45.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,460,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,480,000.00 USD | 24,440.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,480,000.00 USD | 223.10 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,480,000.00 USD | 224.70 USD | 0.00 USD | `+47.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,480,000.00 USD | 226.30 USD | 0.00 USD | `+48.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,480,000.00 USD | 950.34 USD | 0.00 USD | `+49.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,490,000.00 USD | 229.50 USD | 0.00 USD | `+50.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,490,000.00 USD | 771.08 USD | 0.00 USD | `+51.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,490,000.00 USD | 942.95 USD | 0.00 USD | `+51.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,490,000.00 USD | 230.90 USD | 0.00 USD | `+51.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,490,000.00 USD | 288.18 USD | 0.00 USD | `+51.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,490,000.00 USD | 619.10 USD | 0.00 USD | `+52.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,490,000.00 USD | 1,250.00 USD | 0.00 USD | `+52.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,490,000.00 USD | 1,050.00 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,490,000.00 USD | 232.30 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,490,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,490,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,500,000.00 USD | 3,730.00 USD | 0.00 USD | `+54.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,500,000.00 USD | 676.22 USD | 0.00 USD | `+54.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,500,000.00 USD | 648.25 USD | 0.00 USD | `+55.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,500,000.00 USD | 1,510.00 USD | 0.00 USD | `+55.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,500,000.00 USD | 448.52 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,500,000.00 USD | 124.58 USD | 0.00 USD | `+56.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,500,000.00 USD | 691.80 USD | 0.00 USD | `+57.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,620,000.00 USD | 117,860.00 USD | 0.00 USD | `+57.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,620,000.00 USD | 143.22 USD | 0.00 USD | `+58.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,620,000.00 USD | 1,380.00 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,620,000.00 USD | 2,270.00 USD | 0.00 USD | `+60.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,620,000.00 USD | 871.99 USD | 0.00 USD | `+60.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,650,000.00 USD | 29,610.00 USD | 0.00 USD | `+66.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,650,000.00 USD | 400.21 USD | 0.00 USD | `+67.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,670,000.00 USD | 13,850.00 USD | 0.00 USD | `+73.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,670,000.00 USD | 2,360.00 USD | 0.00 USD | `+73.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,670,000.00 USD | 4,160.00 USD | 0.00 USD | `+78.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,680,000.00 USD | 114.70 USD | 0.00 USD | `+79.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,680,000.00 USD | 278.50 USD | 0.00 USD | `+84.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,680,000.00 USD | 1,160.00 USD | 0.00 USD | `+86.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,680,000.00 USD | 173.57 USD | 0.00 USD | `+86.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,680,000.00 USD | 380.09 USD | 0.00 USD | `+87.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,690,000.00 USD | 17,150.00 USD | 0.00 USD | `+87.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,700,000.00 USD | 1,440.00 USD | 0.00 USD | `+89.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,700,000.00 USD | 433.35 USD | 0.00 USD | `+89.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,700,000.00 USD | 452.26 USD | 0.00 USD | `+91.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,700,000.00 USD | 3,640.00 USD | 0.00 USD | `+93.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,760,000.00 USD | 55,720.00 USD | 0.00 USD | `+94.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,760,000.00 USD | 2,120.00 USD | 0.00 USD | `+94.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,780,000.00 USD | 19,850.00 USD | 0.00 USD | `+97.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,780,000.00 USD | 1,620.00 USD | 0.00 USD | `+99.05%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0678` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD |
| `1D` | `0.0679` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD |
| `1D` | `0.0680` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0681` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 134,240.00 USD |
| `1D` | `0.0682` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,630.00 USD |
| `1D` | `0.0683` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 0.00 USD | 20,340.00 USD | 723.57 USD |
| `1D` | `0.0684` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 24,150.00 USD | 15,070.00 USD | 584.27 USD |
| `1D` | `0.0685` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 41,510.00 USD | 12,720.00 USD | 17,260.00 USD |
| `1D` | `0.0686` | 11,320,000.00 USD | 0.00 USD | 11,320,000.00 USD | 41,080.00 USD | 1,410.00 USD | 13,570.00 USD |
| `1D` | `0.0687` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD |
| `1D` | `0.0688` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0691` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD |
| `1D` | `0.0698` | 11,140,000.00 USD | 0.00 USD | 11,140,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,650.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,850.00 USD |
| `1D` | `0.0700` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 35,400.00 USD | 18,030.00 USD | 29,630.00 USD |
| `1D` | `0.0702` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 78,740.00 USD | 36,780.00 USD | 164.89 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 87,540.00 USD | 31,470.00 USD | 41,850.00 USD |
| `1D` | `0.0704` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,120.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 41,490.00 USD | 24,910.00 USD | 32,230.00 USD |
| `1D` | `0.0706` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 36,930.00 USD | 29,080.00 USD | 26,890.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 54,240.00 USD | 21,680.00 USD | 23,150.00 USD |
| `1D` | `0.0708` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 25,410.00 USD | 16,310.00 USD | 27,960.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 36,740.00 USD | 37,120.00 USD | 15,180.00 USD |
| `1D` | `0.0710` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,580.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,320.00 USD |
| `1D` | `0.0712` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 35,120.00 USD | 58,130.00 USD | 67,120.00 USD |
| `1D` | `0.0714` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 34,440.00 USD | 8,830.00 USD | 38,710.00 USD |
| `1D` | `0.0716` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 24,840.00 USD | 31,610.00 USD | 0.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 10,910.00 USD | 7,710.00 USD | 21,890.00 USD |
| `1D` | `0.0718` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 67,080.00 USD | 31,390.00 USD | 32,350.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 10,150.00 USD | 0.00 USD | 2,170.00 USD |
| `1D` | `0.0720` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 31,160.00 USD | 29,440.00 USD | 32,460.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 136,510.00 USD | 76,220.00 USD | 15,670.00 USD |
| `1D` | `0.0722` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,670.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 54,790.00 USD | 162,040.00 USD | 153,140.00 USD |
| `1D` | `0.0724` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 27,830.00 USD | 87,980.00 USD | 92,380.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 54,140.00 USD | 22,980.00 USD | 23,580.00 USD |
| `1D` | `0.0726` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 51,960.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 168,660.00 USD | 0.00 USD | 345,080.00 USD |
| `1D` | `0.0728` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 66,510.00 USD | 85,670.00 USD | 75,670.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 19,510.00 USD | 82,260.00 USD | 30,250.00 USD |
| `1D` | `0.0730` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 112,200.00 USD | 54,520.00 USD | 1,580.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 152,870.00 USD | 49,300.00 USD | 43,260.00 USD |
| `1D` | `0.0732` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 154,930.00 USD | 60,240.00 USD | 81,810.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 15,550.00 USD | 0.00 USD | 71,460.00 USD |
| `1D` | `0.0734` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 33,390.00 USD | 31,100.00 USD | 299.76 USD |
| `1D` | `0.0736` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 234,720.00 USD | 123,630.00 USD | 1.38 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 51,890.00 USD | 42,510.00 USD | 636.56 USD |
| `1D` | `0.0738` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,360.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,490.00 USD |
| `1D` | `0.0740` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 33,740.00 USD | 0.00 USD | 267.65 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 36,980.00 USD | 0.00 USD | 560.08 USD |
| `1D` | `0.0742` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 286,340.00 USD | 0.00 USD | 684,970.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 118,640.00 USD | 234,470.00 USD | 190,020.00 USD |
| `1D` | `0.0744` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 19,880.00 USD | 187,400.00 USD | 59,430.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 199,850.00 USD | 166,270.00 USD | 24,880.00 USD |
| `1D` | `0.0746` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 371,240.00 USD | 274,020.00 USD | 211,560.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 466,980.00 USD | 159,330.00 USD | 131,210.00 USD |
| `1D` | `0.0748` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 130,290.00 USD | 143,100.00 USD | 194,200.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 635,760.00 USD | 0.00 USD | 635,760.00 USD | 203,330.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `0.0750` | 282,960.00 USD | 0.00 USD | 282,960.00 USD | 69,890.00 USD | 0.00 USD | 120,790.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 92,290.00 USD | 0.00 USD | 92,290.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 85,440.00 USD | 0.00 USD | 85,440.00 USD | 0.00 USD | 85,010.00 USD | 0.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0760` | 424.91 USD | 0.00 USD | 424.91 USD | 0.00 USD | 0.00 USD | 424.91 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 412.85 USD | 412.85 USD | 0.00 USD | 0.00 USD | 0.00 USD | 412.85 USD |
| `1D` | `0.0761` | 825.70 USD | 825.70 USD | 0.00 USD | 0.00 USD | 0.00 USD | 412.85 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 14,210.00 USD | 14,210.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD | 168.86 USD |
| `1D` | `0.0764` | 340,180.00 USD | 340,180.00 USD | 0.00 USD | 0.00 USD | 325,960.00 USD | 0.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 598,420.00 USD | 598,420.00 USD | 0.00 USD | 0.00 USD | 257,590.00 USD | 656.49 USD |
| `1D` | `0.0766` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 745,930.00 USD | 360,800.00 USD | 0.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 169,980.00 USD | 188,260.00 USD | 502.92 USD |
| `1D` | `0.0768` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 351,760.00 USD | 0.00 USD | 514,350.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 181,440.00 USD | 341,350.00 USD | 148,810.00 USD |
| `1D` | `0.0770` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 272,760.00 USD | 93,300.00 USD | 253,920.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 216,410.00 USD | 232,340.00 USD | 212,480.00 USD |
| `1D` | `0.0772` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 286,340.00 USD | 0.00 USD | 685,130.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 65,160.00 USD | 169,730.00 USD | 149,070.00 USD |
| `1D` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 164,510.00 USD | 19,440.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 155,740.00 USD | 109,050.00 USD | 0.00 USD |
| `1D` | `0.0776` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 190,100.00 USD | 110,600.00 USD | 86,320.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 205,390.00 USD | 264,690.00 USD | 80,710.00 USD |
| `1D` | `0.0778` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 16,790.00 USD | 202,930.00 USD | 295,930.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 85,950.00 USD | 140,460.00 USD |
| `1D` | `0.0780` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 69,890.00 USD | 31,980.00 USD | 253.82 USD |
| `1D` | `0.0781` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 113,060.00 USD | 68,670.00 USD | 1,410.00 USD |
| `1D` | `0.0782` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 8,010.00 USD | 184,740.00 USD | 145,430.00 USD |
| `1D` | `0.0784` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 191,180.00 USD | 117,040.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 298,820.00 USD | 307,550.00 USD | 344,880.00 USD |
| `1D` | `0.0788` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 75,490.00 USD | 181,170.00 USD | 75,110.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 234,900.00 USD | 192,150.00 USD | 96,560.00 USD |
| `1D` | `0.0790` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 102,120.00 USD | 57,780.00 USD | 1,460.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 152,950.00 USD | 95,070.00 USD | 95,210.00 USD |
| `1D` | `0.0792` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 104,950.00 USD | 18,870.00 USD | 33,930.00 USD |
| `1D` | `0.0794` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 92,580.00 USD | 41,370.00 USD | 47,790.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 10,150.00 USD | 0.00 USD | 73,430.00 USD |
| `1D` | `0.0796` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 16,850.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 191,110.00 USD | 89,760.00 USD | 242,940.00 USD |
| `1D` | `0.0798` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD |
| `1D` | `0.0800` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD |
| `1D` | `0.0801` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 6,300.00 USD | 0.00 USD | 2,110.00 USD |
| `1D` | `0.0802` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 7,730.00 USD | 1,770.00 USD | 2,600.00 USD |
| `1D` | `0.0803` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 38,610.00 USD |
| `1D` | `0.0804` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD |
| `1D` | `0.0806` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 221,690.00 USD | 208,070.00 USD | 41,170.00 USD |
| `1D` | `0.0808` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 419,500.00 USD | 131,030.00 USD | 523,560.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 17,490,000.00 USD | 17,490,000.00 USD | 0.00 USD | 477,790.00 USD | 336,610.00 USD | 12,790.00 USD |
| `1D` | `0.0810` | 18,100,000.00 USD | 18,100,000.00 USD | 0.00 USD | 293,220.00 USD | 180,540.00 USD | 133,520.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 18,430,000.00 USD | 18,430,000.00 USD | 0.00 USD | 83,280.00 USD | 241,410.00 USD | 875.97 USD |
| `1D` | `0.0812` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 144,600.00 USD | 99,490.00 USD | 120,600.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 19,070,000.00 USD | 19,070,000.00 USD | 0.00 USD | 49,290.00 USD | 23,210.00 USD | 208,970.00 USD |
| `1D` | `0.0814` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 29,840.00 USD | 79,960.00 USD | 292,740.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 150,190.00 USD | 72,710.00 USD | 124,900.00 USD |
| `1D` | `0.0816` | 20,540,000.00 USD | 20,540,000.00 USD | 0.00 USD | 348,980.00 USD | 194,790.00 USD | 177,540.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 21,100,000.00 USD | 21,100,000.00 USD | 0.00 USD | 301,230.00 USD | 127,050.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 21,840,000.00 USD | 21,840,000.00 USD | 0.00 USD | 269,340.00 USD | 161,260.00 USD | 308,240.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 174,640.00 USD | 312,480.00 USD | 128,780.00 USD |
| `1D` | `0.0820` | 23,140,000.00 USD | 23,140,000.00 USD | 0.00 USD | 136,010.00 USD | 202,840.00 USD | 344,550.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 210,590.00 USD | 79,630.00 USD | 170,610.00 USD |
| `1D` | `0.0822` | 24,190,000.00 USD | 24,190,000.00 USD | 0.00 USD | 262,170.00 USD | 169,200.00 USD | 156,380.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 270,850.00 USD | 75,420.00 USD | 8,520.00 USD |
| `1D` | `0.0824` | 25,120,000.00 USD | 25,120,000.00 USD | 0.00 USD | 151,910.00 USD | 226,510.00 USD | 198,590.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 25,400,000.00 USD | 25,400,000.00 USD | 0.00 USD | 127,790.00 USD | 122,020.00 USD | 27,800.00 USD |
| `1D` | `0.0826` | 25,820,000.00 USD | 25,820,000.00 USD | 0.00 USD | 150,570.00 USD | 84,820.00 USD | 190,080.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 25,920,000.00 USD | 25,920,000.00 USD | 0.00 USD | 49,040.00 USD | 48,230.00 USD | 399.88 USD |
| `1D` | `0.0828` | 26,270,000.00 USD | 26,270,000.00 USD | 0.00 USD | 216,200.00 USD | 75,940.00 USD | 58,410.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 26,640,000.00 USD | 26,640,000.00 USD | 0.00 USD | 182,720.00 USD | 111,290.00 USD | 72,580.00 USD |
| `1D` | `0.0830` | 26,960,000.00 USD | 26,960,000.00 USD | 0.00 USD | 140,600.00 USD | 84,690.00 USD | 98,250.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 27,030,000.00 USD | 27,030,000.00 USD | 0.00 USD | 39,850.00 USD | 0.00 USD | 24,360.00 USD |
| `1D` | `0.0832` | 27,340,000.00 USD | 27,340,000.00 USD | 0.00 USD | 171,130.00 USD | 66,230.00 USD | 80,110.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 27,680,000.00 USD | 27,680,000.00 USD | 0.00 USD | 119,590.00 USD | 55,260.00 USD | 165,680.00 USD |
| `1D` | `0.0834` | 28,030,000.00 USD | 28,030,000.00 USD | 0.00 USD | 127,020.00 USD | 94,190.00 USD | 126,700.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 0.00 USD | 104,680.00 USD | 176,580.00 USD | 65,050.00 USD |
| `1D` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 0.00 USD | 48,890.00 USD | 63,220.00 USD | 144,680.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 28,850,000.00 USD | 28,850,000.00 USD | 0.00 USD | 129,000.00 USD | 30,430.00 USD | 51,350.00 USD |
| `1D` | `0.0838` | 29,120,000.00 USD | 29,120,000.00 USD | 0.00 USD | 168,220.00 USD | 70,030.00 USD | 38,860.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 29,210,000.00 USD | 29,210,000.00 USD | 0.00 USD | 52,570.00 USD | 16,550.00 USD | 15,430.00 USD |
| `1D` | `0.0840` | 29,270,000.00 USD | 29,270,000.00 USD | 0.00 USD | 13,720.00 USD | 15,480.00 USD | 28,470.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 29,290,000.00 USD | 29,290,000.00 USD | 0.00 USD | 23,380.00 USD | 2,010.00 USD | 1,220.00 USD |
| `1D` | `0.0842` | 29,360,000.00 USD | 29,360,000.00 USD | 0.00 USD | 22,710.00 USD | 0.00 USD | 46,530.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 29,400,000.00 USD | 29,400,000.00 USD | 0.00 USD | 33,600.00 USD | 0.00 USD | 634.86 USD |
| `1D` | `0.0844` | 29,470,000.00 USD | 29,470,000.00 USD | 0.00 USD | 79,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 29,490,000.00 USD | 29,490,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | 264.53 USD |
| `1D` | `0.0846` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 29,590,000.00 USD | 29,590,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
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
  * Total Open Interest: `1.05B` | Total OI Tokens: `13,863,329,204.4 DOGE`
  * 1h OI Change: `+0.76%` | 4h OI Change: `-1.17%` | 24h OI Change: `-5.87%`
  * Exchange Breakdown: Binance=`242.95M` | Bybit=`106.38M` | OKX=`109.78M` | Hyperliquid=`76.24M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.20K` | Last 24h: `35.55K` | Last 3d: `229.21K` | Last 7d: `310.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0022%` | **USDT OKX** | `-0.0062%` |
| **USDT Bybit** | `-0.0034%` | **USDT KuCoin** | `-0.0095%` |
| **USDT MEXC** | `0.0020%` | **USDT BingX** | `0.0020%` |
| **USDT Gate** | `0.0040%` | **USDT Bitget** | `-0.0014%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `41.31%` | `58.69%` | `0.70` | 29,840,000.00 USD |
| `15M` | `Binance` | `42.12%` | `57.88%` | `0.73` | 19,990,000.00 USD |
| `15M` | `OKX` | `40.66%` | `59.34%` | `0.69` | 2,730,000.00 USD |
| `15M` | `Bybit` | `33.87%` | `66.13%` | `0.51` | 2,030,000.00 USD |
| `15M` | `KuCoin` | `53.03%` | `46.97%` | `1.13` | 255,460.00 USD |
| `15M` | `Gate` | `43.57%` | `56.43%` | `0.77` | 858,360.00 USD |
| `15M` | `Bitget` | `24.46%` | `75.54%` | `0.32` | 743,440.00 USD |
| `15M` | `BingX` | `61.41%` | `38.59%` | `1.59` | 457,700.00 USD |
| `15M` | `MEXC` | `41.67%` | `58.33%` | `0.71` | 369,650.00 USD |
| `15M` | `Bitunix` | `43.17%` | `56.83%` | `0.76` | 756,000.00 USD |
| `15M` | `Hyperliquid` | `46.99%` | `53.01%` | `0.89` | 682,280.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.94%` | `52.06%` | `0.92` | 71,720.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 6,440.00 USD |
| `15M` | `HTX` | `19.46%` | `80.54%` | `0.24` | 417,730.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `45.33%` | `54.67%` | `0.83` | 338,800.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.28%` | `50.72%` | `0.97` | 141,430.00 USD |
| `15M` | `Whale Positions` | `42.12%` | `57.88%` | `0.73` | 19,990,000.00 USD |
| `15M` | `Global Accounts` | `41.31%` | `58.69%` | `0.70` | 29,840,000.00 USD |
| `1H` | `DOGE` | `50.33%` | `49.67%` | `1.01` | 113,910,000.00 USD |
| `1H` | `Binance` | `49.88%` | `50.12%` | `1.00` | 69,800,000.00 USD |
| `1H` | `OKX` | `51.48%` | `48.52%` | `1.06` | 12,430,000.00 USD |
| `1H` | `Bybit` | `49.43%` | `50.57%` | `0.98` | 10,200,000.00 USD |
| `1H` | `KuCoin` | `52.13%` | `47.87%` | `1.09` | 672,050.00 USD |
| `1H` | `Gate` | `51.2%` | `48.8%` | `1.05` | 3,120,000.00 USD |
| `1H` | `Bitget` | `41.04%` | `58.96%` | `0.70` | 2,440,000.00 USD |
| `1H` | `BingX` | `42.35%` | `57.65%` | `0.73` | 2,030,000.00 USD |
| `1H` | `MEXC` | `53.47%` | `46.53%` | `1.15` | 1,150,000.00 USD |
| `1H` | `Bitunix` | `52.22%` | `47.78%` | `1.09` | 2,970,000.00 USD |
| `1H` | `Hyperliquid` | `64.06%` | `35.94%` | `1.78` | 4,810,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.83%` | `52.17%` | `0.92` | 444,310.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `22.17%` | `77.83%` | `0.28` | 67,640.00 USD |
| `1H` | `HTX` | `25.9%` | `74.1%` | `0.35` | 650,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `100%` | `0.00` | 3,750.00 USD |
| `1H` | `Aster` | `50.52%` | `49.48%` | `1.02` | 2,180,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.66%` | `45.34%` | `1.21` | 952,470.00 USD |
| `1H` | `Whale Positions` | `49.88%` | `50.12%` | `1.00` | 69,800,000.00 USD |
| `1H` | `Global Accounts` | `50.33%` | `49.67%` | `1.01` | 113,910,000.00 USD |
| `4H` | `DOGE` | `49.63%` | `50.37%` | `0.99` | 818,380,000.00 USD |
| `4H` | `Binance` | `49.48%` | `50.52%` | `0.98` | 523,110,000.00 USD |
| `4H` | `OKX` | `46.84%` | `53.16%` | `0.88` | 70,390,000.00 USD |
| `4H` | `Bybit` | `54.57%` | `45.43%` | `1.20` | 58,280,000.00 USD |
| `4H` | `KuCoin` | `57.25%` | `42.75%` | `1.34` | 4,750,000.00 USD |
| `4H` | `Gate` | `47.56%` | `52.44%` | `0.91` | 21,570,000.00 USD |
| `4H` | `Bitget` | `51.47%` | `48.53%` | `1.06` | 15,940,000.00 USD |
| `4H` | `BingX` | `40.47%` | `59.53%` | `0.68` | 12,830,000.00 USD |
| `4H` | `MEXC` | `53.99%` | `46.01%` | `1.17` | 8,940,000.00 USD |
| `4H` | `Bitunix` | `52.58%` | `47.42%` | `1.11` | 19,400,000.00 USD |
| `4H` | `Hyperliquid` | `52.62%` | `47.38%` | `1.11` | 42,890,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.24%` | `50.76%` | `0.97` | 4,970,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `30.18%` | `69.82%` | `0.43` | 508,300.00 USD |
| `4H` | `HTX` | `42.85%` | `57.15%` | `0.75` | 2,590,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.5%` | `36.5%` | `1.74` | 2,740,000.00 USD |
| `4H` | `Aster` | `50.75%` | `49.25%` | `1.03` | 20,430,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `30.43%` | `69.57%` | `0.44` | 9,030,000.00 USD |
| `4H` | `Whale Positions` | `49.48%` | `50.52%` | `0.98` | 523,110,000.00 USD |
| `4H` | `Global Accounts` | `49.63%` | `50.37%` | `0.99` | 818,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0739` | `0.0740` | `0.0739` | `0.0743` | `0.0738` | 4,177,023.31 USD | 1,948,188.05 USD | 2,228,835.27 USD | -280,647.22 USD | `-6.72%` | `6B / 5S` |
| `0:00 UTC` | `0.0737` | `0.0739` | `0.0737` | `0.0743` | `0.0736` | 6,164,268.63 USD | 2,938,067.77 USD | 3,226,200.86 USD | -288,133.08 USD | `-4.67%` | `9B / 6S` |
| `5:00 UTC` | `0.0749` | `0.0747` | `0.0749` | `0.0751` | `0.0743` | 6,484,284.24 USD | 3,589,529.58 USD | 2,894,754.66 USD | 694,774.91 USD | `+10.71%` | `19B / 5S` |
| `0:00 UTC` | `0.0749` | `0.0750` | `0.0749` | `0.0752` | `0.0748` | 6,915,504.04 USD | 3,908,951.74 USD | 3,006,552.30 USD | 902,399.44 USD | `+13.05%` | `6B / 3S` |
| `5:00 UTC` | `0.0749` | `0.0749` | `0.0749` | `0.0752` | `0.0748` | 4,286,041.88 USD | 2,098,889.29 USD | 2,187,152.59 USD | -88,263.30 USD | `-2.06%` | `4B / 13S` |
| `0:00 UTC` | `0.0751` | `0.0751` | `0.0751` | `0.0752` | `0.0749` | 4,647,855.36 USD | 2,795,154.23 USD | 1,852,701.13 USD | 942,453.10 USD | `+20.28%` | `6B / 2S` |
| `5:00 UTC` | `0.0753` | `0.0752` | `0.0753` | `0.0754` | `0.0750` | 3,128,035.72 USD | 1,829,490.22 USD | 1,298,545.51 USD | 530,944.71 USD | `+16.97%` | `7B / 3S` |
| `0:00 UTC` | `0.0758` | `0.0757` | `0.0758` | `0.0759` | `0.0754` | 5,177,761.26 USD | 2,608,553.38 USD | 2,569,207.88 USD | 39,345.50 USD | `+0.76%` | `6B / 5S` |
| `5:00 UTC` | `0.0761` | `0.0760` | `0.0761` | `0.0761` | `0.0758` | 4,745,125.96 USD | 2,439,783.51 USD | 2,305,342.45 USD | 134,441.06 USD | `+2.83%` | `2B / 3S` |
| `0:00 UTC` | `0.0760` | `0.0760` | `0.0760` | `0.0761` | `0.0760` | 203,562.69 USD | 52,725.37 USD | 150,837.32 USD | -98,111.95 USD | `-48.20%` | `0B / 3S` |

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
| `5m` | -178,060.00 USD | -495,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -71,600.00 USD | 979,930.00 USD | **`ACCUMULATION`** |
| `30m` | 65,560.00 USD | 2,190,000.00 USD | **`ACCUMULATION`** |
| `1h` | 494,180.00 USD | 4,170,000.00 USD | **`ACCUMULATION`** |
| `2h` | 2,720,000.00 USD | 6,860,000.00 USD | **`ACCUMULATION`** |
| `4h` | -7,250,000.00 USD | -13,350,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,530,000.00 USD | -16,780,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -17,780,000.00 USD | -50,690,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -21,730,000.00 USD | -57,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,580,000.00 USD | -60,170,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -60,310,000.00 USD | -183,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -285,260,000.00 USD | -795,750,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-178.06K` | 15m=`-71.60K` | 1h=`+494.18K` | 24h=`-18.58M`
* Futures Capital Netflows: 5m=`-495.00K` | 15m=`+979.93K` | 1h=`+4.17M` | 24h=`-60.17M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0732` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0692` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0837`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0797` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0652`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0763`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
