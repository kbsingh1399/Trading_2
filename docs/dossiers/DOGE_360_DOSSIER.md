# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 15:12:01 IST` (`2026-10-30 09:42:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0744` | **Live Ask Quote**: `0.0765` | **Mid Price**: `0.0754`
- **Spread Points**: `21.00` | **Spread BPS**: `278.33 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0737` | VWAP Z-Score: `+0.54` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000424` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.05` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0769` | Lower -3.00σ Band: `0.0706`
  * Upper +2.51σ Band: `0.0764` | Lower -2.51σ Band: `0.0711`
  * Upper +2.01σ Band: `0.0759` | Lower -2.01σ Band: `0.0716`
  * Upper +2.00σ Band: `0.0758` | Lower -2.00σ Band: `0.0716`
  * Upper +1.28σ Band: `0.0751` | Lower -1.28σ Band: `0.0724`
  * Upper +1.00σ Band: `0.0748` | Lower -1.00σ Band: `0.0727`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0745` | EMA-20=`0.0746` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0750` (Slope: `+0.0000`) | EMA-100=`0.0757`
  * Institutional Anchors: EMA-144=`0.0761` | EMA-200=`0.0764` (Slope: `-0.2950`) | EMA-233=`0.0766`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0755` (Distance: `-0.10%`)
  * Point of Control (POC) = `0.0749` (Distance: `+0.75%`)
  * Value Area Low (VAL) = `0.0737` (Distance: `+2.41%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0783` | Weekly POC=`0.0762` | Weekly VAL=`0.0747`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0756` | Low=`0.0741`
  * New York Session (13:00-21:00 UTC): High=`0.0759` | Low=`0.0750`
  * Initial Balance (First Hour): IB High=`0.0754` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0751` - `0.0758`
  * Optimal Trade Entry (OTE 0.705): `0.0756`
  * Structural Invalidation Anchor (0.786): `0.0761`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0754` | `0.0754` | `0.0752` | `0.0754` | `16,788,426` | 1,264,574.94 USD | -555,250.35 USD | `-43.91%` | -37,519,384.24 USD | `-1.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0754` | `0.0755` | `0.0754` | `0.0755` | `10,922,392` | 823,923.98 USD | 291,220.04 USD | `+35.35%` | -37,228,164.20 USD | `+1.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0755` | `0.0755` | `0.0755` | `0.0755` | `2,330,833` | 175,996.89 USD | 47,149.28 USD | `+26.79%` | -37,181,014.92 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0756` | `0.0758` | `0.0754` | `0.0755` | `30,602,806` | 2,313,298.65 USD | 81,984.32 USD | `+3.54%` | -36,719,457.45 USD | `+0.81` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0755` | `0.0756` | `0.0753` | `0.0754` | `29,966,276` | 2,260,519.88 USD | -244,676.43 USD | `-10.82%` | -36,964,133.88 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0754` | `0.0755` | `0.0752` | `0.0755` | `29,938,665` | 2,256,720.43 USD | -223,646.66 USD | `-9.91%` | -37,187,780.54 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0764` | `0.0765` | `0.0755` | `0.0756` | `201,594,432` | 15,303,841.53 USD | -2,746,811.49 USD | `-17.95%` | -33,956,752.10 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.0756` | `0.0761` | `0.0753` | `0.0756` | `194,653,019` | 14,729,253.09 USD | -2,572,015.39 USD | `-17.46%` | -36,528,767.49 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0756` | `0.0758` | `0.0752` | `0.0755` | `90,507,747` | 6,830,538.96 USD | -386,338.77 USD | `-5.66%` | -36,915,106.26 USD | `+0.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0752` | `0.0755` | `285,263,752` | 21,567,567.43 USD | -2,951,588.53 USD | `-13.69%` | -34,650,797.24 USD | `+0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | 1,581,082.63 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -21,458,643.59 USD | `-1.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0752` | `0.0755` | `285,263,752` | 21,567,567.43 USD | -2,951,588.53 USD | `-13.69%` | -34,650,797.24 USD | `+0.34` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0754`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0755` | `173934.0000` | 13,137.58 USD | 136,732.69 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.0755` | `539585.0000` | 40,755.39 USD | 123,595.11 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `12860.0000` | 971.32 USD | 82,839.72 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `48754.0000` | 3,682.29 USD | 81,868.40 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `19860.0000` | 1,499.97 USD | 78,186.11 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `50553.0000` | 3,818.07 USD | 76,686.14 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `19860.0000` | 1,499.93 USD | 72,868.08 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `429626.0000` | 32,447.07 USD | 71,368.15 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `99889.0000` | 7,543.92 USD | 38,921.07 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `32720.0000` | 2,471.08 USD | 31,377.16 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `19860.0000` | 1,499.85 USD | 28,906.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `95581.0000` | 7,218.28 USD | 27,406.23 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `19860.0000` | 1,499.81 USD | 20,187.95 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `19860.0000` | 1,499.79 USD | 18,688.15 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `19863.0000` | 1,499.99 USD | 17,188.36 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `19863.0000` | 1,499.97 USD | 15,688.36 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0755` | `15744.0000` | 1,188.91 USD | 14,188.39 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0755` | `137851.0000` | 10,409.68 USD | 12,999.48 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0755` | `33762.0000` | 2,549.33 USD | 2,589.80 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0755` | `536.0000` | 40.47 USD | 40.47 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0755` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0755` | `61661.0000` | 4,655.22 USD | 4,655.22 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `0.0755` | `92719.0000` | 6,999.54 USD | 11,654.76 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0755` | `57177.0000` | 4,316.35 USD | 15,971.11 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0755` | `549.0000` | 41.44 USD | 16,012.56 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0755` | `123642.0000` | 9,333.24 USD | 25,345.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0755` | `12860.0000` | 970.74 USD | 26,316.53 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0755` | `12860.0000` | 970.71 USD | 27,287.24 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0755` | `30820.0000` | 2,326.36 USD | 29,613.60 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0755` | `419985.0000` | 31,700.89 USD | 61,314.49 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0755` | `69515.0000` | 5,246.99 USD | 66,561.48 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0755` | `452464.0000` | 34,150.63 USD | 100,712.10 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0755` | `12860.0000` | 970.62 USD | 101,682.73 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0755` | `5911.0000` | 446.13 USD | 102,128.86 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.0755` | `19202.0000` | 1,449.21 USD | 103,578.07 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0755` | `52472.0000` | 3,960.06 USD | 107,538.13 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0755` | `128246.0000` | 9,678.47 USD | 117,216.60 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0755` | `100785.0000` | 7,605.94 USD | 124,822.54 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0755` | `82944.0000` | 6,259.20 USD | 131,081.75 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0755` | `23520.0000` | 1,774.87 USD | 132,856.61 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0755` | `97845.0000` | 7,383.48 USD | 140,240.09 USD | `2 orders` | `-0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:10:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `307` | `0xb83d...6e36` | `SHORT` | 7,738,476.29 USD | `102,645,925.00` | `0.0946` | `0.0753` | `1.17` | 1,968,865.37 USD | `+25.44%` | `3X Cross` |
| `315` | `0xc63a...a3cd` | `LONG` | 7,527,500.00 USD | `100,000,000.00` | `0.0856` | `0.0753` | `0.000000` | -1,037,321.96 USD | `-13.78%` | `10X Cross` |
| `316` | `0x610b...b613` | `LONG` | 7,437,968.37 USD | `98,666,424.00` | `0.0872` | `0.0753` | `0.0604` | -1,162,213.53 USD | `-15.63%` | `5X Cross` |
| `613` | `0x5b5d...c060` | `SHORT` | 3,730,218.42 USD | `49,478,955.00` | `0.0946` | `0.0753` | `3.02` | 951,298.19 USD | `+25.50%` | `3X Cross` |
| `646` | `0xca49...53c8` | `SHORT` | 3,503,172.10 USD | `46,542,649.00` | `0.0929` | `0.0753` | `0.3978` | 822,872.57 USD | `+23.49%` | `10X Cross` |
| `661` | `0x45d2...4029` | `SHORT` | 3,423,666.77 USD | `45,426,000.00` | `0.0954` | `0.0753` | `0.9903` | 911,962.45 USD | `+26.64%` | `10X Cross` |
| `689` | `0xecb6...2b00` | `SHORT` | 3,269,139.89 USD | `43,363,044.00` | `0.0788` | `0.0753` | `0.7706` | 148,629.59 USD | `+4.55%` | `10X Cross` |
| `1193` | `0x458d...ab3b` | `LONG` | 1,843,029.37 USD | `24,454,063.00` | `0.1002` | `0.0753` | `0.0714` | -607,892.54 USD | `-32.98%` | `3X Isolated` |
| `1201` | `0xeadc...9d55` | `LONG` | 1,832,805.45 USD | `24,317,440.00` | `0.0926` | `0.0753` | `0.000000` | -418,789.12 USD | `-22.85%` | `10X Cross` |
| `1337` | `0xf48f...10fe` | `LONG` | 1,614,678.64 USD | `21,424,497.00` | `0.0968` | `0.0753` | `0.0474` | -459,625.96 USD | `-28.47%` | `4X Cross` |
| `1366` | `0x9946...0852` | `SHORT` | 1,570,795.09 USD | `20,845,267.00` | `0.0859` | `0.0753` | `0.1500` | 220,490.92 USD | `+14.04%` | `10X Cross` |
| `1580` | `0xcac1...26b3` | `SHORT` | 1,366,582.09 USD | `18,126,835.00` | `0.0943` | `0.0753` | `0.5481` | 342,877.11 USD | `+25.09%` | `10X Cross` |
| `1601` | `0x0d6a...ca57` | `LONG` | 1,328,417.78 USD | `17,626,455.00` | `0.0875` | `0.0753` | `0.0626` | -213,687.18 USD | `-16.09%` | `3X Isolated` |
| `1666` | `0x4808...a82c` | `LONG` | 1,268,522.25 USD | `16,828,143.00` | `0.0883` | `0.0753` | `0.0632` | -217,950.73 USD | `-17.18%` | `3X Cross` |
| `1716` | `0x9aa5...58af` | `SHORT` | 1,227,030.05 USD | `16,275,119.00` | `0.0907` | `0.0753` | `0.6420` | 248,610.49 USD | `+20.26%` | `10X Cross` |
| `1809` | `0x31ef...f715` | `LONG` | 1,147,892.79 USD | `15,230,102.00` | `0.0936` | `0.0753` | `0.0668` | -277,803.14 USD | `-24.20%` | `3X Isolated` |
| `1832` | `0xbfc7...80b4` | `SHORT` | 1,132,402.86 USD | `15,020,000.00` | `0.0920` | `0.0753` | `0.1813` | 249,996.43 USD | `+22.08%` | `10X Cross` |
| `1912` | `0x7cee...fc93` | `SHORT` | 1,055,984.88 USD | `14,013,468.00` | `0.0863` | `0.0753` | `0.2642` | 152,892.48 USD | `+14.48%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0782` | 5,001.16 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.00K USD at 0.0782 USD [API] | `2026-10-29 09:16:31` |
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 5,002.89 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.00K USD at 0.0783 USD [API] | `2026-10-29 09:19:04` |
| `ANNOUNCEMENT` | `INFO` | `0.0782` | 6,305.19 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.31K USD at 0.0782 USD [API] | `2026-10-29 09:28:21` |
| `ANNOUNCEMENT` | `INFO` | `0.0781` | 10,286.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.29K USD at 0.0781 USD [API] | `2026-10-29 09:48:31` |
| `ANNOUNCEMENT` | `INFO` | `0.0780` | 5,273.56 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.27K USD at 0.0780 USD [API] | `2026-10-29 10:28:51` |
| `ANNOUNCEMENT` | `INFO` | `0.0784` | 5,209.28 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.21K USD at 0.0784 USD [API] | `2026-10-29 10:47:36` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 6,966.22 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 6.97K USD at 0.0786 USD [API] | `2026-10-29 11:01:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 6,257.77 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 6.26K USD at 0.0786 USD [API] | `2026-10-29 11:01:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 10,493.93 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.49K USD at 0.0786 USD [API] | `2026-10-29 11:01:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 42,624.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 42.62K USD at 0.0800 USD [API] | `2026-10-15 02:22:46` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 7,468.63 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.47K USD at 0.0791 USD [API] | `2026-10-29 13:15:02` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 7,925.53 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.93K USD at 0.0792 USD [API] | `2026-10-29 13:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 23,358.29 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 23.36K USD at 0.0791 USD [API] | `2026-10-29 13:24:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 5,177.50 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.18K USD at 0.0791 USD [API] | `2026-10-29 13:24:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0801` | 16,847.38 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 16.85K USD at 0.0801 USD [API] | `2026-10-29 17:04:14` |
| `ANNOUNCEMENT` | `INFO` | `0.0801` | 10,443.92 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.44K USD at 0.0801 USD [API] | `2026-10-29 17:04:14` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 5,402.81 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.40K USD at 0.0800 USD [API] | `2026-10-29 17:05:53` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 5,145.70 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.15K USD at 0.0800 USD [API] | `2026-10-29 17:16:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.91%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.93%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.91%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.93%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.91%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.93%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.91%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.93%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0152` | 1,450.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0162` | 1,800.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0167` | 5,320.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0168` | 2,570.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0170` | 204.07 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0175` | 1,040.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0175` | 1,050.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0192` | 1,440.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0203` | 648.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0222` | 138.08 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0226` | 884.46 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 11,580.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0236` | 142.50 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0249` | 394.09 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0253` | 22,570.00 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0254` | 4,020.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0256` | 760.04 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0265` | 416.51 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0266` | 531.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 40,570.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0289` | 498.04 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0297` | 158.98 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0300` | 967.33 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0308` | 266.67 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0321` | 6,040.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0326` | 458.31 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0330` | 133.94 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 760.15 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 4,630.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 13,620.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 8,390.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 35,100.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0376` | 169.54 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 1,790.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 181.66 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0387` | 207.27 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 201.32 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 6,110.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 1,480.00 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 56,970.00 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 21,880.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 6,400.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 596.82 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 2,960.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0428` | 49,010.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 5,030.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 22,660.00 USD | 16,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 113,160.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 2,620.00 USD | 16,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 772.50 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 893.78 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 438.22 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 33,660.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0462` | 1,250.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 11,970.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 2,870.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 1,420.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 1,120,000.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 258.33 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 58,890.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 1,780.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0486` | 2,430.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 4,800.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 106.23 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,310.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 254.25 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 4,950.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 314.91 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 3,530.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 6,970.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,420.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 2,390.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 4,790.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 44,830.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,920.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0530` | 27,810.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 14,030.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 6,010.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 42,580.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 800.95 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 1,040.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 223.18 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 258.10 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 3,030.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 95,630.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 903.30 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 892.81 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 23,860.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 2,380.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 347.95 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 1,100.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 4,010.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 144.08 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 41,360.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 4,060.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 181.77 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,760.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 622.09 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 17,220.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 47,390.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 4,050.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,140.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,680.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 4,970.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 3,580.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 2,500.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 5,970,000.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 35,530.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 357,770.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 17,110.00 USD | 7,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 1,940.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 5,110.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 709.03 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 27,580.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 2,330.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,800.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 1,120.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,430.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,850.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 9,740.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 150.01 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 3,270.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 1,330.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,280.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,180.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0647` | 29,780,000.00 USD | 29,780,000.00 USD | 23,160.00 USD | 13,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0649` | 29,740,000.00 USD | 29,740,000.00 USD | 21,850.00 USD | 0.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 14,160.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0657` | 29,710,000.00 USD | 29,710,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0661` | 29,690,000.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 13,740.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0663` | 29,650,000.00 USD | 29,650,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0665` | 29,640,000.00 USD | 29,640,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 8,880.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0669` | 29,460,000.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 6,120.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 2,830.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 4,830.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0675` | 29,460,000.00 USD | 29,460,000.00 USD | 25,430.00 USD | 8,460.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,610.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0677` | 17,660,000.00 USD | 17,660,000.00 USD | 48,630.00 USD | 94,300.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0677` | 29,410,000.00 USD | 29,410,000.00 USD | 10,470.00 USD | 0.00 USD | 475.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 17,500,000.00 USD | 17,500,000.00 USD | 18,700.00 USD | 39,890.00 USD | 65,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 17,370,000.00 USD | 17,370,000.00 USD | 57,130.00 USD | 39,580.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0679` | 29,390,000.00 USD | 29,390,000.00 USD | 6,140.00 USD | 59,770.00 USD | 61,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 17,270,000.00 USD | 17,270,000.00 USD | 51,160.00 USD | 43,850.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 667.50 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 17,130,000.00 USD | 17,130,000.00 USD | 36,810.00 USD | 55,770.00 USD | 149,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0681` | 29,270,000.00 USD | 29,270,000.00 USD | 118,640.00 USD | 61,880.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0682` | 16,890,000.00 USD | 16,890,000.00 USD | 14,920.00 USD | 58,710.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,770.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 16,790,000.00 USD | 16,790,000.00 USD | 15,780.00 USD | 32,750.00 USD | 23.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0683` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 58,370.00 USD | 66,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 16,740,000.00 USD | 16,740,000.00 USD | 24,150.00 USD | 26,540.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 79,490.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 16,690,000.00 USD | 16,690,000.00 USD | 58,140.00 USD | 14,450.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0685` | 28,800,000.00 USD | 28,800,000.00 USD | 142,840.00 USD | 77,920.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 8,890.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 16,590,000.00 USD | 16,590,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 4,840.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 16,500,000.00 USD | 16,500,000.00 USD | 17,350.00 USD | 32,460.00 USD | 29,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0687` | 28,550,000.00 USD | 28,550,000.00 USD | 101,720.00 USD | 128,090.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 16,420,000.00 USD | 16,420,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 38,040.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 16,360,000.00 USD | 16,360,000.00 USD | 10,400.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0689` | 28,320,000.00 USD | 28,320,000.00 USD | 225,480.00 USD | 77,640.00 USD | 61,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 508,320.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 10,030.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 16,340,000.00 USD | 16,340,000.00 USD | 1,460.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0691` | 27,960,000.00 USD | 27,960,000.00 USD | 162,010.00 USD | 95,020.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 16,340,000.00 USD | 16,340,000.00 USD | 23,110.00 USD | 0.00 USD | 670.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,140.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 16,310,000.00 USD | 16,310,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0693` | 27,570,000.00 USD | 27,570,000.00 USD | 207,150.00 USD | 190,180.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 16,300,000.00 USD | 16,300,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 16,270,000.00 USD | 16,270,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0695` | 27,090,000.00 USD | 27,090,000.00 USD | 282,470.00 USD | 212,530.00 USD | 212,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 4,950.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 16,270,000.00 USD | 16,270,000.00 USD | 31,720.00 USD | 13,590.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0697` | 26,380,000.00 USD | 26,380,000.00 USD | 142,190.00 USD | 148,620.00 USD | 263,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 6,970.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 16,200,000.00 USD | 16,200,000.00 USD | 10,960.00 USD | 10,400.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,910.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 16,170,000.00 USD | 16,170,000.00 USD | 38,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0699` | 25,830,000.00 USD | 25,830,000.00 USD | 325,570.00 USD | 205,450.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 16,130,000.00 USD | 16,130,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 16,010,000.00 USD | 16,010,000.00 USD | 39,680.00 USD | 108,360.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0701` | 25,160,000.00 USD | 25,160,000.00 USD | 283,670.00 USD | 119,790.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,180.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 15,860,000.00 USD | 15,860,000.00 USD | 47,190.00 USD | 19,670.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,300.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 15,790,000.00 USD | 15,790,000.00 USD | 148,860.00 USD | 62,920.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0703` | 24,610,000.00 USD | 24,610,000.00 USD | 261,240.00 USD | 120,430.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 3,790.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 15,570,000.00 USD | 15,570,000.00 USD | 15,860.00 USD | 36,100.00 USD | 20,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 780.37 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 15,500,000.00 USD | 15,500,000.00 USD | 41,460.00 USD | 30,720.00 USD | 37,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0705` | 24,180,000.00 USD | 24,180,000.00 USD | 224,080.00 USD | 133,180.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 15,390,000.00 USD | 15,390,000.00 USD | 22,880.00 USD | 1,120.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 608.86 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 15,350,000.00 USD | 15,350,000.00 USD | 136,920.00 USD | 69,310.00 USD | 45,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0707` | 23,650,000.00 USD | 23,650,000.00 USD | 171,490.00 USD | 37,160.00 USD | 156,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 15,100,000.00 USD | 15,100,000.00 USD | 69,400.00 USD | 62,000.00 USD | 105,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 14,860,000.00 USD | 14,860,000.00 USD | 38,730.00 USD | 82,010.00 USD | 151,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0709` | 23,280,000.00 USD | 23,280,000.00 USD | 485,290.00 USD | 159,720.00 USD | 139,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 14,590,000.00 USD | 14,590,000.00 USD | 117,230.00 USD | 91,550.00 USD | 125,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 4,720.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 14,260,000.00 USD | 14,260,000.00 USD | 49,210.00 USD | 25,670.00 USD | 42,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0711` | 22,500,000.00 USD | 22,500,000.00 USD | 285,730.00 USD | 252,130.00 USD | 91,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,860.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 14,140,000.00 USD | 14,140,000.00 USD | 165,590.00 USD | 46,690.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 13,930,000.00 USD | 13,930,000.00 USD | 75,840.00 USD | 85,230.00 USD | 64,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0713` | 21,870,000.00 USD | 21,870,000.00 USD | 379,600.00 USD | 171,480.00 USD | 139,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 13,700,000.00 USD | 13,700,000.00 USD | 120,780.00 USD | 51,930.00 USD | 46,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 13,270.00 USD | 408,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 13,480,000.00 USD | 13,480,000.00 USD | 79,660.00 USD | 238,460.00 USD | 41,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0715` | 21,180,000.00 USD | 21,180,000.00 USD | 211,700.00 USD | 51,460.00 USD | 66,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 394,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 13,120,000.00 USD | 13,120,000.00 USD | 19,480.00 USD | 51,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 3,840.00 USD | 386,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 13,050,000.00 USD | 13,050,000.00 USD | 238,310.00 USD | 96,160.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0717` | 20,850,000.00 USD | 20,850,000.00 USD | 285,100.00 USD | 190,890.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 48,180.00 USD | 382,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 12,710,000.00 USD | 12,710,000.00 USD | 64,570.00 USD | 101,030.00 USD | 15,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,090.00 USD | 334,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 12,530,000.00 USD | 12,530,000.00 USD | 229,400.00 USD | 45,330.00 USD | 68,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0719` | 20,320,000.00 USD | 20,320,000.00 USD | 233,070.00 USD | 63,390.00 USD | 276,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 333,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 12,190,000.00 USD | 12,190,000.00 USD | 138,650.00 USD | 50,600.00 USD | 69,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 5,090.00 USD | 331,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 11,930,000.00 USD | 11,930,000.00 USD | 308,410.00 USD | 298,040.00 USD | 65,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0721` | 19,750,000.00 USD | 19,750,000.00 USD | 422,700.00 USD | 285,460.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 613.35 USD | 326,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 11,260,000.00 USD | 11,260,000.00 USD | 181,970.00 USD | 124,010.00 USD | 149,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 38,340.00 USD | 326,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 10,800,000.00 USD | 10,800,000.00 USD | 89,550.00 USD | 258,330.00 USD | 323,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0723` | 18,950,000.00 USD | 18,950,000.00 USD | 242,550.00 USD | 148,860.00 USD | 110,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 286,760.00 USD | 287,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 10,130,000.00 USD | 10,130,000.00 USD | 176,130.00 USD | 226,580.00 USD | 401,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 984.89 USD | 984.89 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 9,330,000.00 USD | 9,330,000.00 USD | 253,760.00 USD | 262,460.00 USD | 310,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0725` | 18,440,000.00 USD | 18,440,000.00 USD | 1,070,000.00 USD | 365,360.00 USD | 152,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 8,500,000.00 USD | 8,500,000.00 USD | 153,630.00 USD | 148,410.00 USD | 59,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 8,140,000.00 USD | 8,140,000.00 USD | 190,550.00 USD | 161,760.00 USD | 40,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0727` | 16,860,000.00 USD | 16,860,000.00 USD | 249,200.00 USD | 432,030.00 USD | 92,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 7,740,000.00 USD | 7,740,000.00 USD | 60,510.00 USD | 154,910.00 USD | 47,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 7,480,000.00 USD | 7,480,000.00 USD | 58,550.00 USD | 41,110.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0729` | 16,080,000.00 USD | 16,080,000.00 USD | 114,120.00 USD | 105,410.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,370,000.00 USD | 7,370,000.00 USD | 123,090.00 USD | 55,310.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 7,150,000.00 USD | 7,150,000.00 USD | 44,230.00 USD | 81,130.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0731` | 15,830,000.00 USD | 15,830,000.00 USD | 565,310.00 USD | 49,290.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 6,990,000.00 USD | 6,990,000.00 USD | 153,570.00 USD | 93,810.00 USD | 92,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,650,000.00 USD | 6,650,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0733` | 15,200,000.00 USD | 15,200,000.00 USD | 470,120.00 USD | 0.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 6,460,000.00 USD | 6,460,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 6,020,000.00 USD | 6,020,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0735` | 14,700,000.00 USD | 14,700,000.00 USD | 589,440.00 USD | 93,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 5,850,000.00 USD | 5,850,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,600,000.00 USD | 5,600,000.00 USD | 113,510.00 USD | 56,690.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0737` | 14,020,000.00 USD | 14,020,000.00 USD | 506,070.00 USD | 494,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,380,000.00 USD | 5,380,000.00 USD | 78,630.00 USD | 23,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,280,000.00 USD | 5,280,000.00 USD | 198,660.00 USD | 41,170.00 USD | 62,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0739` | 13,020,000.00 USD | 13,020,000.00 USD | 265,850.00 USD | 515,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,980,000.00 USD | 4,980,000.00 USD | 57,880.00 USD | 121,290.00 USD | 117,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,680,000.00 USD | 4,680,000.00 USD | 217,950.00 USD | 183,810.00 USD | 102,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0741` | 12,240,000.00 USD | 12,240,000.00 USD | 66,970.00 USD | 294,670.00 USD | 178,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,180,000.00 USD | 4,180,000.00 USD | 90,280.00 USD | 290,690.00 USD | 80,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,710,000.00 USD | 3,710,000.00 USD | 236,300.00 USD | 181,510.00 USD | 284,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0743` | 11,700,000.00 USD | 11,700,000.00 USD | 774,380.00 USD | 209,100.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,010,000.00 USD | 3,010,000.00 USD | 217,450.00 USD | 118,720.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,570,000.00 USD | 2,570,000.00 USD | 87,580.00 USD | 88,750.00 USD | 46,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0745` | 9,600,000.00 USD | 9,600,000.00 USD | 1,360,000.00 USD | 951,300.00 USD | 326,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,350,000.00 USD | 2,350,000.00 USD | 88,460.00 USD | 86,840.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 2,030,000.00 USD | 2,030,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0747` | 6,960,000.00 USD | 6,960,000.00 USD | 1,410,000.00 USD | 1,830,000.00 USD | 649,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,040,000.00 USD | 1,040,000.00 USD | 98,680.00 USD | 109,690.00 USD | 198,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 636,130.00 USD | 636,130.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0749` | 3,070,000.00 USD | 3,070,000.00 USD | 706,340.00 USD | 459,930.00 USD | 875,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 291,080.00 USD | 291,080.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 226,740.00 USD | 226,740.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0751` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 30,900.00 USD | 84,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 178,710.00 USD | 178,710.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 154,290.00 USD | 154,290.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0753` | 907,280.00 USD | 907,280.00 USD | 751,120.00 USD | 53,860.00 USD | 102,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0754` | 113.76 USD | 113.76 USD | 0.00 USD | 0.00 USD | 113.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0754` | 227.52 USD | 227.52 USD | 0.00 USD | 0.00 USD | 113.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0755` | 2,120.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0755` | 938,670.00 USD | 938,670.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0755` | 1,880,000.00 USD | 1,880,000.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0756` | 32,790.00 USD | 32,790.00 USD | 0.00 USD | 30,100.00 USD | 570.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 144,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0758` | 37,710.00 USD | 37,710.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0759` | 38,190.00 USD | 38,190.00 USD | 0.00 USD | 0.00 USD | 477.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0759` | 2,130,000.00 USD | 2,130,000.00 USD | 40,360.00 USD | 66,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0760` | 38,770.00 USD | 38,770.00 USD | 0.00 USD | 0.00 USD | 585.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 40,420.00 USD | 40,420.00 USD | 0.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 41,560.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 56,810.00 USD | 56,810.00 USD | 0.00 USD | 14,830.00 USD | 424.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 404,480.00 USD | 404,480.00 USD | 211,600.00 USD | 37,120.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0765` | 3,400,000.00 USD | 3,400,000.00 USD | 772,480.00 USD | 496,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,350,000.00 USD | 1,350,000.00 USD | 471,060.00 USD | 475,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 1,990,000.00 USD | 1,990,000.00 USD | 153,710.00 USD | 322,470.00 USD | 159,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0767` | 4,670,000.00 USD | 4,670,000.00 USD | 1,180,000.00 USD | 90,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,900,000.00 USD | 2,900,000.00 USD | 224,320.00 USD | 93,770.00 USD | 592,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 4,090,000.00 USD | 4,090,000.00 USD | 375,270.00 USD | 462,440.00 USD | 351,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0769` | 5,940,000.00 USD | 5,940,000.00 USD | 760,570.00 USD | 84,300.00 USD | 429,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,290,000.00 USD | 5,290,000.00 USD | 412,020.00 USD | 301,010.00 USD | 486,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 6,440,000.00 USD | 6,440,000.00 USD | 441,280.00 USD | 459,510.00 USD | 250,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0771` | 8,430,000.00 USD | 8,430,000.00 USD | 888,600.00 USD | 798,440.00 USD | 794,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 8,010,000.00 USD | 8,010,000.00 USD | 480,450.00 USD | 327,770.00 USD | 767,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 8,820,000.00 USD | 8,820,000.00 USD | 190,960.00 USD | 368,960.00 USD | 243,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 69,030.00 USD | 347,590.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,220,000.00 USD | 9,220,000.00 USD | 118,800.00 USD | 246,740.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 9,750,000.00 USD | 9,750,000.00 USD | 288,570.00 USD | 180,890.00 USD | 60,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0775` | 10,060,000.00 USD | 10,060,000.00 USD | 779,670.00 USD | 375,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,390,000.00 USD | 10,390,000.00 USD | 284,830.00 USD | 214,460.00 USD | 145,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 11,300,000.00 USD | 11,300,000.00 USD | 401,010.00 USD | 342,630.00 USD | 165,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0777` | 10,620,000.00 USD | 10,620,000.00 USD | 265,980.00 USD | 286,560.00 USD | 693.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 12,160,000.00 USD | 12,160,000.00 USD | 116,640.00 USD | 340,450.00 USD | 399,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 12,920,000.00 USD | 12,920,000.00 USD | 345,840.00 USD | 210,420.00 USD | 204,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0779` | 11,630,000.00 USD | 11,630,000.00 USD | 270,450.00 USD | 301,690.00 USD | 438,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 13,250,000.00 USD | 13,250,000.00 USD | 212,580.00 USD | 78,920.00 USD | 38,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 13,620,000.00 USD | 13,620,000.00 USD | 151,030.00 USD | 193,800.00 USD | 22,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0781` | 11,960,000.00 USD | 11,960,000.00 USD | 186,410.00 USD | 142,450.00 USD | 4,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 13,850,000.00 USD | 13,850,000.00 USD | 70,430.00 USD | 86,550.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 14,290,000.00 USD | 14,290,000.00 USD | 52,750.00 USD | 214,890.00 USD | 174,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0783` | 12,450,000.00 USD | 12,450,000.00 USD | 15,350.00 USD | 285,880.00 USD | 193,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 14,880,000.00 USD | 14,880,000.00 USD | 388,250.00 USD | 122,020.00 USD | 72,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 15,390,000.00 USD | 15,390,000.00 USD | 216,540.00 USD | 171,160.00 USD | 121,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0785` | 13,070,000.00 USD | 13,070,000.00 USD | 197,420.00 USD | 141,600.00 USD | 278,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 16,250,000.00 USD | 16,250,000.00 USD | 352,080.00 USD | 218,550.00 USD | 294,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 17,480,000.00 USD | 17,480,000.00 USD | 379,110.00 USD | 464,730.00 USD | 382,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0787` | 14,670,000.00 USD | 14,670,000.00 USD | 437,500.00 USD | 346,050.00 USD | 812,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 354.19 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 18,030,000.00 USD | 18,030,000.00 USD | 168,080.00 USD | 262,350.00 USD | 121,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 18,680,000.00 USD | 18,680,000.00 USD | 312,410.00 USD | 233,260.00 USD | 104,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0789` | 15,480,000.00 USD | 15,480,000.00 USD | 301,760.00 USD | 259,180.00 USD | 249,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 18,950,000.00 USD | 18,950,000.00 USD | 153,960.00 USD | 87,240.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 19,410,000.00 USD | 19,410,000.00 USD | 203,370.00 USD | 133,580.00 USD | 124,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0791` | 16,040,000.00 USD | 16,040,000.00 USD | 476,430.00 USD | 81,300.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 19,770,000.00 USD | 19,770,000.00 USD | 224,560.00 USD | 57,840.00 USD | 75,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0793` | 5,230.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0793` | 19,780,000.00 USD | 19,780,000.00 USD | 5,950.00 USD | 0.00 USD | 421.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0793` | 16,380,000.00 USD | 16,380,000.00 USD | 27,550.00 USD | 61,220.00 USD | 246,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0794` | 3,550.00 USD | 9,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0794` | 20,130,000.00 USD | 20,130,000.00 USD | 158,580.00 USD | 96,210.00 USD | 102,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 104.72 USD | 9,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0795` | 20,370,000.00 USD | 20,370,000.00 USD | 92,560.00 USD | 45,380.00 USD | 101,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0795` | 17,050,000.00 USD | 17,050,000.00 USD | 206,900.00 USD | 0.00 USD | 469,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 855.64 USD | 10,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0796` | 20,590,000.00 USD | 20,590,000.00 USD | 199,280.00 USD | 12,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 20,920,000.00 USD | 20,920,000.00 USD | 206,810.00 USD | 89,760.00 USD | 40,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0797` | 18,020,000.00 USD | 18,020,000.00 USD | 640,790.00 USD | 203,560.00 USD | 119,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 21,050,000.00 USD | 21,050,000.00 USD | 58,670.00 USD | 63,560.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 21,340,000.00 USD | 21,340,000.00 USD | 64,660.00 USD | 191,860.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0799` | 18,790,000.00 USD | 18,790,000.00 USD | 561,590.00 USD | 130,870.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 21,500,000.00 USD | 21,500,000.00 USD | 48,550.00 USD | 9,760.00 USD | 94,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 21,520,000.00 USD | 21,520,000.00 USD | 25,740.00 USD | 0.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0801` | 18,980,000.00 USD | 18,980,000.00 USD | 85,040.00 USD | 0.00 USD | 104,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 21,550,000.00 USD | 21,550,000.00 USD | 25,490.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 21,660,000.00 USD | 21,660,000.00 USD | 24,020.00 USD | 43,340.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0803` | 19,020,000.00 USD | 19,020,000.00 USD | 42,220.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 21,670,000.00 USD | 21,670,000.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 826.14 USD | 10,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0805` | 21,840,000.00 USD | 21,840,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0805` | 19,350,000.00 USD | 19,350,000.00 USD | 228,320.00 USD | 43,910.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 22,100,000.00 USD | 22,100,000.00 USD | 28,730.00 USD | 21,040.00 USD | 215,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0806` | 213.40 USD | 11,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0807` | 22,510,000.00 USD | 22,510,000.00 USD | 228,350.00 USD | 143,670.00 USD | 32,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0807` | 20,790,000.00 USD | 20,790,000.00 USD | 217,720.00 USD | 934,840.00 USD | 294,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 23,160,000.00 USD | 23,160,000.00 USD | 150,860.00 USD | 116,140.00 USD | 381,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 23,500,000.00 USD | 23,500,000.00 USD | 109,380.00 USD | 220,760.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0809` | 22,570,000.00 USD | 22,570,000.00 USD | 9,880.00 USD | 1,760,000.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 23,950,000.00 USD | 23,950,000.00 USD | 192,870.00 USD | 127,690.00 USD | 132,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 24,200,000.00 USD | 24,200,000.00 USD | 100,060.00 USD | 139,750.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0811` | 23,430,000.00 USD | 23,430,000.00 USD | 131,030.00 USD | 730,620.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 24,480,000.00 USD | 24,480,000.00 USD | 135,690.00 USD | 102,020.00 USD | 38,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 24,660,000.00 USD | 24,660,000.00 USD | 39,090.00 USD | 29,030.00 USD | 109,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0813` | 24,500,000.00 USD | 24,500,000.00 USD | 517,320.00 USD | 548,390.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 24,960,000.00 USD | 24,960,000.00 USD | 43,650.00 USD | 108,690.00 USD | 148,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 25,080,000.00 USD | 25,080,000.00 USD | 20,890.00 USD | 6,740.00 USD | 94,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0815` | 26,110,000.00 USD | 26,110,000.00 USD | 671,840.00 USD | 643,990.00 USD | 300,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 25,780,000.00 USD | 25,780,000.00 USD | 323,740.00 USD | 194,310.00 USD | 177,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 26,320,000.00 USD | 26,320,000.00 USD | 280,410.00 USD | 134,560.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0817` | 28,680,000.00 USD | 28,680,000.00 USD | 1,200,000.00 USD | 745,850.00 USD | 614,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 26,980,000.00 USD | 26,980,000.00 USD | 234,840.00 USD | 161,260.00 USD | 268,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 11,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 27,580,000.00 USD | 27,580,000.00 USD | 156,470.00 USD | 312,480.00 USD | 128,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0819` | 30,790,000.00 USD | 30,790,000.00 USD | 672,340.00 USD | 512,490.00 USD | 929,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 28,120,000.00 USD | 28,120,000.00 USD | 46,550.00 USD | 172,050.00 USD | 319,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 28,400,000.00 USD | 28,400,000.00 USD | 145,950.00 USD | 48,110.00 USD | 84,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0821` | 33,150,000.00 USD | 33,150,000.00 USD | 1,210,000.00 USD | 760,670.00 USD | 390,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 28,960,000.00 USD | 28,960,000.00 USD | 249,310.00 USD | 151,600.00 USD | 157,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 29,310,000.00 USD | 29,310,000.00 USD | 267,050.00 USD | 72,540.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0823` | 34,920,000.00 USD | 34,920,000.00 USD | 884,810.00 USD | 520,900.00 USD | 366,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 29,870,000.00 USD | 29,870,000.00 USD | 168,680.00 USD | 204,930.00 USD | 190,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 30,120,000.00 USD | 30,120,000.00 USD | 102,430.00 USD | 125,690.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0825` | 36,500,000.00 USD | 36,500,000.00 USD | 761,460.00 USD | 514,320.00 USD | 307,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0825` | 217.85 USD | 11,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0826` | 30,550,000.00 USD | 30,550,000.00 USD | 131,950.00 USD | 125,260.00 USD | 171,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 30,640,000.00 USD | 30,640,000.00 USD | 13,110.00 USD | 62,900.00 USD | 16,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0827` | 37,650,000.00 USD | 37,650,000.00 USD | 658,340.00 USD | 220,660.00 USD | 271,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 30,970,000.00 USD | 30,970,000.00 USD | 189,510.00 USD | 75,940.00 USD | 65,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 218.81 USD | 11,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0829` | 31,250,000.00 USD | 31,250,000.00 USD | 182,550.00 USD | 89,690.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0829` | 38,690,000.00 USD | 38,690,000.00 USD | 645,990.00 USD | 177,740.00 USD | 214,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0829` | 219.07 USD | 12,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0830` | 31,390,000.00 USD | 31,390,000.00 USD | 54,060.00 USD | 37,820.00 USD | 42,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 31,470,000.00 USD | 31,470,000.00 USD | 22,160.00 USD | 16,920.00 USD | 45,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0831` | 39,590,000.00 USD | 39,590,000.00 USD | 452,190.00 USD | 160,720.00 USD | 288,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 15,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 31,850,000.00 USD | 31,850,000.00 USD | 184,130.00 USD | 93,160.00 USD | 100,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 32,270,000.00 USD | 32,270,000.00 USD | 125,800.00 USD | 111,030.00 USD | 181,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0833` | 40,810,000.00 USD | 40,810,000.00 USD | 524,880.00 USD | 414,820.00 USD | 276,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 32,650,000.00 USD | 32,650,000.00 USD | 123,760.00 USD | 118,950.00 USD | 143,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 33,020,000.00 USD | 33,020,000.00 USD | 109,250.00 USD | 188,990.00 USD | 64,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0835` | 41,970,000.00 USD | 41,970,000.00 USD | 365,460.00 USD | 261,800.00 USD | 536,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 33,280,000.00 USD | 33,280,000.00 USD | 44,050.00 USD | 74,690.00 USD | 148,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 15,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 33,510,000.00 USD | 33,510,000.00 USD | 130,410.00 USD | 29,090.00 USD | 62,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0837` | 42,770,000.00 USD | 42,770,000.00 USD | 453,970.00 USD | 227,430.00 USD | 115,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 33,780,000.00 USD | 33,780,000.00 USD | 150,900.00 USD | 81,260.00 USD | 42,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 221.45 USD | 17,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0839` | 43,250,000.00 USD | 43,250,000.00 USD | 321,350.00 USD | 128,090.00 USD | 36,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 221.54 USD | 17,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0840` | 122.71 USD | 18,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0841` | 43,520,000.00 USD | 43,520,000.00 USD | 205,170.00 USD | 0.00 USD | 64,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 264.21 USD | 18,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0843` | 44,020,000.00 USD | 44,020,000.00 USD | 337,540.00 USD | 77,640.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0845` | 44,490,000.00 USD | 44,490,000.00 USD | 234,950.00 USD | 95,020.00 USD | 138,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 223.39 USD | 18,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0847` | 45,000,000.00 USD | 45,000,000.00 USD | 244,090.00 USD | 190,180.00 USD | 77,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 426.71 USD | 18,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0849` | 45,730,000.00 USD | 45,730,000.00 USD | 310,690.00 USD | 205,870.00 USD | 208,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 46,060,000.00 USD | 46,060,000.00 USD | 87,360.00 USD | 53,240.00 USD | 186,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0853` | 224.97 USD | 19,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 19,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,250.00 USD | 23,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0868` | 155.98 USD | 23,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 23,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0877` | 231.57 USD | 24,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 24,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 24,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 25,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0901` | 237.64 USD | 25,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 32,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 33,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 38,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 39,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0925` | 901.07 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 40,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0934` | 4,200.00 USD | 44,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 84,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0948` | 47,380.00 USD | 132,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 156,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 761.26 USD | 157,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0955` | 194.44 USD | 157,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 158,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0970` | 1,540.00 USD | 159,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 159,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 160,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0987` | 2,880.00 USD | 163,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 202.21 USD | 163,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 170,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 173,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 174,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1053` | 3,270.00 USD | 177,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 183,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 184,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 187,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1106` | 1,840.00 USD | 189,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 189,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1137` | 147.86 USD | 189,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1152` | 147.05 USD | 189,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1159` | 837.04 USD | 190,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 637.53 USD | 191,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1252` | 120.77 USD | 191,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 191,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 191,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 194,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 45,230.00 USD | 239,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1326` | 5,930.00 USD | 245,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 245,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1389` | 1,210.00 USD | 246,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 247,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,090.00 USD | 248,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1412` | 22,910.00 USD | 271,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1426` | 1,800.00 USD | 273,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 274,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1439` | 1,840.00 USD | 276,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 276,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1442` | 13,770.00 USD | 290,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 292,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 31,970.00 USD | 324,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1446` | 144.55 USD | 324,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1459` | 1,930.00 USD | 326,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,110.00 USD | 334,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1489` | 446.85 USD | 334,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1497` | 24,060.00 USD | 358,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1499` | 3,130,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0152` | 16,530,000.00 USD | 0.00 USD | 1,450.00 USD | `-79.94%` | `95,954.00` |
| `Live` | `Long` | `0.0160` | 16,530,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.75%` | `244,573.00` |
| `Live` | `Long` | `0.0162` | 16,520,000.00 USD | 0.00 USD | 1,800.00 USD | `-78.61%` | `111,254.00` |
| `Live` | `Long` | `0.0164` | 16,520,000.00 USD | 0.00 USD | 407.02 USD | `-78.22%` | `24,743.00` |
| `Live` | `Long` | `0.0167` | 16,520,000.00 USD | 0.00 USD | 5,320.00 USD | `-77.95%` | `319,394.00` |
| `Live` | `Long` | `0.0168` | 16,520,000.00 USD | 0.00 USD | 2,570.00 USD | `-77.82%` | `153,201.00` |
| `Live` | `Long` | `0.0170` | 16,510,000.00 USD | 0.00 USD | 204.07 USD | `-77.42%` | `11,969.00` |
| `Live` | `Long` | `0.0175` | 16,510,000.00 USD | 0.00 USD | 1,040.00 USD | `-76.89%` | `59,317.00` |
| `Live` | `Long` | `0.0175` | 16,510,000.00 USD | 0.00 USD | 1,050.00 USD | `-76.76%` | `60,000.00` |
| `Live` | `Long` | `0.0192` | 16,510,000.00 USD | 0.00 USD | 1,440.00 USD | `-74.51%` | `75,012.00` |
| `Live` | `Long` | `0.0203` | 16,510,000.00 USD | 0.00 USD | 648.00 USD | `-73.19%` | `32,000.00` |
| `Live` | `Long` | `0.0215` | 16,510,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.46%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,490,000.00 USD | 0.00 USD | 541.25 USD | `-71.33%` | `25,000.00` |
| `Live` | `Long` | `0.0222` | 16,490,000.00 USD | 0.00 USD | 138.08 USD | `-70.54%` | `6,206.00` |
| `Live` | `Long` | `0.0226` | 16,490,000.00 USD | 0.00 USD | 884.46 USD | `-70.01%` | `39,049.00` |
| `Live` | `Long` | `0.0232` | 16,490,000.00 USD | 0.00 USD | 11,580.00 USD | `-69.35%` | `500,000.00` |
| `Live` | `Long` | `0.0236` | 16,480,000.00 USD | 0.00 USD | 142.50 USD | `-68.82%` | `6,051.00` |
| `Live` | `Long` | `0.0249` | 16,480,000.00 USD | 0.00 USD | 394.09 USD | `-66.96%` | `15,795.00` |
| `Live` | `Long` | `0.0253` | 16,480,000.00 USD | 0.00 USD | 22,570.00 USD | `-66.57%` | `893,720.00` |
| `Live` | `Long` | `0.0254` | 16,450,000.00 USD | 0.00 USD | 4,020.00 USD | `-66.43%` | `158,606.00` |
| `Live` | `Long` | `0.0256` | 16,450,000.00 USD | 0.00 USD | 760.04 USD | `-66.04%` | `29,631.00` |
| `Live` | `Long` | `0.0265` | 16,450,000.00 USD | 0.00 USD | 416.51 USD | `-64.98%` | `15,747.00` |
| `Live` | `Long` | `0.0266` | 16,450,000.00 USD | 0.00 USD | 531.00 USD | `-64.84%` | `20,000.00` |
| `Live` | `Long` | `0.0272` | 16,450,000.00 USD | 0.00 USD | 40,570.00 USD | `-63.92%` | `1,488,849.00` |
| `Live` | `Long` | `0.0279` | 16,410,000.00 USD | 0.00 USD | 1,730.00 USD | `-62.99%` | `61,775.00` |
| `Live` | `Long` | `0.0289` | 16,410,000.00 USD | 0.00 USD | 498.04 USD | `-61.80%` | `17,263.00` |
| `Live` | `Long` | `0.0297` | 16,410,000.00 USD | 0.00 USD | 158.98 USD | `-60.61%` | `5,344.00` |
| `Live` | `Long` | `0.0300` | 16,410,000.00 USD | 0.00 USD | 967.33 USD | `-60.34%` | `32,298.00` |
| `Live` | `Long` | `0.0306` | 16,400,000.00 USD | 0.00 USD | 137.41 USD | `-59.55%` | `4,498.00` |
| `Live` | `Long` | `0.0308` | 16,400,000.00 USD | 0.00 USD | 266.67 USD | `-59.15%` | `8,644.00` |
| `Live` | `Long` | `0.0321` | 16,400,000.00 USD | 0.00 USD | 6,040.00 USD | `-57.43%` | `187,979.00` |
| `Live` | `Long` | `0.0326` | 16,400,000.00 USD | 0.00 USD | 458.31 USD | `-56.77%` | `14,037.00` |
| `Live` | `Long` | `0.0330` | 16,400,000.00 USD | 0.00 USD | 133.94 USD | `-56.37%` | `4,065.00` |
| `Live` | `Long` | `0.0331` | 16,400,000.00 USD | 0.00 USD | 760.15 USD | `-56.24%` | `23,000.00` |
| `Live` | `Long` | `0.0336` | 16,400,000.00 USD | 0.00 USD | 393.23 USD | `-55.44%` | `11,686.00` |
| `Live` | `Long` | `0.0345` | 16,400,000.00 USD | 0.00 USD | 4,630.00 USD | `-54.38%` | `134,443.00` |
| `Live` | `Long` | `0.0350` | 16,390,000.00 USD | 0.00 USD | 13,620.00 USD | `-53.72%` | `389,633.00` |
| `Live` | `Long` | `0.0358` | 16,380,000.00 USD | 0.00 USD | 214.53 USD | `-52.53%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,380,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.40%` | `233,408.00` |
| `Live` | `Long` | `0.0369` | 16,370,000.00 USD | 0.00 USD | 35,100.00 USD | `-51.07%` | `950,000.00` |
| `Live` | `Long` | `0.0376` | 16,330,000.00 USD | 0.00 USD | 169.54 USD | `-50.28%` | `4,515.00` |
| `Live` | `Long` | `0.0377` | 16,330,000.00 USD | 0.00 USD | 1,790.00 USD | `-50.15%` | `47,501.00` |
| `Live` | `Long` | `0.0381` | 16,330,000.00 USD | 0.00 USD | 1,600.00 USD | `-49.62%` | `41,929.00` |
| `Live` | `Long` | `0.0386` | 16,330,000.00 USD | 0.00 USD | 121.74 USD | `-48.95%` | `3,158.00` |
| `Live` | `Long` | `0.0386` | 16,330,000.00 USD | 0.00 USD | 181.66 USD | `-48.82%` | `4,700.00` |
| `Live` | `Long` | `0.0387` | 16,330,000.00 USD | 0.00 USD | 207.27 USD | `-48.69%` | `5,349.00` |
| `Live` | `Long` | `0.0389` | 16,330,000.00 USD | 0.00 USD | 201.32 USD | `-48.56%` | `5,182.00` |
| `Live` | `Long` | `0.0393` | 16,330,000.00 USD | 0.00 USD | 6,110.00 USD | `-48.03%` | `155,633.00` |
| `Live` | `Long` | `0.0396` | 16,320,000.00 USD | 0.00 USD | 1,480.00 USD | `-47.50%` | `37,344.00` |
| `Live` | `Long` | `0.0399` | 16,320,000.00 USD | 0.00 USD | 103.31 USD | `-47.10%` | `2,586.00` |
| `Live` | `Long` | `0.0404` | 16,320,000.00 USD | 0.00 USD | 56,970.00 USD | `-46.44%` | `1,408,334.00` |
| `Live` | `Long` | `0.0408` | 16,270,000.00 USD | 0.00 USD | 21,880.00 USD | `-46.04%` | `536,940.00` |
| `Live` | `Long` | `0.0415` | 16,240,000.00 USD | 0.00 USD | 6,400.00 USD | `-45.11%` | `154,349.00` |
| `Live` | `Long` | `0.0415` | 16,240,000.00 USD | 0.00 USD | 1,030.00 USD | `-44.98%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 16,240,000.00 USD | 0.00 USD | 596.82 USD | `-44.32%` | `14,193.00` |
| `Live` | `Long` | `0.0423` | 16,240,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.05%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,230,000.00 USD | 0.00 USD | 267.52 USD | `-43.92%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,230,000.00 USD | 0.00 USD | 455.06 USD | `-43.79%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,230,000.00 USD | 0.00 USD | 883.34 USD | `-43.66%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,230,000.00 USD | 0.00 USD | 2,960.00 USD | `-43.52%` | `69,502.00` |
| `Live` | `Long` | `0.0428` | 16,230,000.00 USD | 0.00 USD | 49,010.00 USD | `-43.39%` | `1,146,341.00` |
| `Live` | `Long` | `0.0430` | 16,180,000.00 USD | 0.00 USD | 859.00 USD | `-43.13%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,180,000.00 USD | 0.00 USD | 5,030.00 USD | `-42.86%` | `116,653.00` |
| `Live` | `Long` | `0.0432` | 16,170,000.00 USD | 0.00 USD | 22,660.00 USD | `-42.73%` | `523,977.00` |
| `Live` | `Long` | `0.0433` | 16,150,000.00 USD | 0.00 USD | 2,450.00 USD | `-42.60%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 16,150,000.00 USD | 0.00 USD | 113,160.00 USD | `-42.20%` | `2,592,536.00` |
| `Live` | `Long` | `0.0439` | 16,040,000.00 USD | 0.00 USD | 2,620.00 USD | `-41.94%` | `59,668.00` |
| `Live` | `Long` | `0.0440` | 16,030,000.00 USD | 0.00 USD | 750.58 USD | `-41.80%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,030,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.67%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,030,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.27%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 15,930,000.00 USD | 0.00 USD | 444.76 USD | `-40.88%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 15,930,000.00 USD | 0.00 USD | 248.63 USD | `-40.74%` | `5,556.00` |
| `Live` | `Long` | `0.0449` | 15,930,000.00 USD | 0.00 USD | 772.50 USD | `-40.61%` | `17,224.00` |
| `Live` | `Long` | `0.0449` | 15,930,000.00 USD | 0.00 USD | 810.81 USD | `-40.48%` | `18,038.00` |
| `Live` | `Long` | `0.0452` | 15,930,000.00 USD | 0.00 USD | 893.78 USD | `-40.08%` | `19,752.00` |
| `Live` | `Long` | `0.0454` | 15,930,000.00 USD | 0.00 USD | 438.22 USD | `-39.95%` | `9,663.00` |
| `Live` | `Long` | `0.0454` | 15,930,000.00 USD | 0.00 USD | 2,170.00 USD | `-39.82%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 15,920,000.00 USD | 0.00 USD | 33,660.00 USD | `-39.68%` | `738,931.00` |
| `Live` | `Long` | `0.0457` | 15,890,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.42%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 15,890,000.00 USD | 0.00 USD | 689.25 USD | `-39.16%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 15,880,000.00 USD | 0.00 USD | 4,500.00 USD | `-39.02%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 15,880,000.00 USD | 0.00 USD | 114.36 USD | `-38.89%` | `2,478.00` |
| `Live` | `Long` | `0.0462` | 15,880,000.00 USD | 0.00 USD | 1,250.00 USD | `-38.76%` | `27,061.00` |
| `Live` | `Long` | `0.0464` | 15,880,000.00 USD | 0.00 USD | 11,970.00 USD | `-38.63%` | `258,208.00` |
| `Live` | `Long` | `0.0464` | 15,870,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.49%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 15,850,000.00 USD | 0.00 USD | 109.49 USD | `-38.23%` | `2,347.00` |
| `Live` | `Long` | `0.0473` | 15,850,000.00 USD | 0.00 USD | 2,870.00 USD | `-37.43%` | `60,799.00` |
| `Live` | `Long` | `0.0474` | 15,850,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.30%` | `29,884.00` |
| `Live` | `Long` | `0.0476` | 15,850,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-36.90%` | `23,493,307.00` |
| `Live` | `Long` | `0.0478` | 14,730,000.00 USD | 0.00 USD | 258.33 USD | `-36.77%` | `5,410.00` |
| `Live` | `Long` | `0.0481` | 14,730,000.00 USD | 0.00 USD | 58,890.00 USD | `-36.24%` | `1,223,127.00` |
| `Live` | `Long` | `0.0483` | 14,670,000.00 USD | 0.00 USD | 1,780.00 USD | `-35.98%` | `36,742.00` |
| `Live` | `Long` | `0.0485` | 14,670,000.00 USD | 0.00 USD | 1,480.00 USD | `-35.84%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 14,660,000.00 USD | 0.00 USD | 2,430.00 USD | `-35.71%` | `50,080.00` |
| `Live` | `Long` | `0.0488` | 14,660,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.32%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,660,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.18%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,650,000.00 USD | 0.00 USD | 1,080.00 USD | `-35.05%` | `21,989.00` |
| `Live` | `Long` | `0.0495` | 14,650,000.00 USD | 0.00 USD | 4,800.00 USD | `-34.39%` | `96,957.00` |
| `Live` | `Long` | `0.0498` | 14,650,000.00 USD | 0.00 USD | 253.82 USD | `-34.12%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,650,000.00 USD | 0.00 USD | 501.50 USD | `-33.73%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,650,000.00 USD | 0.00 USD | 106.23 USD | `-33.46%` | `2,114.00` |
| `Live` | `Long` | `0.0503` | 14,650,000.00 USD | 0.00 USD | 5,310.00 USD | `-33.33%` | `105,458.00` |
| `Live` | `Long` | `0.0505` | 14,640,000.00 USD | 0.00 USD | 334.89 USD | `-33.20%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,640,000.00 USD | 0.00 USD | 1,040.00 USD | `-32.93%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,640,000.00 USD | 0.00 USD | 5,350.00 USD | `-32.80%` | `105,363.00` |
| `Live` | `Long` | `0.0508` | 14,640,000.00 USD | 0.00 USD | 254.25 USD | `-32.67%` | `5,000.00` |
| `Live` | `Long` | `0.0510` | 14,640,000.00 USD | 0.00 USD | 535.43 USD | `-32.53%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,630,000.00 USD | 0.00 USD | 566.65 USD | `-32.40%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,630,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.27%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,620,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.14%` | `29,005.00` |
| `Live` | `Long` | `0.0515` | 14,620,000.00 USD | 0.00 USD | 4,950.00 USD | `-31.74%` | `95,997.00` |
| `Live` | `Long` | `0.0517` | 14,620,000.00 USD | 0.00 USD | 314.91 USD | `-31.61%` | `6,097.00` |
| `Live` | `Long` | `0.0517` | 14,620,000.00 USD | 0.00 USD | 3,530.00 USD | `-31.48%` | `68,212.00` |
| `Live` | `Long` | `0.0519` | 14,610,000.00 USD | 0.00 USD | 6,970.00 USD | `-31.34%` | `134,439.00` |
| `Live` | `Long` | `0.0520` | 14,610,000.00 USD | 0.00 USD | 277.72 USD | `-31.21%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,610,000.00 USD | 0.00 USD | 4,420.00 USD | `-31.08%` | `84,852.00` |
| `Live` | `Long` | `0.0522` | 14,600,000.00 USD | 0.00 USD | 275,090.00 USD | `-30.81%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,330,000.00 USD | 0.00 USD | 2,390.00 USD | `-30.55%` | `45,590.00` |
| `Live` | `Long` | `0.0525` | 14,320,000.00 USD | 0.00 USD | 4,790.00 USD | `-30.42%` | `91,115.00` |
| `Live` | `Long` | `0.0527` | 14,320,000.00 USD | 0.00 USD | 44,830.00 USD | `-30.28%` | `851,411.00` |
| `Live` | `Long` | `0.0527` | 14,270,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.15%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,270,000.00 USD | 0.00 USD | 673.52 USD | `-30.02%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,270,000.00 USD | 0.00 USD | 181,920.00 USD | `-29.89%` | `3,435,663.00` |
| `Live` | `Long` | `0.0530` | 14,090,000.00 USD | 0.00 USD | 27,810.00 USD | `-29.75%` | `524,263.00` |
| `Live` | `Long` | `0.0532` | 14,060,000.00 USD | 0.00 USD | 14,030.00 USD | `-29.62%` | `263,990.00` |
| `Live` | `Long` | `0.0532` | 14,050,000.00 USD | 0.00 USD | 6,010.00 USD | `-29.49%` | `112,948.00` |
| `Live` | `Long` | `0.0534` | 14,040,000.00 USD | 0.00 USD | 42,580.00 USD | `-29.36%` | `798,082.00` |
| `Live` | `Long` | `0.0534` | 14,000,000.00 USD | 0.00 USD | 800.95 USD | `-29.22%` | `14,985.00` |
| `Live` | `Long` | `0.0536` | 14,000,000.00 USD | 0.00 USD | 1,040.00 USD | `-29.09%` | `19,489.00` |
| `Live` | `Long` | `0.0537` | 14,000,000.00 USD | 0.00 USD | 223.18 USD | `-28.96%` | `4,160.00` |
| `Live` | `Long` | `0.0539` | 14,000,000.00 USD | 0.00 USD | 258.10 USD | `-28.69%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 14,000,000.00 USD | 0.00 USD | 5,290.00 USD | `-28.56%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,990,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.43%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,990,000.00 USD | 0.00 USD | 3,030.00 USD | `-28.30%` | `55,906.00` |
| `Live` | `Long` | `0.0542` | 13,990,000.00 USD | 0.00 USD | 95,630.00 USD | `-28.16%` | `1,762,722.00` |
| `Live` | `Long` | `0.0544` | 13,890,000.00 USD | 0.00 USD | 903.30 USD | `-28.03%` | `16,620.00` |
| `Live` | `Long` | `0.0546` | 13,890,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.64%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,890,000.00 USD | 0.00 USD | 892.81 USD | `-27.50%` | `16,307.00` |
| `Live` | `Long` | `0.0549` | 13,890,000.00 USD | 0.00 USD | 23,860.00 USD | `-27.37%` | `435,000.00` |
| `Live` | `Long` | `0.0551` | 13,860,000.00 USD | 0.00 USD | 1,760.00 USD | `-26.97%` | `31,888.00` |
| `Live` | `Long` | `0.0554` | 13,860,000.00 USD | 0.00 USD | 2,380.00 USD | `-26.71%` | `43,069.00` |
| `Live` | `Long` | `0.0554` | 13,860,000.00 USD | 0.00 USD | 347.95 USD | `-26.58%` | `6,275.00` |
| `Live` | `Long` | `0.0556` | 13,860,000.00 USD | 0.00 USD | 1,100.00 USD | `-26.44%` | `19,864.00` |
| `Live` | `Long` | `0.0558` | 13,860,000.00 USD | 0.00 USD | 4,010.00 USD | `-26.05%` | `71,715.00` |
| `Live` | `Long` | `0.0561` | 13,850,000.00 USD | 0.00 USD | 8,410.00 USD | `-25.78%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 13,840,000.00 USD | 0.00 USD | 144.08 USD | `-25.65%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,840,000.00 USD | 0.00 USD | 41,360.00 USD | `-25.52%` | `735,300.00` |
| `Live` | `Long` | `0.0563` | 13,800,000.00 USD | 0.00 USD | 351.85 USD | `-25.38%` | `6,244.00` |
| `Live` | `Long` | `0.0568` | 13,800,000.00 USD | 0.00 USD | 568.50 USD | `-24.72%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,800,000.00 USD | 0.00 USD | 315.67 USD | `-24.59%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,800,000.00 USD | 0.00 USD | 8,350.00 USD | `-24.46%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,790,000.00 USD | 0.00 USD | 814.04 USD | `-24.32%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,790,000.00 USD | 0.00 USD | 4,060.00 USD | `-24.06%` | `70,727.00` |
| `Live` | `Long` | `0.0575` | 13,790,000.00 USD | 0.00 USD | 181.77 USD | `-23.93%` | `3,164.00` |
| `Live` | `Long` | `0.0575` | 13,790,000.00 USD | 0.00 USD | 3,960.00 USD | `-23.80%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 13,780,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.66%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,770,000.00 USD | 0.00 USD | 14,210.00 USD | `-23.53%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,760,000.00 USD | 0.00 USD | 3,760.00 USD | `-23.40%` | `65,000.00` |
| `Live` | `Long` | `0.0580` | 13,750,000.00 USD | 0.00 USD | 622.09 USD | `-23.27%` | `10,735.00` |
| `Live` | `Long` | `0.0580` | 13,750,000.00 USD | 0.00 USD | 431.14 USD | `-23.13%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,750,000.00 USD | 0.00 USD | 447.17 USD | `-23.00%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,750,000.00 USD | 0.00 USD | 582.50 USD | `-22.87%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,750,000.00 USD | 0.00 USD | 17,220.00 USD | `-22.74%` | `295,079.00` |
| `Live` | `Long` | `0.0585` | 13,740,000.00 USD | 0.00 USD | 172.78 USD | `-22.47%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,740,000.00 USD | 0.00 USD | 47,390.00 USD | `-22.34%` | `808,039.00` |
| `Live` | `Long` | `0.0587` | 13,690,000.00 USD | 0.00 USD | 4,050.00 USD | `-22.21%` | `68,967.00` |
| `Live` | `Long` | `0.0590` | 13,680,000.00 USD | 0.00 USD | 212.22 USD | `-21.94%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,680,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.68%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,660,000.00 USD | 0.00 USD | 546.26 USD | `-21.41%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,660,000.00 USD | 0.00 USD | 4,140.00 USD | `-21.28%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,650,000.00 USD | 0.00 USD | 3,680.00 USD | `-21.15%` | `61,718.00` |
| `Live` | `Long` | `0.0597` | 13,650,000.00 USD | 0.00 USD | 4,970.00 USD | `-20.88%` | `83,140.00` |
| `Live` | `Long` | `0.0599` | 13,640,000.00 USD | 0.00 USD | 2,110.00 USD | `-20.75%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 13,640,000.00 USD | 0.00 USD | 3,580.00 USD | `-20.62%` | `59,709.00` |
| `Live` | `Long` | `0.0600` | 13,640,000.00 USD | 0.00 USD | 7,210.00 USD | `-20.48%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,630,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.35%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 13,620,000.00 USD | 0.00 USD | 2,500.00 USD | `-20.09%` | `41,451.00` |
| `Live` | `Long` | `0.0604` | 13,620,000.00 USD | 0.00 USD | 5,970,000.00 USD | `-19.95%` | `98,680,453.00` |
| `Live` | `Long` | `0.0605` | 7,650,000.00 USD | 0.00 USD | 35,530.00 USD | `-19.82%` | `586,817.00` |
| `Live` | `Long` | `0.0607` | 7,620,000.00 USD | 0.00 USD | 357,770.00 USD | `-19.69%` | `5,898,919.00` |
| `Live` | `Long` | `0.0607` | 7,260,000.00 USD | 0.00 USD | 17,110.00 USD | `-19.56%` | `281,570.00` |
| `Live` | `Long` | `0.0609` | 7,240,000.00 USD | 0.00 USD | 1,940.00 USD | `-19.43%` | `31,875.00` |
| `Live` | `Long` | `0.0609` | 7,240,000.00 USD | 0.00 USD | 5,110.00 USD | `-19.29%` | `83,914.00` |
| `Live` | `Long` | `0.0612` | 7,240,000.00 USD | 0.00 USD | 629.72 USD | `-19.03%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,240,000.00 USD | 0.00 USD | 709.03 USD | `-18.90%` | `11,576.00` |
| `Live` | `Long` | `0.0614` | 7,240,000.00 USD | 0.00 USD | 655.16 USD | `-18.76%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,230,000.00 USD | 0.00 USD | 1,890.00 USD | `-18.50%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,230,000.00 USD | 0.00 USD | 11,100.00 USD | `-18.37%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 7,220,000.00 USD | 0.00 USD | 158.08 USD | `-18.23%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,220,000.00 USD | 0.00 USD | 27,580.00 USD | `-17.84%` | `444,421.00` |
| `Live` | `Long` | `0.0621` | 7,190,000.00 USD | 0.00 USD | 345.86 USD | `-17.70%` | `5,565.00` |
| `Live` | `Long` | `0.0624` | 7,190,000.00 USD | 0.00 USD | 2,330.00 USD | `-17.44%` | `37,317.00` |
| `Live` | `Long` | `0.0624` | 7,190,000.00 USD | 0.00 USD | 43,800.00 USD | `-17.31%` | `701,306.00` |
| `Live` | `Long` | `0.0625` | 7,150,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.17%` | `17,626,455.00` |
| `Live` | `Long` | `0.0626` | 6,050,000.00 USD | 0.00 USD | 1,120.00 USD | `-17.04%` | `17,888.00` |
| `Live` | `Long` | `0.0628` | 6,040,000.00 USD | 0.00 USD | 461.78 USD | `-16.91%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,040,000.00 USD | 0.00 USD | 6,400.00 USD | `-16.78%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,040,000.00 USD | 0.00 USD | 2,430.00 USD | `-16.51%` | `38,603.00` |
| `Live` | `Long` | `0.0631` | 6,030,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-16.38%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.25%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,970,000.00 USD | 0.00 USD | 12,850.00 USD | `-16.11%` | `202,898.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-15.98%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-15.85%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 633.38 USD | `-15.72%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 4,950,000.00 USD | 0.00 USD | 9,740.00 USD | `-15.59%` | `152,837.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 23,220.00 USD | `-15.45%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,920,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.32%` | `31,194.00` |
| `Live` | `Long` | `0.0640` | 4,920,000.00 USD | 0.00 USD | 150.01 USD | `-15.19%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,920,000.00 USD | 0.00 USD | 3,270.00 USD | `-15.06%` | `50,913.00` |
| `Live` | `Long` | `0.0643` | 4,910,000.00 USD | 0.00 USD | 1,330.00 USD | `-14.92%` | `20,766.00` |
| `Live` | `Long` | `0.0644` | 4,910,000.00 USD | 0.00 USD | 76,280.00 USD | `-14.79%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,840,000.00 USD | 0.00 USD | 27,180.00 USD | `-14.66%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,810,000.00 USD | 0.00 USD | 631.94 USD | `-14.53%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,810,000.00 USD | 0.00 USD | 162,920.00 USD | `-14.26%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,650,000.00 USD | 0.00 USD | 8,800.00 USD | `-14.13%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,640,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.00%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,610,000.00 USD | 0.00 USD | 2,380.00 USD | `-13.73%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,610,000.00 USD | 0.00 USD | 13,770.00 USD | `-13.60%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,600,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.20%` | `118,852.00` |
| `Live` | `Long` | `0.0657` | 4,590,000.00 USD | 0.00 USD | 14,160.00 USD | `-13.07%` | `215,665.00` |
| `Live` | `Long` | `0.0658` | 4,580,000.00 USD | 0.00 USD | 66,820.00 USD | `-12.94%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,510,000.00 USD | 0.00 USD | 14,600.00 USD | `-12.80%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 9,600.00 USD | `-12.67%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,490,000.00 USD | 0.00 USD | 2,280.00 USD | `-12.41%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,480,000.00 USD | 0.00 USD | 13,740.00 USD | `-12.27%` | `207,423.00` |
| `Live` | `Long` | `0.0664` | 4,470,000.00 USD | 0.00 USD | 17,410.00 USD | `-12.14%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,450,000.00 USD | 0.00 USD | 1,270.00 USD | `-12.01%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,450,000.00 USD | 0.00 USD | 34,860.00 USD | `-11.75%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,420,000.00 USD | 0.00 USD | 8,880.00 USD | `-11.61%` | `133,009.00` |
| `Live` | `Long` | `0.0669` | 4,410,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-11.48%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-11.35%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,260,000.00 USD | 0.00 USD | 6,120.00 USD | `-11.22%` | `91,206.00` |
| `Live` | `Long` | `0.0672` | 3,250,000.00 USD | 0.00 USD | 2,830.00 USD | `-11.08%` | `42,083.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,220.00 USD | `-10.95%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 4,830.00 USD | `-10.82%` | `71,711.00` |
| `Live` | `Long` | `0.0674` | 3,240,000.00 USD | 0.00 USD | 1,780.00 USD | `-10.69%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,230,000.00 USD | 0.00 USD | 112,780.00 USD | `-10.55%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,120,000.00 USD | 0.00 USD | 12,610.00 USD | `-10.42%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,110,000.00 USD | 0.00 USD | 4,290.00 USD | `-10.29%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 34,090.00 USD | `-10.16%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,070,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.02%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,050,000.00 USD | 0.00 USD | 667.50 USD | `-9.89%` | `9,809.00` |
| `Live` | `Long` | `0.0683` | 3,050,000.00 USD | 0.00 USD | 55,770.00 USD | `-9.63%` | `817,124.00` |
| `Live` | `Long` | `0.0684` | 3,000,000.00 USD | 0.00 USD | 79,490.00 USD | `-9.36%` | `1,161,220.00` |
| `Live` | `Long` | `0.0685` | 2,920,000.00 USD | 0.00 USD | 8,890.00 USD | `-9.23%` | `129,646.00` |
| `Live` | `Long` | `0.0687` | 2,910,000.00 USD | 0.00 USD | 4,840.00 USD | `-9.10%` | `70,447.00` |
| `Live` | `Long` | `0.0688` | 2,900,000.00 USD | 0.00 USD | 16,210.00 USD | `-8.96%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,890,000.00 USD | 0.00 USD | 38,040.00 USD | `-8.83%` | `552,461.00` |
| `Live` | `Long` | `0.0689` | 2,850,000.00 USD | 0.00 USD | 508,320.00 USD | `-8.70%` | `7,372,312.00` |
| `Live` | `Long` | `0.0691` | 2,340,000.00 USD | 0.00 USD | 10,030.00 USD | `-8.57%` | `145,229.00` |
| `Live` | `Long` | `0.0692` | 2,330,000.00 USD | 0.00 USD | 13,510.00 USD | `-8.43%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,320,000.00 USD | 0.00 USD | 9,140.00 USD | `-8.30%` | `131,951.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.17%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,310,000.00 USD | 0.00 USD | 4,980.00 USD | `-8.04%` | `71,770.00` |
| `Live` | `Long` | `0.0697` | 2,300,000.00 USD | 0.00 USD | 4,950.00 USD | `-7.77%` | `71,115.00` |
| `Live` | `Long` | `0.0698` | 2,300,000.00 USD | 0.00 USD | 6,970.00 USD | `-7.64%` | `99,923.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 2,910.00 USD | `-7.51%` | `41,684.00` |
| `Live` | `Long` | `0.0699` | 2,290,000.00 USD | 0.00 USD | 1,310.00 USD | `-7.38%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,290,000.00 USD | 0.00 USD | 9,620.00 USD | `-7.24%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,280,000.00 USD | 0.00 USD | 8,180.00 USD | `-7.11%` | `116,620.00` |
| `Live` | `Long` | `0.0703` | 2,270,000.00 USD | 0.00 USD | 4,300.00 USD | `-6.98%` | `61,162.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 3,790.00 USD | `-6.85%` | `53,920.00` |
| `Live` | `Long` | `0.0704` | 2,260,000.00 USD | 0.00 USD | 780.37 USD | `-6.71%` | `11,077.00` |
| `Live` | `Long` | `0.0707` | 2,260,000.00 USD | 0.00 USD | 608.86 USD | `-6.45%` | `8,618.00` |
| `Live` | `Long` | `0.0707` | 2,260,000.00 USD | 0.00 USD | 94,410.00 USD | `-6.32%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,160,000.00 USD | 0.00 USD | 821.60 USD | `-6.05%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,160,000.00 USD | 0.00 USD | 4,720.00 USD | `-5.92%` | `66,436.00` |
| `Live` | `Long` | `0.0712` | 2,160,000.00 USD | 0.00 USD | 1,860.00 USD | `-5.79%` | `26,118.00` |
| `Live` | `Long` | `0.0712` | 2,160,000.00 USD | 0.00 USD | 802.06 USD | `-5.65%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,160,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-5.52%` | `24,500,580.00` |
| `Live` | `Long` | `0.0714` | 408,170.00 USD | 0.00 USD | 13,270.00 USD | `-5.39%` | `185,735.00` |
| `Live` | `Long` | `0.0716` | 394,900.00 USD | 0.00 USD | 8,120.00 USD | `-5.26%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 386,790.00 USD | 0.00 USD | 3,840.00 USD | `-5.12%` | `53,537.00` |
| `Live` | `Long` | `0.0717` | 382,950.00 USD | 0.00 USD | 48,180.00 USD | `-4.99%` | `671,440.00` |
| `Live` | `Long` | `0.0718` | 334,780.00 USD | 0.00 USD | 1,090.00 USD | `-4.86%` | `15,170.00` |
| `Live` | `Long` | `0.0720` | 333,690.00 USD | 0.00 USD | 1,900.00 USD | `-4.73%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 331,790.00 USD | 0.00 USD | 5,090.00 USD | `-4.59%` | `70,701.00` |
| `Live` | `Long` | `0.0722` | 326,700.00 USD | 0.00 USD | 613.35 USD | `-4.46%` | `8,501.00` |
| `Live` | `Long` | `0.0722` | 326,080.00 USD | 0.00 USD | 38,340.00 USD | `-4.33%` | `530,618.00` |
| `Live` | `Long` | `0.0723` | 287,750.00 USD | 0.00 USD | 286,760.00 USD | `-4.20%` | `3,963,544.00` |
| `Live` | `Long` | `0.0725` | 984.89 USD | 0.00 USD | 984.89 USD | `-4.07%` | `13,594.00` |
| `Live` | `Short` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | `+2.69%` | `3,107.00` |
| `Live` | `Short` | `0.0788` | 354.19 USD | 113.24 USD | 0.00 USD | `+4.28%` | `1,438.00` |
| `Live` | `Short` | `0.0793` | 5,580.00 USD | 5,230.00 USD | 0.00 USD | `+4.94%` | `65,988.00` |
| `Live` | `Short` | `0.0794` | 9,130.00 USD | 3,550.00 USD | 0.00 USD | `+5.07%` | `44,701.00` |
| `Live` | `Short` | `0.0795` | 9,240.00 USD | 104.72 USD | 0.00 USD | `+5.20%` | `1,318.00` |
| `Live` | `Short` | `0.0795` | 10,090.00 USD | 855.64 USD | 0.00 USD | `+5.34%` | `10,756.00` |
| `Live` | `Short` | `0.0804` | 10,920.00 USD | 826.14 USD | 0.00 USD | `+6.53%` | `10,269.00` |
| `Live` | `Short` | `0.0806` | 11,130.00 USD | 213.40 USD | 0.00 USD | `+6.79%` | `2,646.00` |
| `Live` | `Short` | `0.0819` | 11,510.00 USD | 380.85 USD | 0.00 USD | `+8.38%` | `4,653.00` |
| `Live` | `Short` | `0.0825` | 11,730.00 USD | 217.85 USD | 0.00 USD | `+9.31%` | `2,639.00` |
| `Live` | `Short` | `0.0828` | 11,950.00 USD | 218.81 USD | 0.00 USD | `+9.71%` | `2,641.00` |
| `Live` | `Short` | `0.0829` | 12,170.00 USD | 219.07 USD | 0.00 USD | `+9.84%` | `2,641.00` |
| `Live` | `Short` | `0.0832` | 15,620.00 USD | 3,450.00 USD | 0.00 USD | `+10.10%` | `41,543.00` |
| `Live` | `Short` | `0.0837` | 15,910.00 USD | 293.44 USD | 0.00 USD | `+10.77%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 17,490.00 USD | 1,570.00 USD | 0.00 USD | `+10.90%` | `18,767.00` |
| `Live` | `Short` | `0.0838` | 17,710.00 USD | 221.45 USD | 0.00 USD | `+11.03%` | `2,641.00` |
| `Live` | `Short` | `0.0839` | 17,930.00 USD | 221.54 USD | 0.00 USD | `+11.16%` | `2,639.00` |
| `Live` | `Short` | `0.0840` | 18,050.00 USD | 122.71 USD | 0.00 USD | `+11.30%` | `1,460.00` |
| `Live` | `Short` | `0.0843` | 18,320.00 USD | 264.21 USD | 0.00 USD | `+11.56%` | `3,136.00` |
| `Live` | `Short` | `0.0847` | 18,540.00 USD | 223.39 USD | 0.00 USD | `+12.09%` | `2,639.00` |
| `Live` | `Short` | `0.0848` | 18,970.00 USD | 426.71 USD | 0.00 USD | `+12.35%` | `5,029.00` |
| `Live` | `Short` | `0.0853` | 19,190.00 USD | 224.97 USD | 0.00 USD | `+12.88%` | `2,639.00` |
| `Live` | `Short` | `0.0858` | 19,310.00 USD | 115.30 USD | 0.00 USD | `+13.68%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 23,550.00 USD | 4,250.00 USD | 0.00 USD | `+13.81%` | `49,397.00` |
| `Live` | `Short` | `0.0868` | 23,710.00 USD | 155.98 USD | 0.00 USD | `+15.00%` | `1,796.00` |
| `Live` | `Short` | `0.0871` | 23,850.00 USD | 138.58 USD | 0.00 USD | `+15.27%` | `1,592.00` |
| `Live` | `Short` | `0.0877` | 24,080.00 USD | 231.57 USD | 0.00 USD | `+16.19%` | `2,639.00` |
| `Live` | `Short` | `0.0881` | 24,540.00 USD | 465.17 USD | 0.00 USD | `+16.59%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 24,960.00 USD | 411.53 USD | 0.00 USD | `+17.52%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 25,370.00 USD | 418.80 USD | 0.00 USD | `+17.92%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 25,660.00 USD | 285.70 USD | 0.00 USD | `+18.45%` | `3,194.00` |
| `Live` | `Short` | `0.0901` | 25,900.00 USD | 237.64 USD | 0.00 USD | `+19.24%` | `2,639.00` |
| `Live` | `Short` | `0.0905` | 32,660.00 USD | 6,760.00 USD | 0.00 USD | `+19.77%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 33,970.00 USD | 1,310.00 USD | 0.00 USD | `+20.03%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 38,910.00 USD | 4,940.00 USD | 0.00 USD | `+20.70%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 39,080.00 USD | 171.49 USD | 0.00 USD | `+21.89%` | `1,863.00` |
| `Live` | `Short` | `0.0925` | 39,980.00 USD | 901.07 USD | 0.00 USD | `+22.55%` | `9,736.00` |
| `Live` | `Short` | `0.0931` | 40,790.00 USD | 805.37 USD | 0.00 USD | `+23.34%` | `8,646.00` |
| `Live` | `Short` | `0.0934` | 44,990.00 USD | 4,200.00 USD | 0.00 USD | `+23.61%` | `45,000.00` |
| `Live` | `Short` | `0.0944` | 84,690.00 USD | 39,700.00 USD | 0.00 USD | `+24.93%` | `420,808.00` |
| `Live` | `Short` | `0.0948` | 132,070.00 USD | 47,380.00 USD | 0.00 USD | `+25.46%` | `500,000.00` |
| `Live` | `Short` | `0.0950` | 156,530.00 USD | 24,460.00 USD | 0.00 USD | `+25.73%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 157,290.00 USD | 761.26 USD | 0.00 USD | `+25.86%` | `8,009.00` |
| `Live` | `Short` | `0.0955` | 157,490.00 USD | 194.44 USD | 0.00 USD | `+26.52%` | `2,035.00` |
| `Live` | `Short` | `0.0961` | 158,100.00 USD | 609.59 USD | 0.00 USD | `+27.32%` | `6,340.00` |
| `Live` | `Short` | `0.0970` | 159,630.00 USD | 1,540.00 USD | 0.00 USD | `+28.51%` | `15,857.00` |
| `Live` | `Short` | `0.0974` | 159,760.00 USD | 121.23 USD | 0.00 USD | `+29.04%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 160,230.00 USD | 477.50 USD | 0.00 USD | `+30.10%` | `4,860.00` |
| `Live` | `Short` | `0.0987` | 163,120.00 USD | 2,880.00 USD | 0.00 USD | `+30.63%` | `29,217.00` |
| `Live` | `Short` | `0.1003` | 163,320.00 USD | 202.21 USD | 0.00 USD | `+32.88%` | `2,015.00` |
| `Live` | `Short` | `0.1014` | 170,940.00 USD | 7,630.00 USD | 0.00 USD | `+34.34%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 173,910.00 USD | 2,970.00 USD | 0.00 USD | `+34.60%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 174,410.00 USD | 492.85 USD | 0.00 USD | `+34.86%` | `4,839.00` |
| `Live` | `Short` | `0.1053` | 177,670.00 USD | 3,270.00 USD | 0.00 USD | `+39.50%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 183,780.00 USD | 6,110.00 USD | 0.00 USD | `+40.56%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 184,400.00 USD | 616.19 USD | 0.00 USD | `+42.55%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 187,640.00 USD | 3,240.00 USD | 0.00 USD | `+43.74%` | `29,849.00` |
| `Live` | `Short` | `0.1106` | 189,480.00 USD | 1,840.00 USD | 0.00 USD | `+46.52%` | `16,647.00` |
| `Live` | `Short` | `0.1127` | 189,690.00 USD | 214.15 USD | 0.00 USD | `+49.17%` | `1,901.00` |
| `Live` | `Short` | `0.1137` | 189,840.00 USD | 147.86 USD | 0.00 USD | `+50.49%` | `1,301.00` |
| `Live` | `Short` | `0.1152` | 189,990.00 USD | 147.05 USD | 0.00 USD | `+52.48%` | `1,277.00` |
| `Live` | `Short` | `0.1159` | 190,830.00 USD | 837.04 USD | 0.00 USD | `+53.54%` | `7,219.00` |
| `Live` | `Short` | `0.1222` | 191,460.00 USD | 637.53 USD | 0.00 USD | `+61.88%` | `5,215.00` |
| `Live` | `Short` | `0.1252` | 191,580.00 USD | 120.77 USD | 0.00 USD | `+65.72%` | `965.00` |
| `Live` | `Short` | `0.1270` | 191,690.00 USD | 108.80 USD | 0.00 USD | `+68.10%` | `857.00` |
| `Live` | `Short` | `0.1296` | 191,860.00 USD | 171.66 USD | 0.00 USD | `+71.68%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 194,000.00 USD | 2,140.00 USD | 0.00 USD | `+73.66%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 239,230.00 USD | 45,230.00 USD | 0.00 USD | `+74.59%` | `343,012.00` |
| `Live` | `Short` | `0.1326` | 245,160.00 USD | 5,930.00 USD | 0.00 USD | `+75.65%` | `44,734.00` |
| `Live` | `Short` | `0.1338` | 245,370.00 USD | 205.31 USD | 0.00 USD | `+77.11%` | `1,535.00` |
| `Live` | `Short` | `0.1389` | 246,580.00 USD | 1,210.00 USD | 0.00 USD | `+83.86%` | `8,712.00` |
| `Live` | `Short` | `0.1404` | 247,240.00 USD | 663.63 USD | 0.00 USD | `+85.98%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 248,330.00 USD | 1,090.00 USD | 0.00 USD | `+86.77%` | `7,715.00` |
| `Live` | `Short` | `0.1412` | 271,240.00 USD | 22,910.00 USD | 0.00 USD | `+87.04%` | `162,180.00` |
| `Live` | `Short` | `0.1426` | 273,040.00 USD | 1,800.00 USD | 0.00 USD | `+88.76%` | `12,652.00` |
| `Live` | `Short` | `0.1432` | 274,910.00 USD | 1,860.00 USD | 0.00 USD | `+89.68%` | `13,010.00` |
| `Live` | `Short` | `0.1439` | 276,740.00 USD | 1,840.00 USD | 0.00 USD | `+90.61%` | `12,755.00` |
| `Live` | `Short` | `0.1441` | 276,940.00 USD | 196.63 USD | 0.00 USD | `+90.74%` | `1,365.00` |
| `Live` | `Short` | `0.1442` | 290,710.00 USD | 13,770.00 USD | 0.00 USD | `+90.88%` | `95,545.00` |
| `Live` | `Short` | `0.1444` | 292,250.00 USD | 1,540.00 USD | 0.00 USD | `+91.14%` | `10,691.00` |
| `Live` | `Short` | `0.1444` | 324,220.00 USD | 31,970.00 USD | 0.00 USD | `+91.27%` | `221,300.00` |
| `Live` | `Short` | `0.1446` | 324,370.00 USD | 144.55 USD | 0.00 USD | `+91.41%` | `1,000.00` |
| `Live` | `Short` | `0.1459` | 326,300.00 USD | 1,930.00 USD | 0.00 USD | `+93.26%` | `13,240.00` |
| `Live` | `Short` | `0.1479` | 334,410.00 USD | 8,110.00 USD | 0.00 USD | `+95.78%` | `54,875.00` |
| `Live` | `Short` | `0.1489` | 334,860.00 USD | 446.85 USD | 0.00 USD | `+97.23%` | `3,000.00` |
| `Live` | `Short` | `0.1497` | 358,920.00 USD | 24,060.00 USD | 0.00 USD | `+98.16%` | `160,802.00` |
| `Live` | `Short` | `0.1499` | 3,480,000.00 USD | 3,130,000.00 USD | 0.00 USD | `+98.56%` | `20,845,267.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 732,660.00 USD | 0.00 USD | 375.42 USD | `-65.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 732,290.00 USD | 0.00 USD | 409.59 USD | `-46.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 731,880.00 USD | 0.00 USD | 132.68 USD | `-46.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 731,750.00 USD | 0.00 USD | 788.27 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 730,960.00 USD | 0.00 USD | 527.05 USD | `-44.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 730,430.00 USD | 0.00 USD | 286.87 USD | `-40.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 730,140.00 USD | 0.00 USD | 252.42 USD | `-38.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 729,890.00 USD | 0.00 USD | 468.67 USD | `-37.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 729,420.00 USD | 0.00 USD | 5,160.00 USD | `-35.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 724,260.00 USD | 0.00 USD | 920.48 USD | `-34.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 723,340.00 USD | 0.00 USD | 236.01 USD | `-33.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 723,110.00 USD | 0.00 USD | 175.41 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 722,930.00 USD | 0.00 USD | 242.96 USD | `-31.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 722,690.00 USD | 0.00 USD | 2,670.00 USD | `-28.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 720,020.00 USD | 0.00 USD | 1,370.00 USD | `-26.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 718,640.00 USD | 0.00 USD | 437.58 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 718,210.00 USD | 0.00 USD | 183.30 USD | `-22.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 718,020.00 USD | 0.00 USD | 752.54 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 717,270.00 USD | 0.00 USD | 984.67 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 716,280.00 USD | 0.00 USD | 668.84 USD | `-20.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 715,620.00 USD | 0.00 USD | 273.90 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 715,340.00 USD | 0.00 USD | 8,800.00 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 706,540.00 USD | 0.00 USD | 838.79 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 705,710.00 USD | 0.00 USD | 218.94 USD | `-19.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 705,490.00 USD | 0.00 USD | 504.26 USD | `-18.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 704,980.00 USD | 0.00 USD | 2,280.00 USD | `-17.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 702,700.00 USD | 0.00 USD | 118.27 USD | `-17.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 702,580.00 USD | 0.00 USD | 1,280.00 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 701,310.00 USD | 0.00 USD | 1,820.00 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 699,480.00 USD | 0.00 USD | 1,340.00 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 698,150.00 USD | 0.00 USD | 386.70 USD | `-15.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 697,760.00 USD | 0.00 USD | 644.50 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 697,120.00 USD | 0.00 USD | 11,270.00 USD | `-13.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 685,850.00 USD | 0.00 USD | 362.24 USD | `-13.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 685,480.00 USD | 0.00 USD | 3,140.00 USD | `-13.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 682,340.00 USD | 0.00 USD | 1,100.00 USD | `-12.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 681,250.00 USD | 0.00 USD | 1,200.00 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 680,050.00 USD | 0.00 USD | 996.31 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 679,050.00 USD | 0.00 USD | 909.85 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 678,140.00 USD | 0.00 USD | 115.57 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 678,030.00 USD | 0.00 USD | 33,620.00 USD | `-10.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 644,400.00 USD | 0.00 USD | 12,860.00 USD | `-10.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 631,540.00 USD | 0.00 USD | 1,540.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 630,000.00 USD | 0.00 USD | 108.08 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 629,890.00 USD | 0.00 USD | 19,540.00 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 610,350.00 USD | 0.00 USD | 1,430.00 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 608,920.00 USD | 0.00 USD | 8,540.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 600,380.00 USD | 0.00 USD | 8,580.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 591,810.00 USD | 0.00 USD | 4,970.00 USD | `-9.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 586,840.00 USD | 0.00 USD | 3,100.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 583,740.00 USD | 0.00 USD | 160.31 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 583,580.00 USD | 0.00 USD | 38,710.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 544,870.00 USD | 0.00 USD | 21,140.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 523,740.00 USD | 0.00 USD | 3,190.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 520,550.00 USD | 0.00 USD | 478.66 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 520,070.00 USD | 0.00 USD | 176.08 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 519,890.00 USD | 0.00 USD | 142.09 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 519,750.00 USD | 0.00 USD | 925.29 USD | `-7.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 518,830.00 USD | 0.00 USD | 797.80 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 518,030.00 USD | 0.00 USD | 68,440.00 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 449,590.00 USD | 0.00 USD | 141.77 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 449,450.00 USD | 0.00 USD | 895.27 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 448,550.00 USD | 0.00 USD | 523.23 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 448,030.00 USD | 0.00 USD | 468.88 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 447,560.00 USD | 0.00 USD | 235.12 USD | `-6.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 447,320.00 USD | 0.00 USD | 1,090.00 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 446,240.00 USD | 0.00 USD | 71,660.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0711` | 374,580.00 USD | 0.00 USD | 729.61 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 373,850.00 USD | 0.00 USD | 355.75 USD | `-5.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 373,490.00 USD | 0.00 USD | 20,180.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 353,310.00 USD | 0.00 USD | 608.76 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 352,700.00 USD | 0.00 USD | 16,880.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 335,830.00 USD | 0.00 USD | 110.12 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 335,720.00 USD | 0.00 USD | 1,880.00 USD | `-5.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 333,830.00 USD | 0.00 USD | 17,760.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 316,070.00 USD | 0.00 USD | 13,550.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 302,520.00 USD | 0.00 USD | 551.98 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 301,970.00 USD | 0.00 USD | 138,380.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 163,590.00 USD | 0.00 USD | 1,690.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 161,900.00 USD | 0.00 USD | 34,460.00 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 127,440.00 USD | 0.00 USD | 2,030.00 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 125,410.00 USD | 0.00 USD | 2,340.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 123,080.00 USD | 0.00 USD | 383.97 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 122,690.00 USD | 0.00 USD | 2,540.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 120,150.00 USD | 0.00 USD | 4,030.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 116,110.00 USD | 0.00 USD | 386.09 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 115,730.00 USD | 0.00 USD | 1,950.00 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 113,780.00 USD | 0.00 USD | 535.16 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 113,240.00 USD | 0.00 USD | 227.92 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 113,010.00 USD | 0.00 USD | 397.76 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 112,620.00 USD | 0.00 USD | 398.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 112,220.00 USD | 0.00 USD | 797.39 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 111,420.00 USD | 0.00 USD | 59,820.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 51,600.00 USD | 0.00 USD | 1,640.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 49,950.00 USD | 0.00 USD | 189.57 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 49,770.00 USD | 0.00 USD | 1,480.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 48,290.00 USD | 0.00 USD | 2,900.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 45,390.00 USD | 0.00 USD | 415.62 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 44,980.00 USD | 0.00 USD | 16,520.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 28,460.00 USD | 0.00 USD | 3,170.00 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 25,280.00 USD | 0.00 USD | 375.86 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 24,910.00 USD | 0.00 USD | 391.32 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 24,520.00 USD | 0.00 USD | 140.04 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 24,380.00 USD | 0.00 USD | 1,490.00 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 22,880.00 USD | 0.00 USD | 3,750.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 19,130.00 USD | 0.00 USD | 16,870.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 2,260.00 USD | 0.00 USD | 406.95 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 1,850.00 USD | 0.00 USD | 1,700.00 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 151.35 USD | 0.00 USD | 151.35 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 7,490.00 USD | 7,490.00 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 7,640.00 USD | 150.85 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 8,860.00 USD | 1,210.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 9,360.00 USD | 504.10 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 9,760.00 USD | 398.13 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 13,160.00 USD | 3,400.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 33,400.00 USD | 20,230.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 34,210.00 USD | 814.81 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 37,980.00 USD | 3,770.00 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 38,090.00 USD | 109.63 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 39,340.00 USD | 1,250.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 39,520.00 USD | 183.50 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 39,720.00 USD | 200.93 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 40,680.00 USD | 955.71 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 41,500.00 USD | 816.05 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 42,210.00 USD | 715.18 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 44,540.00 USD | 2,330.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 45,520.00 USD | 978.37 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 49,450.00 USD | 3,930.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 49,860.00 USD | 407.23 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 50,180.00 USD | 321.13 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 50,590.00 USD | 409.84 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 52,830.00 USD | 2,240.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 53,160.00 USD | 329.23 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 53,320.00 USD | 155.43 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 54,140.00 USD | 823.90 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 57,060.00 USD | 2,920.00 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 58,040.00 USD | 975.23 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 58,450.00 USD | 413.84 USD | 0.00 USD | `+3.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 58,610.00 USD | 157.14 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 58,740.00 USD | 130.71 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 100,350.00 USD | 41,610.00 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 100,490.00 USD | 141.44 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 101,260.00 USD | 773.68 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 101,950.00 USD | 687.81 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 107,370.00 USD | 5,420.00 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 108,480.00 USD | 1,110.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 113,850.00 USD | 5,370.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 122,870.00 USD | 9,020.00 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 123,190.00 USD | 312.56 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 123,640.00 USD | 455.34 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 123,770.00 USD | 125.45 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 124,000.00 USD | 230.40 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 124,320.00 USD | 319.16 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 125,320.00 USD | 1,010.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 148,070.00 USD | 22,750.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 148,470.00 USD | 400.91 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 148,670.00 USD | 200.46 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 148,930.00 USD | 259.13 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 149,640.00 USD | 707.08 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 158,650.00 USD | 9,010.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 255,430.00 USD | 96,780.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 256,240.00 USD | 807.50 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 256,490.00 USD | 257.18 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 256,920.00 USD | 424.74 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 257,020.00 USD | 101.80 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 258,400.00 USD | 1,380.00 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 260,430.00 USD | 2,030.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 261,860.00 USD | 1,430.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 261,990.00 USD | 129.67 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 263,010.00 USD | 1,020.00 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 263,270.00 USD | 256.05 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 264,290.00 USD | 1,030.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 267,310.00 USD | 3,020.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 267,640.00 USD | 327.80 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 268,100.00 USD | 457.92 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 268,790.00 USD | 691.29 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 269,590.00 USD | 800.79 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 270,100.00 USD | 512.05 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 270,600.00 USD | 495.36 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 270,990.00 USD | 389.31 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 271,140.00 USD | 154.58 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 271,450.00 USD | 303.56 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 271,560.00 USD | 112.89 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 271,940.00 USD | 381.45 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 272,100.00 USD | 155.82 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 316,480.00 USD | 44,390.00 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 316,790.00 USD | 309.23 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 318,050.00 USD | 1,260.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 319,290.00 USD | 1,240.00 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,070,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,070,000.00 USD | 3,150.00 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,070,000.00 USD | 1,470.00 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,070,000.00 USD | 107.71 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,070,000.00 USD | 2,690.00 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,070,000.00 USD | 529.92 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,070,000.00 USD | 219.07 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,070,000.00 USD | 242.84 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,080,000.00 USD | 10,140.00 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,080,000.00 USD | 876.11 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,090,000.00 USD | 812.54 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,090,000.00 USD | 126.76 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,090,000.00 USD | 307.41 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,090,000.00 USD | 614.09 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,090,000.00 USD | 859.50 USD | 0.00 USD | `+13.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,090,000.00 USD | 2,020.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,130,000.00 USD | 43,760.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,130,000.00 USD | 123.94 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,130,000.00 USD | 271.53 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,140,000.00 USD | 1,660.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,140,000.00 USD | 1,840.00 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,140,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,140,000.00 USD | 117.71 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,140,000.00 USD | 111.61 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,140,000.00 USD | 571.18 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,140,000.00 USD | 375.94 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,140,000.00 USD | 627.55 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,140,000.00 USD | 211.04 USD | 0.00 USD | `+17.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,140,000.00 USD | 108.36 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,140,000.00 USD | 543.32 USD | 0.00 USD | `+17.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,140,000.00 USD | 1,820.00 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,150,000.00 USD | 2,080.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,160,000.00 USD | 17,680.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,170,000.00 USD | 1,370.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,170,000.00 USD | 5,630.00 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,170,000.00 USD | 1,090.00 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,170,000.00 USD | 224.86 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,190,000.00 USD | 20,540.00 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,190,000.00 USD | 114.93 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,190,000.00 USD | 679.12 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,190,000.00 USD | 173.36 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,200,000.00 USD | 1,810.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,200,000.00 USD | 1,530.00 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,200,000.00 USD | 2,280.00 USD | 0.00 USD | `+22.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,200,000.00 USD | 541.32 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,340,000.00 USD | 137,500.00 USD | 0.00 USD | `+22.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,340,000.00 USD | 691.07 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,340,000.00 USD | 6,250.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,360,000.00 USD | 13,480.00 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,360,000.00 USD | 734.82 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,360,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,360,000.00 USD | 105.00 USD | 0.00 USD | `+23.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,360,000.00 USD | 184.09 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,360,000.00 USD | 1,120.00 USD | 0.00 USD | `+24.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,360,000.00 USD | 1,860.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,360,000.00 USD | 1,070.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,360,000.00 USD | 512.15 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,370,000.00 USD | 6,620.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,370,000.00 USD | 404.96 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,370,000.00 USD | 129.85 USD | 0.00 USD | `+26.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,380,000.00 USD | 3,740.00 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,380,000.00 USD | 409.17 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,380,000.00 USD | 203.74 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,380,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,380,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,380,000.00 USD | 694.56 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,380,000.00 USD | 940.91 USD | 0.00 USD | `+30.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,380,000.00 USD | 2,980.00 USD | 0.00 USD | `+31.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,380,000.00 USD | 104.99 USD | 0.00 USD | `+31.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,390,000.00 USD | 1,930.00 USD | 0.00 USD | `+31.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,410,000.00 USD | 19,950.00 USD | 0.00 USD | `+31.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,410,000.00 USD | 1,490.00 USD | 0.00 USD | `+31.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,410,000.00 USD | 1,090.00 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,410,000.00 USD | 438.96 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,410,000.00 USD | 973.76 USD | 0.00 USD | `+32.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,420,000.00 USD | 10,000.00 USD | 0.00 USD | `+32.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,420,000.00 USD | 175.59 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,420,000.00 USD | 2,060.00 USD | 0.00 USD | `+32.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,420,000.00 USD | 482.89 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,420,000.00 USD | 201.90 USD | 0.00 USD | `+33.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,420,000.00 USD | 489.46 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,420,000.00 USD | 103.68 USD | 0.00 USD | `+34.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,430,000.00 USD | 2,590.00 USD | 0.00 USD | `+34.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,430,000.00 USD | 3,810.00 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,440,000.00 USD | 11,200.00 USD | 0.00 USD | `+35.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,450,000.00 USD | 4,330.00 USD | 0.00 USD | `+35.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,450,000.00 USD | 205.50 USD | 0.00 USD | `+36.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,450,000.00 USD | 3,490.00 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,450,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,450,000.00 USD | 207.50 USD | 0.00 USD | `+37.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,450,000.00 USD | 813.88 USD | 0.00 USD | `+38.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,480,000.00 USD | 23,160.00 USD | 0.00 USD | `+38.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,480,000.00 USD | 209.30 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,480,000.00 USD | 1,440.00 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,480,000.00 USD | 5,140.00 USD | 0.00 USD | `+39.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,480,000.00 USD | 585.32 USD | 0.00 USD | `+39.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,480,000.00 USD | 210.90 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,480,000.00 USD | 1,850.00 USD | 0.00 USD | `+39.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,480,000.00 USD | 105.75 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,490,000.00 USD | 3,220.00 USD | 0.00 USD | `+40.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,490,000.00 USD | 1,600.00 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,490,000.00 USD | 212.90 USD | 0.00 USD | `+40.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,490,000.00 USD | 472.63 USD | 0.00 USD | `+41.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,490,000.00 USD | 214.50 USD | 0.00 USD | `+42.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,490,000.00 USD | 1,040.00 USD | 0.00 USD | `+42.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,490,000.00 USD | 136.12 USD | 0.00 USD | `+42.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,490,000.00 USD | 216.10 USD | 0.00 USD | `+43.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,490,000.00 USD | 1,010.00 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,490,000.00 USD | 217.90 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,490,000.00 USD | 219.70 USD | 0.00 USD | `+45.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,500,000.00 USD | 7,780.00 USD | 0.00 USD | `+45.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,500,000.00 USD | 154.22 USD | 0.00 USD | `+46.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,500,000.00 USD | 221.30 USD | 0.00 USD | `+46.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,530,000.00 USD | 24,190.00 USD | 0.00 USD | `+47.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,530,000.00 USD | 223.10 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,530,000.00 USD | 224.70 USD | 0.00 USD | `+48.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,530,000.00 USD | 226.30 USD | 0.00 USD | `+49.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,530,000.00 USD | 950.34 USD | 0.00 USD | `+50.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,530,000.00 USD | 229.50 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,530,000.00 USD | 771.08 USD | 0.00 USD | `+52.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,530,000.00 USD | 942.95 USD | 0.00 USD | `+52.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,530,000.00 USD | 230.90 USD | 0.00 USD | `+52.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,530,000.00 USD | 288.18 USD | 0.00 USD | `+53.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,530,000.00 USD | 619.10 USD | 0.00 USD | `+53.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,530,000.00 USD | 1,250.00 USD | 0.00 USD | `+53.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,530,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,530,000.00 USD | 232.30 USD | 0.00 USD | `+53.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,540,000.00 USD | 1,600.00 USD | 0.00 USD | `+54.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,540,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,540,000.00 USD | 3,730.00 USD | 0.00 USD | `+55.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,540,000.00 USD | 676.22 USD | 0.00 USD | `+56.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,540,000.00 USD | 648.25 USD | 0.00 USD | `+56.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,540,000.00 USD | 1,510.00 USD | 0.00 USD | `+56.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,540,000.00 USD | 448.52 USD | 0.00 USD | `+56.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,540,000.00 USD | 124.58 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,550,000.00 USD | 1,050.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,550,000.00 USD | 691.80 USD | 0.00 USD | `+58.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,660,000.00 USD | 117,860.00 USD | 0.00 USD | `+58.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,660,000.00 USD | 143.22 USD | 0.00 USD | `+59.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,670,000.00 USD | 1,380.00 USD | 0.00 USD | `+60.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,670,000.00 USD | 2,270.00 USD | 0.00 USD | `+61.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,670,000.00 USD | 871.99 USD | 0.00 USD | `+62.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,700,000.00 USD | 29,610.00 USD | 0.00 USD | `+67.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,700,000.00 USD | 400.21 USD | 0.00 USD | `+68.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,700,000.00 USD | 2,360.00 USD | 0.00 USD | `+74.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,700,000.00 USD | 4,160.00 USD | 0.00 USD | `+79.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,700,000.00 USD | 114.70 USD | 0.00 USD | `+80.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,710,000.00 USD | 278.50 USD | 0.00 USD | `+85.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,710,000.00 USD | 1,160.00 USD | 0.00 USD | `+87.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,710,000.00 USD | 173.57 USD | 0.00 USD | `+88.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,710,000.00 USD | 380.09 USD | 0.00 USD | `+88.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,720,000.00 USD | 17,150.00 USD | 0.00 USD | `+88.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,730,000.00 USD | 1,440.00 USD | 0.00 USD | `+90.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,730,000.00 USD | 433.35 USD | 0.00 USD | `+91.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,730,000.00 USD | 452.26 USD | 0.00 USD | `+93.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,730,000.00 USD | 3,640.00 USD | 0.00 USD | `+94.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,790,000.00 USD | 55,720.00 USD | 0.00 USD | `+95.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,790,000.00 USD | 2,120.00 USD | 0.00 USD | `+96.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,810,000.00 USD | 19,850.00 USD | 0.00 USD | `+98.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0647` | 29,780,000.00 USD | 0.00 USD | 29,780,000.00 USD | 23,160.00 USD | 13,720.00 USD | 0.00 USD |
| `7D` | `0.0649` | 29,740,000.00 USD | 0.00 USD | 29,740,000.00 USD | 21,850.00 USD | 0.00 USD | 15,770.00 USD |
| `7D` | `0.0657` | 29,710,000.00 USD | 0.00 USD | 29,710,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0661` | 29,690,000.00 USD | 0.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD |
| `7D` | `0.0663` | 29,650,000.00 USD | 0.00 USD | 29,650,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `7D` | `0.0665` | 29,640,000.00 USD | 0.00 USD | 29,640,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD |
| `7D` | `0.0669` | 29,460,000.00 USD | 0.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `7D` | `0.0675` | 29,460,000.00 USD | 0.00 USD | 29,460,000.00 USD | 25,430.00 USD | 8,460.00 USD | 19,470.00 USD |
| `1D` | `0.0677` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 48,630.00 USD | 94,300.00 USD | 19,040.00 USD |
| `7D` | `0.0677` | 29,410,000.00 USD | 0.00 USD | 29,410,000.00 USD | 10,470.00 USD | 0.00 USD | 475.18 USD |
| `1D` | `0.0678` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 18,700.00 USD | 39,890.00 USD | 65,900.00 USD |
| `1D` | `0.0679` | 17,370,000.00 USD | 0.00 USD | 17,370,000.00 USD | 57,130.00 USD | 39,580.00 USD | 8,010.00 USD |
| `7D` | `0.0679` | 29,390,000.00 USD | 0.00 USD | 29,390,000.00 USD | 6,140.00 USD | 59,770.00 USD | 61,020.00 USD |
| `1D` | `0.0680` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 51,160.00 USD | 43,850.00 USD | 41,660.00 USD |
| `1D` | `0.0681` | 17,130,000.00 USD | 0.00 USD | 17,130,000.00 USD | 36,810.00 USD | 55,770.00 USD | 149,430.00 USD |
| `7D` | `0.0681` | 29,270,000.00 USD | 0.00 USD | 29,270,000.00 USD | 118,640.00 USD | 61,880.00 USD | 164,800.00 USD |
| `1D` | `0.0682` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 14,920.00 USD | 58,710.00 USD | 26,770.00 USD |
| `1D` | `0.0683` | 16,790,000.00 USD | 0.00 USD | 16,790,000.00 USD | 15,780.00 USD | 32,750.00 USD | 23.24 USD |
| `7D` | `0.0683` | 28,920,000.00 USD | 0.00 USD | 28,920,000.00 USD | 0.00 USD | 58,370.00 USD | 66,930.00 USD |
| `1D` | `0.0684` | 16,740,000.00 USD | 0.00 USD | 16,740,000.00 USD | 24,150.00 USD | 26,540.00 USD | 3,910.00 USD |
| `1D` | `0.0685` | 16,690,000.00 USD | 0.00 USD | 16,690,000.00 USD | 58,140.00 USD | 14,450.00 USD | 29,220.00 USD |
| `7D` | `0.0685` | 28,800,000.00 USD | 0.00 USD | 28,800,000.00 USD | 142,840.00 USD | 77,920.00 USD | 25,380.00 USD |
| `1D` | `0.0686` | 16,590,000.00 USD | 0.00 USD | 16,590,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,200.00 USD |
| `1D` | `0.0687` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 17,350.00 USD | 32,460.00 USD | 29,690.00 USD |
| `7D` | `0.0687` | 28,550,000.00 USD | 0.00 USD | 28,550,000.00 USD | 101,720.00 USD | 128,090.00 USD | 1,010.00 USD |
| `1D` | `0.0688` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD |
| `1D` | `0.0689` | 16,360,000.00 USD | 0.00 USD | 16,360,000.00 USD | 10,400.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `0.0689` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 225,480.00 USD | 77,640.00 USD | 61,090.00 USD |
| `1D` | `0.0690` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD |
| `1D` | `0.0691` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 1,460.00 USD | 0.00 USD | 1,140.00 USD |
| `7D` | `0.0691` | 27,960,000.00 USD | 0.00 USD | 27,960,000.00 USD | 162,010.00 USD | 95,020.00 USD | 130,900.00 USD |
| `1D` | `0.0692` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 23,110.00 USD | 0.00 USD | 670.09 USD |
| `1D` | `0.0693` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0693` | 27,570,000.00 USD | 0.00 USD | 27,570,000.00 USD | 207,150.00 USD | 190,180.00 USD | 80,200.00 USD |
| `1D` | `0.0694` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 16,270,000.00 USD | 0.00 USD | 16,270,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0695` | 27,090,000.00 USD | 0.00 USD | 27,090,000.00 USD | 282,470.00 USD | 212,530.00 USD | 212,560.00 USD |
| `1D` | `0.0697` | 16,270,000.00 USD | 0.00 USD | 16,270,000.00 USD | 31,720.00 USD | 13,590.00 USD | 20,060.00 USD |
| `7D` | `0.0697` | 26,380,000.00 USD | 0.00 USD | 26,380,000.00 USD | 142,190.00 USD | 148,620.00 USD | 263,500.00 USD |
| `1D` | `0.0698` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 10,960.00 USD | 10,400.00 USD | 10,460.00 USD |
| `1D` | `0.0699` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 38,680.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0699` | 25,830,000.00 USD | 0.00 USD | 25,830,000.00 USD | 325,570.00 USD | 205,450.00 USD | 138,220.00 USD |
| `1D` | `0.0700` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,060.00 USD |
| `1D` | `0.0701` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 39,680.00 USD | 108,360.00 USD | 1,980.00 USD |
| `7D` | `0.0701` | 25,160,000.00 USD | 0.00 USD | 25,160,000.00 USD | 283,670.00 USD | 119,790.00 USD | 142,750.00 USD |
| `1D` | `0.0702` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 47,190.00 USD | 19,670.00 USD | 2,110.00 USD |
| `1D` | `0.0703` | 15,790,000.00 USD | 0.00 USD | 15,790,000.00 USD | 148,860.00 USD | 62,920.00 USD | 8,230.00 USD |
| `7D` | `0.0703` | 24,610,000.00 USD | 0.00 USD | 24,610,000.00 USD | 261,240.00 USD | 120,430.00 USD | 50,710.00 USD |
| `1D` | `0.0704` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 15,860.00 USD | 36,100.00 USD | 20,350.00 USD |
| `1D` | `0.0705` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 41,460.00 USD | 30,720.00 USD | 37,250.00 USD |
| `7D` | `0.0705` | 24,180,000.00 USD | 0.00 USD | 24,180,000.00 USD | 224,080.00 USD | 133,180.00 USD | 178,570.00 USD |
| `1D` | `0.0706` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 22,880.00 USD | 1,120.00 USD | 14,210.00 USD |
| `1D` | `0.0707` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 136,920.00 USD | 69,310.00 USD | 45,290.00 USD |
| `7D` | `0.0707` | 23,650,000.00 USD | 0.00 USD | 23,650,000.00 USD | 171,490.00 USD | 37,160.00 USD | 156,120.00 USD |
| `1D` | `0.0708` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 69,400.00 USD | 62,000.00 USD | 105,010.00 USD |
| `1D` | `0.0709` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 38,730.00 USD | 82,010.00 USD | 151,140.00 USD |
| `7D` | `0.0709` | 23,280,000.00 USD | 0.00 USD | 23,280,000.00 USD | 485,290.00 USD | 159,720.00 USD | 139,080.00 USD |
| `1D` | `0.0710` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 117,230.00 USD | 91,550.00 USD | 125,030.00 USD |
| `1D` | `0.0711` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 49,210.00 USD | 25,670.00 USD | 42,180.00 USD |
| `7D` | `0.0711` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 285,730.00 USD | 252,130.00 USD | 91,190.00 USD |
| `1D` | `0.0712` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 165,590.00 USD | 46,690.00 USD | 1,080.00 USD |
| `1D` | `0.0713` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 75,840.00 USD | 85,230.00 USD | 64,950.00 USD |
| `7D` | `0.0713` | 21,870,000.00 USD | 0.00 USD | 21,870,000.00 USD | 379,600.00 USD | 171,480.00 USD | 139,950.00 USD |
| `1D` | `0.0714` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 120,780.00 USD | 51,930.00 USD | 46,340.00 USD |
| `1D` | `0.0715` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 79,660.00 USD | 238,460.00 USD | 41,100.00 USD |
| `7D` | `0.0715` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 211,700.00 USD | 51,460.00 USD | 66,820.00 USD |
| `1D` | `0.0716` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 19,480.00 USD | 51,080.00 USD | 0.00 USD |
| `1D` | `0.0717` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 238,310.00 USD | 96,160.00 USD | 3,300.00 USD |
| `7D` | `0.0717` | 20,850,000.00 USD | 0.00 USD | 20,850,000.00 USD | 285,100.00 USD | 190,890.00 USD | 48,380.00 USD |
| `1D` | `0.0718` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 64,570.00 USD | 101,030.00 USD | 15,780.00 USD |
| `1D` | `0.0719` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 229,400.00 USD | 45,330.00 USD | 68,560.00 USD |
| `7D` | `0.0719` | 20,320,000.00 USD | 0.00 USD | 20,320,000.00 USD | 233,070.00 USD | 63,390.00 USD | 276,250.00 USD |
| `1D` | `0.0720` | 12,190,000.00 USD | 0.00 USD | 12,190,000.00 USD | 138,650.00 USD | 50,600.00 USD | 69,850.00 USD |
| `1D` | `0.0721` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 308,410.00 USD | 298,040.00 USD | 65,900.00 USD |
| `7D` | `0.0721` | 19,750,000.00 USD | 0.00 USD | 19,750,000.00 USD | 422,700.00 USD | 285,460.00 USD | 95,670.00 USD |
| `1D` | `0.0722` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 181,970.00 USD | 124,010.00 USD | 149,230.00 USD |
| `1D` | `0.0723` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 89,550.00 USD | 258,330.00 USD | 323,600.00 USD |
| `7D` | `0.0723` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 242,550.00 USD | 148,860.00 USD | 110,740.00 USD |
| `1D` | `0.0724` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 176,130.00 USD | 226,580.00 USD | 401,900.00 USD |
| `1D` | `0.0725` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 253,760.00 USD | 262,460.00 USD | 310,860.00 USD |
| `7D` | `0.0725` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 1,070,000.00 USD | 365,360.00 USD | 152,800.00 USD |
| `1D` | `0.0726` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 153,630.00 USD | 148,410.00 USD | 59,610.00 USD |
| `1D` | `0.0727` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 190,550.00 USD | 161,760.00 USD | 40,450.00 USD |
| `7D` | `0.0727` | 16,860,000.00 USD | 0.00 USD | 16,860,000.00 USD | 249,200.00 USD | 432,030.00 USD | 92,170.00 USD |
| `1D` | `0.0728` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 60,510.00 USD | 154,910.00 USD | 47,440.00 USD |
| `1D` | `0.0729` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 58,550.00 USD | 41,110.00 USD | 8,540.00 USD |
| `7D` | `0.0729` | 16,080,000.00 USD | 0.00 USD | 16,080,000.00 USD | 114,120.00 USD | 105,410.00 USD | 37,020.00 USD |
| `1D` | `0.0730` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 123,090.00 USD | 55,310.00 USD | 49,630.00 USD |
| `1D` | `0.0731` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 44,230.00 USD | 81,130.00 USD | 28,420.00 USD |
| `7D` | `0.0731` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 565,310.00 USD | 49,290.00 USD | 12,800.00 USD |
| `1D` | `0.0732` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 153,570.00 USD | 93,810.00 USD | 92,570.00 USD |
| `1D` | `0.0733` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD |
| `7D` | `0.0733` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 470,120.00 USD | 0.00 USD | 29,970.00 USD |
| `1D` | `0.0734` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD |
| `1D` | `0.0735` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD |
| `7D` | `0.0735` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 589,440.00 USD | 93,670.00 USD | 0.00 USD |
| `1D` | `0.0736` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `1D` | `0.0737` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 113,510.00 USD | 56,690.00 USD | 49,860.00 USD |
| `7D` | `0.0737` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 506,070.00 USD | 494,020.00 USD | 0.00 USD |
| `1D` | `0.0738` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 78,630.00 USD | 23,440.00 USD | 0.00 USD |
| `1D` | `0.0739` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 198,660.00 USD | 41,170.00 USD | 62,540.00 USD |
| `7D` | `0.0739` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 265,850.00 USD | 515,020.00 USD | 0.00 USD |
| `1D` | `0.0740` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 57,880.00 USD | 121,290.00 USD | 117,450.00 USD |
| `1D` | `0.0741` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 217,950.00 USD | 183,810.00 USD | 102,820.00 USD |
| `7D` | `0.0741` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 66,970.00 USD | 294,670.00 USD | 178,730.00 USD |
| `1D` | `0.0742` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 90,280.00 USD | 290,690.00 USD | 80,900.00 USD |
| `1D` | `0.0743` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 236,300.00 USD | 181,510.00 USD | 284,730.00 USD |
| `7D` | `0.0743` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 774,380.00 USD | 209,100.00 USD | 1,120,000.00 USD |
| `1D` | `0.0744` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 217,450.00 USD | 118,720.00 USD | 107,270.00 USD |
| `1D` | `0.0745` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 87,580.00 USD | 88,750.00 USD | 46,710.00 USD |
| `7D` | `0.0745` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 1,360,000.00 USD | 951,300.00 USD | 326,000.00 USD |
| `1D` | `0.0746` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 88,460.00 USD | 86,840.00 USD | 142,590.00 USD |
| `1D` | `0.0747` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,540.00 USD |
| `7D` | `0.0747` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 1,410,000.00 USD | 1,830,000.00 USD | 649,410.00 USD |
| `1D` | `0.0748` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 98,680.00 USD | 109,690.00 USD | 198,860.00 USD |
| `1D` | `0.0749` | 636,130.00 USD | 0.00 USD | 636,130.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD |
| `7D` | `0.0749` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 706,340.00 USD | 459,930.00 USD | 875,850.00 USD |
| `1D` | `0.0750` | 291,080.00 USD | 0.00 USD | 291,080.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD |
| `1D` | `0.0751` | 226,740.00 USD | 0.00 USD | 226,740.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD |
| `7D` | `0.0751` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 30,900.00 USD | 84,880.00 USD |
| `1D` | `0.0752` | 178,710.00 USD | 0.00 USD | 178,710.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `1D` | `0.0753` | 154,290.00 USD | 0.00 USD | 154,290.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD |
| `7D` | `0.0753` | 907,280.00 USD | 0.00 USD | 907,280.00 USD | 751,120.00 USD | 53,860.00 USD | 102,300.00 USD |
| `1D` | `0.0754` | 113.76 USD | 113.76 USD | 0.00 USD | 0.00 USD | 0.00 USD | 113.76 USD |
| `1D` | `0.0754` | 227.52 USD | 227.52 USD | 0.00 USD | 0.00 USD | 0.00 USD | 113.76 USD |
| `1D` | `0.0755` | 2,120.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD |
| `7D` | `0.0755` | 938,670.00 USD | 938,670.00 USD | 0.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD |
| `7D` | `0.0755` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD |
| `1D` | `0.0756` | 32,790.00 USD | 32,790.00 USD | 0.00 USD | 0.00 USD | 30,100.00 USD | 570.06 USD |
| `7D` | `0.0757` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 144,530.00 USD | 0.00 USD |
| `1D` | `0.0758` | 37,710.00 USD | 37,710.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD |
| `1D` | `0.0759` | 38,190.00 USD | 38,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 477.98 USD |
| `7D` | `0.0759` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 40,360.00 USD | 66,300.00 USD | 0.00 USD |
| `1D` | `0.0760` | 38,770.00 USD | 38,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 585.47 USD |
| `1D` | `0.0762` | 40,420.00 USD | 40,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,650.00 USD |
| `1D` | `0.0763` | 41,560.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `0.0764` | 56,810.00 USD | 56,810.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | 424.20 USD |
| `1D` | `0.0765` | 404,480.00 USD | 404,480.00 USD | 0.00 USD | 211,600.00 USD | 37,120.00 USD | 98,950.00 USD |
| `7D` | `0.0765` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 772,480.00 USD | 496,590.00 USD | 0.00 USD |
| `1D` | `0.0766` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 471,060.00 USD | 475,330.00 USD | 0.00 USD |
| `1D` | `0.0767` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 153,710.00 USD | 322,470.00 USD | 159,480.00 USD |
| `7D` | `0.0767` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 1,180,000.00 USD | 90,730.00 USD | 0.00 USD |
| `1D` | `0.0768` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 224,320.00 USD | 93,770.00 USD | 592,840.00 USD |
| `1D` | `0.0769` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 375,270.00 USD | 462,440.00 USD | 351,290.00 USD |
| `7D` | `0.0769` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 760,570.00 USD | 84,300.00 USD | 429,490.00 USD |
| `1D` | `0.0770` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 412,020.00 USD | 301,010.00 USD | 486,890.00 USD |
| `1D` | `0.0771` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 441,280.00 USD | 459,510.00 USD | 250,860.00 USD |
| `7D` | `0.0771` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 888,600.00 USD | 798,440.00 USD | 794,320.00 USD |
| `1D` | `0.0772` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 480,450.00 USD | 327,770.00 USD | 767,000.00 USD |
| `1D` | `0.0773` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 190,960.00 USD | 368,960.00 USD | 243,630.00 USD |
| `7D` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 69,030.00 USD | 347,590.00 USD | 64,060.00 USD |
| `1D` | `0.0774` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 118,800.00 USD | 246,740.00 USD | 36,420.00 USD |
| `1D` | `0.0775` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 288,570.00 USD | 180,890.00 USD | 60,420.00 USD |
| `7D` | `0.0775` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 779,670.00 USD | 375,100.00 USD | 0.00 USD |
| `1D` | `0.0776` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 284,830.00 USD | 214,460.00 USD | 145,500.00 USD |
| `1D` | `0.0777` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 401,010.00 USD | 342,630.00 USD | 165,130.00 USD |
| `7D` | `0.0777` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 265,980.00 USD | 286,560.00 USD | 693.20 USD |
| `1D` | `0.0778` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 116,640.00 USD | 340,450.00 USD | 399,710.00 USD |
| `1D` | `0.0779` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 345,840.00 USD | 210,420.00 USD | 204,370.00 USD |
| `7D` | `0.0779` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 270,450.00 USD | 301,690.00 USD | 438,670.00 USD |
| `1D` | `0.0780` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 212,580.00 USD | 78,920.00 USD | 38,190.00 USD |
| `1D` | `0.0781` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 22,110.00 USD |
| `7D` | `0.0781` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 186,410.00 USD | 142,450.00 USD | 4,370.00 USD |
| `1D` | `0.0782` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 70,430.00 USD | 86,550.00 USD | 79,320.00 USD |
| `1D` | `0.0783` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 52,750.00 USD | 214,890.00 USD | 174,690.00 USD |
| `7D` | `0.0783` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 15,350.00 USD | 285,880.00 USD | 193,490.00 USD |
| `1D` | `0.0784` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 388,250.00 USD | 122,020.00 USD | 72,810.00 USD |
| `1D` | `0.0785` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 216,540.00 USD | 171,160.00 USD | 121,090.00 USD |
| `7D` | `0.0785` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 197,420.00 USD | 141,600.00 USD | 278,250.00 USD |
| `1D` | `0.0786` | 16,250,000.00 USD | 16,250,000.00 USD | 0.00 USD | 352,080.00 USD | 218,550.00 USD | 294,920.00 USD |
| `1D` | `0.0787` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 379,110.00 USD | 464,730.00 USD | 382,860.00 USD |
| `7D` | `0.0787` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 437,500.00 USD | 346,050.00 USD | 812,710.00 USD |
| `1D` | `0.0788` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 168,080.00 USD | 262,350.00 USD | 121,810.00 USD |
| `1D` | `0.0789` | 18,680,000.00 USD | 18,680,000.00 USD | 0.00 USD | 312,410.00 USD | 233,260.00 USD | 104,610.00 USD |
| `7D` | `0.0789` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 301,760.00 USD | 259,180.00 USD | 249,350.00 USD |
| `1D` | `0.0790` | 18,950,000.00 USD | 18,950,000.00 USD | 0.00 USD | 153,960.00 USD | 87,240.00 USD | 28,160.00 USD |
| `1D` | `0.0791` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 203,370.00 USD | 133,580.00 USD | 124,340.00 USD |
| `7D` | `0.0791` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 476,430.00 USD | 81,300.00 USD | 5,350.00 USD |
| `1D` | `0.0792` | 19,770,000.00 USD | 19,770,000.00 USD | 0.00 USD | 224,560.00 USD | 57,840.00 USD | 75,020.00 USD |
| `1D` | `0.0793` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 5,950.00 USD | 0.00 USD | 421.36 USD |
| `7D` | `0.0793` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 27,550.00 USD | 61,220.00 USD | 246,330.00 USD |
| `1D` | `0.0794` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 158,580.00 USD | 96,210.00 USD | 102,830.00 USD |
| `1D` | `0.0795` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 92,560.00 USD | 45,380.00 USD | 101,740.00 USD |
| `7D` | `0.0795` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 469,960.00 USD |
| `1D` | `0.0796` | 20,590,000.00 USD | 20,590,000.00 USD | 0.00 USD | 199,280.00 USD | 12,890.00 USD | 0.00 USD |
| `1D` | `0.0797` | 20,920,000.00 USD | 20,920,000.00 USD | 0.00 USD | 206,810.00 USD | 89,760.00 USD | 40,270.00 USD |
| `7D` | `0.0797` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 640,790.00 USD | 203,560.00 USD | 119,170.00 USD |
| `1D` | `0.0798` | 21,050,000.00 USD | 21,050,000.00 USD | 0.00 USD | 58,670.00 USD | 63,560.00 USD | 3,930.00 USD |
| `1D` | `0.0799` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 64,660.00 USD | 191,860.00 USD | 37,760.00 USD |
| `7D` | `0.0799` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 561,590.00 USD | 130,870.00 USD | 78,050.00 USD |
| `1D` | `0.0800` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 48,550.00 USD | 9,760.00 USD | 94,110.00 USD |
| `1D` | `0.0801` | 21,520,000.00 USD | 21,520,000.00 USD | 0.00 USD | 25,740.00 USD | 0.00 USD | 2,400.00 USD |
| `7D` | `0.0801` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 85,040.00 USD | 0.00 USD | 104,840.00 USD |
| `1D` | `0.0802` | 21,550,000.00 USD | 21,550,000.00 USD | 0.00 USD | 25,490.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 21,660,000.00 USD | 21,660,000.00 USD | 0.00 USD | 24,020.00 USD | 43,340.00 USD | 37,070.00 USD |
| `7D` | `0.0803` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 1,480.00 USD |
| `1D` | `0.0804` | 21,670,000.00 USD | 21,670,000.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 21,840,000.00 USD | 21,840,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD |
| `7D` | `0.0805` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 228,320.00 USD | 43,910.00 USD | 53,390.00 USD |
| `1D` | `0.0806` | 22,100,000.00 USD | 22,100,000.00 USD | 0.00 USD | 28,730.00 USD | 21,040.00 USD | 215,620.00 USD |
| `1D` | `0.0807` | 22,510,000.00 USD | 22,510,000.00 USD | 0.00 USD | 228,350.00 USD | 143,670.00 USD | 32,620.00 USD |
| `7D` | `0.0807` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 217,720.00 USD | 934,840.00 USD | 294,860.00 USD |
| `1D` | `0.0808` | 23,160,000.00 USD | 23,160,000.00 USD | 0.00 USD | 150,860.00 USD | 116,140.00 USD | 381,410.00 USD |
| `1D` | `0.0809` | 23,500,000.00 USD | 23,500,000.00 USD | 0.00 USD | 109,380.00 USD | 220,760.00 USD | 12,350.00 USD |
| `7D` | `0.0809` | 22,570,000.00 USD | 22,570,000.00 USD | 0.00 USD | 9,880.00 USD | 1,760,000.00 USD | 1,700.00 USD |
| `1D` | `0.0810` | 23,950,000.00 USD | 23,950,000.00 USD | 0.00 USD | 192,870.00 USD | 127,690.00 USD | 132,060.00 USD |
| `1D` | `0.0811` | 24,200,000.00 USD | 24,200,000.00 USD | 0.00 USD | 100,060.00 USD | 139,750.00 USD | 12,540.00 USD |
| `7D` | `0.0811` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 131,030.00 USD | 730,620.00 USD | 1,610.00 USD |
| `1D` | `0.0812` | 24,480,000.00 USD | 24,480,000.00 USD | 0.00 USD | 135,690.00 USD | 102,020.00 USD | 38,870.00 USD |
| `1D` | `0.0813` | 24,660,000.00 USD | 24,660,000.00 USD | 0.00 USD | 39,090.00 USD | 29,030.00 USD | 109,010.00 USD |
| `7D` | `0.0813` | 24,500,000.00 USD | 24,500,000.00 USD | 0.00 USD | 517,320.00 USD | 548,390.00 USD | 2,470.00 USD |
| `1D` | `0.0814` | 24,960,000.00 USD | 24,960,000.00 USD | 0.00 USD | 43,650.00 USD | 108,690.00 USD | 148,070.00 USD |
| `1D` | `0.0815` | 25,080,000.00 USD | 25,080,000.00 USD | 0.00 USD | 20,890.00 USD | 6,740.00 USD | 94,630.00 USD |
| `7D` | `0.0815` | 26,110,000.00 USD | 26,110,000.00 USD | 0.00 USD | 671,840.00 USD | 643,990.00 USD | 300,370.00 USD |
| `1D` | `0.0816` | 25,780,000.00 USD | 25,780,000.00 USD | 0.00 USD | 323,740.00 USD | 194,310.00 USD | 177,840.00 USD |
| `1D` | `0.0817` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 280,410.00 USD | 134,560.00 USD | 130,180.00 USD |
| `7D` | `0.0817` | 28,680,000.00 USD | 28,680,000.00 USD | 0.00 USD | 1,200,000.00 USD | 745,850.00 USD | 614,910.00 USD |
| `1D` | `0.0818` | 26,980,000.00 USD | 26,980,000.00 USD | 0.00 USD | 234,840.00 USD | 161,260.00 USD | 268,280.00 USD |
| `1D` | `0.0819` | 27,580,000.00 USD | 27,580,000.00 USD | 0.00 USD | 156,470.00 USD | 312,480.00 USD | 128,570.00 USD |
| `7D` | `0.0819` | 30,790,000.00 USD | 30,790,000.00 USD | 0.00 USD | 672,340.00 USD | 512,490.00 USD | 929,000.00 USD |
| `1D` | `0.0820` | 28,120,000.00 USD | 28,120,000.00 USD | 0.00 USD | 46,550.00 USD | 172,050.00 USD | 319,890.00 USD |
| `1D` | `0.0821` | 28,400,000.00 USD | 28,400,000.00 USD | 0.00 USD | 145,950.00 USD | 48,110.00 USD | 84,710.00 USD |
| `7D` | `0.0821` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 1,210,000.00 USD | 760,670.00 USD | 390,320.00 USD |
| `1D` | `0.0822` | 28,960,000.00 USD | 28,960,000.00 USD | 0.00 USD | 249,310.00 USD | 151,600.00 USD | 157,000.00 USD |
| `1D` | `0.0823` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 267,050.00 USD | 72,540.00 USD | 8,640.00 USD |
| `7D` | `0.0823` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 884,810.00 USD | 520,900.00 USD | 366,690.00 USD |
| `1D` | `0.0824` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 168,680.00 USD | 204,930.00 USD | 190,720.00 USD |
| `1D` | `0.0825` | 30,120,000.00 USD | 30,120,000.00 USD | 0.00 USD | 102,430.00 USD | 125,690.00 USD | 21,980.00 USD |
| `7D` | `0.0825` | 36,500,000.00 USD | 36,500,000.00 USD | 0.00 USD | 761,460.00 USD | 514,320.00 USD | 307,380.00 USD |
| `1D` | `0.0826` | 30,550,000.00 USD | 30,550,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 171,760.00 USD |
| `1D` | `0.0827` | 30,640,000.00 USD | 30,640,000.00 USD | 0.00 USD | 13,110.00 USD | 62,900.00 USD | 16,670.00 USD |
| `7D` | `0.0827` | 37,650,000.00 USD | 37,650,000.00 USD | 0.00 USD | 658,340.00 USD | 220,660.00 USD | 271,680.00 USD |
| `1D` | `0.0828` | 30,970,000.00 USD | 30,970,000.00 USD | 0.00 USD | 189,510.00 USD | 75,940.00 USD | 65,050.00 USD |
| `1D` | `0.0829` | 31,250,000.00 USD | 31,250,000.00 USD | 0.00 USD | 182,550.00 USD | 89,690.00 USD | 8,010.00 USD |
| `7D` | `0.0829` | 38,690,000.00 USD | 38,690,000.00 USD | 0.00 USD | 645,990.00 USD | 177,740.00 USD | 214,060.00 USD |
| `1D` | `0.0830` | 31,390,000.00 USD | 31,390,000.00 USD | 0.00 USD | 54,060.00 USD | 37,820.00 USD | 42,560.00 USD |
| `1D` | `0.0831` | 31,470,000.00 USD | 31,470,000.00 USD | 0.00 USD | 22,160.00 USD | 16,920.00 USD | 45,280.00 USD |
| `7D` | `0.0831` | 39,590,000.00 USD | 39,590,000.00 USD | 0.00 USD | 452,190.00 USD | 160,720.00 USD | 288,260.00 USD |
| `1D` | `0.0832` | 31,850,000.00 USD | 31,850,000.00 USD | 0.00 USD | 184,130.00 USD | 93,160.00 USD | 100,760.00 USD |
| `1D` | `0.0833` | 32,270,000.00 USD | 32,270,000.00 USD | 0.00 USD | 125,800.00 USD | 111,030.00 USD | 181,320.00 USD |
| `7D` | `0.0833` | 40,810,000.00 USD | 40,810,000.00 USD | 0.00 USD | 524,880.00 USD | 414,820.00 USD | 276,510.00 USD |
| `1D` | `0.0834` | 32,650,000.00 USD | 32,650,000.00 USD | 0.00 USD | 123,760.00 USD | 118,950.00 USD | 143,830.00 USD |
| `1D` | `0.0835` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 109,250.00 USD | 188,990.00 USD | 64,130.00 USD |
| `7D` | `0.0835` | 41,970,000.00 USD | 41,970,000.00 USD | 0.00 USD | 365,460.00 USD | 261,800.00 USD | 536,330.00 USD |
| `1D` | `0.0836` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 44,050.00 USD | 74,690.00 USD | 148,530.00 USD |
| `1D` | `0.0837` | 33,510,000.00 USD | 33,510,000.00 USD | 0.00 USD | 130,410.00 USD | 29,090.00 USD | 62,750.00 USD |
| `7D` | `0.0837` | 42,770,000.00 USD | 42,770,000.00 USD | 0.00 USD | 453,970.00 USD | 227,430.00 USD | 115,210.00 USD |
| `1D` | `0.0838` | 33,780,000.00 USD | 33,780,000.00 USD | 0.00 USD | 150,900.00 USD | 81,260.00 USD | 42,490.00 USD |
| `7D` | `0.0839` | 43,250,000.00 USD | 43,250,000.00 USD | 0.00 USD | 321,350.00 USD | 128,090.00 USD | 36,900.00 USD |
| `7D` | `0.0841` | 43,520,000.00 USD | 43,520,000.00 USD | 0.00 USD | 205,170.00 USD | 0.00 USD | 64,950.00 USD |
| `7D` | `0.0843` | 44,020,000.00 USD | 44,020,000.00 USD | 0.00 USD | 337,540.00 USD | 77,640.00 USD | 85,070.00 USD |
| `7D` | `0.0845` | 44,490,000.00 USD | 44,490,000.00 USD | 0.00 USD | 234,950.00 USD | 95,020.00 USD | 138,940.00 USD |
| `7D` | `0.0847` | 45,000,000.00 USD | 45,000,000.00 USD | 0.00 USD | 244,090.00 USD | 190,180.00 USD | 77,700.00 USD |
| `7D` | `0.0849` | 45,730,000.00 USD | 45,730,000.00 USD | 0.00 USD | 310,690.00 USD | 205,870.00 USD | 208,400.00 USD |
| `7D` | `0.0850` | 46,060,000.00 USD | 46,060,000.00 USD | 0.00 USD | 87,360.00 USD | 53,240.00 USD | 186,300.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.05B` | Total OI Tokens: `14,000,732,249.0 DOGE`
  * 1h OI Change: `-0.39%` | 4h OI Change: `-1.09%` | 24h OI Change: `-5.56%`
  * Exchange Breakdown: Binance=`239.55M` | Bybit=`106.37M` | OKX=`109.77M` | Hyperliquid=`75.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `27.60K` | Last 24h: `49.48K` | Last 3d: `238.63K` | Last 7d: `304.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0009%` |
| **USDT Bybit** | `0.0058%` | **USDT KuCoin** | `0.0076%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0029%` | **USDT Bitget** | `0.0020%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `47.18%` | `52.82%` | `0.89` | 67,400,000.00 USD |
| `15M` | `Binance` | `46.56%` | `53.44%` | `0.87` | 19,270,000.00 USD |
| `15M` | `OKX` | `43.72%` | `56.28%` | `0.78` | 16,490,000.00 USD |
| `15M` | `Bybit` | `35.36%` | `64.64%` | `0.55` | 5,710,000.00 USD |
| `15M` | `KuCoin` | `54.72%` | `45.28%` | `1.21` | 280,290.00 USD |
| `15M` | `Gate` | `48.23%` | `51.77%` | `0.93` | 8,050,000.00 USD |
| `15M` | `Bitget` | `43.33%` | `56.67%` | `0.76` | 2,910,000.00 USD |
| `15M` | `BingX` | `51.58%` | `48.42%` | `1.07` | 2,950,000.00 USD |
| `15M` | `MEXC` | `66.63%` | `33.37%` | `2.00` | 2,910,000.00 USD |
| `15M` | `Bitunix` | `53.72%` | `46.28%` | `1.16` | 2,510,000.00 USD |
| `15M` | `Hyperliquid` | `49.26%` | `50.74%` | `0.97` | 1,990,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.1%` | `50.9%` | `0.96` | 1,500,000.00 USD |
| `15M` | `Crypto.com` | `42.97%` | `57.03%` | `0.75` | 395,690.00 USD |
| `15M` | `WhiteBIT` | `98.42%` | `1.58%` | `62.29` | 1,060,000.00 USD |
| `15M` | `HTX` | `75.95%` | `24.05%` | `3.16` | 60,840.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `28.12%` | `71.88%` | `0.39` | 530,780.00 USD |
| `15M` | `Aster` | `43.66%` | `56.34%` | `0.77` | 295,870.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.77%` | `50.23%` | `0.99` | 481,230.00 USD |
| `15M` | `Whale Positions` | `46.56%` | `53.44%` | `0.87` | 19,270,000.00 USD |
| `15M` | `Global Accounts` | `47.18%` | `52.82%` | `0.89` | 67,400,000.00 USD |
| `1H` | `DOGE` | `42.71%` | `57.29%` | `0.75` | 34,110,000.00 USD |
| `1H` | `Binance` | `43.19%` | `56.81%` | `0.76` | 11,580,000.00 USD |
| `1H` | `OKX` | `44.71%` | `55.29%` | `0.81` | 7,870,000.00 USD |
| `1H` | `Bybit` | `45.93%` | `54.07%` | `0.85` | 2,510,000.00 USD |
| `1H` | `KuCoin` | `40.22%` | `59.78%` | `0.67` | 274,890.00 USD |
| `1H` | `Gate` | `44.06%` | `55.94%` | `0.79` | 5,610,000.00 USD |
| `1H` | `Bitget` | `39.59%` | `60.41%` | `0.66` | 508,370.00 USD |
| `1H` | `BingX` | `51.18%` | `48.82%` | `1.05` | 606,340.00 USD |
| `1H` | `MEXC` | `61.53%` | `38.47%` | `1.60` | 1,070,000.00 USD |
| `1H` | `Bitunix` | `41.06%` | `58.94%` | `0.70` | 688,060.00 USD |
| `1H` | `Hyperliquid` | `48.34%` | `51.66%` | `0.94` | 254,620.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.9%` | `57.1%` | `0.75` | 228,910.00 USD |
| `1H` | `Crypto.com` | `40.86%` | `59.14%` | `0.69` | 42,440.00 USD |
| `1H` | `WhiteBIT` | `14.14%` | `85.86%` | `0.16` | 2,140,000.00 USD |
| `1H` | `HTX` | `53.2%` | `46.8%` | `1.14` | 189,220.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.43%` | `53.57%` | `0.87` | 322,870.00 USD |
| `1H` | `Aster` | `29.85%` | `70.15%` | `0.43` | 197,760.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `74.09%` | `25.91%` | `2.86` | 16,790.00 USD |
| `1H` | `Whale Positions` | `43.19%` | `56.81%` | `0.76` | 11,580,000.00 USD |
| `1H` | `Global Accounts` | `42.71%` | `57.29%` | `0.75` | 34,110,000.00 USD |
| `4H` | `DOGE` | `44.07%` | `55.93%` | `0.79` | 159,190,000.00 USD |
| `4H` | `Binance` | `44.4%` | `55.6%` | `0.80` | 58,990,000.00 USD |
| `4H` | `OKX` | `45.65%` | `54.35%` | `0.84` | 33,840,000.00 USD |
| `4H` | `Bybit` | `42.49%` | `57.51%` | `0.74` | 10,680,000.00 USD |
| `4H` | `KuCoin` | `44.37%` | `55.63%` | `0.80` | 1,070,000.00 USD |
| `4H` | `Gate` | `46.5%` | `53.5%` | `0.87` | 26,590,000.00 USD |
| `4H` | `Bitget` | `41.14%` | `58.86%` | `0.70` | 3,060,000.00 USD |
| `4H` | `BingX` | `36.62%` | `63.38%` | `0.58` | 2,890,000.00 USD |
| `4H` | `MEXC` | `41.39%` | `58.61%` | `0.71` | 9,680,000.00 USD |
| `4H` | `Bitunix` | `47.61%` | `52.39%` | `0.91` | 3,880,000.00 USD |
| `4H` | `Hyperliquid` | `54.87%` | `45.13%` | `1.22` | 1,250,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.86%` | `50.14%` | `0.99` | 1,120,000.00 USD |
| `4H` | `Crypto.com` | `35.64%` | `64.36%` | `0.55` | 200,060.00 USD |
| `4H` | `WhiteBIT` | `20.27%` | `79.73%` | `0.25` | 3,860,000.00 USD |
| `4H` | `HTX` | `42.01%` | `57.99%` | `0.72` | 714,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.92%` | `51.08%` | `0.96` | 434,300.00 USD |
| `4H` | `Aster` | `37.91%` | `62.09%` | `0.61` | 898,020.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `63.58%` | `36.42%` | `1.75` | 34,600.00 USD |
| `4H` | `Whale Positions` | `44.4%` | `55.6%` | `0.80` | 58,990,000.00 USD |
| `4H` | `Global Accounts` | `44.07%` | `55.93%` | `0.79` | 159,190,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0762` | `0.0762` | `0.0762` | `0.0763` | `0.0760` | 2,543,107.52 USD | 868,277.41 USD | 1,674,830.11 USD | -806,552.70 USD | `-31.72%` | `2B / 3S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0763` | `0.0755` | 6,345,196.06 USD | 2,713,125.81 USD | 3,632,070.25 USD | -918,944.44 USD | `-14.48%` | `8B / 18S` |
| `5:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0755` | 3,504,858.24 USD | 1,671,375.40 USD | 1,833,482.84 USD | -162,107.45 USD | `-4.63%` | `6B / 5S` |
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0759` | `0.0755` | 6,252,708.50 USD | 2,400,535.02 USD | 3,852,173.48 USD | -1,451,638.46 USD | `-23.22%` | `9B / 7S` |
| `5:00 UTC` | `0.0758` | `0.0759` | `0.0758` | `0.0761` | `0.0758` | 3,515,276.40 USD | 1,545,960.58 USD | 1,969,315.82 USD | -423,355.24 USD | `-12.04%` | `4B / 6S` |
| `0:00 UTC` | `0.0757` | `0.0757` | `0.0757` | `0.0759` | `0.0755` | 2,056,025.64 USD | 709,276.38 USD | 1,346,749.25 USD | -637,472.87 USD | `-31.01%` | `2B / 13S` |
| `5:00 UTC` | `0.0754` | `0.0755` | `0.0754` | `0.0757` | `0.0753` | 2,905,242.56 USD | 1,422,846.87 USD | 1,482,395.68 USD | -59,548.81 USD | `-2.05%` | `8B / 3S` |
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0754` | 2,313,298.65 USD | 1,197,641.49 USD | 1,115,657.16 USD | 81,984.32 USD | `+3.54%` | `3B / 4S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0756` | `0.0753` | 2,260,519.88 USD | 1,007,921.72 USD | 1,252,598.16 USD | -244,676.43 USD | `-10.82%` | `2B / 8S` |
| `0:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0755` | `0.0752` | 1,765,150.27 USD | 694,824.11 USD | 1,070,326.16 USD | -375,502.05 USD | `-21.27%` | `3B / 8S` |

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
| `5m` | -23,380.00 USD | 243,930.00 USD | **`ACCUMULATION`** |
| `15m` | -78,390.00 USD | -187,250.00 USD | **`DISTRIBUTION`** |
| `30m` | -667,520.00 USD | -1,140,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -958,260.00 USD | -1,950,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -766,060.00 USD | -6,900,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,960,000.00 USD | -10,960,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -89,950.00 USD | -11,130,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 2,480,000.00 USD | -14,030,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,540,000.00 USD | -29,440,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,090,000.00 USD | -66,190,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -61,040,000.00 USD | -195,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -284,660,000.00 USD | -809,260,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-23.38K` | 15m=`-78.39K` | 1h=`-958.26K` | 24h=`-18.09M`
* Futures Capital Netflows: 5m=`+243.93K` | 15m=`-187.25K` | 1h=`-1.95M` | 24h=`-66.19M`
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
  * `2026-10-30 14:41:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:27 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0700` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0842`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0755` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0792` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0650`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0761`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
