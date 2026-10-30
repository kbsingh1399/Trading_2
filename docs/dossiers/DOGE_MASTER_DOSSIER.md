# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0747` | **Live Ask Quote**: `0.0768` | **Mid Price**: `0.0757`
- **Spread Points**: `21.00` | **Spread BPS**: `277.23 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0738` | VWAP Z-Score: `+0.89` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000412` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0769` | Lower -3.00σ Band: `0.0707`
  * Upper +2.51σ Band: `0.0764` | Lower -2.51σ Band: `0.0712`
  * Upper +2.01σ Band: `0.0758` | Lower -2.01σ Band: `0.0717`
  * Upper +2.00σ Band: `0.0758` | Lower -2.00σ Band: `0.0717`
  * Upper +1.28σ Band: `0.0751` | Lower -1.28σ Band: `0.0725`
  * Upper +1.00σ Band: `0.0748` | Lower -1.00σ Band: `0.0728`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0745` | EMA-20=`0.0746` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0749` (Slope: `+0.0000`) | EMA-100=`0.0756`
  * Institutional Anchors: EMA-144=`0.0760` | EMA-200=`0.0764` (Slope: `-0.3195`) | EMA-233=`0.0765`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0754` (Distance: `+0.46%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.15%`)
  * Value Area Low (VAL) = `0.0737` (Distance: `+2.78%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0783` | Weekly POC=`0.0762` | Weekly VAL=`0.0747`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0756` | Low=`0.0741`
  * New York Session (13:00-21:00 UTC): High=`0.0748` | Low=`0.0741`
  * Initial Balance (First Hour): IB High=`0.0754` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0754` - `0.0761`
  * Optimal Trade Entry (OTE 0.705): `0.0759`
  * Structural Invalidation Anchor (0.786): `0.0764`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0758` | `0.0760` | `0.0758` | `0.0758` | `14,456,147` | 1,096,782.28 USD | 138,096.58 USD | `+12.59%` | -36,692,173.94 USD | `+0.87` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.0758` | `0.0759` | `0.0756` | `0.0757` | `17,420,994` | 1,319,115.20 USD | -442,161.29 USD | `-33.52%` | -37,134,335.23 USD | `-1.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0757` | `0.0758` | `0.0757` | `0.0758` | `6,363,004` | 481,975.50 USD | -165,873.85 USD | `-34.42%` | -37,300,209.08 USD | `-0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0754` | `0.0756` | `0.0752` | `0.0755` | `30,952,227` | 2,334,240.03 USD | -264,839.88 USD | `-11.35%` | -36,095,084.91 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0755` | `0.0760` | `0.0754` | `0.0758` | `53,265,206` | 4,037,679.84 USD | 45,145.39 USD | `+1.12%` | -36,049,939.51 USD | `+0.87` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.0758` | `0.0759` | `0.0756` | `0.0758` | `23,783,998` | 1,801,090.71 USD | -608,035.14 USD | `-33.76%` | -36,657,974.65 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.0756` | `0.0761` | `0.0753` | `0.0756` | `194,653,019` | 14,729,253.09 USD | -2,572,015.39 USD | `-17.46%` | -35,337,222.98 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0756` | `0.0758` | `0.0752` | `0.0755` | `120,232,507` | 9,072,419.63 USD | -620,139.43 USD | `-6.84%` | -35,957,362.42 USD | `+0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0755` | `0.0760` | `0.0752` | `0.0758` | `161,494,939` | 12,202,153.21 USD | -700,612.23 USD | `-5.74%` | -36,657,974.65 USD | `+0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0752` | `0.0758` | `476,402,997` | 36,005,534.15 USD | -3,891,146.77 USD | `-10.81%` | -35,590,355.48 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | 1,581,082.63 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -21,458,643.59 USD | `-1.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0752` | `0.0758` | `476,402,997` | 36,005,534.15 USD | -3,891,146.77 USD | `-10.81%` | -35,590,355.48 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.0757`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0758` | `19174.0000` | 1,454.33 USD | 5,817.20 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `19174.0000` | 1,454.31 USD | 4,362.87 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `19174.0000` | 1,454.29 USD | 2,908.56 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `19174.0000` | 1,454.27 USD | 1,454.27 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.0758` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0758` | `33600.0000` | 2,548.06 USD | 2,548.06 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `39149.0000` | 2,968.83 USD | 5,516.88 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `134400.0000` | 10,191.96 USD | 15,708.84 USD | `12 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `134400.0000` | 10,191.82 USD | 25,900.66 USD | `12 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `1432.0000` | 108.59 USD | 26,009.25 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `18810.0000` | 1,426.32 USD | 27,435.57 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `18778.0000` | 1,423.79 USD | 28,859.36 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `38424.0000` | 2,913.19 USD | 31,772.55 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `18779.0000` | 1,423.75 USD | 33,196.30 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `472901.0000` | 35,852.52 USD | 69,048.81 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `68537.0000` | 5,196.00 USD | 74,244.81 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `36533.0000` | 2,769.49 USD | 77,014.30 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `27875.0000` | 2,113.12 USD | 79,127.42 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `92339.0000` | 6,999.76 USD | 86,127.18 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `45984.0000` | 3,485.77 USD | 89,612.95 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `247296.0000` | 18,745.78 USD | 108,358.73 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `147937.0000` | 11,213.92 USD | 119,572.65 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `18778.0000` | 1,423.39 USD | 120,996.04 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `89102.0000` | 6,753.93 USD | 127,749.98 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `573626.0000` | 43,480.28 USD | 171,230.25 USD | `2 orders` | `-0.05%` | `-` |
| `ASK` | `0.0759` | `659.0000` | 50.00 USD | 180,726.79 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0759` | `462879.0000` | 35,116.32 USD | 180,676.79 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0759` | `18810.0000` | 1,427.00 USD | 145,560.48 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0759` | `450139.0000` | 34,148.44 USD | 144,133.47 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0759` | `111446.0000` | 8,454.41 USD | 109,985.03 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0759` | `20499.0000` | 1,555.05 USD | 101,530.62 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0759` | `37981.0000` | 2,881.20 USD | 99,975.57 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `19171.0000` | 1,454.27 USD | 97,094.37 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `19171.0000` | 1,454.25 USD | 95,640.10 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `161919.0000` | 12,282.53 USD | 94,185.84 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `102739.0000` | 7,793.27 USD | 81,903.31 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `432357.0000` | 32,796.01 USD | 74,110.05 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `19171.0000` | 1,454.18 USD | 41,314.04 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `87672.0000` | 6,650.10 USD | 39,859.86 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0759` | `19171.0000` | 1,454.14 USD | 33,209.76 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0759` | `341970.0000` | 25,938.42 USD | 31,755.62 USD | `3 orders` | `+0.01%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `298` | `0xb83d...6e36` | `SHORT` | 7,794,418.31 USD | `102,645,925.00` | `0.0946` | `0.0758` | `1.05` | 1,912,923.34 USD | `+24.54%` | `3X Cross` |
| `308` | `0xc63a...a3cd` | `LONG` | 7,586,300.00 USD | `100,000,000.00` | `0.0856` | `0.0758` | `0.000000` | -978,521.96 USD | `-12.90%` | `10X Cross` |
| `312` | `0x610b...b613` | `LONG` | 7,489,866.91 USD | `98,666,424.00` | `0.0872` | `0.0758` | `0.0604` | -1,110,314.99 USD | `-14.82%` | `5X Cross` |
| `601` | `0x5b5d...c060` | `SHORT` | 3,752,236.55 USD | `49,478,955.00` | `0.0946` | `0.0758` | `2.94` | 929,280.05 USD | `+24.77%` | `3X Cross` |
| `611` | `0xecb6...2b00` | `SHORT` | 3,717,004.11 USD | `48,996,271.00` | `0.0784` | `0.0758` | `0.7043` | 125,987.49 USD | `+3.39%` | `10X Cross` |
| `637` | `0xca49...53c8` | `SHORT` | 3,530,864.98 USD | `46,542,649.00` | `0.0929` | `0.0758` | `0.3915` | 795,179.70 USD | `+22.52%` | `10X Cross` |
| `653` | `0x45d2...4029` | `SHORT` | 3,446,152.64 USD | `45,426,000.00` | `0.0954` | `0.0758` | `0.9593` | 889,476.58 USD | `+25.81%` | `10X Cross` |
| `1191` | `0x458d...ab3b` | `LONG` | 1,854,620.59 USD | `24,454,063.00` | `0.1002` | `0.0758` | `0.0714` | -596,301.31 USD | `-32.15%` | `3X Isolated` |
| `1198` | `0xeadc...9d55` | `LONG` | 1,843,091.73 USD | `24,317,440.00` | `0.0926` | `0.0758` | `0.000000` | -408,502.84 USD | `-22.16%` | `10X Cross` |
| `1330` | `0xf48f...10fe` | `LONG` | 1,626,869.18 USD | `21,424,497.00` | `0.0968` | `0.0758` | `0.0444` | -447,435.43 USD | `-27.50%` | `4X Cross` |
| `1354` | `0x9946...0852` | `SHORT` | 1,581,384.49 USD | `20,845,267.00` | `0.0859` | `0.0758` | `0.1489` | 209,901.52 USD | `+13.27%` | `10X Cross` |
| `1585` | `0x0d6a...ca57` | `LONG` | 1,338,059.45 USD | `17,626,455.00` | `0.0875` | `0.0758` | `0.0626` | -204,045.51 USD | `-15.25%` | `3X Isolated` |
| `1643` | `0x4808...a82c` | `LONG` | 1,276,667.07 USD | `16,828,143.00` | `0.0883` | `0.0758` | `0.0632` | -209,805.91 USD | `-16.43%` | `3X Cross` |
| `1704` | `0x9aa5...58af` | `SHORT` | 1,227,750.90 USD | `16,182,084.00` | `0.0907` | `0.0758` | `0.6236` | 239,454.30 USD | `+19.50%` | `10X Cross` |
| `1790` | `0x31ef...f715` | `LONG` | 1,154,974.79 USD | `15,230,102.00` | `0.0936` | `0.0758` | `0.0668` | -270,721.14 USD | `-23.44%` | `3X Isolated` |
| `1813` | `0xbfc7...80b4` | `SHORT` | 1,138,996.64 USD | `15,020,000.00` | `0.0920` | `0.0758` | `0.1754` | 243,402.65 USD | `+21.37%` | `10X Cross` |
| `1900` | `0x7cee...fc93` | `SHORT` | 1,063,776.37 USD | `14,013,468.00` | `0.0863` | `0.0758` | `0.2644` | 145,100.99 USD | `+13.64%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 7,468.63 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.47K USD at 0.0791 USD [API] | `2026-10-29 13:15:02` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 7,925.53 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.93K USD at 0.0792 USD [API] | `2026-10-29 13:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 23,358.29 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 23.36K USD at 0.0791 USD [API] | `2026-10-29 13:24:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 5,177.50 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.18K USD at 0.0791 USD [API] | `2026-10-29 13:24:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0801` | 16,847.38 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 16.85K USD at 0.0801 USD [API] | `2026-10-29 17:04:14` |
| `ANNOUNCEMENT` | `INFO` | `0.0801` | 10,443.92 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.44K USD at 0.0801 USD [API] | `2026-10-29 17:04:14` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 5,402.81 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.40K USD at 0.0800 USD [API] | `2026-10-29 17:05:53` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 5,145.70 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.15K USD at 0.0800 USD [API] | `2026-10-29 17:16:51` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 7,301.12 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.30K USD at 0.0796 USD [API] | `2026-10-29 18:04:30` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 6,511.06 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.51K USD at 0.0796 USD [API] | `2026-10-29 18:04:30` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 5,148.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.15K USD at 0.0793 USD [API] | `2026-10-29 18:28:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 8,833.99 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 8.83K USD at 0.0792 USD [API] | `2026-10-29 18:38:32` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 10,392.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.39K USD at 0.0792 USD [API] | `2026-10-29 18:38:32` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 9,242.18 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.24K USD at 0.0792 USD [API] | `2026-10-29 18:51:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 182.03 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.18K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 23,344.60 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 23.34K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 8,679.08 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 8.68K USD at 0.0791 USD [API] | `2026-10-29 19:07:46` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 23,344.60 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 23.34K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 622.87 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.62K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 10,475.77 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 10.48K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 9,558.25 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0793 USD [API] | `2026-10-29 19:38:02` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 7,332.37 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.33K USD at 0.0793 USD [API] | `2026-10-29 19:54:46` |
| `ANNOUNCEMENT` | `INFO` | `0.0933` | 4,799.26 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 4.80K USD at 0.0933 USD [API] | `2026-09-28 05:30:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0933` | 706.28 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.71K USD at 0.0933 USD [API] | `2026-09-28 05:30:23` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0157` | 1,500.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0163` | 219.10 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0167` | 5,320.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0174` | 1,030.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0177` | 1,970.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0181` | 127.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 223.22 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 1,480.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 1,190.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0205` | 657.60 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0223` | 138.70 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0230` | 896.17 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 140.69 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0233` | 11,680.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0254` | 4,020.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0257` | 763.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0259` | 23,100.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0265` | 416.51 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0266` | 950.36 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0295` | 157.38 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 520.48 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0308` | 266.67 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0316` | 46,970.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0318` | 1,030.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0319` | 6,010.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0328` | 459.71 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0330` | 133.94 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 762.45 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0347` | 4,660.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 13,700.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 8,390.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0370` | 35,200.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 3,190.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0384` | 1,830.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 181.66 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0387` | 207.27 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 3,960.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 56,970.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 2,030.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0410` | 21,570.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,330.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,250.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.68 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 5,160.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 5,370.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 44,730.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 2,960.00 USD | 16,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 12,480.00 USD | 16,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 10,460.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 7,400.00 USD | 16,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 112,760.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 2,620.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,170.00 USD | 16,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 153.57 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 781.11 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,610.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 1,300.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0462` | 913.53 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0467` | 10,500.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 1,040.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 2,880.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 1,420.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 256.70 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 98,470.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 1,030,000.00 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 58,890.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 1,780.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 7,930.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 1,320.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 4,810.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 106.23 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,310.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 309.15 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 3,520.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 6,970.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 594.46 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,420.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 279,790.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,440.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 4,790.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,400.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,920.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0530` | 1,300.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 9,900.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 50,030.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 42,580.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 800.95 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 1,040.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 4,820.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,550.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 4,080.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 95,630.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 903.30 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 28,420.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 347.32 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 25,270.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 10,830.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 144.08 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 4,440.00 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 1,070.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 4,060.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 50,510.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 622.09 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 16,730.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 3,930.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 703.21 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,140.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,300.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 4,320.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 644.22 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 3,580.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 360,820.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 10,360.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 2,880.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 848.05 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 6,010,000.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 1,940.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 5,110.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 412.21 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0619` | 782.68 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 17,850.00 USD | 7,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,420.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 1,120.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,430.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 479.68 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 9,740.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 3,420.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 733.80 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,880.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,180.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 367.23 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0650` | 21,580.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 14,160.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0657` | 30,770,000.00 USD | 30,770,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0661` | 30,750,000.00 USD | 30,750,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0662` | 30,710,000.00 USD | 30,710,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0663` | 13,740.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0665` | 30,710,000.00 USD | 30,710,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 8,880.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0669` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 6,120.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 4,830.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0674` | 30,520,000.00 USD | 30,520,000.00 USD | 5,520.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0675` | 30,510,000.00 USD | 30,510,000.00 USD | 19,910.00 USD | 4,530.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0676` | 30,470,000.00 USD | 30,470,000.00 USD | 6,810.00 USD | 0.00 USD | 475.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,610.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0677` | 18,620,000.00 USD | 18,620,000.00 USD | 67,140.00 USD | 96,830.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0677` | 30,460,000.00 USD | 30,460,000.00 USD | 3,660.00 USD | 9,140.00 USD | 609.05 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 18,440,000.00 USD | 18,440,000.00 USD | 40,890.00 USD | 47,200.00 USD | 80,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0678` | 30,450,000.00 USD | 30,450,000.00 USD | 12,840.00 USD | 51,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 18,270,000.00 USD | 18,270,000.00 USD | 72,650.00 USD | 39,580.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0679` | 30,380,000.00 USD | 30,380,000.00 USD | 19,040.00 USD | 8,140.00 USD | 74,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 18,150,000.00 USD | 18,150,000.00 USD | 51,160.00 USD | 43,850.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0680` | 30,280,000.00 USD | 30,280,000.00 USD | 84,730.00 USD | 47,420.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 390.81 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 18,020,000.00 USD | 18,020,000.00 USD | 36,810.00 USD | 55,770.00 USD | 150,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0681` | 29,990,000.00 USD | 29,990,000.00 USD | 54,210.00 USD | 14,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0682` | 17,770,000.00 USD | 17,770,000.00 USD | 15,430.00 USD | 67,700.00 USD | 32,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0682` | 29,920,000.00 USD | 29,920,000.00 USD | 0.00 USD | 35,790.00 USD | 66,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,770.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 17,660,000.00 USD | 17,660,000.00 USD | 27,270.00 USD | 32,750.00 USD | 467.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0683` | 29,810,000.00 USD | 29,810,000.00 USD | 0.00 USD | 22,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 3,040.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 17,600,000.00 USD | 17,600,000.00 USD | 24,150.00 USD | 26,540.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0684` | 29,790,000.00 USD | 29,790,000.00 USD | 111,040.00 USD | 4,760.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 79,490.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 17,540,000.00 USD | 17,540,000.00 USD | 58,140.00 USD | 14,450.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0685` | 29,670,000.00 USD | 29,670,000.00 USD | 31,800.00 USD | 73,160.00 USD | 24,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 8,890.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 17,440,000.00 USD | 17,440,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0686` | 29,550,000.00 USD | 29,550,000.00 USD | 57,320.00 USD | 64,030.00 USD | 388.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 5,120.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 17,350,000.00 USD | 17,350,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0687` | 29,420,000.00 USD | 29,420,000.00 USD | 44,400.00 USD | 64,060.00 USD | 617.20 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 50,630.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 17,270,000.00 USD | 17,270,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0688` | 29,310,000.00 USD | 29,310,000.00 USD | 40,320.00 USD | 0.00 USD | 60,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 345.83 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 17,210,000.00 USD | 17,210,000.00 USD | 10,400.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0689` | 29,210,000.00 USD | 29,210,000.00 USD | 185,160.00 USD | 77,640.00 USD | 277.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 508,320.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0690` | 28,950,000.00 USD | 28,950,000.00 USD | 112,090.00 USD | 64,360.00 USD | 73,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 17,200,000.00 USD | 17,200,000.00 USD | 1,460.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0691` | 28,700,000.00 USD | 28,700,000.00 USD | 49,920.00 USD | 30,660.00 USD | 57,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 17,200,000.00 USD | 17,200,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0692` | 28,560,000.00 USD | 28,560,000.00 USD | 78,440.00 USD | 76,890.00 USD | 41,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,140.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 17,170,000.00 USD | 17,170,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0693` | 28,360,000.00 USD | 28,360,000.00 USD | 128,710.00 USD | 113,280.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 17,150,000.00 USD | 17,150,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0694` | 28,080,000.00 USD | 28,080,000.00 USD | 169,230.00 USD | 67,150.00 USD | 102,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 17,130,000.00 USD | 17,130,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0695` | 27,750,000.00 USD | 27,750,000.00 USD | 113,240.00 USD | 145,370.00 USD | 110,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 27,380,000.00 USD | 27,380,000.00 USD | 100,230.00 USD | 61,080.00 USD | 186,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 4,950.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 17,120,000.00 USD | 17,120,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0697` | 27,030,000.00 USD | 27,030,000.00 USD | 41,960.00 USD | 87,540.00 USD | 76,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 6,970.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 17,060,000.00 USD | 17,060,000.00 USD | 10,960.00 USD | 10,400.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 26,820,000.00 USD | 26,820,000.00 USD | 127,350.00 USD | 103,870.00 USD | 71,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,910.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 17,030,000.00 USD | 17,030,000.00 USD | 38,680.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0699` | 26,520,000.00 USD | 26,520,000.00 USD | 198,220.00 USD | 101,580.00 USD | 67,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 16,990,000.00 USD | 16,990,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 26,150,000.00 USD | 26,150,000.00 USD | 117,390.00 USD | 110,810.00 USD | 86,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 16,870,000.00 USD | 16,870,000.00 USD | 32,570.00 USD | 108,360.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0701` | 25,840,000.00 USD | 25,840,000.00 USD | 166,270.00 USD | 8,980.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,180.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 16,720,000.00 USD | 16,720,000.00 USD | 47,790.00 USD | 0.00 USD | 122.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 25,610,000.00 USD | 25,610,000.00 USD | 168,320.00 USD | 97,270.00 USD | 50,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 16,680,000.00 USD | 16,680,000.00 USD | 139,990.00 USD | 57,870.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0703` | 25,290,000.00 USD | 25,290,000.00 USD | 107,990.00 USD | 23,160.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 3,790.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 16,470,000.00 USD | 16,470,000.00 USD | 4,460.00 USD | 31,030.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 25,160,000.00 USD | 25,160,000.00 USD | 139,040.00 USD | 55,790.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 780.37 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 16,440,000.00 USD | 16,440,000.00 USD | 41,460.00 USD | 30,720.00 USD | 34,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0705` | 24,950,000.00 USD | 24,950,000.00 USD | 85,040.00 USD | 77,390.00 USD | 160,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 16,330,000.00 USD | 16,330,000.00 USD | 24,210.00 USD | 1,120.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 24,620,000.00 USD | 24,620,000.00 USD | 25,760.00 USD | 13,870.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 608.86 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 16,290,000.00 USD | 16,290,000.00 USD | 139,250.00 USD | 69,310.00 USD | 45,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0707` | 24,540,000.00 USD | 24,540,000.00 USD | 145,730.00 USD | 23,290.00 USD | 109,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 16,040,000.00 USD | 16,040,000.00 USD | 69,400.00 USD | 62,000.00 USD | 107,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 24,260,000.00 USD | 24,260,000.00 USD | 20,200.00 USD | 31,420.00 USD | 51,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 15,800,000.00 USD | 15,800,000.00 USD | 38,730.00 USD | 82,010.00 USD | 149,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0709` | 24,160,000.00 USD | 24,160,000.00 USD | 465,090.00 USD | 128,300.00 USD | 87,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 351.63 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 15,530,000.00 USD | 15,530,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 23,470,000.00 USD | 23,470,000.00 USD | 196,450.00 USD | 161,070.00 USD | 62,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 4,720.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 15,200,000.00 USD | 15,200,000.00 USD | 49,210.00 USD | 25,670.00 USD | 43,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0711` | 23,050,000.00 USD | 23,050,000.00 USD | 89,280.00 USD | 91,060.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 2,190.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 15,080,000.00 USD | 15,080,000.00 USD | 165,590.00 USD | 46,690.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 22,850,000.00 USD | 22,850,000.00 USD | 200,920.00 USD | 117,120.00 USD | 72,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,740.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 14,860,000.00 USD | 14,860,000.00 USD | 75,840.00 USD | 85,230.00 USD | 63,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0713` | 22,450,000.00 USD | 22,450,000.00 USD | 178,680.00 USD | 54,360.00 USD | 67,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 14,640,000.00 USD | 14,640,000.00 USD | 123,320.00 USD | 51,930.00 USD | 48,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 22,150,000.00 USD | 22,150,000.00 USD | 92,880.00 USD | 49,400.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 13,270.00 USD | 408,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 14,410,000.00 USD | 14,410,000.00 USD | 81,850.00 USD | 238,460.00 USD | 43,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0715` | 21,970,000.00 USD | 21,970,000.00 USD | 138,920.00 USD | 2,060.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 395,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 14,050,000.00 USD | 14,050,000.00 USD | 19,480.00 USD | 51,080.00 USD | 215.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 21,800,000.00 USD | 21,800,000.00 USD | 123,820.00 USD | 189,070.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 4,970.00 USD | 387,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 13,980,000.00 USD | 13,980,000.00 USD | 238,310.00 USD | 96,160.00 USD | 385.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0717` | 21,470,000.00 USD | 21,470,000.00 USD | 156,500.00 USD | 1,810.00 USD | 32,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 48,180.00 USD | 382,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 13,650,000.00 USD | 13,650,000.00 USD | 64,570.00 USD | 101,030.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 21,280,000.00 USD | 21,280,000.00 USD | 61,410.00 USD | 22,840.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 960.13 USD | 334,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 13,470,000.00 USD | 13,470,000.00 USD | 231,180.00 USD | 45,330.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0719` | 21,150,000.00 USD | 21,150,000.00 USD | 163,670.00 USD | 29,960.00 USD | 228,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 333,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 13,120,000.00 USD | 13,120,000.00 USD | 141,760.00 USD | 50,600.00 USD | 72,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 20,730,000.00 USD | 20,730,000.00 USD | 282,840.00 USD | 169,120.00 USD | 54,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 5,090.00 USD | 331,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 12,850,000.00 USD | 12,850,000.00 USD | 308,410.00 USD | 298,040.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0721` | 20,220,000.00 USD | 20,220,000.00 USD | 139,860.00 USD | 116,340.00 USD | 40,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 613.35 USD | 326,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 12,180,000.00 USD | 12,180,000.00 USD | 199,310.00 USD | 130,350.00 USD | 150,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 19,930,000.00 USD | 19,930,000.00 USD | 54,310.00 USD | 26,930.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 38,130.00 USD | 325,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 11,700,000.00 USD | 11,700,000.00 USD | 166,340.00 USD | 283,230.00 USD | 369,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0723` | 19,840,000.00 USD | 19,840,000.00 USD | 204,990.00 USD | 144,790.00 USD | 126,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 286,760.00 USD | 287,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 10,880,000.00 USD | 10,880,000.00 USD | 224,260.00 USD | 256,770.00 USD | 402,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 19,360,000.00 USD | 19,360,000.00 USD | 1,050,000.00 USD | 84,550.00 USD | 186,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 984.89 USD | 984.89 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 10,000,000.00 USD | 10,000,000.00 USD | 276,150.00 USD | 262,460.00 USD | 311,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0725` | 18,040,000.00 USD | 18,040,000.00 USD | 174,770.00 USD | 304,550.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 9,150,000.00 USD | 9,150,000.00 USD | 153,630.00 USD | 148,410.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 17,540,000.00 USD | 17,540,000.00 USD | 167,610.00 USD | 227,020.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 8,780,000.00 USD | 8,780,000.00 USD | 191,440.00 USD | 161,760.00 USD | 45,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0727` | 17,050,000.00 USD | 17,050,000.00 USD | 81,590.00 USD | 205,010.00 USD | 558.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 8,390,000.00 USD | 8,390,000.00 USD | 73,270.00 USD | 177,390.00 USD | 65,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 16,770,000.00 USD | 16,770,000.00 USD | 34,520.00 USD | 22,770.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 8,070,000.00 USD | 8,070,000.00 USD | 87,260.00 USD | 41,110.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0729` | 16,680,000.00 USD | 16,680,000.00 USD | 112,700.00 USD | 82,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,930,000.00 USD | 7,930,000.00 USD | 123,090.00 USD | 55,310.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 16,480,000.00 USD | 16,480,000.00 USD | 384,130.00 USD | 25,240.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 7,700,000.00 USD | 7,700,000.00 USD | 44,230.00 USD | 81,130.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0731` | 16,060,000.00 USD | 16,060,000.00 USD | 181,180.00 USD | 24,050.00 USD | 8,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 7,550,000.00 USD | 7,550,000.00 USD | 153,570.00 USD | 93,810.00 USD | 93,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 15,850,000.00 USD | 15,850,000.00 USD | 344,710.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 7,210,000.00 USD | 7,210,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0733` | 15,500,000.00 USD | 15,500,000.00 USD | 125,410.00 USD | 0.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 7,020,000.00 USD | 7,020,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 15,350,000.00 USD | 15,350,000.00 USD | 183,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 6,570,000.00 USD | 6,570,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0735` | 15,170,000.00 USD | 15,170,000.00 USD | 406,040.00 USD | 93,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 6,400,000.00 USD | 6,400,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 14,670,000.00 USD | 14,670,000.00 USD | 272,970.00 USD | 385,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 6,160,000.00 USD | 6,160,000.00 USD | 145,660.00 USD | 69,370.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0737` | 14,010,000.00 USD | 14,010,000.00 USD | 233,090.00 USD | 153,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,890,000.00 USD | 5,890,000.00 USD | 226,750.00 USD | 73,230.00 USD | 85,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 13,620,000.00 USD | 13,620,000.00 USD | 265,850.00 USD | 474,350.00 USD | 40,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,510,000.00 USD | 5,510,000.00 USD | 294,920.00 USD | 101,560.00 USD | 62,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0739` | 12,840,000.00 USD | 12,840,000.00 USD | 218,050.00 USD | 40,680.00 USD | 69,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 5,050,000.00 USD | 5,050,000.00 USD | 99,850.00 USD | 121,290.00 USD | 117,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 12,510,000.00 USD | 12,510,000.00 USD | 101,490.00 USD | 91,130.00 USD | 37,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,710,000.00 USD | 4,710,000.00 USD | 217,950.00 USD | 183,810.00 USD | 102,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0741` | 12,280,000.00 USD | 12,280,000.00 USD | 66,970.00 USD | 251,010.00 USD | 178,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,210,000.00 USD | 4,210,000.00 USD | 90,280.00 USD | 290,690.00 USD | 80,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 11,790,000.00 USD | 11,790,000.00 USD | 478,860.00 USD | 163,570.00 USD | 481,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,740,000.00 USD | 3,740,000.00 USD | 257,710.00 USD | 226,460.00 USD | 319,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0743` | 10,660,000.00 USD | 10,660,000.00 USD | 295,530.00 USD | 45,530.00 USD | 635,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 2,940,000.00 USD | 2,940,000.00 USD | 274,880.00 USD | 118,720.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 9,690,000.00 USD | 9,690,000.00 USD | 325,550.00 USD | 495,640.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,440,000.00 USD | 2,440,000.00 USD | 87,580.00 USD | 88,750.00 USD | 46,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0745` | 8,730,000.00 USD | 8,730,000.00 USD | 1,100,000.00 USD | 455,650.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,220,000.00 USD | 2,220,000.00 USD | 88,460.00 USD | 86,840.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 6,980,000.00 USD | 6,980,000.00 USD | 784,410.00 USD | 925,150.00 USD | 364,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,900,000.00 USD | 1,900,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0747` | 4,910,000.00 USD | 4,910,000.00 USD | 626,490.00 USD | 907,690.00 USD | 285,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 914,030.00 USD | 914,030.00 USD | 80,900.00 USD | 109,690.00 USD | 198,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 3,090,000.00 USD | 3,090,000.00 USD | 706,340.00 USD | 324,980.00 USD | 181,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 524,580.00 USD | 524,580.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0749` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 134,940.00 USD | 694,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 179,540.00 USD | 179,540.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 84,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 115,190.00 USD | 115,190.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0751` | 961,320.00 USD | 961,320.00 USD | 0.00 USD | 30,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 67,170.00 USD | 67,170.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 930,410.00 USD | 930,410.00 USD | 751,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 42,740.00 USD | 42,740.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0753` | 179,300.00 USD | 179,300.00 USD | 0.00 USD | 53,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 30,100.00 USD | 30,100.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 125,430.00 USD | 125,430.00 USD | 0.00 USD | 125,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 19,100.00 USD | 19,100.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 38,200.00 USD | 38,200.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0758` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0758` | 9,840.00 USD | 9,840.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0758` | 104,490.00 USD | 104,490.00 USD | 0.00 USD | 66,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0759` | 10,010.00 USD | 10,010.00 USD | 0.00 USD | 0.00 USD | 160.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0759` | 144,860.00 USD | 144,860.00 USD | 40,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 10,430.00 USD | 10,430.00 USD | 0.00 USD | 0.00 USD | 420.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 10,590.00 USD | 10,590.00 USD | 0.00 USD | 0.00 USD | 168.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 25,420.00 USD | 25,420.00 USD | 0.00 USD | 14,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0764` | 399,460.00 USD | 399,460.00 USD | 0.00 USD | 254,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 373,580.00 USD | 373,580.00 USD | 211,600.00 USD | 37,120.00 USD | 99,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0765` | 1,410,000.00 USD | 1,410,000.00 USD | 772,480.00 USD | 241,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,150,000.00 USD | 1,150,000.00 USD | 352,420.00 USD | 421,720.00 USD | 291.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0766` | 2,100,000.00 USD | 2,100,000.00 USD | 594,350.00 USD | 90,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 1,810,000.00 USD | 1,810,000.00 USD | 164,440.00 USD | 335,150.00 USD | 159,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0767` | 2,730,000.00 USD | 2,730,000.00 USD | 587,940.00 USD | 45,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 3,000,000.00 USD | 3,000,000.00 USD | 372,440.00 USD | 143,560.00 USD | 680,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0768` | 2,950,000.00 USD | 2,950,000.00 USD | 117,000.00 USD | 7,860.00 USD | 92,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 4,350,000.00 USD | 4,350,000.00 USD | 471,540.00 USD | 522,820.00 USD | 350,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0769` | 4,330,000.00 USD | 4,330,000.00 USD | 861,620.00 USD | 76,450.00 USD | 445,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,590,000.00 USD | 5,590,000.00 USD | 456,790.00 USD | 301,010.00 USD | 487,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0770` | 5,340,000.00 USD | 5,340,000.00 USD | 392,100.00 USD | 325,170.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 6,750,000.00 USD | 6,750,000.00 USD | 441,280.00 USD | 459,510.00 USD | 251,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0771` | 7,000,000.00 USD | 7,000,000.00 USD | 597,990.00 USD | 520,750.00 USD | 540,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 8,320,000.00 USD | 8,320,000.00 USD | 480,450.00 USD | 327,770.00 USD | 765,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0772` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 284,970.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 9,220,000.00 USD | 9,220,000.00 USD | 212,370.00 USD | 413,920.00 USD | 278,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0773` | 7,480,000.00 USD | 7,480,000.00 USD | 69,030.00 USD | 62,610.00 USD | 62,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,680,000.00 USD | 9,680,000.00 USD | 176,230.00 USD | 246,740.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0774` | 7,830,000.00 USD | 7,830,000.00 USD | 137,990.00 USD | 210,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 10,210,000.00 USD | 10,210,000.00 USD | 288,570.00 USD | 180,890.00 USD | 61,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0775` | 8,700,000.00 USD | 8,700,000.00 USD | 707,860.00 USD | 164,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,860,000.00 USD | 10,860,000.00 USD | 284,830.00 USD | 214,460.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0776` | 8,990,000.00 USD | 8,990,000.00 USD | 250,110.00 USD | 39,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 11,760,000.00 USD | 11,760,000.00 USD | 401,010.00 USD | 342,630.00 USD | 163,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0777` | 9,260,000.00 USD | 9,260,000.00 USD | 15,870.00 USD | 247,550.00 USD | 693.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 12,620,000.00 USD | 12,620,000.00 USD | 116,640.00 USD | 340,450.00 USD | 401,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0778` | 9,650,000.00 USD | 9,650,000.00 USD | 229,240.00 USD | 86,160.00 USD | 78,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 13,380,000.00 USD | 13,380,000.00 USD | 345,840.00 USD | 210,420.00 USD | 205,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0779` | 10,270,000.00 USD | 10,270,000.00 USD | 41,210.00 USD | 215,530.00 USD | 359,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 13,710,000.00 USD | 13,710,000.00 USD | 212,580.00 USD | 78,920.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0780` | 10,510,000.00 USD | 10,510,000.00 USD | 169,380.00 USD | 64,660.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 14,080,000.00 USD | 14,080,000.00 USD | 151,030.00 USD | 193,800.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0781` | 10,600,000.00 USD | 10,600,000.00 USD | 17,030.00 USD | 77,790.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 14,340,000.00 USD | 14,340,000.00 USD | 87,770.00 USD | 92,890.00 USD | 79,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0782` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 148,920.00 USD | 195,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 14,930,000.00 USD | 14,930,000.00 USD | 129,550.00 USD | 239,780.00 USD | 220,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0783` | 11,160,000.00 USD | 11,160,000.00 USD | 32,110.00 USD | 159,820.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 15,590,000.00 USD | 15,590,000.00 USD | 436,380.00 USD | 152,210.00 USD | 70,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0784` | 11,500,000.00 USD | 11,500,000.00 USD | 109,020.00 USD | 45,010.00 USD | 187,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 16,120,000.00 USD | 16,120,000.00 USD | 238,930.00 USD | 171,160.00 USD | 120,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0785` | 12,010,000.00 USD | 12,010,000.00 USD | 248,170.00 USD | 120,330.00 USD | 144,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 16,990,000.00 USD | 16,990,000.00 USD | 352,080.00 USD | 218,550.00 USD | 296,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0786` | 12,900,000.00 USD | 12,900,000.00 USD | 201,610.00 USD | 202,070.00 USD | 488,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 18,220,000.00 USD | 18,220,000.00 USD | 380,000.00 USD | 464,730.00 USD | 386,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0787` | 13,610,000.00 USD | 13,610,000.00 USD | 235,890.00 USD | 143,980.00 USD | 324,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 354.19 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 18,820,000.00 USD | 18,820,000.00 USD | 180,850.00 USD | 284,830.00 USD | 140,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0788` | 13,850,000.00 USD | 13,850,000.00 USD | 74,330.00 USD | 22,770.00 USD | 146,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 19,500,000.00 USD | 19,500,000.00 USD | 341,120.00 USD | 233,260.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0789` | 14,450,000.00 USD | 14,450,000.00 USD | 260,530.00 USD | 236,420.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 19,770,000.00 USD | 19,770,000.00 USD | 156,500.00 USD | 87,240.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0790` | 14,870,000.00 USD | 14,870,000.00 USD | 353,930.00 USD | 65,630.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 20,240,000.00 USD | 20,240,000.00 USD | 205,560.00 USD | 133,580.00 USD | 125,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0791` | 15,040,000.00 USD | 15,040,000.00 USD | 142,610.00 USD | 15,670.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0791` | 1,650.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0792` | 20,590,000.00 USD | 20,590,000.00 USD | 224,560.00 USD | 57,840.00 USD | 74,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0792` | 15,110,000.00 USD | 15,110,000.00 USD | 13,630.00 USD | 61,220.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0793` | 20,600,000.00 USD | 20,600,000.00 USD | 5,950.00 USD | 0.00 USD | 289.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0793` | 15,370,000.00 USD | 15,370,000.00 USD | 13,920.00 USD | 0.00 USD | 244,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0794` | 3,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0794` | 20,950,000.00 USD | 20,950,000.00 USD | 158,580.00 USD | 96,210.00 USD | 100,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0794` | 15,630,000.00 USD | 15,630,000.00 USD | 23,360.00 USD | 0.00 USD | 234,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 104.72 USD | 5,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0795` | 21,200,000.00 USD | 21,200,000.00 USD | 94,340.00 USD | 45,380.00 USD | 103,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0795` | 16,050,000.00 USD | 16,050,000.00 USD | 183,540.00 USD | 0.00 USD | 235,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 3,610.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0796` | 21,410,000.00 USD | 21,410,000.00 USD | 202,390.00 USD | 12,890.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 16,610,000.00 USD | 16,610,000.00 USD | 334,830.00 USD | 149,090.00 USD | 77,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 21,720,000.00 USD | 21,720,000.00 USD | 206,810.00 USD | 89,760.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0797` | 17,010,000.00 USD | 17,010,000.00 USD | 305,960.00 USD | 54,460.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 21,790,000.00 USD | 21,790,000.00 USD | 58,670.00 USD | 9,940.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 17,660,000.00 USD | 17,660,000.00 USD | 520,400.00 USD | 54,200.00 USD | 73,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 22,050,000.00 USD | 22,050,000.00 USD | 43,250.00 USD | 191,860.00 USD | 25,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0799` | 17,780,000.00 USD | 17,780,000.00 USD | 41,190.00 USD | 76,670.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 22,200,000.00 USD | 22,200,000.00 USD | 48,550.00 USD | 9,760.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0800` | 17,930,000.00 USD | 17,930,000.00 USD | 46,190.00 USD | 0.00 USD | 102,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 22,230,000.00 USD | 22,230,000.00 USD | 25,740.00 USD | 0.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0801` | 17,970,000.00 USD | 17,970,000.00 USD | 38,850.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 22,260,000.00 USD | 22,260,000.00 USD | 27,390.00 USD | 1,770.00 USD | 122.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0802` | 17,990,000.00 USD | 17,990,000.00 USD | 12,270.00 USD | 0.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 22,370,000.00 USD | 22,370,000.00 USD | 25,660.00 USD | 43,340.00 USD | 41,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0803` | 18,030,000.00 USD | 18,030,000.00 USD | 45,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 213.09 USD | 9,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0804` | 22,380,000.00 USD | 22,380,000.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 18,140,000.00 USD | 18,140,000.00 USD | 108,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 826.14 USD | 10,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0805` | 22,550,000.00 USD | 22,550,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0805` | 18,360,000.00 USD | 18,360,000.00 USD | 120,200.00 USD | 43,910.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 22,820,000.00 USD | 22,820,000.00 USD | 28,730.00 USD | 21,040.00 USD | 215,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 18,460,000.00 USD | 18,460,000.00 USD | 99,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0806` | 213.40 USD | 10,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0807` | 23,220,000.00 USD | 23,220,000.00 USD | 228,350.00 USD | 143,670.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0807` | 19,800,000.00 USD | 19,800,000.00 USD | 118,470.00 USD | 934,840.00 USD | 294,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 23,870,000.00 USD | 23,870,000.00 USD | 152,200.00 USD | 116,140.00 USD | 382,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 20,720,000.00 USD | 20,720,000.00 USD | 9,880.00 USD | 910,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 24,220,000.00 USD | 24,220,000.00 USD | 111,710.00 USD | 220,760.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0809` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 851,040.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 24,650,000.00 USD | 24,650,000.00 USD | 175,100.00 USD | 127,690.00 USD | 132,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 21,970,000.00 USD | 21,970,000.00 USD | 131,030.00 USD | 264,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 24,850,000.00 USD | 24,850,000.00 USD | 100,060.00 USD | 85,950.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0811` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 466,230.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0811` | 215.29 USD | 10,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0812` | 25,100,000.00 USD | 25,100,000.00 USD | 133,170.00 USD | 101,130.00 USD | 19,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 22,780,000.00 USD | 22,780,000.00 USD | 138,370.00 USD | 200,500.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 25,230,000.00 USD | 25,230,000.00 USD | 37,200.00 USD | 28,660.00 USD | 56,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0813` | 23,510,000.00 USD | 23,510,000.00 USD | 378,950.00 USD | 347,890.00 USD | 874.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 25,520,000.00 USD | 25,520,000.00 USD | 43,650.00 USD | 108,690.00 USD | 143,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 24,100,000.00 USD | 24,100,000.00 USD | 142,940.00 USD | 446,780.00 USD | 3,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 25,640,000.00 USD | 25,640,000.00 USD | 20,890.00 USD | 6,740.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0815` | 24,960,000.00 USD | 24,960,000.00 USD | 447,170.00 USD | 144,240.00 USD | 265,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 26,340,000.00 USD | 26,340,000.00 USD | 323,740.00 USD | 194,310.00 USD | 179,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 25,820,000.00 USD | 25,820,000.00 USD | 267,850.00 USD | 451,830.00 USD | 145,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 26,890,000.00 USD | 26,890,000.00 USD | 280,410.00 USD | 134,560.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0817` | 27,340,000.00 USD | 27,340,000.00 USD | 789,320.00 USD | 294,010.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 27,550,000.00 USD | 27,550,000.00 USD | 232,030.00 USD | 161,260.00 USD | 267,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 28,310,000.00 USD | 28,310,000.00 USD | 249,420.00 USD | 327,510.00 USD | 388,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 11,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 28,140,000.00 USD | 28,140,000.00 USD | 153,870.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0819` | 29,460,000.00 USD | 29,460,000.00 USD | 422,920.00 USD | 184,980.00 USD | 540,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 28,680,000.00 USD | 28,680,000.00 USD | 42,510.00 USD | 172,050.00 USD | 319,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 30,350,000.00 USD | 30,350,000.00 USD | 288,610.00 USD | 382,680.00 USD | 217,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 28,950,000.00 USD | 28,950,000.00 USD | 144,440.00 USD | 48,110.00 USD | 85,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0821` | 31,810,000.00 USD | 31,810,000.00 USD | 916,830.00 USD | 377,990.00 USD | 172,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 29,510,000.00 USD | 29,510,000.00 USD | 249,310.00 USD | 151,600.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 32,520,000.00 USD | 32,520,000.00 USD | 374,110.00 USD | 203,780.00 USD | 128,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 29,860,000.00 USD | 29,860,000.00 USD | 267,050.00 USD | 72,540.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0823` | 33,590,000.00 USD | 33,590,000.00 USD | 510,700.00 USD | 317,120.00 USD | 237,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 30,420,000.00 USD | 30,420,000.00 USD | 168,680.00 USD | 204,930.00 USD | 190,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 34,530,000.00 USD | 34,530,000.00 USD | 470,790.00 USD | 274,570.00 USD | 194,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 30,670,000.00 USD | 30,670,000.00 USD | 102,430.00 USD | 125,690.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0825` | 35,170,000.00 USD | 35,170,000.00 USD | 290,680.00 USD | 239,750.00 USD | 112,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0825` | 217.85 USD | 11,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0826` | 31,100,000.00 USD | 31,100,000.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 36,000,000.00 USD | 36,000,000.00 USD | 514,230.00 USD | 68,910.00 USD | 251,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 31,200,000.00 USD | 31,200,000.00 USD | 19,540.00 USD | 65,440.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0827` | 36,330,000.00 USD | 36,330,000.00 USD | 144,110.00 USD | 160,890.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 31,580,000.00 USD | 31,580,000.00 USD | 211,700.00 USD | 83,250.00 USD | 80,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 36,870,000.00 USD | 36,870,000.00 USD | 376,390.00 USD | 110,640.00 USD | 54,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 218.81 USD | 11,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0829` | 31,870,000.00 USD | 31,870,000.00 USD | 198,070.00 USD | 89,690.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0829` | 37,400,000.00 USD | 37,400,000.00 USD | 283,400.00 USD | 67,100.00 USD | 173,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 32,010,000.00 USD | 32,010,000.00 USD | 54,060.00 USD | 37,820.00 USD | 43,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 37,760,000.00 USD | 37,760,000.00 USD | 112,420.00 USD | 80,560.00 USD | 173,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 32,090,000.00 USD | 32,090,000.00 USD | 20,050.00 USD | 16,920.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0831` | 38,210,000.00 USD | 38,210,000.00 USD | 294,840.00 USD | 53,670.00 USD | 98,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,670.00 USD | 15,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 32,470,000.00 USD | 32,470,000.00 USD | 182,190.00 USD | 93,160.00 USD | 100,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 38,820,000.00 USD | 38,820,000.00 USD | 186,700.00 USD | 262,800.00 USD | 160,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 32,880,000.00 USD | 32,880,000.00 USD | 122,770.00 USD | 111,030.00 USD | 181,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0833` | 39,340,000.00 USD | 39,340,000.00 USD | 266,360.00 USD | 152,020.00 USD | 100,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 33,280,000.00 USD | 33,280,000.00 USD | 123,130.00 USD | 127,940.00 USD | 149,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 39,840,000.00 USD | 39,840,000.00 USD | 90,460.00 USD | 146,730.00 USD | 265,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 33,660,000.00 USD | 33,660,000.00 USD | 120,730.00 USD | 188,990.00 USD | 64,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0835` | 40,500,000.00 USD | 40,500,000.00 USD | 275,000.00 USD | 115,070.00 USD | 271,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 33,900,000.00 USD | 33,900,000.00 USD | 37,940.00 USD | 57,720.00 USD | 146,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 40,820,000.00 USD | 40,820,000.00 USD | 204,620.00 USD | 27,680.00 USD | 88,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 15,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0837` | 41,290,000.00 USD | 41,290,000.00 USD | 239,800.00 USD | 199,750.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 17,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0838` | 41,580,000.00 USD | 41,580,000.00 USD | 199,340.00 USD | 64,030.00 USD | 31,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 221.45 USD | 17,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0839` | 41,750,000.00 USD | 41,750,000.00 USD | 94,520.00 USD | 64,060.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 221.54 USD | 17,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0840` | 41,930,000.00 USD | 41,930,000.00 USD | 117,710.00 USD | 0.00 USD | 62,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0841` | 42,020,000.00 USD | 42,020,000.00 USD | 87,460.00 USD | 0.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0842` | 122.86 USD | 17,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0842` | 42,350,000.00 USD | 42,350,000.00 USD | 220,360.00 USD | 33,520.00 USD | 81,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 264.21 USD | 17,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0843` | 42,520,000.00 USD | 42,520,000.00 USD | 117,190.00 USD | 44,120.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 42,820,000.00 USD | 42,820,000.00 USD | 164,260.00 USD | 64,360.00 USD | 77,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0845` | 42,980,000.00 USD | 42,980,000.00 USD | 70,690.00 USD | 30,660.00 USD | 57,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 43,210,000.00 USD | 43,210,000.00 USD | 106,330.00 USD | 76,890.00 USD | 40,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 223.39 USD | 18,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0847` | 43,490,000.00 USD | 43,490,000.00 USD | 137,750.00 USD | 113,280.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 43,770,000.00 USD | 43,770,000.00 USD | 117,070.00 USD | 57,210.00 USD | 99,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 426.71 USD | 18,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0853` | 224.97 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 18,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,250.00 USD | 23,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0868` | 155.98 USD | 23,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 23,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0877` | 231.57 USD | 23,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 24,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 24,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 24,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 25,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0901` | 237.64 USD | 25,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 32,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 33,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 38,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0915` | 1,810.00 USD | 40,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 40,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0925` | 4,160.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 45,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0940` | 915.67 USD | 46,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 86,880.00 USD | 133,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,660.00 USD | 157,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 761.26 USD | 158,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0953` | 1,150.00 USD | 159,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 160,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0970` | 365.68 USD | 160,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 160,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 161,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0993` | 2,900.00 USD | 164,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0994` | 235.90 USD | 164,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 202.21 USD | 164,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 172,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 175,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 175,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1048` | 3,250.00 USD | 179,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 185,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 185,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 189,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1095` | 1,820.00 USD | 190,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 191,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1137` | 147.86 USD | 191,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1152` | 978.31 USD | 192,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 637.53 USD | 192,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1263` | 121.93 USD | 192,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 193,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 193,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1308` | 44,780.00 USD | 238,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 240,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 240,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 240,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1348` | 134.04 USD | 240,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1361` | 6,090.00 USD | 246,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1391` | 1,210.00 USD | 247,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 248,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1426` | 1,800.00 USD | 250,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1431` | 23,200.00 USD | 273,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 275,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1439` | 1,840.00 USD | 277,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 277,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1442` | 13,770.00 USD | 291,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1442` | 31,920.00 USD | 323,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 324,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1446` | 144.55 USD | 324,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1466` | 1,940.00 USD | 326,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,090.00 USD | 334,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1482` | 1,030.00 USD | 335,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0157` | 16,540,000.00 USD | 0.00 USD | 1,500.00 USD | `-79.20%` | `95,954.00` |
| `Live` | `Long` | `0.0160` | 16,540,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.67%` | `244,573.00` |
| `Live` | `Long` | `0.0163` | 16,540,000.00 USD | 0.00 USD | 219.10 USD | `-78.41%` | `13,483.00` |
| `Live` | `Long` | `0.0164` | 16,540,000.00 USD | 0.00 USD | 407.02 USD | `-78.14%` | `24,743.00` |
| `Live` | `Long` | `0.0167` | 16,540,000.00 USD | 0.00 USD | 5,320.00 USD | `-77.88%` | `319,394.00` |
| `Live` | `Long` | `0.0174` | 16,530,000.00 USD | 0.00 USD | 1,030.00 USD | `-76.95%` | `59,317.00` |
| `Live` | `Long` | `0.0177` | 16,530,000.00 USD | 0.00 USD | 1,970.00 USD | `-76.41%` | `111,254.00` |
| `Live` | `Long` | `0.0181` | 16,530,000.00 USD | 0.00 USD | 127.00 USD | `-76.01%` | `7,036.00` |
| `Live` | `Long` | `0.0186` | 16,530,000.00 USD | 0.00 USD | 223.22 USD | `-75.22%` | `11,969.00` |
| `Live` | `Long` | `0.0198` | 16,530,000.00 USD | 0.00 USD | 1,480.00 USD | `-73.76%` | `75,012.00` |
| `Live` | `Long` | `0.0198` | 16,530,000.00 USD | 0.00 USD | 1,190.00 USD | `-73.62%` | `60,000.00` |
| `Live` | `Long` | `0.0205` | 16,530,000.00 USD | 0.00 USD | 657.60 USD | `-72.69%` | `32,000.00` |
| `Live` | `Long` | `0.0215` | 16,530,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.36%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,510,000.00 USD | 0.00 USD | 541.25 USD | `-71.23%` | `25,000.00` |
| `Live` | `Long` | `0.0223` | 16,510,000.00 USD | 0.00 USD | 138.70 USD | `-70.30%` | `6,206.00` |
| `Live` | `Long` | `0.0230` | 16,510,000.00 USD | 0.00 USD | 896.17 USD | `-69.50%` | `39,049.00` |
| `Live` | `Long` | `0.0232` | 16,510,000.00 USD | 0.00 USD | 140.69 USD | `-69.11%` | `6,051.00` |
| `Live` | `Long` | `0.0233` | 16,510,000.00 USD | 0.00 USD | 11,680.00 USD | `-68.97%` | `500,000.00` |
| `Live` | `Long` | `0.0254` | 16,490,000.00 USD | 0.00 USD | 4,020.00 USD | `-66.31%` | `158,606.00` |
| `Live` | `Long` | `0.0257` | 16,490,000.00 USD | 0.00 USD | 763.00 USD | `-65.78%` | `29,631.00` |
| `Live` | `Long` | `0.0259` | 16,490,000.00 USD | 0.00 USD | 23,100.00 USD | `-65.65%` | `893,720.00` |
| `Live` | `Long` | `0.0265` | 16,470,000.00 USD | 0.00 USD | 416.51 USD | `-64.85%` | `15,747.00` |
| `Live` | `Long` | `0.0266` | 16,470,000.00 USD | 0.00 USD | 950.36 USD | `-64.72%` | `35,795.00` |
| `Live` | `Long` | `0.0279` | 16,460,000.00 USD | 0.00 USD | 1,730.00 USD | `-62.86%` | `61,775.00` |
| `Live` | `Long` | `0.0295` | 16,460,000.00 USD | 0.00 USD | 157.38 USD | `-60.87%` | `5,344.00` |
| `Live` | `Long` | `0.0301` | 16,460,000.00 USD | 0.00 USD | 520.48 USD | `-59.94%` | `17,263.00` |
| `Live` | `Long` | `0.0306` | 16,460,000.00 USD | 0.00 USD | 137.41 USD | `-59.40%` | `4,498.00` |
| `Live` | `Long` | `0.0308` | 16,460,000.00 USD | 0.00 USD | 266.67 USD | `-59.01%` | `8,644.00` |
| `Live` | `Long` | `0.0316` | 16,460,000.00 USD | 0.00 USD | 46,970.00 USD | `-58.08%` | `1,488,849.00` |
| `Live` | `Long` | `0.0318` | 16,410,000.00 USD | 0.00 USD | 1,030.00 USD | `-57.81%` | `32,298.00` |
| `Live` | `Long` | `0.0319` | 16,410,000.00 USD | 0.00 USD | 6,010.00 USD | `-57.54%` | `187,979.00` |
| `Live` | `Long` | `0.0328` | 16,410,000.00 USD | 0.00 USD | 459.71 USD | `-56.48%` | `14,037.00` |
| `Live` | `Long` | `0.0330` | 16,410,000.00 USD | 0.00 USD | 133.94 USD | `-56.22%` | `4,065.00` |
| `Live` | `Long` | `0.0331` | 16,410,000.00 USD | 0.00 USD | 762.45 USD | `-55.95%` | `23,000.00` |
| `Live` | `Long` | `0.0336` | 16,410,000.00 USD | 0.00 USD | 393.23 USD | `-55.29%` | `11,686.00` |
| `Live` | `Long` | `0.0347` | 16,410,000.00 USD | 0.00 USD | 4,660.00 USD | `-53.96%` | `134,443.00` |
| `Live` | `Long` | `0.0352` | 16,400,000.00 USD | 0.00 USD | 13,700.00 USD | `-53.29%` | `389,633.00` |
| `Live` | `Long` | `0.0358` | 16,390,000.00 USD | 0.00 USD | 214.53 USD | `-52.36%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,390,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.23%` | `233,408.00` |
| `Live` | `Long` | `0.0370` | 16,380,000.00 USD | 0.00 USD | 35,200.00 USD | `-50.77%` | `950,000.00` |
| `Live` | `Long` | `0.0381` | 16,340,000.00 USD | 0.00 USD | 3,190.00 USD | `-49.44%` | `83,788.00` |
| `Live` | `Long` | `0.0384` | 16,340,000.00 USD | 0.00 USD | 1,830.00 USD | `-48.91%` | `47,501.00` |
| `Live` | `Long` | `0.0386` | 16,340,000.00 USD | 0.00 USD | 121.74 USD | `-48.77%` | `3,158.00` |
| `Live` | `Long` | `0.0386` | 16,340,000.00 USD | 0.00 USD | 181.66 USD | `-48.64%` | `4,700.00` |
| `Live` | `Long` | `0.0387` | 16,340,000.00 USD | 0.00 USD | 207.27 USD | `-48.51%` | `5,349.00` |
| `Live` | `Long` | `0.0393` | 16,340,000.00 USD | 0.00 USD | 221.10 USD | `-47.84%` | `5,633.00` |
| `Live` | `Long` | `0.0396` | 16,340,000.00 USD | 0.00 USD | 3,960.00 USD | `-47.45%` | `100,000.00` |
| `Live` | `Long` | `0.0399` | 16,330,000.00 USD | 0.00 USD | 103.31 USD | `-46.91%` | `2,586.00` |
| `Live` | `Long` | `0.0404` | 16,330,000.00 USD | 0.00 USD | 56,970.00 USD | `-46.25%` | `1,408,334.00` |
| `Live` | `Long` | `0.0406` | 16,280,000.00 USD | 0.00 USD | 2,030.00 USD | `-45.98%` | `50,000.00` |
| `Live` | `Long` | `0.0408` | 16,280,000.00 USD | 0.00 USD | 419.28 USD | `-45.85%` | `10,289.00` |
| `Live` | `Long` | `0.0410` | 16,270,000.00 USD | 0.00 USD | 21,570.00 USD | `-45.59%` | `526,651.00` |
| `Live` | `Long` | `0.0415` | 16,250,000.00 USD | 0.00 USD | 1,330.00 USD | `-44.92%` | `32,043.00` |
| `Live` | `Long` | `0.0415` | 16,250,000.00 USD | 0.00 USD | 1,250.00 USD | `-44.79%` | `29,991.00` |
| `Live` | `Long` | `0.0420` | 16,250,000.00 USD | 0.00 USD | 266.68 USD | `-44.12%` | `6,342.00` |
| `Live` | `Long` | `0.0421` | 16,250,000.00 USD | 0.00 USD | 5,160.00 USD | `-43.99%` | `122,306.00` |
| `Live` | `Long` | `0.0423` | 16,250,000.00 USD | 0.00 USD | 1,670.00 USD | `-43.86%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,240,000.00 USD | 0.00 USD | 267.52 USD | `-43.72%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,240,000.00 USD | 0.00 USD | 5,370.00 USD | `-43.59%` | `126,494.00` |
| `Live` | `Long` | `0.0425` | 16,240,000.00 USD | 0.00 USD | 44,730.00 USD | `-43.46%` | `1,051,327.00` |
| `Live` | `Long` | `0.0427` | 16,190,000.00 USD | 0.00 USD | 2,960.00 USD | `-43.33%` | `69,502.00` |
| `Live` | `Long` | `0.0430` | 16,190,000.00 USD | 0.00 USD | 859.00 USD | `-42.93%` | `20,000.00` |
| `Live` | `Long` | `0.0430` | 16,190,000.00 USD | 0.00 USD | 12,480.00 USD | `-42.79%` | `290,000.00` |
| `Live` | `Long` | `0.0432` | 16,180,000.00 USD | 0.00 USD | 10,460.00 USD | `-42.53%` | `241,828.00` |
| `Live` | `Long` | `0.0433` | 16,170,000.00 USD | 0.00 USD | 7,400.00 USD | `-42.40%` | `170,715.00` |
| `Live` | `Long` | `0.0435` | 16,160,000.00 USD | 0.00 USD | 112,760.00 USD | `-42.13%` | `2,589,112.00` |
| `Live` | `Long` | `0.0439` | 16,050,000.00 USD | 0.00 USD | 2,620.00 USD | `-41.73%` | `59,668.00` |
| `Live` | `Long` | `0.0440` | 16,040,000.00 USD | 0.00 USD | 750.58 USD | `-41.60%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,040,000.00 USD | 0.00 USD | 1,170.00 USD | `-41.47%` | `26,467.00` |
| `Live` | `Long` | `0.0444` | 16,040,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.07%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 15,940,000.00 USD | 0.00 USD | 444.76 USD | `-40.67%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 15,940,000.00 USD | 0.00 USD | 248.63 USD | `-40.54%` | `5,556.00` |
| `Live` | `Long` | `0.0449` | 15,940,000.00 USD | 0.00 USD | 153.57 USD | `-40.40%` | `3,424.00` |
| `Live` | `Long` | `0.0449` | 15,940,000.00 USD | 0.00 USD | 810.81 USD | `-40.27%` | `18,038.00` |
| `Live` | `Long` | `0.0454` | 15,940,000.00 USD | 0.00 USD | 781.11 USD | `-39.74%` | `17,224.00` |
| `Live` | `Long` | `0.0454` | 15,940,000.00 USD | 0.00 USD | 2,610.00 USD | `-39.61%` | `57,510.00` |
| `Live` | `Long` | `0.0456` | 15,940,000.00 USD | 0.00 USD | 32,650.00 USD | `-39.47%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 15,900,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.21%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 15,900,000.00 USD | 0.00 USD | 689.25 USD | `-38.94%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 15,900,000.00 USD | 0.00 USD | 4,500.00 USD | `-38.81%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 15,890,000.00 USD | 0.00 USD | 1,300.00 USD | `-38.68%` | `28,207.00` |
| `Live` | `Long` | `0.0462` | 15,890,000.00 USD | 0.00 USD | 913.53 USD | `-38.54%` | `19,752.00` |
| `Live` | `Long` | `0.0464` | 15,890,000.00 USD | 0.00 USD | 362.87 USD | `-38.41%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 15,890,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.28%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 15,870,000.00 USD | 0.00 USD | 109.49 USD | `-38.01%` | `2,347.00` |
| `Live` | `Long` | `0.0467` | 15,870,000.00 USD | 0.00 USD | 10,500.00 USD | `-37.88%` | `224,650.00` |
| `Live` | `Long` | `0.0471` | 15,860,000.00 USD | 0.00 USD | 1,040.00 USD | `-37.35%` | `22,129.00` |
| `Live` | `Long` | `0.0473` | 15,860,000.00 USD | 0.00 USD | 2,880.00 USD | `-37.21%` | `60,960.00` |
| `Live` | `Long` | `0.0474` | 15,860,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.08%` | `29,884.00` |
| `Live` | `Long` | `0.0474` | 15,860,000.00 USD | 0.00 USD | 256.70 USD | `-36.95%` | `5,410.00` |
| `Live` | `Long` | `0.0476` | 15,860,000.00 USD | 0.00 USD | 98,470.00 USD | `-36.68%` | `2,066,606.00` |
| `Live` | `Long` | `0.0479` | 15,760,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-36.28%` | `21,424,497.00` |
| `Live` | `Long` | `0.0481` | 14,730,000.00 USD | 0.00 USD | 58,890.00 USD | `-36.02%` | `1,223,127.00` |
| `Live` | `Long` | `0.0483` | 14,670,000.00 USD | 0.00 USD | 1,780.00 USD | `-35.75%` | `36,742.00` |
| `Live` | `Long` | `0.0485` | 14,670,000.00 USD | 0.00 USD | 1,480.00 USD | `-35.62%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 14,670,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.09%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,670,000.00 USD | 0.00 USD | 7,930.00 USD | `-34.95%` | `161,921.00` |
| `Live` | `Long` | `0.0491` | 14,660,000.00 USD | 0.00 USD | 1,080.00 USD | `-34.82%` | `21,989.00` |
| `Live` | `Long` | `0.0493` | 14,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.56%` | `26,900.00` |
| `Live` | `Long` | `0.0496` | 14,660,000.00 USD | 0.00 USD | 4,810.00 USD | `-34.02%` | `96,957.00` |
| `Live` | `Long` | `0.0498` | 14,650,000.00 USD | 0.00 USD | 253.82 USD | `-33.89%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,650,000.00 USD | 0.00 USD | 501.50 USD | `-33.49%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,650,000.00 USD | 0.00 USD | 106.23 USD | `-33.23%` | `2,114.00` |
| `Live` | `Long` | `0.0503` | 14,650,000.00 USD | 0.00 USD | 5,310.00 USD | `-33.09%` | `105,458.00` |
| `Live` | `Long` | `0.0505` | 14,650,000.00 USD | 0.00 USD | 334.89 USD | `-32.96%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,650,000.00 USD | 0.00 USD | 1,040.00 USD | `-32.70%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,640,000.00 USD | 0.00 USD | 5,350.00 USD | `-32.56%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,640,000.00 USD | 0.00 USD | 535.43 USD | `-32.30%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,640,000.00 USD | 0.00 USD | 566.65 USD | `-32.16%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,640,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.03%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,630,000.00 USD | 0.00 USD | 1,490.00 USD | `-31.90%` | `29,005.00` |
| `Live` | `Long` | `0.0515` | 14,630,000.00 USD | 0.00 USD | 309.15 USD | `-31.50%` | `5,997.00` |
| `Live` | `Long` | `0.0517` | 14,630,000.00 USD | 0.00 USD | 3,520.00 USD | `-31.37%` | `68,212.00` |
| `Live` | `Long` | `0.0519` | 14,620,000.00 USD | 0.00 USD | 6,970.00 USD | `-31.10%` | `134,439.00` |
| `Live` | `Long` | `0.0520` | 14,610,000.00 USD | 0.00 USD | 594.46 USD | `-30.97%` | `11,443.00` |
| `Live` | `Long` | `0.0520` | 14,610,000.00 USD | 0.00 USD | 4,420.00 USD | `-30.84%` | `84,852.00` |
| `Live` | `Long` | `0.0522` | 14,610,000.00 USD | 0.00 USD | 279,790.00 USD | `-30.57%` | `5,354,820.00` |
| `Live` | `Long` | `0.0524` | 14,330,000.00 USD | 0.00 USD | 1,440.00 USD | `-30.30%` | `27,383.00` |
| `Live` | `Long` | `0.0525` | 14,330,000.00 USD | 0.00 USD | 4,790.00 USD | `-30.17%` | `91,115.00` |
| `Live` | `Long` | `0.0527` | 14,320,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.04%` | `45,551.00` |
| `Live` | `Long` | `0.0527` | 14,320,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.90%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,320,000.00 USD | 0.00 USD | 673.52 USD | `-29.77%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,320,000.00 USD | 0.00 USD | 181,920.00 USD | `-29.64%` | `3,435,663.00` |
| `Live` | `Long` | `0.0530` | 14,140,000.00 USD | 0.00 USD | 1,300.00 USD | `-29.51%` | `24,520.00` |
| `Live` | `Long` | `0.0532` | 14,140,000.00 USD | 0.00 USD | 9,900.00 USD | `-29.37%` | `186,196.00` |
| `Live` | `Long` | `0.0532` | 14,130,000.00 USD | 0.00 USD | 50,030.00 USD | `-29.24%` | `939,476.00` |
| `Live` | `Long` | `0.0534` | 14,080,000.00 USD | 0.00 USD | 42,580.00 USD | `-29.11%` | `798,082.00` |
| `Live` | `Long` | `0.0534` | 14,030,000.00 USD | 0.00 USD | 800.95 USD | `-28.97%` | `14,985.00` |
| `Live` | `Long` | `0.0536` | 14,030,000.00 USD | 0.00 USD | 1,040.00 USD | `-28.84%` | `19,489.00` |
| `Live` | `Long` | `0.0537` | 14,030,000.00 USD | 0.00 USD | 4,820.00 USD | `-28.71%` | `89,931.00` |
| `Live` | `Long` | `0.0539` | 14,030,000.00 USD | 0.00 USD | 5,290.00 USD | `-28.31%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 14,020,000.00 USD | 0.00 USD | 2,550.00 USD | `-28.18%` | `47,142.00` |
| `Live` | `Long` | `0.0541` | 14,020,000.00 USD | 0.00 USD | 4,080.00 USD | `-28.04%` | `75,394.00` |
| `Live` | `Long` | `0.0542` | 14,010,000.00 USD | 0.00 USD | 95,630.00 USD | `-27.91%` | `1,762,722.00` |
| `Live` | `Long` | `0.0544` | 13,920,000.00 USD | 0.00 USD | 903.30 USD | `-27.78%` | `16,620.00` |
| `Live` | `Long` | `0.0544` | 13,920,000.00 USD | 0.00 USD | 28,420.00 USD | `-27.65%` | `521,978.00` |
| `Live` | `Long` | `0.0546` | 13,890,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.38%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,890,000.00 USD | 0.00 USD | 188.07 USD | `-27.25%` | `3,435.00` |
| `Live` | `Long` | `0.0551` | 13,890,000.00 USD | 0.00 USD | 1,760.00 USD | `-26.72%` | `31,888.00` |
| `Live` | `Long` | `0.0554` | 13,880,000.00 USD | 0.00 USD | 347.32 USD | `-26.45%` | `6,275.00` |
| `Live` | `Long` | `0.0556` | 13,880,000.00 USD | 0.00 USD | 25,270.00 USD | `-26.18%` | `454,864.00` |
| `Live` | `Long` | `0.0561` | 13,860,000.00 USD | 0.00 USD | 10,830.00 USD | `-25.52%` | `193,146.00` |
| `Live` | `Long` | `0.0561` | 13,850,000.00 USD | 0.00 USD | 144.08 USD | `-25.39%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,850,000.00 USD | 0.00 USD | 40,620.00 USD | `-25.25%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,810,000.00 USD | 0.00 USD | 4,440.00 USD | `-25.12%` | `78,743.00` |
| `Live` | `Long` | `0.0568` | 13,800,000.00 USD | 0.00 USD | 568.50 USD | `-24.46%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,800,000.00 USD | 0.00 USD | 1,070.00 USD | `-24.32%` | `18,778.00` |
| `Live` | `Long` | `0.0570` | 13,800,000.00 USD | 0.00 USD | 8,350.00 USD | `-24.19%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,790,000.00 USD | 0.00 USD | 814.04 USD | `-24.06%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,790,000.00 USD | 0.00 USD | 4,060.00 USD | `-23.79%` | `70,727.00` |
| `Live` | `Long` | `0.0575` | 13,790,000.00 USD | 0.00 USD | 3,960.00 USD | `-23.53%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 13,780,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.39%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,770,000.00 USD | 0.00 USD | 14,210.00 USD | `-23.26%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,760,000.00 USD | 0.00 USD | 50,510.00 USD | `-23.13%` | `873,039.00` |
| `Live` | `Long` | `0.0580` | 13,710,000.00 USD | 0.00 USD | 622.09 USD | `-23.00%` | `10,735.00` |
| `Live` | `Long` | `0.0580` | 13,710,000.00 USD | 0.00 USD | 431.14 USD | `-22.86%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,710,000.00 USD | 0.00 USD | 447.17 USD | `-22.73%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,710,000.00 USD | 0.00 USD | 582.50 USD | `-22.60%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,710,000.00 USD | 0.00 USD | 16,730.00 USD | `-22.46%` | `286,750.00` |
| `Live` | `Long` | `0.0585` | 13,690,000.00 USD | 0.00 USD | 172.78 USD | `-22.20%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,690,000.00 USD | 0.00 USD | 3,930.00 USD | `-22.06%` | `66,937.00` |
| `Live` | `Long` | `0.0587` | 13,690,000.00 USD | 0.00 USD | 305.15 USD | `-21.93%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,680,000.00 USD | 0.00 USD | 703.21 USD | `-21.67%` | `11,929.00` |
| `Live` | `Long` | `0.0592` | 13,680,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.40%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,660,000.00 USD | 0.00 USD | 546.26 USD | `-21.13%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,660,000.00 USD | 0.00 USD | 4,140.00 USD | `-21.00%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,650,000.00 USD | 0.00 USD | 3,300.00 USD | `-20.87%` | `55,392.00` |
| `Live` | `Long` | `0.0597` | 13,650,000.00 USD | 0.00 USD | 4,320.00 USD | `-20.74%` | `72,358.00` |
| `Live` | `Long` | `0.0597` | 13,640,000.00 USD | 0.00 USD | 644.22 USD | `-20.60%` | `10,782.00` |
| `Live` | `Long` | `0.0599` | 13,640,000.00 USD | 0.00 USD | 2,110.00 USD | `-20.47%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 13,640,000.00 USD | 0.00 USD | 3,580.00 USD | `-20.34%` | `59,709.00` |
| `Live` | `Long` | `0.0600` | 13,640,000.00 USD | 0.00 USD | 360,820.00 USD | `-20.20%` | `6,008,741.00` |
| `Live` | `Long` | `0.0602` | 13,280,000.00 USD | 0.00 USD | 10,360.00 USD | `-20.07%` | `172,235.00` |
| `Live` | `Long` | `0.0604` | 13,270,000.00 USD | 0.00 USD | 2,880.00 USD | `-19.81%` | `47,777.00` |
| `Live` | `Long` | `0.0604` | 13,260,000.00 USD | 0.00 USD | 848.05 USD | `-19.67%` | `14,029.00` |
| `Live` | `Long` | `0.0605` | 13,260,000.00 USD | 0.00 USD | 6,010,000.00 USD | `-19.54%` | `99,253,241.00` |
| `Live` | `Long` | `0.0607` | 7,250,000.00 USD | 0.00 USD | 622.63 USD | `-19.41%` | `10,266.00` |
| `Live` | `Long` | `0.0609` | 7,250,000.00 USD | 0.00 USD | 1,940.00 USD | `-19.14%` | `31,875.00` |
| `Live` | `Long` | `0.0609` | 7,250,000.00 USD | 0.00 USD | 5,110.00 USD | `-19.01%` | `83,914.00` |
| `Live` | `Long` | `0.0612` | 7,250,000.00 USD | 0.00 USD | 629.72 USD | `-18.74%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,250,000.00 USD | 0.00 USD | 298.17 USD | `-18.61%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,250,000.00 USD | 0.00 USD | 655.16 USD | `-18.48%` | `10,679.00` |
| `Live` | `Long` | `0.0614` | 7,240,000.00 USD | 0.00 USD | 412.21 USD | `-18.34%` | `6,708.00` |
| `Live` | `Long` | `0.0616` | 7,240,000.00 USD | 0.00 USD | 1,890.00 USD | `-18.21%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,240,000.00 USD | 0.00 USD | 11,100.00 USD | `-18.08%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 7,230,000.00 USD | 0.00 USD | 158.08 USD | `-17.95%` | `2,560.00` |
| `Live` | `Long` | `0.0619` | 7,230,000.00 USD | 0.00 USD | 782.68 USD | `-17.68%` | `12,634.00` |
| `Live` | `Long` | `0.0621` | 7,230,000.00 USD | 0.00 USD | 26,790.00 USD | `-17.55%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,200,000.00 USD | 0.00 USD | 17,850.00 USD | `-17.41%` | `287,135.00` |
| `Live` | `Long` | `0.0624` | 7,190,000.00 USD | 0.00 USD | 1,900.00 USD | `-17.15%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,180,000.00 USD | 0.00 USD | 43,420.00 USD | `-17.02%` | `695,308.00` |
| `Live` | `Long` | `0.0625` | 7,140,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-16.88%` | `17,639,337.00` |
| `Live` | `Long` | `0.0626` | 6,040,000.00 USD | 0.00 USD | 1,120.00 USD | `-16.75%` | `17,888.00` |
| `Live` | `Long` | `0.0628` | 6,040,000.00 USD | 0.00 USD | 461.78 USD | `-16.62%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,040,000.00 USD | 0.00 USD | 6,400.00 USD | `-16.48%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,030,000.00 USD | 0.00 USD | 2,430.00 USD | `-16.22%` | `38,603.00` |
| `Live` | `Long` | `0.0631` | 6,030,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-16.09%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 4,960,000.00 USD | 0.00 USD | 3,030.00 USD | `-15.95%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-15.82%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-15.69%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,940,000.00 USD | 0.00 USD | 479.68 USD | `-15.55%` | `7,548.00` |
| `Live` | `Long` | `0.0636` | 4,940,000.00 USD | 0.00 USD | 633.38 USD | `-15.42%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 4,940,000.00 USD | 0.00 USD | 9,740.00 USD | `-15.29%` | `152,837.00` |
| `Live` | `Long` | `0.0639` | 4,930,000.00 USD | 0.00 USD | 23,220.00 USD | `-15.16%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.02%` | `31,194.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 3,420.00 USD | `-14.76%` | `53,255.00` |
| `Live` | `Long` | `0.0643` | 4,910,000.00 USD | 0.00 USD | 733.80 USD | `-14.62%` | `11,421.00` |
| `Live` | `Long` | `0.0644` | 4,900,000.00 USD | 0.00 USD | 76,880.00 USD | `-14.49%` | `1,194,761.00` |
| `Live` | `Long` | `0.0644` | 4,830,000.00 USD | 0.00 USD | 27,180.00 USD | `-14.36%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,800,000.00 USD | 0.00 USD | 631.94 USD | `-14.22%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,800,000.00 USD | 0.00 USD | 162,920.00 USD | `-13.96%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,640,000.00 USD | 0.00 USD | 8,800.00 USD | `-13.83%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,630,000.00 USD | 0.00 USD | 367.23 USD | `-13.69%` | `5,654.00` |
| `Live` | `Long` | `0.0650` | 4,630,000.00 USD | 0.00 USD | 21,580.00 USD | `-13.56%` | `331,693.00` |
| `Live` | `Long` | `0.0651` | 4,610,000.00 USD | 0.00 USD | 2,380.00 USD | `-13.43%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,600,000.00 USD | 0.00 USD | 13,770.00 USD | `-13.29%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,590,000.00 USD | 0.00 USD | 7,790.00 USD | `-12.90%` | `118,852.00` |
| `Live` | `Long` | `0.0657` | 4,580,000.00 USD | 0.00 USD | 14,160.00 USD | `-12.76%` | `215,665.00` |
| `Live` | `Long` | `0.0658` | 4,570,000.00 USD | 0.00 USD | 66,820.00 USD | `-12.63%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,500,000.00 USD | 0.00 USD | 14,600.00 USD | `-12.50%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 9,600.00 USD | `-12.36%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-12.10%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,470,000.00 USD | 0.00 USD | 13,740.00 USD | `-11.97%` | `207,423.00` |
| `Live` | `Long` | `0.0664` | 4,460,000.00 USD | 0.00 USD | 17,410.00 USD | `-11.83%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,440,000.00 USD | 0.00 USD | 1,270.00 USD | `-11.70%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,440,000.00 USD | 0.00 USD | 34,860.00 USD | `-11.43%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 8,880.00 USD | `-11.30%` | `133,009.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-11.17%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,250,000.00 USD | 0.00 USD | 1,180.00 USD | `-11.04%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,250,000.00 USD | 0.00 USD | 6,120.00 USD | `-10.90%` | `91,206.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,220.00 USD | `-10.64%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 4,830.00 USD | `-10.50%` | `71,711.00` |
| `Live` | `Long` | `0.0674` | 3,230,000.00 USD | 0.00 USD | 1,780.00 USD | `-10.37%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,230,000.00 USD | 0.00 USD | 112,780.00 USD | `-10.24%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,120,000.00 USD | 0.00 USD | 12,610.00 USD | `-10.11%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 4,290.00 USD | `-9.97%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 34,090.00 USD | `-9.84%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,070,000.00 USD | 0.00 USD | 16,630.00 USD | `-9.71%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,050,000.00 USD | 0.00 USD | 390.81 USD | `-9.57%` | `5,743.00` |
| `Live` | `Long` | `0.0683` | 3,050,000.00 USD | 0.00 USD | 55,770.00 USD | `-9.31%` | `817,124.00` |
| `Live` | `Long` | `0.0683` | 2,990,000.00 USD | 0.00 USD | 3,040.00 USD | `-9.18%` | `44,473.00` |
| `Live` | `Long` | `0.0684` | 2,990,000.00 USD | 0.00 USD | 79,490.00 USD | `-9.04%` | `1,161,220.00` |
| `Live` | `Long` | `0.0685` | 2,910,000.00 USD | 0.00 USD | 8,890.00 USD | `-8.91%` | `129,646.00` |
| `Live` | `Long` | `0.0687` | 2,900,000.00 USD | 0.00 USD | 5,120.00 USD | `-8.78%` | `74,513.00` |
| `Live` | `Long` | `0.0688` | 2,900,000.00 USD | 0.00 USD | 50,630.00 USD | `-8.64%` | `736,452.00` |
| `Live` | `Long` | `0.0688` | 2,850,000.00 USD | 0.00 USD | 345.83 USD | `-8.51%` | `5,023.00` |
| `Live` | `Long` | `0.0689` | 2,850,000.00 USD | 0.00 USD | 508,320.00 USD | `-8.38%` | `7,372,312.00` |
| `Live` | `Long` | `0.0691` | 2,340,000.00 USD | 0.00 USD | 6,960.00 USD | `-8.25%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,330,000.00 USD | 0.00 USD | 13,510.00 USD | `-8.11%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,320,000.00 USD | 0.00 USD | 9,140.00 USD | `-7.98%` | `131,951.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.85%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,310,000.00 USD | 0.00 USD | 4,980.00 USD | `-7.71%` | `71,770.00` |
| `Live` | `Long` | `0.0697` | 2,300,000.00 USD | 0.00 USD | 4,950.00 USD | `-7.45%` | `71,115.00` |
| `Live` | `Long` | `0.0698` | 2,300,000.00 USD | 0.00 USD | 6,970.00 USD | `-7.32%` | `99,923.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 2,910.00 USD | `-7.18%` | `41,684.00` |
| `Live` | `Long` | `0.0699` | 2,290,000.00 USD | 0.00 USD | 1,310.00 USD | `-7.05%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,280,000.00 USD | 0.00 USD | 9,620.00 USD | `-6.92%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,270,000.00 USD | 0.00 USD | 8,180.00 USD | `-6.78%` | `116,620.00` |
| `Live` | `Long` | `0.0703` | 2,270,000.00 USD | 0.00 USD | 1,070.00 USD | `-6.65%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,270,000.00 USD | 0.00 USD | 3,790.00 USD | `-6.52%` | `53,920.00` |
| `Live` | `Long` | `0.0704` | 2,260,000.00 USD | 0.00 USD | 780.37 USD | `-6.38%` | `11,077.00` |
| `Live` | `Long` | `0.0707` | 2,260,000.00 USD | 0.00 USD | 608.86 USD | `-6.12%` | `8,618.00` |
| `Live` | `Long` | `0.0707` | 2,260,000.00 USD | 0.00 USD | 94,410.00 USD | `-5.99%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,170,000.00 USD | 0.00 USD | 351.63 USD | `-5.72%` | `4,956.00` |
| `Live` | `Long` | `0.0711` | 2,170,000.00 USD | 0.00 USD | 4,720.00 USD | `-5.59%` | `66,436.00` |
| `Live` | `Long` | `0.0712` | 2,160,000.00 USD | 0.00 USD | 2,190.00 USD | `-5.45%` | `30,741.00` |
| `Live` | `Long` | `0.0712` | 2,160,000.00 USD | 0.00 USD | 1,740.00 USD | `-5.32%` | `24,442.00` |
| `Live` | `Long` | `0.0713` | 2,160,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-5.19%` | `24,494,524.00` |
| `Live` | `Long` | `0.0714` | 408,970.00 USD | 0.00 USD | 13,270.00 USD | `-5.06%` | `185,735.00` |
| `Live` | `Long` | `0.0716` | 395,700.00 USD | 0.00 USD | 8,120.00 USD | `-4.92%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 387,590.00 USD | 0.00 USD | 4,970.00 USD | `-4.79%` | `69,434.00` |
| `Live` | `Long` | `0.0717` | 382,610.00 USD | 0.00 USD | 48,180.00 USD | `-4.66%` | `671,440.00` |
| `Live` | `Long` | `0.0718` | 334,440.00 USD | 0.00 USD | 960.13 USD | `-4.52%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 333,480.00 USD | 0.00 USD | 1,900.00 USD | `-4.39%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 331,580.00 USD | 0.00 USD | 5,090.00 USD | `-4.26%` | `70,701.00` |
| `Live` | `Long` | `0.0722` | 326,490.00 USD | 0.00 USD | 613.35 USD | `-4.13%` | `8,501.00` |
| `Live` | `Long` | `0.0722` | 325,870.00 USD | 0.00 USD | 38,130.00 USD | `-3.99%` | `527,683.00` |
| `Live` | `Long` | `0.0723` | 287,750.00 USD | 0.00 USD | 286,760.00 USD | `-3.86%` | `3,963,544.00` |
| `Live` | `Long` | `0.0725` | 984.89 USD | 0.00 USD | 984.89 USD | `-3.73%` | `13,594.00` |
| `Live` | `Short` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | `+3.05%` | `3,107.00` |
| `Live` | `Short` | `0.0788` | 354.19 USD | 113.24 USD | 0.00 USD | `+4.64%` | `1,438.00` |
| `Live` | `Short` | `0.0791` | 2,000.00 USD | 1,650.00 USD | 0.00 USD | `+5.18%` | `20,832.00` |
| `Live` | `Short` | `0.0794` | 5,550.00 USD | 3,550.00 USD | 0.00 USD | `+5.44%` | `44,701.00` |
| `Live` | `Short` | `0.0795` | 5,650.00 USD | 104.72 USD | 0.00 USD | `+5.57%` | `1,318.00` |
| `Live` | `Short` | `0.0795` | 9,260.00 USD | 3,610.00 USD | 0.00 USD | `+5.71%` | `45,349.00` |
| `Live` | `Short` | `0.0804` | 9,480.00 USD | 213.09 USD | 0.00 USD | `+6.77%` | `2,652.00` |
| `Live` | `Short` | `0.0804` | 10,300.00 USD | 826.14 USD | 0.00 USD | `+6.90%` | `10,269.00` |
| `Live` | `Short` | `0.0806` | 10,510.00 USD | 213.40 USD | 0.00 USD | `+7.17%` | `2,646.00` |
| `Live` | `Short` | `0.0811` | 10,730.00 USD | 215.29 USD | 0.00 USD | `+7.83%` | `2,653.00` |
| `Live` | `Short` | `0.0819` | 11,110.00 USD | 380.85 USD | 0.00 USD | `+8.76%` | `4,653.00` |
| `Live` | `Short` | `0.0825` | 11,330.00 USD | 217.85 USD | 0.00 USD | `+9.69%` | `2,639.00` |
| `Live` | `Short` | `0.0828` | 11,550.00 USD | 218.81 USD | 0.00 USD | `+10.09%` | `2,641.00` |
| `Live` | `Short` | `0.0832` | 15,220.00 USD | 3,670.00 USD | 0.00 USD | `+10.49%` | `44,187.00` |
| `Live` | `Short` | `0.0837` | 15,520.00 USD | 293.44 USD | 0.00 USD | `+11.16%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 17,090.00 USD | 1,570.00 USD | 0.00 USD | `+11.29%` | `18,767.00` |
| `Live` | `Short` | `0.0838` | 17,310.00 USD | 221.45 USD | 0.00 USD | `+11.42%` | `2,641.00` |
| `Live` | `Short` | `0.0839` | 17,530.00 USD | 221.54 USD | 0.00 USD | `+11.55%` | `2,639.00` |
| `Live` | `Short` | `0.0842` | 17,650.00 USD | 122.86 USD | 0.00 USD | `+11.82%` | `1,460.00` |
| `Live` | `Short` | `0.0843` | 17,920.00 USD | 264.21 USD | 0.00 USD | `+11.95%` | `3,136.00` |
| `Live` | `Short` | `0.0847` | 18,140.00 USD | 223.39 USD | 0.00 USD | `+12.48%` | `2,639.00` |
| `Live` | `Short` | `0.0848` | 18,570.00 USD | 426.71 USD | 0.00 USD | `+12.75%` | `5,029.00` |
| `Live` | `Short` | `0.0853` | 18,790.00 USD | 224.97 USD | 0.00 USD | `+13.28%` | `2,639.00` |
| `Live` | `Short` | `0.0858` | 18,910.00 USD | 115.30 USD | 0.00 USD | `+14.08%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 23,150.00 USD | 4,250.00 USD | 0.00 USD | `+14.21%` | `49,397.00` |
| `Live` | `Short` | `0.0868` | 23,310.00 USD | 155.98 USD | 0.00 USD | `+15.41%` | `1,796.00` |
| `Live` | `Short` | `0.0871` | 23,450.00 USD | 138.58 USD | 0.00 USD | `+15.67%` | `1,592.00` |
| `Live` | `Short` | `0.0877` | 23,680.00 USD | 231.57 USD | 0.00 USD | `+16.60%` | `2,639.00` |
| `Live` | `Short` | `0.0881` | 24,140.00 USD | 465.17 USD | 0.00 USD | `+17.00%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 24,560.00 USD | 411.53 USD | 0.00 USD | `+17.93%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 24,970.00 USD | 418.80 USD | 0.00 USD | `+18.33%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 25,260.00 USD | 285.70 USD | 0.00 USD | `+18.86%` | `3,194.00` |
| `Live` | `Short` | `0.0901` | 25,500.00 USD | 237.64 USD | 0.00 USD | `+19.66%` | `2,639.00` |
| `Live` | `Short` | `0.0905` | 32,260.00 USD | 6,760.00 USD | 0.00 USD | `+20.19%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 33,570.00 USD | 1,310.00 USD | 0.00 USD | `+20.46%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 38,510.00 USD | 4,940.00 USD | 0.00 USD | `+21.12%` | `54,197.00` |
| `Live` | `Short` | `0.0915` | 40,320.00 USD | 1,810.00 USD | 0.00 USD | `+21.52%` | `19,839.00` |
| `Live` | `Short` | `0.0921` | 40,500.00 USD | 171.49 USD | 0.00 USD | `+22.32%` | `1,863.00` |
| `Live` | `Short` | `0.0925` | 44,660.00 USD | 4,160.00 USD | 0.00 USD | `+22.98%` | `45,000.00` |
| `Live` | `Short` | `0.0931` | 45,470.00 USD | 805.37 USD | 0.00 USD | `+23.78%` | `8,646.00` |
| `Live` | `Short` | `0.0940` | 46,380.00 USD | 915.67 USD | 0.00 USD | `+24.98%` | `9,736.00` |
| `Live` | `Short` | `0.0944` | 133,260.00 USD | 86,880.00 USD | 0.00 USD | `+25.37%` | `920,808.00` |
| `Live` | `Short` | `0.0950` | 157,920.00 USD | 24,660.00 USD | 0.00 USD | `+26.17%` | `259,694.00` |
| `Live` | `Short` | `0.0950` | 158,680.00 USD | 761.26 USD | 0.00 USD | `+26.30%` | `8,009.00` |
| `Live` | `Short` | `0.0953` | 159,830.00 USD | 1,150.00 USD | 0.00 USD | `+26.57%` | `12,089.00` |
| `Live` | `Short` | `0.0961` | 160,440.00 USD | 609.59 USD | 0.00 USD | `+27.77%` | `6,340.00` |
| `Live` | `Short` | `0.0970` | 160,810.00 USD | 365.68 USD | 0.00 USD | `+28.96%` | `3,768.00` |
| `Live` | `Short` | `0.0974` | 160,930.00 USD | 121.23 USD | 0.00 USD | `+29.49%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 161,400.00 USD | 477.50 USD | 0.00 USD | `+30.56%` | `4,860.00` |
| `Live` | `Short` | `0.0993` | 164,300.00 USD | 2,900.00 USD | 0.00 USD | `+31.88%` | `29,217.00` |
| `Live` | `Short` | `0.0994` | 164,540.00 USD | 235.90 USD | 0.00 USD | `+32.15%` | `2,372.00` |
| `Live` | `Short` | `0.1003` | 164,740.00 USD | 202.21 USD | 0.00 USD | `+33.35%` | `2,015.00` |
| `Live` | `Short` | `0.1014` | 172,370.00 USD | 7,630.00 USD | 0.00 USD | `+34.81%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 175,340.00 USD | 2,970.00 USD | 0.00 USD | `+35.07%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 175,830.00 USD | 492.85 USD | 0.00 USD | `+35.34%` | `4,839.00` |
| `Live` | `Short` | `0.1048` | 179,080.00 USD | 3,250.00 USD | 0.00 USD | `+39.33%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 185,190.00 USD | 6,110.00 USD | 0.00 USD | `+41.05%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 185,810.00 USD | 616.19 USD | 0.00 USD | `+43.05%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 189,050.00 USD | 3,240.00 USD | 0.00 USD | `+44.24%` | `29,849.00` |
| `Live` | `Short` | `0.1095` | 190,870.00 USD | 1,820.00 USD | 0.00 USD | `+45.44%` | `16,647.00` |
| `Live` | `Short` | `0.1127` | 191,080.00 USD | 214.15 USD | 0.00 USD | `+49.69%` | `1,901.00` |
| `Live` | `Short` | `0.1137` | 191,230.00 USD | 147.86 USD | 0.00 USD | `+51.02%` | `1,301.00` |
| `Live` | `Short` | `0.1152` | 192,210.00 USD | 978.31 USD | 0.00 USD | `+53.01%` | `8,496.00` |
| `Live` | `Short` | `0.1222` | 192,850.00 USD | 637.53 USD | 0.00 USD | `+62.45%` | `5,215.00` |
| `Live` | `Short` | `0.1263` | 192,970.00 USD | 121.93 USD | 0.00 USD | `+67.90%` | `965.00` |
| `Live` | `Short` | `0.1270` | 193,080.00 USD | 108.80 USD | 0.00 USD | `+68.69%` | `857.00` |
| `Live` | `Short` | `0.1296` | 193,250.00 USD | 171.66 USD | 0.00 USD | `+72.28%` | `1,324.00` |
| `Live` | `Short` | `0.1308` | 238,030.00 USD | 44,780.00 USD | 0.00 USD | `+73.88%` | `342,231.00` |
| `Live` | `Short` | `0.1311` | 240,170.00 USD | 2,140.00 USD | 0.00 USD | `+74.27%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 240,270.00 USD | 102.97 USD | 0.00 USD | `+75.20%` | `781.00` |
| `Live` | `Short` | `0.1338` | 240,480.00 USD | 205.31 USD | 0.00 USD | `+77.73%` | `1,535.00` |
| `Live` | `Short` | `0.1348` | 240,610.00 USD | 134.04 USD | 0.00 USD | `+79.19%` | `994.00` |
| `Live` | `Short` | `0.1361` | 246,700.00 USD | 6,090.00 USD | 0.00 USD | `+80.79%` | `44,734.00` |
| `Live` | `Short` | `0.1391` | 247,910.00 USD | 1,210.00 USD | 0.00 USD | `+84.90%` | `8,712.00` |
| `Live` | `Short` | `0.1404` | 248,570.00 USD | 663.63 USD | 0.00 USD | `+86.63%` | `4,725.00` |
| `Live` | `Short` | `0.1426` | 250,380.00 USD | 1,800.00 USD | 0.00 USD | `+89.42%` | `12,652.00` |
| `Live` | `Short` | `0.1431` | 273,580.00 USD | 23,200.00 USD | 0.00 USD | `+90.09%` | `162,180.00` |
| `Live` | `Short` | `0.1432` | 275,440.00 USD | 1,860.00 USD | 0.00 USD | `+90.35%` | `13,010.00` |
| `Live` | `Short` | `0.1439` | 277,280.00 USD | 1,840.00 USD | 0.00 USD | `+91.28%` | `12,755.00` |
| `Live` | `Short` | `0.1441` | 277,470.00 USD | 196.63 USD | 0.00 USD | `+91.42%` | `1,365.00` |
| `Live` | `Short` | `0.1442` | 291,250.00 USD | 13,770.00 USD | 0.00 USD | `+91.55%` | `95,545.00` |
| `Live` | `Short` | `0.1442` | 323,170.00 USD | 31,920.00 USD | 0.00 USD | `+91.68%` | `221,300.00` |
| `Live` | `Short` | `0.1444` | 324,710.00 USD | 1,540.00 USD | 0.00 USD | `+91.81%` | `10,691.00` |
| `Live` | `Short` | `0.1446` | 324,860.00 USD | 144.55 USD | 0.00 USD | `+92.08%` | `1,000.00` |
| `Live` | `Short` | `0.1466` | 326,800.00 USD | 1,940.00 USD | 0.00 USD | `+94.74%` | `13,240.00` |
| `Live` | `Short` | `0.1479` | 334,890.00 USD | 8,090.00 USD | 0.00 USD | `+96.47%` | `54,718.00` |
| `Live` | `Short` | `0.1482` | 335,920.00 USD | 1,030.00 USD | 0.00 USD | `+96.86%` | `6,978.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 738,100.00 USD | 0.00 USD | 375.42 USD | `-65.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 737,730.00 USD | 0.00 USD | 409.59 USD | `-46.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 737,320.00 USD | 0.00 USD | 132.68 USD | `-45.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 737,190.00 USD | 0.00 USD | 788.27 USD | `-44.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 736,400.00 USD | 0.00 USD | 527.05 USD | `-44.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 735,870.00 USD | 0.00 USD | 286.87 USD | `-40.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 735,580.00 USD | 0.00 USD | 252.42 USD | `-38.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 735,330.00 USD | 0.00 USD | 468.67 USD | `-37.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 734,860.00 USD | 0.00 USD | 5,160.00 USD | `-34.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 729,700.00 USD | 0.00 USD | 920.48 USD | `-34.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 728,780.00 USD | 0.00 USD | 236.01 USD | `-33.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 728,550.00 USD | 0.00 USD | 175.41 USD | `-31.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 728,370.00 USD | 0.00 USD | 242.96 USD | `-31.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 728,130.00 USD | 0.00 USD | 2,670.00 USD | `-28.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 725,460.00 USD | 0.00 USD | 1,370.00 USD | `-26.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 724,080.00 USD | 0.00 USD | 437.58 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 723,650.00 USD | 0.00 USD | 183.30 USD | `-22.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 723,460.00 USD | 0.00 USD | 752.54 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 722,710.00 USD | 0.00 USD | 984.67 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 721,720.00 USD | 0.00 USD | 668.84 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 721,060.00 USD | 0.00 USD | 273.90 USD | `-19.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 720,780.00 USD | 0.00 USD | 8,800.00 USD | `-19.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 711,980.00 USD | 0.00 USD | 838.79 USD | `-19.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 711,150.00 USD | 0.00 USD | 218.94 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 710,930.00 USD | 0.00 USD | 504.26 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 710,420.00 USD | 0.00 USD | 2,280.00 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 708,140.00 USD | 0.00 USD | 118.27 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 708,020.00 USD | 0.00 USD | 1,280.00 USD | `-17.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 706,750.00 USD | 0.00 USD | 1,820.00 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 704,920.00 USD | 0.00 USD | 1,340.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 703,590.00 USD | 0.00 USD | 386.70 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 703,200.00 USD | 0.00 USD | 644.50 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 702,560.00 USD | 0.00 USD | 11,270.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 691,290.00 USD | 0.00 USD | 362.24 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 690,920.00 USD | 0.00 USD | 3,140.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 687,780.00 USD | 0.00 USD | 1,100.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 686,690.00 USD | 0.00 USD | 1,200.00 USD | `-12.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 685,490.00 USD | 0.00 USD | 996.31 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 684,490.00 USD | 0.00 USD | 909.85 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 683,580.00 USD | 0.00 USD | 115.57 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 683,470.00 USD | 0.00 USD | 33,620.00 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 649,840.00 USD | 0.00 USD | 12,860.00 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 636,980.00 USD | 0.00 USD | 1,540.00 USD | `-10.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 635,440.00 USD | 0.00 USD | 108.08 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 635,330.00 USD | 0.00 USD | 19,540.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 615,790.00 USD | 0.00 USD | 1,430.00 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 614,360.00 USD | 0.00 USD | 8,540.00 USD | `-9.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 605,820.00 USD | 0.00 USD | 8,580.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 597,250.00 USD | 0.00 USD | 4,970.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 592,280.00 USD | 0.00 USD | 3,100.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 589,180.00 USD | 0.00 USD | 160.31 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 589,020.00 USD | 0.00 USD | 38,710.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 550,310.00 USD | 0.00 USD | 21,140.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 529,180.00 USD | 0.00 USD | 3,190.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 525,990.00 USD | 0.00 USD | 478.66 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 525,510.00 USD | 0.00 USD | 176.08 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 525,330.00 USD | 0.00 USD | 142.09 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 525,190.00 USD | 0.00 USD | 925.29 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 524,270.00 USD | 0.00 USD | 797.80 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 523,470.00 USD | 0.00 USD | 71,220.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 452,240.00 USD | 0.00 USD | 141.77 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 452,100.00 USD | 0.00 USD | 895.27 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 451,210.00 USD | 0.00 USD | 523.23 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 450,680.00 USD | 0.00 USD | 468.88 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 450,220.00 USD | 0.00 USD | 235.12 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 449,980.00 USD | 0.00 USD | 1,090.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 448,890.00 USD | 0.00 USD | 71,660.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0711` | 377,230.00 USD | 0.00 USD | 729.61 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 376,500.00 USD | 0.00 USD | 355.75 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 376,150.00 USD | 0.00 USD | 20,180.00 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 355,970.00 USD | 0.00 USD | 608.76 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 355,360.00 USD | 0.00 USD | 16,880.00 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 338,480.00 USD | 0.00 USD | 110.12 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 338,370.00 USD | 0.00 USD | 1,670.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 336,700.00 USD | 0.00 USD | 17,760.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 318,940.00 USD | 0.00 USD | 13,550.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 305,390.00 USD | 0.00 USD | 551.98 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 304,840.00 USD | 0.00 USD | 138,380.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 166,460.00 USD | 0.00 USD | 1,690.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 164,770.00 USD | 0.00 USD | 34,460.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 130,310.00 USD | 0.00 USD | 2,030.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 128,280.00 USD | 0.00 USD | 2,340.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 125,940.00 USD | 0.00 USD | 383.97 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 125,560.00 USD | 0.00 USD | 2,540.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 123,020.00 USD | 0.00 USD | 4,030.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 118,980.00 USD | 0.00 USD | 386.09 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 118,600.00 USD | 0.00 USD | 1,950.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 116,640.00 USD | 0.00 USD | 535.16 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 116,110.00 USD | 0.00 USD | 227.92 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 115,880.00 USD | 0.00 USD | 397.76 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 115,480.00 USD | 0.00 USD | 398.00 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 115,080.00 USD | 0.00 USD | 797.39 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 114,290.00 USD | 0.00 USD | 59,820.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 54,460.00 USD | 0.00 USD | 1,640.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 52,820.00 USD | 0.00 USD | 189.57 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 52,630.00 USD | 0.00 USD | 1,480.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 51,150.00 USD | 0.00 USD | 334.27 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 50,820.00 USD | 0.00 USD | 415.62 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 50,400.00 USD | 0.00 USD | 16,520.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 33,890.00 USD | 0.00 USD | 3,170.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 30,710.00 USD | 0.00 USD | 7,460.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 23,250.00 USD | 0.00 USD | 391.32 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 22,860.00 USD | 0.00 USD | 140.04 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 22,720.00 USD | 0.00 USD | 1,490.00 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 21,220.00 USD | 0.00 USD | 3,750.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 17,470.00 USD | 0.00 USD | 17,270.00 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 198.96 USD | 0.00 USD | 198.96 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0754` | 1,700.00 USD | 1,700.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0755` | 1,850.00 USD | 151.35 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 9,350.00 USD | 7,490.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 9,500.00 USD | 150.85 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 10,710.00 USD | 1,210.00 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 11,210.00 USD | 504.10 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 11,610.00 USD | 398.13 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 15,010.00 USD | 3,400.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 17,040.00 USD | 2,020.00 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 17,850.00 USD | 814.81 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 21,630.00 USD | 3,770.00 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 21,740.00 USD | 109.63 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 22,980.00 USD | 1,250.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 23,160.00 USD | 183.50 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 23,370.00 USD | 200.93 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 24,730.00 USD | 1,360.00 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 25,550.00 USD | 816.05 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 26,670.00 USD | 1,120.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 29,290.00 USD | 2,620.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 30,470.00 USD | 1,180.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 34,400.00 USD | 3,930.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 34,810.00 USD | 407.23 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 35,130.00 USD | 321.13 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 35,540.00 USD | 409.84 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 37,790.00 USD | 2,240.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 38,120.00 USD | 329.23 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 38,270.00 USD | 155.43 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 39,090.00 USD | 823.90 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 42,020.00 USD | 2,920.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 42,990.00 USD | 975.23 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 43,410.00 USD | 413.84 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 43,560.00 USD | 157.14 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 43,690.00 USD | 130.71 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 85,660.00 USD | 41,960.00 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 85,800.00 USD | 141.44 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 86,570.00 USD | 773.68 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 87,260.00 USD | 687.81 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 92,680.00 USD | 5,420.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 93,490.00 USD | 812.79 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 98,860.00 USD | 5,370.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 107,880.00 USD | 9,020.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 108,190.00 USD | 312.56 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 108,650.00 USD | 455.34 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 108,780.00 USD | 125.45 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 109,010.00 USD | 230.40 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 109,330.00 USD | 319.16 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 110,330.00 USD | 1,010.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 133,080.00 USD | 22,750.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 133,480.00 USD | 400.91 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 133,680.00 USD | 200.46 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 133,940.00 USD | 259.13 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 137,140.00 USD | 3,200.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 146,150.00 USD | 9,010.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 242,930.00 USD | 96,780.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 243,740.00 USD | 807.50 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 244,000.00 USD | 257.18 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 244,420.00 USD | 424.74 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 244,520.00 USD | 101.80 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 245,910.00 USD | 1,380.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 247,930.00 USD | 2,030.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 249,360.00 USD | 1,430.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 249,490.00 USD | 129.67 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 250,510.00 USD | 1,020.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 250,770.00 USD | 256.05 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 251,790.00 USD | 1,030.00 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 254,820.00 USD | 3,020.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 255,140.00 USD | 327.80 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 255,600.00 USD | 457.92 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 256,290.00 USD | 691.29 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 257,090.00 USD | 800.79 USD | 0.00 USD | `+9.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 257,610.00 USD | 512.05 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 258,100.00 USD | 495.36 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 258,490.00 USD | 389.31 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 258,650.00 USD | 154.58 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 258,950.00 USD | 303.56 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 259,060.00 USD | 112.89 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 259,440.00 USD | 381.45 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 259,600.00 USD | 155.82 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 303,990.00 USD | 44,390.00 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 304,290.00 USD | 309.23 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 305,550.00 USD | 1,260.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 306,800.00 USD | 1,240.00 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,050,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,060,000.00 USD | 3,150.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,060,000.00 USD | 1,470.00 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,060,000.00 USD | 107.71 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,060,000.00 USD | 2,690.00 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,060,000.00 USD | 529.92 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,060,000.00 USD | 219.07 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,060,000.00 USD | 242.84 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,070,000.00 USD | 10,140.00 USD | 0.00 USD | `+12.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,070,000.00 USD | 876.11 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,070,000.00 USD | 812.54 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,070,000.00 USD | 126.76 USD | 0.00 USD | `+13.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,070,000.00 USD | 307.41 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,070,000.00 USD | 614.09 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,070,000.00 USD | 859.50 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,080,000.00 USD | 2,020.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,120,000.00 USD | 43,760.00 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,120,000.00 USD | 123.94 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,120,000.00 USD | 271.53 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,120,000.00 USD | 1,660.00 USD | 0.00 USD | `+15.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,120,000.00 USD | 1,840.00 USD | 0.00 USD | `+15.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,130,000.00 USD | 2,760.00 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,130,000.00 USD | 117.71 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,130,000.00 USD | 111.61 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,130,000.00 USD | 571.18 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,130,000.00 USD | 375.94 USD | 0.00 USD | `+17.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,130,000.00 USD | 627.55 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,130,000.00 USD | 211.04 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,130,000.00 USD | 108.36 USD | 0.00 USD | `+17.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,130,000.00 USD | 543.32 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,130,000.00 USD | 1,820.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,130,000.00 USD | 2,080.00 USD | 0.00 USD | `+18.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,150,000.00 USD | 17,680.00 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,150,000.00 USD | 1,370.00 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,160,000.00 USD | 5,630.00 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,160,000.00 USD | 1,090.00 USD | 0.00 USD | `+19.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,160,000.00 USD | 224.86 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,180,000.00 USD | 20,540.00 USD | 0.00 USD | `+20.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,180,000.00 USD | 114.93 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,180,000.00 USD | 679.12 USD | 0.00 USD | `+20.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,180,000.00 USD | 173.36 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,180,000.00 USD | 1,810.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,180,000.00 USD | 1,530.00 USD | 0.00 USD | `+21.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,190,000.00 USD | 2,280.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,190,000.00 USD | 541.32 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,320,000.00 USD | 137,500.00 USD | 0.00 USD | `+22.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,330,000.00 USD | 691.07 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,330,000.00 USD | 6,250.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,350,000.00 USD | 13,480.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,350,000.00 USD | 734.82 USD | 0.00 USD | `+23.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,350,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,350,000.00 USD | 105.00 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,350,000.00 USD | 184.09 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,350,000.00 USD | 1,120.00 USD | 0.00 USD | `+24.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,350,000.00 USD | 1,860.00 USD | 0.00 USD | `+24.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,350,000.00 USD | 1,070.00 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,350,000.00 USD | 512.15 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,360,000.00 USD | 6,620.00 USD | 0.00 USD | `+25.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,360,000.00 USD | 404.96 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,360,000.00 USD | 129.85 USD | 0.00 USD | `+26.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,360,000.00 USD | 3,740.00 USD | 0.00 USD | `+27.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,360,000.00 USD | 409.17 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,360,000.00 USD | 203.74 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,370,000.00 USD | 2,800.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,370,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,370,000.00 USD | 694.56 USD | 0.00 USD | `+29.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,370,000.00 USD | 940.91 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,370,000.00 USD | 2,980.00 USD | 0.00 USD | `+31.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,370,000.00 USD | 104.99 USD | 0.00 USD | `+31.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,370,000.00 USD | 1,930.00 USD | 0.00 USD | `+31.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | `+32.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,400,000.00 USD | 1,490.00 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,400,000.00 USD | 1,090.00 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,400,000.00 USD | 438.96 USD | 0.00 USD | `+32.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,400,000.00 USD | 973.76 USD | 0.00 USD | `+32.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,410,000.00 USD | 10,000.00 USD | 0.00 USD | `+32.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,410,000.00 USD | 175.59 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,410,000.00 USD | 2,060.00 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,410,000.00 USD | 482.89 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,410,000.00 USD | 201.90 USD | 0.00 USD | `+34.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,410,000.00 USD | 489.46 USD | 0.00 USD | `+34.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,410,000.00 USD | 103.68 USD | 0.00 USD | `+34.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,410,000.00 USD | 2,590.00 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,420,000.00 USD | 3,810.00 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,430,000.00 USD | 11,200.00 USD | 0.00 USD | `+35.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,430,000.00 USD | 4,330.00 USD | 0.00 USD | `+35.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,430,000.00 USD | 205.50 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,440,000.00 USD | 3,490.00 USD | 0.00 USD | `+36.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,440,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,440,000.00 USD | 207.50 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,440,000.00 USD | 813.88 USD | 0.00 USD | `+38.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,460,000.00 USD | 23,160.00 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,460,000.00 USD | 209.30 USD | 0.00 USD | `+39.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,460,000.00 USD | 1,440.00 USD | 0.00 USD | `+39.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,470,000.00 USD | 5,140.00 USD | 0.00 USD | `+39.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,470,000.00 USD | 585.32 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,470,000.00 USD | 210.90 USD | 0.00 USD | `+40.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,470,000.00 USD | 1,850.00 USD | 0.00 USD | `+40.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,470,000.00 USD | 105.75 USD | 0.00 USD | `+40.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,480,000.00 USD | 3,220.00 USD | 0.00 USD | `+40.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,480,000.00 USD | 1,600.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,480,000.00 USD | 212.90 USD | 0.00 USD | `+41.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,480,000.00 USD | 472.63 USD | 0.00 USD | `+42.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,480,000.00 USD | 214.50 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,480,000.00 USD | 1,040.00 USD | 0.00 USD | `+43.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,480,000.00 USD | 136.12 USD | 0.00 USD | `+43.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,480,000.00 USD | 216.10 USD | 0.00 USD | `+43.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,480,000.00 USD | 1,010.00 USD | 0.00 USD | `+44.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,480,000.00 USD | 217.90 USD | 0.00 USD | `+44.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,480,000.00 USD | 219.70 USD | 0.00 USD | `+45.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,490,000.00 USD | 7,780.00 USD | 0.00 USD | `+46.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,490,000.00 USD | 154.22 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,490,000.00 USD | 221.30 USD | 0.00 USD | `+47.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,490,000.00 USD | 1,050.00 USD | 0.00 USD | `+47.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,510,000.00 USD | 24,190.00 USD | 0.00 USD | `+47.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,510,000.00 USD | 223.10 USD | 0.00 USD | `+48.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,510,000.00 USD | 224.70 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,520,000.00 USD | 226.30 USD | 0.00 USD | `+50.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,520,000.00 USD | 950.34 USD | 0.00 USD | `+51.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,520,000.00 USD | 229.50 USD | 0.00 USD | `+52.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,520,000.00 USD | 771.08 USD | 0.00 USD | `+52.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,520,000.00 USD | 942.95 USD | 0.00 USD | `+52.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,520,000.00 USD | 230.90 USD | 0.00 USD | `+53.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,520,000.00 USD | 288.18 USD | 0.00 USD | `+53.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,520,000.00 USD | 619.10 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,520,000.00 USD | 1,250.00 USD | 0.00 USD | `+54.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,520,000.00 USD | 232.30 USD | 0.00 USD | `+54.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,520,000.00 USD | 1,600.00 USD | 0.00 USD | `+55.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,530,000.00 USD | 3,730.00 USD | 0.00 USD | `+55.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,530,000.00 USD | 676.22 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,530,000.00 USD | 648.25 USD | 0.00 USD | `+56.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,530,000.00 USD | 1,510.00 USD | 0.00 USD | `+56.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,530,000.00 USD | 448.52 USD | 0.00 USD | `+57.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,530,000.00 USD | 124.58 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,530,000.00 USD | 1,050.00 USD | 0.00 USD | `+58.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,530,000.00 USD | 691.80 USD | 0.00 USD | `+59.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,650,000.00 USD | 117,860.00 USD | 0.00 USD | `+59.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,650,000.00 USD | 143.22 USD | 0.00 USD | `+59.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,650,000.00 USD | 1,380.00 USD | 0.00 USD | `+60.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,650,000.00 USD | 2,270.00 USD | 0.00 USD | `+62.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,660,000.00 USD | 871.99 USD | 0.00 USD | `+62.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,690,000.00 USD | 29,610.00 USD | 0.00 USD | `+68.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,690,000.00 USD | 400.21 USD | 0.00 USD | `+68.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,690,000.00 USD | 2,360.00 USD | 0.00 USD | `+75.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,690,000.00 USD | 4,160.00 USD | 0.00 USD | `+80.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,690,000.00 USD | 114.70 USD | 0.00 USD | `+81.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,690,000.00 USD | 278.50 USD | 0.00 USD | `+85.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,690,000.00 USD | 1,160.00 USD | 0.00 USD | `+87.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,690,000.00 USD | 173.57 USD | 0.00 USD | `+88.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,690,000.00 USD | 380.09 USD | 0.00 USD | `+89.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,710,000.00 USD | 17,150.00 USD | 0.00 USD | `+89.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,710,000.00 USD | 1,440.00 USD | 0.00 USD | `+91.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,710,000.00 USD | 433.35 USD | 0.00 USD | `+91.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,710,000.00 USD | 452.26 USD | 0.00 USD | `+93.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,720,000.00 USD | 3,640.00 USD | 0.00 USD | `+95.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,770,000.00 USD | 55,720.00 USD | 0.00 USD | `+96.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,780,000.00 USD | 2,120.00 USD | 0.00 USD | `+97.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,800,000.00 USD | 19,850.00 USD | 0.00 USD | `+99.26%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0657` | 30,770,000.00 USD | 0.00 USD | 30,770,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0661` | 30,750,000.00 USD | 0.00 USD | 30,750,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD |
| `7D` | `0.0662` | 30,710,000.00 USD | 0.00 USD | 30,710,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `7D` | `0.0665` | 30,710,000.00 USD | 0.00 USD | 30,710,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD |
| `7D` | `0.0669` | 30,520,000.00 USD | 0.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `7D` | `0.0674` | 30,520,000.00 USD | 0.00 USD | 30,520,000.00 USD | 5,520.00 USD | 3,930.00 USD | 0.00 USD |
| `7D` | `0.0675` | 30,510,000.00 USD | 0.00 USD | 30,510,000.00 USD | 19,910.00 USD | 4,530.00 USD | 19,470.00 USD |
| `7D` | `0.0676` | 30,470,000.00 USD | 0.00 USD | 30,470,000.00 USD | 6,810.00 USD | 0.00 USD | 475.18 USD |
| `1D` | `0.0677` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 67,140.00 USD | 96,830.00 USD | 17,460.00 USD |
| `7D` | `0.0677` | 30,460,000.00 USD | 0.00 USD | 30,460,000.00 USD | 3,660.00 USD | 9,140.00 USD | 609.05 USD |
| `1D` | `0.0678` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 40,890.00 USD | 47,200.00 USD | 80,440.00 USD |
| `7D` | `0.0678` | 30,450,000.00 USD | 0.00 USD | 30,450,000.00 USD | 12,840.00 USD | 51,630.00 USD | 0.00 USD |
| `1D` | `0.0679` | 18,270,000.00 USD | 0.00 USD | 18,270,000.00 USD | 72,650.00 USD | 39,580.00 USD | 8,120.00 USD |
| `7D` | `0.0679` | 30,380,000.00 USD | 0.00 USD | 30,380,000.00 USD | 19,040.00 USD | 8,140.00 USD | 74,820.00 USD |
| `1D` | `0.0680` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 51,160.00 USD | 43,850.00 USD | 41,570.00 USD |
| `7D` | `0.0680` | 30,280,000.00 USD | 0.00 USD | 30,280,000.00 USD | 84,730.00 USD | 47,420.00 USD | 164,800.00 USD |
| `1D` | `0.0681` | 18,020,000.00 USD | 0.00 USD | 18,020,000.00 USD | 36,810.00 USD | 55,770.00 USD | 150,410.00 USD |
| `7D` | `0.0681` | 29,990,000.00 USD | 0.00 USD | 29,990,000.00 USD | 54,210.00 USD | 14,460.00 USD | 0.00 USD |
| `1D` | `0.0682` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 15,430.00 USD | 67,700.00 USD | 32,040.00 USD |
| `7D` | `0.0682` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 0.00 USD | 35,790.00 USD | 66,930.00 USD |
| `1D` | `0.0683` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 27,270.00 USD | 32,750.00 USD | 467.62 USD |
| `7D` | `0.0683` | 29,810,000.00 USD | 0.00 USD | 29,810,000.00 USD | 0.00 USD | 22,580.00 USD | 0.00 USD |
| `1D` | `0.0684` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 24,150.00 USD | 26,540.00 USD | 3,380.00 USD |
| `7D` | `0.0684` | 29,790,000.00 USD | 0.00 USD | 29,790,000.00 USD | 111,040.00 USD | 4,760.00 USD | 1,160.00 USD |
| `1D` | `0.0685` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 58,140.00 USD | 14,450.00 USD | 28,590.00 USD |
| `7D` | `0.0685` | 29,670,000.00 USD | 0.00 USD | 29,670,000.00 USD | 31,800.00 USD | 73,160.00 USD | 24,220.00 USD |
| `1D` | `0.0686` | 17,440,000.00 USD | 0.00 USD | 17,440,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,280.00 USD |
| `7D` | `0.0686` | 29,550,000.00 USD | 0.00 USD | 29,550,000.00 USD | 57,320.00 USD | 64,030.00 USD | 388.90 USD |
| `1D` | `0.0687` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,030.00 USD |
| `7D` | `0.0687` | 29,420,000.00 USD | 0.00 USD | 29,420,000.00 USD | 44,400.00 USD | 64,060.00 USD | 617.20 USD |
| `1D` | `0.0688` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD |
| `7D` | `0.0688` | 29,310,000.00 USD | 0.00 USD | 29,310,000.00 USD | 40,320.00 USD | 0.00 USD | 60,810.00 USD |
| `1D` | `0.0689` | 17,210,000.00 USD | 0.00 USD | 17,210,000.00 USD | 10,400.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.0689` | 29,210,000.00 USD | 0.00 USD | 29,210,000.00 USD | 185,160.00 USD | 77,640.00 USD | 277.73 USD |
| `1D` | `0.0690` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `7D` | `0.0690` | 28,950,000.00 USD | 0.00 USD | 28,950,000.00 USD | 112,090.00 USD | 64,360.00 USD | 73,160.00 USD |
| `1D` | `0.0691` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 1,460.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `0.0691` | 28,700,000.00 USD | 0.00 USD | 28,700,000.00 USD | 49,920.00 USD | 30,660.00 USD | 57,750.00 USD |
| `1D` | `0.0692` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0692` | 28,560,000.00 USD | 0.00 USD | 28,560,000.00 USD | 78,440.00 USD | 76,890.00 USD | 41,990.00 USD |
| `1D` | `0.0693` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0693` | 28,360,000.00 USD | 0.00 USD | 28,360,000.00 USD | 128,710.00 USD | 113,280.00 USD | 38,210.00 USD |
| `1D` | `0.0694` | 17,150,000.00 USD | 0.00 USD | 17,150,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0694` | 28,080,000.00 USD | 0.00 USD | 28,080,000.00 USD | 169,230.00 USD | 67,150.00 USD | 102,450.00 USD |
| `1D` | `0.0695` | 17,130,000.00 USD | 0.00 USD | 17,130,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0695` | 27,750,000.00 USD | 0.00 USD | 27,750,000.00 USD | 113,240.00 USD | 145,370.00 USD | 110,100.00 USD |
| `7D` | `0.0696` | 27,380,000.00 USD | 0.00 USD | 27,380,000.00 USD | 100,230.00 USD | 61,080.00 USD | 186,810.00 USD |
| `1D` | `0.0697` | 17,120,000.00 USD | 0.00 USD | 17,120,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD |
| `7D` | `0.0697` | 27,030,000.00 USD | 0.00 USD | 27,030,000.00 USD | 41,960.00 USD | 87,540.00 USD | 76,690.00 USD |
| `1D` | `0.0698` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 10,960.00 USD | 10,400.00 USD | 9,890.00 USD |
| `7D` | `0.0698` | 26,820,000.00 USD | 0.00 USD | 26,820,000.00 USD | 127,350.00 USD | 103,870.00 USD | 71,040.00 USD |
| `1D` | `0.0699` | 17,030,000.00 USD | 0.00 USD | 17,030,000.00 USD | 38,680.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `0.0699` | 26,520,000.00 USD | 0.00 USD | 26,520,000.00 USD | 198,220.00 USD | 101,580.00 USD | 67,180.00 USD |
| `1D` | `0.0700` | 16,990,000.00 USD | 0.00 USD | 16,990,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,890.00 USD |
| `7D` | `0.0700` | 26,150,000.00 USD | 0.00 USD | 26,150,000.00 USD | 117,390.00 USD | 110,810.00 USD | 86,640.00 USD |
| `1D` | `0.0701` | 16,870,000.00 USD | 0.00 USD | 16,870,000.00 USD | 32,570.00 USD | 108,360.00 USD | 1,860.00 USD |
| `7D` | `0.0701` | 25,840,000.00 USD | 0.00 USD | 25,840,000.00 USD | 166,270.00 USD | 8,980.00 USD | 56,110.00 USD |
| `1D` | `0.0702` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 47,790.00 USD | 0.00 USD | 122.84 USD |
| `7D` | `0.0702` | 25,610,000.00 USD | 0.00 USD | 25,610,000.00 USD | 168,320.00 USD | 97,270.00 USD | 50,390.00 USD |
| `1D` | `0.0703` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 139,990.00 USD | 57,870.00 USD | 4,210.00 USD |
| `7D` | `0.0703` | 25,290,000.00 USD | 0.00 USD | 25,290,000.00 USD | 107,990.00 USD | 23,160.00 USD | 1,240.00 USD |
| `1D` | `0.0704` | 16,470,000.00 USD | 0.00 USD | 16,470,000.00 USD | 4,460.00 USD | 31,030.00 USD | 2,320.00 USD |
| `7D` | `0.0704` | 25,160,000.00 USD | 0.00 USD | 25,160,000.00 USD | 139,040.00 USD | 55,790.00 USD | 17,600.00 USD |
| `1D` | `0.0705` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 41,460.00 USD | 30,720.00 USD | 34,210.00 USD |
| `7D` | `0.0705` | 24,950,000.00 USD | 0.00 USD | 24,950,000.00 USD | 85,040.00 USD | 77,390.00 USD | 160,970.00 USD |
| `1D` | `0.0706` | 16,330,000.00 USD | 0.00 USD | 16,330,000.00 USD | 24,210.00 USD | 1,120.00 USD | 15,630.00 USD |
| `7D` | `0.0706` | 24,620,000.00 USD | 0.00 USD | 24,620,000.00 USD | 25,760.00 USD | 13,870.00 USD | 46,870.00 USD |
| `1D` | `0.0707` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 139,250.00 USD | 69,310.00 USD | 45,730.00 USD |
| `7D` | `0.0707` | 24,540,000.00 USD | 0.00 USD | 24,540,000.00 USD | 145,730.00 USD | 23,290.00 USD | 109,250.00 USD |
| `1D` | `0.0708` | 16,040,000.00 USD | 0.00 USD | 16,040,000.00 USD | 69,400.00 USD | 62,000.00 USD | 107,390.00 USD |
| `7D` | `0.0708` | 24,260,000.00 USD | 0.00 USD | 24,260,000.00 USD | 20,200.00 USD | 31,420.00 USD | 51,150.00 USD |
| `1D` | `0.0709` | 15,800,000.00 USD | 0.00 USD | 15,800,000.00 USD | 38,730.00 USD | 82,010.00 USD | 149,320.00 USD |
| `7D` | `0.0709` | 24,160,000.00 USD | 0.00 USD | 24,160,000.00 USD | 465,090.00 USD | 128,300.00 USD | 87,930.00 USD |
| `1D` | `0.0710` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,960.00 USD |
| `7D` | `0.0710` | 23,470,000.00 USD | 0.00 USD | 23,470,000.00 USD | 196,450.00 USD | 161,070.00 USD | 62,470.00 USD |
| `1D` | `0.0711` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 49,210.00 USD | 25,670.00 USD | 43,530.00 USD |
| `7D` | `0.0711` | 23,050,000.00 USD | 0.00 USD | 23,050,000.00 USD | 89,280.00 USD | 91,060.00 USD | 28,720.00 USD |
| `1D` | `0.0712` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 165,590.00 USD | 46,690.00 USD | 4,000.00 USD |
| `7D` | `0.0712` | 22,850,000.00 USD | 0.00 USD | 22,850,000.00 USD | 200,920.00 USD | 117,120.00 USD | 72,910.00 USD |
| `1D` | `0.0713` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 75,840.00 USD | 85,230.00 USD | 63,930.00 USD |
| `7D` | `0.0713` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 178,680.00 USD | 54,360.00 USD | 67,050.00 USD |
| `1D` | `0.0714` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 123,320.00 USD | 51,930.00 USD | 48,230.00 USD |
| `7D` | `0.0714` | 22,150,000.00 USD | 0.00 USD | 22,150,000.00 USD | 92,880.00 USD | 49,400.00 USD | 38,070.00 USD |
| `1D` | `0.0715` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 81,850.00 USD | 238,460.00 USD | 43,180.00 USD |
| `7D` | `0.0715` | 21,970,000.00 USD | 0.00 USD | 21,970,000.00 USD | 138,920.00 USD | 2,060.00 USD | 29,970.00 USD |
| `1D` | `0.0716` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 19,480.00 USD | 51,080.00 USD | 215.70 USD |
| `7D` | `0.0716` | 21,800,000.00 USD | 0.00 USD | 21,800,000.00 USD | 123,820.00 USD | 189,070.00 USD | 15,490.00 USD |
| `1D` | `0.0717` | 13,980,000.00 USD | 0.00 USD | 13,980,000.00 USD | 238,310.00 USD | 96,160.00 USD | 385.38 USD |
| `7D` | `0.0717` | 21,470,000.00 USD | 0.00 USD | 21,470,000.00 USD | 156,500.00 USD | 1,810.00 USD | 32,890.00 USD |
| `1D` | `0.0718` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 64,570.00 USD | 101,030.00 USD | 13,040.00 USD |
| `7D` | `0.0718` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 61,410.00 USD | 22,840.00 USD | 47,910.00 USD |
| `1D` | `0.0719` | 13,470,000.00 USD | 0.00 USD | 13,470,000.00 USD | 231,180.00 USD | 45,330.00 USD | 72,220.00 USD |
| `7D` | `0.0719` | 21,150,000.00 USD | 0.00 USD | 21,150,000.00 USD | 163,670.00 USD | 29,960.00 USD | 228,140.00 USD |
| `1D` | `0.0720` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 141,760.00 USD | 50,600.00 USD | 72,110.00 USD |
| `7D` | `0.0720` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 282,840.00 USD | 169,120.00 USD | 54,740.00 USD |
| `1D` | `0.0721` | 12,850,000.00 USD | 0.00 USD | 12,850,000.00 USD | 308,410.00 USD | 298,040.00 USD | 67,520.00 USD |
| `7D` | `0.0721` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 139,860.00 USD | 116,340.00 USD | 40,930.00 USD |
| `1D` | `0.0722` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 199,310.00 USD | 130,350.00 USD | 150,730.00 USD |
| `7D` | `0.0722` | 19,930,000.00 USD | 0.00 USD | 19,930,000.00 USD | 54,310.00 USD | 26,930.00 USD | 5,890.00 USD |
| `1D` | `0.0723` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 166,340.00 USD | 283,230.00 USD | 369,550.00 USD |
| `7D` | `0.0723` | 19,840,000.00 USD | 0.00 USD | 19,840,000.00 USD | 204,990.00 USD | 144,790.00 USD | 126,410.00 USD |
| `1D` | `0.0724` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 224,260.00 USD | 256,770.00 USD | 402,310.00 USD |
| `7D` | `0.0724` | 19,360,000.00 USD | 0.00 USD | 19,360,000.00 USD | 1,050,000.00 USD | 84,550.00 USD | 186,070.00 USD |
| `1D` | `0.0725` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 276,150.00 USD | 262,460.00 USD | 311,510.00 USD |
| `7D` | `0.0725` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 174,770.00 USD | 304,550.00 USD | 20,160.00 USD |
| `1D` | `0.0726` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 153,630.00 USD | 148,410.00 USD | 59,700.00 USD |
| `7D` | `0.0726` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 167,610.00 USD | 227,020.00 USD | 91,610.00 USD |
| `1D` | `0.0727` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 191,440.00 USD | 161,760.00 USD | 45,510.00 USD |
| `7D` | `0.0727` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 81,590.00 USD | 205,010.00 USD | 558.98 USD |
| `1D` | `0.0728` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 73,270.00 USD | 177,390.00 USD | 65,480.00 USD |
| `7D` | `0.0728` | 16,770,000.00 USD | 0.00 USD | 16,770,000.00 USD | 34,520.00 USD | 22,770.00 USD | 32,990.00 USD |
| `1D` | `0.0729` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 87,260.00 USD | 41,110.00 USD | 9,650.00 USD |
| `7D` | `0.0729` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 112,700.00 USD | 82,650.00 USD | 4,030.00 USD |
| `1D` | `0.0730` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 123,090.00 USD | 55,310.00 USD | 51,030.00 USD |
| `7D` | `0.0730` | 16,480,000.00 USD | 0.00 USD | 16,480,000.00 USD | 384,130.00 USD | 25,240.00 USD | 4,280.00 USD |
| `1D` | `0.0731` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 44,230.00 USD | 81,130.00 USD | 28,420.00 USD |
| `7D` | `0.0731` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 181,180.00 USD | 24,050.00 USD | 8,510.00 USD |
| `1D` | `0.0732` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 153,570.00 USD | 93,810.00 USD | 93,610.00 USD |
| `7D` | `0.0732` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 344,710.00 USD | 0.00 USD | 1,540.00 USD |
| `1D` | `0.0733` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD |
| `7D` | `0.0733` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 125,410.00 USD | 0.00 USD | 28,420.00 USD |
| `1D` | `0.0734` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD |
| `7D` | `0.0734` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 183,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0735` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD |
| `7D` | `0.0735` | 15,170,000.00 USD | 0.00 USD | 15,170,000.00 USD | 406,040.00 USD | 93,670.00 USD | 0.00 USD |
| `1D` | `0.0736` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `7D` | `0.0736` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 272,970.00 USD | 385,750.00 USD | 0.00 USD |
| `1D` | `0.0737` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 145,660.00 USD | 69,370.00 USD | 49,860.00 USD |
| `7D` | `0.0737` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 233,090.00 USD | 153,990.00 USD | 0.00 USD |
| `1D` | `0.0738` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 226,750.00 USD | 73,230.00 USD | 85,530.00 USD |
| `7D` | `0.0738` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 265,850.00 USD | 474,350.00 USD | 40,090.00 USD |
| `1D` | `0.0739` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 294,920.00 USD | 101,560.00 USD | 62,540.00 USD |
| `7D` | `0.0739` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 218,050.00 USD | 40,680.00 USD | 69,010.00 USD |
| `1D` | `0.0740` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 99,850.00 USD | 121,290.00 USD | 117,450.00 USD |
| `7D` | `0.0740` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 101,490.00 USD | 91,130.00 USD | 37,850.00 USD |
| `1D` | `0.0741` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 217,950.00 USD | 183,810.00 USD | 102,820.00 USD |
| `7D` | `0.0741` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 66,970.00 USD | 251,010.00 USD | 178,730.00 USD |
| `1D` | `0.0742` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 90,280.00 USD | 290,690.00 USD | 80,900.00 USD |
| `7D` | `0.0742` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 478,860.00 USD | 163,570.00 USD | 481,020.00 USD |
| `1D` | `0.0743` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 257,710.00 USD | 226,460.00 USD | 319,340.00 USD |
| `7D` | `0.0743` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 295,530.00 USD | 45,530.00 USD | 635,320.00 USD |
| `1D` | `0.0744` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 274,880.00 USD | 118,720.00 USD | 107,270.00 USD |
| `7D` | `0.0744` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 325,550.00 USD | 495,640.00 USD | 129,160.00 USD |
| `1D` | `0.0745` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 87,580.00 USD | 88,750.00 USD | 46,710.00 USD |
| `7D` | `0.0745` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 1,100,000.00 USD | 455,650.00 USD | 196,840.00 USD |
| `1D` | `0.0746` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 88,460.00 USD | 86,840.00 USD | 142,590.00 USD |
| `7D` | `0.0746` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 784,410.00 USD | 925,150.00 USD | 364,110.00 USD |
| `1D` | `0.0747` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,860.00 USD |
| `7D` | `0.0747` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 626,490.00 USD | 907,690.00 USD | 285,310.00 USD |
| `1D` | `0.0748` | 914,030.00 USD | 0.00 USD | 914,030.00 USD | 80,900.00 USD | 109,690.00 USD | 198,860.00 USD |
| `7D` | `0.0748` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 706,340.00 USD | 324,980.00 USD | 181,500.00 USD |
| `1D` | `0.0749` | 524,580.00 USD | 0.00 USD | 524,580.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD |
| `7D` | `0.0749` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 134,940.00 USD | 694,350.00 USD |
| `1D` | `0.0750` | 179,540.00 USD | 0.00 USD | 179,540.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD |
| `7D` | `0.0750` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 84,880.00 USD |
| `1D` | `0.0751` | 115,190.00 USD | 0.00 USD | 115,190.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD |
| `7D` | `0.0751` | 961,320.00 USD | 0.00 USD | 961,320.00 USD | 0.00 USD | 30,900.00 USD | 0.00 USD |
| `1D` | `0.0752` | 67,170.00 USD | 0.00 USD | 67,170.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `7D` | `0.0752` | 930,410.00 USD | 0.00 USD | 930,410.00 USD | 751,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0753` | 42,740.00 USD | 0.00 USD | 42,740.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD |
| `7D` | `0.0753` | 179,300.00 USD | 0.00 USD | 179,300.00 USD | 0.00 USD | 53,860.00 USD | 0.00 USD |
| `1D` | `0.0756` | 30,100.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD |
| `7D` | `0.0756` | 125,430.00 USD | 0.00 USD | 125,430.00 USD | 0.00 USD | 125,430.00 USD | 0.00 USD |
| `7D` | `0.0757` | 19,100.00 USD | 19,100.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD |
| `7D` | `0.0757` | 38,200.00 USD | 38,200.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD |
| `1D` | `0.0758` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD |
| `1D` | `0.0758` | 9,840.00 USD | 9,840.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD |
| `7D` | `0.0758` | 104,490.00 USD | 104,490.00 USD | 0.00 USD | 0.00 USD | 66,300.00 USD | 0.00 USD |
| `1D` | `0.0759` | 10,010.00 USD | 10,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.56 USD |
| `7D` | `0.0759` | 144,860.00 USD | 144,860.00 USD | 0.00 USD | 40,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0761` | 10,430.00 USD | 10,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 420.80 USD |
| `1D` | `0.0762` | 10,590.00 USD | 10,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.86 USD |
| `1D` | `0.0764` | 25,420.00 USD | 25,420.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | 0.00 USD |
| `7D` | `0.0764` | 399,460.00 USD | 399,460.00 USD | 0.00 USD | 0.00 USD | 254,610.00 USD | 0.00 USD |
| `1D` | `0.0765` | 373,580.00 USD | 373,580.00 USD | 0.00 USD | 211,600.00 USD | 37,120.00 USD | 99,440.00 USD |
| `7D` | `0.0765` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 772,480.00 USD | 241,990.00 USD | 0.00 USD |
| `1D` | `0.0766` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 352,420.00 USD | 421,720.00 USD | 291.50 USD |
| `7D` | `0.0766` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 594,350.00 USD | 90,730.00 USD | 0.00 USD |
| `1D` | `0.0767` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 164,440.00 USD | 335,150.00 USD | 159,130.00 USD |
| `7D` | `0.0767` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 587,940.00 USD | 45,720.00 USD | 0.00 USD |
| `1D` | `0.0768` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 372,440.00 USD | 143,560.00 USD | 680,280.00 USD |
| `7D` | `0.0768` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 117,000.00 USD | 7,860.00 USD | 92,730.00 USD |
| `1D` | `0.0769` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 471,540.00 USD | 522,820.00 USD | 350,170.00 USD |
| `7D` | `0.0769` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 861,620.00 USD | 76,450.00 USD | 445,860.00 USD |
| `1D` | `0.0770` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 456,790.00 USD | 301,010.00 USD | 487,080.00 USD |
| `7D` | `0.0770` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 392,100.00 USD | 325,170.00 USD | 291,470.00 USD |
| `1D` | `0.0771` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 441,280.00 USD | 459,510.00 USD | 251,890.00 USD |
| `7D` | `0.0771` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 597,990.00 USD | 520,750.00 USD | 540,700.00 USD |
| `1D` | `0.0772` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 480,450.00 USD | 327,770.00 USD | 765,720.00 USD |
| `7D` | `0.0772` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 0.00 USD | 284,970.00 USD | 1,630.00 USD |
| `1D` | `0.0773` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 212,370.00 USD | 413,920.00 USD | 278,550.00 USD |
| `7D` | `0.0773` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 69,030.00 USD | 62,610.00 USD | 62,430.00 USD |
| `1D` | `0.0774` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 176,230.00 USD | 246,740.00 USD | 36,420.00 USD |
| `7D` | `0.0774` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 137,990.00 USD | 210,270.00 USD | 0.00 USD |
| `1D` | `0.0775` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 288,570.00 USD | 180,890.00 USD | 61,000.00 USD |
| `7D` | `0.0775` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 707,860.00 USD | 164,830.00 USD | 0.00 USD |
| `1D` | `0.0776` | 10,860,000.00 USD | 10,860,000.00 USD | 0.00 USD | 284,830.00 USD | 214,460.00 USD | 142,590.00 USD |
| `7D` | `0.0776` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 250,110.00 USD | 39,020.00 USD | 0.00 USD |
| `1D` | `0.0777` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 401,010.00 USD | 342,630.00 USD | 163,070.00 USD |
| `7D` | `0.0777` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 15,870.00 USD | 247,550.00 USD | 693.20 USD |
| `1D` | `0.0778` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 116,640.00 USD | 340,450.00 USD | 401,410.00 USD |
| `7D` | `0.0778` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 229,240.00 USD | 86,160.00 USD | 78,860.00 USD |
| `1D` | `0.0779` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 345,840.00 USD | 210,420.00 USD | 205,560.00 USD |
| `7D` | `0.0779` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 41,210.00 USD | 215,530.00 USD | 359,800.00 USD |
| `1D` | `0.0780` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 212,580.00 USD | 78,920.00 USD | 39,560.00 USD |
| `7D` | `0.0780` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 169,380.00 USD | 64,660.00 USD | 3,180.00 USD |
| `1D` | `0.0781` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 19,450.00 USD |
| `7D` | `0.0781` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 17,030.00 USD | 77,790.00 USD | 1,190.00 USD |
| `1D` | `0.0782` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 87,770.00 USD | 92,890.00 USD | 79,490.00 USD |
| `7D` | `0.0782` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 148,920.00 USD | 195,010.00 USD |
| `1D` | `0.0783` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 129,550.00 USD | 239,780.00 USD | 220,140.00 USD |
| `7D` | `0.0783` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 32,110.00 USD | 159,820.00 USD | 20,040.00 USD |
| `1D` | `0.0784` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 436,380.00 USD | 152,210.00 USD | 70,780.00 USD |
| `7D` | `0.0784` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 109,020.00 USD | 45,010.00 USD | 187,060.00 USD |
| `1D` | `0.0785` | 16,120,000.00 USD | 16,120,000.00 USD | 0.00 USD | 238,930.00 USD | 171,160.00 USD | 120,930.00 USD |
| `7D` | `0.0785` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 248,170.00 USD | 120,330.00 USD | 144,620.00 USD |
| `1D` | `0.0786` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 352,080.00 USD | 218,550.00 USD | 296,610.00 USD |
| `7D` | `0.0786` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 201,610.00 USD | 202,070.00 USD | 488,040.00 USD |
| `1D` | `0.0787` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 380,000.00 USD | 464,730.00 USD | 386,460.00 USD |
| `7D` | `0.0787` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 235,890.00 USD | 143,980.00 USD | 324,670.00 USD |
| `1D` | `0.0788` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 180,850.00 USD | 284,830.00 USD | 140,960.00 USD |
| `7D` | `0.0788` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 74,330.00 USD | 22,770.00 USD | 146,160.00 USD |
| `1D` | `0.0789` | 19,500,000.00 USD | 19,500,000.00 USD | 0.00 USD | 341,120.00 USD | 233,260.00 USD | 102,060.00 USD |
| `7D` | `0.0789` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 260,530.00 USD | 236,420.00 USD | 103,190.00 USD |
| `1D` | `0.0790` | 19,770,000.00 USD | 19,770,000.00 USD | 0.00 USD | 156,500.00 USD | 87,240.00 USD | 27,690.00 USD |
| `7D` | `0.0790` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 353,930.00 USD | 65,630.00 USD | 3,910.00 USD |
| `1D` | `0.0791` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 205,560.00 USD | 133,580.00 USD | 125,170.00 USD |
| `7D` | `0.0791` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 142,610.00 USD | 15,670.00 USD | 2,660.00 USD |
| `1D` | `0.0792` | 20,590,000.00 USD | 20,590,000.00 USD | 0.00 USD | 224,560.00 USD | 57,840.00 USD | 74,750.00 USD |
| `7D` | `0.0792` | 15,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | 13,630.00 USD | 61,220.00 USD | 2,100.00 USD |
| `1D` | `0.0793` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 5,950.00 USD | 0.00 USD | 289.58 USD |
| `7D` | `0.0793` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 13,920.00 USD | 0.00 USD | 244,240.00 USD |
| `1D` | `0.0794` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 158,580.00 USD | 96,210.00 USD | 100,830.00 USD |
| `7D` | `0.0794` | 15,630,000.00 USD | 15,630,000.00 USD | 0.00 USD | 23,360.00 USD | 0.00 USD | 234,520.00 USD |
| `1D` | `0.0795` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 94,340.00 USD | 45,380.00 USD | 103,710.00 USD |
| `7D` | `0.0795` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 183,540.00 USD | 0.00 USD | 235,440.00 USD |
| `1D` | `0.0796` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 202,390.00 USD | 12,890.00 USD | 1,890.00 USD |
| `7D` | `0.0796` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 334,830.00 USD | 149,090.00 USD | 77,660.00 USD |
| `1D` | `0.0797` | 21,720,000.00 USD | 21,720,000.00 USD | 0.00 USD | 206,810.00 USD | 89,760.00 USD | 6,200.00 USD |
| `7D` | `0.0797` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 305,960.00 USD | 54,460.00 USD | 41,520.00 USD |
| `1D` | `0.0798` | 21,790,000.00 USD | 21,790,000.00 USD | 0.00 USD | 58,670.00 USD | 9,940.00 USD | 2,870.00 USD |
| `7D` | `0.0798` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 520,400.00 USD | 54,200.00 USD | 73,200.00 USD |
| `1D` | `0.0799` | 22,050,000.00 USD | 22,050,000.00 USD | 0.00 USD | 43,250.00 USD | 191,860.00 USD | 25,390.00 USD |
| `7D` | `0.0799` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 41,190.00 USD | 76,670.00 USD | 4,850.00 USD |
| `1D` | `0.0800` | 22,200,000.00 USD | 22,200,000.00 USD | 0.00 USD | 48,550.00 USD | 9,760.00 USD | 95,080.00 USD |
| `7D` | `0.0800` | 17,930,000.00 USD | 17,930,000.00 USD | 0.00 USD | 46,190.00 USD | 0.00 USD | 102,900.00 USD |
| `1D` | `0.0801` | 22,230,000.00 USD | 22,230,000.00 USD | 0.00 USD | 25,740.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `0.0801` | 17,970,000.00 USD | 17,970,000.00 USD | 0.00 USD | 38,850.00 USD | 0.00 USD | 1,950.00 USD |
| `1D` | `0.0802` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 27,390.00 USD | 1,770.00 USD | 122.84 USD |
| `7D` | `0.0802` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 12,270.00 USD | 0.00 USD | 2,390.00 USD |
| `1D` | `0.0803` | 22,370,000.00 USD | 22,370,000.00 USD | 0.00 USD | 25,660.00 USD | 43,340.00 USD | 41,270.00 USD |
| `7D` | `0.0803` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 45,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0804` | 22,380,000.00 USD | 22,380,000.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0804` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 108,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 22,550,000.00 USD | 22,550,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,270.00 USD |
| `7D` | `0.0805` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 120,200.00 USD | 43,910.00 USD | 53,390.00 USD |
| `1D` | `0.0806` | 22,820,000.00 USD | 22,820,000.00 USD | 0.00 USD | 28,730.00 USD | 21,040.00 USD | 215,520.00 USD |
| `7D` | `0.0806` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 99,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 23,220,000.00 USD | 23,220,000.00 USD | 0.00 USD | 228,350.00 USD | 143,670.00 USD | 30,480.00 USD |
| `7D` | `0.0807` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 118,470.00 USD | 934,840.00 USD | 294,860.00 USD |
| `1D` | `0.0808` | 23,870,000.00 USD | 23,870,000.00 USD | 0.00 USD | 152,200.00 USD | 116,140.00 USD | 382,880.00 USD |
| `7D` | `0.0808` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 9,880.00 USD | 910,170.00 USD | 0.00 USD |
| `1D` | `0.0809` | 24,220,000.00 USD | 24,220,000.00 USD | 0.00 USD | 111,710.00 USD | 220,760.00 USD | 12,790.00 USD |
| `7D` | `0.0809` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 0.00 USD | 851,040.00 USD | 1,700.00 USD |
| `1D` | `0.0810` | 24,650,000.00 USD | 24,650,000.00 USD | 0.00 USD | 175,100.00 USD | 127,690.00 USD | 132,630.00 USD |
| `7D` | `0.0810` | 21,970,000.00 USD | 21,970,000.00 USD | 0.00 USD | 131,030.00 USD | 264,390.00 USD | 0.00 USD |
| `1D` | `0.0811` | 24,850,000.00 USD | 24,850,000.00 USD | 0.00 USD | 100,060.00 USD | 85,950.00 USD | 11,510.00 USD |
| `7D` | `0.0811` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 466,230.00 USD | 1,610.00 USD |
| `1D` | `0.0812` | 25,100,000.00 USD | 25,100,000.00 USD | 0.00 USD | 133,170.00 USD | 101,130.00 USD | 19,950.00 USD |
| `7D` | `0.0812` | 22,780,000.00 USD | 22,780,000.00 USD | 0.00 USD | 138,370.00 USD | 200,500.00 USD | 1,600.00 USD |
| `1D` | `0.0813` | 25,230,000.00 USD | 25,230,000.00 USD | 0.00 USD | 37,200.00 USD | 28,660.00 USD | 56,010.00 USD |
| `7D` | `0.0813` | 23,510,000.00 USD | 23,510,000.00 USD | 0.00 USD | 378,950.00 USD | 347,890.00 USD | 874.59 USD |
| `1D` | `0.0814` | 25,520,000.00 USD | 25,520,000.00 USD | 0.00 USD | 43,650.00 USD | 108,690.00 USD | 143,260.00 USD |
| `7D` | `0.0814` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 142,940.00 USD | 446,780.00 USD | 3,190.00 USD |
| `1D` | `0.0815` | 25,640,000.00 USD | 25,640,000.00 USD | 0.00 USD | 20,890.00 USD | 6,740.00 USD | 94,490.00 USD |
| `7D` | `0.0815` | 24,960,000.00 USD | 24,960,000.00 USD | 0.00 USD | 447,170.00 USD | 144,240.00 USD | 265,690.00 USD |
| `1D` | `0.0816` | 26,340,000.00 USD | 26,340,000.00 USD | 0.00 USD | 323,740.00 USD | 194,310.00 USD | 179,480.00 USD |
| `7D` | `0.0816` | 25,820,000.00 USD | 25,820,000.00 USD | 0.00 USD | 267,850.00 USD | 451,830.00 USD | 145,480.00 USD |
| `1D` | `0.0817` | 26,890,000.00 USD | 26,890,000.00 USD | 0.00 USD | 280,410.00 USD | 134,560.00 USD | 130,180.00 USD |
| `7D` | `0.0817` | 27,340,000.00 USD | 27,340,000.00 USD | 0.00 USD | 789,320.00 USD | 294,010.00 USD | 437,490.00 USD |
| `1D` | `0.0818` | 27,550,000.00 USD | 27,550,000.00 USD | 0.00 USD | 232,030.00 USD | 161,260.00 USD | 267,770.00 USD |
| `7D` | `0.0818` | 28,310,000.00 USD | 28,310,000.00 USD | 0.00 USD | 249,420.00 USD | 327,510.00 USD | 388,760.00 USD |
| `1D` | `0.0819` | 28,140,000.00 USD | 28,140,000.00 USD | 0.00 USD | 153,870.00 USD | 312,480.00 USD | 128,220.00 USD |
| `7D` | `0.0819` | 29,460,000.00 USD | 29,460,000.00 USD | 0.00 USD | 422,920.00 USD | 184,980.00 USD | 540,240.00 USD |
| `1D` | `0.0820` | 28,680,000.00 USD | 28,680,000.00 USD | 0.00 USD | 42,510.00 USD | 172,050.00 USD | 319,740.00 USD |
| `7D` | `0.0820` | 30,350,000.00 USD | 30,350,000.00 USD | 0.00 USD | 288,610.00 USD | 382,680.00 USD | 217,720.00 USD |
| `1D` | `0.0821` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 144,440.00 USD | 48,110.00 USD | 85,260.00 USD |
| `7D` | `0.0821` | 31,810,000.00 USD | 31,810,000.00 USD | 0.00 USD | 916,830.00 USD | 377,990.00 USD | 172,610.00 USD |
| `1D` | `0.0822` | 29,510,000.00 USD | 29,510,000.00 USD | 0.00 USD | 249,310.00 USD | 151,600.00 USD | 156,380.00 USD |
| `7D` | `0.0822` | 32,520,000.00 USD | 32,520,000.00 USD | 0.00 USD | 374,110.00 USD | 203,780.00 USD | 128,840.00 USD |
| `1D` | `0.0823` | 29,860,000.00 USD | 29,860,000.00 USD | 0.00 USD | 267,050.00 USD | 72,540.00 USD | 8,520.00 USD |
| `7D` | `0.0823` | 33,590,000.00 USD | 33,590,000.00 USD | 0.00 USD | 510,700.00 USD | 317,120.00 USD | 237,850.00 USD |
| `1D` | `0.0824` | 30,420,000.00 USD | 30,420,000.00 USD | 0.00 USD | 168,680.00 USD | 204,930.00 USD | 190,880.00 USD |
| `7D` | `0.0824` | 34,530,000.00 USD | 34,530,000.00 USD | 0.00 USD | 470,790.00 USD | 274,570.00 USD | 194,990.00 USD |
| `1D` | `0.0825` | 30,670,000.00 USD | 30,670,000.00 USD | 0.00 USD | 102,430.00 USD | 125,690.00 USD | 22,000.00 USD |
| `7D` | `0.0825` | 35,170,000.00 USD | 35,170,000.00 USD | 0.00 USD | 290,680.00 USD | 239,750.00 USD | 112,380.00 USD |
| `1D` | `0.0826` | 31,100,000.00 USD | 31,100,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD |
| `7D` | `0.0826` | 36,000,000.00 USD | 36,000,000.00 USD | 0.00 USD | 514,230.00 USD | 68,910.00 USD | 251,430.00 USD |
| `1D` | `0.0827` | 31,200,000.00 USD | 31,200,000.00 USD | 0.00 USD | 19,540.00 USD | 65,440.00 USD | 16,720.00 USD |
| `7D` | `0.0827` | 36,330,000.00 USD | 36,330,000.00 USD | 0.00 USD | 144,110.00 USD | 160,890.00 USD | 20,850.00 USD |
| `1D` | `0.0828` | 31,580,000.00 USD | 31,580,000.00 USD | 0.00 USD | 211,700.00 USD | 83,250.00 USD | 80,790.00 USD |
| `7D` | `0.0828` | 36,870,000.00 USD | 36,870,000.00 USD | 0.00 USD | 376,390.00 USD | 110,640.00 USD | 54,090.00 USD |
| `1D` | `0.0829` | 31,870,000.00 USD | 31,870,000.00 USD | 0.00 USD | 198,070.00 USD | 89,690.00 USD | 8,360.00 USD |
| `7D` | `0.0829` | 37,400,000.00 USD | 37,400,000.00 USD | 0.00 USD | 283,400.00 USD | 67,100.00 USD | 173,780.00 USD |
| `1D` | `0.0830` | 32,010,000.00 USD | 32,010,000.00 USD | 0.00 USD | 54,060.00 USD | 37,820.00 USD | 43,280.00 USD |
| `7D` | `0.0830` | 37,760,000.00 USD | 37,760,000.00 USD | 0.00 USD | 112,420.00 USD | 80,560.00 USD | 173,830.00 USD |
| `1D` | `0.0831` | 32,090,000.00 USD | 32,090,000.00 USD | 0.00 USD | 20,050.00 USD | 16,920.00 USD | 44,840.00 USD |
| `7D` | `0.0831` | 38,210,000.00 USD | 38,210,000.00 USD | 0.00 USD | 294,840.00 USD | 53,670.00 USD | 98,180.00 USD |
| `1D` | `0.0832` | 32,470,000.00 USD | 32,470,000.00 USD | 0.00 USD | 182,190.00 USD | 93,160.00 USD | 100,500.00 USD |
| `7D` | `0.0832` | 38,820,000.00 USD | 38,820,000.00 USD | 0.00 USD | 186,700.00 USD | 262,800.00 USD | 160,430.00 USD |
| `1D` | `0.0833` | 32,880,000.00 USD | 32,880,000.00 USD | 0.00 USD | 122,770.00 USD | 111,030.00 USD | 181,680.00 USD |
| `7D` | `0.0833` | 39,340,000.00 USD | 39,340,000.00 USD | 0.00 USD | 266,360.00 USD | 152,020.00 USD | 100,110.00 USD |
| `1D` | `0.0834` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 123,130.00 USD | 127,940.00 USD | 149,290.00 USD |
| `7D` | `0.0834` | 39,840,000.00 USD | 39,840,000.00 USD | 0.00 USD | 90,460.00 USD | 146,730.00 USD | 265,290.00 USD |
| `1D` | `0.0835` | 33,660,000.00 USD | 33,660,000.00 USD | 0.00 USD | 120,730.00 USD | 188,990.00 USD | 64,110.00 USD |
| `7D` | `0.0835` | 40,500,000.00 USD | 40,500,000.00 USD | 0.00 USD | 275,000.00 USD | 115,070.00 USD | 271,030.00 USD |
| `1D` | `0.0836` | 33,900,000.00 USD | 33,900,000.00 USD | 0.00 USD | 37,940.00 USD | 57,720.00 USD | 146,570.00 USD |
| `7D` | `0.0836` | 40,820,000.00 USD | 40,820,000.00 USD | 0.00 USD | 204,620.00 USD | 27,680.00 USD | 88,950.00 USD |
| `7D` | `0.0837` | 41,290,000.00 USD | 41,290,000.00 USD | 0.00 USD | 239,800.00 USD | 199,750.00 USD | 26,260.00 USD |
| `7D` | `0.0838` | 41,580,000.00 USD | 41,580,000.00 USD | 0.00 USD | 199,340.00 USD | 64,030.00 USD | 31,610.00 USD |
| `7D` | `0.0839` | 41,750,000.00 USD | 41,750,000.00 USD | 0.00 USD | 94,520.00 USD | 64,060.00 USD | 4,690.00 USD |
| `7D` | `0.0840` | 41,930,000.00 USD | 41,930,000.00 USD | 0.00 USD | 117,710.00 USD | 0.00 USD | 62,190.00 USD |
| `7D` | `0.0841` | 42,020,000.00 USD | 42,020,000.00 USD | 0.00 USD | 87,460.00 USD | 0.00 USD | 2,760.00 USD |
| `7D` | `0.0842` | 42,350,000.00 USD | 42,350,000.00 USD | 0.00 USD | 220,360.00 USD | 33,520.00 USD | 81,570.00 USD |
| `7D` | `0.0843` | 42,520,000.00 USD | 42,520,000.00 USD | 0.00 USD | 117,190.00 USD | 44,120.00 USD | 3,500.00 USD |
| `7D` | `0.0844` | 42,820,000.00 USD | 42,820,000.00 USD | 0.00 USD | 164,260.00 USD | 64,360.00 USD | 77,300.00 USD |
| `7D` | `0.0845` | 42,980,000.00 USD | 42,980,000.00 USD | 0.00 USD | 70,690.00 USD | 30,660.00 USD | 57,750.00 USD |
| `7D` | `0.0846` | 43,210,000.00 USD | 43,210,000.00 USD | 0.00 USD | 106,330.00 USD | 76,890.00 USD | 40,580.00 USD |
| `7D` | `0.0847` | 43,490,000.00 USD | 43,490,000.00 USD | 0.00 USD | 137,750.00 USD | 113,280.00 USD | 35,260.00 USD |
| `7D` | `0.0848` | 43,770,000.00 USD | 43,770,000.00 USD | 0.00 USD | 117,070.00 USD | 57,210.00 USD | 99,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.07B` | Total OI Tokens: `14,058,936,046.3 DOGE`
  * 1h OI Change: `+0.55%` | 4h OI Change: `+0.21%` | 24h OI Change: `-5.15%`
  * Exchange Breakdown: Binance=`240.92M` | Bybit=`107.12M` | OKX=`110.79M` | Hyperliquid=`75.74M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `16.34K` | Last 24h: `49.48K` | Last 3d: `238.63K` | Last 7d: `304.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0046%` |
| **USDT Bybit** | `-0.0081%` | **USDT KuCoin** | `0.0056%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0031%` | **USDT Bitget** | `0.0008%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0097%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `42.76%` | `57.24%` | `0.75` | 12,820,000.00 USD |
| `15M` | `Binance` | `37.63%` | `62.37%` | `0.60` | 7,750,000.00 USD |
| `15M` | `OKX` | `42.44%` | `57.56%` | `0.74` | 1,140,000.00 USD |
| `15M` | `Bybit` | `53.45%` | `46.55%` | `1.15` | 1,230,000.00 USD |
| `15M` | `KuCoin` | `37.06%` | `62.94%` | `0.59` | 96,150.00 USD |
| `15M` | `Gate` | `51.64%` | `48.36%` | `1.07` | 747,710.00 USD |
| `15M` | `Bitget` | `65.03%` | `34.97%` | `1.86` | 118,880.00 USD |
| `15M` | `BingX` | `59.97%` | `40.03%` | `1.50` | 266,480.00 USD |
| `15M` | `MEXC` | `29.64%` | `70.36%` | `0.42` | 152,450.00 USD |
| `15M` | `Bitunix` | `63.04%` | `36.96%` | `1.71` | 576,820.00 USD |
| `15M` | `Hyperliquid` | `60.89%` | `39.11%` | `1.56` | 226,790.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `26.03%` | `73.97%` | `0.35` | 126,500.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `70.49%` | `29.51%` | `2.39` | 55,840.00 USD |
| `15M` | `HTX` | `35.59%` | `64.41%` | `0.55` | 94,240.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.8%` | `50.2%` | `0.99` | 13,450.00 USD |
| `15M` | `Aster` | `65.75%` | `34.25%` | `1.92` | 106,120.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `30.52%` | `69.48%` | `0.44` | 121,630.00 USD |
| `15M` | `Whale Positions` | `37.63%` | `62.37%` | `0.60` | 7,750,000.00 USD |
| `15M` | `Global Accounts` | `42.76%` | `57.24%` | `0.75` | 12,820,000.00 USD |
| `1H` | `DOGE` | `45.77%` | `54.23%` | `0.84` | 57,280,000.00 USD |
| `1H` | `Binance` | `42.74%` | `57.26%` | `0.75` | 33,270,000.00 USD |
| `1H` | `OKX` | `57.38%` | `42.62%` | `1.35` | 6,010,000.00 USD |
| `1H` | `Bybit` | `44.65%` | `55.35%` | `0.81` | 4,790,000.00 USD |
| `1H` | `KuCoin` | `50.96%` | `49.04%` | `1.04` | 687,290.00 USD |
| `1H` | `Gate` | `53.01%` | `46.99%` | `1.13` | 2,770,000.00 USD |
| `1H` | `Bitget` | `55.83%` | `44.17%` | `1.26` | 816,010.00 USD |
| `1H` | `BingX` | `57.94%` | `42.06%` | `1.38` | 1,230,000.00 USD |
| `1H` | `MEXC` | `58.75%` | `41.25%` | `1.42` | 769,860.00 USD |
| `1H` | `Bitunix` | `35.7%` | `64.3%` | `0.56` | 2,100,000.00 USD |
| `1H` | `Hyperliquid` | `56.99%` | `43.01%` | `1.33` | 2,090,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.34%` | `50.66%` | `0.97` | 446,480.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `9.38%` | `90.62%` | `0.10` | 650,700.00 USD |
| `1H` | `HTX` | `34.81%` | `65.19%` | `0.53` | 405,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `65.3%` | `34.7%` | `1.88` | 140,220.00 USD |
| `1H` | `Aster` | `45.22%` | `54.78%` | `0.83` | 775,390.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.99%` | `49.01%` | `1.04` | 337,200.00 USD |
| `1H` | `Whale Positions` | `42.74%` | `57.26%` | `0.75` | 33,270,000.00 USD |
| `1H` | `Global Accounts` | `45.77%` | `54.23%` | `0.84` | 57,280,000.00 USD |
| `4H` | `DOGE` | `41.60%` | `58.40%` | `0.71` | 264,640,000.00 USD |
| `4H` | `Binance` | `39.76%` | `60.24%` | `0.66` | 169,410,000.00 USD |
| `4H` | `OKX` | `46.34%` | `53.66%` | `0.86` | 21,190,000.00 USD |
| `4H` | `Bybit` | `36.07%` | `63.93%` | `0.56` | 18,740,000.00 USD |
| `4H` | `KuCoin` | `48.6%` | `51.4%` | `0.95` | 3,250,000.00 USD |
| `4H` | `Gate` | `48.69%` | `51.31%` | `0.95` | 12,980,000.00 USD |
| `4H` | `Bitget` | `45.72%` | `54.28%` | `0.84` | 5,820,000.00 USD |
| `4H` | `BingX` | `47.43%` | `52.57%` | `0.90` | 5,190,000.00 USD |
| `4H` | `MEXC` | `54.1%` | `45.9%` | `1.18` | 3,120,000.00 USD |
| `4H` | `Bitunix` | `44.33%` | `55.67%` | `0.80` | 7,040,000.00 USD |
| `4H` | `Hyperliquid` | `51.19%` | `48.81%` | `1.05` | 6,440,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.08%` | `51.92%` | `0.93` | 2,230,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `3.77%` | `96.23%` | `0.04` | 2,320,000.00 USD |
| `4H` | `HTX` | `51.52%` | `48.48%` | `1.06` | 1,760,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `69.47%` | `30.53%` | `2.28` | 1,050,000.00 USD |
| `4H` | `Aster` | `46.77%` | `53.23%` | `0.88` | 2,570,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `67.25%` | `32.75%` | `2.05` | 1,520,000.00 USD |
| `4H` | `Whale Positions` | `39.76%` | `60.24%` | `0.66` | 169,410,000.00 USD |
| `4H` | `Global Accounts` | `41.60%` | `58.40%` | `0.71` | 264,640,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0757` | `0.0757` | `0.0757` | `0.0759` | `0.0755` | 2,056,025.64 USD | 709,276.38 USD | 1,346,749.25 USD | -637,472.87 USD | `-31.01%` | `2B / 13S` |
| `5:00 UTC` | `0.0754` | `0.0755` | `0.0754` | `0.0757` | `0.0753` | 2,905,242.56 USD | 1,422,846.87 USD | 1,482,395.68 USD | -59,548.81 USD | `-2.05%` | `8B / 3S` |
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0754` | 2,313,298.65 USD | 1,197,641.49 USD | 1,115,657.16 USD | 81,984.32 USD | `+3.54%` | `3B / 4S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0756` | `0.0753` | 2,260,519.88 USD | 1,007,921.72 USD | 1,252,598.16 USD | -244,676.43 USD | `-10.82%` | `2B / 8S` |
| `0:00 UTC` | `0.0755` | `0.0754` | `0.0755` | `0.0756` | `0.0752` | 2,922,007.92 USD | 1,333,625.48 USD | 1,588,382.44 USD | -254,756.96 USD | `-8.72%` | `6B / 8S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0755` | `0.0753` | 1,576,593.18 USD | 686,951.41 USD | 889,641.77 USD | -202,690.36 USD | `-12.86%` | `0B / 6S` |
| `0:00 UTC` | `0.0753` | `0.0753` | `0.0753` | `0.0755` | `0.0752` | 4,029,142.63 USD | 2,078,130.01 USD | 1,951,012.62 USD | 127,117.39 USD | `+3.15%` | `4B / 6S` |
| `5:00 UTC` | `0.0753` | `0.0754` | `0.0753` | `0.0756` | `0.0752` | 2,334,240.03 USD | 1,034,700.08 USD | 1,299,539.95 USD | -264,839.88 USD | `-11.35%` | `4B / 9S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0760` | `0.0754` | 4,037,679.84 USD | 2,041,412.62 USD | 1,996,267.22 USD | 45,145.39 USD | `+1.12%` | `14B / 6S` |
| `5:00 UTC` | `0.0758` | `0.0757` | `0.0758` | `0.0759` | `0.0756` | 1,225,839.15 USD | 364,406.63 USD | 861,432.51 USD | -497,025.88 USD | `-40.55%` | `2B / 6S` |

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
| `5m` | 4,630.00 USD | -195,650.00 USD | **`DISTRIBUTION`** |
| `15m` | 73,400.00 USD | 31,320.00 USD | **`ACCUMULATION`** |
| `30m` | 245,050.00 USD | 435,480.00 USD | **`ACCUMULATION`** |
| `1h` | 855,320.00 USD | 367,830.00 USD | **`ACCUMULATION`** |
| `2h` | -4,820.00 USD | 534,210.00 USD | **`ACCUMULATION`** |
| `4h` | -174,870.00 USD | -9,580,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 156,970.00 USD | -9,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 1,310,000.00 USD | -6,040,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -6,870,000.00 USD | -30,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -17,790,000.00 USD | -64,820,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -59,930,000.00 USD | -194,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -285,230,000.00 USD | -822,940,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.63K` | 15m=`+73.40K` | 1h=`+855.32K` | 24h=`-17.79M`
* Futures Capital Netflows: 5m=`-195.65K` | 15m=`+31.32K` | 1h=`+367.83K` | 24h=`-64.82M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0737` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0701` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0842`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0754` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0790` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0649`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0764`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
