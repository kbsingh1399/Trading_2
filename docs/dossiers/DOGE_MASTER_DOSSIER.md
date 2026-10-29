# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 04:38:02 IST` (`2026-10-29 23:08:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0745` | **Live Ask Quote**: `0.0766` | **Mid Price**: `0.0756`
- **Spread Points**: `21.00` | **Spread BPS**: `277.96 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0769` | VWAP Z-Score: `-1.29` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000715` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.12` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0814` | Lower -3.00σ Band: `0.0725`
  * Upper +2.51σ Band: `0.0807` | Lower -2.51σ Band: `0.0732`
  * Upper +2.01σ Band: `0.0799` | Lower -2.01σ Band: `0.0739`
  * Upper +2.00σ Band: `0.0799` | Lower -2.00σ Band: `0.0739`
  * Upper +1.28σ Band: `0.0788` | Lower -1.28σ Band: `0.0750`
  * Upper +1.00σ Band: `0.0784` | Lower -1.00σ Band: `0.0754`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0753` | EMA-20=`0.0761` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0770` (Slope: `+0.0000`) | EMA-100=`0.0774`
  * Institutional Anchors: EMA-144=`0.0775` | EMA-200=`0.0774` (Slope: `-0.3489`) | EMA-233=`0.0774`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0733` | Weekly High=`0.0803` | Weekly Low=`0.0733`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0753` (Distance: `+0.45%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.00%`)
  * Value Area Low (VAL) = `0.0747` (Distance: `+1.33%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0784` | Weekly POC=`0.0761` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0738`
  * London Session (08:00-16:00 UTC): High=`0.0759` | Low=`0.0752`
  * New York Session (13:00-21:00 UTC): High=`0.0760` | Low=`0.0751`
  * Initial Balance (First Hour): IB High=`0.0758` | IB Low=`0.0753`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0752` - `0.0759`
  * Optimal Trade Entry (OTE 0.705): `0.0757`
  * Structural Invalidation Anchor (0.786): `0.0762`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0760` | `0.0762` | `0.0759` | `0.0761` | `19,827,121` | 1,508,187.58 USD | 196,310.79 USD | `+13.02%` | -31,479,145.88 USD | `+0.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.0761` | `0.0762` | `0.0756` | `0.0757` | `34,838,670` | 2,641,803.07 USD | -846,072.20 USD | `-32.03%` | -32,325,218.08 USD | `-0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0757` | `0.0758` | `0.0757` | `0.0757` | `5,729,047` | 433,847.20 USD | 252,205.15 USD | `+58.13%` | -32,073,012.93 USD | `+0.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0761` | `0.0766` | `0.0760` | `0.0763` | `225,326,645` | 17,208,343.82 USD | -6,245,910.85 USD | `-36.30%` | -31,077,097.98 USD | `-1.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0763` | `0.0763` | `0.0758` | `0.0761` | `87,917,024` | 6,688,766.39 USD | -346,855.91 USD | `-5.19%` | -31,423,953.90 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0761` | `0.0762` | `0.0756` | `0.0757` | `40,567,717` | 3,075,650.27 USD | -593,867.05 USD | `-19.31%` | -32,017,820.94 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.0753` | `0.0770` | `0.0749` | `0.0761` | `774,393,994` | 58,822,673.99 USD | 562,478.15 USD | `+0.96%` | -31,429,993.58 USD | `+0.43` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0761` | `0.0766` | `0.0754` | `0.0761` | `662,898,037` | 50,470,734.54 USD | 298,494.35 USD | `+0.59%` | -31,131,499.23 USD | `+0.36` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0761` | `0.0762` | `0.0756` | `0.0757` | `40,522,957` | 3,072,261.60 USD | -595,912.23 USD | `-19.40%` | -31,727,411.46 USD | `+0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0757` | `3,369,659,564` | 256,972,093.09 USD | -18,901,985.96 USD | `-7.36%` | -31,727,411.46 USD | `-1.93` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -11,383,503.61 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -14,406,508.13 USD | `+1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0757` | `3,369,659,564` | 256,972,093.09 USD | -18,901,985.96 USD | `-7.36%` | -31,727,411.46 USD | `-1.93` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.0756` | `72926.0000` | 5,516.71 USD | 96,821.63 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `0.0756` | `125911.0000` | 9,524.54 USD | 106,346.16 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0756` | `154228.0000` | 11,666.42 USD | 118,012.59 USD | `1 orders` | `-0.06%` | `-` |
