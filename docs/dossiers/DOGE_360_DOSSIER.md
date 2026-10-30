# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 08:21:40 IST` (`2026-10-30 02:51:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0740` | **Live Ask Quote**: `0.0761` | **Mid Price**: `0.0751`
- **Spread Points**: `21.00` | **Spread BPS**: `279.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0729` | VWAP Z-Score: `+1.67` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000838` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `44.21` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0745` | Lower -3.00σ Band: `0.0712`
  * Upper +2.51σ Band: `0.0743` | Lower -2.51σ Band: `0.0714`
  * Upper +2.01σ Band: `0.0740` | Lower -2.01σ Band: `0.0717`
  * Upper +2.00σ Band: `0.0740` | Lower -2.00σ Band: `0.0717`
  * Upper +1.28σ Band: `0.0736` | Lower -1.28σ Band: `0.0721`
  * Upper +1.00σ Band: `0.0734` | Lower -1.00σ Band: `0.0723`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0733` | EMA-20=`0.0740` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0755` (Slope: `+0.0000`) | EMA-100=`0.0764`
  * Institutional Anchors: EMA-144=`0.0767` | EMA-200=`0.0769` (Slope: `-0.5982`) | EMA-233=`0.0770`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `-0.88%`)
  * Point of Control (POC) = `0.0749` (Distance: `+0.22%`)
  * Value Area Low (VAL) = `0.0731` (Distance: `+2.72%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0788` | Weekly POC=`0.0762` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0754` | Low=`0.0747`
  * New York Session (13:00-21:00 UTC): High=`0.0755` | Low=`0.0746`
  * Initial Balance (First Hour): IB High=`0.0753` | IB Low=`0.0748`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0747` - `0.0754`
  * Optimal Trade Entry (OTE 0.705): `0.0752`
  * Structural Invalidation Anchor (0.786): `0.0757`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0749` | `0.0750` | `0.0748` | `0.0748` | `28,253,963` | 2,117,880.07 USD | 31,836.56 USD | `+1.50%` | -36,617,558.67 USD | `+0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0748` | `0.0751` | `0.0748` | `0.0751` | `42,421,225` | 3,182,499.06 USD | 905,818.29 USD | `+28.46%` | -35,711,740.38 USD | `+1.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0751` | `0.0752` | `0.0751` | `0.0752` | `13,674,108` | 1,027,724.55 USD | 91,025.83 USD | `+8.86%` | -35,620,714.55 USD | `+0.10` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.0740` | `0.0743` | `0.0736` | `0.0743` | `83,396,176` | 6,164,268.63 USD | -288,133.08 USD | `-4.67%` | -37,344,170.15 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0743` | `0.0751` | `0.0743` | `0.0750` | `86,826,832` | 6,484,284.24 USD | 694,774.91 USD | `+10.71%` | -36,649,395.23 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.0749` | `0.0752` | `0.0748` | `0.0752` | `84,401,455` | 6,332,023.94 USD | 1,032,369.18 USD | `+16.30%` | -35,617,026.05 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0752` | `0.0755` | `0.0722` | `0.0743` | `1,126,246,051` | 82,965,237.76 USD | -7,583,601.19 USD | `-9.14%` | -37,201,996.32 USD | `-1.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0743` | `0.0746` | `0.0733` | `0.0740` | `386,101,231` | 28,593,595.00 USD | -713,201.79 USD | `-2.49%` | -37,915,198.11 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0740` | `0.0752` | `0.0736` | `0.0752` | `254,572,304` | 18,976,656.55 USD | 1,435,322.52 USD | `+7.56%` | -36,479,875.59 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -5,801,361.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -28,841,087.48 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0755` | `0.0722` | `0.0752` | `1,766,971,745` | 130,539,409.56 USD | -6,857,791.97 USD | `-5.25%` | -35,698,879.44 USD | `-0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -7,382,443.88 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -2,793,692.45 USD | `+1.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -5,801,361.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -28,841,087.48 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0755` | `0.0722` | `0.0752` | `1,766,971,745` | 130,539,409.56 USD | -6,857,791.97 USD | `-5.25%` | -35,698,879.44 USD | `-0.11` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0751`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0751` | `16274.0000` | 1,222.97 USD | 9,301.38 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0751` | `16273.0000` | 1,222.83 USD | 10,524.22 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0751` | `596582.0000` | 44,827.17 USD | 55,351.39 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0751` | `159128.0000` | 11,956.72 USD | 67,308.11 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0751` | `45610.0000` | 3,427.00 USD | 70,735.10 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0751` | `454697.0000` | 34,163.20 USD | 104,898.31 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0751` | `99688.0000` | 7,489.86 USD | 112,388.17 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `0.0751` | `10000.0000` | 751.32 USD | 113,139.49 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0751` | `16275.0000` | 1,222.76 USD | 114,362.24 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0751` | `1034.0000` | 77.68 USD | 114,439.93 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0751` | `10000.0000` | 751.28 USD | 115,191.21 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0751` | `24629.0000` | 1,850.30 USD | 117,041.51 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0751` | `142879.0000` | 10,733.93 USD | 127,775.44 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0751` | `16274.0000` | 1,222.55 USD | 128,997.99 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0751` | `76377.0000` | 5,737.52 USD | 134,735.51 USD | `3 orders` | `-0.07%` | `-` |
| `ASK` | `0.0752` | `25107.0000` | 1,887.97 USD | 124,614.46 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0752` | `454327.0000` | 34,163.57 USD | 122,726.49 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0752` | `5080.0000` | 381.99 USD | 88,562.91 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0752` | `157432.0000` | 11,837.94 USD | 88,180.92 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0752` | `56700.0000` | 4,263.44 USD | 76,342.98 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0752` | `555833.0000` | 41,794.19 USD | 72,079.54 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0752` | `36219.0000` | 2,723.34 USD | 30,285.34 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `19947.0000` | 1,499.81 USD | 27,562.00 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `36221.0000` | 2,723.42 USD | 26,062.19 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `23835.0000` | 1,792.11 USD | 23,338.76 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `29950.0000` | 2,251.85 USD | 21,546.66 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `19950.0000` | 1,499.96 USD | 19,294.81 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `19950.0000` | 1,499.94 USD | 17,794.85 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0752` | `19950.0000` | 1,499.92 USD | 16,294.91 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0752` | `19950.0000` | 1,499.90 USD | 14,794.99 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0752` | `19950.0000` | 1,499.88 USD | 13,295.08 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0752` | `19950.0000` | 1,499.86 USD | 11,795.20 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0752` | `39799.0000` | 2,992.09 USD | 10,295.34 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0752` | `3000.0000` | 225.53 USD | 7,303.25 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `0.0752` | `94150.0000` | 7,077.73 USD | 7,077.73 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0752` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0752` | `19179.0000` | 1,441.70 USD | 1,441.70 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0752` | `40000.0000` | 3,006.60 USD | 4,448.30 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0752` | `16272.0000` | 1,223.05 USD | 5,671.36 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0752` | `16272.0000` | 1,222.95 USD | 6,894.31 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0752` | `15756.0000` | 1,184.09 USD | 8,078.41 USD | `2 orders` | `-0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `308` | `0xb83d...6e36` | `SHORT` | 7,717,947.10 USD | `102,645,925.00` | `0.0946` | `0.0752` | `1.38` | 1,989,394.55 USD | `+25.78%` | `3X Cross` |
| `314` | `0xc63a...a3cd` | `LONG` | 7,518,900.00 USD | `100,000,000.00` | `0.0856` | `0.0752` | `0.000000` | -1,045,921.96 USD | `-13.91%` | `10X Cross` |
| `316` | `0x610b...b613` | `LONG` | 7,418,728.42 USD | `98,666,424.00` | `0.0872` | `0.0752` | `0.0615` | -1,181,453.48 USD | `-15.93%` | `5X Cross` |
| `606` | `0x5b5d...c060` | `SHORT` | 3,720,322.63 USD | `49,478,955.00` | `0.0946` | `0.0752` | `3.36` | 961,193.98 USD | `+25.84%` | `3X Cross` |
| `641` | `0xca49...53c8` | `SHORT` | 3,499,960.66 USD | `46,542,649.00` | `0.0929` | `0.0752` | `0.4032` | 826,084.02 USD | `+23.60%` | `10X Cross` |
| `649` | `0x45d2...4029` | `SHORT` | 3,415,989.77 USD | `45,426,000.00` | `0.0954` | `0.0752` | `1.00` | 919,639.45 USD | `+26.92%` | `10X Cross` |
| `765` | `0xecb6...2b00` | `SHORT` | 2,983,008.21 USD | `39,672,938.00` | `0.0791` | `0.0752` | `0.7711` | 157,051.89 USD | `+5.26%` | `10X Cross` |
| `1183` | `0x458d...ab3b` | `LONG` | 1,838,701.00 USD | `24,454,063.00` | `0.1002` | `0.0752` | `0.0714` | -612,220.91 USD | `-33.30%` | `3X Isolated` |
| `1199` | `0xeadc...9d55` | `LONG` | 1,828,428.31 USD | `24,317,440.00` | `0.0926` | `0.0752` | `0.000000` | -423,166.26 USD | `-23.14%` | `10X Cross` |
| `1337` | `0xf48f...10fe` | `LONG` | 1,610,907.93 USD | `21,424,497.00` | `0.0968` | `0.0752` | `0.0493` | -463,396.68 USD | `-28.77%` | `4X Cross` |
| `1368` | `0x9946...0852` | `SHORT` | 1,565,468.54 USD | `20,821,554.00` | `0.0871` | `0.0752` | `0.1571` | 247,373.27 USD | `+15.80%` | `10X Cross` |
| `1532` | `0x9aa5...58af` | `SHORT` | 1,397,635.19 USD | `18,586,563.00` | `0.0907` | `0.0752` | `0.5701` | 287,580.49 USD | `+20.58%` | `10X Cross` |
| `1562` | `0xcac1...26b3` | `SHORT` | 1,362,938.60 USD | `18,126,835.00` | `0.0943` | `0.0752` | `0.5585` | 346,520.60 USD | `+25.42%` | `10X Cross` |
| `1591` | `0x0d6a...ca57` | `LONG` | 1,325,333.15 USD | `17,626,455.00` | `0.0875` | `0.0752` | `0.0626` | -216,771.81 USD | `-16.36%` | `3X Isolated` |
| `1648` | `0x4808...a82c` | `LONG` | 1,265,308.07 USD | `16,828,143.00` | `0.0883` | `0.0752` | `0.0631` | -221,164.91 USD | `-17.48%` | `3X Cross` |
| `1783` | `0x31ef...f715` | `LONG` | 1,145,151.37 USD | `15,230,102.00` | `0.0936` | `0.0752` | `0.0668` | -280,544.56 USD | `-24.50%` | `3X Isolated` |
| `1804` | `0xbfc7...80b4` | `SHORT` | 1,129,443.92 USD | `15,020,000.00` | `0.0920` | `0.0752` | `0.1997` | 252,955.37 USD | `+22.40%` | `10X Cross` |
| `1890` | `0x7cee...fc93` | `SHORT` | 1,053,742.73 USD | `14,013,468.00` | `0.0863` | `0.0752` | `0.2728` | 155,134.64 USD | `+14.72%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 9,999.94 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.00K USD at 0.0799 USD [API] | `2026-10-28 20:24:37` |
| `ANNOUNCEMENT` | `INFO` | `0.0803` | 7,134.96 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.13K USD at 0.0803 USD [API] | `2026-10-28 20:59:18` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 8,202.51 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 8.20K USD at 0.0800 USD [API] | `2026-10-28 22:02:56` |
| `ANNOUNCEMENT` | `INFO` | `0.0801` | 12,172.83 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 12.17K USD at 0.0801 USD [API] | `2026-10-28 22:02:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 8,348.29 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 8.35K USD at 0.0799 USD [API] | `2026-10-28 22:51:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0798` | 5,249.24 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.25K USD at 0.0798 USD [API] | `2026-10-28 23:08:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.07%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--1.98%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.07%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--1.98%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.07%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--1.98%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.07%`) | Long MP=`0.0745` (Vol: 886,200.00 USD, Dist: `--1.98%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 3,610.00 USD | 16,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0180` | 7,850.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0185` | 221.12 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0190` | 1,120.00 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0196` | 763.41 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 9,930.00 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0213` | 2,780.00 USD | 16,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0214` | 683.20 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0221` | 13,290.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0222` | 1,330.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0227` | 2,180.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0230` | 5,740.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 369.37 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0255` | 157.94 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0257` | 4,080.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0286` | 299.22 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0293` | 585.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 2,430.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0314` | 2,370.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0324` | 3,610.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 943.11 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0333` | 178.22 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 503.25 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 30,250.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 1,390.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0353` | 13,770.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 330.01 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 315.94 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 7,000.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 5,060.00 USD | 16,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 1,280.00 USD | 16,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0382` | 4,170.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 37,190.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 2,180.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0398` | 186.83 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 317.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0401` | 1,300.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 297.75 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 57,130.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 122.55 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0410` | 1,500.00 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0413` | 579.03 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,970.00 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0416` | 6,380.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 12,190.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,920.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 10,640.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 10,350.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 116,120.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 7,860.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,010.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 463.34 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,330.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0486` | 1,080.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 9,650.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,920.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 169.32 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 7,430.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 54,350.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 1,750.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 106,640.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 931.86 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 933.66 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 5,350.00 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 5,210.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 315,250.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 184,180.00 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0530` | 407.21 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 12,030.00 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,350.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 1,890.00 USD | 15,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 15,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 1,590.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 15,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 4,930.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 2,510.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 3,920.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 15,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 1,190,000.00 USD | 15,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 175.44 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 83,000.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 38,870.00 USD | 14,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 2,170.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 567.50 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 13,110.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,700.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 2,470.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 137.54 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 354,280.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 441.75 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 582.13 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 1,330.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 6,120.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,940.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 31,410.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 4,560.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 1,130.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 12,320.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 830.97 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 930.23 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,970.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 6,690.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 5,110.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 958.56 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0619` | 90,950.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 13,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 13,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 29,020.00 USD | 13,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 6,160,000.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,120,000.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 870.40 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,810.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,260.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 2,490.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 4,770.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 5,600.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 24,110.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 150.01 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 15,070.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 11,930.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,380.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 163,360.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 112,510.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 73,340.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0660` | 525.96 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 7,050.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 19,830.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 2,730.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,190.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,370.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 329.58 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,610.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 11,770,000.00 USD | 11,770,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 37,110.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 11,640,000.00 USD | 11,640,000.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 134,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 117.29 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 11,500,000.00 USD | 11,500,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 20,340.00 USD | 723.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 11,430,000.00 USD | 11,430,000.00 USD | 24,150.00 USD | 15,070.00 USD | 584.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 130,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 11,390,000.00 USD | 11,390,000.00 USD | 41,510.00 USD | 12,720.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 6,270.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 11,320,000.00 USD | 11,320,000.00 USD | 41,080.00 USD | 1,410.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 595.81 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 11,260,000.00 USD | 11,260,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 870.75 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 11,200,000.00 USD | 11,200,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,970.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 4,610.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 11,200,000.00 USD | 11,200,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0696` | 11,620.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 11,200,000.00 USD | 11,200,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 4,720.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 11,140,000.00 USD | 11,140,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 11,080,000.00 USD | 11,080,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,590.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 10,950,000.00 USD | 10,950,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 10,810,000.00 USD | 10,810,000.00 USD | 35,400.00 USD | 18,030.00 USD | 29,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 10,750.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 10,720,000.00 USD | 10,720,000.00 USD | 78,740.00 USD | 36,780.00 USD | 164.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 10,610,000.00 USD | 10,610,000.00 USD | 87,540.00 USD | 31,470.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 44,080.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 10,450,000.00 USD | 10,450,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 10,360,000.00 USD | 10,360,000.00 USD | 41,490.00 USD | 24,910.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 10,260,000.00 USD | 10,260,000.00 USD | 36,930.00 USD | 29,080.00 USD | 26,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 423.90 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 10,170,000.00 USD | 10,170,000.00 USD | 54,240.00 USD | 21,680.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 10,070,000.00 USD | 10,070,000.00 USD | 25,410.00 USD | 16,310.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0708` | 487.73 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0709` | 10,000,000.00 USD | 10,000,000.00 USD | 36,740.00 USD | 37,120.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 351.63 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 9,910,000.00 USD | 9,910,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0711` | 9,840,000.00 USD | 9,840,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,920.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 9,770,000.00 USD | 9,770,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 9,700,000.00 USD | 9,700,000.00 USD | 35,120.00 USD | 58,130.00 USD | 67,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 9,540,000.00 USD | 9,540,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 213.78 USD | 397,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 9,440,000.00 USD | 9,440,000.00 USD | 34,440.00 USD | 8,830.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 397,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 9,360,000.00 USD | 9,360,000.00 USD | 24,840.00 USD | 31,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,170.00 USD | 389,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 9,300,000.00 USD | 9,300,000.00 USD | 10,910.00 USD | 7,710.00 USD | 21,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,270.00 USD | 387,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 9,260,000.00 USD | 9,260,000.00 USD | 67,080.00 USD | 31,390.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,070.00 USD | 365,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 9,130,000.00 USD | 9,130,000.00 USD | 10,150.00 USD | 0.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 364,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 9,120,000.00 USD | 9,120,000.00 USD | 31,160.00 USD | 29,440.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,160.00 USD | 362,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 9,030,000.00 USD | 9,030,000.00 USD | 136,510.00 USD | 76,220.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 350,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,800,000.00 USD | 8,800,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 322,050.00 USD | 328,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,720,000.00 USD | 8,720,000.00 USD | 54,790.00 USD | 162,040.00 USD | 153,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 626.77 USD | 6,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.0740` | 5,420.00 USD | 5,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.0767` | 28,530.00 USD | 28,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,930,000.00 USD | 2,930,000.00 USD | 351,760.00 USD | 0.00 USD | 514,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 3,600,000.00 USD | 3,600,000.00 USD | 181,440.00 USD | 341,350.00 USD | 148,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 4,220,000.00 USD | 4,220,000.00 USD | 272,760.00 USD | 93,300.00 USD | 253,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 4,880,000.00 USD | 4,880,000.00 USD | 216,410.00 USD | 232,340.00 USD | 212,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 5,850,000.00 USD | 5,850,000.00 USD | 286,340.00 USD | 0.00 USD | 685,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 6,240,000.00 USD | 6,240,000.00 USD | 65,160.00 USD | 169,730.00 USD | 149,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0774` | 3,490.00 USD | 32,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 164,510.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 6,690,000.00 USD | 6,690,000.00 USD | 155,740.00 USD | 109,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 32,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 7,070,000.00 USD | 7,070,000.00 USD | 190,100.00 USD | 110,600.00 USD | 86,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 205,390.00 USD | 264,690.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0777` | 2,110.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0778` | 8,140,000.00 USD | 8,140,000.00 USD | 16,790.00 USD | 202,930.00 USD | 295,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 85,950.00 USD | 140,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 8,470,000.00 USD | 8,470,000.00 USD | 69,890.00 USD | 31,980.00 USD | 253.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 8,650,000.00 USD | 8,650,000.00 USD | 113,060.00 USD | 68,670.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 8,660,000.00 USD | 8,660,000.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 9,000,000.00 USD | 9,000,000.00 USD | 8,010.00 USD | 184,740.00 USD | 145,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 9,390,000.00 USD | 9,390,000.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 9,740,000.00 USD | 9,740,000.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 10,280,000.00 USD | 10,280,000.00 USD | 191,180.00 USD | 117,040.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 11,230,000.00 USD | 11,230,000.00 USD | 298,820.00 USD | 307,550.00 USD | 344,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 34,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 11,560,000.00 USD | 11,560,000.00 USD | 75,490.00 USD | 181,170.00 USD | 75,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 12,090,000.00 USD | 12,090,000.00 USD | 234,900.00 USD | 192,150.00 USD | 96,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 12,250,000.00 USD | 12,250,000.00 USD | 102,120.00 USD | 57,780.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 12,590,000.00 USD | 12,590,000.00 USD | 152,950.00 USD | 95,070.00 USD | 95,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 12,750,000.00 USD | 12,750,000.00 USD | 104,950.00 USD | 18,870.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 12,930,000.00 USD | 12,930,000.00 USD | 92,580.00 USD | 41,370.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 13,010,000.00 USD | 13,010,000.00 USD | 10,150.00 USD | 0.00 USD | 73,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 13,200,000.00 USD | 13,200,000.00 USD | 174,010.00 USD | 0.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 13,730,000.00 USD | 13,730,000.00 USD | 191,110.00 USD | 89,760.00 USD | 242,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 13,950,000.00 USD | 13,950,000.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 14,520,000.00 USD | 14,520,000.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 14,630,000.00 USD | 14,630,000.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 14,640,000.00 USD | 14,640,000.00 USD | 6,300.00 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 14,650,000.00 USD | 14,650,000.00 USD | 7,730.00 USD | 1,770.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0803` | 216.84 USD | 34,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0803` | 14,700,000.00 USD | 14,700,000.00 USD | 9,970.00 USD | 0.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 217.11 USD | 34,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0804` | 14,720,000.00 USD | 14,720,000.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 14,860,000.00 USD | 14,860,000.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 35,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 22,460,000.00 USD | 22,460,000.00 USD | 174,640.00 USD | 312,480.00 USD | 128,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 23,140,000.00 USD | 23,140,000.00 USD | 136,010.00 USD | 202,840.00 USD | 344,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 23,600,000.00 USD | 23,600,000.00 USD | 210,590.00 USD | 79,630.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 24,190,000.00 USD | 24,190,000.00 USD | 262,170.00 USD | 169,200.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 24,540,000.00 USD | 24,540,000.00 USD | 270,850.00 USD | 75,420.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 265.58 USD | 35,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 39,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 27,340,000.00 USD | 27,340,000.00 USD | 171,130.00 USD | 66,230.00 USD | 80,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 39,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 27,680,000.00 USD | 27,680,000.00 USD | 119,590.00 USD | 55,260.00 USD | 165,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 28,030,000.00 USD | 28,030,000.00 USD | 127,020.00 USD | 94,190.00 USD | 126,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 104,680.00 USD | 176,580.00 USD | 65,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 48,890.00 USD | 63,220.00 USD | 144,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 28,850,000.00 USD | 28,850,000.00 USD | 129,000.00 USD | 30,430.00 USD | 51,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 41,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.0846` | 29,580,000.00 USD | 29,580,000.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0847` | 29,590,000.00 USD | 29,590,000.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 1,150.00 USD | 42,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 42,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,450.00 USD | 47,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 47,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 47,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 48,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 48,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 48,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 55,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 56,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 61,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0916` | 133.66 USD | 61,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 62,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 62,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 43,950.00 USD | 106,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 131,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0955` | 47,770.00 USD | 179,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 195.26 USD | 179,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 179,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 180,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 180,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0990` | 1,200.00 USD | 181,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0994` | 968.25 USD | 182,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 190,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 193,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 193,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 199,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1066` | 3,300.00 USD | 203,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1067` | 3,120.00 USD | 206,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 206,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 210,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1113` | 1,670.00 USD | 211,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 212,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 212,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1138` | 153.68 USD | 212,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1158` | 131.49 USD | 212,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 213,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1250` | 902.01 USD | 214,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 214,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1285` | 43,990.00 USD | 258,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 258,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 260,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 260,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 334.38 USD | 261,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1366` | 41,500.00 USD | 302,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1381` | 22,410.00 USD | 324,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1388` | 968.20 USD | 325,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1399` | 1,960.00 USD | 327,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 100.35 USD | 327,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 328,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 330,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 330,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 332,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1462` | 6,380.00 USD | 338,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1470` | 4,110.00 USD | 342,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,260.00 USD | 350,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 16,910,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.32%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,910,000.00 USD | 0.00 USD | 3,610.00 USD | `-77.78%` | `219,418.00` |
| `Live` | `Long` | `0.0165` | 16,900,000.00 USD | 0.00 USD | 5,290.00 USD | `-77.64%` | `319,394.00` |
| `Live` | `Long` | `0.0180` | 16,900,000.00 USD | 0.00 USD | 7,850.00 USD | `-75.75%` | `437,390.00` |
| `Live` | `Long` | `0.0185` | 16,890,000.00 USD | 0.00 USD | 221.12 USD | `-75.08%` | `11,985.00` |
| `Live` | `Long` | `0.0190` | 16,890,000.00 USD | 0.00 USD | 1,120.00 USD | `-74.40%` | `59,317.00` |
| `Live` | `Long` | `0.0196` | 16,890,000.00 USD | 0.00 USD | 763.41 USD | `-73.59%` | `39,049.00` |
| `Live` | `Long` | `0.0198` | 16,890,000.00 USD | 0.00 USD | 9,930.00 USD | `-73.18%` | `500,000.00` |
| `Live` | `Long` | `0.0213` | 16,880,000.00 USD | 0.00 USD | 2,780.00 USD | `-71.29%` | `130,804.00` |
| `Live` | `Long` | `0.0214` | 16,870,000.00 USD | 0.00 USD | 683.20 USD | `-71.16%` | `32,000.00` |
| `Live` | `Long` | `0.0215` | 16,870,000.00 USD | 0.00 USD | 18,970.00 USD | `-70.89%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,850,000.00 USD | 0.00 USD | 541.25 USD | `-70.75%` | `25,000.00` |
| `Live` | `Long` | `0.0221` | 16,850,000.00 USD | 0.00 USD | 13,290.00 USD | `-70.08%` | `600,000.00` |
| `Live` | `Long` | `0.0222` | 16,840,000.00 USD | 0.00 USD | 1,330.00 USD | `-69.94%` | `60,000.00` |
| `Live` | `Long` | `0.0227` | 16,840,000.00 USD | 0.00 USD | 2,180.00 USD | `-69.27%` | `95,954.00` |
| `Live` | `Long` | `0.0230` | 16,840,000.00 USD | 0.00 USD | 5,740.00 USD | `-69.00%` | `250,000.00` |
| `Live` | `Long` | `0.0244` | 16,830,000.00 USD | 0.00 USD | 369.37 USD | `-67.11%` | `15,169.00` |
| `Live` | `Long` | `0.0255` | 16,830,000.00 USD | 0.00 USD | 157.94 USD | `-65.62%` | `6,206.00` |
| `Live` | `Long` | `0.0257` | 16,830,000.00 USD | 0.00 USD | 4,080.00 USD | `-65.21%` | `158,606.00` |
| `Live` | `Long` | `0.0279` | 16,830,000.00 USD | 0.00 USD | 1,730.00 USD | `-62.24%` | `61,775.00` |
| `Live` | `Long` | `0.0286` | 16,830,000.00 USD | 0.00 USD | 299.22 USD | `-61.30%` | `10,444.00` |
| `Live` | `Long` | `0.0293` | 16,830,000.00 USD | 0.00 USD | 585.00 USD | `-60.49%` | `20,000.00` |
| `Live` | `Long` | `0.0306` | 16,820,000.00 USD | 0.00 USD | 2,430.00 USD | `-58.73%` | `79,510.00` |
| `Live` | `Long` | `0.0314` | 16,820,000.00 USD | 0.00 USD | 2,370.00 USD | `-57.65%` | `75,693.00` |
| `Live` | `Long` | `0.0324` | 16,820,000.00 USD | 0.00 USD | 3,610.00 USD | `-56.16%` | `111,254.00` |
| `Live` | `Long` | `0.0331` | 16,820,000.00 USD | 0.00 USD | 943.11 USD | `-55.35%` | `28,536.00` |
| `Live` | `Long` | `0.0333` | 16,820,000.00 USD | 0.00 USD | 178.22 USD | `-54.95%` | `5,344.00` |
| `Live` | `Long` | `0.0336` | 16,810,000.00 USD | 0.00 USD | 503.25 USD | `-54.68%` | `15,000.00` |
| `Live` | `Long` | `0.0336` | 16,810,000.00 USD | 0.00 USD | 393.23 USD | `-54.54%` | `11,686.00` |
| `Live` | `Long` | `0.0338` | 16,810,000.00 USD | 0.00 USD | 30,250.00 USD | `-54.27%` | `893,720.00` |
| `Live` | `Long` | `0.0345` | 16,780,000.00 USD | 0.00 USD | 1,390.00 USD | `-53.46%` | `40,263.00` |
| `Live` | `Long` | `0.0353` | 16,780,000.00 USD | 0.00 USD | 13,770.00 USD | `-52.25%` | `389,633.00` |
| `Live` | `Long` | `0.0355` | 16,770,000.00 USD | 0.00 USD | 330.01 USD | `-51.98%` | `9,283.00` |
| `Live` | `Long` | `0.0358` | 16,770,000.00 USD | 0.00 USD | 214.53 USD | `-51.57%` | `5,984.00` |
| `Live` | `Long` | `0.0365` | 16,770,000.00 USD | 0.00 USD | 315.94 USD | `-50.62%` | `8,644.00` |
| `Live` | `Long` | `0.0372` | 16,770,000.00 USD | 0.00 USD | 7,000.00 USD | `-49.68%` | `187,979.00` |
| `Live` | `Long` | `0.0377` | 16,760,000.00 USD | 0.00 USD | 5,060.00 USD | `-49.14%` | `134,443.00` |
| `Live` | `Long` | `0.0379` | 16,760,000.00 USD | 0.00 USD | 1,280.00 USD | `-48.87%` | `33,816.00` |
| `Live` | `Long` | `0.0381` | 16,750,000.00 USD | 0.00 USD | 1,600.00 USD | `-48.60%` | `41,929.00` |
| `Live` | `Long` | `0.0382` | 16,750,000.00 USD | 0.00 USD | 4,170.00 USD | `-48.46%` | `109,191.00` |
| `Live` | `Long` | `0.0386` | 16,750,000.00 USD | 0.00 USD | 121.74 USD | `-47.92%` | `3,158.00` |
| `Live` | `Long` | `0.0391` | 16,750,000.00 USD | 0.00 USD | 37,190.00 USD | `-47.11%` | `950,000.00` |
| `Live` | `Long` | `0.0393` | 16,710,000.00 USD | 0.00 USD | 2,180.00 USD | `-46.98%` | `55,633.00` |
| `Live` | `Long` | `0.0398` | 16,710,000.00 USD | 0.00 USD | 186.83 USD | `-46.30%` | `4,700.00` |
| `Live` | `Long` | `0.0399` | 16,710,000.00 USD | 0.00 USD | 317.00 USD | `-46.03%` | `7,935.00` |
| `Live` | `Long` | `0.0401` | 16,710,000.00 USD | 0.00 USD | 1,300.00 USD | `-45.76%` | `32,298.00` |
| `Live` | `Long` | `0.0404` | 16,710,000.00 USD | 0.00 USD | 297.75 USD | `-45.36%` | `7,361.00` |
| `Live` | `Long` | `0.0406` | 16,710,000.00 USD | 0.00 USD | 57,130.00 USD | `-45.09%` | `1,405,488.00` |
| `Live` | `Long` | `0.0408` | 16,650,000.00 USD | 0.00 USD | 419.28 USD | `-44.95%` | `10,289.00` |
| `Live` | `Long` | `0.0408` | 16,650,000.00 USD | 0.00 USD | 122.55 USD | `-44.82%` | `3,000.00` |
| `Live` | `Long` | `0.0410` | 16,650,000.00 USD | 0.00 USD | 1,500.00 USD | `-44.68%` | `36,653.00` |
| `Live` | `Long` | `0.0413` | 16,650,000.00 USD | 0.00 USD | 579.03 USD | `-44.27%` | `14,037.00` |
| `Live` | `Long` | `0.0415` | 16,650,000.00 USD | 0.00 USD | 1,970.00 USD | `-44.00%` | `47,501.00` |
| `Live` | `Long` | `0.0415` | 16,650,000.00 USD | 0.00 USD | 1,030.00 USD | `-43.87%` | `24,809.00` |
| `Live` | `Long` | `0.0416` | 16,640,000.00 USD | 0.00 USD | 6,380.00 USD | `-43.73%` | `153,201.00` |
| `Live` | `Long` | `0.0420` | 16,640,000.00 USD | 0.00 USD | 266.05 USD | `-43.33%` | `6,342.00` |
| `Live` | `Long` | `0.0420` | 16,640,000.00 USD | 0.00 USD | 12,190.00 USD | `-43.19%` | `290,000.00` |
| `Live` | `Long` | `0.0423` | 16,630,000.00 USD | 0.00 USD | 1,920.00 USD | `-42.92%` | `45,551.00` |
| `Live` | `Long` | `0.0423` | 16,620,000.00 USD | 0.00 USD | 267.52 USD | `-42.79%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,620,000.00 USD | 0.00 USD | 455.06 USD | `-42.65%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,620,000.00 USD | 0.00 USD | 883.34 USD | `-42.52%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,620,000.00 USD | 0.00 USD | 3,620.00 USD | `-42.38%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 16,620,000.00 USD | 0.00 USD | 859.00 USD | `-41.98%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,620,000.00 USD | 0.00 USD | 10,640.00 USD | `-41.57%` | `245,946.00` |
| `Live` | `Long` | `0.0433` | 16,610,000.00 USD | 0.00 USD | 2,450.00 USD | `-41.44%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 16,600,000.00 USD | 0.00 USD | 10,350.00 USD | `-40.90%` | `236,565.00` |
| `Live` | `Long` | `0.0439` | 16,590,000.00 USD | 0.00 USD | 1,610.00 USD | `-40.76%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,590,000.00 USD | 0.00 USD | 750.58 USD | `-40.63%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,590,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.49%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,590,000.00 USD | 0.00 USD | 101,440.00 USD | `-40.09%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,490,000.00 USD | 0.00 USD | 444.76 USD | `-39.68%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,490,000.00 USD | 0.00 USD | 248.63 USD | `-39.55%` | `5,556.00` |
| `Live` | `Long` | `0.0449` | 16,490,000.00 USD | 0.00 USD | 116,120.00 USD | `-39.41%` | `2,589,112.00` |
| `Live` | `Long` | `0.0449` | 16,370,000.00 USD | 0.00 USD | 810.81 USD | `-39.28%` | `18,038.00` |
| `Live` | `Long` | `0.0454` | 16,370,000.00 USD | 0.00 USD | 2,170.00 USD | `-38.60%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 16,370,000.00 USD | 0.00 USD | 32,650.00 USD | `-38.47%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 16,340,000.00 USD | 0.00 USD | 7,860.00 USD | `-38.20%` | `171,773.00` |
| `Live` | `Long` | `0.0459` | 16,330,000.00 USD | 0.00 USD | 689.25 USD | `-37.93%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 16,330,000.00 USD | 0.00 USD | 4,500.00 USD | `-37.79%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 16,320,000.00 USD | 0.00 USD | 114.36 USD | `-37.66%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 16,320,000.00 USD | 0.00 USD | 362.87 USD | `-37.39%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 16,320,000.00 USD | 0.00 USD | 16,780.00 USD | `-37.25%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 16,310,000.00 USD | 0.00 USD | 109.49 USD | `-36.98%` | `2,347.00` |
| `Live` | `Long` | `0.0473` | 16,310,000.00 USD | 0.00 USD | 3,010.00 USD | `-36.17%` | `63,783.00` |
| `Live` | `Long` | `0.0476` | 16,300,000.00 USD | 0.00 USD | 105.02 USD | `-35.63%` | `2,204.00` |
| `Live` | `Long` | `0.0479` | 16,300,000.00 USD | 0.00 USD | 463.34 USD | `-35.22%` | `9,663.00` |
| `Live` | `Long` | `0.0481` | 16,300,000.00 USD | 0.00 USD | 56,440.00 USD | `-35.09%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 16,250,000.00 USD | 0.00 USD | 2,330.00 USD | `-34.95%` | `48,418.00` |
| `Live` | `Long` | `0.0483` | 16,240,000.00 USD | 0.00 USD | 2,280.00 USD | `-34.68%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 16,240,000.00 USD | 0.00 USD | 1,480.00 USD | `-34.55%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 16,240,000.00 USD | 0.00 USD | 1,080.00 USD | `-34.28%` | `22,129.00` |
| `Live` | `Long` | `0.0488` | 16,240,000.00 USD | 0.00 USD | 1,280.00 USD | `-34.01%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 16,240,000.00 USD | 0.00 USD | 9,650.00 USD | `-33.87%` | `197,139.00` |
| `Live` | `Long` | `0.0491` | 16,230,000.00 USD | 0.00 USD | 1,920.00 USD | `-33.74%` | `39,213.00` |
| `Live` | `Long` | `0.0495` | 16,230,000.00 USD | 0.00 USD | 169.32 USD | `-33.20%` | `3,424.00` |
| `Live` | `Long` | `0.0498` | 16,230,000.00 USD | 0.00 USD | 253.82 USD | `-32.79%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 16,230,000.00 USD | 0.00 USD | 501.50 USD | `-32.39%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 16,230,000.00 USD | 0.00 USD | 5,410.00 USD | `-32.12%` | `107,572.00` |
| `Live` | `Long` | `0.0505` | 16,220,000.00 USD | 0.00 USD | 334.89 USD | `-31.85%` | `6,638.00` |
| `Live` | `Long` | `0.0505` | 16,220,000.00 USD | 0.00 USD | 7,430.00 USD | `-31.71%` | `147,037.00` |
| `Live` | `Long` | `0.0507` | 16,210,000.00 USD | 0.00 USD | 1,040.00 USD | `-31.58%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 16,210,000.00 USD | 0.00 USD | 5,350.00 USD | `-31.44%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 16,210,000.00 USD | 0.00 USD | 54,350.00 USD | `-31.17%` | `1,066,805.00` |
| `Live` | `Long` | `0.0510` | 16,150,000.00 USD | 0.00 USD | 1,750.00 USD | `-31.04%` | `34,307.00` |
| `Live` | `Long` | `0.0512` | 16,150,000.00 USD | 0.00 USD | 11,000.00 USD | `-30.90%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 16,140,000.00 USD | 0.00 USD | 1,490.00 USD | `-30.77%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 16,140,000.00 USD | 0.00 USD | 385.13 USD | `-30.63%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 16,140,000.00 USD | 0.00 USD | 106,640.00 USD | `-30.50%` | `2,072,603.00` |
| `Live` | `Long` | `0.0517` | 16,030,000.00 USD | 0.00 USD | 931.86 USD | `-30.09%` | `18,007.00` |
| `Live` | `Long` | `0.0519` | 16,030,000.00 USD | 0.00 USD | 933.66 USD | `-29.96%` | `18,007.00` |
| `Live` | `Long` | `0.0520` | 16,030,000.00 USD | 0.00 USD | 277.72 USD | `-29.82%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 16,030,000.00 USD | 0.00 USD | 5,350.00 USD | `-29.68%` | `102,859.00` |
| `Live` | `Long` | `0.0522` | 16,020,000.00 USD | 0.00 USD | 5,210.00 USD | `-29.55%` | `100,000.00` |
| `Live` | `Long` | `0.0522` | 16,020,000.00 USD | 0.00 USD | 315,250.00 USD | `-29.41%` | `6,033,568.00` |
| `Live` | `Long` | `0.0524` | 15,700,000.00 USD | 0.00 USD | 1,170.00 USD | `-29.14%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 15,700,000.00 USD | 0.00 USD | 5,640.00 USD | `-29.01%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 15,700,000.00 USD | 0.00 USD | 2,110.00 USD | `-28.74%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 15,690,000.00 USD | 0.00 USD | 673.52 USD | `-28.60%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 15,690,000.00 USD | 0.00 USD | 184,180.00 USD | `-28.47%` | `3,478,313.00` |
| `Live` | `Long` | `0.0530` | 15,510,000.00 USD | 0.00 USD | 407.21 USD | `-28.33%` | `7,676.00` |
| `Live` | `Long` | `0.0532` | 15,510,000.00 USD | 0.00 USD | 12,030.00 USD | `-28.20%` | `226,274.00` |
| `Live` | `Long` | `0.0532` | 15,500,000.00 USD | 0.00 USD | 8,350.00 USD | `-28.06%` | `156,769.00` |
| `Live` | `Long` | `0.0534` | 15,490,000.00 USD | 0.00 USD | 1,890.00 USD | `-27.79%` | `35,411.00` |
| `Live` | `Long` | `0.0536` | 15,490,000.00 USD | 0.00 USD | 942.48 USD | `-27.66%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 15,480,000.00 USD | 0.00 USD | 1,590.00 USD | `-27.52%` | `29,631.00` |
| `Live` | `Long` | `0.0539` | 15,480,000.00 USD | 0.00 USD | 5,290.00 USD | `-27.12%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 15,480,000.00 USD | 0.00 USD | 2,290.00 USD | `-26.98%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 15,480,000.00 USD | 0.00 USD | 13,510.00 USD | `-26.85%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 15,460,000.00 USD | 0.00 USD | 96,530.00 USD | `-26.71%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 15,370,000.00 USD | 0.00 USD | 4,930.00 USD | `-26.44%` | `90,564.00` |
| `Live` | `Long` | `0.0546` | 15,360,000.00 USD | 0.00 USD | 2,510.00 USD | `-26.31%` | `46,004.00` |
| `Live` | `Long` | `0.0546` | 15,360,000.00 USD | 0.00 USD | 1,420.00 USD | `-26.17%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 15,360,000.00 USD | 0.00 USD | 3,920.00 USD | `-26.04%` | `71,647.00` |
| `Live` | `Long` | `0.0551` | 15,350,000.00 USD | 0.00 USD | 1,760.00 USD | `-25.50%` | `31,888.00` |
| `Live` | `Long` | `0.0554` | 15,350,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-25.23%` | `21,424,497.00` |
| `Live` | `Long` | `0.0554` | 14,170,000.00 USD | 0.00 USD | 175.44 USD | `-25.09%` | `3,164.00` |
| `Live` | `Long` | `0.0556` | 14,170,000.00 USD | 0.00 USD | 907.02 USD | `-24.96%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 14,160,000.00 USD | 0.00 USD | 83,000.00 USD | `-24.69%` | `1,488,849.00` |
| `Live` | `Long` | `0.0561` | 14,080,000.00 USD | 0.00 USD | 8,410.00 USD | `-24.28%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 14,070,000.00 USD | 0.00 USD | 38,870.00 USD | `-24.15%` | `692,198.00` |
| `Live` | `Long` | `0.0563` | 14,030,000.00 USD | 0.00 USD | 2,170.00 USD | `-24.01%` | `38,608.00` |
| `Live` | `Long` | `0.0563` | 14,030,000.00 USD | 0.00 USD | 351.85 USD | `-23.88%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 14,030,000.00 USD | 0.00 USD | 131.48 USD | `-23.61%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 14,030,000.00 USD | 0.00 USD | 567.50 USD | `-23.34%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 14,030,000.00 USD | 0.00 USD | 13,110.00 USD | `-23.07%` | `230,193.00` |
| `Live` | `Long` | `0.0570` | 14,020,000.00 USD | 0.00 USD | 8,700.00 USD | `-22.93%` | `152,415.00` |
| `Live` | `Long` | `0.0571` | 14,010,000.00 USD | 0.00 USD | 814.04 USD | `-22.80%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 14,010,000.00 USD | 0.00 USD | 2,470.00 USD | `-22.66%` | `43,069.00` |
| `Live` | `Long` | `0.0573` | 14,010,000.00 USD | 0.00 USD | 3,910.00 USD | `-22.53%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 14,000,000.00 USD | 0.00 USD | 137.54 USD | `-22.39%` | `2,394.00` |
| `Live` | `Long` | `0.0575` | 14,000,000.00 USD | 0.00 USD | 3,960.00 USD | `-22.25%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 14,000,000.00 USD | 0.00 USD | 10,600.00 USD | `-22.12%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,990,000.00 USD | 0.00 USD | 354,280.00 USD | `-21.98%` | `6,134,633.00` |
| `Live` | `Long` | `0.0578` | 13,630,000.00 USD | 0.00 USD | 3,940.00 USD | `-21.85%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,630,000.00 USD | 0.00 USD | 441.75 USD | `-21.71%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,630,000.00 USD | 0.00 USD | 431.14 USD | `-21.58%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,630,000.00 USD | 0.00 USD | 447.17 USD | `-21.44%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,630,000.00 USD | 0.00 USD | 116.82 USD | `-21.17%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 13,630,000.00 USD | 0.00 USD | 172.78 USD | `-20.90%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,630,000.00 USD | 0.00 USD | 305.15 USD | `-20.63%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,630,000.00 USD | 0.00 USD | 582.13 USD | `-20.36%` | `9,875.00` |
| `Live` | `Long` | `0.0592` | 13,630,000.00 USD | 0.00 USD | 26,980.00 USD | `-20.09%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,600,000.00 USD | 0.00 USD | 1,330.00 USD | `-19.82%` | `22,439.00` |
| `Live` | `Long` | `0.0595` | 13,600,000.00 USD | 0.00 USD | 6,120.00 USD | `-19.69%` | `102,902.00` |
| `Live` | `Long` | `0.0595` | 13,590,000.00 USD | 0.00 USD | 2,940.00 USD | `-19.55%` | `49,364.00` |
| `Live` | `Long` | `0.0597` | 13,590,000.00 USD | 0.00 USD | 31,410.00 USD | `-19.42%` | `526,651.00` |
| `Live` | `Long` | `0.0599` | 13,560,000.00 USD | 0.00 USD | 4,560.00 USD | `-19.15%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 13,550,000.00 USD | 0.00 USD | 1,130.00 USD | `-19.01%` | `18,786.00` |
| `Live` | `Long` | `0.0600` | 13,550,000.00 USD | 0.00 USD | 7,210.00 USD | `-18.88%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,540,000.00 USD | 0.00 USD | 12,320.00 USD | `-18.74%` | `204,866.00` |
| `Live` | `Long` | `0.0602` | 13,530,000.00 USD | 0.00 USD | 830.97 USD | `-18.61%` | `13,792.00` |
| `Live` | `Long` | `0.0604` | 13,530,000.00 USD | 0.00 USD | 930.23 USD | `-18.47%` | `15,414.00` |
| `Live` | `Long` | `0.0604` | 13,530,000.00 USD | 0.00 USD | 1,970.00 USD | `-18.34%` | `32,592.00` |
| `Live` | `Long` | `0.0605` | 13,530,000.00 USD | 0.00 USD | 32,090.00 USD | `-18.20%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 13,500,000.00 USD | 0.00 USD | 622.63 USD | `-18.07%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 13,500,000.00 USD | 0.00 USD | 6,690.00 USD | `-17.93%` | `110,080.00` |
| `Live` | `Long` | `0.0609` | 13,490,000.00 USD | 0.00 USD | 717.73 USD | `-17.80%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 13,490,000.00 USD | 0.00 USD | 5,110.00 USD | `-17.66%` | `83,914.00` |
| `Live` | `Long` | `0.0612` | 13,480,000.00 USD | 0.00 USD | 629.72 USD | `-17.39%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 13,480,000.00 USD | 0.00 USD | 958.56 USD | `-17.26%` | `15,650.00` |
| `Live` | `Long` | `0.0614` | 13,480,000.00 USD | 0.00 USD | 655.16 USD | `-17.12%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 13,480,000.00 USD | 0.00 USD | 1,890.00 USD | `-16.85%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 13,480,000.00 USD | 0.00 USD | 11,100.00 USD | `-16.72%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 13,470,000.00 USD | 0.00 USD | 158.08 USD | `-16.58%` | `2,560.00` |
| `Live` | `Long` | `0.0619` | 13,470,000.00 USD | 0.00 USD | 90,950.00 USD | `-16.31%` | `1,468,052.00` |
| `Live` | `Long` | `0.0621` | 13,380,000.00 USD | 0.00 USD | 26,790.00 USD | `-16.18%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 13,350,000.00 USD | 0.00 USD | 345.86 USD | `-16.04%` | `5,565.00` |
| `Live` | `Long` | `0.0624` | 13,350,000.00 USD | 0.00 USD | 29,020.00 USD | `-15.77%` | `465,433.00` |
| `Live` | `Long` | `0.0624` | 13,320,000.00 USD | 0.00 USD | 6,160,000.00 USD | `-15.64%` | `98,666,424.00` |
| `Live` | `Long` | `0.0625` | 7,160,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-15.50%` | `17,912,020.00` |
| `Live` | `Long` | `0.0626` | 6,040,000.00 USD | 0.00 USD | 870.40 USD | `-15.37%` | `13,893.00` |
| `Live` | `Long` | `0.0628` | 6,040,000.00 USD | 0.00 USD | 461.78 USD | `-15.23%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,040,000.00 USD | 0.00 USD | 6,400.00 USD | `-15.10%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,030,000.00 USD | 0.00 USD | 2,810.00 USD | `-14.82%` | `44,601.00` |
| `Live` | `Long` | `0.0631` | 6,030,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-14.69%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 4,960,000.00 USD | 0.00 USD | 3,260.00 USD | `-14.55%` | `51,566.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-14.42%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 2,490.00 USD | `-14.28%` | `39,249.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-14.15%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 4,770.00 USD | `-14.01%` | `74,997.00` |
| `Live` | `Long` | `0.0638` | 4,940,000.00 USD | 0.00 USD | 5,600.00 USD | `-13.88%` | `87,791.00` |
| `Live` | `Long` | `0.0639` | 4,930,000.00 USD | 0.00 USD | 24,110.00 USD | `-13.74%` | `377,671.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 1,990.00 USD | `-13.61%` | `31,194.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 150.01 USD | `-13.47%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 15,070.00 USD | `-13.34%` | `234,882.00` |
| `Live` | `Long` | `0.0643` | 4,890,000.00 USD | 0.00 USD | 9,150.00 USD | `-13.20%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 4,880,000.00 USD | 0.00 USD | 11,930.00 USD | `-13.07%` | `185,416.00` |
| `Live` | `Long` | `0.0644` | 4,870,000.00 USD | 0.00 USD | 27,380.00 USD | `-12.93%` | `424,844.00` |
| `Live` | `Long` | `0.0645` | 4,840,000.00 USD | 0.00 USD | 631.94 USD | `-12.80%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,840,000.00 USD | 0.00 USD | 163,360.00 USD | `-12.53%` | `2,522,918.00` |
| `Live` | `Long` | `0.0649` | 4,680,000.00 USD | 0.00 USD | 8,800.00 USD | `-12.39%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,670,000.00 USD | 0.00 USD | 21,910.00 USD | `-12.26%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,650,000.00 USD | 0.00 USD | 2,380.00 USD | `-11.99%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,650,000.00 USD | 0.00 USD | 112,510.00 USD | `-11.85%` | `1,724,355.00` |
| `Live` | `Long` | `0.0654` | 4,540,000.00 USD | 0.00 USD | 6,530.00 USD | `-11.72%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,530,000.00 USD | 0.00 USD | 73,340.00 USD | `-11.45%` | `1,118,852.00` |
| `Live` | `Long` | `0.0658` | 4,460,000.00 USD | 0.00 USD | 66,820.00 USD | `-11.18%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,390,000.00 USD | 0.00 USD | 14,600.00 USD | `-11.04%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,370,000.00 USD | 0.00 USD | 9,600.00 USD | `-10.91%` | `145,525.00` |
| `Live` | `Long` | `0.0660` | 4,360,000.00 USD | 0.00 USD | 525.96 USD | `-10.77%` | `7,963.00` |
| `Live` | `Long` | `0.0662` | 4,360,000.00 USD | 0.00 USD | 7,050.00 USD | `-10.64%` | `106,550.00` |
| `Live` | `Long` | `0.0663` | 4,360,000.00 USD | 0.00 USD | 1,630.00 USD | `-10.50%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,360,000.00 USD | 0.00 USD | 19,830.00 USD | `-10.37%` | `298,903.00` |
| `Live` | `Long` | `0.0664` | 4,340,000.00 USD | 0.00 USD | 1,270.00 USD | `-10.23%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,330,000.00 USD | 0.00 USD | 34,860.00 USD | `-9.96%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,300,000.00 USD | 0.00 USD | 2,730.00 USD | `-9.83%` | `40,945.00` |
| `Live` | `Long` | `0.0669` | 4,300,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-9.69%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,150,000.00 USD | 0.00 USD | 1,180.00 USD | `-9.56%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,150,000.00 USD | 0.00 USD | 9,190.00 USD | `-9.42%` | `136,993.00` |
| `Live` | `Long` | `0.0673` | 3,140,000.00 USD | 0.00 USD | 9,220.00 USD | `-9.15%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,130,000.00 USD | 0.00 USD | 15,370.00 USD | `-9.02%` | `228,139.00` |
| `Live` | `Long` | `0.0674` | 3,120,000.00 USD | 0.00 USD | 1,780.00 USD | `-8.88%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,110,000.00 USD | 0.00 USD | 329.58 USD | `-8.75%` | `4,879.00` |
| `Live` | `Long` | `0.0677` | 3,110,000.00 USD | 0.00 USD | 12,610.00 USD | `-8.61%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 4,290.00 USD | `-8.48%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 37,110.00 USD | `-8.34%` | `546,959.00` |
| `Live` | `Long` | `0.0679` | 3,060,000.00 USD | 0.00 USD | 16,630.00 USD | `-8.21%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,040,000.00 USD | 0.00 USD | 212.72 USD | `-8.07%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,040,000.00 USD | 0.00 USD | 117.29 USD | `-7.94%` | `1,721.00` |
| `Live` | `Long` | `0.0683` | 3,040,000.00 USD | 0.00 USD | 6,220.00 USD | `-7.80%` | `91,110.00` |
| `Live` | `Long` | `0.0684` | 3,040,000.00 USD | 0.00 USD | 130,000.00 USD | `-7.53%` | `1,899,254.00` |
| `Live` | `Long` | `0.0685` | 2,910,000.00 USD | 0.00 USD | 6,270.00 USD | `-7.39%` | `91,414.00` |
| `Live` | `Long` | `0.0687` | 2,900,000.00 USD | 0.00 USD | 595.81 USD | `-7.26%` | `8,679.00` |
| `Live` | `Long` | `0.0688` | 2,900,000.00 USD | 0.00 USD | 16,210.00 USD | `-7.12%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,880,000.00 USD | 0.00 USD | 870.75 USD | `-6.99%` | `12,647.00` |
| `Live` | `Long` | `0.0689` | 2,880,000.00 USD | 0.00 USD | 507,660.00 USD | `-6.85%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,370,000.00 USD | 0.00 USD | 6,960.00 USD | `-6.72%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,370,000.00 USD | 0.00 USD | 13,510.00 USD | `-6.58%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,350,000.00 USD | 0.00 USD | 9,970.00 USD | `-6.45%` | `144,028.00` |
| `Live` | `Long` | `0.0693` | 2,340,000.00 USD | 0.00 USD | 4,610.00 USD | `-6.31%` | `66,513.00` |
| `Live` | `Long` | `0.0694` | 2,340,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.18%` | `71,770.00` |
| `Live` | `Long` | `0.0696` | 2,330,000.00 USD | 0.00 USD | 11,620.00 USD | `-6.04%` | `167,011.00` |
| `Live` | `Long` | `0.0697` | 2,320,000.00 USD | 0.00 USD | 5,240.00 USD | `-5.91%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,320,000.00 USD | 0.00 USD | 4,720.00 USD | `-5.77%` | `67,696.00` |
| `Live` | `Long` | `0.0698` | 2,310,000.00 USD | 0.00 USD | 3,630.00 USD | `-5.64%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,310,000.00 USD | 0.00 USD | 1,590.00 USD | `-5.50%` | `22,784.00` |
| `Live` | `Long` | `0.0701` | 2,310,000.00 USD | 0.00 USD | 9,620.00 USD | `-5.37%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,300,000.00 USD | 0.00 USD | 10,750.00 USD | `-5.23%` | `153,233.00` |
| `Live` | `Long` | `0.0703` | 2,290,000.00 USD | 0.00 USD | 1,070.00 USD | `-5.10%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,290,000.00 USD | 0.00 USD | 44,080.00 USD | `-4.96%` | `626,588.00` |
| `Live` | `Long` | `0.0704` | 2,240,000.00 USD | 0.00 USD | 216.56 USD | `-4.83%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,240,000.00 USD | 0.00 USD | 423.90 USD | `-4.56%` | `6,000.00` |
| `Live` | `Long` | `0.0707` | 2,240,000.00 USD | 0.00 USD | 94,410.00 USD | `-4.42%` | `1,334,448.00` |
| `Live` | `Long` | `0.0708` | 2,150,000.00 USD | 0.00 USD | 487.73 USD | `-4.29%` | `6,884.00` |
| `Live` | `Long` | `0.0709` | 2,150,000.00 USD | 0.00 USD | 351.63 USD | `-4.15%` | `4,956.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 1,920.00 USD | `-3.88%` | `27,032.00` |
| `Live` | `Long` | `0.0712` | 2,140,000.00 USD | 0.00 USD | 802.06 USD | `-3.75%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,140,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-3.61%` | `24,470,566.00` |
| `Live` | `Long` | `0.0714` | 397,340.00 USD | 0.00 USD | 213.78 USD | `-3.48%` | `2,992.00` |
| `Live` | `Long` | `0.0716` | 397,130.00 USD | 0.00 USD | 8,120.00 USD | `-3.34%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 389,010.00 USD | 0.00 USD | 1,170.00 USD | `-3.21%` | `16,291.00` |
| `Live` | `Long` | `0.0717` | 387,840.00 USD | 0.00 USD | 22,270.00 USD | `-3.07%` | `310,316.00` |
| `Live` | `Long` | `0.0718` | 365,580.00 USD | 0.00 USD | 1,070.00 USD | `-2.94%` | `14,951.00` |
| `Live` | `Long` | `0.0720` | 364,500.00 USD | 0.00 USD | 1,900.00 USD | `-2.80%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 362,610.00 USD | 0.00 USD | 12,160.00 USD | `-2.67%` | `168,703.00` |
| `Live` | `Long` | `0.0722` | 350,450.00 USD | 0.00 USD | 22,360.00 USD | `-2.53%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 328,100.00 USD | 0.00 USD | 322,050.00 USD | `-2.40%` | `4,457,443.00` |
| `Live` | `Long` | `0.0723` | 6,050.00 USD | 0.00 USD | 626.77 USD | `-2.26%` | `8,663.00` |
| `Live` | `Long` | `0.0740` | 5,420.00 USD | 0.00 USD | 5,420.00 USD | `-0.10%` | `73,280.00` |
| `Live` | `Short` | `0.0767` | 28,530.00 USD | 28,530.00 USD | 0.00 USD | `+3.68%` | `371,673.00` |
| `Live` | `Short` | `0.0774` | 32,020.00 USD | 3,490.00 USD | 0.00 USD | `+4.49%` | `45,176.00` |
| `Live` | `Short` | `0.0775` | 32,260.00 USD | 240.95 USD | 0.00 USD | `+4.76%` | `3,107.00` |
| `Live` | `Short` | `0.0777` | 34,370.00 USD | 2,110.00 USD | 0.00 USD | `+5.03%` | `27,101.00` |
| `Live` | `Short` | `0.0788` | 34,480.00 USD | 113.24 USD | 0.00 USD | `+6.38%` | `1,438.00` |
| `Live` | `Short` | `0.0803` | 34,700.00 USD | 216.84 USD | 0.00 USD | `+8.41%` | `2,702.00` |
| `Live` | `Short` | `0.0804` | 34,920.00 USD | 217.11 USD | 0.00 USD | `+8.55%` | `2,702.00` |
| `Live` | `Short` | `0.0819` | 35,300.00 USD | 380.85 USD | 0.00 USD | `+10.57%` | `4,653.00` |
| `Live` | `Short` | `0.0824` | 35,560.00 USD | 265.58 USD | 0.00 USD | `+11.25%` | `3,225.00` |
| `Live` | `Short` | `0.0832` | 39,020.00 USD | 3,450.00 USD | 0.00 USD | `+12.33%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 39,520.00 USD | 500.17 USD | 0.00 USD | `+12.46%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 39,810.00 USD | 293.44 USD | 0.00 USD | `+13.00%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 41,380.00 USD | 1,570.00 USD | 0.00 USD | `+13.14%` | `18,767.00` |
| `Live` | `Short` | `0.0848` | 42,530.00 USD | 1,150.00 USD | 0.00 USD | `+14.62%` | `13,561.00` |
| `Live` | `Short` | `0.0858` | 42,650.00 USD | 115.30 USD | 0.00 USD | `+15.98%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 47,100.00 USD | 4,450.00 USD | 0.00 USD | `+16.11%` | `51,791.00` |
| `Live` | `Short` | `0.0871` | 47,240.00 USD | 138.58 USD | 0.00 USD | `+17.60%` | `1,592.00` |
| `Live` | `Short` | `0.0881` | 47,700.00 USD | 465.17 USD | 0.00 USD | `+18.95%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 48,110.00 USD | 411.53 USD | 0.00 USD | `+19.89%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 48,530.00 USD | 418.80 USD | 0.00 USD | `+20.30%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 48,820.00 USD | 285.70 USD | 0.00 USD | `+20.84%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 55,580.00 USD | 6,760.00 USD | 0.00 USD | `+22.19%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 56,890.00 USD | 1,310.00 USD | 0.00 USD | `+22.46%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 61,830.00 USD | 4,940.00 USD | 0.00 USD | `+23.14%` | `54,197.00` |
| `Live` | `Short` | `0.0916` | 61,960.00 USD | 133.66 USD | 0.00 USD | `+23.68%` | `1,460.00` |
| `Live` | `Short` | `0.0921` | 62,140.00 USD | 171.49 USD | 0.00 USD | `+24.35%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 62,940.00 USD | 805.37 USD | 0.00 USD | `+25.84%` | `8,646.00` |
| `Live` | `Short` | `0.0944` | 106,890.00 USD | 43,950.00 USD | 0.00 USD | `+27.46%` | `465,808.00` |
| `Live` | `Short` | `0.0950` | 131,350.00 USD | 24,460.00 USD | 0.00 USD | `+28.27%` | `257,659.00` |
| `Live` | `Short` | `0.0955` | 179,130.00 USD | 47,770.00 USD | 0.00 USD | `+29.08%` | `500,000.00` |
| `Live` | `Short` | `0.0959` | 179,320.00 USD | 195.26 USD | 0.00 USD | `+29.62%` | `2,035.00` |
| `Live` | `Short` | `0.0961` | 179,930.00 USD | 609.59 USD | 0.00 USD | `+29.89%` | `6,340.00` |
| `Live` | `Short` | `0.0974` | 180,060.00 USD | 121.23 USD | 0.00 USD | `+31.65%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 180,530.00 USD | 477.50 USD | 0.00 USD | `+32.73%` | `4,860.00` |
| `Live` | `Short` | `0.0990` | 181,730.00 USD | 1,200.00 USD | 0.00 USD | `+33.81%` | `12,089.00` |
| `Live` | `Short` | `0.0994` | 182,700.00 USD | 968.25 USD | 0.00 USD | `+34.35%` | `9,736.00` |
| `Live` | `Short` | `0.1014` | 190,320.00 USD | 7,630.00 USD | 0.00 USD | `+37.05%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 193,290.00 USD | 2,970.00 USD | 0.00 USD | `+37.32%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 193,790.00 USD | 492.85 USD | 0.00 USD | `+37.59%` | `4,839.00` |
| `Live` | `Short` | `0.1061` | 199,900.00 USD | 6,110.00 USD | 0.00 USD | `+43.40%` | `57,554.00` |
| `Live` | `Short` | `0.1066` | 203,200.00 USD | 3,300.00 USD | 0.00 USD | `+43.94%` | `31,000.00` |
| `Live` | `Short` | `0.1067` | 206,320.00 USD | 3,120.00 USD | 0.00 USD | `+44.21%` | `29,217.00` |
| `Live` | `Short` | `0.1076` | 206,930.00 USD | 616.19 USD | 0.00 USD | `+45.43%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 210,170.00 USD | 3,240.00 USD | 0.00 USD | `+46.64%` | `29,849.00` |
| `Live` | `Short` | `0.1113` | 211,850.00 USD | 1,670.00 USD | 0.00 USD | `+50.29%` | `15,036.00` |
| `Live` | `Short` | `0.1127` | 212,060.00 USD | 214.15 USD | 0.00 USD | `+52.18%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 212,200.00 USD | 142.88 USD | 0.00 USD | `+52.59%` | `1,265.00` |
| `Live` | `Short` | `0.1138` | 212,360.00 USD | 153.68 USD | 0.00 USD | `+53.67%` | `1,351.00` |
| `Live` | `Short` | `0.1158` | 212,490.00 USD | 131.49 USD | 0.00 USD | `+56.50%` | `1,135.00` |
| `Live` | `Short` | `0.1222` | 213,290.00 USD | 796.83 USD | 0.00 USD | `+65.15%` | `6,518.00` |
| `Live` | `Short` | `0.1250` | 214,190.00 USD | 902.01 USD | 0.00 USD | `+68.80%` | `7,219.00` |
| `Live` | `Short` | `0.1270` | 214,300.00 USD | 108.80 USD | 0.00 USD | `+71.50%` | `857.00` |
| `Live` | `Short` | `0.1285` | 258,290.00 USD | 43,990.00 USD | 0.00 USD | `+73.66%` | `342,231.00` |
| `Live` | `Short` | `0.1296` | 258,460.00 USD | 171.66 USD | 0.00 USD | `+75.15%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 260,600.00 USD | 2,140.00 USD | 0.00 USD | `+77.17%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 260,700.00 USD | 102.97 USD | 0.00 USD | `+78.12%` | `781.00` |
| `Live` | `Short` | `0.1338` | 261,040.00 USD | 334.38 USD | 0.00 USD | `+80.68%` | `2,500.00` |
| `Live` | `Short` | `0.1366` | 302,540.00 USD | 41,500.00 USD | 0.00 USD | `+84.60%` | `303,679.00` |
| `Live` | `Short` | `0.1381` | 324,940.00 USD | 22,410.00 USD | 0.00 USD | `+86.63%` | `162,180.00` |
| `Live` | `Short` | `0.1388` | 325,910.00 USD | 968.20 USD | 0.00 USD | `+87.44%` | `6,978.00` |
| `Live` | `Short` | `0.1399` | 327,870.00 USD | 1,960.00 USD | 0.00 USD | `+89.06%` | `14,000.00` |
| `Live` | `Short` | `0.1404` | 327,970.00 USD | 100.35 USD | 0.00 USD | `+89.60%` | `715.00` |
| `Live` | `Short` | `0.1404` | 328,630.00 USD | 663.63 USD | 0.00 USD | `+89.74%` | `4,725.00` |
| `Live` | `Short` | `0.1432` | 330,500.00 USD | 1,860.00 USD | 0.00 USD | `+93.52%` | `13,010.00` |
| `Live` | `Short` | `0.1441` | 330,690.00 USD | 196.63 USD | 0.00 USD | `+94.60%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 332,240.00 USD | 1,540.00 USD | 0.00 USD | `+95.00%` | `10,691.00` |
| `Live` | `Short` | `0.1462` | 338,610.00 USD | 6,380.00 USD | 0.00 USD | `+97.57%` | `43,601.00` |
| `Live` | `Short` | `0.1470` | 342,720.00 USD | 4,110.00 USD | 0.00 USD | `+98.65%` | `27,933.00` |
| `Live` | `Short` | `0.1479` | 350,980.00 USD | 8,260.00 USD | 0.00 USD | `+99.73%` | `55,849.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 631,460.00 USD | 0.00 USD | 375.42 USD | `-65.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 631,080.00 USD | 0.00 USD | 409.59 USD | `-45.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 630,670.00 USD | 0.00 USD | 132.68 USD | `-44.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 630,540.00 USD | 0.00 USD | 788.27 USD | `-43.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 629,750.00 USD | 0.00 USD | 527.05 USD | `-43.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 629,220.00 USD | 0.00 USD | 286.87 USD | `-39.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 628,940.00 USD | 0.00 USD | 252.42 USD | `-37.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 628,680.00 USD | 0.00 USD | 468.67 USD | `-36.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 628,210.00 USD | 0.00 USD | 5,160.00 USD | `-33.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 623,060.00 USD | 0.00 USD | 920.48 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 622,140.00 USD | 0.00 USD | 236.01 USD | `-32.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 621,900.00 USD | 0.00 USD | 175.41 USD | `-30.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 621,720.00 USD | 0.00 USD | 242.96 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 621,480.00 USD | 0.00 USD | 2,670.00 USD | `-26.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 618,810.00 USD | 0.00 USD | 1,370.00 USD | `-25.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 617,440.00 USD | 0.00 USD | 437.58 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 617,000.00 USD | 0.00 USD | 752.54 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 616,240.00 USD | 0.00 USD | 9,830.00 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 606,410.00 USD | 0.00 USD | 889.38 USD | `-20.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 605,520.00 USD | 0.00 USD | 668.84 USD | `-18.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 604,860.00 USD | 0.00 USD | 273.90 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 604,580.00 USD | 0.00 USD | 8,800.00 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 595,780.00 USD | 0.00 USD | 218.94 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 595,560.00 USD | 0.00 USD | 504.26 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 595,060.00 USD | 0.00 USD | 2,470.00 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 592,590.00 USD | 0.00 USD | 118.27 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 592,470.00 USD | 0.00 USD | 1,280.00 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 591,190.00 USD | 0.00 USD | 1,820.00 USD | `-14.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 589,370.00 USD | 0.00 USD | 1,340.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 588,030.00 USD | 0.00 USD | 412.42 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 587,620.00 USD | 0.00 USD | 644.50 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 586,980.00 USD | 0.00 USD | 19,520.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 567,460.00 USD | 0.00 USD | 1,410.00 USD | `-11.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 566,050.00 USD | 0.00 USD | 3,140.00 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 562,910.00 USD | 0.00 USD | 1,100.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 561,810.00 USD | 0.00 USD | 1,200.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 560,620.00 USD | 0.00 USD | 2,310.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 558,300.00 USD | 0.00 USD | 909.85 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 557,400.00 USD | 0.00 USD | 115.57 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 557,280.00 USD | 0.00 USD | 33,620.00 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 523,650.00 USD | 0.00 USD | 12,860.00 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 510,790.00 USD | 0.00 USD | 1,540.00 USD | `-8.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 509,250.00 USD | 0.00 USD | 108.08 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 509,140.00 USD | 0.00 USD | 19,540.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 489,600.00 USD | 0.00 USD | 1,430.00 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 488,170.00 USD | 0.00 USD | 7,990.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 480,180.00 USD | 0.00 USD | 8,580.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 471,600.00 USD | 0.00 USD | 606.47 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 471,000.00 USD | 0.00 USD | 3,100.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 467,900.00 USD | 0.00 USD | 160.31 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 467,740.00 USD | 0.00 USD | 38,710.00 USD | `-6.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 429,030.00 USD | 0.00 USD | 12,400.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 416,640.00 USD | 0.00 USD | 2,590.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 414,050.00 USD | 0.00 USD | 533.09 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 413,520.00 USD | 0.00 USD | 378.50 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 413,140.00 USD | 0.00 USD | 925.29 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 412,210.00 USD | 0.00 USD | 797.80 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 411,410.00 USD | 0.00 USD | 9,110.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 402,300.00 USD | 0.00 USD | 141.77 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 402,160.00 USD | 0.00 USD | 895.27 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 401,260.00 USD | 0.00 USD | 523.23 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 400,740.00 USD | 0.00 USD | 468.88 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 400,270.00 USD | 0.00 USD | 235.12 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 400,040.00 USD | 0.00 USD | 1,090.00 USD | `-4.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 398,950.00 USD | 0.00 USD | 71,660.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 327,290.00 USD | 0.00 USD | 497.62 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 326,790.00 USD | 0.00 USD | 20,330.00 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 306,460.00 USD | 0.00 USD | 608.76 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 305,850.00 USD | 0.00 USD | 16,880.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 288,970.00 USD | 0.00 USD | 143.31 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 288,830.00 USD | 0.00 USD | 1,670.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 287,150.00 USD | 0.00 USD | 4,210.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 282,950.00 USD | 0.00 USD | 8,770.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 274,180.00 USD | 0.00 USD | 413.42 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 273,760.00 USD | 0.00 USD | 138,380.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 135,380.00 USD | 0.00 USD | 35,120.00 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 100,270.00 USD | 0.00 USD | 621.12 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 99,640.00 USD | 0.00 USD | 2,030.00 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 97,620.00 USD | 0.00 USD | 1,950.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 95,660.00 USD | 0.00 USD | 29,060.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 66,600.00 USD | 0.00 USD | 3,870.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 62,730.00 USD | 0.00 USD | 2,090.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 60,640.00 USD | 0.00 USD | 23,870.00 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 36,770.00 USD | 0.00 USD | 29,130.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 7,640.00 USD | 0.00 USD | 123.40 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 7,520.00 USD | 0.00 USD | 398.00 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 7,120.00 USD | 0.00 USD | 797.39 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 6,320.00 USD | 0.00 USD | 4,680.00 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 1,640.00 USD | 0.00 USD | 1,640.00 USD | `-0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0741` | 7,330.00 USD | 7,330.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0742` | 10,230.00 USD | 2,900.00 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0743` | 10,640.00 USD | 415.62 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0745` | 12,360.00 USD | 1,720.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0746` | 15,890.00 USD | 3,530.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0746` | 16,270.00 USD | 375.86 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0747` | 20,690.00 USD | 4,430.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0748` | 20,830.00 USD | 140.04 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0750` | 27,110.00 USD | 6,280.00 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0751` | 30,560.00 USD | 3,450.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0751` | 31,300.00 USD | 736.17 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0752` | 31,700.00 USD | 406.95 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0754` | 31,810.00 USD | 103.08 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0755` | 32,210.00 USD | 407.73 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 32,680.00 USD | 465.39 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 33,090.00 USD | 408.81 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 36,960.00 USD | 3,870.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 37,460.00 USD | 504.10 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 37,860.00 USD | 398.13 USD | 0.00 USD | `+2.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 37,970.00 USD | 113.01 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 38,780.00 USD | 806.81 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 39,520.00 USD | 738.18 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 43,290.00 USD | 3,770.00 USD | 0.00 USD | `+3.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 43,400.00 USD | 109.63 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 45,300.00 USD | 1,900.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 45,490.00 USD | 183.50 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 46,330.00 USD | 843.94 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 46,830.00 USD | 502.52 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 47,650.00 USD | 816.05 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 47,910.00 USD | 266.52 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 50,150.00 USD | 2,240.00 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 50,390.00 USD | 240.02 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 54,330.00 USD | 3,930.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 54,730.00 USD | 407.23 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 55,060.00 USD | 321.13 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 56,550.00 USD | 1,490.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 56,960.00 USD | 407.72 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 57,280.00 USD | 329.23 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 57,590.00 USD | 303.77 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 57,770.00 USD | 186.07 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 60,850.00 USD | 3,080.00 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 62,050.00 USD | 1,200.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 66,420.00 USD | 4,370.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 66,580.00 USD | 157.14 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 66,710.00 USD | 130.71 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 108,320.00 USD | 41,610.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 111,350.00 USD | 3,030.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 112,120.00 USD | 773.68 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 112,800.00 USD | 673.60 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 120,500.00 USD | 7,700.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 125,100.00 USD | 4,600.00 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 127,350.00 USD | 2,260.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 135,170.00 USD | 7,820.00 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 135,490.00 USD | 312.56 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 135,940.00 USD | 455.34 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 136,070.00 USD | 125.45 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 136,300.00 USD | 230.40 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 136,620.00 USD | 319.16 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 137,620.00 USD | 1,010.00 USD | 0.00 USD | `+8.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 160,370.00 USD | 22,750.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 160,770.00 USD | 400.91 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 160,970.00 USD | 200.46 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 161,230.00 USD | 259.13 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 161,940.00 USD | 707.08 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 170,950.00 USD | 9,010.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 267,730.00 USD | 96,780.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 268,540.00 USD | 807.50 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 268,790.00 USD | 257.18 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 269,220.00 USD | 424.74 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 269,320.00 USD | 101.80 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 270,700.00 USD | 1,380.00 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 272,730.00 USD | 2,030.00 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 274,160.00 USD | 1,430.00 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 274,290.00 USD | 129.67 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 275,310.00 USD | 1,020.00 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 277,760.00 USD | 2,450.00 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 278,780.00 USD | 1,030.00 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 281,800.00 USD | 3,020.00 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 282,130.00 USD | 327.80 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 282,590.00 USD | 457.92 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 283,280.00 USD | 691.29 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 284,080.00 USD | 800.79 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 284,590.00 USD | 512.05 USD | 0.00 USD | `+11.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 285,090.00 USD | 495.36 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 285,480.00 USD | 389.31 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 285,630.00 USD | 154.58 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 285,940.00 USD | 303.56 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 286,050.00 USD | 112.89 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 286,430.00 USD | 381.45 USD | 0.00 USD | `+12.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 286,590.00 USD | 155.82 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 330,970.00 USD | 44,390.00 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 331,110.00 USD | 138.69 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 332,370.00 USD | 1,260.00 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 332,480.00 USD | 107.03 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,080,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,080,000.00 USD | 3,150.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,080,000.00 USD | 1,470.00 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,080,000.00 USD | 107.71 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,080,000.00 USD | 2,690.00 USD | 0.00 USD | `+13.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,080,000.00 USD | 529.92 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,080,000.00 USD | 219.07 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,080,000.00 USD | 242.84 USD | 0.00 USD | `+14.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,090,000.00 USD | 10,140.00 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,100,000.00 USD | 876.11 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,100,000.00 USD | 812.54 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,100,000.00 USD | 126.76 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,100,000.00 USD | 307.41 USD | 0.00 USD | `+15.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,100,000.00 USD | 614.09 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,100,000.00 USD | 644.62 USD | 0.00 USD | `+16.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,100,000.00 USD | 2,020.00 USD | 0.00 USD | `+16.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,140,000.00 USD | 43,760.00 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,140,000.00 USD | 123.94 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,140,000.00 USD | 271.53 USD | 0.00 USD | `+17.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,150,000.00 USD | 857.15 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,150,000.00 USD | 1,840.00 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,150,000.00 USD | 2,760.00 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,150,000.00 USD | 117.71 USD | 0.00 USD | `+18.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,150,000.00 USD | 111.61 USD | 0.00 USD | `+18.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,150,000.00 USD | 571.18 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,150,000.00 USD | 375.94 USD | 0.00 USD | `+19.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,150,000.00 USD | 627.55 USD | 0.00 USD | `+19.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,150,000.00 USD | 211.04 USD | 0.00 USD | `+19.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,150,000.00 USD | 108.36 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,150,000.00 USD | 543.32 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,150,000.00 USD | 1,820.00 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,160,000.00 USD | 2,080.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,170,000.00 USD | 17,680.00 USD | 0.00 USD | `+20.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,180,000.00 USD | 1,370.00 USD | 0.00 USD | `+20.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,180,000.00 USD | 5,630.00 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,180,000.00 USD | 1,090.00 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,180,000.00 USD | 224.86 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,200,000.00 USD | 20,540.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,200,000.00 USD | 114.93 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,200,000.00 USD | 679.12 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,200,000.00 USD | 173.36 USD | 0.00 USD | `+23.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,210,000.00 USD | 1,810.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,210,000.00 USD | 1,380.00 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,210,000.00 USD | 2,280.00 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,210,000.00 USD | 541.32 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,350,000.00 USD | 137,500.00 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,350,000.00 USD | 691.07 USD | 0.00 USD | `+25.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,350,000.00 USD | 6,250.00 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,370,000.00 USD | 13,480.00 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,370,000.00 USD | 734.82 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,370,000.00 USD | 1,230.00 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,370,000.00 USD | 105.00 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,370,000.00 USD | 184.09 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,370,000.00 USD | 1,120.00 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,370,000.00 USD | 1,860.00 USD | 0.00 USD | `+26.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,370,000.00 USD | 1,070.00 USD | 0.00 USD | `+27.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,370,000.00 USD | 512.15 USD | 0.00 USD | `+27.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,380,000.00 USD | 6,620.00 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,380,000.00 USD | 404.96 USD | 0.00 USD | `+28.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,380,000.00 USD | 129.85 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,390,000.00 USD | 3,740.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,390,000.00 USD | 409.17 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,390,000.00 USD | 203.74 USD | 0.00 USD | `+30.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,390,000.00 USD | 2,800.00 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,390,000.00 USD | 1,320.00 USD | 0.00 USD | `+31.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,390,000.00 USD | 694.56 USD | 0.00 USD | `+31.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,390,000.00 USD | 940.91 USD | 0.00 USD | `+32.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,390,000.00 USD | 2,980.00 USD | 0.00 USD | `+33.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,400,000.00 USD | 104.99 USD | 0.00 USD | `+33.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,400,000.00 USD | 1,930.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,400,000.00 USD | 1,490.00 USD | 0.00 USD | `+34.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,400,000.00 USD | 1,090.00 USD | 0.00 USD | `+34.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,400,000.00 USD | 438.96 USD | 0.00 USD | `+34.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,400,000.00 USD | 973.76 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,410,000.00 USD | 10,000.00 USD | 0.00 USD | `+35.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,410,000.00 USD | 2,890.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,420,000.00 USD | 2,060.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,420,000.00 USD | 482.89 USD | 0.00 USD | `+36.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,420,000.00 USD | 201.90 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,420,000.00 USD | 489.46 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,420,000.00 USD | 103.68 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,420,000.00 USD | 2,590.00 USD | 0.00 USD | `+37.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,420,000.00 USD | 3,810.00 USD | 0.00 USD | `+37.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,430,000.00 USD | 11,200.00 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,440,000.00 USD | 4,330.00 USD | 0.00 USD | `+38.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,440,000.00 USD | 205.50 USD | 0.00 USD | `+38.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,440,000.00 USD | 3,490.00 USD | 0.00 USD | `+39.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,440,000.00 USD | 1,300.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,440,000.00 USD | 207.50 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,450,000.00 USD | 813.88 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,470,000.00 USD | 23,160.00 USD | 0.00 USD | `+41.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,470,000.00 USD | 781.51 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,470,000.00 USD | 209.30 USD | 0.00 USD | `+41.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,470,000.00 USD | 1,440.00 USD | 0.00 USD | `+41.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,480,000.00 USD | 5,140.00 USD | 0.00 USD | `+41.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,480,000.00 USD | 585.32 USD | 0.00 USD | `+42.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,480,000.00 USD | 210.90 USD | 0.00 USD | `+42.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,480,000.00 USD | 1,850.00 USD | 0.00 USD | `+42.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,480,000.00 USD | 105.75 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,480,000.00 USD | 3,220.00 USD | 0.00 USD | `+43.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,480,000.00 USD | 1,600.00 USD | 0.00 USD | `+43.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,480,000.00 USD | 212.90 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,480,000.00 USD | 472.63 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,480,000.00 USD | 214.50 USD | 0.00 USD | `+44.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,490,000.00 USD | 1,040.00 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,490,000.00 USD | 136.12 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,490,000.00 USD | 216.10 USD | 0.00 USD | `+45.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,490,000.00 USD | 1,010.00 USD | 0.00 USD | `+46.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,490,000.00 USD | 217.90 USD | 0.00 USD | `+47.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,490,000.00 USD | 219.70 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,500,000.00 USD | 7,920.00 USD | 0.00 USD | `+48.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,500,000.00 USD | 154.22 USD | 0.00 USD | `+49.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,500,000.00 USD | 221.30 USD | 0.00 USD | `+49.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,520,000.00 USD | 24,440.00 USD | 0.00 USD | `+50.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,520,000.00 USD | 223.10 USD | 0.00 USD | `+50.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,520,000.00 USD | 224.70 USD | 0.00 USD | `+51.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,520,000.00 USD | 226.30 USD | 0.00 USD | `+52.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,520,000.00 USD | 351.57 USD | 0.00 USD | `+53.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,520,000.00 USD | 950.34 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,520,000.00 USD | 229.50 USD | 0.00 USD | `+55.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,520,000.00 USD | 771.08 USD | 0.00 USD | `+55.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,520,000.00 USD | 942.95 USD | 0.00 USD | `+55.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,530,000.00 USD | 230.90 USD | 0.00 USD | `+55.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,530,000.00 USD | 288.18 USD | 0.00 USD | `+56.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,530,000.00 USD | 619.10 USD | 0.00 USD | `+56.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,530,000.00 USD | 1,250.00 USD | 0.00 USD | `+56.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,530,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,530,000.00 USD | 232.30 USD | 0.00 USD | `+56.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,530,000.00 USD | 1,600.00 USD | 0.00 USD | `+57.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,530,000.00 USD | 1,050.00 USD | 0.00 USD | `+57.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,530,000.00 USD | 3,730.00 USD | 0.00 USD | `+58.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,540,000.00 USD | 676.22 USD | 0.00 USD | `+59.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,540,000.00 USD | 648.25 USD | 0.00 USD | `+59.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,540,000.00 USD | 1,510.00 USD | 0.00 USD | `+59.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,540,000.00 USD | 448.52 USD | 0.00 USD | `+59.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,540,000.00 USD | 124.58 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,540,000.00 USD | 1,050.00 USD | 0.00 USD | `+60.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,540,000.00 USD | 691.80 USD | 0.00 USD | `+61.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,660,000.00 USD | 117,860.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,660,000.00 USD | 143.22 USD | 0.00 USD | `+62.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,660,000.00 USD | 1,380.00 USD | 0.00 USD | `+63.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,660,000.00 USD | 2,270.00 USD | 0.00 USD | `+64.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,660,000.00 USD | 871.99 USD | 0.00 USD | `+65.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,690,000.00 USD | 24,560.00 USD | 0.00 USD | `+71.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,690,000.00 USD | 400.21 USD | 0.00 USD | `+71.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,700,000.00 USD | 13,850.00 USD | 0.00 USD | `+78.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,700,000.00 USD | 2,360.00 USD | 0.00 USD | `+78.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,710,000.00 USD | 4,160.00 USD | 0.00 USD | `+83.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,710,000.00 USD | 114.70 USD | 0.00 USD | `+84.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,710,000.00 USD | 278.50 USD | 0.00 USD | `+89.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,710,000.00 USD | 1,160.00 USD | 0.00 USD | `+91.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,710,000.00 USD | 173.57 USD | 0.00 USD | `+92.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,710,000.00 USD | 380.09 USD | 0.00 USD | `+92.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,730,000.00 USD | 17,150.00 USD | 0.00 USD | `+92.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,730,000.00 USD | 1,440.00 USD | 0.00 USD | `+94.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,730,000.00 USD | 433.35 USD | 0.00 USD | `+95.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,730,000.00 USD | 452.26 USD | 0.00 USD | `+96.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,730,000.00 USD | 3,640.00 USD | 0.00 USD | `+98.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,790,000.00 USD | 55,720.00 USD | 0.00 USD | `+99.60%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `1.04B` | Total OI Tokens: `13,900,524,992.4 DOGE`
  * 1h OI Change: `+1.56%` | 4h OI Change: `-3.06%` | 24h OI Change: `-6.34%`
  * Exchange Breakdown: Binance=`241.46M` | Bybit=`105.82M` | OKX=`108.48M` | Hyperliquid=`75.87M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-8.36K` | Last 24h: `35.55K` | Last 3d: `229.21K` | Last 7d: `310.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0023%` | **USDT OKX** | `-0.0040%` |
| **USDT Bybit** | `-0.0024%` | **USDT KuCoin** | `-0.0132%` |
| **USDT MEXC** | `-0.0024%` | **USDT BingX** | `-0.0020%` |
| **USDT Gate** | `0.0048%` | **USDT Bitget** | `-0.0032%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `54.71%` | `45.29%` | `1.21` | 17,930,000.00 USD |
| `15M` | `Binance` | `56.08%` | `43.92%` | `1.28` | 8,100,000.00 USD |
| `15M` | `OKX` | `52.21%` | `47.79%` | `1.09` | 4,250,000.00 USD |
| `15M` | `Bybit` | `59.58%` | `40.42%` | `1.47` | 1,260,000.00 USD |
| `15M` | `KuCoin` | `63.59%` | `36.41%` | `1.75` | 66,470.00 USD |
| `15M` | `Gate` | `51.3%` | `48.7%` | `1.05` | 2,200,000.00 USD |
| `15M` | `Bitget` | `46.12%` | `53.88%` | `0.86` | 214,780.00 USD |
| `15M` | `BingX` | `69.71%` | `30.29%` | `2.30` | 188,650.00 USD |
| `15M` | `MEXC` | `37.6%` | `62.4%` | `0.60` | 221,650.00 USD |
| `15M` | `Bitunix` | `60.1%` | `39.9%` | `1.51` | 519,940.00 USD |
| `15M` | `Hyperliquid` | `65.39%` | `34.61%` | `1.89` | 466,390.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.16%` | `51.84%` | `0.93` | 48,690.00 USD |
| `15M` | `Crypto.com` | `60.68%` | `39.32%` | `1.54` | 13,780.00 USD |
| `15M` | `WhiteBIT` | `33.86%` | `66.14%` | `0.51` | 201,710.00 USD |
| `15M` | `HTX` | `52.52%` | `47.48%` | `1.11` | 81,750.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `28.97%` | `71.03%` | `0.41` | 18,540.00 USD |
| `15M` | `Aster` | `61.59%` | `38.41%` | `1.60` | 73,530.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `6.54%` | `93.46%` | `0.07` | 1,570.00 USD |
| `15M` | `Whale Positions` | `56.08%` | `43.92%` | `1.28` | 8,100,000.00 USD |
| `15M` | `Global Accounts` | `54.71%` | `45.29%` | `1.21` | 17,930,000.00 USD |
| `1H` | `DOGE` | `49.96%` | `50.04%` | `1.00` | 72,690,000.00 USD |
| `1H` | `Binance` | `52.53%` | `47.47%` | `1.11` | 27,320,000.00 USD |
| `1H` | `OKX` | `50.12%` | `49.88%` | `1.00` | 16,140,000.00 USD |
| `1H` | `Bybit` | `57.67%` | `42.33%` | `1.36` | 6,010,000.00 USD |
| `1H` | `KuCoin` | `54.26%` | `45.74%` | `1.19` | 374,330.00 USD |
| `1H` | `Gate` | `50.93%` | `49.07%` | `1.04` | 9,010,000.00 USD |
| `1H` | `Bitget` | `48.87%` | `51.13%` | `0.96` | 1,520,000.00 USD |
| `1H` | `BingX` | `11.64%` | `88.36%` | `0.13` | 3,280,000.00 USD |
| `1H` | `MEXC` | `55.41%` | `44.59%` | `1.24` | 2,090,000.00 USD |
| `1H` | `Bitunix` | `51.86%` | `48.14%` | `1.08` | 2,760,000.00 USD |
| `1H` | `Hyperliquid` | `54.72%` | `45.28%` | `1.21` | 1,170,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `59.1%` | `40.9%` | `1.44` | 266,760.00 USD |
| `1H` | `Crypto.com` | `57.52%` | `42.48%` | `1.35` | 46,580.00 USD |
| `1H` | `WhiteBIT` | `19.21%` | `80.79%` | `0.24` | 543,430.00 USD |
| `1H` | `HTX` | `41.67%` | `58.33%` | `0.71` | 1,370,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `32.66%` | `67.34%` | `0.49` | 172,630.00 USD |
| `1H` | `Aster` | `56.72%` | `43.28%` | `1.31` | 558,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `76.11%` | `23.89%` | `3.19` | 33,490.00 USD |
| `1H` | `Whale Positions` | `52.53%` | `47.47%` | `1.11` | 27,320,000.00 USD |
| `1H` | `Global Accounts` | `49.96%` | `50.04%` | `1.00` | 72,690,000.00 USD |
| `4H` | `DOGE` | `46.99%` | `53.01%` | `0.89` | 526,300,000.00 USD |
| `4H` | `Binance` | `46.07%` | `53.93%` | `0.85` | 194,410,000.00 USD |
| `4H` | `OKX` | `47.53%` | `52.47%` | `0.91` | 119,530,000.00 USD |
| `4H` | `Bybit` | `48.27%` | `51.73%` | `0.93` | 50,970,000.00 USD |
| `4H` | `KuCoin` | `58.87%` | `41.13%` | `1.43` | 4,670,000.00 USD |
| `4H` | `Gate` | `49.21%` | `50.79%` | `0.97` | 46,390,000.00 USD |
| `4H` | `Bitget` | `41.04%` | `58.96%` | `0.70` | 17,500,000.00 USD |
| `4H` | `BingX` | `29.08%` | `70.92%` | `0.41` | 7,470,000.00 USD |
| `4H` | `MEXC` | `47.69%` | `52.31%` | `0.91` | 33,880,000.00 USD |
| `4H` | `Bitunix` | `45.7%` | `54.3%` | `0.84` | 18,820,000.00 USD |
| `4H` | `Hyperliquid` | `45.21%` | `54.79%` | `0.83` | 5,860,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.88%` | `42.12%` | `1.37` | 1,720,000.00 USD |
| `4H` | `Crypto.com` | `46.49%` | `53.51%` | `0.87` | 577,160.00 USD |
| `4H` | `WhiteBIT` | `30.68%` | `69.32%` | `0.44` | 3,950,000.00 USD |
| `4H` | `HTX` | `52.65%` | `47.35%` | `1.11` | 12,500,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.17%` | `50.83%` | `0.97` | 1,660,000.00 USD |
| `4H` | `Aster` | `64.79%` | `35.21%` | `1.84` | 6,110,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.91%` | `46.09%` | `1.17` | 257,000.00 USD |
| `4H` | `Whale Positions` | `46.07%` | `53.93%` | `0.85` | 194,410,000.00 USD |
| `4H` | `Global Accounts` | `46.99%` | `53.01%` | `0.89` | 526,300,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0731` | `0.0734` | `0.0731` | `0.0753` | `0.0722` | 50,037,114.44 USD | 20,847,241.66 USD | 29,189,872.77 USD | -8,342,631.11 USD | `-16.67%` | `2B / 24S` |
| `0:00 UTC` | `0.0737` | `0.0733` | `0.0737` | `0.0739` | `0.0726` | 14,253,795.72 USD | 7,237,958.60 USD | 7,015,837.12 USD | 222,121.48 USD | `+1.56%` | `9B / 1S` |
| `5:00 UTC` | `0.0742` | `0.0741` | `0.0742` | `0.0744` | `0.0737` | 7,508,767.88 USD | 3,858,573.66 USD | 3,650,194.22 USD | 208,379.44 USD | `+2.78%` | `20B / 7S` |
| `0:00 UTC` | `0.0743` | `0.0743` | `0.0743` | `0.0746` | `0.0740` | 5,874,274.94 USD | 2,847,167.45 USD | 3,027,107.49 USD | -179,940.04 USD | `-3.06%` | `8B / 10S` |
| `5:00 UTC` | `0.0740` | `0.0741` | `0.0740` | `0.0745` | `0.0738` | 9,556,878.93 USD | 5,124,624.51 USD | 4,432,254.42 USD | 692,370.09 USD | `+7.24%` | `10B / 10S` |
| `0:00 UTC` | `0.0744` | `0.0740` | `0.0744` | `0.0745` | `0.0733` | 8,985,417.81 USD | 4,020,216.59 USD | 4,965,201.22 USD | -944,984.63 USD | `-10.52%` | `10B / 15S` |
| `5:00 UTC` | `0.0739` | `0.0740` | `0.0739` | `0.0743` | `0.0738` | 4,177,023.31 USD | 1,948,188.05 USD | 2,228,835.27 USD | -280,647.22 USD | `-6.72%` | `6B / 5S` |
| `0:00 UTC` | `0.0737` | `0.0739` | `0.0737` | `0.0743` | `0.0736` | 6,164,268.63 USD | 2,938,067.77 USD | 3,226,200.86 USD | -288,133.08 USD | `-4.67%` | `9B / 6S` |
| `5:00 UTC` | `0.0749` | `0.0747` | `0.0749` | `0.0751` | `0.0743` | 6,484,284.24 USD | 3,589,529.58 USD | 2,894,754.66 USD | 694,774.91 USD | `+10.71%` | `19B / 5S` |
| `0:00 UTC` | `0.0749` | `0.0750` | `0.0749` | `0.0751` | `0.0748` | 5,226,047.33 USD | 3,090,570.96 USD | 2,135,476.37 USD | 955,094.59 USD | `+18.28%` | `5B / 2S` |

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
| `5m` | 266,410.00 USD | 1,680,000.00 USD | **`ACCUMULATION`** |
| `15m` | 929,860.00 USD | 2,500,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,470,000.00 USD | 3,490,000.00 USD | **`ACCUMULATION`** |
| `1h` | 1,550,000.00 USD | 2,110,000.00 USD | **`ACCUMULATION`** |
| `2h` | 2,170,000.00 USD | 2,520,000.00 USD | **`ACCUMULATION`** |
| `4h` | -9,450,000.00 USD | -29,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -13,610,000.00 USD | -42,430,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -19,440,000.00 USD | -56,600,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -22,790,000.00 USD | -60,100,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -19,510,000.00 USD | -63,120,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -62,190,000.00 USD | -189,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -286,930,000.00 USD | -801,820,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+266.41K` | 15m=`+929.86K` | 1h=`+1.55M` | 24h=`-19.51M`
* Futures Capital Netflows: 5m=`+1.68M` | 15m=`+2.50M` | 1h=`+2.11M` | 24h=`-63.12M`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0731` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0689` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0836`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0799` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0652`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0757`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
