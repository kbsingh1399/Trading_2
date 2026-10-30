# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 10:34:48 IST` (`2026-10-30 05:04:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0750` | **Live Ask Quote**: `0.0772` | **Mid Price**: `0.0761`
- **Spread Points**: `22.00` | **Spread BPS**: `289.09 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0732` | VWAP Z-Score: `+1.89` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000588` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `54.40` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0759` | Lower -3.00σ Band: `0.0706`
  * Upper +2.51σ Band: `0.0754` | Lower -2.51σ Band: `0.0711`
  * Upper +2.01σ Band: `0.0750` | Lower -2.01σ Band: `0.0715`
  * Upper +2.00σ Band: `0.0750` | Lower -2.00σ Band: `0.0715`
  * Upper +1.28σ Band: `0.0744` | Lower -1.28σ Band: `0.0721`
  * Upper +1.00σ Band: `0.0741` | Lower -1.00σ Band: `0.0724`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0746` | EMA-20=`0.0744` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0752` (Slope: `+0.0000`) | EMA-100=`0.0761`
  * Institutional Anchors: EMA-144=`0.0765` | EMA-200=`0.0767` (Slope: `-0.3839`) | EMA-233=`0.0768`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `+0.57%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.69%`)
  * Value Area Low (VAL) = `0.0733` (Distance: `+3.95%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0788` | Weekly POC=`0.0762` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0752` | Low=`0.0749`
  * New York Session (13:00-21:00 UTC): High=`0.0766` | Low=`0.0756`
  * Initial Balance (First Hour): IB High=`0.0752` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0758` - `0.0764`
  * Optimal Trade Entry (OTE 0.705): `0.0763`
  * Structural Invalidation Anchor (0.786): `0.0767`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0763` | `0.0763` | `0.0762` | `0.0762` | `19,098,143` | 1,455,684.62 USD | 102,182.44 USD | `+7.02%` | -37,179,865.80 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0762` | `0.0762` | `0.0761` | `0.0761` | `15,368,069` | 1,170,628.64 USD | 240,546.81 USD | `+20.55%` | -36,939,318.99 USD | `+0.77` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0761` | `0.0764` | `0.0761` | `0.0762` | `22,538,331` | 1,717,483.48 USD | 406,894.09 USD | `+23.69%` | -36,532,424.89 USD | `+1.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0762` | `0.0764` | `0.0761` | `0.0763` | `47,959,023` | 3,656,750.71 USD | -253,302.19 USD | `-6.93%` | -37,891,419.23 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0762` | `0.0764` | `0.0761` | `0.0761` | `50,691,556` | 3,864,288.50 USD | 239,969.00 USD | `+6.21%` | -37,651,450.24 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0761` | `0.0764` | `0.0761` | `0.0762` | `22,538,331` | 1,717,483.48 USD | 406,894.09 USD | `+23.69%` | -37,244,556.14 USD | `+0.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0750` | `0.0761` | `0.0749` | `0.0760` | `234,282,632` | 17,698,778.29 USD | 1,647,184.38 USD | `+9.31%` | -33,266,558.06 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0760` | `0.0764` | `0.0756` | `0.0761` | `219,497,371` | 16,694,978.29 USD | -1,885,253.58 USD | `-11.29%` | -35,151,811.64 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0761` | `0.0764` | `0.0761` | `0.0762` | `22,538,331` | 1,717,483.48 USD | 406,894.09 USD | `+23.69%` | -34,744,917.55 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -24,481,648.11 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -29,910,488.74 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0764` | `0.0756` | `0.0762` | `242,043,135` | 18,413,028.46 USD | -1,477,815.97 USD | `-8.03%` | -31,388,304.71 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | 1,565,746.91 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -1,441,921.89 USD | `-0.70` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -24,481,648.11 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -29,910,488.74 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0764` | `0.0756` | `0.0762` | `242,043,135` | 18,413,028.46 USD | -1,477,815.97 USD | `-8.03%` | -31,388,304.71 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `ASK` | `0.0762` | `784009.0000` | 59,779.90 USD | 96,550.24 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `0.0762` | `43000.0000` | 3,278.66 USD | 36,770.34 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `0.0762` | `299032.0000` | 22,799.99 USD | 33,491.68 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `0.0762` | `140228.0000` | 10,691.68 USD | 10,691.68 USD | `6 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0762` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0762` | `26876.0000` | 2,049.13 USD | 2,049.13 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0762` | `2469.0000` | 188.19 USD | 2,237.33 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `17770.0000` | 1,354.46 USD | 3,591.79 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `656.0000` | 50.00 USD | 3,641.79 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `174.0000` | 13.26 USD | 3,655.05 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0762` | `5726.0000` | 436.40 USD | 4,091.45 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0762` | `9372.0000` | 714.24 USD | 4,805.69 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0762` | `446102.0000` | 33,995.65 USD | 38,801.34 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `0.0762` | `448431.0000` | 34,171.79 USD | 72,973.13 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0762` | `13117.0000` | 999.54 USD | 73,972.67 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0762` | `16830.0000` | 1,282.45 USD | 75,255.11 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0762` | `43120.0000` | 3,285.61 USD | 78,540.73 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0762` | `16510.0000` | 1,257.98 USD | 79,798.71 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0762` | `147518.0000` | 11,239.99 USD | 91,038.69 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0762` | `101623.0000` | 7,742.96 USD | 98,781.66 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0762` | `78981.0000` | 6,017.56 USD | 104,799.22 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `0.0762` | `189748.0000` | 14,456.52 USD | 119,255.74 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0762` | `3805.0000` | 289.89 USD | 119,545.63 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.0762` | `16830.0000` | 1,282.21 USD | 120,827.84 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.0762` | `137105.0000` | 10,445.34 USD | 131,273.18 USD | `1 orders` | `-0.08%` | `-` |
| `ASK` | `0.0763` | `70118.0000` | 5,348.39 USD | 174,745.36 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `16828.0000` | 1,283.57 USD | 169,396.97 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `63949.0000` | 4,877.52 USD | 168,113.40 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `144198.0000` | 10,998.13 USD | 163,235.88 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `16828.0000` | 1,283.47 USD | 152,237.75 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `10000.0000` | 762.68 USD | 150,954.28 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `3888.0000` | 296.53 USD | 150,191.60 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `161989.0000` | 12,354.25 USD | 149,895.07 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `26829.0000` | 2,046.11 USD | 137,540.82 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `21734.0000` | 1,657.52 USD | 135,494.71 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `75951.0000` | 5,792.25 USD | 133,837.19 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0763` | `268267.0000` | 20,458.58 USD | 128,044.93 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `0.0763` | `22354.0000` | 1,704.74 USD | 107,586.36 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0763` | `36497.0000` | 2,783.22 USD | 105,881.62 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0763` | `66201.0000` | 5,048.16 USD | 103,098.39 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `0.0763` | `19671.0000` | 1,499.99 USD | 98,050.24 USD | `1 orders` | `+0.01%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `303` | `0xb83d...6e36` | `SHORT` | 7,815,666.02 USD | `102,645,925.00` | `0.0946` | `0.0762` | `1.32` | 1,891,675.63 USD | `+24.20%` | `3X Cross` |
| `309` | `0xc63a...a3cd` | `LONG` | 7,624,900.00 USD | `100,000,000.00` | `0.0856` | `0.0762` | `0.000000` | -939,921.96 USD | `-12.33%` | `10X Cross` |
| `314` | `0x610b...b613` | `LONG` | 7,512,757.52 USD | `98,666,424.00` | `0.0872` | `0.0762` | `0.0601` | -1,087,424.38 USD | `-14.47%` | `5X Cross` |
| `603` | `0x5b5d...c060` | `SHORT` | 3,767,179.20 USD | `49,478,955.00` | `0.0946` | `0.0762` | `3.22` | 914,337.41 USD | `+24.27%` | `3X Cross` |
| `632` | `0xca49...53c8` | `SHORT` | 3,547,527.25 USD | `46,542,649.00` | `0.0929` | `0.0762` | `0.3882` | 778,517.43 USD | `+21.95%` | `10X Cross` |
| `645` | `0x45d2...4029` | `SHORT` | 3,463,005.68 USD | `45,426,000.00` | `0.0954` | `0.0762` | `0.9565` | 872,623.54 USD | `+25.20%` | `10X Cross` |
| `688` | `0xecb6...2b00` | `SHORT` | 3,267,032.67 USD | `42,860,945.00` | `0.0789` | `0.0762` | `0.6916` | 113,948.56 USD | `+3.49%` | `10X Cross` |
| `1186` | `0x458d...ab3b` | `LONG` | 1,862,005.72 USD | `24,454,063.00` | `0.1002` | `0.0762` | `0.0714` | -588,916.18 USD | `-31.63%` | `3X Isolated` |
| `1194` | `0xeadc...9d55` | `LONG` | 1,851,456.93 USD | `24,317,440.00` | `0.0926` | `0.0762` | `0.000000` | -400,137.65 USD | `-21.61%` | `10X Cross` |
| `1334` | `0xf48f...10fe` | `LONG` | 1,631,304.05 USD | `21,424,497.00` | `0.0968` | `0.0762` | `0.0442` | -443,000.56 USD | `-27.16%` | `4X Cross` |
| `1434` | `0x9946...0852` | `SHORT` | 1,529,223.10 USD | `20,059,331.00` | `0.0863` | `0.0762` | `0.1517` | 202,062.97 USD | `+13.21%` | `10X Cross` |
| `1543` | `0x9aa5...58af` | `SHORT` | 1,397,237.56 USD | `18,331,399.00` | `0.0907` | `0.0762` | `0.5632` | 264,842.79 USD | `+18.95%` | `10X Cross` |
| `1569` | `0xcac1...26b3` | `SHORT` | 1,380,503.50 USD | `18,126,835.00` | `0.0943` | `0.0762` | `0.5447` | 328,955.70 USD | `+23.83%` | `10X Cross` |
| `1597` | `0x0d6a...ca57` | `LONG` | 1,342,184.04 USD | `17,626,455.00` | `0.0875` | `0.0762` | `0.0626` | -199,920.92 USD | `-14.90%` | `3X Isolated` |
| `1657` | `0x4808...a82c` | `LONG` | 1,281,244.32 USD | `16,828,143.00` | `0.0883` | `0.0762` | `0.0632` | -205,228.66 USD | `-16.02%` | `3X Cross` |
| `1796` | `0x31ef...f715` | `LONG` | 1,159,574.28 USD | `15,230,102.00` | `0.0936` | `0.0762` | `0.0668` | -266,121.65 USD | `-22.95%` | `3X Isolated` |
| `1819` | `0xbfc7...80b4` | `SHORT` | 1,144,839.42 USD | `15,020,000.00` | `0.0920` | `0.0762` | `0.1780` | 237,559.87 USD | `+20.75%` | `10X Cross` |
| `1909` | `0x7cee...fc93` | `SHORT` | 1,068,120.54 USD | `14,013,468.00` | `0.0863` | `0.0762` | `0.2655` | 140,756.82 USD | `+13.18%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0776` | 6,955.21 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.96K USD at 0.0776 USD [API] | `2026-10-29 02:05:46` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+1.93%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.85%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+1.93%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.85%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+1.93%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.85%`)
  * 7D Horizon: Short MP=`0.0818` (Vol: 1,100,000.00 USD, Dist: `+7.42%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.85%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0158` | 3,940.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0176` | 1,050.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 251.46 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0188` | 603.20 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 1,490.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0204` | 2,280.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0227` | 141.19 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0231` | 900.08 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 278.28 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0237` | 2,580.00 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0242` | 12,460.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 369.37 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0254` | 4,020.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0256` | 22,920.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 140.28 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0265` | 529.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0267` | 161.26 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0268` | 1,000.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 880.12 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0278` | 4,250.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 265.80 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0319` | 549.83 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0330` | 757.85 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 49,950.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 476.56 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 6,400.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0348` | 13,540.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 4,710.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 700.21 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 8,390.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 35,290.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0382` | 1,810.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0384` | 353.40 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 206.74 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 2,180.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0401` | 4,020.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 56,970.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0411` | 5,020.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0411` | 34,120.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 44,200.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 8,550.00 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 27,590.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 954.87 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 122,100.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 149.46 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 967,320.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 27,930.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,610.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 15,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 789.72 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 25,960.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 95,490.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 18,030.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 13,640.00 USD | 14,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0469` | 1,210.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 2,360.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,010.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 1,290.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,330.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0486` | 506.45 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 16,470.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 314.48 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 8,470.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,660.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 308.55 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 931.86 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 7,900.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 5,350.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 315,950.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 2,230.00 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 6,280.00 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 187,290.00 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 9,840.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 11,120.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 1,240.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 1,890.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 4,820.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 6,420.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 257.62 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 3,030.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 341.67 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 2,510.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 4,010.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 63,470.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 1,820.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 567.50 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 10,800.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 7,630.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 441.75 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 5,840.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,140.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,300.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 16,800.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 4,560.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 1,230.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 356,270.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 5,960,000.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 2,070.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 5,110.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,510.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 548.71 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 1,210.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,620.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 1,250.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 10,210.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,530.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,310,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 4,770.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 5,600.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 150.01 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 17,100.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,990.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,280.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,180.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0650` | 2,470.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 7,620.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,050.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,370.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0674` | 15,350,000.00 USD | 15,350,000.00 USD | 77,630.00 USD | 9,710.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0675` | 15,260,000.00 USD | 15,260,000.00 USD | 40,430.00 USD | 9,210.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0676` | 15,200,000.00 USD | 15,200,000.00 USD | 45,230.00 USD | 65,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,880.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0677` | 15,090,000.00 USD | 15,090,000.00 USD | 3,410.00 USD | 19,140.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 15,050,000.00 USD | 15,050,000.00 USD | 15,920.00 USD | 39,890.00 USD | 65,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 14,920,000.00 USD | 14,920,000.00 USD | 28,320.00 USD | 38,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 14,860,000.00 USD | 14,860,000.00 USD | 18,300.00 USD | 9,760.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 14,820,000.00 USD | 14,820,000.00 USD | 17,070.00 USD | 27,520.00 USD | 139,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 117.29 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 14,640,000.00 USD | 14,640,000.00 USD | 2,550.00 USD | 33,950.00 USD | 20,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,650.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 14,580,000.00 USD | 14,580,000.00 USD | 15,780.00 USD | 26,860.00 USD | 23.24 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 14,540,000.00 USD | 14,540,000.00 USD | 24,150.00 USD | 15,070.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 80,430.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 14,500,000.00 USD | 14,500,000.00 USD | 58,140.00 USD | 13,720.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 13,120.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 14,410,000.00 USD | 14,410,000.00 USD | 44,450.00 USD | 8,860.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 34,970.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 14,340,000.00 USD | 14,340,000.00 USD | 9,250.00 USD | 16,550.00 USD | 29,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 870.75 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 14,260,000.00 USD | 14,260,000.00 USD | 9,350.00 USD | 0.00 USD | 827.41 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 14,240,000.00 USD | 14,240,000.00 USD | 1,460.00 USD | 0.00 USD | 670.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 14,240,000.00 USD | 14,240,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,970.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 14,220,000.00 USD | 14,220,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 14,200,000.00 USD | 14,200,000.00 USD | 27,810.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 14,170,000.00 USD | 14,170,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 14,170,000.00 USD | 14,170,000.00 USD | 31,720.00 USD | 13,590.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 11,090.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 14,110,000.00 USD | 14,110,000.00 USD | 14,010.00 USD | 10,800.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 14,070,000.00 USD | 14,070,000.00 USD | 83,570.00 USD | 27,620.00 USD | 31,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 13,930,000.00 USD | 13,930,000.00 USD | 141,150.00 USD | 21,100.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 13,730,000.00 USD | 13,730,000.00 USD | 51,480.00 USD | 115,140.00 USD | 15,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,310.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 13,550,000.00 USD | 13,550,000.00 USD | 87,840.00 USD | 36,120.00 USD | 59.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,480.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 13,420,000.00 USD | 13,420,000.00 USD | 175,640.00 USD | 66,830.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 13,160,000.00 USD | 13,160,000.00 USD | 24,140.00 USD | 45,140.00 USD | 22,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 13,070,000.00 USD | 13,070,000.00 USD | 42,970.00 USD | 30,720.00 USD | 64,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 12,930,000.00 USD | 12,930,000.00 USD | 21,850.00 USD | 1,120.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 423.90 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 12,900,000.00 USD | 12,900,000.00 USD | 140,160.00 USD | 70,030.00 USD | 45,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 12,640,000.00 USD | 12,640,000.00 USD | 75,260.00 USD | 62,000.00 USD | 122,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 12,380,000.00 USD | 12,380,000.00 USD | 43,490.00 USD | 84,200.00 USD | 148,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 12,110,000.00 USD | 12,110,000.00 USD | 125,310.00 USD | 99,310.00 USD | 141,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 5,240.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 11,740,000.00 USD | 11,740,000.00 USD | 42,650.00 USD | 25,670.00 USD | 44,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 2,160.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 11,630,000.00 USD | 11,630,000.00 USD | 159,040.00 USD | 46,690.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 11,420,000.00 USD | 11,420,000.00 USD | 70,910.00 USD | 85,230.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 11,200,000.00 USD | 11,200,000.00 USD | 118,420.00 USD | 51,930.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 5,410.00 USD | 397,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 10,980,000.00 USD | 10,980,000.00 USD | 73,470.00 USD | 238,460.00 USD | 40,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 391,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 10,630,000.00 USD | 10,630,000.00 USD | 19,480.00 USD | 51,080.00 USD | 270.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,170.00 USD | 383,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 10,560,000.00 USD | 10,560,000.00 USD | 232,360.00 USD | 96,160.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,270.00 USD | 382,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 10,230,000.00 USD | 10,230,000.00 USD | 55,690.00 USD | 101,030.00 USD | 15,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,070.00 USD | 360,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 10,060,000.00 USD | 10,060,000.00 USD | 226,040.00 USD | 45,330.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 359,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 9,710,000.00 USD | 9,710,000.00 USD | 135,290.00 USD | 50,600.00 USD | 69,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,160.00 USD | 357,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 9,460,000.00 USD | 9,460,000.00 USD | 308,410.00 USD | 298,040.00 USD | 65,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 345,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,790,000.00 USD | 8,790,000.00 USD | 179,490.00 USD | 119,590.00 USD | 147,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 322,050.00 USD | 322,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,340,000.00 USD | 8,340,000.00 USD | 82,600.00 USD | 258,330.00 USD | 323,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 626.77 USD | 626.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 7,670,000.00 USD | 7,670,000.00 USD | 105,730.00 USD | 206,000.00 USD | 370,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0725` | 6,990,000.00 USD | 6,990,000.00 USD | 234,040.00 USD | 201,810.00 USD | 268,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 6,290,000.00 USD | 6,290,000.00 USD | 29,310.00 USD | 90,560.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 6,160,000.00 USD | 6,160,000.00 USD | 138,060.00 USD | 83,300.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 5,930,000.00 USD | 5,930,000.00 USD | 27,890.00 USD | 84,500.00 USD | 27,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 5,790,000.00 USD | 5,790,000.00 USD | 42,630.00 USD | 26,380.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 5,710,000.00 USD | 5,710,000.00 USD | 105,290.00 USD | 25,850.00 USD | 42,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 5,530,000.00 USD | 5,530,000.00 USD | 26,590.00 USD | 52,750.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 5,450,000.00 USD | 5,450,000.00 USD | 41,070.00 USD | 18,640.00 USD | 68,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 50,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 5,270,000.00 USD | 5,270,000.00 USD | 339,370.00 USD | 67,440.00 USD | 258.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 4,870,000.00 USD | 4,870,000.00 USD | 141,790.00 USD | 23,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 4,700,000.00 USD | 4,700,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 4,460,000.00 USD | 4,460,000.00 USD | 113,510.00 USD | 47,850.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 4,250,000.00 USD | 4,250,000.00 USD | 83,080.00 USD | 23,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 4,140,000.00 USD | 4,140,000.00 USD | 54,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,090,000.00 USD | 4,090,000.00 USD | 54,250.00 USD | 0.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 68,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 133,790.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,770,000.00 USD | 3,770,000.00 USD | 174,420.00 USD | 40,680.00 USD | 245,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,310,000.00 USD | 3,310,000.00 USD | 185,610.00 USD | 89,270.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,930,000.00 USD | 2,930,000.00 USD | 54,460.00 USD | 31,200.00 USD | 35,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,810,000.00 USD | 2,810,000.00 USD | 53,190.00 USD | 32,230.00 USD | 162,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 2,560,000.00 USD | 2,560,000.00 USD | 625,700.00 USD | 225,930.00 USD | 178,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,530,000.00 USD | 1,530,000.00 USD | 105,880.00 USD | 0.00 USD | 208,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 68,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 37,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 24,430.00 USD | 12.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0754` | 928,580.00 USD | 928,580.00 USD | 0.00 USD | 103,430.00 USD | 278,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0755` | 546,770.00 USD | 546,770.00 USD | 182,850.00 USD | 180,020.00 USD | 570.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 183,340.00 USD | 183,340.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0757` | 153,240.00 USD | 153,240.00 USD | 130,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0758` | 22,660.00 USD | 22,660.00 USD | 15,180.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0759` | 2,560.00 USD | 2,560.00 USD | 0.00 USD | 0.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0761` | 191.60 USD | 191.60 USD | 0.00 USD | 0.00 USD | 191.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 1,140.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 72,120.00 USD | 72,120.00 USD | 4,000.00 USD | 65,170.00 USD | 675.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 819,280.00 USD | 819,280.00 USD | 356,880.00 USD | 390,100.00 USD | 168.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 1,400,000.00 USD | 1,400,000.00 USD | 233,890.00 USD | 248,870.00 USD | 99,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 2,550,000.00 USD | 2,550,000.00 USD | 586,470.00 USD | 522,700.00 USD | 40,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 3,300,000.00 USD | 3,300,000.00 USD | 246,530.00 USD | 337,770.00 USD | 160,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 4,230,000.00 USD | 4,230,000.00 USD | 241,290.00 USD | 93,770.00 USD | 594,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 5,200,000.00 USD | 5,200,000.00 USD | 259,990.00 USD | 422,240.00 USD | 287,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0770` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0770` | 6,180,000.00 USD | 6,180,000.00 USD | 396,020.00 USD | 183,310.00 USD | 402,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 7,000,000.00 USD | 7,000,000.00 USD | 252,610.00 USD | 343,810.00 USD | 229,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 8,270,000.00 USD | 8,270,000.00 USD | 390,170.00 USD | 170,860.00 USD | 709,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 8,840,000.00 USD | 8,840,000.00 USD | 129,080.00 USD | 228,140.00 USD | 204,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,180,000.00 USD | 9,180,000.00 USD | 86,950.00 USD | 217,280.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 9,600,000.00 USD | 9,600,000.00 USD | 255,450.00 USD | 121,970.00 USD | 48,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,100,000.00 USD | 10,100,000.00 USD | 249,550.00 USD | 157,720.00 USD | 86,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 10,800,000.00 USD | 10,800,000.00 USD | 258,860.00 USD | 301,970.00 USD | 145,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 11,470,000.00 USD | 11,470,000.00 USD | 64,490.00 USD | 230,760.00 USD | 369,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 11,950,000.00 USD | 11,950,000.00 USD | 223,060.00 USD | 119,670.00 USD | 143,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 12,220,000.00 USD | 12,220,000.00 USD | 174,020.00 USD | 53,140.00 USD | 38,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 12,570,000.00 USD | 12,570,000.00 USD | 151,030.00 USD | 193,800.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 12,810,000.00 USD | 12,810,000.00 USD | 70,430.00 USD | 82,140.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 13,240,000.00 USD | 13,240,000.00 USD | 45,800.00 USD | 214,890.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 13,700,000.00 USD | 13,700,000.00 USD | 316,220.00 USD | 101,430.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 14,100,000.00 USD | 14,100,000.00 USD | 205,570.00 USD | 110,520.00 USD | 82,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 14,740,000.00 USD | 14,740,000.00 USD | 234,330.00 USD | 160,700.00 USD | 245,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 15,810,000.00 USD | 15,810,000.00 USD | 329,770.00 USD | 386,280.00 USD | 355,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 3,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 16,240,000.00 USD | 16,240,000.00 USD | 135,470.00 USD | 191,940.00 USD | 102,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 16,850,000.00 USD | 16,850,000.00 USD | 296,490.00 USD | 218,540.00 USD | 100,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 17,070,000.00 USD | 17,070,000.00 USD | 136,170.00 USD | 57,780.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 17,450,000.00 USD | 17,450,000.00 USD | 179,540.00 USD | 105,210.00 USD | 95,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 17,700,000.00 USD | 17,700,000.00 USD | 145,760.00 USD | 37,510.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0793` | 423.67 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0793` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 17,950,000.00 USD | 17,950,000.00 USD | 115,990.00 USD | 41,370.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 18,040,000.00 USD | 18,040,000.00 USD | 24,520.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 18,230,000.00 USD | 18,230,000.00 USD | 174,010.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 18,640,000.00 USD | 18,640,000.00 USD | 206,810.00 USD | 89,760.00 USD | 114,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 18,810,000.00 USD | 18,810,000.00 USD | 56,190.00 USD | 110,930.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 19,340,000.00 USD | 19,340,000.00 USD | 157,480.00 USD | 193,600.00 USD | 176,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 19,490,000.00 USD | 19,490,000.00 USD | 39,790.00 USD | 9,760.00 USD | 96,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 19,500,000.00 USD | 19,500,000.00 USD | 17,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 19,520,000.00 USD | 19,520,000.00 USD | 18,910.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 19,620,000.00 USD | 19,620,000.00 USD | 16,230.00 USD | 43,340.00 USD | 37,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 19,650,000.00 USD | 19,650,000.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 19,810,000.00 USD | 19,810,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 20,080,000.00 USD | 20,080,000.00 USD | 24,270.00 USD | 21,040.00 USD | 217,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 20,480,000.00 USD | 20,480,000.00 USD | 221,690.00 USD | 145,040.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0808` | 215.60 USD | 4,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0808` | 21,350,000.00 USD | 21,350,000.00 USD | 297,680.00 USD | 118,270.00 USD | 457,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0809` | 215.87 USD | 4,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0809` | 21,890,000.00 USD | 21,890,000.00 USD | 252,300.00 USD | 275,640.00 USD | 12,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 22,430,000.00 USD | 22,430,000.00 USD | 252,220.00 USD | 157,180.00 USD | 132,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0810` | 118.33 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0811` | 22,770,000.00 USD | 22,770,000.00 USD | 98,200.00 USD | 229,260.00 USD | 11,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 23,090,000.00 USD | 23,090,000.00 USD | 138,630.00 USD | 102,020.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 23,280,000.00 USD | 23,280,000.00 USD | 43,130.00 USD | 33,440.00 USD | 110,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 23,650,000.00 USD | 23,650,000.00 USD | 44,610.00 USD | 109,560.00 USD | 217,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 23,790,000.00 USD | 23,790,000.00 USD | 42,020.00 USD | 6,740.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 24,510,000.00 USD | 24,510,000.00 USD | 342,130.00 USD | 194,790.00 USD | 177,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 25,060,000.00 USD | 25,060,000.00 USD | 284,640.00 USD | 136,360.00 USD | 130,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 25,790,000.00 USD | 25,790,000.00 USD | 261,840.00 USD | 161,260.00 USD | 308,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 4,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 26,390,000.00 USD | 26,390,000.00 USD | 161,320.00 USD | 312,480.00 USD | 128,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 26,960,000.00 USD | 26,960,000.00 USD | 68,970.00 USD | 177,510.00 USD | 319,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 27,370,000.00 USD | 27,370,000.00 USD | 176,870.00 USD | 87,420.00 USD | 147,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 27,930,000.00 USD | 27,930,000.00 USD | 256,340.00 USD | 151,600.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 28,280,000.00 USD | 28,280,000.00 USD | 270,020.00 USD | 72,540.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 28,850,000.00 USD | 28,850,000.00 USD | 172,520.00 USD | 204,930.00 USD | 191,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 29,100,000.00 USD | 29,100,000.00 USD | 102,430.00 USD | 125,690.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 29,530,000.00 USD | 29,530,000.00 USD | 131,950.00 USD | 125,260.00 USD | 170,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 29,640,000.00 USD | 29,640,000.00 USD | 28,890.00 USD | 62,110.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 29,980,000.00 USD | 29,980,000.00 USD | 197,110.00 USD | 75,940.00 USD | 65,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 30,220,000.00 USD | 30,220,000.00 USD | 157,080.00 USD | 88,230.00 USD | 121.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 30,360,000.00 USD | 30,360,000.00 USD | 57,230.00 USD | 37,820.00 USD | 42,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 30,420,000.00 USD | 30,420,000.00 USD | 31,420.00 USD | 0.00 USD | 32,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 8,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 30,740,000.00 USD | 30,740,000.00 USD | 154,910.00 USD | 75,990.00 USD | 80,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 8,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 31,100,000.00 USD | 31,100,000.00 USD | 110,470.00 USD | 82,770.00 USD | 169,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 31,450,000.00 USD | 31,450,000.00 USD | 119,430.00 USD | 94,190.00 USD | 137,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 31,810,000.00 USD | 31,810,000.00 USD | 114,510.00 USD | 183,090.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 32,060,000.00 USD | 32,060,000.00 USD | 44,050.00 USD | 63,220.00 USD | 145,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 32,280,000.00 USD | 32,280,000.00 USD | 132,640.00 USD | 31,430.00 USD | 51,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 10,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 32,570,000.00 USD | 32,570,000.00 USD | 171,590.00 USD | 77,480.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 32,670,000.00 USD | 32,670,000.00 USD | 52,570.00 USD | 16,550.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 32,720,000.00 USD | 32,720,000.00 USD | 11,570.00 USD | 15,480.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 128.58 USD | 10,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 426.71 USD | 11,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 11,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,450.00 USD | 15,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 16,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 16,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 16,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 17,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 17,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 24,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 25,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 30,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 30,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 31,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0943` | 1,140.00 USD | 32,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 72,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0948` | 4,260.00 USD | 76,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 101,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 761.26 USD | 101,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0955` | 48,900.00 USD | 150,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 151,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 151,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 152,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0995` | 2,910.00 USD | 154,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1002` | 201.80 USD | 155,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 162,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 165,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 166,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1023` | 3,170.00 USD | 169,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 175,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 176,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1084` | 1,860.00 USD | 178,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 181,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 181,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 181,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1158` | 131.49 USD | 181,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1218` | 2,370.00 USD | 184,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 637.53 USD | 184,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1236` | 119.32 USD | 184,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1249` | 1,240.00 USD | 186,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 186,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1283` | 926.56 USD | 187,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 187,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 189,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 189,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1325` | 45,330.00 USD | 234,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1336` | 34,500.00 USD | 269,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 269,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1346` | 134.42 USD | 269,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1378` | 6,240.00 USD | 275,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1384` | 22,450.00 USD | 298,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 100.35 USD | 298,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 299,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 301,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1434` | 1,900.00 USD | 302,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 303,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 304,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1470` | 2,060.00 USD | 306,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1472` | 441.45 USD | 307,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,180.00 USD | 315,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1487` | 6,480.00 USD | 321,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1500` | 24,130.00 USD | 345,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 1,320.00 USD | 347,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 16,640,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.92%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,630,000.00 USD | 0.00 USD | 407.02 USD | `-78.40%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,630,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.27%` | `319,394.00` |
| `Live` | `Long` | `0.0174` | 16,630,000.00 USD | 0.00 USD | 1,030.00 USD | `-77.22%` | `59,317.00` |
| `Live` | `Long` | `0.0180` | 16,630,000.00 USD | 0.00 USD | 1,350.00 USD | `-76.43%` | `75,012.00` |
| `Live` | `Long` | `0.0181` | 16,630,000.00 USD | 0.00 USD | 217.24 USD | `-76.17%` | `11,969.00` |
| `Live` | `Long` | `0.0184` | 16,630,000.00 USD | 0.00 USD | 2,040.00 USD | `-75.90%` | `111,254.00` |
| `Live` | `Long` | `0.0185` | 16,620,000.00 USD | 0.00 USD | 100.22 USD | `-75.77%` | `5,432.00` |
| `Live` | `Long` | `0.0187` | 16,620,000.00 USD | 0.00 USD | 600.00 USD | `-75.38%` | `32,000.00` |
| `Live` | `Long` | `0.0215` | 16,620,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.70%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,600,000.00 USD | 0.00 USD | 541.25 USD | `-71.57%` | `25,000.00` |
| `Live` | `Long` | `0.0222` | 16,600,000.00 USD | 0.00 USD | 138.08 USD | `-70.78%` | `6,206.00` |
| `Live` | `Long` | `0.0225` | 16,600,000.00 USD | 0.00 USD | 135.84 USD | `-70.52%` | `6,051.00` |
| `Live` | `Long` | `0.0226` | 16,600,000.00 USD | 0.00 USD | 356.18 USD | `-70.39%` | `15,795.00` |
| `Live` | `Long` | `0.0230` | 16,600,000.00 USD | 0.00 USD | 20,510.00 USD | `-69.86%` | `893,720.00` |
| `Live` | `Long` | `0.0232` | 16,580,000.00 USD | 0.00 USD | 907.89 USD | `-69.47%` | `39,049.00` |
| `Live` | `Long` | `0.0244` | 16,580,000.00 USD | 0.00 USD | 369.37 USD | `-68.02%` | `15,169.00` |
| `Live` | `Long` | `0.0253` | 16,580,000.00 USD | 0.00 USD | 16,630.00 USD | `-66.84%` | `658,606.00` |
| `Live` | `Long` | `0.0257` | 16,560,000.00 USD | 0.00 USD | 137.61 USD | `-66.19%` | `5,344.00` |
| `Live` | `Long` | `0.0259` | 16,560,000.00 USD | 0.00 USD | 834.90 USD | `-66.05%` | `32,298.00` |
| `Live` | `Long` | `0.0260` | 16,560,000.00 USD | 0.00 USD | 519.00 USD | `-65.92%` | `20,000.00` |
| `Live` | `Long` | `0.0277` | 16,560,000.00 USD | 0.00 USD | 1,030.00 USD | `-63.69%` | `37,344.00` |
| `Live` | `Long` | `0.0279` | 16,560,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.30%` | `61,775.00` |
| `Live` | `Long` | `0.0286` | 16,560,000.00 USD | 0.00 USD | 4,390.00 USD | `-62.38%` | `153,201.00` |
| `Live` | `Long` | `0.0295` | 16,560,000.00 USD | 0.00 USD | 510.12 USD | `-61.20%` | `17,263.00` |
| `Live` | `Long` | `0.0306` | 16,560,000.00 USD | 0.00 USD | 137.41 USD | `-59.88%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,560,000.00 USD | 0.00 USD | 265.80 USD | `-59.62%` | `8,644.00` |
| `Live` | `Long` | `0.0309` | 16,550,000.00 USD | 0.00 USD | 46,080.00 USD | `-59.36%` | `1,488,849.00` |
| `Live` | `Long` | `0.0324` | 16,510,000.00 USD | 0.00 USD | 746.35 USD | `-57.39%` | `23,000.00` |
| `Live` | `Long` | `0.0326` | 16,510,000.00 USD | 0.00 USD | 456.90 USD | `-57.26%` | `14,037.00` |
| `Live` | `Long` | `0.0330` | 16,510,000.00 USD | 0.00 USD | 6,190.00 USD | `-56.73%` | `187,979.00` |
| `Live` | `Long` | `0.0336` | 16,500,000.00 USD | 0.00 USD | 393.23 USD | `-55.81%` | `11,686.00` |
| `Live` | `Long` | `0.0345` | 16,500,000.00 USD | 0.00 USD | 4,650.00 USD | `-54.63%` | `134,443.00` |
| `Live` | `Long` | `0.0347` | 16,500,000.00 USD | 0.00 USD | 13,500.00 USD | `-54.50%` | `389,633.00` |
| `Live` | `Long` | `0.0358` | 16,480,000.00 USD | 0.00 USD | 214.53 USD | `-52.92%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,480,000.00 USD | 0.00 USD | 8,540.00 USD | `-52.79%` | `237,473.00` |
| `Live` | `Long` | `0.0367` | 16,470,000.00 USD | 0.00 USD | 34,910.00 USD | `-51.74%` | `950,000.00` |
| `Live` | `Long` | `0.0372` | 16,440,000.00 USD | 0.00 USD | 3,730.00 USD | `-51.08%` | `100,000.00` |
| `Live` | `Long` | `0.0374` | 16,440,000.00 USD | 0.00 USD | 1,770.00 USD | `-50.95%` | `47,501.00` |
| `Live` | `Long` | `0.0377` | 16,430,000.00 USD | 0.00 USD | 170.44 USD | `-50.43%` | `4,515.00` |
| `Live` | `Long` | `0.0381` | 16,430,000.00 USD | 0.00 USD | 1,770.00 USD | `-50.03%` | `46,629.00` |
| `Live` | `Long` | `0.0384` | 16,430,000.00 USD | 0.00 USD | 757.49 USD | `-49.64%` | `19,752.00` |
| `Live` | `Long` | `0.0384` | 16,430,000.00 USD | 0.00 USD | 205.67 USD | `-49.51%` | `5,349.00` |
| `Live` | `Long` | `0.0386` | 16,430,000.00 USD | 0.00 USD | 121.74 USD | `-49.38%` | `3,158.00` |
| `Live` | `Long` | `0.0393` | 16,430,000.00 USD | 0.00 USD | 2,180.00 USD | `-48.46%` | `55,633.00` |
| `Live` | `Long` | `0.0399` | 16,430,000.00 USD | 0.00 USD | 103.31 USD | `-47.54%` | `2,586.00` |
| `Live` | `Long` | `0.0401` | 16,430,000.00 USD | 0.00 USD | 21,090.00 USD | `-47.41%` | `526,651.00` |
| `Live` | `Long` | `0.0403` | 16,410,000.00 USD | 0.00 USD | 56,710.00 USD | `-47.01%` | `1,405,488.00` |
| `Live` | `Long` | `0.0404` | 16,350,000.00 USD | 0.00 USD | 115.12 USD | `-46.88%` | `2,846.00` |
| `Live` | `Long` | `0.0406` | 16,350,000.00 USD | 0.00 USD | 4,960.00 USD | `-46.75%` | `122,306.00` |
| `Live` | `Long` | `0.0408` | 16,350,000.00 USD | 0.00 USD | 419.28 USD | `-46.49%` | `10,289.00` |
| `Live` | `Long` | `0.0415` | 16,350,000.00 USD | 0.00 USD | 42,720.00 USD | `-45.57%` | `1,030,567.00` |
| `Live` | `Long` | `0.0415` | 16,300,000.00 USD | 0.00 USD | 1,170.00 USD | `-45.44%` | `28,233.00` |
| `Live` | `Long` | `0.0420` | 16,300,000.00 USD | 0.00 USD | 266.05 USD | `-44.91%` | `6,342.00` |
| `Live` | `Long` | `0.0420` | 16,300,000.00 USD | 0.00 USD | 930.52 USD | `-44.78%` | `22,129.00` |
| `Live` | `Long` | `0.0421` | 16,300,000.00 USD | 0.00 USD | 4,880.00 USD | `-44.65%` | `115,774.00` |
| `Live` | `Long` | `0.0423` | 16,300,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.52%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,290,000.00 USD | 0.00 USD | 267.52 USD | `-44.39%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,290,000.00 USD | 0.00 USD | 455.06 USD | `-44.25%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,290,000.00 USD | 0.00 USD | 883.34 USD | `-44.12%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,290,000.00 USD | 0.00 USD | 3,620.00 USD | `-43.99%` | `84,760.00` |
| `Live` | `Long` | `0.0428` | 16,290,000.00 USD | 0.00 USD | 110,940.00 USD | `-43.73%` | `2,589,112.00` |
| `Live` | `Long` | `0.0430` | 16,180,000.00 USD | 0.00 USD | 5,770.00 USD | `-43.60%` | `134,259.00` |
| `Live` | `Long` | `0.0432` | 16,170,000.00 USD | 0.00 USD | 10,120.00 USD | `-43.20%` | `233,977.00` |
| `Live` | `Long` | `0.0433` | 16,160,000.00 USD | 0.00 USD | 2,450.00 USD | `-43.07%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 16,160,000.00 USD | 0.00 USD | 937,320.00 USD | `-42.55%` | `21,424,497.00` |
| `Live` | `Long` | `0.0439` | 15,220,000.00 USD | 0.00 USD | 2,620.00 USD | `-42.42%` | `59,668.00` |
| `Live` | `Long` | `0.0440` | 15,220,000.00 USD | 0.00 USD | 750.58 USD | `-42.28%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 15,220,000.00 USD | 0.00 USD | 1,060.00 USD | `-42.15%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 15,220,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.76%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 15,120,000.00 USD | 0.00 USD | 444.76 USD | `-41.37%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 15,120,000.00 USD | 0.00 USD | 38,550.00 USD | `-41.23%` | `861,510.00` |
| `Live` | `Long` | `0.0449` | 15,080,000.00 USD | 0.00 USD | 810.81 USD | `-40.97%` | `18,038.00` |
| `Live` | `Long` | `0.0452` | 15,080,000.00 USD | 0.00 USD | 94,530.00 USD | `-40.71%` | `2,093,667.00` |
| `Live` | `Long` | `0.0454` | 14,980,000.00 USD | 0.00 USD | 2,170.00 USD | `-40.32%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,980,000.00 USD | 0.00 USD | 32,650.00 USD | `-40.18%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,950,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.92%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 14,940,000.00 USD | 0.00 USD | 10,300.00 USD | `-39.79%` | `224,650.00` |
| `Live` | `Long` | `0.0459` | 14,930,000.00 USD | 0.00 USD | 689.25 USD | `-39.66%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 14,930,000.00 USD | 0.00 USD | 4,500.00 USD | `-39.53%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,930,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.40%` | `28,207.00` |
| `Live` | `Long` | `0.0464` | 14,920,000.00 USD | 0.00 USD | 1,610.00 USD | `-39.13%` | `34,729.00` |
| `Live` | `Long` | `0.0464` | 14,920,000.00 USD | 0.00 USD | 16,780.00 USD | `-39.00%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,910,000.00 USD | 0.00 USD | 109.49 USD | `-38.74%` | `2,347.00` |
| `Live` | `Long` | `0.0469` | 14,910,000.00 USD | 0.00 USD | 13,620.00 USD | `-38.35%` | `290,000.00` |
| `Live` | `Long` | `0.0473` | 14,890,000.00 USD | 0.00 USD | 3,010.00 USD | `-37.95%` | `63,783.00` |
| `Live` | `Long` | `0.0476` | 14,890,000.00 USD | 0.00 USD | 2,380.00 USD | `-37.56%` | `50,080.00` |
| `Live` | `Long` | `0.0476` | 14,890,000.00 USD | 0.00 USD | 362.81 USD | `-37.43%` | `7,614.00` |
| `Live` | `Long` | `0.0481` | 14,890,000.00 USD | 0.00 USD | 56,440.00 USD | `-36.90%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,830,000.00 USD | 0.00 USD | 2,330.00 USD | `-36.77%` | `48,418.00` |
| `Live` | `Long` | `0.0483` | 14,830,000.00 USD | 0.00 USD | 1,780.00 USD | `-36.51%` | `36,742.00` |
| `Live` | `Long` | `0.0485` | 14,830,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.38%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 14,820,000.00 USD | 0.00 USD | 4,610.00 USD | `-35.85%` | `94,321.00` |
| `Live` | `Long` | `0.0490` | 14,820,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.72%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,810,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.59%` | `26,989.00` |
| `Live` | `Long` | `0.0495` | 14,810,000.00 USD | 0.00 USD | 5,120.00 USD | `-34.93%` | `103,291.00` |
| `Live` | `Long` | `0.0498` | 14,810,000.00 USD | 0.00 USD | 253.82 USD | `-34.67%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,810,000.00 USD | 0.00 USD | 806.66 USD | `-34.27%` | `16,117.00` |
| `Live` | `Long` | `0.0503` | 14,810,000.00 USD | 0.00 USD | 5,410.00 USD | `-34.01%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,800,000.00 USD | 0.00 USD | 40,680.00 USD | `-33.88%` | `808,039.00` |
| `Live` | `Long` | `0.0505` | 14,760,000.00 USD | 0.00 USD | 334.89 USD | `-33.75%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,760,000.00 USD | 0.00 USD | 1,040.00 USD | `-33.49%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,760,000.00 USD | 0.00 USD | 5,350.00 USD | `-33.36%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 535.43 USD | `-33.09%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 566.65 USD | `-32.96%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,750,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.83%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,740,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.70%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,740,000.00 USD | 0.00 USD | 27,480.00 USD | `-32.57%` | `535,213.00` |
| `Live` | `Long` | `0.0515` | 14,710,000.00 USD | 0.00 USD | 308.55 USD | `-32.44%` | `5,997.00` |
| `Live` | `Long` | `0.0515` | 14,710,000.00 USD | 0.00 USD | 395.70 USD | `-32.30%` | `7,676.00` |
| `Live` | `Long` | `0.0517` | 14,710,000.00 USD | 0.00 USD | 4,650.00 USD | `-32.17%` | `90,000.00` |
| `Live` | `Long` | `0.0519` | 14,710,000.00 USD | 0.00 USD | 6,570.00 USD | `-31.91%` | `126,763.00` |
| `Live` | `Long` | `0.0520` | 14,700,000.00 USD | 0.00 USD | 277.72 USD | `-31.78%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,700,000.00 USD | 0.00 USD | 4,420.00 USD | `-31.65%` | `84,852.00` |
| `Live` | `Long` | `0.0522` | 14,700,000.00 USD | 0.00 USD | 315,250.00 USD | `-31.39%` | `6,033,568.00` |
| `Live` | `Long` | `0.0524` | 14,380,000.00 USD | 0.00 USD | 2,230.00 USD | `-31.12%` | `42,425.00` |
| `Live` | `Long` | `0.0525` | 14,380,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.99%` | `119,430.00` |
| `Live` | `Long` | `0.0527` | 14,370,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.73%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,370,000.00 USD | 0.00 USD | 673.52 USD | `-30.60%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,370,000.00 USD | 0.00 USD | 182,740.00 USD | `-30.47%` | `3,451,252.00` |
| `Live` | `Long` | `0.0532` | 14,190,000.00 USD | 0.00 USD | 9,840.00 USD | `-30.20%` | `185,175.00` |
| `Live` | `Long` | `0.0532` | 14,180,000.00 USD | 0.00 USD | 8,100.00 USD | `-30.07%` | `152,035.00` |
| `Live` | `Long` | `0.0534` | 14,170,000.00 USD | 0.00 USD | 5,810.00 USD | `-29.94%` | `108,978.00` |
| `Live` | `Long` | `0.0534` | 14,160,000.00 USD | 0.00 USD | 1,890.00 USD | `-29.81%` | `35,411.00` |
| `Live` | `Long` | `0.0536` | 14,160,000.00 USD | 0.00 USD | 942.48 USD | `-29.68%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 14,160,000.00 USD | 0.00 USD | 1,590.00 USD | `-29.55%` | `29,631.00` |
| `Live` | `Long` | `0.0537` | 14,160,000.00 USD | 0.00 USD | 257.62 USD | `-29.42%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 14,160,000.00 USD | 0.00 USD | 5,630.00 USD | `-29.15%` | `104,280.00` |
| `Live` | `Long` | `0.0541` | 14,150,000.00 USD | 0.00 USD | 2,290.00 USD | `-29.02%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 14,150,000.00 USD | 0.00 USD | 3,030.00 USD | `-28.89%` | `55,906.00` |
| `Live` | `Long` | `0.0542` | 14,150,000.00 USD | 0.00 USD | 96,530.00 USD | `-28.76%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 14,050,000.00 USD | 0.00 USD | 23,640.00 USD | `-28.63%` | `435,000.00` |
| `Live` | `Long` | `0.0546` | 14,030,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.23%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 14,020,000.00 USD | 0.00 USD | 892.81 USD | `-28.10%` | `16,307.00` |
| `Live` | `Long` | `0.0551` | 14,020,000.00 USD | 0.00 USD | 1,760.00 USD | `-27.58%` | `31,888.00` |
| `Live` | `Long` | `0.0553` | 14,020,000.00 USD | 0.00 USD | 3,980.00 USD | `-27.45%` | `72,076.00` |
| `Live` | `Long` | `0.0556` | 14,020,000.00 USD | 0.00 USD | 907.02 USD | `-27.05%` | `16,328.00` |
| `Live` | `Long` | `0.0561` | 14,020,000.00 USD | 0.00 USD | 8,410.00 USD | `-26.40%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 14,010,000.00 USD | 0.00 USD | 144.08 USD | `-26.26%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 14,010,000.00 USD | 0.00 USD | 40,620.00 USD | `-26.13%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,970,000.00 USD | 0.00 USD | 351.85 USD | `-26.00%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,970,000.00 USD | 0.00 USD | 131.48 USD | `-25.74%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,970,000.00 USD | 0.00 USD | 567.50 USD | `-25.48%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,970,000.00 USD | 0.00 USD | 495.86 USD | `-25.21%` | `8,707.00` |
| `Live` | `Long` | `0.0570` | 13,970,000.00 USD | 0.00 USD | 8,350.00 USD | `-25.08%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,960,000.00 USD | 0.00 USD | 814.04 USD | `-24.95%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,960,000.00 USD | 0.00 USD | 7,570.00 USD | `-24.69%` | `132,022.00` |
| `Live` | `Long` | `0.0575` | 13,950,000.00 USD | 0.00 USD | 2,470.00 USD | `-24.56%` | `43,069.00` |
| `Live` | `Long` | `0.0575` | 13,950,000.00 USD | 0.00 USD | 3,960.00 USD | `-24.43%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 13,940,000.00 USD | 0.00 USD | 10,600.00 USD | `-24.29%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,930,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.16%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,920,000.00 USD | 0.00 USD | 3,940.00 USD | `-24.03%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,910,000.00 USD | 0.00 USD | 441.75 USD | `-23.90%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,910,000.00 USD | 0.00 USD | 431.14 USD | `-23.77%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,910,000.00 USD | 0.00 USD | 447.17 USD | `-23.64%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,910,000.00 USD | 0.00 USD | 582.50 USD | `-23.51%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,910,000.00 USD | 0.00 USD | 16,730.00 USD | `-23.37%` | `286,750.00` |
| `Live` | `Long` | `0.0585` | 13,900,000.00 USD | 0.00 USD | 5,840.00 USD | `-23.24%` | `100,000.00` |
| `Live` | `Long` | `0.0585` | 13,890,000.00 USD | 0.00 USD | 172.78 USD | `-23.11%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,890,000.00 USD | 0.00 USD | 4,560.00 USD | `-22.85%` | `77,552.00` |
| `Live` | `Long` | `0.0590` | 13,890,000.00 USD | 0.00 USD | 212.22 USD | `-22.59%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,880,000.00 USD | 0.00 USD | 26,980.00 USD | `-22.32%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,860,000.00 USD | 0.00 USD | 546.26 USD | `-22.06%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,860,000.00 USD | 0.00 USD | 4,510.00 USD | `-21.93%` | `75,899.00` |
| `Live` | `Long` | `0.0595` | 13,850,000.00 USD | 0.00 USD | 3,300.00 USD | `-21.80%` | `55,392.00` |
| `Live` | `Long` | `0.0597` | 13,850,000.00 USD | 0.00 USD | 838.23 USD | `-21.54%` | `14,029.00` |
| `Live` | `Long` | `0.0599` | 13,850,000.00 USD | 0.00 USD | 2,760.00 USD | `-21.41%` | `46,079.00` |
| `Live` | `Long` | `0.0600` | 13,850,000.00 USD | 0.00 USD | 6,990.00 USD | `-21.27%` | `116,520.00` |
| `Live` | `Long` | `0.0600` | 13,840,000.00 USD | 0.00 USD | 5,930,000.00 USD | `-21.14%` | `98,786,512.00` |
| `Live` | `Long` | `0.0602` | 7,910,000.00 USD | 0.00 USD | 8,490.00 USD | `-21.01%` | `141,093.00` |
| `Live` | `Long` | `0.0602` | 7,900,000.00 USD | 0.00 USD | 830.97 USD | `-20.88%` | `13,792.00` |
| `Live` | `Long` | `0.0604` | 7,900,000.00 USD | 0.00 USD | 548.46 USD | `-20.75%` | `9,088.00` |
| `Live` | `Long` | `0.0605` | 7,900,000.00 USD | 0.00 USD | 32,090.00 USD | `-20.49%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,860,000.00 USD | 0.00 USD | 622.63 USD | `-20.35%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 7,860,000.00 USD | 0.00 USD | 1,220.00 USD | `-20.22%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,860,000.00 USD | 0.00 USD | 376,580.00 USD | `-20.09%` | `6,188,726.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 5,110.00 USD | `-19.96%` | `83,914.00` |
| `Live` | `Long` | `0.0611` | 7,480,000.00 USD | 0.00 USD | 420.27 USD | `-19.83%` | `6,884.00` |
| `Live` | `Long` | `0.0612` | 7,480,000.00 USD | 0.00 USD | 629.72 USD | `-19.70%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,480,000.00 USD | 0.00 USD | 298.17 USD | `-19.57%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,480,000.00 USD | 0.00 USD | 655.16 USD | `-19.44%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,480,000.00 USD | 0.00 USD | 1,890.00 USD | `-19.17%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 11,100.00 USD | `-19.04%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 158.08 USD | `-18.91%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 27,580.00 USD | `-18.52%` | `444,421.00` |
| `Live` | `Long` | `0.0621` | 7,440,000.00 USD | 0.00 USD | 345.86 USD | `-18.38%` | `5,565.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.12%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 43,620.00 USD | `-17.99%` | `698,435.00` |
| `Live` | `Long` | `0.0625` | 7,390,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.86%` | `17,636,448.00` |
| `Live` | `Long` | `0.0626` | 6,290,000.00 USD | 0.00 USD | 870.40 USD | `-17.73%` | `13,893.00` |
| `Live` | `Long` | `0.0628` | 6,290,000.00 USD | 0.00 USD | 461.78 USD | `-17.60%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,290,000.00 USD | 0.00 USD | 6,400.00 USD | `-17.47%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,280,000.00 USD | 0.00 USD | 2,430.00 USD | `-17.20%` | `38,603.00` |
| `Live` | `Long` | `0.0631` | 6,280,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-17.07%` | `20,783,139.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.94%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.81%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.68%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-16.55%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 4,770.00 USD | `-16.41%` | `74,997.00` |
| `Live` | `Long` | `0.0638` | 4,940,000.00 USD | 0.00 USD | 5,600.00 USD | `-16.28%` | `87,791.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 23,220.00 USD | `-16.15%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,920,000.00 USD | 0.00 USD | 2,230.00 USD | `-16.02%` | `34,908.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 150.01 USD | `-15.89%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 3,870.00 USD | `-15.76%` | `60,258.00` |
| `Live` | `Long` | `0.0643` | 4,910,000.00 USD | 0.00 USD | 733.80 USD | `-15.63%` | `11,421.00` |
| `Live` | `Long` | `0.0644` | 4,910,000.00 USD | 0.00 USD | 76,280.00 USD | `-15.50%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,830,000.00 USD | 0.00 USD | 27,180.00 USD | `-15.36%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,810,000.00 USD | 0.00 USD | 631.94 USD | `-15.23%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,800,000.00 USD | 0.00 USD | 162,920.00 USD | `-14.97%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,640,000.00 USD | 0.00 USD | 8,800.00 USD | `-14.84%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,630,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.71%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,610,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.45%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,610,000.00 USD | 0.00 USD | 13,770.00 USD | `-14.31%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,590,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.92%` | `118,852.00` |
| `Live` | `Long` | `0.0657` | 4,590,000.00 USD | 0.00 USD | 14,160.00 USD | `-13.79%` | `215,665.00` |
| `Live` | `Long` | `0.0658` | 4,570,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.66%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,510,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.53%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 9,600.00 USD | `-13.39%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-13.13%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,480,000.00 USD | 0.00 USD | 1,630.00 USD | `-13.00%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,480,000.00 USD | 0.00 USD | 17,410.00 USD | `-12.87%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,460,000.00 USD | 0.00 USD | 11,590.00 USD | `-12.74%` | `174,492.00` |
| `Live` | `Long` | `0.0667` | 4,450,000.00 USD | 0.00 USD | 34,860.00 USD | `-12.48%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 11,690.00 USD | `-12.34%` | `175,092.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-12.21%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-12.08%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,250,000.00 USD | 0.00 USD | 9,050.00 USD | `-11.95%` | `134,979.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,500.00 USD | `-11.69%` | `141,218.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 15,370.00 USD | `-11.56%` | `228,139.00` |
| `Live` | `Long` | `0.0674` | 3,220,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.42%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,220,000.00 USD | 0.00 USD | 112,780.00 USD | `-11.29%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,110,000.00 USD | 0.00 USD | 12,610.00 USD | `-11.16%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 4,290.00 USD | `-11.03%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 34,090.00 USD | `-10.90%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,060,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.77%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,040,000.00 USD | 0.00 USD | 34,290.00 USD | `-10.64%` | `503,852.00` |
| `Live` | `Long` | `0.0682` | 3,000,000.00 USD | 0.00 USD | 49,480.00 USD | `-10.51%` | `726,014.00` |
| `Live` | `Long` | `0.0683` | 2,950,000.00 USD | 0.00 USD | 6,220.00 USD | `-10.37%` | `91,110.00` |
| `Live` | `Long` | `0.0684` | 2,950,000.00 USD | 0.00 USD | 80,430.00 USD | `-10.11%` | `1,174,961.00` |
| `Live` | `Long` | `0.0685` | 2,870,000.00 USD | 0.00 USD | 13,120.00 USD | `-9.98%` | `191,414.00` |
| `Live` | `Long` | `0.0687` | 2,860,000.00 USD | 0.00 USD | 595.81 USD | `-9.85%` | `8,679.00` |
| `Live` | `Long` | `0.0688` | 2,850,000.00 USD | 0.00 USD | 16,210.00 USD | `-9.72%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,840,000.00 USD | 0.00 USD | 1,000.00 USD | `-9.59%` | `14,570.00` |
| `Live` | `Long` | `0.0689` | 2,840,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.46%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,330,000.00 USD | 0.00 USD | 6,960.00 USD | `-9.32%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,320,000.00 USD | 0.00 USD | 13,510.00 USD | `-9.19%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 9,970.00 USD | `-9.06%` | `144,028.00` |
| `Live` | `Long` | `0.0693` | 2,300,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.93%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,300,000.00 USD | 0.00 USD | 8,070.00 USD | `-8.80%` | `116,243.00` |
| `Live` | `Long` | `0.0697` | 2,290,000.00 USD | 0.00 USD | 5,240.00 USD | `-8.54%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,280,000.00 USD | 0.00 USD | 6,680.00 USD | `-8.40%` | `95,809.00` |
| `Live` | `Long` | `0.0698` | 2,280,000.00 USD | 0.00 USD | 2,910.00 USD | `-8.27%` | `41,684.00` |
| `Live` | `Long` | `0.0699` | 2,270,000.00 USD | 0.00 USD | 1,310.00 USD | `-8.14%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,270,000.00 USD | 0.00 USD | 9,620.00 USD | `-8.01%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,260,000.00 USD | 0.00 USD | 8,310.00 USD | `-7.88%` | `118,427.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 1,070.00 USD | `-7.75%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,250,000.00 USD | 0.00 USD | 4,360.00 USD | `-7.62%` | `61,923.00` |
| `Live` | `Long` | `0.0704` | 2,250,000.00 USD | 0.00 USD | 216.56 USD | `-7.49%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 423.90 USD | `-7.22%` | `6,000.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 94,410.00 USD | `-7.09%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,150,000.00 USD | 0.00 USD | 821.60 USD | `-6.83%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,150,000.00 USD | 0.00 USD | 4,720.00 USD | `-6.70%` | `66,436.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 1,860.00 USD | `-6.57%` | `26,118.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 1,230.00 USD | `-6.43%` | `17,306.00` |
| `Live` | `Long` | `0.0713` | 2,150,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-6.30%` | `24,500,580.00` |
| `Live` | `Long` | `0.0714` | 397,910.00 USD | 0.00 USD | 5,410.00 USD | `-6.17%` | `75,723.00` |
| `Live` | `Long` | `0.0716` | 392,500.00 USD | 0.00 USD | 8,120.00 USD | `-6.04%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 384,380.00 USD | 0.00 USD | 1,170.00 USD | `-5.91%` | `16,291.00` |
| `Live` | `Long` | `0.0717` | 383,220.00 USD | 0.00 USD | 22,270.00 USD | `-5.78%` | `310,316.00` |
| `Live` | `Long` | `0.0718` | 360,950.00 USD | 0.00 USD | 1,720.00 USD | `-5.65%` | `23,887.00` |
| `Live` | `Long` | `0.0720` | 359,230.00 USD | 0.00 USD | 1,900.00 USD | `-5.52%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 357,340.00 USD | 0.00 USD | 12,310.00 USD | `-5.38%` | `170,786.00` |
| `Live` | `Long` | `0.0722` | 345,030.00 USD | 0.00 USD | 22,360.00 USD | `-5.25%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 322,680.00 USD | 0.00 USD | 322,050.00 USD | `-5.12%` | `4,457,443.00` |
| `Live` | `Long` | `0.0723` | 626.77 USD | 0.00 USD | 626.77 USD | `-4.99%` | `8,663.00` |
| `Live` | `Short` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | `+1.84%` | `3,107.00` |
| `Live` | `Short` | `0.0780` | 3,740.00 USD | 3,500.00 USD | 0.00 USD | `+2.36%` | `44,933.00` |
| `Live` | `Short` | `0.0788` | 3,860.00 USD | 113.24 USD | 0.00 USD | `+3.41%` | `1,438.00` |
| `Live` | `Short` | `0.0795` | 3,960.00 USD | 104.72 USD | 0.00 USD | `+4.33%` | `1,318.00` |
| `Live` | `Short` | `0.0799` | 4,080.00 USD | 116.73 USD | 0.00 USD | `+4.99%` | `1,460.00` |
| `Live` | `Short` | `0.0819` | 4,460.00 USD | 380.85 USD | 0.00 USD | `+7.49%` | `4,653.00` |
| `Live` | `Short` | `0.0832` | 7,910.00 USD | 3,450.00 USD | 0.00 USD | `+9.19%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 8,410.00 USD | 500.17 USD | 0.00 USD | `+9.32%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 8,710.00 USD | 293.44 USD | 0.00 USD | `+9.85%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 10,280.00 USD | 1,570.00 USD | 0.00 USD | `+9.98%` | `18,767.00` |
| `Live` | `Short` | `0.0843` | 10,540.00 USD | 264.21 USD | 0.00 USD | `+10.64%` | `3,136.00` |
| `Live` | `Short` | `0.0847` | 10,670.00 USD | 128.58 USD | 0.00 USD | `+11.16%` | `1,519.00` |
| `Live` | `Short` | `0.0848` | 11,100.00 USD | 426.71 USD | 0.00 USD | `+11.42%` | `5,029.00` |
| `Live` | `Short` | `0.0858` | 11,210.00 USD | 115.30 USD | 0.00 USD | `+12.74%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 15,660.00 USD | 4,450.00 USD | 0.00 USD | `+12.87%` | `51,791.00` |
| `Live` | `Short` | `0.0868` | 15,820.00 USD | 155.98 USD | 0.00 USD | `+14.05%` | `1,796.00` |
| `Live` | `Short` | `0.0871` | 15,960.00 USD | 138.58 USD | 0.00 USD | `+14.31%` | `1,592.00` |
| `Live` | `Short` | `0.0881` | 16,420.00 USD | 465.17 USD | 0.00 USD | `+15.63%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 16,840.00 USD | 411.53 USD | 0.00 USD | `+16.55%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 17,250.00 USD | 418.80 USD | 0.00 USD | `+16.94%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 17,540.00 USD | 285.70 USD | 0.00 USD | `+17.47%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 24,300.00 USD | 6,760.00 USD | 0.00 USD | `+18.78%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 25,610.00 USD | 1,310.00 USD | 0.00 USD | `+19.04%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 30,550.00 USD | 4,940.00 USD | 0.00 USD | `+19.70%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 30,720.00 USD | 171.49 USD | 0.00 USD | `+20.88%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 31,530.00 USD | 805.37 USD | 0.00 USD | `+22.32%` | `8,646.00` |
| `Live` | `Short` | `0.0934` | 31,780.00 USD | 249.24 USD | 0.00 USD | `+22.59%` | `2,670.00` |
| `Live` | `Short` | `0.0944` | 71,480.00 USD | 39,700.00 USD | 0.00 USD | `+23.90%` | `420,808.00` |
| `Live` | `Short` | `0.0946` | 72,400.00 USD | 921.51 USD | 0.00 USD | `+24.29%` | `9,736.00` |
| `Live` | `Short` | `0.0948` | 119,780.00 USD | 47,380.00 USD | 0.00 USD | `+24.43%` | `500,000.00` |
| `Live` | `Short` | `0.0950` | 144,240.00 USD | 24,460.00 USD | 0.00 USD | `+24.69%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 149,280.00 USD | 5,040.00 USD | 0.00 USD | `+24.82%` | `53,009.00` |
| `Live` | `Short` | `0.0955` | 149,480.00 USD | 194.44 USD | 0.00 USD | `+25.48%` | `2,035.00` |
| `Live` | `Short` | `0.0961` | 150,090.00 USD | 609.59 USD | 0.00 USD | `+26.26%` | `6,340.00` |
| `Live` | `Short` | `0.0972` | 151,260.00 USD | 1,170.00 USD | 0.00 USD | `+27.58%` | `12,089.00` |
| `Live` | `Short` | `0.0974` | 151,380.00 USD | 121.23 USD | 0.00 USD | `+27.97%` | `1,244.00` |
| `Live` | `Short` | `0.0980` | 154,250.00 USD | 2,860.00 USD | 0.00 USD | `+28.76%` | `29,217.00` |
| `Live` | `Short` | `0.0983` | 154,720.00 USD | 477.50 USD | 0.00 USD | `+29.02%` | `4,860.00` |
| `Live` | `Short` | `0.1014` | 162,350.00 USD | 7,630.00 USD | 0.00 USD | `+33.22%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 165,320.00 USD | 2,970.00 USD | 0.00 USD | `+33.49%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 165,810.00 USD | 492.85 USD | 0.00 USD | `+33.75%` | `4,839.00` |
| `Live` | `Short` | `0.1035` | 169,020.00 USD | 3,210.00 USD | 0.00 USD | `+35.85%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 175,130.00 USD | 6,110.00 USD | 0.00 USD | `+39.40%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 175,740.00 USD | 616.19 USD | 0.00 USD | `+41.37%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 178,980.00 USD | 3,240.00 USD | 0.00 USD | `+42.55%` | `29,849.00` |
| `Live` | `Short` | `0.1095` | 180,870.00 USD | 1,880.00 USD | 0.00 USD | `+43.86%` | `17,184.00` |
| `Live` | `Short` | `0.1127` | 181,080.00 USD | 214.15 USD | 0.00 USD | `+47.93%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 181,220.00 USD | 142.88 USD | 0.00 USD | `+48.33%` | `1,265.00` |
| `Live` | `Short` | `0.1137` | 181,370.00 USD | 147.86 USD | 0.00 USD | `+49.24%` | `1,301.00` |
| `Live` | `Short` | `0.1158` | 181,500.00 USD | 131.49 USD | 0.00 USD | `+52.13%` | `1,135.00` |
| `Live` | `Short` | `0.1222` | 182,140.00 USD | 637.53 USD | 0.00 USD | `+60.54%` | `5,215.00` |
| `Live` | `Short` | `0.1225` | 182,260.00 USD | 118.16 USD | 0.00 USD | `+60.80%` | `965.00` |
| `Live` | `Short` | `0.1245` | 183,490.00 USD | 1,240.00 USD | 0.00 USD | `+63.56%` | `9,926.00` |
| `Live` | `Short` | `0.1260` | 186,830.00 USD | 3,340.00 USD | 0.00 USD | `+65.40%` | `26,492.00` |
| `Live` | `Short` | `0.1270` | 186,940.00 USD | 108.80 USD | 0.00 USD | `+66.71%` | `857.00` |
| `Live` | `Short` | `0.1296` | 187,110.00 USD | 171.66 USD | 0.00 USD | `+70.26%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 189,250.00 USD | 2,140.00 USD | 0.00 USD | `+72.23%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 189,350.00 USD | 102.97 USD | 0.00 USD | `+73.15%` | `781.00` |
| `Live` | `Short` | `0.1328` | 223,680.00 USD | 34,320.00 USD | 0.00 USD | `+74.46%` | `258,360.00` |
| `Live` | `Short` | `0.1331` | 269,250.00 USD | 45,570.00 USD | 0.00 USD | `+74.85%` | `342,231.00` |
| `Live` | `Short` | `0.1338` | 269,450.00 USD | 205.31 USD | 0.00 USD | `+75.64%` | `1,535.00` |
| `Live` | `Short` | `0.1348` | 269,590.00 USD | 134.72 USD | 0.00 USD | `+77.08%` | `999.00` |
| `Live` | `Short` | `0.1371` | 275,800.00 USD | 6,210.00 USD | 0.00 USD | `+79.97%` | `45,319.00` |
| `Live` | `Short` | `0.1404` | 276,460.00 USD | 663.63 USD | 0.00 USD | `+84.44%` | `4,725.00` |
| `Live` | `Short` | `0.1414` | 299,380.00 USD | 22,920.00 USD | 0.00 USD | `+85.62%` | `162,180.00` |
| `Live` | `Short` | `0.1416` | 305,560.00 USD | 6,170.00 USD | 0.00 USD | `+85.88%` | `43,601.00` |
| `Live` | `Short` | `0.1432` | 307,420.00 USD | 1,860.00 USD | 0.00 USD | `+88.12%` | `13,010.00` |
| `Live` | `Short` | `0.1441` | 307,620.00 USD | 196.63 USD | 0.00 USD | `+89.17%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 322,920.00 USD | 15,300.00 USD | 0.00 USD | `+89.56%` | `106,016.00` |
| `Live` | `Short` | `0.1446` | 323,060.00 USD | 144.55 USD | 0.00 USD | `+89.82%` | `1,000.00` |
| `Live` | `Short` | `0.1451` | 324,890.00 USD | 1,820.00 USD | 0.00 USD | `+90.48%` | `12,559.00` |
| `Live` | `Short` | `0.1454` | 326,810.00 USD | 1,930.00 USD | 0.00 USD | `+91.00%` | `13,240.00` |
| `Live` | `Short` | `0.1472` | 327,250.00 USD | 441.75 USD | 0.00 USD | `+93.37%` | `3,000.00` |
| `Live` | `Short` | `0.1479` | 335,430.00 USD | 8,180.00 USD | 0.00 USD | `+94.16%` | `55,317.00` |
| `Live` | `Short` | `0.1482` | 337,510.00 USD | 2,070.00 USD | 0.00 USD | `+94.55%` | `14,000.00` |
| `Live` | `Short` | `0.1485` | 361,390.00 USD | 23,890.00 USD | 0.00 USD | `+95.08%` | `160,802.00` |
| `Live` | `Short` | `0.1497` | 362,700.00 USD | 1,300.00 USD | 0.00 USD | `+96.52%` | `8,712.00` |
| `Live` | `Short` | `0.1515` | 419,440.00 USD | 56,740.00 USD | 0.00 USD | `+99.02%` | `374,415.00` |
| `Live` | `Short` | `0.1517` | 419,930.00 USD | 492.26 USD | 0.00 USD | `+99.15%` | `3,246.00` |
| `Live` | `Short` | `0.1520` | 3,470,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+99.54%` | `20,059,331.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 654,540.00 USD | 0.00 USD | 375.42 USD | `-66.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 654,170.00 USD | 0.00 USD | 409.59 USD | `-47.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 653,760.00 USD | 0.00 USD | 132.68 USD | `-46.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 653,620.00 USD | 0.00 USD | 788.27 USD | `-45.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 652,840.00 USD | 0.00 USD | 527.05 USD | `-45.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 652,310.00 USD | 0.00 USD | 286.87 USD | `-40.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 652,020.00 USD | 0.00 USD | 252.42 USD | `-39.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 651,770.00 USD | 0.00 USD | 468.67 USD | `-38.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 651,300.00 USD | 0.00 USD | 5,160.00 USD | `-35.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 646,140.00 USD | 0.00 USD | 920.48 USD | `-35.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 645,220.00 USD | 0.00 USD | 236.01 USD | `-34.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 644,990.00 USD | 0.00 USD | 175.41 USD | `-32.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 644,810.00 USD | 0.00 USD | 242.96 USD | `-32.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 644,570.00 USD | 0.00 USD | 2,670.00 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 641,890.00 USD | 0.00 USD | 1,370.00 USD | `-27.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 640,520.00 USD | 0.00 USD | 437.58 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 640,080.00 USD | 0.00 USD | 183.30 USD | `-23.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 639,900.00 USD | 0.00 USD | 752.54 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 639,150.00 USD | 0.00 USD | 9,830.00 USD | `-22.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 629,320.00 USD | 0.00 USD | 1,020.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 628,300.00 USD | 0.00 USD | 668.84 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 627,630.00 USD | 0.00 USD | 273.90 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 627,360.00 USD | 0.00 USD | 8,800.00 USD | `-20.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 618,560.00 USD | 0.00 USD | 419.39 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 618,140.00 USD | 0.00 USD | 218.94 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 617,920.00 USD | 0.00 USD | 504.26 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 617,420.00 USD | 0.00 USD | 2,280.00 USD | `-18.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 615,140.00 USD | 0.00 USD | 118.27 USD | `-18.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 615,020.00 USD | 0.00 USD | 1,280.00 USD | `-18.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 613,740.00 USD | 0.00 USD | 1,820.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 611,920.00 USD | 0.00 USD | 1,340.00 USD | `-16.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 610,580.00 USD | 0.00 USD | 386.70 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 610,200.00 USD | 0.00 USD | 644.50 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 609,550.00 USD | 0.00 USD | 19,520.00 USD | `-14.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 590,040.00 USD | 0.00 USD | 1,410.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 588,630.00 USD | 0.00 USD | 3,140.00 USD | `-13.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 585,490.00 USD | 0.00 USD | 1,100.00 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 584,390.00 USD | 0.00 USD | 1,200.00 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 583,190.00 USD | 0.00 USD | 996.31 USD | `-13.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 582,190.00 USD | 0.00 USD | 909.85 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 581,280.00 USD | 0.00 USD | 115.57 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 581,170.00 USD | 0.00 USD | 33,620.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 547,540.00 USD | 0.00 USD | 12,860.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 534,680.00 USD | 0.00 USD | 1,540.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 533,140.00 USD | 0.00 USD | 108.08 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 533,030.00 USD | 0.00 USD | 19,540.00 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 513,490.00 USD | 0.00 USD | 1,430.00 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 512,060.00 USD | 0.00 USD | 8,540.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 503,520.00 USD | 0.00 USD | 8,580.00 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 494,950.00 USD | 0.00 USD | 4,970.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 489,980.00 USD | 0.00 USD | 3,100.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 486,880.00 USD | 0.00 USD | 160.31 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 486,720.00 USD | 0.00 USD | 38,710.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 448,020.00 USD | 0.00 USD | 27,690.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 420,320.00 USD | 0.00 USD | 3,190.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 417,130.00 USD | 0.00 USD | 533.09 USD | `-8.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 416,600.00 USD | 0.00 USD | 378.50 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 416,220.00 USD | 0.00 USD | 925.29 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 415,300.00 USD | 0.00 USD | 797.80 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 414,500.00 USD | 0.00 USD | 11,920.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 402,580.00 USD | 0.00 USD | 141.77 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 402,440.00 USD | 0.00 USD | 895.27 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 401,540.00 USD | 0.00 USD | 523.23 USD | `-7.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 401,020.00 USD | 0.00 USD | 468.88 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 400,550.00 USD | 0.00 USD | 235.12 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 400,320.00 USD | 0.00 USD | 1,090.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 399,230.00 USD | 0.00 USD | 71,660.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 327,570.00 USD | 0.00 USD | 497.62 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 327,070.00 USD | 0.00 USD | 20,330.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 306,740.00 USD | 0.00 USD | 608.76 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 306,130.00 USD | 0.00 USD | 16,880.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 289,250.00 USD | 0.00 USD | 265.67 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 288,990.00 USD | 0.00 USD | 1,670.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 287,310.00 USD | 0.00 USD | 4,210.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 283,110.00 USD | 0.00 USD | 13,550.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 269,560.00 USD | 0.00 USD | 413.42 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 269,140.00 USD | 0.00 USD | 138,380.00 USD | `-5.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 130,760.00 USD | 0.00 USD | 849.15 USD | `-5.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 129,910.00 USD | 0.00 USD | 34,460.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 95,450.00 USD | 0.00 USD | 2,030.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 93,420.00 USD | 0.00 USD | 1,950.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 91,470.00 USD | 0.00 USD | 2,540.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 88,930.00 USD | 0.00 USD | 4,110.00 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 84,810.00 USD | 0.00 USD | 2,090.00 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 82,720.00 USD | 0.00 USD | 1,950.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 80,770.00 USD | 0.00 USD | 535.16 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 80,240.00 USD | 0.00 USD | 227.92 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 80,010.00 USD | 0.00 USD | 397.76 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 79,610.00 USD | 0.00 USD | 398.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 79,210.00 USD | 0.00 USD | 797.39 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 78,420.00 USD | 0.00 USD | 38,550.00 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 39,870.00 USD | 0.00 USD | 1,640.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 38,230.00 USD | 0.00 USD | 189.57 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 38,040.00 USD | 0.00 USD | 1,480.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 36,560.00 USD | 0.00 USD | 2,900.00 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 33,660.00 USD | 0.00 USD | 415.62 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 33,250.00 USD | 0.00 USD | 16,520.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 16,730.00 USD | 0.00 USD | 3,180.00 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 13,550.00 USD | 0.00 USD | 375.86 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 13,170.00 USD | 0.00 USD | 399.17 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 12,770.00 USD | 0.00 USD | 140.04 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 12,630.00 USD | 0.00 USD | 151.47 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 12,480.00 USD | 0.00 USD | 3,450.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 9,030.00 USD | 0.00 USD | 736.17 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 8,290.00 USD | 0.00 USD | 406.95 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 7,890.00 USD | 0.00 USD | 221.00 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 7,670.00 USD | 0.00 USD | 407.73 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 7,260.00 USD | 0.00 USD | 408.57 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 6,850.00 USD | 0.00 USD | 408.81 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 6,440.00 USD | 0.00 USD | 4,520.00 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 1,930.00 USD | 0.00 USD | 504.10 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 1,420.00 USD | 0.00 USD | 398.13 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 1,020.00 USD | 0.00 USD | 216.21 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 806.81 USD | 0.00 USD | 806.81 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 814.81 USD | 814.81 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 4,590.00 USD | 3,770.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 4,700.00 USD | 109.63 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 5,940.00 USD | 1,250.00 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 6,130.00 USD | 183.50 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 6,970.00 USD | 843.94 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 7,470.00 USD | 502.52 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 8,290.00 USD | 816.05 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 8,560.00 USD | 266.52 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 10,800.00 USD | 2,240.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 11,040.00 USD | 240.02 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 14,970.00 USD | 3,930.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 15,380.00 USD | 407.23 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 15,700.00 USD | 321.13 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 17,190.00 USD | 1,490.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 19,430.00 USD | 2,240.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 19,760.00 USD | 329.23 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 20,070.00 USD | 303.77 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 20,250.00 USD | 186.07 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 23,330.00 USD | 3,080.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 24,310.00 USD | 975.23 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 28,680.00 USD | 4,370.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 28,840.00 USD | 157.14 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 28,970.00 USD | 130.71 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 70,570.00 USD | 41,610.00 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 70,720.00 USD | 141.44 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 71,490.00 USD | 773.68 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 72,180.00 USD | 687.81 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 77,760.00 USD | 5,580.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 82,360.00 USD | 4,600.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 87,620.00 USD | 5,270.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 95,440.00 USD | 7,820.00 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 95,750.00 USD | 312.56 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 96,210.00 USD | 455.34 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 96,340.00 USD | 125.45 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 96,570.00 USD | 230.40 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 96,880.00 USD | 319.16 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 97,890.00 USD | 1,010.00 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 120,640.00 USD | 22,750.00 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 121,040.00 USD | 400.91 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 121,240.00 USD | 200.46 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 121,500.00 USD | 259.13 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 122,210.00 USD | 707.08 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 131,220.00 USD | 9,010.00 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 228,000.00 USD | 96,780.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 228,800.00 USD | 807.50 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 229,060.00 USD | 257.18 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 229,490.00 USD | 424.74 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 229,590.00 USD | 101.80 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 230,970.00 USD | 1,380.00 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 233,000.00 USD | 2,030.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 234,430.00 USD | 1,430.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 234,560.00 USD | 129.67 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 235,580.00 USD | 1,020.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 235,830.00 USD | 256.05 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 236,860.00 USD | 1,030.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 239,880.00 USD | 3,020.00 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 240,210.00 USD | 327.80 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 240,670.00 USD | 457.92 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 241,360.00 USD | 691.29 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 242,160.00 USD | 800.79 USD | 0.00 USD | `+8.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 242,670.00 USD | 512.05 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 243,170.00 USD | 495.36 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 243,560.00 USD | 389.31 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 243,710.00 USD | 154.58 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 244,010.00 USD | 303.56 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 244,130.00 USD | 112.89 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 244,510.00 USD | 381.45 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 244,660.00 USD | 155.82 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 289,050.00 USD | 44,390.00 USD | 0.00 USD | `+9.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 289,190.00 USD | 138.69 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 290,450.00 USD | 1,260.00 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 290,560.00 USD | 107.03 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,860,000.00 USD | 1,570,000.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,860,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,860,000.00 USD | 1,470.00 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,860,000.00 USD | 107.71 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,870,000.00 USD | 2,690.00 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,870,000.00 USD | 529.92 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,870,000.00 USD | 219.07 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,870,000.00 USD | 242.84 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,880,000.00 USD | 10,140.00 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,880,000.00 USD | 876.11 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,880,000.00 USD | 812.54 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,880,000.00 USD | 126.76 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,880,000.00 USD | 307.41 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,880,000.00 USD | 614.09 USD | 0.00 USD | `+12.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,880,000.00 USD | 859.50 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,880,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,930,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 1,930,000.00 USD | 123.94 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 1,930,000.00 USD | 271.53 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 1,930,000.00 USD | 1,550.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 1,930,000.00 USD | 1,840.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 1,930,000.00 USD | 2,760.00 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 1,930,000.00 USD | 117.71 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 1,930,000.00 USD | 111.61 USD | 0.00 USD | `+15.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 1,940,000.00 USD | 571.18 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 1,940,000.00 USD | 375.94 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 1,940,000.00 USD | 627.55 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 1,940,000.00 USD | 211.04 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 1,940,000.00 USD | 108.36 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 1,940,000.00 USD | 543.32 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 1,940,000.00 USD | 1,820.00 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 1,940,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 1,960,000.00 USD | 17,680.00 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 1,960,000.00 USD | 1,370.00 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 1,970,000.00 USD | 5,630.00 USD | 0.00 USD | `+18.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 1,970,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 1,970,000.00 USD | 224.86 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 1,990,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 1,990,000.00 USD | 114.93 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 1,990,000.00 USD | 679.12 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 1,990,000.00 USD | 173.36 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 1,990,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 1,990,000.00 USD | 1,580.00 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 1,990,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 1,990,000.00 USD | 541.32 USD | 0.00 USD | `+21.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,130,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,130,000.00 USD | 691.07 USD | 0.00 USD | `+21.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,140,000.00 USD | 6,250.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,150,000.00 USD | 13,480.00 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,150,000.00 USD | 734.82 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,150,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,150,000.00 USD | 105.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,150,000.00 USD | 184.09 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,160,000.00 USD | 1,120.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,160,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,160,000.00 USD | 1,070.00 USD | 0.00 USD | `+23.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,160,000.00 USD | 512.15 USD | 0.00 USD | `+23.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,170,000.00 USD | 6,620.00 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,170,000.00 USD | 404.96 USD | 0.00 USD | `+24.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,170,000.00 USD | 129.85 USD | 0.00 USD | `+25.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,170,000.00 USD | 3,740.00 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,170,000.00 USD | 409.17 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,170,000.00 USD | 203.74 USD | 0.00 USD | `+26.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,170,000.00 USD | 2,800.00 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,180,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,180,000.00 USD | 694.56 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,180,000.00 USD | 940.91 USD | 0.00 USD | `+29.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,180,000.00 USD | 2,980.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,180,000.00 USD | 104.99 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,180,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,180,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,180,000.00 USD | 1,090.00 USD | 0.00 USD | `+30.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,180,000.00 USD | 438.96 USD | 0.00 USD | `+30.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,190,000.00 USD | 973.76 USD | 0.00 USD | `+30.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,200,000.00 USD | 10,000.00 USD | 0.00 USD | `+31.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,200,000.00 USD | 175.59 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,200,000.00 USD | 2,060.00 USD | 0.00 USD | `+31.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,200,000.00 USD | 482.89 USD | 0.00 USD | `+32.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,200,000.00 USD | 201.90 USD | 0.00 USD | `+32.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,200,000.00 USD | 489.46 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,200,000.00 USD | 103.68 USD | 0.00 USD | `+33.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,200,000.00 USD | 2,590.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,210,000.00 USD | 3,810.00 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,220,000.00 USD | 11,200.00 USD | 0.00 USD | `+34.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,220,000.00 USD | 4,330.00 USD | 0.00 USD | `+34.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,220,000.00 USD | 205.50 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,220,000.00 USD | 3,490.00 USD | 0.00 USD | `+35.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,230,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,230,000.00 USD | 207.50 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,230,000.00 USD | 813.88 USD | 0.00 USD | `+36.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,250,000.00 USD | 23,160.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,250,000.00 USD | 781.51 USD | 0.00 USD | `+37.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,250,000.00 USD | 209.30 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,250,000.00 USD | 1,440.00 USD | 0.00 USD | `+37.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,260,000.00 USD | 5,140.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,260,000.00 USD | 585.32 USD | 0.00 USD | `+38.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,260,000.00 USD | 210.90 USD | 0.00 USD | `+38.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,260,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,260,000.00 USD | 105.75 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,260,000.00 USD | 3,220.00 USD | 0.00 USD | `+39.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,270,000.00 USD | 1,600.00 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,270,000.00 USD | 212.90 USD | 0.00 USD | `+39.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,270,000.00 USD | 472.63 USD | 0.00 USD | `+40.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,270,000.00 USD | 214.50 USD | 0.00 USD | `+40.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,270,000.00 USD | 1,040.00 USD | 0.00 USD | `+41.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,270,000.00 USD | 136.12 USD | 0.00 USD | `+41.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,270,000.00 USD | 216.10 USD | 0.00 USD | `+41.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,270,000.00 USD | 1,010.00 USD | 0.00 USD | `+42.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,270,000.00 USD | 217.90 USD | 0.00 USD | `+43.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,270,000.00 USD | 219.70 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,280,000.00 USD | 7,780.00 USD | 0.00 USD | `+44.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,280,000.00 USD | 154.22 USD | 0.00 USD | `+45.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,280,000.00 USD | 221.30 USD | 0.00 USD | `+45.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,280,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,300,000.00 USD | 24,190.00 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,300,000.00 USD | 223.10 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,300,000.00 USD | 224.70 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,300,000.00 USD | 226.30 USD | 0.00 USD | `+48.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,300,000.00 USD | 950.34 USD | 0.00 USD | `+49.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,300,000.00 USD | 229.50 USD | 0.00 USD | `+50.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,310,000.00 USD | 771.08 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,310,000.00 USD | 942.95 USD | 0.00 USD | `+51.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,310,000.00 USD | 230.90 USD | 0.00 USD | `+51.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,310,000.00 USD | 288.18 USD | 0.00 USD | `+51.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,310,000.00 USD | 619.10 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,310,000.00 USD | 1,250.00 USD | 0.00 USD | `+52.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,310,000.00 USD | 1,050.00 USD | 0.00 USD | `+52.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,310,000.00 USD | 232.30 USD | 0.00 USD | `+52.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,310,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,310,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,320,000.00 USD | 3,730.00 USD | 0.00 USD | `+53.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,320,000.00 USD | 676.22 USD | 0.00 USD | `+54.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,320,000.00 USD | 648.25 USD | 0.00 USD | `+54.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,320,000.00 USD | 1,510.00 USD | 0.00 USD | `+55.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,320,000.00 USD | 448.52 USD | 0.00 USD | `+55.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,320,000.00 USD | 124.58 USD | 0.00 USD | `+55.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,320,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,320,000.00 USD | 691.80 USD | 0.00 USD | `+57.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,440,000.00 USD | 117,860.00 USD | 0.00 USD | `+57.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,440,000.00 USD | 143.22 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,440,000.00 USD | 1,380.00 USD | 0.00 USD | `+59.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,440,000.00 USD | 2,270.00 USD | 0.00 USD | `+60.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,440,000.00 USD | 871.99 USD | 0.00 USD | `+60.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,470,000.00 USD | 29,610.00 USD | 0.00 USD | `+66.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,470,000.00 USD | 400.21 USD | 0.00 USD | `+66.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,490,000.00 USD | 13,850.00 USD | 0.00 USD | `+73.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,490,000.00 USD | 2,360.00 USD | 0.00 USD | `+73.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,490,000.00 USD | 4,160.00 USD | 0.00 USD | `+78.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,490,000.00 USD | 114.70 USD | 0.00 USD | `+79.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,490,000.00 USD | 278.50 USD | 0.00 USD | `+83.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,500,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,500,000.00 USD | 173.57 USD | 0.00 USD | `+86.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,500,000.00 USD | 380.09 USD | 0.00 USD | `+86.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,510,000.00 USD | 17,150.00 USD | 0.00 USD | `+86.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,510,000.00 USD | 1,440.00 USD | 0.00 USD | `+89.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,520,000.00 USD | 433.35 USD | 0.00 USD | `+89.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,520,000.00 USD | 452.26 USD | 0.00 USD | `+91.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,520,000.00 USD | 3,640.00 USD | 0.00 USD | `+92.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,580,000.00 USD | 55,720.00 USD | 0.00 USD | `+94.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,580,000.00 USD | 2,120.00 USD | 0.00 USD | `+94.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,600,000.00 USD | 19,850.00 USD | 0.00 USD | `+96.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,600,000.00 USD | 1,620.00 USD | 0.00 USD | `+98.75%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0674` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 77,630.00 USD | 9,710.00 USD | 1,150.00 USD |
| `1D` | `0.0675` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 40,430.00 USD | 9,210.00 USD | 15,270.00 USD |
| `1D` | `0.0676` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 45,230.00 USD | 65,160.00 USD | 0.00 USD |
| `1D` | `0.0677` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 3,410.00 USD | 19,140.00 USD | 17,460.00 USD |
| `1D` | `0.0678` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 15,920.00 USD | 39,890.00 USD | 65,050.00 USD |
| `1D` | `0.0679` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 28,320.00 USD | 38,120.00 USD | 0.00 USD |
| `1D` | `0.0680` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 18,300.00 USD | 9,760.00 USD | 8,170.00 USD |
| `1D` | `0.0681` | 14,820,000.00 USD | 0.00 USD | 14,820,000.00 USD | 17,070.00 USD | 27,520.00 USD | 139,320.00 USD |
| `1D` | `0.0682` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 2,550.00 USD | 33,950.00 USD | 20,460.00 USD |
| `1D` | `0.0683` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 15,780.00 USD | 26,860.00 USD | 23.24 USD |
| `1D` | `0.0684` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 24,150.00 USD | 15,070.00 USD | 1,090.00 USD |
| `1D` | `0.0685` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 58,140.00 USD | 13,720.00 USD | 17,920.00 USD |
| `1D` | `0.0686` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 44,450.00 USD | 8,860.00 USD | 13,570.00 USD |
| `1D` | `0.0687` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 9,250.00 USD | 16,550.00 USD | 29,490.00 USD |
| `1D` | `0.0688` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0689` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 9,350.00 USD | 0.00 USD | 827.41 USD |
| `1D` | `0.0690` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 2,680.00 USD |
| `1D` | `0.0691` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 1,460.00 USD | 0.00 USD | 670.09 USD |
| `1D` | `0.0692` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0693` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0694` | 14,200,000.00 USD | 0.00 USD | 14,200,000.00 USD | 27,810.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `0.0695` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 31,720.00 USD | 13,590.00 USD | 17,260.00 USD |
| `1D` | `0.0698` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 14,010.00 USD | 10,800.00 USD | 9,960.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 83,570.00 USD | 27,620.00 USD | 31,880.00 USD |
| `1D` | `0.0700` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 141,150.00 USD | 21,100.00 USD | 36,740.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 51,480.00 USD | 115,140.00 USD | 15,660.00 USD |
| `1D` | `0.0702` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 87,840.00 USD | 36,120.00 USD | 59.13 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 175,640.00 USD | 66,830.00 USD | 17,020.00 USD |
| `1D` | `0.0704` | 13,160,000.00 USD | 0.00 USD | 13,160,000.00 USD | 24,140.00 USD | 45,140.00 USD | 22,880.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 42,970.00 USD | 30,720.00 USD | 64,540.00 USD |
| `1D` | `0.0706` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 21,850.00 USD | 1,120.00 USD | 14,210.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 12,900,000.00 USD | 0.00 USD | 12,900,000.00 USD | 140,160.00 USD | 70,030.00 USD | 45,320.00 USD |
| `1D` | `0.0708` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 75,260.00 USD | 62,000.00 USD | 122,470.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 43,490.00 USD | 84,200.00 USD | 148,980.00 USD |
| `1D` | `0.0710` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 125,310.00 USD | 99,310.00 USD | 141,510.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 42,650.00 USD | 25,670.00 USD | 44,800.00 USD |
| `1D` | `0.0712` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 159,040.00 USD | 46,690.00 USD | 1,970.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 70,910.00 USD | 85,230.00 USD | 62,360.00 USD |
| `1D` | `0.0714` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 118,420.00 USD | 51,930.00 USD | 46,120.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 73,470.00 USD | 238,460.00 USD | 40,960.00 USD |
| `1D` | `0.0716` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 19,480.00 USD | 51,080.00 USD | 270.12 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 232,360.00 USD | 96,160.00 USD | 3,010.00 USD |
| `1D` | `0.0718` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 55,690.00 USD | 101,030.00 USD | 15,780.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 226,040.00 USD | 45,330.00 USD | 71,020.00 USD |
| `1D` | `0.0720` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 135,290.00 USD | 50,600.00 USD | 69,850.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 308,410.00 USD | 298,040.00 USD | 65,900.00 USD |
| `1D` | `0.0722` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 179,490.00 USD | 119,590.00 USD | 147,760.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 82,600.00 USD | 258,330.00 USD | 323,490.00 USD |
| `1D` | `0.0724` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 105,730.00 USD | 206,000.00 USD | 370,530.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 234,040.00 USD | 201,810.00 USD | 268,220.00 USD |
| `1D` | `0.0726` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 29,310.00 USD | 90,560.00 USD | 8,200.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 138,060.00 USD | 83,300.00 USD | 12,350.00 USD |
| `1D` | `0.0728` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 27,890.00 USD | 84,500.00 USD | 27,820.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 42,630.00 USD | 26,380.00 USD | 8,540.00 USD |
| `1D` | `0.0730` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 105,290.00 USD | 25,850.00 USD | 42,180.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 26,590.00 USD | 52,750.00 USD | 1,840.00 USD |
| `1D` | `0.0732` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 41,070.00 USD | 18,640.00 USD | 68,980.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 0.00 USD | 50,690.00 USD | 0.00 USD |
| `1D` | `0.0734` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 339,370.00 USD | 67,440.00 USD | 258.52 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 141,790.00 USD | 23,950.00 USD | 0.00 USD |
| `1D` | `0.0736` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 113,510.00 USD | 47,850.00 USD | 49,860.00 USD |
| `1D` | `0.0738` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 83,080.00 USD | 23,440.00 USD | 0.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 54,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0740` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 54,250.00 USD | 0.00 USD | 34,130.00 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 0.00 USD | 68,120.00 USD | 0.00 USD |
| `1D` | `0.0742` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 133,790.00 USD | 25,300.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 174,420.00 USD | 40,680.00 USD | 245,490.00 USD |
| `1D` | `0.0744` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 185,610.00 USD | 89,270.00 USD | 107,270.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 54,460.00 USD | 31,200.00 USD | 35,110.00 USD |
| `1D` | `0.0746` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 53,190.00 USD | 32,230.00 USD | 162,980.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 625,700.00 USD | 225,930.00 USD | 178,560.00 USD |
| `1D` | `0.0748` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 105,880.00 USD | 0.00 USD | 208,610.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 68,350.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 37,490.00 USD | 0.00 USD |
| `1D` | `0.0752` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 24,430.00 USD | 12.26 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD |
| `1D` | `0.0754` | 928,580.00 USD | 0.00 USD | 928,580.00 USD | 0.00 USD | 103,430.00 USD | 278,380.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 546,770.00 USD | 0.00 USD | 546,770.00 USD | 182,850.00 USD | 180,020.00 USD | 570.06 USD |
| `1D` | `0.0756` | 183,340.00 USD | 0.00 USD | 183,340.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 153,240.00 USD | 0.00 USD | 153,240.00 USD | 130,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0758` | 22,660.00 USD | 0.00 USD | 22,660.00 USD | 15,180.00 USD | 4,920.00 USD | 0.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 2,560.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD | 0.00 USD | 2,370.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 191.60 USD | 0.00 USD | 191.60 USD | 0.00 USD | 0.00 USD | 191.60 USD |
| `1D` | `0.0762` | 1,140.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `0.0762` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 72,120.00 USD | 72,120.00 USD | 0.00 USD | 4,000.00 USD | 65,170.00 USD | 675.30 USD |
| `1D` | `0.0764` | 819,280.00 USD | 819,280.00 USD | 0.00 USD | 356,880.00 USD | 390,100.00 USD | 168.86 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 233,890.00 USD | 248,870.00 USD | 99,520.00 USD |
| `1D` | `0.0766` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 586,470.00 USD | 522,700.00 USD | 40,050.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 246,530.00 USD | 337,770.00 USD | 160,980.00 USD |
| `1D` | `0.0768` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 241,290.00 USD | 93,770.00 USD | 594,420.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 259,990.00 USD | 422,240.00 USD | 287,520.00 USD |
| `1D` | `0.0770` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 396,020.00 USD | 183,310.00 USD | 402,920.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 252,610.00 USD | 343,810.00 USD | 229,190.00 USD |
| `1D` | `0.0772` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 390,170.00 USD | 170,860.00 USD | 709,740.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 129,080.00 USD | 228,140.00 USD | 204,860.00 USD |
| `1D` | `0.0774` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 86,950.00 USD | 217,280.00 USD | 36,420.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 255,450.00 USD | 121,970.00 USD | 48,950.00 USD |
| `1D` | `0.0776` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 249,550.00 USD | 157,720.00 USD | 86,320.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 258,860.00 USD | 301,970.00 USD | 145,510.00 USD |
| `1D` | `0.0778` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 64,490.00 USD | 230,760.00 USD | 369,760.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 223,060.00 USD | 119,670.00 USD | 143,910.00 USD |
| `1D` | `0.0780` | 12,220,000.00 USD | 12,220,000.00 USD | 0.00 USD | 174,020.00 USD | 53,140.00 USD | 38,190.00 USD |
| `1D` | `0.0781` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 8,330.00 USD |
| `1D` | `0.0782` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 70,430.00 USD | 82,140.00 USD | 79,320.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 45,800.00 USD | 214,890.00 USD | 174,650.00 USD |
| `1D` | `0.0784` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 316,220.00 USD | 101,430.00 USD | 39,570.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 205,570.00 USD | 110,520.00 USD | 82,150.00 USD |
| `1D` | `0.0786` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 234,330.00 USD | 160,700.00 USD | 245,480.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 329,770.00 USD | 386,280.00 USD | 355,590.00 USD |
| `1D` | `0.0788` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 135,470.00 USD | 191,940.00 USD | 102,190.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 296,490.00 USD | 218,540.00 USD | 100,480.00 USD |
| `1D` | `0.0790` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 136,170.00 USD | 57,780.00 USD | 21,420.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 179,540.00 USD | 105,210.00 USD | 95,400.00 USD |
| `1D` | `0.0792` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 145,760.00 USD | 37,510.00 USD | 66,570.00 USD |
| `1D` | `0.0793` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `1D` | `0.0794` | 17,950,000.00 USD | 17,950,000.00 USD | 0.00 USD | 115,990.00 USD | 41,370.00 USD | 86,980.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 18,040,000.00 USD | 18,040,000.00 USD | 0.00 USD | 24,520.00 USD | 0.00 USD | 70,160.00 USD |
| `1D` | `0.0796` | 18,230,000.00 USD | 18,230,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 18,640,000.00 USD | 18,640,000.00 USD | 0.00 USD | 206,810.00 USD | 89,760.00 USD | 114,980.00 USD |
| `1D` | `0.0798` | 18,810,000.00 USD | 18,810,000.00 USD | 0.00 USD | 56,190.00 USD | 110,930.00 USD | 2,460.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 19,340,000.00 USD | 19,340,000.00 USD | 0.00 USD | 157,480.00 USD | 193,600.00 USD | 176,750.00 USD |
| `1D` | `0.0800` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 39,790.00 USD | 9,760.00 USD | 96,600.00 USD |
| `1D` | `0.0801` | 19,500,000.00 USD | 19,500,000.00 USD | 0.00 USD | 17,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0802` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 18,910.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 16,230.00 USD | 43,340.00 USD | 37,770.00 USD |
| `1D` | `0.0804` | 19,650,000.00 USD | 19,650,000.00 USD | 0.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 19,810,000.00 USD | 19,810,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD |
| `1D` | `0.0806` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 24,270.00 USD | 21,040.00 USD | 217,250.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 20,480,000.00 USD | 20,480,000.00 USD | 0.00 USD | 221,690.00 USD | 145,040.00 USD | 32,800.00 USD |
| `1D` | `0.0808` | 21,350,000.00 USD | 21,350,000.00 USD | 0.00 USD | 297,680.00 USD | 118,270.00 USD | 457,400.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 21,890,000.00 USD | 21,890,000.00 USD | 0.00 USD | 252,300.00 USD | 275,640.00 USD | 12,430.00 USD |
| `1D` | `0.0810` | 22,430,000.00 USD | 22,430,000.00 USD | 0.00 USD | 252,220.00 USD | 157,180.00 USD | 132,180.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 22,770,000.00 USD | 22,770,000.00 USD | 0.00 USD | 98,200.00 USD | 229,260.00 USD | 11,430.00 USD |
| `1D` | `0.0812` | 23,090,000.00 USD | 23,090,000.00 USD | 0.00 USD | 138,630.00 USD | 102,020.00 USD | 78,200.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 23,280,000.00 USD | 23,280,000.00 USD | 0.00 USD | 43,130.00 USD | 33,440.00 USD | 110,880.00 USD |
| `1D` | `0.0814` | 23,650,000.00 USD | 23,650,000.00 USD | 0.00 USD | 44,610.00 USD | 109,560.00 USD | 217,640.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 42,020.00 USD | 6,740.00 USD | 95,080.00 USD |
| `1D` | `0.0816` | 24,510,000.00 USD | 24,510,000.00 USD | 0.00 USD | 342,130.00 USD | 194,790.00 USD | 177,770.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 25,060,000.00 USD | 25,060,000.00 USD | 0.00 USD | 284,640.00 USD | 136,360.00 USD | 130,280.00 USD |
| `1D` | `0.0818` | 25,790,000.00 USD | 25,790,000.00 USD | 0.00 USD | 261,840.00 USD | 161,260.00 USD | 308,580.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 26,390,000.00 USD | 26,390,000.00 USD | 0.00 USD | 161,320.00 USD | 312,480.00 USD | 128,570.00 USD |
| `1D` | `0.0820` | 26,960,000.00 USD | 26,960,000.00 USD | 0.00 USD | 68,970.00 USD | 177,510.00 USD | 319,860.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 27,370,000.00 USD | 27,370,000.00 USD | 0.00 USD | 176,870.00 USD | 87,420.00 USD | 147,290.00 USD |
| `1D` | `0.0822` | 27,930,000.00 USD | 27,930,000.00 USD | 0.00 USD | 256,340.00 USD | 151,600.00 USD | 156,010.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 28,280,000.00 USD | 28,280,000.00 USD | 0.00 USD | 270,020.00 USD | 72,540.00 USD | 8,640.00 USD |
| `1D` | `0.0824` | 28,850,000.00 USD | 28,850,000.00 USD | 0.00 USD | 172,520.00 USD | 204,930.00 USD | 191,760.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 29,100,000.00 USD | 29,100,000.00 USD | 0.00 USD | 102,430.00 USD | 125,690.00 USD | 21,450.00 USD |
| `1D` | `0.0826` | 29,530,000.00 USD | 29,530,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 170,320.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 29,640,000.00 USD | 29,640,000.00 USD | 0.00 USD | 28,890.00 USD | 62,110.00 USD | 17,280.00 USD |
| `1D` | `0.0828` | 29,980,000.00 USD | 29,980,000.00 USD | 0.00 USD | 197,110.00 USD | 75,940.00 USD | 65,170.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 30,220,000.00 USD | 30,220,000.00 USD | 0.00 USD | 157,080.00 USD | 88,230.00 USD | 121.56 USD |
| `1D` | `0.0830` | 30,360,000.00 USD | 30,360,000.00 USD | 0.00 USD | 57,230.00 USD | 37,820.00 USD | 42,640.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 30,420,000.00 USD | 30,420,000.00 USD | 0.00 USD | 31,420.00 USD | 0.00 USD | 32,430.00 USD |
| `1D` | `0.0832` | 30,740,000.00 USD | 30,740,000.00 USD | 0.00 USD | 154,910.00 USD | 75,990.00 USD | 80,400.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 31,100,000.00 USD | 31,100,000.00 USD | 0.00 USD | 110,470.00 USD | 82,770.00 USD | 169,490.00 USD |
| `1D` | `0.0834` | 31,450,000.00 USD | 31,450,000.00 USD | 0.00 USD | 119,430.00 USD | 94,190.00 USD | 137,410.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 31,810,000.00 USD | 31,810,000.00 USD | 0.00 USD | 114,510.00 USD | 183,090.00 USD | 64,680.00 USD |
| `1D` | `0.0836` | 32,060,000.00 USD | 32,060,000.00 USD | 0.00 USD | 44,050.00 USD | 63,220.00 USD | 145,390.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 32,280,000.00 USD | 32,280,000.00 USD | 0.00 USD | 132,640.00 USD | 31,430.00 USD | 51,930.00 USD |
| `1D` | `0.0838` | 32,570,000.00 USD | 32,570,000.00 USD | 0.00 USD | 171,590.00 USD | 77,480.00 USD | 38,900.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 32,670,000.00 USD | 32,670,000.00 USD | 0.00 USD | 52,570.00 USD | 16,550.00 USD | 30,220.00 USD |
| `1D` | `0.0840` | 32,720,000.00 USD | 32,720,000.00 USD | 0.00 USD | 11,570.00 USD | 15,480.00 USD | 28,060.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
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
  * Total Open Interest: `1.06B` | Total OI Tokens: `13,874,915,431.7 DOGE`
  * 1h OI Change: `+0.18%` | 4h OI Change: `+3.50%` | 24h OI Change: `-5.52%`
  * Exchange Breakdown: Binance=`244.32M` | Bybit=`107.08M` | OKX=`110.56M` | Hyperliquid=`76.72M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.08K` | Last 24h: `35.55K` | Last 3d: `229.21K` | Last 7d: `310.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0069%` | **USDT OKX** | `-0.0063%` |
| **USDT Bybit** | `-0.0023%` | **USDT KuCoin** | `-0.0035%` |
| **USDT MEXC** | `0.0068%` | **USDT BingX** | `0.0064%` |
| **USDT Gate** | `0.0022%` | **USDT Bitget** | `0.0006%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `46.26%` | `53.74%` | `0.86` | 10,790,000.00 USD |
| `15M` | `Binance` | `43.06%` | `56.94%` | `0.76` | 6,970,000.00 USD |
| `15M` | `OKX` | `50.09%` | `49.91%` | `1.00` | 831,480.00 USD |
| `15M` | `Bybit` | `58.14%` | `41.86%` | `1.39` | 541,880.00 USD |
| `15M` | `KuCoin` | `54.04%` | `45.96%` | `1.18` | 160,420.00 USD |
| `15M` | `Gate` | `54.7%` | `45.3%` | `1.21` | 603,390.00 USD |
| `15M` | `Bitget` | `35.96%` | `64.04%` | `0.56` | 232,260.00 USD |
| `15M` | `BingX` | `36.67%` | `63.33%` | `0.58` | 381,800.00 USD |
| `15M` | `MEXC` | `51.24%` | `48.76%` | `1.05` | 116,410.00 USD |
| `15M` | `Bitunix` | `49.98%` | `50.02%` | `1.00` | 205,120.00 USD |
| `15M` | `Hyperliquid` | `64.43%` | `35.57%` | `1.81` | 409,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.59%` | `45.41%` | `1.20` | 47,560.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `1.21%` | `98.79%` | `0.01` | 15,990.00 USD |
| `15M` | `HTX` | `55.16%` | `44.84%` | `1.23` | 15,990.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `63%` | `37%` | `1.70` | 229,790.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.65%` | `54.35%` | `0.84` | 24,900.00 USD |
| `15M` | `Whale Positions` | `43.06%` | `56.94%` | `0.76` | 6,970,000.00 USD |
| `15M` | `Global Accounts` | `46.26%` | `53.74%` | `0.86` | 10,790,000.00 USD |
| `1H` | `DOGE` | `46.31%` | `53.69%` | `0.86` | 64,480,000.00 USD |
| `1H` | `Binance` | `44.38%` | `55.62%` | `0.80` | 42,030,000.00 USD |
| `1H` | `OKX` | `47.35%` | `52.65%` | `0.90` | 5,790,000.00 USD |
| `1H` | `Bybit` | `48.38%` | `51.62%` | `0.94` | 3,730,000.00 USD |
| `1H` | `KuCoin` | `49.51%` | `50.49%` | `0.98` | 587,810.00 USD |
| `1H` | `Gate` | `49.53%` | `50.47%` | `0.98` | 2,560,000.00 USD |
| `1H` | `Bitget` | `45.87%` | `54.13%` | `0.85` | 1,330,000.00 USD |
| `1H` | `BingX` | `40.22%` | `59.78%` | `0.67` | 1,440,000.00 USD |
| `1H` | `MEXC` | `57.13%` | `42.87%` | `1.33` | 1,090,000.00 USD |
| `1H` | `Bitunix` | `46.55%` | `53.45%` | `0.87` | 1,440,000.00 USD |
| `1H` | `Hyperliquid` | `33.23%` | `66.77%` | `0.50` | 2,510,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.83%` | `48.17%` | `1.08` | 187,970.00 USD |
| `1H` | `Crypto.com` | `40.44%` | `59.56%` | `0.68` | 0.00 USD |
| `1H` | `WhiteBIT` | `19.97%` | `80.03%` | `0.25` | 84,620.00 USD |
| `1H` | `HTX` | `41.67%` | `58.33%` | `0.71` | 221,410.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `39.25%` | `60.75%` | `0.65` | 1,090,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.17%` | `49.83%` | `1.01` | 394,320.00 USD |
| `1H` | `Whale Positions` | `44.38%` | `55.62%` | `0.80` | 42,030,000.00 USD |
| `1H` | `Global Accounts` | `46.31%` | `53.69%` | `0.86` | 64,480,000.00 USD |
| `4H` | `DOGE` | `50.68%` | `49.32%` | `1.03` | 1,490,000,000.00 USD |
| `4H` | `Binance` | `51.11%` | `48.89%` | `1.05` | 492,850,000.00 USD |
| `4H` | `OKX` | `53.04%` | `46.96%` | `1.13` | 305,460,000.00 USD |
| `4H` | `Bybit` | `52.02%` | `47.98%` | `1.08` | 135,300,000.00 USD |
| `4H` | `KuCoin` | `52.15%` | `47.85%` | `1.09` | 21,670,000.00 USD |
| `4H` | `Gate` | `49.22%` | `50.78%` | `0.97` | 89,140,000.00 USD |
| `4H` | `Bitget` | `54.12%` | `45.88%` | `1.18` | 56,980,000.00 USD |
| `4H` | `BingX` | `48.32%` | `51.68%` | `0.93` | 50,230,000.00 USD |
| `4H` | `MEXC` | `40.77%` | `59.23%` | `0.69` | 125,390,000.00 USD |
| `4H` | `Bitunix` | `47.4%` | `52.6%` | `0.90` | 72,570,000.00 USD |
| `4H` | `Hyperliquid` | `50.3%` | `49.7%` | `1.01` | 68,770,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `60.34%` | `39.66%` | `1.52` | 17,340,000.00 USD |
| `4H` | `Crypto.com` | `52.87%` | `47.13%` | `1.12` | 2,890,000.00 USD |
| `4H` | `WhiteBIT` | `66.6%` | `33.4%` | `1.99` | 12,600,000.00 USD |
| `4H` | `HTX` | `58.76%` | `41.24%` | `1.42` | 2,890,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `55.49%` | `44.51%` | `1.25` | 2,580,000.00 USD |
| `4H` | `Aster` | `54.81%` | `45.19%` | `1.21` | 13,220,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.64%` | `52.36%` | `0.91` | 16,220,000.00 USD |
| `4H` | `Whale Positions` | `51.11%` | `48.89%` | `1.05` | 492,850,000.00 USD |
| `4H` | `Global Accounts` | `50.68%` | `49.32%` | `1.03` | 1,490,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0749` | `0.0749` | `0.0749` | `0.0752` | `0.0748` | 4,286,041.88 USD | 2,098,889.29 USD | 2,187,152.59 USD | -88,263.30 USD | `-2.06%` | `4B / 13S` |
| `0:00 UTC` | `0.0751` | `0.0751` | `0.0751` | `0.0752` | `0.0749` | 4,647,855.36 USD | 2,795,154.23 USD | 1,852,701.13 USD | 942,453.10 USD | `+20.28%` | `6B / 2S` |
| `5:00 UTC` | `0.0753` | `0.0752` | `0.0753` | `0.0754` | `0.0750` | 3,128,035.72 USD | 1,829,490.22 USD | 1,298,545.51 USD | 530,944.71 USD | `+16.97%` | `7B / 3S` |
| `0:00 UTC` | `0.0758` | `0.0757` | `0.0758` | `0.0759` | `0.0754` | 5,177,761.26 USD | 2,608,553.38 USD | 2,569,207.88 USD | 39,345.50 USD | `+0.76%` | `6B / 5S` |
| `5:00 UTC` | `0.0761` | `0.0760` | `0.0761` | `0.0761` | `0.0758` | 4,745,125.96 USD | 2,439,783.51 USD | 2,305,342.45 USD | 134,441.06 USD | `+2.83%` | `2B / 3S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0761` | `0.0756` | 6,291,103.20 USD | 2,334,096.16 USD | 3,957,007.04 USD | -1,622,910.88 USD | `-25.80%` | `4B / 13S` |
| `5:00 UTC` | `0.0761` | `0.0761` | `0.0761` | `0.0763` | `0.0759` | 2,882,835.87 USD | 1,316,913.19 USD | 1,565,922.69 USD | -249,009.50 USD | `-8.64%` | `1B / 8S` |
| `0:00 UTC` | `0.0763` | `0.0763` | `0.0763` | `0.0764` | `0.0761` | 3,656,750.71 USD | 1,701,724.26 USD | 1,955,026.45 USD | -253,302.19 USD | `-6.93%` | `3B / 3S` |
| `5:00 UTC` | `0.0762` | `0.0762` | `0.0762` | `0.0764` | `0.0761` | 3,864,288.50 USD | 2,052,128.75 USD | 1,812,159.75 USD | 239,969.00 USD | `+6.21%` | `3B / 3S` |
| `0:00 UTC` | `0.0761` | `0.0761` | `0.0761` | `0.0762` | `0.0761` | 737,619.30 USD | 469,241.89 USD | 268,377.41 USD | 200,864.48 USD | `+27.23%` | `3B / 0S` |

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
| `5m` | -221,340.00 USD | 183,090.00 USD | **`DISTRIBUTION`** |
| `15m` | -165,920.00 USD | 375,710.00 USD | **`ACCUMULATION`** |
| `30m` | 428,390.00 USD | 97,450.00 USD | **`ACCUMULATION`** |
| `1h` | 395,440.00 USD | -2,240,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,030,000.00 USD | 2,390,000.00 USD | **`ACCUMULATION`** |
| `4h` | 3,020,000.00 USD | 1,550,000.00 USD | **`ACCUMULATION`** |
| `6h` | -7,210,000.00 USD | -21,160,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -8,370,000.00 USD | -53,700,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -20,190,000.00 USD | -55,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,800,000.00 USD | -63,680,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -59,690,000.00 USD | -185,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -283,980,000.00 USD | -797,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-221.34K` | 15m=`-165.92K` | 1h=`+395.44K` | 24h=`-18.80M`
* Futures Capital Netflows: 5m=`+183.09K` | 15m=`+375.71K` | 1h=`-2.24M` | 24h=`-63.68M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0733` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0693` (Risk Distance: `0.0044` pts)
  * +2.5R Take Profit: `0.0843`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0797` (Risk Distance: `0.0044` pts)
  * +2.5R Take Profit: `0.0647`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0767`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
