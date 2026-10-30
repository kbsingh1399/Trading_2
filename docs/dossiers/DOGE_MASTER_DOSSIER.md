# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 15:42:19 IST` (`2026-10-30 10:12:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0742` | **Live Ask Quote**: `0.0763` | **Mid Price**: `0.0753`
- **Spread Points**: `21.00` | **Spread BPS**: `279.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0737` | VWAP Z-Score: `+0.62` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000413` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.05` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0769` | Lower -3.00σ Band: `0.0706`
  * Upper +2.51σ Band: `0.0764` | Lower -2.51σ Band: `0.0711`
  * Upper +2.01σ Band: `0.0758` | Lower -2.01σ Band: `0.0716`
  * Upper +2.00σ Band: `0.0758` | Lower -2.00σ Band: `0.0717`
  * Upper +1.28σ Band: `0.0751` | Lower -1.28σ Band: `0.0724`
  * Upper +1.00σ Band: `0.0748` | Lower -1.00σ Band: `0.0727`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0745` | EMA-20=`0.0746` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0749` (Slope: `+0.0000`) | EMA-100=`0.0757`
  * Institutional Anchors: EMA-144=`0.0761` | EMA-200=`0.0764` (Slope: `-0.3126`) | EMA-233=`0.0765`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0755` (Distance: `-0.33%`)
  * Point of Control (POC) = `0.0749` (Distance: `+0.48%`)
  * Value Area Low (VAL) = `0.0737` (Distance: `+2.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0783` | Weekly POC=`0.0762` | Weekly VAL=`0.0747`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0756` | Low=`0.0741`
  * New York Session (13:00-21:00 UTC): High=`0.0744` | Low=`0.0741`
  * Initial Balance (First Hour): IB High=`0.0754` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0749` - `0.0756`
  * Optimal Trade Entry (OTE 0.705): `0.0754`
  * Structural Invalidation Anchor (0.786): `0.0759`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0755` | `0.0755` | `0.0753` | `0.0754` | `8,249,459` | 621,918.13 USD | -70,050.36 USD | `-11.26%` | -37,016,266.92 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0755` | `0.0755` | `0.0753` | `0.0754` | `8,612,207` | 649,119.21 USD | -175,034.09 USD | `-26.96%` | -37,191,301.02 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0754` | `0.0755` | `0.0754` | `0.0755` | `4,031,199` | 303,972.63 USD | 41,714.26 USD | `+13.72%` | -37,149,586.76 USD | `+0.48` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.0754` | `0.0756` | `0.0752` | `0.0755` | `38,749,584` | 2,922,007.92 USD | -254,756.96 USD | `-8.72%` | -36,007,740.52 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0755` | `0.0755` | `0.0753` | `0.0755` | `20,913,841` | 1,576,593.18 USD | -202,690.36 USD | `-12.86%` | -36,210,430.88 USD | `+0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0755` | `0.0755` | `0.0752` | `0.0753` | `35,544,827` | 2,676,306.51 USD | -266,766.75 USD | `-9.97%` | -36,477,197.63 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0756` | `0.0761` | `0.0753` | `0.0756` | `194,653,019` | 14,729,253.09 USD | -2,572,015.39 USD | `-17.46%` | -35,337,222.98 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0756` | `0.0758` | `0.0752` | `0.0755` | `120,232,507` | 9,072,419.63 USD | -620,139.43 USD | `-6.84%` | -35,957,362.42 USD | `+0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0755` | `0.0755` | `0.0752` | `0.0753` | `34,571,084` | 2,602,937.02 USD | -339,135.27 USD | `-13.03%` | -36,296,497.69 USD | `+0.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0752` | `0.0755` | `314,850,939` | 23,799,062.29 USD | -3,191,807.43 USD | `-13.41%` | -34,891,016.14 USD | `+0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | 1,581,082.63 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -21,458,643.59 USD | `-1.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0752` | `0.0753` | `350,430,450` | 26,477,986.54 USD | -3,458,928.88 USD | `-13.06%` | -35,158,137.59 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0753`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0753` | `16205.0000` | 1,220.98 USD | 1,261.15 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0753` | `14044.0000` | 1,058.10 USD | 2,319.25 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0753` | `10533.0000` | 793.51 USD | 3,112.76 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0753` | `14044.0000` | 1,058.00 USD | 4,170.77 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0753` | `31306.0000` | 2,358.34 USD | 6,529.11 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0753` | `10533.0000` | 793.44 USD | 7,322.55 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0753` | `2583.0000` | 194.57 USD | 7,517.12 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0753` | `2293.0000` | 172.72 USD | 7,689.84 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0753` | `410785.0000` | 30,941.97 USD | 38,631.81 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0753` | `69659.0000` | 5,246.92 USD | 43,878.73 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0753` | `116966.0000` | 8,810.11 USD | 52,688.85 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0753` | `14044.0000` | 1,057.81 USD | 53,746.66 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0753` | `52968.0000` | 3,989.50 USD | 57,736.15 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0753` | `23520.0000` | 1,771.36 USD | 59,507.51 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0753` | `125429.0000` | 9,446.31 USD | 68,953.82 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `0.0753` | `14044.0000` | 1,057.67 USD | 70,011.49 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0753` | `124976.0000` | 9,411.94 USD | 79,423.43 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0753` | `453411.0000` | 34,145.93 USD | 113,569.36 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0753` | `7509.0000` | 565.47 USD | 114,134.84 USD | `1 orders` | `-0.06%` | `-` |
| `ASK` | `0.0754` | `19236.0000` | 1,449.93 USD | 155,751.58 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0754` | `453030.0000` | 34,147.14 USD | 154,301.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0754` | `37564.0000` | 2,831.35 USD | 120,154.51 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0754` | `38316.0000` | 2,887.99 USD | 117,323.16 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0754` | `19899.0000` | 1,499.83 USD | 114,435.17 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `143735.0000` | 10,833.45 USD | 112,935.34 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `108177.0000` | 8,153.30 USD | 102,101.89 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `50520.0000` | 3,807.64 USD | 93,948.59 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `59771.0000` | 4,504.82 USD | 90,140.95 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `19902.0000` | 1,499.95 USD | 85,636.13 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `89522.0000` | 6,746.92 USD | 84,136.17 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `430486.0000` | 32,443.58 USD | 77,389.26 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `19902.0000` | 1,499.89 USD | 44,945.68 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `19902.0000` | 1,499.87 USD | 43,445.79 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `112790.0000` | 8,500.08 USD | 41,945.91 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `87201.0000` | 6,571.47 USD | 33,445.83 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `52505.0000` | 3,956.72 USD | 26,874.36 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `248825.0000` | 18,750.95 USD | 22,917.64 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `2786.0000` | 209.94 USD | 4,166.68 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `0.0754` | `52508.0000` | 3,956.74 USD | 3,956.74 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0754` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0754` | `533.0000` | 40.16 USD | 40.16 USD | `2 orders` | `-0.00%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `307` | `0xb83d...6e36` | `SHORT` | 7,734,883.68 USD | `102,645,925.00` | `0.0946` | `0.0753` | `1.17` | 1,972,457.97 USD | `+25.50%` | `3X Cross` |
| `314` | `0xc63a...a3cd` | `LONG` | 7,536,200.00 USD | `100,000,000.00` | `0.0856` | `0.0753` | `0.000000` | -1,028,621.96 USD | `-13.65%` | `10X Cross` |
| `316` | `0x610b...b613` | `LONG` | 7,435,797.71 USD | `98,666,424.00` | `0.0872` | `0.0753` | `0.0606` | -1,164,384.19 USD | `-15.66%` | `5X Cross` |
| `600` | `0x5b5d...c060` | `SHORT` | 3,734,226.21 USD | `49,478,955.00` | `0.0946` | `0.0753` | `2.99` | 947,290.39 USD | `+25.37%` | `3X Cross` |
| `640` | `0xca49...53c8` | `SHORT` | 3,506,802.43 USD | `46,542,649.00` | `0.0929` | `0.0753` | `0.3968` | 819,242.25 USD | `+23.36%` | `10X Cross` |
| `654` | `0x45d2...4029` | `SHORT` | 3,422,531.12 USD | `45,426,000.00` | `0.0954` | `0.0753` | `0.9839` | 913,098.10 USD | `+26.68%` | `10X Cross` |
| `658` | `0xecb6...2b00` | `SHORT` | 3,396,284.74 USD | `45,070,463.00` | `0.0787` | `0.0753` | `0.7396` | 150,272.63 USD | `+4.42%` | `10X Cross` |
| `1185` | `0x458d...ab3b` | `LONG` | 1,842,735.92 USD | `24,454,063.00` | `0.1002` | `0.0753` | `0.0714` | -608,185.99 USD | `-33.00%` | `3X Isolated` |
| `1192` | `0xeadc...9d55` | `LONG` | 1,835,261.51 USD | `24,317,440.00` | `0.0926` | `0.0753` | `0.000000` | -416,333.06 USD | `-22.69%` | `10X Cross` |
| `1334` | `0xf48f...10fe` | `LONG` | 1,614,871.46 USD | `21,424,497.00` | `0.0968` | `0.0753` | `0.0470` | -459,433.14 USD | `-28.45%` | `4X Cross` |
| `1364` | `0x9946...0852` | `SHORT` | 1,570,148.89 USD | `20,845,267.00` | `0.0859` | `0.0753` | `0.1509` | 221,137.12 USD | `+14.08%` | `10X Cross` |
| `1598` | `0x0d6a...ca57` | `LONG` | 1,328,594.05 USD | `17,626,455.00` | `0.0875` | `0.0753` | `0.0626` | -213,510.91 USD | `-16.07%` | `3X Isolated` |
| `1661` | `0x4808...a82c` | `LONG` | 1,267,680.84 USD | `16,828,143.00` | `0.0883` | `0.0753` | `0.0632` | -218,792.14 USD | `-17.26%` | `3X Cross` |
| `1719` | `0x9aa5...58af` | `SHORT` | 1,222,827.03 USD | `16,232,720.00` | `0.0907` | `0.0753` | `0.6360` | 248,969.25 USD | `+20.36%` | `10X Cross` |
| `1752` | `0xcac1...26b3` | `SHORT` | 1,185,589.24 USD | `15,731,715.00` | `0.0943` | `0.0753` | `0.6243` | 297,997.11 USD | `+25.13%` | `10X Cross` |
| `1797` | `0x31ef...f715` | `LONG` | 1,149,491.95 USD | `15,230,102.00` | `0.0936` | `0.0753` | `0.0668` | -276,203.98 USD | `-24.03%` | `3X Isolated` |
| `1823` | `0xbfc7...80b4` | `SHORT` | 1,133,153.86 USD | `15,020,000.00` | `0.0920` | `0.0753` | `0.1762` | 249,245.43 USD | `+22.00%` | `10X Cross` |
| `1905` | `0x7cee...fc93` | `SHORT` | 1,056,096.99 USD | `14,013,468.00` | `0.0863` | `0.0753` | `0.2628` | 152,780.37 USD | `+14.47%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 7,301.12 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.30K USD at 0.0796 USD [API] | `2026-10-29 18:04:30` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 6,511.06 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.51K USD at 0.0796 USD [API] | `2026-10-29 18:04:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.82%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.02%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.82%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.02%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.82%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.02%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.82%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.02%`)
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
| `1D` | `Long Liquidation` | `0.0677` | 17,800,000.00 USD | 17,800,000.00 USD | 48,630.00 USD | 94,020.00 USD | 16,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0677` | 29,410,000.00 USD | 29,410,000.00 USD | 10,470.00 USD | 0.00 USD | 475.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 17,640,000.00 USD | 17,640,000.00 USD | 29,490.00 USD | 42,100.00 USD | 72,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 17,500,000.00 USD | 17,500,000.00 USD | 72,650.00 USD | 41,660.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0679` | 29,390,000.00 USD | 29,390,000.00 USD | 6,140.00 USD | 59,770.00 USD | 61,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 17,380,000.00 USD | 17,380,000.00 USD | 51,160.00 USD | 41,240.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 667.50 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 17,240,000.00 USD | 17,240,000.00 USD | 36,810.00 USD | 58,950.00 USD | 149,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0681` | 29,270,000.00 USD | 29,270,000.00 USD | 118,640.00 USD | 61,880.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0682` | 17,000,000.00 USD | 17,000,000.00 USD | 14,920.00 USD | 55,530.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,770.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 16,900,000.00 USD | 16,900,000.00 USD | 15,780.00 USD | 32,190.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0683` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 58,370.00 USD | 66,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 16,850,000.00 USD | 16,850,000.00 USD | 24,150.00 USD | 24,010.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 79,490.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 16,800,000.00 USD | 16,800,000.00 USD | 58,140.00 USD | 18,250.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0685` | 28,800,000.00 USD | 28,800,000.00 USD | 142,840.00 USD | 77,920.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 8,890.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 16,690,000.00 USD | 16,690,000.00 USD | 56,540.00 USD | 16,290.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 4,840.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 16,600,000.00 USD | 16,600,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0687` | 28,550,000.00 USD | 28,550,000.00 USD | 101,720.00 USD | 128,090.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 16,520,000.00 USD | 16,520,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 38,040.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 16,460,000.00 USD | 16,460,000.00 USD | 10,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0689` | 28,320,000.00 USD | 28,320,000.00 USD | 225,480.00 USD | 77,640.00 USD | 61,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 508,320.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 10,030.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 16,450,000.00 USD | 16,450,000.00 USD | 1,460.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0691` | 27,960,000.00 USD | 27,960,000.00 USD | 162,010.00 USD | 95,020.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 16,450,000.00 USD | 16,450,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,140.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 16,430,000.00 USD | 16,430,000.00 USD | 18,220.00 USD | 0.00 USD | 670.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0693` | 27,570,000.00 USD | 27,570,000.00 USD | 207,150.00 USD | 190,180.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 16,410,000.00 USD | 16,410,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 16,380,000.00 USD | 16,380,000.00 USD | 2,070.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0695` | 27,090,000.00 USD | 27,090,000.00 USD | 282,470.00 USD | 212,530.00 USD | 212,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 4,950.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 16,380,000.00 USD | 16,380,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0697` | 26,380,000.00 USD | 26,380,000.00 USD | 142,190.00 USD | 148,620.00 USD | 263,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 6,970.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 16,310,000.00 USD | 16,310,000.00 USD | 10,960.00 USD | 10,400.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,910.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 16,280,000.00 USD | 16,280,000.00 USD | 38,680.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0699` | 25,830,000.00 USD | 25,830,000.00 USD | 325,570.00 USD | 205,450.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 16,240,000.00 USD | 16,240,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 16,120,000.00 USD | 16,120,000.00 USD | 39,680.00 USD | 108,360.00 USD | 37.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0701` | 25,160,000.00 USD | 25,160,000.00 USD | 283,670.00 USD | 119,790.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,180.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 15,970,000.00 USD | 15,970,000.00 USD | 45,890.00 USD | 11,420.00 USD | 122.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,300.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 15,910,000.00 USD | 15,910,000.00 USD | 140,500.00 USD | 58,070.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0703` | 24,610,000.00 USD | 24,610,000.00 USD | 261,240.00 USD | 120,430.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 3,790.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 15,710,000.00 USD | 15,710,000.00 USD | 5,220.00 USD | 31,030.00 USD | 20,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 780.37 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 15,650,000.00 USD | 15,650,000.00 USD | 41,460.00 USD | 43,660.00 USD | 34,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0705` | 24,180,000.00 USD | 24,180,000.00 USD | 224,080.00 USD | 133,180.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 15,530,000.00 USD | 15,530,000.00 USD | 22,880.00 USD | 6,490.00 USD | 15,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 608.86 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 15,490,000.00 USD | 15,490,000.00 USD | 136,920.00 USD | 57,570.00 USD | 47,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0707` | 23,650,000.00 USD | 23,650,000.00 USD | 171,490.00 USD | 37,160.00 USD | 156,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 15,250,000.00 USD | 15,250,000.00 USD | 69,400.00 USD | 55,430.00 USD | 105,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 15,020,000.00 USD | 15,020,000.00 USD | 38,730.00 USD | 82,680.00 USD | 149,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0709` | 23,280,000.00 USD | 23,280,000.00 USD | 485,290.00 USD | 159,720.00 USD | 139,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 14,740,000.00 USD | 14,740,000.00 USD | 117,230.00 USD | 92,490.00 USD | 120,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 4,720.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 14,410,000.00 USD | 14,410,000.00 USD | 49,210.00 USD | 26,550.00 USD | 45,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0711` | 22,500,000.00 USD | 22,500,000.00 USD | 285,730.00 USD | 252,130.00 USD | 91,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,860.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 14,290,000.00 USD | 14,290,000.00 USD | 165,590.00 USD | 47,430.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 14,080,000.00 USD | 14,080,000.00 USD | 75,840.00 USD | 89,050.00 USD | 63,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0713` | 21,870,000.00 USD | 21,870,000.00 USD | 379,600.00 USD | 171,480.00 USD | 139,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 13,850,000.00 USD | 13,850,000.00 USD | 120,780.00 USD | 49,200.00 USD | 46,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 13,270.00 USD | 408,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 13,630,000.00 USD | 13,630,000.00 USD | 81,850.00 USD | 236,640.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0715` | 21,180,000.00 USD | 21,180,000.00 USD | 211,700.00 USD | 51,460.00 USD | 66,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 394,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 13,270,000.00 USD | 13,270,000.00 USD | 19,480.00 USD | 49,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 3,840.00 USD | 386,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 13,200,000.00 USD | 13,200,000.00 USD | 238,310.00 USD | 96,820.00 USD | 837.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0717` | 20,850,000.00 USD | 20,850,000.00 USD | 285,100.00 USD | 190,890.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 48,180.00 USD | 382,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 12,870,000.00 USD | 12,870,000.00 USD | 64,570.00 USD | 97,660.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,090.00 USD | 334,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 12,690,000.00 USD | 12,690,000.00 USD | 229,400.00 USD | 78,600.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0719` | 20,320,000.00 USD | 20,320,000.00 USD | 233,070.00 USD | 63,390.00 USD | 276,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 333,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 12,310,000.00 USD | 12,310,000.00 USD | 138,650.00 USD | 40,840.00 USD | 72,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 5,090.00 USD | 331,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 12,060,000.00 USD | 12,060,000.00 USD | 308,410.00 USD | 260,370.00 USD | 66,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0721` | 19,750,000.00 USD | 19,750,000.00 USD | 422,700.00 USD | 285,460.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 613.35 USD | 326,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 11,420,000.00 USD | 11,420,000.00 USD | 181,970.00 USD | 130,710.00 USD | 151,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 38,340.00 USD | 326,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 10,960,000.00 USD | 10,960,000.00 USD | 116,520.00 USD | 251,210.00 USD | 343,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0723` | 18,950,000.00 USD | 18,950,000.00 USD | 242,550.00 USD | 148,860.00 USD | 110,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 286,760.00 USD | 287,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 10,250,000.00 USD | 10,250,000.00 USD | 224,260.00 USD | 249,960.00 USD | 401,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 984.89 USD | 984.89 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 9,370,000.00 USD | 9,370,000.00 USD | 263,550.00 USD | 255,920.00 USD | 311,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0725` | 18,440,000.00 USD | 18,440,000.00 USD | 1,070,000.00 USD | 365,360.00 USD | 152,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 8,540,000.00 USD | 8,540,000.00 USD | 153,630.00 USD | 149,300.00 USD | 59,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 8,180,000.00 USD | 8,180,000.00 USD | 190,550.00 USD | 160,860.00 USD | 40,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0727` | 16,860,000.00 USD | 16,860,000.00 USD | 249,200.00 USD | 432,030.00 USD | 92,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 7,780,000.00 USD | 7,780,000.00 USD | 60,510.00 USD | 154,910.00 USD | 47,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 7,520,000.00 USD | 7,520,000.00 USD | 58,550.00 USD | 41,890.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0729` | 16,080,000.00 USD | 16,080,000.00 USD | 114,120.00 USD | 105,410.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,410,000.00 USD | 7,410,000.00 USD | 123,090.00 USD | 50,400.00 USD | 48,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 7,190,000.00 USD | 7,190,000.00 USD | 44,230.00 USD | 92,640.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0731` | 15,830,000.00 USD | 15,830,000.00 USD | 565,310.00 USD | 49,290.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 7,030,000.00 USD | 7,030,000.00 USD | 153,570.00 USD | 92,040.00 USD | 93,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,690,000.00 USD | 6,690,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0733` | 15,200,000.00 USD | 15,200,000.00 USD | 470,120.00 USD | 0.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 6,490,000.00 USD | 6,490,000.00 USD | 361,270.00 USD | 74,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 6,060,000.00 USD | 6,060,000.00 USD | 141,790.00 USD | 29,700.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0735` | 14,700,000.00 USD | 14,700,000.00 USD | 589,440.00 USD | 93,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 5,880,000.00 USD | 5,880,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,640,000.00 USD | 5,640,000.00 USD | 113,510.00 USD | 70,080.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0737` | 14,020,000.00 USD | 14,020,000.00 USD | 506,070.00 USD | 494,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,400,000.00 USD | 5,400,000.00 USD | 127,100.00 USD | 34,490.00 USD | 39,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,200,000.00 USD | 5,200,000.00 USD | 294,920.00 USD | 87,920.00 USD | 62,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0739` | 13,020,000.00 USD | 13,020,000.00 USD | 265,850.00 USD | 515,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,760,000.00 USD | 4,760,000.00 USD | 77,470.00 USD | 108,230.00 USD | 117,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,450,000.00 USD | 4,450,000.00 USD | 217,950.00 USD | 182,820.00 USD | 102,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0741` | 12,240,000.00 USD | 12,240,000.00 USD | 66,970.00 USD | 294,670.00 USD | 178,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 3,950,000.00 USD | 3,950,000.00 USD | 90,280.00 USD | 288,900.00 USD | 81,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,490,000.00 USD | 3,490,000.00 USD | 236,300.00 USD | 162,360.00 USD | 284,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0743` | 11,700,000.00 USD | 11,700,000.00 USD | 774,380.00 USD | 209,100.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 2,810,000.00 USD | 2,810,000.00 USD | 217,450.00 USD | 93,630.00 USD | 107,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,390,000.00 USD | 2,390,000.00 USD | 87,580.00 USD | 49,100.00 USD | 47,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0745` | 9,600,000.00 USD | 9,600,000.00 USD | 1,360,000.00 USD | 951,300.00 USD | 326,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,200,000.00 USD | 2,200,000.00 USD | 88,460.00 USD | 96,200.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,880,000.00 USD | 1,880,000.00 USD | 625,930.00 USD | 202,480.00 USD | 148,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0747` | 6,960,000.00 USD | 6,960,000.00 USD | 1,410,000.00 USD | 1,830,000.00 USD | 649,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 898,860.00 USD | 898,860.00 USD | 98,680.00 USD | 106,840.00 USD | 198,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 494,490.00 USD | 494,490.00 USD | 122,780.00 USD | 128,240.00 USD | 131,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0749` | 3,070,000.00 USD | 3,070,000.00 USD | 706,340.00 USD | 459,930.00 USD | 875,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 111,950.00 USD | 111,950.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 47,610.00 USD | 47,610.00 USD | 0.00 USD | 12,650.00 USD | 10,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0751` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 30,900.00 USD | 84,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 24,430.00 USD | 24,430.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0753` | 907,280.00 USD | 907,280.00 USD | 751,120.00 USD | 53,860.00 USD | 102,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0755` | 938,670.00 USD | 938,670.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0755` | 1,880,000.00 USD | 1,880,000.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0756` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 144,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0758` | 6,810.00 USD | 6,810.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0759` | 2,130,000.00 USD | 2,130,000.00 USD | 40,360.00 USD | 66,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 7,620.00 USD | 7,620.00 USD | 0.00 USD | 0.00 USD | 807.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 7,760.00 USD | 7,760.00 USD | 0.00 USD | 0.00 USD | 142.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 34,140.00 USD | 34,140.00 USD | 0.00 USD | 24,860.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 66,330.00 USD | 66,330.00 USD | 0.00 USD | 32,030.00 USD | 168.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 408,410.00 USD | 408,410.00 USD | 211,600.00 USD | 31,270.00 USD | 99,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0765` | 3,400,000.00 USD | 3,400,000.00 USD | 772,480.00 USD | 496,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,180,000.00 USD | 1,180,000.00 USD | 352,420.00 USD | 422,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 1,810,000.00 USD | 1,810,000.00 USD | 132,300.00 USD | 330,660.00 USD | 159,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0767` | 4,670,000.00 USD | 4,670,000.00 USD | 1,180,000.00 USD | 90,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,820,000.00 USD | 2,820,000.00 USD | 272,800.00 USD | 109,050.00 USD | 632,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 4,160,000.00 USD | 4,160,000.00 USD | 471,540.00 USD | 515,910.00 USD | 350,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0769` | 5,940,000.00 USD | 5,940,000.00 USD | 760,570.00 USD | 84,300.00 USD | 429,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,370,000.00 USD | 5,370,000.00 USD | 431,600.00 USD | 289,320.00 USD | 486,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 6,520,000.00 USD | 6,520,000.00 USD | 441,280.00 USD | 462,990.00 USD | 250,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0771` | 8,430,000.00 USD | 8,430,000.00 USD | 888,600.00 USD | 798,440.00 USD | 794,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 8,120,000.00 USD | 8,120,000.00 USD | 480,450.00 USD | 348,690.00 USD | 766,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 190,960.00 USD | 355,540.00 USD | 244,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 69,030.00 USD | 347,590.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,310,000.00 USD | 9,310,000.00 USD | 118,800.00 USD | 242,820.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 9,820,000.00 USD | 9,820,000.00 USD | 288,570.00 USD | 164,230.00 USD | 59,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0775` | 10,060,000.00 USD | 10,060,000.00 USD | 779,670.00 USD | 375,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,500,000.00 USD | 10,500,000.00 USD | 284,830.00 USD | 250,900.00 USD | 143,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 11,390,000.00 USD | 11,390,000.00 USD | 401,010.00 USD | 326,260.00 USD | 163,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0777` | 10,620,000.00 USD | 10,620,000.00 USD | 265,980.00 USD | 286,560.00 USD | 693.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 12,230,000.00 USD | 12,230,000.00 USD | 116,640.00 USD | 327,630.00 USD | 400,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 13,000,000.00 USD | 13,000,000.00 USD | 345,840.00 USD | 217,570.00 USD | 206,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0779` | 11,630,000.00 USD | 11,630,000.00 USD | 270,450.00 USD | 301,690.00 USD | 438,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 13,320,000.00 USD | 13,320,000.00 USD | 212,580.00 USD | 60,260.00 USD | 39,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 13,670,000.00 USD | 13,670,000.00 USD | 151,030.00 USD | 182,230.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0781` | 11,960,000.00 USD | 11,960,000.00 USD | 186,410.00 USD | 142,450.00 USD | 4,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 13,940,000.00 USD | 13,940,000.00 USD | 70,430.00 USD | 118,330.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 14,430,000.00 USD | 14,430,000.00 USD | 79,720.00 USD | 213,430.00 USD | 197,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0783` | 12,450,000.00 USD | 12,450,000.00 USD | 15,350.00 USD | 285,880.00 USD | 193,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 15,070,000.00 USD | 15,070,000.00 USD | 436,380.00 USD | 139,260.00 USD | 70,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 15,560,000.00 USD | 15,560,000.00 USD | 226,340.00 USD | 137,970.00 USD | 122,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0785` | 13,070,000.00 USD | 13,070,000.00 USD | 197,420.00 USD | 141,600.00 USD | 278,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 16,430,000.00 USD | 16,430,000.00 USD | 352,080.00 USD | 219,480.00 USD | 296,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 17,670,000.00 USD | 17,670,000.00 USD | 379,110.00 USD | 476,500.00 USD | 382,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0787` | 14,670,000.00 USD | 14,670,000.00 USD | 437,500.00 USD | 346,050.00 USD | 812,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 354.19 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 18,210,000.00 USD | 18,210,000.00 USD | 168,080.00 USD | 256,280.00 USD | 123,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 18,860,000.00 USD | 18,860,000.00 USD | 312,410.00 USD | 231,880.00 USD | 101,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0789` | 15,480,000.00 USD | 15,480,000.00 USD | 301,760.00 USD | 259,180.00 USD | 249,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 19,120,000.00 USD | 19,120,000.00 USD | 153,960.00 USD | 78,340.00 USD | 28,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 19,590,000.00 USD | 19,590,000.00 USD | 205,560.00 USD | 143,060.00 USD | 123,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0791` | 16,040,000.00 USD | 16,040,000.00 USD | 476,430.00 USD | 81,300.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 19,950,000.00 USD | 19,950,000.00 USD | 224,560.00 USD | 57,490.00 USD | 75,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0793` | 5,230.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0793` | 19,960,000.00 USD | 19,960,000.00 USD | 5,950.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0793` | 16,380,000.00 USD | 16,380,000.00 USD | 27,550.00 USD | 61,220.00 USD | 246,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0794` | 3,550.00 USD | 9,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0794` | 20,310,000.00 USD | 20,310,000.00 USD | 158,580.00 USD | 94,790.00 USD | 100,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 104.72 USD | 9,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0795` | 20,550,000.00 USD | 20,550,000.00 USD | 92,560.00 USD | 45,380.00 USD | 101,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0795` | 17,050,000.00 USD | 17,050,000.00 USD | 206,900.00 USD | 0.00 USD | 469,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 855.64 USD | 10,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0796` | 20,770,000.00 USD | 20,770,000.00 USD | 199,280.00 USD | 16,900.00 USD | 2,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 21,070,000.00 USD | 21,070,000.00 USD | 206,810.00 USD | 86,330.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0797` | 18,020,000.00 USD | 18,020,000.00 USD | 640,790.00 USD | 203,560.00 USD | 119,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 21,150,000.00 USD | 21,150,000.00 USD | 58,670.00 USD | 16,860.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 21,410,000.00 USD | 21,410,000.00 USD | 43,250.00 USD | 188,370.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0799` | 18,790,000.00 USD | 18,790,000.00 USD | 561,590.00 USD | 130,870.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 21,560,000.00 USD | 21,560,000.00 USD | 48,550.00 USD | 4,160.00 USD | 97,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 21,590,000.00 USD | 21,590,000.00 USD | 25,740.00 USD | 1,770.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0801` | 18,980,000.00 USD | 18,980,000.00 USD | 85,040.00 USD | 0.00 USD | 104,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 21,610,000.00 USD | 21,610,000.00 USD | 25,490.00 USD | 3,000.00 USD | 122.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 21,720,000.00 USD | 21,720,000.00 USD | 25,660.00 USD | 45,100.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0803` | 19,020,000.00 USD | 19,020,000.00 USD | 42,220.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 21,740,000.00 USD | 21,740,000.00 USD | 13,900.00 USD | 3,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 826.14 USD | 10,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0805` | 21,910,000.00 USD | 21,910,000.00 USD | 89,620.00 USD | 39,290.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0805` | 19,350,000.00 USD | 19,350,000.00 USD | 228,320.00 USD | 43,910.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 22,180,000.00 USD | 22,180,000.00 USD | 28,730.00 USD | 22,650.00 USD | 215,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0806` | 213.40 USD | 11,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0807` | 22,590,000.00 USD | 22,590,000.00 USD | 228,350.00 USD | 153,240.00 USD | 30,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0807` | 20,790,000.00 USD | 20,790,000.00 USD | 217,720.00 USD | 934,840.00 USD | 294,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 23,260,000.00 USD | 23,260,000.00 USD | 150,860.00 USD | 133,620.00 USD | 381,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 23,590,000.00 USD | 23,590,000.00 USD | 109,380.00 USD | 211,270.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0809` | 22,570,000.00 USD | 22,570,000.00 USD | 9,880.00 USD | 1,760,000.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 24,030,000.00 USD | 24,030,000.00 USD | 192,870.00 USD | 115,340.00 USD | 132,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 24,260,000.00 USD | 24,260,000.00 USD | 100,060.00 USD | 118,890.00 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0811` | 23,430,000.00 USD | 23,430,000.00 USD | 131,030.00 USD | 730,620.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 24,500,000.00 USD | 24,500,000.00 USD | 134,440.00 USD | 85,440.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 24,680,000.00 USD | 24,680,000.00 USD | 39,090.00 USD | 24,970.00 USD | 110,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0813` | 24,500,000.00 USD | 24,500,000.00 USD | 517,320.00 USD | 548,390.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 24,970,000.00 USD | 24,970,000.00 USD | 43,650.00 USD | 104,280.00 USD | 143,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 25,090,000.00 USD | 25,090,000.00 USD | 20,890.00 USD | 5,660.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0815` | 26,110,000.00 USD | 26,110,000.00 USD | 671,840.00 USD | 643,990.00 USD | 300,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 25,800,000.00 USD | 25,800,000.00 USD | 323,740.00 USD | 204,920.00 USD | 177,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 26,340,000.00 USD | 26,340,000.00 USD | 280,410.00 USD | 137,200.00 USD | 130,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0817` | 28,680,000.00 USD | 28,680,000.00 USD | 1,200,000.00 USD | 745,850.00 USD | 614,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 27,000,000.00 USD | 27,000,000.00 USD | 234,840.00 USD | 158,110.00 USD | 267,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 11,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 27,600,000.00 USD | 27,600,000.00 USD | 153,870.00 USD | 310,920.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0819` | 30,790,000.00 USD | 30,790,000.00 USD | 672,340.00 USD | 512,490.00 USD | 929,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 28,140,000.00 USD | 28,140,000.00 USD | 44,040.00 USD | 174,350.00 USD | 319,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 28,410,000.00 USD | 28,410,000.00 USD | 145,950.00 USD | 44,820.00 USD | 85,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0821` | 33,150,000.00 USD | 33,150,000.00 USD | 1,210,000.00 USD | 760,670.00 USD | 390,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 28,970,000.00 USD | 28,970,000.00 USD | 249,310.00 USD | 154,040.00 USD | 156,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 29,320,000.00 USD | 29,320,000.00 USD | 267,050.00 USD | 73,580.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0823` | 34,920,000.00 USD | 34,920,000.00 USD | 884,810.00 USD | 520,900.00 USD | 366,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 29,900,000.00 USD | 29,900,000.00 USD | 168,680.00 USD | 216,620.00 USD | 192,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 30,130,000.00 USD | 30,130,000.00 USD | 102,430.00 USD | 109,280.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0825` | 36,500,000.00 USD | 36,500,000.00 USD | 761,460.00 USD | 514,320.00 USD | 307,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0825` | 217.85 USD | 11,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0826` | 30,550,000.00 USD | 30,550,000.00 USD | 131,950.00 USD | 119,210.00 USD | 170,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 30,650,000.00 USD | 30,650,000.00 USD | 13,110.00 USD | 70,370.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0827` | 37,650,000.00 USD | 37,650,000.00 USD | 658,340.00 USD | 220,660.00 USD | 271,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 31,000,000.00 USD | 31,000,000.00 USD | 200,300.00 USD | 78,780.00 USD | 71,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 218.81 USD | 11,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0829` | 31,300,000.00 USD | 31,300,000.00 USD | 198,070.00 USD | 93,430.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0829` | 38,690,000.00 USD | 38,690,000.00 USD | 645,990.00 USD | 177,740.00 USD | 214,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0829` | 219.07 USD | 12,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0830` | 31,440,000.00 USD | 31,440,000.00 USD | 54,060.00 USD | 35,610.00 USD | 42,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 31,520,000.00 USD | 31,520,000.00 USD | 22,160.00 USD | 14,660.00 USD | 45,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0831` | 39,590,000.00 USD | 39,590,000.00 USD | 452,190.00 USD | 160,720.00 USD | 288,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 15,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 31,900,000.00 USD | 31,900,000.00 USD | 182,190.00 USD | 96,860.00 USD | 100,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 32,320,000.00 USD | 32,320,000.00 USD | 123,920.00 USD | 115,930.00 USD | 180,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0833` | 40,810,000.00 USD | 40,810,000.00 USD | 524,880.00 USD | 414,820.00 USD | 276,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 32,700,000.00 USD | 32,700,000.00 USD | 123,760.00 USD | 114,500.00 USD | 143,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 33,060,000.00 USD | 33,060,000.00 USD | 109,250.00 USD | 187,650.00 USD | 64,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0835` | 41,970,000.00 USD | 41,970,000.00 USD | 365,460.00 USD | 261,800.00 USD | 536,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 33,330,000.00 USD | 33,330,000.00 USD | 44,050.00 USD | 72,490.00 USD | 148,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 15,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 33,550,000.00 USD | 33,550,000.00 USD | 130,410.00 USD | 29,090.00 USD | 61,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0837` | 42,770,000.00 USD | 42,770,000.00 USD | 453,970.00 USD | 227,430.00 USD | 115,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 33,820,000.00 USD | 33,820,000.00 USD | 150,900.00 USD | 81,260.00 USD | 42,460.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.0647` | 29,780,000.00 USD | 0.00 USD | 29,780,000.00 USD | 23,160.00 USD | 13,720.00 USD | 0.00 USD |
| `7D` | `0.0649` | 29,740,000.00 USD | 0.00 USD | 29,740,000.00 USD | 21,850.00 USD | 0.00 USD | 15,770.00 USD |
| `7D` | `0.0657` | 29,710,000.00 USD | 0.00 USD | 29,710,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0661` | 29,690,000.00 USD | 0.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD |
| `7D` | `0.0663` | 29,650,000.00 USD | 0.00 USD | 29,650,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `7D` | `0.0665` | 29,640,000.00 USD | 0.00 USD | 29,640,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD |
| `7D` | `0.0669` | 29,460,000.00 USD | 0.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `7D` | `0.0675` | 29,460,000.00 USD | 0.00 USD | 29,460,000.00 USD | 25,430.00 USD | 8,460.00 USD | 19,470.00 USD |
| `1D` | `0.0677` | 17,800,000.00 USD | 0.00 USD | 17,800,000.00 USD | 48,630.00 USD | 94,020.00 USD | 16,690.00 USD |
| `7D` | `0.0677` | 29,410,000.00 USD | 0.00 USD | 29,410,000.00 USD | 10,470.00 USD | 0.00 USD | 475.18 USD |
| `1D` | `0.0678` | 17,640,000.00 USD | 0.00 USD | 17,640,000.00 USD | 29,490.00 USD | 42,100.00 USD | 72,380.00 USD |
| `1D` | `0.0679` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 72,650.00 USD | 41,660.00 USD | 8,010.00 USD |
| `7D` | `0.0679` | 29,390,000.00 USD | 0.00 USD | 29,390,000.00 USD | 6,140.00 USD | 59,770.00 USD | 61,020.00 USD |
| `1D` | `0.0680` | 17,380,000.00 USD | 0.00 USD | 17,380,000.00 USD | 51,160.00 USD | 41,240.00 USD | 41,660.00 USD |
| `1D` | `0.0681` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 36,810.00 USD | 58,950.00 USD | 149,430.00 USD |
| `7D` | `0.0681` | 29,270,000.00 USD | 0.00 USD | 29,270,000.00 USD | 118,640.00 USD | 61,880.00 USD | 164,800.00 USD |
| `1D` | `0.0682` | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 14,920.00 USD | 55,530.00 USD | 26,770.00 USD |
| `1D` | `0.0683` | 16,900,000.00 USD | 0.00 USD | 16,900,000.00 USD | 15,780.00 USD | 32,190.00 USD | 1,160.00 USD |
| `7D` | `0.0683` | 28,920,000.00 USD | 0.00 USD | 28,920,000.00 USD | 0.00 USD | 58,370.00 USD | 66,930.00 USD |
| `1D` | `0.0684` | 16,850,000.00 USD | 0.00 USD | 16,850,000.00 USD | 24,150.00 USD | 24,010.00 USD | 3,840.00 USD |
| `1D` | `0.0685` | 16,800,000.00 USD | 0.00 USD | 16,800,000.00 USD | 58,140.00 USD | 18,250.00 USD | 28,630.00 USD |
| `7D` | `0.0685` | 28,800,000.00 USD | 0.00 USD | 28,800,000.00 USD | 142,840.00 USD | 77,920.00 USD | 25,380.00 USD |
| `1D` | `0.0686` | 16,690,000.00 USD | 0.00 USD | 16,690,000.00 USD | 56,540.00 USD | 16,290.00 USD | 17,200.00 USD |
| `1D` | `0.0687` | 16,600,000.00 USD | 0.00 USD | 16,600,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,070.00 USD |
| `7D` | `0.0687` | 28,550,000.00 USD | 0.00 USD | 28,550,000.00 USD | 101,720.00 USD | 128,090.00 USD | 1,010.00 USD |
| `1D` | `0.0688` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD |
| `1D` | `0.0689` | 16,460,000.00 USD | 0.00 USD | 16,460,000.00 USD | 10,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0689` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 225,480.00 USD | 77,640.00 USD | 61,090.00 USD |
| `1D` | `0.0690` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD |
| `1D` | `0.0691` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 1,460.00 USD | 0.00 USD | 1,510.00 USD |
| `7D` | `0.0691` | 27,960,000.00 USD | 0.00 USD | 27,960,000.00 USD | 162,010.00 USD | 95,020.00 USD | 130,900.00 USD |
| `1D` | `0.0692` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0693` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 18,220.00 USD | 0.00 USD | 670.09 USD |
| `7D` | `0.0693` | 27,570,000.00 USD | 0.00 USD | 27,570,000.00 USD | 207,150.00 USD | 190,180.00 USD | 80,200.00 USD |
| `1D` | `0.0694` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 2,070.00 USD | 0.00 USD | 1,140.00 USD |
| `7D` | `0.0695` | 27,090,000.00 USD | 0.00 USD | 27,090,000.00 USD | 282,470.00 USD | 212,530.00 USD | 212,560.00 USD |
| `1D` | `0.0697` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,690.00 USD |
| `7D` | `0.0697` | 26,380,000.00 USD | 0.00 USD | 26,380,000.00 USD | 142,190.00 USD | 148,620.00 USD | 263,500.00 USD |
| `1D` | `0.0698` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 10,960.00 USD | 10,400.00 USD | 12,610.00 USD |
| `1D` | `0.0699` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 38,680.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `0.0699` | 25,830,000.00 USD | 0.00 USD | 25,830,000.00 USD | 325,570.00 USD | 205,450.00 USD | 138,220.00 USD |
| `1D` | `0.0700` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,060.00 USD |
| `1D` | `0.0701` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 39,680.00 USD | 108,360.00 USD | 37.33 USD |
| `7D` | `0.0701` | 25,160,000.00 USD | 0.00 USD | 25,160,000.00 USD | 283,670.00 USD | 119,790.00 USD | 142,750.00 USD |
| `1D` | `0.0702` | 15,970,000.00 USD | 0.00 USD | 15,970,000.00 USD | 45,890.00 USD | 11,420.00 USD | 122.24 USD |
| `1D` | `0.0703` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 140,500.00 USD | 58,070.00 USD | 4,610.00 USD |
| `7D` | `0.0703` | 24,610,000.00 USD | 0.00 USD | 24,610,000.00 USD | 261,240.00 USD | 120,430.00 USD | 50,710.00 USD |
| `1D` | `0.0704` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 5,220.00 USD | 31,030.00 USD | 20,350.00 USD |
| `1D` | `0.0705` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 41,460.00 USD | 43,660.00 USD | 34,300.00 USD |
| `7D` | `0.0705` | 24,180,000.00 USD | 0.00 USD | 24,180,000.00 USD | 224,080.00 USD | 133,180.00 USD | 178,570.00 USD |
| `1D` | `0.0706` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 22,880.00 USD | 6,490.00 USD | 15,040.00 USD |
| `1D` | `0.0707` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 136,920.00 USD | 57,570.00 USD | 47,400.00 USD |
| `7D` | `0.0707` | 23,650,000.00 USD | 0.00 USD | 23,650,000.00 USD | 171,490.00 USD | 37,160.00 USD | 156,120.00 USD |
| `1D` | `0.0708` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 69,400.00 USD | 55,430.00 USD | 105,460.00 USD |
| `1D` | `0.0709` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 38,730.00 USD | 82,680.00 USD | 149,790.00 USD |
| `7D` | `0.0709` | 23,280,000.00 USD | 0.00 USD | 23,280,000.00 USD | 485,290.00 USD | 159,720.00 USD | 139,080.00 USD |
| `1D` | `0.0710` | 14,740,000.00 USD | 0.00 USD | 14,740,000.00 USD | 117,230.00 USD | 92,490.00 USD | 120,060.00 USD |
| `1D` | `0.0711` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 49,210.00 USD | 26,550.00 USD | 45,450.00 USD |
| `7D` | `0.0711` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 285,730.00 USD | 252,130.00 USD | 91,190.00 USD |
| `1D` | `0.0712` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 165,590.00 USD | 47,430.00 USD | 3,500.00 USD |
| `1D` | `0.0713` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 75,840.00 USD | 89,050.00 USD | 63,100.00 USD |
| `7D` | `0.0713` | 21,870,000.00 USD | 0.00 USD | 21,870,000.00 USD | 379,600.00 USD | 171,480.00 USD | 139,950.00 USD |
| `1D` | `0.0714` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 120,780.00 USD | 49,200.00 USD | 46,290.00 USD |
| `1D` | `0.0715` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 81,850.00 USD | 236,640.00 USD | 43,130.00 USD |
| `7D` | `0.0715` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 211,700.00 USD | 51,460.00 USD | 66,820.00 USD |
| `1D` | `0.0716` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 19,480.00 USD | 49,670.00 USD | 0.00 USD |
| `1D` | `0.0717` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 238,310.00 USD | 96,820.00 USD | 837.78 USD |
| `7D` | `0.0717` | 20,850,000.00 USD | 0.00 USD | 20,850,000.00 USD | 285,100.00 USD | 190,890.00 USD | 48,380.00 USD |
| `1D` | `0.0718` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 64,570.00 USD | 97,660.00 USD | 14,350.00 USD |
| `1D` | `0.0719` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 229,400.00 USD | 78,600.00 USD | 71,880.00 USD |
| `7D` | `0.0719` | 20,320,000.00 USD | 0.00 USD | 20,320,000.00 USD | 233,070.00 USD | 63,390.00 USD | 276,250.00 USD |
| `1D` | `0.0720` | 12,310,000.00 USD | 0.00 USD | 12,310,000.00 USD | 138,650.00 USD | 40,840.00 USD | 72,970.00 USD |
| `1D` | `0.0721` | 12,060,000.00 USD | 0.00 USD | 12,060,000.00 USD | 308,410.00 USD | 260,370.00 USD | 66,820.00 USD |
| `7D` | `0.0721` | 19,750,000.00 USD | 0.00 USD | 19,750,000.00 USD | 422,700.00 USD | 285,460.00 USD | 95,670.00 USD |
| `1D` | `0.0722` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 181,970.00 USD | 130,710.00 USD | 151,320.00 USD |
| `1D` | `0.0723` | 10,960,000.00 USD | 0.00 USD | 10,960,000.00 USD | 116,520.00 USD | 251,210.00 USD | 343,610.00 USD |
| `7D` | `0.0723` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 242,550.00 USD | 148,860.00 USD | 110,740.00 USD |
| `1D` | `0.0724` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 224,260.00 USD | 249,960.00 USD | 401,900.00 USD |
| `1D` | `0.0725` | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 263,550.00 USD | 255,920.00 USD | 311,620.00 USD |
| `7D` | `0.0725` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 1,070,000.00 USD | 365,360.00 USD | 152,800.00 USD |
| `1D` | `0.0726` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 153,630.00 USD | 149,300.00 USD | 59,610.00 USD |
| `1D` | `0.0727` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 190,550.00 USD | 160,860.00 USD | 40,450.00 USD |
| `7D` | `0.0727` | 16,860,000.00 USD | 0.00 USD | 16,860,000.00 USD | 249,200.00 USD | 432,030.00 USD | 92,170.00 USD |
| `1D` | `0.0728` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 60,510.00 USD | 154,910.00 USD | 47,440.00 USD |
| `1D` | `0.0729` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 58,550.00 USD | 41,890.00 USD | 8,540.00 USD |
| `7D` | `0.0729` | 16,080,000.00 USD | 0.00 USD | 16,080,000.00 USD | 114,120.00 USD | 105,410.00 USD | 37,020.00 USD |
| `1D` | `0.0730` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 123,090.00 USD | 50,400.00 USD | 48,680.00 USD |
| `1D` | `0.0731` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 44,230.00 USD | 92,640.00 USD | 28,420.00 USD |
| `7D` | `0.0731` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 565,310.00 USD | 49,290.00 USD | 12,800.00 USD |
| `1D` | `0.0732` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 153,570.00 USD | 92,040.00 USD | 93,520.00 USD |
| `1D` | `0.0733` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD |
| `7D` | `0.0733` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 470,120.00 USD | 0.00 USD | 29,970.00 USD |
| `1D` | `0.0734` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 361,270.00 USD | 74,580.00 USD | 0.00 USD |
| `1D` | `0.0735` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 141,790.00 USD | 29,700.00 USD | 5,270.00 USD |
| `7D` | `0.0735` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 589,440.00 USD | 93,670.00 USD | 0.00 USD |
| `1D` | `0.0736` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `1D` | `0.0737` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 113,510.00 USD | 70,080.00 USD | 49,860.00 USD |
| `7D` | `0.0737` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 506,070.00 USD | 494,020.00 USD | 0.00 USD |
| `1D` | `0.0738` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 127,100.00 USD | 34,490.00 USD | 39,960.00 USD |
| `1D` | `0.0739` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 294,920.00 USD | 87,920.00 USD | 62,550.00 USD |
| `7D` | `0.0739` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 265,850.00 USD | 515,020.00 USD | 0.00 USD |
| `1D` | `0.0740` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 77,470.00 USD | 108,230.00 USD | 117,530.00 USD |
| `1D` | `0.0741` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 217,950.00 USD | 182,820.00 USD | 102,910.00 USD |
| `7D` | `0.0741` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 66,970.00 USD | 294,670.00 USD | 178,730.00 USD |
| `1D` | `0.0742` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 90,280.00 USD | 288,900.00 USD | 81,010.00 USD |
| `1D` | `0.0743` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 236,300.00 USD | 162,360.00 USD | 284,730.00 USD |
| `7D` | `0.0743` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 774,380.00 USD | 209,100.00 USD | 1,120,000.00 USD |
| `1D` | `0.0744` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 217,450.00 USD | 93,630.00 USD | 107,380.00 USD |
| `1D` | `0.0745` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 87,580.00 USD | 49,100.00 USD | 47,320.00 USD |
| `7D` | `0.0745` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 1,360,000.00 USD | 951,300.00 USD | 326,000.00 USD |
| `1D` | `0.0746` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 88,460.00 USD | 96,200.00 USD | 143,040.00 USD |
| `1D` | `0.0747` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 625,930.00 USD | 202,480.00 USD | 148,720.00 USD |
| `7D` | `0.0747` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 1,410,000.00 USD | 1,830,000.00 USD | 649,410.00 USD |
| `1D` | `0.0748` | 898,860.00 USD | 0.00 USD | 898,860.00 USD | 98,680.00 USD | 106,840.00 USD | 198,860.00 USD |
| `1D` | `0.0749` | 494,490.00 USD | 0.00 USD | 494,490.00 USD | 122,780.00 USD | 128,240.00 USD | 131,510.00 USD |
| `7D` | `0.0749` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 706,340.00 USD | 459,930.00 USD | 875,850.00 USD |
| `1D` | `0.0750` | 111,950.00 USD | 0.00 USD | 111,950.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD |
| `1D` | `0.0751` | 47,610.00 USD | 0.00 USD | 47,610.00 USD | 0.00 USD | 12,650.00 USD | 10,540.00 USD |
| `7D` | `0.0751` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 30,900.00 USD | 84,880.00 USD |
| `1D` | `0.0752` | 24,430.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `1D` | `0.0753` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0753` | 907,280.00 USD | 0.00 USD | 907,280.00 USD | 751,120.00 USD | 53,860.00 USD | 102,300.00 USD |
| `7D` | `0.0755` | 938,670.00 USD | 938,670.00 USD | 0.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD |
| `7D` | `0.0755` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD |
| `1D` | `0.0756` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD |
| `7D` | `0.0757` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 144,530.00 USD | 0.00 USD |
| `1D` | `0.0758` | 6,810.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD |
| `7D` | `0.0759` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 40,360.00 USD | 66,300.00 USD | 0.00 USD |
| `1D` | `0.0761` | 7,620.00 USD | 7,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 807.36 USD |
| `1D` | `0.0762` | 7,760.00 USD | 7,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 142.20 USD |
| `1D` | `0.0763` | 34,140.00 USD | 34,140.00 USD | 0.00 USD | 0.00 USD | 24,860.00 USD | 1,510.00 USD |
| `1D` | `0.0764` | 66,330.00 USD | 66,330.00 USD | 0.00 USD | 0.00 USD | 32,030.00 USD | 168.86 USD |
| `1D` | `0.0765` | 408,410.00 USD | 408,410.00 USD | 0.00 USD | 211,600.00 USD | 31,270.00 USD | 99,200.00 USD |
| `7D` | `0.0765` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 772,480.00 USD | 496,590.00 USD | 0.00 USD |
| `1D` | `0.0766` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 352,420.00 USD | 422,220.00 USD | 0.00 USD |
| `1D` | `0.0767` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 132,300.00 USD | 330,660.00 USD | 159,680.00 USD |
| `7D` | `0.0767` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 1,180,000.00 USD | 90,730.00 USD | 0.00 USD |
| `1D` | `0.0768` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 272,800.00 USD | 109,050.00 USD | 632,840.00 USD |
| `1D` | `0.0769` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 471,540.00 USD | 515,910.00 USD | 350,860.00 USD |
| `7D` | `0.0769` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 760,570.00 USD | 84,300.00 USD | 429,490.00 USD |
| `1D` | `0.0770` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 431,600.00 USD | 289,320.00 USD | 486,560.00 USD |
| `1D` | `0.0771` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 441,280.00 USD | 462,990.00 USD | 250,860.00 USD |
| `7D` | `0.0771` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 888,600.00 USD | 798,440.00 USD | 794,320.00 USD |
| `1D` | `0.0772` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 480,450.00 USD | 348,690.00 USD | 766,220.00 USD |
| `1D` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 190,960.00 USD | 355,540.00 USD | 244,690.00 USD |
| `7D` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 69,030.00 USD | 347,590.00 USD | 64,060.00 USD |
| `1D` | `0.0774` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 118,800.00 USD | 242,820.00 USD | 36,420.00 USD |
| `1D` | `0.0775` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 288,570.00 USD | 164,230.00 USD | 59,290.00 USD |
| `7D` | `0.0775` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 779,670.00 USD | 375,100.00 USD | 0.00 USD |
| `1D` | `0.0776` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 284,830.00 USD | 250,900.00 USD | 143,730.00 USD |
| `1D` | `0.0777` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 401,010.00 USD | 326,260.00 USD | 163,360.00 USD |
| `7D` | `0.0777` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 265,980.00 USD | 286,560.00 USD | 693.20 USD |
| `1D` | `0.0778` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 116,640.00 USD | 327,630.00 USD | 400,990.00 USD |
| `1D` | `0.0779` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 345,840.00 USD | 217,570.00 USD | 206,730.00 USD |
| `7D` | `0.0779` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 270,450.00 USD | 301,690.00 USD | 438,670.00 USD |
| `1D` | `0.0780` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 212,580.00 USD | 60,260.00 USD | 39,430.00 USD |
| `1D` | `0.0781` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 151,030.00 USD | 182,230.00 USD | 19,720.00 USD |
| `7D` | `0.0781` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 186,410.00 USD | 142,450.00 USD | 4,370.00 USD |
| `1D` | `0.0782` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 70,430.00 USD | 118,330.00 USD | 79,530.00 USD |
| `1D` | `0.0783` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 79,720.00 USD | 213,430.00 USD | 197,170.00 USD |
| `7D` | `0.0783` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 15,350.00 USD | 285,880.00 USD | 193,490.00 USD |
| `1D` | `0.0784` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 436,380.00 USD | 139,260.00 USD | 70,840.00 USD |
| `1D` | `0.0785` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 226,340.00 USD | 137,970.00 USD | 122,200.00 USD |
| `7D` | `0.0785` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 197,420.00 USD | 141,600.00 USD | 278,250.00 USD |
| `1D` | `0.0786` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 352,080.00 USD | 219,480.00 USD | 296,100.00 USD |
| `1D` | `0.0787` | 17,670,000.00 USD | 17,670,000.00 USD | 0.00 USD | 379,110.00 USD | 476,500.00 USD | 382,860.00 USD |
| `7D` | `0.0787` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 437,500.00 USD | 346,050.00 USD | 812,710.00 USD |
| `1D` | `0.0788` | 18,210,000.00 USD | 18,210,000.00 USD | 0.00 USD | 168,080.00 USD | 256,280.00 USD | 123,220.00 USD |
| `1D` | `0.0789` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 312,410.00 USD | 231,880.00 USD | 101,180.00 USD |
| `7D` | `0.0789` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 301,760.00 USD | 259,180.00 USD | 249,350.00 USD |
| `1D` | `0.0790` | 19,120,000.00 USD | 19,120,000.00 USD | 0.00 USD | 153,960.00 USD | 78,340.00 USD | 28,850.00 USD |
| `1D` | `0.0791` | 19,590,000.00 USD | 19,590,000.00 USD | 0.00 USD | 205,560.00 USD | 143,060.00 USD | 123,610.00 USD |
| `7D` | `0.0791` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 476,430.00 USD | 81,300.00 USD | 5,350.00 USD |
| `1D` | `0.0792` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 224,560.00 USD | 57,490.00 USD | 75,650.00 USD |
| `1D` | `0.0793` | 19,960,000.00 USD | 19,960,000.00 USD | 0.00 USD | 5,950.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `0.0793` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 27,550.00 USD | 61,220.00 USD | 246,330.00 USD |
| `1D` | `0.0794` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 158,580.00 USD | 94,790.00 USD | 100,960.00 USD |
| `1D` | `0.0795` | 20,550,000.00 USD | 20,550,000.00 USD | 0.00 USD | 92,560.00 USD | 45,380.00 USD | 101,740.00 USD |
| `7D` | `0.0795` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 469,960.00 USD |
| `1D` | `0.0796` | 20,770,000.00 USD | 20,770,000.00 USD | 0.00 USD | 199,280.00 USD | 16,900.00 USD | 2,820.00 USD |
| `1D` | `0.0797` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 206,810.00 USD | 86,330.00 USD | 6,400.00 USD |
| `7D` | `0.0797` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 640,790.00 USD | 203,560.00 USD | 119,170.00 USD |
| `1D` | `0.0798` | 21,150,000.00 USD | 21,150,000.00 USD | 0.00 USD | 58,670.00 USD | 16,860.00 USD | 4,330.00 USD |
| `1D` | `0.0799` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 43,250.00 USD | 188,370.00 USD | 25,050.00 USD |
| `7D` | `0.0799` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 561,590.00 USD | 130,870.00 USD | 78,050.00 USD |
| `1D` | `0.0800` | 21,560,000.00 USD | 21,560,000.00 USD | 0.00 USD | 48,550.00 USD | 4,160.00 USD | 97,460.00 USD |
| `1D` | `0.0801` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 25,740.00 USD | 1,770.00 USD | 1,210.00 USD |
| `7D` | `0.0801` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 85,040.00 USD | 0.00 USD | 104,840.00 USD |
| `1D` | `0.0802` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 25,490.00 USD | 3,000.00 USD | 122.24 USD |
| `1D` | `0.0803` | 21,720,000.00 USD | 21,720,000.00 USD | 0.00 USD | 25,660.00 USD | 45,100.00 USD | 38,590.00 USD |
| `7D` | `0.0803` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 1,480.00 USD |
| `1D` | `0.0804` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 13,900.00 USD | 3,310.00 USD | 0.00 USD |
| `1D` | `0.0805` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 89,620.00 USD | 39,290.00 USD | 41,110.00 USD |
| `7D` | `0.0805` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 228,320.00 USD | 43,910.00 USD | 53,390.00 USD |
| `1D` | `0.0806` | 22,180,000.00 USD | 22,180,000.00 USD | 0.00 USD | 28,730.00 USD | 22,650.00 USD | 215,620.00 USD |
| `1D` | `0.0807` | 22,590,000.00 USD | 22,590,000.00 USD | 0.00 USD | 228,350.00 USD | 153,240.00 USD | 30,510.00 USD |
| `7D` | `0.0807` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 217,720.00 USD | 934,840.00 USD | 294,860.00 USD |
| `1D` | `0.0808` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 150,860.00 USD | 133,620.00 USD | 381,410.00 USD |
| `1D` | `0.0809` | 23,590,000.00 USD | 23,590,000.00 USD | 0.00 USD | 109,380.00 USD | 211,270.00 USD | 14,460.00 USD |
| `7D` | `0.0809` | 22,570,000.00 USD | 22,570,000.00 USD | 0.00 USD | 9,880.00 USD | 1,760,000.00 USD | 1,700.00 USD |
| `1D` | `0.0810` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 192,870.00 USD | 115,340.00 USD | 132,690.00 USD |
| `1D` | `0.0811` | 24,260,000.00 USD | 24,260,000.00 USD | 0.00 USD | 100,060.00 USD | 118,890.00 USD | 11,990.00 USD |
| `7D` | `0.0811` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 131,030.00 USD | 730,620.00 USD | 1,610.00 USD |
| `1D` | `0.0812` | 24,500,000.00 USD | 24,500,000.00 USD | 0.00 USD | 134,440.00 USD | 85,440.00 USD | 19,390.00 USD |
| `1D` | `0.0813` | 24,680,000.00 USD | 24,680,000.00 USD | 0.00 USD | 39,090.00 USD | 24,970.00 USD | 110,950.00 USD |
| `7D` | `0.0813` | 24,500,000.00 USD | 24,500,000.00 USD | 0.00 USD | 517,320.00 USD | 548,390.00 USD | 2,470.00 USD |
| `1D` | `0.0814` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 43,650.00 USD | 104,280.00 USD | 143,160.00 USD |
| `1D` | `0.0815` | 25,090,000.00 USD | 25,090,000.00 USD | 0.00 USD | 20,890.00 USD | 5,660.00 USD | 94,490.00 USD |
| `7D` | `0.0815` | 26,110,000.00 USD | 26,110,000.00 USD | 0.00 USD | 671,840.00 USD | 643,990.00 USD | 300,370.00 USD |
| `1D` | `0.0816` | 25,800,000.00 USD | 25,800,000.00 USD | 0.00 USD | 323,740.00 USD | 204,920.00 USD | 177,540.00 USD |
| `1D` | `0.0817` | 26,340,000.00 USD | 26,340,000.00 USD | 0.00 USD | 280,410.00 USD | 137,200.00 USD | 130,480.00 USD |
| `7D` | `0.0817` | 28,680,000.00 USD | 28,680,000.00 USD | 0.00 USD | 1,200,000.00 USD | 745,850.00 USD | 614,910.00 USD |
| `1D` | `0.0818` | 27,000,000.00 USD | 27,000,000.00 USD | 0.00 USD | 234,840.00 USD | 158,110.00 USD | 267,850.00 USD |
| `1D` | `0.0819` | 27,600,000.00 USD | 27,600,000.00 USD | 0.00 USD | 153,870.00 USD | 310,920.00 USD | 128,220.00 USD |
| `7D` | `0.0819` | 30,790,000.00 USD | 30,790,000.00 USD | 0.00 USD | 672,340.00 USD | 512,490.00 USD | 929,000.00 USD |
| `1D` | `0.0820` | 28,140,000.00 USD | 28,140,000.00 USD | 0.00 USD | 44,040.00 USD | 174,350.00 USD | 319,850.00 USD |
| `1D` | `0.0821` | 28,410,000.00 USD | 28,410,000.00 USD | 0.00 USD | 145,950.00 USD | 44,820.00 USD | 85,150.00 USD |
| `7D` | `0.0821` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 1,210,000.00 USD | 760,670.00 USD | 390,320.00 USD |
| `1D` | `0.0822` | 28,970,000.00 USD | 28,970,000.00 USD | 0.00 USD | 249,310.00 USD | 154,040.00 USD | 156,660.00 USD |
| `1D` | `0.0823` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 267,050.00 USD | 73,580.00 USD | 9,070.00 USD |
| `7D` | `0.0823` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 884,810.00 USD | 520,900.00 USD | 366,690.00 USD |
| `1D` | `0.0824` | 29,900,000.00 USD | 29,900,000.00 USD | 0.00 USD | 168,680.00 USD | 216,620.00 USD | 192,020.00 USD |
| `1D` | `0.0825` | 30,130,000.00 USD | 30,130,000.00 USD | 0.00 USD | 102,430.00 USD | 109,280.00 USD | 21,450.00 USD |
| `7D` | `0.0825` | 36,500,000.00 USD | 36,500,000.00 USD | 0.00 USD | 761,460.00 USD | 514,320.00 USD | 307,380.00 USD |
| `1D` | `0.0826` | 30,550,000.00 USD | 30,550,000.00 USD | 0.00 USD | 131,950.00 USD | 119,210.00 USD | 170,120.00 USD |
| `1D` | `0.0827` | 30,650,000.00 USD | 30,650,000.00 USD | 0.00 USD | 13,110.00 USD | 70,370.00 USD | 16,750.00 USD |
| `7D` | `0.0827` | 37,650,000.00 USD | 37,650,000.00 USD | 0.00 USD | 658,340.00 USD | 220,660.00 USD | 271,680.00 USD |
| `1D` | `0.0828` | 31,000,000.00 USD | 31,000,000.00 USD | 0.00 USD | 200,300.00 USD | 78,780.00 USD | 71,600.00 USD |
| `1D` | `0.0829` | 31,300,000.00 USD | 31,300,000.00 USD | 0.00 USD | 198,070.00 USD | 93,430.00 USD | 8,010.00 USD |
| `7D` | `0.0829` | 38,690,000.00 USD | 38,690,000.00 USD | 0.00 USD | 645,990.00 USD | 177,740.00 USD | 214,060.00 USD |
| `1D` | `0.0830` | 31,440,000.00 USD | 31,440,000.00 USD | 0.00 USD | 54,060.00 USD | 35,610.00 USD | 42,990.00 USD |
| `1D` | `0.0831` | 31,520,000.00 USD | 31,520,000.00 USD | 0.00 USD | 22,160.00 USD | 14,660.00 USD | 45,480.00 USD |
| `7D` | `0.0831` | 39,590,000.00 USD | 39,590,000.00 USD | 0.00 USD | 452,190.00 USD | 160,720.00 USD | 288,260.00 USD |
| `1D` | `0.0832` | 31,900,000.00 USD | 31,900,000.00 USD | 0.00 USD | 182,190.00 USD | 96,860.00 USD | 100,540.00 USD |
| `1D` | `0.0833` | 32,320,000.00 USD | 32,320,000.00 USD | 0.00 USD | 123,920.00 USD | 115,930.00 USD | 180,630.00 USD |
| `7D` | `0.0833` | 40,810,000.00 USD | 40,810,000.00 USD | 0.00 USD | 524,880.00 USD | 414,820.00 USD | 276,510.00 USD |
| `1D` | `0.0834` | 32,700,000.00 USD | 32,700,000.00 USD | 0.00 USD | 123,760.00 USD | 114,500.00 USD | 143,830.00 USD |
| `1D` | `0.0835` | 33,060,000.00 USD | 33,060,000.00 USD | 0.00 USD | 109,250.00 USD | 187,650.00 USD | 64,500.00 USD |
| `7D` | `0.0835` | 41,970,000.00 USD | 41,970,000.00 USD | 0.00 USD | 365,460.00 USD | 261,800.00 USD | 536,330.00 USD |
| `1D` | `0.0836` | 33,330,000.00 USD | 33,330,000.00 USD | 0.00 USD | 44,050.00 USD | 72,490.00 USD | 148,140.00 USD |
| `1D` | `0.0837` | 33,550,000.00 USD | 33,550,000.00 USD | 0.00 USD | 130,410.00 USD | 29,090.00 USD | 61,860.00 USD |
| `7D` | `0.0837` | 42,770,000.00 USD | 42,770,000.00 USD | 0.00 USD | 453,970.00 USD | 227,430.00 USD | 115,210.00 USD |
| `1D` | `0.0838` | 33,820,000.00 USD | 33,820,000.00 USD | 0.00 USD | 150,900.00 USD | 81,260.00 USD | 42,460.00 USD |
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
  * Total Open Interest: `1.06B` | Total OI Tokens: `14,054,981,883.7 DOGE`
  * 1h OI Change: `+0.02%` | 4h OI Change: `-0.30%` | 24h OI Change: `-5.45%`
  * Exchange Breakdown: Binance=`239.78M` | Bybit=`106.40M` | OKX=`110.30M` | Hyperliquid=`75.61M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `24.38K` | Last 24h: `49.48K` | Last 3d: `238.63K` | Last 7d: `304.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0023%` |
| **USDT Bybit** | `0.0017%` | **USDT KuCoin** | `0.0078%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0021%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `46.50%` | `53.50%` | `0.87` | 12,760,000.00 USD |
| `15M` | `Binance` | `51.67%` | `48.33%` | `1.07` | 7,020,000.00 USD |
| `15M` | `OKX` | `49.87%` | `50.13%` | `0.99` | 736,830.00 USD |
| `15M` | `Bybit` | `47.27%` | `52.73%` | `0.90` | 1,120,000.00 USD |
| `15M` | `KuCoin` | `60.94%` | `39.06%` | `1.56` | 175,110.00 USD |
| `15M` | `Gate` | `43.85%` | `56.15%` | `0.78` | 643,700.00 USD |
| `15M` | `Bitget` | `33.01%` | `66.99%` | `0.49` | 184,340.00 USD |
| `15M` | `BingX` | `15.99%` | `84.01%` | `0.19` | 280,550.00 USD |
| `15M` | `MEXC` | `69.88%` | `30.12%` | `2.32` | 178,880.00 USD |
| `15M` | `Bitunix` | `34.19%` | `65.81%` | `0.52` | 826,110.00 USD |
| `15M` | `Hyperliquid` | `86.24%` | `13.76%` | `6.27` | 888,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.42%` | `56.58%` | `0.77` | 47,680.00 USD |
| `15M` | `Crypto.com` | `55.95%` | `44.05%` | `1.27` | 0.00 USD |
| `15M` | `WhiteBIT` | `8.6%` | `91.4%` | `0.09` | 242,190.00 USD |
| `15M` | `HTX` | `23.96%` | `76.04%` | `0.32` | 72,430.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `65.52%` | `34.48%` | `1.90` | 69,320.00 USD |
| `15M` | `Aster` | `30.59%` | `69.41%` | `0.44` | 216,660.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `79.79%` | `20.21%` | `3.95` | 48,590.00 USD |
| `15M` | `Whale Positions` | `51.67%` | `48.33%` | `1.07` | 7,020,000.00 USD |
| `15M` | `Global Accounts` | `46.50%` | `53.50%` | `0.87` | 12,760,000.00 USD |
| `1H` | `DOGE` | `46.36%` | `53.64%` | `0.86` | 219,470,000.00 USD |
| `1H` | `Binance` | `48.53%` | `51.47%` | `0.94` | 64,530,000.00 USD |
| `1H` | `OKX` | `40.51%` | `59.49%` | `0.68` | 51,170,000.00 USD |
| `1H` | `Bybit` | `38.75%` | `61.25%` | `0.63` | 17,510,000.00 USD |
| `1H` | `KuCoin` | `51.28%` | `48.72%` | `1.05` | 981,330.00 USD |
| `1H` | `Gate` | `48.91%` | `51.09%` | `0.96` | 20,870,000.00 USD |
| `1H` | `Bitget` | `43.26%` | `56.74%` | `0.76` | 9,290,000.00 USD |
| `1H` | `BingX` | `43.43%` | `56.57%` | `0.77` | 13,170,000.00 USD |
| `1H` | `MEXC` | `53.14%` | `46.86%` | `1.13` | 12,080,000.00 USD |
| `1H` | `Bitunix` | `50.83%` | `49.17%` | `1.03` | 8,440,000.00 USD |
| `1H` | `Hyperliquid` | `52.81%` | `47.19%` | `1.12` | 7,360,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.63%` | `48.37%` | `1.07` | 4,420,000.00 USD |
| `1H` | `Crypto.com` | `39.15%` | `60.85%` | `0.64` | 1,020,000.00 USD |
| `1H` | `WhiteBIT` | `93.99%` | `6.01%` | `15.64` | 3,280,000.00 USD |
| `1H` | `HTX` | `58.91%` | `41.09%` | `1.43` | 273,810.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `29.25%` | `70.75%` | `0.41` | 1,980,000.00 USD |
| `1H` | `Aster` | `26.85%` | `73.15%` | `0.37` | 1,380,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `57.36%` | `42.64%` | `1.35` | 1,710,000.00 USD |
| `1H` | `Whale Positions` | `48.53%` | `51.47%` | `0.94` | 64,530,000.00 USD |
| `1H` | `Global Accounts` | `46.36%` | `53.64%` | `0.86` | 219,470,000.00 USD |
| `4H` | `DOGE` | `47.82%` | `52.18%` | `0.92` | 966,510,000.00 USD |
| `4H` | `Binance` | `47.15%` | `52.85%` | `0.89` | 293,710,000.00 USD |
| `4H` | `OKX` | `45.72%` | `54.28%` | `0.84` | 196,900,000.00 USD |
| `4H` | `Bybit` | `51.52%` | `48.48%` | `1.06` | 90,560,000.00 USD |
| `4H` | `KuCoin` | `49.96%` | `50.04%` | `1.00` | 4,280,000.00 USD |
| `4H` | `Gate` | `51.18%` | `48.82%` | `1.05` | 76,140,000.00 USD |
| `4H` | `Bitget` | `43.34%` | `56.66%` | `0.76` | 44,370,000.00 USD |
| `4H` | `BingX` | `44.14%` | `55.86%` | `0.79` | 44,610,000.00 USD |
| `4H` | `MEXC` | `47.44%` | `52.56%` | `0.90` | 82,400,000.00 USD |
| `4H` | `Bitunix` | `47.99%` | `52.01%` | `0.92` | 44,050,000.00 USD |
| `4H` | `Hyperliquid` | `48.76%` | `51.24%` | `0.95` | 34,900,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.51%` | `48.49%` | `1.06` | 16,330,000.00 USD |
| `4H` | `Crypto.com` | `45.55%` | `54.45%` | `0.84` | 2,860,000.00 USD |
| `4H` | `WhiteBIT` | `85.63%` | `14.37%` | `5.96` | 13,360,000.00 USD |
| `4H` | `HTX` | `48.18%` | `51.82%` | `0.93` | 1,120,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.08%` | `70.92%` | `0.41` | 3,230,000.00 USD |
| `4H` | `Aster` | `41.47%` | `58.53%` | `0.71` | 6,250,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.29%` | `60.71%` | `0.65` | 11,450,000.00 USD |
| `4H` | `Whale Positions` | `47.15%` | `52.85%` | `0.89` | 293,710,000.00 USD |
| `4H` | `Global Accounts` | `47.82%` | `52.18%` | `0.92` | 966,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0755` | 3,504,858.24 USD | 1,671,375.40 USD | 1,833,482.84 USD | -162,107.45 USD | `-4.63%` | `6B / 5S` |
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0759` | `0.0755` | 6,252,708.50 USD | 2,400,535.02 USD | 3,852,173.48 USD | -1,451,638.46 USD | `-23.22%` | `9B / 7S` |
| `5:00 UTC` | `0.0758` | `0.0759` | `0.0758` | `0.0761` | `0.0758` | 3,515,276.40 USD | 1,545,960.58 USD | 1,969,315.82 USD | -423,355.24 USD | `-12.04%` | `4B / 6S` |
| `0:00 UTC` | `0.0757` | `0.0757` | `0.0757` | `0.0759` | `0.0755` | 2,056,025.64 USD | 709,276.38 USD | 1,346,749.25 USD | -637,472.87 USD | `-31.01%` | `2B / 13S` |
| `5:00 UTC` | `0.0754` | `0.0755` | `0.0754` | `0.0757` | `0.0753` | 2,905,242.56 USD | 1,422,846.87 USD | 1,482,395.68 USD | -59,548.81 USD | `-2.05%` | `8B / 3S` |
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0754` | 2,313,298.65 USD | 1,197,641.49 USD | 1,115,657.16 USD | 81,984.32 USD | `+3.54%` | `3B / 4S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0756` | `0.0753` | 2,260,519.88 USD | 1,007,921.72 USD | 1,252,598.16 USD | -244,676.43 USD | `-10.82%` | `2B / 8S` |
| `0:00 UTC` | `0.0755` | `0.0754` | `0.0755` | `0.0756` | `0.0752` | 2,922,007.92 USD | 1,333,625.48 USD | 1,588,382.44 USD | -254,756.96 USD | `-8.72%` | `6B / 8S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0755` | `0.0753` | 1,576,593.18 USD | 686,951.41 USD | 889,641.77 USD | -202,690.36 USD | `-12.86%` | `0B / 6S` |
| `0:00 UTC` | `0.0753` | `0.0753` | `0.0753` | `0.0755` | `0.0752` | 1,653,383.51 USD | 651,969.27 USD | 1,001,414.24 USD | -349,444.97 USD | `-21.14%` | `2B / 8S` |

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
| `5m` | 163,170.00 USD | -560,320.00 USD | **`DISTRIBUTION`** |
| `15m` | 74,720.00 USD | -465,870.00 USD | **`DISTRIBUTION`** |
| `30m` | 18,040.00 USD | -369,510.00 USD | **`DISTRIBUTION`** |
| `1h` | -734,150.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -537,220.00 USD | -3,660,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,370,000.00 USD | -9,980,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 326,590.00 USD | -9,800,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 2,520,000.00 USD | -7,610,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,970,000.00 USD | -28,590,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,050,000.00 USD | -65,360,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -61,000,000.00 USD | -194,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -284,980,000.00 USD | -823,760,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+163.17K` | 15m=`+74.72K` | 1h=`-734.15K` | 24h=`-18.05M`
* Futures Capital Netflows: 5m=`-560.32K` | 15m=`-465.87K` | 1h=`-1.43M` | 24h=`-65.36M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0755` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0791` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0650`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0759`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
