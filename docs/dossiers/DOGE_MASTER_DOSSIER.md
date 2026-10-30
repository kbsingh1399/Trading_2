# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 10:25:42 IST` (`2026-10-30 04:55:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0750` | **Live Ask Quote**: `0.0771` | **Mid Price**: `0.0761`
- **Spread Points**: `21.00` | **Spread BPS**: `276.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0761` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0766` | Lower -3.00σ Band: `0.0755`
  * Upper +2.51σ Band: `0.0765` | Lower -2.51σ Band: `0.0756`
  * Upper +2.01σ Band: `0.0764` | Lower -2.01σ Band: `0.0757`
  * Upper +2.00σ Band: `0.0764` | Lower -2.00σ Band: `0.0757`
  * Upper +1.28σ Band: `0.0763` | Lower -1.28σ Band: `0.0758`
  * Upper +1.00σ Band: `0.0762` | Lower -1.00σ Band: `0.0759`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0761` | EMA-20=`0.0761` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0761` (Slope: `+0.0000`) | EMA-100=`0.0761`
  * Institutional Anchors: EMA-144=`0.0761` | EMA-200=`0.0761` (Slope: `+0.0000`) | EMA-233=`0.0761`
- **Range Boundaries**: 24H High=`0.0768` | 24H Low=`0.0753` | Weekly High=`0.0776` | Weekly Low=`0.0745`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `+0.44%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.55%`)
  * Value Area Low (VAL) = `0.0732` (Distance: `+3.86%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0788` | Weekly POC=`0.0762` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0764` | Low=`0.0757`
  * New York Session (13:00-21:00 UTC): High=`0.0765` | Low=`0.0756`
  * Initial Balance (First Hour): IB High=`0.0763` | IB Low=`0.0758`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0757` - `0.0764`
  * Optimal Trade Entry (OTE 0.705): `0.0762`
  * Structural Invalidation Anchor (0.786): `0.0767`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0762` | `0.0764` | `0.0762` | `0.0762` | `26,835,442` | 2,046,829.79 USD | -95,786.61 USD | `-4.68%` | -36,369,467.93 USD | `-0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.0762` | `0.0763` | `0.0761` | `0.0762` | `13,921,817` | 1,060,735.06 USD | -99,625.33 USD | `-9.39%` | -36,469,093.25 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0762` | `0.0763` | `0.0762` | `0.0763` | `5,439,638` | 414,799.15 USD | 4,692.02 USD | `+1.13%` | -36,464,401.23 USD | `+0.17` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.0761` | `0.0762` | `0.0759` | `0.0762` | `37,876,989` | 2,882,835.87 USD | -249,009.50 USD | `-8.64%` | -36,812,916.25 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0762` | `0.0764` | `0.0761` | `0.0763` | `47,959,023` | 3,656,750.71 USD | -253,302.19 USD | `-6.93%` | -37,066,218.44 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0762` | `0.0764` | `0.0762` | `0.0762` | `33,348,334` | 2,543,060.50 USD | -124,455.59 USD | `-4.89%` | -37,190,674.04 USD | `+0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0740` | `0.0752` | `0.0736` | `0.0750` | `319,578,594` | 23,850,098.79 USD | 1,220,777.97 USD | `+5.12%` | -36,588,180.24 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0750` | `0.0761` | `0.0749` | `0.0760` | `234,282,632` | 17,698,778.29 USD | 1,647,184.38 USD | `+9.31%` | -34,940,995.87 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0760` | `0.0764` | `0.0756` | `0.0762` | `202,158,946` | 15,374,115.96 USD | -2,250,043.84 USD | `-14.64%` | -37,191,039.71 USD | `-0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -24,481,648.11 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -29,910,488.74 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0764` | `0.0756` | `0.0763` | `167,043,689` | 12,696,303.08 USD | -2,062,640.30 USD | `-16.25%` | -31,973,129.04 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | 1,565,746.91 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -1,441,921.89 USD | `-0.70` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -24,481,648.11 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -29,910,488.74 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0764` | `0.0756` | `0.0762` | `202,154,149` | 15,373,750.28 USD | -2,249,678.17 USD | `-14.63%` | -32,160,166.91 USD | `+0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `ASK` | `0.0762` | `75859.0000` | 5,784.10 USD | 17,262.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0762` | `16872.0000` | 1,286.39 USD | 11,478.22 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0762` | `3000.0000` | 228.73 USD | 10,191.83 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0762` | `77414.0000` | 5,902.04 USD | 9,963.10 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0762` | `53271.0000` | 4,061.06 USD | 4,061.06 USD | `3 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0762` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0762` | `28769.0000` | 2,193.15 USD | 2,193.15 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.0762` | `1394.0000` | 106.27 USD | 2,299.41 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0762` | `3065.0000` | 233.64 USD | 2,533.06 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0762` | `16932.0000` | 1,290.68 USD | 3,823.73 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0762` | `16932.0000` | 1,290.61 USD | 5,114.34 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0762` | `17966.0000` | 1,369.35 USD | 6,483.69 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0762` | `15458.0000` | 1,178.18 USD | 7,661.87 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `0.0762` | `147591.0000` | 11,248.94 USD | 18,910.81 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0762` | `10000.0000` | 762.14 USD | 19,672.95 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `416280.0000` | 31,725.95 USD | 51,398.90 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `55649.0000` | 4,241.12 USD | 55,640.02 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `91634.0000` | 6,983.34 USD | 62,623.36 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `123417.0000` | 9,405.36 USD | 72,028.72 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `16638.0000` | 1,267.93 USD | 73,296.65 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0762` | `147616.0000` | 11,248.93 USD | 84,545.58 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0762` | `26666.0000` | 2,032.03 USD | 86,577.61 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0762` | `448430.0000` | 34,170.81 USD | 120,748.43 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0762` | `25000.0000` | 1,905.00 USD | 122,653.43 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0762` | `49958.0000` | 3,806.75 USD | 126,460.18 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0762` | `24367.0000` | 1,856.72 USD | 128,316.89 USD | `1 orders` | `-0.05%` | `-` |