| `ASK` | `0.0757` | `26661.0000` | 2,018.64 USD | 62,841.21 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0757` | `20843.0000` | 1,578.11 USD | 60,822.57 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `19809.0000` | 1,499.80 USD | 59,244.47 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `104332.0000` | 7,899.18 USD | 57,744.67 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `132648.0000` | 10,042.91 USD | 49,845.48 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `34229.0000` | 2,591.48 USD | 39,802.57 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `19812.0000` | 1,499.95 USD | 37,211.09 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `19812.0000` | 1,499.93 USD | 35,711.14 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0757` | `26909.0000` | 2,037.20 USD | 34,211.22 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0757` | `33514.0000` | 2,537.14 USD | 32,174.02 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0757` | `19812.0000` | 1,499.83 USD | 29,636.87 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0757` | `19812.0000` | 1,499.81 USD | 28,137.05 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0757` | `161229.0000` | 12,205.04 USD | 26,637.24 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0757` | `51626.0000` | 3,908.04 USD | 14,432.20 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `0.0757` | `40046.0000` | 3,031.40 USD | 10,524.17 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.0757` | `40046.0000` | 3,031.36 USD | 7,492.76 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.0757` | `33752.0000` | 2,554.89 USD | 4,461.40 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.0757` | `12593.0000` | 953.23 USD | 1,906.51 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0757` | `6297.0000` | 476.65 USD | 953.28 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0757` | `6297.0000` | 476.64 USD | 476.64 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.0757` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0757` | `3000.0000` | 227.05 USD | 227.05 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0757` | `16857.0000` | 1,275.74 USD | 1,502.79 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0757` | `5286.0000` | 400.01 USD | 1,902.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0757` | `9137.0000` | 691.40 USD | 2,594.19 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0757` | `5286.0000` | 399.99 USD | 2,994.18 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `92507.0000` | 6,999.82 USD | 9,994.00 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `5286.0000` | 399.98 USD | 10,393.98 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `418197.0000` | 31,643.29 USD | 42,037.27 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `451438.0000` | 34,158.06 USD | 76,195.33 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `175.0000` | 13.24 USD | 76,208.57 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `30385.0000` | 2,299.02 USD | 78,507.59 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0757` | `2452.0000` | 185.52 USD | 78,693.11 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0757` | `123362.0000` | 9,333.08 USD | 88,026.18 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0757` | `9134.0000` | 691.03 USD | 88,717.22 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0757` | `3000.0000` | 226.96 USD | 88,944.18 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0757` | `26274.0000` | 1,987.71 USD | 90,931.89 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0757` | `4931.0000` | 373.04 USD | 91,304.92 USD | `2 orders` | `-0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `306` | `0xb83d...6e36` | `SHORT` | 7,814,126.33 USD | `102,645,925.00` | `0.0946` | `0.0760` | `1.49` | 1,893,215.32 USD | `+24.23%` | `3X Cross` |
| `311` | `0xc63a...a3cd` | `LONG` | 7,594,000.00 USD | `100,000,000.00` | `0.0856` | `0.0760` | `0.000000` | -970,821.96 USD | `-12.78%` | `10X Cross` |
| `313` | `0x610b...b613` | `LONG` | 7,505,653.54 USD | `98,666,424.00` | `0.0872` | `0.0760` | `0.0608` | -1,094,528.36 USD | `-14.58%` | `5X Cross` |
| `591` | `0x5b5d...c060` | `SHORT` | 3,762,231.30 USD | `49,478,955.00` | `0.0946` | `0.0760` | `3.54` | 919,285.31 USD | `+24.43%` | `3X Cross` |
| `632` | `0xca49...53c8` | `SHORT` | 3,540,592.39 USD | `46,542,649.00` | `0.0929` | `0.0760` | `0.3794` | 785,452.29 USD | `+22.18%` | `10X Cross` |
| `651` | `0x45d2...4029` | `SHORT` | 3,445,016.99 USD | `45,426,000.00` | `0.0954` | `0.0760` | `0.9719` | 890,612.23 USD | `+25.85%` | `10X Cross` |
| `782` | `0xecb6...2b00` | `SHORT` | 2,888,036.98 USD | `37,983,494.00` | `0.0795` | `0.0760` | `0.8139` | 130,084.86 USD | `+4.50%` | `10X Cross` |
| `1195` | `0x458d...ab3b` | `LONG` | 1,860,073.85 USD | `24,454,063.00` | `0.1002` | `0.0760` | `0.0714` | -590,848.05 USD | `-31.76%` | `3X Isolated` |
| `1200` | `0xeadc...9d55` | `LONG` | 1,849,025.19 USD | `24,317,440.00` | `0.0926` | `0.0760` | `0.000000` | -402,569.39 USD | `-21.77%` | `10X Cross` |
| `1289` | `0x9aa5...58af` | `SHORT` | 1,718,946.97 USD | `22,607,312.00` | `0.0907` | `0.0760` | `0.4763` | 330,823.98 USD | `+19.25%` | `10X Cross` |
| `1355` | `0xf48f...10fe` | `LONG` | 1,630,982.68 USD | `21,424,497.00` | `0.0968` | `0.0760` | `0.0494` | -443,321.92 USD | `-27.18%` | `4X Cross` |
| `1382` | `0x9946...0852` | `SHORT` | 1,592,140.57 USD | `20,910,149.00` | `0.0871` | `0.0760` | `0.1479` | 228,414.82 USD | `+14.35%` | `10X Cross` |
| `1575` | `0xcac1...26b3` | `SHORT` | 1,380,213.47 USD | `18,126,835.00` | `0.0943` | `0.0760` | `0.5535` | 329,245.73 USD | `+23.85%` | `10X Cross` |
| `1608` | `0x0d6a...ca57` | `LONG` | 1,341,214.59 USD | `17,626,455.00` | `0.0875` | `0.0760` | `0.0626` | -200,890.37 USD | `-14.98%` | `3X Isolated` |
| `1656` | `0x4808...a82c` | `LONG` | 1,279,527.85 USD | `16,828,143.00` | `0.0883` | `0.0760` | `0.0632` | -206,945.13 USD | `-16.17%` | `3X Cross` |
| `1790` | `0x31ef...f715` | `LONG` | 1,158,462.48 USD | `15,230,102.00` | `0.0936` | `0.0760` | `0.0668` | -267,233.45 USD | `-23.07%` | `3X Isolated` |
| `1811` | `0xbfc7...80b4` | `SHORT` | 1,142,045.70 USD | `15,020,000.00` | `0.0920` | `0.0760` | `0.3198` | 240,353.59 USD | `+21.05%` | `10X Cross` |
| `1935` | `0x7cee...fc93` | `SHORT` | 1,030,803.73 USD | `13,557,142.00` | `0.0868` | `0.0760` | `0.2751` | 146,596.42 USD | `+14.22%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 10,341.99 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.34K USD at 0.0796 USD [API] | `2026-10-28 19:26:41` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 8,959.89 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 8.96K USD at 0.0796 USD [API] | `2026-10-28 19:26:41` |
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 24,345.30 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 24.35K USD at 0.0799 USD [API] | `2026-10-28 19:49:14` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 13,225.13 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 13.23K USD at 0.0800 USD [API] | `2026-10-28 19:56:35` |
| `ANNOUNCEMENT` | `INFO` | `0.0803` | 8,437.53 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 8.44K USD at 0.0803 USD [API] | `2026-10-28 20:10:17` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.00%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--2.04%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.00%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--2.04%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.00%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--2.04%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.00%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--2.04%`)
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
| `1D` | `Long Liquidation` | `0.0673` | 11,500,000.00 USD | 11,500,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,190.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0675` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 5,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0676` | 11,490,000.00 USD | 11,490,000.00 USD | 45,230.00 USD | 24,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 140,600.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 11,420,000.00 USD | 11,420,000.00 USD | 3,200.00 USD | 39,890.00 USD | 56,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 986.19 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 51,050.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 11,150,000.00 USD | 11,150,000.00 USD | 2,550.00 USD | 33,950.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 20,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 11,080,000.00 USD | 11,080,000.00 USD | 24,150.00 USD | 13,610.00 USD | 584.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 11,040,000.00 USD | 11,040,000.00 USD | 41,510.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 455.58 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 11,000,000.00 USD | 11,000,000.00 USD | 41,080.00 USD | 1,410.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 92,360.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 10,950,000.00 USD | 10,950,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 18,800.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 1,170.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 3,670.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 10,880,000.00 USD | 10,880,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,160.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,840.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 10,880,000.00 USD | 10,880,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0696` | 18,020.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 14,650.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 10,880,000.00 USD | 10,880,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,710.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 10,820,000.00 USD | 10,820,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 10,770,000.00 USD | 10,770,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 10,630,000.00 USD | 10,630,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 10,490,000.00 USD | 10,490,000.00 USD | 35,400.00 USD | 18,030.00 USD | 27,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 10,410,000.00 USD | 10,410,000.00 USD | 78,740.00 USD | 36,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 791.79 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 10,290,000.00 USD | 10,290,000.00 USD | 87,540.00 USD | 31,470.00 USD | 40,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 10,130,000.00 USD | 10,130,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 10,040,000.00 USD | 10,040,000.00 USD | 34,530.00 USD | 24,910.00 USD | 35,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 9,950,000.00 USD | 9,950,000.00 USD | 36,930.00 USD | 29,080.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0707` | 9,860,000.00 USD | 9,860,000.00 USD | 54,240.00 USD | 21,680.00 USD | 26,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 9,760,000.00 USD | 9,760,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 9,690,000.00 USD | 9,690,000.00 USD | 36,740.00 USD | 37,120.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0710` | 9,600,000.00 USD | 9,600,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0711` | 9,530,000.00 USD | 9,530,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,790.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 9,450,000.00 USD | 9,450,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 9,390,000.00 USD | 9,390,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 9,230,000.00 USD | 9,230,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 605.68 USD | 771,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 9,140,000.00 USD | 9,140,000.00 USD | 34,440.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 770,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 9,060,000.00 USD | 9,060,000.00 USD | 30,130.00 USD | 31,610.00 USD | 361.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 2,090.00 USD | 762,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 8,990,000.00 USD | 8,990,000.00 USD | 16,400.00 USD | 7,710.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 24,930.00 USD | 760,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 8,950,000.00 USD | 8,950,000.00 USD | 61,550.00 USD | 31,390.00 USD | 36,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 960.13 USD | 735,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 8,820,000.00 USD | 8,820,000.00 USD | 14,000.00 USD | 0.00 USD | 138.82 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 6,600.00 USD | 734,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 8,800,000.00 USD | 8,800,000.00 USD | 31,160.00 USD | 29,440.00 USD | 37,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,470.00 USD | 728,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 8,710,000.00 USD | 8,710,000.00 USD | 136,510.00 USD | 76,220.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 715,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,480,000.00 USD | 8,480,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 10,420.00 USD | 693,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,400,000.00 USD | 8,400,000.00 USD | 54,790.00 USD | 162,040.00 USD | 149,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 163.73 USD | 682,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 8,030,000.00 USD | 8,030,000.00 USD | 27,830.00 USD | 87,980.00 USD | 92,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 996.33 USD | 682,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 7,820,000.00 USD | 7,820,000.00 USD | 54,140.00 USD | 22,980.00 USD | 23,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 681,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 7,720,000.00 USD | 7,720,000.00 USD | 40,350.00 USD | 0.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 18,770.00 USD | 681,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 7,680,000.00 USD | 7,680,000.00 USD | 168,660.00 USD | 0.00 USD | 333,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 50,920.00 USD | 662,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 7,180,000.00 USD | 7,180,000.00 USD | 66,510.00 USD | 85,670.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 611,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 6,950,000.00 USD | 6,950,000.00 USD | 19,510.00 USD | 66,850.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 611,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 6,830,000.00 USD | 6,830,000.00 USD | 112,200.00 USD | 50,880.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,040.00 USD | 538,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 6,670,000.00 USD | 6,670,000.00 USD | 152,870.00 USD | 17,510.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 528,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 6,480,000.00 USD | 6,480,000.00 USD | 154,930.00 USD | 60,240.00 USD | 65,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 29,280.00 USD | 526,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,200,000.00 USD | 6,200,000.00 USD | 15,550.00 USD | 0.00 USD | 70,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 6,110,000.00 USD | 6,110,000.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 3,930.00 USD | 496,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 6,070,000.00 USD | 6,070,000.00 USD | 33,390.00 USD | 31,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,690.00 USD | 492,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 6,000,000.00 USD | 6,000,000.00 USD | 234,720.00 USD | 123,630.00 USD | 41.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 488,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,650,000.00 USD | 5,650,000.00 USD | 51,890.00 USD | 42,510.00 USD | 127.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,740.00 USD | 482,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,550,000.00 USD | 5,550,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 314.08 USD | 472,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,040,000.00 USD | 5,040,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,640.00 USD | 471,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,760,000.00 USD | 4,760,000.00 USD | 33,740.00 USD | 0.00 USD | 328.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,080.00 USD | 458,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,730,000.00 USD | 4,730,000.00 USD | 36,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 1,280.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,690,000.00 USD | 4,690,000.00 USD | 286,340.00 USD | 0.00 USD | 666,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,740,000.00 USD | 3,740,000.00 USD | 118,640.00 USD | 234,470.00 USD | 190,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 249.15 USD | 425.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,190,000.00 USD | 3,190,000.00 USD | 19,880.00 USD | 156,580.00 USD | 59,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 176.30 USD | 176.30 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,960,000.00 USD | 2,960,000.00 USD | 199,850.00 USD | 158,980.00 USD | 24,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,570,000.00 USD | 2,570,000.00 USD | 371,240.00 USD | 210,430.00 USD | 160,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,830,000.00 USD | 1,830,000.00 USD | 466,980.00 USD | 159,330.00 USD | 99,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,110,000.00 USD | 1,110,000.00 USD | 130,290.00 USD | 143,100.00 USD | 194,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 639,090.00 USD | 639,090.00 USD | 203,330.00 USD | 0.00 USD | 148,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 287,320.00 USD | 287,320.00 USD | 69,890.00 USD | 0.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 95,970.00 USD | 95,970.00 USD | 0.00 USD | 6,860.00 USD | 150.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 88,960.00 USD | 88,960.00 USD | 0.00 USD | 0.00 USD | 458.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 88,500.00 USD | 88,500.00 USD | 0.00 USD | 85,010.00 USD | 152.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0754` | 3,340.00 USD | 3,340.00 USD | 0.00 USD | 0.00 USD | 167.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0755` | 3,170.00 USD | 3,170.00 USD | 0.00 USD | 0.00 USD | 144.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 3,030.00 USD | 3,030.00 USD | 0.00 USD | 0.00 USD | 911.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0757` | 2,110.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 275.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0759` | 1,840.00 USD | 1,840.00 USD | 0.00 USD | 0.00 USD | 667.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0760` | 1,170.00 USD | 1,170.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 300.51 USD | 300.51 USD | 0.00 USD | 0.00 USD | 300.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 601.02 USD | 601.02 USD | 0.00 USD | 0.00 USD | 300.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 856.36 USD | 856.36 USD | 0.00 USD | 0.00 USD | 255.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 14,080.00 USD | 14,080.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 341,310.00 USD | 341,310.00 USD | 0.00 USD | 325,960.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 599,360.00 USD | 599,360.00 USD | 0.00 USD | 257,590.00 USD | 457.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,730,000.00 USD | 1,730,000.00 USD | 765,870.00 USD | 360,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 2,110,000.00 USD | 2,110,000.00 USD | 190,810.00 USD | 192,160.00 USD | 502.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,980,000.00 USD | 2,980,000.00 USD | 351,760.00 USD | 0.00 USD | 514,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 3,650,000.00 USD | 3,650,000.00 USD | 181,440.00 USD | 341,350.00 USD | 148,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 4,270,000.00 USD | 4,270,000.00 USD | 272,760.00 USD | 93,300.00 USD | 254,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 4,930,000.00 USD | 4,930,000.00 USD | 216,410.00 USD | 232,340.00 USD | 212,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 5,880,000.00 USD | 5,880,000.00 USD | 286,340.00 USD | 0.00 USD | 666,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 6,260,000.00 USD | 6,260,000.00 USD | 65,160.00 USD | 169,730.00 USD | 149,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 133,700.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 6,680,000.00 USD | 6,680,000.00 USD | 155,740.00 USD | 101,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0776` | 6,950,000.00 USD | 6,950,000.00 USD | 190,100.00 USD | 47,010.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 7,470,000.00 USD | 7,470,000.00 USD | 205,390.00 USD | 264,690.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 7,980,000.00 USD | 7,980,000.00 USD | 16,790.00 USD | 202,930.00 USD | 296,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 85,950.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 8,310,000.00 USD | 8,310,000.00 USD | 69,890.00 USD | 31,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 8,490,000.00 USD | 8,490,000.00 USD | 113,060.00 USD | 68,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 8,500,000.00 USD | 8,500,000.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 8,830,000.00 USD | 8,830,000.00 USD | 8,010.00 USD | 184,740.00 USD | 142,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 9,220,000.00 USD | 9,220,000.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 9,570,000.00 USD | 9,570,000.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 10,110,000.00 USD | 10,110,000.00 USD | 179,570.00 USD | 117,040.00 USD | 237,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 11,050,000.00 USD | 11,050,000.00 USD | 298,820.00 USD | 307,550.00 USD | 333,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0788` | 11,380,000.00 USD | 11,380,000.00 USD | 75,490.00 USD | 181,170.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 11,890,000.00 USD | 11,890,000.00 USD | 234,900.00 USD | 176,740.00 USD | 91,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 12,040,000.00 USD | 12,040,000.00 USD | 102,120.00 USD | 54,140.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 12,330,000.00 USD | 12,330,000.00 USD | 152,950.00 USD | 63,280.00 USD | 66,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 12,470,000.00 USD | 12,470,000.00 USD | 104,950.00 USD | 18,870.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 12,640,000.00 USD | 12,640,000.00 USD | 83,300.00 USD | 41,370.00 USD | 52,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 12,730,000.00 USD | 12,730,000.00 USD | 10,150.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 12,920,000.00 USD | 12,920,000.00 USD | 174,010.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 13,440,000.00 USD | 13,440,000.00 USD | 191,110.00 USD | 89,760.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 13,660,000.00 USD | 13,660,000.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 14,240,000.00 USD | 14,240,000.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 14,340,000.00 USD | 14,340,000.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 14,350,000.00 USD | 14,350,000.00 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 14,360,000.00 USD | 14,360,000.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0803` | 558.06 USD | 558.06 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0803` | 14,410,000.00 USD | 14,410,000.00 USD | 9,970.00 USD | 0.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 14,430,000.00 USD | 14,430,000.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 14,570,000.00 USD | 14,570,000.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 14,830,000.00 USD | 14,830,000.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 15,300,000.00 USD | 15,300,000.00 USD | 214,730.00 USD | 208,070.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 16,370,000.00 USD | 16,370,000.00 USD | 419,500.00 USD | 131,030.00 USD | 522,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0809` | 4,530.00 USD | 5,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0809` | 17,200,000.00 USD | 17,200,000.00 USD | 477,790.00 USD | 336,610.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 17,810,000.00 USD | 17,810,000.00 USD | 293,220.00 USD | 180,540.00 USD | 132,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 18,130,000.00 USD | 18,130,000.00 USD | 83,280.00 USD | 241,410.00 USD | 875.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 18,510,000.00 USD | 18,510,000.00 USD | 144,600.00 USD | 99,490.00 USD | 135,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 18,790,000.00 USD | 18,790,000.00 USD | 49,290.00 USD | 23,210.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 19,200,000.00 USD | 19,200,000.00 USD | 29,840.00 USD | 79,960.00 USD | 292,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 19,590,000.00 USD | 19,590,000.00 USD | 191,850.00 USD | 80,500.00 USD | 122,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 20,310,000.00 USD | 20,310,000.00 USD | 348,980.00 USD | 194,790.00 USD | 177,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0817` | 428.01 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0817` | 20,870,000.00 USD | 20,870,000.00 USD | 301,230.00 USD | 127,050.00 USD | 130,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 241.90 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 21,610,000.00 USD | 21,610,000.00 USD | 269,340.00 USD | 161,260.00 USD | 308,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 22,230,000.00 USD | 22,230,000.00 USD | 174,640.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 22,910,000.00 USD | 22,910,000.00 USD | 136,010.00 USD | 202,840.00 USD | 344,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 23,370,000.00 USD | 23,370,000.00 USD | 210,590.00 USD | 79,630.00 USD | 170,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 23,960,000.00 USD | 23,960,000.00 USD | 262,170.00 USD | 169,200.00 USD | 155,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 24,310,000.00 USD | 24,310,000.00 USD | 270,850.00 USD | 75,420.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 265.58 USD | 6,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0824` | 24,890,000.00 USD | 24,890,000.00 USD | 151,910.00 USD | 226,510.00 USD | 199,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 25,170,000.00 USD | 25,170,000.00 USD | 127,790.00 USD | 122,020.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 25,590,000.00 USD | 25,590,000.00 USD | 150,570.00 USD | 84,820.00 USD | 190,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 25,690,000.00 USD | 25,690,000.00 USD | 52,670.00 USD | 48,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 26,060,000.00 USD | 26,060,000.00 USD | 225,780.00 USD | 75,940.00 USD | 65,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 26,440,000.00 USD | 26,440,000.00 USD | 197,520.00 USD | 111,290.00 USD | 72,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 26,790,000.00 USD | 26,790,000.00 USD | 161,710.00 USD | 84,690.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 26,870,000.00 USD | 26,870,000.00 USD | 60,680.00 USD | 3,890.00 USD | 24,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 9,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 27,190,000.00 USD | 27,190,000.00 USD | 166,490.00 USD | 66,230.00 USD | 81,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 27,530,000.00 USD | 27,530,000.00 USD | 119,590.00 USD | 55,260.00 USD | 164,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 5,700.00 USD | 15,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0834` | 27,880,000.00 USD | 27,880,000.00 USD | 127,020.00 USD | 94,190.00 USD | 127,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 28,230,000.00 USD | 28,230,000.00 USD | 107,580.00 USD | 176,580.00 USD | 64,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 28,480,000.00 USD | 28,480,000.00 USD | 48,890.00 USD | 61,760.00 USD | 145,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 15,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 28,670,000.00 USD | 28,670,000.00 USD | 131,180.00 USD | 17,710.00 USD | 40,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 17,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 28,950,000.00 USD | 28,950,000.00 USD | 170,560.00 USD | 70,030.00 USD | 32,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 7,970.00 USD | 25,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0839` | 29,030,000.00 USD | 29,030,000.00 USD | 52,570.00 USD | 16,550.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 29,090,000.00 USD | 29,090,000.00 USD | 13,720.00 USD | 15,480.00 USD | 28,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 29,110,000.00 USD | 29,110,000.00 USD | 23,380.00 USD | 2,010.00 USD | 284.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 29,180,000.00 USD | 29,180,000.00 USD | 22,710.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0843` | 29,220,000.00 USD | 29,220,000.00 USD | 33,600.00 USD | 0.00 USD | 1.38 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 29,300,000.00 USD | 29,300,000.00 USD | 79,050.00 USD | 0.00 USD | 371.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 29,320,000.00 USD | 29,320,000.00 USD | 18,230.00 USD | 0.00 USD | 542.17 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 29,400,000.00 USD | 29,400,000.00 USD | 72,340.00 USD | 16,670.00 USD | 9.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0847` | 29,420,000.00 USD | 29,420,000.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 723.94 USD | 25,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0157` | 16,780,000.00 USD | 0.00 USD | 1,500.00 USD | `-79.43%` | `95,954.00` |
| `Live` | `Long` | `0.0160` | 16,770,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.91%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,770,000.00 USD | 0.00 USD | 407.02 USD | `-78.38%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,770,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.25%` | `319,394.00` |
| `Live` | `Long` | `0.0176` | 16,760,000.00 USD | 0.00 USD | 4,410.00 USD | `-76.80%` | `250,000.00` |
| `Live` | `Long` | `0.0181` | 16,760,000.00 USD | 0.00 USD | 1,070.00 USD | `-76.28%` | `59,317.00` |
| `Live` | `Long` | `0.0191` | 16,760,000.00 USD | 0.00 USD | 5,340.00 USD | `-74.96%` | `280,072.00` |
| `Live` | `Long` | `0.0202` | 16,750,000.00 USD | 0.00 USD | 121.93 USD | `-73.52%` | `6,051.00` |
| `Live` | `Long` | `0.0204` | 16,750,000.00 USD | 0.00 USD | 20,180.00 USD | `-73.26%` | `991,662.00` |
| `Live` | `Long` | `0.0208` | 16,730,000.00 USD | 0.00 USD | 30,890.00 USD | `-72.73%` | `1,488,849.00` |
| `Live` | `Long` | `0.0216` | 16,700,000.00 USD | 0.00 USD | 692.80 USD | `-71.55%` | `32,000.00` |
| `Live` | `Long` | `0.0221` | 16,700,000.00 USD | 0.00 USD | 119.78 USD | `-71.02%` | `5,432.00` |
| `Live` | `Long` | `0.0226` | 16,700,000.00 USD | 0.00 USD | 884.46 USD | `-70.23%` | `39,049.00` |
| `Live` | `Long` | `0.0227` | 16,700,000.00 USD | 0.00 USD | 141.19 USD | `-70.10%` | `6,206.00` |
| `Live` | `Long` | `0.0232` | 16,700,000.00 USD | 0.00 USD | 367.23 USD | `-69.44%` | `15,795.00` |
| `Live` | `Long` | `0.0244` | 16,700,000.00 USD | 0.00 USD | 369.37 USD | `-68.00%` | `15,169.00` |
| `Live` | `Long` | `0.0244` | 16,700,000.00 USD | 0.00 USD | 1,830.00 USD | `-67.87%` | `75,012.00` |
| `Live` | `Long` | `0.0248` | 16,700,000.00 USD | 0.00 USD | 296.23 USD | `-67.47%` | `11,969.00` |
| `Live` | `Long` | `0.0249` | 16,700,000.00 USD | 0.00 USD | 22,210.00 USD | `-67.34%` | `893,720.00` |
| `Live` | `Long` | `0.0266` | 16,680,000.00 USD | 0.00 USD | 531.00 USD | `-65.11%` | `20,000.00` |
| `Live` | `Long` | `0.0267` | 16,670,000.00 USD | 0.00 USD | 535.00 USD | `-64.84%` | `20,000.00` |
| `Live` | `Long` | `0.0277` | 16,670,000.00 USD | 0.00 USD | 477.32 USD | `-63.66%` | `17,263.00` |
| `Live` | `Long` | `0.0279` | 16,670,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.27%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 16,670,000.00 USD | 0.00 USD | 14,180.00 USD | `-62.74%` | `500,000.00` |
| `Live` | `Long` | `0.0284` | 16,660,000.00 USD | 0.00 USD | 13,970.00 USD | `-62.61%` | `491,018.00` |
| `Live` | `Long` | `0.0288` | 16,640,000.00 USD | 0.00 USD | 928.57 USD | `-62.22%` | `32,298.00` |
| `Live` | `Long` | `0.0300` | 16,640,000.00 USD | 0.00 USD | 4,590.00 USD | `-60.64%` | `153,201.00` |
| `Live` | `Long` | `0.0303` | 16,640,000.00 USD | 0.00 USD | 3,310.00 USD | `-60.11%` | `109,191.00` |
| `Live` | `Long` | `0.0306` | 16,640,000.00 USD | 0.00 USD | 137.41 USD | `-59.85%` | `4,498.00` |
| `Live` | `Long` | `0.0323` | 16,630,000.00 USD | 0.00 USD | 152.05 USD | `-57.48%` | `4,700.00` |
| `Live` | `Long` | `0.0328` | 16,630,000.00 USD | 0.00 USD | 6,180.00 USD | `-56.83%` | `187,979.00` |
| `Live` | `Long` | `0.0331` | 16,630,000.00 USD | 0.00 USD | 2,600.00 USD | `-56.43%` | `78,319.00` |
| `Live` | `Long` | `0.0340` | 16,630,000.00 USD | 0.00 USD | 477.96 USD | `-55.25%` | `14,037.00` |
| `Live` | `Long` | `0.0347` | 16,630,000.00 USD | 0.00 USD | 185.17 USD | `-54.46%` | `5,344.00` |
| `Live` | `Long` | `0.0355` | 16,630,000.00 USD | 0.00 USD | 4,770.00 USD | `-53.41%` | `134,443.00` |
| `Live` | `Long` | `0.0358` | 16,620,000.00 USD | 0.00 USD | 214.53 USD | `-52.88%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,620,000.00 USD | 0.00 USD | 452.18 USD | `-52.62%` | `12,543.00` |
| `Live` | `Long` | `0.0372` | 16,620,000.00 USD | 0.00 USD | 35,290.00 USD | `-51.18%` | `950,000.00` |
| `Live` | `Long` | `0.0377` | 16,580,000.00 USD | 0.00 USD | 2,850.00 USD | `-50.52%` | `75,693.00` |
| `Live` | `Long` | `0.0381` | 16,580,000.00 USD | 0.00 USD | 246.45 USD | `-49.99%` | `6,477.00` |
| `Live` | `Long` | `0.0384` | 16,580,000.00 USD | 0.00 USD | 173.60 USD | `-49.47%` | `4,515.00` |
| `Live` | `Long` | `0.0386` | 16,580,000.00 USD | 0.00 USD | 121.74 USD | `-49.34%` | `3,158.00` |
| `Live` | `Long` | `0.0389` | 16,580,000.00 USD | 0.00 USD | 207.81 USD | `-48.94%` | `5,349.00` |
| `Live` | `Long` | `0.0393` | 16,580,000.00 USD | 0.00 USD | 5,020.00 USD | `-48.42%` | `127,939.00` |
| `Live` | `Long` | `0.0404` | 16,580,000.00 USD | 0.00 USD | 115.12 USD | `-46.84%` | `2,846.00` |
| `Live` | `Long` | `0.0406` | 16,580,000.00 USD | 0.00 USD | 432.03 USD | `-46.58%` | `10,628.00` |
| `Live` | `Long` | `0.0408` | 16,580,000.00 USD | 0.00 USD | 419.28 USD | `-46.44%` | `10,289.00` |
| `Live` | `Long` | `0.0413` | 16,580,000.00 USD | 0.00 USD | 141.24 USD | `-45.79%` | `3,424.00` |
| `Live` | `Long` | `0.0413` | 16,570,000.00 USD | 0.00 USD | 58,120.00 USD | `-45.66%` | `1,405,488.00` |
| `Live` | `Long` | `0.0415` | 16,520,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.39%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 16,520,000.00 USD | 0.00 USD | 266.05 USD | `-44.87%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,520,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.47%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,510,000.00 USD | 0.00 USD | 267.52 USD | `-44.34%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,510,000.00 USD | 0.00 USD | 455.06 USD | `-44.21%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,510,000.00 USD | 0.00 USD | 5,750.00 USD | `-44.08%` | `135,019.00` |
| `Live` | `Long` | `0.0427` | 16,510,000.00 USD | 0.00 USD | 3,620.00 USD | `-43.95%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 16,500,000.00 USD | 0.00 USD | 859.00 USD | `-43.55%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,500,000.00 USD | 0.00 USD | 10,760.00 USD | `-43.16%` | `248,704.00` |
| `Live` | `Long` | `0.0433` | 16,490,000.00 USD | 0.00 USD | 2,450.00 USD | `-43.03%` | `56,456.00` |
| `Live` | `Long` | `0.0435` | 16,490,000.00 USD | 0.00 USD | 25,000.00 USD | `-42.77%` | `574,152.00` |
| `Live` | `Long` | `0.0439` | 16,460,000.00 USD | 0.00 USD | 1,610.00 USD | `-42.37%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,460,000.00 USD | 0.00 USD | 114,760.00 USD | `-42.24%` | `2,611,227.00` |
| `Live` | `Long` | `0.0440` | 16,350,000.00 USD | 0.00 USD | 1,060.00 USD | `-42.11%` | `24,073.00` |
| `Live` | `Long` | `0.0442` | 16,350,000.00 USD | 0.00 USD | 2,210.00 USD | `-41.85%` | `50,000.00` |
| `Live` | `Long` | `0.0444` | 16,350,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.71%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,240,000.00 USD | 0.00 USD | 444.76 USD | `-41.32%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,240,000.00 USD | 0.00 USD | 248.63 USD | `-41.19%` | `5,556.00` |
| `Live` | `Long` | `0.0454` | 16,240,000.00 USD | 0.00 USD | 3,180.00 USD | `-40.27%` | `69,976.00` |
| `Live` | `Long` | `0.0456` | 16,240,000.00 USD | 0.00 USD | 32,650.00 USD | `-40.14%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 16,210,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.87%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 16,200,000.00 USD | 0.00 USD | 4,500.00 USD | `-39.48%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 16,200,000.00 USD | 0.00 USD | 909.25 USD | `-39.35%` | `19,702.00` |
| `Live` | `Long` | `0.0464` | 16,200,000.00 USD | 0.00 USD | 810.75 USD | `-39.09%` | `17,492.00` |
| `Live` | `Long` | `0.0464` | 16,200,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.95%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 16,180,000.00 USD | 0.00 USD | 1,380.00 USD | `-38.82%` | `29,561.00` |
| `Live` | `Long` | `0.0466` | 16,180,000.00 USD | 0.00 USD | 48,190.00 USD | `-38.69%` | `1,032,914.00` |
| `Live` | `Long` | `0.0473` | 16,130,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.90%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 16,130,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.77%` | `29,884.00` |
| `Live` | `Long` | `0.0474` | 16,130,000.00 USD | 0.00 USD | 593.13 USD | `-37.64%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 16,130,000.00 USD | 0.00 USD | 105.02 USD | `-37.38%` | `2,204.00` |
| `Live` | `Long` | `0.0479` | 16,130,000.00 USD | 0.00 USD | 3,270.00 USD | `-36.98%` | `68,212.00` |
| `Live` | `Long` | `0.0481` | 16,120,000.00 USD | 0.00 USD | 59,790.00 USD | `-36.72%` | `1,241,696.00` |
| `Live` | `Long` | `0.0483` | 16,060,000.00 USD | 0.00 USD | 1,240.00 USD | `-36.59%` | `25,729.00` |
| `Live` | `Long` | `0.0483` | 16,060,000.00 USD | 0.00 USD | 2,280.00 USD | `-36.46%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 16,060,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.33%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 16,060,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.80%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 16,060,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.67%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 16,050,000.00 USD | 0.00 USD | 25,600.00 USD | `-35.54%` | `521,989.00` |
| `Live` | `Long` | `0.0493` | 16,020,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-35.14%` | `21,424,497.00` |
| `Live` | `Long` | `0.0495` | 14,970,000.00 USD | 0.00 USD | 18,690.00 USD | `-34.88%` | `377,099.00` |
| `Live` | `Long` | `0.0496` | 14,950,000.00 USD | 0.00 USD | 4,260.00 USD | `-34.75%` | `85,771.00` |
| `Live` | `Long` | `0.0498` | 14,940,000.00 USD | 0.00 USD | 253.82 USD | `-34.62%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,940,000.00 USD | 0.00 USD | 661.09 USD | `-34.35%` | `13,235.00` |
| `Live` | `Long` | `0.0500` | 14,940,000.00 USD | 0.00 USD | 501.50 USD | `-34.22%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,940,000.00 USD | 0.00 USD | 5,410.00 USD | `-33.96%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,940,000.00 USD | 0.00 USD | 2,520.00 USD | `-33.83%` | `50,080.00` |
| `Live` | `Long` | `0.0505` | 14,940,000.00 USD | 0.00 USD | 334.89 USD | `-33.70%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,930,000.00 USD | 0.00 USD | 3,880.00 USD | `-33.43%` | `76,653.00` |
| `Live` | `Long` | `0.0508` | 14,930,000.00 USD | 0.00 USD | 5,350.00 USD | `-33.30%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,930,000.00 USD | 0.00 USD | 535.43 USD | `-33.04%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,930,000.00 USD | 0.00 USD | 566.65 USD | `-32.91%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,920,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.78%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,910,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.65%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,910,000.00 USD | 0.00 USD | 1,580.00 USD | `-32.51%` | `30,707.00` |
| `Live` | `Long` | `0.0515` | 14,910,000.00 USD | 0.00 USD | 309.15 USD | `-32.25%` | `5,997.00` |
| `Live` | `Long` | `0.0520` | 14,910,000.00 USD | 0.00 USD | 277.72 USD | `-31.73%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,910,000.00 USD | 0.00 USD | 3,990.00 USD | `-31.59%` | `76,663.00` |
| `Live` | `Long` | `0.0522` | 14,910,000.00 USD | 0.00 USD | 317.96 USD | `-31.46%` | `6,097.00` |
| `Live` | `Long` | `0.0522` | 14,910,000.00 USD | 0.00 USD | 315,250.00 USD | `-31.33%` | `6,033,568.00` |
| `Live` | `Long` | `0.0524` | 14,590,000.00 USD | 0.00 USD | 401.84 USD | `-31.20%` | `7,676.00` |
| `Live` | `Long` | `0.0524` | 14,590,000.00 USD | 0.00 USD | 1,300.00 USD | `-31.07%` | `24,777.00` |
| `Live` | `Long` | `0.0525` | 14,590,000.00 USD | 0.00 USD | 5,640.00 USD | `-30.94%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,580,000.00 USD | 0.00 USD | 395.09 USD | `-30.81%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,580,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.67%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,580,000.00 USD | 0.00 USD | 673.52 USD | `-30.54%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,580,000.00 USD | 0.00 USD | 183,340.00 USD | `-30.41%` | `3,462,426.00` |
| `Live` | `Long` | `0.0532` | 14,400,000.00 USD | 0.00 USD | 9,240.00 USD | `-30.15%` | `173,844.00` |
| `Live` | `Long` | `0.0532` | 14,390,000.00 USD | 0.00 USD | 100.96 USD | `-30.02%` | `1,896.00` |
| `Live` | `Long` | `0.0534` | 14,390,000.00 USD | 0.00 USD | 2,670.00 USD | `-29.89%` | `50,000.00` |
| `Live` | `Long` | `0.0534` | 14,380,000.00 USD | 0.00 USD | 314,750.00 USD | `-29.75%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 14,070,000.00 USD | 0.00 USD | 942.48 USD | `-29.62%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 14,070,000.00 USD | 0.00 USD | 1,590.00 USD | `-29.49%` | `29,631.00` |
| `Live` | `Long` | `0.0539` | 14,070,000.00 USD | 0.00 USD | 258.10 USD | `-29.23%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 14,070,000.00 USD | 0.00 USD | 5,290.00 USD | `-29.10%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 14,060,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.97%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 14,060,000.00 USD | 0.00 USD | 13,510.00 USD | `-28.83%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 14,050,000.00 USD | 0.00 USD | 138,260.00 USD | `-28.70%` | `2,548,649.00` |
| `Live` | `Long` | `0.0544` | 13,910,000.00 USD | 0.00 USD | 112,760.00 USD | `-28.44%` | `2,070,976.00` |
| `Live` | `Long` | `0.0546` | 13,790,000.00 USD | 0.00 USD | 12,250.00 USD | `-28.31%` | `224,650.00` |
| `Live` | `Long` | `0.0546` | 13,780,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.18%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,780,000.00 USD | 0.00 USD | 892.81 USD | `-28.05%` | `16,307.00` |
| `Live` | `Long` | `0.0549` | 13,780,000.00 USD | 0.00 USD | 15,810.00 USD | `-27.78%` | `287,745.00` |
| `Live` | `Long` | `0.0556` | 13,760,000.00 USD | 0.00 USD | 1,080.00 USD | `-26.99%` | `19,492.00` |
| `Live` | `Long` | `0.0559` | 13,760,000.00 USD | 0.00 USD | 1,440.00 USD | `-26.47%` | `25,791.00` |
| `Live` | `Long` | `0.0561` | 13,760,000.00 USD | 0.00 USD | 144.08 USD | `-26.21%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,760,000.00 USD | 0.00 USD | 97,190.00 USD | `-26.07%` | `1,727,812.00` |
| `Live` | `Long` | `0.0563` | 13,660,000.00 USD | 0.00 USD | 351.85 USD | `-25.94%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,660,000.00 USD | 0.00 USD | 131.48 USD | `-25.68%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,660,000.00 USD | 0.00 USD | 568.50 USD | `-25.29%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,660,000.00 USD | 0.00 USD | 315.67 USD | `-25.15%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,660,000.00 USD | 0.00 USD | 8,350.00 USD | `-25.02%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,650,000.00 USD | 0.00 USD | 644.99 USD | `-24.89%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,650,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.63%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,650,000.00 USD | 0.00 USD | 3,590.00 USD | `-24.37%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,640,000.00 USD | 0.00 USD | 10,600.00 USD | `-24.23%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,630,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.10%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,620,000.00 USD | 0.00 USD | 3,940.00 USD | `-23.97%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,620,000.00 USD | 0.00 USD | 431.14 USD | `-23.71%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,620,000.00 USD | 0.00 USD | 810.49 USD | `-23.58%` | `13,938.00` |
| `Live` | `Long` | `0.0583` | 13,620,000.00 USD | 0.00 USD | 116.82 USD | `-23.31%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 13,610,000.00 USD | 0.00 USD | 172.78 USD | `-23.05%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,610,000.00 USD | 0.00 USD | 371.02 USD | `-22.92%` | `6,326.00` |
| `Live` | `Long` | `0.0587` | 13,610,000.00 USD | 0.00 USD | 9,120.00 USD | `-22.79%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 13,610,000.00 USD | 0.00 USD | 212.22 USD | `-22.53%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,610,000.00 USD | 0.00 USD | 26,980.00 USD | `-22.26%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,580,000.00 USD | 0.00 USD | 546.26 USD | `-22.00%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,580,000.00 USD | 0.00 USD | 3,660.00 USD | `-21.87%` | `61,626.00` |
| `Live` | `Long` | `0.0595` | 13,570,000.00 USD | 0.00 USD | 3,520.00 USD | `-21.74%` | `59,115.00` |
| `Live` | `Long` | `0.0599` | 13,570,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.34%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 13,570,000.00 USD | 0.00 USD | 2,830.00 USD | `-21.21%` | `47,268.00` |
| `Live` | `Long` | `0.0600` | 13,570,000.00 USD | 0.00 USD | 8,050.00 USD | `-21.08%` | `134,117.00` |
| `Live` | `Long` | `0.0602` | 13,560,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.95%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 13,550,000.00 USD | 0.00 USD | 772.60 USD | `-20.69%` | `12,802.00` |
| `Live` | `Long` | `0.0604` | 13,550,000.00 USD | 0.00 USD | 2,390.00 USD | `-20.55%` | `39,476.00` |
| `Live` | `Long` | `0.0605` | 13,550,000.00 USD | 0.00 USD | 35,950.00 USD | `-20.42%` | `593,779.00` |
| `Live` | `Long` | `0.0607` | 13,510,000.00 USD | 0.00 USD | 6,000,000.00 USD | `-20.16%` | `98,686,504.00` |
| `Live` | `Long` | `0.0609` | 7,510,000.00 USD | 0.00 USD | 717.73 USD | `-20.03%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,510,000.00 USD | 0.00 USD | 2,220.00 USD | `-19.90%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,510,000.00 USD | 0.00 USD | 629.72 USD | `-19.63%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,510,000.00 USD | 0.00 USD | 298.17 USD | `-19.50%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,510,000.00 USD | 0.00 USD | 655.16 USD | `-19.37%` | `10,679.00` |
| `Live` | `Long` | `0.0614` | 7,510,000.00 USD | 0.00 USD | 662.55 USD | `-19.24%` | `10,782.00` |
| `Live` | `Long` | `0.0616` | 7,510,000.00 USD | 0.00 USD | 1,400.00 USD | `-19.11%` | `22,725.00` |
| `Live` | `Long` | `0.0617` | 7,510,000.00 USD | 0.00 USD | 13,460.00 USD | `-18.98%` | `218,374.00` |
| `Live` | `Long` | `0.0617` | 7,490,000.00 USD | 0.00 USD | 158.08 USD | `-18.85%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,490,000.00 USD | 0.00 USD | 26,790.00 USD | `-18.45%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 2,150.00 USD | `-18.32%` | `34,643.00` |
| `Live` | `Long` | `0.0624` | 7,470,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.06%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,460,000.00 USD | 0.00 USD | 3,470.00 USD | `-17.93%` | `55,505.00` |
| `Live` | `Long` | `0.0625` | 7,460,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.79%` | `17,635,152.00` |
| `Live` | `Long` | `0.0626` | 6,360,000.00 USD | 0.00 USD | 40,580.00 USD | `-17.66%` | `647,669.00` |
| `Live` | `Long` | `0.0628` | 6,320,000.00 USD | 0.00 USD | 1,250.00 USD | `-17.53%` | `19,993.00` |
| `Live` | `Long` | `0.0629` | 6,320,000.00 USD | 0.00 USD | 10,930.00 USD | `-17.40%` | `173,976.00` |
| `Live` | `Long` | `0.0630` | 6,300,000.00 USD | 0.00 USD | 3,280.00 USD | `-17.14%` | `51,996.00` |
| `Live` | `Long` | `0.0631` | 6,300,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-17.01%` | `17,004,273.00` |
| `Live` | `Long` | `0.0633` | 5,230,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.87%` | `19,161.00` |
| `Live` | `Long` | `0.0634` | 5,230,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.74%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.61%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 280.95 USD | `-16.48%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,210,000.00 USD | 0.00 USD | 633.38 USD | `-16.35%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,210,000.00 USD | 0.00 USD | 6,230.00 USD | `-16.22%` | `97,791.00` |
| `Live` | `Long` | `0.0639` | 5,200,000.00 USD | 0.00 USD | 23,220.00 USD | `-16.09%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,180,000.00 USD | 0.00 USD | 1,360.00 USD | `-15.95%` | `21,194.00` |
| `Live` | `Long` | `0.0641` | 5,180,000.00 USD | 0.00 USD | 633.29 USD | `-15.69%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,180,000.00 USD | 0.00 USD | 9,150.00 USD | `-15.56%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,170,000.00 USD | 0.00 USD | 2,860.00 USD | `-15.43%` | `44,505.00` |
| `Live` | `Long` | `0.0644` | 5,170,000.00 USD | 0.00 USD | 24,070.00 USD | `-15.30%` | `373,512.00` |
| `Live` | `Long` | `0.0645` | 5,140,000.00 USD | 0.00 USD | 740.39 USD | `-15.17%` | `11,470.00` |
| `Live` | `Long` | `0.0646` | 5,140,000.00 USD | 0.00 USD | 3,520.00 USD | `-15.03%` | `54,442.00` |
| `Live` | `Long` | `0.0648` | 5,140,000.00 USD | 0.00 USD | 86,870.00 USD | `-14.90%` | `1,341,590.00` |
| `Live` | `Long` | `0.0649` | 5,050,000.00 USD | 0.00 USD | 9,290.00 USD | `-14.77%` | `143,265.00` |
| `Live` | `Long` | `0.0649` | 5,040,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.64%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 5,020,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.38%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 5,020,000.00 USD | 0.00 USD | 62,700.00 USD | `-14.25%` | `960,965.00` |
| `Live` | `Long` | `0.0654` | 4,960,000.00 USD | 0.00 USD | 6,530.00 USD | `-14.11%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,950,000.00 USD | 0.00 USD | 5,340.00 USD | `-13.85%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 4,940,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.59%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,880,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.46%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,860,000.00 USD | 0.00 USD | 9,600.00 USD | `-13.33%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,850,000.00 USD | 0.00 USD | 339.48 USD | `-13.06%` | `5,132.00` |
| `Live` | `Long` | `0.0663` | 4,850,000.00 USD | 0.00 USD | 1,900.00 USD | `-12.93%` | `28,692.00` |
| `Live` | `Long` | `0.0664` | 4,850,000.00 USD | 0.00 USD | 27,600.00 USD | `-12.80%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,820,000.00 USD | 0.00 USD | 1,030.00 USD | `-12.67%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,820,000.00 USD | 0.00 USD | 68,480.00 USD | `-12.54%` | `1,029,041.00` |
| `Live` | `Long` | `0.0667` | 4,750,000.00 USD | 0.00 USD | 71,570.00 USD | `-12.41%` | `1,073,782.00` |
| `Live` | `Long` | `0.0668` | 4,680,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.27%` | `19,836.00` |
| `Live` | `Long` | `0.0669` | 4,680,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-12.14%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,660,000.00 USD | 0.00 USD | 4,540.00 USD | `-12.01%` | `67,813.00` |
| `Live` | `Long` | `0.0670` | 3,660,000.00 USD | 0.00 USD | 9,190.00 USD | `-11.88%` | `136,993.00` |
| `Live` | `Long` | `0.0672` | 3,650,000.00 USD | 0.00 USD | 899.27 USD | `-11.75%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,650,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.62%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,640,000.00 USD | 0.00 USD | 96,190.00 USD | `-11.49%` | `1,428,139.00` |
| `Live` | `Long` | `0.0674` | 3,540,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.35%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,540,000.00 USD | 0.00 USD | 310.73 USD | `-11.22%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,540,000.00 USD | 0.00 USD | 10,030.00 USD | `-11.09%` | `148,270.00` |
| `Live` | `Long` | `0.0678` | 3,530,000.00 USD | 0.00 USD | 140,600.00 USD | `-10.96%` | `2,075,221.00` |
| `Live` | `Long` | `0.0678` | 3,390,000.00 USD | 0.00 USD | 55,180.00 USD | `-10.83%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,330,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.70%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,320,000.00 USD | 0.00 USD | 212.72 USD | `-10.57%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,320,000.00 USD | 0.00 USD | 4,720.00 USD | `-10.44%` | `69,194.00` |
| `Live` | `Long` | `0.0683` | 3,310,000.00 USD | 0.00 USD | 55,650.00 USD | `-10.30%` | `815,403.00` |
| `Live` | `Long` | `0.0683` | 3,260,000.00 USD | 0.00 USD | 1,290.00 USD | `-10.17%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,260,000.00 USD | 0.00 USD | 6,000.00 USD | `-10.04%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,250,000.00 USD | 0.00 USD | 4,690.00 USD | `-9.91%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,250,000.00 USD | 0.00 USD | 68,230.00 USD | `-9.78%` | `993,855.00` |
| `Live` | `Long` | `0.0688` | 3,180,000.00 USD | 0.00 USD | 18,800.00 USD | `-9.65%` | `273,487.00` |
| `Live` | `Long` | `0.0688` | 3,160,000.00 USD | 0.00 USD | 1,170.00 USD | `-9.52%` | `17,063.00` |
| `Live` | `Long` | `0.0689` | 3,160,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.38%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,650,000.00 USD | 0.00 USD | 3,670.00 USD | `-9.25%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,650,000.00 USD | 0.00 USD | 8,350.00 USD | `-9.12%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,640,000.00 USD | 0.00 USD | 21,930.00 USD | `-8.99%` | `316,670.00` |
| `Live` | `Long` | `0.0693` | 2,620,000.00 USD | 0.00 USD | 2,160.00 USD | `-8.86%` | `31,211.00` |
| `Live` | `Long` | `0.0694` | 2,610,000.00 USD | 0.00 USD | 5,100.00 USD | `-8.73%` | `73,369.00` |
| `Live` | `Long` | `0.0696` | 2,610,000.00 USD | 0.00 USD | 14,930.00 USD | `-8.60%` | `214,659.00` |
| `Live` | `Long` | `0.0697` | 2,590,000.00 USD | 0.00 USD | 15,070.00 USD | `-8.46%` | `216,338.00` |
| `Live` | `Long` | `0.0698` | 2,580,000.00 USD | 0.00 USD | 3,420.00 USD | `-8.33%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,570,000.00 USD | 0.00 USD | 3,630.00 USD | `-8.20%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,570,000.00 USD | 0.00 USD | 1,310.00 USD | `-8.07%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,570,000.00 USD | 0.00 USD | 264.58 USD | `-7.94%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,570,000.00 USD | 0.00 USD | 1,590.00 USD | `-7.81%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,570,000.00 USD | 0.00 USD | 791.79 USD | `-7.68%` | `11,271.00` |
| `Live` | `Long` | `0.0703` | 2,570,000.00 USD | 0.00 USD | 5,060.00 USD | `-7.54%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,560,000.00 USD | 0.00 USD | 216.56 USD | `-7.41%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,560,000.00 USD | 0.00 USD | 94,410.00 USD | `-7.02%` | `1,334,448.00` |
| `Live` | `Long` | `0.0712` | 2,470,000.00 USD | 0.00 USD | 1,460.00 USD | `-6.49%` | `20,578.00` |
| `Live` | `Long` | `0.0712` | 2,470,000.00 USD | 0.00 USD | 389.38 USD | `-6.36%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,470,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-6.23%` | `24,493,121.00` |
| `Live` | `Long` | `0.0714` | 718,050.00 USD | 0.00 USD | 605.68 USD | `-6.10%` | `8,477.00` |
| `Live` | `Long` | `0.0716` | 717,450.00 USD | 0.00 USD | 8,120.00 USD | `-5.97%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 709,330.00 USD | 0.00 USD | 2,090.00 USD | `-5.84%` | `29,152.00` |
| `Live` | `Long` | `0.0717` | 707,240.00 USD | 0.00 USD | 24,930.00 USD | `-5.70%` | `347,503.00` |
| `Live` | `Long` | `0.0718` | 682,310.00 USD | 0.00 USD | 960.13 USD | `-5.57%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 681,350.00 USD | 0.00 USD | 1,900.00 USD | `-5.44%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 679,450.00 USD | 0.00 USD | 12,960.00 USD | `-5.31%` | `179,910.00` |
| `Live` | `Long` | `0.0722` | 666,490.00 USD | 0.00 USD | 22,360.00 USD | `-5.18%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 644,140.00 USD | 0.00 USD | 10,920.00 USD | `-5.05%` | `151,151.00` |
| `Live` | `Long` | `0.0723` | 633,210.00 USD | 0.00 USD | 626.77 USD | `-4.92%` | `8,663.00` |
| `Live` | `Long` | `0.0725` | 632,590.00 USD | 0.00 USD | 1,400.00 USD | `-4.78%` | `19,342.00` |
| `Live` | `Long` | `0.0726` | 631,190.00 USD | 0.00 USD | 260.74 USD | `-4.65%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 630,930.00 USD | 0.00 USD | 18,770.00 USD | `-4.52%` | `258,364.00` |
| `Live` | `Long` | `0.0727` | 612,160.00 USD | 0.00 USD | 452.21 USD | `-4.39%` | `6,216.00` |
| `Live` | `Long` | `0.0728` | 611,700.00 USD | 0.00 USD | 646.11 USD | `-4.26%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 611,060.00 USD | 0.00 USD | 72,950.00 USD | `-4.13%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 538,110.00 USD | 0.00 USD | 10,040.00 USD | `-4.00%` | `137,397.00` |
| `Live` | `Long` | `0.0732` | 528,070.00 USD | 0.00 USD | 1,930.00 USD | `-3.86%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 526,140.00 USD | 0.00 USD | 29,280.00 USD | `-3.73%` | `399,671.00` |
| `Live` | `Long` | `0.0735` | 496,870.00 USD | 0.00 USD | 3,930.00 USD | `-3.47%` | `53,459.00` |
| `Live` | `Long` | `0.0736` | 492,940.00 USD | 0.00 USD | 4,690.00 USD | `-3.34%` | `63,750.00` |
| `Live` | `Long` | `0.0736` | 488,250.00 USD | 0.00 USD | 5,490.00 USD | `-3.21%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 482,760.00 USD | 0.00 USD | 10,740.00 USD | `-3.08%` | `145,658.00` |
| `Live` | `Long` | `0.0738` | 472,020.00 USD | 0.00 USD | 314.08 USD | `-2.94%` | `4,253.00` |
| `Live` | `Long` | `0.0740` | 471,700.00 USD | 0.00 USD | 13,640.00 USD | `-2.81%` | `184,392.00` |
| `Live` | `Long` | `0.0741` | 458,070.00 USD | 0.00 USD | 455,080.00 USD | `-2.68%` | `6,145,600.00` |
| `Live` | `Long` | `0.0741` | 2,990.00 USD | 0.00 USD | 1,280.00 USD | `-2.55%` | `17,295.00` |
| `Live` | `Long` | `0.0742` | 1,700.00 USD | 0.00 USD | 1,280.00 USD | `-2.42%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 425.44 USD | 0.00 USD | 249.15 USD | `-2.29%` | `3,351.00` |
| `Live` | `Long` | `0.0745` | 176.30 USD | 0.00 USD | 176.30 USD | `-2.16%` | `2,368.00` |
| `Live` | `Short` | `0.0781` | 3,850.00 USD | 3,850.00 USD | 0.00 USD | `+2.71%` | `49,275.00` |
| `Live` | `Short` | `0.0795` | 4,180.00 USD | 329.00 USD | 0.00 USD | `+4.42%` | `4,141.00` |
| `Live` | `Short` | `0.0805` | 11,080.00 USD | 6,900.00 USD | 0.00 USD | `+5.86%` | `85,643.00` |
| `Live` | `Short` | `0.0817` | 11,290.00 USD | 214.66 USD | 0.00 USD | `+7.31%` | `2,629.00` |
| `Live` | `Short` | `0.0818` | 11,940.00 USD | 643.94 USD | 0.00 USD | `+7.44%` | `7,877.00` |
| `Live` | `Short` | `0.0822` | 15,920.00 USD | 3,990.00 USD | 0.00 USD | `+7.96%` | `48,519.00` |
| `Live` | `Short` | `0.0824` | 16,190.00 USD | 265.58 USD | 0.00 USD | `+8.23%` | `3,225.00` |
| `Live` | `Short` | `0.0832` | 19,640.00 USD | 3,450.00 USD | 0.00 USD | `+9.28%` | `41,543.00` |
| `Live` | `Short` | `0.0837` | 19,940.00 USD | 293.44 USD | 0.00 USD | `+9.94%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 21,510.00 USD | 1,570.00 USD | 0.00 USD | `+10.07%` | `18,767.00` |
| `Live` | `Short` | `0.0848` | 22,230.00 USD | 723.94 USD | 0.00 USD | `+11.51%` | `8,532.00` |
| `Live` | `Short` | `0.0858` | 22,350.00 USD | 115.30 USD | 0.00 USD | `+12.83%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 26,590.00 USD | 4,250.00 USD | 0.00 USD | `+12.96%` | `49,397.00` |
| `Live` | `Short` | `0.0871` | 29,260.00 USD | 2,660.00 USD | 0.00 USD | `+14.40%` | `30,613.00` |
| `Live` | `Short` | `0.0881` | 29,720.00 USD | 465.17 USD | 0.00 USD | `+15.72%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 30,130.00 USD | 411.53 USD | 0.00 USD | `+16.64%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 30,550.00 USD | 418.80 USD | 0.00 USD | `+17.03%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 30,840.00 USD | 285.70 USD | 0.00 USD | `+17.56%` | `3,194.00` |
| `Live` | `Short` | `0.0906` | 32,150.00 USD | 1,310.00 USD | 0.00 USD | `+19.14%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 32,890.00 USD | 743.15 USD | 0.00 USD | `+19.79%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 36,930.00 USD | 4,040.00 USD | 0.00 USD | `+19.92%` | `44,324.00` |
| `Live` | `Short` | `0.0917` | 38,700.00 USD | 1,760.00 USD | 0.00 USD | `+20.58%` | `19,213.00` |
| `Live` | `Short` | `0.0921` | 38,870.00 USD | 171.49 USD | 0.00 USD | `+20.98%` | `1,863.00` |
| `Live` | `Short` | `0.0922` | 39,060.00 USD | 187.73 USD | 0.00 USD | `+21.24%` | `2,035.00` |
| `Live` | `Short` | `0.0931` | 39,860.00 USD | 805.37 USD | 0.00 USD | `+22.42%` | `8,646.00` |
| `Live` | `Short` | `0.0935` | 42,050.00 USD | 2,190.00 USD | 0.00 USD | `+22.82%` | `23,466.00` |
| `Live` | `Short` | `0.0950` | 55,850.00 USD | 13,800.00 USD | 0.00 USD | `+24.79%` | `145,305.00` |
| `Live` | `Short` | `0.0950` | 103,380.00 USD | 47,520.00 USD | 0.00 USD | `+24.92%` | `500,000.00` |
| `Live` | `Short` | `0.0953` | 107,660.00 USD | 4,290.00 USD | 0.00 USD | `+25.18%` | `45,000.00` |
| `Live` | `Short` | `0.0961` | 108,270.00 USD | 609.59 USD | 0.00 USD | `+26.36%` | `6,340.00` |
| `Live` | `Short` | `0.0969` | 109,210.00 USD | 942.93 USD | 0.00 USD | `+27.28%` | `9,736.00` |
| `Live` | `Short` | `0.0974` | 109,350.00 USD | 139.74 USD | 0.00 USD | `+28.07%` | `1,434.00` |
| `Live` | `Short` | `0.0983` | 109,830.00 USD | 477.50 USD | 0.00 USD | `+29.12%` | `4,860.00` |
| `Live` | `Short` | `0.1014` | 117,460.00 USD | 7,630.00 USD | 0.00 USD | `+33.33%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 120,430.00 USD | 2,970.00 USD | 0.00 USD | `+33.59%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 120,920.00 USD | 492.85 USD | 0.00 USD | `+33.85%` | `4,839.00` |
| `Live` | `Short` | `0.1051` | 124,180.00 USD | 3,260.00 USD | 0.00 USD | `+38.19%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 130,290.00 USD | 6,110.00 USD | 0.00 USD | `+39.51%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 130,910.00 USD | 616.19 USD | 0.00 USD | `+41.48%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 134,150.00 USD | 3,240.00 USD | 0.00 USD | `+42.66%` | `29,849.00` |
| `Live` | `Short` | `0.1125` | 136,080.00 USD | 1,930.00 USD | 0.00 USD | `+47.92%` | `17,184.00` |
| `Live` | `Short` | `0.1127` | 138,560.00 USD | 2,480.00 USD | 0.00 USD | `+48.05%` | `22,021.00` |
| `Live` | `Short` | `0.1129` | 138,700.00 USD | 142.88 USD | 0.00 USD | `+48.44%` | `1,265.00` |
| `Live` | `Short` | `0.1130` | 142,090.00 USD | 3,390.00 USD | 0.00 USD | `+48.57%` | `29,960.00` |
| `Live` | `Short` | `0.1187` | 142,200.00 USD | 106.19 USD | 0.00 USD | `+55.93%` | `895.00` |
| `Live` | `Short` | `0.1215` | 143,070.00 USD | 876.75 USD | 0.00 USD | `+59.61%` | `7,219.00` |
| `Live` | `Short` | `0.1222` | 143,870.00 USD | 796.83 USD | 0.00 USD | `+60.67%` | `6,518.00` |
| `Live` | `Short` | `0.1234` | 145,360.00 USD | 1,490.00 USD | 0.00 USD | `+62.11%` | `12,089.00` |
| `Live` | `Short` | `0.1270` | 145,470.00 USD | 108.80 USD | 0.00 USD | `+66.84%` | `857.00` |
| `Live` | `Short` | `0.1286` | 145,590.00 USD | 124.15 USD | 0.00 USD | `+69.08%` | `965.00` |
| `Live` | `Short` | `0.1296` | 145,770.00 USD | 171.66 USD | 0.00 USD | `+70.39%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 147,900.00 USD | 2,140.00 USD | 0.00 USD | `+72.36%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 148,010.00 USD | 102.97 USD | 0.00 USD | `+73.28%` | `781.00` |
| `Live` | `Short` | `0.1326` | 182,250.00 USD | 34,250.00 USD | 0.00 USD | `+74.20%` | `258,360.00` |
| `Live` | `Short` | `0.1338` | 182,460.00 USD | 205.31 USD | 0.00 USD | `+75.78%` | `1,535.00` |
| `Live` | `Short` | `0.1361` | 182,590.00 USD | 134.38 USD | 0.00 USD | `+78.93%` | `987.00` |
| `Live` | `Short` | `0.1404` | 206,030.00 USD | 23,440.00 USD | 0.00 USD | `+84.58%` | `166,905.00` |
| `Live` | `Short` | `0.1417` | 207,130.00 USD | 1,090.00 USD | 0.00 USD | `+86.29%` | `7,716.00` |
| `Live` | `Short` | `0.1432` | 208,990.00 USD | 1,860.00 USD | 0.00 USD | `+88.26%` | `13,010.00` |
| `Live` | `Short` | `0.1441` | 209,190.00 USD | 196.63 USD | 0.00 USD | `+89.32%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 210,730.00 USD | 1,540.00 USD | 0.00 USD | `+89.71%` | `10,691.00` |
| `Live` | `Short` | `0.1447` | 211,170.00 USD | 434.25 USD | 0.00 USD | `+90.24%` | `3,000.00` |
| `Live` | `Short` | `0.1467` | 217,560.00 USD | 6,390.00 USD | 0.00 USD | `+92.73%` | `43,601.00` |
| `Live` | `Short` | `0.1479` | 225,840.00 USD | 8,280.00 USD | 0.00 USD | `+94.31%` | `56,001.00` |
| `Live` | `Short` | `0.1479` | 3,320,000.00 USD | 3,090,000.00 USD | 0.00 USD | `+94.44%` | `20,910,149.00` |
| `Live` | `Short` | `0.1484` | 3,320,000.00 USD | 1,970.00 USD | 0.00 USD | `+95.10%` | `13,240.00` |
| `Live` | `Short` | `0.1522` | 3,380,000.00 USD | 56,970.00 USD | 0.00 USD | `+99.96%` | `374,415.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 533,370.00 USD | 0.00 USD | 375.42 USD | `-66.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 533,000.00 USD | 0.00 USD | 409.59 USD | `-47.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 532,590.00 USD | 0.00 USD | 132.68 USD | `-46.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 532,450.00 USD | 0.00 USD | 788.27 USD | `-45.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 531,660.00 USD | 0.00 USD | 527.05 USD | `-45.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 531,140.00 USD | 0.00 USD | 286.87 USD | `-40.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 530,850.00 USD | 0.00 USD | 252.42 USD | `-39.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 530,600.00 USD | 0.00 USD | 468.67 USD | `-38.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 530,130.00 USD | 0.00 USD | 5,160.00 USD | `-35.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 524,970.00 USD | 0.00 USD | 920.48 USD | `-35.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 524,050.00 USD | 0.00 USD | 1,730.00 USD | `-34.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 522,320.00 USD | 0.00 USD | 175.41 USD | `-32.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 522,140.00 USD | 0.00 USD | 2,670.00 USD | `-28.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 519,470.00 USD | 0.00 USD | 1,370.00 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 518,100.00 USD | 0.00 USD | 437.58 USD | `-26.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 517,660.00 USD | 0.00 USD | 752.54 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 516,910.00 USD | 0.00 USD | 9,830.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 507,080.00 USD | 0.00 USD | 1,020.00 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 506,060.00 USD | 0.00 USD | 668.84 USD | `-21.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 505,390.00 USD | 0.00 USD | 8,800.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 496,590.00 USD | 0.00 USD | 504.26 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 496,090.00 USD | 0.00 USD | 2,280.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 493,810.00 USD | 0.00 USD | 1,280.00 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 492,530.00 USD | 0.00 USD | 920.18 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 491,610.00 USD | 0.00 USD | 412.42 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 491,200.00 USD | 0.00 USD | 1,130.00 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 490,070.00 USD | 0.00 USD | 362.24 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 489,710.00 USD | 0.00 USD | 3,140.00 USD | `-13.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 486,570.00 USD | 0.00 USD | 1,100.00 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 485,470.00 USD | 0.00 USD | 1,200.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 484,270.00 USD | 0.00 USD | 996.31 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 483,280.00 USD | 0.00 USD | 632.88 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 482,640.00 USD | 0.00 USD | 115.57 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 482,530.00 USD | 0.00 USD | 33,620.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 448,900.00 USD | 0.00 USD | 12,860.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 436,040.00 USD | 0.00 USD | 1,260.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 434,780.00 USD | 0.00 USD | 108.08 USD | `-11.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 434,670.00 USD | 0.00 USD | 21,550.00 USD | `-11.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 413,120.00 USD | 0.00 USD | 1,430.00 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 411,690.00 USD | 0.00 USD | 7,990.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 403,690.00 USD | 0.00 USD | 8,580.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 395,120.00 USD | 0.00 USD | 606.47 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 394,510.00 USD | 0.00 USD | 160.31 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 394,350.00 USD | 0.00 USD | 38,710.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 355,650.00 USD | 0.00 USD | 660.06 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 354,990.00 USD | 0.00 USD | 102.34 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 354,880.00 USD | 0.00 USD | 1,120.00 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 353,770.00 USD | 0.00 USD | 144.59 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 353,620.00 USD | 0.00 USD | 925.29 USD | `-8.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 352,700.00 USD | 0.00 USD | 697.50 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 352,000.00 USD | 0.00 USD | 17,520.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 334,470.00 USD | 0.00 USD | 1,350.00 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 333,130.00 USD | 0.00 USD | 523.23 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 332,600.00 USD | 0.00 USD | 235.12 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 332,370.00 USD | 0.00 USD | 204.40 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 332,160.00 USD | 0.00 USD | 107,720.00 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 224,440.00 USD | 0.00 USD | 12,930.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 211,510.00 USD | 0.00 USD | 20,070.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 191,440.00 USD | 0.00 USD | 608.76 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 190,830.00 USD | 0.00 USD | 16,880.00 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 173,960.00 USD | 0.00 USD | 1,670.00 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 172,280.00 USD | 0.00 USD | 4,710.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 167,570.00 USD | 0.00 USD | 8,430.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 159,140.00 USD | 0.00 USD | 413.42 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 158,730.00 USD | 0.00 USD | 881.82 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 157,840.00 USD | 0.00 USD | 703.43 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 157,140.00 USD | 0.00 USD | 621.12 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 156,520.00 USD | 0.00 USD | 1,430.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 155,090.00 USD | 0.00 USD | 29,060.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 126,020.00 USD | 0.00 USD | 4,500.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 121,520.00 USD | 0.00 USD | 2,090.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 119,430.00 USD | 0.00 USD | 23,870.00 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 95,560.00 USD | 0.00 USD | 28,940.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 66,620.00 USD | 0.00 USD | 123.40 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 66,490.00 USD | 0.00 USD | 2,710.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 63,790.00 USD | 0.00 USD | 1,530.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 62,250.00 USD | 0.00 USD | 4,680.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 57,570.00 USD | 0.00 USD | 1,000.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 56,570.00 USD | 0.00 USD | 2,900.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 53,680.00 USD | 0.00 USD | 415.62 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 53,260.00 USD | 0.00 USD | 1,720.00 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 51,550.00 USD | 0.00 USD | 5,750.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 45,790.00 USD | 0.00 USD | 375.86 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 45,420.00 USD | 0.00 USD | 193.90 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 45,220.00 USD | 0.00 USD | 140.04 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 45,080.00 USD | 0.00 USD | 37,480.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 7,610.00 USD | 0.00 USD | 3,450.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 4,160.00 USD | 0.00 USD | 736.17 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 3,420.00 USD | 0.00 USD | 398.60 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 3,020.00 USD | 0.00 USD | 465.39 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 2,560.00 USD | 0.00 USD | 358.13 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 2,200.00 USD | 0.00 USD | 206.80 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 1,990.00 USD | 0.00 USD | 796.88 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 1,200.00 USD | 0.00 USD | 398.13 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 797.92 USD | 0.00 USD | 797.92 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 806.81 USD | 806.81 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 1,170.00 USD | 359.60 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 1,500.00 USD | 335.56 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 1,610.00 USD | 109.63 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 1,820.00 USD | 203.47 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 5,350.00 USD | 3,540.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 5,520.00 USD | 168.24 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 5,670.00 USD | 143.94 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 6,480.00 USD | 816.05 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 21,880.00 USD | 15,400.00 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 24,120.00 USD | 2,240.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 24,330.00 USD | 210.89 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 28,150.00 USD | 3,820.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 28,560.00 USD | 407.23 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 28,880.00 USD | 321.13 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 30,370.00 USD | 1,490.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 30,780.00 USD | 407.72 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 31,320.00 USD | 544.09 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 31,730.00 USD | 409.16 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 33,740.00 USD | 2,010.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 35,090.00 USD | 1,350.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 35,310.00 USD | 222.46 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 39,680.00 USD | 4,370.00 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 40,070.00 USD | 396.49 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 55,860.00 USD | 15,790.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 97,280.00 USD | 41,420.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 100,310.00 USD | 3,030.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 100,420.00 USD | 100.53 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 101,980.00 USD | 1,560.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 104,340.00 USD | 2,360.00 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 108,940.00 USD | 4,600.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 111,190.00 USD | 2,260.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 112,210.00 USD | 1,010.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 112,650.00 USD | 444.13 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 113,110.00 USD | 455.34 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 113,230.00 USD | 125.45 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 113,460.00 USD | 230.40 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 113,780.00 USD | 319.16 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 114,790.00 USD | 1,010.00 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 137,540.00 USD | 22,750.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 137,940.00 USD | 400.91 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 138,140.00 USD | 200.46 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 138,400.00 USD | 259.13 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 139,110.00 USD | 707.08 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 140,150.00 USD | 1,050.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 236,930.00 USD | 96,780.00 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 237,740.00 USD | 807.50 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 238,000.00 USD | 257.18 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 238,420.00 USD | 424.74 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 238,520.00 USD | 101.80 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 239,910.00 USD | 1,380.00 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 240,170.00 USD | 264.63 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 241,600.00 USD | 1,430.00 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 241,730.00 USD | 129.67 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 242,750.00 USD | 1,020.00 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 245,200.00 USD | 2,450.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 246,220.00 USD | 1,030.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 248,830.00 USD | 2,610.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 249,160.00 USD | 327.80 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 249,770.00 USD | 607.58 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 256,650.00 USD | 6,880.00 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 257,450.00 USD | 800.79 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 257,970.00 USD | 512.05 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 258,210.00 USD | 240.26 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 258,600.00 USD | 389.31 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 259,300.00 USD | 706.02 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 259,610.00 USD | 303.56 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 259,720.00 USD | 112.89 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 260,100.00 USD | 381.45 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 260,260.00 USD | 155.82 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 261,690.00 USD | 1,430.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 261,830.00 USD | 138.69 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 263,090.00 USD | 1,260.00 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 263,190.00 USD | 107.03 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,010,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,020,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,020,000.00 USD | 341.34 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,020,000.00 USD | 107.71 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,020,000.00 USD | 2,690.00 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,020,000.00 USD | 1,440.00 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,020,000.00 USD | 219.07 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,020,000.00 USD | 326.97 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,020,000.00 USD | 242.84 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,040,000.00 USD | 13,510.00 USD | 0.00 USD | `+11.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 2,040,000.00 USD | 152.92 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,040,000.00 USD | 876.11 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,040,000.00 USD | 205.59 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,040,000.00 USD | 126.76 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,040,000.00 USD | 307.41 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,040,000.00 USD | 614.09 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,040,000.00 USD | 644.62 USD | 0.00 USD | `+12.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 2,040,000.00 USD | 180.45 USD | 0.00 USD | `+13.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,040,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,090,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,090,000.00 USD | 1,080.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,090,000.00 USD | 384.06 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,090,000.00 USD | 1,840.00 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,090,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,090,000.00 USD | 117.71 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,090,000.00 USD | 111.61 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,090,000.00 USD | 571.18 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,090,000.00 USD | 375.94 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,090,000.00 USD | 627.55 USD | 0.00 USD | `+16.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,090,000.00 USD | 211.04 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,090,000.00 USD | 108.36 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,090,000.00 USD | 543.32 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,100,000.00 USD | 1,820.00 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,100,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,120,000.00 USD | 17,680.00 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,120,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,120,000.00 USD | 5,630.00 USD | 0.00 USD | `+18.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,120,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,120,000.00 USD | 224.86 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,140,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,140,000.00 USD | 114.93 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,150,000.00 USD | 679.12 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,150,000.00 USD | 173.36 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,150,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,150,000.00 USD | 1,580.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,150,000.00 USD | 2,300.00 USD | 0.00 USD | `+21.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,150,000.00 USD | 541.32 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,290,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,290,000.00 USD | 691.07 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,300,000.00 USD | 6,250.00 USD | 0.00 USD | `+21.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,310,000.00 USD | 13,480.00 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,310,000.00 USD | 734.82 USD | 0.00 USD | `+22.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,310,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,310,000.00 USD | 184.09 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,310,000.00 USD | 1,120.00 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,320,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,320,000.00 USD | 512.15 USD | 0.00 USD | `+23.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,320,000.00 USD | 6,620.00 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,320,000.00 USD | 404.96 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,320,000.00 USD | 129.85 USD | 0.00 USD | `+25.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,330,000.00 USD | 3,740.00 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,330,000.00 USD | 2,400.00 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,330,000.00 USD | 409.17 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,330,000.00 USD | 203.74 USD | 0.00 USD | `+27.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,330,000.00 USD | 2,800.00 USD | 0.00 USD | `+27.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,330,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,330,000.00 USD | 694.56 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,340,000.00 USD | 940.91 USD | 0.00 USD | `+29.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,340,000.00 USD | 2,980.00 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,340,000.00 USD | 104.99 USD | 0.00 USD | `+30.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,340,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,340,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,340,000.00 USD | 1,090.00 USD | 0.00 USD | `+30.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,340,000.00 USD | 438.96 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,340,000.00 USD | 973.76 USD | 0.00 USD | `+31.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,460,000.00 USD | 111,100.00 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,460,000.00 USD | 175.59 USD | 0.00 USD | `+31.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,460,000.00 USD | 482.89 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,460,000.00 USD | 201.90 USD | 0.00 USD | `+32.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,460,000.00 USD | 489.46 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,460,000.00 USD | 103.68 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,460,000.00 USD | 203.70 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,460,000.00 USD | 3,810.00 USD | 0.00 USD | `+33.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,470,000.00 USD | 11,200.00 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,480,000.00 USD | 4,330.00 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,480,000.00 USD | 205.50 USD | 0.00 USD | `+35.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,480,000.00 USD | 3,490.00 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,480,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,480,000.00 USD | 207.50 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,480,000.00 USD | 813.88 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,510,000.00 USD | 23,160.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,510,000.00 USD | 781.51 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,510,000.00 USD | 209.30 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,510,000.00 USD | 1,440.00 USD | 0.00 USD | `+37.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,510,000.00 USD | 5,140.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,510,000.00 USD | 585.32 USD | 0.00 USD | `+38.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,510,000.00 USD | 210.90 USD | 0.00 USD | `+38.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,520,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,520,000.00 USD | 105.75 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,520,000.00 USD | 3,220.00 USD | 0.00 USD | `+39.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,520,000.00 USD | 1,600.00 USD | 0.00 USD | `+39.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,520,000.00 USD | 212.90 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,520,000.00 USD | 472.63 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,520,000.00 USD | 214.50 USD | 0.00 USD | `+40.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,520,000.00 USD | 1,040.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,520,000.00 USD | 136.12 USD | 0.00 USD | `+41.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,520,000.00 USD | 216.10 USD | 0.00 USD | `+42.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,560,000.00 USD | 40,920.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,560,000.00 USD | 217.90 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,560,000.00 USD | 219.70 USD | 0.00 USD | `+44.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,570,000.00 USD | 7,920.00 USD | 0.00 USD | `+44.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,570,000.00 USD | 154.22 USD | 0.00 USD | `+45.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,570,000.00 USD | 221.30 USD | 0.00 USD | `+45.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,570,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,600,000.00 USD | 24,440.00 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,600,000.00 USD | 223.10 USD | 0.00 USD | `+46.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,600,000.00 USD | 2,120.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,600,000.00 USD | 226.30 USD | 0.00 USD | `+48.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,600,000.00 USD | 351.57 USD | 0.00 USD | `+49.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,600,000.00 USD | 950.34 USD | 0.00 USD | `+49.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,600,000.00 USD | 229.50 USD | 0.00 USD | `+50.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,600,000.00 USD | 771.08 USD | 0.00 USD | `+51.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,600,000.00 USD | 230.90 USD | 0.00 USD | `+51.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,600,000.00 USD | 288.18 USD | 0.00 USD | `+51.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,600,000.00 USD | 619.10 USD | 0.00 USD | `+52.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,610,000.00 USD | 1,250.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,610,000.00 USD | 1,050.00 USD | 0.00 USD | `+52.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,610,000.00 USD | 232.30 USD | 0.00 USD | `+52.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,610,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,610,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,610,000.00 USD | 3,730.00 USD | 0.00 USD | `+54.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,610,000.00 USD | 676.22 USD | 0.00 USD | `+54.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,610,000.00 USD | 648.25 USD | 0.00 USD | `+55.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,620,000.00 USD | 1,510.00 USD | 0.00 USD | `+55.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,620,000.00 USD | 448.52 USD | 0.00 USD | `+55.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,620,000.00 USD | 136.93 USD | 0.00 USD | `+55.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,620,000.00 USD | 124.58 USD | 0.00 USD | `+55.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,620,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,620,000.00 USD | 691.80 USD | 0.00 USD | `+57.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,740,000.00 USD | 117,860.00 USD | 0.00 USD | `+57.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,740,000.00 USD | 143.22 USD | 0.00 USD | `+58.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,740,000.00 USD | 803.95 USD | 0.00 USD | `+58.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,740,000.00 USD | 1,380.00 USD | 0.00 USD | `+59.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,740,000.00 USD | 2,270.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,740,000.00 USD | 871.99 USD | 0.00 USD | `+60.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,770,000.00 USD | 24,560.00 USD | 0.00 USD | `+66.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,770,000.00 USD | 400.21 USD | 0.00 USD | `+66.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,780,000.00 USD | 13,850.00 USD | 0.00 USD | `+73.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,780,000.00 USD | 2,360.00 USD | 0.00 USD | `+73.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,790,000.00 USD | 4,160.00 USD | 0.00 USD | `+78.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,790,000.00 USD | 114.70 USD | 0.00 USD | `+79.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,790,000.00 USD | 257.51 USD | 0.00 USD | `+83.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,790,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,790,000.00 USD | 173.57 USD | 0.00 USD | `+86.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,790,000.00 USD | 380.09 USD | 0.00 USD | `+86.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,810,000.00 USD | 17,150.00 USD | 0.00 USD | `+87.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,810,000.00 USD | 433.35 USD | 0.00 USD | `+89.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,810,000.00 USD | 3,640.00 USD | 0.00 USD | `+93.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,870,000.00 USD | 55,720.00 USD | 0.00 USD | `+94.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,870,000.00 USD | 2,120.00 USD | 0.00 USD | `+94.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,890,000.00 USD | 19,850.00 USD | 0.00 USD | `+97.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,890,000.00 USD | 1,620.00 USD | 0.00 USD | `+98.91%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0673` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0675` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 0.00 USD | 5,530.00 USD | 0.00 USD |
| `1D` | `0.0676` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 45,230.00 USD | 24,730.00 USD | 0.00 USD |
| `1D` | `0.0678` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 3,200.00 USD | 39,890.00 USD | 56,870.00 USD |
| `1D` | `0.0679` | 11,320,000.00 USD | 0.00 USD | 11,320,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD |
| `1D` | `0.0680` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 986.19 USD |
| `1D` | `0.0681` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 133,250.00 USD |
| `1D` | `0.0682` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 2,550.00 USD | 33,950.00 USD | 10,630.00 USD |
| `1D` | `0.0683` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 0.00 USD | 20,340.00 USD | 0.00 USD |
| `1D` | `0.0684` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 24,150.00 USD | 13,610.00 USD | 584.27 USD |
| `1D` | `0.0685` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 41,510.00 USD | 0.00 USD | 6,950.00 USD |
| `1D` | `0.0686` | 11,000,000.00 USD | 0.00 USD | 11,000,000.00 USD | 41,080.00 USD | 1,410.00 USD | 7,120.00 USD |
| `1D` | `0.0687` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD |
| `1D` | `0.0688` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0691` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD |
| `1D` | `0.0698` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,560.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,900.00 USD |
| `1D` | `0.0700` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,780.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 35,400.00 USD | 18,030.00 USD | 27,560.00 USD |
| `1D` | `0.0702` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 78,740.00 USD | 36,780.00 USD | 0.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 87,540.00 USD | 31,470.00 USD | 40,010.00 USD |
| `1D` | `0.0704` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,040.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 34,530.00 USD | 24,910.00 USD | 35,660.00 USD |
| `1D` | `0.0706` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 36,930.00 USD | 29,080.00 USD | 25,400.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 54,240.00 USD | 21,680.00 USD | 26,900.00 USD |
| `1D` | `0.0708` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 25,410.00 USD | 16,310.00 USD | 26,670.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 36,740.00 USD | 37,120.00 USD | 14,980.00 USD |
| `1D` | `0.0710` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,600.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,110.00 USD |
| `1D` | `0.0712` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 35,120.00 USD | 58,130.00 USD | 62,580.00 USD |
| `1D` | `0.0714` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,660.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 34,440.00 USD | 8,830.00 USD | 36,110.00 USD |
| `1D` | `0.0716` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 30,130.00 USD | 31,610.00 USD | 361.93 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 16,400.00 USD | 7,710.00 USD | 21,830.00 USD |
| `1D` | `0.0718` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 61,550.00 USD | 31,390.00 USD | 36,920.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 14,000.00 USD | 0.00 USD | 138.82 USD |
| `1D` | `0.0720` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 31,160.00 USD | 29,440.00 USD | 37,180.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 136,510.00 USD | 76,220.00 USD | 12,510.00 USD |
| `1D` | `0.0722` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,800.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 54,790.00 USD | 162,040.00 USD | 149,810.00 USD |
| `1D` | `0.0724` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 27,830.00 USD | 87,980.00 USD | 92,430.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 54,140.00 USD | 22,980.00 USD | 23,620.00 USD |
| `1D` | `0.0726` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 40,350.00 USD | 0.00 USD | 3,840.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 168,660.00 USD | 0.00 USD | 333,360.00 USD |
| `1D` | `0.0728` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 66,510.00 USD | 85,670.00 USD | 79,030.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 19,510.00 USD | 66,850.00 USD | 28,860.00 USD |
| `1D` | `0.0730` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 112,200.00 USD | 50,880.00 USD | 1,460.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 152,870.00 USD | 17,510.00 USD | 17,460.00 USD |
| `1D` | `0.0732` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 154,930.00 USD | 60,240.00 USD | 65,690.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 15,550.00 USD | 0.00 USD | 70,240.00 USD |
| `1D` | `0.0734` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 33,390.00 USD | 31,100.00 USD | 0.00 USD |
| `1D` | `0.0736` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 234,720.00 USD | 123,630.00 USD | 41.24 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 51,890.00 USD | 42,510.00 USD | 127.94 USD |
| `1D` | `0.0738` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,450.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,920.00 USD |
| `1D` | `0.0740` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 33,740.00 USD | 0.00 USD | 328.72 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 36,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0742` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 286,340.00 USD | 0.00 USD | 666,830.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 118,640.00 USD | 234,470.00 USD | 190,450.00 USD |
| `1D` | `0.0744` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 19,880.00 USD | 156,580.00 USD | 59,340.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 199,850.00 USD | 158,980.00 USD | 24,790.00 USD |
| `1D` | `0.0746` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 371,240.00 USD | 210,430.00 USD | 160,380.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 466,980.00 USD | 159,330.00 USD | 99,060.00 USD |
| `1D` | `0.0748` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 130,290.00 USD | 143,100.00 USD | 194,490.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 639,090.00 USD | 0.00 USD | 639,090.00 USD | 203,330.00 USD | 0.00 USD | 148,440.00 USD |
| `1D` | `0.0750` | 287,320.00 USD | 0.00 USD | 287,320.00 USD | 69,890.00 USD | 0.00 USD | 121,470.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 95,970.00 USD | 0.00 USD | 95,970.00 USD | 0.00 USD | 6,860.00 USD | 150.54 USD |
| `1D` | `0.0752` | 88,960.00 USD | 0.00 USD | 88,960.00 USD | 0.00 USD | 0.00 USD | 458.62 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 88,500.00 USD | 0.00 USD | 88,500.00 USD | 0.00 USD | 85,010.00 USD | 152.61 USD |
| `1D` | `0.0754` | 3,340.00 USD | 0.00 USD | 3,340.00 USD | 0.00 USD | 0.00 USD | 167.18 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 3,170.00 USD | 0.00 USD | 3,170.00 USD | 0.00 USD | 0.00 USD | 144.95 USD |
| `1D` | `0.0756` | 3,030.00 USD | 0.00 USD | 3,030.00 USD | 0.00 USD | 0.00 USD | 911.60 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 2,110.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 275.94 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 1,840.00 USD | 0.00 USD | 1,840.00 USD | 0.00 USD | 0.00 USD | 667.96 USD |
| `1D` | `0.0760` | 1,170.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 300.51 USD | 300.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | 300.51 USD |
| `1D` | `0.0761` | 601.02 USD | 601.02 USD | 0.00 USD | 0.00 USD | 0.00 USD | 300.51 USD |
| `1D` | `0.0762` | 856.36 USD | 856.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | 255.34 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 14,080.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD |
| `1D` | `0.0764` | 341,310.00 USD | 341,310.00 USD | 0.00 USD | 0.00 USD | 325,960.00 USD | 1,280.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 599,360.00 USD | 599,360.00 USD | 0.00 USD | 0.00 USD | 257,590.00 USD | 457.32 USD |
| `1D` | `0.0766` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 765,870.00 USD | 360,800.00 USD | 0.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 190,810.00 USD | 192,160.00 USD | 502.66 USD |
| `1D` | `0.0768` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 351,760.00 USD | 0.00 USD | 514,240.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 181,440.00 USD | 341,350.00 USD | 148,150.00 USD |
| `1D` | `0.0770` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 272,760.00 USD | 93,300.00 USD | 254,120.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 216,410.00 USD | 232,340.00 USD | 212,270.00 USD |
| `1D` | `0.0772` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 286,340.00 USD | 0.00 USD | 666,710.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 65,160.00 USD | 169,730.00 USD | 149,000.00 USD |
| `1D` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 133,700.00 USD | 19,440.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 155,740.00 USD | 101,750.00 USD | 0.00 USD |
| `1D` | `0.0776` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 190,100.00 USD | 47,010.00 USD | 34,750.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 205,390.00 USD | 264,690.00 USD | 47,950.00 USD |
| `1D` | `0.0778` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 16,790.00 USD | 202,930.00 USD | 296,140.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 85,950.00 USD | 140,320.00 USD |
| `1D` | `0.0780` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 69,890.00 USD | 31,980.00 USD | 0.00 USD |
| `1D` | `0.0781` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 113,060.00 USD | 68,670.00 USD | 0.00 USD |
| `1D` | `0.0782` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 8,010.00 USD | 184,740.00 USD | 142,180.00 USD |
| `1D` | `0.0784` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 179,570.00 USD | 117,040.00 USD | 237,660.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 298,820.00 USD | 307,550.00 USD | 333,120.00 USD |
| `1D` | `0.0788` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 75,490.00 USD | 181,170.00 USD | 79,030.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 234,900.00 USD | 176,740.00 USD | 91,930.00 USD |
| `1D` | `0.0790` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 102,120.00 USD | 54,140.00 USD | 1,460.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 152,950.00 USD | 63,280.00 USD | 66,830.00 USD |
| `1D` | `0.0792` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 104,950.00 USD | 18,870.00 USD | 17,800.00 USD |
| `1D` | `0.0794` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 83,300.00 USD | 41,370.00 USD | 52,360.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 10,150.00 USD | 0.00 USD | 70,160.00 USD |
| `1D` | `0.0796` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 21,670.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 191,110.00 USD | 89,760.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 13,660,000.00 USD | 13,660,000.00 USD | 0.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD |
| `1D` | `0.0800` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD |
| `1D` | `0.0801` | 14,350,000.00 USD | 14,350,000.00 USD | 0.00 USD | 6,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0802` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 36,660.00 USD |
| `1D` | `0.0804` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD |
| `1D` | `0.0806` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 214,730.00 USD | 208,070.00 USD | 44,370.00 USD |
| `1D` | `0.0808` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 419,500.00 USD | 131,030.00 USD | 522,200.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 477,790.00 USD | 336,610.00 USD | 16,490.00 USD |
| `1D` | `0.0810` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 293,220.00 USD | 180,540.00 USD | 132,320.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 83,280.00 USD | 241,410.00 USD | 875.97 USD |
| `1D` | `0.0812` | 18,510,000.00 USD | 18,510,000.00 USD | 0.00 USD | 144,600.00 USD | 99,490.00 USD | 135,920.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 49,290.00 USD | 23,210.00 USD | 208,970.00 USD |
| `1D` | `0.0814` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 29,840.00 USD | 79,960.00 USD | 292,740.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 19,590,000.00 USD | 19,590,000.00 USD | 0.00 USD | 191,850.00 USD | 80,500.00 USD | 122,740.00 USD |
| `1D` | `0.0816` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 348,980.00 USD | 194,790.00 USD | 177,800.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 301,230.00 USD | 127,050.00 USD | 130,420.00 USD |
| `1D` | `0.0818` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 269,340.00 USD | 161,260.00 USD | 308,300.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 22,230,000.00 USD | 22,230,000.00 USD | 0.00 USD | 174,640.00 USD | 312,480.00 USD | 128,220.00 USD |
| `1D` | `0.0820` | 22,910,000.00 USD | 22,910,000.00 USD | 0.00 USD | 136,010.00 USD | 202,840.00 USD | 344,490.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 23,370,000.00 USD | 23,370,000.00 USD | 0.00 USD | 210,590.00 USD | 79,630.00 USD | 170,520.00 USD |
| `1D` | `0.0822` | 23,960,000.00 USD | 23,960,000.00 USD | 0.00 USD | 262,170.00 USD | 169,200.00 USD | 155,850.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 24,310,000.00 USD | 24,310,000.00 USD | 0.00 USD | 270,850.00 USD | 75,420.00 USD | 8,500.00 USD |
| `1D` | `0.0824` | 24,890,000.00 USD | 24,890,000.00 USD | 0.00 USD | 151,910.00 USD | 226,510.00 USD | 199,280.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 25,170,000.00 USD | 25,170,000.00 USD | 0.00 USD | 127,790.00 USD | 122,020.00 USD | 27,930.00 USD |
| `1D` | `0.0826` | 25,590,000.00 USD | 25,590,000.00 USD | 0.00 USD | 150,570.00 USD | 84,820.00 USD | 190,080.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 25,690,000.00 USD | 25,690,000.00 USD | 0.00 USD | 52,670.00 USD | 48,230.00 USD | 0.00 USD |
| `1D` | `0.0828` | 26,060,000.00 USD | 26,060,000.00 USD | 0.00 USD | 225,780.00 USD | 75,940.00 USD | 65,320.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 26,440,000.00 USD | 26,440,000.00 USD | 0.00 USD | 197,520.00 USD | 111,290.00 USD | 72,510.00 USD |
| `1D` | `0.0830` | 26,790,000.00 USD | 26,790,000.00 USD | 0.00 USD | 161,710.00 USD | 84,690.00 USD | 97,900.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 26,870,000.00 USD | 26,870,000.00 USD | 0.00 USD | 60,680.00 USD | 3,890.00 USD | 24,400.00 USD |
| `1D` | `0.0832` | 27,190,000.00 USD | 27,190,000.00 USD | 0.00 USD | 166,490.00 USD | 66,230.00 USD | 81,010.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 27,530,000.00 USD | 27,530,000.00 USD | 0.00 USD | 119,590.00 USD | 55,260.00 USD | 164,980.00 USD |
| `1D` | `0.0834` | 27,880,000.00 USD | 27,880,000.00 USD | 0.00 USD | 127,020.00 USD | 94,190.00 USD | 127,900.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 28,230,000.00 USD | 28,230,000.00 USD | 0.00 USD | 107,580.00 USD | 176,580.00 USD | 64,110.00 USD |
| `1D` | `0.0836` | 28,480,000.00 USD | 28,480,000.00 USD | 0.00 USD | 48,890.00 USD | 61,760.00 USD | 145,930.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 28,670,000.00 USD | 28,670,000.00 USD | 0.00 USD | 131,180.00 USD | 17,710.00 USD | 40,830.00 USD |
| `1D` | `0.0838` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 170,560.00 USD | 70,030.00 USD | 32,510.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 29,030,000.00 USD | 29,030,000.00 USD | 0.00 USD | 52,570.00 USD | 16,550.00 USD | 15,730.00 USD |
| `1D` | `0.0840` | 29,090,000.00 USD | 29,090,000.00 USD | 0.00 USD | 13,720.00 USD | 15,480.00 USD | 28,660.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 29,110,000.00 USD | 29,110,000.00 USD | 0.00 USD | 23,380.00 USD | 2,010.00 USD | 284.68 USD |
| `1D` | `0.0842` | 29,180,000.00 USD | 29,180,000.00 USD | 0.00 USD | 22,710.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 29,220,000.00 USD | 29,220,000.00 USD | 0.00 USD | 33,600.00 USD | 0.00 USD | 1.38 USD |
| `1D` | `0.0844` | 29,300,000.00 USD | 29,300,000.00 USD | 0.00 USD | 79,050.00 USD | 0.00 USD | 371.78 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | 542.17 USD |
| `1D` | `0.0846` | 29,400,000.00 USD | 29,400,000.00 USD | 0.00 USD | 72,340.00 USD | 16,670.00 USD | 9.48 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 29,420,000.00 USD | 29,420,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.08B` | Total OI Tokens: `14,154,793,622.3 DOGE`
  * 1h OI Change: `-0.22%` | 4h OI Change: `-3.69%` | 24h OI Change: `-5.84%`
  * Exchange Breakdown: Binance=`250.41M` | Bybit=`107.83M` | OKX=`108.16M` | Hyperliquid=`76.53M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-859.98` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0046%` | **USDT OKX** | `0.0029%` |
| **USDT Bybit** | `-0.0138%` | **USDT KuCoin** | `-0.0006%` |
| **USDT MEXC** | `0.0046%` | **USDT BingX** | `0.0051%` |
| **USDT Gate** | `-0.0017%` | **USDT Bitget** | `-0.0002%` |
| **CoinM Binance** | `0.0078%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `46.57%` | `53.43%` | `0.87` | 66,250,000.00 USD |
| `15M` | `Binance` | `50.05%` | `49.95%` | `1.00` | 41,680,000.00 USD |
| `15M` | `OKX` | `47.76%` | `52.24%` | `0.91` | 3,880,000.00 USD |
| `15M` | `Bybit` | `37.07%` | `62.93%` | `0.59` | 9,820,000.00 USD |
| `15M` | `KuCoin` | `50.87%` | `49.13%` | `1.04` | 124,370.00 USD |
| `15M` | `Gate` | `55.98%` | `44.02%` | `1.27` | 808,390.00 USD |
| `15M` | `Bitget` | `44.41%` | `55.59%` | `0.80` | 644,140.00 USD |
| `15M` | `BingX` | `59.71%` | `40.29%` | `1.48` | 662,690.00 USD |
| `15M` | `MEXC` | `58.7%` | `41.3%` | `1.42` | 719,740.00 USD |
| `15M` | `Bitunix` | `49.34%` | `50.66%` | `0.97` | 1,540,000.00 USD |
| `15M` | `Hyperliquid` | `32.19%` | `67.81%` | `0.47` | 3,830,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.24%` | `52.76%` | `0.90` | 412,100.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `2.39%` | `97.61%` | `0.02` | 103,360.00 USD |
| `15M` | `HTX` | `57.69%` | `42.31%` | `1.36` | 38,110.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `77.35%` | `22.65%` | `3.42` | 181,280.00 USD |
| `15M` | `Aster` | `34.14%` | `65.86%` | `0.52` | 864,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `24.11%` | `75.89%` | `0.32` | 936,020.00 USD |
| `15M` | `Whale Positions` | `50.05%` | `49.95%` | `1.00` | 41,680,000.00 USD |
| `15M` | `Global Accounts` | `46.57%` | `53.43%` | `0.87` | 66,250,000.00 USD |
| `1H` | `DOGE` | `49.67%` | `50.33%` | `0.99` | 242,710,000.00 USD |
| `1H` | `Binance` | `52.15%` | `47.85%` | `1.09` | 147,900,000.00 USD |
| `1H` | `OKX` | `51.91%` | `48.09%` | `1.08` | 21,400,000.00 USD |
| `1H` | `Bybit` | `39.12%` | `60.88%` | `0.64` | 27,970,000.00 USD |
| `1H` | `KuCoin` | `47.84%` | `52.16%` | `0.92` | 542,490.00 USD |
| `1H` | `Gate` | `47.22%` | `52.78%` | `0.89` | 3,700,000.00 USD |
| `1H` | `Bitget` | `44.2%` | `55.8%` | `0.79` | 3,190,000.00 USD |
| `1H` | `BingX` | `53.96%` | `46.04%` | `1.17` | 2,650,000.00 USD |
| `1H` | `MEXC` | `57.53%` | `42.47%` | `1.35` | 2,100,000.00 USD |
| `1H` | `Bitunix` | `53.92%` | `46.08%` | `1.17` | 6,250,000.00 USD |
| `1H` | `Hyperliquid` | `43.23%` | `56.77%` | `0.76` | 15,940,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 1,310,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `10.72%` | `89.28%` | `0.12` | 621,700.00 USD |
| `1H` | `HTX` | `53.47%` | `46.53%` | `1.15` | 158,110.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `65.84%` | `34.16%` | `1.93` | 646,720.00 USD |
| `1H` | `Aster` | `48.99%` | `51.01%` | `0.96` | 4,310,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.72%` | `57.28%` | `0.75` | 4,000,000.00 USD |
| `1H` | `Whale Positions` | `52.15%` | `47.85%` | `1.09` | 147,900,000.00 USD |
| `1H` | `Global Accounts` | `49.67%` | `50.33%` | `0.99` | 242,710,000.00 USD |
| `4H` | `DOGE` | `48.74%` | `51.26%` | `0.95` | 2,430,000,000.00 USD |
| `4H` | `Binance` | `48.91%` | `51.09%` | `0.96` | 1,400,000,000.00 USD |
| `4H` | `OKX` | `50.54%` | `49.46%` | `1.02` | 157,990,000.00 USD |
| `4H` | `Bybit` | `47.75%` | `52.25%` | `0.91` | 282,630,000.00 USD |
| `4H` | `KuCoin` | `45.68%` | `54.32%` | `0.84` | 13,580,000.00 USD |
| `4H` | `Gate` | `48.71%` | `51.29%` | `0.95` | 54,730,000.00 USD |
| `4H` | `Bitget` | `46.47%` | `53.53%` | `0.87` | 62,360,000.00 USD |
| `4H` | `BingX` | `48.84%` | `51.16%` | `0.95` | 23,790,000.00 USD |
| `4H` | `MEXC` | `48.41%` | `51.59%` | `0.94` | 32,470,000.00 USD |
| `4H` | `Bitunix` | `48.86%` | `51.14%` | `0.96` | 57,790,000.00 USD |
| `4H` | `Hyperliquid` | `48.3%` | `51.7%` | `0.93` | 239,430,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.11%` | `49.89%` | `1.00` | 15,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `37.65%` | `62.35%` | `0.60` | 4,230,000.00 USD |
| `4H` | `HTX` | `37.29%` | `62.71%` | `0.59` | 3,250,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.76%` | `50.24%` | `0.99` | 8,660,000.00 USD |
| `4H` | `Aster` | `49.82%` | `50.18%` | `0.99` | 50,400,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.37%` | `49.63%` | `1.01` | 27,320,000.00 USD |
| `4H` | `Whale Positions` | `48.91%` | `51.09%` | `0.96` | 1,400,000,000.00 USD |
| `4H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 2,430,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0757` | `0.0754` | `0.0757` | `0.0762` | `0.0742` | 60,549,155.39 USD | 27,187,435.52 USD | 33,361,719.87 USD | -6,174,284.35 USD | `-10.20%` | `1B / 21S` |
| `0:00 UTC` | `0.0753` | `0.0755` | `0.0753` | `0.0761` | `0.0749` | 29,212,143.58 USD | 15,504,806.30 USD | 13,707,337.28 USD | 1,797,469.02 USD | `+6.15%` | `8B / 1S` |
| `5:00 UTC` | `0.0766` | `0.0764` | `0.0766` | `0.0769` | `0.0759` | 15,471,814.11 USD | 7,521,434.27 USD | 7,950,379.84 USD | -428,945.57 USD | `-2.77%` | `7B / 6S` |
| `0:00 UTC` | `0.0768` | `0.0767` | `0.0768` | `0.0770` | `0.0762` | 6,979,124.86 USD | 3,191,852.39 USD | 3,787,272.47 USD | -595,420.08 USD | `-8.53%` | `11B / 14S` |
| `5:00 UTC` | `0.0761` | `0.0762` | `0.0761` | `0.0765` | `0.0760` | 7,159,591.43 USD | 3,474,483.11 USD | 3,685,108.33 USD | -210,625.22 USD | `-2.94%` | `4B / 7S` |
| `0:00 UTC` | `0.0760` | `0.0760` | `0.0760` | `0.0764` | `0.0754` | 12,740,089.09 USD | 6,794,980.63 USD | 5,945,108.46 USD | 849,872.18 USD | `+6.67%` | `14B / 1S` |
| `5:00 UTC` | `0.0759` | `0.0760` | `0.0759` | `0.0764` | `0.0757` | 13,833,535.23 USD | 9,937,462.08 USD | 3,896,073.14 USD | 6,041,388.94 USD | `+43.67%` | `12B / 6S` |
| `0:00 UTC` | `0.0765` | `0.0764` | `0.0765` | `0.0766` | `0.0760` | 17,208,343.82 USD | 5,481,216.49 USD | 11,727,127.34 USD | -6,245,910.85 USD | `-36.30%` | `10B / 12S` |
| `5:00 UTC` | `0.0761` | `0.0761` | `0.0761` | `0.0763` | `0.0758` | 6,688,766.39 USD | 3,170,955.24 USD | 3,517,811.15 USD | -346,855.91 USD | `-5.19%` | `4B / 8S` |
| `0:00 UTC` | `0.0759` | `0.0760` | `0.0759` | `0.0762` | `0.0758` | 1,135,069.05 USD | 387,598.55 USD | 747,470.50 USD | -359,871.95 USD | `-31.70%` | `4B / 16S` |

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
| `5m` | -91,940.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 104,340.00 USD | 110,530.00 USD | **`ACCUMULATION`** |
| `30m` | -723,030.00 USD | -6,230,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -552,200.00 USD | 2,050,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,610,000.00 USD | 3,940,000.00 USD | **`ACCUMULATION`** |
| `4h` | -11,050,000.00 USD | -33,110,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,870,000.00 USD | -34,560,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,700,000.00 USD | -31,290,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,740,000.00 USD | -32,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -14,470,000.00 USD | -52,380,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -51,810,000.00 USD | -160,600,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -279,650,000.00 USD | -779,310,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-91.94K` | 15m=`+104.34K` | 1h=`-552.20K` | 24h=`-14.47M`
* Futures Capital Netflows: 5m=`-1.16M` | 15m=`+110.53K` | 1h=`+2.05M` | 24h=`-52.38M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0747` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0707` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0852`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0753` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0793` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0648`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0762`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