| `ASK` | `0.0763` | `264582.0000` | 20,179.40 USD | 158,069.26 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `0.0763` | `25556.0000` | 1,949.11 USD | 137,889.85 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `0.0763` | `19665.0000` | 1,499.79 USD | 135,940.75 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `19668.0000` | 1,500.00 USD | 134,440.96 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `19668.0000` | 1,499.98 USD | 132,940.96 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `19668.0000` | 1,499.96 USD | 131,440.98 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `590137.0000` | 45,005.62 USD | 129,941.02 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `164969.0000` | 12,580.87 USD | 84,935.40 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `20702.0000` | 1,578.76 USD | 72,354.53 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0763` | `22328.0000` | 1,702.73 USD | 70,775.78 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `406079.0000` | 30,965.96 USD | 69,073.04 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `16932.0000` | 1,291.13 USD | 38,107.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `137701.0000` | 10,500.11 USD | 36,815.95 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0763` | `10000.0000` | 762.52 USD | 26,315.84 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0763` | `108733.0000` | 8,291.00 USD | 25,553.32 USD | `2 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `304` | `0xb83d...6e36` | `SHORT` | 7,828,086.18 USD | `102,645,925.00` | `0.0946` | `0.0763` | `1.31` | 1,879,255.47 USD | `+24.01%` | `3X Cross` |
| `310` | `0xc63a...a3cd` | `LONG` | 7,627,200.00 USD | `100,000,000.00` | `0.0856` | `0.0763` | `0.000000` | -937,621.96 USD | `-12.29%` | `10X Cross` |
| `317` | `0x610b...b613` | `LONG` | 7,525,189.49 USD | `98,666,424.00` | `0.0872` | `0.0763` | `0.0601` | -1,074,992.41 USD | `-14.29%` | `5X Cross` |
| `602` | `0x5b5d...c060` | `SHORT` | 3,772,522.92 USD | `49,478,955.00` | `0.0946` | `0.0763` | `3.20` | 908,993.68 USD | `+24.10%` | `3X Cross` |
| `634` | `0xca49...53c8` | `SHORT` | 3,549,714.75 USD | `46,542,649.00` | `0.0929` | `0.0763` | `0.3885` | 776,329.93 USD | `+21.87%` | `10X Cross` |
| `644` | `0x45d2...4029` | `SHORT` | 3,463,914.20 USD | `45,426,000.00` | `0.0954` | `0.0763` | `0.9632` | 871,715.02 USD | `+25.17%` | `10X Cross` |
| `690` | `0xecb6...2b00` | `SHORT` | 3,269,051.17 USD | `42,859,874.00` | `0.0789` | `0.0763` | `0.6939` | 111,848.42 USD | `+3.42%` | `10X Cross` |
| `1185` | `0x458d...ab3b` | `LONG` | 1,865,086.93 USD | `24,454,063.00` | `0.1002` | `0.0763` | `0.0714` | -585,834.97 USD | `-31.41%` | `3X Isolated` |
| `1189` | `0xeadc...9d55` | `LONG` | 1,854,083.21 USD | `24,317,440.00` | `0.0926` | `0.0763` | `0.000000` | -397,511.36 USD | `-21.44%` | `10X Cross` |
| `1338` | `0xf48f...10fe` | `LONG` | 1,633,896.41 USD | `21,424,497.00` | `0.0968` | `0.0763` | `0.0436` | -440,408.19 USD | `-26.95%` | `4X Cross` |
| `1436` | `0x9946...0852` | `SHORT` | 1,529,724.58 USD | `20,059,331.00` | `0.0863` | `0.0763` | `0.1523` | 201,561.49 USD | `+13.18%` | `10X Cross` |
| `1541` | `0x9aa5...58af` | `SHORT` | 1,398,233.59 USD | `18,331,960.00` | `0.0907` | `0.0763` | `0.5617` | 263,897.63 USD | `+18.87%` | `10X Cross` |
| `1566` | `0xcac1...26b3` | `SHORT` | 1,382,352.44 USD | `18,126,835.00` | `0.0943` | `0.0763` | `0.5467` | 327,106.76 USD | `+23.66%` | `10X Cross` |
| `1595` | `0x0d6a...ca57` | `LONG` | 1,344,352.10 USD | `17,626,455.00` | `0.0875` | `0.0763` | `0.0626` | -197,752.86 USD | `-14.71%` | `3X Isolated` |
| `1651` | `0x4808...a82c` | `LONG` | 1,282,556.92 USD | `16,828,143.00` | `0.0883` | `0.0763` | `0.0632` | -203,916.06 USD | `-15.90%` | `3X Cross` |
| `1794` | `0x31ef...f715` | `LONG` | 1,161,219.13 USD | `15,230,102.00` | `0.0936` | `0.0763` | `0.0668` | -264,476.80 USD | `-22.78%` | `3X Isolated` |
| `1818` | `0xbfc7...80b4` | `SHORT` | 1,145,620.46 USD | `15,020,000.00` | `0.0920` | `0.0763` | `0.1799` | 236,778.83 USD | `+20.67%` | `10X Cross` |
| `1908` | `0x7cee...fc93` | `SHORT` | 1,068,849.24 USD | `14,013,468.00` | `0.0863` | `0.0763` | `0.2657` | 140,028.12 USD | `+13.10%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0776` | 6,955.21 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.96K USD at 0.0776 USD [API] | `2026-10-29 02:05:46` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.24%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.24%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.24%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
  * 7D Horizon: Short MP=`0.0818` (Vol: 1,100,000.00 USD, Dist: `+7.74%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.56%`)
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
| `1D` | `Long Liquidation` | `0.0672` | 15,320,000.00 USD | 15,320,000.00 USD | 4,130.00 USD | 7,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0673` | 15,310,000.00 USD | 15,310,000.00 USD | 6,250.00 USD | 704.90 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,370.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0674` | 15,300,000.00 USD | 15,300,000.00 USD | 69,290.00 USD | 9,000.00 USD | 166.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0675` | 15,230,000.00 USD | 15,230,000.00 USD | 40,430.00 USD | 9,210.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0676` | 15,160,000.00 USD | 15,160,000.00 USD | 45,230.00 USD | 65,160.00 USD | 234.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,880.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0677` | 15,050,000.00 USD | 15,050,000.00 USD | 3,410.00 USD | 19,140.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 15,010,000.00 USD | 15,010,000.00 USD | 15,920.00 USD | 39,890.00 USD | 64,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 14,890,000.00 USD | 14,890,000.00 USD | 28,320.00 USD | 38,120.00 USD | 827.41 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 14,820,000.00 USD | 14,820,000.00 USD | 18,300.00 USD | 9,760.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 14,790,000.00 USD | 14,790,000.00 USD | 17,070.00 USD | 27,520.00 USD | 138,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 117.29 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 14,600,000.00 USD | 14,600,000.00 USD | 2,550.00 USD | 33,950.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,650.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 14,540,000.00 USD | 14,540,000.00 USD | 15,780.00 USD | 26,860.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 14,500,000.00 USD | 14,500,000.00 USD | 24,150.00 USD | 15,070.00 USD | 338.82 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 80,430.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 14,460,000.00 USD | 14,460,000.00 USD | 58,140.00 USD | 13,720.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 13,120.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 14,370,000.00 USD | 14,370,000.00 USD | 44,450.00 USD | 8,860.00 USD | 13,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 34,970.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 14,300,000.00 USD | 14,300,000.00 USD | 9,250.00 USD | 16,550.00 USD | 29,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 870.75 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 14,220,000.00 USD | 14,220,000.00 USD | 9,350.00 USD | 0.00 USD | 670.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 14,210,000.00 USD | 14,210,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 14,210,000.00 USD | 14,210,000.00 USD | 23,110.00 USD | 0.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,970.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 14,180,000.00 USD | 14,180,000.00 USD | 18,220.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 14,160,000.00 USD | 14,160,000.00 USD | 27,810.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 14,140,000.00 USD | 14,140,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 14,130,000.00 USD | 14,130,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 11,090.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 14,070,000.00 USD | 14,070,000.00 USD | 14,010.00 USD | 10,800.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 14,040,000.00 USD | 14,040,000.00 USD | 83,570.00 USD | 27,620.00 USD | 32,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 13,890,000.00 USD | 13,890,000.00 USD | 141,150.00 USD | 21,100.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 13,690,000.00 USD | 13,690,000.00 USD | 51,480.00 USD | 115,140.00 USD | 15,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,310.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 13,510,000.00 USD | 13,510,000.00 USD | 87,840.00 USD | 36,120.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,480.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 13,380,000.00 USD | 13,380,000.00 USD | 175,640.00 USD | 66,830.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 13,130,000.00 USD | 13,130,000.00 USD | 25,820.00 USD | 45,140.00 USD | 20,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 13,030,000.00 USD | 13,030,000.00 USD | 50,870.00 USD | 30,720.00 USD | 68,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 12,880,000.00 USD | 12,880,000.00 USD | 21,850.00 USD | 1,120.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 423.90 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 12,850,000.00 USD | 12,850,000.00 USD | 140,160.00 USD | 70,030.00 USD | 45,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 12,590,000.00 USD | 12,590,000.00 USD | 75,260.00 USD | 62,000.00 USD | 123,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 12,330,000.00 USD | 12,330,000.00 USD | 43,490.00 USD | 84,200.00 USD | 147,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 12,050,000.00 USD | 12,050,000.00 USD | 125,310.00 USD | 99,310.00 USD | 141,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 5,240.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 11,690,000.00 USD | 11,690,000.00 USD | 42,650.00 USD | 25,670.00 USD | 42,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 2,160.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 11,580,000.00 USD | 11,580,000.00 USD | 159,040.00 USD | 46,690.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 11,370,000.00 USD | 11,370,000.00 USD | 70,910.00 USD | 85,230.00 USD | 65,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 11,150,000.00 USD | 11,150,000.00 USD | 118,420.00 USD | 51,930.00 USD | 50,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 5,410.00 USD | 397,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 10,930,000.00 USD | 10,930,000.00 USD | 73,470.00 USD | 238,460.00 USD | 40,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 391,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 10,580,000.00 USD | 10,580,000.00 USD | 19,480.00 USD | 51,080.00 USD | 148.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,170.00 USD | 383,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 10,510,000.00 USD | 10,510,000.00 USD | 232,360.00 USD | 96,160.00 USD | 46.48 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,270.00 USD | 382,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 10,180,000.00 USD | 10,180,000.00 USD | 55,690.00 USD | 101,030.00 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,070.00 USD | 360,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 10,010,000.00 USD | 10,010,000.00 USD | 226,040.00 USD | 45,330.00 USD | 69,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 359,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 9,670,000.00 USD | 9,670,000.00 USD | 135,290.00 USD | 50,600.00 USD | 69,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,160.00 USD | 357,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 9,410,000.00 USD | 9,410,000.00 USD | 308,410.00 USD | 298,040.00 USD | 70,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 345,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,730,000.00 USD | 8,730,000.00 USD | 179,490.00 USD | 119,590.00 USD | 154,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 322,050.00 USD | 322,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,280,000.00 USD | 8,280,000.00 USD | 82,600.00 USD | 258,330.00 USD | 326,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 626.77 USD | 626.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 7,610,000.00 USD | 7,610,000.00 USD | 105,730.00 USD | 206,000.00 USD | 370,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0725` | 6,930,000.00 USD | 6,930,000.00 USD | 234,040.00 USD | 201,810.00 USD | 268,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 6,230,000.00 USD | 6,230,000.00 USD | 29,310.00 USD | 90,560.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 6,100,000.00 USD | 6,100,000.00 USD | 138,060.00 USD | 83,300.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 5,860,000.00 USD | 5,860,000.00 USD | 27,890.00 USD | 84,500.00 USD | 27,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 5,720,000.00 USD | 5,720,000.00 USD | 42,630.00 USD | 26,380.00 USD | 8,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 5,650,000.00 USD | 5,650,000.00 USD | 105,290.00 USD | 25,850.00 USD | 42,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 5,470,000.00 USD | 5,470,000.00 USD | 26,590.00 USD | 52,750.00 USD | 89.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 5,390,000.00 USD | 5,390,000.00 USD | 26,690.00 USD | 18,640.00 USD | 60,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 50,690.00 USD | 100.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 5,240,000.00 USD | 5,240,000.00 USD | 339,370.00 USD | 67,440.00 USD | 1.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 4,830,000.00 USD | 4,830,000.00 USD | 141,790.00 USD | 23,950.00 USD | 258.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 4,660,000.00 USD | 4,660,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 4,420,000.00 USD | 4,420,000.00 USD | 113,510.00 USD | 47,850.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 4,210,000.00 USD | 4,210,000.00 USD | 83,080.00 USD | 23,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 4,100,000.00 USD | 4,100,000.00 USD | 54,600.00 USD | 0.00 USD | 263.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,050,000.00 USD | 4,050,000.00 USD | 54,250.00 USD | 0.00 USD | 34,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 68,120.00 USD | 510.72 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 133,790.00 USD | 24,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,730,000.00 USD | 3,730,000.00 USD | 174,420.00 USD | 40,680.00 USD | 245,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,270,000.00 USD | 3,270,000.00 USD | 185,610.00 USD | 89,270.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,890,000.00 USD | 2,890,000.00 USD | 54,460.00 USD | 31,200.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,770,000.00 USD | 2,770,000.00 USD | 53,190.00 USD | 32,230.00 USD | 162,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 2,520,000.00 USD | 2,520,000.00 USD | 625,700.00 USD | 225,930.00 USD | 164,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,510,000.00 USD | 1,510,000.00 USD | 77,120.00 USD | 0.00 USD | 209,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 69,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 37,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 12,650.00 USD | 142,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0754` | 932,640.00 USD | 932,640.00 USD | 0.00 USD | 103,430.00 USD | 278,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0755` | 550,840.00 USD | 550,840.00 USD | 182,850.00 USD | 180,020.00 USD | 167.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 187,800.00 USD | 187,800.00 USD | 0.00 USD | 30,100.00 USD | 791.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0757` | 156,910.00 USD | 156,910.00 USD | 130,570.00 USD | 0.00 USD | 1,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0758` | 24,890.00 USD | 24,890.00 USD | 15,180.00 USD | 4,920.00 USD | 570.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0759` | 4,220.00 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 974.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0760` | 3,240.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0762` | 1,190.00 USD | 1,190.00 USD | 0.00 USD | 0.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 69,170.00 USD | 69,170.00 USD | 4,000.00 USD | 65,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 138,340.00 USD | 138,340.00 USD | 4,000.00 USD | 65,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 887,370.00 USD | 887,370.00 USD | 356,880.00 USD | 390,100.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 1,470,000.00 USD | 1,470,000.00 USD | 233,890.00 USD | 248,870.00 USD | 100,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 2,640,000.00 USD | 2,640,000.00 USD | 602,560.00 USD | 522,700.00 USD | 40,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 3,450,000.00 USD | 3,450,000.00 USD | 302,280.00 USD | 352,540.00 USD | 160,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 4,380,000.00 USD | 4,380,000.00 USD | 241,290.00 USD | 93,770.00 USD | 594,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 5,350,000.00 USD | 5,350,000.00 USD | 259,990.00 USD | 422,240.00 USD | 286,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0770` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0770` | 6,330,000.00 USD | 6,330,000.00 USD | 396,020.00 USD | 183,310.00 USD | 402,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 7,160,000.00 USD | 7,160,000.00 USD | 252,610.00 USD | 343,810.00 USD | 228,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 8,430,000.00 USD | 8,430,000.00 USD | 390,170.00 USD | 170,860.00 USD | 711,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 8,990,000.00 USD | 8,990,000.00 USD | 129,080.00 USD | 228,140.00 USD | 204,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,330,000.00 USD | 9,330,000.00 USD | 86,950.00 USD | 217,280.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 9,760,000.00 USD | 9,760,000.00 USD | 255,450.00 USD | 121,970.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,250,000.00 USD | 10,250,000.00 USD | 249,550.00 USD | 157,720.00 USD | 86,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 10,940,000.00 USD | 10,940,000.00 USD | 258,860.00 USD | 301,970.00 USD | 129,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 11,580,000.00 USD | 11,580,000.00 USD | 35,730.00 USD | 230,760.00 USD | 369,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 12,060,000.00 USD | 12,060,000.00 USD | 223,060.00 USD | 119,670.00 USD | 142,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 12,330,000.00 USD | 12,330,000.00 USD | 174,020.00 USD | 53,140.00 USD | 39,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 12,680,000.00 USD | 12,680,000.00 USD | 151,030.00 USD | 193,800.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 12,920,000.00 USD | 12,920,000.00 USD | 70,430.00 USD | 82,140.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 13,350,000.00 USD | 13,350,000.00 USD | 45,800.00 USD | 214,890.00 USD | 174,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 13,810,000.00 USD | 13,810,000.00 USD | 316,220.00 USD | 101,430.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 14,210,000.00 USD | 14,210,000.00 USD | 205,570.00 USD | 110,520.00 USD | 78,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 14,840,000.00 USD | 14,840,000.00 USD | 234,330.00 USD | 160,700.00 USD | 242,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 15,920,000.00 USD | 15,920,000.00 USD | 329,770.00 USD | 386,280.00 USD | 355,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 3,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 16,350,000.00 USD | 16,350,000.00 USD | 135,470.00 USD | 191,940.00 USD | 102,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 16,970,000.00 USD | 16,970,000.00 USD | 296,490.00 USD | 218,540.00 USD | 106,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 17,180,000.00 USD | 17,180,000.00 USD | 136,170.00 USD | 57,780.00 USD | 22,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 17,560,000.00 USD | 17,560,000.00 USD | 179,540.00 USD | 105,210.00 USD | 94,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 17,810,000.00 USD | 17,810,000.00 USD | 145,760.00 USD | 37,510.00 USD | 59,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0793` | 423.67 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0793` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 46.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 18,030,000.00 USD | 18,030,000.00 USD | 101,610.00 USD | 41,370.00 USD | 84,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 18,130,000.00 USD | 18,130,000.00 USD | 24,520.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 18,320,000.00 USD | 18,320,000.00 USD | 174,010.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 18,730,000.00 USD | 18,730,000.00 USD | 206,810.00 USD | 89,760.00 USD | 117,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 18,900,000.00 USD | 18,900,000.00 USD | 56,190.00 USD | 110,930.00 USD | 677.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 19,500,000.00 USD | 19,500,000.00 USD | 213,230.00 USD | 193,600.00 USD | 197,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 19,650,000.00 USD | 19,650,000.00 USD | 39,790.00 USD | 9,760.00 USD | 94,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 19,670,000.00 USD | 19,670,000.00 USD | 17,000.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 19,690,000.00 USD | 19,690,000.00 USD | 18,910.00 USD | 1,770.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 19,790,000.00 USD | 19,790,000.00 USD | 16,230.00 USD | 43,340.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 19,810,000.00 USD | 19,810,000.00 USD | 13,900.00 USD | 10,910.00 USD | 755.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 19,980,000.00 USD | 19,980,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 20,240,000.00 USD | 20,240,000.00 USD | 24,270.00 USD | 21,040.00 USD | 215,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 20,640,000.00 USD | 20,640,000.00 USD | 221,690.00 USD | 145,040.00 USD | 30,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0808` | 215.60 USD | 4,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0808` | 21,510,000.00 USD | 21,510,000.00 USD | 297,680.00 USD | 118,270.00 USD | 457,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0809` | 215.87 USD | 4,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0809` | 22,050,000.00 USD | 22,050,000.00 USD | 252,300.00 USD | 275,640.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 22,600,000.00 USD | 22,600,000.00 USD | 252,220.00 USD | 157,180.00 USD | 134,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0810` | 118.33 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0811` | 22,930,000.00 USD | 22,930,000.00 USD | 98,200.00 USD | 229,260.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 23,250,000.00 USD | 23,250,000.00 USD | 138,630.00 USD | 102,020.00 USD | 78,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 23,450,000.00 USD | 23,450,000.00 USD | 47,340.00 USD | 33,440.00 USD | 120,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 23,840,000.00 USD | 23,840,000.00 USD | 44,610.00 USD | 109,560.00 USD | 227,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 23,980,000.00 USD | 23,980,000.00 USD | 42,020.00 USD | 6,740.00 USD | 94,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 24,690,000.00 USD | 24,690,000.00 USD | 342,130.00 USD | 194,790.00 USD | 177,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 25,250,000.00 USD | 25,250,000.00 USD | 284,640.00 USD | 136,360.00 USD | 130,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 25,980,000.00 USD | 25,980,000.00 USD | 261,840.00 USD | 161,260.00 USD | 308,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 4,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 26,580,000.00 USD | 26,580,000.00 USD | 161,320.00 USD | 312,480.00 USD | 128,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 27,150,000.00 USD | 27,150,000.00 USD | 68,970.00 USD | 177,510.00 USD | 320,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 27,560,000.00 USD | 27,560,000.00 USD | 180,240.00 USD | 87,420.00 USD | 147,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 28,130,000.00 USD | 28,130,000.00 USD | 256,340.00 USD | 151,600.00 USD | 155,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 28,480,000.00 USD | 28,480,000.00 USD | 270,020.00 USD | 72,540.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 29,040,000.00 USD | 29,040,000.00 USD | 172,520.00 USD | 204,930.00 USD | 191,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 29,290,000.00 USD | 29,290,000.00 USD | 102,430.00 USD | 125,690.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 29,720,000.00 USD | 29,720,000.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 29,830,000.00 USD | 29,830,000.00 USD | 28,890.00 USD | 62,110.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 30,170,000.00 USD | 30,170,000.00 USD | 197,110.00 USD | 75,940.00 USD | 65,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 30,420,000.00 USD | 30,420,000.00 USD | 157,080.00 USD | 88,230.00 USD | 168.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 30,550,000.00 USD | 30,550,000.00 USD | 57,230.00 USD | 37,820.00 USD | 42,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 30,620,000.00 USD | 30,620,000.00 USD | 31,420.00 USD | 0.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 8,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 30,930,000.00 USD | 30,930,000.00 USD | 154,910.00 USD | 75,990.00 USD | 79,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 8,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 31,290,000.00 USD | 31,290,000.00 USD | 110,470.00 USD | 82,770.00 USD | 169,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 31,640,000.00 USD | 31,640,000.00 USD | 121,950.00 USD | 94,190.00 USD | 138,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 32,010,000.00 USD | 32,010,000.00 USD | 114,510.00 USD | 183,090.00 USD | 65,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 32,260,000.00 USD | 32,260,000.00 USD | 44,050.00 USD | 63,220.00 USD | 145,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 32,470,000.00 USD | 32,470,000.00 USD | 132,640.00 USD | 31,430.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 10,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 32,760,000.00 USD | 32,760,000.00 USD | 171,590.00 USD | 77,480.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 32,860,000.00 USD | 32,860,000.00 USD | 52,570.00 USD | 16,550.00 USD | 30,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 32,920,000.00 USD | 32,920,000.00 USD | 11,570.00 USD | 15,480.00 USD | 28,060.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0158` | 16,690,000.00 USD | 0.00 USD | 3,940.00 USD | `-79.23%` | `250,000.00` |
| `Live` | `Long` | `0.0160` | 16,680,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.83%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,680,000.00 USD | 0.00 USD | 407.02 USD | `-78.30%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,680,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.17%` | `319,394.00` |
| `Live` | `Long` | `0.0176` | 16,670,000.00 USD | 0.00 USD | 1,050.00 USD | `-76.72%` | `59,317.00` |
| `Live` | `Long` | `0.0186` | 16,670,000.00 USD | 0.00 USD | 251.46 USD | `-75.40%` | `13,483.00` |
| `Live` | `Long` | `0.0188` | 16,670,000.00 USD | 0.00 USD | 603.20 USD | `-75.14%` | `32,000.00` |
| `Live` | `Long` | `0.0198` | 16,670,000.00 USD | 0.00 USD | 1,490.00 USD | `-73.82%` | `75,012.00` |
| `Live` | `Long` | `0.0204` | 16,670,000.00 USD | 0.00 USD | 2,280.00 USD | `-73.03%` | `111,254.00` |
| `Live` | `Long` | `0.0215` | 16,670,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.58%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,650,000.00 USD | 0.00 USD | 541.25 USD | `-71.44%` | `25,000.00` |
| `Live` | `Long` | `0.0227` | 16,650,000.00 USD | 0.00 USD | 141.19 USD | `-69.99%` | `6,206.00` |
| `Live` | `Long` | `0.0231` | 16,650,000.00 USD | 0.00 USD | 900.08 USD | `-69.60%` | `39,049.00` |
| `Live` | `Long` | `0.0232` | 16,650,000.00 USD | 0.00 USD | 278.28 USD | `-69.33%` | `11,969.00` |
| `Live` | `Long` | `0.0237` | 16,650,000.00 USD | 0.00 USD | 2,580.00 USD | `-68.81%` | `109,191.00` |
| `Live` | `Long` | `0.0242` | 16,640,000.00 USD | 0.00 USD | 12,460.00 USD | `-68.15%` | `515,795.00` |
| `Live` | `Long` | `0.0244` | 16,630,000.00 USD | 0.00 USD | 369.37 USD | `-67.88%` | `15,169.00` |
| `Live` | `Long` | `0.0254` | 16,630,000.00 USD | 0.00 USD | 4,020.00 USD | `-66.56%` | `158,606.00` |
| `Live` | `Long` | `0.0256` | 16,630,000.00 USD | 0.00 USD | 22,920.00 USD | `-66.17%` | `893,720.00` |
| `Live` | `Long` | `0.0262` | 16,610,000.00 USD | 0.00 USD | 140.28 USD | `-65.38%` | `5,344.00` |
| `Live` | `Long` | `0.0265` | 16,600,000.00 USD | 0.00 USD | 529.00 USD | `-65.11%` | `20,000.00` |
| `Live` | `Long` | `0.0267` | 16,600,000.00 USD | 0.00 USD | 161.26 USD | `-64.85%` | `6,051.00` |
| `Live` | `Long` | `0.0268` | 16,600,000.00 USD | 0.00 USD | 1,000.00 USD | `-64.58%` | `37,344.00` |
| `Live` | `Long` | `0.0272` | 16,600,000.00 USD | 0.00 USD | 880.12 USD | `-64.06%` | `32,298.00` |
| `Live` | `Long` | `0.0278` | 16,600,000.00 USD | 0.00 USD | 4,250.00 USD | `-63.40%` | `153,201.00` |
| `Live` | `Long` | `0.0279` | 16,600,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.13%` | `61,775.00` |
| `Live` | `Long` | `0.0306` | 16,600,000.00 USD | 0.00 USD | 137.41 USD | `-59.70%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,600,000.00 USD | 0.00 USD | 265.80 USD | `-59.44%` | `8,644.00` |
| `Live` | `Long` | `0.0319` | 16,600,000.00 USD | 0.00 USD | 549.83 USD | `-57.99%` | `17,263.00` |
| `Live` | `Long` | `0.0330` | 16,600,000.00 USD | 0.00 USD | 757.85 USD | `-56.54%` | `23,000.00` |
| `Live` | `Long` | `0.0336` | 16,590,000.00 USD | 0.00 USD | 49,950.00 USD | `-55.75%` | `1,488,849.00` |
| `Live` | `Long` | `0.0336` | 16,540,000.00 USD | 0.00 USD | 393.23 USD | `-55.62%` | `11,686.00` |
| `Live` | `Long` | `0.0340` | 16,540,000.00 USD | 0.00 USD | 476.56 USD | `-55.22%` | `14,037.00` |
| `Live` | `Long` | `0.0340` | 16,540,000.00 USD | 0.00 USD | 6,400.00 USD | `-55.09%` | `187,979.00` |
| `Live` | `Long` | `0.0348` | 16,540,000.00 USD | 0.00 USD | 13,540.00 USD | `-54.16%` | `389,633.00` |
| `Live` | `Long` | `0.0350` | 16,520,000.00 USD | 0.00 USD | 4,710.00 USD | `-53.77%` | `134,443.00` |
| `Live` | `Long` | `0.0355` | 16,520,000.00 USD | 0.00 USD | 700.21 USD | `-53.24%` | `19,752.00` |
| `Live` | `Long` | `0.0358` | 16,520,000.00 USD | 0.00 USD | 214.53 USD | `-52.71%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,520,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.58%` | `233,408.00` |
| `Live` | `Long` | `0.0372` | 16,510,000.00 USD | 0.00 USD | 35,290.00 USD | `-51.00%` | `950,000.00` |
| `Live` | `Long` | `0.0381` | 16,470,000.00 USD | 0.00 USD | 1,600.00 USD | `-49.81%` | `41,929.00` |
| `Live` | `Long` | `0.0382` | 16,470,000.00 USD | 0.00 USD | 1,810.00 USD | `-49.68%` | `47,501.00` |
| `Live` | `Long` | `0.0384` | 16,470,000.00 USD | 0.00 USD | 353.40 USD | `-49.42%` | `9,215.00` |
| `Live` | `Long` | `0.0386` | 16,470,000.00 USD | 0.00 USD | 121.74 USD | `-49.15%` | `3,158.00` |
| `Live` | `Long` | `0.0386` | 16,470,000.00 USD | 0.00 USD | 206.74 USD | `-49.02%` | `5,349.00` |
| `Live` | `Long` | `0.0393` | 16,470,000.00 USD | 0.00 USD | 2,180.00 USD | `-48.23%` | `55,633.00` |
| `Live` | `Long` | `0.0399` | 16,470,000.00 USD | 0.00 USD | 103.31 USD | `-47.31%` | `2,586.00` |
| `Live` | `Long` | `0.0401` | 16,470,000.00 USD | 0.00 USD | 4,020.00 USD | `-47.04%` | `100,000.00` |
| `Live` | `Long` | `0.0404` | 16,460,000.00 USD | 0.00 USD | 56,970.00 USD | `-46.65%` | `1,408,334.00` |
| `Live` | `Long` | `0.0408` | 16,410,000.00 USD | 0.00 USD | 419.28 USD | `-46.25%` | `10,289.00` |
| `Live` | `Long` | `0.0411` | 16,410,000.00 USD | 0.00 USD | 5,020.00 USD | `-45.86%` | `122,306.00` |
| `Live` | `Long` | `0.0411` | 16,400,000.00 USD | 0.00 USD | 34,120.00 USD | `-45.72%` | `829,067.00` |
| `Live` | `Long` | `0.0415` | 16,370,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.20%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 16,370,000.00 USD | 0.00 USD | 266.05 USD | `-44.67%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,370,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.27%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,360,000.00 USD | 0.00 USD | 267.52 USD | `-44.14%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,360,000.00 USD | 0.00 USD | 44,200.00 USD | `-44.01%` | `1,041,287.00` |
| `Live` | `Long` | `0.0425` | 16,320,000.00 USD | 0.00 USD | 883.34 USD | `-43.88%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,320,000.00 USD | 0.00 USD | 8,550.00 USD | `-43.74%` | `200,534.00` |
| `Live` | `Long` | `0.0430` | 16,310,000.00 USD | 0.00 USD | 859.00 USD | `-43.35%` | `20,000.00` |
| `Live` | `Long` | `0.0430` | 16,310,000.00 USD | 0.00 USD | 27,590.00 USD | `-43.22%` | `640,910.00` |
| `Live` | `Long` | `0.0432` | 16,280,000.00 USD | 0.00 USD | 954.87 USD | `-43.09%` | `22,129.00` |
| `Live` | `Long` | `0.0432` | 16,280,000.00 USD | 0.00 USD | 122,100.00 USD | `-42.95%` | `2,823,089.00` |
| `Live` | `Long` | `0.0433` | 16,160,000.00 USD | 0.00 USD | 2,450.00 USD | `-42.82%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 16,160,000.00 USD | 0.00 USD | 149.46 USD | `-42.43%` | `3,424.00` |
| `Live` | `Long` | `0.0439` | 16,160,000.00 USD | 0.00 USD | 1,610.00 USD | `-42.16%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,160,000.00 USD | 0.00 USD | 750.58 USD | `-42.03%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,150,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.90%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,150,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.50%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,050,000.00 USD | 0.00 USD | 444.76 USD | `-41.11%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,050,000.00 USD | 0.00 USD | 248.63 USD | `-40.97%` | `5,556.00` |
| `Live` | `Long` | `0.0449` | 16,050,000.00 USD | 0.00 USD | 810.81 USD | `-40.71%` | `18,038.00` |
| `Live` | `Long` | `0.0452` | 16,050,000.00 USD | 0.00 USD | 967,320.00 USD | `-40.45%` | `21,424,497.00` |
| `Live` | `Long` | `0.0454` | 15,080,000.00 USD | 0.00 USD | 27,930.00 USD | `-40.18%` | `615,937.00` |
| `Live` | `Long` | `0.0454` | 15,060,000.00 USD | 0.00 USD | 2,610.00 USD | `-40.05%` | `57,510.00` |
| `Live` | `Long` | `0.0456` | 15,050,000.00 USD | 0.00 USD | 32,650.00 USD | `-39.92%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 15,020,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.66%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 15,010,000.00 USD | 0.00 USD | 789.72 USD | `-39.52%` | `17,224.00` |
| `Live` | `Long` | `0.0459` | 15,010,000.00 USD | 0.00 USD | 689.25 USD | `-39.39%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 15,010,000.00 USD | 0.00 USD | 25,960.00 USD | `-39.26%` | `563,730.00` |
| `Live` | `Long` | `0.0461` | 14,990,000.00 USD | 0.00 USD | 95,490.00 USD | `-39.13%` | `2,069,084.00` |
| `Live` | `Long` | `0.0464` | 14,890,000.00 USD | 0.00 USD | 362.87 USD | `-38.86%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 14,890,000.00 USD | 0.00 USD | 18,030.00 USD | `-38.73%` | `388,263.00` |
| `Live` | `Long` | `0.0466` | 14,870,000.00 USD | 0.00 USD | 13,640.00 USD | `-38.47%` | `292,347.00` |
| `Live` | `Long` | `0.0469` | 14,860,000.00 USD | 0.00 USD | 1,210.00 USD | `-38.20%` | `25,729.00` |
| `Live` | `Long` | `0.0471` | 14,860,000.00 USD | 0.00 USD | 2,360.00 USD | `-37.94%` | `50,080.00` |
| `Live` | `Long` | `0.0473` | 14,860,000.00 USD | 0.00 USD | 3,010.00 USD | `-37.68%` | `63,783.00` |
| `Live` | `Long` | `0.0476` | 14,850,000.00 USD | 0.00 USD | 105.02 USD | `-37.15%` | `2,204.00` |
| `Live` | `Long` | `0.0479` | 14,850,000.00 USD | 0.00 USD | 1,290.00 USD | `-36.75%` | `26,900.00` |
| `Live` | `Long` | `0.0481` | 14,850,000.00 USD | 0.00 USD | 56,440.00 USD | `-36.62%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,800,000.00 USD | 0.00 USD | 2,330.00 USD | `-36.49%` | `48,418.00` |
| `Live` | `Long` | `0.0483` | 14,790,000.00 USD | 0.00 USD | 2,280.00 USD | `-36.23%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,790,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.09%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 14,790,000.00 USD | 0.00 USD | 506.45 USD | `-35.83%` | `10,410.00` |
| `Live` | `Long` | `0.0488` | 14,790,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.57%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,790,000.00 USD | 0.00 USD | 16,470.00 USD | `-35.43%` | `336,491.00` |
| `Live` | `Long` | `0.0491` | 14,770,000.00 USD | 0.00 USD | 1,080.00 USD | `-35.30%` | `21,989.00` |
| `Live` | `Long` | `0.0496` | 14,770,000.00 USD | 0.00 USD | 314.48 USD | `-34.51%` | `6,334.00` |
| `Live` | `Long` | `0.0498` | 14,770,000.00 USD | 0.00 USD | 8,470.00 USD | `-34.38%` | `170,271.00` |
| `Live` | `Long` | `0.0500` | 14,760,000.00 USD | 0.00 USD | 501.50 USD | `-33.98%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,760,000.00 USD | 0.00 USD | 5,410.00 USD | `-33.72%` | `107,572.00` |
| `Live` | `Long` | `0.0505` | 14,750,000.00 USD | 0.00 USD | 334.89 USD | `-33.46%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,750,000.00 USD | 0.00 USD | 1,040.00 USD | `-33.19%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,750,000.00 USD | 0.00 USD | 5,660.00 USD | `-33.06%` | `111,460.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 535.43 USD | `-32.80%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 566.65 USD | `-32.67%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,750,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.53%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,740,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.40%` | `29,005.00` |
| `Live` | `Long` | `0.0515` | 14,730,000.00 USD | 0.00 USD | 308.55 USD | `-32.14%` | `5,997.00` |
| `Live` | `Long` | `0.0517` | 14,730,000.00 USD | 0.00 USD | 931.86 USD | `-31.74%` | `18,007.00` |
| `Live` | `Long` | `0.0519` | 14,730,000.00 USD | 0.00 USD | 7,900.00 USD | `-31.61%` | `152,446.00` |
| `Live` | `Long` | `0.0520` | 14,730,000.00 USD | 0.00 USD | 277.72 USD | `-31.48%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,720,000.00 USD | 0.00 USD | 5,350.00 USD | `-31.35%` | `102,859.00` |
| `Live` | `Long` | `0.0522` | 14,720,000.00 USD | 0.00 USD | 315,950.00 USD | `-31.08%` | `6,046,803.00` |
| `Live` | `Long` | `0.0524` | 14,400,000.00 USD | 0.00 USD | 2,230.00 USD | `-30.82%` | `42,425.00` |
| `Live` | `Long` | `0.0525` | 14,400,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.69%` | `119,430.00` |
| `Live` | `Long` | `0.0527` | 14,400,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.42%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,390,000.00 USD | 0.00 USD | 673.52 USD | `-30.29%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,390,000.00 USD | 0.00 USD | 187,290.00 USD | `-30.16%` | `3,537,023.00` |
| `Live` | `Long` | `0.0532` | 14,200,000.00 USD | 0.00 USD | 9,840.00 USD | `-29.90%` | `185,175.00` |
| `Live` | `Long` | `0.0532` | 14,200,000.00 USD | 0.00 USD | 11,120.00 USD | `-29.76%` | `208,846.00` |
| `Live` | `Long` | `0.0534` | 14,180,000.00 USD | 0.00 USD | 1,240.00 USD | `-29.63%` | `23,207.00` |
| `Live` | `Long` | `0.0534` | 14,180,000.00 USD | 0.00 USD | 1,890.00 USD | `-29.50%` | `35,411.00` |
| `Live` | `Long` | `0.0536` | 14,180,000.00 USD | 0.00 USD | 4,820.00 USD | `-29.37%` | `89,958.00` |
| `Live` | `Long` | `0.0537` | 14,180,000.00 USD | 0.00 USD | 6,420.00 USD | `-29.24%` | `119,631.00` |
| `Live` | `Long` | `0.0537` | 14,170,000.00 USD | 0.00 USD | 257.62 USD | `-29.10%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 14,170,000.00 USD | 0.00 USD | 5,290.00 USD | `-28.84%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 14,160,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.71%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 14,160,000.00 USD | 0.00 USD | 3,030.00 USD | `-28.58%` | `55,906.00` |
| `Live` | `Long` | `0.0542` | 14,160,000.00 USD | 0.00 USD | 96,530.00 USD | `-28.44%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 14,060,000.00 USD | 0.00 USD | 341.67 USD | `-28.18%` | `6,275.00` |
| `Live` | `Long` | `0.0546` | 14,060,000.00 USD | 0.00 USD | 2,510.00 USD | `-28.05%` | `46,004.00` |
| `Live` | `Long` | `0.0546` | 14,060,000.00 USD | 0.00 USD | 1,420.00 USD | `-27.92%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 14,060,000.00 USD | 0.00 USD | 188.07 USD | `-27.78%` | `3,435.00` |
| `Live` | `Long` | `0.0551` | 14,060,000.00 USD | 0.00 USD | 1,760.00 USD | `-27.26%` | `31,888.00` |
| `Live` | `Long` | `0.0556` | 14,060,000.00 USD | 0.00 USD | 907.02 USD | `-26.73%` | `16,328.00` |
| `Live` | `Long` | `0.0556` | 14,060,000.00 USD | 0.00 USD | 4,010.00 USD | `-26.60%` | `72,076.00` |
| `Live` | `Long` | `0.0561` | 14,050,000.00 USD | 0.00 USD | 8,410.00 USD | `-26.07%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 14,040,000.00 USD | 0.00 USD | 63,470.00 USD | `-25.94%` | `1,130,362.00` |
| `Live` | `Long` | `0.0563` | 13,980,000.00 USD | 0.00 USD | 1,820.00 USD | `-25.81%` | `32,433.00` |
| `Live` | `Long` | `0.0563` | 13,980,000.00 USD | 0.00 USD | 351.85 USD | `-25.67%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,980,000.00 USD | 0.00 USD | 131.48 USD | `-25.41%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,980,000.00 USD | 0.00 USD | 567.50 USD | `-25.15%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,980,000.00 USD | 0.00 USD | 315.67 USD | `-24.88%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,980,000.00 USD | 0.00 USD | 10,800.00 USD | `-24.75%` | `189,387.00` |
| `Live` | `Long` | `0.0571` | 13,970,000.00 USD | 0.00 USD | 814.04 USD | `-24.62%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,960,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.36%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,960,000.00 USD | 0.00 USD | 7,630.00 USD | `-24.09%` | `132,603.00` |
| `Live` | `Long` | `0.0576` | 13,950,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.96%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,940,000.00 USD | 0.00 USD | 14,210.00 USD | `-23.83%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,930,000.00 USD | 0.00 USD | 3,940.00 USD | `-23.70%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,920,000.00 USD | 0.00 USD | 441.75 USD | `-23.56%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,920,000.00 USD | 0.00 USD | 431.14 USD | `-23.43%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,920,000.00 USD | 0.00 USD | 447.17 USD | `-23.30%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,920,000.00 USD | 0.00 USD | 582.50 USD | `-23.17%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,920,000.00 USD | 0.00 USD | 116.82 USD | `-23.04%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 13,920,000.00 USD | 0.00 USD | 5,840.00 USD | `-22.90%` | `100,000.00` |
| `Live` | `Long` | `0.0585` | 13,920,000.00 USD | 0.00 USD | 172.78 USD | `-22.77%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,920,000.00 USD | 0.00 USD | 305.15 USD | `-22.51%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,920,000.00 USD | 0.00 USD | 212.22 USD | `-22.24%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,920,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.98%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,890,000.00 USD | 0.00 USD | 546.26 USD | `-21.72%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,890,000.00 USD | 0.00 USD | 4,140.00 USD | `-21.59%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,880,000.00 USD | 0.00 USD | 3,300.00 USD | `-21.45%` | `55,392.00` |
| `Live` | `Long` | `0.0597` | 13,880,000.00 USD | 0.00 USD | 16,800.00 USD | `-21.32%` | `281,570.00` |
| `Live` | `Long` | `0.0599` | 13,860,000.00 USD | 0.00 USD | 4,560.00 USD | `-21.06%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 13,860,000.00 USD | 0.00 USD | 1,230.00 USD | `-20.93%` | `20,496.00` |
| `Live` | `Long` | `0.0600` | 13,860,000.00 USD | 0.00 USD | 7,210.00 USD | `-20.79%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,850,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.66%` | `141,093.00` |
| `Live` | `Long` | `0.0602` | 13,840,000.00 USD | 0.00 USD | 356,270.00 USD | `-20.53%` | `5,913,227.00` |
| `Live` | `Long` | `0.0604` | 13,490,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-20.40%` | `98,675,512.00` |
| `Live` | `Long` | `0.0605` | 7,530,000.00 USD | 0.00 USD | 32,090.00 USD | `-20.13%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,500,000.00 USD | 0.00 USD | 622.63 USD | `-20.00%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 7,500,000.00 USD | 0.00 USD | 2,070.00 USD | `-19.87%` | `34,109.00` |
| `Live` | `Long` | `0.0609` | 7,500,000.00 USD | 0.00 USD | 717.73 USD | `-19.74%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,500,000.00 USD | 0.00 USD | 5,110.00 USD | `-19.61%` | `83,914.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 629.72 USD | `-19.34%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 298.17 USD | `-19.21%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 655.16 USD | `-19.08%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,490,000.00 USD | 0.00 USD | 1,890.00 USD | `-18.82%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,490,000.00 USD | 0.00 USD | 11,510.00 USD | `-18.68%` | `186,736.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 548.71 USD | `-18.55%` | `8,886.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-18.16%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,450,000.00 USD | 0.00 USD | 345.86 USD | `-18.02%` | `5,565.00` |
| `Live` | `Long` | `0.0622` | 7,450,000.00 USD | 0.00 USD | 1,210.00 USD | `-17.89%` | `19,518.00` |
| `Live` | `Long` | `0.0624` | 7,450,000.00 USD | 0.00 USD | 1,900.00 USD | `-17.76%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 43,620.00 USD | `-17.63%` | `698,435.00` |
| `Live` | `Long` | `0.0625` | 7,400,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.50%` | `17,630,450.00` |
| `Live` | `Long` | `0.0626` | 6,300,000.00 USD | 0.00 USD | 1,250.00 USD | `-17.36%` | `19,891.00` |
| `Live` | `Long` | `0.0628` | 6,300,000.00 USD | 0.00 USD | 10,210.00 USD | `-17.23%` | `162,702.00` |
| `Live` | `Long` | `0.0629` | 6,290,000.00 USD | 0.00 USD | 6,400.00 USD | `-17.10%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,280,000.00 USD | 0.00 USD | 2,530.00 USD | `-16.84%` | `40,193.00` |
| `Live` | `Long` | `0.0631` | 6,280,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-16.71%` | `20,783,139.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.57%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.44%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.31%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-16.18%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 4,770.00 USD | `-16.05%` | `74,997.00` |
| `Live` | `Long` | `0.0638` | 4,940,000.00 USD | 0.00 USD | 5,600.00 USD | `-15.91%` | `87,791.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 23,220.00 USD | `-15.78%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.65%` | `31,194.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 150.01 USD | `-15.52%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 17,100.00 USD | `-15.39%` | `266,578.00` |
| `Live` | `Long` | `0.0643` | 4,890,000.00 USD | 0.00 USD | 9,990.00 USD | `-15.25%` | `155,456.00` |
| `Live` | `Long` | `0.0644` | 4,880,000.00 USD | 0.00 USD | 76,280.00 USD | `-15.12%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,810,000.00 USD | 0.00 USD | 27,180.00 USD | `-14.99%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,780,000.00 USD | 0.00 USD | 631.94 USD | `-14.86%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,780,000.00 USD | 0.00 USD | 162,920.00 USD | `-14.59%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,620,000.00 USD | 0.00 USD | 8,800.00 USD | `-14.46%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,610,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.33%` | `337,347.00` |
| `Live` | `Long` | `0.0650` | 4,590,000.00 USD | 0.00 USD | 2,470.00 USD | `-14.20%` | `38,008.00` |
| `Live` | `Long` | `0.0651` | 4,580,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.07%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,580,000.00 USD | 0.00 USD | 13,770.00 USD | `-13.94%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,570,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.54%` | `118,852.00` |
| `Live` | `Long` | `0.0658` | 4,560,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.28%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.14%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,480,000.00 USD | 0.00 USD | 9,600.00 USD | `-13.01%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,470,000.00 USD | 0.00 USD | 2,280.00 USD | `-12.75%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,470,000.00 USD | 0.00 USD | 1,630.00 USD | `-12.62%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,470,000.00 USD | 0.00 USD | 17,410.00 USD | `-12.48%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,450,000.00 USD | 0.00 USD | 1,270.00 USD | `-12.35%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,450,000.00 USD | 0.00 USD | 34,860.00 USD | `-12.09%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 7,620.00 USD | `-11.96%` | `114,225.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-11.82%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-11.69%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,260,000.00 USD | 0.00 USD | 9,050.00 USD | `-11.56%` | `134,979.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.30%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 15,370.00 USD | `-11.17%` | `228,139.00` |
| `Live` | `Long` | `0.0674` | 3,220,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.03%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,220,000.00 USD | 0.00 USD | 112,780.00 USD | `-10.90%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,110,000.00 USD | 0.00 USD | 12,880.00 USD | `-10.77%` | `190,436.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 4,290.00 USD | `-10.64%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 34,090.00 USD | `-10.51%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,060,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.37%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,040,000.00 USD | 0.00 USD | 212.72 USD | `-10.24%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,040,000.00 USD | 0.00 USD | 117.29 USD | `-10.11%` | `1,721.00` |
| `Live` | `Long` | `0.0683` | 3,040,000.00 USD | 0.00 USD | 55,650.00 USD | `-9.98%` | `815,403.00` |
| `Live` | `Long` | `0.0684` | 2,990,000.00 USD | 0.00 USD | 80,430.00 USD | `-9.71%` | `1,174,961.00` |
| `Live` | `Long` | `0.0685` | 2,900,000.00 USD | 0.00 USD | 13,120.00 USD | `-9.58%` | `191,414.00` |
| `Live` | `Long` | `0.0687` | 2,890,000.00 USD | 0.00 USD | 34,970.00 USD | `-9.45%` | `509,405.00` |
| `Live` | `Long` | `0.0688` | 2,860,000.00 USD | 0.00 USD | 16,210.00 USD | `-9.32%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,840,000.00 USD | 0.00 USD | 870.75 USD | `-9.19%` | `12,647.00` |
| `Live` | `Long` | `0.0689` | 2,840,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.05%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,330,000.00 USD | 0.00 USD | 6,960.00 USD | `-8.92%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,320,000.00 USD | 0.00 USD | 13,510.00 USD | `-8.79%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 9,970.00 USD | `-8.66%` | `144,028.00` |
| `Live` | `Long` | `0.0693` | 2,300,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.53%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,300,000.00 USD | 0.00 USD | 4,980.00 USD | `-8.40%` | `71,770.00` |
| `Live` | `Long` | `0.0697` | 2,290,000.00 USD | 0.00 USD | 5,240.00 USD | `-8.13%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 11,090.00 USD | `-8.00%` | `158,931.00` |
| `Live` | `Long` | `0.0698` | 2,280,000.00 USD | 0.00 USD | 3,630.00 USD | `-7.87%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,270,000.00 USD | 0.00 USD | 1,310.00 USD | `-7.74%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,270,000.00 USD | 0.00 USD | 9,620.00 USD | `-7.60%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,260,000.00 USD | 0.00 USD | 8,310.00 USD | `-7.47%` | `118,427.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 1,480.00 USD | `-7.34%` | `21,015.00` |
| `Live` | `Long` | `0.0703` | 2,250,000.00 USD | 0.00 USD | 4,360.00 USD | `-7.21%` | `61,923.00` |
| `Live` | `Long` | `0.0704` | 2,250,000.00 USD | 0.00 USD | 216.56 USD | `-7.08%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 423.90 USD | `-6.81%` | `6,000.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 94,410.00 USD | `-6.68%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,150,000.00 USD | 0.00 USD | 821.60 USD | `-6.42%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,150,000.00 USD | 0.00 USD | 5,240.00 USD | `-6.29%` | `73,732.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 2,160.00 USD | `-6.15%` | `30,362.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 802.06 USD | `-6.02%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,150,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-5.89%` | `24,500,580.00` |
| `Live` | `Long` | `0.0714` | 397,120.00 USD | 0.00 USD | 5,410.00 USD | `-5.76%` | `75,723.00` |
| `Live` | `Long` | `0.0716` | 391,710.00 USD | 0.00 USD | 8,120.00 USD | `-5.63%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 383,590.00 USD | 0.00 USD | 1,170.00 USD | `-5.49%` | `16,291.00` |
| `Live` | `Long` | `0.0717` | 382,420.00 USD | 0.00 USD | 22,270.00 USD | `-5.36%` | `310,316.00` |
| `Live` | `Long` | `0.0718` | 360,160.00 USD | 0.00 USD | 1,070.00 USD | `-5.23%` | `14,951.00` |
| `Live` | `Long` | `0.0720` | 359,080.00 USD | 0.00 USD | 1,900.00 USD | `-5.10%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 357,190.00 USD | 0.00 USD | 12,160.00 USD | `-4.97%` | `168,703.00` |
| `Live` | `Long` | `0.0722` | 345,030.00 USD | 0.00 USD | 22,360.00 USD | `-4.83%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 322,680.00 USD | 0.00 USD | 322,050.00 USD | `-4.70%` | `4,457,443.00` |
| `Live` | `Long` | `0.0723` | 626.77 USD | 0.00 USD | 626.77 USD | `-4.57%` | `8,663.00` |
| `Live` | `Short` | `0.0770` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | `+1.50%` | `42,311.00` |
| `Live` | `Short` | `0.0775` | 3,500.00 USD | 240.95 USD | 0.00 USD | `+2.29%` | `3,107.00` |
| `Live` | `Short` | `0.0788` | 3,610.00 USD | 113.24 USD | 0.00 USD | `+3.87%` | `1,438.00` |
| `Live` | `Short` | `0.0793` | 4,030.00 USD | 423.67 USD | 0.00 USD | `+4.53%` | `5,346.00` |
| `Live` | `Short` | `0.0808` | 4,250.00 USD | 215.60 USD | 0.00 USD | `+6.51%` | `2,670.00` |
| `Live` | `Short` | `0.0809` | 4,470.00 USD | 215.87 USD | 0.00 USD | `+6.64%` | `2,670.00` |
| `Live` | `Short` | `0.0810` | 4,580.00 USD | 118.33 USD | 0.00 USD | `+6.90%` | `1,460.00` |
| `Live` | `Short` | `0.0819` | 4,960.00 USD | 380.85 USD | 0.00 USD | `+7.96%` | `4,653.00` |
| `Live` | `Short` | `0.0832` | 8,420.00 USD | 3,450.00 USD | 0.00 USD | `+9.67%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 8,920.00 USD | 500.17 USD | 0.00 USD | `+9.81%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 9,210.00 USD | 293.44 USD | 0.00 USD | `+10.33%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 10,780.00 USD | 1,570.00 USD | 0.00 USD | `+10.47%` | `18,767.00` |
| `Live` | `Short` | `0.0847` | 10,910.00 USD | 128.58 USD | 0.00 USD | `+11.65%` | `1,519.00` |
| `Live` | `Short` | `0.0848` | 11,340.00 USD | 426.71 USD | 0.00 USD | `+11.92%` | `5,029.00` |
| `Live` | `Short` | `0.0858` | 11,450.00 USD | 115.30 USD | 0.00 USD | `+13.24%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 15,910.00 USD | 4,450.00 USD | 0.00 USD | `+13.37%` | `51,791.00` |
| `Live` | `Short` | `0.0871` | 16,040.00 USD | 138.58 USD | 0.00 USD | `+14.82%` | `1,592.00` |
| `Live` | `Short` | `0.0881` | 16,510.00 USD | 465.17 USD | 0.00 USD | `+16.14%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 16,920.00 USD | 411.53 USD | 0.00 USD | `+17.06%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 17,340.00 USD | 418.80 USD | 0.00 USD | `+17.46%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 17,630.00 USD | 285.70 USD | 0.00 USD | `+17.98%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 24,390.00 USD | 6,760.00 USD | 0.00 USD | `+19.30%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 25,700.00 USD | 1,310.00 USD | 0.00 USD | `+19.57%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 30,640.00 USD | 4,940.00 USD | 0.00 USD | `+20.23%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 30,810.00 USD | 171.49 USD | 0.00 USD | `+21.41%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 31,610.00 USD | 805.37 USD | 0.00 USD | `+22.86%` | `8,646.00` |
| `Live` | `Short` | `0.0943` | 32,750.00 USD | 1,140.00 USD | 0.00 USD | `+24.32%` | `12,089.00` |
| `Live` | `Short` | `0.0944` | 72,460.00 USD | 39,700.00 USD | 0.00 USD | `+24.45%` | `420,808.00` |
| `Live` | `Short` | `0.0948` | 76,720.00 USD | 4,260.00 USD | 0.00 USD | `+24.98%` | `45,000.00` |
| `Live` | `Short` | `0.0950` | 101,190.00 USD | 24,460.00 USD | 0.00 USD | `+25.24%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 101,950.00 USD | 761.26 USD | 0.00 USD | `+25.37%` | `8,009.00` |
| `Live` | `Short` | `0.0955` | 150,850.00 USD | 48,900.00 USD | 0.00 USD | `+26.03%` | `511,771.00` |
| `Live` | `Short` | `0.0961` | 151,460.00 USD | 609.59 USD | 0.00 USD | `+26.82%` | `6,340.00` |
| `Live` | `Short` | `0.0974` | 151,580.00 USD | 121.23 USD | 0.00 USD | `+28.54%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 152,050.00 USD | 477.50 USD | 0.00 USD | `+29.59%` | `4,860.00` |
| `Live` | `Short` | `0.0995` | 154,960.00 USD | 2,910.00 USD | 0.00 USD | `+31.31%` | `29,217.00` |
| `Live` | `Short` | `0.1002` | 155,160.00 USD | 201.80 USD | 0.00 USD | `+32.10%` | `2,015.00` |
| `Live` | `Short` | `0.1014` | 162,790.00 USD | 7,630.00 USD | 0.00 USD | `+33.81%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 165,760.00 USD | 2,970.00 USD | 0.00 USD | `+34.08%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 166,250.00 USD | 492.85 USD | 0.00 USD | `+34.34%` | `4,839.00` |
| `Live` | `Short` | `0.1023` | 169,430.00 USD | 3,170.00 USD | 0.00 USD | `+35.00%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 175,540.00 USD | 6,110.00 USD | 0.00 USD | `+40.01%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 176,150.00 USD | 616.19 USD | 0.00 USD | `+41.99%` | `5,724.00` |
| `Live` | `Short` | `0.1084` | 178,010.00 USD | 1,860.00 USD | 0.00 USD | `+42.91%` | `17,184.00` |
| `Live` | `Short` | `0.1085` | 181,250.00 USD | 3,240.00 USD | 0.00 USD | `+43.18%` | `29,849.00` |
| `Live` | `Short` | `0.1127` | 181,470.00 USD | 214.15 USD | 0.00 USD | `+48.59%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 181,610.00 USD | 142.88 USD | 0.00 USD | `+48.98%` | `1,265.00` |
| `Live` | `Short` | `0.1158` | 181,740.00 USD | 131.49 USD | 0.00 USD | `+52.81%` | `1,135.00` |
| `Live` | `Short` | `0.1218` | 184,120.00 USD | 2,370.00 USD | 0.00 USD | `+60.72%` | `19,483.00` |
| `Live` | `Short` | `0.1222` | 184,750.00 USD | 637.53 USD | 0.00 USD | `+61.25%` | `5,215.00` |
| `Live` | `Short` | `0.1236` | 184,870.00 USD | 119.32 USD | 0.00 USD | `+63.09%` | `965.00` |
| `Live` | `Short` | `0.1249` | 186,110.00 USD | 1,240.00 USD | 0.00 USD | `+64.68%` | `9,926.00` |
| `Live` | `Short` | `0.1270` | 186,220.00 USD | 108.80 USD | 0.00 USD | `+67.45%` | `857.00` |
| `Live` | `Short` | `0.1283` | 187,150.00 USD | 926.56 USD | 0.00 USD | `+69.29%` | `7,219.00` |
| `Live` | `Short` | `0.1296` | 187,320.00 USD | 171.66 USD | 0.00 USD | `+71.01%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 189,460.00 USD | 2,140.00 USD | 0.00 USD | `+72.99%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 189,560.00 USD | 102.97 USD | 0.00 USD | `+73.91%` | `781.00` |
| `Live` | `Short` | `0.1325` | 234,890.00 USD | 45,330.00 USD | 0.00 USD | `+74.70%` | `342,231.00` |
| `Live` | `Short` | `0.1336` | 269,390.00 USD | 34,500.00 USD | 0.00 USD | `+76.15%` | `258,360.00` |
| `Live` | `Short` | `0.1338` | 269,600.00 USD | 205.31 USD | 0.00 USD | `+76.42%` | `1,535.00` |
| `Live` | `Short` | `0.1346` | 269,730.00 USD | 134.42 USD | 0.00 USD | `+77.47%` | `999.00` |
| `Live` | `Short` | `0.1378` | 275,980.00 USD | 6,240.00 USD | 0.00 USD | `+81.69%` | `45,319.00` |
| `Live` | `Short` | `0.1384` | 298,430.00 USD | 22,450.00 USD | 0.00 USD | `+82.62%` | `162,180.00` |
| `Live` | `Short` | `0.1404` | 298,530.00 USD | 100.35 USD | 0.00 USD | `+85.12%` | `715.00` |
| `Live` | `Short` | `0.1404` | 299,190.00 USD | 663.63 USD | 0.00 USD | `+85.25%` | `4,725.00` |
| `Live` | `Short` | `0.1432` | 301,060.00 USD | 1,860.00 USD | 0.00 USD | `+88.95%` | `13,010.00` |
| `Live` | `Short` | `0.1434` | 302,960.00 USD | 1,900.00 USD | 0.00 USD | `+89.21%` | `13,240.00` |
| `Live` | `Short` | `0.1441` | 303,150.00 USD | 196.63 USD | 0.00 USD | `+90.00%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 304,700.00 USD | 1,540.00 USD | 0.00 USD | `+90.40%` | `10,691.00` |
| `Live` | `Short` | `0.1470` | 306,760.00 USD | 2,060.00 USD | 0.00 USD | `+93.96%` | `14,000.00` |
| `Live` | `Short` | `0.1472` | 307,200.00 USD | 441.45 USD | 0.00 USD | `+94.09%` | `3,000.00` |
| `Live` | `Short` | `0.1479` | 315,380.00 USD | 8,180.00 USD | 0.00 USD | `+95.01%` | `55,317.00` |
| `Live` | `Short` | `0.1487` | 321,860.00 USD | 6,480.00 USD | 0.00 USD | `+96.07%` | `43,601.00` |
| `Live` | `Short` | `0.1500` | 345,990.00 USD | 24,130.00 USD | 0.00 USD | `+97.92%` | `160,802.00` |
| `Live` | `Short` | `0.1515` | 347,310.00 USD | 1,320.00 USD | 0.00 USD | `+99.89%` | `8,712.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 652,620.00 USD | 0.00 USD | 375.42 USD | `-65.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 652,240.00 USD | 0.00 USD | 409.59 USD | `-47.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 651,830.00 USD | 0.00 USD | 132.68 USD | `-46.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 651,700.00 USD | 0.00 USD | 788.27 USD | `-45.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 650,910.00 USD | 0.00 USD | 527.05 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 650,380.00 USD | 0.00 USD | 286.87 USD | `-40.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 650,100.00 USD | 0.00 USD | 252.42 USD | `-38.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 649,840.00 USD | 0.00 USD | 468.67 USD | `-37.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 649,380.00 USD | 0.00 USD | 5,160.00 USD | `-35.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 644,220.00 USD | 0.00 USD | 920.48 USD | `-34.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 643,300.00 USD | 0.00 USD | 236.01 USD | `-34.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 643,060.00 USD | 0.00 USD | 175.41 USD | `-32.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 642,890.00 USD | 0.00 USD | 242.96 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 642,640.00 USD | 0.00 USD | 2,670.00 USD | `-28.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 639,970.00 USD | 0.00 USD | 1,370.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 638,600.00 USD | 0.00 USD | 437.58 USD | `-26.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 638,160.00 USD | 0.00 USD | 183.30 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 637,980.00 USD | 0.00 USD | 752.54 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 637,220.00 USD | 0.00 USD | 9,830.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 627,390.00 USD | 0.00 USD | 1,020.00 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 626,380.00 USD | 0.00 USD | 668.84 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 625,710.00 USD | 0.00 USD | 273.90 USD | `-20.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 625,430.00 USD | 0.00 USD | 8,800.00 USD | `-20.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 616,640.00 USD | 0.00 USD | 419.39 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 616,220.00 USD | 0.00 USD | 218.94 USD | `-19.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 616,000.00 USD | 0.00 USD | 504.26 USD | `-18.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 615,490.00 USD | 0.00 USD | 2,280.00 USD | `-18.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 613,210.00 USD | 0.00 USD | 118.27 USD | `-18.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 613,090.00 USD | 0.00 USD | 1,280.00 USD | `-17.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 611,820.00 USD | 0.00 USD | 1,820.00 USD | `-16.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 609,990.00 USD | 0.00 USD | 1,340.00 USD | `-15.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 608,660.00 USD | 0.00 USD | 386.70 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 608,270.00 USD | 0.00 USD | 644.50 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 607,630.00 USD | 0.00 USD | 19,520.00 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 588,110.00 USD | 0.00 USD | 1,410.00 USD | `-13.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 586,700.00 USD | 0.00 USD | 3,140.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 583,560.00 USD | 0.00 USD | 1,100.00 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 582,460.00 USD | 0.00 USD | 1,200.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 581,270.00 USD | 0.00 USD | 996.31 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 580,270.00 USD | 0.00 USD | 909.85 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 579,360.00 USD | 0.00 USD | 115.57 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 579,240.00 USD | 0.00 USD | 33,620.00 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 545,620.00 USD | 0.00 USD | 12,860.00 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 532,760.00 USD | 0.00 USD | 1,540.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 531,220.00 USD | 0.00 USD | 108.08 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 531,110.00 USD | 0.00 USD | 19,540.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 511,570.00 USD | 0.00 USD | 1,430.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 510,130.00 USD | 0.00 USD | 8,540.00 USD | `-10.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 501,600.00 USD | 0.00 USD | 8,580.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 493,020.00 USD | 0.00 USD | 4,970.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 488,050.00 USD | 0.00 USD | 3,100.00 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 484,960.00 USD | 0.00 USD | 160.31 USD | `-9.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 484,800.00 USD | 0.00 USD | 38,710.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 446,090.00 USD | 0.00 USD | 27,690.00 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 418,400.00 USD | 0.00 USD | 3,190.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 415,210.00 USD | 0.00 USD | 533.09 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 414,670.00 USD | 0.00 USD | 378.50 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 414,300.00 USD | 0.00 USD | 925.29 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 413,370.00 USD | 0.00 USD | 797.80 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 412,570.00 USD | 0.00 USD | 11,920.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 400,660.00 USD | 0.00 USD | 141.77 USD | `-7.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 400,510.00 USD | 0.00 USD | 895.27 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 399,620.00 USD | 0.00 USD | 523.23 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 399,100.00 USD | 0.00 USD | 468.88 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 398,630.00 USD | 0.00 USD | 235.12 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 398,390.00 USD | 0.00 USD | 1,090.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 397,300.00 USD | 0.00 USD | 71,660.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 325,640.00 USD | 0.00 USD | 497.62 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 325,150.00 USD | 0.00 USD | 20,330.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 304,810.00 USD | 0.00 USD | 608.76 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 304,200.00 USD | 0.00 USD | 16,880.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 287,330.00 USD | 0.00 USD | 265.67 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 287,060.00 USD | 0.00 USD | 1,670.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 285,390.00 USD | 0.00 USD | 4,210.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 281,180.00 USD | 0.00 USD | 13,550.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 267,630.00 USD | 0.00 USD | 413.42 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 267,220.00 USD | 0.00 USD | 138,380.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 128,840.00 USD | 0.00 USD | 849.15 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 127,990.00 USD | 0.00 USD | 34,460.00 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 93,520.00 USD | 0.00 USD | 2,030.00 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 91,500.00 USD | 0.00 USD | 1,950.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 89,540.00 USD | 0.00 USD | 2,540.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 87,000.00 USD | 0.00 USD | 4,110.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 82,890.00 USD | 0.00 USD | 2,090.00 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 80,800.00 USD | 0.00 USD | 1,950.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 78,850.00 USD | 0.00 USD | 535.16 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 78,310.00 USD | 0.00 USD | 227.92 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 78,080.00 USD | 0.00 USD | 397.76 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 77,690.00 USD | 0.00 USD | 398.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 77,290.00 USD | 0.00 USD | 797.39 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 76,490.00 USD | 0.00 USD | 38,550.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 37,940.00 USD | 0.00 USD | 1,640.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 36,300.00 USD | 0.00 USD | 189.57 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 36,110.00 USD | 0.00 USD | 1,480.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 34,630.00 USD | 0.00 USD | 2,900.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 31,740.00 USD | 0.00 USD | 415.62 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 31,320.00 USD | 0.00 USD | 16,520.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 14,800.00 USD | 0.00 USD | 3,180.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 11,620.00 USD | 0.00 USD | 375.86 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 11,250.00 USD | 0.00 USD | 399.17 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 10,850.00 USD | 0.00 USD | 140.04 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 10,710.00 USD | 0.00 USD | 151.47 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 10,560.00 USD | 0.00 USD | 3,450.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 7,110.00 USD | 0.00 USD | 736.17 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 6,370.00 USD | 0.00 USD | 406.95 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 5,960.00 USD | 0.00 USD | 221.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 5,740.00 USD | 0.00 USD | 407.73 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 5,330.00 USD | 0.00 USD | 408.57 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 4,930.00 USD | 0.00 USD | 408.81 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 4,520.00 USD | 0.00 USD | 4,520.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 504.10 USD | 504.10 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 902.23 USD | 398.13 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 1,120.00 USD | 216.21 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 1,930.00 USD | 806.81 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 2,740.00 USD | 814.81 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 6,510.00 USD | 3,770.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 6,620.00 USD | 109.63 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 7,870.00 USD | 1,250.00 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 8,050.00 USD | 183.50 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 8,900.00 USD | 843.94 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 9,400.00 USD | 502.52 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 10,220.00 USD | 816.05 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 10,480.00 USD | 266.52 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 12,720.00 USD | 2,240.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 12,960.00 USD | 240.02 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 16,890.00 USD | 3,930.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 17,300.00 USD | 407.23 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 17,620.00 USD | 321.13 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 19,110.00 USD | 1,490.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 21,360.00 USD | 2,240.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 21,690.00 USD | 329.23 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 21,990.00 USD | 303.77 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 22,180.00 USD | 186.07 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 25,260.00 USD | 3,080.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 26,230.00 USD | 975.23 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 30,600.00 USD | 4,370.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 30,760.00 USD | 157.14 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 30,890.00 USD | 130.71 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 72,500.00 USD | 41,610.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 72,640.00 USD | 141.44 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 73,420.00 USD | 773.68 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 74,100.00 USD | 687.81 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 79,680.00 USD | 5,580.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 84,280.00 USD | 4,600.00 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 89,550.00 USD | 5,270.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 97,370.00 USD | 7,820.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 97,680.00 USD | 312.56 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 98,130.00 USD | 455.34 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 98,260.00 USD | 125.45 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 98,490.00 USD | 230.40 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 98,810.00 USD | 319.16 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 99,820.00 USD | 1,010.00 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 122,570.00 USD | 22,750.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 122,970.00 USD | 400.91 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 123,170.00 USD | 200.46 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 123,430.00 USD | 259.13 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 124,130.00 USD | 707.08 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 133,140.00 USD | 9,010.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 229,920.00 USD | 96,780.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 230,730.00 USD | 807.50 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 230,990.00 USD | 257.18 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 231,410.00 USD | 424.74 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 231,510.00 USD | 101.80 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 232,900.00 USD | 1,380.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 234,920.00 USD | 2,030.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 236,360.00 USD | 1,430.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 236,480.00 USD | 129.67 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 237,500.00 USD | 1,020.00 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 237,760.00 USD | 256.05 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 238,780.00 USD | 1,030.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 241,810.00 USD | 3,020.00 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 242,130.00 USD | 327.80 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 242,590.00 USD | 457.92 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 243,280.00 USD | 691.29 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 244,080.00 USD | 800.79 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 244,600.00 USD | 512.05 USD | 0.00 USD | `+8.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 245,090.00 USD | 495.36 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 245,480.00 USD | 389.31 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 245,640.00 USD | 154.58 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 245,940.00 USD | 303.56 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 246,050.00 USD | 112.89 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 246,430.00 USD | 381.45 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 246,590.00 USD | 155.82 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 290,980.00 USD | 44,390.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 291,110.00 USD | 138.69 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 292,370.00 USD | 1,260.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 292,480.00 USD | 107.03 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,860,000.00 USD | 1,570,000.00 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,870,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,870,000.00 USD | 1,470.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,870,000.00 USD | 107.71 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,870,000.00 USD | 2,690.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,870,000.00 USD | 529.92 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,870,000.00 USD | 219.07 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,870,000.00 USD | 242.84 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,880,000.00 USD | 10,140.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,880,000.00 USD | 876.11 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,880,000.00 USD | 812.54 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,880,000.00 USD | 126.76 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,880,000.00 USD | 307.41 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,880,000.00 USD | 614.09 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,880,000.00 USD | 859.50 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,890,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,930,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 1,930,000.00 USD | 123.94 USD | 0.00 USD | `+14.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 1,930,000.00 USD | 271.53 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 1,930,000.00 USD | 1,550.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 1,930,000.00 USD | 1,840.00 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 1,940,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 1,940,000.00 USD | 117.71 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 1,940,000.00 USD | 111.61 USD | 0.00 USD | `+16.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 1,940,000.00 USD | 571.18 USD | 0.00 USD | `+16.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 1,940,000.00 USD | 375.94 USD | 0.00 USD | `+16.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 1,940,000.00 USD | 627.55 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 1,940,000.00 USD | 211.04 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 1,940,000.00 USD | 108.36 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 1,940,000.00 USD | 543.32 USD | 0.00 USD | `+17.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 1,940,000.00 USD | 1,820.00 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 1,940,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 1,960,000.00 USD | 17,680.00 USD | 0.00 USD | `+17.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 1,960,000.00 USD | 1,370.00 USD | 0.00 USD | `+17.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 1,970,000.00 USD | 5,630.00 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 1,970,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 1,970,000.00 USD | 224.86 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 1,990,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 1,990,000.00 USD | 114.93 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 1,990,000.00 USD | 679.12 USD | 0.00 USD | `+19.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 1,990,000.00 USD | 173.36 USD | 0.00 USD | `+20.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 1,990,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 1,990,000.00 USD | 1,580.00 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,000,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,000,000.00 USD | 541.32 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,130,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,130,000.00 USD | 691.07 USD | 0.00 USD | `+22.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,140,000.00 USD | 6,250.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,150,000.00 USD | 13,480.00 USD | 0.00 USD | `+22.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,160,000.00 USD | 734.82 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,160,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,160,000.00 USD | 105.00 USD | 0.00 USD | `+23.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,160,000.00 USD | 184.09 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,160,000.00 USD | 1,120.00 USD | 0.00 USD | `+23.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,160,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,160,000.00 USD | 1,070.00 USD | 0.00 USD | `+24.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,160,000.00 USD | 512.15 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,170,000.00 USD | 6,620.00 USD | 0.00 USD | `+24.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,170,000.00 USD | 404.96 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,170,000.00 USD | 129.85 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,170,000.00 USD | 3,740.00 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,170,000.00 USD | 409.17 USD | 0.00 USD | `+26.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,170,000.00 USD | 203.74 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,180,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,180,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,180,000.00 USD | 694.56 USD | 0.00 USD | `+28.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,180,000.00 USD | 940.91 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,180,000.00 USD | 2,980.00 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,180,000.00 USD | 104.99 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,180,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,190,000.00 USD | 1,490.00 USD | 0.00 USD | `+31.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,190,000.00 USD | 1,090.00 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,190,000.00 USD | 438.96 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,190,000.00 USD | 973.76 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,200,000.00 USD | 10,000.00 USD | 0.00 USD | `+31.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,200,000.00 USD | 175.59 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,200,000.00 USD | 2,060.00 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,200,000.00 USD | 482.89 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,200,000.00 USD | 201.90 USD | 0.00 USD | `+33.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,200,000.00 USD | 489.46 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,200,000.00 USD | 103.68 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,200,000.00 USD | 2,590.00 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,210,000.00 USD | 3,810.00 USD | 0.00 USD | `+34.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,220,000.00 USD | 11,200.00 USD | 0.00 USD | `+34.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,220,000.00 USD | 4,330.00 USD | 0.00 USD | `+34.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,220,000.00 USD | 205.50 USD | 0.00 USD | `+35.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,230,000.00 USD | 3,490.00 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,230,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,230,000.00 USD | 207.50 USD | 0.00 USD | `+36.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,230,000.00 USD | 813.88 USD | 0.00 USD | `+37.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,250,000.00 USD | 23,160.00 USD | 0.00 USD | `+37.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,250,000.00 USD | 781.51 USD | 0.00 USD | `+37.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,250,000.00 USD | 209.30 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,250,000.00 USD | 1,440.00 USD | 0.00 USD | `+38.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,260,000.00 USD | 5,140.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,260,000.00 USD | 585.32 USD | 0.00 USD | `+38.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,260,000.00 USD | 210.90 USD | 0.00 USD | `+39.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,260,000.00 USD | 1,850.00 USD | 0.00 USD | `+39.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,260,000.00 USD | 105.75 USD | 0.00 USD | `+39.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,270,000.00 USD | 3,220.00 USD | 0.00 USD | `+39.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,270,000.00 USD | 1,600.00 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,270,000.00 USD | 212.90 USD | 0.00 USD | `+40.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,270,000.00 USD | 472.63 USD | 0.00 USD | `+41.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,270,000.00 USD | 214.50 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,270,000.00 USD | 1,040.00 USD | 0.00 USD | `+42.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,270,000.00 USD | 136.12 USD | 0.00 USD | `+42.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,270,000.00 USD | 216.10 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,270,000.00 USD | 1,010.00 USD | 0.00 USD | `+43.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,270,000.00 USD | 217.90 USD | 0.00 USD | `+43.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,270,000.00 USD | 219.70 USD | 0.00 USD | `+44.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,280,000.00 USD | 7,780.00 USD | 0.00 USD | `+45.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,280,000.00 USD | 154.22 USD | 0.00 USD | `+45.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,280,000.00 USD | 221.30 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,280,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,300,000.00 USD | 24,190.00 USD | 0.00 USD | `+46.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,300,000.00 USD | 223.10 USD | 0.00 USD | `+47.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,300,000.00 USD | 224.70 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,310,000.00 USD | 226.30 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,310,000.00 USD | 950.34 USD | 0.00 USD | `+50.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,310,000.00 USD | 229.50 USD | 0.00 USD | `+51.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,310,000.00 USD | 771.08 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,310,000.00 USD | 942.95 USD | 0.00 USD | `+51.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,310,000.00 USD | 230.90 USD | 0.00 USD | `+52.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,310,000.00 USD | 288.18 USD | 0.00 USD | `+52.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,310,000.00 USD | 619.10 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,310,000.00 USD | 1,250.00 USD | 0.00 USD | `+52.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,310,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,310,000.00 USD | 232.30 USD | 0.00 USD | `+53.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,310,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,310,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,320,000.00 USD | 3,730.00 USD | 0.00 USD | `+54.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,320,000.00 USD | 676.22 USD | 0.00 USD | `+55.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,320,000.00 USD | 648.25 USD | 0.00 USD | `+55.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,320,000.00 USD | 1,510.00 USD | 0.00 USD | `+55.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,320,000.00 USD | 448.52 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,320,000.00 USD | 124.58 USD | 0.00 USD | `+56.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,320,000.00 USD | 1,050.00 USD | 0.00 USD | `+57.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,320,000.00 USD | 691.80 USD | 0.00 USD | `+57.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,440,000.00 USD | 117,860.00 USD | 0.00 USD | `+58.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,440,000.00 USD | 143.22 USD | 0.00 USD | `+58.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,440,000.00 USD | 1,380.00 USD | 0.00 USD | `+59.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,440,000.00 USD | 2,270.00 USD | 0.00 USD | `+60.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,450,000.00 USD | 871.99 USD | 0.00 USD | `+61.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,480,000.00 USD | 29,610.00 USD | 0.00 USD | `+67.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,480,000.00 USD | 400.21 USD | 0.00 USD | `+67.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,490,000.00 USD | 13,850.00 USD | 0.00 USD | `+73.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,490,000.00 USD | 2,360.00 USD | 0.00 USD | `+74.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,500,000.00 USD | 4,160.00 USD | 0.00 USD | `+78.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,500,000.00 USD | 114.70 USD | 0.00 USD | `+80.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,500,000.00 USD | 278.50 USD | 0.00 USD | `+84.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,500,000.00 USD | 1,160.00 USD | 0.00 USD | `+86.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,500,000.00 USD | 173.57 USD | 0.00 USD | `+87.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,500,000.00 USD | 380.09 USD | 0.00 USD | `+87.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,520,000.00 USD | 17,150.00 USD | 0.00 USD | `+87.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,520,000.00 USD | 1,440.00 USD | 0.00 USD | `+89.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,520,000.00 USD | 433.35 USD | 0.00 USD | `+90.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,520,000.00 USD | 452.26 USD | 0.00 USD | `+92.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,520,000.00 USD | 3,640.00 USD | 0.00 USD | `+93.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,580,000.00 USD | 55,720.00 USD | 0.00 USD | `+94.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,580,000.00 USD | 2,120.00 USD | 0.00 USD | `+95.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,600,000.00 USD | 19,850.00 USD | 0.00 USD | `+97.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,600,000.00 USD | 1,620.00 USD | 0.00 USD | `+99.63%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0672` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 4,130.00 USD | 7,790.00 USD | 0.00 USD |
| `1D` | `0.0673` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 6,250.00 USD | 704.90 USD | 0.00 USD |
| `1D` | `0.0674` | 15,300,000.00 USD | 0.00 USD | 15,300,000.00 USD | 69,290.00 USD | 9,000.00 USD | 166.57 USD |
| `1D` | `0.0675` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 40,430.00 USD | 9,210.00 USD | 15,270.00 USD |
| `1D` | `0.0676` | 15,160,000.00 USD | 0.00 USD | 15,160,000.00 USD | 45,230.00 USD | 65,160.00 USD | 234.44 USD |
| `1D` | `0.0677` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 3,410.00 USD | 19,140.00 USD | 18,890.00 USD |
| `1D` | `0.0678` | 15,010,000.00 USD | 0.00 USD | 15,010,000.00 USD | 15,920.00 USD | 39,890.00 USD | 64,810.00 USD |
| `1D` | `0.0679` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 28,320.00 USD | 38,120.00 USD | 827.41 USD |
| `1D` | `0.0680` | 14,820,000.00 USD | 0.00 USD | 14,820,000.00 USD | 18,300.00 USD | 9,760.00 USD | 7,700.00 USD |
| `1D` | `0.0681` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 17,070.00 USD | 27,520.00 USD | 138,190.00 USD |
| `1D` | `0.0682` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 2,550.00 USD | 33,950.00 USD | 21,590.00 USD |
| `1D` | `0.0683` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 15,780.00 USD | 26,860.00 USD | 1,310.00 USD |
| `1D` | `0.0684` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 24,150.00 USD | 15,070.00 USD | 338.82 USD |
| `1D` | `0.0685` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 58,140.00 USD | 13,720.00 USD | 17,300.00 USD |
| `1D` | `0.0686` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 44,450.00 USD | 8,860.00 USD | 13,610.00 USD |
| `1D` | `0.0687` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 9,250.00 USD | 16,550.00 USD | 29,490.00 USD |
| `1D` | `0.0688` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0689` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 9,350.00 USD | 0.00 USD | 670.09 USD |
| `1D` | `0.0691` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0692` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 23,110.00 USD | 0.00 USD | 2,640.00 USD |
| `1D` | `0.0693` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 18,220.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `0.0694` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 27,810.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `0.0695` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 14,130,000.00 USD | 0.00 USD | 14,130,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD |
| `1D` | `0.0698` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 14,010.00 USD | 10,800.00 USD | 9,890.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 83,570.00 USD | 27,620.00 USD | 32,040.00 USD |
| `1D` | `0.0700` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 141,150.00 USD | 21,100.00 USD | 37,360.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 51,480.00 USD | 115,140.00 USD | 15,990.00 USD |
| `1D` | `0.0702` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 87,840.00 USD | 36,120.00 USD | 5,460.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 13,380,000.00 USD | 0.00 USD | 13,380,000.00 USD | 175,640.00 USD | 66,830.00 USD | 14,520.00 USD |
| `1D` | `0.0704` | 13,130,000.00 USD | 0.00 USD | 13,130,000.00 USD | 25,820.00 USD | 45,140.00 USD | 20,070.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 50,870.00 USD | 30,720.00 USD | 68,460.00 USD |
| `1D` | `0.0706` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 21,850.00 USD | 1,120.00 USD | 14,200.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 12,850,000.00 USD | 0.00 USD | 12,850,000.00 USD | 140,160.00 USD | 70,030.00 USD | 45,360.00 USD |
| `1D` | `0.0708` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 75,260.00 USD | 62,000.00 USD | 123,800.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 12,330,000.00 USD | 0.00 USD | 12,330,000.00 USD | 43,490.00 USD | 84,200.00 USD | 147,820.00 USD |
| `1D` | `0.0710` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 125,310.00 USD | 99,310.00 USD | 141,190.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 42,650.00 USD | 25,670.00 USD | 42,170.00 USD |
| `1D` | `0.0712` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 159,040.00 USD | 46,690.00 USD | 1,360.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 70,910.00 USD | 85,230.00 USD | 65,700.00 USD |
| `1D` | `0.0714` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 118,420.00 USD | 51,930.00 USD | 50,690.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 73,470.00 USD | 238,460.00 USD | 40,490.00 USD |
| `1D` | `0.0716` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 19,480.00 USD | 51,080.00 USD | 148.69 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 232,360.00 USD | 96,160.00 USD | 46.48 USD |
| `1D` | `0.0718` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 55,690.00 USD | 101,030.00 USD | 12,880.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 226,040.00 USD | 45,330.00 USD | 69,210.00 USD |
| `1D` | `0.0720` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 135,290.00 USD | 50,600.00 USD | 69,850.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 308,410.00 USD | 298,040.00 USD | 70,740.00 USD |
| `1D` | `0.0722` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 179,490.00 USD | 119,590.00 USD | 154,240.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 82,600.00 USD | 258,330.00 USD | 326,000.00 USD |
| `1D` | `0.0724` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 105,730.00 USD | 206,000.00 USD | 370,890.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 234,040.00 USD | 201,810.00 USD | 268,530.00 USD |
| `1D` | `0.0726` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 29,310.00 USD | 90,560.00 USD | 8,340.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 138,060.00 USD | 83,300.00 USD | 12,350.00 USD |
| `1D` | `0.0728` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 27,890.00 USD | 84,500.00 USD | 27,820.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 42,630.00 USD | 26,380.00 USD | 8,490.00 USD |
| `1D` | `0.0730` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 105,290.00 USD | 25,850.00 USD | 42,110.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 26,590.00 USD | 52,750.00 USD | 89.57 USD |
| `1D` | `0.0732` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 26,690.00 USD | 18,640.00 USD | 60,420.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 0.00 USD | 50,690.00 USD | 100.25 USD |
| `1D` | `0.0734` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 339,370.00 USD | 67,440.00 USD | 1.38 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 141,790.00 USD | 23,950.00 USD | 258.52 USD |
| `1D` | `0.0736` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,700.00 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 113,510.00 USD | 47,850.00 USD | 49,860.00 USD |
| `1D` | `0.0738` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 83,080.00 USD | 23,440.00 USD | 0.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 54,600.00 USD | 0.00 USD | 263.61 USD |
| `1D` | `0.0740` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 54,250.00 USD | 0.00 USD | 34,230.00 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 0.00 USD | 68,120.00 USD | 510.72 USD |
| `1D` | `0.0742` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 133,790.00 USD | 24,700.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 174,420.00 USD | 40,680.00 USD | 245,760.00 USD |
| `1D` | `0.0744` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 185,610.00 USD | 89,270.00 USD | 107,270.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 54,460.00 USD | 31,200.00 USD | 35,270.00 USD |
| `1D` | `0.0746` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 53,190.00 USD | 32,230.00 USD | 162,360.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 625,700.00 USD | 225,930.00 USD | 164,040.00 USD |
| `1D` | `0.0748` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 77,120.00 USD | 0.00 USD | 209,630.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 69,130.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 37,490.00 USD | 0.00 USD |
| `1D` | `0.0752` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 12,650.00 USD | 142,120.00 USD |
| `1D` | `0.0754` | 932,640.00 USD | 0.00 USD | 932,640.00 USD | 0.00 USD | 103,430.00 USD | 278,380.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 550,840.00 USD | 0.00 USD | 550,840.00 USD | 182,850.00 USD | 180,020.00 USD | 167.18 USD |
| `1D` | `0.0756` | 187,800.00 USD | 0.00 USD | 187,800.00 USD | 0.00 USD | 30,100.00 USD | 791.92 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 156,910.00 USD | 0.00 USD | 156,910.00 USD | 130,570.00 USD | 0.00 USD | 1,450.00 USD |
| `1D` | `0.0758` | 24,890.00 USD | 0.00 USD | 24,890.00 USD | 15,180.00 USD | 4,920.00 USD | 570.06 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 4,220.00 USD | 0.00 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 974.82 USD |
| `1D` | `0.0760` | 3,240.00 USD | 0.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0762` | 1,190.00 USD | 0.00 USD | 1,190.00 USD | 0.00 USD | 0.00 USD | 1,190.00 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 69,170.00 USD | 69,170.00 USD | 0.00 USD | 4,000.00 USD | 65,170.00 USD | 0.00 USD |
| `1D` | `0.0763` | 138,340.00 USD | 138,340.00 USD | 0.00 USD | 4,000.00 USD | 65,170.00 USD | 0.00 USD |
| `1D` | `0.0764` | 887,370.00 USD | 887,370.00 USD | 0.00 USD | 356,880.00 USD | 390,100.00 USD | 2,050.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 233,890.00 USD | 248,870.00 USD | 100,260.00 USD |
| `1D` | `0.0766` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 602,560.00 USD | 522,700.00 USD | 40,050.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 302,280.00 USD | 352,540.00 USD | 160,020.00 USD |
| `1D` | `0.0768` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 241,290.00 USD | 93,770.00 USD | 594,390.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 259,990.00 USD | 422,240.00 USD | 286,990.00 USD |
| `1D` | `0.0770` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 396,020.00 USD | 183,310.00 USD | 402,520.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 252,610.00 USD | 343,810.00 USD | 228,450.00 USD |
| `1D` | `0.0772` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 390,170.00 USD | 170,860.00 USD | 711,260.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 129,080.00 USD | 228,140.00 USD | 204,590.00 USD |
| `1D` | `0.0774` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 86,950.00 USD | 217,280.00 USD | 36,420.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 255,450.00 USD | 121,970.00 USD | 47,950.00 USD |
| `1D` | `0.0776` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 249,550.00 USD | 157,720.00 USD | 86,320.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 258,860.00 USD | 301,970.00 USD | 129,090.00 USD |
| `1D` | `0.0778` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 35,730.00 USD | 230,760.00 USD | 369,360.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 223,060.00 USD | 119,670.00 USD | 142,780.00 USD |
| `1D` | `0.0780` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 174,020.00 USD | 53,140.00 USD | 39,320.00 USD |
| `1D` | `0.0781` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 10,320.00 USD |
| `1D` | `0.0782` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 70,430.00 USD | 82,140.00 USD | 85,030.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 45,800.00 USD | 214,890.00 USD | 174,070.00 USD |
| `1D` | `0.0784` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 316,220.00 USD | 101,430.00 USD | 39,240.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 205,570.00 USD | 110,520.00 USD | 78,960.00 USD |
| `1D` | `0.0786` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 234,330.00 USD | 160,700.00 USD | 242,320.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 329,770.00 USD | 386,280.00 USD | 355,430.00 USD |
| `1D` | `0.0788` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 135,470.00 USD | 191,940.00 USD | 102,190.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 296,490.00 USD | 218,540.00 USD | 106,980.00 USD |
| `1D` | `0.0790` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 136,170.00 USD | 57,780.00 USD | 22,570.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 17,560,000.00 USD | 17,560,000.00 USD | 0.00 USD | 179,540.00 USD | 105,210.00 USD | 94,000.00 USD |
| `1D` | `0.0792` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 145,760.00 USD | 37,510.00 USD | 59,590.00 USD |
| `1D` | `0.0793` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46.48 USD |
| `1D` | `0.0794` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 101,610.00 USD | 41,370.00 USD | 84,080.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 24,520.00 USD | 0.00 USD | 70,160.00 USD |
| `1D` | `0.0796` | 18,320,000.00 USD | 18,320,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 18,730,000.00 USD | 18,730,000.00 USD | 0.00 USD | 206,810.00 USD | 89,760.00 USD | 117,580.00 USD |
| `1D` | `0.0798` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 56,190.00 USD | 110,930.00 USD | 677.64 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 19,500,000.00 USD | 19,500,000.00 USD | 0.00 USD | 213,230.00 USD | 193,600.00 USD | 197,100.00 USD |
| `1D` | `0.0800` | 19,650,000.00 USD | 19,650,000.00 USD | 0.00 USD | 39,790.00 USD | 9,760.00 USD | 94,090.00 USD |
| `1D` | `0.0801` | 19,670,000.00 USD | 19,670,000.00 USD | 0.00 USD | 17,000.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `0.0802` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 18,910.00 USD | 1,770.00 USD | 3,430.00 USD |
| `1D` | `0.0803` | 19,790,000.00 USD | 19,790,000.00 USD | 0.00 USD | 16,230.00 USD | 43,340.00 USD | 36,660.00 USD |
| `1D` | `0.0804` | 19,810,000.00 USD | 19,810,000.00 USD | 0.00 USD | 13,900.00 USD | 10,910.00 USD | 755.88 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD |
| `1D` | `0.0806` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 24,270.00 USD | 21,040.00 USD | 215,340.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 221,690.00 USD | 145,040.00 USD | 30,440.00 USD |
| `1D` | `0.0808` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 297,680.00 USD | 118,270.00 USD | 457,440.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 22,050,000.00 USD | 22,050,000.00 USD | 0.00 USD | 252,300.00 USD | 275,640.00 USD | 12,560.00 USD |
| `1D` | `0.0810` | 22,600,000.00 USD | 22,600,000.00 USD | 0.00 USD | 252,220.00 USD | 157,180.00 USD | 134,230.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 22,930,000.00 USD | 22,930,000.00 USD | 0.00 USD | 98,200.00 USD | 229,260.00 USD | 10,300.00 USD |
| `1D` | `0.0812` | 23,250,000.00 USD | 23,250,000.00 USD | 0.00 USD | 138,630.00 USD | 102,020.00 USD | 78,720.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 23,450,000.00 USD | 23,450,000.00 USD | 0.00 USD | 47,340.00 USD | 33,440.00 USD | 120,340.00 USD |
| `1D` | `0.0814` | 23,840,000.00 USD | 23,840,000.00 USD | 0.00 USD | 44,610.00 USD | 109,560.00 USD | 227,760.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 23,980,000.00 USD | 23,980,000.00 USD | 0.00 USD | 42,020.00 USD | 6,740.00 USD | 94,600.00 USD |
| `1D` | `0.0816` | 24,690,000.00 USD | 24,690,000.00 USD | 0.00 USD | 342,130.00 USD | 194,790.00 USD | 177,760.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 25,250,000.00 USD | 25,250,000.00 USD | 0.00 USD | 284,640.00 USD | 136,360.00 USD | 130,520.00 USD |
| `1D` | `0.0818` | 25,980,000.00 USD | 25,980,000.00 USD | 0.00 USD | 261,840.00 USD | 161,260.00 USD | 308,090.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 26,580,000.00 USD | 26,580,000.00 USD | 0.00 USD | 161,320.00 USD | 312,480.00 USD | 128,730.00 USD |
| `1D` | `0.0820` | 27,150,000.00 USD | 27,150,000.00 USD | 0.00 USD | 68,970.00 USD | 177,510.00 USD | 320,100.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 27,560,000.00 USD | 27,560,000.00 USD | 0.00 USD | 180,240.00 USD | 87,420.00 USD | 147,350.00 USD |
| `1D` | `0.0822` | 28,130,000.00 USD | 28,130,000.00 USD | 0.00 USD | 256,340.00 USD | 151,600.00 USD | 155,850.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 28,480,000.00 USD | 28,480,000.00 USD | 0.00 USD | 270,020.00 USD | 72,540.00 USD | 8,610.00 USD |
| `1D` | `0.0824` | 29,040,000.00 USD | 29,040,000.00 USD | 0.00 USD | 172,520.00 USD | 204,930.00 USD | 191,030.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 29,290,000.00 USD | 29,290,000.00 USD | 0.00 USD | 102,430.00 USD | 125,690.00 USD | 21,580.00 USD |
| `1D` | `0.0826` | 29,720,000.00 USD | 29,720,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 29,830,000.00 USD | 29,830,000.00 USD | 0.00 USD | 28,890.00 USD | 62,110.00 USD | 19,240.00 USD |
| `1D` | `0.0828` | 30,170,000.00 USD | 30,170,000.00 USD | 0.00 USD | 197,110.00 USD | 75,940.00 USD | 65,240.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 30,420,000.00 USD | 30,420,000.00 USD | 0.00 USD | 157,080.00 USD | 88,230.00 USD | 168.50 USD |
| `1D` | `0.0830` | 30,550,000.00 USD | 30,550,000.00 USD | 0.00 USD | 57,230.00 USD | 37,820.00 USD | 42,690.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 30,620,000.00 USD | 30,620,000.00 USD | 0.00 USD | 31,420.00 USD | 0.00 USD | 31,710.00 USD |
| `1D` | `0.0832` | 30,930,000.00 USD | 30,930,000.00 USD | 0.00 USD | 154,910.00 USD | 75,990.00 USD | 79,680.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 31,290,000.00 USD | 31,290,000.00 USD | 0.00 USD | 110,470.00 USD | 82,770.00 USD | 169,110.00 USD |
| `1D` | `0.0834` | 31,640,000.00 USD | 31,640,000.00 USD | 0.00 USD | 121,950.00 USD | 94,190.00 USD | 138,320.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 32,010,000.00 USD | 32,010,000.00 USD | 0.00 USD | 114,510.00 USD | 183,090.00 USD | 65,420.00 USD |
| `1D` | `0.0836` | 32,260,000.00 USD | 32,260,000.00 USD | 0.00 USD | 44,050.00 USD | 63,220.00 USD | 145,500.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 32,470,000.00 USD | 32,470,000.00 USD | 0.00 USD | 132,640.00 USD | 31,430.00 USD | 51,030.00 USD |
| `1D` | `0.0838` | 32,760,000.00 USD | 32,760,000.00 USD | 0.00 USD | 171,590.00 USD | 77,480.00 USD | 38,900.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 32,860,000.00 USD | 32,860,000.00 USD | 0.00 USD | 52,570.00 USD | 16,550.00 USD | 30,880.00 USD |
| `1D` | `0.0840` | 32,920,000.00 USD | 32,920,000.00 USD | 0.00 USD | 11,570.00 USD | 15,480.00 USD | 28,060.00 USD |
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
  * Total Open Interest: `1.06B` | Total OI Tokens: `13,873,077,257.0 DOGE`
  * 1h OI Change: `+0.52%` | 4h OI Change: `+3.84%` | 24h OI Change: `-5.26%`
  * Exchange Breakdown: Binance=`245.05M` | Bybit=`107.29M` | OKX=`110.79M` | Hyperliquid=`76.85M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.52K` | Last 24h: `35.55K` | Last 3d: `229.21K` | Last 7d: `310.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0060%` | **USDT OKX** | `-0.0058%` |
| **USDT Bybit** | `-0.0024%` | **USDT KuCoin** | `-0.0046%` |
| **USDT MEXC** | `0.0060%` | **USDT BingX** | `0.0054%` |
| **USDT Gate** | `0.0023%` | **USDT Bitget** | `0.0003%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `50.43%` | `49.57%` | `1.02` | 11,620,000.00 USD |
| `15M` | `Binance` | `48.81%` | `51.19%` | `0.95` | 8,050,000.00 USD |
| `15M` | `OKX` | `60.95%` | `39.05%` | `1.56` | 758,200.00 USD |
| `15M` | `Bybit` | `53.36%` | `46.64%` | `1.14` | 517,830.00 USD |
| `15M` | `KuCoin` | `45.18%` | `54.82%` | `0.82` | 127,680.00 USD |
| `15M` | `Gate` | `52.1%` | `47.9%` | `1.09` | 500,210.00 USD |
| `15M` | `Bitget` | `31.44%` | `68.56%` | `0.46` | 254,060.00 USD |
| `15M` | `BingX` | `49.93%` | `50.07%` | `1.00` | 287,060.00 USD |
| `15M` | `MEXC` | `47.8%` | `52.2%` | `0.92` | 125,030.00 USD |
| `15M` | `Bitunix` | `56.66%` | `43.34%` | `1.31` | 243,750.00 USD |
| `15M` | `Hyperliquid` | `54.8%` | `45.2%` | `1.21` | 456,020.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `57.36%` | `42.64%` | `1.35` | 36,430.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 7,040.00 USD |
| `15M` | `HTX` | `58.48%` | `41.52%` | `1.41` | 9,320.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `57.11%` | `42.89%` | `1.33` | 98,040.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `80.77%` | `19.23%` | `4.20` | 150,530.00 USD |
| `15M` | `Whale Positions` | `48.81%` | `51.19%` | `0.95` | 8,050,000.00 USD |
| `15M` | `Global Accounts` | `50.43%` | `49.57%` | `1.02` | 11,620,000.00 USD |
| `1H` | `DOGE` | `47.15%` | `52.85%` | `0.89` | 80,460,000.00 USD |
| `1H` | `Binance` | `45.86%` | `54.14%` | `0.85` | 53,060,000.00 USD |
| `1H` | `OKX` | `47.17%` | `52.83%` | `0.89` | 7,170,000.00 USD |
| `1H` | `Bybit` | `47.61%` | `52.39%` | `0.91` | 5,080,000.00 USD |
| `1H` | `KuCoin` | `51.7%` | `48.3%` | `1.07` | 643,370.00 USD |
| `1H` | `Gate` | `50.44%` | `49.56%` | `1.02` | 2,770,000.00 USD |
| `1H` | `Bitget` | `40.59%` | `59.41%` | `0.68` | 1,800,000.00 USD |
| `1H` | `BingX` | `50.48%` | `49.52%` | `1.02` | 1,490,000.00 USD |
| `1H` | `MEXC` | `64.55%` | `35.45%` | `1.82` | 1,200,000.00 USD |
| `1H` | `Bitunix` | `56.08%` | `43.92%` | `1.28` | 2,140,000.00 USD |
| `1H` | `Hyperliquid` | `59.8%` | `40.2%` | `1.49` | 2,630,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.55%` | `52.45%` | `0.91` | 196,150.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `20.96%` | `79.04%` | `0.27` | 73,560.00 USD |
| `1H` | `HTX` | `25.22%` | `74.78%` | `0.34` | 541,610.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `49.09%` | `50.91%` | `0.96` | 1,190,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.2%` | `54.8%` | `0.82` | 470,650.00 USD |
| `1H` | `Whale Positions` | `45.86%` | `54.14%` | `0.85` | 53,060,000.00 USD |
| `1H` | `Global Accounts` | `47.15%` | `52.85%` | `0.89` | 80,460,000.00 USD |
| `4H` | `DOGE` | `49.43%` | `50.57%` | `0.98` | 601,860,000.00 USD |
| `4H` | `Binance` | `48.16%` | `51.84%` | `0.93` | 380,850,000.00 USD |
| `4H` | `OKX` | `46.26%` | `53.74%` | `0.86` | 55,820,000.00 USD |
| `4H` | `Bybit` | `58.18%` | `41.82%` | `1.39` | 43,280,000.00 USD |
| `4H` | `KuCoin` | `54.04%` | `45.96%` | `1.18` | 3,570,000.00 USD |
| `4H` | `Gate` | `48.79%` | `51.21%` | `0.95` | 18,120,000.00 USD |
| `4H` | `Bitget` | `51.91%` | `48.09%` | `1.08` | 12,380,000.00 USD |
| `4H` | `BingX` | `39.3%` | `60.7%` | `0.65` | 11,040,000.00 USD |
| `4H` | `MEXC` | `57.39%` | `42.61%` | `1.35` | 5,920,000.00 USD |
| `4H` | `Bitunix` | `51.7%` | `48.3%` | `1.07` | 15,140,000.00 USD |
| `4H` | `Hyperliquid` | `58.26%` | `41.74%` | `1.40` | 29,270,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.73%` | `50.27%` | `0.99` | 3,580,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `31.81%` | `68.19%` | `0.47` | 431,510.00 USD |
| `4H` | `HTX` | `41.95%` | `58.05%` | `0.72` | 2,430,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `70.43%` | `29.57%` | `2.38` | 1,850,000.00 USD |
| `4H` | `Aster` | `52.26%` | `47.74%` | `1.09` | 13,740,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.18%` | `58.82%` | `0.70` | 4,420,000.00 USD |
| `4H` | `Whale Positions` | `48.16%` | `51.84%` | `0.93` | 380,850,000.00 USD |
| `4H` | `Global Accounts` | `49.43%` | `50.57%` | `0.98` | 601,860,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0749` | `0.0750` | `0.0749` | `0.0752` | `0.0748` | 6,915,504.04 USD | 3,908,951.74 USD | 3,006,552.30 USD | 902,399.44 USD | `+13.05%` | `6B / 3S` |
| `5:00 UTC` | `0.0749` | `0.0749` | `0.0749` | `0.0752` | `0.0748` | 4,286,041.88 USD | 2,098,889.29 USD | 2,187,152.59 USD | -88,263.30 USD | `-2.06%` | `4B / 13S` |
| `0:00 UTC` | `0.0751` | `0.0751` | `0.0751` | `0.0752` | `0.0749` | 4,647,855.36 USD | 2,795,154.23 USD | 1,852,701.13 USD | 942,453.10 USD | `+20.28%` | `6B / 2S` |
| `5:00 UTC` | `0.0753` | `0.0752` | `0.0753` | `0.0754` | `0.0750` | 3,128,035.72 USD | 1,829,490.22 USD | 1,298,545.51 USD | 530,944.71 USD | `+16.97%` | `7B / 3S` |
| `0:00 UTC` | `0.0758` | `0.0757` | `0.0758` | `0.0759` | `0.0754` | 5,177,761.26 USD | 2,608,553.38 USD | 2,569,207.88 USD | 39,345.50 USD | `+0.76%` | `6B / 5S` |
| `5:00 UTC` | `0.0761` | `0.0760` | `0.0761` | `0.0761` | `0.0758` | 4,745,125.96 USD | 2,439,783.51 USD | 2,305,342.45 USD | 134,441.06 USD | `+2.83%` | `2B / 3S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0761` | `0.0756` | 6,291,103.20 USD | 2,334,096.16 USD | 3,957,007.04 USD | -1,622,910.88 USD | `-25.80%` | `4B / 13S` |
| `5:00 UTC` | `0.0761` | `0.0761` | `0.0761` | `0.0763` | `0.0759` | 2,882,835.87 USD | 1,316,913.19 USD | 1,565,922.69 USD | -249,009.50 USD | `-8.64%` | `1B / 8S` |
| `0:00 UTC` | `0.0763` | `0.0763` | `0.0763` | `0.0764` | `0.0761` | 3,656,750.71 USD | 1,701,724.26 USD | 1,955,026.45 USD | -253,302.19 USD | `-6.93%` | `3B / 3S` |
| `5:00 UTC` | `0.0763` | `0.0763` | `0.0763` | `0.0764` | `0.0762` | 1,496,580.20 USD | 747,359.00 USD | 749,221.20 USD | -1,862.20 USD | `-0.12%` | `2B / 1S` |

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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `-1.13` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.08`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.93`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0767`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
